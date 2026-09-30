# 首尾帧生图 · Black Forest Labs 官方 FLUX 首尾帧 / 关键帧与编辑示例

## 来源概述（非原文）

- 来源（官方厂商文档，2026-09-30 抓取）：
  - Black Forest Labs《Image-to-Video》（FLUX 3）：https://docs.bfl.ml/guides/prompting_video_image_to_video （页面日期：未知（页面未标注））
  - Black Forest Labs《Single-reference editing》（FLUX.2）：https://docs.bfl.ml/guides/prompting_editing_single_reference （页面日期：未知（页面未标注））
  - Black Forest Labs《Multi-reference editing》（FLUX.2）：https://docs.bfl.ml/guides/prompting_editing_multi_reference （页面日期：未知（页面未标注））
- 许可：official-docs; copyright-retained (Black Forest Labs); quoted with attribution。官方文档里的示例提示词按原文引用并注明出处，不代表厂商授权再分发。
- 来源类型：模型厂商官方提示词指南 / API 文档；`text` 围栏内为官方页面上的示例提示词，逐字复制（脚本与抓取页面比对），未改写、未翻译。官方的说明性文字不进围栏，要点写在「备注」里。
- 本文件内容：FLUX 3 首尾帧与关键帧视频提示词；FLUX.2 单图 / 多图编辑（改时间、改视线、保姿势构图）。
- 本文件计数条目：7；核对状态：verified 7
- 相关：做法与出处总表见 `docs/首尾帧工作流.md`、`docs/权威来源.md`。

## 1. Start + end frame · City: day to night

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--04-bfl-flux-official--01"
标题: "FLUX 3 首尾帧：城市日转夜"
原标题: "Start + end frame — City: day to night"
分类: "首尾帧生图"
标签: ["首尾帧"]
适用模型: "FLUX 3（BFL 官方视频指南示例）"
语言: "en"
来源链接: "https://docs.bfl.ml/guides/prompting_video_image_to_video"
镜像: ""
作者: "Black Forest Labs（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (Black Forest Labs); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "官方说明：首尾两帧要相关（同一主体、场景或机位），差距越大模型自由度和不可预测性越高。"
技巧钩子: ""
触发场景: ""
```

```text
A wide waterfront city skyline transitions from bright midday to glittering night: daylight fades through dusk to dark, thousands of lights switching on across the towers and shimmering on the water.
```

## 2. Start + end frame · Ink in motion

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--04-bfl-flux-official--02"
标题: "FLUX 3 首尾帧：墨水颜色渐变"
原标题: "Start + end frame — Ink in motion"
分类: "首尾帧生图"
标签: ["首尾帧"]
适用模型: "FLUX 3（BFL 官方视频指南示例）"
语言: "en"
来源链接: "https://docs.bfl.ml/guides/prompting_video_image_to_video"
镜像: ""
作者: "Black Forest Labs（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (Black Forest Labs); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: ""
技巧钩子: ""
触发场景: ""
```

```text
Vivid clouds of colored ink billow and swirl through dark water: electric blue and crimson tendrils bloom, fold and diffuse, slowly transforming into deep magenta and violet plumes.
```

## 3. Keyframes · Aurora

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--04-bfl-flux-official--03"
标题: "FLUX 3 三关键帧：极光变色（0s / 2.5s / 5s）"
原标题: "Keyframes — Aurora"
分类: "首尾帧生图"
标签: ["关键帧"]
适用模型: "FLUX 3（BFL 官方视频指南示例）"
语言: "en"
来源链接: "https://docs.bfl.ml/guides/prompting_video_image_to_video"
镜像: ""
作者: "Black Forest Labs（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (Black Forest Labs); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "官方说明：关键帧按时间顺序读取，要保持各帧观感一致，镜头才会像一条连续镜头而不是一串剪辑；3 张以上或带时间戳的关键帧需要显式 duration。"
技巧钩子: ""
触发场景: ""
```

```text
A wide long-exposure night sky over snowy northern mountains: the aurora borealis sweeps and ripples, shifting from soft magenta and violet into teal and finally vivid green above the frozen horizon.
```

## 4. Single reference · Change it to Night

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--04-bfl-flux-official--04"
标题: "FLUX.2 单图编辑：改成夜晚（做尾帧）"
原标题: "Lighting, Weather & Season Changes"
分类: "首尾帧生图"
标签: ["图像编辑", "首尾帧"]
适用模型: "FLUX.2（BFL 官方编辑指南示例）"
语言: "en"
来源链接: "https://docs.bfl.ml/guides/prompting_editing_single_reference"
镜像: ""
作者: "Black Forest Labs（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (Black Forest Labs); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "同页还有「Change this to Winter」。"
技巧钩子: ""
触发场景: ""
```

```text
Change it to Night
```

## 5. Single reference · Looking at the camera

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--04-bfl-flux-official--05"
标题: "FLUX.2 单图编辑：只改视线方向"
原标题: "Pose & Expression Changes"
分类: "首尾帧生图"
标签: ["图像编辑", "首尾帧"]
适用模型: "FLUX.2（BFL 官方编辑指南示例）"
语言: "en"
来源链接: "https://docs.bfl.ml/guides/prompting_editing_single_reference"
镜像: ""
作者: "Black Forest Labs（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (Black Forest Labs); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: ""
技巧钩子: ""
触发场景: ""
```

```text
The woman is now looking at the camera
```

## 6. Multi reference · Keep pose, lighting and composition

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--04-bfl-flux-official--06"
标题: "FLUX.2 多图编辑：迁移图 2 的外观，保持图 1 的姿势、光线、构图"
原标题: "Style & Material Transfer"
分类: "首尾帧生图"
标签: ["图像编辑", "参考图/素材引用"]
适用模型: "FLUX.2（BFL 官方编辑指南示例）"
语言: "en"
来源链接: "https://docs.bfl.ml/guides/prompting_editing_multi_reference"
镜像: ""
作者: "Black Forest Labs（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (Black Forest Labs); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: ""
技巧钩子: ""
触发场景: ""
```

```text
Apply the colors, patterns, and surface tones of the animal in Image 2 to the animal in Image 1. Keep the pose, lighting, and overall composition of Image 1 unchanged.
```

## 7. Single reference · Illustration to realistic

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--04-bfl-flux-official--07"
标题: "FLUX.2 插画转写实：比例和布局完全保持"
原标题: "Style Transfer"
分类: "首尾帧生图"
标签: ["图像编辑"]
适用模型: "FLUX.2（BFL 官方编辑指南示例）"
语言: "en"
来源链接: "https://docs.bfl.ml/guides/prompting_editing_single_reference"
镜像: ""
作者: "Black Forest Labs（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (Black Forest Labs); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: ""
技巧钩子: ""
触发场景: ""
```

```text
Transform the architectural illustration from image 1 into a fully realistic house, natural lighting, real textures for walls windows and roof, realistic landscaping around the house, accurate shadows, real materials such as wood stone and glass, high resolution photorealism, clean perspective, keep the proportions and layout exactly as in the illustration while turning every element into a believable real world version.
```

## 总结（非原文）

- 条目数：7（`text` 围栏逐字原文）
- 语言：en 7
- 核对状态：verified 7
- 使用提醒：官方示例只说明写法，参数（画幅、分辨率、首尾帧字段）以对应厂商文档为准；各模型限制对照见 `docs/首尾帧工作流.md` 第 9 节。
