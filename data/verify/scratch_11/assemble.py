import json,glob,os
d="/Users/neureal/Documents/Residency Application Study/data/verify/"
inp=json.load(open(d+"batch_11_in.json"))
out=[]
for i,r in enumerate(inp,1):
    p=d+f"scratch_11/r{i}.json"
    if os.path.exists(p): out.append(json.load(open(p)))
json.dump(out,open(d+"batch_11_out.json","w"),indent=1,ensure_ascii=False)
print(len(out),"rows")
