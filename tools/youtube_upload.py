#!/usr/bin/env python3
"""Prepare and optionally upload Feynman Reader audio to YouTube.

This script keeps generated media and OAuth tokens local. Use `render` to turn
an MP3 into a YouTube-compatible MP4, or `batch` to process a directory of MP3s.
Add `--upload` only when you are ready to authenticate with YouTube Data API.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
DEFAULT_COLOR = "0x111827"
DEFAULT_SIZE = "1920x1080"
DEFAULT_FPS = "1"


def run(cmd: List[str], *, dry_run: bool = False) -> None:
    print("+ " + " ".join(shell_quote(part) for part in cmd))
    if dry_run:
        return
    subprocess.run(cmd, check=True)


def shell_quote(value: str) -> str:
    if not value:
        return "''"
    safe = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_+-=.,/:@%"
    if all(ch in safe for ch in value):
        return value
    return "'" + value.replace("'", "'\"'\"'") + "'"


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def render_video(
    audio: Path,
    output: Path,
    *,
    cover: Optional[Path],
    overwrite: bool,
    dry_run: bool,
    audio_bitrate: str,
) -> None:
    if not audio.exists():
        raise SystemExit(f"Audio file not found: {audio}")
    if output.exists() and not overwrite:
        print(f"Video already exists, skipping: {output}")
        return

    ensure_parent(output)
    cmd = ["ffmpeg"]
    if overwrite:
        cmd.append("-y")
    else:
        cmd.append("-n")

    if cover:
        if not cover.exists():
            raise SystemExit(f"Cover image not found: {cover}")
        cmd += ["-loop", "1", "-framerate", DEFAULT_FPS, "-i", str(cover)]
    else:
        cmd += ["-f", "lavfi", "-i", f"color=c={DEFAULT_COLOR}:s={DEFAULT_SIZE}:r={DEFAULT_FPS}"]

    cmd += [
        "-i",
        str(audio),
        "-c:v",
        "libx264",
        "-tune",
        "stillimage",
        "-c:a",
        "aac",
        "-b:a",
        audio_bitrate,
        "-pix_fmt",
        "yuv420p",
        "-shortest",
        "-movflags",
        "+faststart",
        str(output),
    ]
    run(cmd, dry_run=dry_run)


def missing_google_deps() -> None:
    raise SystemExit(
        "Missing YouTube API dependencies. Install them locally with:\n"
        "  python3 -m pip install -r tools/youtube-upload-requirements.txt"
    )


def load_youtube_client(client_secrets: Path, token_file: Path) -> Any:
    try:
        from google.auth.transport.requests import Request
        from google.oauth2.credentials import Credentials
        from google_auth_oauthlib.flow import InstalledAppFlow
        from googleapiclient.discovery import build
    except ImportError:
        missing_google_deps()

    creds = None
    if token_file.exists():
        creds = Credentials.from_authorized_user_file(str(token_file), SCOPES)

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    if not creds or not creds.valid:
        if not client_secrets.exists():
            raise SystemExit(f"YouTube client secrets file not found: {client_secrets}")
        flow = InstalledAppFlow.from_client_secrets_file(str(client_secrets), SCOPES)
        creds = flow.run_local_server(port=0)

    ensure_parent(token_file)
    token_file.write_text(creds.to_json(), encoding="utf-8")
    return build("youtube", "v3", credentials=creds)


def upload_video(
    youtube: Any,
    video_file: Path,
    *,
    title: str,
    description: str,
    privacy: str,
    category: str,
    tags: Iterable[str],
) -> Dict[str, Any]:
    try:
        from googleapiclient.errors import HttpError
        from googleapiclient.http import MediaFileUpload
    except ImportError:
        missing_google_deps()

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "categoryId": category,
            "tags": [tag for tag in tags if tag],
        },
        "status": {
            "privacyStatus": privacy,
            "selfDeclaredMadeForKids": False,
        },
    }
    media = MediaFileUpload(str(video_file), chunksize=-1, resumable=True)
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

    response = None
    errors = 0
    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                print(f"Uploaded {int(status.progress() * 100)}%: {video_file.name}")
        except HttpError as exc:
            if exc.resp.status not in {500, 502, 503, 504}:
                raise
            errors += 1
            if errors > 5:
                raise
            delay = min(2**errors, 60)
            print(f"Retryable YouTube error {exc.resp.status}; sleeping {delay}s")
            time.sleep(delay)

    return response


def append_manifest(manifest: Path, record: Dict[str, Any]) -> None:
    ensure_parent(manifest)
    with manifest.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def uploaded_audio_paths(manifest: Path) -> set[str]:
    uploaded: set[str] = set()
    if not manifest.exists():
        return uploaded
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue
        if record.get("youtube_id") and record.get("audio"):
            uploaded.add(str(Path(record["audio"]).expanduser()))
    return uploaded


def title_from_template(template: str, audio: Path, index: int) -> str:
    return template.format(stem=audio.stem, name=audio.name, index=index, index1=index + 1)


def collect_mp3s(input_dir: Path) -> List[Path]:
    if input_dir.is_file():
        return [input_dir]
    if not input_dir.exists():
        raise SystemExit(f"Input path not found: {input_dir}")
    return sorted(input_dir.glob("*.mp3"))


def command_render(args: argparse.Namespace) -> None:
    render_video(
        args.audio,
        args.output,
        cover=args.cover,
        overwrite=args.overwrite,
        dry_run=args.dry_run,
        audio_bitrate=args.audio_bitrate,
    )


def command_batch(args: argparse.Namespace) -> None:
    mp3s = collect_mp3s(args.input)
    if not mp3s:
        raise SystemExit(f"No mp3 files found in: {args.input}")
    if args.skip_uploaded:
        uploaded = uploaded_audio_paths(args.manifest)
        before = len(mp3s)
        mp3s = [audio for audio in mp3s if str(audio.expanduser()) not in uploaded]
        print(f"Skipping {before - len(mp3s)} already uploaded file(s) from {args.manifest}")
        if not mp3s:
            print("Nothing left to upload.")
            return

    youtube = None
    if args.upload and not args.dry_run:
        youtube = load_youtube_client(args.client_secrets, args.token_file)

    for index, audio in enumerate(mp3s):
        video = args.output_dir / f"{audio.stem}.mp4"
        title = title_from_template(args.title_template, audio, index)
        render_video(
            audio,
            video,
            cover=args.cover,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
            audio_bitrate=args.audio_bitrate,
        )

        record: Dict[str, Any] = {
            "audio": str(audio),
            "video": str(video),
            "title": title,
            "privacy": args.privacy,
        }

        if args.upload:
            if args.dry_run:
                print(f"DRY RUN upload: {video} -> {title!r}")
            else:
                response = upload_video(
                    youtube,
                    video,
                    title=title,
                    description=args.description,
                    privacy=args.privacy,
                    category=args.category,
                    tags=args.tags,
                )
                video_id = response["id"]
                record["youtube_id"] = video_id
                record["youtube_url"] = f"https://youtu.be/{video_id}"
                print(record["youtube_url"])

        if not args.dry_run:
            append_manifest(args.manifest, record)


def command_upload(args: argparse.Namespace) -> None:
    if not args.file.exists():
        raise SystemExit(f"Video file not found: {args.file}")
    if args.dry_run:
        print(f"DRY RUN upload: {args.file} -> {args.title!r}")
        return
    youtube = load_youtube_client(args.client_secrets, args.token_file)
    response = upload_video(
        youtube,
        args.file,
        title=args.title,
        description=args.description,
        privacy=args.privacy,
        category=args.category,
        tags=args.tags,
    )
    video_id = response["id"]
    record = {
        "video": str(args.file),
        "title": args.title,
        "privacy": args.privacy,
        "youtube_id": video_id,
        "youtube_url": f"https://youtu.be/{video_id}",
    }
    append_manifest(args.manifest, record)
    print(record["youtube_url"])


def add_common_upload_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--client-secrets", type=Path, default=Path("youtube-client-secrets.json"))
    parser.add_argument("--token-file", type=Path, default=Path("youtube-token.json"))
    parser.add_argument("--privacy", choices=["private", "unlisted", "public"], default="private")
    parser.add_argument("--category", default="27", help="YouTube category id; 27 is Education.")
    parser.add_argument("--description", default="")
    parser.add_argument("--tags", nargs="*", default=["feynman-reader"])
    parser.add_argument("--manifest", type=Path, default=Path("youtube-upload-manifest.jsonl"))
    parser.add_argument("--dry-run", action="store_true")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    render = subparsers.add_parser("render", help="Convert one audio file to MP4.")
    render.add_argument("audio", type=Path)
    render.add_argument("output", type=Path)
    render.add_argument("--cover", type=Path)
    render.add_argument("--audio-bitrate", default="192k")
    render.add_argument("--overwrite", action="store_true")
    render.add_argument("--dry-run", action="store_true")
    render.set_defaults(func=command_render)

    upload = subparsers.add_parser("upload", help="Upload one existing MP4.")
    upload.add_argument("file", type=Path)
    upload.add_argument("--title", required=True)
    add_common_upload_args(upload)
    upload.set_defaults(func=command_upload)

    batch = subparsers.add_parser("batch", help="Render a directory of MP3s, optionally upload.")
    batch.add_argument("input", type=Path, help="Directory of mp3 files, or one mp3 file.")
    batch.add_argument("--output-dir", type=Path, default=Path("youtube-videos"))
    batch.add_argument("--cover", type=Path)
    batch.add_argument("--title-template", default="Feynman Reader - {stem}")
    batch.add_argument("--audio-bitrate", default="192k")
    batch.add_argument("--overwrite", action="store_true")
    batch.add_argument("--upload", action="store_true")
    batch.add_argument("--skip-uploaded", action="store_true")
    add_common_upload_args(batch)
    batch.set_defaults(func=command_batch)

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
