#!/usr/bin/env python3
"""Validate agent-native repository architecture. Stdlib only."""
import json, os, re, sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors=[]
required=["AGENTS.md","KNOWLEDGE-MAP.md","agent-manifest.json","TEMPLATES.md","CAPABILITIES.md","COMPILER.md","PLAYBOOK.md","CORE-PICKS.md","index.jsonl","agent-index.jsonl"]
for p in required:
    if not os.path.exists(os.path.join(ROOT,p)): errors.append("missing "+p)
try:
    m=json.load(open(os.path.join(ROOT,"agent-manifest.json"),encoding="utf-8"))
    for p in [m["agent_entrypoint"],m["retrieval_map"],m["compiler"],*m["canonical_layers"].values(),*m["evidence_layers"].values()]:
        if p.endswith("/") or p=="agent-index.jsonl": continue
        if not os.path.exists(os.path.join(ROOT,p)): errors.append("manifest target missing "+p)
except Exception as e: errors.append("manifest invalid: "+str(e))
for path,_,files in os.walk(os.path.join(ROOT,"skills")):
    for fn in files:
        if fn!="SKILL.md": continue
        p=os.path.join(path,fn); s=open(p,encoding="utf-8").read()
        if "AGENTS.md" not in s: errors.append("skill does not route through AGENTS.md: "+os.path.relpath(p,ROOT))
        if len(s.splitlines())>90: errors.append("skill too large; likely duplicated knowledge: "+os.path.relpath(p,ROOT))
        if re.search(r"高强度武戏.*1.?2 个",s): errors.append("stale universal 1-2 move fight rule: "+os.path.relpath(p,ROOT))
seen=set()
for fn in ("index.jsonl","agent-index.jsonl"):
    p=os.path.join(ROOT,fn)
    if not os.path.exists(p): continue
    for n,line in enumerate(open(p,encoding="utf-8"),1):
        try:r=json.loads(line)
        except Exception as e: errors.append(f"{fn}:{n} invalid json: {e}"); continue
        if fn=="agent-index.jsonl":
            for k in ("id","title","path","entry_type","task","models","capabilities","authority","completeness","retrieval_role"):
                if k not in r: errors.append(f"{fn}:{n} missing {k}")
            if r.get("id") in seen: errors.append("duplicate agent id "+str(r.get("id")))
            seen.add(r.get("id"))
if errors:
    print("\n".join("ERROR: "+x for x in errors)); sys.exit(1)
print("agent architecture OK")
