# 技巧锦囊 · Higgsfield Hell Grind 综合摘录（CINEDANCE 空间锁 + ACTING 表演层 + LIRA 生图 4-D 指针）

## 来源概述（非原文）

> body: mixed — 下文「社区原文摘录」`text` 围栏为 Hell Grind Brief 公开 skill 文件的短摘录（逐字）；其余表格、对照、策展备注为策展者编写，**非原文**。本文件**不是** skill 仓镜像，只收与库内官方条目及 `技巧锦囊/45` **不重叠**、且可核对的结构 / 纪律。

- **源（SECONDARY 社区 / 项目 Brief，非火山官方裁定）：**
  - Higgsfield Studio 《Hell Grind》Brief：https://higgsfield.ai/@higgsfield.studio/projects/hell-grind （公开 CINEDANCE / ACTING / LIRA 技能文件）
  - 开源镜像 [XucroYuri/higgsfield-hell-grind-opensource](https://github.com/XucroYuri/higgsfield-hell-grind-opensource) `skills/` — blob SHA（2026-10-01 与本地工作副本一致）：
    - `CINEDANCE HIGGSFIELD SKILL.md` @ `24d38044ae06e5159cf5662b2bf5e09164789894`
    - `ACTING SKILL.md` @ `383db473e88e70a2e3ed30f962e4ea56da5a645b`
    - `LIRA SKILL.md` @ `1e5c80731d5f6ccd0d2e803678598da42ce835e7`
  - 策展工作副本（不入库）：`/workspace/_hell-grind-skills/`
- **收录：** 2026-10-01（Asia/Shanghai）
- **许可：** Hell Grind Brief / 镜像仓自有声明；本库只摘录短片段用于学习归档，并标明社区说法
- **权威层级（强制）：** 火山引擎 / Seedance 官方文档（见 `docs/权威来源.md` §2.1、`技巧锦囊/35`、`首尾帧生图/03`）> `技巧锦囊/45` 社区结构 > **本文件** Hell Grind 社区纪律。与官方矛盾时以官方为准。
- **与本库已有内容的关系（去重）：**
  - **不重复：** 轨道补齐 / 双胞胎 / 发力链（`技巧锦囊/35`、`打斗运镜/32`）；Emily 载体编译、参考 ignore、保真度预算、打斗 2 秒钩子（`技巧锦囊/45`）；正面优先否定（`最佳实践` §5.2 已有通用条，本文件不另立「正面 > 否定」为新规则，仅在 LIRA 节注明其**生图**语境）。
  - **本文件只补：** ① 可度量空间锁（米级距离、地标接触）；② 首帧即占位 / 开场一秒读清房间关系；③ 机位侧（camera side）显式；④ ACTING：压力下行为、master profile 150–220 词、eye life 强制、按场改写勿粘贴、states-not-transitions；⑤ LIRA：4-D **仅用于 IMAGE 提示词**的指针（不 dump 人物卡/首尾帧已有矩阵）。
- 本文件计数条目：3 个 `text` 围栏（社区短摘录）；其余为方法说明，不计数。核对状态：verified 3（对照上述 blob SHA 文件）。

## 1. 社区包装 vs 官方：怎么用本文件

| 层级 | 用什么 | 本库路径 |
|------|--------|----------|
| 官方（优先） | 素材上限、首尾帧 role、双胞胎、轨道补齐、镜头序号 vs 时间戳、否定词范围 | `docs/权威来源.md` §2.1；`技巧锦囊/35`；`docs/最佳实践.md`；`首尾帧生图/03` |
| 社区结构（可试，先于本文件） | 导演载体、参考 ignore、保真度预算、@ 用途、打斗 2 秒钩子 | `技巧锦囊/45` |
| Hell Grind 补丁（可试） | 米级空间锁、首帧占位、camera side、表演 master/eye life/改写、states-not-transitions；LIRA 生图 4-D 指针 | **本文件**；汇总进 `docs/最佳实践.md` 的对应 bullet |
| 跳过 | CINEDANCE 全文 ~1330 行、Hell Grind 成片资产包/剧情、LIRA 全量模型矩阵与模板批发、与 `45` 重复的载体/ignore/2s 钩子 | 见策展计划 SKIP |

> 策展备注（非原文）：CINEDANCE / ACTING / LIRA 是 Hell Grind 项目把影视与表演方法打包成 agent skill 的**社区 / 工作室**材料，**不是**火山引擎官方 API。Seedance 2.0 上精确 `0:03` 时间码仍不稳定——空间锁用「镜头1」叙述同样信息即可（见 `最佳实践` §4）。

## 2. CINEDANCE · 首帧占位 + 可度量空间锁（社区）

> 巧在哪（非原文）：开场不要空建立镜；角色与地标的距离用「within 1 meter / hand on …」等可核验物理语，替代 near/around。机位侧（camera side）与 screen-left/right 一并写清，避免左右翻。

**与官方关系（非原文）：** 官方要求写清主体、站位与动作（SD2.0）；本条是社区场记级空间纪律，不替代官方时长/素材上限。多镜连续性仍优先官方「镜头序号」与 `45` lock line。

```yaml
# 条目元数据（策展者添加，非原文）
id: "jiqiao--46-hell-grind-cinedance-acting-lira-synthesis--01"
标题: "CINEDANCE：首帧占位 + 米级空间锁（社区摘录）"
原标题: "First-frame occupancy lock / Spatial blocking lock"
分类: "技巧锦囊"
标签: ["技巧锦囊", "Seedance", "社区说法", "分镜/多镜头", "空间锁"]
适用模型: "Seedance 2.0 / Higgsfield Seedance（Hell Grind CINEDANCE V4 社区包装；非火山官方术语）"
语言: "en"
来源链接: "https://github.com/XucroYuri/higgsfield-hell-grind-opensource/blob/master/skills/CINEDANCE%20HIGGSFIELD%20SKILL.md"
镜像: "blob 24d38044ae06e5159cf5662b2bf5e09164789894；工作副本 /workspace/_hell-grind-skills/CINEDANCE HIGGSFIELD SKILL.md；Brief https://higgsfield.ai/@higgsfield.studio/projects/hell-grind"
作者: "Higgsfield Studio / Hell Grind CINEDANCE（社区 skill）"
发布日期: "2026-10-01"
热度: "未知（来源无公开互动数据）"
许可: "Hell Grind Brief / 镜像仓声明为准；learning-archive"
原文类型: "文本（community skill 短摘录）"
核对状态: "verified"
核对说明: "2026-10-01 对照 CINEDANCE 文件「First-frame occupancy lock」示例块与「Spatial blocking lock」弱词→强词表及示例句逐字摘录；blob SHA 与本地 git hash-object 一致。"
完整性: "片段：省略 Location map / Optics / Physics 全文与镜头 FOV 词表；要点见下方策展备注"
备注: "社区包装。camera side 另见本文件 §3 方法节。禁止把 CINEDANCE 全文拷进 prompts/。"
技巧钩子: "开场第一帧就要站好位；距离写到米和接触点，并锁住机位在哪一侧"
触发场景: "角色飘在空地、开场空镜、左右翻面、或「near the car」写了却贴不上地标时"
```

```text
The first visible frame already contains all required characters in their correct positions.
No empty establishing frame.
No delayed character reveal.
No opening frame without the required subjects.
The spatial relationship is readable immediately in frame one.

@HERO1V2 stands within 1 meter of the burned-out car, one hand resting on the scorched hood.
@HERO2 and @HERO3 stand together in the foreground, facing @HERO1V2.
Hero2 is camera-right of the pair.
Hero3 is camera-left of the pair.
Both bodies face Hero1.
Both gaze lines are locked on Hero1.
Hero1 faces them from the car.

Never rely on weak words when spatial accuracy matters:

- near
- around
- beside
- somewhere
- in the area
- nearby

Replace them with:

- within 1 meter
- touching
- boots inside the root circle
- hand on the handle
- standing directly under the sign
- back against the wall
- in front of the rear passenger door
- at the south kerb edge
```

## 3. CINEDANCE · camera side 与正向锁（方法不计数）

> 巧在哪（非原文）：机位不止写高度/距离，还要写**站在光源/主体的哪一侧**（camera side / operator on shadow side），与 `45` 的 lock line「机位侧」同族但 CINEDANCE 把它提升为构图必填项。

**社区要点（非原文转述）：** Camera and composition 清单含 `camera side`；Prefer 例：`operator stands on shadow side`、`subject occupies screen-left third`。Silent QA 问「Is the camera side clear?」。正向控制优先于巨型 NEGATIVE 块——「desired state first」；库内通用「正面优先」已在 `最佳实践` §5.2，**此处不重复立规**。

**SKIP：** Optics FOV 词表（47°/84°…）、Physics 全文、Dialogue 规则 dump、Quality suffix 万能尾缀。

## 4. ACTING · 压力下行为 + master / eye life / 改写 / 状态非过程（社区）

> 巧在哪（非原文）：表演层写「在压力下追求目标的行为」，不写情绪标签；常驻角色一份 150–220 词 master profile，每场**改写进当下**而非粘贴；eye life 强制；动作写成已在状态中（mid-throw），少写「伸手→取出→蓄力」过程链。

**与 `45` / 官方去重（非原文）：** Emily「叙事→载体」处理的是权力/潜台词编译；本条专攻**可见表演纪律**（眼、blink、改写）。情绪外化官方表见 SD2.0 / `最佳实践` §2.5——不替代。

```yaml
# 条目元数据（策展者添加，非原文）
id: "jiqiao--46-hell-grind-cinedance-acting-lira-synthesis--02"
标题: "ACTING：压力下行为 + eye life + states-not-transitions（社区摘录）"
原标题: "Behavior under pressure / Eye life / States, not transitions"
分类: "技巧锦囊"
标签: ["技巧锦囊", "Seedance", "社区说法", "表演", "人物一致性"]
适用模型: "Seedance 2.0（Hell Grind ACTING 社区包装；模型无关写法，仍以目标模型官方为准）"
语言: "en"
来源链接: "https://github.com/XucroYuri/higgsfield-hell-grind-opensource/blob/master/skills/ACTING%20SKILL.md"
镜像: "blob 383db473e88e70a2e3ed30f962e4ea56da5a645b；工作副本 /workspace/_hell-grind-skills/ACTING SKILL.md；Brief https://higgsfield.ai/@higgsfield.studio/projects/hell-grind"
作者: "Higgsfield Studio / Hell Grind ACTING（社区 skill）"
发布日期: "2026-10-01"
热度: "未知（来源无公开互动数据）"
许可: "Hell Grind Brief / 镜像仓声明为准；learning-archive"
原文类型: "文本（community skill 短摘录）"
核对状态: "verified"
核对说明: "2026-10-01 对照 ACTING 核心公理段、§7 Eye life 中 saccades/catchlights/eyes-lead 三条、§10 States not transitions 整段逐字摘录（§7 其余 blink/stillness/beat 条见源文件）；blob SHA 与本地一致。"
完整性: "片段：省略五柱详细表、坏演技 Atlas、完整 worked example；master profile 字数与改写规则见下方策展转述"
备注: "社区包装。master profile 目标 150–220 词、一场一改写（rewrite never paste）见源 §6–§8，本围栏未全文收录模板。禁止粘贴 ACTING 全文进 prompts/。"
技巧钩子: "表演写压力下的行为与眼神生命，动作写「已在状态中」，每场改写档案勿整段粘贴"
触发场景: "AI 演技像在「演情绪」、眼神死、或过程动词链导致动作塌缩时"
```

```text
**The core axiom of this entire system: acting is BEHAVIOR under pressure,
not a display of emotion.** A character wants something, something is in the
way, and they act to get it. Emotion is a byproduct of that struggle — never
the thing you write directly. Everything below unpacks this rule.

Dead eyes are the number-one tell of AI-generated acting. Give every
character continuous, naturalistic ocular life:

- **Micro-saccades and gaze targeting** on whoever or whatever they attend
  to; the gaze keeps moving — eyes drift, flick away in thought, scan to a
  detail and settle back. They never lock frozen on a single point.
- **Live catchlights** — the eyes must read as wet, lit and alive.
- **Eyes lead the thought.** The eyes reach the target a touch before the
  head turns. Thought is readable in the eyes before the words come.

Video generation models fail transitions and nail states. Describe
characters already IN the action state — mid-throw, mid-punch, mid-pace,
mid-argument — not the process of getting there ("reaches into the bag,
pulls out, winds up" collapses; "mid-throw, arm extended" lands). Chain
states beat by beat instead of narrating continuous processes.
```

**Master profile + 按场改写（策展者据 §6 / §8 转述，非原文，不计数）：**

- 每角色一份 master：约 **150–220 词**、一段英文流水散文，只写可拍摄行为（体态、声线习性、带触发条件的 tic、步态、However when X… 面具破裂）。
- 每场：**REWRITE** 进当下姿态/节拍；保留身份内核与 eye life；不能发生的 tic **转化出口**（transform, don't delete），勿整段粘贴 master。
- Voice 音频句锁定、不按场改（源 §9）——与即梦/方舟音频字段是否支持无关时，可只当写作纪律。

## 5. LIRA · 生图 4-D 指针（社区，方法不计数）

> 巧在哪（非原文）：LIRA 的 4-D（Deconstruct → Diagnose → Develop → Deliver）明确面向 **IMAGE** 提示词优化（Soul / NBP / Seedream 贴图 pass 等），**不要**把其模型路由矩阵当成 Seedance 视频官方公式。

**入库策略（非原文）：**

| 可取 | 不取 |
|------|------|
| 4-D 流程名与「先诊断失败模式再写 prompt」的纪律指针 | Higgsfield Soul / Cinema Studio / NBP / Seedream / GPT Image **全量**规则矩阵与模板 dump |
| 生图 GENERATION 用正面描述替代 NOT-stack（与 BFL/Runway-Img 官方同向；见 `权威来源` §2.6–2.7） | 与 `人物卡/*`、`首尾帧生图/*`、`docs/首尾帧工作流.md` 重复的角色表/首尾帧流程 |

```yaml
# 条目元数据（策展者添加，非原文）
id: "jiqiao--46-hell-grind-cinedance-acting-lira-synthesis--03"
标题: "LIRA：IMAGE 提示词 4-D 方法论指针（社区摘录）"
原标题: "The 4-D Methodology"
分类: "技巧锦囊"
标签: ["技巧锦囊", "社区说法", "生图", "提示词写法"]
适用模型: "Higgsfield Soul / NBP 等 IMAGE 工作流（Hell Grind LIRA；非 Seedance 视频官方）"
语言: "en"
来源链接: "https://github.com/XucroYuri/higgsfield-hell-grind-opensource/blob/master/skills/LIRA%20SKILL.md"
镜像: "blob 1e5c80731d5f6ccd0d2e803678598da42ce835e7；工作副本 /workspace/_hell-grind-skills/LIRA SKILL.md；Brief https://higgsfield.ai/@higgsfield.studio/projects/hell-grind"
作者: "Higgsfield Studio / Hell Grind LIRA（社区 skill）"
发布日期: "2026-10-01"
热度: "未知（来源无公开互动数据）"
许可: "Hell Grind Brief / 镜像仓声明为准；learning-archive"
原文类型: "文本（community skill 短摘录）"
核对状态: "verified"
核对说明: "2026-10-01 对照 LIRA SKILL.md 第 28–75 行「The 4-D Methodology」整节逐字摘录（含 Develop 任务类型指针）；其下 Model routing / Full Reference / Templates 全文 SKIP。"
完整性: "片段：仅 4-D Methodology 节；完整 model routing / templates 见源文件，本库不入库"
备注: "仅 IMAGE。视频仍走 `技巧锦囊/35`+`45`+官方。人物一致性优先库内人物卡与官方大头照+全身照，不依赖 Soul ID 专有参数当通用规则。"
技巧钩子: "生图提示词先走拆解→诊断失败模式→再按任务选技法，而不是堆关键词"
触发场景: "写角色表/场景静帧/局部修图提示词，需要一条可检查的优化流程时"
```

```text
## The 4-D Methodology

Run every request through these four stages internally, then deliver.

1. **DECONSTRUCT** — break down
   - Identify the core intent, key subject(s), and context
   - Determine the target model (Soul 2.0 / Soul Cinema / NBP / Seedream 4.5 /
     GPT Image 2) and output constraints (aspect ratio, single image vs sheet,
     edit vs generation)
   - Map what is given vs what is missing

2. **DIAGNOSE** — diagnose
   - Find gaps in clarity and ambiguity (camera angle, light, palette, subject
     count, framing)
   - Check specificity and completeness
   - Assess whether the request risks a known failure mode (illustration
     drift, tattoo/text artifacts, multi-character collapse, bloated
     over-long prompts)

3. **DEVELOP** — develop
   - Pick techniques by request type:
     - Character → Soul 2.0: consistent identity anchors + Soul ID +
       3-panel sheet structure. Alternative: Cinema Studio AI Cast builds
       the reference sheet AUTOMATICALLY — standalone tool on Higgsfield,
       parameters set in its UI (no prompt needed); offer it when the goal
       is a reference sheet
     - Location/environment → Soul Cinema: camera anchor + light + palette +
       tech block
     - Prop → NBP / GPT Image 2 (realistic product context): product-shot
       framing + neutral backdrop + anti-text anchors
     - Edit of an existing frame → NBP FIRST, always, as post-processing
       of the original: minimal CHANGE block + exhaustive PRESERVE EXACTLY
     - Sloppy AI textures in a finished frame → Seedream 4.5 texture pass
       (skin, fabric, surfaces); NEVER point edits on Seedream
     - Finest local micro-edit NBP couldn't take → GPT Image 2, last
       resort (dirty globally, strong locally); same CHANGE / PRESERVE
       discipline. Never rebuild a frame with an edit — regenerate in a
       Soul model
     - Location view change (reverse angle etc.) → GPT Image 2 works well;
       on NBP spell out the NEW object arrangement explicitly (sofa was on
       the right in the main view → on the LEFT in the reverse view)
   - Assign the model a clear role (camera/lens, cinematographer mood)
   - Layer context and impose logical structure

4. **DELIVER** — deliver
   - Construct the optimized prompt
   - Format it to platform + complexity
   - Give brief application notes (what to watch, what to toggle)
```

> 策展备注（非原文）：Develop 子项含 Soul / NBP 等产品名——仅作 IMAGE 工作流指针，**不是** Seedance 视频官方公式；完整 Model routing / Templates **SKIP**。人物一致性仍以库内人物卡与火山「大头照+全身照」为准。

## 6. 给 agent 的薄路由（非原文）

写 Hell Grind / Seedance 电影向提示词时按这个顺序读库，**不要**把三份 skill 全文拷进 `prompts/`：

1. 裁定与官方要点 → `docs/最佳实践.md`、`docs/权威来源.md` §2.1  
2. 冷门官方技巧 → `prompts/技巧锦囊/35-volcengine-seedance2-guide-tricks.md`  
3. Seedance 社区结构补丁 → `prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md`  
4. Hell Grind 空间 / 表演 / 生图指针 → **本文件**  
5. 打斗 → `prompts/打斗运镜/32–34` + `45` §6；运镜词 → `prompts/运镜/*`  
6. Agent 入口 → `skills/hell-grind-library-router/SKILL.md`（只指路；完整 skill 若已装在 agent 侧，以安装副本为准，库内不镜像正文）

## 总结（非原文）

- 条目数：3（`text` 围栏社区短摘录）；方法节不计数。
- 语言：en 3。
- 适用模型：Seedance / Hell Grind 社区包装 2 + IMAGE（LIRA）1。
- 核对状态：verified 3。
- 本轮明确跳过：CINEDANCE 全文、Hell Grind 剧情/资产包、LIRA 模型矩阵与模板批发、与 `45`/`35`/`最佳实践` 已有规则的重复复述。
- 净增值：米级空间锁与首帧占位、camera side、ACTING 压力行为 / eye life / 改写 / states-not-transitions、LIRA 生图 4-D 指针——均标为社区说法，官方冲突时以官方为准。
