#!/usr/bin/env python3
"""Render downloaded NotebookLM Markdown reports into published HTML pages."""

from __future__ import annotations

import argparse
import html
import re
import shutil
import subprocess
from pathlib import Path

from reader_site import ROOT, write_if_changed


REPORT_KINDS = ("briefing", "study-guide")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", required=True, choices=("en", "ru"))
    parser.add_argument("--volume-code", required=True)
    parser.add_argument("--chapters", help="Comma-separated chapter numbers; default: all discovered reports")
    parser.add_argument("--check", action="store_true", help="Fail if rendered output would change.")
    return parser.parse_args()


def parse_chapters(raw: str | None) -> set[int] | None:
    if not raw:
        return None
    return {int(item.strip()) for item in raw.split(",") if item.strip()}


def source_root(language: str, volume_code: str) -> Path:
    return ROOT / "feynman-notebooklm" / language / f"volume-{volume_code}"


def target_reports_dir(language: str, volume_code: str) -> Path:
    return ROOT / f"feynman-html-{language}" / f"volume-{volume_code}-reference-guided-inline-svgmath" / "chapters" / "reports"


def chapter_number(path: Path) -> int | None:
    match = re.fullmatch(r"ch(\d+)", path.name)
    return int(match.group(1)) if match else None


def report_title(markdown: str, fallback: str) -> str:
    match = re.search(r"^\s*#\s+(.+?)\s*$", markdown, flags=re.M)
    if not match:
        return fallback
    title = re.sub(r"[*_`]+", "", match.group(1)).strip()
    return title or fallback


def render_markdown(markdown_path: Path) -> str:
    result = subprocess.run(
        ["pandoc", "--from=markdown+tex_math_dollars", "--to=html5", "--mathml", str(markdown_path)],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def page_html(language: str, chapter: int, title: str, body: str) -> str:
    escaped_title = html.escape(f"{title} - NotebookLM", quote=False)
    return (
        "<!doctype html>\n"
        f'<html lang="{language}">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"  <title>{escaped_title}</title>\n"
        '  <link rel="stylesheet" href="../../styles-20260616-inline-math-copy-fallback.css">\n'
        "</head>\n"
        f'<body class="notebooklm-report-page" data-language="{language}">\n'
        "  <script>\n"
        '    try { document.documentElement.dataset.theme = localStorage.getItem("flp-reader-theme") || "light"; } catch (_) {}\n'
        "  </script>\n"
        '<main class="notebooklm-report-shell">\n'
        f'  <nav class="notebooklm-report-nav"><a href="../ch{chapter:02d}.html">Back to chapter</a></nav>\n'
        '  <article class="notebooklm-report">\n'
        f"{body}\n"
        "  </article>\n"
        "</main>\n"
        "</body>\n"
        "</html>\n"
    )


def render_report(language: str, volume_code: str, chapter: int, kind: str, markdown_path: Path, out_dir: Path, check: bool) -> bool:
    markdown = markdown_path.read_text(encoding="utf-8")
    title = report_title(markdown, f"NotebookLM {kind}")
    body = render_markdown(markdown_path)
    html_text = page_html(language, chapter, title, body)
    html_path = out_dir / f"ch{chapter:02d}-notebooklm-{kind}.html"
    published_md_path = out_dir / f"ch{chapter:02d}-notebooklm-{kind}.md"

    changed = False
    for target, text in ((html_path, html_text), (published_md_path, markdown)):
        old = target.read_text(encoding="utf-8") if target.exists() else None
        if old != text:
            changed = True
            if not check:
                target.parent.mkdir(parents=True, exist_ok=True)
                if target.suffix == ".md":
                    shutil.copyfile(markdown_path, target)
                else:
                    write_if_changed(target, text)
    return changed


def main() -> int:
    args = parse_args()
    chapters_filter = parse_chapters(args.chapters)
    src_root = source_root(args.language, args.volume_code)
    out_dir = target_reports_dir(args.language, args.volume_code)
    changed: list[str] = []
    rendered = 0

    for chapter_dir in sorted(src_root.glob("ch*")):
        chapter = chapter_number(chapter_dir)
        if chapter is None or (chapters_filter is not None and chapter not in chapters_filter):
            continue
        for kind in REPORT_KINDS:
            markdown_path = chapter_dir / "reports" / f"ch{chapter:02d}-notebooklm-{kind}.md"
            if not markdown_path.exists():
                continue
            rendered += 1
            if render_report(args.language, args.volume_code, chapter, kind, markdown_path, out_dir, args.check):
                changed.append(f"ch{chapter:02d}-{kind}")

    if args.check and changed:
        print(f"would update {len(changed)} of {rendered} reports")
        return 1
    print(f"{'would render' if args.check else 'rendered'} {rendered} reports; changed={len(changed)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
