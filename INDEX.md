# 提示词索引（INDEX）

> 本文件由 `scripts/build_index.py` 从 `prompts/` 与 `cases/` 自动生成，请勿手改。AI 检索请用同目录的 `index.jsonl`（每行一条，含完整原文与全部元数据；`条目类型` 为 prompt / case / reference）。
> 每行格式：标题（链接到条目）— 适用模型 · 语言 · 核对状态 · 标签。

## 技巧锦囊（33）

> 想不到要问、但能给人新思路的技巧（力场融合特效、一镜到底打斗、混合风格等），供主动浏览；可交叉收录其他分类的条目。每行：标题 — 技巧钩子（触发场景）· 主分类。

- [森系电竞女角色定妆半身照（中文直输版）](prompts/人物卡/40-douyin-ksr-midjourney-stylize-personalize.md#p1--森系电竞女角色定妆照中文直输版) — 同一段提示词一个字不改，只换 Midjourney 的风格化数值、自建个性化档案（--p）或 Explore 风格页的 Try Style（--sref），就能保住角色设定、只换影调和审美——提示词写得越具体，换风格时保住的元素越多（角色定妆照内容都对但画面审美普通、像素材图，想不重写提示词就试出几种风格时）· 主分类：人物卡
- [奇幻科幻糖果花城全景（中文直输版）](prompts/人物卡/40-douyin-ksr-midjourney-stylize-personalize.md#p2--糖果花城全景中文直输版) — 给一个项目专门建一个 Midjourney 个性化档案：花约一小时只点符合剧本色调的图（作者点到 3000 多分），再把场景提示词挂上它出图；提示词里只留一个暗色巨物当全城视觉终点（要给一个剧本出一批色调统一的场景概念图，想让出图稳定贴近脑中的设定时）· 主分类：人物卡
- [石台遗迹 30s 慢节奏蓄力 + 天灾级爆发对决](prompts/打斗运镜/35-x-lansenai-disaster-taiji.md#1-石台遗迹-30s-慢节奏蓄力--天灾级爆发对决) — 打斗不必全程快切密招：用「慢蓄力 + 一次把人打飞几百米 / 砸进山体」的尺度感，让每一击像天灾（AI 打斗只有原地连招、看不出力量差距，或特效花哨却没有「一击改写空间」的压迫感时）· 主分类：打斗运镜
- [雪境 30s 双女剑客追战（伪一镜到底秒级分镜）](prompts/打斗运镜/36-x-chengzilhy-snow-chase.md#1-雪境-30s-双女剑客追战) — 伪一镜到底可以按「三秒一组、组内逐秒写」：每秒写清运镜 + 景别 + 双方主动作，用急推/甩镜/掠镜衔接，而不是匀速侧跟（想做 30 秒追战却写成站桩对砍，或一镜到底只有环绕没有路径推进、看不清位移时）· 主分类：打斗运镜
- [轨道补齐：两段视频之间生成衔接（落叶激起金色粒子）](prompts/技巧锦囊/35-volcengine-seedance2-guide-tricks.md#1-轨道补齐给两段现成视频补中间) — 把两段接不上的视频交给模型，只让它生成中间那一段过渡（最多 3 段、总长 15 秒）（两段分别生成的镜头硬切太突兀，想要一个自然的过渡段时）· 主分类：技巧锦囊
- [向前延长：在已有视频之前补一个过肩对白镜头](prompts/技巧锦囊/35-volcengine-seedance2-guide-tricks.md#2-向前延长给已有视频补前情) — 延长不只往后续：写「向前延长视频1」就能在已有镜头之前补一段（比如先来个过肩镜头）（已经生成了满意的镜头，却发现前面少一个建立镜头或反打镜头时）· 主分类：技巧锦囊
- [白模转换：把视频转成纯白 3D 模型（续写前的预处理）](prompts/技巧锦囊/35-volcengine-seedance2-guide-tricks.md#4-白模续写先把视频转成白色-3d-模型再拿去延长减少画质劣化) — 续写前先把视频转成「白模视频」，只留结构和动作、去掉会累积劣化的颜色纹理（同一段视频要多次延长，每续一次人脸就更花、出现色块时）· 主分类：技巧锦囊
- [防双胞胎全局约束（加在提示词末尾）](prompts/技巧锦囊/35-volcengine-seedance2-guide-tricks.md#5-防双胞胎人名后标注对应图片--结尾加全局约束且不用三视图) — 多人同框出现两个一模一样的人时，在末尾加一句固定约束，并把三视图换成单人照（多人物参考、画面里人物被「复制」成双胞胎时）· 主分类：技巧锦囊
- [手绘 2D/3D 混合动画：工作室里的小机器人（官方完整示例）](prompts/技巧锦囊/36-openai-sora2-prompting-guide-tricks.md#4-官方完整示例手绘-2d3d-混合动画) — 官方示例本身就在用「混合媒介」：Style 一行写明 2D/3D 手绘混合、定格动画手感、水彩晕染，Actions 按节拍逐条写（想做绘本 / 定格 / 手绘质感的动画短片，或想看「混合媒介 + 动作节拍」完整写法的样板时）· 主分类：技巧锦囊
- [首帧：舞台上唱歌的女歌手（正面中景）](prompts/技巧锦囊/37-google-veo31-first-last-frame-pov-switch.md#step-1--首帧) — 首帧和尾帧用两个不同视角（正面 → 背后 POV），再让模型用一个 180° 环绕把两者连起来，一条镜头里完成视角反转（想在一个镜头里从「看人」转到「用人的视角看世界」（舞台、赛场、发布会），又不想硬切时）· 主分类：技巧锦囊
- [尾帧：从歌手背后看向欢呼人群（POV）](prompts/技巧锦囊/37-google-veo31-first-last-frame-pov-switch.md#step-2--尾帧) — 首帧和尾帧用两个不同视角（正面 → 背后 POV），再让模型用一个 180° 环绕把两者连起来，一条镜头里完成视角反转（想在一个镜头里从「看人」转到「用人的视角看世界」（舞台、赛场、发布会），又不想硬切时）· 主分类：技巧锦囊
- [Veo 3.1 首尾帧：180° 环绕从正面转到背后 POV（含歌词）](prompts/技巧锦囊/37-google-veo31-first-last-frame-pov-switch.md#step-3--veo-31-首尾帧提示词) — 首帧和尾帧用两个不同视角（正面 → 背后 POV），再让模型用一个 180° 环绕把两者连起来，一条镜头里完成视角反转（想在一个镜头里从「看人」转到「用人的视角看世界」（舞台、赛场、发布会），又不想硬切时）· 主分类：技巧锦囊
- [机械公牛穿越沙漠：主体运动 + 摄影机 + 场景运动 + 风格四要素（官方示例）](prompts/技巧锦囊/38-runway-gen4-image-to-video-motion-only.md#4-官方示例四要素齐全的一句) — 图生视频别再描述图里已有的东西：只写「谁怎么动、镜头怎么动、环境怎么被带动」，并用 the subject / 位置词指代主体（图生视频结果几乎不动、动作僵、或模型把图里的人「重画」走样时）· 主分类：技巧锦囊
- [职场一镜到底：人走镜头跟、人停镜头停（官方示例）](prompts/技巧锦囊/39-kling3-camera-freezes-in-sync-long-take.md#2-示例提示词) — 长镜头跟拍不闷的关键：写明「人停镜头也停、人走镜头再跟」，每个小动作都给镜头一个同步反应（一条长镜头里人物要做一连串日常动作（进门、放包、签字、坐下），镜头却一直匀速漂移、没有节奏时）· 主分类：技巧锦囊
- [实拍背景叠加 CG 角色（竹林）](prompts/技巧锦囊/44-douyin-aiqiqi-hybrid-media-cinematic.md#a--实拍背景叠加-cg-角色打字-326400-s) — 不写题材写媒介：把「实拍背景」「CG 角色」「光照匹配」三件事一起写进提示词，画面就不再是千篇一律的纯 CG 渲染（古风、奇幻人物总是出一套塑料感的 3D 国漫 CG，想要更像电影实拍时）· 主分类：技巧锦囊
- [3D 角色 + 2D 手绘水墨施法特效](prompts/技巧锦囊/44-douyin-aiqiqi-hybrid-media-cinematic.md#b--3d-主体叠加-2d-手绘水墨特效打字-502570-s) — 让两种视觉语言硬碰硬：3D 写实角色 + 2D 手绘水墨特效（带飞白边缘），反差本身就成了风格（仙侠、武侠的施法和剑气总是同一种发光粒子，想做出辨识度时）· 主分类：技巧锦囊
- [数字渲染 + 16mm 胶片漏光 + VHS 噪点（赛博修真）](prompts/技巧锦囊/44-douyin-aiqiqi-hybrid-media-cinematic.md#c--高清数字渲染叠加-16mm-胶片漏光与-vhs-噪点打字-686752-s) — 把两个时代的介质叠在一起：高清数字渲染 + 16mm 胶片漏光 + VHS 噪点，得到「另一条时间线」的质感（赛博、科幻、修真画面太干净太数码，想要复古或做旧的电影感时）· 主分类：技巧锦囊
- [Director's Read：内部叙事字段编译成可见载体（社区摘录）](prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md#2-emily--directors-read--只写可见--可听载体社区) — 欲望、权力、潜台词先写在内部提纲里，最终提示词只留机位、视线、道具动作和前后状态差（短剧/对白镜头写了很多「内心纠结」「气场压制」，画面却演不出来时）· 主分类：技巧锦囊
- [参考转移契约：Exact Tag + 一职一角 + ignore 子句（社区摘录）](prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md#3-emily--参考转移契约一职一角--ignore社区) — 每个参考只领一个主职，并写明 ignore 身份/环境/运镜中不该转移的项（参考视频只想借运镜，结果脸、服装、背景一起漂过来时）· 主分类：技巧锦囊
- [打斗开场 2 秒钩子：对手距离 / 兵器流派 / 能量节奏（社区摘录）](prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md#6-beshuaxian--打斗开场-2-秒钩子薄摘录) — 打斗前两秒先让人看清：谁对谁、多远、什么兵器/流派、是轻快还是沉重（武戏开头混乱，观众分不清对手和兵器，后半段发力链写得再细也救不回来时）· 主分类：技巧锦囊
- [CINEDANCE：首帧占位 + 米级空间锁（社区摘录）](prompts/技巧锦囊/46-hell-grind-cinedance-acting-lira-synthesis.md#2-cinedance--首帧占位--可度量空间锁社区) — 开场第一帧就要站好位；距离写到米和接触点，并锁住机位在哪一侧（角色飘在空地、开场空镜、左右翻面、或「near the car」写了却贴不上地标时）· 主分类：技巧锦囊
- [ACTING：压力下行为 + eye life + states-not-transitions（社区摘录）](prompts/技巧锦囊/46-hell-grind-cinedance-acting-lira-synthesis.md#4-acting--压力下行为--master--eye-life--改写--状态非过程社区) — 表演写压力下的行为与眼神生命，动作写「已在状态中」，每场改写档案勿整段粘贴（AI 演技像在「演情绪」、眼神死、或过程动词链导致动作塌缩时）· 主分类：技巧锦囊
- [LIRA：IMAGE 提示词 4-D 方法论指针（社区摘录）](prompts/技巧锦囊/46-hell-grind-cinedance-acting-lira-synthesis.md#5-lira--生图-4-d-指针社区方法不计数) — 生图提示词先走拆解→诊断失败模式→再按任务选技法，而不是堆关键词（写角色表/场景静帧/局部修图提示词，需要一条可检查的优化流程时）· 主分类：技巧锦囊
- [魔法能量场（奇幻短片）](prompts/特效/41-douyin-aiqiqi-force-field-vfx.md#p1--魔法能量场卡片显示-206236-s正文清晰-210234-s) — 特效不像贴图，关键是写周围怎么被它带动：空气热浪扭曲、风压吹动布料发丝、光影跟着特效变色（「Field 力场扰动模拟」这句本身未见模型专门响应的证据）（AI 做的魔法、能量特效看着像后期贴上去、和周围环境不融合时）· 主分类：特效
- [爆炸冲击波（灾难 / 科幻战斗镜头）](prompts/特效/41-douyin-aiqiqi-force-field-vfx.md#p2--爆炸冲击波卡片显示-284310-s正文清晰-288308-s) — 冲击波要有杀伤力，就写周围怎么被推：空气压缩扭曲、植被布料被风压挤变形、光穿过扰动空气产生色散（AI 爆炸、冲击波看着没威力，周围物体一动不动时）· 主分类：特效
- [沙漠熔岩高温热浪](prompts/特效/41-douyin-aiqiqi-force-field-vfx.md#p3--沙漠熔岩高温热浪卡片显示-346368-s正文清晰-350366-s) — 热浪不靠加滤镜：写地热力场让近地面空气扭曲震颤、远景轮廓被折射，再配长焦压缩构图（想拍沙漠、熔岩、高温场景的热浪感，但画面只是颜色变暖时）· 主分类：特效
- [午夜空餐厅完全锁定静止镜头](prompts/运镜/44-runway-official-ai-camera-prompts.md#5-午夜空餐厅完全锁定静止镜头static-dramatic) — 静止镜头要主动给模型「戏」：写清场景里谁在动（雨、灯光闪烁），再加一句 camera entirely motionless（建立镜头或空镜总被模型偷偷漂移、推拉时）· 主分类：运镜
- [三拍子① 窄巷建立镜头（锁定俯角）](prompts/运镜/44-runway-official-ai-camera-prompts.md#8-三拍子①-窄巷建立镜头锁定俯角beat-1-establishing) — 三拍子剪辑：建立（锁定）→ 推进制造威胁 → 反转特写；每拍单独生成再硬切，比一条里堆三种运镜稳（想做短叙事悬疑/恐怖，但一条提示词里又推又摇又环绕导致漂移时）· 主分类：运镜
- [只改一个条件：同一画面改成冬夜下雪](prompts/首尾帧生图/01-openai-gpt-image-official.md#7-change-one-condition--只改一个条件) — 尾帧不用重新生成：拿首帧做一次「只改一个条件」的编辑（天气、时间、表情），构图和人物自然对齐（做首尾帧视频（日转夜、晴转雪、表情变化），需要两张构图完全一致的图时）· 主分类：首尾帧生图
- [角色多角度：一次只要一个角度（360 view）](prompts/首尾帧生图/02-google-gemini-veo-official.md#5-character-consistency-360-view--逐个角度生成) — 多角度参考图不要一张图拼三视图：每次只要一个角度、把上一张作为输入，得到一组独立的单视图（要给视频模型准备角色多角度参考，但 Seedance 2.0 等模型不建议用三视图 / 多视图拼图时）· 主分类：首尾帧生图
- [Runway：首帧里的运动暗示会和提示词打架](prompts/首尾帧生图/05-runway-official.md#2-image-to-video-faq--与画面运动暗示相反的提示) — 首帧要「静」：先用图像编辑去掉运动模糊、扬尘、半空中的姿势，再让视频模型按提示词动起来（图生视频时模型总往你不想要的方向动、或让它静止它却一直在动时）· 主分类：首尾帧生图
- [AI 打斗别乱剪：用好一镜到底](prompts/打斗运镜/34-douyin-baolaoshi-one-take-fight.md) — AI 打斗少剪反而更燃：一条 10 秒长镜头里用手持跟拍、环境挨打、人数压迫撑起燃感（AI 打斗片段剪得碎、没有临场感，或多段拼接后动作接不上时）· 主分类：打斗运镜
- [用 AI 提示词控制画面景别：中景、全景、远景怎么选](prompts/运镜/43-douyin-huxiaolv-shot-size-jingbie.md) — 选景别不看帅不帅，看这一镜要交代什么：攻防用中景看清身体距离，技能范围用全景 / 超远景，结尾拉远景让主角显得更强；特写反而看不清怎么打（AI 战斗画面好看但看不懂谁在打谁、技能打到哪，或每一镜都是近景特写时）· 主分类：运镜

## 统计

| 分类 | 说明 | 提示词条目 | 对照样例（cases/） |
|------|------|-----------:|-------------------:|
| [技巧锦囊](prompts/技巧锦囊/) | 想不到要问、但能给人新思路的技巧（力场融合特效、一镜到底打斗、混合风格等），供主动浏览；可交叉收录其他分类的条目 | 19（另有交叉收录 14 条） | 0 |
| [打斗运镜](prompts/打斗运镜/) | 打斗、武戏、动作编排与配套运镜（含发力链、打击感方法） | 59 | 6 |
| [运镜](prompts/运镜/) | 以摄影机运动、镜头调度为主要看点的提示词与运镜词典、景别方法 | 108 | 3 |
| [特效](prompts/特效/) | 技能特效、魔法、能量、粒子、破坏等视觉特效 | 17 | 4 |
| [光影打光](prompts/光影打光/) | 以打光为主要看点的提示词：光源时段、方位角度、软硬、色温与光型（逆光、伦勃朗光、丁达尔光柱等） | 2 | 0 |
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
| [首尾帧生图](prompts/首尾帧生图/) | 给图生视频准备首帧 / 尾帧 / 关键帧 / 角色参考图的生图与编辑方法，以及首尾帧之间的视频提示词（以厂商官方示例为主） | 43 | 0 |
| [人物卡](prompts/人物卡/) | 人物设定图、三视图、表情包等角色资产图（生图） | 13 | 0 |
| [生图修画质](prompts/生图修画质/) | 图片降噪、画质修复、干净出图（生图） | 11 | 0 |
| [提示词写法](prompts/提示词写法/) | 提示词写法方法论、公式与官方示例 | 13 | 0 |
| **合计** | | **393** | **17** |

核对状态：verified 363、verified-with-fix 24、source-unreachable 6

## 技巧锦囊（19）

想不到要问、但能给人新思路的技巧（力场融合特效、一镜到底打斗、混合风格等），供主动浏览；可交叉收录其他分类的条目

### `prompts/技巧锦囊/35-volcengine-seedance2-guide-tricks.md`

- [轨道补齐：两段视频之间生成衔接（落叶激起金色粒子）](prompts/技巧锦囊/35-volcengine-seedance2-guide-tricks.md#1-轨道补齐给两段现成视频补中间) — Seedance 2.0 系列（来源标注：火山引擎《Doubao Seedance 2.0 系列提示词指南》） · zh · verified · 技巧锦囊、视频延长、轨道补齐、参考素材、转场、Seedance　`jiqiao--35-volcengine-seedance2-guide-tricks--01`
- [向前延长：在已有视频之前补一个过肩对白镜头](prompts/技巧锦囊/35-volcengine-seedance2-guide-tricks.md#2-向前延长给已有视频补前情) — Seedance 2.0 系列（来源标注：火山引擎《Doubao Seedance 2.0 系列提示词指南》） · zh · verified · 技巧锦囊、视频延长、向前延长、台词、过肩镜头、Seedance　`jiqiao--35-volcengine-seedance2-guide-tricks--02`
- [白模转换：把视频转成纯白 3D 模型（续写前的预处理）](prompts/技巧锦囊/35-volcengine-seedance2-guide-tricks.md#4-白模续写先把视频转成白色-3d-模型再拿去延长减少画质劣化) — Seedance 2.0 系列（来源标注：火山引擎《Doubao Seedance 2.0 系列提示词指南》） · zh · verified · 技巧锦囊、视频延长、白模、画质、视频编辑、Seedance　`jiqiao--35-volcengine-seedance2-guide-tricks--03`
- [防双胞胎全局约束（加在提示词末尾）](prompts/技巧锦囊/35-volcengine-seedance2-guide-tricks.md#5-防双胞胎人名后标注对应图片--结尾加全局约束且不用三视图) — Seedance 2.0 系列（来源标注：火山引擎《Doubao Seedance 2.0 系列提示词指南》） · zh · verified · 技巧锦囊、负面约束、多人物、参考图/素材引用、一致性、Seedance　`jiqiao--35-volcengine-seedance2-guide-tricks--04`

### `prompts/技巧锦囊/36-openai-sora2-prompting-guide-tricks.md`

- [手绘 2D/3D 混合动画：工作室里的小机器人（官方完整示例）](prompts/技巧锦囊/36-openai-sora2-prompting-guide-tricks.md#4-官方完整示例手绘-2d3d-混合动画) — Sora 2（来源标注：OpenAI《Sora 2 Prompting Guide》） · en · verified · 技巧锦囊、混合媒介、3D+2D、动作节拍、调色板、分段结构、台词、音效　`jiqiao--36-openai-sora2-prompting-guide-tricks--01`

### `prompts/技巧锦囊/37-google-veo31-first-last-frame-pov-switch.md`

- [首帧：舞台上唱歌的女歌手（正面中景）](prompts/技巧锦囊/37-google-veo31-first-last-frame-pov-switch.md#step-1--首帧) — Gemini 2.5 Flash Image（Nano Banana）（来源标注：用来生成首帧） · en · verified · 技巧锦囊、首尾帧、视角切换、环绕运镜、POV、参考图/素材引用、生图　`jiqiao--37-google-veo31-first-last-frame-pov-switch--01`
- [尾帧：从歌手背后看向欢呼人群（POV）](prompts/技巧锦囊/37-google-veo31-first-last-frame-pov-switch.md#step-2--尾帧) — Gemini 2.5 Flash Image（Nano Banana）（来源标注：用来生成尾帧） · en · verified · 技巧锦囊、首尾帧、视角切换、环绕运镜、POV、参考图/素材引用、生图　`jiqiao--37-google-veo31-first-last-frame-pov-switch--02`
- [Veo 3.1 首尾帧：180° 环绕从正面转到背后 POV（含歌词）](prompts/技巧锦囊/37-google-veo31-first-last-frame-pov-switch.md#step-3--veo-31-首尾帧提示词) — Veo 3.1（来源标注；使用 First and Last Frame 功能） · en · verified · 技巧锦囊、首尾帧、视角切换、环绕运镜、POV、参考图/素材引用、台词、音频　`jiqiao--37-google-veo31-first-last-frame-pov-switch--03`

### `prompts/技巧锦囊/38-runway-gen4-image-to-video-motion-only.md`

- [机械公牛穿越沙漠：主体运动 + 摄影机 + 场景运动 + 风格四要素（官方示例）](prompts/技巧锦囊/38-runway-gen4-image-to-video-motion-only.md#4-官方示例四要素齐全的一句) — Runway Gen-4（来源标注：Runway《Gen-4 Video Prompting Guide》，需配合输入图） · en · verified · 技巧锦囊、图生视频、只写运动、场景运动、手持、风格词　`jiqiao--38-runway-gen4-image-to-video-motion-only--01`

### `prompts/技巧锦囊/39-kling3-camera-freezes-in-sync-long-take.md`

- [职场一镜到底：人走镜头跟、人停镜头停（官方示例）](prompts/技巧锦囊/39-kling3-camera-freezes-in-sync-long-take.md#2-示例提示词) — Kling VIDEO 3.0（来源标注：可灵《Kling VIDEO 3.0 Model User Guide》；示例使用首帧 + 主体参考） · en · verified · 技巧锦囊、一镜到底、跟拍、同步停顿、参考图/素材引用、首帧　`jiqiao--39-kling3-camera-freezes-in-sync-long-take--01`

### `prompts/技巧锦囊/44-douyin-aiqiqi-hybrid-media-cinematic.md`

- [实拍背景叠加 CG 角色（竹林）](prompts/技巧锦囊/44-douyin-aiqiqi-hybrid-media-cinematic.md#a--实拍背景叠加-cg-角色打字-326400-s) — 即梦 Seedance 2.0 Fast（画面中生成界面显示「即梦 Seedance 2.0 Fast VIP」「全能参考」；作者未另外说明） · zh+en · verified · 技巧锦囊、混合媒介、实拍+CG、光照匹配、国风古装、风格词　`jiqiao--44-douyin-aiqiqi-hybrid-media-cinematic--01`
- [3D 角色 + 2D 手绘水墨施法特效](prompts/技巧锦囊/44-douyin-aiqiqi-hybrid-media-cinematic.md#b--3d-主体叠加-2d-手绘水墨特效打字-502570-s) — 即梦 Seedance 2.0 Fast（画面中生成界面显示「即梦 Seedance 2.0 Fast VIP」「全能参考」；作者未另外说明） · zh+en · verified · 技巧锦囊、混合媒介、3D+2D、水墨、飞白、特效、国风古装、风格词　`jiqiao--44-douyin-aiqiqi-hybrid-media-cinematic--02`
- [数字渲染 + 16mm 胶片漏光 + VHS 噪点（赛博修真）](prompts/技巧锦囊/44-douyin-aiqiqi-hybrid-media-cinematic.md#c--高清数字渲染叠加-16mm-胶片漏光与-vhs-噪点打字-686752-s) — 即梦 Seedance 2.0 Fast（画面中生成界面显示「即梦 Seedance 2.0 Fast VIP」「全能参考」；作者未另外说明） · zh+en · verified · 技巧锦囊、混合媒介、数字+胶片、胶片质感、VHS、漏光、赛博、风格词　`jiqiao--44-douyin-aiqiqi-hybrid-media-cinematic--03`

### `prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md`

- [Director's Read：内部叙事字段编译成可见载体（社区摘录）](prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md#2-emily--directors-read--只写可见--可听载体社区) — Seedance 2.0（社区 skill 包装；官方未使用 Director's Read 术语） · en · verified · 技巧锦囊、Seedance、社区说法、分镜/多镜头、叙事载体　`jiqiao--45-seedance-agent-skill-synthesis--01`
- [参考转移契约：Exact Tag + 一职一角 + ignore 子句（社区摘录）](prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md#3-emily--参考转移契约一职一角--ignore社区) — Seedance 2.0（社区；绑定写法随界面：@Image1 / @图片1 / 图片1） · en · verified · 技巧锦囊、Seedance、社区说法、参考图/素材引用　`jiqiao--45-seedance-agent-skill-synthesis--02`
- [打斗开场 2 秒钩子：对手距离 / 兵器流派 / 能量节奏（社区摘录）](prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md#6-beshuaxian--打斗开场-2-秒钩子薄摘录) — Seedance 2.0（社区 Higgsfield 向 skill；时间码在 Seedance 2.0 上不稳定，见备注） · zh · verified · 技巧锦囊、Seedance、社区说法、打斗、时间码分段　`jiqiao--45-seedance-agent-skill-synthesis--03`

### `prompts/技巧锦囊/46-hell-grind-cinedance-acting-lira-synthesis.md`

- [CINEDANCE：首帧占位 + 米级空间锁（社区摘录）](prompts/技巧锦囊/46-hell-grind-cinedance-acting-lira-synthesis.md#2-cinedance--首帧占位--可度量空间锁社区) — Seedance 2.0 / Higgsfield Seedance（Hell Grind CINEDANCE V4 社区包装；非火山官方术语） · en · verified · 技巧锦囊、Seedance、社区说法、分镜/多镜头、空间锁　`jiqiao--46-hell-grind-cinedance-acting-lira-synthesis--01`
- [ACTING：压力下行为 + eye life + states-not-transitions（社区摘录）](prompts/技巧锦囊/46-hell-grind-cinedance-acting-lira-synthesis.md#4-acting--压力下行为--master--eye-life--改写--状态非过程社区) — Seedance 2.0（Hell Grind ACTING 社区包装；模型无关写法，仍以目标模型官方为准） · en · verified · 技巧锦囊、Seedance、社区说法、表演、人物一致性　`jiqiao--46-hell-grind-cinedance-acting-lira-synthesis--02`
- [LIRA：IMAGE 提示词 4-D 方法论指针（社区摘录）](prompts/技巧锦囊/46-hell-grind-cinedance-acting-lira-synthesis.md#5-lira--生图-4-d-指针社区方法不计数) — Higgsfield Soul / NBP 等 IMAGE 工作流（Hell Grind LIRA；非 Seedance 视频官方） · en · verified · 技巧锦囊、社区说法、生图、提示词写法　`jiqiao--46-hell-grind-cinedance-acting-lira-synthesis--03`

## 打斗运镜（59）

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
- [呼吸法真人决战](prompts/打斗运镜/30-freyavideo.com-1.md#2-呼吸法真人决战) — Seedance 2.0（来源标注） · zh · verified · 打斗　`fight-camera--30-freyavideo.com-1--03`

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

### `prompts/打斗运镜/35-x-lansenai-disaster-taiji.md`

- [石台遗迹 30s 慢节奏蓄力 + 天灾级爆发对决](prompts/打斗运镜/35-x-lansenai-disaster-taiji.md#1-石台遗迹-30s-慢节奏蓄力--天灾级爆发对决) — 未指定（原文为通用中文 AI 视频提示词；帖文语境偏 Seedance 系） · zh · verified · 时间码分段、分镜/多镜头、负面约束、武侠/仙侠、古风、打斗、慢动作/变速、技巧锦囊　`fight-camera--35-x-lansenai-disaster-taiji--01`
- [雨中石台 25s 太极宗师纯享技能展示](prompts/打斗运镜/35-x-lansenai-disaster-taiji.md#2-雨中石台-25s-太极宗师纯享技能展示) — 未指定（原文为通用中文 AI 视频提示词） · zh · verified · 时间码分段、分镜/多镜头、武侠/仙侠、古风、特效、负面约束　`fight-camera--35-x-lansenai-disaster-taiji--02`

### `prompts/打斗运镜/36-x-chengzilhy-snow-chase.md`

- [雪境 30s 双女剑客追战（伪一镜到底秒级分镜）](prompts/打斗运镜/36-x-chengzilhy-snow-chase.md#1-雪境-30s-双女剑客追战) — Seedance 2.5（来源标注） · zh · verified · 时间码分段、分镜/多镜头、一镜到底、参考图/素材引用、负面约束、武侠/仙侠、打斗、技巧锦囊　`fight-camera--36-x-chengzilhy-snow-chase--01`

## 运镜（108）

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

### `prompts/运镜/44-runway-official-ai-camera-prompts.md`

- [雨夜女子中近景缓慢推进](prompts/运镜/44-runway-official-ai-camera-prompts.md#1-雨夜女子中近景缓慢推进cinematic-push-in) — Runway Gen-4.5（来源标注；文中称电影术语也可迁移到 Veo 等） · en · verified · 运镜、官方示例　`camera-motion--44-runway-official-ai-camera-prompts--01`
- [黑石奢侈手表慢速顺时针环绕](prompts/运镜/44-runway-official-ai-camera-prompts.md#2-黑石奢侈手表慢速顺时针环绕product-reveal) — Runway Gen-4.5（来源标注；文中称电影术语也可迁移到 Veo 等） · en · verified · 运镜、官方示例　`camera-motion--44-runway-official-ai-camera-prompts--02`
- [雾中山村日出航拍建立镜头](prompts/运镜/44-runway-official-ai-camera-prompts.md#3-雾中山村日出航拍建立镜头drone-establishing-shot) — Runway Gen-4.5（来源标注；文中称电影术语也可迁移到 Veo 等） · en · verified · 运镜、官方示例　`camera-motion--44-runway-official-ai-camera-prompts--03`
- [未来都市骑行低机位横向跟拍](prompts/运镜/44-runway-official-ai-camera-prompts.md#4-未来都市骑行低机位横向跟拍tracking-action) — Runway Gen-4.5（来源标注；文中称电影术语也可迁移到 Veo 等） · en · verified · 运镜、官方示例　`camera-motion--44-runway-official-ai-camera-prompts--04`
- [午夜空餐厅完全锁定静止镜头](prompts/运镜/44-runway-official-ai-camera-prompts.md#5-午夜空餐厅完全锁定静止镜头static-dramatic) — Runway Gen-4.5（来源标注；文中称电影术语也可迁移到 Veo 等） · en · verified · 运镜、官方示例、技巧锦囊　`camera-motion--44-runway-official-ai-camera-prompts--05`
- [前景水杯拉焦到背景独坐者](prompts/运镜/44-runway-official-ai-camera-prompts.md#6-前景水杯拉焦到背景独坐者rack-focus) — Runway Gen-4.5（来源标注；文中称电影术语也可迁移到 Veo 等） · en · verified · 运镜、官方示例　`camera-motion--44-runway-official-ai-camera-prompts--06`
- [市集街头乐手手持纪录片感](prompts/运镜/44-runway-official-ai-camera-prompts.md#7-市集街头乐手手持纪录片感handheld-documentary) — Runway Gen-4.5（来源标注；文中称电影术语也可迁移到 Veo 等） · en · verified · 运镜、官方示例　`camera-motion--44-runway-official-ai-camera-prompts--07`
- [三拍子① 窄巷建立镜头（锁定俯角）](prompts/运镜/44-runway-official-ai-camera-prompts.md#8-三拍子①-窄巷建立镜头锁定俯角beat-1-establishing) — Runway Gen-4.5（来源标注；文中称电影术语也可迁移到 Veo 等） · en · verified · 运镜、官方示例、分镜/多镜头、技巧锦囊　`camera-motion--44-runway-official-ai-camera-prompts--08`
- [三拍子② 身后跟随者缓慢推进](prompts/运镜/44-runway-official-ai-camera-prompts.md#9-三拍子②-身后跟随者缓慢推进beat-2-push-in) — Runway Gen-4.5（来源标注；文中称电影术语也可迁移到 Veo 等） · en · verified · 运镜、官方示例、分镜/多镜头　`camera-motion--44-runway-official-ai-camera-prompts--09`
- [三拍子③ 街灯下露尖牙特写反转](prompts/运镜/44-runway-official-ai-camera-prompts.md#10-三拍子③-街灯下露尖牙特写反转beat-3-reveal) — Runway Gen-4.5（来源标注；文中称电影术语也可迁移到 Veo 等） · en · verified · 运镜、官方示例、分镜/多镜头　`camera-motion--44-runway-official-ai-camera-prompts--10`

### `prompts/运镜/45-runway-official-camera-terms-examples.md`

- [微距特写（黑蝴蝶翅膀）](prompts/运镜/45-runway-official-camera-terms-examples.md#1-微距特写黑蝴蝶翅膀macro) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--01`
- [大特写（无五官面孔与投影光）](prompts/运镜/45-runway-official-camera-terms-examples.md#2-大特写无五官面孔与投影光extreme-close-up) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--02`
- [特写（象脸白绘纹）](prompts/运镜/45-runway-official-camera-terms-examples.md#3-特写象脸白绘纹close-up) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--03`
- [中景（牛仔坠马）](prompts/运镜/45-runway-official-camera-terms-examples.md#4-中景牛仔坠马medium) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--04`
- [全身（维多利亚女子与迷宫狐狸）](prompts/运镜/45-runway-official-camera-terms-examples.md#5-全身维多利亚女子与迷宫狐狸full) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--05`
- [全景（荒原落日剪影）](prompts/运镜/45-runway-official-camera-terms-examples.md#6-全景荒原落日剪影wide) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--06`
- [大远景（水下峡谷与潜艇）](prompts/运镜/45-runway-official-camera-terms-examples.md#7-大远景水下峡谷与潜艇extreme-wide) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--07`
- [建立镜头（90年代体育馆看台）](prompts/运镜/45-runway-official-camera-terms-examples.md#8-建立镜头90年代体育馆看台establishing) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--08`
- [航拍俯视（风暴中渔船）](prompts/运镜/45-runway-official-camera-terms-examples.md#9-航拍俯视风暴中渔船aerial) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--09`
- [高角度（雾谷红袍圆舞）](prompts/运镜/45-runway-official-camera-terms-examples.md#10-高角度雾谷红袍圆舞high-angle) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--10`
- [低角度（乳白盔甲异形生物）](prompts/运镜/45-runway-official-camera-terms-examples.md#11-低角度乳白盔甲异形生物low-angle) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--11`
- [鸟瞰（白鹭羽层推近）](prompts/运镜/45-runway-official-camera-terms-examples.md#12-鸟瞰白鹭羽层推近birds-eye-view) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--12`
- [蚁视（土坑仰望天空）](prompts/运镜/45-runway-official-camera-terms-examples.md#13-蚁视土坑仰望天空worms-eye-view) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--13`
- [过肩（悬崖望风暴海）](prompts/运镜/45-runway-official-camera-terms-examples.md#14-过肩悬崖望风暴海over-the-shoulder) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--14`
- [主观镜头（熊取蜜）](prompts/运镜/45-runway-official-camera-terms-examples.md#15-主观镜头熊取蜜pov) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--15`
- [引导线（海岸公路巴士）](prompts/运镜/45-runway-official-camera-terms-examples.md#16-引导线海岸公路巴士leading-lines) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--16`
- [框中框（走廊剪影女子）](prompts/运镜/45-runway-official-camera-terms-examples.md#17-框中框走廊剪影女子frame-within-frame) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--17`
- [对称构图（红裙上楼梯）](prompts/运镜/45-runway-official-camera-terms-examples.md#18-对称构图红裙上楼梯symmetrical) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--18`
- [负空间（盐湖红色吉普）](prompts/运镜/45-runway-official-camera-terms-examples.md#19-负空间盐湖红色吉普negative-space) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--19`
- [横摇（松林与湖上小船）](prompts/运镜/45-runway-official-camera-terms-examples.md#20-横摇松林与湖上小船pan) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--20`
- [俯仰（古街到天空）](prompts/运镜/45-runway-official-camera-terms-examples.md#21-俯仰古街到天空tilt-updown) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--21`
- [轨道后拉（巷弄孤影）](prompts/运镜/45-runway-official-camera-terms-examples.md#22-轨道后拉巷弄孤影dolly) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--22`
- [推进（鱼形异形控制台）](prompts/运镜/45-runway-official-camera-terms-examples.md#23-推进鱼形异形控制台push-in) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--23`
- [后拉揭示（微型画手到画室）](prompts/运镜/45-runway-official-camera-terms-examples.md#24-后拉揭示微型画手到画室pull-back) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--24`
- [横移（花田到山顶变景）](prompts/运镜/45-runway-official-camera-terms-examples.md#25-横移花田到山顶变景truck) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--25`
- [跟拍（月球滑板宇航员）](prompts/运镜/45-runway-official-camera-terms-examples.md#26-跟拍月球滑板宇航员tracking) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--26`
- [升降（香水瓶升移）](prompts/运镜/45-runway-official-camera-terms-examples.md#27-升降香水瓶升移pedestal) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--27`
- [摇臂下降（办公室孤影）](prompts/运镜/45-runway-official-camera-terms-examples.md#28-摇臂下降办公室孤影cranejib-boom-updown) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--28`
- [环绕（白蛇柠檬静物）](prompts/运镜/45-runway-official-camera-terms-examples.md#29-环绕白蛇柠檬静物orbit) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--29`
- [变焦后拉（探险者跃涧）](prompts/运镜/45-runway-official-camera-terms-examples.md#30-变焦后拉探险者跃涧zoom) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--30`
- [急推特写（变色龙瞳孔）](prompts/运镜/45-runway-official-camera-terms-examples.md#31-急推特写变色龙瞳孔crash-zoom) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--31`
- [甩镜（黏土侦探到反派）](prompts/运镜/45-runway-official-camera-terms-examples.md#32-甩镜黏土侦探到反派whip-pan) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--32`
- [手持（地震城市）](prompts/运镜/45-runway-official-camera-terms-examples.md#33-手持地震城市handheld) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--33`
- [斯坦尼康（马拉松运动员）](prompts/运镜/45-runway-official-camera-terms-examples.md#34-斯坦尼康马拉松运动员steadicam) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--34`
- [云台（植物园跟拍升空）](prompts/运镜/45-runway-official-camera-terms-examples.md#35-云台植物园跟拍升空gimbal) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--35`
- [静止机位（公寓弹性变形）](prompts/运镜/45-runway-official-camera-terms-examples.md#36-静止机位公寓弹性变形static) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例、运动镜头　`camera-motion--45-runway-official-camera-terms-examples--36`
- [深焦（古董店）](prompts/运镜/45-runway-official-camera-terms-examples.md#37-深焦古董店deep-focus) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--37`
- [柔焦（雾中水边人影）](prompts/运镜/45-runway-official-camera-terms-examples.md#38-柔焦雾中水边人影soft-focus) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--38`
- [焦点转移（厨师到手到食客）](prompts/运镜/45-runway-official-camera-terms-examples.md#39-焦点转移厨师到手到食客rack-focus) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--39`
- [浅景深（铬色气泡）](prompts/运镜/45-runway-official-camera-terms-examples.md#40-浅景深铬色气泡shallow-focus) — Runway Gen-4.5（来源标注 Text to Video） · en · verified · 运镜、官方示例　`camera-motion--45-runway-official-camera-terms-examples--40`

## 特效（17）

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

### `prompts/特效/41-douyin-aiqiqi-force-field-vfx.md`

- [魔法能量场（奇幻短片）](prompts/特效/41-douyin-aiqiqi-force-field-vfx.md#p1--魔法能量场卡片显示-206236-s正文清晰-210234-s) — 未指定（原文未标注生成模型；「UE5.4 渲染」「Octane X 渲染」是渲染器风格词，不是生成模型） · zh+en · verified · 技巧锦囊、特效、力场扰动、能量场、光影联动、空气折射、热浪扭曲、布料/发丝、体积粒子、湍流、奇幻、摄影机/渲染词　`vfx--41-douyin-aiqiqi-force-field-vfx--01`
- [爆炸冲击波（灾难 / 科幻战斗镜头）](prompts/特效/41-douyin-aiqiqi-force-field-vfx.md#p2--爆炸冲击波卡片显示-284310-s正文清晰-288308-s) — 未指定（原文未标注生成模型；「UE5.4 渲染」「Octane X 渲染」是渲染器风格词，不是生成模型） · zh+en · verified · 技巧锦囊、特效、力场扰动、冲击波、爆炸、空气压缩、风压、空气折射、色散、体积烟尘、物理流体、灾难/科幻、渲染词　`vfx--41-douyin-aiqiqi-force-field-vfx--02`
- [沙漠熔岩高温热浪](prompts/特效/41-douyin-aiqiqi-force-field-vfx.md#p3--沙漠熔岩高温热浪卡片显示-346368-s正文清晰-350366-s) — 未指定（原文未标注生成模型；「UE5.4 渲染」「Octane X 渲染」是渲染器风格词，不是生成模型） · zh+en · verified · 技巧锦囊、特效、力场扰动、热浪、地热、热对流、空气折射、色散、热雾、光影联动、长焦、胶片质感　`vfx--41-douyin-aiqiqi-force-field-vfx--03`

## 光影打光（2）

以打光为主要看点的提示词：光源时段、方位角度、软硬、色温与光型（逆光、伦勃朗光、丁达尔光柱等）

### `prompts/光影打光/40-douyin-aiqiqi-lighting-prompts.md`

- [日落前 20 分钟魔幻时刻：右后方 45 度逆光发丝与暖色轮廓光](prompts/光影打光/40-douyin-aiqiqi-lighting-prompts.md#p1--日落前-20-分钟魔幻时刻逆光打字-416512-s完整显示-512544-s) — 即梦 Seedance 2.0 Fast（画面中生成界面显示「视频生成」「即梦 Seedance 2.0 Fast VIP」「全能参考」；作者未另外说明） · zh · verified · 光影打光、逆光、轮廓光、黄金时刻/魔幻时刻、光源方位、发丝光、天空渐变　`lighting--40-douyin-aiqiqi-lighting-prompts--01`
- [赛博朋克双色光：右侧霓虹粉光 + 左侧冷蓝补光，面部锐利分界线](prompts/光影打光/40-douyin-aiqiqi-lighting-prompts.md#p2--赛博朋克双色霓虹光打字-730804-s完整显示-804806-s) — 即梦 Seedance 2.0 Fast（画面中生成界面显示「视频生成」「即梦 Seedance 2.0 Fast VIP」「全能参考」；作者未另外说明） · zh · verified · 光影打光、赛博朋克、霓虹、双色光、补光、分界线　`lighting--40-douyin-aiqiqi-lighting-prompts--02`

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

## 首尾帧生图（43）

给图生视频准备首帧 / 尾帧 / 关键帧 / 角色参考图的生图与编辑方法，以及首尾帧之间的视频提示词（以厂商官方示例为主）

### `prompts/首尾帧生图/01-openai-gpt-image-official.md`

- [写实首帧：老水手（主体 + 取景 + 光线 + 质感）](prompts/首尾帧生图/01-openai-gpt-image-official.md#1-control-style-and-lighting--写实人像首帧老水手) — GPT Image 2.5（官方指南示例；Flare / Sunburst） · en · verified · 首帧　`keyframe-image--01-openai-gpt-image-official--01`
- [保身份只换衣服（锁脸、锁姿势、锁机位）](prompts/首尾帧生图/01-openai-gpt-image-official.md#2-preserve-identity-and-change-clothing--保身份只换衣服) — GPT Image 2.5（官方指南示例） · en · verified · 参考图/素材引用、角色一致性、图像编辑　`keyframe-image--01-openai-gpt-image-official--02`
- [多图合成：把图 2 的主体放进图 1（光线与构图不变）](prompts/首尾帧生图/01-openai-gpt-image-official.md#3-combine-references--多图合成) — GPT Image 2.5（官方指南示例） · en · verified · 参考图/素材引用、图像编辑　`keyframe-image--01-openai-gpt-image-official--03`
- [草图 / 分镜线稿转写实首帧](prompts/首尾帧生图/01-openai-gpt-image-official.md#4-turn-a-drawing-into-a-realistic-image--草图转写实) — GPT Image 2.5（官方指南示例） · en · verified · 图像编辑　`keyframe-image--01-openai-gpt-image-official--04`
- [删除一个物体，其余不变](prompts/首尾帧生图/01-openai-gpt-image-official.md#5-remove-an-object--删除一个物体) — GPT Image 2.5（官方指南示例） · en · verified · 图像编辑　`keyframe-image--01-openai-gpt-image-official--05`
- [人物放进新场景（保身份，要真实照片感）](prompts/首尾帧生图/01-openai-gpt-image-official.md#6-insert-a-person-into-a-scene--人物放进新场景) — GPT Image 2.5（官方指南示例） · en · verified · 参考图/素材引用、角色一致性　`keyframe-image--01-openai-gpt-image-official--06`
- [只改一个条件：同一画面改成冬夜下雪](prompts/首尾帧生图/01-openai-gpt-image-official.md#7-change-one-condition--只改一个条件) — GPT Image 2.5（官方指南示例） · en · verified · 图像编辑、首尾帧、技巧锦囊　`keyframe-image--01-openai-gpt-image-official--07`
- [建立可复用的角色参考图](prompts/首尾帧生图/01-openai-gpt-image-official.md#8-keep-a-character-consistent--建立角色) — GPT Image 2.5（官方指南示例） · en · verified · 角色一致性　`keyframe-image--01-openai-gpt-image-official--08`
- [角色延续到新场景（重复外观约束）](prompts/首尾帧生图/01-openai-gpt-image-official.md#9-keep-a-character-consistent--延续角色到新场景) — GPT Image 2.5（官方指南示例） · en · verified · 角色一致性、参考图/素材引用　`keyframe-image--01-openai-gpt-image-official--09`

### `prompts/首尾帧生图/02-google-gemini-veo-official.md`

- [写实场景模板（镜头类型 + 主体 + 场景 + 光线 + 机位 + 镜头）](prompts/首尾帧生图/02-google-gemini-veo-official.md#1-photorealistic-scenes--模板) — Gemini 图像模型（Nano Banana 系列，官方指南模板） · en · verified · 首帧　`keyframe-image--02-google-gemini-veo-official--01`
- [写实场景示例：珊瑚礁（写明 16:9）](prompts/首尾帧生图/02-google-gemini-veo-official.md#2-photorealistic-scenes--示例) — Gemini 图像模型（官方指南示例） · en · verified · 首帧、横屏16:9　`keyframe-image--02-google-gemini-veo-official--02`
- [语义蒙版：只改一处，其余完全不变](prompts/首尾帧生图/02-google-gemini-veo-official.md#3-inpainting-semantic-masking--只改一处) — Gemini 图像模型（官方指南示例） · en · verified · 图像编辑　`keyframe-image--02-google-gemini-veo-official--03`
- [编辑时保住脸和关键细节（先把要保的细节写详细）](prompts/首尾帧生图/02-google-gemini-veo-official.md#4-high-fidelity-detail-preservation--保细节) — Gemini 图像模型（官方指南示例） · en · verified · 图像编辑、角色一致性、参考图/素材引用　`keyframe-image--02-google-gemini-veo-official--04`
- [角色多角度：一次只要一个角度（360 view）](prompts/首尾帧生图/02-google-gemini-veo-official.md#5-character-consistency-360-view--逐个角度生成) — Gemini 图像模型（官方指南示例） · en · verified · 角色一致性、参考图/素材引用、技巧锦囊　`keyframe-image--02-google-gemini-veo-official--05`
- [Veo 3.1 首尾帧：秋千上的幽灵逐渐消失](prompts/首尾帧生图/02-google-gemini-veo-official.md#6-veo-31--首尾帧插值示例) — Veo 3.1（Gemini API 官方示例） · en · verified · 首尾帧　`keyframe-image--02-google-gemini-veo-official--06`
- [Veo 首尾帧（Vertex）：一只手伸进来放下牛奶](prompts/首尾帧生图/02-google-gemini-veo-official.md#7-veovertex-首尾帧示例) — Veo（Gemini Enterprise Agent Platform / Vertex 官方示例） · en · verified · 首尾帧　`keyframe-image--02-google-gemini-veo-official--07`

### `prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md`

- [Seedream：主体 + 行为 + 环境 + 风格（推荐写法）](prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md#1-seedream-通用规则-1--自然语言描述画面) — Seedream 5.0 lite / 4.5 / 4.0（官方指南示例） · zh · verified · —　`keyframe-image--03-volcengine-seedream-seedance-official--01`
- [Seedream 编辑：指明对象 + 改什么 + 保持动作不变](prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md#2-seedream-通用规则-5--编辑目标--保持不变) — Seedream 5.0 lite / 4.5 / 4.0（官方指南示例） · zh · verified · 图像编辑　`keyframe-image--03-volcengine-seedream-seedance-official--02`
- [Seedream 编辑：替换主体，保持动作和表情](prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md#3-seedream-图像编辑--替换并保持动作表情) — Seedream 5.0 lite / 4.5 / 4.0（官方指南示例） · zh · verified · 图像编辑　`keyframe-image--03-volcengine-seedream-seedance-official--03`
- [Seedream 编辑：按位置分别指定每个主体的动作](prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md#4-seedream-图像编辑--改材质并分别改动作) — Seedream 5.0 lite / 4.5 / 4.0（官方指南示例） · zh · verified · 图像编辑、首尾帧　`keyframe-image--03-volcengine-seedream-seedance-official--04`
- [Seedream 参考图生图：指明参考对象 + 描述新画面](prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md#5-seedream-参考图生图--参考人物形象) — Seedream 5.0 lite / 4.5 / 4.0（官方指南示例） · zh · verified · 参考图/素材引用、角色一致性　`keyframe-image--03-volcengine-seedream-seedance-official--05`
- [Seedream 多图输入：图一人物穿图二服装](prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md#6-seedream-多图输入--组合) — Seedream 5.0 lite / 4.5 / 4.0（官方指南示例） · zh · verified · 参考图/素材引用　`keyframe-image--03-volcengine-seedream-seedance-official--06`
- [Seedream 组图：一次生成四张连贯的影视分镜](prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md#7-seedream-多图输出--影视分镜组图) — Seedream 5.0 lite / 4.5 / 4.0（官方指南示例） · zh · verified · 分镜/多镜头、关键帧　`keyframe-image--03-volcengine-seedream-seedance-official--07`
- [Seedream 参考图生组图：同一人物四种状态](prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md#8-seedream-参考图生组图--同一人物四种状态) — Seedream 5.0 lite / 4.5 / 4.0（官方教程 API 示例） · zh · verified · 参考图/素材引用、角色一致性、关键帧　`keyframe-image--03-volcengine-seedream-seedance-official--08`
- [Seedance 2.5：在提示词里指定首帧 / 尾帧（reference_image 方式）](prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md#9-seedance-25--首尾帧指代句式) — Seedance 2.5（官方指南示例） · zh · verified · 首尾帧、参考图/素材引用　`keyframe-image--03-volcengine-seedream-seedance-official--09`
- [Seedance 2.5 关键帧：第一句写明「以图片 x 至图片 x 的顺序作为关键帧」](prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md#10-seedance-25--关键帧参考灵鱼) — Seedance 2.5（官方指南示例） · zh · verified · 关键帧、参考图/素材引用、分镜/多镜头　`keyframe-image--03-volcengine-seedream-seedance-official--10`
- [Seedance 2.5 线稿分镜：素材绑定 → 逐镜补齐动作与构图](prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md#11-seedance-25--线稿分镜故事板) — Seedance 2.5（官方指南示例） · zh · verified · 分镜/多镜头、参考图/素材引用　`keyframe-image--03-volcengine-seedream-seedance-official--11`
- [Seedance 2.5 概念分镜：分镜已是关键帧设计时可简写](prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md#12-seedance-25--概念分镜简写) — Seedance 2.5（官方指南示例） · zh · verified · 分镜/多镜头　`keyframe-image--03-volcengine-seedream-seedance-official--12`
- [Seedance 2.0：脸参考大头照、妆造参考全身照](prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md#13-seedance-20--大头照--全身照的主体定义) — Seedance 2.0（官方指南 FAQ） · zh · verified · 角色一致性、参考图/素材引用　`keyframe-image--03-volcengine-seedream-seedance-official--13`

### `prompts/首尾帧生图/04-bfl-flux-official.md`

- [FLUX 3 首尾帧：城市日转夜](prompts/首尾帧生图/04-bfl-flux-official.md#1-start--end-frame--city-day-to-night) — FLUX 3（BFL 官方视频指南示例） · en · verified · 首尾帧　`keyframe-image--04-bfl-flux-official--01`
- [FLUX 3 首尾帧：墨水颜色渐变](prompts/首尾帧生图/04-bfl-flux-official.md#2-start--end-frame--ink-in-motion) — FLUX 3（BFL 官方视频指南示例） · en · verified · 首尾帧　`keyframe-image--04-bfl-flux-official--02`
- [FLUX 3 三关键帧：极光变色（0s / 2.5s / 5s）](prompts/首尾帧生图/04-bfl-flux-official.md#3-keyframes--aurora) — FLUX 3（BFL 官方视频指南示例） · en · verified · 关键帧　`keyframe-image--04-bfl-flux-official--03`
- [FLUX.2 单图编辑：改成夜晚（做尾帧）](prompts/首尾帧生图/04-bfl-flux-official.md#4-single-reference--change-it-to-night) — FLUX.2（BFL 官方编辑指南示例） · en · verified · 图像编辑、首尾帧　`keyframe-image--04-bfl-flux-official--04`
- [FLUX.2 单图编辑：只改视线方向](prompts/首尾帧生图/04-bfl-flux-official.md#5-single-reference--looking-at-the-camera) — FLUX.2（BFL 官方编辑指南示例） · en · verified · 图像编辑、首尾帧　`keyframe-image--04-bfl-flux-official--05`
- [FLUX.2 多图编辑：迁移图 2 的外观，保持图 1 的姿势、光线、构图](prompts/首尾帧生图/04-bfl-flux-official.md#6-multi-reference--keep-pose-lighting-and-composition) — FLUX.2（BFL 官方编辑指南示例） · en · verified · 图像编辑、参考图/素材引用　`keyframe-image--04-bfl-flux-official--06`
- [FLUX.2 插画转写实：比例和布局完全保持](prompts/首尾帧生图/04-bfl-flux-official.md#7-single-reference--illustration-to-realistic) — FLUX.2（BFL 官方编辑指南示例） · en · verified · 图像编辑　`keyframe-image--04-bfl-flux-official--07`

### `prompts/首尾帧生图/05-runway-official.md`

- [Runway 图生视频：只写运动（机位运动 + 主体动作）](prompts/首尾帧生图/05-runway-official.md#1-image-to-video--结构示例) — Runway Gen-4.5（官方 Image to Video Prompting Guide 示例） · en · verified · 首帧　`keyframe-image--05-runway-official--01`
- [Runway：首帧里的运动暗示会和提示词打架](prompts/首尾帧生图/05-runway-official.md#2-image-to-video-faq--与画面运动暗示相反的提示) — Runway Gen-4.5（官方 FAQ 示例） · en · verified · 首帧、技巧锦囊　`keyframe-image--05-runway-official--02`
- [Runway：让镜头尽量静止的三句](prompts/首尾帧生图/05-runway-official.md#3-image-to-video-faq--减少运动) — Runway Gen-4.5（官方 FAQ 示例） · en · verified · 首帧　`keyframe-image--05-runway-official--03`
- [Runway Gen-4 References：用 @名字 调用保存的角色参考](prompts/首尾帧生图/05-runway-official.md#4-gen-4-references--单参考图) — Runway Gen-4 Image References（官方示例） · en · verified · 参考图/素材引用、角色一致性　`keyframe-image--05-runway-official--04`
- [Runway Gen-4 References：同一场景换角度 / 补 B-roll](prompts/首尾帧生图/05-runway-official.md#5-gen-4-references--一致场景) — Runway Gen-4 Image References（官方示例） · en · verified · 参考图/素材引用　`keyframe-image--05-runway-official--05`

### `prompts/首尾帧生图/06-aliyun-wan-official.md`

- [万相 3.0 首尾帧：起止画面已定，提示词写中间的剧情与运镜](prompts/首尾帧生图/06-aliyun-wan-official.md#1-wan-30--首尾帧生视频四镜头) — 通义万相 wan3.0（阿里云百炼官方指南示例） · zh · verified · 首尾帧、分镜/多镜头、时间码分段　`keyframe-image--06-aliyun-wan-official--01`
- [万相 3.0：首帧 / 尾帧 + 参考视频的 LOGO 动画](prompts/首尾帧生图/06-aliyun-wan-official.md#2-wan-30--首尾帧-logo-生长) — 通义万相 wan3.0（阿里云百炼官方指南示例） · zh · verified · 首尾帧、参考图/素材引用　`keyframe-image--06-aliyun-wan-official--02`

## 人物卡（13）

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

### `prompts/人物卡/40-douyin-ksr-midjourney-stylize-personalize.md`

- [森系电竞女角色定妆半身照（中文直输版）](prompts/人物卡/40-douyin-ksr-midjourney-stylize-personalize.md#p1--森系电竞女角色定妆照中文直输版) — Midjourney V8.1（原文参数 --v 8.1 --raw；画面中粘贴到 Midjourney 网页版生成） · zh+en · verified · 技巧锦囊、人物卡、角色定妆照、Midjourney、中文直输、参数后缀、负面约束、动机光、摄影机/胶片词、双风格拼贴　`character-card--40-douyin-ksr-midjourney-stylize-personalize--01`
- [奇幻科幻糖果花城全景（中文直输版）](prompts/人物卡/40-douyin-ksr-midjourney-stylize-personalize.md#p2--糖果花城全景中文直输版) — Midjourney V8.1（原文参数 --v 8.1 --raw --hd；画面中粘贴到 Midjourney 网页版生成） · zh+en · verified · 技巧锦囊、场景概念图、Midjourney、中文直输、参数后缀、负面约束、俯拍鸟瞰、超广角、色彩策略、微缩模型质感、摄影机/镜头词　`character-card--40-douyin-ksr-midjourney-stylize-personalize--02`

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

## 提示词写法（13）

提示词写法方法论、公式与官方示例

### `prompts/提示词写法/01-web-prompt-writing-methodology.md`

- [优化后城市街头示例](prompts/提示词写法/01-web-prompt-writing-methodology.md#13-优化后城市街头示例) — 未指定（通用写法） · zh · verified · 横屏16:9、手持　`prompt-writing--01-web-prompt-writing-methodology--01`
- [通用负面](prompts/提示词写法/01-web-prompt-writing-methodology.md#14-通用负面) — 未指定（通用写法） · zh · verified · —　`prompt-writing--01-web-prompt-writing-methodology--02`
- [城市漫游模板](prompts/提示词写法/01-web-prompt-writing-methodology.md#15-城市漫游模板) — 未指定（通用写法） · zh · verified · 横屏16:9　`prompt-writing--01-web-prompt-writing-methodology--03`
- [产品广告模板](prompts/提示词写法/01-web-prompt-writing-methodology.md#16-产品广告模板) — 未指定（通用写法） · zh · verified · 产品/广告　`prompt-writing--01-web-prompt-writing-methodology--04`
- [主体定义句式](prompts/提示词写法/01-web-prompt-writing-methodology.md#22-主体定义句式) — Seedance 2.0（来源标注） · zh · verified · —　`prompt-writing--01-web-prompt-writing-methodology--05`
- [主体定义句式（2）](prompts/提示词写法/01-web-prompt-writing-methodology.md#22-主体定义句式) — Seedance 2.0（来源标注） · zh · verified · —　`prompt-writing--01-web-prompt-writing-methodology--06`
- [正面约束模板](prompts/提示词写法/01-web-prompt-writing-methodology.md#33-正面约束模板) — Seedance 2.0（来源标注） · zh · verified · —　`prompt-writing--01-web-prompt-writing-methodology--08`
- [Seedance 2.0 推荐（序号式）](prompts/提示词写法/01-web-prompt-writing-methodology.md#42-seedance-20-推荐序号式) — Seedance 2.5（来源标注） · zh · verified · 分镜/多镜头　`prompt-writing--01-web-prompt-writing-methodology--09`
- [Seedance 2.5 推荐（秒级时间戳）](prompts/提示词写法/01-web-prompt-writing-methodology.md#43-seedance-25-推荐秒级时间戳) — Seedance 2.5（来源标注） · zh · verified · 时间码分段　`prompt-writing--01-web-prompt-writing-methodology--10`

### `prompts/提示词写法/32-runway-seedance-2.0-prompt-guide.md`

- [八要素示例 · 陶艺师](prompts/提示词写法/32-runway-seedance-2.0-prompt-guide.md#1-八要素示例--陶艺师eight-elements-ceramicist-example) — Seedance 2.0（来源标注） · en · verified · —　`prompt-writing--32-runway-seedance-2.0-prompt-guide--01`

### `prompts/提示词写法/33-official-vendor-video-examples.md`

- [Seedance 2.0 官方示例 1：宿舍情感短剧（偏文戏 / 对话）](prompts/提示词写法/33-official-vendor-video-examples.md#1-seedance-20-官方示例-1--宿舍情感短剧) — Seedance 2.0（官方指南示例） · zh · verified · 分镜/多镜头、参考图/素材引用、音频/音效、台词/对白　`prompt-writing--33-official-vendor-video-examples--01`
- [Veo 主提示词（配合下一条负面提示）](prompts/提示词写法/33-official-vendor-video-examples.md#2-veo-官方示例--负面提示名词列表) — Veo（Google Cloud 官方提示词指南示例） · en · verified · —　`prompt-writing--33-official-vendor-video-examples--02`
- [Veo 负面提示词：只列不想要的东西，不写 no / don't](prompts/提示词写法/33-official-vendor-video-examples.md#3-veo-官方示例--负面提示词) — Veo（Google Cloud 官方提示词指南示例） · en · verified · 负面约束　`prompt-writing--33-official-vendor-video-examples--03`

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
