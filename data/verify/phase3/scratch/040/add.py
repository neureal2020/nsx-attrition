import json,sys,os
inp=json.load(open('batch_040_in.json'))
byk={p['key']:p for p in inp}
outf='batch_040_out.json'
cur=json.load(open(outf)) if os.path.exists(outf) else []
d={e['key']:e for e in cur}
new=json.load(open(sys.argv[1]))
for e in new:
    p=byk[e['key']]
    base={"name":p['name'],"program_id":p['program_id'],"year_left":None,"destination_program":None,"destination_start_year":None,"abns_certified":False,"agrees_with_db":True,"disagreement":"","searches_used":2}
    base.update(e); d[e['key']]=base
out=[d[p['key']] for p in inp if p['key'] in d]
json.dump(out,open(outf,'w'),indent=1)
print(len(out))
