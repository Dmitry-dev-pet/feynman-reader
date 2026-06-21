#!/usr/bin/env python3
"""Apply SEO metadata to the static Feynman Reader release."""

from __future__ import annotations

import json
import re
from datetime import date
from html import escape, unescape
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://dmitry-dev-pet.github.io/feynman-reader/"
FAVICON_URL = BASE_URL + "feynman-reader/favicon-192.png"
APPLE_TOUCH_ICON_URL = BASE_URL + "feynman-reader/apple-touch-icon.png"
TODAY = date.today().isoformat()

VOLUMES = {
    "volume-I": {
        "ru_name": "том I",
        "en_name": "Volume I",
        "ru_topic": "механика, излучение и тепло",
        "en_topic": "mechanics, radiation, and heat",
    },
    "volume-II": {
        "ru_name": "том II",
        "en_name": "Volume II",
        "ru_topic": "электромагнетизм и материя",
        "en_topic": "electromagnetism and matter",
    },
    "volume-III": {
        "ru_name": "том III",
        "en_name": "Volume III",
        "ru_topic": "квантовая механика",
        "en_topic": "quantum mechanics",
    },
}


def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def extract_tag(text: str, tag: str) -> str:
    match = re.search(rf"<{tag}\b[^>]*>(.*?)</{tag}>", text, re.I | re.S)
    return clean_text(match.group(1)) if match else ""


def extract_lang(path: Path, text: str) -> str:
    match = re.search(r"<html\b[^>]*\blang=[\"']([^\"']+)", text, re.I)
    if match:
        return match.group(1).split("-")[0].lower()
    return "ru" if "feynman-html-ru" in path.parts else "en"


def volume_key(path: Path) -> str:
    for part in path.parts:
        match = re.match(r"(volume-[IVX]+)-", part)
        if match:
            return match.group(1)
    return ""


def relative_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    return "" if rel == "index.html" else rel


def absolute_url(path: Path) -> str:
    rel = relative_url(path)
    if not rel:
        return BASE_URL
    return BASE_URL + quote(rel, safe="/-_.~")


def paired_language_path(path: Path) -> Path | None:
    rel = path.relative_to(ROOT).as_posix()
    if rel.startswith("feynman-html-ru/"):
        other = ROOT / rel.replace("feynman-html-ru/", "feynman-html-en/", 1)
    elif rel.startswith("feynman-html-en/"):
        other = ROOT / rel.replace("feynman-html-en/", "feynman-html-ru/", 1)
    else:
        return None
    return other if other.exists() else None


def page_description(path: Path, label: str, lang: str, is_chapter: bool) -> str:
    key = volume_key(path)
    meta = VOLUMES.get(key, {})
    if is_chapter:
        if lang == "ru":
            volume = meta.get("ru_name", "том")
            return (
                f"{label}: глава из Фейнмановских лекций по физике, {volume}. "
                "Формулы, рисунки, оглавление, медиа и учебные материалы для чтения онлайн."
            )
        volume = meta.get("en_name", "Volume")
        return (
            f"{label}: chapter from The Feynman Lectures on Physics, {volume}. "
            "Online reading with formulas, figures, navigation, and companion study materials where available."
        )
    if key:
        if lang == "ru":
            return (
                f"Оглавление {meta.get('ru_name', 'тома')} Фейнмановских лекций по физике: "
                f"{meta.get('ru_topic', 'главы, формулы и рисунки')}."
            )
        return (
            f"Contents for The Feynman Lectures on Physics, {meta.get('en_name', 'Volume')}: "
            f"{meta.get('en_topic', 'chapters, formulas, and figures')}."
        )
    if lang == "en":
        return (
            "Interactive Feynman Lectures reader with three volumes, formulas, figures, "
            "Russian and English navigation, audio, video, and study materials."
        )
    return (
        "Интерактивный читатель Фейнмановских лекций по физике: три тома, формулы, "
        "рисунки, русская и английская навигация, аудио, видео и учебные материалы."
    )


def seo_block(path: Path, text: str, *, noindex: bool = False) -> str:
    title = extract_tag(text, "title") or extract_tag(text, "h1") or "Feynman Reader"
    lang = extract_lang(path, text)
    is_chapter = "/chapters/ch" in path.as_posix()
    label = extract_tag(text, "h1") or re.split(r"\s+-\s+", title, maxsplit=1)[0]
    if noindex:
        description = (
            "Вспомогательная NotebookLM-страница к Feynman Reader; основная индексируемая версия находится на странице главы."
            if lang == "ru"
            else "Auxiliary NotebookLM page for Feynman Reader; the main indexable version is the chapter page."
        )
    else:
        description = page_description(path, label, lang, is_chapter)
    canonical_path = ROOT / "index.html" if path.relative_to(ROOT).as_posix() == "feynman-reader/index.html" else path
    canonical = absolute_url(canonical_path)
    locale = "ru_RU" if lang == "ru" else "en_US"
    og_type = "article" if is_chapter else "website"

    lines = [
        "<!-- BEGIN SEO -->",
        f'<meta name="description" content="{escape(description, quote=True)}">',
    ]
    if noindex:
        lines.append('<meta name="robots" content="noindex, follow">')
    lines.extend(
        [
            f'<link rel="canonical" href="{escape(canonical, quote=True)}">',
            f'<link rel="icon" type="image/png" sizes="192x192" href="{escape(FAVICON_URL, quote=True)}">',
            f'<link rel="apple-touch-icon" href="{escape(APPLE_TOUCH_ICON_URL, quote=True)}">',
            f'<meta property="og:title" content="{escape(title, quote=True)}">',
            f'<meta property="og:description" content="{escape(description, quote=True)}">',
            f'<meta property="og:type" content="{og_type}">',
            f'<meta property="og:url" content="{escape(canonical, quote=True)}">',
            '<meta property="og:site_name" content="Feynman Reader">',
            f'<meta property="og:locale" content="{locale}">',
            '<meta name="twitter:card" content="summary">',
            f'<meta name="twitter:title" content="{escape(title, quote=True)}">',
            f'<meta name="twitter:description" content="{escape(description, quote=True)}">',
        ]
    )

    pair = paired_language_path(path)
    if pair and not noindex:
        pair_lang = "en" if lang == "ru" else "ru"
        lines.append(f'<link rel="alternate" hreflang="{lang}" href="{escape(canonical, quote=True)}">')
        lines.append(f'<link rel="alternate" hreflang="{pair_lang}" href="{escape(absolute_url(pair), quote=True)}">')
        lines.append(f'<link rel="alternate" hreflang="x-default" href="{escape(absolute_url(pair if pair_lang == "en" else path), quote=True)}">')

    if not noindex:
        structured = {
            "@context": "https://schema.org",
            "@type": "Chapter" if is_chapter else "WebPage",
            "name": title,
            "description": description,
            "url": canonical,
            "isPartOf": {
                "@type": "Book",
                "name": "The Feynman Lectures on Physics",
            },
            "inLanguage": lang,
        }
        lines.append('<script type="application/ld+json">')
        lines.append(json.dumps(structured, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/"))
        lines.append("</script>")

    lines.append("<!-- END SEO -->")
    return "\n".join(lines)


def replace_seo_block(text: str, block: str) -> str:
    text = re.sub(r"\n?[ \t]*<!-- BEGIN SEO -->.*?<!-- END SEO -->[ \t]*\n?", "\n", text, flags=re.S)
    title_match = re.search(r"</title>", text, re.I)
    if title_match:
        rest = re.sub(r"^\s*", "\n", text[title_match.end():], count=1)
        return text[: title_match.end()] + "\n" + block + rest
    head_match = re.search(r"</head>", text, re.I)
    if not head_match:
        raise ValueError("missing </head>")
    return text[: head_match.start()] + block + "\n" + text[head_match.start():]


def write_if_changed(path: Path, text: str) -> bool:
    if not path.exists():
        path.write_text(text, encoding="utf-8")
        return True
    old = path.read_text(encoding="utf-8")
    if old == text:
        return False
    path.write_text(text, encoding="utf-8")
    return True


def html_pages() -> list[Path]:
    pages = [ROOT / "index.html", ROOT / "feynman-reader/index.html"]
    pages.extend(sorted((ROOT / "feynman-html-ru").glob("volume-*-reference-guided-inline-svgmath/index.html")))
    pages.extend(sorted((ROOT / "feynman-html-en").glob("volume-*-reference-guided-inline-svgmath/index.html")))
    pages.extend(sorted((ROOT / "feynman-html-ru").glob("volume-*-reference-guided-inline-svgmath/chapters/ch*.html")))
    pages.extend(sorted((ROOT / "feynman-html-en").glob("volume-*-reference-guided-inline-svgmath/chapters/ch*.html")))
    return pages


def report_pages() -> list[Path]:
    return sorted((ROOT / "feynman-html-ru").glob("volume-*-reference-guided-inline-svgmath/chapters/reports/*.html")) + sorted(
        (ROOT / "feynman-html-en").glob("volume-*-reference-guided-inline-svgmath/chapters/reports/*.html")
    )


def sitemap_pages() -> list[Path]:
    pages = [ROOT / "index.html"]
    pages.extend(sorted((ROOT / "feynman-html-ru").glob("volume-*-reference-guided-inline-svgmath/index.html")))
    pages.extend(sorted((ROOT / "feynman-html-en").glob("volume-*-reference-guided-inline-svgmath/index.html")))
    pages.extend(sorted((ROOT / "feynman-html-ru").glob("volume-*-reference-guided-inline-svgmath/chapters/ch*.html")))
    pages.extend(sorted((ROOT / "feynman-html-en").glob("volume-*-reference-guided-inline-svgmath/chapters/ch*.html")))
    return pages


def build_sitemap(pages: list[Path]) -> str:
    urls = []
    for path in pages:
        loc = absolute_url(path)
        priority = "1.0" if path == ROOT / "index.html" else "0.8" if path.name == "index.html" else "0.6"
        urls.append(
            "  <url>\n"
            f"    <loc>{escape(loc)}</loc>\n"
            f"    <lastmod>{TODAY}</lastmod>\n"
            f"    <priority>{priority}</priority>\n"
            "  </url>"
        )
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"


def main() -> None:
    changed = 0
    for path in html_pages():
        text = path.read_text(encoding="utf-8")
        if write_if_changed(path, replace_seo_block(text, seo_block(path, text))):
            changed += 1

    for path in report_pages():
        text = path.read_text(encoding="utf-8")
        if write_if_changed(path, replace_seo_block(text, seo_block(path, text, noindex=True))):
            changed += 1

    robots = (
        "User-agent: *\n"
        "Allow: /\n\n"
        f"Sitemap: {BASE_URL}sitemap.xml\n"
    )
    if write_if_changed(ROOT / "robots.txt", robots):
        changed += 1

    sitemap = build_sitemap(sitemap_pages())
    if write_if_changed(ROOT / "sitemap.xml", sitemap):
        changed += 1

    print(f"SEO metadata applied: changed={changed}, sitemap_urls={len(sitemap_pages())}, reports_noindex={len(report_pages())}")


if __name__ == "__main__":
    main()
