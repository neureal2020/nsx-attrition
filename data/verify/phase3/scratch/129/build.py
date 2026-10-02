import json
inp=json.load(open('batch_129_in.json'))
R="https://www.urmc.rochester.edu/education/graduate-medical-education/prospective-residents/neurosurgery/our-residents"
USF="https://health.usf.edu/medicine/neurosurgery/residency/alumni/"
D="https://www.doximity.com/pub/"
def s(u,t,e): return {"url":u,"type":t,"evidence":e}
# key: (identity, basis, res_stated list, outcome, detail, year_left, current, abns, dox, sources, searches, google)
ro={}
def roch(key,pgy,school,dox_slug,dox_ev,dox,ident="confirmed",searches=1,extra=None,end=None,start=None,cur=None):
    src=[s(R,"program_page",f"Roster lists {key} as PGY-{pgy}; medical school {school}")]
    if dox_slug: src.append(s(D+dox_slug,"doximity",dox_ev))
    if extra: src+=extra
    ro[key]=dict(identity=ident,src=src,dox=dox,searches=searches,pgy=pgy,school=school,end=end,start=start)
p=lambda n:n
notes={}
def add(key,**kw): notes[key]=kw
# Rochester
rocs=[
("102:der:george",7,"University of Colorado","derek-george-md","Residency, Neurological Surgery, 2020 - 2027 at University of Rochester Medical Center; MD Colorado 2020","found","confirmed",1,2027),
("102:tay:furst",7,"Upstate Medical University","taylor-furst-md","Residency, Neurological Surgery, 2020 - 2027, University of Rochester Medical Center; SUNY Upstate MD 2020","found","confirmed",1,2027),
("102:cat:jay",6,"University of Rochester","catherine-jay-md","Residency, Neurological Surgery, 2021 - 2028, University of Rochester Medical Center; MD 2021","found","confirmed",1,2028),
("102:pra:romiyo",6,"Cooper Medical School","prasanth-romiyo-md","Residency, Neurological Surgery, 2021 - 2028, University of Rochester Medical Center; Cooper Medical School of Rowan 2020","found","confirmed",1,2028),
("102:ada:li",5,"Icahn School of Medicine at Mount Sinai","adam-li-md","Residency, Neurological Surgery, 2022 - 2029, University of Rochester Medical Center; Mount Sinai MD 2022","found","confirmed",1,2029),
("102:rac:whyte",5,"University of Rochester SMD","racquel-whyte-md","Resident Physician, Rochester NY; MD University of Rochester SMD Class of 2022 (no residency line shown)","found","confirmed",1,None),
("102:roh:singh",4,"Mayo Clinic Arizona","rohin-singh-md","Neurosurgery resident at University of Rochester/Strong Memorial Hospital; Mayo Clinic Class of 2023","found","confirmed",1,None),
("102:ste:susa",4,"University of Rochester","stephen-susa-md","Resident Physician, Rochester NY; MD University of Rochester SMD Class of 2023 (no residency line shown)","found","confirmed",1,None),
("102:kar:ortiz",3,"Ponce Health Sciences University",None,None,"not_found","confirmed",3,None),
("102:kes:sharma",3,"University of Rochester (MSTP)","keshov-sharma-md","Listed Rochester NY; MD University of Rochester SMD Class of 2024; specialty shown as Other MD/DO, no residency line","found","confirmed",1,None),
("102:huy:dang",2,"Baylor College of Medicine","huy-dang-md-0ecd7516","Huy Dang MD, Houston TX; Baylor College of Medicine Class of 2025 (no residency listed; same-name profiles exist, this one matches roster medical school)","found","probable",2,None),
("102:saj:akkipeddi",2,"University of Rochester SMD","sajal-medha-akkipeddi-md","Rochester NY; MD University of Rochester SMD Class of 2025 (no residency line)","found","confirmed",2,None),
("102:ibr:jalal",1,"University of Rochester",None,None,"not_found","probable",2,None),
("102:mar:green",1,"Brody School of Medicine at East Carolina University",None,None,"not_found","probable",2,None),
]
out=[]
byk={p['key']:p for p in inp}
extra={
"102:tay:furst":[s("https://doctor.webmd.com/doctor/taylor-furst-8a5e1b9c-bfa2-44f4-be0f-b1e14316337a-overview","search_snippet","completed his residency in Neurological Surgery at University of Rochester Medical Center from 2020-2027; MD SUNY Upstate 2020")],
"102:der:george":[s(R,"search_snippet","Derek D. George is a PGY-6 resident in neurosurgery ... University of Colorado School of Medicine (older roster version)")],
"102:roh:singh":[s("https://health.usnews.com/doctors/rohin-singh-3294689","search_snippet","US News URL surfaced in search; not opened (US News paused)")],
"102:kar:ortiz":[s("https://www.urmc.rochester.edu/education/graduate-medical-education/prospective-residents/neurosurgery/our-residents/resident-perspectives","program_page","Search result text: Pellot Ortiz MD Ponce Health Sciences University, matched to URMC Neurosurgery on Match Day 2024")],
"102:kes:sharma":[s("https://keshovsharma.com/","search_snippet","MD/PhD trainee at University of Rochester who matched at the Neurosurgery Residency Program")],
"102:huy:dang":[s("https://www.linkedin.com/in/huy-dang-75174ab6/","search_snippet","Huy Dang - Neurosurgery Resident Physician (University of Rochester)")],
"102:saj:akkipeddi":[s("https://www.instagram.com/p/DLn9juOpBaa/","search_snippet","Say hello to Dr. Sajal Akkipeddi and Dr. Huy Dang, our ... (URMC neurosurgery incoming interns)")],
"102:ibr:jalal":[s("https://www.urmc.rochester.edu/labs/stone-lab/lab-members","program_page","Stone Lab member Ibrahim Jalal, University of Rochester medical student; doximity search found no profile")],
"102:mar:green":[s("https://www.urmc.rochester.edu/education/graduate-medical-education/prospective-residents/neurosurgery/our-residents","program_page","Roster only; Google and doximity searches found no independent profile")],
}
for key,pgy,school,slug,ev,dox,ident,ns,endy in rocs:
    pr=byk[key]
    src=[s(R,"program_page",f"Current URochester neurosurgery roster lists {pr['name']} as PGY-{pgy}; medical school {school}")]
    if slug: src.append(s(D+slug,"doximity",ev))
    src+=extra.get(key,[])
    ident_basis=f"URochester neurosurgery roster (PGY-{pgy}, {school})"+ ("; Doximity profile agrees" if slug else "; no independent profile found") 
    rs=[{"institution":"University of Rochester Medical Center","specialty":"neurosurgery","start":pr['entry_year'],"end":endy}] if endy else [{"institution":"University of Rochester Medical Center","specialty":"neurosurgery","start":pr['entry_year'],"end":None}]
    out.append(dict(key=key,name=pr['name'],program_id=pr['program_id'],identity=ident,identity_basis=ident_basis,residency_stated=rs,outcome="in_training",
      outcome_detail=f"Currently PGY-{pgy} on the URochester neurosurgery resident roster (2026-27)"+(f"; Doximity lists residency 2{endy-7 if False else ''}" if False else ""),
      year_left=None,destination_program=None,destination_start_year=None,current=f"PGY-{pgy} neurosurgery resident, University of Rochester",agrees_with_db=True,disagreement="",
      checks={"google":"found","doximity":dox,"usnews":"deferred"},abns_certified=False,sources=src,searches_used=ns))
# USF
usf=[
("103:sco:raffa","confirmed",2018,"Scott Raffa, MD MBA, neurosurgeon, Paley Orthopedic & Spine Institute, West Palm Beach/Mangonia Park FL",True,2011,"scott-raffa-md","Residency, Neurological Surgery, USF Morsani 2011 - 2018; Fellowship Neurosurgical Spine Surgery Univ of Miami 2018-2019; ABNS certified; MD USF 2011","found",1,"Class of 2018: Scott J. Raffa, MD, MBA - Spine Fellow (2018-2019), Miller School of Medicine; Memorial Healthcare System"),
("103:ste:reintjes","confirmed",2018,"Stephen L. Reintjes Jr., MD, neurosurgeon, North Kansas City Hospital / Gladstone MO",True,2011,"stephen-reintjes-md-03bb3fd4","Residency, Neurological Surgery, USF Morsani 2011 - 2018; UMKC MD 2011; ABNS listed (this is the Jr. profile; the separate stephen-reintjes-md profile is Sr., KU residency 1984-89, different person)","found",2,"Class of 2018: Stephen L. Reintjes, Jr., MD - North Kansas City Hospital"),
("103:and:vivas","confirmed",2019,"Andrew Vivas, MD, Assistant Professor of Neurosurgery, UCLA (Valencia CA)",True,2012,"andrew-vivas-md","Residency, Neurological Surgery, USF Morsani 2012 - 2019; MD USF 2012; ABNS listed; fellowships Shriners Philadelphia, USF epilepsy, Columbia spine","found",1,"Class of 2019: Andrew Vivas, MD - Adult & Pediatric Complex Spinal Deformity Fellow, Columbia University"),
("103:jas:paluzzi","confirmed",2019,"Jason Paluzzi, MD, Assistant Professor, USF Health / James A. Haley VA, Tampa FL",True,2012,"jason-paluzzi-md","Residency, Neurological Surgery, USF Morsani 2012 - 2019; Wake Forest MD 2012; ABNS listed","found",1,"Class of 2019: Jason Paluzzi, MD - Assistant Professor, USF Health; James A. Haley Veterans' Hospital"),
("103:ale:haas","confirmed",2020,"Alexander Haas, MD, Assistant Professor, USF Health / James A. Haley VA, Tampa FL",True,2013,"alexander-haas-md-3df917fb","Residency, Neurological Surgery, USF Morsani 2013 - 2020; Univ of Illinois MD 2013; ABNS listed","found",1,"Class of 2020: Alex Haas, MD - Assistant Professor, USF Health; James A. Haley Veterans' Hospital"),
("103:mel:martinez-sosa","confirmed",2020,"Meleine Martinez-Sosa, MD, pediatric neurosurgeon, Rutherford NJ (Hackensack Meridian / RWJBarnabas)",True,2013,"meleine-martinez-sosa-md","Doximity: Univ of Michigan Medical School Class of 2013; ABNS listed (no residency line shown); pediatric neurosurgeon","found",1,"Class of 2020: Meleine Martinez-Sosa, MD - Johns Hopkins All Children's Hospital Pediatric Neurosurgery Fellow"),
("103:bro:osburn","confirmed",2021,"Brooks Osburn, MD, neurosurgeon, Florida Orthopaedic Institute / AdventHealth Tampa, Temple Terrace FL",True,2014,"brooks-osburn-md","UMKC MD Class of 2014; ABNS listed (no residency line shown); FL license 2021-2027","found",2,"Class of 2021: Brooks Osburn, MD - Florida Orthopedic Institute"),
("103:sar:hartnett","confirmed",2021,"Sara Hartnett(-Wright), MD, pediatric neurosurgeon, Johns Hopkins All Children's Hospital, St. Petersburg FL; USF Assistant Professor",True,2014,"sara-hartnett-md","Residency, Neurological Surgery, USF Morsani 2014 - 2021; Fellowship Cincinnati 2021-2022; UT Health San Antonio MD 2014; ABNS listed","found",1,"Class of 2021: Sara Hartnett-Wright, MD - Assistant Professor, USF Health; Johns Hopkins All Children's Hospital"),
("103:cla:bauer","confirmed",2022,"Clayton Bauer, MD PhD, neurosurgeon (spine), Orthopaedic Medical Group of Tampa Bay, Lithia FL",True,2015,"clayton-bauer-md","VCU MD Class of 2015; ABNS listed (no residency line shown); FL license 2022-2028","found",1,"Class of 2022: Clayton Bauer, MD, PhD - Orthopaedic Medical Group of Tampa Bay"),
("103:pau:krafft","confirmed",2022,"Paul Krafft, MD, neurosurgeon, UF Health / Halifax Health, Daytona Beach FL",True,2015,"paul-krafft-md","Goethe Univ Frankfurt MD 2009; ABNS listed (no residency line shown); Google bio: completed residency in neurosurgery ... at the University of South Florida","found",1,"Class of 2022: Paul Krafft, MD - University of Florida - Halifax Health"),
("103:tra:dailey","confirmed",2022,"Travis Dailey, MD, neurosurgeon, AdventHealth Tampa",None,2015,"travis-dailey-md","USF Morsani MD Class of 2015; no residency or ABNS line on Doximity (specialty listed Other MD/DO); AdventHealth bio names USF neurosurgery residency","found",2,"Class of 2022: Travis Dailey, MD - Advent Health - Tampa"),
]
for key,ident,endy,cur,abns,starty,slug,ev,dox,ns,alum in usf:
    pr=byk[key]
    src=[s(USF,"program_page",alum),s(D+slug,"doximity",ev)]
    if key=="103:pau:krafft":
        src.append(s("https://ufhealth.org/doctors/paul-krafft","bio","Dr. Krafft completed a residency in neurosurgery and an enfolded fellowship in complex spine surgery at the University of South Florida"))
    if key=="103:tra:dailey":
        src.append(s("https://www.adventhealth.com/doctors/travis-dailey-md-1629462734","bio","completed his medical degree at USF Morsani ... residency at University of South Florida Health Department of Neurosurgery (search snippet)"))
    if key=="103:mel:martinez-sosa":
        src.append(s("https://www.atlantichealth.org/find-a-doctor/meleine-martinez-sosa-1801157441","bio","completed neurosurgery residency at the University of South Florida in Tampa (search snippet)"))
    if key=="103:bro:osburn":
        src.append(s("https://www.adventhealth.com/find-doctor/doctor/brooks-osburn-md-1932527298","bio","completed his residency in Neurological Surgery at the University of South Florida (search snippet)"))
    if key=="103:cla:bauer":
        src.append(s("https://www.floridamedicalclinic.com/doctors/clayton-bauer-md-phd-faans/","bio","completed his neurosurgery residency at the University of South Florida (search snippet)"))
    if key=="103:ale:haas":
        src.append(s("https://health.usf.edu/medicine/neurosurgery/faculty/ahaas1","bio","Residency: Neurological Surgery, University of South Florida Morsani College of Medicine, 2020"))
    if key=="103:ste:reintjes":
        src.append(s("https://www.nkchealth.org/provider/stephen-l-reintjes-jr-neurosurgery","bio","Residency: University Of South Florida (2018); Fellowship Swedish Neuroscience Institute (2016); ABNS"))
    if key=="103:and:vivas":
        src.append(s("https://www.uclahealth.org/providers/andrew-vivas","bio","Residency: Neurological Surgery, University of South Florida College of Medicine, 2019; ABNS 2023"))
    if key=="103:sco:raffa": pass
    rs=[{"institution":"University of South Florida Morsani","specialty":"neurosurgery","start":starty,"end":endy}]
    out.append(dict(key=key,name=pr['name'],program_id=pr['program_id'],identity=ident,
      identity_basis=f"USF neurosurgery alumni page lists graduation year {endy}; Doximity/bio names same USF residency and neurosurgeon practice",
      residency_stated=rs,outcome="completed",
      outcome_detail=f"Completed USF neurosurgery residency ({endy}); practising neurosurgeon",
      year_left=None,destination_program=None,destination_start_year=None,current=cur,agrees_with_db=True,disagreement="",
      checks={"google":"found","doximity":dox if dox else "found","usnews":"deferred"},abns_certified=(False if key=="103:tra:dailey" else True) if key!="103:tra:dailey" else None,
      sources=src,searches_used=ns))
# fix specifics
for o in out:
    if o['key']=="103:tra:dailey": o['abns_certified']=None
    if o['key']=="103:pau:krafft":
        o['outcome_detail']="Completed USF neurosurgery residency (2022); transferred into USF in 2017 from Loma Linda per DB notes (not re-verified here); practising neurosurgeon"
        o['residency_stated'][0]['start']=2017
    if o['key'] in ("103:sco:raffa","103:ste:reintjes","103:and:vivas","103:jas:paluzzi","103:ale:haas","103:sar:hartnett"):
        pass
    if o['key']=="103:ale:haas": o['identity_basis']+="; input flagged ambiguous name but USF faculty page (MD Illinois 2013, USF residency 2020) matches"
    if o['key']=="102:huy:dang": o['identity_basis']+="; input flagged ambiguous name, several unrelated Huy Dang profiles exist, only Baylor Class of 2025 profile matches"
    if o['key']=="102:roh:singh": o['identity_basis']+="; Doximity says neurosurgery resident at Univ of Rochester/Strong Memorial, Mayo 2023 MD (unambiguous)"
    if o['key']=="102:mar:green": o['identity_basis']="URochester neurosurgery roster only (PGY-1, Brody/ECU); no independent profile found, common name"
for o in out:
    if o['key'].startswith('102') : o['abns_certified']=False
json.dump(out,open('batch_129_out.json','w'),indent=1)
from collections import Counter
print(len(out),Counter(o['outcome'] for o in out),Counter(o['identity'] for o in out),Counter(o['checks']['doximity'] for o in out),sum(o['searches_used'] for o in out))
