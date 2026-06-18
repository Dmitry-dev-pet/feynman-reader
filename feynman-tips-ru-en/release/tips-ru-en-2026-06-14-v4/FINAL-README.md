# Feynman's Tips on Physics RU/EN Release v4

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
- Russian reflow PDF: `212` pages, `370993` text chars, `18` links/bookmarks.
- English figure placement: `117` inline, `2` fallback atlas.
- Russian figure placement: `115` inline, `4` fallback atlas.

## v4 Changes

Release v4 keeps the English build on the conservative parser and applies the expanded math repair only to the Russian LLM text. This removes most escaped TeX artifacts from formulas without reintroducing the English math-mode regression.

Russian TeX artifact counts improved from v3 to v4:

- `textbackslash{}mathbf`: `79` -> `0`
- `textbackslash{}frac`: `22` -> `0`
- `textbackslash{}left`: `6` -> `0`
- `textbackslash{}sqrt`: `21` -> `2`
- `textbackslash{}int`: `6` -> `0`

The EN/RU reflow PDFs are rebuilt from the local PDF text layer and are intended as editable LaTeX outputs with text layer, TOC, bookmarks, and vector figure assets. They are not page-exact replicas of the publisher PDF.

