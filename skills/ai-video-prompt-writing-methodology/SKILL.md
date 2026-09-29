---
name: AI Video / Image Prompt Writing Methodology
description: Use when the user asks how to write AI video or image prompts (提示词编写思路), needs a reusable formula (主体/动作/运镜/光影/约束), or wants a meta-recipe to expand a one-line idea into Seedance/Jimeng/Kling-ready structured prompts — not a finished scene dump.
---

# AI Video / Image Prompt Writing Methodology（提示词编写思路）

## When to use

- User asks **怎么写提示词 / 提示词编写思路 / prompt formula / 分镜怎么写**.
- Need a **methodology skill** (recipe + checklist), not a one-off fight/VFX/character dump.
- Targets: Seedance / 即梦, Kling, Runway, Veo, generic T2V/I2V; also still-image prompts when structured the same way (drop motion/audio layers).
- Inputs needed: one-line idea, optional refs (@Image/@Video/@Audio), duration + aspect, model generation (2.0 序号镜头 vs 2.5 秒级时间戳), genre.

**Source grounding (Douyin body NOT recovered):**
- Douyin target `https://v.douyin.com/mM3gTkJWuzQ/` (cue: AI绘梦菌「AI提示词编写思路」) → **0 body** — see `docs/douyin-blockers/douyin-mM3gTkJWuzQ-AI绘梦菌.md` (copy: `raw/douyin-mM3gTkJWuzQ-blocker.md`).
- Distilled from public guides only; cite, do not invent Douyin slides/voiceover:
  - https://xiangyugongzuoliu.com/seedance-video-prompt-guide/ (八层框架)
  - https://aistacknav.com/ai-video-prompt-tips-camera-scene-action/ (万能公式 + 模板)
  - https://raw.githubusercontent.com/cclank/lanshu-awesome-ai-video-kit/main/methodology/02-进阶公式.md (8 要素)
  - https://suno.bi/zh/blog/seedance-2-5-prompt-guide (2.5 四段式 + 时间戳分歧)
- Verbatim excerpts: `raw/05-web-prompt-writing-methodology.md` and `prompts/提示词写法/`.

## Recipe (canonical)

### 1) Pick structure by model era

| Model | Shot segmentation | Notes |
|-------|-------------------|--------|
| Seedance / 即梦 **2.0** | `镜头 1` / `镜头 2` … (2–4 shots) | Official: precise `0–3s` often unstable |
| Seedance **2.5** | `0s-3s：` / `3s-8s：` OR `镜头 N` | Timestamps are first-class |
| Generic / unknown | Prefer `镜头 N` + duration at end | Safer default |

### 2) Fill layers in this order (left-to-right attention)

```text
【可选·素材角色】@Image/@Video/@Audio → 各锁什么（身份 / 运镜 / 节奏）
【概述】一句话：谁 + 在哪 + 发生什么 + 题材风格
【逐镜】镜头N 或 时间戳：
  景别+主体(2–3个稳定静态特征)
  → 动作(部位+幅度+速度；情绪外化，禁抽象「悲伤」)
  → 运镜(每镜只写一个；中文+英文括注；与主体动作分开)
  → 场景+光影(环境 + 光源方向/色温 + 氛围)
  → 音效：(对话/SFX/环境音)
【收尾·全局一次】风格锚点 + 正面约束 + 画质/比例/时长
```

Shorter 5-stack (quick test / no refs):

```text
主体 → 动作 → 运镜 → 风格 → 约束
```

8-element engineering form (kit):

```text
精准主体 + 动作细节 + 场景环境 + 光影色调 + 镜头运镜 + 视觉风格 + 画质 + 约束条件
```

Universal one-liner form (AI Stack Nav):

```text
主体 + 场景 + 动作过程 + 镜头景别 + 运镜方式 + 光线氛围 + 画面风格 + 时长/比例 + 负面或正面约束
```

### 3) Must-have writing rules

1. **Concrete > pretty:** 「穿红色亚麻裙、松散低马尾」not「漂亮女孩」; 「主光从左上方、暖补光、黄金时段逆光尘埃」not「美丽电影光」。
2. **Action chain:** start pose → process → end state; add speed/amplitude; prefer slow continuous motions for stability; externalize emotion via body.
3. **One camera move per shot:** dolly / pan / tracking / orbit / handheld / fixed / crane / push in / rack focus — never stack conflicting moves.
4. **Separate camera from subject action:** wrong「镜头环绕旋转，跳舞的女人」; right「女人缓慢舞蹈，双臂抬起。镜头以稳定弧线环绕（orbit）。」
5. **Refs:** always say *what* to take from which file (`将图片1中…定义为主体1`); do not rely on text baked into the image.
6. **Constraints:** prefer positive locks for Jimeng (`保持面部一致，无变形…`); add explicit negatives where the model supports them (脸部变形、多指、背景跳变、水印字幕…).
7. **Length bands (community):** single-shot ~60–100 words; multi-shot ~200–300 words; front-load subject+action.
8. **Color recipe (optional but high ROI):** 主色调基底 + 次色调主体层 + 点缀色高光.

### 4) Emotion externalization cheat sheet (cite Source A)

| Abstract | Write instead |
|----------|----------------|
| 悲伤 | 低头，肩微颤，眼眶泛红，手指攥衣角 |
| 喜悦 | 嘴角上扬，眉眼舒展，脚步轻快 |
| 紧张 | 看表，敲桌，呼吸急促，目光闪躲 |
| 愤怒 | 双拳紧握，下颚绷紧，胸膛起伏 |
| 释然 | 长呼气，双肩放松，淡淡微笑 |

### 5) Meta-prompt (ask LLM to expand user idea)

Paste into Claude/GPT/DeepSeek, then give one sentence:

```text
你是 AI 视频提示词工程师。把用户一句话扩成可直接粘贴的中文分镜提示词。
规则：按「素材指代(若有)→镜头标签→景别主体→动作→运镜→场景光影→音效→全局风格与约束」顺序；
每镜只一个运镜；情绪必须身体外化；禁止空洞形容词；末尾正面约束+比例时长。
只输出提示词正文，无前言后语。默认 16:9、8–15 秒、电影写实。
```

## Output checklist

- [ ] Subject has 2–3 stable visual anchors
- [ ] Action has body part + speed + chain
- [ ] Exactly one camera move per shot; separated from action
- [ ] Lighting has direction + quality (not just「电影感」)
- [ ] Style not conflicting (pick one primary)
- [ ] Constraints / bans present
- [ ] Duration + aspect stated
- [ ] Segmentation matches model (镜头N vs timestamps)
- [ ] If refs: each @file has an explicit role

## Do not

- Invent Douyin / AI绘梦菌 post text — body unrecovered.
- Dump unrelated fight/VFX long-forms when user only asked for writing methodology (point to those skills instead).
- Stack 「写实+动漫+赛博+复古」in one prompt.
- Use bare「fast/快速」as the only motion cue on fragile models — describe physical detail instead.
