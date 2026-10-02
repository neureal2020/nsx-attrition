import json
P="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/"
inp=json.load(open(P+"batch_048_in.json"))
R={}
def add(key, **kw): R[key]=kw
MAYO="Mayo Clinic College of Medicine and Science (Rochester)"
def res(s,e): return [{"institution":MAYO,"specialty":"neurosurgery","start":s,"end":e}]
def src(url,t,ev): return {"url":url,"type":t,"evidence":ev}
def person(key, **kw):
    R[key]=kw
exec(open(P+"scratch/048/data.py").read())
out=[]
for p in inp:
    k=p["key"]; d=R.get(k)
    if not d: continue
    o={"key":k,"name":p["name"],"program_id":p["program_id"]}
    o.update(d); out.append(o)
json.dump(out,open(P+"batch_048_out.json","w"),indent=1)
print(len(out))
