import json,sys,os
out='data/verify/programs/recon_B1_out.json'
d=json.load(open(out)) if os.path.exists(out) else []
row=json.loads(sys.stdin.read())
d=[r for r in d if not (r['program_id']==row['program_id'] and r.get('name')==row.get('name'))]+[row]
json.dump(d,open(out,'w'),indent=1)
print(len(d))
