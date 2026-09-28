# 00 Source Fetch Log

Fetched: 2026-09-29 Asia/Shanghai (UTC+8). Goal: publicly available verbatim AI prompts for fight/camera, Image2 denoise, character cards.

## Legend
- OK = readable content with extractable prompts or useful text
- PARTIAL = page loads but prompts thin / JS-heavy / truncated
- FAIL = blocked, empty of prompts, or unusable for verbatim extraction

## X / Twitter: @lansenai

| URL | Result | Notes |
|-----|--------|-------|
| https://x.com/lansenai | FAIL (readable prompts) | HTTP 200 SPA shell; no usable prompt text without browser/login |
| https://fxtwitter.com/lansenai | PARTIAL | HTTP 200 HTML; limited card text, not full long prompts |
| https://vxtwitter.com/lansenai | FAIL | HTTP 403 Cloudflare challenge |
| https://xcancel.com/lansenai | FAIL | HTTP 451 Unavailable For Legal Reasons |
| https://nitter.privacydev.net/lansenai | FAIL | Connection refused |
| https://twiscan.com/zh_TW/x/lansenai | **OK** | Full timeline mirror; multiple long Chinese fight/camera prompts (used as primary @lansenai source) |

## Douyin short links

| URL | Redirect chain | Readable prompts? |
|-----|----------------|-------------------|
| https://v.douyin.com/F0CQtRHUZQk/ | 302 → `https://www.iesdouyin.com/share/user/MS4wLjABAAAAnCjKlkpiZyn4b7ucXiygrRDSipBneMo52DCIi1PwJbtK2OtiV_3QBrihQUZWTpGT?...` then 200 HTML (~73KB share user page) | **No** — title/share shell only; no prompt body |
| https://v.douyin.com/bV59188e3cE/ | 302 → `iesdouyin.com/share/note/7670845777770047338/...` → 302 → `https://www.douyin.com/note/7670845777770047338?...` | **No** — note share HTML title “在抖音记录美好生活”; meta desc has no prompt |
| https://v.douyin.com/UP3Ck9IsM_U/ | 302 → `iesdouyin.com/share/video/7659111522644810153/...` | **No** — video share shell; no extractable prompt text |

**Blocker:** Douyin share pages need app/browser JS; curl/WebFetch cannot recover「心流」人物卡 prompts from these short links.

## Category research pages (succinct)

### Fight / camera
| URL | Status |
|-----|--------|
| https://twiscan.com/zh_TW/x/lansenai | OK — long Seedance-style fight prompts |
| https://aitoolsguidebook.com/zh/articles/anime-action-clip-prompts/ | OK — 10 English anime action templates |
| https://www.seedance.tv/zh/blog/seedance-2-5-fight-scene-prompt | OK — formula + pasteable templates ZH/EN |
| https://m.163.com/dy/article/KP3NASBD0532O7TK.html | OK — many short 运镜 prompt lines (fight subset cited) |
| https://www.atlascloud.ai/zh/blog/guides/seedance-2-gpt-image-2-api-tutorial | PARTIAL — workflow; one short Seedance follow-board prompt |
| https://www.chooseai.net/news/788/ | PARTIAL — method prose; few short example phrases |
| https://www.jxxy.net/ai/articles/GoSailGlobal-2041684217529340360/ | PARTIAL — workflow tips; limited full prompts |
| GitHub liangdabiao/make-prompt-seedance2 | Search-indexed; not fully mirrored here |

### Image2 / denoise / upscale
| URL | Status |
|-----|--------|
| https://istarry.com.cn/ps/gpt-image2-denoise-prompt-tutorial/ | OK — generate + edit denoise prompts EN + ZH |
| https://raw.githubusercontent.com/btwiuse/video-skills/24e4c8af/im2-clean-image/SKILL.md | OK — IM2 clean/negative hygiene blocks |
| https://ernie-image.app/blog/ei-029-img2img-guide-cn-20260506 | OK — denoise ranges + repair prompts |
| https://tudingai.cn/blog/202607/gpt-image-2-noise-grain-3-causes-fix/ | OK — Chinese clean-constraint phrases (not full long prompts) |
| https://www.chooseai.net/news/6017/ | FAIL | WebFetch 500; curl also failed this run |
| https://sandner.art/latent-interpolate-upscale-expanding-flux-and-sdxls-denoising-range/ | PARTIAL — denoise numeric guidance, not prose prompts |
| https://github.com/rik-python/Comfyu--Image-detailer-and-skin-detailer-workflows | PARTIAL — workflow settings (denoise 0.10–0.35), not text prompts |

### Character card / asset sheet
| URL | Status |
|-----|--------|
| https://aitoolsguidebook.com/zh/articles/game-character-portrait-sheets/ | OK — 12 English sheet prompts |
| https://www.ipipp.com/html/20260904/50447.html | OK — Midjourney 人设/三视图/表情包 templates |
| https://www.qpipi.com/87930/ | OK — Flux/IL/Pony CharacterDesign sheet layouts |
| https://melon-hub.com/guides/character-design-prompts | OK — MJ/SD/Flux templates |
| https://www.lovart.ai/zh/blog/ai-character-design | PARTIAL — strong workflow; almost no copy-paste prompt fences |
| Douyin「心流」 short links above | FAIL — no readable prompts |

## Files written
- `02-web-fight-camera-prompts.md`
- `03-web-image2-denoise-prompts.md`
- `04-web-character-card-prompts.md`
- `00-source-fetch-log.md` (this file)
