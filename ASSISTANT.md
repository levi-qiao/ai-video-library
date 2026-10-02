# ASSISTANT.md · Compatibility Entry

> Canonical agent instructions now live in [AGENTS.md](AGENTS.md). This file remains as a compatibility entry for tools or users that already reference `ASSISTANT.md`.

## Use the knowledge base

Before answering repository-grounded AI-video tasks, follow `AGENTS.md`.

For prompt creation or optimization, the minimum path is:

`TEMPLATES.md → CAPABILITIES.md → COMPILER.md → PLAYBOOK.md → docs/最佳实践.md`

Use `CORE-PICKS.md` only when a representative mother example helps. Use `index.jsonl`, `prompts/`, and `cases/` only when exact evidence, original text, or a missing component is needed.

## Important

- `skills/` route tasks into the canonical knowledge graph; they do not override it.
- Do not duplicate rules from skills into answers when a canonical rule exists.
- Give a copy-ready result first unless the user explicitly asks for a tutorial or audit.
- Preserve source/authority boundaries and model uncertainty.

See [AGENTS.md](AGENTS.md) for the full agent contract.
