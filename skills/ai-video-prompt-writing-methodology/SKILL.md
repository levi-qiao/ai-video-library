---
name: AI Video Prompt Compiler Router
description: Use when the user asks how to write, expand, rewrite, diagnose, or optimize an AI video prompt across supported models.
---

# AI Video Prompt Compiler Router

Read `AGENTS.md` first. This skill routes general prompt-writing tasks into the canonical knowledge base; it does not maintain a second methodology.

## Route

- skeleton → `TEMPLATES.md`
- natural-language need → `CAPABILITIES.md`
- generation/rewrite pipeline → `COMPILER.md`
- canonical writing rules → `PLAYBOOK.md`
- model differences → `docs/最佳实践.md`
- terminology → `docs/术语速查.md`
- representative examples → `CORE-PICKS.md`
- exact original evidence → `index.jsonl` then `prompts/`

## Workflow

For a new or rewritten prompt, execute the compiler flow from `AGENTS.md`: Parse → Route → Retrieve → Blueprint → Materialize → Model-adapt → Lint → Emit.

Ask a clarifying question only when the core event or required source/reference is missing. Optional style, aspect ratio, or model usually should not block a useful generic result.

## Output

Default to one copy-ready prompt. Explain structure only when requested. Do not dump multiple formula variants, stale model tables, or source lists into the answer unless they solve the user's task.
