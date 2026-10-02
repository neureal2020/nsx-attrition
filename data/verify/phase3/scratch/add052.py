import json,sys,os
inp=json.load(open('batch_052_in.json'))
byk={p['key']:p for p in inp}
out_f='batch_052_out.json'
def add(key,**kw):
    out=json.load(open(out_f)) if os.path.exists(out_f) else []
    out=[o for o in out if o['key']!=key]
    p=byk[key]
    d={"key":key,"name":p['name'],"program_id":p['program_id']}
    d.update(kw)
    d.setdefault("checks",{})["usnews"]="deferred"
    out.append(d)
    order={p['key']:i for i,p in enumerate(inp)}
    out.sort(key=lambda o:order[o['key']])
    json.dump(out,open(out_f,'w'),indent=1)
