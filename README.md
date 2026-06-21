# Feynman Reader Release

Kind: `lite-no-media`
Entry: `feynman-reader/index.html`
Approximate size: `736.3 MiB`

Open `feynman-reader/index.html` in a browser, or serve this directory as a static site.

This package is intended for local/private use.

## Reader Maintenance

The reader shell is static HTML plus shared assets in `feynman-reader/`.
Use the repo-local tools below after changing chapter media, report links, or
shared reader CSS/JS:

```bash
python3 tools/build_media_manifest.py
python3 tools/clean_manifest_backed_html.py
python3 tools/clean_manifest_backed_css.py
python3 tools/apply_reader_shell.py --check
python3 tools/validate_reader_site.py
```

To intentionally bump the shared media-player cache key across pages:

```bash
python3 tools/bump_reader_assets.py 20260621-new-label
```

Local media files, YouTube tokens, upload manifests, and rendered compilations
are intentionally ignored by git.
