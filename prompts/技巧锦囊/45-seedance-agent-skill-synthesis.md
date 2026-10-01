# 技巧锦囊 · Seedance agent-skill 综合摘录（Emily 导演结构 + dexhunter @ 用途 + beshuaxian 打斗开场钩子）

## 来源概述（非原文）

> body: mixed — 下文「社区原文摘录」`text` 围栏为对应 GitHub skill 文件的短摘录（逐字）；其余表格、对照、策展备注为策展者编写，**非原文**。本文件**不是** skill 仓镜像，只收与库内官方条目不重叠、且可核对的结构 / 词汇。

- **源仓（SECONDARY 社区，非权威裁定）：**
  - Emily2040/seedance-2.0 @ `4668457e560eee06e95d7fcfdf441c8c0bba802e`（MIT）— `references/directors-read.md`、`reference-transfer-contract.md`、`allocation-model.md`、`direct-for-the-model.md`、`field-observed-tips.md`
  - dexhunter/seedance2-skill @ `516284d5bab58361bfdfed3cc96cee3e837d4c44` — `zh/SKILL.md`「核心语法：@ 引用系统」
  - beshuaxian/higgsfield-seedance2-jineng @ `83dcb10ee38c9694ac0f455ec55a62f2be3b8a14` — `skills/05-fight-scenes/zh-CN/SKILL.md`「打斗场景的2秒钩子框架」
- **收录：** 2026-10-01（Asia/Shanghai）；工作克隆在策展环境 `/workspace/_curate-seedance/`（不入库）
- **许可：** 各源仓自有许可（Emily MIT；其余见仓库）；本库只摘录短片段用于学习归档，并标明社区说法
- **权威层级（强制）：** 火山引擎 / Seedance 官方文档（见 `docs/权威来源.md` §2.1、`技巧锦囊/35`、`首尾帧生图/03`）> 本文件社区结构。与官方矛盾时以官方为准，并在备注写明。
- **与本库已有内容的关系（去重）：**
  - **不重复：** 轨道补齐 / 向前延长 / 白模续写 / 防双胞胎 / 删帧拼接（已在 `技巧锦囊/35`）；发力链（`打斗运镜/32`、`最佳实践` §3）；官方 `@图片 1` 宿舍示例（`提示词写法/33`）；首尾帧 API 与关键帧（`首尾帧生图/03`、`docs/首尾帧工作流.md`）；运镜词表（`运镜/*`、SD1.0 官方）。
  - **本文件只补：** ① 叙事内部判断如何落成可见载体；② 参考「一职一角 + 明确不转移」；③ 单镜保真度预算（身份 / 运动 / 场景密度）；④ 多镜 lock line；⑤ `@` 用途分层表（对照官方「图片1/视频1」写法）；⑥ 打斗开场 2 秒信息钩子（薄，不批发风格提示词）。
- 本文件计数条目：3 个 `text` 围栏（社区短摘录）；其余为方法说明，不计数。核对状态：verified 3（对照上述 SHA 文件）。

## 1. 社区包装 vs 官方：怎么用本文件

| 层级 | 用什么 | 本库路径 |
|------|--------|----------|
| 官方（优先） | 素材上限、首尾帧 role、双胞胎、轨道补齐、镜头序号 vs 时间戳、否定词范围 | `docs/权威来源.md` §2.1；`技巧锦囊/35`；`docs/最佳实践.md`；`首尾帧生图/03` |
| 社区结构（可试） | 导演读 → 载体、参考契约、保真度预算、lock line、@ 用途互斥、打斗 2 秒钩子 | **本文件**；汇总进 `docs/最佳实践.md` 的对应 bullet |
| 跳过 | API/计价/surface 矩阵、多语言 vocab dump、15+ 打斗风格全文、social-hook 营销百科 | 见策展计划 SKIP |

> 策展备注（非原文）：Emily 仓自称「operating loop / Director's Read」——是**社区把影视方法打包成 agent 流程**，不是火山引擎官方 API。dexhunter 的 `@图片1` 是即梦界面常见写法；官方文档正文更多用「图片1 / 视频1」（可带或不带 `@`）。绑定语义以官方「声明映射关系」为准（SD2.0 / SD2.5）。

## 2. Emily · Director's Read → 只写可见 / 可听载体（社区）

> 巧在哪（非原文）：写提示词前先在脑内分清「叙事转折」还是「展示/表演」；叙事字段（欲望、权力、潜台词）**禁止原样进生成提示词**，必须改成机位、视线、道具动作、站位变化等载体。

**社区方法骨架（非原文转述，完整字段名见源文件）：**

```
叙事镜头内部记录（勿写入最终提示词）：
  dramatic function / turn / POV / power shift /
  hidden want / obstacle / subtext /
  visible suppressed behavior / non-transferable detail /
  stock solution refused

编译成载体后再写生成句：
  POV → 机位、知情范围、视线、声音透视
  power shift → 高低、占幅、距离、谁先动
  want/obstacle → 任务、道具动作、靠近或后退
  suppressed behavior → 一个足够被镜头读到的小动作
  turn → 可见的前后状态差 + 镜头落点
```

```yaml
# 条目元数据（策展者添加，非原文）
id: "jiqiao--45-seedance-agent-skill-synthesis--01"
标题: "Director's Read：内部叙事字段编译成可见载体（社区摘录）"
原标题: "Compile to Carriers"
分类: "技巧锦囊"
标签: ["技巧锦囊", "Seedance", "社区说法", "分镜/多镜头", "叙事载体"]
适用模型: "Seedance 2.0（社区 skill 包装；官方未使用 Director's Read 术语）"
语言: "en"
来源链接: "https://github.com/Emily2040/seedance-2.0/blob/4668457e560eee06e95d7fcfdf441c8c0bba802e/references/directors-read.md"
镜像: "shallow clone /workspace/_curate-seedance/seedance-2.0 @ 4668457e"
作者: "@Emily2040（社区 skill）"
发布日期: "2026-10-01"
热度: "未知（来源无公开互动数据）"
许可: "MIT（源仓 LICENSE）"
原文类型: "文本（community skill reference 短摘录）"
核对状态: "verified"
核对说明: "2026-10-01 对照 directors-read.md「Compile to Carriers」表与「Do not paste … into the final generation prompt」句逐字摘录；未改词。"
完整性: "片段：仅摘 Compile to Carriers 表头说明与禁令句，完整十字段与示例见源文件"
备注: "社区包装。与官方不冲突：官方要求写清主体/动作/场景/镜头；本条强调「情绪抽象词要落成行为」。"
技巧钩子: "欲望、权力、潜台词先写在内部提纲里，最终提示词只留机位、视线、道具动作和前后状态差"
触发场景: "短剧/对白镜头写了很多「内心纠结」「气场压制」，画面却演不出来时"
```

```text
Translate every useful abstraction into something the model can render or play:

| Internal read | Prompt carrier |
|---|---|
| POV | shot position, information withheld or revealed, eyeline, sound perspective |
| power shift | height, frame share, distance, who moves first, who yields space |
| hidden want/objective | a task, prop action, approach, retreat, delay, or repeated attempt |
| obstacle/tactic | visible interference followed by one playable response |
| subtext/contradiction | words against body, smile against grip, agreement against retreat, silence against urgent action |
| visible suppressed behavior | one timed gesture the camera can hold long enough to read |
| turn | a legible before/after state and camera endpoint |
| non-transferable detail | the exact object, ritual, sound, or environment fact preserved in the shot |
| stock solution refused | a physical exclusion only when needed, paired with the chosen replacement |

Do not paste `dramatic function`, `POV`, `power shift`, `hidden want`, `subtext`, or other read labels into the final generation prompt.
```

## 3. Emily · 参考转移契约：一职一角 + ignore（社区）

> 巧在哪（非原文）：官方已要求「声明映射」（见 `最佳实践` §2）；社区补强的是——每个素材只领一个主职，并显式写出**不要**从该素材转移什么，避免运镜参考把人脸/背景一起带过来。

**与官方对照（非原文）：** SD2.0 / SD2.5 要「主体定义清晰、每个主体标注对应参考图」；本条的 `@Image1 controls … only; ignore …` 是社区英文句式，投即梦 / 方舟时可改写为「参考图片1 的运镜，不参考其人物与背景」。

```yaml
# 条目元数据（策展者添加，非原文）
id: "jiqiao--45-seedance-agent-skill-synthesis--02"
标题: "参考转移契约：Exact Tag + 一职一角 + ignore 子句（社区摘录）"
原标题: "Reference Transfer Contract"
分类: "技巧锦囊"
标签: ["技巧锦囊", "Seedance", "社区说法", "参考图/素材引用"]
适用模型: "Seedance 2.0（社区；绑定写法随界面：@Image1 / @图片1 / 图片1）"
语言: "en"
来源链接: "https://github.com/Emily2040/seedance-2.0/blob/4668457e560eee06e95d7fcfdf441c8c0bba802e/references/reference-transfer-contract.md"
镜像: "shallow clone /workspace/_curate-seedance/seedance-2.0 @ 4668457e"
作者: "@Emily2040（社区 skill）"
发布日期: "2026-10-01"
热度: "未知（来源无公开互动数据）"
许可: "MIT（源仓 LICENSE）"
原文类型: "文本（community skill reference 短摘录）"
核对状态: "verified"
核对说明: "2026-10-01 对照 reference-transfer-contract.md「Exact Tag Rule」「Role Separation」「Transfer And Ignore Clause」逐字摘录关键句。"
完整性: "片段：省略 Continuity Source / Multi-Subject Selector 全文，要点见下方策展备注"
备注: "标签写法保留用户原文，勿擅自把 @Image1 改成 @图片1。防双胞胎、大头照+全身照仍以官方 `技巧锦囊/35` / `首尾帧生图/03` 为准。"
技巧钩子: "每个参考只领一个主职，并写明 ignore 身份/环境/运镜中不该转移的项"
触发场景: "参考视频只想借运镜，结果脸、服装、背景一起漂过来时"
```

```text
Preserve every user-supplied reference tag exactly. Never invent, normalize, translate, reformat, renumber, correct spacing, or change case in tags such as `@Image1`, `@Image 1`, `@Image1`, `[Video 1]`, or interface-provided equivalents.

Assign each reference one primary role:

- image: identity, product, pose, costume, environment, first frame, or last frame;
- video: source clip, motion, camera, timing, blocking, or continuity source;
- audio: tempo, ambience, music phase, rhythm, delivery tone, or active dialogue source;
- final frame: observed state or target endpoint.

State what transfers and what must not transfer. R2V and continuation work fail when identity, motion, camera, environment, and audio roles bleed together.

Every role-bound reference should be expressed as:

`[ReferenceTag] controls [role] only; ignore [identity/environment/logo/audio/camera/motion] from that reference.`
```

## 4. Emily · 保真度预算 + Direct-for-the-model（社区，方法不计数）

> 巧在哪（非原文）：一镜里同时要「脸稳 + 大动作 + 群戏密度」会互相抢预算；先定本镜主花销，其余刻意省。另：一句里堆多个主动作，模型常只演一个；切镜后不重申光/人/站位/机位侧会丢连续性。

**Allocation（社区转述，非原文）：**

| 主花销 | 买到什么 | 典型代价 |
|--------|----------|----------|
| Identity fidelity | 脸 / 产品 / 服装稳定 | 大幅运动易漂 |
| Motion boldness | 动作与物理 | 近景脸手易糊 |
| Scene density | 群杂与层次 | 单人精度下降 |

规则（社区）：每镜只选一个 primary + 至多一个 secondary；身份能交给参考图的，就不要在正文里重复描写省预算。

**Direct-for-the-model 要点（社区转述，非原文；详见源 `direct-for-the-model.md`）：**

1. 情绪 = 一个白话感受词 + 一个身体锚点；禁成语直译（如「脸沉下来」被渲成脸变灰）。
2. 每镜一个主动作；其余人写 idle business，禁止「全员不动」冻成假人。
3. 每个分镜块末尾 lock line：光源与色、主创年龄/发型/服装、相对地标站位与朝向、摄影机在房间哪一侧。
4. 非自愿后果（绊倒、衣角夹门）不要写成角色主动终点；写刻意动作，或后果放画外。

> 与官方关系：SD2.0「单镜一种运镜」、武戏「分段拼接」仍优先；本条是社区场记纪律，不替代官方时长/素材上限。

## 5. dexhunter · `@` 引用用途分层（社区整理，对照官方）

> 巧在哪（非原文）：把「参考了谁」写成「参考它的哪一层」（形象 / 运镜 / 动作 / 特效 / 节奏 / 音色），减少素材串味。官方示例已有「参考 @视频 1 的运镜方式」（`提示词写法/33`）；下表是社区扩写的用途清单，**不是**新 API。

**用途表（策展者据 `zh/SKILL.md` 整理，非逐字全文）：**

| 用途 | 社区示例写法 | 官方侧已有近似 |
|------|--------------|----------------|
| 首帧 / 尾帧 | `@图片1 作为首帧` | SD2.5 `role=first_frame/last_frame` 或提示词「图片 x 为首帧」（`首尾帧生图/03`） |
| 人物形象 | `参考 @图片1 的人物形象` | 「面部特征参考图片1（大头照）」（官方） |
| 运镜 | `参考 @视频1 的运镜效果` | `提示词写法/33` 官方示例 |
| 动作编排 | `参考 @视频1 的动作编排` | 社区常见；官方强调映射声明 |
| 特效 | `完全参考 @视频1 的特效和转场` | `技巧锦囊/35` 建议用参考视频定义特效 |
| 节奏 / BGM / 音效 | `视频节奏参考 @视频1` / `BGM参考 @音频1` | 视界面是否支持音频参考；以当前官方文档为准 |

**组合一句（社区原文短摘，作语法示意，不计数）：**

```
@图片1 的人物作为主体，参考 @视频1 的运镜和动作编排，
背景BGM参考 @音频1，场景参考 @图片2
```

> 策展备注（非原文）：即梦界面常用 `@图片1`；火山文档示例常见「图片1 / 视频1」。**Exact Tag：用户已写哪种就保留哪种，不要互相「纠正」。** 输入张数 / 时长上限以官方为准（图片 ≤9、视频 ≤3、总文件 ≤12 等——以当前文档页为准，本文件不保证数字最新）。

**SKIP 说明：** dexhunter 后半运镜表、电商/短剧长示例、延长全文 —— 与 `运镜/*`、`技巧锦囊/35`、官方重复，不入库。

## 6. beshuaxian · 打斗开场 2 秒钩子（薄摘录）

> 巧在哪（非原文）：库内孔明侧重「发力链」、爆老师侧重「一镜到底临场感」；本条只补**开场两秒要让观众读到的三件事**：谁打谁+距离、兵器或流派、能量节奏。不收录其 15 种风格完整提示词。

```yaml
# 条目元数据（策展者添加，非原文）
id: "jiqiao--45-seedance-agent-skill-synthesis--03"
标题: "打斗开场 2 秒钩子：对手距离 / 兵器流派 / 能量节奏（社区摘录）"
原标题: "打斗场景的2秒钩子框架"
分类: "技巧锦囊"
标签: ["技巧锦囊", "Seedance", "社区说法", "打斗", "时间码分段"]
适用模型: "Seedance 2.0（社区 Higgsfield 向 skill；时间码在 Seedance 2.0 上不稳定，见备注）"
语言: "zh"
来源链接: "https://github.com/beshuaxian/higgsfield-seedance2-jineng/blob/83dcb10ee38c9694ac0f455ec55a62f2be3b8a14/skills/05-fight-scenes/zh-CN/SKILL.md"
镜像: "shallow clone /workspace/_curate-seedance/higgsfield-seedance2-jineng @ 83dcb10e"
作者: "@beshuaxian（社区 skill）"
发布日期: "2026-10-01"
热度: "未知（来源无公开互动数据）"
许可: "未在摘录段声明；以源仓为准；learning-archive"
原文类型: "文本（community skill 短摘录）"
核对状态: "verified"
核对说明: "2026-10-01 对照 05-fight-scenes/zh-CN/SKILL.md「打斗场景的2秒钩子框架」框架块与三条约定句逐字摘录。"
完整性: "片段：仅框架与三条约定；省略其后战斗类型大表与完整提示词模板"
备注: "Seedance 2.0 官方：精确 0–3 秒时间戳不稳定，应用「镜头1」叙述同样的开场信息，或改用 2.5。发力链仍以 `打斗运镜/32` 为准。禁止把源仓 15 风格全文拷进本库。"
技巧钩子: "打斗前两秒先让人看清：谁对谁、多远、什么兵器/流派、是轻快还是沉重"
触发场景: "武戏开头混乱，观众分不清对手和兵器，后半段发力链写得再细也救不回来时"
```

```text
打斗的力量来自即时的视觉和物理承诺。前两秒应该表达：

1. **对手身份与距离**——我在看谁打谁？
2. **武器或武术风格**——这是什么类型的战斗？
3. **能量和节奏**——打斗是快速和敏捷还是力量和重量感？

### 框架

[0–0.5秒]: [对手建立] + [距离/武器] + [光照强度]
[0.5–1秒]: [初始动作/转向] + [速度提示]
[1–2秒]: [冲击或动作转向] + [音频/视觉反应]
```

**Seedance 2.0 改写示意（策展者，非原文，不计数）：**

```
镜头1：两人中景对峙，间距约两臂，双方持刀低位；硬侧光；男子先垫步刺出，刀尖带短促残影。
```

**SKIP：** `01-cinematic` 完整模板、`11-social-hook` 百科、`05` 其余风格 dump。

## 7. 给 agent 的薄路由（非原文）

写 Seedance 提示词时按这个顺序读库，**不要**去克隆 skill 仓当提示词库：

1. 裁定与官方要点 → `docs/最佳实践.md`、`docs/权威来源.md` §2.1  
2. 冷门官方技巧 → `prompts/技巧锦囊/35-volcengine-seedance2-guide-tricks.md`  
3. 结构示例 → `prompts/提示词写法/32`、`33`；首尾帧 → `prompts/首尾帧生图/03-*`  
4. 打斗 → `prompts/打斗运镜/32–34` + 本文件 §6；运镜词 → `prompts/运镜/*`  
5. 社区结构补丁 → **本文件** §2–5  
6. Agent 入口 → `skills/seedance-library-router/SKILL.md`（只指路，不复制正文）

## 总结（非原文）

- 条目数：3（`text` 围栏社区短摘录）；方法节不计数。
- 语言：en 2 · zh 1。
- 适用模型：Seedance 2.0（社区包装标注）3。
- 核对状态：verified 3。
- 本轮明确跳过：Emily 全仓、dexhunter 运镜/延长/电商长文、beshuaxian 风格批发与 social-hook、Higgsfield API skill。
- 净增值：导演载体编译、参考 ignore 契约、保真度预算与 lock line、@ 用途分层对照、打斗 2 秒开场钩子——且均标为社区说法，官方冲突时以官方为准。
