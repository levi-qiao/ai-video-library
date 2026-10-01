---
name: Hell Grind Library Router
description: Thin router for Higgsfield Hell Grind CINEDANCE / ACTING / LIRA methods inside ai-video-library. Use when the user asks for measurable spatial blocking, first-frame occupancy, camera-side locks, acting under pressure, eye life, master-profile rewrite, states-not-transitions, or Lira-style IMAGE 4-D prompt optimization — point to library paths; do not paste full Hell Grind skill dumps. Note: the agent may already have the full skills installed separately.
---

# Hell Grind Library Router（薄路由 · 不复制 skill 正文）

> **2026-10-01（非原文）：** 本 skill 只指路。权威与去重以库内文档为准；Hell Grind 三技能仅作社区纪律补丁，见 `prompts/技巧锦囊/46-hell-grind-cinedance-acting-lira-synthesis.md`。
>
> **安装说明：** 若 agent 环境已单独安装完整 `cinedance-hell-grind` / `acting-hell-grind` / `lira-image-prompts`，以安装副本为准做生成；**库内不镜像**三份全文。本路由只告诉你库里保留了哪些净新增摘录与官方优先序。

## When to use

- User wants **Hell Grind / CINEDANCE / ACTING / LIRA** style help for Seedance cinematic video or IMAGE prompts.
- Symptoms: empty opening frame, vague “near the car”, flipped camera side, dead eyes, pasted character bible every shot, transition-verb action collapse, or image-prompt optimization workflow questions.

## Authority order (do not invert)

1. Official Volcengine → `docs/权威来源.md` §2.1；cold tricks → `prompts/技巧锦囊/35-volcengine-seedance2-guide-tricks.md`
2. Library rulings → `docs/最佳实践.md`（含 §2.13–14 Hell Grind 净新增）；first/last frame → `docs/首尾帧工作流.md` + `prompts/首尾帧生图/03-*`
3. Seedance community structure (Emily / @ roles / 2s fight hook) → `prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md` + `skills/seedance-library-router/SKILL.md`
4. Hell Grind community patch only → `prompts/技巧锦囊/46-hell-grind-cinedance-acting-lira-synthesis.md`
5. Fight / camera corpora → `prompts/打斗运镜/32–34`、`prompts/运镜/*`
6. Secondary source registry → `docs/权威来源.md` §6（Seedance skills）+ §7（Hell Grind）

## Hard rules

- **Do not** wholesale-copy CINEDANCE (~1330 lines)、ACTING、LIRA into `prompts/`.
- **Do not** restate 双胞胎 / 轨道补齐 / 发力链 / Emily carriers / ignore / 打斗 2 秒钩子 as if new — already in `35` / `45` / `打斗运镜/32` / `最佳实践`.
- Mark Hell Grind tips as **社区说法**; if they conflict with §2.1 official docs, keep official.
- LIRA 4-D is **IMAGE-only**; do not apply Soul/NBP product matrices as Seedance video law.
- Seedance **2.0**: prefer `镜头N` over precise `0:03` timestamps even when CINEDANCE examples use clocks (`docs/最佳实践.md` §4).

## Minimal checklist before delivering a prompt

- [ ] Official model era chosen (2.0 镜头序号 vs 2.5 时间戳)
- [ ] Spatial: measurable distance / contact + first-frame occupancy if characters must be visible (`46` §2)
- [ ] Camera side explicit (`46` §3); optional Emily lock line (`45` §4)
- [ ] If performance: behavior under pressure, eye life, rewrite-not-paste, states-not-transitions (`46` §4)
- [ ] If IMAGE: LIRA 4-D pointer only (`46` §5); character refs / first-last frame still follow library official paths
- [ ] Full skill bodies: use agent install if present — **do not** dump them into the reply or into `prompts/`
