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

计数口径：每个 ` ```text ` 围栏算 1 条原文（含人物卡/修画质子模板）。2026-09-29 早搜后重计。

| 分类 | 条目（约） |
|------|-----------|
| 打斗运镜 | 68 |
| 特效 | 21 |
| 运镜 | 26 |
| 国漫3D | 32 |
| 真人漫剧 | 8 |
| 短剧 | 5 |
| 产品生活 | 13 |
| 电影大场面 | 7 |
| 动画电影感 | 6 |
| 变形转换 | 1 |
| 游戏PV | 2 |
| 超现实喜剧 | 6 |
| 恐怖 | 2 |
| UGC短视频 | 3 |
| 其他 | 8 |
| 人物卡 | 28 |
| 生图修画质 | 23 |
| 提示词写法 | 19 |
| **合计** | **~278** |

规则：

1. 每条必须是 **完整原文**（`body: verbatim`），禁止摘要/截断/改写。
2. 必须标注 **source URL** 与 **license/open-source tag**。
3. 若来源为图片中的提示词，用视觉识读逐字誊写，并在元数据标注 `source_type: image-ocr`（语义：图文视觉誊写，非自动 OCR 引擎）。
4. 抖音图文若仍无法拿到正文/配图，保留 blocker，**禁止编造**。

见 `../docs/CURATION-LOG.md` 与 `../docs/OPEN-SOURCE.md`。

## 2026-09-29 增补

- 新增分类 **`提示词写法/`**：公开方法论公式与示例（web），因抖音 `v.douyin.com/mM3gTkJWuzQ/`（AI绘梦菌「AI提示词编写思路」）正文不可恢复；blocker 见 `docs/douyin-blockers/douyin-mM3gTkJWuzQ-AI绘梦菌.md`。
- 配套 skill：`skills/ai-video-prompt-writing-methodology/SKILL.md`。
