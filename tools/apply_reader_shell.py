#!/usr/bin/env python3
"""Apply repeatable reader-shell maintenance updates."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from reader_site import CURRENT_ASSET_VERSION, ROOT


def run(args: list[str]) -> None:
    print("+ " + " ".join(args))
    subprocess.run(args, cwd=ROOT, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--asset-version", default=CURRENT_ASSET_VERSION)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    python = sys.executable
    tools = Path("tools")
    check_flag = ["--check"] if args.check else []
    run([python, str(tools / "bump_reader_assets.py"), args.asset_version, *check_flag])
    run([python, str(tools / "build_media_manifest.py"), *check_flag])
    run([python, str(tools / "ensure_media_player_assets.py"), *check_flag])
    run([python, str(tools / "clean_manifest_backed_html.py"), *check_flag])
    run([python, str(tools / "clean_manifest_backed_css.py"), *check_flag])
    run([python, str(tools / "update_notebooklm_report_shell.py"), *check_flag])
    run([python, str(tools / "update_volume_index_material_links.py"), *check_flag])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
