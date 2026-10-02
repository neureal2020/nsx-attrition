import json,sys,os
OUT='batch_115_out.json'
inp={p['key']:p for p in json.load(open('batch_115_in.json'))}
def add(key,ident,basis,res,outcome,detail,cur,gsrc,dox,sources,searches,abns,agrees=True,dis="",yl=None,dest=None,dsy=None,g="found"):
    out=json.load(open(OUT)) if os.path.exists(OUT) else []
    out=[o for o in out if o['key']!=key]
    p=inp[key]
    out.append({"key":key,"name":p['name'],"program_id":p['program_id'],"identity":ident,"identity_basis":basis,
     "residency_stated":res,"outcome":outcome,"outcome_detail":detail,"year_left":yl,"destination_program":dest,"destination_start_year":dsy,
     "current":cur,"agrees_with_db":agrees,"disagreement":dis,"checks":{"google":g,"doximity":dox,"usnews":"deferred"},
     "abns_certified":abns,"sources":[{"url":u,"type":t,"evidence":e} for u,t,e in sources],"searches_used":searches})
    order=list(inp)
    out.sort(key=lambda o:order.index(o['key']))
    json.dump(out,open(OUT,'w'),indent=1)
