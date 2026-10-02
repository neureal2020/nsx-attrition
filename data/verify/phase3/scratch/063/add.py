import json,sys,os
OUT="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/batch_063_out.json"
def add(e):
    d=json.load(open(OUT)) if os.path.exists(OUT) else []
    d=[x for x in d if x['key']!=e['key']]
    d.append(e)
    json.dump(d,open(OUT,'w'),indent=1)
