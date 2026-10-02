import json,os
base='/Users/neureal/Documents/Residency Application Study/data/verify/phase3/'
inp=json.load(open(base+'gold/g_017_in.json'))
res=json.load(open(base+'scratch/g017/res.json'))
out=[]
for p in inp:
    r=res.get(p['key'])
    if not r: continue
    o={"key":p['key'],"name":p['name'],"program_id":p['program_id'],"outcome":p['outcome']}
    o.update(r); out.append(o)
json.dump(out,open(base+'gold/g_017_out.json','w'),indent=1)
print(len(out))
