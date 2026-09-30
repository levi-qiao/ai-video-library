# 首尾帧生图 · OpenAI 官方 GPT Image 2.5 提示词指南示例

## 来源概述（非原文）

- 来源（官方厂商文档，2026-09-30 抓取）：
  - OpenAI《Image prompting guide》（GPT Image 2.5）：https://developers.openai.com/api/docs/guides/image-prompting （页面日期：未知（页面未标注））
- 许可：official-docs; copyright-retained (OpenAI); quoted with attribution。官方文档里的示例提示词按原文引用并注明出处，不代表厂商授权再分发。
- 来源类型：模型厂商官方提示词指南 / API 文档；`text` 围栏内为官方页面上的示例提示词，逐字复制（脚本与抓取页面比对），未改写、未翻译。官方的说明性文字不进围栏，要点写在「备注」里。
- 本文件内容：首帧写实出图、只改一个条件做尾帧、保身份换装、多图合成、角色延续。
- 本文件计数条目：9；核对状态：verified 9
- 相关：做法与出处总表见 `docs/首尾帧工作流.md`、`docs/权威来源.md`。

## 1. Control style and lighting · 写实人像首帧（老水手）

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--01-openai-gpt-image-official--01"
标题: "写实首帧：老水手（主体 + 取景 + 光线 + 质感）"
原标题: "Control style and lighting"
分类: "首尾帧生图"
标签: ["首帧"]
适用模型: "GPT Image 2.5（官方指南示例；Flare / Sunburst）"
语言: "en"
来源链接: "https://developers.openai.com/api/docs/guides/image-prompting"
镜像: ""
作者: "OpenAI（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (OpenAI); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "官方给出的生成设置：size=\"1024x1536\", quality=\"medium\"。做视频首帧时把 size 改成目标视频的比例（见 docs/首尾帧工作流.md 第 1 步）。"
技巧钩子: ""
触发场景: ""
```

```text
Create a photorealistic candid photograph of an elderly sailor standing on a small fishing boat.
He has weathered skin with visible wrinkles, pores, and sun texture, and a few faded traditional sailor tattoos on his arms.
He is calmly adjusting a net while his dog sits nearby on the deck. Shot like a 35mm film photograph, medium close-up at eye level, using a 50mm lens.
Soft coastal daylight, shallow depth of field, subtle film grain, natural color balance.
The image should feel honest and unposed, with real skin texture, worn materials, and everyday detail. No glamorization, no heavy retouching.
```

## 2. Preserve identity and change clothing · 保身份只换衣服

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--01-openai-gpt-image-official--02"
标题: "保身份只换衣服（锁脸、锁姿势、锁机位）"
原标题: "Preserve identity and change clothing"
分类: "首尾帧生图"
标签: ["参考图/素材引用", "角色一致性", "图像编辑"]
适用模型: "GPT Image 2.5（官方指南示例）"
语言: "en"
来源链接: "https://developers.openai.com/api/docs/guides/image-prompting"
镜像: ""
作者: "OpenAI（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (OpenAI); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "输入：人物照 + 三张服装参考图。"
技巧钩子: ""
触发场景: ""
```

```text
Edit the image to dress the woman using the provided clothing images. Do not change her face, facial features, skin tone, body shape, pose, or identity in any way. Preserve her exact likeness, expression, hairstyle, and proportions. Replace only the clothing, fitting the garments naturally to her existing pose and body geometry with realistic fabric behavior. Match lighting, shadows, and color temperature to the original photo so the outfit integrates photorealistically, without looking pasted on. Do not change the background, camera angle, framing, or image quality, and do not add accessories, text, logos, or watermarks.
```

## 3. Combine references · 多图合成

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--01-openai-gpt-image-official--03"
标题: "多图合成：把图 2 的主体放进图 1（光线与构图不变）"
原标题: "Combine references"
分类: "首尾帧生图"
标签: ["参考图/素材引用", "图像编辑"]
适用模型: "GPT Image 2.5（官方指南示例）"
语言: "en"
来源链接: "https://developers.openai.com/api/docs/guides/image-prompting"
镜像: ""
作者: "OpenAI（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (OpenAI); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "官方说明：按编号给每张输入图分配角色，写清楚移动什么、放到哪里、什么保持不变。"
技巧钩子: ""
触发场景: ""
```

```text
Place the dog from the second image into the setting of image 1, right next to the woman, use the same style of lighting, composition and background. Do not change anything else.
```

## 4. Turn a drawing into a realistic image · 草图转写实

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--01-openai-gpt-image-official--04"
标题: "草图 / 分镜线稿转写实首帧"
原标题: "Turn a drawing into a realistic image"
分类: "首尾帧生图"
标签: ["图像编辑"]
适用模型: "GPT Image 2.5（官方指南示例）"
语言: "en"
来源链接: "https://developers.openai.com/api/docs/guides/image-prompting"
镜像: ""
作者: "OpenAI（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (OpenAI); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "官方说明：把提示词当规格书，保留布局与透视，再补材质、光线、环境。"
技巧钩子: ""
触发场景: ""
```

```text
Turn this drawing into a photorealistic image.
Preserve the exact layout, proportions, and perspective.
Choose realistic materials and lighting consistent with the sketch intent.
Do not add new elements or text.
```

## 5. Remove an object · 删除一个物体

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--01-openai-gpt-image-official--05"
标题: "删除一个物体，其余不变"
原标题: "Remove an object"
分类: "首尾帧生图"
标签: ["图像编辑"]
适用模型: "GPT Image 2.5（官方指南示例）"
语言: "en"
来源链接: "https://developers.openai.com/api/docs/guides/image-prompting"
镜像: ""
作者: "OpenAI（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (OpenAI); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: ""
技巧钩子: ""
触发场景: ""
```

```text
Remove the flower from man's hand. Do not change anything else.
```

## 6. Insert a person into a scene · 人物放进新场景

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--01-openai-gpt-image-official--06"
标题: "人物放进新场景（保身份，要真实照片感）"
原标题: "Insert a person into a scene"
分类: "首尾帧生图"
标签: ["参考图/素材引用", "角色一致性"]
适用模型: "GPT Image 2.5（官方指南示例）"
语言: "en"
来源链接: "https://developers.openai.com/api/docs/guides/image-prompting"
镜像: ""
作者: "OpenAI（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (OpenAI); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "原文要求真实照片感，所以明确写了不要电影化布光和调色；想要电影感时不要照搬最后一句。"
技巧钩子: ""
触发场景: ""
```

```text
Generate a highly realistic action scene where this person is running away from a large, realistic brown bear attacking a campsite. The image should look like a real photograph someone could have taken, not an overly enhanced or cinematic movie-poster image.
She is centered in the image but looking away from the camera, wearing outdoorsy camping attire, with dirt on her face and tears in her clothing. She is clearly afraid but focused on escaping, running away from the bear as it destroys the campsite behind her.
The campsite is in Yosemite National Park, with believable natural details. The time of day is dusk, with natural lighting and realistic colors. Everything should feel grounded, authentic, and unstyled, as if captured in a real moment. Avoid cinematic lighting, dramatic color grading, or stylized composition.
```

## 7. Change one condition · 只改一个条件

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--01-openai-gpt-image-official--07"
标题: "只改一个条件：同一画面改成冬夜下雪"
原标题: "Change one condition"
分类: "首尾帧生图"
标签: ["图像编辑", "首尾帧", "技巧锦囊"]
适用模型: "GPT Image 2.5（官方指南示例）"
语言: "en"
来源链接: "https://developers.openai.com/api/docs/guides/image-prompting"
镜像: ""
作者: "OpenAI（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (OpenAI); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "官方用法：把上一步的输出作为这一步的输入，只提一个改动。"
技巧钩子: "尾帧不用重新生成：拿首帧做一次「只改一个条件」的编辑（天气、时间、表情），构图和人物自然对齐"
触发场景: "做首尾帧视频（日转夜、晴转雪、表情变化），需要两张构图完全一致的图时"
```

```text
Make it look like a winter evening with snowfall.
```

## 8. Keep a character consistent · 建立角色

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--01-openai-gpt-image-official--08"
标题: "建立可复用的角色参考图"
原标题: "Keep a character consistent — Establish the character"
分类: "首尾帧生图"
标签: ["角色一致性"]
适用模型: "GPT Image 2.5（官方指南示例）"
语言: "en"
来源链接: "https://developers.openai.com/api/docs/guides/image-prompting"
镜像: ""
作者: "OpenAI（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (OpenAI); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "与下一条配套使用。"
技巧钩子: ""
触发场景: ""
```

```text
Create a children’s book illustration introducing a main character.

Character:
A young, storybook-style hero inspired by a little forest outlaw,
wearing a simple green hooded tunic, soft brown boots, and a small belt pouch.
The character has a kind expression, gentle eyes, and a brave but warm demeanor.
Carries a small wooden bow used only for helping, never harming.

Theme:
The character protects and rescues small forest animals like squirrels, birds, and rabbits.

Style:
Children’s book illustration, hand-painted watercolor look,
soft outlines, warm earthy colors, whimsical and friendly.
Proportions suitable for picture books (slightly oversized head, expressive face).

Constraints:
- Original character (no copyrighted characters)
- No text
- No watermarks
- Plain forest background to clearly showcase the character
```

## 9. Keep a character consistent · 延续角色到新场景

```yaml
# 条目元数据（策展者添加，非原文）
id: "keyframe-image--01-openai-gpt-image-official--09"
标题: "角色延续到新场景（重复外观约束）"
原标题: "Keep a character consistent — Continue the story"
分类: "首尾帧生图"
标签: ["角色一致性", "参考图/素材引用"]
适用模型: "GPT Image 2.5（官方指南示例）"
语言: "en"
来源链接: "https://developers.openai.com/api/docs/guides/image-prompting"
镜像: ""
作者: "OpenAI（官方文档）"
发布日期: "未知（页面未标注）"
热度: "未知（来源无公开互动数据）"
许可: "official-docs; copyright-retained (OpenAI); quoted with attribution"
原文类型: "文本"
核对状态: "verified"
核对说明: "与 2026-09-30 抓取的官方页面逐字一致（脚本比对）"
完整性: "完整"
备注: "官方说明：复用上一条生成的角色图，并重复外观约束。"
技巧钩子: ""
触发场景: ""
```

```text
Continue the children’s book story using the same character.

Scene:
The same young forest hero is gently helping a frightened squirrel
out of a fallen tree after a winter storm.
The character kneels beside the squirrel, offering reassurance.

Character Consistency:
- Same green hooded tunic
- Same facial features, proportions, and color palette
- Same gentle, heroic personality

Style:
Children’s book watercolor illustration,
soft lighting, snowy forest environment,
warm and comforting mood.

Constraints:
- Do not redesign the character
- No text
- No watermarks
```

## 总结（非原文）

- 条目数：9（`text` 围栏逐字原文）
- 语言：en 9
- 核对状态：verified 9
- 使用提醒：官方示例只说明写法，参数（画幅、分辨率、首尾帧字段）以对应厂商文档为准；各模型限制对照见 `docs/首尾帧工作流.md` 第 9 节。
