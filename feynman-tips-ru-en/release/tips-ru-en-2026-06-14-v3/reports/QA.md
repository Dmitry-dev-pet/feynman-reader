# Feynman's Tips Release v3 QA

## Completed

- Full text recovered from `pdf-text-pages.json` by TOC page ranges.
- Full Russian translation completed with `gemini-3.5-flash-low`.
- Two model-refusal chunks were repaired by smaller subchunk translation.
- EN and RU LaTeX builds compile with LuaLaTeX.
- Reflow PDFs use body-page geometry: `396 x 594 bp`.
- Text layer verified with PyMuPDF stats.
- TOC/bookmark links verified by link counts.
- `119` vector figure crops extracted from the source PDF.
- Figures inserted inline near detected captions where possible.
- Remaining unmatched figures are kept in fallback atlases.
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
- Inline figure placement is caption-near, not publisher-geometry-exact.
- EN has `117` inline figures and `2` fallback atlas figures.
- RU has `115` inline figures and `4` fallback atlas figures.
- Formula quality is limited by the PDF text layer and translation output; common math forms are preserved, but full semantic equation reconstruction remains a separate pass.
- Dense exercise/index pages still produce normal TeX underfull/overfull warnings.
