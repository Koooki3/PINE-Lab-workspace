# Multi-engine conversion policy

## Default pipeline

1. Use Poppler `pdfinfo`, `pdftotext -layout`, `pdftotext -raw`, `pdfimages -list`, and `pdftocairo` from the isolated ASCII-path environment at `%USERPROFILE%/.codex/tools/pdf-md-env`.
2. Run Poppler against an ASCII temporary copy on Windows; copy validated results back to the repository. This avoids Unicode-path failures in font maps and output files.
3. Build one source-faithful Markdown page per PDF page with stable anchors and a full rendered page asset.
4. Use pypdf as an independent token-coverage baseline. A unique-word recall below 90% triggers manual review; below 80% triggers a different backend.
5. Use PDFium to render a sample from the source independently. Compare at least the first page, one method/equation or experiment page, and the last/reference/appendix page of every paper.

## MarkItDown role

Use Microsoft MarkItDown only as a secondary comparator for headings and missing text. Its official documentation positions output for text analysis rather than high-fidelity conversion. Do not replace page-aware Poppler output with MarkItDown plain text. Merge only a clearly missing, source-verified block; never append the complete second extraction because that duplicates tokens.

## MinerU escalation

The robust-vase MinerU workflow contributes useful design rules: immutable English source Markdown, page anchors, SHA-256 metadata, separate localized output, optional OCR/hybrid backend, and automatic raw cleanup. On this Windows repository, do not install its roughly 5 GB model stack by default. Escalate to MinerU in Linux/WSL only when pages are scanned, formulas/tables are structurally unusable, or Poppler coverage/visual checks fail.

## Acceptance thresholds

- Source hash current; PDF page count equals anchors and rendered assets.
- No missing asset links or empty page without a warning and rendered source page.
- pypdf cross-token recall at least 90%, or a documented page-level explanation and manual source check.
- Visual sample shows no crop, missing figure, color failure, obvious symbol loss, or column displacement.
- Precise formula/table claims continue to cite and inspect the linked source page.

## Sources

- LiuMengxuan04 translate-paper-pdf-to-md: https://github.com/LiuMengxuan04/translate-paper-pdf-to-md
- Microsoft MarkItDown: https://github.com/microsoft/markitdown
- MarkItDown guide supplied by the user: https://dashen-tech.com/dev-tools/markitdown-guide/
- robust-vase MinerU skills: https://github.com/robust-vase/PDF-To-MarkDown-skills
