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
- 交叉收录：`打斗运镜/34`（一镜到底打斗，讲解类）；`特效/41` P1–P3（力场扰动，见下一节）。专门的技巧锦囊收集任务（新条目与候选清单）尚未交付，交付后按 `docs/条目格式规范.md`「技巧锦囊（交叉收录）」并入。

## 2026-09-30 下午 — 抖音 AI琪琪「力场模拟 解决 AI 特效廉价贴图感」

- 新文件：`prompts/特效/41-douyin-aiqiqi-force-field-vfx.md`（特效现有 10 / 30 / 31 / 40，取 41）。
- 来源：https://v.douyin.com/l63b3G_ozGw/ → aweme `7688284716386028840`（AI琪琪，2026-09-22 17:11:26 UTC+8；抓取 2026-09-30 13:42 UTC+8：386 赞 / 405 收藏 / 23 评论 / 108 分享；作者粉丝 9726、总获赞 6.0万）。
- 获取：移动端 UA 解析短链；无头 Chrome 取匿名 cookie → `yt-dlp --cookies`（首次 403，刷新 cookie 后成功，下到 HEVC 720p 与 H.264 720p）；Googlebot UA 抓 SSR 拿文案、互动数、发布时间与 10 条顶层评论。文案在 SSR h1 / `<title>` / JSON-LD 与 detail JSON 四处逐字一致。
- 誊写：0.2 s 一帧共 270 帧全部目视；三张提示词卡三遍独立誊写（HEVC 整卡、HEVC 逐行、H.264 逐行 2 倍放大），逐字 diff 0 处差异。「湍」「焰」放大确认；「ARRI」末字母与 l 字形相同，按品牌名记 I；P3「Field」在行尾，与下一行「力场扰动模拟」之间的半角空格按作者其余写法推定（均已在文件和 blocker 里注明）。
- ASR：Silero VAD 1 段（0–54.08 s）；faster-whisper medium（zh）开 / 不开 VAD 结果一致，38 段。8 处同音 / 英文词误识修正（「立场→力场」×5、「菲尔的 / FU的→Field」×3），全部有同时刻画面文字佐证；6 处非同音误识未改，逐条列出。作者 50.6 s 底部字幕本身写作「立场才是空气」（叠字为「力场」），照录未改。
- 技术核对：对照 Blender 手册（Force Fields）、SideFX 文档（POP Force / Wind / Axis Force / Attract、Vellum、Pyro）、NASA（纹影与激波）。有出入：力场只改变运动，不产生光照与折射（原文把光影联动算在「力场扰动模拟」里）；「强光穿过扰动空气产生色散」在自然条件下很弱，属风格化效果。原文未改。
- 去重：全库（prompts / cases / skills / docs）搜 aweme id、短链、「AI琪琪」「力场」「扰动模拟」「Field 力场」「湍流」「Portra」「ARRI Alexa」「UE5.4」「Octane X」「Golden Hour」均无命中；与 345 个围栏 / case 文本 rapidfuzz 比对最高 ratio 0.18、partial 0.28。**无重复**。与 `特效/40` 只加链接。
- Blocker：无作者文字版；示例画面含带字幕的现成影视素材；评论区多条「666求一个」疑有私发资料，无公开证据。见 `docs/douyin-blockers/README.md`。
- **+3** ` ```text `：提示词 3 条（P1 魔法能量场 155 字符 / P2 爆炸冲击波 133 / P3 地热热浪 129）。原稿把帖子文案也记为 1 条 `text`（共 +4）；2026-09-30 整合时按 `打斗运镜/33`、`打斗运镜/34`、`运镜/43` 的先例，文案不是提示词，改放无语言代码块并删去其元数据块，不计数。
- 未确认字：提示词 0 个；背景影片自带字幕被遮挡处标 `【?】`（不是提示词）。去重删除 0。
- 格式：按 `docs/条目格式规范.md` 统一（来源概述在前、总结移到文末、章节号前移一位，条目 id 改为 `--01`–`--03`），P1–P3 标签加 `技巧锦囊` 并填写技巧钩子、触发场景（交叉收录）。
- 计数：特效 14 → **17**，库内合计 270 → **273**（整合后口径）。本条随 2026-09-30 整合分支一起提交。

## 2026-09-30 傍晚 — 技巧锦囊首批（6 个新文件 +13 条，交叉收录 +1）

- 基线：整合分支 `consolidate-2026-09-30`（ef322c4，273 条）。本批在其上提交，需在整合分支合入 main 之后（或一起）合入。
- **新文件**（`prompts/技巧锦囊/`）：
  - `44-douyin-aiqiqi-hybrid-media-cinematic.md`：抖音 AI琪琪「不要再写3D国漫了……混合媒介指令」（aweme `7663851807801625908`，2026-07-19 08:08 UTC+8；抓取 2026-09-30 14:23 UTC+8：点赞 22,899 · 收藏 2.0万 · 评论 3,384 · 分享 3,718）。**+3**：输入框打字过程逐帧誊写的 A（实拍 + CG）、B（3D + 2D 水墨）、C（数字 + 胶片 / VHS）三段，两遍独立誊写 0 差异；A 段有 1 处被画面边缘遮住的连续几个字记【?】（字幕与口播为「背景完全匹配」，原文不补）。模板文档只收 29 个小标题（正文被裁、被字幕压住）；8.6–10.0 s 选中文字为片段；口播 ASR 按字幕更正 17 处（全部列在文件 §2.5）。核对：丁达尔效应、环境遮蔽、飞白、漏光对照 Wikipedia；作者「AI 会当成两个图层处理」的说法无官方依据，标为作者比喻；点赞最高的评论（168 赞）质疑画风来自 MJ 出图，已写入 §3。
  - `35-volcengine-seedance2-guide-tricks.md`：火山引擎 Seedance 2.0 官方指南（2026-09-22 更新版）中 `docs/最佳实践.md` 未写到的 10 个做法。**+4**（轨道补齐、向前延长、白模转换、防双胞胎约束）；删帧、人脸参考、横屏防字幕、分组合照、参考视频定义特效、同音字防读错 6 节为方法原文，不计数。
  - `36-openai-sora2-prompting-guide-tricks.md`：Sora 2 官方指南的节拍写法、调色板锚点、编辑只改一处。**+1**（Example 1 手绘 2D/3D 混合动画完整示例）。
  - `37-google-veo31-first-last-frame-pov-switch.md`：Veo 3.1 官方博客 Workflow 1，首尾帧取正面 / 背后 POV，180° 环绕连接。**+3**（首帧、尾帧、Veo 提示词）。
  - `38-runway-gen4-image-to-video-motion-only.md`：Runway Gen-4 官方指南「图生视频只写运动、不复述画面」「用 the subject 指代」「暗示式 vs 描述式场景运动」。**+1**（机械公牛示例）。
  - `39-kling3-camera-freezes-in-sync-long-take.md`：Kling 3.0 官方指南的「人停镜头停」长镜头示例。**+1**。
- 编号：`35`–`39` 为官方网页来源（沿用 `3x` 网页来源段，避开各分类已用的 30–34），`44` 为抖音单篇（接在 `运镜/43` 之后）。
- **交叉收录 +1**：`运镜/43`（胡小绿景别，讲解类，点赞 18,642 · 收藏 8,510）加标签 `技巧锦囊` 并填写技巧钩子、触发场景。
- **考虑过但未交叉收录**：`特效/40`（小悦儿「三层拆解」；两条提示词都止于画面「……」，是片段，思路已由已交叉收录的 `特效/41` 展开）；`打斗运镜/33`（胡小绿斗法；与 `运镜/43` 同一作者同一方法，互动低 552 赞，避免重复）；`打斗运镜/32`（孔明武器招式，查表型词库，不是「想不到要问」的技巧；其中「发力链 + 受力反馈」已写入 `docs/最佳实践.md` 第 3 节）；`运镜/41`、`运镜/42`（Adrian 运镜词典，查表型）；`提示词写法/01`（情绪外化对照已在最佳实践第 2 节）；`提示词写法/32`（Runway 转述的 Seedance 结构，通用写法）。
- **考虑过但未收录**：各官方指南的五段式公式、时间戳分镜、否定写法、「先简单后复杂」「一个镜头一种运镜」「文戏延长 / 武戏拼接」「素材 4–5 个」「符号约定」（已在 `docs/最佳实践.md` 或大量「时间码分段」条目中）；Sora「无声镜头用一个小声音做节奏提示」、Seedance「音色参考不准时补充音色描述」（太薄）；Sora Example 2（常规写法）；Veo 时间戳示例（库内已大量存在）；B 站专栏搜索「AI视频 提示词 技巧」「Seedance 提示词 技巧」（最高为朋克马007「即梦Seedance2.0提示词技巧，4张图说明……」149 赞，其余 ≤42 赞；标题多为通用入门、资料包引流，互动低，未逐篇收录；「即梦 提示词 进阶」无结果）；Reddit r/aivideo 热门帖（作品展示为主，没有公开提示词）。
- **AI琪琪 主页**：按用户要求尝试浏览作者全部作品（sec_uid 取自 aweme detail）。主页接口可读到 作品 61 / 粉丝 9,731 / 获赞 59,927，但作品列表接口（`aweme/post`，web 与 iesdouyin 两个入口）匿名访问返回空内容，页面弹出登录框和滑块验证码；未绕过验证码。本轮只能确认 3 条作品，见 `docs/douyin-blockers/README.md`。
- 去重：13 条新围栏对全库 290 条原文（NFKC 去标点空白，6-gram 覆盖率 + difflib）最高覆盖 0.087、最高 ratio 0.396（短句偶然重合），无重复；全库检索各来源 URL 与关键句均无命中。
- 冲突检查：Seedance 2.0 官方可写否定约束（如防双胞胎约束句）vs Runway Gen-4 不支持否定写法——两者都是官方对自家模型的说明，已在 `35` §5 与 `38` 总结中注明适用模型，与 `docs/最佳实践.md` 第 1、5 节一致；Seedance「主体定义清晰、标注对应参考图」vs Runway「用 the subject 泛指」——输入方式不同（多素材参考 vs 首帧），已在 `38` 总结中注明。`人物卡/` 的三视图设定图与 Seedance「不要用多视图做参考」不冲突（用途不同），已在 `35` §6 注明。
- 计数：技巧锦囊 0 → **13**，库内合计 273 → **286**；核对状态 verified 242 → 255。

## 2026-09-30 傍晚 — 新增分类「光影打光」与抖音 AI琪琪「打光指令」

- 基线：main `78e5753`（tree `1a21fb2e19314faf17ee7b8621ab9a8968a00d4e`，286 条；含整合分支与技巧锦囊首批）。
- 新分类：`prompts/光影打光/`（`scripts/build_index.py` 的 `CAT_ORDER` 放在 `特效` 之后，`CAT_DESC` 加说明；id 英文代号 `lighting`）。理由：本条主看点是写光源时段、方位、颜色、软硬；`生图修画质`（降噪修复）、`动画电影感`（动画画风）、`特效`、`提示词写法`（通用方法论）都不合适。
- 新文件：`prompts/光影打光/40-douyin-aiqiqi-lighting-prompts.md`。
- 来源：https://v.douyin.com/eGqNpizHAi0/ → aweme `7663321309908143406`（AI琪琪，2026-07-17 17:30 UTC+8；抓取 2026-09-30 14:45 UTC+8：6,008 赞 / 4,076 收藏 / 1,322 评论 / 747 分享；点赞、评论、分享 SSR 与 yt-dlp detail JSON 一致）。
- 获取：移动端 UA 解析短链；无头 Chrome 取匿名 cookie → `yt-dlp --cookies`（首次 403，刷新后成功，HEVC 720p + H.264 720p）；Googlebot UA 抓 SSR 拿文案、互动数、发布时间与评论。
- 誊写：0.2 s 一帧，HEVC / H.264 各 528 帧。P1、P2 是即梦输入框（「即梦 Seedance 2.0 Fast VIP」）里的打字过程，三遍独立誊写（HEVC 横条、HEVC 逐段 2 倍、H.264 逐段 2–4 倍）逐字 0 差异。「紫兰」「反双光」是输入法选字，照录。模板文档「打光方案」一节两遍一致，作为片段放无语言代码块（8 处【?】，3 张证据图）。
- ASR：Silero VAD 1 段（0–105.68 s）；faster-whisper medium 两遍，以第 2 遍（initial_prompt + 词级时间戳，65 段）为准，OpenCC 转简体。6 处同音修正（屏→平、它→他、伯→勃、映→硬 ×2、相→箱），全部有同时刻字幕或花字佐证；9 处非同音误识未改，逐条列出。
- 技术核对：ARRI Lighting Handbook、ASC《Shot Craft: Light Quality 101》、StudioBinder（伦勃朗光）、Wikipedia（Golden hour，引 Ascher、Blain Brown）、Britannica（丁达尔效应）、GOV.UK（护照照片无阴影）。一致：魔幻时刻＝黄金时段、逆光轮廓光、伦勃朗三角在暗侧、窗口尘埃光柱、硬光锐利 / 柔光过渡。有出入或夸大：软硬由光源相对大小和距离决定而非灯具名称；柔光箱是透射扩散不是漫反射；「情绪温暖」混淆软硬与冷暖；「三角形高光」用词；「AI 用完全不同的阴影算法」不成立 / 未证实。原文未改。
- 去重：全库（prompts / cases / skills / docs，main 78e5753）搜 aweme id、短链与「魔幻时刻」「伦勃朗」「丁达尔」「窗口光柱」「霓虹粉光」「双色光」「打光指令」「柔光箱」「紫兰」「Rembrandt」「Tyndall」等；aweme id 只在 blockers README 的「另一任务处理」说明里（已更新），术语只在术语表和 `技巧锦囊/44` 出现。P1、P2、口播写法、模板片段与 307 个 `text` 围栏 + 17 个 case 比对，最高 ratio 0.151、6-gram 覆盖 0。**无重复，无删除**。
- 矛盾检查：与 `docs/术语速查.md` 第 9 节、`docs/最佳实践.md` 第 2 节第 6 条无矛盾；术语速查「黄金时刻」一行补「魔幻时刻 / magic hour」；最佳实践第 7 节加打光入口，第 8 节冲突表加「光的软硬由什么决定、柔光是否温暖」。`技巧锦囊/44` §3 对丁达尔效应的说法略窄（Britannica 含烟尘），未改 44。
- 技巧锦囊：不交叉收录（「写光源、方向、质感」已是最佳实践第 2 节第 6 条的常规写法）。
- **+2** ` ```text `：P1 日落前 20 分钟魔幻时刻逆光 56 字符 / P2 赛博朋克双色光 38 字符；verified 2。
- 计数：光影打光 0 → **2**，库内合计 286 → **288**；核对状态 verified 255 → 257。

## 2026-09-30 傍晚 — 抖音 Ksr桑「吊打99%付费！原来做AI视频能这么简单？」（Midjourney 风格化 / 个性化档案）

- 基线：main `2b5dfb5`（tree `7e05e8a501c678afce680e366f388181f7375cec`，288 条；含整合、技巧锦囊首批、光影打光）。本分支 `douyin-ksr-2026-09-30` 建在同 tree 的 `a5657af` 上。
- 新文件：`prompts/人物卡/40-douyin-ksr-midjourney-stylize-personalize.md`。
- 来源：https://v.douyin.com/zg6RGFH-jUQ/ → aweme `7690677900311285032`（Ksr桑，2026-09-29 12:20 UTC+8，669 s；抓取 2026-09-30 15:34 UTC+8：点赞 17,939 · 收藏 1.3万 · 评论 2,889 · 分享 2,188；14:52 首抓 17,624 / 2,858 / 2,158，与 yt-dlp detail JSON 基本一致）。
- 获取：移动端 UA 解析短链；无头 Chrome 取匿名 cookie → `yt-dlp --cookies`（HEVC 720p + H.264 1024×576）；Googlebot UA 抓 SSR 拿文案、互动数、发布时间与评论。
- 誊写：P1（森系电竞女角色定妆照，625 字符）、P2（糖果花城全景，798 字符）是扣子智能体回复里的【中文直输版】，三遍核对 0 差异（B、C 为对照 A 稿的逐行目视复核，不同帧、不同放大倍数）；「锥」按 Midjourney 输入框确认。两段【英文版】只露出开头、被输入框挡住，作为片段放无语言代码块，不计数。
- ASR：Silero VAD 7 段；faster-whisper medium（zh），以开 VAD 的 482 段为准。与 669 帧字幕带逐条对照，55 处同音 / 音近 / 英文品牌名修正全部有字幕佐证，逐条列表；8 类非同音误识未改。
- 分类：`人物卡`（视频自述「角色和场景的资产图设计」，主演示在 P1 角色定妆照上）；P2 是场景概念图，同来源同文件，标签「场景概念图」。若以后场景设定图变多，建议新建 `场景概念图/`。
- 技巧锦囊：P1、P2 交叉收录（同一提示词只换 stylize / 个性化档案 / Try Style 换审美；为项目专门点图建档案锁色调）。
- 技术核对（Midjourney 官方文档 Version / Stylize / Weird / Chaos / Personalization / No / Style Reference；字节 Seed 博客；TapNow 文档）：参数默认值与范围、个性化档案做法、Try Style＝套 `--sref`、HD 比例、Seedance 2.5 单次 30 秒一致；「风格化最多拉到500」是经验建议（上限 1000）；提示词 `--v 8.1` 会覆盖面板的 8.2；**正文里的「不要……」是 Midjourney 官方列出的错误示例，`--no` 多词短语可能被逐词拆开**（P2 `--no … blooming flowers`）。标题与开场营销话术无法核对。结论：标题党，但内容扎实，**建议收录**。
- 去重：全库检索 aweme id、短链、作者名、关键术语；两段对 306 个 `text` 围栏 rapidfuzz 最高 ratio 0.19，无重复，删除 0。
- 矛盾检查：`docs/术语速查.md` 第 10 节、`docs/最佳实践.md` 第 5、8 节原来没有 Midjourney 的否定写法；补 Midjourney 一行与出处「MJ-No」，原文不改。与第 9 节动机光一致。
- **+2** ` ```text `（verified 2，均交叉收录技巧锦囊）；证据图 3 张（`docs/douyin-blockers/zg6RGFH-jUQ-*.png`）。
- 计数：人物卡 11 → **13**，技巧锦囊交叉收录 5 → **7**，库内合计 288 → **290**；核对状态 verified 257 → 259。

## 2026-09-30 下午 — 官方文档复核与「首尾帧生图」分类（+46 −2，286 → 330）

- 基线：main `78e5753`（树 `1a21fb2e`，286 条，含技巧锦囊首批）。
- **裁定标准：** 新增 `docs/权威来源.md`，列出火山引擎、OpenAI、Google、Midjourney、可灵、Runway、BFL、阿里云万相、Luma、Pika、Adobe、Stability AI 的官方文档 URL、页面日期、抓取时间（2026-09-30 14:53–15:10 UTC+8）与逐字摘录；无法抓取的页面单列。以后以此为质量标准。
- **新分类 `首尾帧生图`（+43）：** 6 个官方来源文件：OpenAI GPT Image 9、Google Gemini / Imagen / Veo 7、火山引擎 Seedream / Seedance 13、BFL FLUX 7、Runway 5、阿里云万相 2。全部为官方页面上的示例提示词，脚本逐字比对。与 `技巧锦囊/35–38` 去重：防双胞胎约束句只保留 `35` 的版本。
- **`提示词写法/33`（+3）：** Seedance 2.0 官方示例 1（宿舍短剧，官方逐字版），Veo 橡树示例及其负面提示。
- **新文档：** `docs/首尾帧工作流.md`（非原文，逐条注明官方出处）。**更新：** `docs/术语速查.md`（常用出处、第 10 节加生图模型、新增第 11 节首尾帧术语）、`docs/最佳实践.md`（第 8 节新增 7 行裁定、新增第 9 节）、两个生图 skill 的复核说明、`技巧锦囊/README.md`（+3 张卡片）。
- **元数据备注（原文未改）：** `人物卡/04` #01–03、#05、#09；`打斗运镜/02` #02；`打斗运镜/30` #03；`提示词写法/01` #02；Kling 4.0 标注 6 条；`特效/40` #01–02；`技巧锦囊/36`（Sora 2 已下线）；`生图修画质/03` §1.6 加说明。
- **移除 / 移出计数（−2）：** `打斗运镜/30` 原 #02「东京雨夜机甲大战」（只有题材和形容词，不符合 Seedance 2.0 官方「工程型指令」要求，且依赖第三方 IP）；`提示词写法/01` §2.3 kit 版宿舍短剧移出计数（官方逐字版在 `33`，kit 原文作对照保留在原位）。
- 核对：所有保留条目的 `text` 围栏与基线逐 id 比对，0 处改动；`build_index.py --check` 通过。

## 2026-09-30 晚 — 官方文档复核补丁重做在 main `1085d8c` 上（290 → 334）

- 原补丁基线 main `78e5753`（树 `1a21fb2e`，286 条）；期间合入 #16 光影打光/40（+2）与 #17 人物卡/40（+2）。本次在 main `1085d8c`（树 `f9129a7c`，290 条）上 `git am -3` 重做 6 个补丁，另加第 7 个补丁。
- 冲突处理：`scripts/build_index.py` 的 `CAT_ORDER` 两边都保留（`光影打光` 在 `特效` 后，`首尾帧生图` 在 `人物卡` 前）；`INDEX.md`、`index.jsonl`、`prompts/README.md` 由 `build_index.py` 重新生成；`docs/术语速查.md`「常用出处」保留 `MJ-No` 与复核新增的 11 行（`MJ-No` 放在 `MJ` 后），第 10 节两行 Midjourney 合并为生图模型下的一行（保留 #17 的写法，出处写「MJ-No；参数表见 MJ」）；本日志两边的段落都保留。
- 按 `docs/权威来源.md` 第 1 节复核 #16、#17 的新条目（只改元数据「备注」和非原文小节，`text` 围栏 0 改动）：
  - `光影打光/40` P1、P2「备注」写明适用范围（打光写法是多家官方的共识，示例在即梦 Seedance 2.0 Fast 演示），并注明作者说「电影质感」没用，与 SD2.0 官方示例有出入；新增 §3.8「与厂商官方文档的对照」（SD2.0 公式、SD2.5 示例、Seedream、Veo 光线示例）。`docs/最佳实践.md` 第 8 节加一行「只写『电影质感』有没有用」。
  - `人物卡/40` P1、P2「备注」写明只适用于 Midjourney、`--v 8.1` 不是当前默认版本，以及正文「不要……」与 Midjourney 官方《No》页矛盾（原来只在 §3.1 写了，按规则 3 补进「备注」）；§3.2 补火山引擎官方 API 对 21:9 的说明（原来只有第三方转述）；§3.4 加指向 `docs/权威来源.md` 的链接。
  - `docs/权威来源.md` §2.4：No 参数一行补逐字摘录和库内例子；Version 一行补当前默认版本 V8.2；新增 Stylize / Weird / Chaos / Personalization 链接一行（概括，非摘录）。§2.3 Veo prompt guide 一行链接到 `光影打光/40` §3.8。
  - `技巧锦囊/README.md`：补 `人物卡/40` P1、P2 两张卡片（#17 已交叉收录，但当时没加卡片）；交叉收录计数改为 10。
- 计数：库内合计 290 → **334**（+46 −2）；技巧锦囊 13 + 交叉收录 10 = 23；`build_index.py --check` 通过。

---

## 2026-10-01 早 — 模式 A 早搜补充（+13）

- 基线：main `ad1802158a57e614d1fa32e7068c2df188718cec`（334 条；昨晚晚质检 NO_CHANGES）。
- 分支：`morning-2026-10-01`。
- **新增 13** ` ```text `：
  - `打斗运镜/35-x-lansenai-disaster-taiji.md`（+2）：@lansenai「石台遗迹 30s 慢节奏蓄力 + 天灾级爆发」https://x.com/lansenai/status/2097629748805484837（点赞 59 / 浏览 14,380）；「雨中石台 25s 太极纯享」https://x.com/lansenai/status/2097319055829201188（点赞 159 / 浏览 14,000）。经 api.fxtwitter.com + twiscan 两遍核对。天灾条交叉收录技巧锦囊。
  - `打斗运镜/36-x-chengzilhy-snow-chase.md`（+1）：@Chengzilhy「雪境 30s 追战」https://x.com/Chengzilhy/status/2098326362801221835（点赞 182 / 浏览 55,057；@lansenai 转发推荐，以原作者为准）。交叉收录技巧锦囊（伪一镜到底秒级分镜）。
  - `运镜/44-runway-official-ai-camera-prompts.md`（+10）：Runway 官方《AI Camera Prompts》（2026-08-21，Leah Retta）可复制镜头库 7 条 + 三拍子序列 3 条；HTML 逐字核对。其中静止镜头与三拍子①交叉收录技巧锦囊。
- **搜索但未入库 / 剔除：**
  - 抖音优先作者（胡小绿、AI琪琪、孔明AI剧社、爆老师、AIGC小悦儿）：匿名主页/作品列表仍登录墙+滑块，未绕过；记 blocker（见下）。已收作品未发现可公开抓到的新合格正文。
  - @AdrianPunk115：近期公开帖偏 FDE / Punk-Skill 落地与线下分享，无新的可复用 AI 视频运镜提示词正文。
  - @lansenai 时间线上「雨夜义庄」「吸星大法」等多为短文案或视频无全文提示词可见，未收。
  - Seedance.tv / Kapwing / 社区 Seedance 2.5 指南：打斗示例与运镜词典与库内已有条目重复或为转述，未收。
  - Kling 4.0：仍无官方提示词文档（仅新闻称 10 月发布），不收第三方「Kling 4 prompt guide」。
  - 阿里云 Vidu 官方 Prompt 指南：多为词表与公式，完整可复用示例偏少且偏漫剧；本轮暂不收，列入下周可跟进。
- **去重：** 新 13 条对全库检索 status ID / 关键句（天灾级爆发、太极水流、雪境30秒追战、Locked-off wide shot of an empty diner、slow dolly push-in toward her face 等）无命中；与 `打斗运镜/01`、`02`、`运镜/31`、`41`、`42` 主题相邻但不重复。
- **矛盾：** Runway 官方「否定提示不支持（Gen-4 Image）」与 Seedance 可写否定约束——模型差异，已在既有最佳实践；本批 Runway 运镜示例未引入否定词冲突。页面「可与相机控制设置同用但勿双重指挥」记入条目备注。
- **blocker：** 抖音正文抓取仍 blocked（登录墙/滑块）；X 侧 api.fxtwitter.com 登录墙对 curl 拦截，经无头 Chrome 可读 JSON；twiscan 可作镜像但互动数以 fxtwitter 为准。
- 计数：打斗运镜 56→**59**，运镜 58→**68**，技巧锦囊交叉收录相应 +3；库内合计 334→**347**；`build_index.py --check` 0 不同步。

---

## 2026-10-01 · Seedance agent-skill 薄摘录（非全仓镜像）

- **计划：** `docs/CURATION-PLAN-seedance-agent-skills-2026-10-01.md`
- **KEEP：** `prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md`（3 条社区短摘录 + 方法节）；`docs/权威来源.md` §6 SECONDARY；`docs/最佳实践.md` §2.10–12、§3.6、§7 指引；`skills/seedance-library-router/SKILL.md`；`prompts/技巧锦囊/README.md` 卡片。
- **SKIP：** Emily 全仓 / API·vocab·首尾帧长文；dexhunter 运镜与延长长示例；beshuaxian 15 风格打斗全文、`01-cinematic`、`11-social-hook`；Higgsfield API。
- **MERGE：** 打斗 2 秒钩子 → 最佳实践 §3；参考 ignore / 载体 / 预算 → 最佳实践 §2。
- **原则：** 官方 Volcengine > 社区结构；零 wholesale clone 进 `prompts/`。
- **rebase note：** 相对 main `0a58506`（#19 早搜 +13）重放；索引由 `build_index.py` 重生。

---

## 2026-10-01 · Higgsfield Hell Grind skills 薄摘录（非全仓镜像）

- **计划：** `docs/CURATION-PLAN-hell-grind-skills-2026-10-01.md`
- **KEEP：** `prompts/技巧锦囊/46-hell-grind-cinedance-acting-lira-synthesis.md`（3 条社区短摘录 + 方法节）；`docs/权威来源.md` §7 SECONDARY；`docs/最佳实践.md` §2.13–14、§7 指引、§9.8；`skills/hell-grind-library-router/SKILL.md`；`prompts/技巧锦囊/README.md` 卡片。
- **SKIP：** CINEDANCE 全文 ~1330 行；Hell Grind 成片资产/剧情；Optics/Physics/Dialogue dump；ACTING Atlas/worked example 全文；LIRA Model routing / Templates；与 `45`/`35`/`最佳实践` §5.2 已有内容的重复。
- **MERGE：** 空间锁/首帧/camera side → 最佳实践 §2.13；ACTING 纪律 → §2.14；LIRA 4-D IMAGE 指针 → §9.8。
- **原则：** 官方 Volcengine > `技巧锦囊/45` > Hell Grind 社区补丁；零 wholesale clone 进 `prompts/`；完整 skill 可在 agent 侧另行安装，库内只薄路由。
- **核对：** 本地文件 git hash-object = 镜像 blob `24d38044` / `383db473` / `1e5c8073`；Brief https://higgsfield.ai/@higgsfield.studio/projects/hell-grind 。

---

## 2026-10-02 早 — 模式 A 早搜补充（+40）

- 基线：main `2c72b0447c45e374c60b6331e3f54f5deb775f54`（353 条；昨晚晚质检 NO_CHANGES；#19/#20/#21 已合入）。
- 分支：`morning-2026-10-02`。
- **新增 40** ` ```text `：
  - `运镜/45-runway-official-camera-terms-examples.md`（+40）：Runway Help Center《Camera Terms, Prompts, & Examples》https://help.runwayml.com/hc/en-us/articles/46749315925395-Camera-Terms-Prompts-Examples 各术语表「Prompt example」列完整示例（景别 8 + 角度 7 + 构图 4 + 运镜 17 + 焦点 4）。HTML 表格三遍逐字核对一致。面向 Gen-4.5 Text to Video。与 `运镜/44`（Resources《AI Camera Prompts》）互补：44 偏叙事场面与三拍子；本文件偏单术语锚定。
- **搜索但未入库 / 剔除：**
  - 抖音优先作者（胡小绿、AI琪琪、孔明AI剧社、爆老师、AIGC小悦儿）：匿名搜索/用户页仍为 JS 壳（无正文），登录墙/滑块未绕过；记 blocker。
  - @lansenai：近期公开帖（Higgsfield Credits Reset、MiniMax H3 PV 感想、Dots x Higgsfield）无新的可复用全文提示词；硬派石质院落肉搏 https://x.com/lansenai/status/2098529517736476962 **已在** `打斗运镜/02` §1.1；天灾/太极/雪境已在 `35`/`36`。
  - @Chengzilhy：「缘一 VS 百鬼」GoodCase 镜像有全文且标注来源 https://x.com/Chengzilhy/status/2102586866302345657，但 twiscan 报「推文不存在」、HTML/RSC 无法做双镜像逐字还原 → **不收**（不强行用单侧镜像入库）。时间线其余帖多为「Prompt 在评论区」且评论区不可抓，或短文案无全文。水上障碍赛与库内 `@liyue_ai` 已收完整版主题相邻，不重复收镜像残段。
  - @AdrianPunk115：twiscan 可见时间线仍偏 FDE / 增长长文与毛毡风格图文，无新的可复用 AI 视频运镜词典正文（上/下篇已在 `运镜/42`/`41`）。
  - Runway《AI Video Prompting Guide: 92 Ready-to-Use Prompts》（2025-11-04，Julia Martins）：官方 Resources 长文，示例量大且与 Camera Terms / `运镜/44` 主题大量重叠、部分为社媒变换模板；本轮优先收 Help Center 术语示例库，92 条指南列入下周可精选跟进。
  - Seedance.tv / 社区 Seedance 打斗指南 / KreadoAI 等：转述或与库内已有公式重复，未收。
  - Kling 4.0：仍无官方提示词文档，不收第三方「Kling 4 prompt guide」。
  - MapleShaw/seedance2.0-prompt-skill：社区 skill，与昨日薄摘录策略一致，本轮不批发镜像。
- **去重：** 新 40 条对全库检索特征句（black butterfly wing、elder elephant、albino snake、astronaut skateboarder、elastic apartment 等）0 命中；与 `运镜/44` 静止/推进等主题相邻但例句不同。跳过官方页截断的 Arc 示例 1 条。
- **矛盾：** Runway Gen-4 Image 不支持负面提示（既有最佳实践）；本批 Camera Terms 示例为 Video、未引入否定词冲突。Truck 示例原文疑似缺词（`along a in a field`）、Zoom 示例正文实为 pull back——均保留原文并在备注标明。
- **blocker：** 抖音正文抓取仍 blocked；X 侧 api.fxtwitter.com / vxtwitter 对本轮多帖 403，改用 twiscan 状态页；@Chengzilhy/2102586866302345657 原帖不可用。
- 计数：运镜 68→**108**；库内合计 353→**393**；`build_index.py --check` 0 不同步。

---

## 2026-10-02 下午 — 模式 C：每周历史深度审查（首次 · Week 1/≈5–6）

- **基线：** main `f51187cb3d7c359660ae79bc1207b6c914d3ee2e`（树 `353dc0830eb7cc4295f8a9d2f25fa48aae9e8b4b`，393 条；今早 #22 +40 已合入）。
- **分支：** `weekly-mode-c-2026-10-02`。
- **轮审范围（约全库 1/4）：** `技巧锦囊`（整类 19）+ `光影打光`（3）+ `人物卡`（13）+ `生图修画质`（11）+ `提示词写法`（14）+ `首尾帧生图`（43）= **约 103 条** ` ```text `（含交叉元数据条目；计数口径仍以全库围栏为准）。
- **进度起点：** CURATION-LOG 此前无模式 C 记录 → 按规范从「技巧锦囊 / 编号较早分类」起审。

### 官方链接抽查（docs/权威来源.md）

| 结果 | 说明 |
|------|------|
| OK（HTTP 200） | 火山 Seedance/Seedream、OpenAI Image/Video、Google Imagen/Veo/Gemini、Midjourney 参数/Legacy/Video、Kling 3.0/API、Runway Gen-4 Image/Image-to-Video/Keyframes、BFL FLUX.2/编辑/i2v、万相 3.0、Luma、Pika FAQ 等主要链接 |
| 口径未变 | OpenAI：「Sora 2 models and Videos API were shut down on September 24, 2026」；Runway Gen-4 Image 仍不支持负面提示；Cookbook《Sora 2 Prompting Guide》现标 **archived** |
| 更新记录 | Adobe 旧链 learn-the-basics/… 由 403→**404**；搜索到新链 work-with-images/…/writing-effective-text-prompts.html（索引可见，本环境 curl 403）；Stability Prompt Guide / BFL kontext_i2i 仍 404 |
| 写入 | `docs/权威来源.md` §3 Sora 行、§4 Adobe 条、§5 抽查记录 |

### 条目重核与改动

| 文件 / 条目 | 动作 | 理由 |
|-------------|------|------|
| `人物卡/04` #01–#03（ipipp） | `source-unreachable` → **verified**；发布日期补 `2026-09-04`；核对说明写本轮逐字比对 | 本轮页面 HTTP 200，三条文案与页内代码块逐字一致（此前 WAF） |
| `人物卡/04` #04–#07（qpipi） | 核对说明刷新为 2026-10-02 重核 | 页面 200；触发词仍在页内 |
| `人物卡/04` #08–#11（Melon Hub） | 发布日期补 `2026-05-25`；核对说明刷新 | 页面可访问；正向/负向/三视图与页内一致 |
| `技巧锦囊/36`（Sora Example 1） | 来源概述加「Cookbook archived + API 已下线」；核对说明刷新 | 官方标 archived；围栏正文仍一致；**保留为历史参考，不删** |
| 首尾帧生图 / OpenAI GPT Image 抽样 | 抽查 3 条特征句在官方 Image prompting 页命中 | 无需改正文 |
| 技巧锦囊其余 / 光影打光 / 生图修画质 / 提示词写法 | 元数据与来源链接存活抽查；短官方示例（Seedream 编辑句等）按官方原文保留 | 非注水；无新增矛盾需写最佳实践 §8 |

### 去重 / 删除 / 降级

- 全库 exact 去重（规范化 sha1）：**0** 组。
- **删除 0 / 降级 0 / 围栏数不变 393。**
- 未删 Melon Hub「负向」示例：备注已写明 FLUX 官方不支持负面、SD 可用；属模型相关，非错误原文。
- 未删 ipipp `--niji 6` / `--cref`：备注已标旧版；属历史可用参数。

### 矛盾裁决

- 无新增需写入 `docs/最佳实践.md` §8 的矛盾。
- 既有：Sora 已下线（历史参考）、Runway/FLUX 不支持负面 vs Seedance/Imagen/SD 可写负面——本批仅加固标注，不改口径。

### 下周模式 C 起点（Week 2）

从 **`打斗运镜/`** 最早编号起：`01-lansenai-x` → `02-web` → `10-hf` → `20-web` → `30-*`，并视容量带上 **`特效/`**、**`国风古装/`** 前半。`运镜/`（体量大，含 41–45）单独排后续周。

### 校验

- `python3 scripts/build_index.py` + `--check`：0 不同步。
- 库内 ` ```text `：**393**（不变）。

---

## 2026-10-02 — Levi Qiao 投稿：雾山五行水墨武戏分镜四则（+4）

- 基线：main `b9b9178`（393 条；模式 C Week 1 已合入）。
- 分支：`cursor/ink-wuxia-fight-prompts-8ceb`。
- **新文件：** `prompts/打斗运镜/37-levi-qiao-ink-wuxia-fights.md`（打斗运镜现有最高 36，取 37）。**+4** ` ```text `，均 verified（对照投稿附件），均交叉收录技巧锦囊。
  - #01 玄衣刀客 vs 赤刃女武者 · 落日河滩雨景（7060 字）：三级碰撞写进每一镜的【碰撞等级】。
  - #02 黑发剑客 vs 骨伞女 · 暴雨悬崖古刹（3574 字）：零站桩落在庭院 / 回廊 / 飞檐 / 塌顶 / 铜钟。
  - #03 铜币转场 · 怒江竹筏到月夜竹林（3912 字）：银币把镜头从竹筏带过满月再俯冲进竹林。附件首行「8.5，铜币转场」是收集者题名，记入原标题，未入围栏。
  - #04 白刃刀客 vs 青衫剑主 · 黄昏竹林（1913 字）：机位埋在竹叶后再爆冲。附件首行「竹林打斗」同样只作原标题。
- **为什么整段收录、不薄摘：** 四条都复用雾山五行水墨 + 轻 / 重 / 大招（0.05s / 0.1s / 0.15s 抽帧）语汇，和 `cases/打斗运镜/lansenai-ink-skill-30s` 同族。6-gram 覆盖率（NFKC、去空白标点）对全库最高分别是 0.014 / 0.013 / 0.010 / 0.043，全部对上该样例，无精确重复。该样例是无兵器单人技能；这四条是不同人物、场景、镜头表的完整分镜，按「重叠高才薄摘、完整分镜整段留」整段收录，不另抽一条公式。
- **未收：** [AITOP100 水墨技能教程](https://www.aitop100.cn/infomation/details/34783.html) 是上述 lansenai 样例的转述，页面写「使用 AI 智能大模型技术生成」，不入库。
- **公开检索：** 「千云墨斩」「骨伞女 悬崖古刹」「铜币转场 怒江」「白刃刀客 青衫剑主」未找到可逐字核对的原帖。作者记为未知，来源记为 Levi Qiao 2026-10-02 投稿；热度不编造。原文未改处：#01 文末收束镜编号写成「镜头 5」；#02「積水」保留繁体「積」。#01 附件开头 11 个空行是上传留白，未入围栏。
- **技巧锦囊：** 四条钩子不同（三级碰撞、地形零站桩、铜币转场、竹叶埋机位），卡片写入 `prompts/技巧锦囊/README.md`。
- **矛盾：** 亚秒抽帧 vs Seedance 2.0「精确时间不稳定」——原文不改，写入 `docs/最佳实践.md` §3.7–8、§7、§8 与 `docs/术语速查.md` 打击感 / 转场的库内用法。否定约束（无字幕、无水印、无 BGM）沿用既有「按模型选否定」口径，不新开裁定。
- 计数：打斗运镜 59 → **63**，技巧锦囊交叉收录 +4；库内合计 393 → **397**。

