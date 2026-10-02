import json,sys,os
out='/Users/neureal/Documents/Residency Application Study/data/verify/programs/x_recon_2_out.json'
rows=json.load(open(out)) if os.path.exists(out) else []
new=json.load(open(sys.argv[1]))
rows=[r for r in rows if r['program_id']!=new['program_id']]+[new]
json.dump(rows,open(out,'w'),indent=1)
print(len(rows))
