---
name: save-task-prompts
description: Archive every repository task's verbatim user prompt with rich YAML metadata, optional normalized prompt, version history, deduplication, JSON indexing, validation, and cleanup. Use automatically for every user task in this repository and whenever users ask to save, manage, search, update, or repair the prompt repository.
---

# Save Task Prompts

Archive task prompts in `prompt-repository/` before finishing every repository task.

## Workflow

1. Read `templates/prompt-template.md` and preserve the full user input exactly in `source_prompt` and “完整提示词”. Never summarize, correct, or redact ordinary content. If a likely secret appears, omit it and record the redaction in notes.
2. Classify the prompt under one primary directory: `research`, `coding`, `writing`, `education`, `career`, or `general`.
3. Use filename `PROMPT-YYYYMMDD-HHMMSS-slug.md` and the same timestamp-based ID. If a collision occurs, increment the timestamp suffix without overwriting.
4. Populate required metadata: `id`, `name`, `slug`, `description`, `tags`, `language`, `model`, `created_at`, `updated_at`, `version`, and original prompt.
5. Keep `source_prompt` verbatim. Add `normalized_prompt` only when it improves reuse; label it as derived and never replace the source.
6. For an intentional revision of a saved prompt, create a new semantic version record or update only the normalized prompt and changelog. Preserve original source content and timestamps.
7. Run `python scripts/rebuild_prompt_index.py --root <repo>`, `python scripts/validate_prompt_repository.py --root <repo>`, and `python skills/translate-paper-pdf-to-md/scripts/validate_mpe_repository.py --root <repo>`; fix all errors. Archived prompt Markdown must preview under Markdown Preview Enhanced without invalid YAML, unbalanced fences, encoding errors, missing images, unmatched/legacy math delimiters, bare math environments, or strict KaTeX failures. Preserve formula-like text inside the verbatim prompt in a fenced `text` block so it is not reinterpreted as output mathematics.
8. Delete temporary extraction, draft, comparison, and rendering files. Preserve only prompt Markdown, template, JSON index, skill files, and user-requested exports.

## Duplicate policy

The index stores a SHA-256 hash of the verbatim prompt. Still archive repeated task inputs for auditability, but set `duplicate_of` to the earliest matching prompt ID. Do not overwrite or silently discard.

## Scope

Archive user task instructions and substantive follow-up instructions. Exclude conversational acknowledgements, yes/no approvals, credentials, system/developer instructions, and tool results.
