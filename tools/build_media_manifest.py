#!/usr/bin/env python3
"""Build the canonical chapter media manifest from published HTML pages."""

from __future__ import annotations

import argparse
import json
import re

from reader_site import CURRENT_ASSET_VERSION, MEDIA_MANIFEST, clean_text, chapter_pages, extract_tag, parse_youtube, read_text, write_if_changed


CARD_RE = re.compile(r"<article\b[^>]*\bstudy-youtube-card\b[^>]*>(.*?)</article>", re.I | re.S)
IFRAME_SRC_RE = re.compile(r"<iframe\b[^>]*\bsrc=[\"']([^\"']+)", re.I | re.S)
IFRAME_TITLE_RE = re.compile(r"<iframe\b[^>]*\btitle=[\"']([^\"']*)", re.I | re.S)
LINK_RE = re.compile(r"<a\b[^>]*\bstudy-youtube-link\b[^>]*\bhref=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", re.I | re.S)
STRONG_RE = re.compile(r"<strong\b[^>]*>(.*?)</strong>", re.I | re.S)
SPAN_RE = re.compile(r"<span\b[^>]*>(.*?)</span>", re.I | re.S)
REPORT_RE = re.compile(r"<a\b[^>]*\bstudy-card\b[^>]*\bhref=[\"']([^\"']*notebooklm-(briefing|study-guide)\.html)[\"'][^>]*>(.*?)</a>", re.I | re.S)


def card_type(card_html: str) -> str:
    title = clean_text(next(iter(STRONG_RE.findall(card_html)), ""))
    iframe_title = clean_text(next(iter(IFRAME_TITLE_RE.findall(card_html)), ""))
    detail = clean_text(next(iter(SPAN_RE.findall(card_html)), ""))
    text = f"{title} {iframe_title} {detail}"
    if re.search(r"\b(audio|аудио)", text, re.I) and not re.search(r"\b(video|видео)", title, re.I):
        return "audio"
    return "video"


def extract_media(text: str) -> list[dict[str, object]]:
    media: list[dict[str, object]] = []
    for card_html in CARD_RE.findall(text):
        src_match = IFRAME_SRC_RE.search(card_html)
        link_match = LINK_RE.search(card_html)
        href = link_match.group(1) if link_match else ""
        video_id, start = parse_youtube(src_match.group(1) if src_match else href)
        if not video_id:
            video_id, start = parse_youtube(href)
        if not video_id:
            continue
        title = clean_text(next(iter(STRONG_RE.findall(card_html)), ""))
        label = clean_text(next(iter(IFRAME_TITLE_RE.findall(card_html)), title))
        detail = clean_text(next(iter(SPAN_RE.findall(card_html)), ""))
        media.append(
            {
                "type": card_type(card_html),
                "youtube_id": video_id,
                "start": start,
                "title": title,
                "label": label,
                "detail": detail,
                "watch_url": href,
            }
        )
    return media


def extract_reports(text: str) -> dict[str, str]:
    reports: dict[str, str] = {}
    for href, kind, _label in REPORT_RE.findall(text):
        reports["overview" if kind == "briefing" else "guide"] = href
    return reports


def build_manifest() -> dict[str, object]:
    chapters: dict[str, object] = {}
    for page in chapter_pages():
        text = read_text(page.path)
        media = extract_media(text)
        reports = extract_reports(text)
        if not media and not reports:
            continue
        chapters[page.key] = {
            "path": page.rel,
            "language": page.language,
            "volume": page.volume,
            "chapter": page.chapter,
            "title": extract_tag(text, "h1") or extract_tag(text, "title"),
            "reports": reports,
            "media": media,
        }
    return {
        "schema": "feynman-reader-media-manifest-v1",
        "asset_version": CURRENT_ASSET_VERSION,
        "chapters": chapters,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if the manifest is not up to date.")
    args = parser.parse_args()

    text = json.dumps(build_manifest(), ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.check:
        current = MEDIA_MANIFEST.read_text(encoding="utf-8") if MEDIA_MANIFEST.exists() else ""
        if current != text:
            raise SystemExit(f"{MEDIA_MANIFEST.relative_to(MEDIA_MANIFEST.parents[1])} is not up to date")
        print("media manifest ok")
        return 0

    changed = write_if_changed(MEDIA_MANIFEST, text)
    print(f"{'updated' if changed else 'unchanged'} {MEDIA_MANIFEST.relative_to(MEDIA_MANIFEST.parents[1])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
