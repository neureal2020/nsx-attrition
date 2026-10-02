import json,os
d=os.path.dirname(os.path.abspath(__file__))
inp=json.load(open(os.path.join(d,'..','batch_12_in.json')))
out=[]
for i,r in enumerate(inp):
    p=os.path.join(d,f'row_{i:02d}.json')
    if os.path.exists(p): out.append(json.load(open(p)))
json.dump(out,open(os.path.join(d,'..','batch_12_out.json'),'w'),indent=1,ensure_ascii=False)
print(len(out),'rows written')
