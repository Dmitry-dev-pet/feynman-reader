# Feynman's Tips full DOM hybrid

Full-book build that uses the HTML-DOM rebuild for chapters 1--4 and the older PDF text-layer reflow for PDF-only sections.

- PDF-only section indexes: [0, 1, 2, 3, 4, 5, 6, 7, 8, 13, 14, 15]
- HTML-DOM section indexes: [9, 10, 11, 12]
- DOM figure assets: 82
- PDF-layer figure crops outside DOM chapters: 37
- English PDF: `/Users/dmitry/Project/docs-to-latex/output/analysis/feynman-tips-ru-en/release/tips-ru-en-2026-06-14-v5-dom-hybrid/en/feynmans-tips-en-full-dom-hybrid.pdf`
- Russian PDF: `/Users/dmitry/Project/docs-to-latex/output/analysis/feynman-tips-ru-en/release/tips-ru-en-2026-06-14-v5-dom-hybrid/ru/feynmans-tips-ru-full-dom-hybrid.pdf`

## QA notes

- Chapters 1--4 are rebuilt from the online HTML DOM: text nodes are translated separately, formulas stay as TeX nodes, and figures come from the HTML assets.
- PDF-only sections are inherited from the older PDF text-layer reflow. That includes front matter, interviews, selected exercises, photo credits, and index.
- Known boundary: PDF-only sections can still contain old text-layer/LLM formula artifacts, especially in selected exercises. Fixing those needs a separate non-PDF source or a dedicated exercise cleanup pass.
- Visual QA contact sheets, when generated, live under `reports/visual-qa/`.
