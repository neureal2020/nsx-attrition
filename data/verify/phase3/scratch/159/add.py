import json,sys,os
out='batch_159_out.json'
inp={p['key']:p for p in json.load(open('batch_159_in.json'))}
cur=json.load(open(out)) if os.path.exists(out) else []
have={c['key'] for c in cur}
for r in json.load(sys.stdin):
    p=inp[r['key']]
    base={"name":p['name'],"program_id":p['program_id'],"residency_stated":[],"year_left":None,"destination_program":None,"destination_start_year":None,"agrees_with_db":True,"disagreement":"","abns_certified":False,"searches_used":2}
    base.update(r)
    base.setdefault("checks",{})["usnews"]="deferred"
    cur=[c for c in cur if c['key']!=r['key']]+[base]
order=[p['key'] for p in json.load(open('batch_159_in.json'))]
cur.sort(key=lambda c:order.index(c['key']))
json.dump(cur,open(out,'w'),indent=1)
print(len(cur))
