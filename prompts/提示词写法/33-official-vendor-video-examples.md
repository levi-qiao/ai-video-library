# 提示词写法 · 官方视频提示词示例（用于裁定库内冲突）

## 来源概述（非原文）

- 来源（官方厂商文档，2026-09-30 抓取）：
  - 火山引擎《Doubao Seedance 2.0 系列提示词指南》：https://www.volcengine.com/docs/82379/2222480 （页面日期：2026-09-22（文档更新时间））
  - Google Cloud《Veo prompt guide》：https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide （页面日期：2026-09-28（页面 Last updated，UTC））
- 许可：CC-BY-4.0 (Google Developers Site Policies: page content CC BY 4.0, code Apache 2.0); attribute Google；official-docs; copyright-retained (火山引擎 / ByteDance); quoted with attribution。官方文档里的示例提示词按原文引用并注明出处，不代表厂商授权再分发。
- 来源类型：模型厂商官方提示词指南 / API 文档；`text` 围栏内为官方页面上的示例提示词，逐字复制（脚本与抓取页面比对），未改写、未翻译。官方的说明性文字不进围栏，要点写在「备注」里。
- 本文件内容：Seedance 2.0 官方示例 1（取代原 lanshu kit 衍生版）；Veo 负面提示词的官方写法。
- 本文件计数条目：3；核对状态：verified 3
- 相关：做法与出处总表见 `docs/首尾帧工作流.md`、`docs/权威来源.md`。

## 1. Seedance 2.0 官方示例 1 · 宿舍情感短剧

```yaml
# 条目元数据（策展者添加，非原文）
id: "prompt-writing--33-official-vendor-video-examples--01"
标题: "Seedance 2.0 官方示例 1：宿舍情感短剧（偏文戏 / 对话）"
原标题: "示例1：宿舍情感短剧（偏文戏 / 对话）"
分类: "提示词写法"
标签: ["分镜/多镜头", "参考图/素材引用", "音频/音效", "台词/对白"]
适用模型: "Seedance 2.0（官方指南示例）"
语言: "zh"
来源链接: "https://www.volcengine.com/docs/82379/2222480"
镜像: ""
作者: "火山引擎（官方文档）"
发布日期: "2026-09-22（文档更新时间）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (火山引擎 / ByteDance); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）；已去掉网页 Markdown 加粗标记 **，文字未改"
完整性: "完整"
备注: "取代 `提示词写法/01` 原 §2.3 的 lanshu kit 衍生版本（该版本与官方有 3 处字词差异，已移出计数，原文作对照保留在该节）。素材准备：@图片 1 女主半身照、@图片 2 宿舍场景参考图、@视频 1 室内对话运镜参考、@音频 1 室内环境声或轻音乐。"
技巧钩子: ""
触发场景: ""
```

```text
@图片 1 中的女孩作为主角，@图片 2 作为宿舍场景风格参考，参考 @视频 1 的运镜方式。

镜头 1：傍晚时分，女孩 @图片 1 脚步轻快地走到宿舍门口 @图片 2，镜头中景平稳跟拍，暖黄色日光从窗外洒进走廊，她在门口停顿一下，深呼吸，表情略带紧张。

镜头 2：女孩 @图片 1 推开门走进宿舍，镜头切到室内中景，舍友们一边整理书本一边抬头看向她，其中一人笑着问 {考得怎么样呀，过了吗}，镜头在几人之间缓慢切换半身特写。

镜头 3：女孩 @图片 1 先低头露出落寞表情，镜头给到她的近景，随后她抬头憋不住笑意，哈哈大笑说 {骗你们的}，舍友们追着打闹起来，镜头缓慢拉远，定格在宿舍内一片欢声笑语的全景画面。

全程画面高清电影纪实风，色调温暖，光影柔和；人物面部稳定不变形，动作自然流畅，无卡顿无闪烁；环境音效与 @音频 1 自然融合。
```

## 2. Veo 官方示例 · 负面提示（名词列表）

```yaml
# 条目元数据（策展者添加，非原文）
id: "prompt-writing--33-official-vendor-video-examples--02"
标题: "Veo 主提示词（配合下一条负面提示）"
原标题: "Negative prompts — Prompt"
分类: "提示词写法"
标签: []
适用模型: "Veo（Google Cloud 官方提示词指南示例）"
语言: "en"
来源链接: "https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide"
镜像: ""
作者: "Google Cloud（官方文档）"
发布日期: "2026-09-28（页面 Last updated，UTC）"
热度: "未知（来源无公开互动数据）"
许可: "CC-BY-4.0 (Google Developers Site Policies: page content CC BY 4.0, code Apache 2.0); attribute Google"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "与下一条负面提示词配套。"
技巧钩子: ""
触发场景: ""
```

```text
Generate a short, stylized animation of a large, solitary oak tree with leaves blowing vigorously in a strong wind. The tree should have a slightly exaggerated, whimsical form, with dynamic, flowing branches. The leaves should display a variety of autumn colors, swirling and dancing in the wind. The animation should feature a gentle, atmospheric soundtrack and use a warm, inviting color palette.
```

## 3. Veo 官方示例 · 负面提示词

```yaml
# 条目元数据（策展者添加，非原文）
id: "prompt-writing--33-official-vendor-video-examples--03"
标题: "Veo 负面提示词：只列不想要的东西，不写 no / don't"
原标题: "Negative prompts — With negative prompt"
分类: "提示词写法"
标签: ["负面约束"]
适用模型: "Veo（Google Cloud 官方提示词指南示例）"
语言: "en"
来源链接: "https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide"
镜像: ""
作者: "Google Cloud（官方文档）"
发布日期: "2026-09-28（页面 Last updated，UTC）"
热度: "未知（来源无公开互动数据）"
许可: "CC-BY-4.0 (Google Developers Site Policies: page content CC BY 4.0, code Apache 2.0); attribute Google"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "放在 negativePrompt 字段，不写进主提示词。官方：「Not recommended: using instructive language or words such as \"no\" or \"don't\"」。"
技巧钩子: ""
触发场景: ""
```

```text
urban background, man-made structures, dark, stormy, or threatening atmosphere.
```

## 总结（非原文）

- 条目数：3（`text` 围栏逐字原文）
- 语言：zh 1、en 2
- 核对状态：verified 3
- 使用提醒：官方示例只说明写法，参数（画幅、分辨率、首尾帧字段）以对应厂商文档为准；各模型限制对照见 `docs/首尾帧工作流.md` 第 9 节。
