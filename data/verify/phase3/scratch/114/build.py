import json,os
base="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/"
inp=json.load(open(base+"batch_114_in.json"))
R=json.load(open(base+"scratch/114/res.json")) if os.path.exists(base+"scratch/114/res.json") else {}
out=[]
for p in inp:
    r=R.get(p['key'])
    if not r: continue
    o={"key":p['key'],"name":p['name'],"program_id":p['program_id']}
    o.update(r); out.append(o)
json.dump(out,open(base+"batch_114_out.json","w"),indent=1)
print(len(out))
