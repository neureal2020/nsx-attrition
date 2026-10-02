import json,sys,os
F='/Users/neureal/Documents/Residency Application Study/data/verify/phase3/batch_075_out.json'
def add(entries):
    d=json.load(open(F)) if os.path.exists(F) else []
    have={e['key'] for e in d}
    for e in entries:
        if e['key'] not in have: d.append(e)
    json.dump(d,open(F,'w'),indent=1)
def S(u,t,e): return {"url":u,"type":t,"evidence":e}
R="Riverside University Health System"
