# AGENTS.md · AI Video Prompt Lab

This repository is a curated, executable knowledge base for AI video prompting. Treat the repository as a knowledge system, not a bag of prompt files.

## Canonical knowledge graph

Read the minimum layer needed for the task:

1. `TEMPLATES.md` — task skeletons and fill-in structures.
2. `CAPABILITIES.md` — maps user symptoms/goals to reusable control capabilities.
3. `COMPILER.md` — canonical pipeline for creating or rewriting prompts.
4. `PLAYBOOK.md` — canonical rules, conflict resolution, vocabulary, and quality criteria.
5. `CORE-PICKS.md` — representative mother examples; borrow structure, never blindly reskin.
6. `docs/最佳实践.md` — model-specific behavior and current rulings.
7. `docs/术语速查.md` — terminology.
8. `index.jsonl` / `INDEX.md` — retrieval index for original material.
9. `prompts/` and `cases/` — evidence/original examples; descend here only when needed.

`skills/` are routing adapters. They are not independent sources of truth. If a skill conflicts with the canonical files above, the canonical files win.

## Default agent workflow

For a new/rewritten/optimized prompt:

`Parse → Route → Retrieve → Blueprint → Materialize → Model-adapt → Lint → Emit`

- **Parse:** identify task, model, duration, aspect ratio, references, identity anchors, core event, preferences, constraints.
- **Route:** choose one skeleton from `TEMPLATES.md` and normally 3–5 capabilities from `CAPABILITIES.md`.
- **Retrieve:** use at most one primary and optionally one secondary mother example from `CORE-PICKS.md`. Search `index.jsonl` only for missing evidence, terminology, or model-specific examples.
- **Blueprint:** define shot/beat state changes before prose.
- **Materialize:** convert capability labels into visible actions, camera behavior, contact, reaction, environment and VFX.
- **Model-adapt:** apply `docs/最佳实践.md`; never invent unsupported model controls.
- **Lint:** check identity, space, causality, camera conflicts, continuity, VFX triggers, model syntax and redundancy.
- **Emit:** give the copy-ready result first. Hide internal routing unless the user asks for analysis.

For explanation/research tasks, skip compilation and retrieve the smallest canonical/evidence set that answers the question.

## Retrieval policy

Do not scan or dump the entire repository.

Use this order:
- reusable output → Templates + Capabilities + Compiler;
- method/diagnosis → Playbook + Capabilities;
- model behavior → Best Practices, then official/source evidence;
- exact original/source → index, then prompt/case file;
- terminology → terminology quick reference;
- specialized workflow → matching skill, which routes back into these canonical layers.

Prefer high-authority and verified material. Authority order:
`target-model official docs > verified original author material > curated community evidence > inference`.

Preserve uncertainty. A community timing trick is not a universal model guarantee.

## Fight/action invariant

Do not collapse all “fast combat” into one rule.

- **Readable heavy-hit mode:** few important actions; show force → contact → reaction.
- **Hyper-speed exchange mode:** short bursts of repeated attack → defense → immediate counter → reposition; minimal recovery. “Several exchanges per second” is a rhythm target, not universal exact timing.
- Fastest exchanges use a relatively readable camera; large reposition may use snap/whip reframing; camera reacts after contact.
- VFX hierarchy: fast path = short thin trail; light contact = localized pop; heavy/finisher = larger particle/environment response.
- Environment state persists after damage.

## Knowledge integrity

- Never silently rewrite third-party original text.
- Distilled rules belong in canonical files, not duplicated across skills.
- Exact duplicates keep one source copy.
- A reskin is a case, not a new methodology.
- If real generation contradicts a distilled rule, update the canonical rule and add/adjust a regression case.
- Do not treat `reference` entries as complete prompts.
- Third-party material keeps its own attribution/license status; repository MIT does not relicense it.

## Contribution / maintenance

When adding indexed source material, run:

```bash
python3 scripts/build_index.py
python3 scripts/build_index.py --check
```

When changing only distilled knowledge, update the canonical file and relevant regression test; do not copy the same rule into every skill.

## Output contract

Default response:
1. usable artifact/prompt first;
2. only the few decisions that materially matter;
3. source paths/evidence only when useful.

Optimize for executable clarity, not apparent comprehensiveness.
