#!/usr/bin/env python3
"""Publish one reviewed verified-video contract to the configured YouTube channel."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
from typing import Any

from youtube_upload import load_youtube_client, upload_video


ALLOWED_SOURCE_REPOSITORY = "Dmitry-dev-pet/mac-access"
ALLOWED_PRIVACY = {"unlisted"}
SHA256_HEX = set("0123456789abcdef")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def digest_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_contract(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    require(payload.get("version") == 1, "publication contract version must be 1")

    operation = payload.get("operation")
    require(
        isinstance(operation, str)
        and operation
        and all(ch.isalnum() or ch in "-_" for ch in operation),
        "invalid publication operation",
    )
    require(
        payload.get("issue_title") == f"[youtube] {operation}",
        "issue title must match the fixed publication operation",
    )

    source = payload.get("source") or {}
    require(
        source.get("repository") == ALLOWED_SOURCE_REPOSITORY,
        "publication source repository is not allowlisted",
    )
    require(
        isinstance(source.get("run_id"), int) and source["run_id"] > 0,
        "source run_id must be a positive integer",
    )
    for key in ("artifact_name", "video_file", "verification_file"):
        value = source.get(key)
        require(
            isinstance(value, str)
            and value
            and "/" not in value
            and "\\" not in value
            and value not in {".", ".."},
            f"invalid source {key}",
        )

    sha = source.get("video_sha256")
    require(
        isinstance(sha, str)
        and len(sha) == 64
        and all(ch in SHA256_HEX for ch in sha),
        "invalid source video_sha256",
    )

    expected = source.get("expected") or {}
    require(expected.get("verified") is True, "expected verifier state must be true")
    require(
        isinstance(expected.get("frame_count"), int) and expected["frame_count"] > 0,
        "expected frame_count must be positive",
    )
    require(
        isinstance(expected.get("fps"), int) and expected["fps"] > 0,
        "expected fps must be positive",
    )
    require(
        isinstance(expected.get("duration_seconds"), (int, float))
        and expected["duration_seconds"] > 0,
        "expected duration must be positive",
    )
    require(
        isinstance(expected.get("resolution"), list)
        and len(expected["resolution"]) == 2
        and all(isinstance(value, int) and value > 0 for value in expected["resolution"]),
        "expected resolution must be [width, height]",
    )

    youtube = payload.get("youtube") or {}
    require(
        youtube.get("channel_handle") == "@feynmanreadermedia",
        "unexpected YouTube channel handle",
    )
    require(
        youtube.get("privacy") in ALLOWED_PRIVACY,
        "publication privacy must be unlisted",
    )
    require(
        isinstance(youtube.get("title"), str) and 1 <= len(youtube["title"]) <= 100,
        "invalid YouTube title",
    )
    require(
        isinstance(youtube.get("description"), str)
        and sha in youtube["description"]
        and "OpenStreetMap" in youtube["description"]
        and "DGT" in youtube["description"],
        "description must contain SHA and source attribution",
    )
    require(
        isinstance(youtube.get("category"), str) and youtube["category"].isdigit(),
        "invalid YouTube category",
    )
    tags = youtube.get("tags")
    require(
        isinstance(tags, list)
        and all(isinstance(tag, str) and tag for tag in tags),
        "invalid YouTube tags",
    )
    return payload


def verify_artifact(root: Path, contract: dict[str, Any]) -> Path:
    source = contract["source"]
    video = root / source["video_file"]
    verification_path = root / source["verification_file"]

    require(video.is_file() and video.stat().st_size > 0, "verified video file is missing")
    require(verification_path.is_file(), "verification evidence is missing")

    actual_sha = digest_file(video)
    require(actual_sha == source["video_sha256"], "video SHA-256 does not match contract")

    verification = json.loads(verification_path.read_text(encoding="utf-8"))
    expected = source["expected"]
    require(verification.get("verified") is expected["verified"], "verifier status mismatch")
    require(
        int(verification.get("frame_count", 0)) == expected["frame_count"],
        "verified frame count mismatch",
    )
    require(int(verification.get("fps", 0)) == expected["fps"], "verified fps mismatch")
    require(
        math.isclose(
            float(verification.get("duration_seconds", 0)),
            float(expected["duration_seconds"]),
            abs_tol=0.04,
        ),
        "verified duration mismatch",
    )
    require(
        verification.get("resolution") == expected["resolution"],
        "verified resolution mismatch",
    )
    require(
        verification.get("video_sha256") == source["video_sha256"],
        "verifier video SHA-256 mismatch",
    )
    return video


def authenticated_channel(youtube: Any, expected_handle: str) -> tuple[str, str]:
    response = youtube.channels().list(
        part="id,snippet,contentDetails",
        mine=True,
    ).execute()
    items = response.get("items", [])
    require(len(items) == 1, "expected exactly one authenticated YouTube channel")
    channel = items[0]
    handle = (channel.get("snippet", {}).get("customUrl") or "").lower()
    require(handle == expected_handle.lower(), f"unexpected authenticated channel: {handle!r}")
    uploads = (
        channel.get("contentDetails", {})
        .get("relatedPlaylists", {})
        .get("uploads")
    )
    require(bool(uploads), "authenticated channel has no uploads playlist")
    return channel["id"], uploads


def existing_by_sha(youtube: Any, uploads_playlist: str, sha: str) -> dict[str, Any] | None:
    ids: list[str] = []
    page_token = None
    while True:
        response = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=uploads_playlist,
            maxResults=50,
            pageToken=page_token,
        ).execute()
        for item in response.get("items", []):
            video_id = item.get("contentDetails", {}).get("videoId")
            if video_id:
                ids.append(video_id)
        page_token = response.get("nextPageToken")
        if not page_token:
            break

    for offset in range(0, len(ids), 50):
        response = youtube.videos().list(
            part="snippet,status",
            id=",".join(ids[offset : offset + 50]),
        ).execute()
        for item in response.get("items", []):
            description = item.get("snippet", {}).get("description") or ""
            if sha in description:
                return item
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--token-file", type=Path, required=True)
    parser.add_argument("--result", type=Path, required=True)
    args = parser.parse_args()

    contract = load_contract(args.contract)
    video = verify_artifact(args.artifact_root, contract)
    youtube_spec = contract["youtube"]
    source = contract["source"]

    youtube = load_youtube_client(Path("__unused_client_secrets.json"), args.token_file)
    channel_id, uploads_playlist = authenticated_channel(
        youtube,
        youtube_spec["channel_handle"],
    )

    existing = existing_by_sha(youtube, uploads_playlist, source["video_sha256"])
    if existing is not None:
        video_id = existing["id"]
        result = {
            "status": "existing",
            "youtube_id": video_id,
            "youtube_url": f"https://youtu.be/{video_id}",
            "privacy": existing.get("status", {}).get("privacyStatus"),
            "title": existing.get("snippet", {}).get("title"),
            "video_sha256": source["video_sha256"],
            "channel_id": channel_id,
        }
    else:
        response = upload_video(
            youtube,
            video,
            title=youtube_spec["title"],
            description=youtube_spec["description"],
            privacy=youtube_spec["privacy"],
            category=youtube_spec["category"],
            tags=youtube_spec["tags"],
        )
        video_id = response["id"]
        result = {
            "status": "uploaded",
            "youtube_id": video_id,
            "youtube_url": f"https://youtu.be/{video_id}",
            "privacy": youtube_spec["privacy"],
            "title": youtube_spec["title"],
            "video_sha256": source["video_sha256"],
            "channel_id": channel_id,
        }

    args.result.parent.mkdir(parents=True, exist_ok=True)
    args.result.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(result["youtube_url"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
