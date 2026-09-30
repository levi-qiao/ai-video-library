# 技巧锦囊 · Google Cloud《The ultimate prompting guide for Veo 3.1》：用首尾帧做「正面 → 背后 POV」的视角反转

## 来源概述（非原文）

> body: verbatim — 无语言代码块是官方博客对应段落的原文；三个 `text` 围栏是官方给出的三步提示词原文。「巧在哪」「总结（非原文）」为策展者所写，**非原文**。

- **source URL:** https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1
- **publisher:** Google Cloud 博客（署名 Khulan Davaajav, Product Marketing Manager；Hussain Chinoy, Technical Solutions Manager），2025-10-15
- **captured:** 2026-09-30（UTC+8），HTML 保存在 box `/workspace/prompt-extract/raw/jiqiao-sources/veo31.html`
- **license:** 未注明（来源未声明许可）
- **与本库已有内容的关系（去重）:** `docs/术语速查.md` 引用的是另一份 Veo 文档（Vertex AI《Veo prompt guide》），本博客的工作流此前未收录（全库检索「180-degree arc」「First and Last Frame」无结果）。同一博客的五段式公式、否定写法、时间戳分镜在 `docs/最佳实践.md` 和大量「时间码分段」条目中已有，不重复收。
- 本文件计数条目：3 个 `text` 围栏（首帧、尾帧、Veo 提示词）；核对状态：verified 3。

## 1. 方法原文

> 巧在哪（非原文）：首尾帧常被用来做「同一角度的变化」（变身、换装）。这里的用法是**首尾帧取两个互补视角**，让模型自己找出一条连续的摄影机路径（180° 环绕），相当于用两张图「规定起点和终点」来控制运镜。

```
Workflow 1: The dynamic transition with "first and last frame"

This technique allows you to create a specific and controlled camera movement or transformation between two distinct points of view.

Step 1: Create the starting frame: Use Gemini 2.5 Flash Image to generate your initial shot.

Step 2: Create the ending frame: Generate a second, complementary image with Gemini 2.5 Flash Image, such as a different POV angle.

Step 3: Animate with Veo. Input both images into Veo using the First and Last Frame feature. In your prompt, describe the transition and the audio you want.
```

## 2. 三步提示词

### Step 1 · 首帧

```yaml
# 条目元数据（策展者添加，非原文）
id: "jiqiao--37-google-veo31-first-last-frame-pov-switch--01"
标题: "首帧：舞台上唱歌的女歌手（正面中景）"
原标题: "Step 1: Create the starting frame"
分类: "技巧锦囊"
标签: ["技巧锦囊", "首尾帧", "视角切换", "环绕运镜", "POV", "参考图/素材引用", "生图"]
适用模型: "Gemini 2.5 Flash Image（Nano Banana）（来源标注：用来生成首帧）"
语言: "en"
来源链接: "https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1"
镜像: "2026-09-30 直接抓取官方博客 HTML（box: /workspace/prompt-extract/raw/jiqiao-sources/veo31.html）"
作者: "Google Cloud（发布方；署名 Khulan Davaajav、Hussain Chinoy）"
发布日期: "2025-10-15（页面显示 October 15, 2025，美国时间；结构化数据 datePublished 2025-10-16）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本（官方博客 Workflow 1 · Step 1 的图片提示词）"
核对状态: "verified"
核对说明: "与官方博客 HTML 转出的文本逐字核对一致；两端的弯引号“”是博客的引用符号，未收入围栏。"
完整性: "完整"
备注: "三步组成一个工作流：本条（首帧）→ 02（尾帧）→ 03（Veo 3.1 首尾帧提示词）。"
技巧钩子: "首帧和尾帧用两个不同视角（正面 → 背后 POV），再让模型用一个 180° 环绕把两者连起来，一条镜头里完成视角反转"
触发场景: "想在一个镜头里从「看人」转到「用人的视角看世界」（舞台、赛场、发布会），又不想硬切时"
```

```text
Medium shot of a female pop star singing passionately into a vintage microphone. She is on a dark stage, lit by a single, dramatic spotlight from the front. She has her eyes closed, capturing an emotional moment. Photorealistic, cinematic.
```

### Step 2 · 尾帧

```yaml
# 条目元数据（策展者添加，非原文）
id: "jiqiao--37-google-veo31-first-last-frame-pov-switch--02"
标题: "尾帧：从歌手背后看向欢呼人群（POV）"
原标题: "Step 2: Create the ending frame"
分类: "技巧锦囊"
标签: ["技巧锦囊", "首尾帧", "视角切换", "环绕运镜", "POV", "参考图/素材引用", "生图"]
适用模型: "Gemini 2.5 Flash Image（Nano Banana）（来源标注：用来生成尾帧）"
语言: "en"
来源链接: "https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1"
镜像: "2026-09-30 直接抓取官方博客 HTML（box: /workspace/prompt-extract/raw/jiqiao-sources/veo31.html）"
作者: "Google Cloud（发布方；署名 Khulan Davaajav、Hussain Chinoy）"
发布日期: "2025-10-15（页面显示 October 15, 2025，美国时间；结构化数据 datePublished 2025-10-16）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本（官方博客 Workflow 1 · Step 2 的图片提示词）"
核对状态: "verified"
核对说明: "与官方博客 HTML 转出的文本逐字核对一致；两端的弯引号是博客的引用符号，未收入。"
完整性: "完整"
备注: "官方原话：「Generate a second, complementary image … such as a different POV angle」——尾帧要与首帧互补，而不是同一角度。"
技巧钩子: "首帧和尾帧用两个不同视角（正面 → 背后 POV），再让模型用一个 180° 环绕把两者连起来，一条镜头里完成视角反转"
触发场景: "想在一个镜头里从「看人」转到「用人的视角看世界」（舞台、赛场、发布会），又不想硬切时"
```

```text
POV shot from behind the singer on stage, looking out at a large, cheering crowd. The stage lights are bright, creating lens flare. You can see the back of the singer's head and shoulders in the foreground. The audience is a sea of lights and silhouettes. Energetic atmosphere.
```

### Step 3 · Veo 3.1 首尾帧提示词

```yaml
# 条目元数据（策展者添加，非原文）
id: "jiqiao--37-google-veo31-first-last-frame-pov-switch--03"
标题: "Veo 3.1 首尾帧：180° 环绕从正面转到背后 POV（含歌词）"
原标题: "Step 3: Animate with Veo"
分类: "技巧锦囊"
标签: ["技巧锦囊", "首尾帧", "视角切换", "环绕运镜", "POV", "参考图/素材引用", "台词", "音频"]
适用模型: "Veo 3.1（来源标注；使用 First and Last Frame 功能）"
语言: "en"
来源链接: "https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1"
镜像: "2026-09-30 直接抓取官方博客 HTML（box: /workspace/prompt-extract/raw/jiqiao-sources/veo31.html）"
作者: "Google Cloud（发布方；署名 Khulan Davaajav、Hussain Chinoy）"
发布日期: "2025-10-15（页面显示 October 15, 2025，美国时间；结构化数据 datePublished 2025-10-16）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本（官方博客 Workflow 1 · Step 3 的 Veo 3.1 提示词）"
核对状态: "verified"
核对说明: "与官方博客 HTML 转出的文本逐字核对一致。原文开头的弯引号「“」是博客的引用符号，未收入；句中歌词前的「“」与结尾「”」照原样保留（原文引号本身不成对）。"
完整性: "完整"
备注: "官方原文：「In your prompt, describe the transition and the audio you want.」首尾帧提示词只写两帧之间的运动与声音。"
技巧钩子: "首帧和尾帧用两个不同视角（正面 → 背后 POV），再让模型用一个 180° 环绕把两者连起来，一条镜头里完成视角反转"
触发场景: "想在一个镜头里从「看人」转到「用人的视角看世界」（舞台、赛场、发布会），又不想硬切时"
```

```text
The camera performs a smooth 180-degree arc shot, starting with the front-facing view of the singer and circling around her to seamlessly end on the POV shot from behind her on stage. The singer sings “when you look me in the eyes, I can see a million stars.”
```

## 总结（非原文）

- **做法**：先生成两张互补视角的图（正面中景 / 背后 POV），作为首帧和尾帧；视频提示词只写两帧之间的摄影机路径（180° arc）和声音。
- **为什么值得记**：比起在文字里描述复杂环绕，用两张图锁定起点和终点更可控；同一思路可用于「门外 → 门内」「地面 → 高空俯瞰」「角色 → 角色看到的东西」。
- **注意**：两张图的人物、服装、灯光要一致（官方用同一模型连续生成），否则模型会在中途「变人」。Seedance 2.0 的首尾帧、Kling 的首尾帧能否同样走出环绕路径，官方文档没有说明，需要自测。

本文件统计：计数条目 3（verified 3）；不计数代码块 1（官方方法原文）。
