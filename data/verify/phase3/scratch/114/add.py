import json,sys,os
f="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/scratch/114/res.json"
R=json.load(open(f)) if os.path.exists(f) else {}
R.update(json.load(sys.stdin))
json.dump(R,open(f,"w"),indent=1)
