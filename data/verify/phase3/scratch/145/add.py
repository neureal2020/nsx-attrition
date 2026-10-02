import json,sys,os
IN='batch_145_in.json'; OUT='batch_145_out.json'
def add(idx,identity,basis,res,outcome,detail,current,agrees,dis,g,d,abns,src,n,yl=None,dest=None,dsy=None):
    inp=json.load(open(IN))
    out=json.load(open(OUT)) if os.path.exists(OUT) else []
    p=inp[idx]
    out=[o for o in out if o['key']!=p['key']]
    out.append(dict(key=p['key'],name=p['name'],program_id=p['program_id'],identity=identity,identity_basis=basis,
      residency_stated=[dict(institution=i,specialty=s,start=a,end=b) for i,s,a,b in res],
      outcome=outcome,outcome_detail=detail,year_left=yl,destination_program=dest,destination_start_year=dsy,current=current,
      agrees_with_db=agrees,disagreement=dis,checks=dict(google=g,doximity=d,usnews="deferred"),abns_certified=abns,
      sources=[dict(url=u,type=t,evidence=e) for u,t,e in src],searches_used=n))
    order={p['key']:i for i,p in enumerate(inp)}
    out.sort(key=lambda o:order[o['key']])
    json.dump(out,open(OUT,'w'),indent=1)
