#!/usr/bin/env python3
"""Give NotebookLM report pages the same reader navigation shell."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from reader_site import ROOT, write_if_changed


REPORT_RE = re.compile(
    r"<main class=\"notebooklm-report-shell\">\s*"
    r"<nav class=\"notebooklm-report-nav\">.*?</nav>\s*"
    r"<article class=\"notebooklm-report\">",
    re.S,
)


def report_pages() -> list[Path]:
    pages: list[Path] = []
    for language_dir in ("feynman-html-ru", "feynman-html-en"):
        pages.extend(sorted((ROOT / language_dir).glob("volume-*-reference-guided-inline-svgmath/chapters/reports/*notebooklm-*.html")))
    return pages


def labels(language: str, report_kind: str) -> dict[str, str]:
    if language == "ru":
        return {
            "aria": "Быстрая навигация",
            "back": "Назад к главе",
            "reader": "Учебник",
            "contents": "Оглавление",
            "theme": "Сменить тему",
            "title": f"NotebookLM · {'Конспект' if report_kind == 'study-guide' else 'Обзор'}",
        }
    return {
        "aria": "Quick navigation",
        "back": "Back to chapter",
        "reader": "Reader",
        "contents": "Contents",
        "theme": "Toggle theme",
        "title": f"NotebookLM · {'Guide' if report_kind == 'study-guide' else 'Overview'}",
    }


def toolbar_html(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    language = "ru" if rel.startswith("feynman-html-ru/") else "en"
    chapter_match = re.search(r"/ch(\d+)-notebooklm-", rel)
    if not chapter_match:
        raise ValueError(f"Cannot infer chapter from {rel}")
    chapter = chapter_match.group(1)
    report_kind = "study-guide" if "study-guide" in path.name else "briefing"
    text = labels(language, report_kind)
    chapter_href = f"../ch{chapter}.html"
    chapter_anchor = f"{chapter_href}#ch{chapter}"
    return (
        '<main class="notebooklm-report-shell">\n'
        f'    <header aria-label="{text["aria"]}" class="reader-toolbar report-toolbar">\n'
        '      <div class="toolbar-group toolbar-navigation">\n'
        f'        <a class="toolbar-btn" href="{chapter_href}">{text["back"]}</a>\n'
        f'        <a class="toolbar-btn" href="../../../../feynman-reader/index.html">{text["reader"]}</a>\n'
        f'        <a class="toolbar-btn" href="../../index.html">{text["contents"]}</a>\n'
        '      </div>\n'
        f'      <a class="toolbar-title" href="{chapter_anchor}" title="{text["title"]}">{text["title"]}</a>\n'
        '      <div class="toolbar-group toolbar-settings">\n'
        f'        <button aria-label="{text["theme"]}" class="toolbar-btn icon-btn" data-report-action="theme" title="{text["theme"]}" type="button">◐</button>\n'
        '      </div>\n'
        '    </header>\n'
        '    <article class="notebooklm-report">'
    )


def update_theme_script(html: str) -> str:
    new = (
        '  <script>\n'
        '    (() => {\n'
        '      const key = "flp-reader-theme";\n'
        '      const applyTheme = (theme) => {\n'
        '        const next = theme === "dark" ? "dark" : "light";\n'
        '        document.documentElement.dataset.theme = next;\n'
        '        document.body.dataset.theme = next;\n'
        '        try { localStorage.setItem(key, next); } catch (_) {}\n'
        '      };\n'
        '      try { applyTheme(localStorage.getItem(key) || "light"); } catch (_) { applyTheme("light"); }\n'
        '      document.addEventListener("click", (event) => {\n'
        '        const button = event.target.closest(\'[data-report-action="theme"]\');\n'
        '        if (!button) return;\n'
        '        applyTheme(document.documentElement.dataset.theme === "dark" ? "light" : "dark");\n'
        '      });\n'
        '    })();\n'
        '  </script>'
    )
    if 'document.documentElement.dataset.theme = next;' in html:
        return html
    html, count = re.subn(r"\s*<script>\s*try\s*\{.*?flp-reader-theme.*?</script>\s*", "\n" + new + "\n", html, count=1, flags=re.S)
    if count != 1:
        raise ValueError("Expected report theme script was not found")
    return html


def update_page(path: Path) -> bool:
    html = path.read_text(encoding="utf-8")
    html = update_theme_script(html)
    if 'class="reader-toolbar report-toolbar"' not in html:
        html, count = REPORT_RE.subn(toolbar_html(path), html, count=1)
        if count != 1:
            raise ValueError(f"Expected one report nav in {path.relative_to(ROOT)}")
    html = re.sub(r'href="(\.\./ch\d+\.html)#study-panel"', r'href="\1"', html)
    return write_if_changed(path, html)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    changed: list[Path] = []
    for path in report_pages():
        original = path.read_text(encoding="utf-8")
        update_page(path)
        updated = path.read_text(encoding="utf-8")
        if updated != original:
            changed.append(path)
            if args.check:
                path.write_text(original, encoding="utf-8")

    if args.check and changed:
        print(f"would update {len(changed)} report files")
        return 1
    print(f"updated {len(changed)} report files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
