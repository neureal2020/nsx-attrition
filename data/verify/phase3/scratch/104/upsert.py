import json,sys,os
inp=json.load(open('batch_104_in.json'))
outp='batch_104_out.json'
cur={e['key']:e for e in json.load(open(outp))} if os.path.exists(outp) else {}
new=json.load(sys.stdin)
for e in new: cur[e['key']]=e
res=[cur[p['key']] for p in inp if p['key'] in cur]
json.dump(res,open(outp,'w'),indent=1)
print(len(res),'saved')
