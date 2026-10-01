#!/usr/bin/env python3
"""One-time bootstrap for the read-only GitHub Artifact Reader App.

The App is intentionally separate from github-control. It receives only
GitHub Actions read permission and should be installed only for mac-access.

Requirements:
- Python 3.12+
- gh CLI authenticated as Dmitry-dev-pet
- a browser on the same machine

The App private key is kept in memory and streamed directly into the
feynman-reader GitHub Actions secret. It is never written to disk or printed.
"""

from __future__ import annotations

import html
import json
import os
import secrets
import subprocess
import sys
import threading
import urllib.error
import urllib.parse
import urllib.request
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer

REPO = "Dmitry-dev-pet/feynman-reader"
HOST = "127.0.0.1"
PORT = int(os.environ.get("ARTIFACT_READER_BOOTSTRAP_PORT", "8768"))
API_VERSION = "2026-03-10"
CLIENT_ID_VARIABLE = "ARTIFACT_READER_APP_CLIENT_ID"
PRIVATE_KEY_SECRET = "ARTIFACT_READER_APP_PRIVATE_KEY"


def run_gh(*args: str, input_text: str | None = None) -> str:
    proc = subprocess.run(
        ["gh", *args],
        input=input_text,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"gh {' '.join(args)} failed")
    return proc.stdout.strip()


def exchange_manifest_code(code: str, auth_token: str) -> dict:
    req = urllib.request.Request(
        f"https://api.github.com/app-manifests/{urllib.parse.quote(code, safe='')}/conversions",
        data=b"",
        method="POST",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {auth_token}",
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "feynman-artifact-reader-bootstrap",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"GitHub manifest conversion failed: HTTP {exc.code}: {body}"
        ) from exc


def main() -> int:
    try:
        run_gh("auth", "status")
        auth_token = run_gh("auth", "token")
    except Exception as exc:
        print(f"ERROR: authenticated gh CLI is required: {exc}", file=sys.stderr)
        return 2

    state = secrets.token_urlsafe(32)
    redirect_url = f"http://{HOST}:{PORT}/callback"
    manifest = {
        "name": "dmitry-feynman-artifact-reader",
        "url": "https://github.com/Dmitry-dev-pet/feynman-reader",
        "redirect_url": redirect_url,
        "description": (
            "Read-only GitHub App used by feynman-reader to retrieve verified "
            "mac-access Actions artifacts for publication"
        ),
        "public": False,
        "default_permissions": {
            "actions": "read",
        },
        "default_events": [],
        "request_oauth_on_install": False,
    }

    result: dict[str, str] = {}
    error: list[str] = []

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt: str, *args) -> None:
            return

        def do_GET(self) -> None:
            parsed = urllib.parse.urlparse(self.path)
            if parsed.path == "/start":
                manifest_json = json.dumps(manifest, separators=(",", ":"))
                page = f"""<!doctype html>
<html><body>
<p>Redirecting to GitHub Artifact Reader App registration…</p>
<form id="f" method="post"
 action="https://github.com/settings/apps/new?state={urllib.parse.quote(state)}">
<input type="hidden" name="manifest" value="{html.escape(manifest_json, quote=True)}">
</form>
<script>document.getElementById('f').submit();</script>
</body></html>"""
                data = page.encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
                return

            if parsed.path != "/callback":
                self.send_error(404)
                return

            query = urllib.parse.parse_qs(parsed.query)
            returned_state = query.get("state", [""])[0]
            code = query.get("code", [""])[0]
            if returned_state != state or not code:
                error.append("Invalid callback state or missing manifest code")
                body = b"Artifact Reader bootstrap failed: invalid callback."
            else:
                try:
                    app = exchange_manifest_code(code, auth_token)
                    client_id = app["client_id"]
                    pem = app["pem"]
                    slug = app["slug"]

                    run_gh(
                        "secret",
                        "set",
                        PRIVATE_KEY_SECRET,
                        "--repo",
                        REPO,
                        input_text=pem,
                    )
                    result.update(
                        {
                            "slug": slug,
                            "client_id": client_id,
                            "install_url": f"https://github.com/apps/{slug}/installations/new",
                        }
                    )
                    body = (
                        b"Artifact Reader App created and private key stored. "
                        b"Return to the terminal to install it."
                    )
                except Exception as exc:
                    error.append(str(exc))
                    body = b"Artifact Reader bootstrap failed. Return to the terminal."

            self.send_response(200 if not error else 500)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            threading.Thread(target=self.server.shutdown, daemon=True).start()

    server = HTTPServer((HOST, PORT), Handler)
    start_url = f"http://{HOST}:{PORT}/start"
    print("Opening Artifact Reader App registration in your browser.")
    print(f"If the browser does not open, visit: {start_url}")
    webbrowser.open(start_url)
    server.serve_forever()

    if error:
        print(f"ERROR: {error[0]}", file=sys.stderr)
        return 3

    install_url = result["install_url"]
    print()
    print("The private key is stored in feynman-reader, but App auth is not active yet.")
    print("Opening the installation page.")
    print("Choose 'Only select repositories' and select ONLY: mac-access")
    print(f"If the browser does not open, visit: {install_url}")
    webbrowser.open(install_url)
    input("After GitHub shows the installation as complete, press Enter here... ")

    run_gh(
        "variable",
        "set",
        CLIENT_ID_VARIABLE,
        "--repo",
        REPO,
        "--body",
        result["client_id"],
    )

    try:
        print("Triggering Artifact Reader smoke verification...")
        run_gh(
            "workflow",
            "run",
            "artifact-reader-smoke.yml",
            "--repo",
            REPO,
        )

        run_id = run_gh(
            "run",
            "list",
            "--repo",
            REPO,
            "--workflow",
            "artifact-reader-smoke.yml",
            "--event",
            "workflow_dispatch",
            "--limit",
            "1",
            "--json",
            "databaseId",
            "--jq",
            ".[0].databaseId",
        )
        if not run_id:
            print("Smoke workflow dispatched; run ID was not visible yet.")
            return 0

        print(f"Watching workflow run {run_id}...")
        proc = subprocess.run(
            ["gh", "run", "watch", run_id, "--repo", REPO, "--exit-status"],
            check=False,
        )
        if proc.returncode != 0:
            raise RuntimeError(f"smoke workflow {run_id} failed")
    except Exception as exc:
        try:
            run_gh("variable", "delete", CLIENT_ID_VARIABLE, "--repo", REPO)
        except Exception:
            pass
        print(
            "Artifact Reader App was created but verification failed; "
            f"activation variable was removed. {exc}",
            file=sys.stderr,
        )
        return 4

    print("Artifact Reader bootstrap complete.")
    print("The App can read Actions artifacts from mac-access only.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
