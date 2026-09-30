# 提示词索引（INDEX）

> 本文件由 `scripts/build_index.py` 从 `prompts/` 与 `cases/` 自动生成，请勿手改。AI 检索请用同目录的 `index.jsonl`（每行一条，含完整原文与全部元数据；`条目类型` 为 prompt / case / reference）。
> 每行格式：标题（链接到条目）— 适用模型 · 语言 · 核对状态 · 标签。

## 技巧锦囊（1）

> 想不到要问、但能给人新思路的技巧（力场融合特效、一镜到底打斗、混合风格等），供主动浏览；可交叉收录其他分类的条目。每行：标题 — 技巧钩子（触发场景）· 主分类。

- [AI 打斗别乱剪：用好一镜到底](prompts/打斗运镜/34-douyin-baolaoshi-one-take-fight.md) — AI 打斗少剪反而更燃：一条 10 秒长镜头里用手持跟拍、环境挨打、人数压迫撑起燃感（AI 打斗片段剪得碎、没有临场感，或多段拼接后动作接不上时）· 主分类：打斗运镜

## 统计

| 分类 | 说明 | 提示词条目 | 对照样例（cases/） |
|------|------|-----------:|-------------------:|
| [技巧锦囊](prompts/技巧锦囊/) | 想不到要问、但能给人新思路的技巧（力场融合特效、一镜到底打斗、混合风格等），供主动浏览；可交叉收录其他分类的条目 | 0（另有交叉收录 1 条） | 0 |
| [打斗运镜](prompts/打斗运镜/) | 打斗、武戏、动作编排与配套运镜（含发力链、打击感方法） | 57 | 6 |
| [运镜](prompts/运镜/) | 以摄影机运动、镜头调度为主要看点的提示词与运镜词典、景别方法 | 58 | 3 |
| [特效](prompts/特效/) | 技能特效、魔法、能量、粒子、破坏等视觉特效 | 14 | 4 |
| [国风古装](prompts/国风古装/) | 国风、古装、武侠、仙侠题材（含 3D 国漫质感） | 21 | 2 |
| [电影大场面](prompts/电影大场面/) | 电影感大场面、史诗、灾难、怪物、战争等 | 14 | 2 |
| [动画电影感](prompts/动画电影感/) | 动画 / 动漫 / 手绘 / 3D 动画电影风格 | 11 | 0 |
| [真人漫剧](prompts/真人漫剧/) | 真人漫剧（真人演绎的漫画式短剧） | 8 | 0 |
| [短剧](prompts/短剧/) | 剧情短剧、偶像剧、情景剧 | 6 | 0 |
| [超现实喜剧](prompts/超现实喜剧/) | 超现实、荒诞、搞笑 | 10 | 0 |
| [恐怖](prompts/恐怖/) | 恐怖、惊悚、悬疑 | 3 | 0 |
| [变形转换](prompts/变形转换/) | 变身、换装、形态转换、无缝转场 | 3 | 0 |
| [产品生活](prompts/产品生活/) | 产品广告、商业片、生活方式 | 19 | 0 |
| [UGC短视频](prompts/UGC短视频/) | UGC、自拍 Vlog、手机拍摄感短视频 | 11 | 0 |
| [游戏PV](prompts/游戏PV/) | 游戏宣传片、格斗游戏序列 | 2 | 0 |
| [人物卡](prompts/人物卡/) | 人物设定图、三视图、表情包等角色资产图（生图） | 11 | 0 |
| [生图修画质](prompts/生图修画质/) | 图片降噪、画质修复、干净出图（生图） | 11 | 0 |
| [提示词写法](prompts/提示词写法/) | 提示词写法方法论、公式与官方示例 | 11 | 0 |
| **合计** | | **270** | **17** |

核对状态：verified 239、verified-with-fix 24、source-unreachable 6、source-contradicts 1

## 打斗运镜（57）

打斗、武戏、动作编排与配套运镜（含发力链、打击感方法）

### `prompts/打斗运镜/01-lansenai-x.md`

- [文成百丈瀑 · 12 秒一镜到底武侠](prompts/打斗运镜/01-lansenai-x.md#post-5) — 未指定（通用写法） · zh · verified · 时间码分段、分镜/多镜头、一镜到底、竖屏9:16、武侠/仙侠、古风　`fight-camera--01-lansenai-x--01`
- [LANSEN 角色登场片头 · 15 秒 13 切镜](prompts/打斗运镜/01-lansenai-x.md#post-6) — 未指定（通用写法） · zh · verified · 时间码分段、分镜/多镜头、参考图/素材引用、音频/音效、负面约束、横屏16:9、古风、打斗、慢动作/变速、动画风格、产品/广告　`fight-camera--01-lansenai-x--02`
- [水墨烟雾艺术片头 · 15 秒一镜到底](prompts/打斗运镜/01-lansenai-x.md#post-7) — 未指定（通用写法） · zh · verified · 时间码分段、一镜到底、参考图/素材引用、负面约束　`fight-camera--01-lansenai-x--03`

### `prompts/打斗运镜/02-web-fight-camera-prompts.md`

- [石质院落 30s 硬派近身武侠肉搏（完整）](prompts/打斗运镜/02-web-fight-camera-prompts.md#11-石质院落-30s-硬派近身武侠肉搏完整) — 未指定（通用写法） · zh · verified · 分镜/多镜头、负面约束、武侠/仙侠、古风、打斗、慢动作/变速、手持、航拍/FPV　`fight-camera--02-web-fight-camera-prompts--01`
- [Boss 对决首帧（英文，@lansenai 分享）](prompts/打斗运镜/02-web-fight-camera-prompts.md#12-boss-showdown-first-frame-en-shared-by-lansenai) — Midjourney（正文提及） · en · verified · 横屏16:9、打斗　`fight-camera--02-web-fight-camera-prompts--02`
- [武士一刀横斩](prompts/打斗运镜/02-web-fight-camera-prompts.md#21-武士一刀横斩) — Kling / PixVerse / Runway / Veo（来源标注） · en · verified · 打斗、动画风格　`fight-camera--02-web-fight-camera-prompts--03`
- [双刃回旋一周](prompts/打斗运镜/02-web-fight-camera-prompts.md#22-双刃回旋一周) — Kling / PixVerse / Runway / Veo（来源标注） · en · verified · 打斗、动画风格　`fight-camera--02-web-fight-camera-prompts--04`
- [拳震尘环](prompts/打斗运镜/02-web-fight-camera-prompts.md#23-拳震尘环) — Kling / PixVerse / Runway / Veo（来源标注） · en · verified · 打斗、动画风格　`fight-camera--02-web-fight-camera-prompts--05`
- [屋顶飞跃追逐](prompts/打斗运镜/02-web-fight-camera-prompts.md#24-屋顶飞跃追逐) — Kling / PixVerse / Runway / Veo（来源标注） · en · verified · 动画风格　`fight-camera--02-web-fight-camera-prompts--06`
- [摩托穿巷追逐](prompts/打斗运镜/02-web-fight-camera-prompts.md#25-摩托穿巷追逐) — Kling / PixVerse / Runway / Veo（来源标注） · en · verified · 动画风格　`fight-camera--02-web-fight-camera-prompts--07`
- [雨夜小巷对决](prompts/打斗运镜/02-web-fight-camera-prompts.md#26-雨夜小巷对决) — Kling / PixVerse / Runway / Veo（来源标注） · en · verified · 打斗、动画风格　`fight-camera--02-web-fight-camera-prompts--08`
- [高空拔刀](prompts/打斗运镜/02-web-fight-camera-prompts.md#27-高空拔刀) — Kling / PixVerse / Runway / Veo（来源标注） · en · verified · 竖屏9:16、动画风格　`fight-camera--02-web-fight-camera-prompts--09`
- [龙骑与骑士空中错身](prompts/打斗运镜/02-web-fight-camera-prompts.md#28-龙骑与骑士空中错身) — Kling / PixVerse / Runway / Veo（来源标注） · en · verified · 动画风格　`fight-camera--02-web-fight-camera-prompts--10`

### `prompts/打斗运镜/10-hf-seedance-fight-camera.md`

- [暴雪狼袭手绘动画](prompts/打斗运镜/10-hf-seedance-fight-camera.md#1-暴雪狼袭手绘动画brutal-wolf-chase-hand-painted-animation) — Seedance 2.0 · en · verified · 音频/音效、负面约束、手持、动画风格、stop-motion、wolf-attack、hand-painted　`fight-camera--10-hf-seedance-fight-camera--01`
- [仙侠师姐定力挑战](prompts/打斗运镜/10-hf-seedance-fight-camera.md#2-仙侠师姐定力挑战xianxia-sisters-stoic-challenge-scene) — Seedance 2.0（HF 数据集标注） · zh · verified-with-fix · 时间码分段、参考图/素材引用、台词/对白、音频/音效、负面约束、横屏16:9、武侠/仙侠、古风、打斗、xianxia、comedy、cinematic　`fight-camera--10-hf-seedance-fight-camera--02`
- [水上障碍竞技](prompts/打斗运镜/10-hf-seedance-fight-camera.md#3-水上障碍竞技japanese-water-obstacle-course-challenge) — Seedance 2.5（作者帖文注明；HF 数据集标注为 2.0） · zh · verified-with-fix · 时间码分段、参考图/素材引用、音频/音效、横屏16:9、water-obstacle、japanese-tv、live-broadcast　`fight-camera--10-hf-seedance-fight-camera--03`
- [珀尔修斯斩蛇妖](prompts/打斗运镜/10-hf-seedance-fight-camera.md#4-珀尔修斯斩蛇妖perseus-slays-medusa-dark-epic) — Seedance 2.0 · en · verified · 时间码分段、负面约束、打斗、慢动作/变速、手持、GreekMyth、DarkEpic、Cinematic　`fight-camera--10-hf-seedance-fight-camera--04`
- [仙侠姐妹抬价记](prompts/打斗运镜/10-hf-seedance-fight-camera.md#5-仙侠姐妹抬价记wuxia-sisters-hilarious-price-negotiation) — Seedance 2.0（HF 数据集标注） · zh · verified · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、负面约束、横屏16:9、武侠/仙侠、古风、打斗、wuxia、comedy、seedance　`fight-camera--10-hf-seedance-fight-camera--05`
- [白鹤认米不认琴](prompts/打斗运镜/10-hf-seedance-fight-camera.md#6-白鹤认米不认琴cranes-prefer-rice-over-qin-music) — Seedance 2.0（HF 数据集标注） · zh · verified-with-fix · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、音频/音效、负面约束、横屏16:9、武侠/仙侠、古风、wuxia comedy、crane twist、cinematic　`fight-camera--10-hf-seedance-fight-camera--06`
- [仙侠推差事喜剧](prompts/打斗运镜/10-hf-seedance-fight-camera.md#7-仙侠推差事喜剧sect-duty-deadpan-comedy) — Seedance 2.0 · zh · verified · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、负面约束、横屏16:9、武侠/仙侠、古风、打斗、xianxia、deadpan、wuxia　`fight-camera--10-hf-seedance-fight-camera--07`
- [仙侠剑影对决](prompts/打斗运镜/10-hf-seedance-fight-camera.md#8-仙侠剑影对决cinematic-xianxia-sword-duel) — Seedance 2.0（HF 数据集标注） · zh · verified · 时间码分段、参考图/素材引用、台词/对白、音频/音效、负面约束、横屏16:9、武侠/仙侠、古风、打斗、手持、动画风格、xianxia、martial-arts、cinematic　`fight-camera--10-hf-seedance-fight-camera--08`
- [剑仙闯红灯被罚](prompts/打斗运镜/10-hf-seedance-fight-camera.md#9-剑仙闯红灯被罚xianxia-sword-rider-caught-running-red-light) — Seedance 2.0（HF 数据集标注） · zh · verified · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、音频/音效、负面约束、横屏16:9、武侠/仙侠、xianxia comedy、traffic violation、plot twist　`fight-camera--10-hf-seedance-fight-camera--09`
- [血色黄昏 · 骑兵冲锋](prompts/打斗运镜/10-hf-seedance-fight-camera.md#10-血色黄昏--骑兵冲锋blood-dusk-cavalry-charge) — Seedance 2.0 · en · verified · 时间码分段、一镜到底、音频/音效、横屏16:9、打斗、慢动作/变速、手持、动画风格、battlefield、onershot、fantasy　`fight-camera--10-hf-seedance-fight-camera--10`
- [韩校女打戏](prompts/打斗运镜/10-hf-seedance-fight-camera.md#11-韩校女打戏korean-school-fight-one-shot) — Seedance 2.0 · en · verified-with-fix · 时间码分段、一镜到底、参考图/素材引用、音频/音效、打斗、慢动作/变速、手持、korean-action、classroom-fight、one-shot　`fight-camera--10-hf-seedance-fight-camera--11`

### `prompts/打斗运镜/20-web-fight-camera-prompts.md`

- [多镜头动漫打斗编排（CreateVision）](prompts/打斗运镜/20-web-fight-camera-prompts.md#1-多镜头动漫打斗编排createvisioncreatevision-multi-shot-anime-fight-choreography) — Seedance（来源标注） · en · verified · 时间码分段、分镜/多镜头、参考图/素材引用、打斗、动画风格　`fight-camera--20-web-fight-camera-prompts--01`
- [30 秒雨夜地铁近身肉搏（apimodels，作者发布）](prompts/打斗运镜/20-web-fight-camera-prompts.md#2-30-秒雨夜地铁近身肉搏apimodels作者发布apimodels--30s-rain-metro-hand-to-hand-author-published) — Seedance 2.5（来源标注） · zh · verified-with-fix · 一镜到底、参考图/素材引用、台词/对白、音频/音效、负面约束、横屏16:9、武侠/仙侠、打斗、慢动作/变速　`fight-camera--20-web-fight-camera-prompts--02`
- [一镜到底天台武打 · 短版（Seedance.tv）](prompts/打斗运镜/20-web-fight-camera-prompts.md#3-一镜到底天台武打--短版seedancetvseedancetv--one-take-rooftop-martial-arts-short) — Seedance 2.5（来源标注） · en · verified · 打斗　`fight-camera--20-web-fight-camera-prompts--03`
- [分时段天台打斗 · 完整版（Seedance.tv）](prompts/打斗运镜/20-web-fight-camera-prompts.md#4-分时段天台打斗--完整版seedancetvseedancetv--copy-ready-timed-rooftop-fight-full) — Seedance 2.5（来源标注） · en · verified · 时间码分段、台词/对白、横屏16:9、打斗　`fight-camera--20-web-fight-camera-prompts--04`
- [电影感剑术对决（Seedance.tv）](prompts/打斗运镜/20-web-fight-camera-prompts.md#5-电影感剑术对决seedancetvseedancetv--cinematic-sword-duel) — Seedance 2.5（来源标注） · en · verified · 打斗　`fight-camera--20-web-fight-camera-prompts--05`
- [风格化奇幻战斗（Seedance.tv）](prompts/打斗运镜/20-web-fight-camera-prompts.md#6-风格化奇幻战斗seedancetvseedancetv--stylized-fantasy-battle) — Seedance 2.5（来源标注） · en · verified · —　`fight-camera--20-web-fight-camera-prompts--06`

### `prompts/打斗运镜/30-createvision.ai-2.md`

- [HBO 质感 · 忍者对战鬼（CreateVision）](prompts/打斗运镜/30-createvision.ai-2.md#1-hbo-质感--忍者对战鬼createvisioncreatevision-hbo-ninja-vs-oni) — Seedance（来源标注） · en · verified · 参考图/素材引用、负面约束、打斗、动画风格　`fight-camera--30-createvision.ai-2--01`

### `prompts/打斗运镜/30-freyavideo.com-1.md`

- [空中战场浪人斩击](prompts/打斗运镜/30-freyavideo.com-1.md#1-空中战场浪人斩击) — Seedance 2.0（来源标注） · zh · verified · 手持　`fight-camera--30-freyavideo.com-1--01`
- [东京雨夜机甲大战](prompts/打斗运镜/30-freyavideo.com-1.md#2-东京雨夜机甲大战) — Seedance 2.0（来源标注） · zh · verified · —　`fight-camera--30-freyavideo.com-1--02`
- [呼吸法真人决战](prompts/打斗运镜/30-freyavideo.com-1.md#3-呼吸法真人决战) — Seedance 2.0（来源标注） · zh · verified · 打斗　`fight-camera--30-freyavideo.com-1--03`

### `prompts/打斗运镜/30-github.com-3.md`

- [水獭机甲 vs 章鱼](prompts/打斗运镜/30-github.com-3.md#1-水獭机甲-vs-章鱼) — Seedance 2.0（来源标注） · zh · verified · —　`fight-camera--30-github.com-3--01`

### `prompts/打斗运镜/31-atlabs.ai.md`

- [雨夜屋顶追逐](prompts/打斗运镜/31-atlabs.ai.md#1-雨夜屋顶追逐rooftop-chase) — Kling 3.0（来源标注） · en · verified · 时间码分段、分镜/多镜头、音频/音效、慢动作/变速、手持　`fight-camera--31-atlabs.ai--01`
- [雨巷拳斗](prompts/打斗运镜/31-atlabs.ai.md#2-雨巷拳斗fist-fight-in-the-rain) — Kling 3.0（来源标注） · en · verified · 时间码分段、分镜/多镜头、音频/音效、打斗、慢动作/变速、手持　`fight-camera--31-atlabs.ai--02`

### `prompts/打斗运镜/32-douyin-kongming-weapon-fight.md`

- [枪刺](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#枪刺) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · 古风、手持　`fight-camera--32-douyin-kongming-weapon-fight--01`
- [枪挑](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#枪挑) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--02`
- [枪扫](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#枪扫) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--03`
- [架枪格挡](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#架枪格挡) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--04`
- [剑刺](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#剑刺) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--05`
- [剑撩](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#剑撩) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--06`
- [剑斩](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#剑斩) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--07`
- [格剑](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#格剑) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · 手持　`fight-camera--32-douyin-kongming-weapon-fight--08`
- [）一剑开天门](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#1一剑开天门) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--09`
- [）万剑归宗](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#2万剑归宗) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--10`
- [）引雷剑](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#3引雷剑) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--11`
- [）太极剑](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#4太极剑) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--12`
- [断岳斩 — 势如山崩，一刀斩山岳](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#1-断岳斩--势如山崩一刀斩山岳) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · 古风　`fight-camera--32-douyin-kongming-weapon-fight--13`
- [追魂劈 — 刀光如追魂夺命，势不可挡](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#2-追魂劈--刀光如追魂夺命势不可挡) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · 古风、打斗　`fight-camera--32-douyin-kongming-weapon-fight--14`
- [旋龙卷 — 刀随身转，龙卷风生](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#3-旋龙卷--刀随身转龙卷风生) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · 古风　`fight-camera--32-douyin-kongming-weapon-fight--15`
- [绝影斩 — 快如闪电，一击必杀](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#4-绝影斩--快如闪电一击必杀) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · 古风、打斗　`fight-camera--32-douyin-kongming-weapon-fight--16`
- [劈棍（原图无编号）](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#劈棍原图无编号) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--17`
- [扫棍](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#2扫棍) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--18`
- [戳棍](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#3戳棍) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--19`
- [格挡](prompts/打斗运镜/32-douyin-kongming-weapon-fight.md#4格挡) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`fight-camera--32-douyin-kongming-weapon-fight--20`

## 运镜（58）

以摄影机运动、镜头调度为主要看点的提示词与运镜词典、景别方法

### `prompts/运镜/10-hf-seedance-camera-motion.md`

- [雪原幼女狼嚎惊魂](prompts/运镜/10-hf-seedance-camera-motion.md#1-雪原幼女狼嚎惊魂toddler-trapped-in-whiteout-terror) — Seedance 2.0 · en · verified · 一镜到底、台词/对白、音频/音效、负面约束、竖屏9:16、手持、动画风格、hand-drawn animation、survival horror、atmospheric thriller　`camera-motion--10-hf-seedance-camera-motion--01`
- [闪光灯恶作剧](prompts/运镜/10-hf-seedance-camera-motion.md#2-闪光灯恶作剧flash-prank-on-friend) — Seedance 2.0 · en · verified · 时间码分段、参考图/素材引用、音频/音效、负面约束、手持、产品/广告、candid、night flash、friend prank　`camera-motion--10-hf-seedance-camera-motion--02`
- [球场惊魂悬念](prompts/运镜/10-hf-seedance-camera-motion.md#3-球场惊魂悬念stadium-thriller-cliffhanger-scene) — Seedance 2.0 · en · verified · 时间码分段、台词/对白、音频/音效、打斗、手持、产品/广告、football thriller、cinematic prompt、suspense drama　`camera-motion--10-hf-seedance-camera-motion--03`
- [高管决断时刻](prompts/运镜/10-hf-seedance-camera-motion.md#4-高管决断时刻executives-decisive-move) — Seedance 2.0 · en · verified-with-fix · 时间码分段、台词/对白、负面约束、手持、corporate、cinematic、decision　`camera-motion--10-hf-seedance-camera-motion--04`
- [极限巨浪冲浪](prompts/运镜/10-hf-seedance-camera-motion.md#5-极限巨浪冲浪cinematic-barrel-surfing-masterpiece) — Seedance 2.0 · en · verified · 时间码分段、参考图/素材引用、负面约束、慢动作/变速、产品/广告、surfing、cinematic、barrel　`camera-motion--10-hf-seedance-camera-motion--05`
- [广场足球传情](prompts/运镜/10-hf-seedance-camera-motion.md#6-广场足球传情one-ball-unites-a-city-square) — Seedance 2.0 · en · verified · 时间码分段、一镜到底、负面约束、慢动作/变速、手持、航拍/FPV、动画风格、street football、one-take、human connection　`camera-motion--10-hf-seedance-camera-motion--06`
- [HAJAR电蚊拍炫灭之夜](prompts/运镜/10-hf-seedance-camera-motion.md#7-hajar电蚊拍炫灭之夜hajar-racket-midnight-strike) — Seedance 2.0 · en · verified · 时间码分段、分镜/多镜头、负面约束、慢动作/变速、产品/广告、electric racket、brand commercial、premium product　`camera-motion--10-hf-seedance-camera-motion--07`
- [深夜厨房情感对峙](prompts/运镜/10-hf-seedance-camera-motion.md#8-深夜厨房情感对峙emotional-confrontation-in-a-dim-kitchen) — Seedance 2.0 · en · verified · 参考图/素材引用、台词/对白、负面约束、手持、Cinematic、Emotional、Realism　`camera-motion--10-hf-seedance-camera-motion--08`

### `prompts/运镜/20-web-camera-motion-prompts.md`

- [30 秒一镜到底 · 东京巨人与武士（apimodels）](prompts/运镜/20-web-camera-motion-prompts.md#1-30-秒一镜到底--东京巨人与武士apimodelsapimodels--30s-unbroken-one-shot-tokyo-titansamurai) — Seedance 2.5（来源标注） · en · verified · 竖屏9:16、横屏16:9、手持、航拍/FPV　`camera-motion--20-web-camera-motion-prompts--01`

### `prompts/运镜/30-anikuku.com-2.md`

- [图生视频 转身望窗](prompts/运镜/30-anikuku.com-2.md#1-图生视频-转身望窗) — Seedance 2.0（来源标注） · zh · verified · 参考图/素材引用　`camera-motion--30-anikuku.com-2--01`
- [多镜头 隧道骑手三节拍](prompts/运镜/30-anikuku.com-2.md#2-多镜头-隧道骑手三节拍) — Seedance 2.0（来源标注） · zh · verified · 时间码分段　`camera-motion--30-anikuku.com-2--02`
- [匹配剪辑 黑胶到环岛](prompts/运镜/30-anikuku.com-2.md#3-匹配剪辑-黑胶到环岛) — Seedance 2.0（来源标注） · zh · verified · 横屏16:9、航拍/FPV　`camera-motion--30-anikuku.com-2--03`

### `prompts/运镜/30-freyavideo.com-1.md`

- [悬崖城市飞车追逐](prompts/运镜/30-freyavideo.com-1.md#1-悬崖城市飞车追逐) — Seedance 2.0（来源标注） · zh · verified · —　`camera-motion--30-freyavideo.com-1--01`
- [疯狂驾驶卡通分镜](prompts/运镜/30-freyavideo.com-1.md#2-疯狂驾驶卡通分镜) — Seedance 2.0（来源标注） · zh · verified · 音频/音效　`camera-motion--30-freyavideo.com-1--02`

### `prompts/运镜/31-atlabs.ai.md`

- [空间站走廊](prompts/运镜/31-atlabs.ai.md#1-空间站走廊space-station-corridor) — Kling 3.0（来源标注） · en · verified · 音频/音效　`camera-motion--31-atlabs.ai--01`

### `prompts/运镜/31-kling.ai.md`

- [大理石雕像推镜](prompts/运镜/31-kling.ai.md#1-大理石雕像推镜marble-statue-dolly-in) — Kling（官方博客） · en · verified · —　`camera-motion--31-kling.ai--01`
- [赛博女飞行员多镜](prompts/运镜/31-kling.ai.md#2-赛博女飞行员多镜cyberpunk-pilot-multi-shot) — Kling（官方博客） · en · verified · 分镜/多镜头　`camera-motion--31-kling.ai--02`

### `prompts/运镜/31-memons.ai.md`

- [霓虹雨巷推进](prompts/运镜/31-memons.ai.md#1-霓虹雨巷推进neon-rain-soaked-alley) — PixVerse（来源标注） · en · verified · 横屏16:9　`camera-motion--31-memons.ai--01`

### `prompts/运镜/31-runway.com.md`

- [脏蓝气球巷道跟踪](prompts/运镜/31-runway.com.md#1-脏蓝气球巷道跟踪dirty-blue-balloon-alley) — Runway Gen-3 Alpha（已于 2026-07-08 下线） · en · verified · 手持　`camera-motion--31-runway.com--01`

### `prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md`

- [先判断你正在控制哪一层](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#一先判断你正在控制哪一层) — 未指定（原文为通用 AI 视频提示词） · zh · verified · 手持　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--01`
- [手持镜头](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#1-手持镜头) — 未指定（原文为通用 AI 视频提示词） · zh · verified · 手持　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--02`
- [稳定器跟拍](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#2-稳定器跟拍) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--03`
- [摇臂与吊臂运镜](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#3-摇臂与吊臂运镜) — 未指定（原文为通用 AI 视频提示词） · zh · verified · 航拍/FPV　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--04`
- [航拍与无人机运镜](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#4-航拍与无人机运镜) — 未指定（原文为通用 AI 视频提示词） · zh · verified · 航拍/FPV　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--05`
- [主观镜头 POV](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#5-主观镜头-pov) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--06`
- [第一人称飞行 FPV](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#6-第一人称飞行-fpv) — 未指定（原文为通用 AI 视频提示词） · zh · verified · 航拍/FPV　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--07`
- [镜头翻滚](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#7-镜头翻滚) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--08`
- [希区柯克变焦](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#8-希区柯克变焦) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--09`
- [长镜头](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#9-长镜头) — 未指定（原文为通用 AI 视频提示词） · zh · verified · 一镜到底　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--10`
- [复杂组合运镜](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#10-复杂组合运镜) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--11`
- [复杂运镜要写成“动作编排”](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#八复杂运镜要写成动作编排) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--12`
- [手持现场感模板](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#手持现场感模板) — 未指定（原文为通用 AI 视频提示词） · zh · verified · 手持　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--13`
- [稳定器连续跟拍模板](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#稳定器连续跟拍模板) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--14`
- [FPV 路线模板](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#fpv-路线模板) — 未指定（原文为通用 AI 视频提示词） · zh · verified · 航拍/FPV　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--15`
- [希区柯克变焦模板](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#希区柯克变焦模板) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--16`
- [长镜头与组合运镜模板](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#长镜头与组合运镜模板) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--17`
- [一条最快的选择路径](prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md#一条最快的选择路径) — 未指定（原文为通用 AI 视频提示词） · zh · verified · 一镜到底、手持　`camera-motion--41-x-adrianpunk115-camera-dictionary-part2--18`

### `prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md`

- [AI 视频提示词的六层结构](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#二ai-视频提示词的六层结构) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--01`
- [固定镜头](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#1-固定镜头) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--02`
- [摇摄](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#2-摇摄) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--03`
- [甩镜](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#3-甩镜) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--04`
- [俯仰](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#4-俯仰) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--05`
- [变焦](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#5-变焦) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--06`
- [移焦](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#6-移焦) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--07`
- [推近](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#7-推近) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--08`
- [拉远](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#8-拉远) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--09`
- [横移](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#9-横移) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--10`
- [升降](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#10-升降) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--11`
- [跟拍](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#11-跟拍) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--12`
- [环绕运镜](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#12-环绕运镜) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--13`
- [把一个运镜词写成可执行指令](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#六把一个运镜词写成可执行指令) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--14`
- [单一运镜模板](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#单一运镜模板) — 未指定（原文为通用 AI 视频提示词） · zh · verified · 手持　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--15`
- [固定主体大小的跟拍模板](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#固定主体大小的跟拍模板) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--16`
- [揭示信息的运镜模板](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#揭示信息的运镜模板) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--17`
- [同一个场景，换一种情绪就换一种运镜](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#3-同一个场景换一种情绪就换一种运镜) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--18`
- [同一个场景，换一种情绪就换一种运镜（2）](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#3-同一个场景换一种情绪就换一种运镜) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--19`
- [同一个场景，换一种情绪就换一种运镜（3）](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#3-同一个场景换一种情绪就换一种运镜) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--20`
- [同一个场景，换一种情绪就换一种运镜（4）](prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md#3-同一个场景换一种情绪就换一种运镜) — 未指定（原文为通用 AI 视频提示词） · zh · verified · —　`camera-motion--42-x-adrianpunk115-camera-dictionary-part1--21`

## 特效（14）

技能特效、魔法、能量、粒子、破坏等视觉特效

### `prompts/特效/10-hf-seedance-vfx.md`

- [街头极速狂飙](prompts/特效/10-hf-seedance-vfx.md#1-街头极速狂飙night-street-racing-cinematic-sequence) — Seedance 2.0 · en · verified · 时间码分段、慢动作/变速、street racing、night driving、cinematic　`vfx--10-hf-seedance-vfx--01`
- [高山龙女温情时刻](prompts/特效/10-hf-seedance-vfx.md#2-高山龙女温情时刻cinematic-dragon-bond-on-alpine-peak) — Seedance 2.0 / GPT Image 2 · en · verified · 负面约束、竖屏9:16、横屏16:9、打斗、手持、动画风格、cinematic、dragon、photorealistic　`vfx--10-hf-seedance-vfx--02`
- [奢华电影时尚建筑片](prompts/特效/10-hf-seedance-vfx.md#3-奢华电影时尚建筑片luxury-cinematic-fashion-construction) — Seedance 2.0 / GPT Image 2 · en · verified-with-fix · 时间码分段、慢动作/变速、航拍/FPV、产品/广告、luxury fashion、cinematic architecture、material transformation　`vfx--10-hf-seedance-vfx--03`
- [狼影救婴](prompts/特效/10-hf-seedance-vfx.md#4-狼影救婴wolf-saves-child-in-stop-motion-cliff-disaster) — Seedance 2.0 · en · verified-with-fix · 参考图/素材引用、音频/音效、负面约束、竖屏9:16、打斗、手持、动画风格、stop-motion、hand-painted animation、dramatic rescue　`vfx--10-hf-seedance-vfx--04`
- [霓虹赛博朋克拥抱](prompts/特效/10-hf-seedance-vfx.md#5-霓虹赛博朋克拥抱neon-cyberpunk-embrace) — Seedance 2.0 · en · verified · 分镜/多镜头、音频/音效、竖屏9:16、cyberpunk、sci-fi romance、mecha flight　`vfx--10-hf-seedance-vfx--05`
- [奇幻糖果工坊](prompts/特效/10-hf-seedance-vfx.md#6-奇幻糖果工坊magical-candy-workshop-adventure) — Seedance 2.0 · en · verified · 横屏16:9、慢动作/变速、航拍/FPV、动画风格、fantasy animation、magical workshop、pixar style　`vfx--10-hf-seedance-vfx--06`
- [外星飞虫来袭 · POV 变速](prompts/特效/10-hf-seedance-vfx.md#7-外星飞虫来袭--pov-变速alien-fly-attack-pov-speed-ramp) — Seedance 2.0 · en · verified · 时间码分段、一镜到底、横屏16:9、慢动作/变速、first-person POV、macro cinematography、sci-fi forest　`vfx--10-hf-seedance-vfx--07`
- [清冷女主喷火生日](prompts/特效/10-hf-seedance-vfx.md#8-清冷女主喷火生日cool-girls-fire-breathing-birthday-surprise) — Seedance 2.0 · zh · verified-with-fix · 分镜/多镜头、参考图/素材引用、台词/对白、音频/音效、负面约束、竖屏9:16、cinematic、birthday、surprise　`vfx--10-hf-seedance-vfx--08`
- [魔法画室自动绘画](prompts/特效/10-hf-seedance-vfx.md#9-魔法画室自动绘画magical-autonomous-painting-time-lapse) — Seedance 2.0 · en · verified · 时间码分段、参考图/素材引用、time-lapse、painting、magic　`vfx--10-hf-seedance-vfx--09`

### `prompts/特效/30-freyavideo.com.md`

- [动漫《法天象地》特效](prompts/特效/30-freyavideo.com.md#1-动漫法天象地特效) — Seedance 2.0（来源标注） · zh · verified · 时间码分段　`vfx--30-freyavideo.com--01`

### `prompts/特效/31-memons.ai.md`

- [爆炸背影离开](prompts/特效/31-memons.ai.md#1-爆炸背影离开explosion-walk-away-shot) — PixVerse（来源标注） · en · verified · 横屏16:9、慢动作/变速　`vfx--31-memons.ai--01`
- [赛璐璐机甲升空](prompts/特效/31-memons.ai.md#2-赛璐璐机甲升空cel-shaded-mech-launch) — PixVerse（来源标注） · en · verified · 横屏16:9、动画风格　`vfx--31-memons.ai--02`

### `prompts/特效/40-douyin-aigc-xiaoyueer-skill-vfx.md`

- [:Emissive 自发光分层渲染（核心光效）](prompts/特效/40-douyin-aigc-xiaoyueer-skill-vfx.md#1-emissive-自发光分层渲染核心光效) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`vfx--40-douyin-aigc-xiaoyueer-skill-vfx--01`
- [:Motion Blur 运动模糊采样（动态轨迹）](prompts/特效/40-douyin-aigc-xiaoyueer-skill-vfx.md#2-motion-blur-运动模糊采样动态轨迹) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · —　`vfx--40-douyin-aigc-xiaoyueer-skill-vfx--02`

## 国风古装（21）

国风、古装、武侠、仙侠题材（含 3D 国漫质感）

### `prompts/国风古装/10-hf-seedance-guoman-3d.md`

- [剑仙师姐敲错钟](prompts/国风古装/10-hf-seedance-guoman-3d.md#1-剑仙师姐敲错钟sword-immortal-rings-wrong-bell) — Seedance 2.0（HF 数据集标注） · zh · verified-with-fix · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、音频/音效、横屏16:9、武侠/仙侠、古风、xianxia、comedy、cinematic　`guofeng--10-hf-seedance-guoman-3d--01`
- [真香郡主](prompts/国风古装/10-hf-seedance-guoman-3d.md#2-真香郡主princess-meets-her-handsome-groom) — Seedance 2.0 · zh · verified · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、古风、手持、Ancient Romance、Arranged Marriage、Love at First Sight　`guofeng--10-hf-seedance-guoman-3d--02`
- [书房秘术藏深情](prompts/国风古装/10-hf-seedance-guoman-3d.md#3-书房秘术藏深情secret-roof-repair-romance) — Seedance 2.0 · zh · verified-with-fix · 时间码分段、参考图/素材引用、台词/对白、音频/音效、竖屏9:16、古风、动画风格、costume comedy、misunderstanding、romance　`guofeng--10-hf-seedance-guoman-3d--03`
- [塔罗魔女破镜降临](prompts/国风古装/10-hf-seedance-guoman-3d.md#4-塔罗魔女破镜降临tarot-witch-shatters-mirror) — Seedance 2.0 · zh · verified · 时间码分段、动画风格、tarot、witch、mirror　`guofeng--10-hf-seedance-guoman-3d--04`

### `prompts/国风古装/11-hf-seedance-guoman-expanded.md`

- [仙城纸龙乌龙](prompts/国风古装/11-hf-seedance-guoman-expanded.md#1-仙城纸龙乌龙paper-dragon-prank-in-cloud-city) — Seedance 2.0（HF 数据集标注） · zh · verified · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、音频/音效、负面约束、横屏16:9、武侠/仙侠、古风、航拍/FPV　`guofeng--11-hf-seedance-guoman-expanded--01`
- [仙侠师姐冷面吐槽](prompts/国风古装/11-hf-seedance-guoman-expanded.md#2-仙侠师姐冷面吐槽xianxia-sisters-deadpan-ghost-prank-reaction) — Seedance 2.0（HF 数据集标注） · zh · verified-with-fix · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、音频/音效、负面约束、横屏16:9、武侠/仙侠、古风、手持　`guofeng--11-hf-seedance-guoman-expanded--02`
- [仙侠臭豆腐惊魂](prompts/国风古装/11-hf-seedance-guoman-expanded.md#3-仙侠臭豆腐惊魂sword-immortal-versus-fermented-tofu) — Seedance 2.0（HF 数据集标注） · zh · verified-with-fix · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、负面约束、横屏16:9、武侠/仙侠、古风　`guofeng--11-hf-seedance-guoman-expanded--03`
- [断云寺武侠追杀](prompts/国风古装/11-hf-seedance-guoman-expanded.md#4-断云寺武侠追杀high-octane-wuxia-chase-at-dusk) — Seedance 2.0（HF 数据集标注） · zh · verified-with-fix · 负面约束、武侠/仙侠、动画风格　`guofeng--11-hf-seedance-guoman-expanded--04`
- [师姐踏水无痕真相](prompts/国风古装/11-hf-seedance-guoman-expanded.md#5-师姐踏水无痕真相immortals-secret-stepping-stones) — Seedance 2.0 · zh · verified-with-fix · 时间码分段、分镜/多镜头、台词/对白、音频/音效、负面约束、横屏16:9、武侠/仙侠、古风　`guofeng--11-hf-seedance-guoman-expanded--05`
- [仙侠召唤神反转](prompts/国风古装/11-hf-seedance-guoman-expanded.md#6-仙侠召唤神反转xianxia-summoning-comedy-twist) — Seedance 2.0（HF 数据集标注） · zh · verified-with-fix · 时间码分段、分镜/多镜头、台词/对白、音频/音效、负面约束、横屏16:9、武侠/仙侠、古风　`guofeng--11-hf-seedance-guoman-expanded--06`
- [剑仙遇单车](prompts/国风古装/11-hf-seedance-guoman-expanded.md#7-剑仙遇单车sword-fairy-meets-bike-commuter) — Seedance 2.0（HF 数据集标注） · zh · verified-with-fix · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、音频/音效、负面约束、横屏16:9、武侠/仙侠、古风　`guofeng--11-hf-seedance-guoman-expanded--07`
- [御剑翻车现场](prompts/国风古装/11-hf-seedance-guoman-expanded.md#8-御剑翻车现场sword-immortal-epic-fail) — Seedance 2.0 · zh · verified · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、音频/音效、武侠/仙侠、打斗　`guofeng--11-hf-seedance-guoman-expanded--08`
- [剑神水墨战](prompts/国风古装/11-hf-seedance-guoman-expanded.md#9-剑神水墨战ink-sword-god) — Seedance 2.0（HF 数据集标注） · en · source-unreachable · 时间码分段、音频/音效、打斗、动画风格、产品/广告　`guofeng--11-hf-seedance-guoman-expanded--09`
- [万剑归宗切葱花](prompts/国风古装/11-hf-seedance-guoman-expanded.md#10-万剑归宗切葱花ultimate-sword-skill-chops-scallions) — Seedance 2.0（HF 数据集标注） · zh · verified · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、音频/音效、负面约束、横屏16:9、武侠/仙侠、古风　`guofeng--11-hf-seedance-guoman-expanded--10`
- [仙侠伞阵雨天翻车](prompts/国风古装/11-hf-seedance-guoman-expanded.md#11-仙侠伞阵雨天翻车xianxia-umbrella-array-rainy-fail) — Seedance 2.0（HF 数据集标注） · zh · verified-with-fix · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、音频/音效、负面约束、横屏16:9、武侠/仙侠、古风　`guofeng--11-hf-seedance-guoman-expanded--11`
- [剑仙翻车现场](prompts/国风古装/11-hf-seedance-guoman-expanded.md#12-剑仙翻车现场immortal-falls-for-truck-wind) — Seedance 2.0 · zh · verified · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、音频/音效、横屏16:9、武侠/仙侠　`guofeng--11-hf-seedance-guoman-expanded--12`
- [仙法烘干遭喷淋](prompts/国风古装/11-hf-seedance-guoman-expanded.md#13-仙法烘干遭喷淋immortal-drying-fail) — Seedance 2.0（HF 数据集标注） · zh · verified-with-fix · 时间码分段、分镜/多镜头、参考图/素材引用、台词/对白、音频/音效、负面约束、横屏16:9、武侠/仙侠、古风　`guofeng--11-hf-seedance-guoman-expanded--13`

### `prompts/国风古装/20-web-guoman-3d-prompts.md`

- [武侠动作喜剧 · 古代客栈（apimodels，作者 johnAGI168）](prompts/国风古装/20-web-guoman-3d-prompts.md#1-武侠动作喜剧--古代客栈apimodels作者-johnagi168apimodels--wuxia-action-comedy-period-inn-johnagi168) — Seedance 2.5（来源标注） · zh · verified · 时间码分段、参考图/素材引用、音频/音效、负面约束、横屏16:9、武侠/仙侠、古风、打斗、慢动作/变速、产品/广告　`guofeng--20-web-guoman-3d-prompts--01`

### `prompts/国风古装/30-freyavideo.com-1.md`

- [敦煌飞天壁画苏醒](prompts/国风古装/30-freyavideo.com-1.md#1-敦煌飞天壁画苏醒) — Seedance 2.0（来源标注） · zh · verified · —　`guofeng--30-freyavideo.com-1--01`

### `prompts/国风古装/30-github.com-2.md`

- [哪吒与敖丙冰火交锋](prompts/国风古装/30-github.com-2.md#1-哪吒与敖丙冰火交锋) — Seedance 2.0（来源标注） · zh · verified · —　`guofeng--30-github.com-2--01`

### `prompts/国风古装/31-fal.ai.md`

- [雪夜竹林武侠](prompts/国风古装/31-fal.ai.md#1-雪夜竹林武侠snowy-bamboo-wuxia-mystery) — MiniMax Hailuo H3（来源标注） · en · verified · 竖屏9:16、横屏16:9、武侠/仙侠、动画风格、产品/广告　`guofeng--31-fal.ai--01`

## 电影大场面（14）

电影感大场面、史诗、灾难、怪物、战争等

### `prompts/电影大场面/10-hf-seedance-cinematic.md`

- [夜市绑架惊魂](prompts/电影大场面/10-hf-seedance-cinematic.md#1-夜市绑架惊魂kidnapping-foiled-by-police-chase) — Seedance 2.0 · en · verified-with-fix · 时间码分段、分镜/多镜头、音频/音效、负面约束、Kidnapping、Police Chase、Drama　`cinematic--10-hf-seedance-cinematic--01`
- [世界杯绝杀瞬间](prompts/电影大场面/10-hf-seedance-cinematic.md#2-世界杯绝杀瞬间world-cup-final-winning-goal) — Seedance 2.0（HF 数据集标注） · zh · verified-with-fix · 时间码分段、分镜/多镜头、参考图/素材引用、音频/音效、竖屏9:16、动画风格、产品/广告、WorldCup、Soccer、LiveAction　`cinematic--10-hf-seedance-cinematic--02`
- [复古餐厅邂逅](prompts/电影大场面/10-hf-seedance-cinematic.md#3-复古餐厅邂逅diner-noir-a-surprise-encounter) — Seedance 2.0 / Kling · en · verified · Film Noir、1950s Diner、Cinematic　`cinematic--10-hf-seedance-cinematic--03`

### `prompts/电影大场面/30-anikuku.com-2.md`

- [角色特写 雨夜快递员](prompts/电影大场面/30-anikuku.com-2.md#1-角色特写-雨夜快递员) — Seedance 2.0（来源标注） · zh · verified · 横屏16:9　`cinematic--30-anikuku.com-2--01`

### `prompts/电影大场面/30-freyavideo.com-1.md`

- [废墟教堂时逆奏鸣](prompts/电影大场面/30-freyavideo.com-1.md#1-废墟教堂时逆奏鸣) — Seedance 2.0（来源标注） · zh · verified · 音频/音效　`cinematic--30-freyavideo.com-1--01`

### `prompts/电影大场面/30-github.com-3.md`

- [好莱坞专业赛车电影风格](prompts/电影大场面/30-github.com-3.md#1-好莱坞专业赛车电影风格) — Seedance 2.0（来源标注） · zh · verified · 时间码分段、分镜/多镜头、台词/对白　`cinematic--30-github.com-3--01`
- [丹尼斯·维伦纽瓦风格史诗沙漠](prompts/电影大场面/30-github.com-3.md#2-丹尼斯维伦纽瓦风格史诗沙漠) — Seedance 2.0（来源标注） · zh · verified · 时间码分段、慢动作/变速　`cinematic--30-github.com-3--02`
- [王家卫雨夜电话亭](prompts/电影大场面/30-github.com-3.md#3-王家卫雨夜电话亭) — Seedance 2.0（来源标注） · zh · verified · 时间码分段、分镜/多镜头、台词/对白、手持、动画风格　`cinematic--30-github.com-3--03`

### `prompts/电影大场面/31-atlabs.ai.md`

- [末世独行](prompts/电影大场面/31-atlabs.ai.md#1-末世独行last-human-on-earth) — Kling 3.0（来源标注） · en · verified · 音频/音效　`cinematic--31-atlabs.ai--01`

### `prompts/电影大场面/31-runway.com.md`

- [保加利亚巷道海啸](prompts/电影大场面/31-runway.com.md#1-保加利亚巷道海啸tsunami-alley-bulgaria) — Runway Gen-3 Alpha（已于 2026-07-08 下线） · en · verified · —　`cinematic--31-runway.com--01`

### `prompts/电影大场面/32-github-beatapi-awesome-seedance-2-5.md`

- [越南神话海战](prompts/电影大场面/32-github-beatapi-awesome-seedance-2-5.md#1-越南神话海战vietnamese-mythic-sea-battle) — Seedance 2.5（来源标注） · en · verified · 分镜/多镜头、一镜到底、台词/对白、打斗、慢动作/变速　`cinematic--32-github-beatapi-awesome-seedance-2-5--01`

### `prompts/电影大场面/32-github-watreesir-awesome-kling-4.md`

- [丛林实验室怪物惊悚](prompts/电影大场面/32-github-watreesir-awesome-kling-4.md#1-丛林实验室怪物惊悚jungle-lab-creature-thriller) — Kling 4.0（仓库标注） · en · verified · 音频/音效、负面约束、打斗、手持　`cinematic--32-github-watreesir-awesome-kling-4--01`
- [变形宽银幕 · 怪物追逐](prompts/电影大场面/32-github-watreesir-awesome-kling-4.md#2-变形宽银幕--怪物追逐anamorphic-monster-chase) — Kling 4.0（仓库标注） · en · verified · 音频/音效、打斗、手持　`cinematic--32-github-watreesir-awesome-kling-4--02`

### `prompts/电影大场面/32-runway-seedance-2.0-prompt-guide.md`

- [停机坪运兵舰（8 种技法）](prompts/电影大场面/32-runway-seedance-2.0-prompt-guide.md#1-停机坪运兵舰8-种技法pad-deck-dropship-8-techniques) — Seedance 2.0（来源标注） · en · verified · —　`cinematic--32-runway-seedance-2.0-prompt-guide--01`

## 动画电影感（11）

动画 / 动漫 / 手绘 / 3D 动画电影风格

### `prompts/动画电影感/10-hf-seedance-animation.md`

- [九宫格分镜动画](prompts/动画电影感/10-hf-seedance-animation.md#1-九宫格分镜动画storyboard-panel-animation) — Seedance 2.0 · ja · verified · 分镜/多镜头、参考图/素材引用、音频/音效、storyboard、animation、panels　`animation--10-hf-seedance-animation--01`
- [动漫炸猪排盖饭](prompts/动画电影感/10-hf-seedance-animation.md#2-动漫炸猪排盖饭anime-style-katsu-don-cooking) — Seedance 2.0 · ja · verified · 参考图/素材引用、音频/音效、打斗、动画风格、AnimeFood、KatsuDon、Cooking　`animation--10-hf-seedance-animation--02`
- [粉彩黑帮海滩热舞](prompts/动画电影感/10-hf-seedance-animation.md#3-粉彩黑帮海滩热舞pastel-mob-beach-dance-party) — Seedance 2.0 · en · verified · 时间码分段、音频/音效、负面约束、动画风格、kawaii anime、group dance、beach pop　`animation--10-hf-seedance-animation--03`
- [动漫少女奢华下午茶](prompts/动画电影感/10-hf-seedance-animation.md#4-动漫少女奢华下午茶anime-girls-luxury-parfait-date) — Seedance 2.0 · en · verified · 分镜/多镜头、参考图/素材引用、负面约束、动画风格、anime、parfait、cafe　`animation--10-hf-seedance-animation--04`
- [咖啡师的绝技](prompts/动画电影感/10-hf-seedance-animation.md#5-咖啡师的绝技caffeine-chaos-machine) — Seedance 2.0（HF 数据集标注） · en · source-unreachable · 时间码分段、打斗、慢动作/变速、动画风格、Rube Goldberg、Pixar Style、Coffee Shop　`animation--10-hf-seedance-animation--05`

### `prompts/动画电影感/30-createvision.ai-1.md`

- [哥特动漫 · 跨次元列车之旅](prompts/动画电影感/30-createvision.ai-1.md#1-哥特动漫--跨次元列车之旅gothic-anime-interdimensional-train-journey) — Seedance（来源标注） · en · verified · 打斗、慢动作/变速、动画风格　`animation--30-createvision.ai-1--01`

### `prompts/动画电影感/30-github.com-2.md`

- [梵高后印象派动画](prompts/动画电影感/30-github.com-2.md#1-梵高后印象派动画) — Seedance 2.0（来源标注） · zh · verified · 动画风格　`animation--30-github.com-2--01`
- [知名动漫角色力量大会](prompts/动画电影感/30-github.com-2.md#2-知名动漫角色力量大会) — Seedance 2.0（来源标注） · zh · verified · —　`animation--30-github.com-2--02`

### `prompts/动画电影感/31-fal.ai.md`

- [黏土狐跃熔岩谷](prompts/动画电影感/31-fal.ai.md#1-黏土狐跃熔岩谷claymation-lava-canyon-leap) — MiniMax Hailuo H3（来源标注） · en · verified · 慢动作/变速　`animation--31-fal.ai--01`

### `prompts/动画电影感/31-memons.ai.md`

- [列车窗边动漫少女](prompts/动画电影感/31-memons.ai.md#1-列车窗边动漫少女anime-girl-on-a-train) — PixVerse（来源标注） · en · verified · 横屏16:9、动画风格　`animation--31-memons.ai--01`
- [赛博快递追逐](prompts/动画电影感/31-memons.ai.md#2-赛博快递追逐cyberpunk-courier-chase) — PixVerse（来源标注） · en · verified · 横屏16:9、动画风格　`animation--31-memons.ai--02`

## 真人漫剧（8）

真人漫剧（真人演绎的漫画式短剧）

### `prompts/真人漫剧/30-anikuku.com-2.md`

- [竖屏漫剧 女剑客灯笼巷](prompts/真人漫剧/30-anikuku.com-2.md#1-竖屏漫剧-女剑客灯笼巷) — Seedance 2.0（来源标注） · zh · verified · 竖屏9:16　`live-manju--30-anikuku.com-2--01`

### `prompts/真人漫剧/30-github.com-3.md`

- [AI漫剧武侠小说对齐视频1](prompts/真人漫剧/30-github.com-3.md#1-ai漫剧武侠小说对齐视频1) — Seedance 2.0（来源标注） · zh · verified · 参考图/素材引用、打斗　`live-manju--30-github.com-3--01`

### `prompts/真人漫剧/30-seedance22.com-1.md`

- [机甲变身（一镜到底）](prompts/真人漫剧/30-seedance22.com-1.md#1-机甲变身一镜到底) — Seedance 2.0（来源标注） · zh · verified · 时间码分段、一镜到底　`live-manju--30-seedance22.com-1--01`
- [古装重生（喜房醒来）](prompts/真人漫剧/30-seedance22.com-1.md#2-古装重生喜房醒来) — Seedance 2.0（来源标注） · zh · verified · 音频/音效　`live-manju--30-seedance22.com-1--02`
- [素裙绣娘 vs 暗影妖物](prompts/真人漫剧/30-seedance22.com-1.md#3-素裙绣娘-vs-暗影妖物) — Seedance 2.0（来源标注） · zh · verified · 时间码分段、音频/音效、打斗、慢动作/变速　`live-manju--30-seedance22.com-1--03`
- [暗黑特摄变身 BLACKSUN](prompts/真人漫剧/30-seedance22.com-1.md#4-暗黑特摄变身-blacksun) — Seedance 2.0（来源标注） · zh · verified · 时间码分段、一镜到底、手持　`live-manju--30-seedance22.com-1--04`
- [武侠英雄救美](prompts/真人漫剧/30-seedance22.com-1.md#5-武侠英雄救美) — Seedance 2.0（来源标注） · zh · verified · 参考图/素材引用、武侠/仙侠、古风、手持　`live-manju--30-seedance22.com-1--05`
- [古装宗门对峙](prompts/真人漫剧/30-seedance22.com-1.md#6-古装宗门对峙) — Seedance 2.0（来源标注） · zh · verified · —　`live-manju--30-seedance22.com-1--06`

## 短剧（6）

剧情短剧、偶像剧、情景剧

### `prompts/短剧/10-hf-seedance-short-drama.md`

- [偶像Pepero游戏暧昧张力](prompts/短剧/10-hf-seedance-short-drama.md#1-偶像pepero游戏暧昧张力idol-pepero-game-tension) — Seedance 2.0 · en · verified-with-fix · 分镜/多镜头、台词/对白、音频/音效、手持、动画风格、产品/广告、kpop、variety、romance　`short-drama--10-hf-seedance-short-drama--01`

### `prompts/短剧/30-anikuku.com-1.md`

- [对白 侦探餐馆卡座](prompts/短剧/30-anikuku.com-1.md#1-对白-侦探餐馆卡座) — Seedance 2.0（来源标注） · zh · verified · 台词/对白、音频/音效、横屏16:9　`short-drama--30-anikuku.com-1--01`

### `prompts/短剧/30-github.com-2.md`

- [春晚甄嬛与扈绯脱口秀](prompts/短剧/30-github.com-2.md#1-春晚甄嬛与扈绯脱口秀) — Seedance 2.0（来源标注） · zh · verified · 时间码分段、横屏16:9、古风　`short-drama--30-github.com-2--01`
- [中国短剧雨夜情感戏](prompts/短剧/30-github.com-2.md#2-中国短剧雨夜情感戏) — Seedance 2.0（来源标注） · zh · verified · 时间码分段、分镜/多镜头　`short-drama--30-github.com-2--02`
- [豪门恩怨真假千金](prompts/短剧/30-github.com-2.md#3-豪门恩怨真假千金) — Seedance 2.0（来源标注） · zh · verified · 时间码分段、台词/对白、竖屏9:16　`short-drama--30-github.com-2--03`

### `prompts/短剧/31-atlabs.ai.md`

- [审讯室对峙](prompts/短剧/31-atlabs.ai.md#1-审讯室对峙the-interrogation-room) — Kling 3.0（来源标注） · en · verified · 音频/音效　`short-drama--31-atlabs.ai--01`

## 超现实喜剧（10）

超现实、荒诞、搞笑

### `prompts/超现实喜剧/10-hf-seedance-surreal-comedy.md`

- [橘猫CEO的董事会危机](prompts/超现实喜剧/10-hf-seedance-surreal-comedy.md#1-橘猫ceo的董事会危机tabby-ceos-boardroom-crisis) — Seedance 2.0 / GPT Image 2 · en · verified · 时间码分段、台词/对白、音频/音效、负面约束、cat ceo、corporate comedy、prestige drama　`surreal-comedy--10-hf-seedance-surreal-comedy--01`
- [黑裙女子踏碎沙堡](prompts/超现实喜剧/10-hf-seedance-surreal-comedy.md#2-黑裙女子踏碎沙堡gothic-woman-crushes-sandcastle) — Seedance 2.0 · en · verified · 一镜到底、负面约束、打斗、beach、gothic、surreal　`surreal-comedy--10-hf-seedance-surreal-comedy--02`
- [小饭馆慵懒老板娘](prompts/超现实喜剧/10-hf-seedance-surreal-comedy.md#3-小饭馆慵懒老板娘lazy-boss-lady-diner-comedy) — Seedance 2.0 · zh · verified · 分镜/多镜头、参考图/素材引用、台词/对白、音频/音效、负面约束、竖屏9:16、慢动作/变速、手持、diner、boss lady、comedy　`surreal-comedy--10-hf-seedance-surreal-comedy--03`

### `prompts/超现实喜剧/30-freyavideo.com-1.md`

- [哥斯拉级橘猫海岸来袭](prompts/超现实喜剧/30-freyavideo.com-1.md#1-哥斯拉级橘猫海岸来袭) — Seedance 2.0（来源标注） · zh · verified · —　`surreal-comedy--30-freyavideo.com-1--01`

### `prompts/超现实喜剧/30-github.com-2.md`

- [巨型大橘猫模因重庆](prompts/超现实喜剧/30-github.com-2.md#1-巨型大橘猫模因重庆) — Seedance 2.0（来源标注） · zh · verified · 时间码分段、分镜/多镜头　`surreal-comedy--30-github.com-2--01`
- [浴室水槽超现实纪录片](prompts/超现实喜剧/30-github.com-2.md#2-浴室水槽超现实纪录片) — Seedance 2.0（来源标注） · zh · verified · 时间码分段、分镜/多镜头　`surreal-comedy--30-github.com-2--02`

### `prompts/超现实喜剧/31-runway.com.md`

- [水下郊区 FPV](prompts/超现实喜剧/31-runway.com.md#1-水下郊区-fpvunderwater-suburban-fpv) — Runway Gen-3 Alpha（已于 2026-07-08 下线） · en · verified · 航拍/FPV　`surreal-comedy--31-runway.com--01`
- [客厅瀑布 POV](prompts/超现实喜剧/31-runway.com.md#2-客厅瀑布-povliving-room-waterfall-pov) — Runway Gen-3 Alpha（已于 2026-07-08 下线） · en · verified · —　`surreal-comedy--31-runway.com--02`
- [棉花糖巨人](prompts/超现实喜剧/31-runway.com.md#3-棉花糖巨人cotton-candy-humanoid) — Runway Gen-3 Alpha（已于 2026-07-08 下线） · en · verified · —　`surreal-comedy--31-runway.com--03`

### `prompts/超现实喜剧/32-runway-seedance-2.0-prompt-guide.md`

- [梗犬餐厅美食大乱](prompts/超现实喜剧/32-runway-seedance-2.0-prompt-guide.md#1-梗犬餐厅美食大乱terrier-restaurant-food-chaos) — Seedance 2.0（来源标注） · en · verified · 分镜/多镜头、慢动作/变速、手持　`surreal-comedy--32-runway-seedance-2.0-prompt-guide--01`

## 恐怖（3）

恐怖、惊悚、悬疑

### `prompts/恐怖/10-hf-seedance-horror.md`

- [鉴宝现场面具脱落](prompts/恐怖/10-hf-seedance-horror.md#1-鉴宝现场面具脱落antiques-roadshow-eldritch-appraisal) — Seedance 2.0 · en · verified · 时间码分段、音频/音效、产品/广告、mockumentary、body-horror、absurdist　`horror--10-hf-seedance-horror--01`

### `prompts/恐怖/30-freyavideo.com.md`

- [画廊活体肖像恐怖](prompts/恐怖/30-freyavideo.com.md#1-画廊活体肖像恐怖) — Seedance 2.0（来源标注） · zh · verified · 时间码分段、分镜/多镜头　`horror--30-freyavideo.com--01`

### `prompts/恐怖/31-atlabs.ai.md`

- [走廊异动](prompts/恐怖/31-atlabs.ai.md#1-走廊异动something-in-the-hallway) — Kling 3.0（来源标注） · en · verified · 音频/音效　`horror--31-atlabs.ai--01`

## 变形转换（3）

变身、换装、形态转换、无缝转场

### `prompts/变形转换/10-hf-seedance-transform.md`

- [职场时尚变身秀](prompts/变形转换/10-hf-seedance-transform.md#1-职场时尚变身秀stylish-office-fashion-transformation-video) — Seedance 2.5（作者帖文注明；HF 数据集标注为 2.0） · en · verified-with-fix · 负面约束、横屏16:9、fashion、transformation、office　`transform--10-hf-seedance-transform--01`
- [奢华沙龙直发变身](prompts/变形转换/10-hf-seedance-transform.md#2-奢华沙龙直发变身cinematic-salon-hair-transformation) — Seedance 2.0 · en · verified · 时间码分段、负面约束、竖屏9:16、慢动作/变速、动画风格、产品/广告、beauty、hair、3d　`transform--10-hf-seedance-transform--02`

### `prompts/变形转换/30-freyavideo.com.md`

- [美人鱼到蜻蜓的变形](prompts/变形转换/30-freyavideo.com.md#1-美人鱼到蜻蜓的变形) — Seedance 2.0（来源标注） · zh · verified · 慢动作/变速　`transform--30-freyavideo.com--01`

## 产品生活（19）

产品广告、商业片、生活方式

### `prompts/产品生活/10-hf-seedance-product.md`

- [清爽果饮新体验](prompts/产品生活/10-hf-seedance-product.md#1-清爽果饮新体验refreshing-fruve-drink-launch) — Seedance 2.0 / GPT Image 2 · ja · verified · 时间码分段、分镜/多镜头、参考图/素材引用、音频/音效、负面约束、竖屏9:16、慢动作/变速、动画风格、产品/广告、beverage、pixar-style、commercial　`product--10-hf-seedance-product--01`
- [翡翠极光耐克宣传片](prompts/产品生活/10-hf-seedance-product.md#2-翡翠极光耐克宣传片nike-emerald-aurora-campaign-film) — Seedance 2.0 / Nano Banana · en · verified-with-fix · 时间码分段、分镜/多镜头、慢动作/变速、手持、产品/广告、Nike、Sneaker、Commercial　`product--10-hf-seedance-product--02`
- [晨光瑜伽垫奢华广告](prompts/产品生活/10-hf-seedance-product.md#3-晨光瑜伽垫奢华广告morning-light-yoga-mat-luxury) — Seedance 2.0 · en · verified · 时间码分段、负面约束、产品/广告、yoga mat、luxury fitness、premium lifestyle　`product--10-hf-seedance-product--03`
- [奢华口红美妆大片](prompts/产品生活/10-hf-seedance-product.md#4-奢华口红美妆大片luxury-lipstick-beauty-campaign) — Seedance 2.0 / GPT Image 2 · en · verified · 分镜/多镜头、参考图/素材引用、负面约束、手持、产品/广告、lipstick commercial、beauty cinematography、fashion styling　`product--10-hf-seedance-product--04`

### `prompts/产品生活/30-anikuku.com-2.md`

- [产品镜头 哑光音箱](prompts/产品生活/30-anikuku.com-2.md#1-产品镜头-哑光音箱) — Seedance 2.0（来源标注） · zh · verified · 参考图/素材引用、产品/广告　`product--30-anikuku.com-2--01`

### `prompts/产品生活/30-freyavideo.com-1.md`

- [磨砂黑保温杯 8 小时保温测试](prompts/产品生活/30-freyavideo.com-1.md#1-磨砂黑保温杯-8-小时保温测试) — Seedance 2.0（来源标注） · zh · verified · 竖屏9:16、产品/广告　`product--30-freyavideo.com-1--01`
- [暴雨城市无线耳机](prompts/产品生活/30-freyavideo.com-1.md#2-暴雨城市无线耳机) — Seedance 2.0（来源标注） · zh · verified · 音频/音效、竖屏9:16、慢动作/变速　`product--30-freyavideo.com-1--02`
- [RGB 机械键盘微距 ASMR](prompts/产品生活/30-freyavideo.com-1.md#3-rgb-机械键盘微距-asmr) — Seedance 2.0（来源标注） · zh · verified · 竖屏9:16、慢动作/变速　`product--30-freyavideo.com-1--03`
- [金色精华滴落美妆微距](prompts/产品生活/30-freyavideo.com-1.md#4-金色精华滴落美妆微距) — Seedance 2.0（来源标注） · zh · verified · 竖屏9:16、慢动作/变速、产品/广告　`product--30-freyavideo.com-1--04`
- [蓝调清晨跑鞋溅水](prompts/产品生活/30-freyavideo.com-1.md#5-蓝调清晨跑鞋溅水) — Seedance 2.0（来源标注） · zh · verified · 竖屏9:16、慢动作/变速　`product--30-freyavideo.com-1--05`
- [便携榨汁杯公园野餐](prompts/产品生活/30-freyavideo.com-1.md#6-便携榨汁杯公园野餐) — Seedance 2.0（来源标注） · zh · verified · 竖屏9:16、慢动作/变速　`product--30-freyavideo.com-1--06`

### `prompts/产品生活/30-github.com-3.md`

- [穿搭变装卡点展示](prompts/产品生活/30-github.com-3.md#1-穿搭变装卡点展示) — Seedance 2.0（来源标注） · zh · verified · 参考图/素材引用、音频/音效、产品/广告　`product--30-github.com-3--01`
- [直播带货口播面霜](prompts/产品生活/30-github.com-3.md#2-直播带货口播面霜) — Seedance 2.0（来源标注） · zh · verified · 产品/广告　`product--30-github.com-3--02`
- [动态海报定点卡点](prompts/产品生活/30-github.com-3.md#3-动态海报定点卡点) — Seedance 2.0（来源标注） · zh · verified · 分镜/多镜头、参考图/素材引用、音频/音效、竖屏9:16　`product--30-github.com-3--03`
- [广告复刻替换无人机](prompts/产品生活/30-github.com-3.md#4-广告复刻替换无人机) — Seedance 2.0（来源标注） · zh · verified · 分镜/多镜头、参考图/素材引用、音频/音效、航拍/FPV、产品/广告　`product--30-github.com-3--04`

### `prompts/产品生活/31-atlabs.ai.md`

- [奢侈腕表](prompts/产品生活/31-atlabs.ai.md#1-奢侈腕表luxury-watch-product-shot) — Kling 3.0（来源标注） · en · verified · 时间码分段、分镜/多镜头、音频/音效、产品/广告　`product--31-atlabs.ai--01`

### `prompts/产品生活/31-memons.ai.md`

- [香水瓶旋转](prompts/产品生活/31-memons.ai.md#1-香水瓶旋转perfume-bottle-hero-rotation) — PixVerse（来源标注） · en · verified · 产品/广告　`product--31-memons.ai--01`

### `prompts/产品生活/32-github-watreesir-awesome-kling-4.md`

- [日式巧克力广告](prompts/产品生活/32-github-watreesir-awesome-kling-4.md#1-日式巧克力广告japanese-chocolate-commercial) — Kling 4.0（仓库标注） · en · verified · 产品/广告　`product--32-github-watreesir-awesome-kling-4--01`

### `prompts/产品生活/32-runway-seedance-2.0-prompt-guide.md`

- [跑鞋产品多镜头广告](prompts/产品生活/32-runway-seedance-2.0-prompt-guide.md#1-跑鞋产品多镜头广告running-shoe-product-multi-shot) — Seedance 2.0（来源标注） · en · verified · 分镜/多镜头、参考图/素材引用、产品/广告　`product--32-runway-seedance-2.0-prompt-guide--01`

## UGC短视频（11）

UGC、自拍 Vlog、手机拍摄感短视频

### `prompts/UGC短视频/10-hf-seedance-ugc.md`

- [情侣球场甜蜜瞬间](prompts/UGC短视频/10-hf-seedance-ugc.md#1-情侣球场甜蜜瞬间couples-romantic-stadium-moment) — Seedance 2.0 / Hailuo/MiniMax · en · verified · 时间码分段、一镜到底、参考图/素材引用、音频/音效、负面约束、Football、Romance、Stadium　`ugc--10-hf-seedance-ugc--01`
- [夏日祭典自拍Vlog](prompts/UGC短视频/10-hf-seedance-ugc.md#2-夏日祭典自拍vlogfestival-selfie-vlog-glow) — Seedance 2.0（HF 数据集标注） · ja · verified · 时间码分段、分镜/多镜头、竖屏9:16、慢动作/变速、手持、festival-vlog、handheld-ugc、matsuri-energy　`ugc--10-hf-seedance-ugc--02`
- [板球情侣甜蜜瞬间](prompts/UGC短视频/10-hf-seedance-ugc.md#3-板球情侣甜蜜瞬间cricket-stadium-couple-zoom-shot) — Seedance 2.0（HF 数据集标注） · en · source-unreachable · 时间码分段、一镜到底、参考图/素材引用、台词/对白、音频/音效、负面约束、横屏16:9、IPL、Broadcast、Crowd　`ugc--10-hf-seedance-ugc--03`
- [石村湖畔夜游](prompts/UGC短视频/10-hf-seedance-ugc.md#4-石村湖畔夜游seokchon-lake-night-walk-vlog) — Seedance 2.0 · en · verified · 竖屏9:16、手持、nightwalk、cinematic、vlog　`ugc--10-hf-seedance-ugc--04`

### `prompts/UGC短视频/30-freyavideo.com.md`

- [卧室抓拍 Vlog 质感](prompts/UGC短视频/30-freyavideo.com.md#1-卧室抓拍-vlog-质感) — Seedance 2.0（来源标注） · zh · verified · —　`ugc--30-freyavideo.com--01`

### `prompts/UGC短视频/31-atlabs.ai.md`

- [咖啡馆晨间竖屏](prompts/UGC短视频/31-atlabs.ai.md#1-咖啡馆晨间竖屏aesthetic-cafe-morning) — Kling 3.0（来源标注） · en · verified · 时间码分段、分镜/多镜头、音频/音效、竖屏9:16　`ugc--31-atlabs.ai--01`

### `prompts/UGC短视频/31-memons.ai.md`

- [俯拍做菜竖屏](prompts/UGC短视频/31-memons.ai.md#1-俯拍做菜竖屏recipe-overhead-vertical) — PixVerse（来源标注） · en · verified · 竖屏9:16　`ugc--31-memons.ai--01`

### `prompts/UGC短视频/32-github-watreesir-awesome-kling-4.md`

- [一镜到底响指换装](prompts/UGC短视频/32-github-watreesir-awesome-kling-4.md#1-一镜到底响指换装single-take-outfit-transition) — Kling 4.0（仓库标注） · en · verified · 时间码分段、一镜到底、参考图/素材引用、台词/对白、音频/音效、负面约束、竖屏9:16、慢动作/变速　`ugc--32-github-watreesir-awesome-kling-4--01`
- [K-pop 签售会](prompts/UGC短视频/32-github-watreesir-awesome-kling-4.md#2-k-pop-签售会k-pop-fansign) — Kling 4.0（仓库标注） · en · verified · 打斗、手持　`ugc--32-github-watreesir-awesome-kling-4--02`
- [手持自拍 Vlog](prompts/UGC短视频/32-github-watreesir-awesome-kling-4.md#3-手持自拍-vloghandheld-selfie-vlog) — Kling 4.0（仓库标注） · en · verified · 时间码分段、分镜/多镜头、参考图/素材引用、音频/音效、手持　`ugc--32-github-watreesir-awesome-kling-4--03`

### `prompts/UGC短视频/32-runway-seedance-2.0-prompt-guide.md`

- [花园水管 · 家用摄像机生活感](prompts/UGC短视频/32-runway-seedance-2.0-prompt-guide.md#1-花园水管--家用摄像机生活感garden-hose-camcorder-lifestyle) — Seedance 2.0（来源标注） · en · verified · 参考图/素材引用、手持　`ugc--32-runway-seedance-2.0-prompt-guide--01`

## 游戏PV（2）

游戏宣传片、格斗游戏序列

### `prompts/游戏PV/30-youmind.com.md`

- [2D 格斗游戏序列（灵能 Agent）](prompts/游戏PV/30-youmind.com.md#1-2d-格斗游戏序列灵能-agent) — Seedance 2.0（来源标注） · zh · verified · 参考图/素材引用、打斗、慢动作/变速、动画风格　`game-pv--30-youmind.com--01`

### `prompts/游戏PV/31-fal.ai.md`

- [装备 UI 加载开场](prompts/游戏PV/31-fal.ai.md#1-装备-ui-加载开场interactive-game-equipment-ui) — MiniMax Hailuo H3（来源标注） · en · verified · 时间码分段　`game-pv--31-fal.ai--01`

## 人物卡（11）

人物设定图、三视图、表情包等角色资产图（生图）

### `prompts/人物卡/04-web-character-card-prompts.md`

- [角色人设图](prompts/人物卡/04-web-character-card-prompts.md#21-角色人设图) — Midjourney（来源标注） · en · source-unreachable · 动画风格　`character-card--04-web-character-card-prompts--01`
- [三视图 turnaround + cref](prompts/人物卡/04-web-character-card-prompts.md#22-三视图-turnaround--cref) — Midjourney（来源标注） · en · source-unreachable · 横屏16:9、动画风格　`character-card--04-web-character-card-prompts--02`
- [Q版表情包 sticker sheet](prompts/人物卡/04-web-character-card-prompts.md#23-q版表情包-sticker-sheet) — Midjourney（来源标注） · en · source-unreachable · —　`character-card--04-web-character-card-prompts--03`
- [FLUX 推荐版式](prompts/人物卡/04-web-character-card-prompts.md#31-flux-recommended-layout) — Flux / Illustrious / Pony / SD LoRA（来源标注） · en · verified · —　`character-card--04-web-character-card-prompts--04`
- [Illustrious 精简前缀](prompts/人物卡/04-web-character-card-prompts.md#33-illustrious-compact-prefix) — Flux / Illustrious / Pony / SD LoRA（来源标注） · en · verified · —　`character-card--04-web-character-card-prompts--05`
- [触发词（FLUX / 通用）](prompts/人物卡/04-web-character-card-prompts.md#34-trigger-words-flux--shared) — Flux / Illustrious / Pony / SD LoRA（来源标注） · en · verified · —　`character-card--04-web-character-card-prompts--06`
- [社区回复：SD/PDXL 多视角示例（同页评论）](prompts/人物卡/04-web-character-card-prompts.md#36-community-reply--multi-view-sdpdxl-example-same-page-comments) — Flux / Illustrious / Pony / SD LoRA（来源标注） · en · verified · —　`character-card--04-web-character-card-prompts--07`
- [SD / Flux 正向提示词](prompts/人物卡/04-web-character-card-prompts.md#42-sd--flux-positive) — Stable Diffusion / Flux（来源标注） · en · verified · 动画风格　`character-card--04-web-character-card-prompts--08`
- [SD / Flux 负向提示词](prompts/人物卡/04-web-character-card-prompts.md#43-sd--flux-negative) — Stable Diffusion / Flux（来源标注） · en · verified · —　`character-card--04-web-character-card-prompts--09`
- [表情设定图短语（文章）](prompts/人物卡/04-web-character-card-prompts.md#45-expression-sheet-phrase-article) — Stable Diffusion / Flux（来源标注） · en · verified · —　`character-card--04-web-character-card-prompts--10`
- [Style stack example (国风修仙)](prompts/人物卡/04-web-character-card-prompts.md#47-style-stack-example-国风修仙) — Stable Diffusion / Flux（来源标注） · en · verified · 动画风格　`character-card--04-web-character-card-prompts--11`

## 生图修画质（11）

图片降噪、画质修复、干净出图（生图）

### `prompts/生图修画质/03-web-image2-denoise-prompts.md`

- [细节分布控制句](prompts/生图修画质/03-web-image2-denoise-prompts.md#11-detail-distribution-control-line) — GPT Image 2（来源标注） · en · verified · —　`image-repair--03-web-image2-denoise-prompts--01`
- [图片降噪修复 Prompt（优化已有脏图、模糊图）](prompts/生图修画质/03-web-image2-denoise-prompts.md#13-图片降噪修复-prompt优化已有脏图模糊图) — GPT Image 2（来源标注） · en · verified · —　`image-repair--03-web-image2-denoise-prompts--02`
- [三层修图逻辑（片段，verbatim from article）](prompts/生图修画质/03-web-image2-denoise-prompts.md#14-三层修图逻辑片段verbatim-from-article) — GPT Image 2（来源标注） · en · verified · —　`image-repair--03-web-image2-denoise-prompts--03`
- [三层修图逻辑（片段，verbatim from article）（2）](prompts/生图修画质/03-web-image2-denoise-prompts.md#14-三层修图逻辑片段verbatim-from-article) — GPT Image 2（来源标注） · en · verified · —　`image-repair--03-web-image2-denoise-prompts--04`
- [三层修图逻辑（片段，verbatim from article）（3）](prompts/生图修画质/03-web-image2-denoise-prompts.md#14-三层修图逻辑片段verbatim-from-article) — GPT Image 2（来源标注） · en · verified · —　`image-repair--03-web-image2-denoise-prompts--05`
- [Banana/修图中文指令（文章给出的中文修图说法）](prompts/生图修画质/03-web-image2-denoise-prompts.md#15-banana修图中文指令文章给出的中文修图说法) — GPT Image 2（来源标注） · zh · verified · —　`image-repair--03-web-image2-denoise-prompts--06`
- [通用材质质量块](prompts/生图修画质/03-web-image2-denoise-prompts.md#22-universal-material-quality-block) — GPT Image 2（来源标注） · en · verified · —　`image-repair--03-web-image2-denoise-prompts--07`
- [安全默认规避块](prompts/生图修画质/03-web-image2-denoise-prompts.md#23-safe-default-avoid-block) — GPT Image 2（来源标注） · en · verified · 负面约束　`image-repair--03-web-image2-denoise-prompts--08`
- [精简规避块](prompts/生图修画质/03-web-image2-denoise-prompts.md#24-narrower-avoid-block) — GPT Image 2（来源标注） · en · verified · 负面约束　`image-repair--03-web-image2-denoise-prompts--09`
- [完整清理附加块](prompts/生图修画质/03-web-image2-denoise-prompts.md#25-full-cleanup-add-on) — GPT Image 2（来源标注） · en · verified · —　`image-repair--03-web-image2-denoise-prompts--10`
- [简短清理附加块](prompts/生图修画质/03-web-image2-denoise-prompts.md#26-short-cleanup-add-on) — GPT Image 2（来源标注） · en · verified · —　`image-repair--03-web-image2-denoise-prompts--11`

## 提示词写法（11）

提示词写法方法论、公式与官方示例

### `prompts/提示词写法/01-web-prompt-writing-methodology.md`

- [优化后城市街头示例](prompts/提示词写法/01-web-prompt-writing-methodology.md#13-优化后城市街头示例) — 未指定（通用写法） · zh · verified · 横屏16:9、手持　`prompt-writing--01-web-prompt-writing-methodology--01`
- [通用负面](prompts/提示词写法/01-web-prompt-writing-methodology.md#14-通用负面) — 未指定（通用写法） · zh · verified · —　`prompt-writing--01-web-prompt-writing-methodology--02`
- [城市漫游模板](prompts/提示词写法/01-web-prompt-writing-methodology.md#15-城市漫游模板) — 未指定（通用写法） · zh · verified · 横屏16:9　`prompt-writing--01-web-prompt-writing-methodology--03`
- [产品广告模板](prompts/提示词写法/01-web-prompt-writing-methodology.md#16-产品广告模板) — 未指定（通用写法） · zh · verified · 产品/广告　`prompt-writing--01-web-prompt-writing-methodology--04`
- [主体定义句式](prompts/提示词写法/01-web-prompt-writing-methodology.md#22-主体定义句式) — Seedance 2.0（来源标注） · zh · verified · —　`prompt-writing--01-web-prompt-writing-methodology--05`
- [主体定义句式（2）](prompts/提示词写法/01-web-prompt-writing-methodology.md#22-主体定义句式) — Seedance 2.0（来源标注） · zh · verified · —　`prompt-writing--01-web-prompt-writing-methodology--06`
- [宿舍情感短剧（kit 内官方 PDF 衍生示例）](prompts/提示词写法/01-web-prompt-writing-methodology.md#23-宿舍情感短剧kit-内官方-pdf-衍生示例) — Seedance 2.0（来源标注） · zh · source-contradicts · 分镜/多镜头、参考图/素材引用、音频/音效　`prompt-writing--01-web-prompt-writing-methodology--07`
- [正面约束模板](prompts/提示词写法/01-web-prompt-writing-methodology.md#33-正面约束模板) — Seedance 2.0（来源标注） · zh · verified · —　`prompt-writing--01-web-prompt-writing-methodology--08`
- [Seedance 2.0 推荐（序号式）](prompts/提示词写法/01-web-prompt-writing-methodology.md#42-seedance-20-推荐序号式) — Seedance 2.5（来源标注） · zh · verified · 分镜/多镜头　`prompt-writing--01-web-prompt-writing-methodology--09`
- [Seedance 2.5 推荐（秒级时间戳）](prompts/提示词写法/01-web-prompt-writing-methodology.md#43-seedance-25-推荐秒级时间戳) — Seedance 2.5（来源标注） · zh · verified · 时间码分段　`prompt-writing--01-web-prompt-writing-methodology--10`

### `prompts/提示词写法/32-runway-seedance-2.0-prompt-guide.md`

- [八要素示例 · 陶艺师](prompts/提示词写法/32-runway-seedance-2.0-prompt-guide.md#1-八要素示例--陶艺师eight-elements-ceramicist-example) — Seedance 2.0（来源标注） · en · verified · —　`prompt-writing--32-runway-seedance-2.0-prompt-guide--01`

## 对照样例（cases/）

每个样例目录含 `prompt/prompt.txt`（原文）、成片说明与来源记录；提示词正文与 `prompts/` 不重复。

- [Sword Duel on the Lake](cases/国风古装/hf-sword-duel-on-the-lake/) — 国风古装 · 来源 https://x.com/john87445528/status/2023660939954860134
- [lansenai-xianxia-aerial-sword-30s](cases/国风古装/lansenai-xianxia-aerial-sword-30s/) — 国风古装 · 来源 https://x.com/lansenai/status/2098774755407241445
- [Breathing Technique Showdown](cases/打斗运镜/hf-breathing-technique-showdown/) — 打斗运镜 · 来源 https://x.com/johnAGI168/status/2021610292979876208
- [Classroom Brawl: Introvert's Fury Unleashed](cases/打斗运镜/hf-classroom-brawl-introvert-fury/) — 打斗运镜 · 来源 https://x.com/harboriis/status/2046471880476164411
- [One Man, One Gun, No Mercy](cases/打斗运镜/hf-one-man-one-gun-no-mercy/) — 打斗运镜 · 来源 https://x.com/promptsref/status/2036695357414096941
- [Post-Apocalyptic Superhuman Brawl](cases/打斗运镜/hf-post-apocalyptic-superhuman-brawl/) — 打斗运镜 · 来源 https://x.com/RizwanAly07/status/2046508797854994647
- [lansenai-ink-skill-30s](cases/打斗运镜/lansenai-ink-skill-30s/) — 打斗运镜 · 来源 https://x.com/lansenai/status/2104401414403526688
- [lansenai-street-fighter-ko](cases/打斗运镜/lansenai-street-fighter-ko/) — 打斗运镜 · 来源 https://x.com/lansenai/status/2104176547989205112
- [Celestial Fracture Supernova Strike](cases/特效/hf-celestial-fracture-supernova-strike/) — 特效 · 来源 https://x.com/IqraSaifiii/status/2046605930335551524
- [Frost Dragon Shatters Frozen Citadel](cases/特效/hf-frost-dragon-shatters-frozen-citadel/) — 特效 · 来源 https://x.com/restofart/status/2070513629548425643
- [Glacial Tiger vs Frost Serpent](cases/特效/hf-glacial-tiger-vs-frost-serpent/) — 特效 · 来源 https://x.com/LudovicCreator/status/2045419585491317186
- [Red Energy Orb Explosion in Valley](cases/特效/hf-red-energy-orb-explosion-valley/) — 特效 · 来源 https://x.com/aihustlehub12/status/2046699329369342354
- [Ancient Temple Heroic Cinematic](cases/电影大场面/hf-ancient-temple-heroic-cinematic/) — 电影大场面 · 来源 https://x.com/yuday9909/status/2046595090706215200
- [Mech Collapse Escape](cases/电影大场面/hf-mech-collapse-escape/) — 电影大场面 · 来源 https://x.com/AllaAisling/status/2046716774209495336
- [Bridge Collapse Chase](cases/运镜/hf-bridge-collapse-chase/) — 运镜 · 来源 https://x.com/ChangningL29508/status/2046665211357319647
- [Elegant Bullet-Time Camera Circle](cases/运镜/hf-elegant-bullet-time-camera-circle/) — 运镜 · 来源 https://x.com/KusoPhoto/status/2046590847953879171
- [FPV Over Ancient Vanga Kingdom](cases/运镜/hf-fpv-ancient-vanga-kingdom/) — 运镜 · 来源 https://x.com/shushant_l/status/2046575817686474804

## 方法与讲解文件（不含计数提示词）

这些文件收录教程视频的帖子文案、画面字幕等原文，适合学习写法，但没有可直接复制的完整提示词。

- [用 AI 提示词控制打斗画面：景别、机位、推拉怎么配](prompts/打斗运镜/33-douyin-huxiaolv-fight-control-jigong.md) — 打斗运镜 · 来源 https://www.douyin.com/video/7689064641665748270
- [AI 打斗别乱剪：用好一镜到底](prompts/打斗运镜/34-douyin-baolaoshi-one-take-fight.md) — 打斗运镜 · 来源 https://www.douyin.com/video/7689821368011241832
- [用 AI 提示词控制画面景别：中景、全景、远景怎么选](prompts/运镜/43-douyin-huxiaolv-shot-size-jingbie.md) — 运镜 · 来源 https://www.douyin.com/video/7685608233369056433
