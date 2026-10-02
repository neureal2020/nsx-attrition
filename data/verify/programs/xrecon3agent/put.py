import json,sys,os
out='/Users/neureal/Documents/Residency Application Study/data/verify/programs/x_recon_3_out.json'
row=json.loads(sys.stdin.read())
d=json.load(open(out)) if os.path.exists(out) else []
d=[r for r in d if r['program_id']!=row['program_id']]+[row]
json.dump(d,open(out,'w'),indent=1)
print(len(d))
