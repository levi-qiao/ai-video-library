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
