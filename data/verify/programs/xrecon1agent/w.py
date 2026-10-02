import json,sys,os
p='/Users/neureal/Documents/Residency Application Study/data/verify/programs/x_recon_1_out.json'
out=json.load(open(p)) if os.path.exists(p) else []
row=json.loads(sys.stdin.read())
out=[r for r in out if r['program_id']!=row['program_id']]+[row]
json.dump(out,open(p,'w'),indent=1);print(len(out))
