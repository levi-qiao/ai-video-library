# Seedance agent-skill 策展计划（2026-10-01 Asia/Shanghai）

工作目录：`/workspace/_curate-seedance/`  
目标库：`/workspace/ai-video-library`（remote `levi-qiao/ai-video-library`）

## 源仓（shallow clone · 核对 SHA）

| 源 | HEAD | 用途 |
|----|------|------|
| Emily2040/seedance-2.0 | `4668457e560eee06e95d7fcfdf441c8c0bba802e` | 导演结构 / 参考契约 / 保真度预算 / 场记式写法（社区包装） |
| dexhunter/seedance2-skill | `516284d5bab58361bfdfed3cc96cee3e837d4c44` | `@` 引用用途表（即梦 UI 社区整理） |
| beshuaxian/higgsfield-seedance2-jineng | `83dcb10ee38c9694ac0f455ec55a62f2be3b8a14` | 仅扫 `05-fight` / `01-cinematic` / `11-social-hook` |

权威层级：火山引擎官方 > Emily 导演结构（标社区）> dexhunter `@` 用途表（若库内未覆盖）> beshuaxian 打斗/电影钩子（仅净新增）> 跳过 Higgsfield API / 营销文。

## KEEP（写入库）

| 路径 | 内容 |
|------|------|
| `prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md` | **唯一**综合条目：Emily 导演读 → 可见载体、参考一职一角+ignore、保真度三预算、Direct-for-model 要点；dexhunter `@` 用途分层；beshuaxian 打斗开场 2 秒钩子（薄）。每块标明社区 vs 官方。 |
| `docs/权威来源.md` §6 | 上述三仓列为 **SECONDARY 社区来源**（非权威裁定依据） |
| `docs/最佳实践.md` | Seedance / 打斗节仅加净新增 bullet（引用 45 与源路径） |
| `skills/seedance-library-router/SKILL.md` | 薄路由：指向库内路径，不复制提示词正文 |
| `prompts/技巧锦囊/README.md` | 补 45 的卡片 |
| `docs/CURATION-LOG.md` | 本轮记录 |
| `_curate-seedance/CURATION-PLAN.md` | 本计划（不入库亦可；PR 描述引用） |

## SKIP（整仓 / 大块不入库）

| 内容 | 原因 |
|------|------|
| Emily 全仓 dump（API matrix、surface、pricing、多语言 vocab、ACEScolor、filter/copyright 全套） | 非本库 scope；平台事实以官方为准；vocab 已有 `docs/术语速查.md` |
| Emily `first-last-frame-guide` / i2v 大段 | 重复 `docs/首尾帧工作流.md` + `prompts/首尾帧生图/03-*` + `技巧锦囊/35` |
| Emily recipes / genre library / prompt examples 批发 | 与库内分类提示词重叠；官方优先 |
| Emily anti-slop / filter 全文 | 安全策略由官方与本库裁定；不复制社区「绕过滤」叙述 |
| dexhunter 运镜/景别表、延长/编辑整段示例 | 重复 `运镜/*`、`技巧锦囊/35`、官方 `视频1` 写法、`提示词写法/33` |
| dexhunter 电商/短剧整章示例 dump | 营销模板；无净新增结构 |
| beshuaxian `05` 十余种战斗风格完整提示词 | 与 `打斗运镜/32–34` + fight skill 骨架重复；禁止批发 |
| beshuaxian `01-cinematic` 完整模板与风格速查 | 与 `运镜/*`、`光影打光/*`、官方公式重复 |
| beshuaxian `11-social-hook` 百科（25+ 模式、平台优化） | 营销/完播率文，非 Seedance 可验证写法 |
| Higgsfield 官方 API skill | 任务明确跳过 |

## MERGE（并入已有文件）

| 净新增点 | 并入 |
|----------|------|
| 参考素材「一职一角 + ignore 不转移」 | `最佳实践.md` §2 补充；详述在 45 |
| 单镜保真度预算（身份 / 运动 / 场景密度三选一主） | `最佳实践.md` §4 或 §2；详述在 45 |
| 叙事内部判断 → 只写可见/可听载体 | `最佳实践.md` §2；详述在 45 |
| 多镜 lock line（光/身份/站位/机位侧） | 并入 45；最佳实践一条引用 |
| 打斗开场 2 秒钩子（对手距离 / 兵器或流派 / 能量） | `最佳实践.md` §3 一条；不新建打斗全文 |
| `@图片N/@视频N` 用途分层表 | 45 内对照官方「图片1/视频1」；`最佳实践` 已有映射声明则只补「用途互斥」 |

## 去重对照（已检索）

- `双胞胎` / `轨道补齐` / `发力链`：已在 `技巧锦囊/35`、`最佳实践`、`打斗运镜/32` — **不再复述为新规则**。
- `@Image1` / `@图片1`：官方与 `提示词写法/33`、`首尾帧生图/03` 已有 — 45 只补 **用途互斥 + Exact Tag 不改写**（社区）。
- fight skill 已有发力/镜头骨架 — beshuaxian 不覆盖。

## 实施顺序

1. 写本计划 ✅  
2. 写 45 + 改权威来源 / 最佳实践 / README / skill router / CURATION-LOG  
3. `python3 scripts/build_index.py`  
4. `rg` 抽检关键短语  
5. commit + `gh pr create`
