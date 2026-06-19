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
