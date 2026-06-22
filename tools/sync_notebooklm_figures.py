#!/usr/bin/env python3
"""Convert chapter SVG figures to PNG and add them to NotebookLM notebooks."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKLM = Path("/Users/dmitry/.local/bin/notebooklm")
DEFAULT_PROFILES = ("default", "feynman2", "feynman3", "feynman4")


@dataclass(frozen=True)
class NotebookRef:
    chapter: int
    profile: str
    notebook_id: str
    title: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", default="en")
    parser.add_argument("--volume-code", required=True)
    parser.add_argument("--chapters", help="Comma-separated chapters; default: all discovered")
    parser.add_argument("--profiles", default=",".join(DEFAULT_PROFILES))
    parser.add_argument("--density", type=int, default=220)
    parser.add_argument("--request-timeout", type=float, default=60)
    return parser.parse_args()


def parse_csv_numbers(raw: str | None) -> set[int] | None:
    if not raw:
        return None
    return {int(item.strip()) for item in raw.split(",") if item.strip()}


def parse_csv_strings(raw: str) -> list[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def run_json(command: list[str], *, timeout: int | None = None) -> dict:
    result = subprocess.run(command, check=True, capture_output=True, text=True, timeout=timeout)
    return json.loads(result.stdout)


def notebook_pattern(language: str, volume_code: str) -> re.Pattern[str]:
    suffix = "" if language == "ru" else rf" {re.escape(language.upper())}"
    return re.compile(rf"^Feynman Lectures {re.escape(volume_code)}-(\d\d) NotebookLM{suffix}(?:\b|$)")


def discover_notebooks(profiles: list[str], language: str, volume_code: str, chapters: set[int] | None) -> list[NotebookRef]:
    pattern = notebook_pattern(language, volume_code)
    refs: dict[int, NotebookRef] = {}
    for profile in profiles:
        payload = run_json([str(NOTEBOOKLM), "-p", profile, "list", "--json"])
        for item in payload.get("notebooks", []):
            title = str(item.get("title") or "")
            match = pattern.match(title)
            if not match:
                continue
            chapter = int(match.group(1))
            if chapters is not None and chapter not in chapters:
                continue
            refs.setdefault(chapter, NotebookRef(chapter, profile, str(item["id"]), title))
    return sorted(refs.values(), key=lambda item: item.chapter)


def chapter_root(language: str, volume_code: str, chapter: int) -> Path:
    return ROOT / "feynman-notebooklm" / language / f"volume-{volume_code}" / f"ch{chapter:02d}"


def existing_source_titles(notebook: NotebookRef) -> set[str]:
    payload = run_json([str(NOTEBOOKLM), "-p", notebook.profile, "source", "list", "-n", notebook.notebook_id, "--json"])
    return {str(item.get("title") or "") for item in payload.get("sources", [])}


def run_magick(svg: Path, png: Path, density: int) -> None:
    subprocess.run(
        [
            "magick",
            "-density",
            str(density),
            str(svg),
            "-background",
            "white",
            "-alpha",
            "remove",
            "-alpha",
            "off",
            str(png),
        ],
        check=True,
    )


def remove_dasharray(svg: Path, tmp_dir: Path) -> Path:
    text = svg.read_text(encoding="utf-8")
    normalized = re.sub(r'\s+stroke-dasharray="[^"]+"', "", text)
    tmp_svg = tmp_dir / svg.name
    tmp_svg.write_text(normalized, encoding="utf-8")
    return tmp_svg


def quicklook_png(svg: Path, png: Path) -> None:
    with tempfile.TemporaryDirectory(prefix="feynman-ql-") as tmp:
        tmp_dir = Path(tmp)
        subprocess.run(["qlmanage", "-t", "-s", "1400", "-o", str(tmp_dir), str(svg)], check=True, stdout=subprocess.DEVNULL)
        rendered = tmp_dir / f"{svg.name}.png"
        if not rendered.exists():
            raise FileNotFoundError(rendered)
        shutil.copyfile(rendered, png)


def convert_svg(svg: Path, png: Path, density: int) -> None:
    if png.exists() and png.stat().st_mtime >= svg.stat().st_mtime:
        return
    png.parent.mkdir(parents=True, exist_ok=True)
    try:
        run_magick(svg, png, density)
    except subprocess.CalledProcessError:
        try:
            with tempfile.TemporaryDirectory(prefix="feynman-svg-") as tmp:
                run_magick(remove_dasharray(svg, Path(tmp)), png, density)
        except subprocess.CalledProcessError:
            quicklook_png(svg, png)


def add_source(notebook: NotebookRef, png: Path, timeout: float) -> dict:
    return run_json(
        [
            str(NOTEBOOKLM),
            "-p",
            notebook.profile,
            "source",
            "add",
            str(png),
            "-n",
            notebook.notebook_id,
            "--title",
            png.name,
            "--mime-type",
            "image/png",
            "--request-timeout",
            str(timeout),
            "--json",
        ],
        timeout=int(timeout) + 30,
    )


def sync_one(args: argparse.Namespace, notebook: NotebookRef) -> dict[str, object]:
    root = chapter_root(args.language, args.volume_code, notebook.chapter)
    figures_dir = root / "figures"
    png_dir = root / "figures-png"
    existing = existing_source_titles(notebook)
    added: list[str] = []
    skipped: list[str] = []
    for svg in sorted(figures_dir.glob("*.svg")):
        png = png_dir / f"{svg.stem}.png"
        convert_svg(svg, png, args.density)
        if png.name in existing:
            skipped.append(png.name)
            continue
        add_source(notebook, png, args.request_timeout)
        existing.add(png.name)
        added.append(png.name)
    return {"chapter": notebook.chapter, "profile": notebook.profile, "added": added, "skipped": skipped}


def main() -> int:
    args = parse_args()
    notebooks = discover_notebooks(parse_csv_strings(args.profiles), args.language, args.volume_code, parse_csv_numbers(args.chapters))
    results = [sync_one(args, notebook) for notebook in notebooks]
    print(json.dumps({"notebooks": len(notebooks), "results": results}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
