# 首尾帧生图 · Runway 官方图生视频与 References 示例

## 来源概述（非原文）

- 来源（官方厂商文档，2026-09-30 抓取）：
  - Runway《Image to Video Prompting Guide》（Gen-4.5）：https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide （页面日期：未知（页面未标注））
  - Runway《Creating with Gen-4 Image References》：https://help.runwayml.com/hc/en-us/articles/40042718905875-Creating-with-Gen-4-Image-References （页面日期：未知（页面未标注））
- 许可：official-docs; copyright-retained (Runway); quoted with attribution。官方文档里的示例提示词按原文引用并注明出处，不代表厂商授权再分发。
- 来源类型：模型厂商官方提示词指南 / API 文档；`text` 围栏内为官方页面上的示例提示词，逐字复制（脚本与抓取页面比对），未改写、未翻译。官方的说明性文字不进围栏，要点写在「备注」里。
- 本文件内容：图生视频只写运动、去掉首帧里的运动暗示、减少运动的写法、Gen-4 References 角色与场景一致。
- 本文件计数条目：5；核对状态：verified 5
- 相关：做法与出处总表见 `docs/首尾帧工作流.md`、`docs/权威来源.md`。Runway《Gen-4 Video Prompting Guide》的「只写运动」机械公牛示例见 `prompts/技巧锦囊/38-runway-gen4-image-to-video-motion-only.md`；本文件取自新版《Image to Video Prompting Guide》。

## 1. Image to Video · 结构示例

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--05-runway-official--01"
标题: "Runway 图生视频：只写运动（机位运动 + 主体动作）"
原标题: "Prompt structure & organization"
分类: "首尾帧生图"
标签: ["首帧"]
适用模型: "Runway Gen-4.5（官方 Image to Video Prompting Guide 示例）"
语言: "en"
来源链接: "https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide"
镜像: ""
作者: "Runway（官方帮助中心）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (Runway); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "官方结构：The camera [motion description] as the subject [action]. [Additional descriptions]；输入图就是首帧，提示词「几乎只写运动」。"
技巧钩子: ""
触发场景: ""
```

```text
The camera slowly pushes in as the person scales the giant soda.
```

## 2. Image to Video FAQ · 与画面运动暗示相反的提示

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--05-runway-official--02"
标题: "Runway：首帧里的运动暗示会和提示词打架"
原标题: "Why am I having challenges receiving the desired motion with a certain image?"
分类: "首尾帧生图"
标签: ["首帧", "技巧锦囊"]
适用模型: "Runway Gen-4.5（官方 FAQ 示例）"
语言: "en"
来源链接: "https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide"
镜像: ""
作者: "Runway（官方帮助中心）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (Runway); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "官方说明：输入图里的运动模糊、扬尘、动作中途的姿势、方向线都是「隐含运动」；本例把车周围的扬尘和运动模糊去掉后，同一提示词才得到静止的车。"
技巧钩子: "首帧要「静」：先用图像编辑去掉运动模糊、扬尘、半空中的姿势，再让视频模型按提示词动起来"
触发场景: "图生视频时模型总往你不想要的方向动、或让它静止它却一直在动时"
```

```text
The car is parked and completely motionless. The camera performs an aggressive, sweeping horizontal arc around the parked car.
```

## 3. Image to Video FAQ · 减少运动

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--05-runway-official--03"
标题: "Runway：让镜头尽量静止的三句"
原标题: "How do I minimize camera motion for my shot?"
分类: "首尾帧生图"
标签: ["首帧"]
适用模型: "Runway Gen-4.5（官方 FAQ 示例）"
语言: "en"
来源链接: "https://help.runwayml.com/hc/en-us/articles/48324313115155-Image-to-Video-Prompting-Guide"
镜像: ""
作者: "Runway（官方帮助中心）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (Runway); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）；原文为三条列表项，去掉了网页抽取产生的项间空行"
完整性: "完整"
备注: "官方另建议：用 Animate Frames 应用、首尾两帧放同一张图，控制更强。"
技巧钩子: ""
触发场景: ""
```

```text
- The locked-off camera remains perfectly still.
- The camera must start and end on the exact same frame to create a perfect loop.
- Minimal subject motion only.
```

## 4. Gen-4 References · 单参考图

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--05-runway-official--04"
标题: "Runway Gen-4 References：用 @名字 调用保存的角色参考"
原标题: "Single Reference Prompts"
分类: "首尾帧生图"
标签: ["参考图/素材引用", "角色一致性"]
适用模型: "Runway Gen-4 Image References（官方示例）"
语言: "en"
来源链接: "https://help.runwayml.com/hc/en-us/articles/40042718905875-Creating-with-Gen-4-Image-References"
镜像: ""
作者: "Runway（官方帮助中心）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (Runway); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "官方建议角色参考图：光线自然均匀、中等画质、表情中性；想稳定得到全身，就写鞋子或裤子。"
技巧钩子: ""
触发场景: ""
```

```text
@bryan wearing a denim shirt with the sleeves cut off. he holds a single piece of hay in his mouth. medium length hair in the back. sitting on a plastic lawn chair. cinematic muted color palette. shallow depth of field.
```

## 5. Gen-4 References · 一致场景

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--05-runway-official--05"
标题: "Runway Gen-4 References：同一场景换角度 / 补 B-roll"
原标题: "Generating Consistent Scenes"
分类: "首尾帧生图"
标签: ["参考图/素材引用"]
适用模型: "Runway Gen-4 Image References（官方示例）"
语言: "en"
来源链接: "https://help.runwayml.com/hc/en-us/articles/40042718905875-Creating-with-Gen-4-Image-References"
镜像: ""
作者: "Runway（官方帮助中心）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (Runway); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "同节另有「elfbryan profile view」。"
技巧钩子: ""
触发场景: ""
```

```text
show a sword on the ground in elfbryan
```

## 总结（非原文）

- 条目数：5（`text` 围栏逐字原文）
- 语言：en 5
- 核对状态：verified 5
- 使用提醒：官方示例只说明写法，参数（画幅、分辨率、首尾帧字段）以对应厂商文档为准；各模型限制对照见 `docs/首尾帧工作流.md` 第 9 节。
