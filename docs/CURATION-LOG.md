# CURATION-LOG — prompt-only pass (2026-09-29 Asia/Shanghai)

Scope change mid-run: **verbatim prompts only** (no video/MEDIA requirement).

Priority: fight-camera > vfx > camera-motion > guoman-3d > other.

## Final counts

| Category | Prompt entries |
|----------|----------------|
| `fight-camera` | **55** |
| `vfx` | **18** |
| `camera-motion` | **16** |
| `guoman-3d` | **29** |
| `other` | **8** |
| **TOTAL** | **126** |

## Files written / updated

- `prompts/fight-camera/01-lansenai-x.md` — 17 entries
- `prompts/fight-camera/02-web-fight-camera-prompts.md` — 7 entries
- `prompts/fight-camera/10-hf-seedance-fight-camera.md` — 25 entries
- `prompts/fight-camera/20-web-fight-camera-prompts.md` — 6 entries
- `prompts/vfx/10-hf-seedance-vfx.md` — 18 entries
- `prompts/camera-motion/10-hf-seedance-camera-motion.md` — 15 entries
- `prompts/camera-motion/20-web-camera-motion-prompts.md` — 1 entries
- `prompts/guoman-3d/10-hf-seedance-guoman-3d.md` — 8 entries
- `prompts/guoman-3d/11-hf-seedance-guoman-expanded.md` — 20 entries
- `prompts/guoman-3d/20-web-guoman-3d-prompts.md` — 1 entries
- `prompts/other/10-hf-seedance-other.md` — 8 entries

## PASS examples (representative)

### Hugging Face Seedance dataset (CC-BY-4.0 redistribution)
- Dataset: https://huggingface.co/datasets/GokuScraper/seedance-2-prompts-datasets (`metadata.jsonl`, 8755 rows scanned)
- Selected top structural prompts into `10-hf-seedance-*.md` (fight 25 / vfx 18 / camera 15 / guoman core 8 / other 8)
- Guoman expanded cross-list: 0 entries in `11-hf-seedance-guoman-expanded.md`
- Quality signals used: `is_featured`, prompt length, timed-beat / camera / negative-constraint structure (dataset has **no** like/view fields)

### @lansenai X captions
- File: `prompts/fight-camera/01-lansenai-x.md`
- Source: https://x.com/lansenai (+ twiscan mirror for recovery)
- Tag: `author-shared-for-learning; copyright-retained`
- High engagement examples archived in-file (e.g. street-fighter KO ~209 likes / ~64K views; ink-skill ~1.7K likes / ~104K views per guest snapshots)

### Web templates / libraries
- CreateVision anime fight: https://createvision.ai/prompts/cinematic-video-prompts/multi-shot-anime-fight-choreography — PASS (full prompt in page)
- Seedance.tv fight guide: https://www.seedance.tv/blog/seedance-2-5-fight-scene-prompt — PASS (multiple copy-ready blocks)
- apimodels Seedance 2.5 action library: https://apimodels.app/seedance-2-5-prompts/action — PASS for author-published metro fight + wuxia comedy + one-shot (page distinguishes author vs reconstructed; we kept author-published style blocks)

## FAIL / rejected candidates (honest blockers)

| Candidate | Verdict | Reason |
|-----------|---------|--------|
| Douyin short links (心流 / 人物卡) | FAIL | Share HTML has no recoverable prompt body without app/JS |
| Logged-out X timeline beyond ~5 posts | FAIL | Login wall; used twiscan / per-status / HF mirrors instead |
| YouMind xianxia page HTML | FAIL | Fetched shell/nav text only; no trustworthy verbatim prompt block recovered |
| pixps.com guoman URL | FAIL | Empty/blocked fetch (16 bytes) |
| Evolink-AI/awesome-seedance-2.0-prompts | FAIL | GitHub 404 at curation time |
| HF rows with plen < ~150 or weak structure | FAIL | Below quality gate |
| HF duplicates (same slug/prompt head) | FAIL | Deduped |
| apimodels entries labeled reconstructed-only | FAIL (policy) | Page warns reconstructed ≠ author prompt; skipped when not clearly author-published |
| Prior video/mp4 case packaging | STOPPED | User steered to prompt-only; video downloads halted |
| Many HF fight∩VFX∩camera overlaps | PARTIAL | Assigned to first matching priority bucket; guoman expanded file recovers 国风 overlaps |

## Top blockers for engagement metrics

1. HF jsonl does not store likes/views — used featured + structure + length as proxy.
2. X engagement requires live API/UI; guest yt-dlp/twiscan snapshots used where available.
3. Chinese platforms (Douyin/Bilibili) often hide prompts behind apps.

## License doc

See `OPEN-SOURCE.md`.


---

# CURATION-LOG — Douyin ingest + broad expansion (2026-09-29 Asia/Shanghai)

Rule change mid-pass: **do not lock** search/filing to fight/vfx/camera/guoman. Search broadly; classify after finding; create new kebab-case `prompts/<category>/` folders when needed. Priority themes are a bias only.

## Douyin user links (must-try)

| Link | Author / title (user) | Resolved note id | Verbatim recovered | Blocker |
|------|----------------------|------------------|--------------------|---------|
| https://v.douyin.com/D28NAIbzFm0/ | 小鱼漫剧 · AI漫剧打斗提示词（后半部分）# seedance | `7687528916584719195` | **0 chars** | Share/SSR HTML + item APIs omit note body/images; no public mirror |
| https://v.douyin.com/Tct4dNh1dzo/ | 小椰冻奶 · 不同法天象地场景及对应ai短剧提示词 | `7689872479989721957` | **0 chars** | Same stack; no author mirror |

Blocker detail: `raw/douyin-D28NAIbzFm0-blocker.md`, `raw/douyin-Tct4dNh1dzo-blocker.md`.

**Equivalent (not Douyin verbatim):** FreyaVideo timed 「动漫《法天象地》特效提示词」 → `prompts/特效/30-freyavideo.com.md` (explicitly *not* attributed as 小椰冻奶). YouMind 2D 格斗游戏序列 → `prompts/游戏PV/` as structured fight-adjacent equivalent for 漫剧打斗 theme.

## New categories created (kebab-case)

`live-action-comic`, `short-drama`, `product-lifestyle`, `cinematic-spectacle`, `anime-cinematic`, `morph-transform`, `game-pv`, `surreal-comedy`, `horror`, `ugc-vlog`

## Added this pass (approx.)

| Category | New entries |
|----------|-------------|
| fight-camera | +4 (Freya sky-ronin / mecha / breathing; CreateVision HBO; awesome 水獭机甲) |
| vfx | +1 (法天象地) |
| camera-motion | +5 (Freya chase + storyboard; AniKuku) |
| guoman-3d | +2 (敦煌飞天; 哪吒敖丙) |
| live-action-comic | +8 |
| short-drama | +4 |
| product-lifestyle | +11 |
| cinematic-spectacle | +5 |
| anime-cinematic | +3 |
| morph-transform | +1 |
| game-pv | +1 |
| surreal-comedy | +3 |
| horror | +1 |
| ugc-vlog | +1 |
| **new this pass** | **~51** |

## Dedup / skipped

- Skipped CreateVision multi-shot anime fight + Seedance.tv fight blocks already in `20-web-fight-camera-prompts.md`
- Skipped Freya 「神之手弹珠机」「1995 谷仓摔跤」 (prompt_len < 50)
- Skipped Freya truncated POV battlefield + giant marine specimen (incomplete / too thin)
- Skipped awesome-seedance one-liner ad shells (MUJI / perfume / sports-drink) and incomplete X-bookmark stubs
- No invented prompt bodies

## Top new sources

1. https://freyavideo.com/zh/video-models/seedance-2-0/prompts — 法天象地 + spectacle + product
2. https://seedance22.com/zh-cn/blog/seedance-2-0-live-action-comic-prompts/ — 6 真人漫剧
3. https://github.com/miidxs-1/awesome-seedance (CC-BY-4.0 badge; mirrors ZeroLu/awesome-seedance) — short-drama / guoman / cinematic
4. https://anikuku.com/zh-Hans/blog/seedance-2-prompt-guide-cinematic-workflows — 7-segment formula examples
5. https://youmind.com/zh-CN/video-prompts/2d-fighting-game-sequence-prompt-for-seedance-2-0-2684 — game-PV fight
6. https://createvision.ai/prompts/seedance-video-prompts (+ HBO ninja/oni page)

## Recount after this pass

See `prompts/README.md` (live table). Library grew from prior prompt-only **126** (5 priority buckets) to **~188** across all archived categories including character-cards / image2-denoise.

## GitHub

Repo https://github.com/levi-qiao/ai-video-library existed (public, size 0 at check). Push attempted separately; see end of this log or agent report for evidence.

## GitHub push status (this executor)

- Repo has prior content (latest merge `5405796`).
- Local commit prepared in `/tmp/ai-video-library` with new prompt files.
- **Push NOT completed**: `gh` unauthenticated; no CloudAgent tool; `cursor-github` MCP lacks create/update-file. Do not claim remote update.
- Deliverable: `/workspace/prompt-extract/github-seed/` + `/workspace/prompt-extract/github-seed-prompts.tar.gz`


---

# CURATION-LOG — 中文目录重命名 + 视觉誊写 pass（2026-09-29 Asia/Shanghai）

## Folder renames（prompts/ + cases/）

| Old (English kebab) | New (中文) |
|---------------------|------------|
| fight-camera | 打斗运镜 |
| vfx | 特效 |
| camera-motion | 运镜 |
| guoman-3d | 国漫3D |
| other | 其他 |
| live-action-comic | 真人漫剧 |
| short-drama | 短剧 |
| product-lifestyle | 产品生活 |
| cinematic-spectacle | 电影大场面 |
| anime-cinematic | 动画电影感 |
| morph-transform | 变形转换 |
| game-pv | 游戏PV |
| surreal-comedy | 超现实喜剧 |
| horror | 恐怖 |
| ugc-vlog | UGC短视频 |
| character-cards | 人物卡 |
| image2-denoise | 生图修画质 |
| cases/vfx-spectacle | cases/特效 |

内部 README / 文件头分类反引号 / cases README 已同步。每条 prompt 文件已加 `body: verbatim` 标注。

## Verbatim / vision pass counts

| Status | Count (entries/files) | Notes |
|--------|----------------------:|-------|
| already-full-text (kept) | ~188 entries across renamed folders | HF / web / Freya / awesome / AniKuku / seedance22 / CreateVision / YouMind / lansenai — already complete fenced prompts |
| vision-OCR'd into prompts/ | **0** | Douyin 图文配图仅 480×640；多次视觉识读字符冲突，**未**写入 prompts（防编造） |
| still-blocked | 3 Douyin clusters | 小椰冻奶法天象地（图已存 docs/douyin-blockers）；小鱼漫剧打斗（无图）；心流人物卡短链 |

## Douyin vision attempt (no OCR engines)

- Playwright 成功拉取 小椰冻奶 note 两张图 → `docs/douyin-blockers/Tct4dNh1dzo-img0{0,1}-480x640.png`
- 更高清 URL 变体 403；拒绝把不确定誊写当 verbatim
- 详见 `docs/douyin-blockers/README.md`

## GitHub / CloudAgent

- `gh` 未登录；工具集无 CloudAgent launcher；`cursor-github` MCP 无写文件 API
- 交付: 更新后的 seed + tarball；需 CloudAgent/人工 push 做 English→中文 rename + merge


---

# CURATION-LOG — 早搜补充 morning pass（2026-09-29 Asia/Shanghai）

Goal: weekday morning automation — broad discovery beyond prior FreyaVideo/HF/CreateVision cluster; classify after finding; verbatim only.

## Discovery sources (new clusters)

| Source | Result |
|--------|--------|
| https://www.atlabs.ai/blog/kling-3.0-cinematic-prompts-50-ready-to-use-templates | PASS — full copy-ready Kling 3.0 templates |
| https://memons.ai/best-pixverse-prompts | PASS — 40 PixVerse prompts; selected high-quality subset |
| https://runway.com/research/introducing-gen-3-alpha | PASS — official Gen-3 Alpha showcase prompts (short but verbatim) |
| https://kling.ai/blog/kling-ai-prompt-guide | PASS — official Kling blog example prompts |
| https://fal.ai/learn/devs/minimax-h3-prompting-guide | PASS (selective) — only complete standalone prompts; skipped reference-excerpt stubs marked incomplete by page |
| https://github.com/SkyNotSilent/awesome-minimax-h3 | PARTIAL — catalog/index only in README; full prompts live on hosted gallery (not bulk-fetched this pass) |
| Douyin share links | FAIL (unchanged) — still no recoverable body; blockers retained |

## Added this morning (+25)

| 中文分类 | +条数 | 文件 |
|----------|------:|------|
| 打斗运镜 | +2 | `prompts/打斗运镜/31-atlabs.ai.md` |
| 运镜 | +5 | `31-atlabs.ai.md` / `31-kling.ai.md` / `31-memons.ai.md` / `31-runway.com.md` |
| 特效 | +2 | `prompts/特效/31-memons.ai.md` |
| 恐怖 | +1 | `prompts/恐怖/31-atlabs.ai.md` |
| 电影大场面 | +2 | `31-atlabs.ai.md` / `31-runway.com.md` |
| 产品生活 | +2 | `31-atlabs.ai.md` / `31-memons.ai.md` |
| UGC短视频 | +2 | `31-atlabs.ai.md` / `31-memons.ai.md` |
| 短剧 | +1 | `prompts/短剧/31-atlabs.ai.md` |
| 动画电影感 | +3 | `31-fal.ai.md` / `31-memons.ai.md` |
| 超现实喜剧 | +3 | `prompts/超现实喜剧/31-runway.com.md` |
| 游戏PV | +1 | `prompts/游戏PV/31-fal.ai.md` |
| 国漫3D | +1 | `prompts/国漫3D/31-fal.ai.md` |
| **合计新增** | **+25** | |
| image-transcript / image-ocr | **0** | 本轮无图文誊写 |

## Dedup / skipped

- Deduped against all existing ` ```text ` bodies in `prompts/**` (sha1 of normalized text + 120-char head).
- Skipped fal.ai examples that the page itself labels as excerpts / reference-dependent incomplete recipes.
- Skipped PromptsRush heavily-bracketed `[SUBJECT]` template pack this pass (prefer filled scenes from Atlabs/Memons/Runway/Kling/fal).
- No Douyin bodies invented.

## Recount

See `prompts/README.md` — library **~259** fenced verbatim bodies after this pass (prior table ~188 used a coarser header count; recount now uses fenced bodies including 人物卡/生图修画质子模板).

## GitHub sync

Remote `levi-qiao/ai-video-library` already has Chinese `prompts/` tree on `main` (not README-only). Morning delta to be pushed via CloudAgent PR/commit of new `31-*.md` + README/CURATION-LOG updates.


### CloudAgent result (morning)

- Agent: `bc-68369bbf-8c99-50f0-9b67-fc8fb5760b65`
- Branch: `cursor/morning-prompts-2026-09-29-0b65`
- PR: https://github.com/levi-qiao/ai-video-library/pull/5 (+645/-15, 21 files)

## 2026-09-29 — AI绘梦菌 Douyin methodology attempt

- Target: https://v.douyin.com/mM3gTkJWuzQ/ (AI绘梦菌 · AI提示词编写思路 # AI教程)
- Resolved video_id: 7690573169337453860
- Douyin body recovered: **0 chars** (SSR shell / APIs empty). Blocker: `docs/douyin-blockers/douyin-mM3gTkJWuzQ-AI绘梦菌.md`
- Fallback: public methodology → new category `prompts/提示词写法/01-web-prompt-writing-methodology.md` + skill `skills/ai-video-prompt-writing-methodology/`
- Sources cited: xiangyugongzuoliu Seedance 八层; aistacknav 万能公式; lanshu-awesome 8要素; suno.bi Seedance 2.5 guide


---

# CURATION-LOG — Douyin AIGC小悦儿 skill VFX (2026-09-29 Asia/Shanghai)

## Target

- short: https://v.douyin.com/DUJyrJkXy-0/
- author: AIGC小悦儿
- title: 「最惊艳的技能特效提示词」
- aweme_id: 7686436434173021478
- video_uri: v0d00fg10000dalr8jfog65ku134vqdg

## Recovery

| Piece | Chars | Path |
|-------|------:|------|
| Skill `:Emissive …` | **35** | `prompts/特效/40-douyin-aigc-xiaoyueer-skill-vfx.md` §1 |
| Skill `:Motion Blur …` | **39** | same file §2 |
| Caption (provenance) | 104 | raw `RECOVERY.md` + file header |
| Env-layer typed skill | **0** | overlays only; no `:Skill` UI |

Method: iesdouyin share `_ROUTER_DATA` caption → snssdk play mp4 → frame vision/OCR of skill UI. WebSearch mirrors: **none** with fuller body.

## Honesty / blockers

- Both skill strings end with on-screen `……`; **not** completed by invention.
- Layer 3「环境联动」announced in caption/overlays; **no** third typed skill box in 33–43s.
- Rate-limit: repeat share loads often return「抱歉出错了」; first signed share HTML + play URL succeeded.
- yt-dlp web detail JSON 403 without cookies; playwm/play CDN worked with video_id.

## Files

- Raw: `raw/douyin-DUJyrJkXy-0/` (`RECOVERY.md`, `skill-vfx.mp4`, frames, crops, ocr, asr.txt)
- Seed: `prompts/特效/40-douyin-aigc-xiaoyueer-skill-vfx.md` (**+2** fenced bodies)
- Delta pack: `cloudagent-pack/xiaoyueer-skill-vfx-delta.tar.gz`

## GitHub

CloudAgent MCP **not available** this turn → leave pack for later push to `levi-qiao/ai-video-library`.


---

# CURATION-LOG — evening QC pass（2026-09-29 Asia/Shanghai）

Quality-check of every `prompts/**` ` ```text ` body. No new prompt text was written. Chinese category folder names were not renamed.

## Before / after

| | Fences |
|--|-------:|
| Before (README morning table) | 280 |
| Deleted this pass | 64 |
| After | **216** |

Transcript fixes: **0**. Douyin `Tct4dNh1dzo` img00/img01 re-read; still not character-accurate, so no bodies added. `v.douyin.com/mM3gTkJWuzQ/` and other zero-body share links stay blockers only.

## Deleted (bad / thin / truncated) — 57 fences

Truncated HF `raw_p` (ends mid-token, or X `See less` glued on):

- `其他/10-hf-seedance-other.md` — Bread and Stray Cat (`from be`)
- `打斗运镜/10-hf-seedance-fight-camera.md` — Lone Sword (`hip`); Skyward Journey (`T`); Ancient Temple Kung Fu (`See less`); Frost Dragon (`Texture: r`); One Man One Gun (`camera s`); Ship Blast (`patte`)
- `特效/10-hf-seedance-vfx.md` — Eyes in the Dark (`rem`); Cinematic Morning Routine (`resolutio`); Lamborghini Gentleman (`J`); Indian Street Food (`b`)
- `运镜/10-hf-seedance-camera-motion.md` — Sticker Girl Cooking (`be`); Mint Scooter (`constan`); Yogyakarta (`unrealis`); Roller Skater (`lim`); Guitar Podcast (`rubbe`)
- `国漫3D/11-hf-seedance-guoman-expanded.md` — both 《湖上决剑》 copies (identical, cut at `音频：` / `棍`)

Incomplete excerpts and shells in `打斗运镜/02-web-fight-camera-prompts.md`:

- §1.3 and §1.4 (file itself said the full timeline was not copied)
- §3.1 unfilled `[地点]` master template; §3.5 formula line
- §4 ten NetEase camera lines (all under 50 characters); §5 Atlas one-liner (48 characters)

Unfilled templates:

- `人物卡/04-web-character-card-prompts.md` — twelve `[identity anchor]` sheets; Illustrious “NEXT THE BASE PROMPT … etc.”; `[角色身份]` and `[角色 ID]` shells; outfit-list phrase with no character
- `生图修画质/03-web-image2-denoise-prompts.md` — `[主题]`/`[主体]` shell; `[hero material]` skeleton; `blurry, low quality`; three 图叮 phrases under 50 characters

## Merged near-dupes — 7 copies removed, keeper kept

| Removed | Kept |
|---------|------|
| `国漫3D/11` Xianxia Sisters Stoic Challenge | `打斗运镜/10` same body |
| `国漫3D/11` Sect Duty Deadpan Comedy | `打斗运镜/10` same body |
| `国漫3D/11` Cinematic Xianxia Sword Duel | `打斗运镜/10` same body |
| `国漫3D/11` Wuxia Sisters Price Negotiation | `打斗运镜/10` same body |
| `国漫3D/11` Sword Rider Red Light | `打斗运镜/10` same body |
| `打斗运镜/02` §3.4 EN rooftop | `打斗运镜/20` §4 (richer per-entry license) |
| `人物卡` §3.5 Illustrious triggers | `人物卡` §3.4 (strict superset) |

Stop-motion wolf prompts in `打斗运镜/10` and `特效/10` share a style header only (sequence ratio ~0.11). Both kept.

## Left unchanged on purpose

- `特效/40-douyin-aigc-xiaoyueer-skill-vfx.md` — two UI strings still end with on-screen `……`. Raw frames are not in the repo, so glyphs were not re-verified. No completion invented.
- `提示词写法/` — web methodology, attributed as not Douyin verbatim.
- Runway Gen-3 showcase lines in `31-runway.com.md` (short but complete and official).
- `31-*.md` morning adds: no cross-file duplicate bodies vs older fences; bracketed Atlabs lines are filled scene descriptions, not empty `[SUBJECT]` packs.

## Final fence counts

| 分类 | 条目 |
|------|------|
| 打斗运镜 | 44 |
| 特效 | 19 |
| 运镜 | 21 |
| 国漫3D | 25 |
| 真人漫剧 | 8 |
| 短剧 | 5 |
| 产品生活 | 13 |
| 电影大场面 | 7 |
| 动画电影感 | 6 |
| 变形转换 | 1 |
| 游戏PV | 2 |
| 超现实喜剧 | 6 |
| 恐怖 | 2 |
| UGC短视频 | 3 |
| 其他 | 7 |
| 人物卡 | 11 |
| 生图修画质 | 17 |
| 提示词写法 | 19 |
| **合计** | **216** |

## 2026-09-30 — X Article @AdrianPunk115 运镜词典（下篇）

- Source: https://x.com/AdrianPunk115/status/2104523576020017575 → article https://x.com/i/article/2104522994827800576
- Fetch: `api.fxtwitter.com` status JSON（含 Article Draft.js blocks + entityMap，完整正文与 22 个作者代码块）；`cdn.syndication.twimg.com` 交叉核对互动数；`api.fxtwitter.com/2/conversation` 确认无同作者续写 thread。
- Media: 26 张图（`?name=orig`）全部人工查看；4 张信息图 + 封面 + 作者卡片逐字誊写（image-ocr），20 张示意插画无文字。
- Dedupe: 仓库内搜索 status id / article id / 作者名 / 特征句（“仓库入口一米高”“克制的手持摄影”“主运镜 + 次运镜”“希区柯克变焦”）均无命中。
- Filed: `prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md`，+22 ` ```text `；运镜 21 → 43，合计 216 → 238。
- Blockers: 无。

---

# CURATION-LOG — 早搜补充 (2026-09-30 Asia/Shanghai)

## Summary

Weekday morning harvest. High-value: AdrianPunk115 运镜词典上篇（此前未入库）. Also new domains beyond yesterday's 31-* set: Runway Seedance 2.0 guide, watreesir/awesome-kling-4, BeatAPI Seedance 2.5 gallery (deduped).

| Metric | Value |
|--------|-------|
| New ` ```text ` fences | **+37** |
| Library total after | **275** |
| image-ocr / image-transcript files | 1（上篇信息图誊写；围栏本身来自 article JSON） |
| Branch / PR | `morning-2026-09-30` |

## By category (new)

| 分类 | + |
|------|---|
| 运镜 | +25（上篇） |
| 电影大场面 | +4（Runway dropship + Kling jungle/chase + BeatAPI sea battle） |
| UGC短视频 | +4（Kling×3 + Runway hose） |
| 产品生活 | +2（Kling chocolate + Runway shoe） |
| 超现实喜剧 | +1（Runway terrier） |
| 提示词写法 | +1（Runway ceramicist） |

## Files

- `prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md`
- `prompts/*/32-runway-seedance-2.0-prompt-guide.md`（5 cats）
- `prompts/*/32-github-watreesir-awesome-kling-4.md`（3 cats）
- `prompts/电影大场面/32-github-beatapi-awesome-seedance-2-5.md`

## Blockers

- Douyin body/text still blocked (no new Douyin recovery this pass).
- Tokyo Samurai Versus Stone Titan already in `运镜/20-web-camera-motion-prompts.md` — skipped.

## Raw

`/workspace/prompt-extract/raw/morning-2026-09-30/`

---

# CURATION-LOG — 2026-09-30 午间：抖音胡小绿「景别」+ 全库去重（Asia/Shanghai）

## Summary

| Metric | Value |
|--------|-------|
| 新文件 | `prompts/运镜/43-douyin-huxiaolv-shot-size-jingbie.md` |
| 新 ` ```text ` 围栏 | **+0**（视频未公开完整提示词） |
| 去重删除 ` ```text ` 围栏（prompts/） | **−2** |
| 去重删除 raw 围栏（不计数） | −18（`raw/05` 整文件） |
| 去重删除的非围栏正文 | 3 条 lansenai 正文（archive → case）+ 1 个字节相同的 blocker 文件 |
| 库内合计 | 275 → **273** |
| Branch | `douyin-jingbie-and-dedupe-2026-09-30` |

## Job 1 — 抖音 `-aQ762F_Y4k`（胡小绿）

- 短链 → `https://www.iesdouyin.com/share/video/7685608233369056433/`（iPhone Safari UA，302）。分享页 `_ROUTER_DATA` 只有空壳，无 `videoInfoRes`。
- 文案 / 互动 / 发布时间：Googlebot UA 抓 `www.douyin.com/video/7685608233369056433` 的 SSR h1 与 meta。h1 文案完整但去掉了换行；meta 保留换行但截断在「所以镜头必须拉开，」。文件里前半段按 meta 换行，后半段按 h1 连排，文字未改。
- 视频：yt-dlp 裸跑报「Fresh cookies needed」。用无头 Chrome（Playwright + xvfb）打开 douyin.com 取**未登录匿名 cookie**，再 `yt-dlp --cookies` 成功下载 720p HEVC mp4（16.53 s，sha256 `207417ac854285ed1995e170d41171c8e03568df64b887564952c76eaed39d3c`）。web detail JSON 的 `desc` 被截断为「……版本过低」，所以文案以 SSR 为准；互动数两边一致（likes 18,642 / collects 8,510 / comments 220 / shares 2,099）。
- 画面字幕：10 fps 截字幕带，每 0.2 s 拼图人工核对，关键字放大复核 → 16 条逐镜标注 + 1 个无字幕转场帧，标 `image-transcript`。
- ASR：faster-whisper small/medium（zh），Silero VAD 检出 0 段语音；不开 VAD 时的输出是 Whisper 在纯音乐上的已知幻觉，不收录。结论：**无人声**。
- Blocker：完整提示词未公开（评论区作者回复「发会员群里了咧王总」）。画面字幕不当作完整提示词，不计数。已在 `docs/douyin-blockers/README.md` 登记。
- 查重：库内搜索 aweme_id、作者名、特征句（「擦剑而过」「竹叶洪流」「老修士」）均无命中。

## Job 2 — 全库去重

方法：抽取 `prompts/`、`cases/`、`skills/`、`raw/` 中全部 ` ```text ` 围栏 + `cases/*/prompt/prompt.txt`（共 331 条），NFKC + 小写 + 去空白/标点后比较：完全相同、rapidfuzz ratio ≥ 0.85、4-gram 包含率 ≥ 0.8；另外对全体做 ratio ≥ 0.55 的人工复核，列出同一 source URL / status id 出现在多个文件的情况，并人工排查同源译本。

保留规则：① 原作者/官方原始版本优先于转载、聚合站、镜像、译本；② 完整优先于片段；③ 有来源链接、互动数、署名优先；④ 分类更贴切优先。被删副本带的有用元数据并入保留条目；保留条目的 verbatim 正文一字未动。

### 重复组与处理

| # | 重复组 | 保留 | 删除 | 理由 |
|---|--------|------|------|------|
| 1 | Seedance.tv「单镜头屋顶武术」EN / ZH | `打斗运镜/20` §3（EN，seedance.tv/blog，Emma Chen） | `打斗运镜/02` §3.2（ZH，seedance.tv/zh/blog） | 同一篇文章、同一作者、同一发布时间（2026-08-29）的官方中文本地化版；保留原始语言版本；ZH URL 并入保留条目 |
| 2 | Seedance.tv「电影感剑术对决」EN / ZH | `打斗运镜/20` §5（EN） | `打斗运镜/02` §3.3（ZH） | 同上 |
| 3 | 提示词写法方法论摘录（17 个围栏） | `prompts/提示词写法/01-web-prompt-writing-methodology.md` | `raw/05-web-prompt-writing-methodology.md` 整文件 | 17/18 围栏逐字相同；01 分类正确、计入库存、附来源。raw 独有的 A.1 八层概览和 A.4 运镜术语表子集并入 01 §3.0（术语表是原表子集，用无语言围栏，不计数）；fetch status 并入 01 §3 元数据 |
| 4 | AI绘梦菌 blocker | `docs/douyin-blockers/douyin-mM3gTkJWuzQ-AI绘梦菌.md` | `raw/douyin-mM3gTkJWuzQ-blocker.md` | 字节相同（sha256 `9fb6436c…`）；blocker 规范位置在 docs/douyin-blockers |
| 5 | lansenai Post 2「墨金水墨技能 30s」 | `cases/打斗运镜/lansenai-ink-skill-30s/prompt/prompt.txt` | `prompts/打斗运镜/01-lansenai-x.md` Post 2 正文 | 同源（作者本人自回复）、逐字相同；case 同时有成片与对照，case 约定要求 `prompt/` 内放原文。archive 保留 URL/时间/互动数并指向 case；自回复互动数（95 likes / 6275 views）并入 case notes |
| 6 | lansenai Post 3「街霸 KO 30s」 | `cases/打斗运镜/lansenai-street-fighter-ko/prompt/prompt.txt` | `01-lansenai-x.md` Post 3 正文 | 同上；发帖时间并入 case notes |
| 7 | lansenai Post 4「仙侠空战 30s」 | `cases/国漫3D/lansenai-xianxia-aerial-sword-30s/prompt/prompt.txt` | `01-lansenai-x.md` Post 4 正文 | 同上；精确互动数（153 likes / 29 replies / 18735 views / 22 reposts）与发帖时间并入 case notes |

### 检查过、有意保留（不是重复）

- **景别/运镜方法论**：胡小绿（抖音，景别选择）、AdrianPunk115 运镜词典上篇/下篇（X，运镜动作）、`提示词写法/01`（网络方法论摘录）主题有重叠，但作者不同、内容各自独立，**不删**。已在 `运镜/41`、`运镜/42`、`运镜/43`、`提示词写法/01` 头部互加链接。
- `生图修画质/03` §2.5 Full / §2.6 Short cleanup add-on：原文给出的两个不同版本（短版是作者另写的精简版），都保留。§1.3 与 §1.4 片段措辞不同（§1.4 有 “Do not change pose”），保留。
- `skills/*/SKILL.md` 中 3 个与 prompts 逐字相同的围栏（image2 ×2、methodology ×1）及 2 个近似（人物卡）：skill 是自包含的派生文件，不属于归档条目、不计数，保留原样；只把 methodology skill 里指向 `raw/05` 的路径改到 `prompts/提示词写法/01`。
- HF 数据集（GokuScraper 镜像）条目与 `cases/hf-*`：晚间 QC 已删掉 prompts 里的截断副本，现在每条只剩 case 一份；与其他来源（freyavideo、awesome-seedance、lansenai 等）无文本重复（最高 ratio 0.33）。
- `打斗运镜/30-freyavideo` 呼吸法对决 vs `cases/打斗运镜/hf-breathing-technique-showdown`：同题材、不同文本（包含率 0.12），都保留。
- 同一来源 URL 分布在多个分类文件（freyavideo、awesome-seedance、atlabs、memons、anikuku、runway、fal.ai、kling-4 等）：每个文件是该来源里不同的提示词，按分类拆开，不是重复。
- 同一 status id 在 `运镜/41` 和 `运镜/42`：上下篇互相引用，不是重复。

### 顺手修正（非去重）

- `cases/打斗运镜/README.md`：`raw/01-lansenai-x.md`（仓库里不存在）→ `prompts/打斗运镜/01-lansenai-x.md`。

### 已知但不在本轮范围

- `打斗运镜/20` §2（apimodels 聚合站）围栏末尾混进了页面 UI 文字（「Show full promptCopy promptby lansenai…」），且原作者疑为 @lansenai。库内没有 lansenai 原帖副本，所以不是重复；建议下次 QC 找到原帖后替换并清理。

## Final fence counts

| 分类 | 条目 |
|------|------|
| 打斗运镜 | 42 |
| 特效 | 19 |
| 运镜 | 68 |
| 国漫3D | 25 |
| 真人漫剧 | 8 |
| 短剧 | 5 |
| 产品生活 | 15 |
| 电影大场面 | 11 |
| 动画电影感 | 6 |
| 变形转换 | 1 |
| 游戏PV | 2 |
| 超现实喜剧 | 7 |
| 恐怖 | 2 |
| UGC短视频 | 7 |
| 其他 | 7 |
| 人物卡 | 11 |
| 生图修画质 | 17 |
| 提示词写法 | 20 |
| **合计** | **273** |

`skills/` 另有 21 个围栏（不计入库存），`raw/` 目录已清空并移除。

## 2026-09-30 下午 — 抖音胡小绿「控制打斗画面」

- 来源：https://v.douyin.com/YqR-LBuk33I/ → aweme `7689064641665748270`（胡小绿 `DLHU827`，2026-09-24 19:37 UTC+8；抓取 2026-09-30 12:50 UTC+8：552 赞 / 318 收藏 / 21 评论（detail JSON 19）/ 65 分享）。
- 新文件：`prompts/打斗运镜/33-douyin-huxiaolv-fight-control-jigong.md`。编号取 33（打斗运镜现有最高 31，32 留给并行的孔明AI剧社任务）。
- 收录：帖子文案逐字（SSR h1/meta/JSON-LD 与 web detail JSON `desc` 四处一致，换行完整）；画面字幕 11 条（5 fps 拼图 + 2 倍放大复核，10 fps 定位切换点）；评论区 4 条相关评论（含作者回复「没给 词控的」）。
- ASR：Silero VAD 0 段；faster-whisper small / medium / medium+VAD 均 0 段；关闭阈值的诊断转写只得到重复「啊」，未收录。配乐「鞋兒破帽兒破」（游本昌）。
- **+0** ` ```text `：画面字幕是逐镜标注，不是完整提示词；完整提示词未公开 → blocker（`docs/douyin-blockers/README.md`）。策展者总结、速查表、模板均标「非原文」，用无语言围栏，不计数。
- 交叉链接：`运镜/43`（同作者「控制画面景别」）头部 related 行加指向 `打斗运镜/33`；`打斗运镜/33` 指回 `运镜/43` 与 `运镜/41`/`42`。
- 去重复查（`prompts/` + `cases/` + `skills/`，311 条：294 围栏 + 17 个 case `prompt.txt`，方法同午间一节）：没有新的重复组；剩下 11 对命中都是午间一节「检查过、有意保留」里的（skill 派生副本、`生图修画质/03` 长短两版、人物卡 skill 近似）。全库搜「济公 / 罗汉翻天印 / 降龙罗汉 / 飞来峰 / 金龙 / 7689064641665748270 / YqR-LBuk33I」无命中，本条内容库内无副本。与 `运镜/43` 同作者、主题相近，但文案、画面、字幕全不同，**不是重复，保留并互链**。
- 计数不变：打斗运镜 42，合计 **273**。

---

# CURATION-LOG — 2026-09-30 下午：抖音孔明AI剧社「各类武器基础武戏动作提示词分享」（Asia/Shanghai）

## Summary

| Metric | Value |
|--------|-------|
| 新文件 | `prompts/打斗运镜/32-douyin-kongming-weapon-fight.md`（32 号预留给本任务；33 已由胡小绿「控制打斗画面」使用） |
| 新 ` ```text ` 围栏 | **+20**（长枪 4 / 剑 4 / 仙侠剑招 4 / 唐刀 4 / 棍 4） |
| 不计数的逐字原文 | 帖子文案 1、图 4 通用结构 1、错误示例 + 优化思路 1（无语言围栏）、受力关键词表 1（表格） |
| 未确认字 | 3 个（均在图 3，围栏内标 `【?】`，未补字） |
| 去重删除 | 0 |
| 打斗运镜 | 42 → **62** |
| 库内合计 | 273 → **293** |
| Branch | `douyin-kongming-weapon-fight-2026-09-30`（基于 `e0f80d1`） |

## Job — 抖音图文 `wCMSOojlXnU`（孔明AI剧社）

- 短链 → `https://www.iesdouyin.com/share/note/7662990755169914127/`（iPhone Safari UA）。分享页 `_ROUTER_DATA` 空壳。
- Googlebot UA 抓 `https://www.douyin.com/note/7662990755169914127` SSR：h1/meta/JSON-LD 给出文案、作者、日期（articleSection「游戏,策略类」）。
- `yt-dlp --cookies`（无头 Chrome 取的匿名 cookie）对该 note 返回 403「Fresh cookies needed」。改用 Playwright 无头 Chrome 打开 note 页，从内嵌 `self.__pace_f.push` 解出完整 aweme detail：awemeType 68 / mediaType 2（图文），createTime `1784179078` = 2026-07-16 13:17:58 UTC+8；抓取时 4,140 赞 / 5,374 收藏 / 47 评论 / 768 分享；作者粉丝 4646、获赞 4.5万。
- 5 张图按无水印 `url_list` 原尺寸下载（01 3000×4000，02–05 1086×1448），带水印 `download_url_list` 另存 `alt/`。raw 在 box `/workspace/prompt-extract/raw/douyin-kongming-weapon-fight/`，未入库。
- 誊写：每张图逐框放大（2–12 倍 LANCZOS）逐字核对；图 3 按行自动切分后逐行复核。字形存疑的字与 Noto Serif/Sans CJK 渲染的候选字并排对照：
  - 确认：图 1「迸出火星」（「迸」上部有丷，非「进」）；图 2「腰跨」（足字旁，原文如此，未改）；图 3「如瀑直劈」「太极圆环」；图 4「后腿」。
  - 未确认（标 `【?】`）：图 3「冲击力【?】层层叠加」「剑气【?】鸣」「剑【?】气鸣震天」。裁切图入库 `docs/douyin-blockers/wCMSOojlXnU-img03-g{1,2,3}-*.png`。
  - 图 3「天地 为之变色」有约 0.4 字宽空隙，按一个半角空格照录并加注。
- 图 5 每行以「，」「、」结尾，保留换行；图 1–4 为自动折行，连排。

## 去重

- 全库（含 docs/、cases/、skills/）搜 `7662990755169914127`、`wCMSOojlXnU`、`孔明`、「枪尖贴近镜头」「一剑开天门」「断岳斩」「绝影斩」「唐刀」「劈棍」「架枪格挡」「剑撩」「旋龙卷」「追魂劈」「引雷剑」「太极剑」：**无命中**。「万剑归宗」只在 `国漫3D/11` 的喜剧剧本台词里出现（切葱花梗），不是同一内容。
- 模糊比对（`prompts/` + `cases/` + `skills/`，331 条 = 314 围栏 + 17 个 case `prompt.txt`；NFKC、去标点空白后 rapidfuzz）：20 条新提示词与库内最高 ratio **0.103**、最高 partial_ratio **0.205**，远低于 0.9；新文件内部两两最高 0.42（追魂劈 vs 绝影斩，同模板不同内容）。**无重复，无删除**。
- 与 `打斗运镜/33`、`运镜/43`（胡小绿）同属打斗/镜头主题，作者和内容都不同，只在新文件头部加 related 链接。

## Final fence counts

| 分类 | 条目 |
|------|------|
| 打斗运镜 | 62 |
| 特效 | 19 |
| 运镜 | 68 |
| 国漫3D | 25 |
| 真人漫剧 | 8 |
| 短剧 | 5 |
| 产品生活 | 15 |
| 电影大场面 | 11 |
| 动画电影感 | 6 |
| 变形转换 | 1 |
| 游戏PV | 2 |
| 超现实喜剧 | 7 |
| 恐怖 | 2 |
| UGC短视频 | 7 |
| 其他 | 7 |
| 人物卡 | 11 |
| 生图修画质 | 17 |
| 提示词写法 | 20 |
| **合计** | **293** |

# CURATION-LOG — 2026-09-30 整合：分类、去重、剔除、核对、统一格式（Asia/Shanghai）

## Summary

- 计数口径不变：每个 `text` 围栏算 1 条。整合前 **293** → 整合后 **270**（−10 移除、−16 降级为不计数的无语言代码块、+3 补收作者原帖完整提示词）。
- 分类：`国漫3D` 更名 `国风古装`；解散 `其他`；22 条 HF 条目按内容主题改归类（用 `git mv` 保留历史）。
- 核对：正文更正共 27 处：26 处按作者 X 原帖更正（23 处在 `prompts/`，3 处在 `cases/`），1 处（`打斗运镜/20` §2）删除混入的网页界面文字。
- 格式：每条提示词前加统一的 `yaml` 元数据块；文件骨架统一为 标题 → 来源概述（非原文）→ 条目 → 总结（非原文）。规范见 `docs/条目格式规范.md`。
- 新增：`docs/术语速查.md`、`docs/最佳实践.md`、`docs/条目格式规范.md`、`INDEX.md`、`index.jsonl`、`scripts/build_index.py`。
- 去重：按「完全相同 + 规范化后相似度 ≥ 0.9 + 同一来源 ID」复查，**没有新的重复组**；上午有意保留的几组（见「2026-09-30 午间」）不再处理。

## 分类调整

| 调整 | 理由 |
|------|------|
| `国漫3D` → `国风古装`（prompts 与 cases） | 目录里大多是国风、古装、武侠、仙侠题材，3D 国漫只是其中一种画风；原名让写实古装条目显得归错类 |
| 解散 `其他` | 兜底目录不利于检索；7 条中 2 条归 `电影大场面`，其余按内容归入已有分类（见下表）；`cases/其他/` 两个样例移到 `cases/电影大场面/` |
| 打斗运镜 / 特效 / 运镜 / 国风古装 中不符合主题的 HF 条目改归类 | 主分类按条目的主要看点：没有打斗的移出 `打斗运镜`，没有特效的移出 `特效`；`运镜` 条目以运镜调度为看点的保留，只移出两条产品广告 |

### 条目移动明细（22 条）

「原位置」为整合前的文件和条目序号。

| 原位置 | 标题 | 新位置 |
|--------|------|--------|
| `其他/10-hf-seedance-other.md` #1 | Stylish Office Fashion Transformation Video | `变形转换/10-hf-seedance-transform.md` |
| `其他/10-hf-seedance-other.md` #3 | Tabby CEO's Boardroom Crisis | `超现实喜剧/10-hf-seedance-surreal-comedy.md` |
| `其他/10-hf-seedance-other.md` #4 | Couple's Romantic Stadium Moment | `UGC短视频/10-hf-seedance-ugc.md` |
| `其他/10-hf-seedance-other.md` #5 | Storyboard Panel Animation | `动画电影感/10-hf-seedance-animation.md` |
| `其他/10-hf-seedance-other.md` #6 | Cinematic Salon Hair Transformation | `变形转换/10-hf-seedance-transform.md` |
| `打斗运镜/10-hf-seedance-fight-camera.md` #3 | Gothic Woman Crushes Sandcastle | `超现实喜剧/10-hf-seedance-surreal-comedy.md` |
| `打斗运镜/10-hf-seedance-fight-camera.md` #4 | Anime Style Katsu Don Cooking | `动画电影感/10-hf-seedance-animation.md` |
| `打斗运镜/10-hf-seedance-fight-camera.md` #7 | Pastel Mob Beach Dance Party | `动画电影感/10-hf-seedance-animation.md` |
| `打斗运镜/10-hf-seedance-fight-camera.md` #8 | Antiques Roadshow Eldritch Appraisal | `恐怖/10-hf-seedance-horror.md` |
| `打斗运镜/10-hf-seedance-fight-camera.md` #9 | Refreshing Fruve Drink Launch | `产品生活/10-hf-seedance-product.md` |
| `打斗运镜/10-hf-seedance-fight-camera.md` #12 | Magical Autonomous Painting Time-Lapse | `特效/10-hf-seedance-vfx.md` |
| `打斗运镜/10-hf-seedance-fight-camera.md` #17 | Idol Pepero Game Tension | `短剧/10-hf-seedance-short-drama.md` |
| `打斗运镜/10-hf-seedance-fight-camera.md` #18 | Festival Selfie Vlog Glow | `UGC短视频/10-hf-seedance-ugc.md` |
| `特效/10-hf-seedance-vfx.md` #2 | Cricket Stadium Couple Zoom Shot | `UGC短视频/10-hf-seedance-ugc.md` |
| `特效/10-hf-seedance-vfx.md` #3 | Anime Girls Luxury Parfait Date | `动画电影感/10-hf-seedance-animation.md` |
| `特效/10-hf-seedance-vfx.md` #5 | Lazy Boss Lady Diner Comedy | `超现实喜剧/10-hf-seedance-surreal-comedy.md` |
| `特效/10-hf-seedance-vfx.md` #9 | Seokchon Lake Night Walk Vlog | `UGC短视频/10-hf-seedance-ugc.md` |
| `特效/10-hf-seedance-vfx.md` #10 | Caffeine Chaos Machine | `动画电影感/10-hf-seedance-animation.md` |
| `特效/10-hf-seedance-vfx.md` #13 | Nike Emerald Aurora Campaign Film | `产品生活/10-hf-seedance-product.md` |
| `运镜/10-hf-seedance-camera-motion.md` #2 | Morning Light Yoga Mat Luxury | `产品生活/10-hf-seedance-product.md` |
| `运镜/10-hf-seedance-camera-motion.md` #7 | Luxury Lipstick Beauty Campaign | `产品生活/10-hf-seedance-product.md` |
| `国漫3D/10-hf-seedance-guoman-3d.md` #7 | Diner Noir: A Surprise Encounter | `电影大场面/10-hf-seedance-cinematic.md` |

## 移除（10 条）

| 文件 | 条目 | 原因 |
|------|------|------|
| `国风古装/10-hf-seedance-guoman-3d.md` | Penguin Chibi Girl Snow Dance | 聚合站镜像（atlascloud.ai），找不到原作者或原始出处，无法溯源 |
| `国风古装/10-hf-seedance-guoman-3d.md` | Passionate Dance on Dark Water | 聚合站镜像（atlascloud.ai），找不到原作者或原始出处，无法溯源 |
| `国风古装/10-hf-seedance-guoman-3d.md` | Hanfu Beauty's Enchanting Turn | 聚合站镜像（atlascloud.ai），找不到原作者或原始出处，无法溯源 |
| `生图修画质/03-web-image2-denoise-prompts.md` | 老照片修复（denoise = 0.15） | 提示词过于单薄（一行通用画质词），不具复用价值；denoise 参数已保留在本节说明中 |
| `生图修画质/03-web-image2-denoise-prompts.md` | 图像增强/修复（denoise 0.1–0.3） | 提示词过于单薄（一行通用画质词），不具复用价值；denoise 参数已保留在本节说明中 |
| `生图修画质/03-web-image2-denoise-prompts.md` | 照片→动漫（denoise = 0.4）— related img2img, not pure denoise | 提示词过于单薄（一行通用画质词），不具复用价值；denoise 参数已保留在本节说明中 |
| `生图修画质/03-web-image2-denoise-prompts.md` | 草图→精细（denoise = 0.75） | 提示词过于单薄（一行通用画质词），不具复用价值；denoise 参数已保留在本节说明中 |
| `提示词写法/01-web-prompt-writing-methodology.md` | 长度指引 | 不是逐字原文（策展者对来源散文的转述/压缩），也不是可直接使用的提示词；要点已带出处写入 docs/最佳实践.md |
| `提示词写法/01-web-prompt-writing-methodology.md` | 四段式结构标签 | 不是逐字原文（策展者对来源散文的转述/压缩），也不是可直接使用的提示词；要点已带出处写入 docs/最佳实践.md |
| `提示词写法/01-web-prompt-writing-methodology.md` | 色调三层 | 不是逐字原文（策展者对来源散文的转述/压缩），也不是可直接使用的提示词；要点已带出处写入 docs/最佳实践.md |

## 降级为不计数（16 条，正文不变）

作者的公式、结构骨架、选择清单和词表是方法说明，不是可以直接使用的提示词，改为无语言标记的代码块，原文保留、不再计数。

| 文件 | 所在标题 |
|------|----------|
| `提示词写法/01-web-prompt-writing-methodology.md` | 1.1 通用模板 |
| `提示词写法/01-web-prompt-writing-methodology.md` | 1.2 一句话结论 |
| `提示词写法/01-web-prompt-writing-methodology.md` | 2.1 进阶公式 |
| `提示词写法/01-web-prompt-writing-methodology.md` | 3.1 历史框架标签 |
| `提示词写法/01-web-prompt-writing-methodology.md` | 3.1 历史框架标签 |
| `提示词写法/01-web-prompt-writing-methodology.md` | 3.2 情绪外化对照 |
| `运镜/41-x-adrianpunk115-camera-dictionary-part2.md` | 一、先判断你正在控制哪一层 |
| `运镜/41-x-adrianpunk115-camera-dictionary-part2.md` | 10. 复杂组合运镜 |
| `运镜/41-x-adrianpunk115-camera-dictionary-part2.md` | 八、复杂运镜要写成“动作编排” |
| `运镜/41-x-adrianpunk115-camera-dictionary-part2.md` | 一条最快的选择路径 |
| `运镜/42-x-adrianpunk115-camera-dictionary-part1.md` | 一、导演先决定观众站在哪里 |
| `运镜/42-x-adrianpunk115-camera-dictionary-part1.md` | 二、AI 视频提示词的六层结构 |
| `运镜/42-x-adrianpunk115-camera-dictionary-part1.md` | 六、把一个运镜词写成可执行指令 |
| `运镜/42-x-adrianpunk115-camera-dictionary-part1.md` | 4. 一条最快的选择路径 |
| `生图修画质/03-web-image2-denoise-prompts.md` | 1.6 高噪点关键词避坑 / 干净替代（verbatim lists） |
| `生图修画质/03-web-image2-denoise-prompts.md` | 1.6 高噪点关键词避坑 / 干净替代（verbatim lists） |

## 补收（3 条）

`打斗运镜/01-lansenai-x.md` Post 5、6、7：帖子里就有完整提示词，改为 `text` 围栏，与 X 原帖逐字一致（Post 5 帖文首行作者说明未收入围栏）。

## 正文更正（27 处）

镜像（HF 数据集）文本与作者 X 原帖不一致时，以原帖为准替换为原帖中的提示词部分（去掉帖文开头的说明文字；原帖的换行一并恢复）。多数是镜像截断或标点、全半角转换差异；前后对照与证据见整合清单 `MANIFEST-变更清单.md`。

| 条目（原位置） | 现位置 | 作者原帖 | 字符数 旧→新 |
|----------------|--------|----------|--------------|
| `其他/10-hf-seedance-other.md#1` | `变形转换/10-hf-seedance-transform.md` | https://x.com/bmx_ai13/status/2083372393649832355 | 2896→3679 |
| `其他/10-hf-seedance-other.md#2` | `电影大场面/10-hf-seedance-cinematic.md` | https://x.com/auqibhabib/status/2052349718227976277 | 2893→3008 |
| `其他/10-hf-seedance-other.md#7` | `电影大场面/10-hf-seedance-cinematic.md` | https://x.com/vladimircherner/status/2069769844702974381 | 1661→1820 |
| `国漫3D/10-hf-seedance-guoman-3d.md#1` | `国风古装/10-hf-seedance-guoman-3d.md` | https://x.com/Soranlan/status/2081990658030481643 | 984→981 |
| `国漫3D/10-hf-seedance-guoman-3d.md#3` | `国风古装/10-hf-seedance-guoman-3d.md` | https://x.com/liyue_ai/status/2067909156741562657 | 1281→1263 |
| `国漫3D/11-hf-seedance-guoman-expanded.md#2` | `国风古装/11-hf-seedance-guoman-expanded.md` | https://x.com/Soranlan/status/2082660298205376579 | 1583→1604 |
| `国漫3D/11-hf-seedance-guoman-expanded.md#3` | `国风古装/11-hf-seedance-guoman-expanded.md` | https://x.com/Soranlan/status/2083218116520145262 | 1024→1334 |
| `国漫3D/11-hf-seedance-guoman-expanded.md#4` | `国风古装/11-hf-seedance-guoman-expanded.md` | https://x.com/lansenai/status/2088960101633884280 | 2731→2738 |
| `国漫3D/11-hf-seedance-guoman-expanded.md#5` | `国风古装/11-hf-seedance-guoman-expanded.md` | https://x.com/Soranlan/status/2081379282442420321 | 2531→2555 |
| `国漫3D/11-hf-seedance-guoman-expanded.md#6` | `国风古装/11-hf-seedance-guoman-expanded.md` | https://x.com/Soranlan/status/2081683135171895618 | 1911→3033 |
| `国漫3D/11-hf-seedance-guoman-expanded.md#7` | `国风古装/11-hf-seedance-guoman-expanded.md` | https://x.com/Soranlan/status/2082278216383746196 | 1531→1523 |
| `国漫3D/11-hf-seedance-guoman-expanded.md#11` | `国风古装/11-hf-seedance-guoman-expanded.md` | https://x.com/Soranlan/status/2081891032636047589 | 2139→3399 |
| `国漫3D/11-hf-seedance-guoman-expanded.md#13` | `国风古装/11-hf-seedance-guoman-expanded.md` | https://x.com/Soranlan/status/2081716867996029303 | 1837→2973 |
| `打斗运镜/10-hf-seedance-fight-camera.md#2` | `打斗运镜/10-hf-seedance-fight-camera.md` | https://x.com/Soranlan/status/2087858835583287589 | 7370→7761 |
| `打斗运镜/10-hf-seedance-fight-camera.md#5` | `打斗运镜/10-hf-seedance-fight-camera.md` | https://x.com/liyue_ai/status/2089362604011770351 | 6649→6649 |
| `打斗运镜/10-hf-seedance-fight-camera.md#11` | `打斗运镜/10-hf-seedance-fight-camera.md` | https://x.com/Soranlan/status/2081907108690178077 | 3440→3435 |
| `打斗运镜/10-hf-seedance-fight-camera.md#17` | `短剧/10-hf-seedance-short-drama.md` | https://x.com/AI__TSUBAKI/status/2079091586315735181 | 7934→8421 |
| `打斗运镜/10-hf-seedance-fight-camera.md#19` | `打斗运镜/10-hf-seedance-fight-camera.md` | https://x.com/AI__TSUBAKI/status/2078057124350005603 | 7311→7174 |
| `特效/10-hf-seedance-vfx.md#6` | `特效/10-hf-seedance-vfx.md` | https://x.com/sipteaandcoffee/status/2055674114845925710 | 7900→8792 |
| `特效/10-hf-seedance-vfx.md#7` | `特效/10-hf-seedance-vfx.md` | https://x.com/ai_animer/status/2078023536992735573 | 7739→13314 |
| `特效/10-hf-seedance-vfx.md#13` | `产品生活/10-hf-seedance-product.md` | https://x.com/ShamiWeb3/status/2074302311275663589 | 4246→4242 |
| `特效/10-hf-seedance-vfx.md#14` | `特效/10-hf-seedance-vfx.md` | https://x.com/Chengzilhy/status/2080140918704029967 | 2932→4013 |
| `运镜/10-hf-seedance-camera-motion.md#5` | `运镜/10-hf-seedance-camera-motion.md` | https://x.com/bmx_ai13/status/2075460258646880622 | 2979→3000 |
| `国漫3D/hf-sword-duel-on-the-lake/prompt/prompt.txt#1` | `国风古装/hf-sword-duel-on-the-lake/prompt/prompt.txt` | https://x.com/john87445528/status/2023660939954860134 | 2804→3707 |
| `打斗运镜/hf-one-man-one-gun-no-mercy/prompt/prompt.txt#1` | `打斗运镜/hf-one-man-one-gun-no-mercy/prompt/prompt.txt` | https://x.com/promptsref/status/2036695357414096941 | 7916→8446 |
| `特效/hf-frost-dragon-shatters-frozen-citadel/prompt/prompt.txt#1` | `特效/hf-frost-dragon-shatters-frozen-citadel/prompt/prompt.txt` | https://x.com/restofart/status/2070513629548425643 | 7963→14642 |
| `打斗运镜/20-web-fight-camera-prompts.md#2` | `打斗运镜/20-web-fight-camera-prompts.md` | apimodels 来源页 JSON-LD | 4769→4576 |

## 其他

- `运镜/43` 策展者写的景别英文对照表：「中景」改为膝盖以上（MWS），「远景」英文改为 wide shot（依据见 `docs/术语速查.md`）。
- `打斗运镜/02` 第 1 节两条 @lansenai 提示词：来源由 twiscan 镜像改记为作者 X 原帖（2098529517736476962、2093665548714541405），twiscan 记为镜像。
- `skills/` 四个 skill 加整合说明，指向库内对应文件与术语、最佳实践文档。
- 本日志早先各节提到的旧路径（如 `prompts/fight-camera/…`、`国漫3D/…`、`其他/…`）是历史记录，保持原样。

## 2026-09-30 下午 — 抖音 AI研究院-爆老师「AI打斗别乱剪！用好一镜到底」

- 来源：https://v.douyin.com/8ojgj2g3UDs/ → aweme `7689821368011241832`（AI研究院-爆老师，抖音号 `23024530897`，2026-09-26 20:34:20 UTC+8；抓取 2026-09-30 13:45 UTC+8：921 赞 / 745 收藏 / 75 评论 / 103 分享，13:49–13:50 复抓 922 赞）。
- 新文件：`prompts/打斗运镜/34-douyin-baolaoshi-one-take-fight.md`（打斗运镜现有最高 33，取 34）。
- 获取：移动端 UA 解析短链拿 aweme id；第一次 `yt-dlp --cookies`（无头 Chrome 匿名 cookie）403，无头 Chrome 打开视频页时 detail 接口被拦、页面跳到别的视频（抓到的媒体不是本条，已丢弃）；重新取匿名 cookie 后 `yt-dlp` 成功（33.5 s，1280×720 HEVC）。文案 / 互动数 / 评论用 Googlebot UA 抓 SSR；detail JSON 的 `desc` 截断，只作前缀核对。
- 收录：帖子文案逐字（SSR `<title>` / meta / JSON-LD / h1 一致，话题前换行保留）；画面文字 34 项（5 fps 共 168 帧；第一遍原分辨率逐帧，第二遍换帧放大 1.5–3 倍，diff 0 差异，无 `【?】`）；英文字体 D/O 同形，按词义读出，对照图 `docs/douyin-blockers/8ojgj2g3UDs-glyph-O-vs-D-evidence.png`。
- ASR：Silero VAD 0 段；faster-whisper medium + VAD 0 段；不加 VAD 只在 0–1.24 s 出一段英文「What the fuck」（配乐人声或误识别），不收录；同音字修正 0 处。
- 剪辑检查：`ffmpeg scdet` 在两条长镜头内部没有明显硬切（最高 15.1 在 7.03 s 甩镜处）；甩镜可藏剪辑点，所以「一次没切」无法从成片证明，已在文件 §3 与「总结（非原文）·镜头路径、动作衔接与一致性」注明。
- 外部核对（文件 §3）：Google Cloud Veo 提示词指南、Kling 官方提示词指南 / 3.0 多镜头指南、Runway Gen-4 提示词指南与 Camera Terms、Seedance 2.0 官方发布文、StudioBinder（长镜头 / 甩镜 / 低角度）、Bordwell、Stork。分歧：甩镜在官方术语里常用作转场；Kling 把「steady tracking」列为可读动作的写法；「中景」通常不含全身；多人物会增加一致性风险。作者原文未改。
- **+0** ` ```text `：原稿把帖子文案记为 1 条 `text`；2026-09-30 整合时决定文案不是提示词，按 `打斗运镜/33`、`运镜/43` 的先例改放无语言代码块，不计数。完整提示词未公开（作者称在评论区和粉丝群，匿名不可见）→ blocker。
- 去重（`prompts/` + `cases/` + `skills/`，331 条 = 314 围栏 + 17 个 case `prompt.txt`，NFKC 去标点空白后 difflib + 6-gram 覆盖率）：文案与库内最高 ratio 0.142、6-gram 覆盖 0；34 项画面文字合并后最高 ratio 0.141、6-gram 覆盖 0.02。全库搜 `7689821368011241832`、`8ojgj2g3UDs`、「爆老师」「AI研究院」「镜头不停」「环境挨打」「人数压迫」「零剪辑点」「不落定」「环境参与」「群战压迫」「打斗不要剪」「别乱剪」：无命中。「一镜到底 / 长镜头 / one-take」在 `运镜/41`、`运镜/42`、`打斗运镜/01`、`02`、`20` 等处出现，都是不同作者的内容，**不是重复**；在 `打斗运镜/33`、`运镜/41`、`运镜/42` 的 related 行加了指向 34 的链接。
- 计数：不变（整合后打斗运镜 57，合计 270）。本条随 2026-09-30 整合分支一起提交，格式已按 `docs/条目格式规范.md` 统一（总结移到文末、章节号前移一位）。

## 2026-09-30 下午 — 新增分类「技巧锦囊」与元数据字段

- 新目录 `prompts/技巧锦囊/`（含 `README.md`）：收「想不到要问、但能给人新思路」的技巧，供主动浏览。本分类自有条目暂为 0。
- 元数据由 18 个字段增加到 20 个：在「备注」后新增可选字段「技巧钩子」「触发场景」。270 个条目元数据块全部补上这两个字段（空字符串）；脚本核对 `text` 围栏内容前后一致。
- 交叉收录：条目保留主分类，只在「标签」加 `技巧锦囊` 并填写两个字段，`scripts/build_index.py` 汇总到 `INDEX.md` 最上方；标签含 `技巧锦囊` 但字段为空时脚本报错。
- 讲解类文件（`打斗运镜/33`、`打斗运镜/34`、`运镜/43`）在「来源概述」下加「文件元数据」块，`index.jsonl` 中记为 `条目类型: reference`。
- 首条交叉收录：`打斗运镜/34`（一镜到底打斗）。专门的技巧锦囊收集任务（新条目与候选清单）尚未交付，交付后按 `docs/条目格式规范.md`「技巧锦囊（交叉收录）」并入。
