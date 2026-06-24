#!/usr/bin/env python3
"""Synchronize Feynman Reader YouTube playlists and video metadata."""

from __future__ import annotations

import argparse
import json
import sys
import time
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from youtube_upload import load_youtube_client


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "feynman-reader" / "media-manifest.json"
READER_URL = "https://dmitry-dev-pet.github.io/feynman-reader/"

LANG_LABEL = {"ru": "RU", "en": "EN"}
VOLUME_LABEL = {"I": "Volume I", "II": "Volume II", "III": "Volume III"}
MEDIA_LABEL = {"audio": "Audio", "video": "Video"}
MEDIA_ACTION = {"audio": "listen", "video": "watch"}


@dataclass(frozen=True)
class VideoSpec:
    video_id: str
    language: str
    volume: str
    media_type: str
    chapters: tuple[dict[str, Any], ...]
    part_index: int
    part_count: int

    @property
    def lang_label(self) -> str:
        return LANG_LABEL[self.language]

    @property
    def volume_label(self) -> str:
        return VOLUME_LABEL[self.volume]

    @property
    def media_label(self) -> str:
        return MEDIA_LABEL[self.media_type]

    @property
    def group_title(self) -> str:
        return f"Feynman Reader {self.lang_label} {self.volume_label}"

    @property
    def title(self) -> str:
        base = f"{self.group_title} - NotebookLM {self.media_label}"
        if self.part_count > 1:
            return f"{base} Part {self.part_index}/{self.part_count}"
        return base

    @property
    def tags(self) -> list[str]:
        return [
            "Feynman Reader",
            "Feynman Lectures",
            "NotebookLM",
            "Physics",
            "Education",
            self.lang_label,
            self.volume_label,
            self.media_label,
        ]

    @property
    def description(self) -> str:
        part = f", part {self.part_index}/{self.part_count}" if self.part_count > 1 else ""
        lines = [
            self.title,
            "",
            "Open Feynman Reader:",
            READER_URL,
            "",
            f"{self.lang_label} {self.volume_label} NotebookLM {self.media_type} companion{part}.",
            f"Chapter pages include timestamped {MEDIA_ACTION[self.media_type]} links.",
            "",
            "Chapters:",
        ]
        for chapter in self.chapters:
            lines.append(f"{format_time(chapter['start'])} Chapter {chapter['chapter']}. {chapter['title']}")
        lines += [
            "",
            "Created with AI-assisted NotebookLM study materials.",
            "Independent study-media archive; not an official Feynman Lectures channel.",
        ]
        return "\n".join(lines)


@dataclass(frozen=True)
class PlaylistSpec:
    title: str
    description: str
    video_ids: tuple[str, ...]


def format_time(seconds: int) -> str:
    seconds = int(seconds)
    hours, remainder = divmod(seconds, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def parse_volume(group: str) -> tuple[str, str]:
    language, volume = group.split("-", 1)
    return language, volume


def clean_chapter_title(chapter: int, title: str) -> str:
    prefix = f"{chapter}. "
    if title.startswith(prefix):
        return title[len(prefix) :]
    return title


def load_video_specs() -> list[VideoSpec]:
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    grouped: dict[tuple[str, str, str, str], list[dict[str, Any]]] = defaultdict(list)

    for key, chapter in data["chapters"].items():
        group, _chapter_slug = key.split("/", 1)
        language, volume = parse_volume(group)
        for media in chapter.get("media", []):
            video_id = media.get("youtube_id")
            media_type = media.get("type")
            if not video_id or media_type not in MEDIA_LABEL:
                continue
            grouped[(language, volume, media_type, video_id)].append(
                {
                    "chapter": int(chapter["chapter"]),
                    "title": clean_chapter_title(int(chapter["chapter"]), str(chapter.get("title") or "")),
                    "start": int(media.get("start") or 0),
                }
            )

    group_order = {"ru": 0, "en": 1}
    volume_order = {"I": 0, "II": 1, "III": 2}
    specs: list[VideoSpec] = []
    by_media_group: dict[tuple[str, str, str], list[tuple[str, list[dict[str, Any]]]]] = defaultdict(list)
    for (language, volume, media_type, video_id), chapters in grouped.items():
        chapters.sort(key=lambda item: item["chapter"])
        by_media_group[(language, volume, media_type)].append((video_id, chapters))

    for (language, volume, media_type), rows in by_media_group.items():
        rows.sort(key=lambda row: row[1][0]["chapter"])
        for index, (video_id, chapters) in enumerate(rows, start=1):
            specs.append(
                VideoSpec(
                    video_id=video_id,
                    language=language,
                    volume=volume,
                    media_type=media_type,
                    chapters=tuple(chapters),
                    part_index=index,
                    part_count=len(rows),
                )
            )

    return sorted(
        specs,
        key=lambda spec: (
            group_order[spec.language],
            volume_order[spec.volume],
            0 if spec.media_type == "audio" else 1,
            spec.part_index,
        ),
    )


def playlist_specs(video_specs: list[VideoSpec]) -> list[PlaylistSpec]:
    by_id = {spec.video_id: spec for spec in video_specs}
    group_order = {"ru": 0, "en": 1}
    volume_order = {"I": 0, "II": 1, "III": 2}

    specs: list[PlaylistSpec] = []
    for media_type in ("audio", "video"):
        videos = [
            spec.video_id
            for spec in sorted(
                video_specs,
                key=lambda item: (
                    group_order[item.language],
                    volume_order[item.volume],
                    item.part_index,
                ),
            )
            if spec.media_type == media_type
        ]
        specs.append(
            PlaylistSpec(
                title=f"Feynman Reader NotebookLM {MEDIA_LABEL[media_type]}",
                description=(
                    f"All Feynman Reader NotebookLM {media_type} companion videos, "
                    "organized with chapter timestamps. Open the reader: "
                    f"{READER_URL}"
                ),
                video_ids=tuple(videos),
            )
        )

    for language in ("ru", "en"):
        for volume in ("I", "II", "III"):
            rows = [
                spec
                for spec in video_specs
                if spec.language == language and spec.volume == volume
            ]
            if not rows:
                continue
            rows.sort(key=lambda item: (0 if item.media_type == "audio" else 1, item.part_index))
            title = f"Feynman Reader {LANG_LABEL[language]} {VOLUME_LABEL[volume]}"
            specs.append(
                PlaylistSpec(
                    title=title,
                    description=(
                        f"{title}: NotebookLM audio and video companion media with chapter timestamps. "
                        f"Open the reader: {READER_URL}"
                    ),
                    video_ids=tuple(spec.video_id for spec in rows if spec.video_id in by_id),
                )
            )
    return specs


def batched(items: list[str], size: int) -> list[list[str]]:
    return [items[index : index + size] for index in range(0, len(items), size)]


def existing_playlists(youtube: Any) -> dict[str, dict[str, Any]]:
    playlists: dict[str, dict[str, Any]] = {}
    page_token = None
    while True:
        response = youtube.playlists().list(
            part="id,snippet,status,contentDetails",
            mine=True,
            maxResults=50,
            pageToken=page_token,
        ).execute()
        for item in response.get("items", []):
            playlists[str(item.get("snippet", {}).get("title") or "")] = item
        page_token = response.get("nextPageToken")
        if not page_token:
            return playlists


def playlist_items(youtube: Any, playlist_id: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    page_token = None
    while True:
        for attempt in range(6):
            try:
                response = youtube.playlistItems().list(
                    part="id,snippet",
                    playlistId=playlist_id,
                    maxResults=50,
                    pageToken=page_token,
                ).execute()
                break
            except Exception as exc:
                reason = ""
                try:
                    reason = exc.error_details[0].get("reason", "")
                except Exception:
                    pass
                if reason != "playlistNotFound" or attempt == 5:
                    raise
                time.sleep(2)
        items.extend(response.get("items", []))
        page_token = response.get("nextPageToken")
        if not page_token:
            return items


def sync_video_metadata(youtube: Any, specs: list[VideoSpec], *, dry_run: bool) -> None:
    video_ids = [spec.video_id for spec in specs]
    existing: dict[str, dict[str, Any]] = {}
    for batch in batched(video_ids, 50):
        response = youtube.videos().list(part="id,snippet", id=",".join(batch), maxResults=50).execute()
        for item in response.get("items", []):
            existing[item["id"]] = item

    for spec in specs:
        current = existing.get(spec.video_id)
        if not current:
            print(f"missing video on YouTube: {spec.video_id}")
            continue
        snippet = dict(current.get("snippet", {}))
        changed = (
            snippet.get("title") != spec.title
            or snippet.get("description") != spec.description
            or sorted(snippet.get("tags") or []) != sorted(spec.tags)
        )
        if not changed:
            print(f"video ok: {spec.video_id} {spec.title}")
            continue
        print(f"{'DRY RUN ' if dry_run else ''}update video: {spec.video_id} {spec.title}")
        if dry_run:
            continue
        snippet["title"] = spec.title
        snippet["description"] = spec.description
        snippet["tags"] = spec.tags
        snippet["categoryId"] = snippet.get("categoryId") or "27"
        youtube.videos().update(
            part="snippet",
            body={
                "id": spec.video_id,
                "snippet": snippet,
            },
        ).execute()


def upsert_playlist(youtube: Any, spec: PlaylistSpec, existing: dict[str, dict[str, Any]], *, dry_run: bool) -> str | None:
    current = existing.get(spec.title)
    if current:
        playlist_id = current["id"]
        snippet = current.get("snippet", {})
        status = current.get("status", {})
        changed = snippet.get("description") != spec.description or status.get("privacyStatus") != "public"
        if changed:
            print(f"{'DRY RUN ' if dry_run else ''}update playlist: {spec.title}")
            if not dry_run:
                youtube.playlists().update(
                    part="snippet,status",
                    body={
                        "id": playlist_id,
                        "snippet": {"title": spec.title, "description": spec.description},
                        "status": {"privacyStatus": "public"},
                    },
                ).execute()
        else:
            print(f"playlist ok: {spec.title}")
        return playlist_id

    print(f"{'DRY RUN ' if dry_run else ''}create playlist: {spec.title}")
    if dry_run:
        return None
    response = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {"title": spec.title, "description": spec.description},
            "status": {"privacyStatus": "public"},
        },
    ).execute()
    playlist_id = response["id"]
    existing[spec.title] = response
    return playlist_id


def sync_playlist_items(youtube: Any, spec: PlaylistSpec, playlist_id: str | None, *, dry_run: bool) -> None:
    if playlist_id is None:
        for index, video_id in enumerate(spec.video_ids):
            print(f"DRY RUN add to new playlist {spec.title}[{index}]: {video_id}")
        return

    items = playlist_items(youtube, playlist_id)
    target = list(spec.video_ids)
    seen: dict[str, dict[str, Any]] = {}
    for item in items:
        video_id = item.get("snippet", {}).get("resourceId", {}).get("videoId")
        if not video_id:
            continue
        if video_id in seen or video_id not in target:
            print(f"{'DRY RUN ' if dry_run else ''}remove from {spec.title}: {video_id}")
            if not dry_run:
                youtube.playlistItems().delete(id=item["id"]).execute()
            continue
        seen[video_id] = item

    for index, video_id in enumerate(target):
        current = seen.get(video_id)
        if current:
            snippet = dict(current.get("snippet", {}))
            if int(snippet.get("position", -1)) != index:
                print(f"{'DRY RUN ' if dry_run else ''}move in {spec.title}: {video_id} -> {index}")
                if not dry_run:
                    snippet["position"] = index
                    youtube.playlistItems().update(
                        part="snippet",
                        body={"id": current["id"], "snippet": snippet},
                    ).execute()
            continue

        print(f"{'DRY RUN ' if dry_run else ''}add to {spec.title}[{index}]: {video_id}")
        if not dry_run:
            youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId": playlist_id,
                        "position": index,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": video_id,
                        },
                    }
                },
            ).execute()


def channel_sections(youtube: Any) -> list[dict[str, Any]]:
    response = youtube.channelSections().list(part="id,snippet,contentDetails", mine=True).execute()
    return response.get("items", [])


def sync_channel_sections(
    youtube: Any,
    playlists: list[PlaylistSpec],
    playlist_ids: dict[str, str],
    *,
    dry_run: bool,
) -> None:
    target_titles = [
        "Feynman Reader NotebookLM Video",
        "Feynman Reader NotebookLM Audio",
        "Feynman Reader RU Volume I",
        "Feynman Reader RU Volume II",
        "Feynman Reader RU Volume III",
        "Feynman Reader EN Volume I",
        "Feynman Reader EN Volume II",
        "Feynman Reader EN Volume III",
    ]
    wanted = [playlist_ids[title] for title in target_titles if title in playlist_ids]
    current = channel_sections(youtube)
    by_playlist: dict[str, dict[str, Any]] = {}
    for section in current:
        playlists_in_section = section.get("contentDetails", {}).get("playlists") or []
        if len(playlists_in_section) == 1:
            by_playlist[str(playlists_in_section[0])] = section

    title_by_id = {playlist_ids[spec.title]: spec.title for spec in playlists if spec.title in playlist_ids}
    for position, playlist_id in enumerate(wanted):
        section = by_playlist.get(playlist_id)
        title = title_by_id.get(playlist_id, playlist_id)
        if section:
            current_position = int(section.get("snippet", {}).get("position", -1))
            if current_position == position:
                print(f"channel section ok: {title}")
                continue
            print(f"{'DRY RUN ' if dry_run else ''}move channel section: {title} -> {position}")
            if not dry_run:
                youtube.channelSections().update(
                    part="snippet,contentDetails",
                    body={
                        "id": section["id"],
                        "snippet": {
                            "type": "singleplaylist",
                            "position": position,
                        },
                        "contentDetails": {"playlists": [playlist_id]},
                    },
                ).execute()
            continue

        print(f"{'DRY RUN ' if dry_run else ''}create channel section: {title} -> {position}")
        if not dry_run:
            youtube.channelSections().insert(
                part="snippet,contentDetails",
                body={
                    "snippet": {
                        "type": "singleplaylist",
                        "position": position,
                    },
                    "contentDetails": {"playlists": [playlist_id]},
                },
            ).execute()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--client-secrets", type=Path, default=Path("youtube-client-secrets.json"))
    parser.add_argument("--token-file", type=Path, default=Path("youtube-token.json"))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-video-metadata", action="store_true")
    parser.add_argument("--skip-channel-sections", action="store_true")
    args = parser.parse_args()

    specs = load_video_specs()
    playlists = playlist_specs(specs)
    print(f"videos={len(specs)} playlists={len(playlists)} dry_run={args.dry_run}")
    youtube = load_youtube_client(args.client_secrets, args.token_file)
    if not args.skip_video_metadata:
        sync_video_metadata(youtube, specs, dry_run=args.dry_run)
    existing = existing_playlists(youtube)
    playlist_ids: dict[str, str] = {}
    for playlist in playlists:
        playlist_id = upsert_playlist(youtube, playlist, existing, dry_run=args.dry_run)
        if playlist_id:
            playlist_ids[playlist.title] = playlist_id
        sync_playlist_items(youtube, playlist, playlist_id, dry_run=args.dry_run)
    if not args.skip_channel_sections:
        sync_channel_sections(youtube, playlists, playlist_ids, dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
