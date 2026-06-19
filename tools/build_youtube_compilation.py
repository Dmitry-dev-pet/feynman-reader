#!/usr/bin/env python3
"""Build long YouTube compilation videos with chapter timecodes."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List


DEFAULT_MAX_SECONDS = 11 * 3600 + 50 * 60


@dataclass
class AudioItem:
    path: Path
    duration: float


def run_json(cmd: List[str]) -> dict:
    return json.loads(subprocess.check_output(cmd, text=True))


def duration(path: Path) -> float:
    data = run_json(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", str(path)])
    return float(data["format"]["duration"])


def natural_key(path: Path) -> tuple[int, int, str]:
    match = re.search(r"ch(\d+)", path.name)
    chapter = int(match.group(1)) if match else 999
    # Keep the short ch01 audio before the longer deep dive when both exist.
    variant = 0 if path.name.endswith("notebooklm-audio.mp3") else 1
    return chapter, variant, path.name


def collect(root: Path) -> List[AudioItem]:
    files = sorted(root.glob("*.mp3"), key=natural_key)
    return [AudioItem(path=file, duration=duration(file)) for file in files]


def split_parts(items: Iterable[AudioItem], max_seconds: float) -> List[List[AudioItem]]:
    parts: List[List[AudioItem]] = []
    current: List[AudioItem] = []
    total = 0.0
    for item in items:
        if current and total + item.duration > max_seconds:
            parts.append(current)
            current = []
            total = 0.0
        current.append(item)
        total += item.duration
    if current:
        parts.append(current)
    return parts


def fmt_time(seconds: float) -> str:
    value = int(seconds)
    hours, rem = divmod(value, 3600)
    minutes, secs = divmod(rem, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def chapter_label(path: Path) -> str:
    stem = path.stem
    stem = stem.replace("-notebooklm-audio-deep-dive", " deep dive")
    stem = stem.replace("-notebooklm-audio", " short audio")
    return stem


def quote_concat_path(path: Path) -> str:
    return str(path).replace("'", "'\\''")


def write_part_files(
    out_dir: Path,
    slug: str,
    title: str,
    part_index: int,
    total_parts: int,
    items: List[AudioItem],
) -> tuple[Path, Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    base = out_dir / f"{slug}-part-{part_index:02d}"
    list_path = base.with_suffix(".concat.txt")
    desc_path = base.with_suffix(".description.txt")
    video_path = base.with_suffix(".mp4")

    list_path.write_text("".join(f"file '{quote_concat_path(item.path)}'\n" for item in items), encoding="utf-8")

    cursor = 0.0
    lines = [f"{title} - Part {part_index}/{total_parts}", "", "Chapters:"]
    for item in items:
        lines.append(f"{fmt_time(cursor)} {chapter_label(item.path)}")
        cursor += item.duration
    lines += ["", "Uploaded as private archive media for Feynman Reader."]
    desc_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return list_path, desc_path, video_path


def render(list_path: Path, video_path: Path, overwrite: bool) -> None:
    cmd = ["ffmpeg"]
    cmd.append("-y" if overwrite else "-n")
    cmd += [
        "-f",
        "lavfi",
        "-i",
        "color=c=0x111827:s=1920x1080:r=1",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(list_path),
        "-map",
        "0:v",
        "-map",
        "1:a",
        "-c:v",
        "libx264",
        "-tune",
        "stillimage",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-pix_fmt",
        "yuv420p",
        "-shortest",
        "-movflags",
        "+faststart",
        str(video_path),
    ]
    print("+ " + " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--out-dir", type=Path, default=Path("youtube-compilations"))
    parser.add_argument("--max-seconds", type=float, default=DEFAULT_MAX_SECONDS)
    parser.add_argument("--render", action="store_true")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    items = collect(args.root)
    if not items:
        raise SystemExit(f"No mp3 files found in {args.root}")
    parts = split_parts(items, args.max_seconds)
    print(f"items={len(items)} parts={len(parts)} total_hours={sum(item.duration for item in items) / 3600:.2f}")
    for index, part in enumerate(parts, 1):
        part_seconds = sum(item.duration for item in part)
        list_path, desc_path, video_path = write_part_files(args.out_dir, args.slug, args.title, index, len(parts), part)
        print(f"part={index} files={len(part)} duration={fmt_time(part_seconds)} list={list_path} desc={desc_path} video={video_path}")
        if args.render:
            render(list_path, video_path, args.overwrite)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
