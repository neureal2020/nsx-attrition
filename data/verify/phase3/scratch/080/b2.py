import json
inp=json.load(open('../../batch_080_in.json'))
out=json.load(open('out1.json'))
SIU="Southern Illinois University School of Medicine"
D="https://www.doximity.com/pub/"
def base(i,ident,basis,res,outcome,detail,cur,agree=True,dis="",checks=None,abns=False,src=None,ss=2,yl=None,dest=None,dsy=None):
    p=inp[i]
    return {"key":p['key'],"name":p['name'],"program_id":p['program_id'],"identity":ident,"identity_basis":basis,
     "residency_stated":res,"outcome":outcome,"outcome_detail":detail,"year_left":yl,"destination_program":dest,"destination_start_year":dsy,
     "current":cur,"agrees_with_db":agree,"disagreement":dis,"checks":checks or {"google":"found","doximity":"found","usnews":"deferred"},
     "abns_certified":abns,"sources":src,"searches_used":ss}
def r(inst,s,e,spec="neurosurgery"): return [{"institution":inst,"specialty":spec,"start":s,"end":e}]
def s(u,t,ev): return {"url":u,"type":t,"evidence":ev}
def cur_siu(i,doxy,train,school,extra=None,dstat="found",ss=2):
    p=inp[i]; y=p['entry_year']
    src=[]
    if doxy: src.append(s(D+doxy,"doximity",train))
    if extra: src+=extra
    o=base(i,"confirmed" if doxy or extra else "probable",f"SIU neurosurgery resident (entered {y}); {school}",r(SIU,y,None),"in_training",
       "Current SIU neurosurgery resident per program/faculty-directory listing"+(" and Doximity" if doxy else ""),"neurosurgery resident, SIU School of Medicine, Springfield IL",
       checks={"google":"found","doximity":dstat,"usnews":"deferred"},src=src,ss=ss)
    return o
o=[]
o.append(base(9,"confirmed","Doximity: MD SIU Class of 2014, neurological surgery residency at SIU 2014-2021; Mercy/WashU neurosurgeon; matches the program's first resident (2014)",
 r(SIU,2014,2021),"completed","Completed SIU neurosurgery residency 2021; fellowships in spine (SIU 2020) and neurological surgery at NewYork-Presbyterian (Cornell) 2020-21; now neurosurgeon, ABNS-certified; WashU faculty from July 2026",
 "neurosurgeon, Mercy St. Louis; joining WashU Taylor Family Dept of Neurosurgery (faculty, 2026)",
 src=[s(D+"alex-michael-md","doximity","Residency, Neurological Surgery, 2014 - 2021 (SIU); Certifications: American Board of Neurological Surgery"),
      s("https://neurosurgery.wustl.edu/washu-neurosurgery-welcomes-dr-alex-michael/","news","WashU Neurosurgery Welcomes Dr. Alex Michael"),
      s("https://physicians.wustl.edu/people/alex-p-michael-md-facs/","bio","search snippet: completed neurosurgery residency 2021 at SIU, MD SIU 2014")],abns=True,ss=1))
o.append(base(10,"confirmed","SIU faculty page and Doximity (MD SIU Class of 2015); SIU neurosurgery faculty; residency at SIU",
 r(SIU,2015,2022),"completed","SIU MD 2015, SIU neurosurgery residency (class of 2022), Mayo cerebrovascular/endovascular/skull base fellowship; now Assistant Professor of neurosurgery at SIU Medicine",
 "Assistant Professor, Division of Neurosurgery, SIU Medicine, Springfield IL",
 src=[s("https://www.siumed.edu/breck-jones","bio","search snippet: obtained his medical degree from SIU School of Medicine and completed his neurosurgery residency at SIU; fellowship Mayo Clinic"),
      s(D+"breck-jones-md","doximity","Southern Illinois University School of Medicine, Class of 2015; Springfield IL Neurosurgery")],ss=1))
o.append(base(11,"probable","SIU resident directory page names Victoria Watson (Marshall MD, WVU undergrad) as SIU neurosurgery resident; Marshall news article names Dr. Watson as an internal medicine resident who spent time in neurosurgery; co-author on 2018 SIU neurosurgery abstracts (Watson, V.L.) with the SIU residents",
 r(SIU,2016,2021),"switched_specialty","Left SIU neurosurgery, moved to internal medicine at Marshall University Joan C. Edwards SOM (residency completing 2026 per April 2025 news); plans neurocritical care fellowship. Exact year left/IM start not stated in sources found (DB says left after 2020-21).",
 "internal medicine resident, Marshall University (Joan C. Edwards SOM), completing 2026; planning neurocritical care fellowship",
 checks={"google":"found","doximity":"not_found","usnews":"deferred"},
 src=[s("https://jcesom.marshall.edu/news/musom-news/drs-alagha-watson-and-wright-named-april-residents-of-the-month/","news","Watson: from Pinch, WV; medical degree Marshall; spent time in neurosurgery before internal medicine residency (completing 2026); plans neurocritical care fellowship (Apr 21, 2025)"),
      s("https://www.siumed.edu/resident-fellow/victoria-watson.html","search_snippet","Victoria Watson | SIU School of Medicine - Resident Physician in Neurosurgery; MD Marshall University; undergrad WVU"),
      s(D+"alex-michael-md","doximity","2018 SIU abstracts list V.L. Watson with SIU neurosurgery residents (Cozzens, Jones, Lipson, Michael)")],ss=2,yl=2021,dest="Internal Medicine, Marshall University Joan C. Edwards SOM"))
o.append(base(12,"confirmed","SIU resident profile: Adam Benjamin Lipson, MD Temple 2016/17, PGY neurosurgery SIU 2017-24; Doximity Portland OR profile lists IL license 2017-2024; co-author on SIU abstracts. (NJ neurosurgeon Adam C. Lipson is a namesake, Harvard 2000, not this person)",
 r(SIU,2017,2024),"completed","Completed SIU neurosurgery residency 2024; functional/stereotactic neurosurgery fellowship at OHSU 2024-25; now OHSU functional neurosurgery instructor/faculty (Portland OR)",
 "functional and stereotactic neurosurgeon (post-fellowship), OHSU, Portland OR",
 src=[s("https://www.siumed.edu/resident-fellow/adam-lipson.html","search_snippet","Adam Benjamin Lipson graduated Temple Lewis Katz School of Medicine (MD 2017); neurosurgery resident at SIU Springfield (2017-24)"),
      s("https://www.ohsu.edu/providers/adam-benjamin-lipson-md","bio","OHSU: completed neurosurgery residency at SIU in 2024; fellowship functional and stereotactic neurological surgery OHSU"),
      s(D+"adam-lipson-md-0646aaa9","doximity","Adam Benjamin Lipson, Portland OR, Neurosurgery; IL State Medical License 2017 - 2024; OR license 2024 -")],ss=2))
o.append(base(13,"confirmed","Doximity and SIU pages: residency neurological surgery SIU 2018-2025, MD U Minnesota 2018",
 r(SIU,2018,2025),"completed","Completed SIU neurosurgery residency 2025; neurosurgical oncology fellow at Memorial Sloan Kettering 2025-26; Doximity now lists Miami FL (Baptist Health) neurosurgeon",
 "neurosurgical oncology fellow, MSK (2025-26); Baptist Health, Miami FL faculty per Doximity/MSK page",
 src=[s(D+"nathan-nordmann-md","doximity","Residency, Neurological Surgery, 2018 - 2025 (SIU); Neurosurgeon || Neurosurgical Oncology Fellow"),
      s("https://www.mskcc.org/departments/neurosurgery/neurosurgical-oncology/fellows","program_page","search snippet: MSK neurosurgical oncology fellows list Nathan Nordmann")],ss=1))
o.append(base(14,"probable","Doximity (Springfield IL neurosurgery, MD SIU Class of 2019, co-authored SIU neurosurgery papers with Nordmann/Bernard) and SIU faculty directory; common name",
 r(SIU,2019,2026),"completed","SIU MD 2019; SIU directory lists as neurosurgery resident with graduation year 2026; on 2025-26 roster as PGY7 (chief year) and absent from 2026-27 roster, consistent with completing June 2026. Doximity page shows odd ABIM internal medicine/hematology certifications (likely a merged namesake record); no ABNS listed yet. Not confirmed by a post-residency position.",
 "neurosurgeon, Springfield IL (Lincoln Memorial Hospital affiliation per Doximity)",
 src=[s(D+"matthew-weber-md-87567dee","doximity","Southern Illinois University School of Medicine, Class of 2019; Neurosurgery Springfield IL; affiliated with Lincoln Memorial Hospital; pubs with Nordmann WEB Y-stent"),
      s("https://www.siumed.edu/matthew-weber","search_snippet","Matthew Weber SIU: Neurosurgery Resident Physician, resident graduation year 2026")],ss=1))
# current residents
o.append(cur_siu(15,"justin-michael-md","Residency, Neurological Surgery, 2020 - 2027 (SIU); MD Indiana 2020","Indiana University School of Medicine",
 extra=[s("https://www.siumed.edu/justin-michael","search_snippet","Justin Michael - neurosurgery resident SIU, graduation year 2027; Indiana University School of Medicine")]))
o[-1]["residency_stated"]=r(SIU,2020,2027)
o.append(cur_siu(16,None,"","Indiana University School of Medicine",
 extra=[s("https://www.siumed.edu/kayla-chin","search_snippet","Kayla Chin | SIU School of Medicine - Resident Physician, Neurosurgery; Indiana University School of Medicine"),
        s("https://www.siumed.edu/surgery/neuro/neurosurgery-resident-research","program_page","Chin listed in SIU neurosurgery resident research")],dstat="not_found",ss=2))
o.append(cur_siu(17,None,"","Lewis Katz School of Medicine at Temple",
 extra=[s("https://www.siumed.edu/ava-hoeft","search_snippet","Ava Hoeft SIU neurosurgery resident, Temple Lewis Katz MD, graduation year 2029"),
        s(D+"jeffrey-cozzens-md","search_snippet","2024 Operative Neurosurgery 5-ALA paper co-authored by Ava Hoeft with SIU faculty Cozzens (via Breck Jones Doximity pubs)")],dstat="not_found",ss=2))
o[-1]["residency_stated"]=r(SIU,2022,2029)
o.append(cur_siu(18,"joseph-bernard-md-d2df204f","SIU Class of 2023 MD; Springfield IL Neurosurgery; co-author with SIU neurosurgery residents","Southern Illinois University School of Medicine",
 extra=[s("https://www.siumed.edu/joseph-bernard","search_snippet","Joseph Bernard, SIU neurosurgery resident, graduation year 2030")]))
o[-1]["residency_stated"]=r(SIU,2023,2030)
o.append(cur_siu(19,None,"","University of South Carolina School of Medicine Greenville",
 extra=[s("https://www.siumed.edu/michael-garovich","search_snippet","Michael Garovich | SIU School of Medicine - neurosurgery resident, graduation year 2031; USC SOM Greenville"),
        s("https://www.siumed.edu/surgery/neuro/neurosurgery-resident-research","program_page","Garovich listed in SIU neurosurgery resident research")],dstat="not_found",ss=2))
o[-1]["residency_stated"]=r(SIU,2024,2031)
o.append(cur_siu(20,"sonia-pulido-md","Univ of Illinois College of Medicine at Peoria Class of 2025; Springfield IL Neurosurgery; JNS Case Lessons 2026 with SIU's Bruce Frankel","University of Illinois College of Medicine at Peoria",
 extra=[s("https://www.linkedin.com/in/sonia-pulido-8784b5291/","search_snippet","Sonia Pulido - Neurosurgery PGY-I at Southern Illinois ...")]))
o[-1]["residency_stated"]=r(SIU,2025,2032)
o.append(cur_siu(21,"chibueze-ezeudu-md","MD Texas A&M 2021-2026; IL license 2026-2029; Springfield IL Neurosurgery","Texas A&M Health Science Center College of Medicine"))
o[-1]["residency_stated"]=r(SIU,2026,2033)
o[-1]["outcome_detail"]="Incoming PGY-1 (July 2026) SIU neurosurgery resident; Doximity lists Springfield IL neurosurgery, MD 2026"
SLU="SSM Health/Saint Louis University School of Medicine"
o.append(base(22,"confirmed","Doximity: SLU MD 2011, SLU neurological surgery residency 2011-2018, Jefferson endovascular fellowship 2018-19; SLU chief resident per practice bio",
 r(SLU,2011,2018),"completed","Completed SLU neurosurgery residency 2018 (chief resident), Jefferson cerebrovascular/endovascular fellowship 2018-19; ABNS-listed; practising neurosurgeon at Elite Brain & Spine, Danbury CT (chief neurointerventional surgery, Vassar Brothers)",
 "neurosurgeon/neurointerventional, Elite Brain and Spine of Connecticut, Danbury CT",abns=True,
 src=[s(D+"jonathon-lebovitz-md","doximity","Residency, Neurological Surgery, 2011 - 2018 (SSM Health/SLU); Fellowship Jefferson 2018-2019; American Board of Neurological Surgery"),
      s("https://elitebrainspine.com/jonathon-lebovitz/","bio","completed his surgical internship and residency in Neurological Surgery at Saint Louis University (chief resident); Jefferson fellowship")],ss=1))
o.append(base(23,"confirmed","Doximity and Jefferson faculty bio: chief residency SLU 2011-12, SLU residency 2012-13, Mount Sinai NS residency 2013-2016; Jefferson bio lists neurosurgery residency at Mount Sinai",
 [{"institution":SLU,"specialty":"neurosurgery","start":2011,"end":2013},{"institution":"Icahn School of Medicine at Mount Sinai","specialty":"neurosurgery","start":2013,"end":2016}],
 "transferred","Transferred from SLU neurosurgery (chief residency 2011-12, resident to 2013) to Mount Sinai neurosurgery residency 2013-2016; now cerebrovascular neurosurgeon, ABNS-certified. Note he was already a senior resident when first listed (Sep 2012), so he was not a 2011+ entrant at SLU.",
 "Associate Professor of Neurological Surgery and Division Chief of Neuroscience, Jefferson New Jersey (Sewell NJ)",yl=2013,dest="Icahn School of Medicine at Mount Sinai",dsy=2013,abns=True,
 src=[s(D+"hekmat-zarzour-md","doximity","Residency Neurological Surgery Mount Sinai 2013 - 2016; SSM Health/SLU Residency 2012 - 2013; Chief Residency 2011 - 2012; ABNS"),
      s("https://www.jefferson.edu/academics/colleges-schools-institutes/skmc/departments/neurosurgery/faculty/zarzour.html","bio","Residency: Neurosurgery, Mount Sinai Hospital (bio also lists Burdenko Institute)")],ss=1))
o.append(base(24,"confirmed","Doximity: MD Kansas 2012; SLU surgery internship 2012-13, SLU neurosurgery residency 2013-2019, cerebrovascular fellowship SLU 2019-20; listed as 'Matt Pierson' at Midwest Neurosurgery Associates; co-author with SLU residents",
 r(SLU,2013,2019),"completed","Completed SLU neurosurgery residency 2019 (internship 2012-13 in surgery at SLU), SLU cerebrovascular/skull base fellowship 2019-20; ABNS-listed; practising neurosurgeon at Midwest Neurosurgery Associates, Kansas",
 "skull base and cerebrovascular neurosurgeon, Midwest Neurosurgery Associates (Merriam KS)",abns=True,
 src=[s(D+"matt-pierson-md","doximity","Residency, Neurological Surgery, 2013 - 2019 (SSM Health/SLU); Fellowship Cerebrovascular & Skull Base 2019-2020; ABNS"),
      s("https://www.linkedin.com/in/matthew-pierson-802624134/","search_snippet","Matthew Pierson - Midwest Neurosurgery Associates, P.A.")],ss=1))
# fix note on doximity checks
for x in o:
    pass
# Doximity note for Weber: agrees
# Michael/Jones etc dis
for x in o:
    if x['key'] in ('59:ale:michael','59:bre:jones','59:vic:watson','59:ada:lipson'): pass
allo=out+o
json.dump(allo,open('../../batch_080_out.json','w'),indent=1)
from collections import Counter
print(len(allo),Counter(x['outcome'] for x in allo),Counter(x['identity'] for x in allo))
print(Counter(x['checks']['doximity'] for x in allo),Counter(x['checks']['usnews'] for x in allo),sum(x['searches_used'] for x in allo))
