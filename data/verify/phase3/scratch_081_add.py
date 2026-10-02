import json,sys,os
OUT="batch_081_out.json"
def add(recs):
    d=json.load(open(OUT)) if os.path.exists(OUT) else []
    have={r['key'] for r in d}
    for r in recs:
        if r['key'] not in have: d.append(r)
    json.dump(d,open(OUT,'w'),indent=1)
    print(len(d))
