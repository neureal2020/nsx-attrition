import json,glob
inp=json.load(open('batch_130_in.json'))
E={}
exec(open('scratch/130/entries.py').read())
out=[]
for p in inp:
    k=p['key']
    if k in E:
        e=E[k]; e.setdefault('key',k); e.setdefault('name',p['name']); e.setdefault('program_id',p['program_id'])
        out.append(e)
json.dump(out,open('batch_130_out.json','w'),indent=1)
print(len(out))
