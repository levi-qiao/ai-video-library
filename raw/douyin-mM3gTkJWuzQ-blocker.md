# Douyin ingest attempt — mM3gTkJWuzQ

- short_url: https://v.douyin.com/mM3gTkJWuzQ/
- author (from user cue): AI绘梦菌
- title (from user cue): AI提示词编写思路 # AI教程
- resolved_aweme_id / video_id: 7690573169337453860
- share_url: https://www.iesdouyin.com/share/video/7690573169337453860/
- canonical: https://www.douyin.com/video/7690573169337453860
- social_author_id (from activity_info in share query): 7387370409764897816
- mid (audio?): 7690573202287840026
- content_type: **video** (not 图文 note)
- attempted_at: 2026-09-29 Asia/Shanghai (CST / UTC+8)

## Attempts

1. WebFetch short link → fail / empty provider error
2. curl -sL mobile UA short link → HTTP 302 → iesdouyin share/video/7690573169337453860/ → HTTP 200 HTML ~35KB
3. Parse `window._ROUTER_DATA` → `loaderData.video_layout = null`; page is SSR shell only
4. Meta title: 「在抖音记录美好生活20260929 - 抖音」; meta description: 「于20260929发布在抖音，已经收获了0个喜欢…」— **no caption / no prompt / no on-screen transcript**
5. iesdouyin web/api/v2/aweme/iteminfo → empty body (0 bytes)
6. iesdouyin web/api/v2/aweme/detail → `{"status_code":1,"status_msg":"Url doesn't match"}`
7. douyin.com/aweme/v1/web/aweme/detail → empty
8. m.douyin.com/share/video/{id} → same empty share shell (~32KB)
9. Playwright Chromium → browser binary missing (`chromium_headless_shell` not installed)
10. google-chrome --headless screenshot/dump-dom → hung / no usable capture before kill; no body recovered
11. WebSearch 「AI绘梦菌 AI提示词编写思路」 / aweme id → **no public mirror / transcript / Xiaohongshu-Bilibili repost with verbatim body**. Only tangential @mentions of the creator on unrelated Douyin videos.

## Recovered verbatim post body

**NONE** (0 characters of spoken script, caption, or on-screen slide text from the target post).

Recoverable non-body metadata only: video_id, author_id hint, share timestamps in query string, empty SSR shell HTML saved beside this file (`page.html`, `router.json`, `headers.txt`).

## Mirror search (methodology, NOT attributed as AI绘梦菌 verbatim)

Because the Douyin body is blocked, methodology skill + `prompts/提示词写法/` were distilled **only** from publicly fetchable guides (cited in those files). **Do not treat those as the Douyin post text.**

## Status

INCOMPLETE / UNRECOVERABLE without Douyin app session, logged-in browser with video playback + OCR of on-screen text, or a third-party mirror that actually carries the caption/slides.
