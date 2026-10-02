# usage: python3 add.py rec.json  -> merges record into i_18_out.json in input order
import json,sys,os
base="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/ident/"
inp=json.load(open(base+"i_18_in.json")); order=[p['key'] for p in inp]
out=base+"i_18_out.json"
cur=json.load(open(out)) if os.path.exists(out) else []
d={r['key']:r for r in cur}
for r in json.load(open(sys.argv[1])) if isinstance(json.load(open(sys.argv[1])),list) else [json.load(open(sys.argv[1]))]:
    r.setdefault('searches_used',r.get('ident_searches',0)); d[r['key']]=r
json.dump([d[k] for k in order if k in d],open(out,'w'),indent=1)
print(len(d),'records')
