import json,glob
d=json.load(open('batch_057_in.json'))
ents={}
for f in glob.glob('scratch/057/e_*.json'):
    for e in json.load(open(f)): ents[e['key']]=e
out=[ents[p['key']] for p in d if p['key'] in ents]
json.dump(out,open('batch_057_out.json','w'),indent=1)
print(len(out))
