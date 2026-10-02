import json
inp=json.load(open('batch_066_in.json'))
W="https://neurosurgery.weillcornell.org/residents/"
def rec(i,ident,basis,res,outcome,detail,cur,g,dx,src,ns,abns=False,**kw):
    p=inp[i]
    d={"key":p['key'],"name":p['name'],"program_id":p['program_id'],"identity":ident,"identity_basis":basis,
    "residency_stated":res,"outcome":outcome,"outcome_detail":detail,"year_left":kw.get('yl'),"destination_program":kw.get('dp'),"destination_start_year":kw.get('ds'),
    "current":cur,"agrees_with_db":kw.get('agree',True),"disagreement":kw.get('dis',""),
    "checks":{"google":g,"doximity":dx,"usnews":"deferred"},"abns_certified":abns,"sources":[{"url":u,"type":t,"evidence":e} for u,t,e in src],"searches_used":ns}
    return d
