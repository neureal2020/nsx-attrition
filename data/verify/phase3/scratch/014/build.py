import json
base="scratch/014/"
p1=json.load(open(base+'p1.json')); p2=json.load(open(base+'p2.json'))
inp=json.load(open('batch_014_in.json'))
CW="Case Western Reserve University/University Hospitals Cleveland Medical Center"
def rs(s,e): return [{"institution":CW,"specialty":"neurosurgery","start":s,"end":e}]
def ent(key,name,identity,basis,res,outcome,detail,current,checks,abns,sources,n,agrees=True,dis="",yl=None,dest=None,dsy=None):
    return {"key":key,"name":name,"program_id":10,"identity":identity,"identity_basis":basis,"residency_stated":res,"outcome":outcome,"outcome_detail":detail,"year_left":yl,"destination_program":dest,"destination_start_year":dsy,"current":current,"agrees_with_db":agrees,"disagreement":dis,"checks":checks,"abns_certified":abns,"sources":sources,"searches_used":n}
for e in p2:
    if e['key']=='10:jon:pace':
        e['abns_certified']=True
        e['sources'].append({"url":"https://physicians.lahey.org/details/4928/jonathan-pace-neurosurgery-burlington","type":"bio","evidence":"Lahey profile: Residency and Fellowship Case Western Reserve University School of Medicine; Board Certification Neurological Surgery; MD Medical College of Wisconsin 2013"})
        e['identity']='confirmed'
        e['identity_basis']='Lahey bio: MD Medical College of Wisconsin 2013, internship/residency/fellowship CWRU School of Medicine, board certified Neurological Surgery; CWRU resident page; no Doximity/US News profile found'
        e['searches_used']=4
new=[]
new.append(ent("9:pet:drossopoulos","Peter Drossopoulos","probable","Atrium Health Neurological Surgery residents page lists Peter Drossopoulos as PGY-1, UNC School of Medicine; no Doximity/US News profile found",
 [{"institution":"Atrium Health Carolinas Medical Center","specialty":"neurosurgery","start":2025,"end":None}],"in_training","PGY-1 in Carolinas Medical Center neurosurgery residency (2025-26); listed on the program residents page. (Web search snippets attributing Duke awards to a 'Peter Drossopoulos' were not used: likely a namesake/unreliable.)","neurosurgery resident PGY-1, Atrium Health Carolinas Medical Center, Charlotte NC",
 {"google":"found","doximity":"not_found","usnews":"not_found"},None,
 [{"url":"https://atriumhealth.org/education/graduate-medical-education/physician-residencies/neurological-surgery/residents","type":"program_page","evidence":"Peter Drossopoulos, PGY-1, UNC School of Medicine (WebFetch summary)"}],4))
new.append(ent("10:xia:zhou","Xiaofei Zhou","confirmed","UH bio: MD CWRU 2016, neurological surgery residency UH Cleveland Medical Center 2016-2023, ABNS; CWRU resident page 'Xiaofei Sophie Zhou'; Southwest General bio",
 rs(2016,2023),"completed","Completed 2023; dual neurocritical care and spine fellowships; neurosurgeon, Southwest General/UH, Associate Program Director","neurosurgeon, UH / Southwest General Health Center, Middleburg Heights OH",
 {"google":"found","doximity":"not_found","usnews":"not_found"},True,
 [{"url":"https://www.uhhospitals.org/doctors/zhou-xiaofei-1558724898","type":"bio","evidence":"Residency UH Cleveland Medical Center (2016 - 2023); Neurological Surgery - American Board of Neurological Surgery"},{"url":"https://case.edu/medicine/neurosurgery/meet-our-team/current-residents/xiaofei-sophie-zhou-md","type":"program_page","evidence":"CWRU resident page Xiaofei Sophie Zhou, M.D."}],3))
new.append(ent("10:aub:mcmillan","Aubrey McMillan","confirmed","Doximity/US News list Aubrey (Claire) McMillan, MD Boston University 2017, radiology; Cleveland Clinic bio lists internship CWRU/UH 2018 and radiology residency CWRU (MetroHealth) 2022; CWRU neurosurgery resident page exists",
 [{"institution":"Case Western Reserve University/University Hospitals Case Medical Center (internship / neurosurgery PGY1)","specialty":"neurosurgery","start":2017,"end":2018},{"institution":"Case Western Reserve University (MetroHealth) Program","specialty":"diagnostic radiology","start":2018,"end":2022}],"switched_specialty",
 "Left neurosurgery after PGY1 (2017-18) and switched to diagnostic radiology (MetroHealth/CWRU, residency completed 2022), then neuroradiology fellowship Mass General (2024)","neuroradiologist, Cleveland Clinic (also Mass General affiliation)",
 {"google":"found","doximity":"found","usnews":"found"},None,
 [{"url":"https://providers.clevelandclinic.org/provider/aubrey-mc-millan/4271566","type":"bio","evidence":"Internship: CWRU/UH Case Medical Center 2018; Residency: CWRU (MetroHealth) Program 2022; Fellowship: Mass General/Harvard 2024; ABR Diagnostic Radiology 2023"},{"url":"https://www.doximity.com/pub/aubrey-mcmillan-md","type":"doximity","evidence":"Radiology, Cleveland OH; Boston University School of Medicine Class of 2017; American Board of Radiology"},{"url":"https://health.usnews.com/doctors/aubrey-mcmillan-1189681","type":"usnews","evidence":"Radiology / Neuroradiology, Cleveland Clinic and Mass General; BU School of Medicine"}],2,yl=2018,dest="Case Western Reserve (MetroHealth) Diagnostic Radiology",dsy=2018))
new.append(ent("10:moh:patel","Mohit Patel","confirmed","Doximity/US News: Residency Neurological Surgery CWRU/UH 2017-2024, MD Medical College of Wisconsin 2017; UH bio (chief resident, spine fellowships)",
 rs(2017,2024),"completed","Completed 2024; complex spine fellowship UH and deformity fellowship Johns Hopkins (Baltimore); now UH Spine Center faculty per search snippet","spine neurosurgeon (Johns Hopkins fellowship, Baltimore MD; UH Spine Center faculty per bio)",
 {"google":"found","doximity":"found","usnews":"found"},None,
 [{"url":"https://www.doximity.com/pub/mohit-patel-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2017 - 2024 (CWRU/UH); Medical College of Wisconsin Class of 2017"},{"url":"https://health.usnews.com/doctors/mohit-patel-1182638","type":"usnews","evidence":"Residency, Neurological Surgery, 2017-2024"},{"url":"https://www.uhhospitals.org/doctors/Patel-Mohit-1285166041","type":"bio","evidence":"search result: UH doctor profile Mohit Patel MD (spine and scoliosis neurosurgeon)"}],2))
new.append(ent("10:aru:chugh","Arunit Chugh","confirmed","Doximity/US News (A. Jessey Chugh): Residency CWRU/UH 2016-2023, MD CWRU 2016, ABNS; neurotucson bio",
 rs(2016,2023),"completed","Completed 2023; cerebrovascular/skull base fellowship UH 2021-22; Director of Neurovascular Surgery, Tucson","neurosurgeon, Center for Neurosciences / Tucson Medical Center, Tucson AZ",
 {"google":"found","doximity":"found","usnews":"found"},True,
 [{"url":"https://www.doximity.com/pub/a-jessey-chugh-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2016 - 2023; American Board of Neurological Surgery"},{"url":"https://health.usnews.com/doctors/a-jessey-chugh-2672856","type":"usnews","evidence":"Residency, Neurological Surgery, 2016-2023"},{"url":"https://neurotucson.com/bio/arunit-jessey-chugh-md/","type":"bio","evidence":"Arunit (Jessey) Chugh, MD | Center for Neurosciences"}],3))
new.append(ent("10:roh:mauria","Rohit Mauria","confirmed","US News: Residency CWRU/UH 2018-2025, MD Creighton; residency co-authors are CWRU residents; Emory/Novant bios",
 rs(2018,2025),"completed","Completed 2025; spine fellowship Emory; complex spine neurosurgeon Novant Health Spine, Charlotte NC (US News lists Charlotte NC)","complex spine neurosurgeon, Novant Health, Charlotte NC (Emory spine fellowship)",
 {"google":"found","doximity":"not_found","usnews":"found"},None,
 [{"url":"https://health.usnews.com/doctors/rohit-mauria-3045954","type":"usnews","evidence":"Residency, Neurological Surgery, 2018-2025 (CWRU/UH); Creighton University School of Medicine"},{"url":"https://www.novanthealth.org/pf/providers/1144724121/rohit-mauria","type":"bio","evidence":"search result: Rohit Mauria, MD | Neurological Surgery | Novant Health"}],3))
new.append(ent("10:col:labak","Collin Labak","confirmed","Doximity: Residency Neurological Surgery CWRU/UH 2019-2026, MD Univ of Illinois 2019; IL license 2026-2029 (Chicago address) indicating post-residency move",
 rs(2019,2026),"completed","Residency 2019-2026 per Doximity (finished; now Chicago-based, likely fellowship per IL licence 2026-2029, not confirmed)","Chicago IL (post-residency; role not stated)",
 {"google":"found","doximity":"found","usnews":"not_found"},None,
 [{"url":"https://www.doximity.com/pub/collin-labak-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2019 - 2026; IL State Medical License 2026 - 2029; Neurosurgical Spine Surgery"}],3))
new.append(ent("10:dan:defta","Dana Defta","confirmed","Doximity: Residency CWRU/UH 2019-2026, MD Wright State 2019; Neenah WI neurosurgery practice",
 rs(2019,2026),"completed","Completed 2026; WI licence 2026-2027, Doximity lists neurosurgery practice Neenah WI","neurosurgeon, Neenah WI (Doximity)",
 {"google":"found","doximity":"found","usnews":"not_found"},None,
 [{"url":"https://www.doximity.com/pub/dana-defta-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2019 - 2026; Wright State Class of 2019; Neurosurgery, Neenah WI"}],3))
new.append(ent("10:eri:herring","Eric Herring","confirmed","Doximity: Residency CWRU/UH 2019-2026, MD CWRU 2019; co-author with CWRU residents",
 rs(2019,2026),"completed","Completed 2026; Doximity lists neurosurgery Phoenix AZ (AZ licence 2026-2027), likely fellowship","Phoenix AZ, neurosurgery (fellowship likely; not stated)",
 {"google":"found","doximity":"found","usnews":"blocked"},None,
 [{"url":"https://www.doximity.com/pub/eric-herring-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2019 - 2026; AZ State Medical License 2026 - 2027"}],2))
new.append(ent("10:oli:wijesekera","Olindi Wijesekera","confirmed","Doximity/UW bio: Residency CWRU/UH 2019-2026, MD Boston University 2019; UW spine fellow",
 rs(2019,2026),"completed","Completed 2026; clinical fellow in Endoscopic and Complex Spine at University of Washington (Seattle)","spine fellow, University of Washington, Seattle WA",
 {"google":"found","doximity":"found","usnews":"blocked"},None,
 [{"url":"https://www.doximity.com/pub/olindi-wijesekera-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2019 - 2026; Boston University Class of 2019; Seattle WA"},{"url":"https://neurosurgery.uw.edu/bio/olindi-wijesekera-md-ms","type":"bio","evidence":"search result: Olindi Wijesekera, MD, MS | UW Department of Neurological Surgery (spine fellow)"}],3))
new.append(ent("10:qua:nguyen","Quang Nguyen","probable","UH neurosurgery residents page lists Quang Nguyen PGY-7, Texas Tech HSC School of Medicine; WebMD/Vitals list Quang Nguyen neurosurgery, Cleveland, MD Texas Tech 2020; no Doximity/US News neurosurgery profile found (other-specialty namesakes only)",
 rs(2020,None),"in_training","PGY-7 senior resident, CWRU/UH neurosurgery (entered 2020)","neurosurgery resident PGY-7, University Hospitals Cleveland",
 {"google":"found","doximity":"not_found","usnews":"not_found"},None,
 [{"url":"https://www.uhhospitals.org/medical-education/neurological-surgery-medical-education/neurological-surgery-residency/residents","type":"program_page","evidence":"Quang Nguyen, PGY 7, Texas Tech University Health Sciences Center School of Medicine (WebFetch summary)"}],3))
new.append(ent("10:seb:norrdahl","Sebastian Norrdahl","confirmed","Doximity: Residency CWRU/UH 2020-2027, MD Univ of Tennessee HSC 2020; UH residents page PGY-7",
 rs(2020,2027),"in_training","PGY-7 resident, expected completion 2027","neurosurgery resident PGY-7, University Hospitals Cleveland",
 {"google":"found","doximity":"found","usnews":"not_found"},None,
 [{"url":"https://www.doximity.com/pub/sebastian-norrdahl-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2020 - 2027; Resident Physician"},{"url":"https://www.uhhospitals.org/medical-education/neurological-surgery-medical-education/neurological-surgery-residency/residents","type":"program_page","evidence":"Sebastian Norrdahl, PGY 7 (WebFetch summary)"}],3))
allp={e['key']:e for e in p1+p2+new}
out=[]
for p in inp:
    e=allp[p['key']]; e['program_id']=p['program_id']; e['name']=p['name']; out.append(e)
assert len(out)==25
json.dump(out,open('batch_014_out.json','w'),indent=1)
from collections import Counter
print(Counter(e['outcome'] for e in out),Counter(e['identity'] for e in out))
for s in ('doximity','usnews'): print(s,Counter(e['checks'][s] for e in out))
print(sum(e['searches_used'] for e in out))
print([e['name'] for e in out if not e['agrees_with_db']])
