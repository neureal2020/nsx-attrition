import json,sys,os
F='batch_089_out.json'
def add(key,name,pid,ident,basis,res,outcome,detail,cur,agrees,dis,g,d,abns,sources,ns,yl=None,dest=None,ds=None):
    L=json.load(open(F)) if os.path.exists(F) else []
    L=[x for x in L if x['key']!=key]
    L.append({"key":key,"name":name,"program_id":pid,"identity":ident,"identity_basis":basis,"residency_stated":res,"outcome":outcome,"outcome_detail":detail,"year_left":yl,"destination_program":dest,"destination_start_year":ds,"current":cur,"agrees_with_db":agrees,"disagreement":dis,"checks":{"google":g,"doximity":d,"usnews":"deferred"},"abns_certified":abns,"sources":sources,"searches_used":ns})
    json.dump(L,open(F,'w'),indent=1)
