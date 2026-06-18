# Feynman's Tips Release QA

## Completed

- Full text recovered from `pdf-text-pages.json` by TOC page ranges.
- Full Russian translation completed with `gemini-3.5-flash-low`.
- Two model-refusal chunks were repaired by smaller subchunk translation.
- EN and RU LaTeX builds compile with LuaLaTeX.
- Reflow PDFs use body-page geometry: `396 x 594 bp`.
- Text layer verified with PyMuPDF.
- TOC/bookmark links verified by link counts.
- Visual spot-check contact sheet generated.

## Current Outputs

- EN source PDF: `en/feynmans-tips-on-physics-2013-source.pdf`
- EN reflow PDF: `en/feynmans-tips-en-reflow.pdf`
- RU reflow PDF: `ru/feynmans-tips-ru-gemini-3.5-flash-low.pdf`
- Visual QA: `reports/visual-qa/tips-release-contact-sheet.png`

## Known Limits

- Reflow layout is editable and readable, but not page-exact.
- Original figures/diagrams are not yet restored into the reflow PDFs.
- Formula quality is limited by the PDF text layer; common symbols are TeX-mapped,
  but full semantic equation reconstruction is a separate pass.
- Dense exercise/index pages still produce normal TeX underfull/overfull warnings.
