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
