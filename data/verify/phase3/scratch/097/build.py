import json,sys
D='/Users/neureal/Documents/Residency Application Study/data/verify/phase3/'
inp=json.load(open(D+'batch_097_in.json'))
byk={p['key']:p for p in inp}
R=json.load(open('res.json')) if __import__('os').path.exists('res.json') else {}
def add(key,**kw):
    R[key]=kw; json.dump(R,open('res.json','w'))
def emit():
    out=[]
    for p in inp:
        r=R.get(p['key'])
        if not r: continue
        o={"key":p['key'],"name":p['name'],"program_id":p['program_id']}
        o.update(r); out.append(o)
    json.dump(out,open(D+'batch_097_out.json','w'),indent=1,ensure_ascii=False)
    print(len(out),'written')
