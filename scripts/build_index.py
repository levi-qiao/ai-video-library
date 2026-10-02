#!/usr/bin/env python3
"""从 prompts/ 与 cases/ 的 Markdown 重新生成 INDEX.md、index.jsonl 与 prompts/README.md 的统计块。

用法（在仓库根目录）：
    python3 scripts/build_index.py          # 重新生成并写入
    python3 scripts/build_index.py --check  # 只检查，已提交的文件与生成结果不一致时返回 1

只用 Python 标准库。解析规则见 docs/条目格式规范.md：
每个计数条目 = 一个 ```yaml 元数据块（首行注释「# 条目元数据…」，每行 `键: JSON 值`）+ 紧随其后的 ```text 围栏。
"""
import json, os, re, sys, glob, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KEYS = ['id', '标题', '原标题', '分类', '标签', '适用模型', '语言', '来源链接', '镜像', '作者', '发布日期', '热度',
        '许可', '原文类型', '核对状态', '核对说明', '完整性', '备注', '技巧钩子', '触发场景']
JIQIAO = '技巧锦囊'

# 词典/官方微型示例属于知识参考层，不与完整可生成 Prompt 一起计数。
# 原文仍保留、仍进入 index.jsonl，只把条目类型标为 reference。
REFERENCE_PROMPT_FILES = {
    'prompts/运镜/41-x-adrianpunk115-camera-dictionary-part2.md',
    'prompts/运镜/42-x-adrianpunk115-camera-dictionary-part1.md',
    'prompts/运镜/45-runway-official-camera-terms-examples.md',
    'prompts/首尾帧生图/01-openai-gpt-image-official.md',
    'prompts/首尾帧生图/02-google-gemini-veo-official.md',
    'prompts/首尾帧生图/03-volcengine-seedream-seedance-official.md',
    'prompts/首尾帧生图/04-bfl-flux-official.md',
    'prompts/首尾帧生图/05-runway-official.md',
    'prompts/首尾帧生图/06-aliyun-wan-official.md',
    'prompts/提示词写法/01-web-prompt-writing-methodology.md',
    'prompts/提示词写法/32-runway-seedance-2.0-prompt-guide.md',
    'prompts/提示词写法/33-official-vendor-video-examples.md',
    # 语义体检第二阶段：动作词典 / 组件块 / 社区方法摘录不占核心 Prompt 名额。
    'prompts/打斗运镜/02-web-fight-camera-prompts.md',
    'prompts/打斗运镜/20-web-fight-camera-prompts.md',
    'prompts/打斗运镜/32-douyin-kongming-weapon-fight.md',
    'prompts/人物卡/04-web-character-card-prompts.md',
    'prompts/生图修画质/03-web-image2-denoise-prompts.md',
    'prompts/特效/40-douyin-aigc-xiaoyueer-skill-vfx.md',
    'prompts/技巧锦囊/45-seedance-agent-skill-synthesis.md',
    'prompts/技巧锦囊/46-hell-grind-cinedance-acting-lira-synthesis.md',
}
CAT_ORDER = ['技巧锦囊', '打斗运镜', '运镜', '特效', '光影打光', '国风古装', '电影大场面', '动画电影感', '真人漫剧', '短剧', '超现实喜剧', '恐怖',
             '变形转换', '产品生活', 'UGC短视频', '游戏PV', '首尾帧生图', '人物卡', '生图修画质', '提示词写法']
CAT_DESC = {
    '技巧锦囊': '想不到要问、但能给人新思路的技巧（力场融合特效、一镜到底打斗、混合风格等），供主动浏览；可交叉收录其他分类的条目',
    '打斗运镜': '打斗、武戏、动作编排与配套运镜（含发力链、打击感方法）',
    '运镜': '以摄影机运动、镜头调度为主要看点的完整提示词；术语词典在 reference 层',
    '特效': '技能特效、魔法、能量、粒子、破坏等视觉特效',
    '光影打光': '以打光为主要看点的提示词：光源时段、方位角度、软硬、色温与光型（逆光、伦勃朗光、丁达尔光柱等）',
    '国风古装': '国风、古装、武侠、仙侠题材（含 3D 国漫质感）',
    '电影大场面': '电影感大场面、史诗、灾难、怪物、战争等',
    '动画电影感': '动画 / 动漫 / 手绘 / 3D 动画电影风格',
    '真人漫剧': '真人漫剧（真人演绎的漫画式短剧）',
    '短剧': '剧情短剧、偶像剧、情景剧',
    '超现实喜剧': '超现实、荒诞、搞笑',
    '恐怖': '恐怖、惊悚、悬疑',
    '变形转换': '变身、换装、形态转换、无缝转场',
    '产品生活': '产品广告、商业片、生活方式',
    'UGC短视频': 'UGC、自拍 Vlog、手机拍摄感短视频',
    '游戏PV': '游戏宣传片、格斗游戏序列',
    '首尾帧生图': '完整创作 Prompt；官方微型示例已移到 reference 层',
    '人物卡': '人物设定图、三视图、表情包等角色资产图（生图）',
    '生图修画质': '图片降噪、画质修复、干净出图（生图）',
    '提示词写法': '完整可执行模板；方法片段与官方短例在 reference 层',
}
FENCE_OPEN = re.compile(r'^```([^`\s]*)\s*$')
FENCE_CLOSE = re.compile(r'^```\s*$')
COUNT_START = '<!-- 统计:开始（由 scripts/build_index.py 生成，请勿手改） -->'
COUNT_END = '<!-- 统计:结束 -->'


def blocks(text):
    """把 Markdown 切成 ('line', 行) 与 ('fence', 语言, 正文) 两类块（围栏感知）。"""
    out, lines, i = [], text.split('\n'), 0
    while i < len(lines):
        m = FENCE_OPEN.match(lines[i])
        if m:
            j = i + 1
            while j < len(lines) and not FENCE_CLOSE.match(lines[j]):
                j += 1
            out.append(('fence', m.group(1), '\n'.join(lines[i + 1:j])))
            i = j + 1
            continue
        out.append(('line', lines[i]))
        i += 1
    return out


def gh_anchor(heading, seen):
    """近似 GitHub 的标题锚点算法：小写、去标点、空格变连字符，重名加 -1、-2。"""
    h = re.sub(r'^#+\s*', '', heading).strip().lower()
    h = re.sub(r'[^\w\- ]', '', h, flags=re.UNICODE).replace(' ', '-')
    n = seen.get(h, 0)
    seen[h] = n + 1
    return h if n == 0 else f'{h}-{n}'


def parse_meta(body):
    meta = {}
    for ln in body.split('\n'):
        if not ln.strip() or ln.startswith('#'):
            continue
        k, _, v = ln.partition(': ')
        meta[k.strip()] = json.loads(v)
    if list(meta) != KEYS:
        raise SystemExit(f'元数据字段缺失或顺序不对（应为 {len(KEYS)} 个字段，顺序见 docs/条目格式规范.md）：{meta.get("id", "?")}')
    if JIQIAO in (meta.get('标签') or []) and not (meta.get('技巧钩子') and meta.get('触发场景')):
        raise SystemExit(f'标签含「{JIQIAO}」的条目必须填写「技巧钩子」和「触发场景」：{meta.get("id", "?")}')
    return meta


def parse_prompt_file(path):
    rel = os.path.relpath(path, ROOT).replace(os.sep, '/')
    bl = blocks(open(path, encoding='utf-8').read())
    seen, anchor, heading, out, pending = {}, '', '', [], None
    for b in bl:
        if b[0] == 'line':
            if re.match(r'^#{1,6} ', b[1]):
                heading = re.sub(r'^#+\s*', '', b[1]).strip()
                anchor = gh_anchor(b[1], seen)
            elif b[1].strip():
                pending = None if pending is None else pending
            continue
        if b[1] == 'yaml' and b[2].startswith('# 条目元数据'):
            pending = parse_meta(b[2])
            continue
        if b[1] == 'text':
            if pending is None:
                raise SystemExit(f'{rel}: text 围栏前缺少元数据块（标题：{heading}）')
            rec = {k: pending.get(k, '') for k in KEYS}
            rec.update({'条目类型': 'prompt', '文件': rel, '锚点': anchor, '所在标题': heading, '原文': b[2]})
            out.append(rec)
            pending = None
    return out


def parse_case(dirpath):
    rel = os.path.relpath(dirpath, ROOT).replace(os.sep, '/')
    cat = rel.split('/')[1]
    text = open(os.path.join(dirpath, 'prompt', 'prompt.txt'), encoding='utf-8').read()
    src = ''
    notes = sorted(glob.glob(os.path.join(dirpath, 'notes', '*.md')))
    info = {}
    if notes:
        for ln in open(notes[0], encoding='utf-8').read().split('\n'):
            m = re.match(r'^- \*\*(.+?):\*\*\s*(.*)$', ln)
            if m:
                info[m.group(1)] = m.group(2).strip()
    for k in ('Original source URL', 'Prompt self-reply', 'Source URL (parent clip)', 'Source URL'):
        if info.get(k):
            src = re.findall(r'https?://\S+', info[k])[0] if re.findall(r'https?://\S+', info[k]) else info[k]
            break
    rec = {k: ([] if k == '标签' else '') for k in KEYS}
    rec.update({'id': 'case--' + os.path.basename(dirpath), '标题': info.get('Title (EN)', os.path.basename(dirpath)),
            '分类': cat, '来源链接': src, '作者': info.get('Author', ''), '适用模型': info.get('Model', ''),
            '条目类型': 'case', '文件': rel + '/prompt/prompt.txt', '锚点': '', '所在标题': '', '原文': text.rstrip('\n'),
            '备注': '对照样例（含成片与说明），见 ' + rel + '/'})
    return rec


def parse_reference(path):
    """不含计数提示词的方法 / 讲解文件（如抖音教程视频的字幕与文案），在索引里单独列出。"""
    rel = os.path.relpath(path, ROOT).replace(os.sep, '/')
    text = open(path, encoding='utf-8').read()
    title = re.sub(r'^#\s*', '', text.split('\n', 1)[0]).strip()
    meta = {}
    for b in blocks(text):
        if b[0] == 'fence' and b[1] == 'yaml' and b[2].startswith('# 文件元数据'):
            meta = parse_meta(b[2])
            break
    if not meta:
        raise SystemExit(f'{rel}: 不含计数提示词的文件缺少「文件元数据」块')
    rec = {k: meta.get(k, '') for k in KEYS}
    rec.update({'条目类型': 'reference', '文件': rel, '锚点': '', '所在标题': title, '原文': ''})
    return rec


def collect():
    recs, refs = [], []
    for p in sorted(glob.glob(os.path.join(ROOT, 'prompts', '*', '*.md'))):
        if os.path.basename(p) == 'README.md':
            continue
        got = parse_prompt_file(p)
        rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        if rel in REFERENCE_PROMPT_FILES:
            for r in got:
                r['条目类型'] = 'reference'
            refs += got
        else:
            recs += got
        if not got:
            refs.append(parse_reference(p))
    cases = [parse_case(d) for d in sorted(glob.glob(os.path.join(ROOT, 'cases', '*', '*')))
             if os.path.isfile(os.path.join(d, 'prompt', 'prompt.txt'))]
    return recs, cases + refs


def cat_key(c):
    return (CAT_ORDER.index(c) if c in CAT_ORDER else len(CAT_ORDER), c)


def build_jsonl(recs, cases):
    return ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in recs + cases)


def count_table(recs, cases):
    c = collections.Counter(r['分类'] for r in recs)
    cc = collections.Counter(r['分类'] for r in cases if r['条目类型'] == 'case')
    st = collections.Counter(r['核对状态'] for r in recs)
    rows = ['| 分类 | 说明 | 核心 Prompt | 对照样例（cases/） |', '|------|------|-----------:|-------------------:|']
    dirs = {os.path.basename(d) for d in glob.glob(os.path.join(ROOT, 'prompts', '*')) if os.path.isdir(d)}
    xl = sum(1 for r in recs + cases if JIQIAO in (r.get('标签') or []) and r['分类'] != JIQIAO)
    for k in sorted(dirs | set(c) | set(cc), key=cat_key):
        extra = f'（另有交叉收录 {xl} 条）' if k == JIQIAO else ''
        rows.append(f'| [{k}](prompts/{k}/) | {CAT_DESC.get(k, "")} | {c.get(k, 0)}{extra} | {cc.get(k, 0)} |')
    rows.append(f'| **合计** | | **{sum(c.values())}** | **{sum(cc.values())}** |')
    rows.append('')
    rows.append('核心 Prompt 核对状态：' + '、'.join(f'{k} {v}' for k, v in sorted(st.items(), key=lambda x: -x[1])) + f'；reference {sum(1 for r in cases if r["条目类型"] == "reference")} 条（术语词典 / 官方微型示例 / 方法片段，不计入核心 Prompt）。')
    return '\n'.join(rows)


def build_index_md(recs, cases):
    L = ['# 提示词索引（INDEX）', '',
         '> 本文件由 `scripts/build_index.py` 自动生成。核心索引只统计可直接生成/改写的完整 Prompt；术语词典、官方微型示例和方法片段保留在 reference 层。AI 检索请用 `index.jsonl`。',
         '> 每行格式：标题（链接到条目）— 适用模型 · 语言 · 核对状态 · 标签。', '',
         ]
    jq = [r for r in recs + cases if r['分类'] == JIQIAO or JIQIAO in (r.get('标签') or [])]
    L += [f'## {JIQIAO}（{len(jq)}）', '', '> ' + CAT_DESC[JIQIAO] + '。每行：标题 — 技巧钩子（触发场景）· 主分类。', '']
    if not jq:
        L.append('（暂无条目）')
    for r in jq:
        link = r['文件'] + (f"#{r['锚点']}" if r['锚点'] else '')
        L.append(f"- [{r['标题']}]({link}) — {r.get('技巧钩子') or '（待补技巧钩子）'}（{r.get('触发场景') or '触发场景待补'}）· 主分类：{r['分类']}")
    L.append('')
    L += ['## 统计', '', count_table(recs, cases), '']
    by = collections.defaultdict(list)
    for r in recs:
        by[r['分类']].append(r)
    for cat in sorted(by, key=cat_key):
        L += [f'## {cat}（{len(by[cat])}）', '', CAT_DESC.get(cat, ''), '']
        cur = None
        for r in by[cat]:
            if r['文件'] != cur:
                cur = r['文件']
                if L[-1] != '':
                    L.append('')
                L += [f'### `{cur}`', '']
            tags = '、'.join(r['标签']) if r['标签'] else '—'
            L.append(f"- [{r['标题']}]({cur}#{r['锚点']}) — {r['适用模型']} · {r['语言']} · {r['核对状态']} · {tags}　`{r['id']}`")
        L.append('')
    L += ['## 对照样例（cases/）', '', '每个样例目录含 `prompt/prompt.txt`（原文）、成片说明与来源记录；提示词正文与 `prompts/` 不重复。', '']
    for r in cases:
        if r['条目类型'] == 'case':
            L.append(f"- [{r['标题']}]({os.path.dirname(os.path.dirname(r['文件']))}/) — {r['分类']} · 来源 {r['来源链接'] or '见样例目录'}")
    L += ['', '## 方法与讲解文件（不含计数提示词）', '', '这里包括教程文案、术语词典和官方微型示例：适合查方法/语法，但不与完整可生成 Prompt 一起计数。', '']
    for r in cases:
        if r['条目类型'] == 'reference':
            L.append(f"- [{r['标题']}]({r['文件']}) — {r['分类']} · 来源 {r['来源链接'] or '见文件'}")
    return '\n'.join(L).rstrip('\n') + '\n'


def build_prompts_readme(old, recs, cases):
    table = COUNT_START + '\n\n' + count_table(recs, cases).replace('](prompts/', '](') + '\n\n' + COUNT_END
    if COUNT_START in old and COUNT_END in old:
        a = old.index(COUNT_START)
        b = old.index(COUNT_END) + len(COUNT_END)
        return old[:a] + table + old[b:]
    raise SystemExit('prompts/README.md 缺少统计块标记')


def main():
    check = '--check' in sys.argv
    recs, cases = collect()
    ids = [r['id'] for r in recs]
    dup = [i for i, n in collections.Counter(ids).items() if n > 1]
    if dup:
        raise SystemExit('重复 id：' + ', '.join(dup))
    rp = os.path.join(ROOT, 'prompts', 'README.md')
    outs = {os.path.join(ROOT, 'index.jsonl'): build_jsonl(recs, cases),
            os.path.join(ROOT, 'INDEX.md'): build_index_md(recs, cases),
            rp: build_prompts_readme(open(rp, encoding='utf-8').read(), recs, cases)}
    bad = 0
    for p, s in outs.items():
        cur = open(p, encoding='utf-8').read() if os.path.exists(p) else None
        if cur != s:
            bad += 1
            if check:
                print('不同步：', os.path.relpath(p, ROOT))
            else:
                open(p, 'w', encoding='utf-8').write(s)
    print(f'提示词条目 {len(recs)}，样例与讲解文件 {len(cases)}；' + ('检查' if check else '写入') + f'：{bad} 个文件' + ('不同步' if check else '有更新'))
    return 1 if (check and bad) else 0


if __name__ == '__main__':
    sys.exit(main())
