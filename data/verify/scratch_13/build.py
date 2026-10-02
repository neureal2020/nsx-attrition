import json,sys
inp=json.load(open('../batch_13_in.json'))
rows={}
extras=[]
for l in open('rows.jsonl'):
    l=l.strip()
    if not l: continue
    r=json.loads(l)
    if r.get('_extra'): r.pop('_extra'); extras.append(r)
    else: rows[r['name']]=r
out=[]
for i in inp:
    if i['name'] in rows: out.append(rows[i['name']])
json.dump(out+extras,open('../batch_13_out.json','w'),indent=1)
print(len(out),'rows',len(extras),'extras')
