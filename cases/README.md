# Cases · 对照样例

每个样例一个子目录，尽量成套齐全，便于对比效果：

```
cases/<category>/<slug>/
  prompt/          # 原提示词（verbatim）
  character-card/  # 角色卡 / 定妆 / 参考图
  video/           # 成片或关键片段（mp4/webm；大文件用 Git LFS 或外链清单）
  notes/           # 来源、模型、参数、对比说明
  RESULT.md        # 一眼对照：提示词要点 ↔ 画面效果
```

原则：
- 有提示词没成片也可以先建壳，但 README 里标 `status: prompt-only`
- 有成片务必写清对应提示词版本（hash 或文件名）
- 第三方素材只归档公开分享内容，并在 notes 写来源 URL

## 中文分类目录

与 `prompts/` 对齐：`打斗运镜`、`特效`、`运镜`、`国风古装`（原 `国漫3D`，2026-09-30 更名）、`电影大场面`（原 `其他` 下的样例已移入）、`人物卡`、`生图修画质`。原 `vfx-spectacle` 已并入 `特效`。
