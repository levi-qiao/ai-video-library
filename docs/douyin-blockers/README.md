# Douyin 图文 blockers（视觉誊写未达标）

硬规则：**禁止编造**提示词正文。宁可 incomplete + blocker。

## Tct4dNh1dzo / 小椰冻奶 · 法天象地

- short: https://v.douyin.com/Tct4dNh1dzo/
- note: `7689872479989721957`
- 状态: **仍未入库 verbatim**
- 已做到: Playwright 打开 `m.douyin.com` / `iesdouyin` share，抓到 **2 张** 图文配图（480×640 webp），见本目录 `Tct4dNh1dzo-img0{0,1}-480x640.png`
- 未做到: 更高分辨率变体均 403；480px 上密排中文经多次视觉识读 **字符不一致**（无法保证 character-accurate），故 **不** 写入 `prompts/` 正文
- 对照等价公开源（非本作者）: `prompts/特效/30-freyavideo.com.md`（FreyaVideo 法天象地）
- 2026-09-29 晚间 QC 重读 `Tct4dNh1dzo-img00` 与 `img01`（480×640）。两张都是密排分镜字，字号小、压缩糊、部分行被裁切。**仍然无法逐字确认全文**，因此 **不** 写入 `prompts/`，也不把不确定识读当 verbatim。

## D28NAIbzFm0 / 小鱼漫剧 · AI漫剧打斗

- short: https://v.douyin.com/D28NAIbzFm0/
- note: `7687528916584719195`
- 状态: share / m.douyin 均「抱歉出错了」，**无配图、无正文**

## 心流人物卡短链

- `v.douyin.com/F0CQtRHUZQk/` / `bV59188e3cE/` / `UP3Ck9IsM_U/`
- 状态: 仍 blocker；`bV59188e3cE` 重定向到无关图文，不可当作心流人物卡原文

## mM3gTkJWuzQ / AI绘梦菌 · AI提示词编写思路

- short: https://v.douyin.com/mM3gTkJWuzQ/
- video_id: `7690573169337453860`
- content_type: **video**（非图文）
- 状态: **仍未入库 verbatim** — 口播/字幕/画面字 **0 chars**（SSR shell 与 item API 均为空）
- 详见: `douyin-mM3gTkJWuzQ-AI绘梦菌.md`
- 公开方法论替代（**不是**该抖音正文）: `prompts/提示词写法/01-web-prompt-writing-methodology.md`

## -aQ762F_Y4k / 胡小绿 · 1个视频让你学会用AI提示词控制画面景别（2026-09-30）

- short: https://v.douyin.com/-aQ762F_Y4k/
- video_id: `7685608233369056433`
- content_type: **video**（16.5 s，无口播）
- 状态: **已入库（部分）** → `prompts/运镜/43-douyin-huxiaolv-shot-size-jingbie.md`：帖子文案逐字、画面字幕 image-transcript（16 条逐镜标注）、ASR（无人声）、互动数。
- 仍 blocker: **完整提示词未公开**。画面字幕只是逐镜标注，不是完整提示词；评论区作者回复「发会员群里了咧王总」，推断完整内容只在会员群。未编造、未计入 ` ```text `。
- 文案后半段换行不可见（网页 h1 去掉换行，meta 截断），按 h1 连排保存。
- 可复用的获取方法（本次首次成功拿到抖音 mp4）: 无头 Chrome（Playwright，xvfb）打开 `www.douyin.com` 取**未登录匿名 cookie** → `yt-dlp --cookies <netscape.txt>`；文案用 Googlebot UA 抓 `www.douyin.com/video/<id>` SSR 的 h1/meta。iesdouyin 分享页 `_ROUTER_DATA` 仍为空壳。该方法未在 `mM3gTkJWuzQ` 上重试。
