#!/usr/bin/env python3
"""Update Feynman Reader CSS/JS cache-buster versions."""

from __future__ import annotations

import argparse
import re

from reader_site import ROOT, reader_html_pages, read_text, write_if_changed


ASSET_RE = re.compile(r"(media-player\.(?:css|js)\?v=)([A-Za-z0-9_.-]+)")
SHIM_RE = re.compile(r"(media-player\.js\?v=)([A-Za-z0-9_.-]+)")


def update_text(text: str, version: str) -> str:
    return ASSET_RE.sub(lambda match: match.group(1) + version, text)


def update_shim(text: str, version: str) -> str:
    return SHIM_RE.sub(lambda match: match.group(1) + version, text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("version")
    parser.add_argument("--check", action="store_true", help="Fail if any target would change.")
    args = parser.parse_args()

    targets = reader_html_pages() + [
        ROOT / "feynman-reader" / "chapter-media.js",
        ROOT / "feynman-reader" / "study-media-player.js",
    ]
    changed = []
    for path in targets:
        text = read_text(path)
        new_text = update_shim(text, args.version) if path.suffix == ".js" else update_text(text, args.version)
        if new_text != text:
            changed.append(path)
            if not args.check:
                write_if_changed(path, new_text)

    if args.check and changed:
        for path in changed:
            print(f"stale asset version: {path.relative_to(ROOT)}")
        raise SystemExit(1)

    print(f"{'would update' if args.check else 'updated'} {len(changed)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
