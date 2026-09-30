# 生图修画质 · 网页收录：图片降噪 / 画质修复提示词

## 来源概述（非原文）

- 来源：StartAI / istarry（GPT Image 2 降噪教程）、btwiuse/video-skills 中的 IM2 Clean Image 技能（GitHub）；ERNIE-Image 与 Flux/ComfyUI 两节只有参数，不计数。
- 来源类型：网页 / GitHub；`text` 围栏内为原文，逐字复制；无语言标记的代码块为文章中的词表原文，不计数。
- 收录：2026-09-29（Asia/Shanghai）。主题：告别图片噪点、Image2 画质修复、img2img 降噪。

- 本文件计数条目：11 个 `text` 原文围栏；核对状态：verified 11

## 1. GPT Image 2：干净出图与降噪修图（StartAI / istarry）

- **Language:** en (+ zh repair instruction)
- **Source:** https://istarry.com.cn/ps/gpt-image2-denoise-prompt-tutorial/

### 1.1 Detail-distribution control line

```yaml
# 条目元数据（策展者添加，非原文）
id: "image-repair--03-web-image2-denoise-prompts--01"
标题: "细节分布控制句"
原标题: "Detail-distribution control line"
分类: "生图修画质"
标签: []
适用模型: "GPT Image 2（来源标注）"
语言: "en"
来源链接: "https://istarry.com.cn/ps/gpt-image2-denoise-prompt-tutorial/"
镜像: ""
作者: "istarry / StartAI（发布方）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
```

```text
The main subject should have refined, precise details. Keep the background clean and minimal. Secondary elements should remain simple. Emphasize clarity over decoration.
```

### 1.3 图片降噪修复 Prompt（优化已有脏图、模糊图）

```yaml
# 条目元数据（策展者添加，非原文）
id: "image-repair--03-web-image2-denoise-prompts--02"
标题: "图片降噪修复 Prompt（优化已有脏图、模糊图）"
原标题: ""
分类: "生图修画质"
标签: []
适用模型: "GPT Image 2（来源标注）"
语言: "en"
来源链接: "https://istarry.com.cn/ps/gpt-image2-denoise-prompt-tutorial/"
镜像: ""
作者: "istarry / StartAI（发布方）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
```

```text
Edit this image to make it cleaner, sharper, and more suitable for publication. Keep the original subject, composition, pose, color palette, and overall style unchanged. Clean up background noise, remove random speckles, reduce dirty textures, smooth muddy shadows, soften harsh glow, remove excessive particles, and improve edge clarity. Preserve important details on the main subject. Simplify unnecessary background texture. Do not redraw the whole image. Do not change identity. Do not change clothing. Do not change camera angle. No new text. No watermark. No logo.
```

### 1.4 三层修图逻辑（片段，verbatim from article）

```yaml
# 条目元数据（策展者添加，非原文）
id: "image-repair--03-web-image2-denoise-prompts--03"
标题: "三层修图逻辑（片段，verbatim from article）"
原标题: ""
分类: "生图修画质"
标签: []
适用模型: "GPT Image 2（来源标注）"
语言: "en"
来源链接: "https://istarry.com.cn/ps/gpt-image2-denoise-prompt-tutorial/"
镜像: ""
作者: "istarry / StartAI（发布方）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
```

```text
Keep the original subject. Keep composition unchanged. Keep color palette unchanged. Keep overall style unchanged.
```

```yaml
# 条目元数据（策展者添加，非原文）
id: "image-repair--03-web-image2-denoise-prompts--04"
标题: "三层修图逻辑（片段，verbatim from article）（2）"
原标题: ""
分类: "生图修画质"
标签: []
适用模型: "GPT Image 2（来源标注）"
语言: "en"
来源链接: "https://istarry.com.cn/ps/gpt-image2-denoise-prompt-tutorial/"
镜像: ""
作者: "istarry / StartAI（发布方）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
```

```text
remove random speckles、clean dirty textures、reduce background noise、smooth muddy shadows、soften harsh glow、improve edge clarity
```

```yaml
# 条目元数据（策展者添加，非原文）
id: "image-repair--03-web-image2-denoise-prompts--05"
标题: "三层修图逻辑（片段，verbatim from article）（3）"
原标题: ""
分类: "生图修画质"
标签: []
适用模型: "GPT Image 2（来源标注）"
语言: "en"
来源链接: "https://istarry.com.cn/ps/gpt-image2-denoise-prompt-tutorial/"
镜像: ""
作者: "istarry / StartAI（发布方）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
```

```text
Do not redraw the whole image. Do not change identity. Do not change pose. Do not change clothing. Do not change camera angle.
```

### 1.5 Banana/修图中文指令（文章给出的中文修图说法）

```yaml
# 条目元数据（策展者添加，非原文）
id: "image-repair--03-web-image2-denoise-prompts--06"
标题: "Banana/修图中文指令（文章给出的中文修图说法）"
原标题: ""
分类: "生图修画质"
标签: []
适用模型: "GPT Image 2（来源标注）"
语言: "zh"
来源链接: "https://istarry.com.cn/ps/gpt-image2-denoise-prompt-tutorial/"
镜像: ""
作者: "istarry / StartAI（发布方）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
```

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

## 2. IM2 Clean Image 技能（GitHub）

- **Language:** en
- **Source:** https://raw.githubusercontent.com/btwiuse/video-skills/24e4c8af/im2-clean-image/SKILL.md
- **Repo:** https://github.com/btwiuse/video-skills (path `im2-clean-image/SKILL.md`)

### 2.2 Universal material quality block

```yaml
# 条目元数据（策展者添加，非原文）
id: "image-repair--03-web-image2-denoise-prompts--07"
标题: "通用材质质量块"
原标题: "Universal material quality block"
分类: "生图修画质"
标签: []
适用模型: "GPT Image 2（来源标注）"
语言: "en"
来源链接: "https://raw.githubusercontent.com/btwiuse/video-skills/24e4c8af/im2-clean-image/SKILL.md"
镜像: ""
作者: "未知"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
```

```text
physically distinct material classes, protected highlight texture, smooth cinematic highlight rolloff, readable shadow-side structure, localized contact shadows, distance- and roughness-correct reflections, motivated grazing light, restrained atmosphere, subtle finishing
```

### 2.3 Safe default avoid block

```yaml
# 条目元数据（策展者添加，非原文）
id: "image-repair--03-web-image2-denoise-prompts--08"
标题: "安全默认规避块"
原标题: "Safe default avoid block"
分类: "生图修画质"
标签: ["负面约束"]
适用模型: "GPT Image 2（来源标注）"
语言: "en"
来源链接: "https://raw.githubusercontent.com/btwiuse/video-skills/24e4c8af/im2-clean-image/SKILL.md"
镜像: ""
作者: "未知"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
```

```text
Avoid: dirty texture buildup, random micro-pattern noise, hidden watermark-like marks, ghost texture, latent artifacts, muddy shadows, noisy bokeh, low-contrast residual textures, over-sharpened grime, uniform plastic gloss, pasted-on texture, milky reflections, clipped highlights, crushed blacks, dirty AO halos, malformed anatomy when people are present, stray text or logo unless requested.
```

### 2.4 Narrower avoid block

```yaml
# 条目元数据（策展者添加，非原文）
id: "image-repair--03-web-image2-denoise-prompts--09"
标题: "精简规避块"
原标题: "Narrower avoid block"
分类: "生图修画质"
标签: ["负面约束"]
适用模型: "GPT Image 2（来源标注）"
语言: "en"
来源链接: "https://raw.githubusercontent.com/btwiuse/video-skills/24e4c8af/im2-clean-image/SKILL.md"
镜像: ""
作者: "未知"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
```

```text
Avoid: ghost texture, latent artifacts, hidden watermark-like marks, repeated micro-pattern noise, muddy shadows, noisy bokeh, pasted-on texture.
```

### 2.5 Full cleanup add-on

```yaml
# 条目元数据（策展者添加，非原文）
id: "image-repair--03-web-image2-denoise-prompts--10"
标题: "完整清理附加块"
原标题: "Full cleanup add-on"
分类: "生图修画质"
标签: []
适用模型: "GPT Image 2（来源标注）"
语言: "en"
来源链接: "https://raw.githubusercontent.com/btwiuse/video-skills/24e4c8af/im2-clean-image/SKILL.md"
镜像: ""
作者: "未知"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
```

```text
clean rendering, balanced detail, realistic detail only, natural texture only, controlled material rendering, clean gradients, soft diffused lighting, controlled highlights, subtle reflections only, matte or natural surfaces, clean blurred background, minimal repetitive patterns, no watermark, no signature, no ghost texture, no latent artifacts, no repetitive micro-pattern noise, no hidden marks, no low-contrast residual textures
```

### 2.6 Short cleanup add-on

```yaml
# 条目元数据（策展者添加，非原文）
id: "image-repair--03-web-image2-denoise-prompts--11"
标题: "简短清理附加块"
原标题: "Short cleanup add-on"
分类: "生图修画质"
标签: []
适用模型: "GPT Image 2（来源标注）"
语言: "en"
来源链接: "https://raw.githubusercontent.com/btwiuse/video-skills/24e4c8af/im2-clean-image/SKILL.md"
镜像: ""
作者: "未知"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
```

```text
clean rendering, balanced detail, realistic detail only, natural texture only, controlled highlights, clean blurred background, minimal repetitive patterns, no watermark, no ghost texture, no latent artifacts, no low-contrast residual textures
```

## 3. ERNIE-Image 图生图降噪修复示例

- **Language:** en (prompts) / zh (labels)
- **Source:** https://ernie-image.app/blog/ei-029-img2img-guide-cn-20260506

> 【已移除（2026-09-30 整合）】原 §3.1 示例提示词过于单薄，未保留；来源给出的 denoise 取值为 0.15。

> 【已移除（2026-09-30 整合）】原 §3.2 示例提示词过于单薄，未保留；来源给出的 denoise 取值为 0.1–0.3。

> 【已移除（2026-09-30 整合）】原 §3.3 示例提示词过于单薄，未保留；来源给出的 denoise 取值为 0.4。

> 【已移除（2026-09-30 整合）】原 §3.4 示例提示词过于单薄，未保留；来源给出的 denoise 取值为 0.75。

## 5. Flux / ComfyUI 降噪强度范围（参数，不是提示词）

These pages document **numeric denoise** for upscale repair; included as cited guidance, not invented text prompts.

| Source | Verbatim guidance |
|--------|-------------------|
| https://sandner.art/latent-interpolate-upscale-expanding-flux-and-sdxls-denoising-range/ | “Use of low denoising … value, 0.15-0.4” (LIU); ratio notes for removing upscale artifacts |
| https://github.com/rik-python/Comfyu--Image-detailer-and-skin-detailer-workflows | Flux DyPE Denoise: 0.20–0.35; SRPO Skin Detailer Denoise: 0.10–0.20 |
| https://www.circler.cn/course_info/137/ | KSampler #2 denoise 0.35–0.45 after latent upscale |
| https://www.xjtaxi.com/2026042138005.html | Flux inpaint-style low denoise 0.15–0.25 after Real-ESRGAN; staged 0.6–0.8 / 0.3–0.4 / 0.15–0.2 |

**No long English “repair the image…” prompt** found on those upscale pages beyond parameter tables.

## 6. 本分类失败 / 内容过薄的来源

| URL | Result |
|-----|--------|
| https://www.chooseai.net/news/6017/ | WebFetch HTTP 500; curl download failed this run — known Chinese “两段提示词事前防事后救” article; **not** captured verbatim here |
| Douyin short links in task | Redirect only; no Image2 prompt text |

## 总结（非原文）

- 条目数：11（`text` 围栏逐字原文）
- 语言：en 10、zh 1
- 适用模型：GPT Image 2 11
- 核对状态：verified 11
- 常见写法特征（按规则自动识别）：负面约束 2
