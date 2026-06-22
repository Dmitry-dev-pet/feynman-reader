#!/usr/bin/env python3
"""Ensure chapter pages with manifest-backed materials load media-player assets."""

from __future__ import annotations

import argparse
import json

from reader_site import CURRENT_ASSET_VERSION, MEDIA_MANIFEST, ROOT, chapter_pages, read_text, write_if_changed


CSS_TAG = f'<link rel="stylesheet" href="../../../feynman-reader/media-player.css?v={CURRENT_ASSET_VERSION}">'
JS_TAG = f'<script src="../../../feynman-reader/media-player.js?v={CURRENT_ASSET_VERSION}" defer></script>'


def material_chapter_keys() -> set[str]:
    data = json.loads(MEDIA_MANIFEST.read_text(encoding="utf-8"))
    chapters = data.get("chapters", {})
    keys: set[str] = set()
    if not isinstance(chapters, dict):
        return keys
    for key, item in chapters.items():
        if isinstance(item, dict) and (item.get("media") or item.get("reports")):
            keys.add(str(key))
    return keys


def ensure_assets(text: str) -> str:
    if "media-player.css" not in text:
        text = text.replace("</head>", f"{CSS_TAG}\n</head>", 1)
    if "media-player.js" not in text:
        text = text.replace("</body>", f"{JS_TAG}\n</body>", 1)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    keys = material_chapter_keys()
    changed = []
    for page in chapter_pages():
        if page.key not in keys:
            continue
        text = read_text(page.path)
        updated = ensure_assets(text)
        if updated != text:
            changed.append(page.path)
            if not args.check:
                write_if_changed(page.path, updated)

    if args.check and changed:
        for path in changed[:40]:
            print(f"missing media-player assets: {path.relative_to(ROOT)}")
        if len(changed) > 40:
            print(f"... and {len(changed) - 40} more")
        raise SystemExit(1)

    print(f"{'would update' if args.check else 'updated'} {len(changed)} chapter files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
