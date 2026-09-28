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

**Equivalent (not Douyin verbatim):** FreyaVideo timed 「动漫《法天象地》特效提示词」 → `prompts/vfx/30-freyavideo.com.md` (explicitly *not* attributed as 小椰冻奶). YouMind 2D 格斗游戏序列 → `prompts/game-pv/` as structured fight-adjacent equivalent for 漫剧打斗 theme.

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
