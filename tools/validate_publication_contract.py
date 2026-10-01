#!/usr/bin/env python3
"""Validate reviewed YouTube publication contracts without external credentials."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from publish_verified_video import load_contract  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("contracts", nargs="+", type=Path)
    args = parser.parse_args()

    seen_operations: set[str] = set()
    seen_sha256: set[str] = set()
    for path in args.contracts:
        contract = load_contract(path)
        operation = contract["operation"]
        sha = contract["source"]["video_sha256"]
        if operation in seen_operations:
            raise SystemExit(f"duplicate publication operation: {operation}")
        if sha in seen_sha256:
            raise SystemExit(f"duplicate publication video SHA-256: {sha}")
        seen_operations.add(operation)
        seen_sha256.add(sha)
        print(
            json.dumps(
                {
                    "contract": str(path),
                    "operation": operation,
                    "source_repository": contract["source"]["repository"],
                    "run_id": contract["source"]["run_id"],
                    "artifact_name": contract["source"]["artifact_name"],
                    "privacy": contract["youtube"]["privacy"],
                    "channel_handle": contract["youtube"]["channel_handle"],
                    "video_sha256": sha,
                },
                sort_keys=True,
            )
        )

    print(f"OK: {len(seen_operations)} publication contract(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
