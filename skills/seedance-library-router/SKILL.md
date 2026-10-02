---
name: Seedance Knowledge Router
description: Use for Seedance / 即梦 video prompting, reference usage, model-era syntax, timing, fight prompting, and model-specific optimization.
---

# Seedance Knowledge Router

Read `AGENTS.md` first. This is a model adapter, not a separate Seedance knowledge base.

## Route

1. `docs/最佳实践.md` — current canonical Seedance rulings and model-era differences.
2. `TEMPLATES.md` + `CAPABILITIES.md` — task structure and capability selection.
3. `COMPILER.md` — generation/rewrite pipeline.
4. `docs/首尾帧工作流.md` — reference/first-last-frame workflows.
5. `CORE-PICKS.md` — representative structures when needed.
6. `index.jsonl` and Seedance-related source files — exact evidence only.

## Rules

Do not hard-code old Seedance behavior in this skill. Model syntax and reference limits change; `docs/最佳实践.md` is the repository ruling layer.

When the target version is unknown, avoid inventing precise timing or reference syntax. Preserve user intent with generic shot labels until the version is known or a generic answer is sufficient.

For fights, use the current heavy-hit vs hyper-speed timing distinction from `AGENTS.md` / `PLAYBOOK.md`.

## Output

Apply Seedance adaptation after the generic prompt blueprint is sound. Do not let model syntax replace action causality, identity, space, camera readability, or environment continuity.
