import json,sys,os
out='/Users/neureal/Documents/Residency Application Study/data/verify/phase3/batch_068_out.json'
inp=json.load(open('/Users/neureal/Documents/Residency Application Study/data/verify/phase3/batch_068_in.json'))
cur=json.load(open(out)) if os.path.exists(out) else []
rec=json.loads(sys.stdin.read())
if isinstance(rec,dict): rec=[rec]
for r in rec:
    r.setdefault('program_id',51); r['usnews']=None
    r['checks']['usnews']='deferred'
    cur=[c for c in cur if c['key']!=r['key']]+[r]
order={p['key']:i for i,p in enumerate(inp)}
cur.sort(key=lambda c:order[c['key']])
json.dump(cur,open(out,'w'),indent=1)
print(len(cur))
