import json,sys,os
OUT="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/ident/i_20_out.json"
IN="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/ident/i_20_in.json"
rec=json.load(open(sys.argv[1]))
order=[p['key'] for p in json.load(open(IN))]
cur=json.load(open(OUT)) if os.path.exists(OUT) else []
cur=[r for r in cur if r['key']!=rec['key']]+[rec]
cur.sort(key=lambda r: order.index(r['key']))
json.dump(cur,open(OUT,'w'),indent=1,ensure_ascii=False)
print(len(cur),"records")
