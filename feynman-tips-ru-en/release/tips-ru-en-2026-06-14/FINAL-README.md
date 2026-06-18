# Feynman's Tips on Physics RU/EN Release

Built: 2026-06-14

## Files

- `en/feynmans-tips-on-physics-2013-source.pdf` - canonical local source PDF copy.
- `en/feynmans-tips-en-reflow.pdf` - editable English LaTeX reflow build.
- `en/feynmans-tips-en-reflow.tex` - English reflow LaTeX source.
- `ru/feynmans-tips-ru-gemini-3.5-flash-low.pdf` - full Russian LaTeX reflow build.
- `ru/feynmans-tips-ru-gemini-3.5-flash-low.tex` - Russian LaTeX source.
- `reports/build-report.json` - machine-readable build stats.
- `reports/visual-qa/tips-release-contact-sheet.png` - source/RU visual spot check.

## Build Stats

- Translation model: `gemini-3.5-flash-low`
- Translation chunks: `67`
- Translated source chars: `342860`
- Russian chars: `356444`
- Reflow page size: `396 x 594 bp`
- English source PDF: `209` pages, `346105` text chars, TOC entries present.
- English reflow PDF: `124` pages, `345221` text chars, `17` links/bookmarks.
- Russian reflow PDF: `159` pages, `358564` text chars, `17` links/bookmarks.

## Notes

The English source PDF is kept as the exact reference. The EN/RU reflow PDFs
are rebuilt from the local PDF text layer and are intended as editable LaTeX
outputs with text layer, TOC, and bookmarks. They are not page-exact replicas
of the publisher PDF. Mathematical symbols that survived PDF text extraction
are mapped into TeX where possible; diagrams/figures from the original PDF are
not yet reconstructed as vector assets in the reflow build.
