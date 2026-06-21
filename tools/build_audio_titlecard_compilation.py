#!/usr/bin/env python3
"""Build audio compilation videos with per-chapter title cards."""

from __future__ import annotations

import argparse
import html
import json
import math
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1920
HEIGHT = 1080
FPS = "1"
BG = (17, 24, 39)
ACCENT = (56, 189, 248)
TEXT = (248, 250, 252)
MUTED = (203, 213, 225)
LINE = (71, 85, 105)


@dataclass(frozen=True)
class Chapter:
    number: int
    title: str
    audio: Path
    duration: float


def run_json(cmd: list[str]) -> dict:
    return json.loads(subprocess.check_output(cmd, text=True))


def duration(path: Path) -> float:
    data = run_json(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(path)])
    return float(data["format"]["duration"])


def run(cmd: list[str]) -> None:
    print("+ " + " ".join(quote(arg) for arg in cmd), flush=True)
    subprocess.run(cmd, check=True)


def quote(value: str) -> str:
    if re.fullmatch(r"[A-Za-z0-9_./:@%+=,-]+", value):
        return value
    return "'" + value.replace("'", "'\"'\"'") + "'"


def parse_titles(index: Path) -> dict[int, str]:
    text = index.read_text(encoding="utf-8")
    titles: dict[int, str] = {}
    pattern = re.compile(r'<a\s+class="chapter-list-title"\s+href="chapters/ch(\d{2})\.html"[^>]*>(.*?)</a>', re.S)
    for match in pattern.finditer(text):
        number = int(match.group(1))
        title = re.sub(r"<[^>]+>", "", match.group(2))
        titles[number] = html.unescape(" ".join(title.split()))
    if not titles:
        raise SystemExit(f"No chapter titles found in {index}")
    return titles


def collect_chapters(root: Path, index: Path, start: int, end: int) -> list[Chapter]:
    titles = parse_titles(index)
    chapters: list[Chapter] = []
    for number in range(start, end + 1):
        audio = root / f"ch{number:02d}-notebooklm-audio-deep-dive.mp3"
        if not audio.exists():
            raise SystemExit(f"Missing audio for chapter {number}: {audio}")
        title = titles.get(number)
        if not title:
            raise SystemExit(f"Missing title for chapter {number} in {index}")
        chapters.append(Chapter(number=number, title=title, audio=audio, duration=duration(audio)))
    return chapters


def load_font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Unicode.ttf",
        "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size=size)
        except OSError:
            continue
    return ImageFont.load_default(size=size)


def wrap_to_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.splitlines():
        words = paragraph.split()
        line = ""
        for word in words:
            candidate = f"{line} {word}".strip()
            if draw.textbbox((0, 0), candidate, font=font)[2] <= max_width:
                line = candidate
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
    return lines or [text]


def centered_text(
    draw: ImageDraw.ImageDraw,
    y: int,
    lines: Iterable[str],
    font: ImageFont.ImageFont,
    fill: tuple[int, int, int],
    line_gap: int,
) -> int:
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        draw.text(((WIDTH - width) / 2, y), line, font=font, fill=fill)
        y += height + line_gap
    return y


def write_card(chapter: Chapter, path: Path, volume_label: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)

    title_font = load_font(74, bold=True)
    chapter_font = load_font(48, bold=True)
    meta_font = load_font(32)
    small_font = load_font(26)

    draw.rounded_rectangle((180, 150, WIDTH - 180, HEIGHT - 150), radius=42, outline=LINE, width=3)
    draw.rectangle((180, 150, WIDTH - 180, 164), fill=ACCENT)

    centered_text(draw, 250, ["Фейнмановские лекции по физике"], chapter_font, MUTED, 18)
    centered_text(draw, 350, [volume_label], meta_font, ACCENT, 10)
    centered_text(draw, 430, [f"Глава {chapter.number}"], chapter_font, TEXT, 16)

    title_lines = wrap_to_width(draw, chapter.title, title_font, 1350)
    if len(title_lines) > 3:
        title_font = load_font(62, bold=True)
        title_lines = wrap_to_width(draw, chapter.title, title_font, 1380)
    block_height = sum(draw.textbbox((0, 0), line, font=title_font)[3] for line in title_lines)
    block_height += max(0, len(title_lines) - 1) * 18
    centered_text(draw, max(520, 610 - block_height // 2), title_lines, title_font, TEXT, 18)

    minutes = math.ceil(chapter.duration / 60)
    footer = f"NotebookLM audio overview · {minutes} min"
    centered_text(draw, 830, [footer], small_font, MUTED, 10)
    image.save(path)


def fmt_time(seconds: float) -> str:
    value = int(seconds)
    hours, rem = divmod(value, 3600)
    minutes, secs = divmod(rem, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def render_segment(card: Path, audio: Path, output: Path, seconds: float, overwrite: bool) -> None:
    if output.exists() and not overwrite:
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["ffmpeg", "-y" if overwrite else "-n"]
    cmd += [
        "-loop",
        "1",
        "-framerate",
        FPS,
        "-i",
        str(card),
        "-i",
        str(audio),
        "-t",
        f"{seconds:.3f}",
        "-map",
        "0:v:0",
        "-map",
        "1:a:0",
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-tune",
        "stillimage",
        "-r",
        FPS,
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-pix_fmt",
        "yuv420p",
        "-shortest",
        str(output),
    ]
    run(cmd)


def concat_segments(list_path: Path, output: Path, overwrite: bool) -> None:
    cmd = ["ffmpeg", "-y" if overwrite else "-n"]
    cmd += [
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(list_path),
        "-c",
        "copy",
        "-movflags",
        "+faststart",
        str(output),
    ]
    run(cmd)


def write_outputs(out_dir: Path, slug: str, part_label: str, chapters: list[Chapter]) -> tuple[Path, Path, Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    concat_path = out_dir / f"{slug}.concat.txt"
    desc_path = out_dir / f"{slug}.description.txt"
    starts_path = out_dir / f"{slug}.starts.json"
    video_path = out_dir / f"{slug}.mp4"

    cursor = 0.0
    starts = []
    desc_lines = [
        f"Feynman Reader RU Volume I — NotebookLM Audio, {part_label}",
        "",
        "Chapters:",
    ]
    concat_lines = []
    for chapter in chapters:
        segment = out_dir / "segments" / f"ch{chapter.number:02d}.mp4"
        start = int(cursor)
        starts.append(
            {
                "chapter": chapter.number,
                "title": chapter.title,
                "start": start,
                "duration": chapter.duration,
                "segment": str(segment),
            }
        )
        desc_lines.append(f"{fmt_time(cursor)} Глава {chapter.number}. {chapter.title}")
        segment_path = str(segment.resolve()).replace("'", "'\\''")
        concat_lines.append(f"file '{segment_path}'")
        cursor += chapter.duration

    desc_lines += [
        "",
        "Audio overview generated from NotebookLM notes for Feynman Reader.",
    ]
    concat_path.write_text("\n".join(concat_lines) + "\n", encoding="utf-8")
    desc_path.write_text("\n".join(desc_lines) + "\n", encoding="utf-8")
    starts_path.write_text(json.dumps(starts, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return concat_path, desc_path, starts_path, video_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--media-root", type=Path, required=True)
    parser.add_argument("--index", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=Path("local-media/volume-I/youtube-audio-titlecards"))
    parser.add_argument("--slug", required=True)
    parser.add_argument("--part-label", required=True)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--end", type=int, required=True)
    parser.add_argument("--volume-label", default="Том I")
    parser.add_argument("--render", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    chapters = collect_chapters(args.media_root, args.index, args.start, args.end)
    card_dir = args.out_dir / "cards"
    segment_dir = args.out_dir / "segments"
    for chapter in chapters:
        card = card_dir / f"ch{chapter.number:02d}.png"
        write_card(chapter, card, args.volume_label)
        if args.render:
            segment = segment_dir / f"ch{chapter.number:02d}.mp4"
            render_segment(card, chapter.audio, segment, chapter.duration, args.overwrite)

    concat_path, desc_path, starts_path, video_path = write_outputs(args.out_dir, args.slug, args.part_label, chapters)
    total = sum(chapter.duration for chapter in chapters)
    print(f"chapters={len(chapters)} duration={fmt_time(total)}")
    print(f"concat={concat_path}")
    print(f"description={desc_path}")
    print(f"starts={starts_path}")
    print(f"video={video_path}")
    if args.render:
        concat_segments(concat_path, video_path, args.overwrite)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
