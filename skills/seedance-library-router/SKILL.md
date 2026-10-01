---
name: Seedance Library Router
description: Thin router for Seedance 2.0/2.5 prompt work inside ai-video-library. Use when the user asks for Seedance/即梦/火山方舟 video prompts, @Image/@Video reference binding, first-last frame, fight openings, or community agent-skill structures — point to library paths; do not paste skill-repo dumps.
---

# Seedance Library Router（薄路由 · 不复制提示词正文）

> **2026-10-01（非原文）：** 本 skill 只指路。权威与去重以库内文档为准；社区 agent-skill 仅作结构补丁，见 `prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md`。

## When to use

- User wants **Seedance / 即梦 / 火山方舟** video prompts, reference binding, extend/补齐, fight beat, or “agent skill” structure.
- Inputs: model era (2.0 vs 2.5), refs, duration/aspect, genre.

## Authority order (do not invert)

1. Official Volcengine → `docs/权威来源.md` §2.1；cold tricks → `prompts/技巧锦囊/35-volcengine-seedance2-guide-tricks.md`
2. Library rulings → `docs/最佳实践.md`；first/last frame → `docs/首尾帧工作流.md` + `prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md`
3. Official structure examples → `prompts/提示词写法/32-runway-seedance-2.0-prompt-guide.md`、`prompts/提示词写法/33-official-vendor-video-examples.md`
4. Fight / camera corpora → `prompts/打斗运镜/32–34`、`prompts/运镜/*`、`skills/fight-camera-motion-prompts/SKILL.md`
5. Community structure patch only → `prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md`（Emily carriers / reference ignore / allocation；dexhunter `@` roles；beshuaxian 2s fight hook）
6. Secondary source registry → `docs/权威来源.md` §6
7. Hell Grind spatial/acting/IMAGE patch → `prompts/技巧锦囊/46-hell-grind-cinedance-acting-lira-synthesis.md` + `skills/hell-grind-library-router/SKILL.md`（§7 registry）

## Hard rules

- **Do not** clone or wholesale-copy Emily2040/seedance-2.0、dexhunter/seedance2-skill、beshuaxian/higgsfield-seedance2-jineng、Hell Grind CINEDANCE/ACTING/LIRA full texts into `prompts/`.
- **Do not** restate 双胞胎 / 轨道补齐 / 发力链 as if new — already in `35` / `最佳实践` / `打斗运镜/32`.
- Mark community tips as **社区说法**; if they conflict with §2.1 official docs, keep official.
- Seedance **2.0**: prefer `镜头N` over precise `0–3s` timestamps; **2.5** may use integer-second stamps (`docs/最佳实践.md` §4).

## Minimal checklist before delivering a prompt

- [ ] Model era chosen (2.0 镜头序号 vs 2.5 时间戳)
- [ ] Each ref has one job + mapping line (official); optional ignore clause (`45` §3)
- [ ] One primary camera move per shot; action concrete (or 发力链 if fight)
- [ ] If narrative: carriers only, no pasted “power shift / subtext” labels (`45` §2)
- [ ] If fight open: who/distance/weapon/energy readable in first beat (`45` §6 + `打斗运镜/32`)
