import json,sys,os
f='batch_154_out.json'
d=json.load(open(f)) if os.path.exists(f) else []
new=json.load(sys.stdin)
keys={x['key'] for x in d}
for n in new:
    d=[x for x in d if x['key']!=n['key']]+[n]
order={p['key']:i for i,p in enumerate(json.load(open('batch_154_in.json')))}
d.sort(key=lambda x:order[x['key']])
json.dump(d,open(f,'w'),indent=1)
print(len(d))
