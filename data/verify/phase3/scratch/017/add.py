import json,sys,os
OUT='batch_017_out.json'
inp={p['key']:p for p in json.load(open('batch_017_in.json'))}
def add(key,identity,basis,res,outcome,detail,current,agrees,dis,checks,abns,sources,searches,yl=None,dp=None,ds=None):
    out=json.load(open(OUT)) if os.path.exists(OUT) else []
    out=[o for o in out if o['key']!=key]
    p=inp[key]
    out.append({"key":key,"name":p['name'],"program_id":p['program_id'],"identity":identity,"identity_basis":basis,
    "residency_stated":[dict(institution=i,specialty=s,start=a,end=b) for i,s,a,b in res],
    "outcome":outcome,"outcome_detail":detail,"year_left":yl,"destination_program":dp,"destination_start_year":ds,
    "current":current,"agrees_with_db":agrees,"disagreement":dis,
    "checks":dict(zip(["google","doximity","usnews"],checks)),"abns_certified":abns,
    "sources":[dict(url=u,type=t,evidence=e) for u,t,e in sources],"searches_used":searches})
    order=list(inp)
    out.sort(key=lambda o:order.index(o['key']))
    json.dump(out,open(OUT,'w'),indent=1)
