#!/usr/bin/env python3
"""Build agent-index.jsonl from the canonical source index.

This layer is deliberately derived: index.jsonl remains the evidence/source index;
agent-index.jsonl adds normalized retrieval hints without rewriting source records.
Only Python stdlib is required.
"""
import json, os, re, sys

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC=os.path.join(ROOT,"index.jsonl")
OUT=os.path.join(ROOT,"agent-index.jsonl")

TASK_MAP={
 "打斗运镜":["fight","action","camera"], "运镜":["camera"], "特效":["vfx"],
 "国风古装":["wuxia","style"], "电影大场面":["cinematic","large-scene"],
 "动画电影感":["animation","cinematic"], "产品生活":["product"], "UGC短视频":["ugc"],
 "人物卡":["character-asset"], "生图修画质":["image-repair"], "首尾帧生图":["image-to-video","keyframe"],
 "提示词写法":["prompt-method"], "技巧锦囊":["method"], "短剧":["narrative"],
 "真人漫剧":["narrative"], "游戏PV":["game-pv"], "变形转换":["transformation"],
 "光影打光":["lighting"], "恐怖":["horror"], "超现实喜剧":["surreal","comedy"]
}
CAP_RULES=[
 ("发力|受力|打击|碰撞",["force-chain","contact-reaction"]),
 ("高速|极速|瞬冲|追击|连击|连续格挡",["hyper-speed-exchange"]),
 ("地形|竹林|屋顶|走廊|悬崖|河滩",["terrain-route"]),
 ("粒子|火星|冲击波|特效|刀气|水墨",["vfx-anchoring"]),
 ("运镜|跟拍|环绕|推镜|拉焦|FPV|POV",["camera-control"]),
 ("转场|匹配剪辑|遮挡",["transition"]),
 ("首帧|尾帧|关键帧",["frame-control"]),
 ("角色|人物|一致性|双胞胎",["identity-lock"]),
 ("产品|商品|广告",["hero-product"]),
 ("Vlog|UGC|自拍|手机",["ugc-naturalism"])
]

def authority(r):
    s=" ".join(str(r.get(k,"")) for k in ("核对状态","原文类型","来源链接","作者","备注")).lower()
    if "official" in s or "官方" in s: return "official"
    if r.get("核对状态") in ("verified","verified-with-fix"): return "verified-original"
    if r.get("来源链接"): return "curated-community"
    return "unknown"

def completeness(r):
    if r["条目类型"]=="case": return "case"
    if r["条目类型"]=="reference": return "component"
    return "complete"

def role(r):
    if r["条目类型"]=="case": return "compare"
    if r["条目类型"]=="reference": return "evidence"
    return "generate"

def split_models(v):
    if isinstance(v,list): return [str(x).strip() for x in v if str(x).strip()]
    return [x.strip() for x in re.split(r"[,，/、;；|]+",str(v)) if x.strip()]

def enrich(r):
    text=" ".join([str(r.get("标题","")),str(r.get("所在标题","")),str(r.get("技巧钩子","")),str(r.get("触发场景",""))," ".join(r.get("标签") or [])])
    caps=[]
    for pat,names in CAP_RULES:
        if re.search(pat,text,re.I):
            caps.extend(names)
    out={
      "id":r["id"],"title":r.get("标题",""),"path":r.get("文件",""),
      "entry_type":r["条目类型"],"task":TASK_MAP.get(r.get("分类",""),[r.get("分类","")]),
      "models":split_models(r.get("适用模型","")),"capabilities":sorted(set(caps)),
      "authority":authority(r),"completeness":completeness(r),"retrieval_role":role(r),
      "verification":r.get("核对状态",""),"source_url":r.get("来源链接",""),
      "tags":r.get("标签") or [],"trigger":r.get("触发场景",""),"hook":r.get("技巧钩子","")
    }
    return out

def build():
    rows=[]
    with open(SRC,encoding="utf-8") as f:
        for n,line in enumerate(f,1):
            if not line.strip(): continue
            try: rows.append(enrich(json.loads(line)))
            except Exception as e: raise SystemExit(f"index.jsonl line {n}: {e}")
    return "".join(json.dumps(x,ensure_ascii=False,sort_keys=True)+"\n" for x in rows)

def main():
    generated=build()
    check="--check" in sys.argv
    current=open(OUT,encoding="utf-8").read() if os.path.exists(OUT) else None
    if check:
        if current!=generated:
            print("不同步: agent-index.jsonl")
            return 1
        print("agent-index.jsonl OK")
        return 0
    with open(OUT,"w",encoding="utf-8") as f:f.write(generated)
    print("wrote agent-index.jsonl")
    return 0

if __name__=="__main__": raise SystemExit(main())
