#!/usr/bin/env python3
"""Remove chapter HTML blocks now backed by media-manifest.json."""

from __future__ import annotations

import argparse
import re

from reader_site import ROOT, chapter_pages, read_text, write_if_changed


SECTION_RE = re.compile(
    r"\n?[ \t]*<section\b(?=[^>]*\bstudy-section\b)(?=[^>]*\bdata-study-section=[\"'](?:notes|media)[\"'])[^>]*>.*?</section>[ \t]*\n?",
    re.I | re.S,
)
MODE_BUTTON_RE = re.compile(
    r"<button\b(?=[^>]*\bstudy-mode-btn\b)(?=[^>]*\bdata-study-mode=[\"'](?:notes|media)[\"'])[^>]*>.*?</button>",
    re.I | re.S,
)


def clean_text(text: str) -> str:
    text = SECTION_RE.sub("\n", text)
    text = MODE_BUTTON_RE.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if any chapter still needs cleanup.")
    args = parser.parse_args()

    changed = []
    for page in chapter_pages():
        text = read_text(page.path)
        new_text = clean_text(text)
        if new_text != text:
            changed.append(page.path)
            if not args.check:
                write_if_changed(page.path, new_text)

    if args.check and changed:
        for path in changed[:40]:
            print(f"manifest-backed HTML remains: {path.relative_to(ROOT)}")
        if len(changed) > 40:
            print(f"... and {len(changed) - 40} more")
        raise SystemExit(1)

    print(f"{'would clean' if args.check else 'cleaned'} {len(changed)} chapter files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
