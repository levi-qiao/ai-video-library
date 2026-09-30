# Douyin 图文 blockers（视觉誊写未达标）

硬规则：**禁止编造**提示词正文。宁可 incomplete + blocker。

## Tct4dNh1dzo / 小椰冻奶 · 法天象地

- short: https://v.douyin.com/Tct4dNh1dzo/
- note: `7689872479989721957`
- 状态: **仍未入库 verbatim**
- 已做到: Playwright 打开 `m.douyin.com` / `iesdouyin` share，抓到 **2 张** 图文配图（480×640 webp），见本目录 `Tct4dNh1dzo-img0{0,1}-480x640.png`
- 未做到: 更高分辨率变体均 403；480px 上密排中文经多次视觉识读 **字符不一致**（无法保证 character-accurate），故 **不** 写入 `prompts/` 正文
- 对照等价公开源（非本作者）: `prompts/特效/30-freyavideo.com.md`（FreyaVideo 法天象地）
- 2026-09-29 晚间 QC 重读 `Tct4dNh1dzo-img00` 与 `img01`（480×640）。两张都是密排分镜字，字号小、压缩糊、部分行被裁切。**仍然无法逐字确认全文**，因此 **不** 写入 `prompts/`，也不把不确定识读当 verbatim。

## D28NAIbzFm0 / 小鱼漫剧 · AI漫剧打斗

- short: https://v.douyin.com/D28NAIbzFm0/
- note: `7687528916584719195`
- 状态: share / m.douyin 均「抱歉出错了」，**无配图、无正文**

## 心流人物卡短链

- `v.douyin.com/F0CQtRHUZQk/` / `bV59188e3cE/` / `UP3Ck9IsM_U/`
- 状态: 仍 blocker；`bV59188e3cE` 重定向到无关图文，不可当作心流人物卡原文

## mM3gTkJWuzQ / AI绘梦菌 · AI提示词编写思路

- short: https://v.douyin.com/mM3gTkJWuzQ/
- video_id: `7690573169337453860`
- content_type: **video**（非图文）
- 状态: **仍未入库 verbatim** — 口播/字幕/画面字 **0 chars**（SSR shell 与 item API 均为空）
- 详见: `douyin-mM3gTkJWuzQ-AI绘梦菌.md`
- 公开方法论替代（**不是**该抖音正文）: `prompts/提示词写法/01-web-prompt-writing-methodology.md`

## -aQ762F_Y4k / 胡小绿 · 1个视频让你学会用AI提示词控制画面景别（2026-09-30）

- short: https://v.douyin.com/-aQ762F_Y4k/
- video_id: `7685608233369056433`
- content_type: **video**（16.5 s，无口播）
- 状态: **已入库（部分）** → `prompts/运镜/43-douyin-huxiaolv-shot-size-jingbie.md`：帖子文案逐字、画面字幕 image-transcript（16 条逐镜标注）、ASR（无人声）、互动数。
- 仍 blocker: **完整提示词未公开**。画面字幕只是逐镜标注，不是完整提示词；评论区作者回复「发会员群里了咧王总」，推断完整内容只在会员群。未编造、未计入 ` ```text `。
- 文案后半段换行不可见（网页 h1 去掉换行，meta 截断），按 h1 连排保存。
- 可复用的获取方法（本次首次成功拿到抖音 mp4）: 无头 Chrome（Playwright，xvfb）打开 `www.douyin.com` 取**未登录匿名 cookie** → `yt-dlp --cookies <netscape.txt>`；文案用 Googlebot UA 抓 `www.douyin.com/video/<id>` SSR 的 h1/meta。iesdouyin 分享页 `_ROUTER_DATA` 仍为空壳。该方法未在 `mM3gTkJWuzQ` 上重试。

## YqR-LBuk33I / 胡小绿 · 1个视频让你学会用AI提示词控制打斗画面（2026-09-30）

- short: https://v.douyin.com/YqR-LBuk33I/
- video_id: `7689064641665748270`
- content_type: **video**（27.2 s，无口播，配乐「鞋兒破帽兒破」）
- 状态: **已入库（部分）** → `prompts/打斗运镜/33-douyin-huxiaolv-fight-control-jigong.md`：帖子文案逐字（换行完整）、画面字幕 image-transcript（11 条逐镜标注）、ASR（无人声）、互动数、相关评论。
- 仍 blocker: **完整提示词未公开**。画面字幕只是逐镜标注，不是完整提示词。评论「老师可以看看完整提示词吗」下抓取时看不到作者回复；作者在另一楼回复「没给 词控的」（指金龙没用参考图）。是否在会员群，无公开证据。未编造、未计入 ` ```text `。
- 楼中楼回复（全岛锈盒楼 5 条、.零楼 1 条、V 楼 3 条）未抓到：无头浏览器展开时出现登录框 + 滑块验证，未绕过。
- 景别标签里的箭头按字形记为 `→`（U+2192），像素无法区分长箭头码位。
- 获取方法同 `-aQ762F_Y4k`（匿名 cookie + `yt-dlp --cookies`；Googlebot UA 抓 SSR）。本条 detail JSON 的 `desc` 未截断。

## wCMSOojlXnU / 孔明AI剧社 · 各类武器基础武戏动作提示词分享（2026-09-30）

- short: https://v.douyin.com/wCMSOojlXnU/
- note: `7662990755169914127`
- content_type: **图文**（5 张：01 3000×4000，02–05 1086×1448，接口最大尺寸）
- 状态: **已入库（部分）** → `prompts/打斗运镜/32-douyin-kongming-weapon-fight.md`：帖子文案逐字、5 张图 20 条提示词逐字誊写（+20 ` ```text `）。
- 仍 blocker: 图 3（仙侠剑招，文字为 AI 渲染）有 **3 个畸变字** 无法确认，围栏内标 `【?】`，未补字：
  1. 「2）万剑归宗」第 4 行「冲击力【?】层层叠加」→ `wCMSOojlXnU-img03-g1-chongjili-X-cengceng.png`
  2. 「2）万剑归宗」第 5 行「剑气【?】鸣」（形近「轰」但结构不符）→ `wCMSOojlXnU-img03-g2-jianqi-X-ming.png`
  3. 「3）引雷剑」末行「剑【?】气鸣震天」（口字旁，形近「咆」但不能确认）→ `wCMSOojlXnU-img03-g3-jian-X-qiming.png`
- 这 3 处是字形本身畸变，不是分辨率不够；同图其他字都能逐字确认。拿到作者原始文本（例如作者在评论区或其他渠道发的文字版）后可替换。
- 获取方法: iesdouyin 分享页 `_ROUTER_DATA` 空壳；`yt-dlp --cookies`（匿名 cookie）对该 note 返回 403「Fresh cookies needed」。可行的是 Googlebot UA 抓 `www.douyin.com/note/<id>` SSR（文案/作者/日期），再用 Playwright 无头 Chrome 打开 note 页，从内嵌 `self.__pace_f.push` 数据解出 aweme detail（互动数、图片 `url_list`）并直接下载原图。

## 8ojgj2g3UDs / AI研究院-爆老师 · AI打斗别乱剪！用好一镜到底（2026-09-30）

- short: https://v.douyin.com/8ojgj2g3UDs/
- video_id: `7689821368011241832`
- content_type: **video**（33.5 s，无口播，配乐「WDF FUNK！」）
- 状态: **已入库（部分）** → `prompts/打斗运镜/34-douyin-baolaoshi-one-take-fight.md`：帖子文案逐字（2026-09-30 整合决定：文案不是提示词，放在无语言代码块，不计数）、画面文字 34 项 image-transcript（两遍 0 差异）、ASR（无口播）、互动数、相关评论。
- 仍 blocker: **完整提示词未公开**。片尾字卡「完整写法 在评论区」；作者回复「评论区和群里发了 可以自取哈[比心]」「评论区和粉丝群都发了哈[比心]」「已发[比心]」。匿名 SSR 只给 10 条顶层评论 + 3 条作者回复，其中没有提示词；其余 65 条评论和楼中楼在无头浏览器里被登录框 + 滑块验证挡住，未绕过。未编造、未计入 ` ```text `。
- 字形: 英文行「HANDHELD」「DUST」「CROWD」所用字体 D 与 O 几乎同形，按词义读出 → `8ojgj2g3UDs-glyph-O-vs-D-evidence.png`；分隔点记为 `·`（U+00B7），像素无法区分 `·` / `・` / `•`。
- 获取方法: 第一次 `yt-dlp --cookies`（匿名 cookie）403；重新取匿名 cookie 后成功。无头 Chrome 直接开视频页时 detail 接口返回「Blocked by ArgusSecurityPlugin Sign Invalid」，页面换成了推荐流里的别的视频，这时抓到的媒体地址不能用。文案用 Googlebot UA 抓 SSR；web detail JSON 的 `desc` 截断。

## l63b3G_ozGw / AI琪琪 · AI进阶学习 | 力场模拟 解决 AI 特效廉价贴图感（2026-09-30）

- short: https://v.douyin.com/l63b3G_ozGw/
- video_id: `7688284716386028840`
- content_type: **video**（54 s，有口播）
- 状态: **已入库** → `prompts/特效/41-douyin-aiqiqi-force-field-vfx.md`：3 张提示词卡逐字誊写（+3 ` ```text `，三遍一致）、帖子文案（2026-09-30 整合决定：文案不是提示词，放无语言代码块，不计数）、画面文字、ASR、评论。
- 仍需注意:
  1. 没有作者文字版，提示词来自视频画面誊写。
  2. P3 末尾「Field」在行尾，与下一行「力场扰动模拟」之间的半角空格为推定 → `l63b3G_ozGw-P3-Field-linewrap-x2.png`
  3. P1「ARRI」末字母字形与小写 l 相同，按品牌名记 I → `l63b3G_ozGw-P1-ARRI-Alexa-glyph-x3.png`
  4. 背景影片自带中英字幕被遮挡（不是提示词），标 `【?】` → `l63b3G_ozGw-bgsub-27.8s-occluded.png`、`l63b3G_ozGw-bgsub-31.6s-occluded.png`、`l63b3G_ozGw-bgsub-30.6s-attacking-gap-x3.png`
  5. 评论区多条「666求一个」，疑有私发资料；视频与文案未提领取方式，无公开证据。「展开1条回复」未展开。

## DovMrdo1J0o / AI琪琪 · 不要再写3D国漫了，想要电影感AI视频试试这套混合媒介指令（2026-09-30）

- short: https://v.douyin.com/DovMrdo1J0o/
- video_id: `7663851807801625908`
- content_type: **video**（97 s，有口播）
- 状态: **已入库** → `prompts/技巧锦囊/44-douyin-aiqiqi-hybrid-media-cinematic.md`：A / B / C 三段提示词逐帧誊写（+3，两遍一致）。
- 仍 blocker:
  1. A 段打字时画面平移，「……CG人物光照与背」之后几个字从未完整出现在画面内，记【?】；字幕与口播为「背景完全匹配」 → `DovMrdo1J0o-A-offscreen-span-37.8-40.0s.png`
  2. 片尾「混合媒介风格」模板文档右半边被画面裁掉、正文被大字幕压住，只收小标题；完整模板作者以评论「666」领取，无公开文字版 → `DovMrdo1J0o-template-doc-cropped-82.2s.png`
  3. 8.6–10.0 s 选中的长文字左右被裁，只作片段 → `DovMrdo1J0o-M-paragraph-edges-cropped-9.4s.png`
  4. 片尾花字「每天教你一个AI【?】知识」，存疑字形像「泠」，口播为「冷」（不是提示词） → `DovMrdo1J0o-outro-glyph-before-zhishi-x2.png`
  5. C 段打字结束帧（75.2 s）结尾完整，作为完整性证据 → `DovMrdo1J0o-C-typing-cut-75.2s.png`
- 获取方法: 移动端 UA 解析短链；有界面 Chrome 先开首页再开视频页取匿名 cookie → `yt-dlp --cookies`（前几次 403，刷新 cookie 后成功，HEVC 720p）；Googlebot UA 抓 SSR 拿文案、互动数（含收藏「2.0万」）、发布时间与评论。

## AI琪琪 主页作品列表（2026-09-30）

- sec_uid: `MS4wLjABAAAA68boldsaVKNbHb-GjzNXbadMba7g00NUB_U89WeE0trMOG8B2F11V86T36BrGmyC`（取自 aweme detail 的作者字段）
- 能拿到: 主页资料接口（`user/profile/other`）返回 作品 61 / 粉丝 9,731 / 获赞 59,927、简介。
- 拿不到: 作品列表。`www.douyin.com/aweme/v1/web/aweme/post/` 与 `iesdouyin.com/web/api/v2/aweme/post/` 匿名访问均为 HTTP 200 空内容；有界面 Chrome 打开主页与视频页都弹出「Log in to Douyin」和滑块验证码；Googlebot / Baiduspider / bingbot UA 抓主页返回 JS 挑战页（`Blocked by ArgusSecurityPlugin Uifid Not Found`）；搜狗、Bing 搜索没有索引到该账号的其他作品。**未尝试绕过验证码。**
- 本轮确认的作品（3 条）：`7663851807801625908` 混合媒介（本批 `技巧锦囊/44`）；`7688284716386028840` 力场模拟（`特效/41`，另一任务）；`7663321309908143406`「打光指令」（6,008 赞，另一任务处理，已入库为 `光影打光/40`，见下一节）。
- 解决办法: 用户在 box 浏览器里登录抖音后重跑（登录状态会保留）；或直接提供想收录的作品分享链接。

## eGqNpizHAi0 / AI琪琪 · 别人一张图氛围拉满，你的是平光大头照？差距就在提示词里的“打光指令（2026-09-30）

- short: https://v.douyin.com/eGqNpizHAi0/
- video_id: `7663321309908143406`
- content_type: **video**（约 105.7 s，有口播）
- 状态: **已入库** → `prompts/光影打光/40-douyin-aiqiqi-lighting-prompts.md`：P1、P2 两段输入框打字提示词逐帧誊写（+2，三遍一致）、帖子文案、画面文字、ASR（6 处同音修正）、评论。
- 仍 blocker:
  1. 10.2–16.8 s 滚动的多维度模板文档（口播「暗号333直接领走」）左右被卡片裁掉，只收「打光方案」一节的片段（16 行，8 处【?】，两遍一致），不计数 → `eGqNpizHAi0-doc-lighting-head-12.6s-x2.png`、`eGqNpizHAi0-doc-lighting-right-edge-12.6-14.4s-x3.png`、`eGqNpizHAi0-doc-lighting-left-edge-14.4s-x3.png`。完整模板无公开文字版，评论区多条「333」索取，看不到作者回复。
  2. 口播念出的伦勃朗光、窗口光柱 / 丁达尔、硬光、柔光四组写法只有 ASR 与分句字幕，没有作者文字版和标点，放无语言代码块，不计数。
  3. P1「紫兰」、P2「反双光」是输入法选字，照输入框原样收录（字幕与口播为「紫蓝」「反光」）。
- 获取方法: 同 `l63b3G_ozGw`（匿名 cookie + `yt-dlp --cookies`，首次 403、刷新 cookie 后成功；HEVC 720p + H.264 720p；Googlebot UA 抓 SSR）。

## zg6RGFH-jUQ / Ksr桑 · 吊打99%付费！原来做AI视频能这么简单？（2026-09-30）

- short: https://v.douyin.com/zg6RGFH-jUQ/
- video_id: `7690677900311285032`
- content_type: **video**（669.1 s，有口播）
- 状态: **已入库** → `prompts/人物卡/40-douyin-ksr-midjourney-stylize-personalize.md`：扣子智能体回复里的两段【中文直输版】Midjourney 提示词逐帧誊写（+2，三遍核对 0 差异）、帖子文案、请求与思路、画面文字选录、ASR（55 处修正）、评论。
- 仍 blocker:
  1. 两段【英文版】都只露出开头（P1 9 行、P2 7 行），下面被扣子输入框挡住，全片没有再出现；作为片段收录，不计数。P1 第 8–9 行被字幕和滚动箭头压住，3 处【?】 → `zg6RGFH-jUQ-P1-en-line8-9-subtitle-occluded.png`；P2 第 6 行 1 处【?】（滚动箭头）。
  2. P1 前言首行上半截在窗口外，「这【?】的核心是双风格拼贴」第 2 个字无法辨认（不是提示词正文） → `zg6RGFH-jUQ-P1-preamble-top-line-clipped.png`
  3. P2「尖锥苞」的「锥」在聊天窗口里被指针压住，已按 Midjourney 输入框里同一段文字确认（已解决，作为证据图） → `zg6RGFH-jUQ-P2-zhui-mjbox-evidence.png`
  4. 贵族定妆照提示词、「导演顾问」写的 30 秒分镜提示词、前一版「花茎森林城市」提示词都没有完整出现在画面上；KSRMJv3 与「导演顾问」两个扣子技能、作者的个性化档案都是私发，无公开文字版。未编造。
  5. 帖子文案三处（detail JSON、SSR 正文、JSON-LD）都以「...」结尾，无法判断是否被截断；收藏数 SSR 只有约数「1.3万」；「展开106条回复」楼中楼未展开。
- 获取方法: 移动端 UA 解析短链；无头 Chrome 取匿名 cookie → `yt-dlp --cookies`（HEVC 720p；H.264 重试后成功，1024×576；detail JSON 曾 403 警告）；Googlebot UA 抓 SSR 拿文案、互动数、发布时间与评论（14:52 与 15:34 UTC+8 两次）。
