import json,sys,os
f='batch_045_out.json'
cur=json.load(open(f)) if os.path.exists(f) else []
inp={p['key']:p for p in json.load(open('batch_045_in.json'))}
for r in json.load(sys.stdin):
    p=inp[r['key']]
    r.setdefault('name',p['name']); r['program_id']=37
    r.setdefault('usnews_note',None); 
    r['checks']['usnews']='deferred'
    r.setdefault('year_left',None); r.setdefault('destination_program',None); r.setdefault('destination_start_year',None)
    cur=[c for c in cur if c['key']!=r['key']]+[r]
order=[p['key'] for p in json.load(open('batch_045_in.json'))]
cur.sort(key=lambda c:order.index(c['key']))
json.dump(cur,open(f,'w'),indent=1)
print(len(cur))
