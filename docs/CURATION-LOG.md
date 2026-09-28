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
