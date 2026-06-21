#!/usr/bin/env python3
"""Update volume table-of-contents links to current media/report routes."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from reader_site import ROOT, write_if_changed


def index_pages() -> list[Path]:
    pages: list[Path] = []
    for language_dir in ("feynman-html-ru", "feynman-html-en"):
        pages.extend(sorted((ROOT / language_dir).glob("volume-*-reference-guided-inline-svgmath/index.html")))
    return pages


def update_page(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")

    def guide_href(match: re.Match[str]) -> str:
        chapter = match.group(1)
        report = path.parent / "chapters" / "reports" / f"ch{chapter}-notebooklm-study-guide.html"
        if report.exists():
            return f'chapters/reports/ch{chapter}-notebooklm-study-guide.html'
        return f'chapters/ch{chapter}.html'

    html = re.sub(r"chapters/ch(\d+)\.html#study-panel", guide_href, html)
    html = re.sub(r"chapters/ch(\d+)\.html#study-media", r"chapters/ch\1.html#chapter-media", html)
    return write_if_changed(path, html)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    changed: list[Path] = []
    for path in index_pages():
        original = path.read_text(encoding="utf-8")
        update_page(path)
        updated = path.read_text(encoding="utf-8")
        if updated != original:
            changed.append(path)
            if args.check:
                path.write_text(original, encoding="utf-8")

    if args.check and changed:
        print(f"would update {len(changed)} volume index files")
        return 1
    print(f"updated {len(changed)} volume index files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
