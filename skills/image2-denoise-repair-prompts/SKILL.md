---
name: Image2 / Denoise / Quality Repair Prompts
description: Use when generating clean GPT-Image-2 / IM2 images or editing existing noisy/dirty images — detail distribution, preserve-locks, denoise repair language, material-clean layer, and numeric denoise ranges.
---

# Image2 / Denoise / Quality Repair (生图修画质)

## When to use

- User wants **clean generation** (防噪) or **edit/repair** of a dirty/noisy/blurry image (降噪修图) for GPT Image 2 / IM2 / img2img pipelines.
- Inputs needed: mode (`generate` | `edit`), subject/theme, what must stay locked, noise symptoms (grain/speckles/muddy shadows/particles), optional denoise numeric target, language (EN/ZH).

**Source grounding:** `/workspace/prompt-extract/raw/03-web-image2-denoise-prompts.md` (§1 istarry, §2 IM2 clean skill, §3 ERNIE ranges, §4 图叮 phrases, §5 Flux/Comfy numeric). Also `raw/fetch-tmp/im2-clean-skill.md` for fuller IM2 hygiene.

## Canonical prompt skeletons

### A) Clean generate (全新生图防噪)

```text
Create a clean, refined, publication-ready {{style}} about {{theme}}.
The main subject is {{subject}}, clearly recognizable and placed as the visual focus.
{{detail_distribution}}
Lighting: {{lighting}} (prefer soft diffused / large softbox; avoid hard light that shreds shadows into noise).
Background: {{background}} (simple / low-noise; if dark, use hex deep grey e.g. #1E1E1E — not pure black).
Material-light (optional but strong): {{material_sentence}}
Clean layer: clean rendering, balanced detail, realistic detail only, natural texture only, controlled highlights, minimal repetitive patterns.
Negative constraints: {{avoid_block}}
```

Detail-distribution default:

```text
The main subject should have refined, precise details. Keep the background clean and minimal. Secondary elements should remain simple. Emphasize clarity over decoration.
```

### B) Edit / denoise repair (已有脏图)

```text
Edit this image to make it cleaner, sharper, and more suitable for publication.
KEEP LOCK: original subject, composition, pose, color palette, overall style, identity, clothing, camera angle.
CLEAN OPS: clean up background noise, remove random speckles, reduce dirty textures, smooth muddy shadows, soften harsh glow, remove excessive particles, improve edge clarity. Preserve important details on the main subject. Simplify unnecessary background texture.
DO NOT: redraw the whole image; change identity/pose/clothing/camera angle; add new text/watermark/logo.
{{optional_zh_line}}
```

ZH repair one-liner (from §1.5):

```text
保留原图构图、色彩、主体造型，去除画面噪点、颗粒杂色、脏污纹理，优化边缘清晰度，柔和暗部阴影，整体干净通透，无AI质感；
```

### C) Material sentence (IM2 §2.1)

```text
The [hero material] shows [physical behavior] under [lighting condition], with [local imperfections/topology] visible at [camera scale]; [specific areas] remain [matte/dry/absorbing] while [specific edges/surfaces] catch [soft/sharp/specular/anisotropic] highlights.
```

## Must-have modules

| Module | Role |
|--------|------|
| Mode select | `generate` vs `edit` — different KEEP/CLEAN/DO-NOT |
| Detail distribution | Hero refined; background minimal; clarity > decoration |
| Preserve lock (edit) | Subject / composition / palette / style / identity / clothing / angle |
| Clean ops | Speckles, dirty texture, muddy shadows, harsh glow, particles, edge clarity |
| Material-light (IM2) | Hero surfaces + light response before anti-dirt phrases |
| Avoid / negative hygiene | Compact artifact-class bans; do not dump old failed nouns |
| Denoise number (img2img) | Pair prose with range (see below) |

## Hard negatives / bans (distilled)

**Avoid block (safe default, §2.3):**  
dirty texture buildup, random micro-pattern noise, hidden watermark-like marks, ghost texture, latent artifacts, muddy shadows, noisy bokeh, low-contrast residual textures, over-sharpened grime, uniform plastic gloss, pasted-on texture, milky reflections, clipped highlights, crushed blacks, dirty AO halos, malformed anatomy (when people), stray text/logo unless requested.

**High-noise bait words to delete or replace (§1.6 / §4):**  
cinematic lighting, dramatic lighting, volumetric fog, glowing particles, epic atmosphere, hyper detailed background, complex texture, high contrast, neon glow, film grain, analog, 胶片, 复古质感, 颗粒感.

**Clean substitutes:**  
clean editorial illustration, minimal background, soft diffused lighting, high readability, smooth surfaces, publication-ready, low visual noise; 画面整体干净无噪点，暗部色彩纯净，阴影区保留层次而不是压成死黑.

**Negative hygiene:** prefer broad artifact classes; do not list old failed props/characters in Avoid (can re-summon them).

## Denoise numeric guidance (settings, not prose)

| Use case | Typical denoise | Source |
|----------|-----------------|--------|
| Photo repair / light enhance | 0.10–0.30 (e.g. 0.15 portrait) | ERNIE §3 |
| Flux skin/detailer | 0.10–0.20 | Comfy §5 |
| Flux DyPE / LIU mild | 0.15–0.40 | sandner / Comfy §5 |
| After latent upscale (stronger) | 0.35–0.45 | circler §5 |
| Staged pipeline | 0.6–0.8 → 0.3–0.4 → 0.15–0.2 | xjtaxi §5 |

Rule of thumb: lower denoise = preserve structure; higher = more redraw (sketch→finish ~0.75 is not “denoise repair”).

## Fill-in checklist

- [ ] Mode: generate or edit
- [ ] Subject + theme + style
- [ ] Detail distribution sentence
- [ ] Lighting + background (hex if dark)
- [ ] Edit: KEEP / CLEAN / DO-NOT triple
- [ ] Optional material-light sentence
- [ ] Compact avoid block (no laundry list of old failures)
- [ ] If img2img: pick denoise number for intent
- [ ] Language EN and/or ZH line

## Short examples

**Example A — clean editorial generate (§1.2 trimmed)**  
```text
Create a clean, refined, publication-ready editorial illustration about neural network pruning.
Main subject: simplified network graph as visual focus. Soft diffused light, white background,
refined colorful palette, high readability. Hero has clean edges; background low-noise.
Avoid: No grain, No dirty texture, No muddy shadows, No random speckles, No watermark, No logo, No readable text.
```

**Example B — edit repair (§1.3)**  
```text
Edit this image to make it cleaner and sharper. Keep subject, composition, pose, palette, style.
Clean speckles/dirty textures/muddy shadows/harsh glow/particles; improve edge clarity.
Do not redraw whole image; do not change identity, clothing, or camera angle. No new text/watermark.
```
