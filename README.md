# AI Video Library · AI 视频提示词与镜头语言知识库

> **不是 Prompt 堆积站，而是经过筛选、核对、实战蒸馏的 AI 视频创作知识库。**
>
> Templates · Prompt Compiler · Cinematic Camera · Fight Choreography · VFX · Image-to-Video · Model Best Practices

面向 AI 视频创作者、导演型工作流和 AI Agent：把零散的提示词案例整理成**可复制模板、可组合能力、可追溯原文和可执行规则**。重点覆盖高速打斗、电影运镜、粒子/VFX、国风武侠、图生视频、角色一致性、产品/UGC 等常见生成任务。

**核心理念：先用，再查；先给可执行结果，再下钻原始资料。**

[开始使用](#30-秒入口) · [核心模板](TEMPLATES.md) · [Prompt Compiler](COMPILER.md) · [能力地图](CAPABILITIES.md) · [精选母版](CORE-PICKS.md) · [参与贡献](CONTRIBUTING.md)

### 为什么值得收藏

- **精选而不是堆量**：完整 Prompt、reference、成片 cases 分层管理，低价值重复内容持续清理。
- **能直接生成**：从一句需求出发，用模板 + 能力 + Compiler 组合成新的可执行 Prompt，而不是只复制旧案例换皮。
- **专门研究“怎么拍”**：动作因果、接触受力、镜头路径、环境反馈、粒子触发和节奏都拆成可复用规则。
- **保留证据链**：第三方原文与蒸馏结论分层；原文不因方法论更新被静默改写。
- **持续实测迭代**：模板会根据真实生成结果修正，例如高速武戏已区分“重击可读”和“短时高频交击”两种节奏模式。

> 如果这个库帮你少走了一次弯路，欢迎 **Star**。如果你有跑得特别好的 Prompt、成片对照或模型实测，欢迎提交 Issue / PR，一起把“玄学经验”变成可复用的方法。

---

## 30 秒入口

| 你现在要做什么 | 直接打开 |
|---|---|
| **复制一个模板马上写** | [TEMPLATES.md](TEMPLATES.md) |
| **学最重要的规则/词汇/冲突裁定** | [PLAYBOOK.md](PLAYBOOK.md) |
| **让 AI 按本库方式回答你** | [ASSISTANT.md](ASSISTANT.md) |
| **把一句需求编译成 Prompt** | [COMPILER.md](COMPILER.md) |
| **按需求组合能力** | [CAPABILITIES.md](CAPABILITIES.md) |
| **先看最有代表性的案例** | [CORE-PICKS.md](CORE-PICKS.md) |
| 找完整原始提示词 | [INDEX.md](INDEX.md) |
| 查术语 | [docs/术语速查.md](docs/术语速查.md) |
| 查模型差异与最佳实践 | [docs/最佳实践.md](docs/最佳实践.md) |
| 看提示词 + 成片对照 | [cases/](cases/) |

### 最短万能公式

```text
主体 → 动作 → 场景 → 景别 → 单一主运镜 → 光影 → 环境反馈 → 约束
```

### 打斗最短公式

```text
发力 → 接触 → 受力 → 镜头反应 → 环境反馈
```

不要用“很帅 / 很燃 / 很快 / 电影感 / 8K”代替上面这些可执行信息；这些词最多放最后做风格修饰。

---

## 顶层蒸馏层

- **TEMPLATES.md**：通用视频、多镜头、打斗、水墨武戏、图生视频、光影、运镜、AI 扩写模板。
- **PLAYBOOK.md**：全库蒸馏后的 canonical 规则、高价值词汇、降权词、模型冲突裁定、四则水墨武戏 diff 结论。
- **ASSISTANT.md**：给 AI/Agent 的检索与回答规则，默认“先给能直接用的，再解释”，避免把整库资料重新倾倒给用户。
- **COMPILER.md**：Parse → Route → Select → Blueprint → Materialize → Adapt → Lint → Emit 的固定生成流水线。
- **CAPABILITIES.md**：把“更有力量 / 别站桩 / 更有高潮”等需求映射成可组合能力。
- **CORE-PICKS.md**：代表性方法入口；不是把 151 条再平铺一遍，而是先指向最值得拆解的母案例。

**蒸馏层可以修改和迭代；原文层不因方法论更新而篡改。**

---

## 原文证据层

本库采用 **核心 Prompt + reference + cases** 三层：核心 Prompt 用于直接生成/改写；reference 保存术语词典、官方微型示例和方法片段；cases 保存成片对照。低权威、低信息密度且被高质量来源覆盖的聚合转载不再保留。

| 路径 | 内容 |
|---|---|
| `prompts/<中文分类>/` | 核心 Prompt 与 reference 原始材料；`text` 围栏逐字保留 |
| `cases/<中文分类>/<样例>/` | 提示词 + 成片/来源对照 |
| `INDEX.md` | 给人看的索引 |
| `index.jsonl` | 给 AI / 程序检索的完整索引 |
| `skills/` | 专项工作流 |
| `docs/` | 术语、官方依据、最佳实践、策展记录 |
| `scripts/build_index.py` | 重新生成索引与统计 |

分类与条目数见 [prompts/README.md](prompts/README.md)。

### 原文保护规则

- `text` 围栏里的原文不润色、不翻译、不为了“统一风格”改写。
- 完全重复原文只保留一个副本，其余用索引/链接指向。
- 术语词典、单句官方示例、方法片段进入 reference，不与完整 Prompt 混排计数。
- 第三方聚合转载若同时满足“低权威 + 信息密度低 + 被官方/作者原文覆盖”，可删除而不是永久归档。
- 同一知识点可以存在于多个案例，但**蒸馏结论只在 PLAYBOOK 保留一次**。
- 原文与当前模型官方指南冲突时：原文保留，蒸馏层注明适用条件和裁定。

---

## 四则水墨武戏

2026-10-02 提交的“河滩 / 悬崖古刹骨伞 / 铜币转场 / 竹林打斗”已经收录在：

`prompts/打斗运镜/37-levi-qiao-ink-wuxia-fights.md`

四条原文保留；共同规则不再复制成第五条原文。蒸馏后的可复用部分已经进入 [TEMPLATES.md](TEMPLATES.md) 的“水墨武戏风格插件”和 [PLAYBOOK.md](PLAYBOOK.md)。

---

## 维护

修改或新增原文条目后运行：

```bash
python3 scripts/build_index.py
python3 scripts/build_index.py --check
```

只修改顶层蒸馏文件时不需要重建原文索引。

## 参与开源

欢迎贡献高质量 Prompt、Prompt + 成片对照、模型实测、错误修正和可复用方法。提交前请先看 [CONTRIBUTING.md](CONTRIBUTING.md)。

我们更看重**可验证的新信息**，而不是数量：一个能解释“为什么这样写更稳定”的实测案例，比几十条换皮 Prompt 更有价值。

## License

MIT（仓库结构与自写文档）。第三方提示词 / 图片 / 视频版权归原作者，仅作学习归档；各条目的许可见元数据“许可”字段。
