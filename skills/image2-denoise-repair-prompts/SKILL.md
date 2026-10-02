---
name: Image Cleanup / Repair Prompt Router
description: Use for image cleanup, denoise, artifact repair, detail preservation, or preparing clean image-to-video reference frames.
---

# Image Cleanup / Repair Prompt Router

Read `AGENTS.md` first.

## Route

1. `PLAYBOOK.md` for concrete visible descriptions and preservation logic.
2. `docs/最佳实践.md` for current image-model behavior.
3. `docs/首尾帧工作流.md` when preparing video reference frames.
4. `index.jsonl` → `prompts/生图修画质/` for source components and historical/community parameter guidance.

## Modes

- **Generate clean:** prioritize subject, controlled detail distribution, material/light behavior, simple background.
- **Edit/repair:** explicitly separate KEEP LOCK from CLEAN OPS; preserve identity, composition, pose, palette and camera unless the user asks to change them.

Numeric denoise values in source material are workflow/community parameters, not universal prompt syntax. Negative prompting is model-dependent.

## Output

Return one concise generation or edit instruction first. Do not turn historical cleanup snippets into a giant negative list.
