import json,sys
inp={p['key']:p for p in json.load(open('batch_084_in.json'))}
order=[p['key'] for p in json.load(open('batch_084_in.json'))]
try: out={r['key']:r for r in json.load(open('batch_084_out.json'))}
except: out={}
def add(key,identity,basis,res,outcome,detail,current,agrees,dis,g,d,srcs,abns=None,ns=2,yl=None,dest=None,dys=None):
    p=inp[key]
    out[key]=dict(key=key,name=p['name'],program_id=p['program_id'],identity=identity,identity_basis=basis,residency_stated=[dict(institution=i,specialty="neurosurgery",start=s,end=e) for i,s,e in res],outcome=outcome,outcome_detail=detail,year_left=yl,destination_program=dest,destination_start_year=dys,current=current,agrees_with_db=agrees,disagreement=dis,checks=dict(google=g,doximity=d,usnews="deferred"),abns_certified=abns,sources=[dict(url=u,type=t,evidence=e) for u,t,e in srcs],searches_used=ns)
def save():
    json.dump([out[k] for k in order if k in out],open('batch_084_out.json','w'),indent=1)
