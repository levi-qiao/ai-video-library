---
name: Fight / Action Video Prompt Router
description: Use for fights, chases, duels, weapon combat, impact design, hyper-speed exchanges, combat camera, or combat VFX.
---

# Fight / Action Video Prompt Router

This is a thin adapter into the repository knowledge graph. Read `AGENTS.md` first. Do not treat this file as an independent fight-prompt handbook.

## Route

1. `TEMPLATES.md` → choose fight skeleton and timing mode.
2. `CAPABILITIES.md` → choose 3–5 capabilities.
3. `COMPILER.md` → compile the request.
4. `PLAYBOOK.md` → action causality, camera readability, impact and VFX rules.
5. `docs/最佳实践.md` → target-model syntax/limitations.
6. `CORE-PICKS.md` → at most one primary + one secondary mother example.
7. Only then use `index.jsonl` / `prompts/打斗运镜/` for exact source evidence or missing vocabulary.

## Diagnose before writing

Map the symptom, not the nearest old prompt:

- weak impact → force/contact/reaction/contact-point readability;
- standing combat → continuous pursuit/terrain route/re-entry;
- “one second several hits” → hyper-speed exchange mode, not readable-heavy-hit mode;
- pasted VFX → trajectory/contact anchoring + physical/environment response;
- chaotic camera → one main camera intention; keep the fastest exchange more readable than the weapons;
- flat climax → light/heavy/finisher hierarchy.

## Fight invariants

Use the current rules in `AGENTS.md` and `PLAYBOOK.md`. In particular, never restore the old universal rule that every high-intensity segment must contain only 1–2 moves. That rule applies to readable heavy-hit segments, not hyper-speed exchange bursts.

Sub-second counts express rhythm density unless the target model explicitly supports reliable timing control.

## Output

Return the usable prompt first. Do not expose capability labels in the final prompt. If the user asks why, explain only the few routing decisions that changed the result.
