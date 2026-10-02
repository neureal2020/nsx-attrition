import json,sys,os
P="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/batch_090_out.json"
def add(entries):
    d=json.load(open(P)) if os.path.exists(P) else []
    have={e['key'] for e in d}
    for e in entries:
        if e['key'] not in have: d.append(e)
    json.dump(d,open(P,'w'),indent=1)
    print(len(d))
