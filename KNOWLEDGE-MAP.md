# KNOWLEDGE MAP · Agent Retrieval Map

AI Video Prompt Lab uses layered retrieval so humans and agents share the same source of truth.

| Need | Read first | Then |
|---|---|---|
| Start a context-free session | AGENTS.md | START-HERE.md for human copy/paste patterns |
|---|---|---|
| Write/optimize a prompt | TEMPLATES.md + CAPABILITIES.md + COMPILER.md | PLAYBOOK.md → model best practices |
| Diagnose why a prompt failed | CAPABILITIES.md + PLAYBOOK.md | relevant skill → source evidence |
| Target a specific model | docs/最佳实践.md | compiler + relevant source |
| Find a representative pattern | CORE-PICKS.md | exact prompt only if needed |
| Retrieve by task/model/capability | agent-index.jsonl | index.jsonl for source truth |
| Find original/source material | index.jsonl / INDEX.md | prompts/ or cases/ |
| Learn terminology | docs/术语速查.md | source evidence if disputed |
| Prepare first/last frames | docs/首尾帧工作流.md | character/image skills |
| Contribute/update knowledge | AGENTS.md + CONTRIBUTING.md | regression tests / index build |

## Layer ownership

- **AGENTS.md** owns agent behavior and retrieval policy.
- **TEMPLATES.md** owns reusable structural skeletons.
- **CAPABILITIES.md** owns normalized capabilities and natural-language routing.
- **COMPILER.md** owns prompt compilation flow.
- **PLAYBOOK.md** owns canonical quality rules and conflict resolution.
- **docs/最佳实践.md** owns model-specific rulings.
- **CORE-PICKS.md** owns representative mother-example routing.
- **skills/** own trigger/scope adapters only.
- **prompts/** and **cases/** own evidence/original material, not canonical rules.
- **index.jsonl** owns source/evidence metadata.
- **agent-index.jsonl** is a deterministic derived retrieval view; never hand-edit it.
- **agent-manifest.json** exposes the knowledge contract to external agents.

When knowledge changes, update the owner layer instead of copying the rule elsewhere.
