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
