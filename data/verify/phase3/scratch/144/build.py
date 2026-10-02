import json,os
IN=json.load(open('batch_144_in.json'))
P='batch_144_out.json'
out=json.load(open(P)) if os.path.exists(P) else []
def add(idx,**k):
    p=IN[idx]
    r={"key":p["key"],"name":p["name"],"program_id":p["program_id"]}
    r.update(k)
    r.setdefault("usnews_note",None)
    r["checks"].setdefault("usnews","deferred")
    out[:]=[o for o in out if o["key"]!=p["key"]]+[r]
    order={q["key"]:i for i,q in enumerate(IN)}
    out.sort(key=lambda o:order[o["key"]])
    json.dump(out,open(P,'w'),indent=1)
UVA="https://med.virginia.edu/neurosurgery/resident-training/current-residents/"
ROSTER={"url":UVA,"type":"program_page","evidence":"UVA Neurosurgery Current Residents page (2026-27) lists PGY-%s: %s"}
