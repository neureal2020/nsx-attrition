import json,os
OUT='batch_093_out.json'
def add(key,name,pid,identity,basis,resid,outcome,detail,current,checks,sources,searches,abns=None,agrees=True,dis="",year_left=None,dest=None,dest_start=None):
    d=json.load(open(OUT)) if os.path.exists(OUT) else []
    d=[x for x in d if x['key']!=key]
    d.append(dict(key=key,name=name,program_id=pid,identity=identity,identity_basis=basis,residency_stated=resid,outcome=outcome,outcome_detail=detail,year_left=year_left,destination_program=dest,destination_start_year=dest_start,current=current,agrees_with_db=agrees,disagreement=dis,checks=checks,abns_certified=abns,sources=sources,searches_used=searches))
    json.dump(d,open(OUT,'w'),indent=1,ensure_ascii=False)
