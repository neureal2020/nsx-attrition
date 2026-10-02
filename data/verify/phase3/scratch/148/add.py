import json,os,sys
IN='batch_148_in.json';OUT='batch_148_out.json'
inp={p['key']:p for p in json.load(open(IN))}
out=json.load(open(OUT)) if os.path.exists(OUT) else []
GR="https://www.neurosurgery.pitt.edu/training/residency-program/graduates"
def add(key,identity,basis,res,outcome,detail,current,dox,abns,sources,searches,google="found",agrees=True,dis="",yl=None,dest=None,dstart=None):
    p=inp[key]
    out[:]=[o for o in out if o['key']!=key]
    out.append(dict(key=key,name=p['name'],program_id=p['program_id'],identity=identity,identity_basis=basis,residency_stated=res,outcome=outcome,outcome_detail=detail,year_left=yl,destination_program=dest,destination_start_year=dstart,current=current,agrees_with_db=agrees,disagreement=dis,checks=dict(google=google,doximity=dox,usnews="deferred"),abns_certified=abns,sources=sources,searches_used=searches))
    order=[p['key'] for p in json.load(open(IN))]
    out.sort(key=lambda o:order.index(o['key']))
    json.dump(out,open(OUT,'w'),indent=1)
def S(url,t,ev):return dict(url=url,type=t,evidence=ev)
def R(a,b,inst="UPMC Medical Education",spec="neurosurgery"):return [dict(institution=inst,specialty=spec,start=a,end=b)]
