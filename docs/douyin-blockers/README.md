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
