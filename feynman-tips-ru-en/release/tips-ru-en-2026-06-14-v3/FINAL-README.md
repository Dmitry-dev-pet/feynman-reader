# Feynman's Tips on Physics RU/EN Release v3

Built: 2026-06-14

## Files

- `en/feynmans-tips-on-physics-2013-source.pdf` - canonical local source PDF copy.
- `en/feynmans-tips-en-reflow.pdf` - editable English LaTeX reflow build with inline vector figures.
- `en/feynmans-tips-en-reflow.tex` - English reflow LaTeX source.
- `ru/feynmans-tips-ru-gemini-3.5-flash-low.pdf` - full Russian LaTeX reflow build with inline vector figures.
- `ru/feynmans-tips-ru-gemini-3.5-flash-low.tex` - Russian LaTeX source.
- `assets/figures/` - vector PDF crops extracted from the source PDF.
- `en/*-figure-placement.json` and `ru/*-figure-placement.json` - inline/fallback figure placement reports.
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
- English reflow PDF: `172` pages, `365271` text chars, `18` links/bookmarks.
- Russian reflow PDF: `213` pages, `373449` text chars, `18` links/bookmarks.
- English figure placement: `117` inline, `2` fallback atlas.
- Russian figure placement: `115` inline, `4` fallback atlas.

## Notes

The English source PDF is kept as the exact reference. The EN/RU reflow PDFs are rebuilt from the local PDF text layer and are intended as editable LaTeX outputs with text layer, TOC, bookmarks, and vector figure assets. They are not page-exact replicas of the publisher PDF.

Release v3 inserts vector PDF figure crops near detected caption labels. The fallback atlas now only contains figures whose captions were not reliably present in the reflow text. Formula handling supports inline `$...$`, display `$$...$$`, common Unicode math symbols, and repair of JSON-decoded TeX escape damage such as broken `\right`.
