---
name: Character Asset Card / Sheet Prompts
description: Use when generating character design sheets, turnarounds, expression grids, outfit variants, or locked identity portrait cards for games/IP — consistent face anchors across panels.
---

# Character Asset Card / Sheet (人物资产图 / 人物卡)

> **2026-09-30 整合说明（非原文）：** 本 skill 中「Source grounding」里的 `raw/…` 路径和「§」编号指早期 raw 草稿，库内对应文件为 `prompts/人物卡/04-web-character-card-prompts.md`（整合后章节号可能不同）。术语口径以 `docs/术语速查.md` 为准，写法冲突的裁定见 `docs/最佳实践.md`。


> **2026-09-30 官方文档复核（非原文，出处见 `docs/权威来源.md`）：**
>
> - **Midjourney `--cref` / `--cw` 是旧参数。** MJ 官方：「Character Reference is a feature compatible with Midjourney and Niji version 6. It allows you to recreate a specific character in multiple images, but was replaced by Omni Reference in V7, and the Edit Model in V8.X.」下面的 `--niji 6 --cref … --cw` 模式只适用于 V6 / Niji 6；V7 用 `--oref`，V8.X 用 Edit Model（最多 4 张参考图）。
> - **`--style raw`：** MJ 现行参数表写的是 `--raw`（Raw Mode）；`--style raw` 这种写法是否仍被接受，本轮未核实【?】。
> - **三视图 / 多视图设定图不要直接当视频参考。** Seedance 2.0 官方不建议用人物多视图作参考（易出「双胞胎」），改用大头照 + 全身照；Seedance 2.5 在 1–5 个主体时可用多视图；Gemini 建议逐个角度迭代生成单视图。见 `docs/最佳实践.md` 第 8 节「三视图 / 多视图作参考」。
> - **负面提示看模型。** 下文「Negatives」一栏适用于有负面字段的模型（SD3.5 等）；FLUX.2 不支持负面提示，要改写成正面描述；MJ 用 `--no`。见 `docs/术语速查.md` 第 10 节。
> - **画质标签（masterpiece、best quality 等）** 只对按标签训练的模型有意义；官方指南里 Imagen 列出 4K、HDR 等修饰词，Seedream、FLUX 建议简洁、不堆叠。
> - 给图生视频准备角色参考图的做法见 `docs/首尾帧工作流.md` 第 2 节与 `prompts/首尾帧生图/`。

## When to use

> Scope: **visual** asset sheets (turnaround / expression / outfit grids). Not a prose RPG stat-block card; keep name/personality/backstory text outside the image prompt unless the user asks for on-image labels.

- User needs a **character sheet / turnaround / expression pack / outfit row / dialogue portrait** with identity locked across panels.
- Pipelines: Midjourney (--cref/--cw), Flux/SD CharacterDesign LoRAs, concept-art sheets, sticker/chibi packs.
- Inputs needed: identity anchor (hair, eyes, key feature, costume), sheet type, view/pose grid, background, style stack, optional cref URL + cw, aspect.

**Source grounding:** `/workspace/prompt-extract/raw/04-web-character-card-prompts.md` (§1 portrait sheets, §2 IPIPP MJ, §3 Qpipi LoRA, §4 Melon Hub). Douyin「心流」not recovered — see gaps in validation.

## Canonical prompt skeleton

```text
{{sheet_type}}, same character: {{identity_anchor}},
{{layout_spec}},
{{view_or_pose_rules}},
{{background}}, {{lighting}},
{{style_stack}},
{{model_params}}
```

### Identity anchor (always first concrete lock)

```text
{{age_body}}, {{hair}}, {{eyes}}, {{key_feature}}, wearing {{costume}}, holding {{prop}}, {{signature_element}}, {{attitude_pose}}
```

### Sheet-type library (pick one)

| sheet_type | layout_spec (fill) |
|------------|--------------------|
| character portrait / expression sheet | N expressions in a row or AxB grid: {{emotion_list}}; consistent face structure |
| character turnaround sheet | front, three-quarter/side, back (optionally T-pose); identical proportions; orthographic / model sheet |
| character outfit variations | N outfits: {{outfit_list}}; identical face and hair; full body; three-quarter |
| character pose sheet | N idle poses: {{pose_list}}; identical outfit and face |
| character age progression | N ages: {{age_list}}; keep hair color + key feature; consistent bone structure |
| lighting grid | N lighting setups; identical pose and outfit; only lighting changes |
| NPC dialogue portraits | N dialogue states; shoulders-up; slight 3/4; VN/JRPG style |
| hairstyle exploration | face locked, hair variable; N styles |
| chibi / sticker sheet | multiple expressions; N stickers; white border; kawaii |
| hero cover shot | single dynamic three-quarter; world-hint background; key-art |
| CharacterDesignFLUX / Illustrious reference sheet | white/simple bg; multiple views; upper/full body; color palette / color guide |

### Midjourney turnaround + cref pattern (§2.2 / §4.4)

```text
character turnaround sheet of {{identity_anchor}},
front view, side view, back view, three views in one image,
T-pose, neutral expression, plain white background,
orthographic projection, model sheet, design document layout,
{{style_stack}} --ar 16:9 --style raw --cref {{main_sheet_url}} --cw 100
```

### SD / Flux solo concept (§4.2) vs sheet

- **Solo concept:** `1girl, solo, full body, standing, front view, … simple background`  
  Negative often **includes** `multiple views` (because this shot is single).
- **Sheet shot:** positive **requires** `multiple views, reference sheet, turnaround…` — do **not** put `multiple views` in negative.

## Must-have modules

| Module | Content |
|--------|---------|
| Identity anchor | Hair, eyes, key feature, costume — repeated verbatim on every variant |
| Same-character lock | Explicit `same character` / consistent face structure / identical proportions |
| Layout | Grid/row count + named cells (emotions, views, outfits) |
| Neutral stage | Grey/white/plain background; even/flat/soft studio light (unless lighting-grid sheet) |
| Style stack | Medium + reference + craft (e.g. anime illustration, clean lineart, soft shading) |
| Consistency tools | MJ `--cref` + `--cw` (100 for turnaround, ~60 for chibi drift); LoRA triggers |
| Negatives | Extra limbs, bad anatomy, blurry, watermark, text, deformed hands; **not** `multiple views` on sheet prompts |

## Hard negatives / bans (distilled)

From §4.3 and sheet practice:

```text
extra limbs, bad anatomy, blurry, watermark, text, low quality, deformed hands
```

Also avoid:

- Mixing unrelated characters on one sheet without saying so
- Changing face/hair while claiming “same character” (except intentional hairstyle-exploration sheet)
- Busy scenic backgrounds on model sheets (use plain/neutral)
- Putting `multiple views` in the **negative** when the goal **is** a multi-view sheet
- Readable logos/UI unless part of costume design

## Fill-in checklist

- [ ] Sheet type chosen from library
- [ ] Identity anchor fully specified (and reused verbatim)
- [ ] Layout: panel count + labels
- [ ] Background + lighting appropriate to sheet type
- [ ] Style stack (1–3 layers)
- [ ] Aspect / niji / style raw / stylize as needed
- [ ] If continuity: cref URL + cw weight
- [ ] If Flux/IL LoRA: correct trigger + color guide / multiple views
- [ ] Negatives matched to solo vs sheet
- [ ] Optional: separate hero key-art vs utility sheets

## Short examples

**Example A — 4-expression portrait sheet (§1.1)**  
```text
character portrait sheet, same character: silver short hair, amber eyes, black witch hat with gold trim, navy cloak,
4 expressions in a row: neutral, smile, angry, sad, consistent face structure,
neutral grey background, even soft lighting, concept art style, 16:9
```

**Example B — turnaround + cref (§2.2 trimmed)**  
```text
character turnaround sheet, three views of the same character, front, side, back,
young witch girl, silver short hair, amber eyes, black witch hat with gold trim, navy blue cloak,
T-pose, consistent lighting, white background, anime style --ar 16:9 --niji 6 --cref {{url}} --cw 100
```
