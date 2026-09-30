# 技巧锦囊 · OpenAI《Sora 2 Prompting Guide》里的冷门技巧：动作写成节拍、调色板锚点、编辑只改一处

## 来源概述（非原文）

> body: verbatim — 无语言代码块是官方指南对应小节的原文（去掉了页面上的对比视频与按钮文字，文字不改）；`text` 围栏是官方完整示例提示词。每节开头的「巧在哪」和「总结（非原文）」为策展者所写，**非原文**。

- **source URL:** https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide
- **publisher:** OpenAI Cookbook（署名 Robin Koenig、Joanne Shin）；页面标注「Updated - March 2026」
- **captured:** 2026-09-30（UTC+8），HTML 保存在 box `/workspace/prompt-extract/raw/jiqiao-sources/sora2.html`
- **license:** 未注明（来源未声明许可）；只摘录与技巧相关的小节
- **与本库已有内容的关系（去重）:** 本库此前没有收录这份指南（全库检索 sora2_prompting_guide、「four steps to the window」「Palette anchors」「cluttered workshop」均无结果）。`docs/最佳实践.md` 的「一个镜头只写一种主运镜」「先简单后复杂」与本指南方向一致，本文件不重复，只收三条不容易想到的做法和一个与 `技巧锦囊/44`（AI琪琪 混合媒介）呼应的官方完整示例。
- 本文件计数条目：1 个 `text` 围栏（Example 1）；核对状态：verified 1。

## 1. 动作写成「节拍 / 计数」

> 巧在哪（非原文）：不要写「走过房间」，要写「走四步到窗边、停一下、在最后一秒拉窗帘」——把动作拆成可数的小步和停顿，时间就落地了。

```
## Control motion and timing

Movement is often the hardest part to get right, so keep it simple. Each shot should have one clear camera move and one clear subject action. Actions work best when described in beats or counts – small steps, gestures, or pauses – so they feel grounded in time.

“Actor walks across the room” doesn’t give much to work with. A line like “Actor takes four steps to the window, pauses, and pulls the curtain in the final second” makes the timing precise and achievable.

Weak

Actor walks across the room.

Strong

Actor takes four steps to the window, pauses, and pulls the curtain in the final second.
```

同一指南「Visual cues」一节的对照（原文）：

```
“Person moves quickly”
“Cyclist pedals three times, brakes, and stops at crosswalk”
```

## 2. 调色板锚点：点名 3–5 个颜色，多段剪在一起才不跳色

> 巧在哪（非原文）：多段分别生成再剪辑，最容易露馅的是光和色不统一。官方建议除了写光源组合，再点名三到五个「锚点色」。

```
## Lighting and color consistency

Light determines mood as much as action or setting. Diffuse light across the frame feels calm and neutral, while a single strong source creates sharp contrast and tension. When you want to cut multiple clips together, keeping lighting logic consistent is what makes the edit seamless.

Describe both the quality of the light and the color anchors that reinforce it. Instead of a broad note like “brightly lit room,” specify the mix of sources and tones: “soft window light with a warm lamp fill and a cool edge from the hallway.” Naming three to five colors helps keep the palette stable across shots.

Weak

Lighting + palette: brightly lit room

Strong

Lighting + palette: soft window light with warm lamp fill, cool rim from hallway 
Palette anchors: amber, cream, walnut brown
```

## 3. 编辑是「微调」不是「重抽」：一次只改一处，说清改什么；总失败就先做减法

> 巧在哪（非原文）：结果接近时，把它固定为参考，只描述要改的一处（如「同一个镜头，换成 85 mm」）；一直失败时反过来——固定机位、简化动作、清空背景，成功后再一层层加回去。

```
## Iterate with video edits

Editing is for nudging, not gambling. Use it to make controlled changes – one at a time – and say what you’re changing: “same shot, switch to 85 mm,” or “same lighting, new palette: teal, sand, rust.” When a result is close, pin it as a reference and describe only the tweak. That way, everything that already works stays locked.

If a shot keeps misfiring, strip it back: freeze the camera, simplify the action, clear the background. Once it works, layer additional complexity step by step.

Edit prompt: “Change the color of the monster to orange”

Edit prompt: “A second monster comes out right after”
```

> 策展备注（非原文）：这里的「编辑」指 Sora 的视频编辑（remix）功能；在其他模型上可以对应为「用上一版结果做参考图 / 参考视频，只改一处描述」。

## 4. 官方完整示例：手绘 2D/3D 混合动画

> 巧在哪（非原文）：Style 一行就是「混合媒介」写法（2D/3D 手绘混合 + 定格手感 + 水彩晕染），Cinematography 分列镜头、镜头焦段、光线、情绪，Actions 按节拍逐条写，台词和背景音单独成段。可与 `技巧锦囊/44`（AI琪琪「3D 渲染角色 + 2D 手绘水墨」）对照看。

```yaml
# 条目元数据（策展者添加，非原文）
id: "jiqiao--36-openai-sora2-prompting-guide-tricks--01"
标题: "手绘 2D/3D 混合动画：工作室里的小机器人（官方完整示例）"
原标题: "Example 1"
分类: "技巧锦囊"
标签: ["技巧锦囊", "混合媒介", "3D+2D", "动作节拍", "调色板", "分段结构", "台词", "音效"]
适用模型: "Sora 2（来源标注：OpenAI《Sora 2 Prompting Guide》）"
语言: "en"
来源链接: "https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide"
镜像: "2026-09-30 直接抓取官方页面 HTML（box: /workspace/prompt-extract/raw/jiqiao-sources/sora2.html）"
作者: "OpenAI（发布方；页面署名 Robin Koenig、Joanne Shin）"
发布日期: "2026-03（页面标注「Updated - March 2026」，未标具体日期）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本（官方指南「Prompt Examples · Example 1」）"
核对状态: "verified"
核对说明: "与官方页面 HTML 转出的文本逐字核对一致；分段与换行照原样，列表的「- 」照原样。"
完整性: "完整"
备注: "官方页面在该示例上方没有给出成片；同页 Example 2（1970 年代屋顶舞蹈）是常规写法，未收入。"
技巧钩子: "官方示例本身就在用「混合媒介」：Style 一行写明 2D/3D 手绘混合、定格动画手感、水彩晕染，Actions 按节拍逐条写"
触发场景: "想做绘本 / 定格 / 手绘质感的动画短片，或想看「混合媒介 + 动作节拍」完整写法的样板时"
```

```text
Style: Hand-painted 2D/3D hybrid animation with soft brush textures, warm tungsten lighting, and a tactile, stop-motion feel. The aesthetic evokes mid-2000s storybook animation — cozy, imperfect, full of mechanical charm. Subtle watercolor wash and painterly textures; warm–cool balance in grade; filmic motion blur for animated realism.

Inside a cluttered workshop, shelves overflow with gears, bolts, and yellowing blueprints. At the center, a small round robot sits on a wooden bench, its dented body patched with mismatched plates and old paint layers. Its large glowing eyes flicker pale blue as it fiddles nervously with a humming light bulb. The air hums with quiet mechanical whirs, rain patters on the window, and the clock ticks steadily in the background.

Cinematography:
Camera: medium close-up, slow push-in with gentle parallax from hanging tools
Lens: 35 mm virtual lens; shallow depth of field to soften background clutter
Lighting: warm key from overhead practical; cool spill from window for contrast
Mood: gentle, whimsical, a touch of suspense

Actions:
- The robot taps the bulb; sparks crackle.
- It flinches, dropping the bulb, eyes widening.
- The bulb tumbles in slow motion; it catches it just in time.
- A puff of steam escapes its chest — relief and pride.
- Robot says quietly: "Almost lost it… but I got it!"

Background Sound:
Rain, ticking clock, soft mechanical hum, faint bulb sizzle.
```

## 总结（非原文）

- **节拍**：动作写成「几步、停顿、最后一秒做什么」，每个镜头一个机位动作 + 一个主体动作。
- **锚点色**：多段要剪在一起时，写清光源组合，再点名 3–5 个颜色。
- **编辑**：接近时只改一处并说清楚；一直失败时先做减法（固定机位、简化动作、清空背景）。
- **混合媒介**：官方示例同样用「2D/3D hybrid + 质感词」来定画风，和 AI琪琪 的思路一致；这是风格写法的示例，官方没有承诺某种写法一定得到某种画风。

本文件统计：计数条目 1（verified 1）；不计数代码块 5（官方原文小节）。
