# Markdown Preview Enhanced math policy

Use this policy for every generated or edited repository Markdown file.

## Renderer profile

- Target Markdown Preview Enhanced with `markdown-it` and KaTeX.
- Use `$...$` for inline mathematics and `$$...$$` for display mathematics.
- Do not use `\(...\)`, `\[...\]`, bare TeX environments, or Markdown code spans as mathematical output.
- Escape a literal currency or prose dollar sign as `\$` when it could be parsed as a delimiter.

## Formula construction

- Keep inline formulas on one line with no whitespace immediately inside the delimiters.
- Put display delimiters on their own lines, separated from prose by blank lines.
- Place `aligned`, `gathered`, `matrix`, `cases`, and related environments inside `$$...$$`.
- Use `aligned` for multi-line equations instead of raw alignment tabs.
- Expand document-specific macros. Remove publisher-only layout, color, scaling, phantom, label, reference, numbering, and unsupported package commands unless their visual meaning is preserved with supported KaTeX.
- Keep prose outside math; use `\text{...}` only for short labels. Avoid raw HTML and unsafe URL/image commands in formulas.
- Prefer canonical TeX from the source. Never promote unverified PDF glyph extraction to a formula.

## Acceptance

Run `validate_mpe_repository.py --root <repo>`. Acceptance requires:

- balanced and non-empty delimiters;
- no legacy delimiters or bare math environments;
- every expression renders with `throwOnError: true`, `strict: error`, and `trust: false`;
- no Markdown/YAML/fence/asset/UTF-8 errors;
- source-formula visual comparison when conversion changed mathematical content.

KaTeX is the compatibility baseline because it is stricter than MathJax. Use MathJax only when a user explicitly requires a construct that cannot be represented faithfully in supported KaTeX, and record that renderer dependency.
