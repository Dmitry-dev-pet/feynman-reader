#!/usr/bin/env python3
"""Shared helpers for Feynman Reader static-site maintenance."""

from __future__ import annotations

import re
from dataclasses import dataclass
from html import unescape
from pathlib import Path
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parents[1]
READER_DIR = ROOT / "feynman-reader"
MEDIA_MANIFEST = READER_DIR / "media-manifest.json"
CURRENT_ASSET_VERSION = "20260621-floating-video"


@dataclass(frozen=True)
class ChapterPage:
    path: Path
    language: str
    volume: str
    chapter: int

    @property
    def key(self) -> str:
        return f"{self.language}-{self.volume}/ch{self.chapter:02d}"

    @property
    def rel(self) -> str:
        return self.path.relative_to(ROOT).as_posix()


def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = unescape(value)
    return re.sub(r"\s+", " ", value).strip()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, text: str) -> bool:
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if old == text:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def chapter_pages() -> list[ChapterPage]:
    pages: list[ChapterPage] = []
    for lang_dir in ("feynman-html-ru", "feynman-html-en"):
        language = "ru" if lang_dir.endswith("-ru") else "en"
        for path in sorted((ROOT / lang_dir).glob("volume-*-reference-guided-inline-svgmath/chapters/ch*.html")):
            volume_match = re.search(r"volume-([IVX]+)-", path.as_posix())
            chapter_match = re.search(r"/ch(\d+)\.html$", path.as_posix())
            if not volume_match or not chapter_match:
                continue
            pages.append(ChapterPage(path=path, language=language, volume=volume_match.group(1), chapter=int(chapter_match.group(1))))
    return pages


def reader_html_pages() -> list[Path]:
    pages = [
        ROOT / "index.html",
        ROOT / "feynman.html",
        READER_DIR / "index.html",
    ]
    pages.extend(sorted((ROOT / "feynman-html-ru").glob("volume-*-reference-guided-inline-svgmath/index.html")))
    pages.extend(sorted((ROOT / "feynman-html-en").glob("volume-*-reference-guided-inline-svgmath/index.html")))
    pages.extend(page.path for page in chapter_pages())
    pages.extend(sorted((ROOT / "feynman-html-ru").glob("volume-*-reference-guided-inline-svgmath/chapters/reports/*.html")))
    pages.extend(sorted((ROOT / "feynman-html-en").glob("volume-*-reference-guided-inline-svgmath/chapters/reports/*.html")))
    return [page for page in pages if page.exists()]


def extract_tag(text: str, tag: str) -> str:
    match = re.search(rf"<{tag}\b[^>]*>(.*?)</{tag}>", text, re.I | re.S)
    return clean_text(match.group(1)) if match else ""


def parse_youtube(value: str) -> tuple[str, int]:
    if not value:
        return "", 0
    url = urlparse(unescape(value))
    video_id = ""
    if "youtu.be" in url.netloc:
        video_id = url.path.strip("/").split("/")[0]
    elif "youtube" in url.netloc:
        query = parse_qs(url.query)
        video_id = query.get("v", [""])[0]
        if not video_id and "/embed/" in url.path:
            video_id = url.path.split("/embed/", 1)[1].split("/", 1)[0]
    query = parse_qs(url.query)
    start_value = query.get("start", query.get("t", ["0"]))[0]
    return video_id, parse_time(start_value)


def parse_time(value: str) -> int:
    value = str(value or "0").strip()
    if value.isdigit():
        return int(value)
    match = re.fullmatch(r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?", value, flags=re.I)
    if not match:
        return 0
    return int(match.group(1) or 0) * 3600 + int(match.group(2) or 0) * 60 + int(match.group(3) or 0)
