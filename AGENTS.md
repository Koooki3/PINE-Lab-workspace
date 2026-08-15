# Repository agent instructions

## Mandatory prompt archiving

For every user task in every thread that operates in this repository, use `skills/save-task-prompts/SKILL.md` before finishing the turn.

1. Archive each user task input verbatim, including formatting, in `prompt-repository/prompts/`.
2. Run the skill's index rebuild and validation scripts.
3. Do not archive system/developer messages, secrets, approval replies, trivial acknowledgements, or tool output.
4. Complete prompt archiving even when the main task fails or is blocked.
5. Delete temporary prompt-processing files before finishing. Never alter an existing archived source prompt; create a new version or archive record.

For “更新references知识库” and equivalent requests, also use `skills/manage-references-knowledge/SKILL.md`.
