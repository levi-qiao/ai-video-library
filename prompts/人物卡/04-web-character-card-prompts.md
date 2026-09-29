# 04 Web — Character asset sheet / character card prompts (人物资产图 / 人物卡)

> body: verbatim — full original prompt text only; no summary/teaser.

Collected 2026-09-29 Asia/Shanghai. **Verbatim** public prompts only. Language + URL labeled. No invented prompts.

**Douyin「心流」:** short links `v.douyin.com/F0CQtRHUZQk/`, `bV59188e3cE/`, `UP3Ck9IsM_U/` redirected to iesdouyin/douyin share shells; **no readable prompt text** via WebFetch/curl (see `00-source-fetch-log.md`). Below are public Midjourney / Flux / SD character-sheet samples in the same product niche.

---

## 2) Midjourney 人设图 / 三视图 / Q版表情包 (IPIPP)

- **Language:** en (prompt body)
- **Source:** https://www.ipipp.com/html/20260904/50447.html

### 2.1 角色人设图
```text
character design sheet of a young witch girl,
silver short hair, amber eyes, black witch hat with gold trim,
navy blue cloak, holding a magic staff,
full body, standing pose, clean white background,
anime style, soft shading, high detail
--ar 3:4 --niji 6
```

### 2.2 三视图 turnaround + cref
```text
character turnaround sheet, three views of the same character,
front view, side view, back view,
a young witch girl, silver short hair, amber eyes,
black witch hat with gold trim, navy blue cloak,
T-pose, consistent lighting, white background,
anime style --ar 16:9 --niji 6
--cref 目标人设图的图片链接 --cw 100
```

### 2.3 Q版表情包 sticker sheet
```text
chibi version of the same character, sticker sheet,
a young witch girl, silver short hair, amber eyes,
black witch hat with gold trim, navy blue cloak,
multiple expressions: happy, angry, crying, surprised, winking,
9 emojis on one sheet, white border around each,
simple pastel background, kawaii style
--ar 1:1 --niji 6 --cref 人设图链接 --cw 60
```

---

## 3) Character Design Sheet LoRA layouts (Flux / Illustrious / Pony / SD)

- **Language:** en
- **Source:** https://www.qpipi.com/87930/

### 3.1 FLUX recommended layout
```text
CharacterDesignFLUX, reference sheet, white background, simple background, multiple views, upper body, front, from side, color palette reference, high_detailed, captured in high detail, (all character characteristics), magic particles, multiple references
```

### 3.3 Illustrious compact prefix
```text
highres, hi res, best quality, masterpiece, intricate details, absurdres, 4k, semi realistic,, CharacterDesignIllustrious, reference sheet, simple white background, (color guide:1.2), (multiple views), (full body), dynamic pose
```

### 3.4 Trigger words (FLUX / shared)
```text
(CharacterSheet:1)
(multiple views, full body, upper body, reference sheet:1)
high_detailed, captured in high detail
magic particles, multiple references
```

### 3.6 Community reply — multi-view SD/PDXL example (same page comments)
```text
Prompt: character design sheet, front view, side view, back view, turnaround sheet, multiple views, uniform grid, clean lines, flat color, concept art, white background
```

---

## 4) Melon Hub — concept → turnaround templates

- **Language:** en (templates); article zh
- **Source:** https://melon-hub.com/guides/character-design-prompts

### 4.2 SD / Flux positive
```text
1girl, solo, full body, standing, front view, 
silver long hair, blue eyes, mechanical arm, navy military coat, 
red scarf, confident expression, anime illustration, 
clean lineart, soft cinematic lighting, simple background
```

### 4.3 SD / Flux negative
```text
multiple views, extra limbs, bad anatomy, 
blurry, watermark, text, low quality, deformed hands
```

### 4.5 Expression sheet phrase (article)
```text
expression sheet, 9 expressions in grid, smiling, angry, crying, surprised, embarrassed, calm, smug, sleepy, screaming, same character
```

### 4.7 Style stack example (国风修仙)
```text
anime illustration, ink wash aesthetic, clean lineart with soft shading, inspired by Honkai Star Rail character design
```

---

## 5) Lovart blog — workflow, almost no copy-paste prompts

- **Source:** https://www.lovart.ai/zh/blog/ai-character-design
- **Status:** Strong 人物资产系统 narrative (转面图/表情表/Brand Kit). **No** substantial fenced Midjourney/Flux prompt samples recovered. Do not invent; leave empty of fake prompts.

Example of non-prompt instruction style on page (quoted as prose, not a model prompt):  
「@reference turnaround.jpg。这个角色在 [场景/表情/姿势] 中」— template phrase only.

---

## 6) Douyin「心流」blocker

| Short link | Redirect | Prompt text |
|------------|----------|-------------|
| https://v.douyin.com/F0CQtRHUZQk/ | iesdouyin share **user** page | none |
| https://v.douyin.com/bV59188e3cE/ | note `7670845777770047338` | none |
| https://v.douyin.com/UP3Ck9IsM_U/ | video `7659111522644810153` | none |

Needs browser/app to recover creator overlays/captions.

---

## Verbatim prompt count (this file)

| Section | Fenced blocks |
|---------|--------------:|
| 2 IPIPP MJ (filled witch) | 3 |
| 3 Qpipi LoRA (layout / triggers, not unfilled shells) | 4 |
| 4 Melon Hub filled lines | 4 |
| **Total** | **11** |

Evening QC 2026-09-29 removed unfilled `[identity anchor]` / `[角色身份]` / `[角色 ID]` shells, the “NEXT THE BASE PROMPT … etc.” layout, the Illustrious trigger subset of §3.4, and the outfit-list phrase with no character.
