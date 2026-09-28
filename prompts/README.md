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

`cases/vfx-spectacle` 亦归入 `cases/特效/`（与 prompts `vfx→特效` 对齐）。

| 分类 | 条目（约） |
|------|-----------|
| 打斗运镜 | 59 |
| 特效 | 19 |
| 运镜 | 21 |
| 国漫3D | 31 |
| 真人漫剧 | 8 |
| 短剧 | 4 |
| 产品生活 | 11 |
| 电影大场面 | 5 |
| 动画电影感 | 3 |
| 变形转换 | 1 |
| 游戏PV | 1 |
| 超现实喜剧 | 3 |
| 恐怖 | 1 |
| UGC短视频 | 1 |
| 其他 | 8 |
| 人物卡 | 6 |
| 生图修画质 | 6 |
| **合计** | **~188** |

规则：

1. 每条必须是 **完整原文**（`body: verbatim`），禁止摘要/截断/改写。
2. 必须标注 **source URL** 与 **license/open-source tag**。
3. 若来源为图片中的提示词，用视觉识读逐字誊写，并在元数据标注 `source_type: image-ocr`（语义：图文视觉誊写，非自动 OCR 引擎）。
4. 抖音图文若仍无法拿到正文/配图，保留 blocker，**禁止编造**。

见 `../docs/CURATION-LOG.md` 与 `../docs/OPEN-SOURCE.md`。
