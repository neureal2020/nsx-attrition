import json,sys,os
OUT='batch_056_out.json'
def add(recs):
    d=json.load(open(OUT)) if os.path.exists(OUT) else []
    keys={r['key'] for r in d}
    for r in recs:
        if r['key'] in keys: d=[x for x in d if x['key']!=r['key']]
        d.append(r)
    order=[p['key'] for p in json.load(open('batch_056_in.json'))]
    d.sort(key=lambda r: order.index(r['key']))
    json.dump(d,open(OUT,'w'),indent=1)
    print(len(d))
