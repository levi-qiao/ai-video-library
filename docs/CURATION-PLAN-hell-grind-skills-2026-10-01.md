# Hell Grind skills 策展计划（2026-10-01 Asia/Shanghai）

工作目录：`/workspace/_hell-grind-skills/`  
目标库：`/workspace/ai-video-library`（remote `levi-qiao/ai-video-library`）  
对照先例：PR #20 Seedance agent-skill 薄摘录（`技巧锦囊/45`）

## 源文件（已下载 · 与镜像 blob 一致）

| 源 | blob SHA | 用途 |
|----|----------|------|
| `CINEDANCE HIGGSFIELD SKILL.md` | `24d38044ae06e5159cf5662b2bf5e09164789894` | 空间锁 / 首帧占位 / camera side |
| `ACTING SKILL.md` | `383db473e88e70a2e3ed30f962e4ea56da5a645b` | 压力行为 / master / eye life / rewrite / states |
| `LIRA SKILL.md` | `1e5c80731d5f6ccd0d2e803678598da42ce835e7` | IMAGE-only 4-D 指针 |
| Brief | https://higgsfield.ai/@higgsfield.studio/projects/hell-grind | 官方项目入口 |
| 镜像仓 | https://github.com/XucroYuri/higgsfield-hell-grind-opensource/tree/master/skills | 可引用 HTML 路径 |

权威层级：火山引擎官方 > `技巧锦囊/45` Seedance 社区结构 > Hell Grind 本轮净新增（标社区）> 跳过全文 dump / 成片资产 / 与 45 重复项。

## KEEP（写入库）

| 路径 | 内容 |
|------|------|
| `prompts/技巧锦囊/46-hell-grind-cinedance-acting-lira-synthesis.md` | **唯一**综合条目：CINEDANCE 首帧+米级空间锁；camera side 方法；ACTING 压力/eye life/states；LIRA 4-D 指针。每块标明社区 vs 官方。 |
| `docs/权威来源.md` §7 | Hell Grind Brief + 三 skill 列为 **SECONDARY** |
| `docs/最佳实践.md` | 仅净新增 §2.13–14、§7 指引、§9.8 LIRA 指针 |
| `skills/hell-grind-library-router/SKILL.md` | 薄路由：指路 + 注明完整 skill 可能已在 agent 侧安装 |
| `prompts/技巧锦囊/README.md` | 补 46 的卡片 |
| `docs/CURATION-LOG.md` | 本轮记录 |
| `docs/CURATION-PLAN-hell-grind-skills-2026-10-01.md` | 本计划 |

## SKIP（整文件 / 大块不入库）

| 内容 | 原因 |
|------|------|
| CINEDANCE 全文 ~1330 行 | 任务禁止 wholesale；只留空间/首帧/camera side |
| Optics FOV 词表、Physics、Dialogue、Quality suffix 长段 | 与 `运镜/*`、官方公式、社区运镜词典重叠或过厚 |
| Hell Grind 成片资产包 / 剧情 | 非提示词写法库 scope |
| ACTING 坏演技 Atlas 全文、worked example 整角 | 方法已由短摘录覆盖；避免角色卡 dump |
| LIRA Model routing / Full Reference / Templates | 与 `人物卡/*`、`首尾帧生图/*`、`docs/首尾帧工作流.md` 冗余；平台专有 |
| 与 `技巧锦囊/45` 重复：载体编译、ignore、保真度预算、打斗 2 秒钩子 | 已收；本轮不复述 |
| 与 `最佳实践` §5.2 重复：另立「正面 > 否定」通用新规 | 已有；CINEDANCE 仅作方法备注 |

## MERGE（并入已有文件）

| 净新增点 | 并入 |
|----------|------|
| 米级空间锁 + 首帧占位 + camera side | `最佳实践.md` §2.13；详述在 46 |
| 压力行为 / master 150–220 / eye life / rewrite / states-not-transitions | `最佳实践.md` §2.14；详述在 46 |
| LIRA 4-D IMAGE 指针 | `最佳实践.md` §9.8；详述在 46 §5 |
| SECONDARY 登记 | `权威来源.md` §7 |

## 去重对照（已检索）

- `双胞胎` / `轨道补齐` / `发力链`：已在 `35`、`最佳实践`、`打斗运镜/32` — **不再复述**。
- Emily carriers / ignore / allocation / 2s fight hook：已在 `45` — **不再复述**。
- 「正面优先否定」：已在 `最佳实践` §5.2 — Hell Grind 不另立通用条。
- `within 1 meter` / `camera side` / `eye life` / `states, not transitions`：库内先前无命中 — **本轮 KEEP**。

## 实施顺序

1. 写本计划  
2. 写 46 + 改权威来源 / 最佳实践 / README / hell-grind router / CURATION-LOG  
3. `python3 scripts/build_index.py` 与 `--check`  
4. `rg` 抽检关键短语  
5. commit + PR to main（不 merge）
