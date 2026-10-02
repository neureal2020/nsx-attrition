import json,sys,os
base="/Users/neureal/Documents/Residency Application Study/data/verify/phase3/"
inp={p['key']:p for p in json.load(open(base+'batch_098_in.json'))}
jl=base+'scratch/098/recs.jsonl'
def add(key,identity,basis,res,outcome,detail,current,agrees,dis,dox,google,abns,sources,searches,yl=None,dest=None,dst=None):
    p=inp[key]
    r={"key":key,"name":p['name'],"program_id":p['program_id'],"identity":identity,"identity_basis":basis,
    "residency_stated":[{"institution":a,"specialty":"neurosurgery" if len(x)<4 else x[3],"start":b,"end":c} for x in res for a,b,c in [x[:3]]],
    "outcome":outcome,"outcome_detail":detail,"year_left":yl,"destination_program":dest,"destination_start_year":dst,
    "current":current,"agrees_with_db":agrees,"disagreement":dis,
    "checks":{"google":google,"doximity":dox,"usnews":"deferred"},"abns_certified":abns,
    "sources":[{"url":u,"type":t,"evidence":e} for u,t,e in sources],"searches_used":searches}
    open(jl,'a').write(json.dumps(r)+"\n")
def compile():
    got={}
    for l in open(jl):
        r=json.loads(l);got[r['key']]=r
    out=[got[k] for k in inp if k in got]
    json.dump(out,open(base+'batch_098_out.json','w'),indent=1)
    print(len(out))
