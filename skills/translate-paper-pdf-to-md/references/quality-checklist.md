# Quality checklist

## Completeness

- Source hash, page count, converter, and timestamp exist in `conversion.json`.
- Markdown contains one ordered `source-page` anchor for every PDF page.
- Empty/text-poor pages retain a page image and an extraction warning.
- Abstract, major sections, captions, acknowledgments, and references remain discoverable.
- Citation brackets, equation variables, URLs, model names, datasets, and bibliography text are not normalized away.

## Encoding integrity

- Every Markdown file decodes as strict UTF-8.
- No replacement character, C0/C1 control, unresolved private-use glyph, or common mojibake sequence remains.
- Known private-use mathematical glyphs are normalized only in searchable page text; canonical mathematics comes from the TeX formula registry.
- Invalid custom-font lines are marked as omitted and remain recoverable through the linked rendered page, never guessed.

## Asset integrity

- Every Markdown image link resolves.
- Page images are legible and use stable zero-padded names.
- No page image, axis, legend, table row, or formula is cropped.

## VS Code preview

- Every `$...$` and `$$...$$` expression renders under the MPE-compatible KaTeX baseline with `throwOnError`, strict mode, and trust disabled.
- No unmatched/empty delimiter, whitespace-padded inline formula, `\(...\)`/`\[...\]`, bare math environment, or unescaped prose dollar remains.
- Display delimiters occupy their own lines; multi-line environments remain inside `$$...$$`.
- No custom paper macro, alignment tab outside `aligned`, nested dollar delimiter, publisher color, scaling, phantom, or unsupported environment remains.
- Generated navigation uses Markdown labels and comments, not raw HTML anchors or repeated headings.
- The complete file parses successfully as CommonMark with HTML disabled or unnecessary.

## Reading efficiency

- Top-level metadata and a generated section index support `rg`/heading navigation.
- Each page is independently addressable without loading the whole paper.
- The knowledge workflow reads only relevant Markdown ranges and opens page images only for layout-dependent evidence.

## Cleanup

- Final output contains only `.md`, `conversion.json`, and referenced assets.
- Extraction work directories, duplicate renders, temporary text, and crop specifications are deleted after validation.
