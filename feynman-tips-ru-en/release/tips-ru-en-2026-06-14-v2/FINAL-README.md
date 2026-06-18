# Feynman's Tips on Physics RU/EN Release v2

Built: 2026-06-14

## Files

- `en/feynmans-tips-on-physics-2013-source.pdf` - canonical local source PDF copy.
- `en/feynmans-tips-en-reflow.pdf` - editable English LaTeX reflow build with figure atlas.
- `en/feynmans-tips-en-reflow.tex` - English reflow LaTeX source.
- `ru/feynmans-tips-ru-gemini-3.5-flash-low.pdf` - full Russian LaTeX reflow build with figure atlas.
- `ru/feynmans-tips-ru-gemini-3.5-flash-low.tex` - Russian LaTeX source.
- `assets/figures/` - vector PDF crops extracted from the source PDF.
- `reports/build-report.json` - machine-readable build stats.
- `reports/figure-inventory.json` - extracted figure crop inventory.
- `reports/visual-qa/tips-release-contact-sheet.png` - source/RU visual spot check.
- `reports/visual-qa/figure-crop-sample-sheet.png` - sampled vector figure crop QA sheet.

## Build Stats

- Translation model: `gemini-3.5-flash-low`
- Translation chunks: `67`
- Translated source chars: `342860`
- Russian chars after repairs: `356444`
- Reflow page size: `396 x 594 bp`
- Extracted figure crops: `119`
- English source PDF: `209` pages, `346105` text chars.
- English reflow PDF: `184` pages, `365320` text chars, `18` links/bookmarks.
- Russian reflow PDF: `221` pages, `373482` text chars, `18` links/bookmarks.

## Notes

The English source PDF is kept as the exact reference. The EN/RU reflow PDFs are rebuilt from the local PDF text layer and are intended as editable LaTeX outputs with text layer, TOC, bookmarks, and vector figure assets. They are not page-exact replicas of the publisher PDF.

Formula handling now supports inline `$...$`, display `$$...$$`, common Unicode math symbols, and repair of JSON-decoded TeX escape damage such as broken `\right`. Figure crops are vector PDF assets from the original PDF, appended as an atlas; inline figure placement is still a separate layout pass.
