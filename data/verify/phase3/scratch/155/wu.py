import sys; sys.path.insert(0,'scratch/155')
from add import add
def wu(k,ident,basis,start,end,detail,cur,src,g="found",d="found",abns=True,n=2,dis="",agree=True,outcome="completed"):
    add(k,identity=ident,identity_basis=basis,
     residency_stated=[{"institution":"Washington University/B-JH/SLCH Consortium","specialty":"neurosurgery","start":start,"end":end}],
     outcome=outcome,outcome_detail=detail,current=cur,agrees_with_db=agree,disagreement=dis,
     checks={"google":g,"doximity":d},abns_certified=abns,sources=src,searches_used=n)
D="https://www.doximity.com/pub/"
