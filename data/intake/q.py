import json,sys
f='data/intake/phase1_queue.json'; q=json.load(open(f))
done,start=[int(x) for x in sys.argv[1].split(',') if x],[int(x) for x in sys.argv[2].split(',') if x]
for d in done:
    if d in q['running']: q['running'].remove(d)
    q['done'].append(d)
for s in start: q['pending'].remove(s); q['running'].append(s)
json.dump(q,open(f,'w'),indent=0)
print('done',len(q['done']),'running',q['running'],'pending',len(q['pending']),'next',q['pending'][:5])
