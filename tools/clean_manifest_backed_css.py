#!/usr/bin/env python3
"""Remove CSS for chapter UI now replaced by media-manifest runtime."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from reader_site import ROOT, READER_DIR, read_text, write_if_changed


LEGACY_VOLUME_PREFIX_RE = re.compile(
    r"(/\* BEGIN NotebookLM reports \*/\n).*?(?=\.notebooklm-index-panel)",
    re.S,
)
LEGACY_VOLUME_MEDIA_RE = re.compile(
    r"\n@media \(max-width: 860px\) \{\n\s*\.study-mode-switch\b.*?\n\}\n(?=/\* END NotebookLM reports \*/)",
    re.S,
)
LEGACY_MEDIA_PLAYER_RE = re.compile(
    r"\n?(?:body\[data-theme=\"dark\"\]\s+)?\.study-(?:mode-switch|youtube)[^{]*\{[^{}]*\}\n?",
    re.S,
)


def css_files() -> list[Path]:
    files = sorted((ROOT / "feynman-html-ru").glob("volume-*-reference-guided-inline-svgmath/styles*.css"))
    files += sorted((ROOT / "feynman-html-en").glob("volume-*-reference-guided-inline-svgmath/styles*.css"))
    files.append(READER_DIR / "media-player.css")
    return files


def clean_text(text: str, path: Path) -> str:
    if path.name == "media-player.css":
        text = LEGACY_MEDIA_PLAYER_RE.sub("\n", text)
    else:
        text = LEGACY_VOLUME_PREFIX_RE.sub(r"\1", text)
        text = LEGACY_VOLUME_MEDIA_RE.sub("\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if any CSS still needs cleanup.")
    args = parser.parse_args()

    changed = []
    for path in css_files():
        if not path.exists():
            continue
        text = read_text(path)
        new_text = clean_text(text, path)
        if new_text != text:
            changed.append(path)
            if not args.check:
                write_if_changed(path, new_text)

    if args.check and changed:
        for path in changed[:40]:
            print(f"manifest-backed CSS remains: {path.relative_to(ROOT)}")
        if len(changed) > 40:
            print(f"... and {len(changed) - 40} more")
        raise SystemExit(1)

    print(f"{'would clean' if args.check else 'cleaned'} {len(changed)} CSS files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
