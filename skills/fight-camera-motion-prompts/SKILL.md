---
name: Fight / Action Video Camera Motion Prompts
description: Use when writing Seedance/Kling/PixVerse-style fight or action video prompts that need character lock, scene lock, action physics, camera path, VFX rules, and timed storyboard beats.
---

# Fight / Action Video Camera Motion (打斗运镜)

> **2026-09-30 整合说明（非原文）：** 本 skill 中「Source grounding」里的 `raw/…` 路径和「§」编号指早期 raw 草稿，库内对应文件为 `prompts/打斗运镜/01-lansenai-x.md`、`prompts/打斗运镜/02-web-fight-camera-prompts.md`、`prompts/打斗运镜/20-web-fight-camera-prompts.md`（整合后章节号可能不同）。术语口径以 `docs/术语速查.md` 为准，写法冲突的裁定见 `docs/最佳实践.md`。
>
> - 本 skill 示例里的 `[0–3s]` 式时间码适合 Seedance 2.5；Seedance 2.0 官方说明精确时间支持不稳定，应改用「镜头1/镜头2」。高强度武戏按官方建议分段生成再拼接，单段 1–2 个招式、单一运镜（见 `docs/最佳实践.md` 第 3 节）。

## When to use

- User wants a **fight / chase / duel / martial-arts** video prompt (Seedance-class, Kling, PixVerse, Runway, Veo, etc.).
- Need reusable structure: identity lock + scene lock + action rules + camera rules + VFX bans + timed beats — not a one-off character dump.
- Inputs needed: genre/tone, duration + aspect, cast count (usually 2), identity anchors (or first-frame refs), location, combat style (unarmed / weapons), camera flavor, VFX palette, hard bans.

**Source grounding (do not paste full 30s dumps into replies):** distill from `raw/01-lansenai-x.md` (X captions / self-replies) and `raw/02-web-fight-camera-prompts.md` (§1 twiscan mirror, §2 anime clips, §3 Seedance formulas, §4 运镜库). Point to those raw files for full 30s text.

## Canonical prompt skeleton

```text
【全局设定】
{{duration}}，{{aspect}}，{{fps_or_quality}}，{{style_medium}}。
战斗核心：{{combat_loop}}（例：爆发贴近→高密度攻防→重击迫退→立即追击→新落点再交锋）。
时间流速：{{time_flow}}。首帧已交锋/已蓄力。
末帧二选一：{{end_state}} = mid-motion（硬派连打，不摆pose） | stable-ready（舞台化有序对决，回预备姿态）。

【角色锁定】
模式：{{cast_mode}} = duo | solo+dummy_opponent | solo_skill_showcase。
若有参考图：严格使用参考图人物作为视觉基准 / 唯一主角（禁止换脸换装、肌肉化、无故盔甲化）。
角色A（首帧{{A_side}}）：{{A_identity_anchor}}。流派/主招：{{A_moveset}}。气质：{{A_vibe}}。
角色B（首帧{{B_side}}，若 duo）：{{B_identity_anchor}}。流派/主招：{{B_moveset}}。气质：{{B_vibe}}。
可选反差规则：{{contrast_rule}}（例：本人动作轻/静/克制，但极小动作引发超尺度能量反应）。
换位后仍按 A/B 身份区分；脸/发型/衣服色/布料层次/体型/年龄全程稳定。
禁止第三人（除非指定路人虚化）、分身、换脸换装、额外手脚。

【场景锁定】
严格继承首帧/参考：{{location}}。地面/纵深/空气介质：{{env_detail}}。光线：{{lighting}}。
环境破坏可累积且不可自动恢复：{{destructibles}}（受力→变形→开裂→爆碎→飞散→坠落）。

【动作规则】
风格：{{action_style}}（硬派近身 / 慢蓄力天灾级 / 格斗游戏连段 / 空战剑斗 / 舞台化有序攻防…）。
可选连段骨架（格斗游戏向）：轻试探 → 近身压制 → 连续技 → 浮空追击 → 霸体对拼 → 能量爆发 → 超必杀/终局。
必须可见：支撑脚、髋肩旋转、重心转换、回收与惯性、受击压缩、卸力再反打、借地形反作用力；命中反馈（身体震动、衣物摆动、碎石/裂纹）。
身法边界：{{movement_bounds}}（短距爆冲/踩墙反冲 OK；无原因闪现/乱飞禁止；残影若用则写“运动切片”而非分身）。

【镜头规则】
摄影：{{camera_rig}}（例：24mm 超广角 FPV + 受控手持；或单一慢侧跟；或低机位急推+拉远）。
原则：{{camera_principles}}
- 贴攻击轴线时快速后撤；贴身短打小半径半环绕；低扫腿降至脚踝高度
- 接触瞬间先看清接触点再震镜/推开；只能穿过真实空隙，不穿模
- 单一主路径优先；避免无故滚转、持续匀速侧跟冒充位移
- 可选：Time Ramp（加速↔短促降速）、冲击帧/抽帧/短促过曝/黑白闪击 — 仅绑最强碰撞，不可滥用
- 技能展示向：避免长期正面摆拍；多用侧后/贴地/FPV/Whip Pan/Orbit

【特效规则】
特效只跟真实打击点/刀路：{{vfx_allowed}}
（无色冲击波/马赫环/尘土 或 随刀锋展开的刀气扇面/月牙/楔形；刀气不自动追踪、不变远程大招）。
禁止：{{vfx_banned}}（彩色内力、魔法球、廉价粒子、固定悬浮环、游戏UI…）。
震镜仅在接触之后；轻交击不震镜。

【分镜】
按 {{beat_size}} 写（例：每 3s 一组，组内 t=Ns）：
镜头N（t0—t1）｜{{beat_title}}
t={{sec}} 运镜：{{cam_move}}。景别：{{shot_size}}。
A：{{A_action}}；B：{{B_reaction}}；接触反应：{{impact}}；环境：{{env_change}}。
…（覆盖满 {{duration}}；首尾连贯）

【音效】（可选）
{{sfx}}

【负面 / 硬禁】
{{hard_negatives}}
```

Shorter Seedance-style one-liner variant (from §3 formula):

```text
[角色锚点] + [地点与初始间距] + [有序动作编排] + [分时节拍] + [单一镜头路径] + [物理反应] + [音效]
```

## Must-have modules

| Module | What to lock |
|--------|----------------|
| 角色锁定 | Face, hair, outfit colors/layers, body ratio, age; A/B IDs after swap; no third person |
| 场景锁定 | Inherit first frame; destructible stack that never resets |
| 动作规则 | Weight, hip/shoulder, recovery, causal hits; no pose-spam / idle stare |
| 镜头规则 | One primary path; contact-first then shake; FPV/handheld bounds; no clipping through geometry |
| 特效规则 | Colorless physics / blade-bound FX only; impact-timed |
| 分镜 | Timed beats covering full duration; start mid-action, end mid-motion |

## Hard negatives / bans (distilled)

From §1.1 负面提示词 + §1.3/1.4 + §3.4:

- No slow-mo / freeze / pose-holding / waiting / one-move-then-stop (unless user explicitly wants “慢节奏蓄力” style — then only brief stretch on heavy hits).
- No fast-forward mush; punches must stay readable; no weightless flailing or flips without hit causality.
- No third person, clones, face/outfit/hair drift, extra limbs, clipping.
- No rainbow Qi, spell beams, fireballs, arrays, game UI, cheap particles, floating shock rings that ignore contact.
- No full-white dust wipe that hides action; no auto-healing environment.
- No gore/limb loss unless user asks; prefer sweat/dust/light abrasion.
- No dialogue/captions/watermarks unless requested (KO/HIT stingers only if user explicitly wants fighting-game HUD).
- Staged/non-graphic variants: no blood, preserve left-right positions and layout.

## Fill-in checklist

- [ ] Duration, aspect, fps/quality, style medium
- [ ] Cast mode + A/B (or solo) identity anchors + movesets + first-frame / ref-image lock
- [ ] Optional contrast_rule or fighting-game combo skeleton
- [ ] Location + lighting + cumulative destruction list
- [ ] Action style + movement bounds
- [ ] Camera rig + principles (single path preferred)
- [ ] Allowed vs banned VFX
- [ ] Full timed storyboard covering 0→end
- [ ] Hard negatives block
- [ ] Optional SFX

## Short examples (trimmed; not full 30s)

**Example A — hard-contact courtyard opener (structure from §1.1; truncated)**  
Fill: 30s / 16:9 / 硬派近身武侠；A 光头僧袍重踢，B 发髻粗布短拳；石质院落青灰石板；24mm FPV；无色冲击波/马赫环；t=1s 中线对撞土浪…  
→ Point to raw `02` §1.1 / `01` aerial-sword & courtyard-class posts for complete dumps.

**Example B — Seedance 15s rooftop staged (from §3.2/3.4)**  
```text
蓝调时刻 15 秒屋顶武术交锋。A 锈色夹克 / B 炭灰训练外套，起始间距三米。
[0–3s] 预备，平视全景静止；[3–7s] A 右直拳，B 外闪，慢侧跟；
[7–11s] B 左侧踢，A 小臂格挡滑过积水；[11–15s] 分开回预备，镜头定住。
音效：雨、鞋、布料、呼吸、一次闷响。禁止第三人、跳切、换装、血腥。
```
