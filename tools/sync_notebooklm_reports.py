#!/usr/bin/env python3
"""Download NotebookLM report artifacts into local chapter package folders."""

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
    parser.add_argument("--notebooklm-root", type=Path)
    parser.add_argument("--timeout", type=int, default=180)
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


def report_artifacts(profile: str, notebook_id: str) -> list[dict]:
    payload = run_json([str(NOTEBOOKLM), "-p", profile, "artifact", "list", "-n", notebook_id, "--json"])
    reports = [
        artifact
        for artifact in payload.get("artifacts", [])
        if str(artifact.get("type_id") or "") == "report" and str(artifact.get("status") or "") == "completed"
    ]
    return sorted(reports, key=lambda item: str(item.get("created_at") or ""))


def report_kind(artifact: dict, index: int) -> str:
    title = str(artifact.get("title") or artifact.get("name") or "").casefold()
    if any(token in title for token in ("briefing", "analytic", "analysis", "отчет", "анализ")):
        return "briefing"
    if any(token in title for token in ("study", "guide", "конспект", "пособие", "руководство")):
        return "study-guide"
    return "briefing" if index == 0 else "study-guide"


def default_root(language: str, volume_code: str) -> Path:
    return ROOT / "feynman-notebooklm" / language / f"volume-{volume_code}"


def sync_one(root: Path, notebook: NotebookRef, timeout: int) -> dict[str, object]:
    reports_dir = root / f"ch{notebook.chapter:02d}" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    outcomes: list[dict[str, object]] = []
    used: set[str] = set()
    for index, artifact in enumerate(report_artifacts(notebook.profile, notebook.notebook_id)):
        kind = report_kind(artifact, index)
        if kind in used:
            kind = f"report-{index + 1}"
        used.add(kind)
        artifact_id = str(artifact["id"])
        out_path = reports_dir / f"ch{notebook.chapter:02d}-notebooklm-{kind}.md"
        try:
            run_json(
                [
                    str(NOTEBOOKLM),
                    "-p",
                    notebook.profile,
                    "download",
                    "report",
                    "-n",
                    notebook.notebook_id,
                    "-a",
                    artifact_id,
                    str(out_path),
                    "--force",
                    "--json",
                ],
                timeout=timeout,
            )
            outcomes.append({"kind": kind, "status": "downloaded", "artifact_id": artifact_id, "path": str(out_path)})
        except subprocess.TimeoutExpired:
            outcomes.append({"kind": kind, "status": "timeout", "artifact_id": artifact_id})
        except subprocess.CalledProcessError as exc:
            outcomes.append(
                {
                    "kind": kind,
                    "status": "error",
                    "artifact_id": artifact_id,
                    "stderr": (exc.stderr or "").strip()[-500:],
                }
            )
    return {
        "chapter": notebook.chapter,
        "profile": notebook.profile,
        "notebook_id": notebook.notebook_id,
        "reports": outcomes,
    }


def main() -> int:
    args = parse_args()
    chapters = parse_csv_numbers(args.chapters)
    profiles = parse_csv_strings(args.profiles)
    root = args.notebooklm_root or default_root(args.language, args.volume_code)
    notebooks = discover_notebooks(profiles, args.language, args.volume_code, chapters)
    results = [sync_one(root, notebook, args.timeout) for notebook in notebooks]
    print(json.dumps({"notebooks": len(notebooks), "results": results}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
