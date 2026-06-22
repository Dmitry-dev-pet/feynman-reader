#!/usr/bin/env python3
"""Generate and download NotebookLM audio overviews for chapter notebooks."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
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
    parser.add_argument("--generate-missing", action="store_true")
    parser.add_argument("--length", choices=("short", "default", "long"), default="default")
    parser.add_argument("--format", choices=("deep-dive", "brief", "critique", "debate"), default="deep-dive")
    parser.add_argument("--timeout", type=int, default=1200)
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


def output_dir(language: str, volume_code: str) -> Path:
    return ROOT / f"feynman-html-{language}" / f"volume-{volume_code}-reference-guided-inline-svgmath" / "chapters" / "media"


def audio_artifacts(profile: str, notebook_id: str) -> list[dict]:
    payload = run_json([str(NOTEBOOKLM), "-p", profile, "artifact", "list", "-n", notebook_id, "--json"])
    artifacts = []
    for artifact in payload.get("artifacts", []):
        type_text = f"{artifact.get('type_id') or ''} {artifact.get('type') or ''}".casefold()
        if "audio" in type_text and str(artifact.get("status") or "") == "completed":
            artifacts.append(artifact)
    return sorted(artifacts, key=lambda item: str(item.get("created_at") or ""))


def generate_audio(args: argparse.Namespace, notebook: NotebookRef) -> dict:
    command = [
        str(NOTEBOOKLM),
        "-p",
        notebook.profile,
        "generate",
        "audio",
        "-n",
        notebook.notebook_id,
        "--format",
        args.format,
        "--length",
        args.length,
        "--language",
        args.language,
        "--wait",
        "--timeout",
        str(args.timeout),
        "--json",
    ]
    return run_json(command, timeout=args.timeout + 60)


def download_audio(notebook: NotebookRef, artifact_id: str, out_path: Path) -> dict:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    return run_json(
        [
            str(NOTEBOOKLM),
            "-p",
            notebook.profile,
            "download",
            "audio",
            "-n",
            notebook.notebook_id,
            "-a",
            artifact_id,
            str(out_path),
            "--force",
            "--json",
        ],
        timeout=300,
    )


def sync_one(args: argparse.Namespace, notebook: NotebookRef, media_dir: Path) -> dict[str, object]:
    out_path = media_dir / f"ch{notebook.chapter:02d}-notebooklm-audio-deep-dive.mp3"
    if out_path.exists() and out_path.stat().st_size > 0:
        return {"chapter": notebook.chapter, "profile": notebook.profile, "status": "exists", "path": str(out_path)}

    artifacts = audio_artifacts(notebook.profile, notebook.notebook_id)
    generated = False
    if not artifacts and args.generate_missing:
        generate_audio(args, notebook)
        generated = True
        artifacts = audio_artifacts(notebook.profile, notebook.notebook_id)
    if not artifacts:
        return {"chapter": notebook.chapter, "profile": notebook.profile, "status": "missing"}

    artifact = artifacts[-1]
    download_audio(notebook, str(artifact["id"]), out_path)
    return {
        "chapter": notebook.chapter,
        "profile": notebook.profile,
        "status": "downloaded-generated" if generated else "downloaded",
        "artifact_id": str(artifact["id"]),
        "path": str(out_path),
    }


def main() -> int:
    args = parse_args()
    notebooks = discover_notebooks(parse_csv_strings(args.profiles), args.language, args.volume_code, parse_csv_numbers(args.chapters))
    media_dir = output_dir(args.language, args.volume_code)
    results = [sync_one(args, notebook, media_dir) for notebook in notebooks]
    print(json.dumps({"notebooks": len(notebooks), "results": results}, ensure_ascii=False, indent=2))
    missing = [item for item in results if item.get("status") == "missing"]
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
