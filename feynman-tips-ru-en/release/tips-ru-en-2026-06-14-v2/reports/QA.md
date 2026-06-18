# Feynman's Tips Release v2 QA

## Completed

- Full text recovered from `pdf-text-pages.json` by TOC page ranges.
- Full Russian translation completed with `gemini-3.5-flash-low`.
- Two model-refusal chunks were repaired by smaller subchunk translation.
- EN and RU LaTeX builds compile with LuaLaTeX.
- Reflow PDFs use body-page geometry: `396 x 594 bp`.
- Text layer verified with PyMuPDF stats.
- TOC/bookmark links verified by link counts.
- `119` vector figure crops extracted from the source PDF.
- Figure atlas appended to both EN and RU reflow PDFs.
- Visual spot-check contact sheet generated.
- Figure crop sample sheet generated.

## Current Outputs

- EN source PDF: `en/feynmans-tips-on-physics-2013-source.pdf`
- EN reflow PDF: `en/feynmans-tips-en-reflow.pdf`
- RU reflow PDF: `ru/feynmans-tips-ru-gemini-3.5-flash-low.pdf`
- Figure assets: `assets/figures/`
- Visual QA: `reports/visual-qa/tips-release-contact-sheet.png`
- Figure QA: `reports/visual-qa/figure-crop-sample-sheet.png`

## Known Limits

- Reflow layout is editable and readable, but not page-exact.
- Figures are restored as vector PDF crops in an atlas, not yet placed inline.
- Formula quality is limited by the PDF text layer and translation output; common math forms are preserved, but full semantic equation reconstruction remains a separate pass.
- Dense exercise/index pages still produce normal TeX underfull/overfull warnings.
