# Content schema

Paper pages contain: bibliographic record; one-sentence position; problem and assumptions; prerequisite bridge; method and equations; data/training/inference flow; evidence; limitations; reproducibility pointers; graph relationships; beginner checklist.

Graph relations: `requires`, `uses`, `extends`, `enables`, `contrasts-with`, and `evaluated-on`. Every edge needs a concise `why`. Concept IDs use lowercase kebab-case; paper nodes carry a `source_id` matching `manifest.json`.

Evidence levels are `primary-local`, `primary-web`, `secondary`, and explicitly labeled `synthesis`.
