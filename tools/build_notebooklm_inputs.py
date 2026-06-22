#!/usr/bin/env python3
"""Build local NotebookLM source packages from generated chapter HTML."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
VOLUME_NAMES = {"I": "I", "II": "II", "III": "III"}


@dataclass
class Node:
    tag: str
    attrs: dict[str, str] = field(default_factory=dict)
    children: list["Node | str"] = field(default_factory=list)


@dataclass
class Block:
    kind: str
    text: str
    block_id: str | None = None
    level: int | None = None
    path: str | None = None


class ArticleParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root: Node | None = None
        self.stack: list[Node] = []
        self.in_article = False
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k: v or "" for k, v in attrs}
        classes = set(attrs_dict.get("class", "").split())

        if self.skip_depth:
            if tag not in VOID_TAGS:
                self.skip_depth += 1
            return

        if tag == "article" and "chapter-flow" in classes:
            self.root = Node(tag, attrs_dict)
            self.stack = [self.root]
            self.in_article = True
            return

        if not self.in_article:
            return

        if tag in {"script", "style"}:
            self.skip_depth = 1
            return

        node = Node(tag, attrs_dict)
        self.stack[-1].children.append(node)

        if tag == "svg" and "math-svg" in classes:
            self.skip_depth = 1
            return

        if tag not in VOID_TAGS:
            self.stack.append(node)

    def handle_endtag(self, tag: str) -> None:
        if self.skip_depth:
            self.skip_depth -= 1
            return
        if not self.in_article:
            return
        while len(self.stack) > 1:
            node = self.stack.pop()
            if node.tag == tag:
                break
        if tag == "article":
            self.in_article = False
            self.stack = []

    def handle_data(self, data: str) -> None:
        if self.in_article and not self.skip_depth and self.stack:
            self.stack[-1].children.append(data)


def norm_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def clean_heading(value: str) -> str:
    return norm_space(value.replace("#", ""))


def chapter_title(title: str, chapter: int) -> str:
    title = re.sub(rf"^\s*{chapter}\s*[\.\-:]\s*", "", title).strip()
    return f"Chapter {chapter}. {title}" if title else f"Chapter {chapter}"


def has_class(node: Node, name: str) -> bool:
    return name in node.attrs.get("class", "").split()


def text_of(node: Node | str) -> str:
    if isinstance(node, str):
        return node
    if has_class(node, "permalink") or has_class(node, "math-copy-fallback"):
        return ""
    if node.tag == "svg" and has_class(node, "math-svg"):
        return node.attrs.get("data-tex") or node.attrs.get("aria-label", "")
    if node.tag == "img":
        return node.attrs.get("alt", "")
    if node.tag == "br":
        return "\n"
    pieces = [text_of(child) for child in node.children]
    return " ".join(piece for piece in pieces if piece)


def markdown_escape_table_cell(value: str) -> str:
    return norm_space(value).replace("|", "\\|")


def table_markdown(table_node: Node) -> str:
    rows: list[list[str]] = []
    for tr in walk_tags(table_node, {"tr"}):
        cells = [markdown_escape_table_cell(text_of(cell)) for cell in tr.children if isinstance(cell, Node) and cell.tag in {"th", "td"}]
        if cells:
            rows.append(cells)
    if not rows:
        return norm_space(text_of(table_node))
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    lines = ["| " + " | ".join(rows[0]) + " |", "| " + " | ".join(["---"] * width) + " |"]
    for row in rows[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def walk_tags(node: Node, tags: set[str]) -> Iterable[Node]:
    for child in node.children:
        if isinstance(child, Node):
            if child.tag in tags:
                yield child
            yield from walk_tags(child, tags)


def direct_tag(node: Node, tag: str) -> Node | None:
    for child in node.children:
        if isinstance(child, Node) and child.tag == tag:
            return child
    return None


def find_first(node: Node, predicate) -> Node | None:
    if predicate(node):
        return node
    for child in node.children:
        if isinstance(child, Node):
            found = find_first(child, predicate)
            if found:
                return found
    return None


def figure_record(node: Node, html_chapter_dir: Path, out_dir: Path) -> tuple[Block, dict[str, str]]:
    fig_id = node.attrs.get("id", "figure")
    image = find_first(node, lambda item: item.tag == "img")
    caption_node = find_first(node, lambda item: item.tag == "figcaption")
    caption = norm_space(text_of(caption_node)) if caption_node else norm_space(image.attrs.get("alt", "") if image else "")
    src = image.attrs.get("src", "") if image else ""
    local_name = Path(src).name if src else ""
    local_path = f"figures/{local_name}" if local_name else ""

    if src and local_name:
        source = (html_chapter_dir / src).resolve()
        target = out_dir / local_path
        if source.exists():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    lines = [f"### Figure {fig_id}", f"Caption: {caption}"]
    if local_path:
        lines.extend([f"Image: {local_path}", f"![{caption}]({local_path})"])
    block = Block("figure", "\n".join(lines), fig_id, path=local_path)
    record = {"id": fig_id, "caption": caption, "image": local_path}
    return block, record


def linear_blocks(article: Node, html_chapter_dir: Path, out_dir: Path) -> tuple[list[Block], list[dict[str, str]]]:
    blocks: list[Block] = []
    figures: list[dict[str, str]] = []

    for child in article.children:
        if not isinstance(child, Node):
            continue
        if child.tag in {"h1", "h2", "h3", "h4"}:
            level = int(child.tag[1])
            blocks.append(Block("heading", clean_heading(text_of(child)), child.attrs.get("id"), level=level))
        elif child.tag == "p":
            text = norm_space(text_of(child))
            if text:
                blocks.append(Block("paragraph", text))
        elif child.tag in {"ul", "ol"}:
            for li in walk_tags(child, {"li"}):
                text = norm_space(text_of(li))
                if text:
                    blocks.append(Block("list_item", f"- {text}"))
        elif child.tag == "figure" and has_class(child, "flp-figure"):
            block, record = figure_record(child, html_chapter_dir, out_dir)
            blocks.append(block)
            figures.append(record)
        elif child.tag == "figure" and has_class(child, "source-table"):
            text = table_markdown(child)
            if text:
                blocks.append(Block("table", text, child.attrs.get("id")))
        elif child.tag == "table":
            text = table_markdown(child)
            if text:
                blocks.append(Block("table", text, child.attrs.get("id")))
        else:
            text = norm_space(text_of(child))
            if text:
                blocks.append(Block(child.tag, text, child.attrs.get("id")))
    return blocks, figures


def markdown_from_blocks(blocks: list[Block]) -> str:
    lines: list[str] = []
    for block in blocks:
        if block.kind == "heading":
            level = block.level or 2
            lines.append(f"{'#' * level} {block.text}")
        else:
            lines.append(block.text)
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def notebook_text(header: str, blocks: list[Block]) -> str:
    lines = [header.rstrip(), ""]
    for block in blocks:
        if block.kind == "heading":
            lines.append(block.text.upper() if block.level == 1 else block.text)
        elif block.kind == "figure":
            parts = block.text.splitlines()
            lines.append(parts[0].replace("### Figure", "FIGURE"))
            for part in parts[1:3]:
                lines.append(part.replace("Image:", "Image file:"))
        else:
            lines.append(block.text)
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def sections_from_blocks(blocks: list[Block]) -> dict[str, list[Block]]:
    sections: dict[str, list[Block]] = {}
    current_id = "intro"
    sections[current_id] = []
    for block in blocks:
        if block.kind == "heading" and block.level == 2:
            current_id = block.block_id or slugify(block.text)
            sections.setdefault(current_id, [block])
        else:
            sections.setdefault(current_id, []).append(block)
    return {key: value for key, value in sections.items() if value}


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.lower()).strip("-")
    return slug or "section"


def chapter_number(path: Path) -> int:
    match = re.search(r"ch(\d+)\.html$", path.name)
    if not match:
        raise ValueError(f"Cannot parse chapter number from {path}")
    return int(match.group(1))


def source_url(volume: str, chapter: int) -> str:
    return f"https://www.feynmanlectures.caltech.edu/{volume}_{chapter:02d}.html"


def report_pages(language: str, volume: str, chapter: int) -> dict[str, str]:
    ch = f"ch{chapter:02d}"
    base = f"feynman-html-{language}/volume-{volume}-reference-guided-inline-svgmath/chapters/reports"
    return {
        "briefing_html": f"{base}/{ch}-notebooklm-briefing.html",
        "study_guide_html": f"{base}/{ch}-notebooklm-study-guide.html",
    }


def build_chapter(language: str, volume: str, html_path: Path, output_root: Path, overwrite: bool) -> dict[str, object]:
    chapter = chapter_number(html_path)
    ch = f"ch{chapter:02d}"
    out_dir = output_root / language / f"volume-{volume}" / ch
    if out_dir.exists() and not overwrite:
        return {"chapter": chapter, "status": "skipped", "reason": "exists", "path": str(out_dir)}

    parser = ArticleParser()
    parser.feed(html_path.read_text(encoding="utf-8"))
    if not parser.root:
        raise RuntimeError(f"No article.chapter-flow found in {html_path}")

    if out_dir.exists() and overwrite:
        shutil.rmtree(out_dir)
    for subdir in ("figures", "sections", "figure-context", "reports"):
        (out_dir / subdir).mkdir(parents=True, exist_ok=True)

    blocks, figures = linear_blocks(parser.root, html_path.parent, out_dir)
    title_block = next((block for block in blocks if block.kind == "heading" and block.level == 1), None)
    title = title_block.text if title_block else f"Chapter {chapter}"
    full_title = title if title.lower().startswith("chapter") else chapter_title(title, chapter)
    header = "\n".join(
        [
            f"SOURCE: Feynman Lectures on Physics, Volume {volume}, Chapter {chapter}",
            f"LANGUAGE: {language}",
            f"TITLE: {full_title}",
            f"SOURCE_URL: {source_url(volume, chapter)}",
            "NOTEBOOKLM_USE: clean lecture text with TeX math and figure captions; reader navigation removed.",
        ]
    )

    (out_dir / f"{ch}-full.md").write_text(markdown_from_blocks(blocks), encoding="utf-8")
    (out_dir / f"{ch}-notebooklm.txt").write_text(notebook_text(header, blocks), encoding="utf-8")

    with (out_dir / "blocks.jsonl").open("w", encoding="utf-8") as handle:
        for index, block in enumerate(blocks, 1):
            handle.write(json.dumps({"index": index, **block.__dict__}, ensure_ascii=False) + "\n")

    sections = sections_from_blocks(blocks)
    with (out_dir / "chunks.jsonl").open("w", encoding="utf-8") as handle:
        for index, (section_id, section_blocks) in enumerate(sections.items(), 1):
            text = markdown_from_blocks(section_blocks)
            handle.write(json.dumps({"index": index, "id": section_id, "text": text}, ensure_ascii=False) + "\n")
            (out_dir / "sections" / f"{section_id}.md").write_text(text, encoding="utf-8")
            (out_dir / "sections" / f"{section_id}.txt").write_text(re.sub(r"^#+\s*", "", text, flags=re.M), encoding="utf-8")

    figure_context = {
        "language": language,
        "volume": volume,
        "chapter": chapter,
        "figures": figures,
    }
    (out_dir / "figure-context" / f"{ch}-figures-context.json").write_text(json.dumps(figure_context, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    context_md = [f"# Figure context for Volume {volume}, Chapter {chapter}", ""]
    for figure in figures:
        context_md.extend([f"## {figure['id']}", f"Caption: {figure['caption']}", f"Image: {figure['image']}", ""])
    (out_dir / "figure-context" / f"{ch}-figures-context.md").write_text("\n".join(context_md).strip() + "\n", encoding="utf-8")
    (out_dir / "figure-context" / "manifest.json").write_text(json.dumps(figure_context, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out_dir / "reports" / "html-report-pages.json").write_text(json.dumps(report_pages(language, volume, chapter), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    tex_formulas = len(re.findall(r'class="[^"]*math-svg[^"]*"', html_path.read_text(encoding="utf-8")))
    manifest = {
        "language": language,
        "volume": volume,
        "chapter": chapter,
        "title": full_title,
        "source_html": str(html_path),
        "source_url": source_url(volume, chapter),
        "outputs": {
            "markdown": f"{ch}-full.md",
            "paste_text": f"{ch}-notebooklm.txt",
            "blocks_jsonl": "blocks.jsonl",
            "chunks_jsonl": "chunks.jsonl",
            "figures_dir": "figures",
            "sections_dir": "sections",
        },
        "counts": {
            "blocks": len(blocks),
            "chunks": len(sections),
            "figures": len(figures),
            "tables": sum(1 for block in blocks if block.kind == "table"),
            "tex_formulas": tex_formulas,
        },
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"chapter": chapter, "status": "built", "path": str(out_dir), "counts": manifest["counts"]}


def volume_html_dir(language: str, volume: str) -> Path:
    return ROOT / f"feynman-html-{language}" / f"volume-{volume}-reference-guided-inline-svgmath" / "chapters"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--language", default="en")
    parser.add_argument("--volumes", nargs="+", choices=sorted(VOLUME_NAMES), required=True)
    parser.add_argument("--output-root", type=Path, default=ROOT / "feynman-notebooklm")
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--write-queue", action="store_true", help="Write upload queue files for the selected volumes.")
    args = parser.parse_args()

    results = []
    for volume in args.volumes:
        html_dir = volume_html_dir(args.language, volume)
        chapters = sorted(html_dir.glob("ch*.html"))
        if not chapters:
            raise SystemExit(f"No chapter HTML files found in {html_dir}")
        for html_path in chapters:
            results.append(build_chapter(args.language, volume, html_path, args.output_root, args.overwrite))

    queue_paths: dict[str, str] = {}
    if args.write_queue:
        queue_paths = write_upload_queue(args.language, args.volumes, args.output_root)

    built = sum(1 for item in results if item["status"] == "built")
    skipped = sum(1 for item in results if item["status"] == "skipped")
    print(json.dumps({"built": built, "skipped": skipped, "queue": queue_paths, "results": results}, ensure_ascii=False, indent=2))
    return 0


def write_upload_queue(language: str, volumes: list[str], output_root: Path) -> dict[str, str]:
    language_root = output_root / language
    rows: list[dict[str, object]] = []
    for volume in volumes:
        for chapter_dir in sorted((language_root / f"volume-{volume}").glob("ch*")):
            if not chapter_dir.is_dir():
                continue
            manifest_path = chapter_dir / "manifest.json"
            if not manifest_path.exists():
                continue
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            chapter = int(manifest["chapter"])
            ch = f"ch{chapter:02d}"
            rows.append(
                {
                    "language": language,
                    "volume": volume,
                    "chapter": chapter,
                    "title": manifest["title"],
                    "notebooklm_text": str(chapter_dir / f"{ch}-notebooklm.txt"),
                    "full_markdown": str(chapter_dir / f"{ch}-full.md"),
                    "figures": manifest["counts"]["figures"],
                    "sections": manifest["counts"]["chunks"],
                }
            )

    queue_base = language_root / ("notebooklm-upload-queue-" + "-".join(volumes))
    json_path = queue_base.with_suffix(".json")
    tsv_path = queue_base.with_suffix(".tsv")
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    columns = ["language", "volume", "chapter", "title", "notebooklm_text", "full_markdown", "figures", "sections"]
    tsv_lines = ["\t".join(columns)]
    for row in rows:
        tsv_lines.append("\t".join(str(row[column]).replace("\t", " ") for column in columns))
    tsv_path.write_text("\n".join(tsv_lines) + "\n", encoding="utf-8")
    return {"json": str(json_path), "tsv": str(tsv_path), "items": str(len(rows))}


if __name__ == "__main__":
    raise SystemExit(main())
