import sys; sys.path.insert(0,'/Users/neureal/Documents/Residency Application Study/data/verify/phase3/scratch/090')
from add import add
from b1 import E, UB
cur="https://medicine.buffalo.edu/departments/neurosurgery/education/residency/residents/current.html"
def IT(key,name,ident,basis,start,end,dox,src,ns,extra="",google="found",dis="",curr=None):
    return E(key,name,ident,basis,[{"institution":UB,"specialty":"neurosurgery","start":start,"end":end}],"in_training",
      "Listed on UB current residents page; Doximity/other sources show UB neurosurgery residency %s-%s (expected end). %s"%(start,end,extra),
      curr or "neurosurgery resident, University at Buffalo",None,dox,src,ns,google=google,dis=dis)
add([
IT("69:ash:khan","Asham Khan","confirmed","UB current residents page (PGY-6 chief, RCSI MD) and Doximity residency 2020-2027, RCSI Class of 2015",2020,2027,"found",
 [{"url":cur,"type":"program_page","evidence":"PGY-6 Asham Khan, MD (Chief) | Royal College of Surgeons in Ireland"},{"url":"https://www.doximity.com/pub/asham-khan-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2020 - 2027, University at Buffalo"}],2),
IT("69:eli:nyabuto","Elizabeth Nyabuto","confirmed","UB current residents page (PGY-6 chief, UTMB) and Doximity residency 2020-2027, UTMB Class of 2020",2020,2027,"found",
 [{"url":cur,"type":"program_page","evidence":"PGY-6 Elizabeth Nyabuto, MD (Chief) | UTMB Galveston"},{"url":"https://www.doximity.com/pub/elizabeth-nyabuto-md-556fa995","type":"doximity","evidence":"Residency, Neurological Surgery, 2020 - 2027, University at Buffalo"}],2),
IT("69:kyu:rho","Kyungduk Rho","confirmed","UB current residents page (Jacobs MD) and Doximity residency 2021-2028, Jacobs Class of 2021",2021,2028,"found",
 [{"url":cur,"type":"program_page","evidence":"PGY-5 Kyungduk Rho, MD | Jacobs School"},{"url":"https://www.doximity.com/pub/kyungduk-rho-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2021 - 2028, University at Buffalo"}],2,
 dis="DB last_pgy 6 in 2026-27; UB current page lists PGY-5 (page may lag); Doximity 2021-2028 implies 7-year track"),
IT("69:mat:moser","Matthew Moser","confirmed","UB current residents page (VCU MD) and Doximity residency 2021-2029, VCU Class of 2021",2021,2029,"found",
 [{"url":cur,"type":"program_page","evidence":"PGY-5 Matthew Moser, MD | Virginia Commonwealth"},{"url":"https://www.doximity.com/pub/matt-moser-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2021 - 2029, University at Buffalo; VCU Class of 2021"}],2,
 dis="Doximity end 2029 (incl. possible research years); DB PGY-6 vs UB page PGY-5"),
E("69:nei:almeida","Neil Almeida","probable","Roswell Park bio: radiation oncology resident, MD George Washington Univ; name and Buffalo location; phase2 note (medicine.buffalo.edu 2022-10-14 lists him as neurosurgery PGY-2, Roswell Park profile) already ties the two",
 [{"institution":UB,"specialty":"neurosurgery","start":2021,"end":2023},{"institution":"Roswell Park Cancer Institute","specialty":"radiation oncology","start":2023,"end":None}],"switched_specialty",
 "Left UB neurosurgery after PGY-2 (2022-23); now radiation oncology resident, Roswell Park Department of Radiation Medicine (PGY-5 in 2026-27, implying start 2023). Search snippet: 'received his MD from George Washington University'; interests include neuro-oncology/neurosurgery/Gamma Knife.",
 "radiation oncology resident PGY-5, Roswell Park Comprehensive Cancer Center, Buffalo NY",None,"not_found",
 [{"url":"https://www.roswellpark.org/neil-almeida","type":"program_page","evidence":"Resident Physician, PGY 5, Department of Radiation Medicine; MD - George Washington University School of Medicine"},{"url":"https://www.roswellpark.org/education/residency-programs/radiation-oncology/current-residents-alumni","type":"search_snippet","evidence":"Roswell Park Radiation Oncology current residents list"}],3,
 ),
IT("69:tan:singh","Tanya Singh","confirmed","UB current residents page (UCF MD) and Doximity: UB residency 2022-2027, Vanderbilt surgery residency 2020-2022, UCF Class of 2020",2022,2027,"found",
 [{"url":cur,"type":"program_page","evidence":"PGY-5 Tanya Singh, MD | University of Central Florida College of Medicine"},{"url":"https://www.doximity.com/pub/tanya-singh-md-3002eaee","type":"doximity","evidence":"Residency, Neurological Surgery, 2022 - 2027, University at Buffalo; Residency, Surgery, 2020 - 2022, Vanderbilt University Medical Center"}],3,
 extra="Joined UB at PGY-2 in 2022 after two years of general surgery residency at Vanderbilt (2020-2022): origin resolved as a surgery-to-neurosurgery move, not a neurosurgery transfer.",
 dis="Resolves DB 'origin unknown': came from Vanderbilt general surgery residency 2020-2022"),
IT("69:ale:fritz","Alexander Fritz","confirmed","UB current residents page (Alex Fritz, PGY-4, Jacobs MD) and Doximity/WebMD: Jacobs MD 2022, Buffalo neurological surgery; UB co-authors Monteiro, Cappuzzo, Waqas. Doximity page shows an inconsistent 'Neurology' specialty and NYP-Columbia neurology residency 2020-2023, not credible with MD 2022; disregarded.",2022,None,"found",
 [{"url":cur,"type":"program_page","evidence":"PGY-4 Alex Fritz, MD | Jacobs School of Medicine and Biomedical Sciences"},{"url":"https://www.doximity.com/pub/alexander-fritz-md","type":"doximity","evidence":"Class of 2022 Jacobs School; listing shows Neurology and Columbia residency 2020-2023 (inconsistent)"}],2),
IT("69:dev:patel","Devan Patel","confirmed","UB current residents page (FSU MD) and Doximity residency UB 2022-2029, FSU Class of 2021",2022,2029,"found",
 [{"url":cur,"type":"program_page","evidence":"PGY-4 Devan Patel, MD | Florida State University"},{"url":"https://www.doximity.com/pub/devan-patel-md-9bc97259","type":"doximity","evidence":"Residency, Neurological Surgery, 2022 - 2029, University at Buffalo; Florida State University College of Medicine Class of 2021; Long Island Jewish Residency Emergency Medicine (undated)"}],2),
IT("69:muh:waqas","Muhammad Waqas","probable","UB current residents page (PGY-4, Hamdard University Karachi) matches Hamdard MD 2010, Aga Khan neurosurgery, UNC surgery intern and UB neuroendovascular fellow bio; no Doximity profile found. Note: trained/fellow at UB earlier, so start date as neurosurgery resident is not from a source.",2022,None,"not_found",
 [{"url":cur,"type":"program_page","evidence":"PGY-4 Muhammad Waqas, MD | Hamdard University Karachi, Pakistan"},{"url":"https://www.healthgrades.com/physician/dr-muhammad-waqas-gi60wh2926","type":"search_snippet","evidence":"graduated from HAMDARD UNIVERSITY / HAMDARD COLLEGE OF MEDICINE (HCMD) in 2010 ... works with University at Buffalo Neurosurgery and Gates Vascular Institute"}],2,
 extra="Prior research/fellowship at UB (neuroendovascular fellow) and Aga Khan neurosurgery training abroad; current US neurosurgery residency at UB."),
IT("69:and:monteiro","Andre Monteiro","confirmed","UB current residents page (PGY-3, PUC Campinas) and Doximity residency UB 2023-2030, PUC Campinas Class of 2018",2023,2030,"found",
 [{"url":cur,"type":"program_page","evidence":"PGY-3 Andre Monteiro, MD | Pontificia Universidade Catolica de Campinas"},{"url":"https://www.doximity.com/pub/andre-monteiro-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2023 - 2030, University at Buffalo"}],2),
IT("69:kat:locke","Katherine Locke","confirmed","UB current residents page (Drexel MD) and Doximity residency UB 2023-2030, Drexel Class of 2023",2023,2030,"found",
 [{"url":cur,"type":"program_page","evidence":"PGY-3 Katherine Locke, MD | Drexel University College of Medicine"},{"url":"https://www.doximity.com/pub/katherine-locke-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2023 - 2030, University at Buffalo"}],2),
IT("69:ter:xia","Terry Xia","confirmed","UB current residents page (Drexel MD) and Doximity residency UB 2023-2030, Drexel Class of 2023",2023,2030,"found",
 [{"url":cur,"type":"program_page","evidence":"PGY-3 Terry Xia, MD | Drexel University College of Medicine"},{"url":"https://www.doximity.com/pub/terry-xia-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2023 - 2030, University at Buffalo"}],2),
])
d=__import__('add')
