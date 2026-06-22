#!/usr/bin/env python3
"""Generate and download NotebookLM video overviews for chapter notebooks."""

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
    parser.add_argument("--regenerate", action="store_true", help="Generate a new video even if a video artifact already exists")
    parser.add_argument("--force-download", action="store_true", help="Overwrite existing local video files")
    parser.add_argument("--format", choices=("explainer", "brief"), default="explainer")
    parser.add_argument("--style", default="classic")
    parser.add_argument("--timeout", type=int, default=1800)
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


def video_artifacts(profile: str, notebook_id: str, *, completed_only: bool = True) -> list[dict]:
    payload = run_json([str(NOTEBOOKLM), "-p", profile, "artifact", "list", "-n", notebook_id, "--json"])
    artifacts = []
    for artifact in payload.get("artifacts", []):
        type_text = f"{artifact.get('type_id') or ''} {artifact.get('type') or ''}".casefold()
        if "video" not in type_text:
            continue
        if completed_only and str(artifact.get("status") or "") != "completed":
            continue
        artifacts.append(artifact)
    return sorted(artifacts, key=lambda item: str(item.get("created_at") or ""))


def generate_video(args: argparse.Namespace, notebook: NotebookRef) -> dict:
    command = [
        str(NOTEBOOKLM),
        "-p",
        notebook.profile,
        "generate",
        "video",
        "-n",
        notebook.notebook_id,
        "--format",
        args.format,
        "--style",
        args.style,
        "--language",
        args.language,
        "--wait",
        "--timeout",
        str(args.timeout),
        "--json",
    ]
    return run_json(command, timeout=args.timeout + 60)


def wait_artifact(args: argparse.Namespace, notebook: NotebookRef, artifact_id: str) -> dict:
    return run_json(
        [
            str(NOTEBOOKLM),
            "-p",
            notebook.profile,
            "artifact",
            "wait",
            artifact_id,
            "-n",
            notebook.notebook_id,
            "--timeout",
            str(args.timeout),
            "--json",
        ],
        timeout=args.timeout + 60,
    )


def download_video(notebook: NotebookRef, artifact_id: str, out_path: Path) -> dict:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    return run_json(
        [
            str(NOTEBOOKLM),
            "-p",
            notebook.profile,
            "download",
            "video",
            "-n",
            notebook.notebook_id,
            "-a",
            artifact_id,
            str(out_path),
            "--force",
            "--json",
        ],
        timeout=600,
    )


def sync_one(args: argparse.Namespace, notebook: NotebookRef, media_dir: Path) -> dict[str, object]:
    out_path = media_dir / f"ch{notebook.chapter:02d}-notebooklm-video.mp4"
    if out_path.exists() and out_path.stat().st_size > 0 and not args.force_download and not args.regenerate:
        return {"chapter": notebook.chapter, "profile": notebook.profile, "status": "exists", "path": str(out_path)}

    all_existing = video_artifacts(notebook.profile, notebook.notebook_id, completed_only=False)
    existing_ids = {str(artifact.get("id")) for artifact in all_existing}
    artifacts = video_artifacts(notebook.profile, notebook.notebook_id)
    if not artifacts:
        pending = [artifact for artifact in all_existing if str(artifact.get("status") or "") in {"in_progress", "pending"}]
        if pending:
            wait_artifact(args, notebook, str(pending[-1]["id"]))
            artifacts = video_artifacts(notebook.profile, notebook.notebook_id)
    generated = False
    if args.regenerate or (not artifacts and args.generate_missing):
        try:
            generate_video(args, notebook)
        except subprocess.CalledProcessError:
            pass
        generated = True
        refreshed_all = video_artifacts(notebook.profile, notebook.notebook_id, completed_only=False)
        new_any_status = [artifact for artifact in refreshed_all if str(artifact.get("id")) not in existing_ids]
        if new_any_status:
            wait_artifact(args, notebook, str(new_any_status[-1]["id"]))
        refreshed = video_artifacts(notebook.profile, notebook.notebook_id)
        new_artifacts = [artifact for artifact in refreshed if str(artifact.get("id")) not in existing_ids]
        artifacts = new_artifacts or refreshed
    if not artifacts:
        return {"chapter": notebook.chapter, "profile": notebook.profile, "status": "missing"}

    artifact = artifacts[-1]
    download_video(notebook, str(artifact["id"]), out_path)
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
