# Feynman's Tips Release v4 QA

## Completed

- Full text recovered from `pdf-text-pages.json` by TOC page ranges.
- Full Russian translation completed with `gemini-3.5-flash-low`.
- EN and RU LaTeX builds compile with LuaLaTeX.
- Build log has no fatal LaTeX errors, undefined control sequences, emergency stops, or missing-character warnings.
- Reflow PDFs use body-page geometry: `396 x 594 bp`.
- Text layer verified with PyMuPDF stats.
- TOC/bookmark links verified by link counts.
- `119` vector figure crops extracted from the source PDF.
- Figures inserted inline near detected captions where possible.
- Remaining unmatched figures are kept in fallback atlases.
- Visual spot-check contact sheet generated.
- Figure crop sample sheet generated.
- Russian formula post-processing now preserves bare raw TeX commands, numbered equation tails, Cyrillic text inside formulas, and Unicode square-root/superscript fragments.

## Current Outputs

- EN source PDF: `en/feynmans-tips-on-physics-2013-source.pdf`
- EN reflow PDF: `en/feynmans-tips-en-reflow.pdf`
- RU reflow PDF: `ru/feynmans-tips-ru-gemini-3.5-flash-low.pdf`
- Figure assets: `assets/figures/`
- Visual QA: `reports/visual-qa/tips-release-contact-sheet.png`
- Figure QA: `reports/visual-qa/figure-crop-sample-sheet.png`

## Verification

- EN reflow PDF: `172` pages, `365271` text chars, `18` links/bookmarks.
- RU reflow PDF: `212` pages, `370993` text chars, `18` links/bookmarks.
- EN TeX escaped-formula artifacts: zero for `mathbf`, `frac`, `Delta`, `left`, `sqrt`, `int`, `text`, and escaped dollars.
- RU TeX escaped-formula artifacts remaining: `Delta=3`, `sqrt=2`, `text=4`, escaped dollars `9`, mostly in markdown-table or dense exercise/index text.

## Known Limits

- Reflow layout is editable and readable, but not page-exact.
- Inline figure placement is caption-near, not publisher-geometry-exact.
- EN has `117` inline figures and `2` fallback atlas figures.
- RU has `115` inline figures and `4` fallback atlas figures.
- Dense exercise/index pages and LLM markdown tables still need a dedicated table/list normalization pass.
- Full semantic equation reconstruction remains a separate pass; v4 fixes the main escaped-TeX regression rather than claiming publisher-perfect math.

