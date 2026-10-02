import json,os
inp=json.load(open('batch_102_in.json'))
by={p['key']:p for p in inp}
out=json.load(open('batch_102_out.json')) if os.path.exists('batch_102_out.json') else []
def add(key,identity,basis,res,outcome,detail,current,dox,src,searches,abns=None,disagree=None,google="found",ident_notes=None):
    p=by[key]
    r={"key":key,"name":p['name'],"program_id":p['program_id'],"identity":identity,"identity_basis":basis,
    "residency_stated":res,"outcome":outcome,"outcome_detail":detail,"year_left":None,"destination_program":None,"destination_start_year":None,
    "current":current,"agrees_with_db":disagree is None,"disagreement":disagree,
    "checks":{"google":google,"doximity":dox,"usnews":"deferred"},"abns_certified":abns,"sources":src,"searches_used":searches}
    out[:]=[o for o in out if o['key']!=key]+[r]
    order={p['key']:i for i,p in enumerate(inp)}
    out.sort(key=lambda o:order[o['key']])
    json.dump(out,open('batch_102_out.json','w'),indent=1)
UC="University of Cincinnati Medical Center/College of Medicine"
