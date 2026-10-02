import json,sys,os
base="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/"
out=base+"ident/i_17_out.json"
ps=json.load(open(base+"program_sources.json"))
inp=json.load(open(base+"ident/i_17_in.json"))
order=[p['key'] for p in inp]
rec=json.load(open(sys.argv[1]))
k=rec['key']
if 'program_site_url' not in rec:
    srcs=[s for s in ps.get(k,[]) if s['url'].startswith('http')]
    rec['program_site_url']=srcs[-1]['url'] if srcs else None
rec.setdefault('checks',{}).setdefault('usnews','deferred')
rec['searches_used']=rec.get('ident_searches')
cur=json.load(open(out)) if os.path.exists(out) else []
cur=[r for r in cur if r['key']!=k]+[rec]
cur.sort(key=lambda r: order.index(r['key']))
json.dump(cur,open(out,'w'),indent=1)
print(len(cur),"records")
