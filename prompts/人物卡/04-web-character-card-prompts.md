# 04 Web — Character asset sheet / character card prompts (人物资产图 / 人物卡)

> body: verbatim — full original prompt text only; no summary/teaser.

Collected 2026-09-29 Asia/Shanghai. **Verbatim** public prompts only. Language + URL labeled. No invented prompts.

**Douyin「心流」:** short links `v.douyin.com/F0CQtRHUZQk/`, `bV59188e3cE/`, `UP3Ck9IsM_U/` redirected to iesdouyin/douyin share shells; **no readable prompt text** via WebFetch/curl (see `00-source-fetch-log.md`). Below are public Midjourney / Flux / SD character-sheet samples in the same product niche.

---

## 1) Game character portrait sheets (12 templates)

- **Language:** en
- **Source:** https://aitoolsguidebook.com/zh/articles/game-character-portrait-sheets/

### 1.1 四表情基础 sheet
```text
character portrait sheet, same character: [identity anchor — hair, eyes, key feature, costume], 4 expressions in a row: neutral, smile, angry, sad, consistent face structure, neutral grey background, even soft lighting, concept art style, 16:9
```

### 1.2 八表情扩展 sheet
```text
character expression sheet, same character: [identity anchor], 8 expressions in a 4x2 grid: neutral, smile, laugh, smirk, angry, sad, surprised, scared, identical face structure across panels, neutral grey background, flat lighting, concept art style
```

### 1.3 服装变体一排
```text
character outfit variations, same character: [identity anchor], 4 outfits: casual, formal, combat, festival, identical face and hair, neutral background, full body, three-quarter view, concept art style
```

### 1.4 三视图转身
```text
character turnaround sheet, same character: [identity anchor], three views in one row: front, three-quarter, side profile, identical proportions, neutral grey background, even lighting, model sheet style with clean line art
```

### 1.5 年龄进程 sheet
```text
character age progression, same character: [identity anchor — keep hair color and key feature], 4 ages: child (8), teen (15), young adult (25), elder (55), consistent facial bone structure across ages, neutral background, concept art style
```

### 1.6 灯光锁姿势变
```text
same character: [identity anchor], 4 lighting setups in a grid: soft daylight, dramatic rim light, golden hour, moonlight, identical pose and outfit, only lighting changes, painterly concept art style
```

### 1.7 情绪特写小图
```text
character emotion close-up sheet, same character: [identity anchor], tight headshots only, 6 emotions: determined, exhausted, joyful, suspicious, heartbroken, defiant, identical face structure, soft studio light, neutral background
```

### 1.8 RPG 职业变体
```text
same character: [identity anchor — face and hair locked], 4 class variants: warrior, mage, rogue, cleric, identical face across variants, only armor and props change, full body, three-quarter view, fantasy concept art
```

### 1.9 待机姿势 sheet
```text
character pose sheet, same character: [identity anchor], 4 idle poses: standing relaxed, arms crossed, leaning, mid-walk, identical outfit and face, neutral grey background, clean line art with flat color, model sheet style
```

### 1.10 NPC 对话立绘
```text
NPC dialogue portraits, same character: [identity anchor], 4 dialogue states: greeting, explaining, surprised, farewell, shoulders-up framing, consistent face and outfit, slight 3/4 angle, JRPG visual novel style, flat lighting
```

### 1.11 发型探索一排
```text
hairstyle exploration sheet, same character: [identity anchor — face locked, hair variable], 4 hairstyles: short crop, shoulder length, long braid, updo, identical face, neutral background, soft front lighting, concept art style
```

### 1.12 主视觉 hero shot
```text
hero cover shot of same character: [identity anchor], dynamic three-quarter pose, dramatic lighting, painterly background hinting at the world, identical face to the rest of the sheet, 9:16, key-art style
```

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

### 3.2 IllustriousXL layout
```text
highres, hi res, best quality, masterpiece, intricate details, absurdres, 4k, semi realistic,,"NEXT THE BASE PROMPT"--> CharacterDesignIllustrious, reference sheet, simple white background, (color guide:1.2), (multiple views), (full body), dynamic pose "NEXT THE CHARACTER CHARACTERISTICS" --> blonde, bluen eyes etc.
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

### 3.5 Illustrious triggers
```text
(CharacterSheet:1)
(multiple views, full body, upper body, reference sheet:1)
```

### 3.6 Community reply — multi-view SD/PDXL example (same page comments)
```text
Prompt: character design sheet, front view, side view, back view, turnaround sheet, multiple views, uniform grid, clean lines, flat color, concept art, white background
```

---

## 4) Melon Hub — concept → turnaround templates

- **Language:** en (templates); article zh
- **Source:** https://melon-hub.com/guides/character-design-prompts

### 4.1 Midjourney full-body concept
```text
full body character concept art of [角色身份], [年龄+体型], 
[发型+发色], [瞳色], wearing [服装描述], holding [道具], 
[标志性元素], [性格姿态], 
[第一层风格], [第二层参考], [第三层工艺], 
plain neutral background, front view, standing pose, 
character sheet --ar 2:3 --style raw --s 250
```

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

### 4.4 Midjourney 三视图
```text
character turnaround sheet of [角色 ID], 
front view, side view, back view, three views in one image, 
T-pose, neutral expression, plain white background, 
orthographic projection, model sheet, design document layout, 
[风格三层堆叠] --ar 16:9 --style raw --cref [主图URL] --cw 100
```

### 4.5 Expression sheet phrase (article)
```text
expression sheet, 9 expressions in grid, smiling, angry, crying, surprised, embarrassed, calm, smug, sleepy, screaming, same character
```

### 4.6 Outfit variations phrase
```text
same character in different outfits, casual outfit, formal outfit, combat outfit, swimsuit
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
| 1 Portrait sheets | 12 |
| 2 IPIPP MJ | 3 |
| 3 Qpipi LoRA | 6 |
| 4 Melon Hub | 7 |
| **Total** | **28** |
