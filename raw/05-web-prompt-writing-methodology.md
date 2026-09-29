# 05 Web — AI video / image prompt writing methodology (提示词编写思路)

> Collected 2026-09-29 Asia/Shanghai after Douyin `https://v.douyin.com/mM3gTkJWuzQ/` (AI绘梦菌「AI提示词编写思路」) returned **0 body**.
> These are **public web sources**, cited per block. **Not** the Douyin post. Do not invent attribution to AI绘梦菌.

## Legend
- OK = readable methodology / formulas / templates
- Used for skill: `skills/ai-video-prompt-writing-methodology/SKILL.md`
- Used for prompts archive: `prompts/提示词写法/` (verbatim excerpts only)

---

## Source A — 翔宇 · 即梦 Seedance 2.0 八层框架

- URL: https://xiangyugongzuoliu.com/seedance-video-prompt-guide/
- Status: OK (full article fetched 2026-09-29)
- License note: third-party blog; archive excerpt for curation; not claiming ownership

### A.1 Eight-layer overview (table essence, paraphrased only in skill; formulas below are near-verbatim structure labels from article)

八层：1 素材角色声明 → 2 镜头标签 → 3 景别与主体 → 4 动作 → 5 运镜 → 6 场景与光影 → 7 音频 → 8 全局收尾

### A.2 Verbatim formula fragments (article)

```text
主体→动作→运镜→风格→约束
```

```text
上下文→素材引用→动作→构图→时序
```

### A.3 Verbatim emotion-externalization rows (article)

```text
悲伤 → 低下头，肩膀微微发抖，眼眶泛红，手指不自觉攥紧衣角
喜悦 → 嘴角不自觉上扬，眉眼舒展，脚步变得轻快，忍不住原地转圈
紧张 → 频繁看手表，手指不停敲桌面，呼吸急促，目光闪躲
愤怒 → 双拳紧握，下颚线绷紧，胸膛剧烈起伏，牙关紧咬挤出话来
释然 → 长长呼出一口气，绷紧的双肩彻底放松，久违的淡淡微笑浮现
```

### A.4 Verbatim camera term table (subset)

```text
dolly in/out — 推进/拉出
pan left/right — 左摇/右摇
tracking shot — 跟拍
orbit — 环绕
handheld — 手持
fixed/locked — 固定/锁定
crane up/down — 升降
push in — 推入
slow dolly — 缓慢推进
rack focus — 焦点转移
```

### A.5 Verbatim positive constraints (article; Jimeng has no negative prompts)

```text
保持面部一致，无变形，无拉伸，避免抖动和弯曲肢体，避免身份漂移，不生成字幕，不生成水印
```

### A.6 Verbatim single-shot length guidance

```text
单镜头 60-100 词；多镜头序列 200-300 词；低于 30 词模型会随机脑补，超过 300 词后半段容易被忽略
```

Full article HTML/markdown was too long to dump here; skill + prompts cite URL for complete templates 1–10 and meta-prompts.

---

## Source B — AI Stack Nav · 镜头/场景/动作技巧

- URL: https://aistacknav.com/ai-video-prompt-tips-camera-scene-action/
- Status: OK (fetched 2026-09-29)

### B.1 Verbatim universal formula

```text
主体 + 场景 + 动作过程 + 镜头景别 + 运镜方式 + 光线氛围 + 画面风格 + 时长/比例 + 负面提示词
```

### B.2 Verbatim one-liner conclusion

```text
AI 视频提示词 = 主体 + 场景 + 动作链 + 镜头语言 + 光线风格 + 时长比例 + 负面限制。写得越像导演给摄影师和演员的说明，生成结果越可控。
```

### B.3 Verbatim city-walk template

```text
一名穿浅色风衣的年轻女性走在雨后的城市街头，夜晚，路面有霓虹灯反射。镜头从中景缓慢推近到近景，轻微手持感，人物先低头看手机，然后抬头看向远处，表情从迷茫变得坚定。电影感写实风格，浅景深，柔和蓝紫色霓虹光，5 秒，16:9。避免脸部变形、手部多指、背景跳变、文字乱码。
```

### B.4 Verbatim generic negatives

```text
避免人物脸部变形、手指数量错误、肢体扭曲、眼睛错位、背景突然变化、物体漂移、文字乱码、水印、画面闪烁、镜头过度晃动、主体消失、动作不连贯。
```

---

## Source C — lanshu-awesome-ai-video-kit · 进阶公式 8 要素

- URL: https://raw.githubusercontent.com/cclank/lanshu-awesome-ai-video-kit/main/methodology/02-%E8%BF%9B%E9%98%B6%E5%85%AC%E5%BC%8F.md
- Status: OK (raw GitHub MIT-likely kit; fetched 2026-09-29)

### C.1 Verbatim formula

```text
精准主体 + 动作细节 + 场景环境 + 光影色调 + 镜头运镜 + 视觉风格 + 画质 + 约束条件
```

### C.2 Verbatim subject definition pattern

```text
将 <图片/视频N> 中的 [主体核心特征] 定义为 <主体N>
```

```text
将图片1中穿红色连衣裙、戴草帽的女人定义为主体1
```

### C.3 Verbatim dorm short-drama example (official-PDF-derived in kit)

```text
@图片 1 中的女孩作为主角，@图片 2 作为宿舍场景风格参考，参考 @视频 1 的运镜方式。

镜头 1：傍晚时分，女孩@图片 1 脚步轻快地走到宿舍门口@图片 2，镜头中景平稳跟拍，
        暖黄色日光从窗外洒进走廊，她在门口停顿一下，深呼吸，表情略带紧张。

镜头 2：女孩@图片 1 推开门走进宿舍，镜头切到室内中景，舍友们一边整理书本一边
        抬头看向她，其中一人笑着问 {考得怎么样啊，过了吗}，镜头在几人之间缓慢
        切换半身特写。

镜头 3：女孩@图片 1 先低头露出落寞表情，镜头给到她的近景，随后她抬头憋不住笑容，
        哈哈大笑说 {骗你们的}，舍友们追着打闹起来，镜头缓慢拉远，定格在宿舍内
        一片欢声笑语的全景画面。

全程画面高清电影纪实风，色调温暖，光影柔和；人物面部稳定不变形，动作自然流畅，
无卡顿无闪烁；环境音效与 @音频 1 自然融合。
```

---

## Source D — SunoMV · Seedance 2.5 官方公式对照

- URL: https://suno.bi/zh/blog/seedance-2-5-prompt-guide
- Status: OK (fetched 2026-09-29)
- Note: summarizes ByteDance Seedance 2.5 guide; 2.0 vs 2.5 timestamp divergence

### D.1 Verbatim four-part structure (article paraphrase of official)

```text
1. 素材指代
2. 一句话概述
3. 具体情节（时间戳或「镜头 N」）
4. 结尾收束
```

### D.2 Verbatim 2.0 vs 2.5 shot examples

```text
镜头 1：街巷侧拍，男人缓慢起跑，带有急促的呼吸感。
镜头 2：男人撞翻水果摊，镜头快速摇动并给到男人惊恐的特写。
镜头 3：男人翻过矮墙消失，镜头缓慢拉远定格在空荡的街道。
```

```text
0s-3s：低机位中远景，熊猫幼崽趴在绿色草坡上，顺着斜坡慢慢侧滚，阳光从左上方穿过树林。
3s-8s：熊猫滚到画面右下方停下，从侧躺变成趴卧，圆脸朝向镜头，头部小幅抬起又放低。
```

### D.3 Verbatim color three-layer recipe (article)

```text
主色调：大面积基底
次色调：主体相关的中间层
点缀色：一两个反复出现的小面积高光
```

---

## Douyin target (blocked)

See `raw/douyin-mM3gTkJWuzQ/blocker.md` — 0 body characters recovered from AI绘梦菌 post.
