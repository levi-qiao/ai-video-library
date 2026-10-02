---
name: Character Asset Card Prompt Router
description: Use for character sheets, turnarounds, expression grids, outfit variants, identity reference assets, or character-consistency preparation.
---

# Character Asset Card Prompt Router

Read `AGENTS.md` first.

## Route

1. `TEMPLATES.md` / `PLAYBOOK.md` for prompt structure and identity locks.
2. `docs/最佳实践.md` for current model-specific reference-image behavior.
3. `docs/首尾帧工作流.md` when the asset will feed image-to-video.
4. `index.jsonl` → `prompts/人物卡/` for exact reference components or source evidence.

## Invariants

Lock a small stable identity anchor: face/hair/key costume or signature feature. Separate the utility asset goal (turnaround, expression, outfit, single reference portrait) from decorative key art.

Do not assume that a multi-view sheet is the best video reference. Follow current model guidance in `docs/最佳实践.md`.

Model parameters and negative-prompt behavior must come from current model guidance, not old examples embedded in source material.

## Output

Give the requested asset prompt first, with layout and identity locks explicit. Add model-specific parameters only when supported.
