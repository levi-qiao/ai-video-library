# 提示词归档（仅原文 verbatim）

分类目录已统一为 **中文文件夹名**（由原英文 kebab-case 重命名）。优先级主题只是检索偏置，找到后再归类；若新集群无合适目录，可新增清晰中文名并在本表登记。

历史偏置：`打斗运镜/` > `特效/` > `运镜/` > `国漫3D/` …

## 目录映射（English → 中文）

| 原英文目录 | 中文目录 |
|------------|----------|
| fight-camera | 打斗运镜 |
| vfx | 特效 |
| camera-motion | 运镜 |
| guoman-3d | 国漫3D |
| other | 其他 |
| live-action-comic | 真人漫剧 |
| short-drama | 短剧 |
| product-lifestyle | 产品生活 |
| cinematic-spectacle | 电影大场面 |
| anime-cinematic | 动画电影感 |
| morph-transform | 变形转换 |
| game-pv | 游戏PV |
| surreal-comedy | 超现实喜剧 |
| horror | 恐怖 |
| ugc-vlog | UGC短视频 |
| character-cards | 人物卡 |
| image2-denoise | 生图修画质 |
| *(new)* | 提示词写法 |

`cases/vfx-spectacle` 亦归入 `cases/特效/`（与 prompts `vfx→特效` 对齐）。

计数口径：每个 ` ```text ` 围栏算 1 条原文。2026-09-29 晚间 QC 后实计 216，2026-09-30 增补后（含下篇）238，同日早搜再补上篇与新源后 275，同日午间全库去重（−2）并新增胡小绿景别（+0 围栏）后 **273**。

| 分类 | 条目 |
|------|------|
| 打斗运镜 | 42 |
| 特效 | 19 |
| 运镜 | 68 |
| 国漫3D | 25 |
| 真人漫剧 | 8 |
| 短剧 | 5 |
| 产品生活 | 15 |
| 电影大场面 | 11 |
| 动画电影感 | 6 |
| 变形转换 | 1 |
| 游戏PV | 2 |
| 超现实喜剧 | 7 |
| 恐怖 | 2 |
| UGC短视频 | 7 |
| 其他 | 7 |
| 人物卡 | 11 |
| 生图修画质 | 17 |
| 提示词写法 | 20 |
| **合计** | **273** |

规则：

1. 每条必须是 **完整原文**（`body: verbatim`），禁止摘要/截断/改写。
2. 必须标注 **source URL** 与 **license/open-source tag**。
3. 若来源为图片中的提示词，用视觉识读逐字誊写，并在元数据标注 `source_type: image-ocr`（语义：图文视觉誊写，非自动 OCR 引擎）。
4. 抖音图文若仍无法拿到正文/配图，保留 blocker，**禁止编造**。

见 `../docs/CURATION-LOG.md` 与 `../docs/OPEN-SOURCE.md`。

## 2026-09-29 增补

- 新增分类 **`提示词写法/`**：公开方法论公式与示例（web），因抖音 `v.douyin.com/mM3gTkJWuzQ/`（AI绘梦菌「AI提示词编写思路」）正文不可恢复；blocker 见 `docs/douyin-blockers/douyin-mM3gTkJWuzQ-AI绘梦菌.md`。
- 配套 skill：`skills/ai-video-prompt-writing-methodology/SKILL.md`。

## 2026-09-29 — AIGC小悦儿技能特效

- Douyin `v.douyin.com/DUJyrJkXy-0/`（AIGC小悦儿「最惊艳的技能特效提示词」）→ `特效/40-douyin-aigc-xiaoyueer-skill-vfx.md`（**+2** UI skill 原文：`:Emissive…` / `:Motion Blur…`；环境联动层无第三段 typed skill；省略号后未编造）。
- Raw：`raw/douyin-DUJyrJkXy-0/RECOVERY.md`（该目录不在当前仓库；晚间 QC 未改这两条，也未补全 `……`）。

## 2026-09-29 晚间 QC

- 删除截断、未填模板、过短碎片，并去掉跨文件完全重复。实计 **216** 条 ` ```text `（详见 `docs/CURATION-LOG.md` 晚间一节）。
- 抖音 `Tct4dNh1dzo` 两张图重读后仍无法逐字誊写，未入库。

## 2026-09-30 — X @AdrianPunk115「AI 视频运镜词典（下篇）」

- X 长文 https://x.com/AdrianPunk115/status/2104523576020017575（Adrian Punk，2026-09-28）→ `运镜/41-x-adrianpunk115-camera-dictionary-part2.md`（**+22** ` ```text `：13 条完整示例 + 8 条作者模板/骨架 + 1 条选择清单；全文 verbatim，另附策展者中文总结、蒸馏模板与速查表，均标注“非原文”）。
- 4 张信息图（四层 / 六组易混 / 按情绪 / 按场景）已视觉誊写为表格（`source_type: image-ocr`），不计入围栏数；其余 20 张为无文字示意插画。
- 上篇已于同日早搜收录：见下方「2026-09-30 早搜」与 `运镜/42-x-adrianpunk115-camera-dictionary-part1.md`。


## 2026-09-30 早搜补充

- X @AdrianPunk115「AI 视频运镜词典（上篇）」https://x.com/AdrianPunk115/status/2104172387575222768 → `运镜/42-x-adrianpunk115-camera-dictionary-part1.md`（**+25** ` ```text `；信息图 image-ocr：六层结构 / 按情绪 / 按场景）。
- Runway Seedance 2.0 官方提示词指南 https://runway.com/resources/seedance-2-0-prompt-guide → 分散写入 `提示词写法/` `电影大场面/` `产品生活/` `UGC短视频/` `超现实喜剧/` 下 `32-runway-seedance-2.0-prompt-guide.md`（**+5**）。
- GitHub watreesir/awesome-kling-4 → `UGC短视频/` `产品生活/` `电影大场面/` 下 `32-github-watreesir-awesome-kling-4.md`（**+6**）。
- GitHub BeatAPI/awesome-seedance-2-5-prompts（Vietnamese Mythic Sea Battle）→ `电影大场面/32-github-beatapi-awesome-seedance-2-5.md`（**+1**；Tokyo Samurai 与库内 `运镜/20-web-camera-motion-prompts.md` 重复，跳过）。
- 本轮合计 **+37** ` ```text `，库内 **275**。

## 2026-09-30 午间 — 抖音胡小绿「景别」+ 全库去重

- 抖音 https://v.douyin.com/-aQ762F_Y4k/（胡小绿「1个视频让你学会用AI提示词控制画面景别」，2026-09-15）→ `运镜/43-douyin-huxiaolv-shot-size-jingbie.md`：帖子文案逐字 + 16 条画面字幕（image-transcript）+ ASR（无人声）+ 中文总结/景别中英词表/蒸馏模板（非原文）。**+0** ` ```text `：视频未公开完整提示词（疑在会员群），blocker 见 `docs/douyin-blockers/README.md`。
- 全库去重（`prompts/` + `cases/` + `raw/`）：
  - `打斗运镜/02` §3.2/§3.3（seedance.tv 中文译本）→ 保留 `打斗运镜/20` §3/§5 英文原文，中文版 URL 并入元数据（**−2**）。
  - `raw/05-web-prompt-writing-methodology.md`（17/18 围栏与 `提示词写法/01` 逐字重复）删除，独有的八层概览与术语表子集并入 `提示词写法/01` §3.0（不计数）。
  - `raw/douyin-mM3gTkJWuzQ-blocker.md` 与 `docs/douyin-blockers/douyin-mM3gTkJWuzQ-AI绘梦菌.md` 字节相同，删除 raw 副本。
  - `打斗运镜/01-lansenai-x.md` Post 2/3/4 正文与 3 个 lansenai case 的 `prompt/prompt.txt` 逐字相同 → 正文只留 case，archive 留元数据并指向 case（非围栏，不影响计数）。
  - 景别/运镜方法论（胡小绿、AdrianPunk115 上下篇、提示词写法/01）是不同作者的独立原创，**不删，互相加链接**。
- 合计 275 → **273**。明细见 `docs/CURATION-LOG.md`「2026-09-30 午间」。
