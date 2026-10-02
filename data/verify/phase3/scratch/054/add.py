import json,sys,os
out='batch_054_out.json'
inp={p['key']:p for p in json.load(open('batch_054_in.json'))}
def add(e):
    d=json.load(open(out)) if os.path.exists(out) else []
    d=[x for x in d if x['key']!=e['key']]
    p=inp[e['key']]
    e.setdefault('name',p['name']); e.setdefault('program_id',p['program_id'])
    e.setdefault('checks',{}); e['checks']['usnews']='deferred'
    order=[k for k in inp]
    d.append(e); d.sort(key=lambda x:order.index(x['key']))
    json.dump(d,open(out,'w'),indent=1)
