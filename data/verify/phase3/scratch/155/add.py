import json,sys,os
OUT='batch_155_out.json'
inp={p['key']:p for p in json.load(open('batch_155_in.json'))}
def add(key,**kw):
    out=json.load(open(OUT)) if os.path.exists(OUT) else []
    out=[o for o in out if o['key']!=key]
    p=inp[key]
    r={"key":key,"name":p['name'],"program_id":p['program_id'],"usnews_note":None}
    r.pop('usnews_note')
    r.update(kw)
    r['checks']['usnews']='deferred'
    out.append(r)
    order=list(inp)
    out.sort(key=lambda o:order.index(o['key']))
    json.dump(out,open(OUT,'w'),indent=1)
