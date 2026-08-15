---
name: manage-references-knowledge
description: Incrementally build and maintain the repository references knowledge base, prerequisite learning path, source ledger, knowledge graph, PDF-derived Markdown corpus, and references/Knowledge graph/PINE.md. Use whenever the user asks to create, update, refresh, check, or synchronize the references knowledge base or says “更新references知识库”.
---

# Manage References Knowledge

Maintain `references/Knowledge graph/` as a source-grounded learning system.

## Required workflow

1. Treat top-level files in `references/` as source artifacts. Exclude generated `references/Markdown/` and `references/Knowledge graph/` from source discovery.
2. Run `python scripts/reference_inventory.py --root <repo>` and read `change-report.json`.
3. Run `python skills/translate-paper-pdf-to-md/scripts/batch_convert_references.py --root <repo>` and then `validate_conversion.py`. For deleted PDFs, remove their generated Markdown directory.
4. Search and read the corresponding files under `references/Markdown/`; do not extract or ingest PDF text directly. Use `rg` and page anchors to load only relevant ranges. For mathematics, follow `../translate-paper-pdf-to-md/references/mpe-math-policy.md`, use only the canonical LaTeX formula registry, and inspect linked page images or the source PDF to verify formula context, numbering, tables, or figures.
5. Re-read every added or changed Markdown paper for its problem, assumptions, method, equations, evidence, limitations, and prerequisites. Remove deleted-source claims and graph edges unless retained evidence supports them.
6. Search broadly for missing prerequisites and current bibliography. Prefer original papers, official project/code pages, textbooks, standards, and official documentation. Record URL and access date in `06-source-ledger.md`.
7. Update affected knowledge Markdown and `graph.json` in easy-to-hard order: mathematics/control, ML, MDP/RL, imitation and offline RL, sequence/action modeling, VLA/foundation policies, real-robot systems.
8. Check both directions of the knowledge chain: every advanced node has prerequisites and every prerequisite serves a downstream node.
9. Run `python scripts/validate_knowledge.py --root <repo>` and `python skills/translate-paper-pdf-to-md/scripts/validate_mpe_repository.py --root <repo>`; fix every error and review every warning. Markdown Preview Enhanced is the final preview/compilation authority for all repository Markdown. Validation includes strict UTF-8/mojibake checks, YAML/fence/image checks, Markdown-it parsing, delimiter integrity, legacy/bare-math rejection, and strict untrusted KaTeX rendering.
10. Run `python scripts/build_pine_md.py --root <repo>` to regenerate `references/Knowledge graph/PINE.md`, then validate it is current and contains all chapters.
11. Run inventory with `--accept` only after all checks pass, then run `python skills/translate-paper-pdf-to-md/scripts/cleanup_artifacts.py --root <repo>`. Confirm extraction work, QA renders, failed local environments, duplicate exports, deleted-source conversions, and obsolete `PINE.docx` are gone.

## Content contract

- Explain for each paper: problem, difficulty, idea, formal mechanism, data/training/inference flow, evidence, limits, prerequisites, and relationships.
- Cite exact quantitative claims; weaken claims that cannot be verified.
- Use stable source IDs from `manifest.json` and stable concept IDs from `graph.json`.
- Paraphrase; do not copy long passages.
- Never silently accept a hash change. The converted Markdown hash linkage must pass before knowledge work begins.

Read `references/content-schema.md` before adding a new paper family.
