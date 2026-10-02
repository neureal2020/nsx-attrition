from add import add
R="https://health.ucdavis.edu/neurological-surgery/academic-programs/residency/current-residents"
def res(key,pgy,school,ent,idn,basis,dox,extra_src=None,n=3,cur=None):
    src=[{"url":R,"type":"program_page","evidence":"UC Davis Neurological Surgery residents 2026-2027, PGY-%d, %s"%(pgy,school)}]
    if extra_src: src+=extra_src
    add(key,identity=idn,identity_basis=basis,residency_stated=[{"institution":"UC Davis Health","specialty":"neurosurgery","start":ent,"end":None}],
     outcome="in_training",outcome_detail="Listed on the UC Davis neurosurgery current-residents page for 2026-27 as PGY-%d"%pgy,current=cur or "Neurosurgery resident (PGY-%d), UC Davis"%pgy,
     agrees_with_db=True,disagreement="",checks={"google":"found","doximity":dox,"usnews":"deferred"},sources=src,searches_used=n)
res("77:rob:riestenberg",6,"Northwestern University, 2021",2021,"confirmed","UC Davis roster PGY-6 Northwestern 2021; Feinberg student news 2019; UC Davis-coauthored 2024 J Neurooncol paper","not_found")
res("77:gun:lee",5,"University of Hawaii, 2022",2022,"confirmed","UC Davis roster PGY-5 Hawaii JABSOM 2022 matches Doximity resident physician Sacramento, JABSOM Class of 2022, UC Davis co-authors","found",
 [{"url":"https://www.doximity.com/pub/gunnar-lee-md","type":"doximity","evidence":"Resident Physician Sacramento CA; University of Hawaii JABSOM Class of 2022; CA license 2026-2028"}])
res("77:mar:taylor",5,"State University of New York at Buffalo, 2022",2022,"confirmed","UC Davis roster PGY-5 Buffalo 2022; Doximity/WebMD Buffalo 2022, Sacramento, co-author with UC Davis Waldau/Moskalik","found",
 [{"url":"https://www.doximity.com/pub/maritza-taylor-md","type":"doximity","evidence":"Other MD/DO Sacramento; Jacobs School of Medicine University at Buffalo Class of 2022"}])
res("77:mor:jude",4,"University of California, Davis, 2023",2023,"confirmed","UC Davis roster PGY-4 UC Davis MD 2023; co-author Morgan B Jude with Shahlaie (UC Davis) on sellar masses paper","not_found")
res("77:pao:palmisciano",4,"University of Catania, 2019",2023,"confirmed","UC Davis roster PGY-4 Catania 2019; bio: graduated Catania July 2019, currently neurosurgery resident UC Davis","not_found",
 [{"url":"https://www.linkedin.com/in/paolo-palmisciano-624972164/","type":"search_snippet","evidence":"Paolo Palmisciano - PGY-4 Neurosurgery Resident"}])
res("77:kha:soufi",3,"University of California, Davis, 2024",2024,"confirmed","UC Davis roster PGY-3 UC Davis MD 2024; WebMD/LinkedIn: matched UC Davis neurosurgery","not_found")
res("77:sir:mor",3,"University of California, Davis, 2024",2024,"confirmed","UC Davis roster PGY-3 UC Davis MD 2024; UC Davis Match Day 2024 news","not_found")
res("77:and:conching",2,"University of Hawaii, 2025",2025,"confirmed","UC Davis roster PGY-2 JABSOM 2025; Hawaii News Now Dec 2025: six months into seven-year neurosurgery residency at UC Davis","not_found",
 [{"url":"https://www.hawaiinewsnow.com/2025/12/25/native-hawaiian-woman-breaks-barriers-first-neurosurgeon/","type":"news","evidence":"six months into a seven-year neurosurgery residency at UC Davis (search snippet)"}])
res("77:ala:harris",2,"Virginia Commonwealth University, 2025",2025,"confirmed","UC Davis roster PGY-2 VCU 2025; UC Davis Match 2025 LinkedIn post welcomes Alan Harris, M.D. (VCU). Common name but roster+post match.","not_found",
 [{"url":"https://www.linkedin.com/posts/uc-davis-department-of-neurological-surgery_match2025-neurosurgery-residents-activity-7308895281968820224-kvOG","type":"search_snippet","evidence":"incoming residents of our residency program, Andie Conching, M.D., and Alan Harris, M.D."}])
res("77:ish:shah",1,"University of Southern California, 2026",2026,"probable","UC Davis roster PGY-1 USC 2026; Keck/USC student Ishan Shah worked in Zada neurosurgery lab; no independent page tying him to UC Davis. Name is common.","not_found")
res("77:lar:rostomian",1,"Wayne State University, 2026",2026,"confirmed","UC Davis roster PGY-1 Wayne State 2026; search snippet: incoming neurological surgery resident at UC Davis Health, Wayne State","not_found")
def dn(key,name,school,ab):
    add(key,identity="confirmed",identity_basis="Doximity: University of Chicago neurological surgery residency 2011-2018, %s Class of 2011; ABNS listed"%school,
     residency_stated=[{"institution":"University of Chicago","specialty":"neurosurgery","start":2011,"end":2018}],outcome="completed",
     outcome_detail="Completed University of Chicago neurosurgery 2011-2018; practising neurosurgeon, ABNS listed",abns_certified=True,agrees_with_db=True,disagreement="",
     checks={"google":"found","doximity":"found","usnews":"deferred"},**ab)
dn("78:ash:ralston","Ashley Ralston","Wayne State University School of Medicine",dict(current="Pediatric neurosurgeon, Driscoll Children's Hospital, Corpus Christi TX (pediatric neurosurgery fellowship Children's Healthcare of Atlanta 2018-19)",
 sources=[{"url":"https://www.doximity.com/pub/ashley-ralston-md","type":"doximity","evidence":"University of Chicago Residency, Neurological Surgery, 2011 - 2018; American Board of Neurological Surgery"}],searches_used=1))
dn("78:mel:stamates","Melissa Stamates","Ohio State University College of Medicine",dict(current="Neurosurgeon, Cape Fear Valley Medical Center, Fayetteville NC",
 sources=[{"url":"https://www.doximity.com/pub/melissa-stamates-md","type":"doximity","evidence":"University of Chicago Residency, Neurological Surgery, 2011 - 2018; American Board of Neurological Surgery"},
 {"url":"https://www.capefearvalley.com/doctors/melissa-stamates-md","type":"bio","evidence":"Melissa Stamates, MD, Cape Fear Valley Health (search result)"}],searches_used=1))
