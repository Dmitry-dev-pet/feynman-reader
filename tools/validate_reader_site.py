#!/usr/bin/env python3
"""Validate the static Feynman Reader release wiring."""

from __future__ import annotations

import argparse
import json
import re
import subprocess

from build_media_manifest import build_manifest
from reader_site import CURRENT_ASSET_VERSION, MEDIA_MANIFEST, ROOT, chapter_pages, read_text, reader_html_pages


EXPECTED_CHAPTERS = {
    "ru-I": 52,
    "en-I": 52,
    "ru-II": 42,
    "en-II": 42,
    "ru-III": 21,
    "en-III": 21,
}
EXPECTED_MEDIA_PAGES = {
    "ru-I": 52,
    "en-I": 28,
    "ru-II": 42,
    "en-II": 0,
    "ru-III": 21,
    "en-III": 0,
}
EXPECTED_REPORT_PAGES = {
    "ru-I": 52,
    "en-I": 52,
    "ru-II": 42,
    "en-II": 0,
    "ru-III": 21,
    "en-III": 0,
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def git_tracked(paths: list[str]) -> list[str]:
    result = subprocess.run(["git", "ls-files", *paths], cwd=ROOT, check=True, text=True, capture_output=True)
    return [line for line in result.stdout.splitlines() if line.strip()]


def validate_manifest(errors: list[str]) -> None:
    expected = json.dumps(build_manifest(), ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    actual = MEDIA_MANIFEST.read_text(encoding="utf-8") if MEDIA_MANIFEST.exists() else ""
    if actual != expected:
        fail(errors, "feynman-reader/media-manifest.json is stale; run tools/build_media_manifest.py")


def validate_assets(errors: list[str]) -> None:
    stale_re = re.compile(r"media-player\.(?:css|js)\?v=(?!%s)[A-Za-z0-9_.-]+" % re.escape(CURRENT_ASSET_VERSION))
    for path in reader_html_pages():
        text = read_text(path)
        if stale_re.search(text):
            fail(errors, f"stale media-player asset version in {path.relative_to(ROOT)}")
    for rel in ("feynman-reader/chapter-media.js", "feynman-reader/study-media-player.js"):
        path = ROOT / rel
        if stale_re.search(read_text(path)):
            fail(errors, f"stale shim asset version in {rel}")


def validate_chapters(errors: list[str]) -> None:
    manifest = build_manifest()
    manifest_chapters = manifest.get("chapters", {})
    chapter_counts = {key: 0 for key in EXPECTED_CHAPTERS}
    media_counts = {key: 0 for key in EXPECTED_MEDIA_PAGES}
    report_counts = {key: 0 for key in EXPECTED_REPORT_PAGES}

    for page in chapter_pages():
        group = f"{page.language}-{page.volume}"
        chapter_counts[group] = chapter_counts.get(group, 0) + 1
        text = read_text(page.path)
        rel = page.path.relative_to(ROOT)
        manifest_entry = manifest_chapters.get(page.key, {})
        has_media = bool(manifest_entry.get("media")) if isinstance(manifest_entry, dict) else False
        has_reports = bool(manifest_entry.get("reports")) if isinstance(manifest_entry, dict) else False

        if "chapter-media-panel" in text:
            fail(errors, f"legacy chapter-media-panel remains in {rel}")
        if "study-workspace" in text:
            fail(errors, f"legacy study workspace remains in {rel}")
        if "study-mode-switch" in text:
            fail(errors, f"legacy study mode switch remains in {rel}")
        if "data-study-mode=" in text:
            fail(errors, f"legacy study mode button remains in {rel}")
        if "data-study-section=" in text:
            fail(errors, f"legacy study section remains in {rel}")
        if "BEGIN NotebookLM script" in text:
            fail(errors, f"legacy NotebookLM inline script remains in {rel}")
        if 'data-study-section="notes"' in text or "data-study-section='notes'" in text:
            fail(errors, f"manifest-backed notes section remains in {rel}")
        if 'data-study-section="media"' in text or "data-study-section='media'" in text:
            fail(errors, f"manifest-backed media section remains in {rel}")
        if "study-youtube-card" in text:
            fail(errors, f"manifest-backed YouTube card remains in {rel}")
        if has_media:
            media_counts[group] = media_counts.get(group, 0) + 1
            if f"media-player.js?v={CURRENT_ASSET_VERSION}" not in text:
                fail(errors, f"missing current media-player.js on media page {rel}")
            if f"media-player.css?v={CURRENT_ASSET_VERSION}" not in text:
                fail(errors, f"missing current media-player.css on media page {rel}")
        if has_reports:
            report_counts[group] = report_counts.get(group, 0) + 1
            if f"media-player.js?v={CURRENT_ASSET_VERSION}" not in text:
                fail(errors, f"missing current media-player.js on report page {rel}")
            if f"media-player.css?v={CURRENT_ASSET_VERSION}" not in text:
                fail(errors, f"missing current media-player.css on report page {rel}")

    for group, expected in EXPECTED_CHAPTERS.items():
        if chapter_counts.get(group, 0) != expected:
            fail(errors, f"{group} chapter count {chapter_counts.get(group, 0)} != {expected}")
    for group, expected in EXPECTED_MEDIA_PAGES.items():
        if media_counts.get(group, 0) != expected:
            fail(errors, f"{group} media page count {media_counts.get(group, 0)} != {expected}")
    for group, expected in EXPECTED_REPORT_PAGES.items():
        if report_counts.get(group, 0) != expected:
            fail(errors, f"{group} report page count {report_counts.get(group, 0)} != {expected}")


def validate_git_boundary(errors: list[str]) -> None:
    tracked = git_tracked([
        "youtube-client-secrets*.json",
        "youtube-token*.json",
        "local-media",
        "youtube-compilations",
        "youtube-video-compilations",
    ])
    if tracked:
        fail(errors, "local media or YouTube credentials are tracked: " + ", ".join(tracked[:8]))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    errors: list[str] = []

    validate_manifest(errors)
    validate_assets(errors)
    validate_chapters(errors)
    validate_git_boundary(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("reader site validation ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
