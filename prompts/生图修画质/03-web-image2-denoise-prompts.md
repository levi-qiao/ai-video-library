# 03 Web — Image quality / denoise / Image2 upscale repair prompts

> body: verbatim — full original prompt text only; no summary/teaser.

Collected 2026-09-29 Asia/Shanghai. **Verbatim** public prompts only. Language + URL on each block. No invented prompts.

Theme match: “告别图片噪点 / Image2 画质修复 / denoise img2img”.

---

## 1) GPT Image 2 — generate clean + edit denoise (StartAI / istarry)

- **Language:** en (+ zh repair instruction)
- **Source:** https://istarry.com.cn/ps/gpt-image2-denoise-prompt-tutorial/

### 1.1 Detail-distribution control line
```text
The main subject should have refined, precise details. Keep the background clean and minimal. Secondary elements should remain simple. Emphasize clarity over decoration.
```

### 1.2 通用高清生图 Prompt（全新生成干净无噪图片）
```text
Create a clean, refined, publication-ready editorial illustration about [主题]. The main subject is [主体], clearly recognizable and placed as the visual focus. Use a modern scientific explainer style with a white or light background, soft diffused lighting, refined colorful palette, elegant spacing, and high readability. The main subject should have refined details with clean edges, smooth surfaces, and accurate structure. Keep the background simple and low-noise. Avoid excessive decoration. Negative constraints: No grain, No dirty texture, No muddy shadows, No random speckles, No messy background, No excessive particles, No neon cyberpunk, No watermark, No logo, No readable text.
```

### 1.3 图片降噪修复 Prompt（优化已有脏图、模糊图）
```text
Edit this image to make it cleaner, sharper, and more suitable for publication. Keep the original subject, composition, pose, color palette, and overall style unchanged. Clean up background noise, remove random speckles, reduce dirty textures, smooth muddy shadows, soften harsh glow, remove excessive particles, and improve edge clarity. Preserve important details on the main subject. Simplify unnecessary background texture. Do not redraw the whole image. Do not change identity. Do not change clothing. Do not change camera angle. No new text. No watermark. No logo.
```

### 1.4 三层修图逻辑（片段，verbatim from article）
```text
Keep the original subject. Keep composition unchanged. Keep color palette unchanged. Keep overall style unchanged.
```

```text
remove random speckles、clean dirty textures、reduce background noise、smooth muddy shadows、soften harsh glow、improve edge clarity
```

```text
Do not redraw the whole image. Do not change identity. Do not change pose. Do not change clothing. Do not change camera angle.
```

### 1.5 Banana/修图中文指令（文章给出的中文修图说法）
```text
保留原图构图、色彩、主体造型，去除画面噪点、颗粒杂色、脏污纹理，优化边缘清晰度，柔和暗部阴影，整体干净通透，无AI质感；
```

### 1.6 高噪点关键词避坑 / 干净替代（verbatim lists）
```text
cinematic lighting、dramatic lighting、volumetric fog、glowing particles、epic atmosphere、hyper detailed background、complex texture、high contrast、neon glow
```

```text
clean editorial illustration、minimal background、soft diffused lighting、high readability、smooth surfaces、publication-ready、low visual noise
```

---

## 2) IM2 Clean Image skill (GitHub raw)

- **Language:** en
- **Source:** https://raw.githubusercontent.com/btwiuse/video-skills/24e4c8af/im2-clean-image/SKILL.md
- **Repo:** https://github.com/btwiuse/video-skills (path `im2-clean-image/SKILL.md`)

### 2.1 Material sentence skeleton
```text
The [hero material] shows [physical behavior] under [lighting condition], with [local imperfections/topology] visible at [camera scale]; [specific areas] remain [matte/dry/absorbing] while [specific edges/surfaces] catch [soft/sharp/specular/anisotropic] highlights.
```

### 2.2 Universal material quality block
```text
physically distinct material classes, protected highlight texture, smooth cinematic highlight rolloff, readable shadow-side structure, localized contact shadows, distance- and roughness-correct reflections, motivated grazing light, restrained atmosphere, subtle finishing
```

### 2.3 Safe default avoid block
```text
Avoid: dirty texture buildup, random micro-pattern noise, hidden watermark-like marks, ghost texture, latent artifacts, muddy shadows, noisy bokeh, low-contrast residual textures, over-sharpened grime, uniform plastic gloss, pasted-on texture, milky reflections, clipped highlights, crushed blacks, dirty AO halos, malformed anatomy when people are present, stray text or logo unless requested.
```

### 2.4 Narrower avoid block
```text
Avoid: ghost texture, latent artifacts, hidden watermark-like marks, repeated micro-pattern noise, muddy shadows, noisy bokeh, pasted-on texture.
```

### 2.5 Full cleanup add-on
```text
clean rendering, balanced detail, realistic detail only, natural texture only, controlled material rendering, clean gradients, soft diffused lighting, controlled highlights, subtle reflections only, matte or natural surfaces, clean blurred background, minimal repetitive patterns, no watermark, no signature, no ghost texture, no latent artifacts, no repetitive micro-pattern noise, no hidden marks, no low-contrast residual textures
```

### 2.6 Short cleanup add-on
```text
clean rendering, balanced detail, realistic detail only, natural texture only, controlled highlights, clean blurred background, minimal repetitive patterns, no watermark, no ghost texture, no latent artifacts, no low-contrast residual textures
```

---

## 3) ERNIE-Image img2img denoise repair examples

- **Language:** en (prompts) / zh (labels)
- **Source:** https://ernie-image.app/blog/ei-029-img2img-guide-cn-20260506

### 3.1 老照片修复（denoise = 0.15）
```text
clear portrait, high resolution, sharp details, warm lighting
```
(Article pairs with Denoise：0.15)

### 3.2 图像增强/修复（denoise 0.1–0.3）
```text
high resolution, sharp details, professional photography, 4K quality
```

### 3.3 照片→动漫（denoise = 0.4）— related img2img, not pure denoise
```text
a cute anime girl, detailed eyes, chibi style, pastel colors
```

### 3.4 草图→精细（denoise = 0.75）
```text
modern glass office building, sunset lighting, photorealistic, architectural photography
```

### 3.5 Negative example snippet from same guide
```text
blurry, low quality
```

---

## 4) 图叮 — GPT Image 2 噪点分诊后的干净约束短语

- **Language:** zh-CN
- **Source:** https://tudingai.cn/blog/202607/gpt-image-2-noise-grain-3-causes-fix/
- **Note:** Mostly diagnostic workflow. Verbatim constraint phrases:

```text
画面整体干净无噪点，暗部色彩纯净，阴影区保留层次而不是压成死黑。
```

```text
别写纯黑背景，给一个带 hex 值的深灰，比如 #1E1E1E。
```

```text
大面积柔光箱主光，避免硬光在暗部切出噪声状的碎影。
```

*(Article also says delete: film grain、analog、胶片、复古质感、颗粒感 — as words to remove, not a positive prompt.)*

---

## 5) Flux / ComfyUI denoise ranges (settings, not prose prompts)

These pages document **numeric denoise** for upscale repair; included as cited guidance, not invented text prompts.

| Source | Verbatim guidance |
|--------|-------------------|
| https://sandner.art/latent-interpolate-upscale-expanding-flux-and-sdxls-denoising-range/ | “Use of low denoising … value, 0.15-0.4” (LIU); ratio notes for removing upscale artifacts |
| https://github.com/rik-python/Comfyu--Image-detailer-and-skin-detailer-workflows | Flux DyPE Denoise: 0.20–0.35; SRPO Skin Detailer Denoise: 0.10–0.20 |
| https://www.circler.cn/course_info/137/ | KSampler #2 denoise 0.35–0.45 after latent upscale |
| https://www.xjtaxi.com/2026042138005.html | Flux inpaint-style low denoise 0.15–0.25 after Real-ESRGAN; staged 0.6–0.8 / 0.3–0.4 / 0.15–0.2 |

**No long English “repair the image…” prompt** found on those upscale pages beyond parameter tables.

---

## 6) Failed / thin sources this category

| URL | Result |
|-----|--------|
| https://www.chooseai.net/news/6017/ | WebFetch HTTP 500; curl download failed this run — known Chinese “两段提示词事前防事后救” article; **not** captured verbatim here |
| Douyin short links in task | Redirect only; no Image2 prompt text |

---

## Verbatim prompt / block count (this file)

| Section | Fenced blocks |
|---------|--------------:|
| 1 istarry/Image2 | 9 |
| 2 IM2 clean skill | 6 |
| 3 ERNIE img2img | 5 |
| 4 图叮 phrases | 3 |
| **Total fenced** | **23** |

Plus denoise **numeric** citations in §5 (not counted as prose prompts).
