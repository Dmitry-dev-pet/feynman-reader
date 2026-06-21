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
TOOLBAR_BLOCK_RE = re.compile(
    r"\n?[ \t]*<!-- BEGIN NotebookLM toolbar -->.*?<!-- END NotebookLM toolbar -->[ \t]*\n?",
    re.S,
)
REPORTS_BLOCK_RE = re.compile(
    r"\n?[ \t]*<!-- BEGIN NotebookLM reports -->.*?<!-- END NotebookLM reports -->[ \t]*\n?",
    re.S,
)
SCRIPT_BLOCK_RE = re.compile(
    r"\n?[ \t]*<!-- BEGIN NotebookLM script -->.*?<!-- END NotebookLM script -->[ \t]*\n?",
    re.S,
)
MODE_BUTTON_RE = re.compile(
    r"<button\b(?=[^>]*\bstudy-mode-btn\b)(?=[^>]*\bdata-study-mode=[\"'](?:notes|media)[\"'])[^>]*>.*?</button>",
    re.I | re.S,
)
ARTICLE_TAG_RE = re.compile(r"<article\b[^>]*>", re.I)


def clean_article_tag(match: re.Match[str]) -> str:
    tag = match.group(0)
    if "chapter-flow" not in tag:
        return tag

    tag = re.sub(r"\s+data-study-section=[\"']lecture[\"']", "", tag, flags=re.I)

    def clean_class(class_match: re.Match[str]) -> str:
        quote = class_match.group(1)
        classes = [name for name in class_match.group(2).split() if name != "study-section"]
        return f"class={quote}{' '.join(classes)}{quote}"

    return re.sub(r"\bclass=([\"'])(.*?)(\1)", lambda m: clean_class(m), tag, count=1, flags=re.I)


def clean_text(text: str) -> str:
    text = SECTION_RE.sub("\n", text)
    text = MODE_BUTTON_RE.sub("", text)
    text = TOOLBAR_BLOCK_RE.sub("\n", text)
    text = REPORTS_BLOCK_RE.sub("\n", text)
    text = SCRIPT_BLOCK_RE.sub("\n", text)
    text = ARTICLE_TAG_RE.sub(clean_article_tag, text)
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
