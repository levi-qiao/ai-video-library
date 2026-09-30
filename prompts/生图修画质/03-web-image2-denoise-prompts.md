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
```
cinematic lighting、dramatic lighting、volumetric fog、glowing particles、epic atmosphere、hyper detailed background、complex texture、high contrast、neon glow
```

```
clean editorial illustration、minimal background、soft diffused lighting、high readability、smooth surfaces、publication-ready、low visual noise
```

---

## 2) IM2 Clean Image skill (GitHub raw)

- **Language:** en
- **Source:** https://raw.githubusercontent.com/btwiuse/video-skills/24e4c8af/im2-clean-image/SKILL.md
- **Repo:** https://github.com/btwiuse/video-skills (path `im2-clean-image/SKILL.md`)

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

> 【已移除（2026-09-30 整合）】原 §3.1 示例提示词过于单薄，未保留；来源给出的 denoise 取值为 0.15。

> 【已移除（2026-09-30 整合）】原 §3.2 示例提示词过于单薄，未保留；来源给出的 denoise 取值为 0.1–0.3。

> 【已移除（2026-09-30 整合）】原 §3.3 示例提示词过于单薄，未保留；来源给出的 denoise 取值为 0.4。

> 【已移除（2026-09-30 整合）】原 §3.4 示例提示词过于单薄，未保留；来源给出的 denoise 取值为 0.75。

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
| 1 istarry/Image2 | 8 |
| 2 IM2 clean skill | 5 |
| 3 ERNIE img2img | 4 |
| **Total fenced** | **17** |

Evening QC 2026-09-29 removed the unfilled `[主题]`/`[主体]` shell, the `[hero material]` skeleton, the 19-character negative `blurry, low quality`, and three 图叮 phrases under 50 characters.

Plus denoise **numeric** citations in §5 (not counted as prose prompts).
