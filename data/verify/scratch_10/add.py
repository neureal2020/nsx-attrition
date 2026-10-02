import json,sys,os
p='/Users/neureal/Documents/Residency Application Study/data/verify/batch_10_out.json'
rows=json.load(open(p)) if os.path.exists(p) else []
new=json.load(sys.stdin)
if isinstance(new,dict): new=[new]
names={r['name'] for r in new}
rows=[r for r in rows if r['name'] not in names]+new
order=[r['name'] for r in json.load(open('/Users/neureal/Documents/Residency Application Study/data/verify/batch_10_in.json'))]
rows.sort(key=lambda r: order.index(r['name']))
json.dump(rows,open(p,'w'),indent=1)
print(len(rows))
