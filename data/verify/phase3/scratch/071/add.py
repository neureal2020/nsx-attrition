import json,sys,os
OUT="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/batch_071_out.json"
INP=json.load(open("/Users/neureal/Documents/Residency Application Study/data/verify/phase3/batch_071_in.json"))
byk={p['key']:p for p in INP}
def add(key,**kw):
    out=json.load(open(OUT)) if os.path.exists(OUT) else []
    out=[o for o in out if o['key']!=key]
    p=byk[key]
    d={"key":key,"name":p['name'],"program_id":p['program_id']}
    d.update(kw)
    d["checks"]=kw.get("checks")
    out.append(d)
    order={p['key']:i for i,p in enumerate(INP)}
    out.sort(key=lambda o:order[o['key']])
    json.dump(out,open(OUT,"w"),indent=1)
