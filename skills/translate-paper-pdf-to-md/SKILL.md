---
name: translate-paper-pdf-to-md
description: Convert or translate academic PDF papers into traceable Markdown while preserving complete page text, page anchors, figures through rendered source pages, equations, citations, references, document structure, and terminology. Use before any repository task reads, summarizes, compares, or cites a PDF in references; use for batch PDF-to-Markdown synchronization and localized paper readers.
---

# Translate Paper PDF to Markdown

Adapted from [LiuMengxuan04/translate-paper-pdf-to-md](https://github.com/LiuMengxuan04/translate-paper-pdf-to-md) for repository-first, loss-aware conversion.

## Output contract

- Main file: `references/Markdown/<paper-stem>/<paper-stem>.md`.
- Assets: `references/Markdown/<paper-stem>/assets/pages/`.
- Metadata: `references/Markdown/<paper-stem>/conversion.json`.
- Work files: `tmp/pdf-to-md/<paper-stem>/`; delete after validation.

Keep the source PDF. Markdown is the primary reading/indexing artifact; the PDF remains the visual authority when extraction is ambiguous.

## Repository workflow

1. Run `python scripts/batch_convert_references.py --root <repo>` before reading PDFs in `references/`.
2. Convert only PDFs whose hash differs from `conversion.json`; remove generated Markdown directories for deleted PDFs.
3. Apply the engine policy in `references/engine-policy.md`: Poppler is the default page-aware extractor/renderer; MarkItDown is a structure and coverage comparator; pypdf is an independent text-coverage oracle; PDFium is the visual comparison renderer. Escalate complex/scanned pages to MinerU only when the local engines fail their thresholds.
4. Preserve every source page under a stable `<!-- source-page: N -->` anchor. Do not silently omit pages with little/no extractable text; retain their rendered page image.
5. Preserve source-language text by default for lossless indexing. When the user requests localization, add a target-language reading layer without replacing the source text.
6. Preserve section order, citations, references, variables, system names, datasets, and URLs. For every mathematical expression, prefer the paper's verified TeX source and emit inline math as `$...$` and display math as `$$...$$`; never present PDF glyph extraction as a canonical formula. Store a complete canonical formula registry in the paper Markdown and record its source/count in `conversion.json`. Use formula OCR only when verified TeX is unavailable, and require manual visual review before acceptance.
7. Run `python scripts/validate_markdown_assets.py <paper.md>`, `validate_text_encoding.py <paper.md>`, `validate_vscode_preview.py <paper.md>`, `validate_mpe_repository.py --root <repo>`, `validate_conversion.py`, and `generate_quality_report.py`. The encoding check must reject malformed UTF-8, replacement characters, C0/C1 controls, unresolved private-use glyphs, and common mojibake markers. Accept only after Markdown Preview Enhanced-compatible Markdown-it parsing, YAML/fence/image checks, zero encoding/KaTeX errors, page/hash checks, and source-PDF visual sampling pass.
8. Run `python scripts/cleanup_artifacts.py --root <repo>` after validation. Keep final Markdown, page assets, conversion metadata, and quality report; remove obsolete conversions, work trees, failed local tool environments, QA images, raw extractor files, and legacy exports.

## Reading rule

Never feed an entire PDF or entire converted paper into context by default. Search the Markdown with `rg`, read the relevant sections and page anchors, then inspect only the corresponding page images or PDF pages when layout matters.

## Localization profile

If localization is requested and preferences are absent, ask briefly for locale, field, reader/tone, terminology, and figure/table handling. If immediate work is requested, use faithful academic Chinese, preserve English key terms on first use, keep original figure labels, translate captions, and keep bibliography entries in the source language.

Read `references/engine-policy.md` and `references/mpe-math-policy.md` before conversion, then read `references/quality-checklist.md` before acceptance.

## Markdown preview compatibility

- Do not emit raw HTML anchors or hundreds of repeated formula headings. Use plain Markdown labels such as `**Formula F0001**`.
- Do not carry publisher layout commands into formulas. Expand custom macros; remove color, scaling, phantom, tag, and numbering commands; wrap alignment tabs in `aligned`.
- Scan `.tex`, `.sty`, and `.cls` for macro definitions, but extract mathematical content only from `.tex` source files.
- Treat a VS Code KaTeX parse error as a conversion failure. Never suppress or merely configure away formula errors.
- Markdown Preview Enhanced is the repository preview authority. Validate every repository `.md` file for strict UTF-8, YAML front matter, balanced fences, local image resolution, Markdown-it parsing, note-size limits, and KaTeX rendering before acceptance.
- Reject unmatched or empty dollar delimiters, whitespace-padded inline math, `\(...\)`/`\[...\]`, and mathematical environments outside dollar delimiters. Render every detected expression with KaTeX using `throwOnError: true`, `strict: error`, and `trust: false`; do not accept a file merely because malformed math was skipped by extraction.
- Normalize known PDF private-use math glyphs to standard Unicode only in searchable page text. If a line contains an invalid font map or cannot be decoded without guessing, omit that line, emit one extraction warning, and preserve the rendered page; never invent the missing text.
