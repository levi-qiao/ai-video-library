# 技巧锦囊 · Runway《Gen-4 Video Prompting Guide》：图生视频只写运动，不复述画面

## 来源概述（非原文）

> body: verbatim — 无语言代码块是官方指南对应段落的原文（页面上的 ❌ / ✅ 对照照原样保留）；`text` 围栏是官方示例提示词。「巧在哪」「总结（非原文）」为策展者所写，**非原文**。

- **source URL:** https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide
- **publisher:** Runway 帮助中心（页面未标注发布日期）
- **captured:** 2026-09-30（UTC+8）
- **license:** 未注明（来源未声明许可）
- **与本库已有内容的关系（去重）:** `docs/最佳实践.md` 与 `docs/术语速查.md` 已引用本指南的「不支持否定写法」和「先简单后复杂」，本文件不重复，只收「图生视频不要复述画面」「用 the subject 指代」「暗示式与描述式场景运动」三条。
- 本文件计数条目：1 个 `text` 围栏；核对状态：verified 1。

## 1. 图生视频：只写运动，不要把图里的东西再描述一遍

> 巧在哪（非原文）：直觉上描述越细越好，但官方说输入图本身就是提示词的一部分，**再把图里的外貌衣着写一遍，反而会让动作变少或出怪结果**。

```
Focus on describing the motion, rather than the input image
Both text and image inputs are considered part of your prompt. Reiterating elements that exist within the image in high detail can lead to reduced motion or unexpected results in the output.
❌ The tall man with black hair wearing a blue business suit and red tie reaches out his hand for a handshake
✅ The man extends his arm to shake hands, then nods politely.
```

## 2. 用 the subject、简单代词或位置词指代主体

> 巧在哪（非原文）：不写「那个穿红裙的金发女孩」，写「the subject」「she」「左边的人」，模型就不会去重新诠释主体的外貌，专心做动作。

```
When describing subject motion, refer to characters or objects with general terms like "the subject" or simple pronouns. For example: "The subject turns slowly" or "She raises her hand." This helps the model focus on creating smooth motion rather than reinterpreting subject details already present in your image.
For Multiple Subjects
When your image contains multiple subjects needing different movements:
Use clear positional language: "The subject on the left walks forward. The subject on the right remains still."
Or simple descriptive identifiers: "The woman nods. The man waves."
```

## 3. 场景运动：用形容词「暗示」更自然，直接「描述」会被强调

> 巧在哪（非原文）：想要自然的扬尘，写「dusty desert」就够；写成「身后扬起尘土」会被放大成重点。按想要的强度选写法。

```
Insinuated motion: "The subject runs across the dusty desert"
Described motion: "The subject runs across the desert. Dust trails behind them as they move"
Insinuating motion with adjectives can lead to more natural results, while directly describing the motion can lead to emphasis of the element. If insinuated scene motion doesn't provide the desired results, try insinuating motion multiple times or adding simple description to further emphasize the movement.
```

## 4. 官方示例：四要素齐全的一句

```yaml
# 条目元数据（策展者添加，非原文）
id: "jiqiao--38-runway-gen4-image-to-video-motion-only--01"
标题: "机械公牛穿越沙漠：主体运动 + 摄影机 + 场景运动 + 风格四要素（官方示例）"
原标题: ""
分类: "技巧锦囊"
标签: ["技巧锦囊", "图生视频", "只写运动", "场景运动", "手持", "风格词"]
适用模型: "Runway Gen-4（来源标注：Runway《Gen-4 Video Prompting Guide》，需配合输入图）"
语言: "en"
来源链接: "https://help.runwayml.com/hc/en-us/articles/39789879462419-Gen-4-Video-Prompting-Guide"
镜像: "2026-09-30 直接抓取官方帮助中心 HTML（box: /workspace/prompt-extract/raw/jiqiao-sources/runway_gen4.html；另存 /workspace/prompt-extract/raw/douyin-baolaoshi-one-take-fight/sources/）"
作者: "Runway（发布方）"
发布日期: ""
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本（官方指南「Prompting for Iteration」示例提示词）"
核对状态: "verified"
核对说明: "官方页面把这句按四种要素分色显示（每段一个 span），拼接后与 HTML 逐字一致；全小写、句点照原样。"
完整性: "完整"
备注: "页面未标注发布日期，故留空。官方页面附输入图与成片。"
技巧钩子: "图生视频别再描述图里已有的东西：只写「谁怎么动、镜头怎么动、环境怎么被带动」，并用 the subject / 位置词指代主体"
触发场景: "图生视频结果几乎不动、动作僵、或模型把图里的人「重画」走样时"
```

```text
a handheld camera tracks the mechanical bull as it runs across the desert. the movement disturbs dust that trails behind the mechanical creature. cinematic live-action.
```

## 总结（非原文）

- 图生视频时，文字只负责「动」：主体动作、摄影机运动、场景被带动的方式、风格词；外貌、服装、构图交给输入图。
- 指代用 the subject / 代词 / 位置词；多人时用「左边的 / 右边的」分配动作。
- 场景运动先用形容词暗示，不够再直接描述。
- 这些是 Runway Gen-4 的官方建议；Seedance 2.0 使用参考图时官方反而要求「主体定义清晰、说明与参考图的对应关系」（见 `技巧锦囊/35` 第 5、6 节），两者针对的输入方式不同（Runway 的输入图是首帧，Seedance 是多素材参考），不要混用。

本文件统计：计数条目 1（verified 1）；不计数代码块 3（官方原文段落）。
