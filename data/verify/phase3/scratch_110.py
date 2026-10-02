import json
D=json.load(open('batch_110_in.json'))
R={}
def add(i,identity,basis,res,outcome,detail,cur,dox,ab,srcs,searches,ident_note=None,yl=None):
    p=D[i]
    R[i]={"key":p['key'],"name":p['name'],"program_id":p['program_id'],"identity":identity,"identity_basis":basis,
    "residency_stated":res,"outcome":outcome,"outcome_detail":detail,"year_left":yl,"destination_program":None,"destination_start_year":None,
    "current":cur,"agrees_with_db":True,"disagreement":"",
    "checks":{"google":"found","doximity":dox,"usnews":"deferred"},"abns_certified":ab,
    "sources":[{"url":u,"type":t,"evidence":e} for u,t,e in srcs],"searches_used":searches}
def out():
    json.dump([R[i] for i in sorted(R)],open('batch_110_out.json','w'),indent=1)
