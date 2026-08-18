---
name: use-openpi-knowledge
description: Use the repository's source-grounded openpi knowledge graph for Chinese learning, code navigation, dataset adaptation, model selection, training, inference, deployment, and kooki environment checks. Use for tasks about this checkout's openpi library; re-check source when current behavior or versions matter.
---

# Use openpi Knowledge

Start with `openpi_knowledge/graph.json` to identify the relevant layer, then read only the matching sections of `openpi_knowledge/openpi.md` and `openpi_knowledge/sources.md`.

## Operating rules

- Treat local `openpi/` source and its commit as implementation truth; distinguish it from paper claims and upstream-current behavior.
- For data integration, verify raw keys, coordinate frames, action semantics, episode boundaries, action horizon, and training/inference normalization symmetry.
- For model questions, distinguish π0 flow matching, π0.5 flow matching, and π0-FAST autoregressive tokenization; do not claim unsupported PyTorch features.
- For deployment, trace the full path: platform adapter → transforms → Policy → server/client → safety controller.
- Use Conda environment `kooki` for routine repository Python work. Before dependency changes, inspect `openpi/pyproject.toml`, Python/OS/GPU support, and current `pip check` output.
- Do not describe Windows `kooki` as full openpi GPU support. Full JAX/CUDA and RLDS work should use an Ubuntu/WSL2 Python 3.11 environment unless upstream support changes.
- Never send unvalidated learned actions directly to hardware; require bounds, timeout, emergency stop, low-speed trial, and logged closed-loop tests.

## Refresh triggers

Refresh the knowledge base when the openpi commit, dependency lock, model list, checkpoint table, data format, or deployment protocol changes. Record the new commit and rerun repository Markdown and skill validation.
