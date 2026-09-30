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
        '许可', '原文类型', '核对状态', '核对说明', '完整性', '备注']
CAT_ORDER = ['打斗运镜', '运镜', '特效', '国风古装', '电影大场面', '动画电影感', '真人漫剧', '短剧', '超现实喜剧', '恐怖',
             '变形转换', '产品生活', 'UGC短视频', '游戏PV', '人物卡', '生图修画质', '提示词写法']
CAT_DESC = {
    '打斗运镜': '打斗、武戏、动作编排与配套运镜（含发力链、打击感方法）',
    '运镜': '以摄影机运动、镜头调度为主要看点的提示词与运镜词典、景别方法',
    '特效': '技能特效、魔法、能量、粒子、破坏等视觉特效',
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
    '人物卡': '人物设定图、三视图、表情包等角色资产图（生图）',
    '生图修画质': '图片降噪、画质修复、干净出图（生图）',
    '提示词写法': '提示词写法方法论、公式与官方示例',
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
    return {'id': 'case--' + os.path.basename(dirpath), '标题': info.get('Title (EN)', os.path.basename(dirpath)),
            '分类': cat, '来源链接': src, '作者': info.get('Author', ''), '适用模型': info.get('Model', ''),
            '条目类型': 'case', '文件': rel + '/prompt/prompt.txt', '锚点': '', '原文': text.rstrip('\n'),
            '备注': '对照样例（含成片与说明），见 ' + rel + '/'}


def collect():
    recs = []
    for p in sorted(glob.glob(os.path.join(ROOT, 'prompts', '*', '*.md'))):
        if os.path.basename(p) == 'README.md':
            continue
        recs += parse_prompt_file(p)
    cases = [parse_case(d) for d in sorted(glob.glob(os.path.join(ROOT, 'cases', '*', '*')))
             if os.path.isfile(os.path.join(d, 'prompt', 'prompt.txt'))]
    return recs, cases


def cat_key(c):
    return (CAT_ORDER.index(c) if c in CAT_ORDER else len(CAT_ORDER), c)


def build_jsonl(recs, cases):
    return ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in recs + cases)


def count_table(recs, cases):
    c = collections.Counter(r['分类'] for r in recs)
    cc = collections.Counter(r['分类'] for r in cases)
    st = collections.Counter(r['核对状态'] for r in recs)
    rows = ['| 分类 | 说明 | 提示词条目 | 对照样例（cases/） |', '|------|------|-----------:|-------------------:|']
    for k in sorted(set(c) | set(cc), key=cat_key):
        rows.append(f'| [{k}](prompts/{k}/) | {CAT_DESC.get(k, "")} | {c.get(k, 0)} | {cc.get(k, 0)} |')
    rows.append(f'| **合计** | | **{sum(c.values())}** | **{sum(cc.values())}** |')
    rows.append('')
    rows.append('核对状态：' + '、'.join(f'{k} {v}' for k, v in sorted(st.items(), key=lambda x: -x[1])))
    return '\n'.join(rows)


def build_index_md(recs, cases):
    L = ['# 提示词索引（INDEX）', '',
         '> 本文件由 `scripts/build_index.py` 从 `prompts/` 与 `cases/` 自动生成，请勿手改。AI 检索请用同目录的 `index.jsonl`（每行一条，含完整原文与全部元数据）。',
         '> 每行格式：标题（链接到条目）— 适用模型 · 语言 · 核对状态 · 标签。', '',
         '## 统计', '', count_table(recs, cases), '']
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
        L.append(f"- [{r['标题']}]({os.path.dirname(os.path.dirname(r['文件']))}/) — {r['分类']} · 来源 {r['来源链接'] or '见样例目录'}")
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
    print(f'提示词条目 {len(recs)}，对照样例 {len(cases)}；' + ('检查' if check else '写入') + f'：{bad} 个文件' + ('不同步' if check else '有更新'))
    return 1 if (check and bad) else 0


if __name__ == '__main__':
    sys.exit(main())
