# 首尾帧生图 · Google 官方 Gemini 图像 / Veo 首尾帧示例

## 来源概述（非原文）

- 来源（官方厂商文档，2026-09-30 抓取）：
  - Google《Nano Banana image generation》（Gemini API）：https://ai.google.dev/gemini-api/docs/image-generation （页面日期：2026-09-23（页面 Last updated，UTC））
  - Google《Generate videos with Veo 3.1》（Gemini API）：https://ai.google.dev/gemini-api/docs/veo （页面日期：2026-09-17（页面 Last updated，UTC））
  - Google Cloud《Generate videos using first and last video frames》：https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-first-and-last-frames （页面日期：2026-09-29（页面 Last updated，UTC））
- 许可：CC-BY-4.0 (Google Developers Site Policies: page content CC BY 4.0, code Apache 2.0); attribute Google。官方文档里的示例提示词按原文引用并注明出处，不代表厂商授权再分发。
- 来源类型：模型厂商官方提示词指南 / API 文档；`text` 围栏内为官方页面上的示例提示词，逐字复制（脚本与抓取页面比对），未改写、未翻译。官方的说明性文字不进围栏，要点写在「备注」里。
- 本文件内容：写实场景模板（含画幅）、语义蒙版局部修改、保细节编辑、逐角度生成角色、Veo 首尾帧插值。
- 本文件计数条目：7；核对状态：verified 7
- 相关：做法与出处总表见 `docs/首尾帧工作流.md`、`docs/权威来源.md`。Veo 3.1 首尾帧「正面 → 背后 POV」的完整三步示例见 `prompts/技巧锦囊/37-google-veo31-first-last-frame-pov-switch.md`。

## 1. Photorealistic scenes · 模板

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--02-google-gemini-veo-official--01"
标题: "写实场景模板（镜头类型 + 主体 + 场景 + 光线 + 机位 + 镜头）"
原标题: "Photorealistic scenes — Template"
分类: "首尾帧生图"
标签: ["首帧"]
适用模型: "Gemini 图像模型（Nano Banana 系列，官方指南模板）"
语言: "en"
来源链接: "https://ai.google.dev/gemini-api/docs/image-generation"
镜像: ""
作者: "Google（官方文档）"
发布日期: "2026-09-23（页面 Last updated，UTC）"
热度: "未知（来源无公开互动数据）"
许可: "CC-BY-4.0 (Google Developers Site Policies: page content CC BY 4.0, code Apache 2.0); attribute Google"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "模板里的 [ ] 是占位符，使用前替换。"
技巧钩子: ""
触发场景: ""
```

```text
A photorealistic [type of shot] of a [subject description] in a [setting
description]. [Description of the light]. Shot from a [camera angle]
with a [lens type].
```

## 2. Photorealistic scenes · 示例

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--02-google-gemini-veo-official--02"
标题: "写实场景示例：珊瑚礁（写明 16:9）"
原标题: "Photorealistic scenes — Prompt"
分类: "首尾帧生图"
标签: ["首帧", "横屏16:9"]
适用模型: "Gemini 图像模型（官方指南示例）"
语言: "en"
来源链接: "https://ai.google.dev/gemini-api/docs/image-generation"
镜像: ""
作者: "Google（官方文档）"
发布日期: "2026-09-23（页面 Last updated，UTC）"
热度: "未知（来源无公开互动数据）"
许可: "CC-BY-4.0 (Google Developers Site Policies: page content CC BY 4.0, code Apache 2.0); attribute Google"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "官方代码示例同时把 aspect_ratio 参数设为 \"16:9\"。"
技巧钩子: ""
触发场景: ""
```

```text
A photorealistic wide-angle shot of a vibrant coral reef teeming with tropical fish. Crystal-clear turquoise water with sunbeams filtering down from the surface, illuminating a sea turtle gliding gracefully over the coral. Shot from a low perspective with a wide-angle lens. Aspect ratio 16:9.
```

## 3. Inpainting (semantic masking) · 只改一处

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--02-google-gemini-veo-official--03"
标题: "语义蒙版：只改一处，其余完全不变"
原标题: "Inpainting (semantic masking)"
分类: "首尾帧生图"
标签: ["图像编辑"]
适用模型: "Gemini 图像模型（官方指南示例）"
语言: "en"
来源链接: "https://ai.google.dev/gemini-api/docs/image-generation"
镜像: ""
作者: "Google（官方文档）"
发布日期: "2026-09-23（页面 Last updated，UTC）"
热度: "未知（来源无公开互动数据）"
许可: "CC-BY-4.0 (Google Developers Site Policies: page content CC BY 4.0, code Apache 2.0); attribute Google"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "原文带首尾引号和换行，照录。"
技巧钩子: ""
触发场景: ""
```

```text
"Using the provided image of a living room, change only the blue sofa to be
a vintage, brown leather chesterfield sofa. Keep the rest of the room,
including the pillows on the sofa and the lighting, unchanged."
```

## 4. High-fidelity detail preservation · 保细节

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--02-google-gemini-veo-official--04"
标题: "编辑时保住脸和关键细节（先把要保的细节写详细）"
原标题: "High-fidelity detail preservation"
分类: "首尾帧生图"
标签: ["图像编辑", "角色一致性", "参考图/素材引用"]
适用模型: "Gemini 图像模型（官方指南示例）"
语言: "en"
来源链接: "https://ai.google.dev/gemini-api/docs/image-generation"
镜像: ""
作者: "Google（官方文档）"
发布日期: "2026-09-23（页面 Last updated，UTC）"
热度: "未知（来源无公开互动数据）"
许可: "CC-BY-4.0 (Google Developers Site Policies: page content CC BY 4.0, code Apache 2.0); attribute Google"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "官方说明：要保住脸或 Logo 这类关键细节，就在编辑请求里把它们描述详细。"
技巧钩子: ""
触发场景: ""
```

```text
"Take the first image of the woman with brown hair, blue eyes, and a neutral
expression. Add the logo from the second image onto her black t-shirt.
Ensure the woman's face and features remain completely unchanged. The logo
should look like it's naturally printed on the fabric, following the folds
of the shirt."
```

## 5. Character consistency: 360 view · 逐个角度生成

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--02-google-gemini-veo-official--05"
标题: "角色多角度：一次只要一个角度（360 view）"
原标题: "Character consistency: 360 view"
分类: "首尾帧生图"
标签: ["角色一致性", "参考图/素材引用", "技巧锦囊"]
适用模型: "Gemini 图像模型（官方指南示例）"
语言: "en"
来源链接: "https://ai.google.dev/gemini-api/docs/image-generation"
镜像: ""
作者: "Google（官方文档）"
发布日期: "2026-09-23（页面 Last updated，UTC）"
热度: "未知（来源无公开互动数据）"
许可: "CC-BY-4.0 (Google Developers Site Policies: page content CC BY 4.0, code Apache 2.0); attribute Google"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "官方说明：逐个角度迭代生成，并把前面生成的图一起传入以保持一致；复杂姿势附姿势参考图。"
技巧钩子: "多角度参考图不要一张图拼三视图：每次只要一个角度、把上一张作为输入，得到一组独立的单视图"
触发场景: "要给视频模型准备角色多角度参考，但 Seedance 2.0 等模型不建议用三视图 / 多视图拼图时"
```

```text
A studio portrait of this man against white, in profile looking right
```

## 6. Veo 3.1 · 首尾帧插值示例

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--02-google-gemini-veo-official--06"
标题: "Veo 3.1 首尾帧：秋千上的幽灵逐渐消失"
原标题: "Using first and last frames"
分类: "首尾帧生图"
标签: ["首尾帧"]
适用模型: "Veo 3.1（Gemini API 官方示例）"
语言: "en"
来源链接: "https://ai.google.dev/gemini-api/docs/veo"
镜像: ""
作者: "Google（官方文档）"
发布日期: "2026-09-17（页面 Last updated，UTC）"
热度: "未知（来源无公开互动数据）"
许可: "CC-BY-4.0 (Google Developers Site Policies: page content CC BY 4.0, code Apache 2.0); attribute Google"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "代码中首帧作为 image 传入，尾帧作为 config.last_frame 传入；官方参数表写明尾帧「Must be used in combination with the image parameter」。"
技巧钩子: ""
触发场景: ""
```

```text
A cinematic, haunting video. A ghostly woman with long white hair and a flowing dress swings gently on a rope swing beneath a massive, gnarled tree in a foggy, moonlit clearing. The fog thickens and swirls around her, and she slowly fades away, vanishing completely. The empty swing is left swaying rhythmically on its own in the eerie silence.
```

## 7. Veo（Vertex）· 首尾帧示例

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--02-google-gemini-veo-official--07"
标题: "Veo 首尾帧（Vertex）：一只手伸进来放下牛奶"
原标题: "Use Veo to create a video from first and last frames"
分类: "首尾帧生图"
标签: ["首尾帧"]
适用模型: "Veo（Gemini Enterprise Agent Platform / Vertex 官方示例）"
语言: "en"
来源链接: "https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/generate-videos-from-first-and-last-frames"
镜像: ""
作者: "Google Cloud（官方文档）"
发布日期: "2026-09-29（页面 Last updated，UTC）"
热度: "未知（来源无公开互动数据）"
许可: "CC-BY-4.0 (Google Developers Site Policies: page content CC BY 4.0, code Apache 2.0); attribute Google"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "提示词只写首尾两帧之间发生的动作，不重复描述画面。"
技巧钩子: ""
触发场景: ""
```

```text
a hand reaches in and places a glass of milk next to the plate of cookies
```

## 总结（非原文）

- 条目数：7（`text` 围栏逐字原文）
- 语言：en 7
- 核对状态：verified 7
- 使用提醒：官方示例只说明写法，参数（画幅、分辨率、首尾帧字段）以对应厂商文档为准；各模型限制对照见 `docs/首尾帧工作流.md` 第 9 节。
