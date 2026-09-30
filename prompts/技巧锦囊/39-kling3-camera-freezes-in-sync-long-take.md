# 技巧锦囊 · 可灵《Kling VIDEO 3.0 Model User Guide》：长镜头里「人停镜头停」的同步跟拍写法

## 来源概述（非原文）

> body: verbatim — `text` 围栏是官方示例提示词原文；无语言代码块为官方说明原文。「巧在哪」「总结（非原文）」为策展者所写，**非原文**。

- **source URL:** https://kling.ai/quickstart/klingai-video-3-model-user-guide
- **publisher:** 可灵 AI（Kling AI），页面结构化数据 datePublished 2026-02-06 15:51（UTC+8）
- **captured:** 2026-09-30（UTC+8）
- **license:** 未注明（来源未声明许可）
- **与本库已有内容的关系（去重）:** 本库 `运镜/31-kling.ai.md` 收的是 Kling 博客（kling-ai-prompt-guide）的两条示例，与本页不同；全库检索「freezes instantly」「camera freezes」无结果。`打斗运镜/34`（爆老师一镜到底）讲的是打斗长镜头的手持跟拍，本条是日常戏的同步跟拍，两者互补。
- 本文件计数条目：1 个 `text` 围栏；核对状态：verified 1。

## 1. 官方说明

```
Building on the Text-to-Video feature, VIDEO 3.0 introduces element binding, allowing you to lock specific elements of the frame to ensure the main character remains consistent. Even with camera movements like zooming, panning, or tilting, the subject stays clear and stable without shifting or disappearing.
```

## 2. 示例提示词

> 巧在哪（非原文）：整段反复出现「the camera tracks her … freezes instantly when she pauses」「she pauses, the camera freezes in sync」「she walks forward again, the camera tracks her in sync」，把镜头的走停和人物动作逐一绑定，长镜头因此有了呼吸和节奏。

```yaml
# 条目元数据（策展者添加，非原文）
id: "jiqiao--39-kling3-camera-freezes-in-sync-long-take--01"
标题: "职场一镜到底：人走镜头跟、人停镜头停（官方示例）"
原标题: ""
分类: "技巧锦囊"
标签: ["技巧锦囊", "一镜到底", "跟拍", "同步停顿", "参考图/素材引用", "首帧"]
适用模型: "Kling VIDEO 3.0（来源标注：可灵《Kling VIDEO 3.0 Model User Guide》；示例使用首帧 + 主体参考）"
语言: "en"
来源链接: "https://kling.ai/quickstart/klingai-video-3-model-user-guide"
镜像: "2026-09-30 直接抓取官方页面 HTML（box: /workspace/prompt-extract/raw/jiqiao-sources/kling3.html）"
作者: "可灵 AI / Kling AI（发布方）"
发布日期: "2026-02-06"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本（官方指南「2. Image-to-Video & Element Reference」示例提示词）"
核对状态: "verified"
核对说明: "与官方页面 HTML 转出的文本逐字核对一致；分号分隔照原样，无换行。"
完整性: "完整"
备注: "官方页面附首帧、主体参考图与成片，并对比了「首帧 + 主体一致性增强」与「只用首帧」两种输出。同节另说明：主体若已绑定音色，不建议在提示词里再指定音色。"
技巧钩子: "长镜头跟拍不闷的关键：写明「人停镜头也停、人走镜头再跟」，每个小动作都给镜头一个同步反应"
触发场景: "一条长镜头里人物要做一连串日常动作（进门、放包、签字、坐下），镜头却一直匀速漂移、没有节奏时"
```

```text
Authentic workplace texture, one continuous long take without any cuts. The camera follows the professional woman steadily in a medium shot throughout, moving in sync with her: the camera tracks her as she walks and freezes instantly when she pauses, with natural and smooth movements and fluid camera work. The woman walks forward out of the elevator, and the elevator doors close slowly and naturally behind her; she steps into the office area, takes off her sunglasses by hand, tucks them into her commuter bag casually, and nods politely to colleagues passing by; she pauses briefly, the camera freezes in sync, she hangs her commuter bag on the coat rack in the office area, then takes off her outer coat and hangs it on the same rack; after hanging up her clothes, she walks forward again, the camera tracks her in sync; a young man in a formal shirt walks towards her, hands her a document and a signature pen, she pauses, the camera freezes in sync, takes them and signs the document; after signing, she walks forward again, the camera tracks her in sync; finally, she walks to her desk, sits down by the chair, reaches out to pick up a cup of tea on the desk, and sips it with her head down, her movements relaxed and natural.
```

## 总结（非原文）

- **句式**：开头先定规则（「moving in sync with her: tracks her as she walks and freezes instantly when she pauses」），后面每个停顿点重复「she pauses, the camera freezes in sync」，每次起步重复「she walks forward again, the camera tracks her in sync」。
- **适用**：日常戏、职场戏、Vlog 式长镜头；打斗长镜头见 `打斗运镜/34`。
- **注意**：官方示例同时用了首帧和主体绑定（element binding）来保证人物一致；只靠文字能否同样稳定，官方未说明。Seedance 2.0 官方则建议单段内优先写缓慢连续的小幅动作（见 `docs/最佳实践.md` 第 3 节），本例正是这类动作，方向一致。

本文件统计：计数条目 1（verified 1）；不计数代码块 1（官方说明原文）。
