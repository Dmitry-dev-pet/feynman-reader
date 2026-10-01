# YouTube Upload CLI

This helper keeps audio out of git while letting the reader point to YouTube URLs.

## 1. Render MP3 to MP4

YouTube does not accept MP3-only uploads. Convert each audio file to an MP4 first:

```bash
python3 tools/youtube_upload.py render path/to/ch01.mp3 youtube-videos/ch01.mp4 --overwrite
```

Optional cover image:

```bash
python3 tools/youtube_upload.py render path/to/ch01.mp3 youtube-videos/ch01.mp4 \
  --cover cover.png --overwrite
```

## 2. Install Upload Dependencies

```bash
python3 -m pip install -r tools/youtube-upload-requirements.txt
```

The existing `/Users/dmitry/Project/docs-to-latex/.venv/bin/python` environment
already has these dependencies installed and can run this CLI directly.

Create an OAuth client in Google Cloud Console, enable YouTube Data API v3, download
the OAuth JSON, and save it locally as `youtube-client-secrets.json`.

That file is ignored by git.

## 3. Upload One MP4

```bash
python3 tools/youtube_upload.py upload youtube-videos/ch01.mp4 \
  --title "Feynman Reader RU I-01" \
  --privacy private \
  --client-secrets youtube-client-secrets.json
```

The first upload opens a browser for OAuth and writes `youtube-token.json`.
The upload result is appended to `youtube-upload-manifest.jsonl`.

The CLI requests both YouTube scopes used by this project:

- `https://www.googleapis.com/auth/youtube.upload` for uploads.
- `https://www.googleapis.com/auth/youtube.force-ssl` for metadata, privacy, channel branding, and playlists.

Check the authenticated channel and granted scopes:

```bash
python3 tools/youtube_upload.py auth
```

Force a fresh consent screen if the saved token was created with narrower access:

```bash
python3 tools/youtube_upload.py auth --reset
```

## 4. Batch Render And Upload

Dry run:

```bash
python3 tools/youtube_upload.py batch path/to/mp3-dir \
  --title-template "Feynman Reader RU I - {stem}" \
  --privacy private \
  --dry-run
```

Real upload:

```bash
python3 tools/youtube_upload.py batch path/to/mp3-dir \
  --title-template "Feynman Reader RU I - {stem}" \
  --privacy private \
  --upload
```

Use `private` first. Switch to `unlisted` only when you are comfortable with the
rights and platform-policy risk.


## 5. Audit And Synchronize Channel Metadata

Before changing anything on YouTube, inspect the 17 reader videos and their
current visibility:

```bash
python3 tools/sync_youtube_channel.py --video-report-only
```

The report shows each video ID, its current `public` / `unlisted` /
`private` status, and the proposed search-oriented title.

Preview the full synchronization without writes:

```bash
python3 tools/sync_youtube_channel.py --dry-run
```

Apply the metadata and playlist synchronization only after reviewing that
output:

```bash
python3 tools/sync_youtube_channel.py
```

The synchronized video titles and descriptions deliberately describe the
uploads as independent AI-assisted study companions. They use common search
phrases such as `Feynman Lectures on Physics` and
`Фейнмановские лекции по физике` without presenting the channel as an
official Caltech or Feynman Lectures source.

This synchronization does **not** change video privacy. Visibility remains an
explicit separate decision via `youtube_upload.py set-privacy`.

## 6. GitHub Actions Authentication

The `YouTube channel audit` workflow uses the `youtube-audit` environment and
requires one environment secret:

- `YOUTUBE_TOKEN_B64` — the complete `youtube-token.json` created by this CLI.

The authorized-user token already contains the refresh token, OAuth client ID,
client secret, token URI, and granted scopes needed to refresh credentials.
Do not add a separate `YOUTUBE_CLIENT_SECRETS_B64` secret.

Set or rotate the token from macOS without printing its contents:

```bash
base64 < youtube-token.json | \
  gh secret set YOUTUBE_TOKEN_B64 --env youtube-audit
```

Base64 is transport encoding, not encryption. Protection is provided by the
GitHub environment secret; never commit either OAuth JSON file or persist the
decoded token as an Actions artifact or cache.


## 7. Private Actions artifact reader

Verified rendered videos are produced in the private
`Dmitry-dev-pet/mac-access` repository. Do not copy the powerful GitHub Control
App private key into this repository and do not persist temporary signed artifact
URLs in workflow files.

Instead, bootstrap the dedicated **Artifact Reader App** once:

```bash
python3 tools/bootstrap_artifact_reader_app.py
```

The bootstrap creates a private GitHub App with only:

- repository permission **Actions: read**;
- no Contents, Administration, Pages, Issues, Secrets, or write permission;
- installation restricted to **mac-access only**.

The private key is streamed directly to the
`ARTIFACT_READER_APP_PRIVATE_KEY` repository secret. The non-secret identifiers are stored as `ARTIFACT_READER_APP_CLIENT_ID` and
`ARTIFACT_READER_APP_ID`. Workflows accept either one, so an interrupted older
bootstrap can still be completed without recreating the App. The bootstrap then runs
`artifact-reader-smoke.yml`, which mints a one-hour token scoped to
`mac-access` and requests only `actions: read`.

The resulting token is used only to download a pinned Actions artifact. It is not
stored as a repository secret or publication artifact.

## 8. Contract-driven verified publication

Publication requests are reviewed JSON contracts under
`youtube-publication-contracts/`. A contract pins:

- source repository, Actions run ID and artifact name;
- exact final MP4 filename and SHA-256;
- expected verifier frame count, FPS, duration and resolution;
- YouTube channel, title, privacy, category, tags and attribution.

The issue workflow ignores issue bodies and accepts no dynamic repository, run, artifact, URL or privacy inputs. Currently the accepted command is:

```text
[youtube] coimbra-032
```

The publisher:

1. mints an Artifact Reader token scoped to `mac-access` with Actions read only;
2. downloads the exact pinned artifact;
3. verifies the MP4 SHA-256 and independent render verification evidence;
4. authenticates to exactly `@feynmanreadermedia`;
5. searches existing uploads for the same video SHA-256;
6. reuses the existing URL instead of uploading a duplicate;
7. otherwise uploads as **unlisted**;
8. returns a sanitized publication receipt and closes the issue.

Adding a future video requires a new reviewed contract and an explicit fixed route in
`youtube-publish-verified.yml`. Do not add arbitrary run IDs, artifact names,
repositories, URLs, titles, or privacy settings from issue bodies.
