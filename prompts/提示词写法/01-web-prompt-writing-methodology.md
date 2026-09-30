# 提示词写法 · 网页收录：AI 视频 / 图片提示词编写方法（原文摘录）

## 来源概述（非原文）

- 来源：AI Stack Nav、lanshu-awesome-ai-video-kit（GitHub）、翔宇工作流、SunoMV 四个公开来源；各节标注具体链接。
- 来源类型：网页 / GitHub；`text` 围栏内为可直接使用的原文公式或示例，逐字复制；无语言标记的代码块是作者的方法说明原文，不计数。
- 收录：2026-09-29（Asia/Shanghai）。
- 背景：用户给的抖音链接 `https://v.douyin.com/mM3gTkJWuzQ/`（AI绘梦菌「AI提示词编写思路」）2026-09-29 无法取得正文，见 `docs/douyin-blockers/douyin-mM3gTkJWuzQ-AI绘梦菌.md`；本文件收录公开的方法论原文，供本分类使用。
- 相关（交叉链接，非重复）：景别 `运镜/43-douyin-huxiaolv-shot-size-jingbie.md`；运镜词典 `运镜/42-x-adrianpunk115-camera-dictionary-part1.md`、`运镜/41-x-adrianpunk115-camera-dictionary-part2.md`；官方指南 `提示词写法/32-runway-seedance-2.0-prompt-guide.md`；术语与写法裁定见 `docs/术语速查.md`、`docs/最佳实践.md`。

- 本文件计数条目：9 个 `text` 原文围栏；核对状态：verified 9（2026-09-30 下午：宿舍短剧 kit 版移出计数，官方逐字版见 `提示词写法/33`）

## 1. AI Stack Nav：万能公式与城市漫游示例

- **Language:** zh-CN
- **Source:** https://aistacknav.com/ai-video-prompt-tips-camera-scene-action/
- **license/open-source tag:** public web article (third-party tutorial); curation excerpt

### 1.1 通用模板

```
主体 + 场景 + 动作过程 + 镜头景别 + 运镜方式 + 光线氛围 + 画面风格 + 时长/比例 + 负面提示词
```

### 1.2 一句话结论

```
AI 视频提示词 = 主体 + 场景 + 动作链 + 镜头语言 + 光线风格 + 时长比例 + 负面限制。写得越像导演给摄影师和演员的说明，生成结果越可控。
```

### 1.3 优化后城市街头示例

```yaml
# 条目元数据（策展者添加，非原文）
id: "prompt-writing--01-web-prompt-writing-methodology--01"
标题: "优化后城市街头示例"
原标题: ""
分类: "提示词写法"
标签: ["横屏16:9", "手持"]
适用模型: "未指定（通用写法）"
语言: "zh"
来源链接: "https://aistacknav.com/ai-video-prompt-tips-camera-scene-action/"
镜像: ""
作者: "AI Stack Nav（发布方）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
技巧钩子: ""
触发场景: ""
```

```text
一名穿浅色风衣的年轻女性走在雨后的城市街头，夜晚，路面有霓虹灯反射。镜头从中景缓慢推近到近景，轻微手持感，人物先低头看手机，然后抬头看向远处，表情从迷茫变得坚定。电影感写实风格，浅景深，柔和蓝紫色霓虹光，5 秒，16:9。避免脸部变形、手部多指、背景跳变、文字乱码。
```

### 1.4 通用负面

```yaml
# 条目元数据（策展者添加，非原文）
id: "prompt-writing--01-web-prompt-writing-methodology--02"
标题: "通用负面"
原标题: ""
分类: "提示词写法"
标签: []
适用模型: "未指定（通用写法）"
语言: "zh"
来源链接: "https://aistacknav.com/ai-video-prompt-tips-camera-scene-action/"
镜像: ""
作者: "AI Stack Nav（发布方）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: "【2026-09-30 官方文档复核（非原文）】这类「避免……」清单只适合接受否定写法的模型：Runway Gen-4 不支持否定写法；Veo 要求在单独的负面字段里只列名词；Seedance 2.5 否定只建议用于字幕和音频。见 docs/术语速查.md 第 10 节。"
技巧钩子: ""
触发场景: ""
```

```text
避免人物脸部变形、手指数量错误、肢体扭曲、眼睛错位、背景突然变化、物体漂移、文字乱码、水印、画面闪烁、镜头过度晃动、主体消失、动作不连贯。
```

### 1.5 城市漫游模板

```yaml
# 条目元数据（策展者添加，非原文）
id: "prompt-writing--01-web-prompt-writing-methodology--03"
标题: "城市漫游模板"
原标题: ""
分类: "提示词写法"
标签: ["横屏16:9"]
适用模型: "未指定（通用写法）"
语言: "zh"
来源链接: "https://aistacknav.com/ai-video-prompt-tips-camera-scene-action/"
镜像: ""
作者: "AI Stack Nav（发布方）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
技巧钩子: ""
触发场景: ""
```

```text
一名旅行者背着小包走在现代城市街头，清晨阳光穿过高楼之间，街道干净，路边有咖啡店和行人。镜头从人物背后中景横向跟拍，人物自然向前走，偶尔转头观察街景，衣角轻微摆动。电影感写实风格，柔和自然光，浅景深，节奏舒缓，6 秒，16:9。避免脸部变形、行人穿模、背景跳变、文字乱码。
```

### 1.6 产品广告模板

```yaml
# 条目元数据（策展者添加，非原文）
id: "prompt-writing--01-web-prompt-writing-methodology--04"
标题: "产品广告模板"
原标题: ""
分类: "提示词写法"
标签: ["产品/广告"]
适用模型: "未指定（通用写法）"
语言: "zh"
来源链接: "https://aistacknav.com/ai-video-prompt-tips-camera-scene-action/"
镜像: ""
作者: "AI Stack Nav（发布方）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
技巧钩子: ""
触发场景: ""
```

```text
一只极简风无线耳机放在磨砂黑色桌面上，背景为柔和蓝色渐变灯光。镜头从产品特写缓慢环绕到 45 度侧面，耳机表面保持清晰，金属边缘有高光反射，背景轻微虚化。商业广告质感，干净高级，4 秒，1:1。产品外形保持一致，避免 Logo 变形、物体漂移、画面闪烁。
```

## 2. lanshu-awesome-ai-video-kit：8 要素公式与宿舍短剧示例

- **Language:** zh-CN
- **Source:** https://raw.githubusercontent.com/cclank/lanshu-awesome-ai-video-kit/main/methodology/02-%E8%BF%9B%E9%98%B6%E5%85%AC%E5%BC%8F.md
- **license/open-source tag:** public GitHub methodology (kit); check upstream LICENSE

### 2.1 进阶公式

```
精准主体 + 动作细节 + 场景环境 + 光影色调 + 镜头运镜 + 视觉风格 + 画质 + 约束条件
```

### 2.2 主体定义句式

```yaml
# 条目元数据（策展者添加，非原文）
id: "prompt-writing--01-web-prompt-writing-methodology--05"
标题: "主体定义句式"
原标题: ""
分类: "提示词写法"
标签: []
适用模型: "Seedance 2.0（来源标注）"
语言: "zh"
来源链接: "https://raw.githubusercontent.com/cclank/lanshu-awesome-ai-video-kit/main/methodology/02-%E8%BF%9B%E9%98%B6%E5%85%AC%E5%BC%8F.md"
镜像: ""
作者: "未知"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致（来源中为「推荐句式」一行行内代码）"
完整性: "完整"
备注: ""
技巧钩子: ""
触发场景: ""
```

```text
将 <图片/视频N> 中的 [主体核心特征] 定义为 <主体N>
```

```yaml
# 条目元数据（策展者添加，非原文）
id: "prompt-writing--01-web-prompt-writing-methodology--06"
标题: "主体定义句式（2）"
原标题: ""
分类: "提示词写法"
标签: []
适用模型: "Seedance 2.0（来源标注）"
语言: "zh"
来源链接: "https://raw.githubusercontent.com/cclank/lanshu-awesome-ai-video-kit/main/methodology/02-%E8%BF%9B%E9%98%B6%E5%85%AC%E5%BC%8F.md"
镜像: ""
作者: "未知"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
技巧钩子: ""
触发场景: ""
```

```text
将图片1中穿红色连衣裙、戴草帽的女人定义为主体1
```

### 2.3 宿舍情感短剧（kit 内官方 PDF 衍生示例）

> 2026-09-30 官方文档复核（非原文）：本条原为计数条目 `prompt-writing--01-web-prompt-writing-methodology--07`（核对状态 source-contradicts），现**移出计数**。理由：它是火山引擎《Doubao Seedance 2.0 系列提示词指南》示例 1 的转录版，与官方有 3 处字词差异（「考得怎么样啊」「憋不住笑容」，官方为「考得怎么样呀」「憋不住笑意」）并有人工换行；官方逐字版已收录为 `提示词写法/33-official-vendor-video-examples.md` 第 1 条。下面保留 kit 原文作对照（无语言标记代码块，不计数），未改动。

```
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

## 3. 翔宇工作流：Seedance 2.0 八层写法原文片段

- **Language:** zh-CN
- **Source:** https://xiangyugongzuoliu.com/seedance-video-prompt-guide/
- **license/open-source tag:** public blog; curation excerpt (full 10 templates remain at URL — not fully mirrored to avoid huge dump)
- **fetch status（自原 `raw/05` 并入，2026-09-30 去重）:** OK — full article fetched 2026-09-29 Asia/Shanghai
- **related（2026-09-30 交叉链接）:** 景别/运镜术语的完整原创讲解见 `运镜/43-douyin-huxiaolv-shot-size-jingbie.md`（胡小绿 · 景别）、`运镜/42-x-adrianpunk115-camera-dictionary-part1.md`（上篇）、`运镜/41-x-adrianpunk115-camera-dictionary-part2.md`（下篇）

### 3.0 八层概览与运镜术语表子集（自原 `raw/05-web-prompt-writing-methodology.md` §A.1/§A.4 并入）

> 2026-09-30 全库去重：`raw/05` 的 18 个围栏中 17 个与本文件逐字重复，已删除该 raw 副本；仅以下两项本文件原先没有，原样并入。**A.4 是原文表格的子集（非完整表），因此用无语言围栏保存、不计入 ` ```text ` 条目数。**

八层（原 raw 记录为表格要点，非逐字）：1 素材角色声明 → 2 镜头标签 → 3 景别与主体 → 4 动作 → 5 运镜 → 6 场景与光影 → 7 音频 → 8 全局收尾

```
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

### 3.1 历史框架标签

```
主体→动作→运镜→风格→约束
```

```
上下文→素材引用→动作→构图→时序
```

### 3.2 情绪外化对照

```
悲伤 → 低下头，肩膀微微发抖，眼眶泛红，手指不自觉攥紧衣角
喜悦 → 嘴角不自觉上扬，眉眼舒展，脚步变得轻快，忍不住原地转圈
紧张 → 频繁看手表，手指不停敲桌面，呼吸急促，目光闪躲
愤怒 → 双拳紧握，下颚线绷紧，胸膛剧烈起伏，牙关紧咬挤出话来
释然 → 长长呼出一口气，绷紧的双肩彻底放松，久违的淡淡微笑浮现
```

### 3.3 正面约束模板

```yaml
# 条目元数据（策展者添加，非原文）
id: "prompt-writing--01-web-prompt-writing-methodology--08"
标题: "正面约束模板"
原标题: ""
分类: "提示词写法"
标签: []
适用模型: "Seedance 2.0（来源标注）"
语言: "zh"
来源链接: "https://xiangyugongzuoliu.com/seedance-video-prompt-guide/"
镜像: ""
作者: "翔宇工作流（发布方）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
技巧钩子: ""
触发场景: ""
```

```text
保持面部一致，无变形，无拉伸，避免抖动和弯曲肢体，避免身份漂移，不生成字幕，不生成水印
```

> 【已移除（2026-09-30 整合）】原 §3.4「长度指引」为策展者转述（原文写作「补脑」且为散文段落），不是逐字原文；要点见 `docs/最佳实践.md`。

## 4. SunoMV：Seedance 2.0 / 2.5 分镜写法对照

- **Language:** zh-CN
- **Source:** https://suno.bi/zh/blog/seedance-2-5-prompt-guide
- **license/open-source tag:** public blog summarizing ByteDance guide

> 【已移除（2026-09-30 整合）】原 §4.1「四段式结构标签」为对 suno.bi 原文的压缩改写，不是逐字原文；结构说明见 `docs/最佳实践.md`（以火山引擎官方 Seedance 2.5 指南为准）。

### 4.2 Seedance 2.0 推荐（序号式）

```yaml
# 条目元数据（策展者添加，非原文）
id: "prompt-writing--01-web-prompt-writing-methodology--09"
标题: "Seedance 2.0 推荐（序号式）"
原标题: ""
分类: "提示词写法"
标签: ["分镜/多镜头"]
适用模型: "Seedance 2.5（来源标注）"
语言: "zh"
来源链接: "https://suno.bi/zh/blog/seedance-2-5-prompt-guide"
镜像: ""
作者: "SunoMV（发布方）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
技巧钩子: ""
触发场景: ""
```

```text
镜头 1：街巷侧拍，男人缓慢起跑，带有急促的呼吸感。
镜头 2：男人撞翻水果摊，镜头快速摇动并给到男人惊恐的特写。
镜头 3：男人翻过矮墙消失，镜头缓慢拉远定格在空荡的街道。
```

### 4.3 Seedance 2.5 推荐（秒级时间戳）

```yaml
# 条目元数据（策展者添加，非原文）
id: "prompt-writing--01-web-prompt-writing-methodology--10"
标题: "Seedance 2.5 推荐（秒级时间戳）"
原标题: ""
分类: "提示词写法"
标签: ["时间码分段"]
适用模型: "Seedance 2.5（来源标注）"
语言: "zh"
来源链接: "https://suno.bi/zh/blog/seedance-2-5-prompt-guide"
镜像: ""
作者: "SunoMV（发布方）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "未注明（来源未声明许可）"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 重新抓取的来源页逐字一致"
完整性: "完整"
备注: ""
技巧钩子: ""
触发场景: ""
```

```text
0s-3s：低机位中远景，熊猫幼崽趴在绿色草坡上，顺着斜坡慢慢侧滚，阳光从左上方穿过树林。
3s-8s：熊猫滚到画面右下方停下，从侧躺变成趴卧，圆脸朝向镜头，头部小幅抬起又放低。
```

> 【已移除（2026-09-30 整合）】原 §4.4「色调三层」为对 suno.bi 原文的压缩改写（删去了原文括注示例），不是逐字原文；要点见 `docs/最佳实践.md`。

## 抖音来源缺口

- short_url: https://v.douyin.com/mM3gTkJWuzQ/
- video_id: 7690573169337453860
- author cue: AI绘梦菌
- recovered_verbatim_from_douyin: **0 chars**

## 总结（非原文）

- 条目数：9（`text` 围栏逐字原文）
- 语言：zh 9
- 适用模型：未指定 4、Seedance 2.0 3、Seedance 2.5 2
- 核对状态：verified 9
- 常见写法特征（按规则自动识别）：横屏16:9 2、分镜/多镜头 1、手持 1、产品/广告 1、时间码分段 1
