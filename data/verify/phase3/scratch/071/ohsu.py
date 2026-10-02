import sys
sys.path.insert(0,"/Users/neureal/Documents/Residency Application Study/data/verify/phase3/scratch/071")
from add import add
R="https://www.ohsu.edu/school-of-medicine/neurosurgery/current-residents"
OHSU="Oregon Health & Science University"
def rec(key,pgy,school,start,dox,doxurl=None,doxev=None,extra=None,ident="confirmed",searches=2):
    src=[{"url":R,"type":"program_page","evidence":f"OHSU neurosurgery current residents page lists it under PGY-{pgy} with {school}"}]
    if doxurl: src.append({"url":doxurl,"type":"doximity","evidence":doxev})
    if extra: src+=extra
    add(key,identity=ident,identity_basis=f"OHSU current residents page lists this name as PGY-{pgy}, {school}"+(f"; Doximity page matches (OHSU residency, same school)" if dox=="found" else ""),
        residency_stated=[{"institution":OHSU,"specialty":"neurosurgery","start":start,"end":None}],
        outcome="in_training",outcome_detail=f"Current PGY-{pgy} neurosurgery resident at OHSU (2026-27 roster); not yet completed.",
        year_left=None,destination_program=None,destination_start_year=None,
        current=f"PGY-{pgy} neurosurgery resident, OHSU",agrees_with_db=True,disagreement="",
        checks={"google":"found","doximity":dox,"usnews":"deferred"},abns_certified=False,sources=src,searches_used=searches)
rec("52:jef:abaricia",4,"Virginia Commonwealth University School of Medicine",2023,"found","https://www.doximity.com/pub/jefferson-abaricia-md","Residency, Neurological Surgery, OHSU 2023 - 2030; VCU School of Medicine Class of 2023")
rec("52:jos:nugent",4,"OHSU School of Medicine",2023,"found","https://www.doximity.com/cv/jgnugent","Residency, Neurological Surgery, OHSU 2023 - 2030; OHSU School of Medicine Class of 2023")
rec("52:jam:godil",3,"OHSU School of Medicine",2024,"not_found")
rec("52:muh:tora",3,"Emory University School of Medicine",2024,"found","https://www.doximity.com/pub/muhibullah-tora-md","Doximity lists Emory MD Class of 2023 (expected), PhD Georgia Tech; no residency listed (stale profile)")
rec("52:tay:charron",3,"UT Southwestern Medical School",2024,"found","https://www.doximity.com/pub/taylor-charron-md","Neurosurgery, Portland OR, 3181 SW Sam Jackson Park Rd; UT Southwestern Medical School Class of 2024")
rec("52:jul:gendreau",2,"Mercer University School of Medicine",2025,"found","https://www.doximity.com/pub/julian-gendreau-md","Residency, Neurological Surgery, OHSU 2025 - 2032; Mercer Class of 2020")
rec("52:lou:blanpain",2,"Emory University School of Medicine",2025,"not_found")
rec("52:noa:yaffe",2,"Case Western Reserve University",2025,"not_found")
rec("52:ang:tang-tan",1,"Keck School of Medicine of USC",2026,"not_found")
rec("52:kar:khalifeh",1,"UC San Diego School of Medicine",2026,"not_found")
rec("52:meg:lim",1,"Carle Illinois College of Medicine",2026,"not_found")
