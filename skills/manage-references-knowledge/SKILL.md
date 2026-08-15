---
name: manage-references-knowledge
description: Incrementally build and maintain the repository references knowledge base, prerequisite learning path, source ledger, knowledge graph, and references/Knowledge graph/PINE.docx. Use whenever the user asks to create, update, refresh, check, or synchronize the references knowledge base or says “更新references知识库”.
---

# Manage References Knowledge

Maintain `references/Knowledge graph/` as a source-grounded learning system.

## Required workflow

1. Treat `references/` as the source directory and exclude `references/Knowledge graph/` from discovery.
2. Run `python scripts/reference_inventory.py --root <repo>` and read `change-report.json`.
3. Re-read every added or changed primary artifact for its problem, assumptions, method, equations, evidence, limitations, and prerequisites. Remove deleted-source claims and graph edges unless retained evidence supports them.
4. Search broadly for missing prerequisites and current bibliography. Prefer original papers, official project/code pages, textbooks, standards, and official documentation. Record URL and access date in `06-source-ledger.md`.
5. Update affected Markdown and `graph.json` in easy-to-hard order: mathematics/control, ML, MDP/RL, imitation and offline RL, sequence/action modeling, VLA/foundation policies, real-robot systems.
6. Check both directions of the knowledge chain: every advanced node has prerequisites and every prerequisite serves a downstream node.
7. Run `python scripts/validate_knowledge.py --root <repo>` and fix every error; review every warning.
8. Run `python scripts/build_pine_docx.py --root <repo>`, render the DOCX, inspect every page, and rebuild until clean.
9. Run inventory with `--accept` only after content and rendering pass. Delete extraction, rendering, conversion, and other temporary files.

## Content contract

- Explain for each paper: problem, difficulty, idea, formal mechanism, data/training/inference flow, evidence, limits, prerequisites, and relationships.
- Cite exact quantitative claims; weaken claims that cannot be verified.
- Use stable source IDs from `manifest.json` and stable concept IDs from `graph.json`.
- Paraphrase; do not copy long passages.
- Never silently accept a hash change.

Read `references/content-schema.md` before adding a new paper family.
