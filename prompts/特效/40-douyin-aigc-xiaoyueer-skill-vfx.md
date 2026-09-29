# Douyin · AIGC小悦儿 — 技能特效提示词（视觉誊写）

> body: verbatim — on-screen UI skill strings only; trailing `……` kept as shown. No invented continuation.

Source: https://v.douyin.com/DUJyrJkXy-0/ → https://www.douyin.com/video/7686436434173021478  
Author: AIGC小悦儿（抖音号 73972760866）  
Title cue: 「最惊艳的技能特效提示词」/ 合集「底层图形学提示词解析」  
License tag: `author-shared-on-douyin; copyright-retained; learning-archive`  
Curation: 2026-09-29 Asia/Shanghai  
`source_type: image-ocr`（视频帧 UI 视觉誊写；非自动 OCR 定稿）  
Raw dossier cited by the morning ingest: `raw/douyin-DUJyrJkXy-0/RECOVERY.md` — **not in this checkout**. Evening QC 2026-09-29 did not re-read frames, did not change these two strings, and did not invent text after `……`.

Count in this file: **2** skill bodies (+ caption archived outside fences for provenance)

Caption (not counted as skill body):

> 这是我目前为止用过最惊艳的技能特效提示词 ，一秒跳脱五毛贴图感，从核心光效到动态轨迹再到环境联动三层拆解，精准对标院线级特效质感，赶紧截屏下来悄悄看。#AI教学#AI漫剧教程#AIGC#游戏cg#ai创作浪潮

---

## 1. :Emissive 自发光分层渲染（核心光效）

- **source URL:** https://v.douyin.com/DUJyrJkXy-0/
- **canonical:** https://www.douyin.com/video/7686436434173021478
- **author:** AIGC小悦儿
- **layer:** 核心光效 / Emissive
- **source_type:** image-ocr
- **license:** `author-shared-on-douyin; copyright-retained; learning-archive`
- **prompt_len:** 35
- **notes:** UI 结尾为屏幕上的省略号；未 invent 省略号后内容。配套画面字卡含「高光锚定纹路中心」。第三层「环境联动」无独立 `:Skill` UI 箱。

### Prompt (verbatim)

```text
:Emissive 自发光分层渲染，精准管控核心亮度与边缘弥散梯度……
```

---

## 2. :Motion Blur 运动模糊采样（动态轨迹）

- **source URL:** https://v.douyin.com/DUJyrJkXy-0/
- **canonical:** https://www.douyin.com/video/7686436434173021478
- **author:** AIGC小悦儿
- **layer:** 动态轨迹 / Motion Blur
- **source_type:** image-ocr
- **license:** `author-shared-on-douyin; copyright-retained; learning-archive`
- **prompt_len:** 39
- **notes:** 屏幕原文止于「伴随对……」；禁止补全。

### Prompt (verbatim)

```text
:Motion Blur 运动模糊采样，还原轨迹拖影与粒子扩散动态，伴随对……
```
