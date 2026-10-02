from add import add
G={"google":"found","doximity":"found","usnews":"deferred"}
N={"google":"found","doximity":"not_found","usnews":"deferred"}
add("77:jar:clouse",identity="confirmed",identity_basis="Doximity: Indiana Univ SOM 2019, Sacramento 4860 Y St (UC Davis Neurosurgery); Miami fellows page says neurosurgery residency at UC Davis",
 residency_stated=[{"institution":"UC Davis Health","specialty":"neurosurgery","start":2019,"end":2026}],outcome="completed",
 outcome_detail="Completed UC Davis neurosurgery residency (with enfolded skull base fellowship); Neuro-Oncology Fellow at Univ of Miami 07/2026-06/2027",
 current="Neuro-oncology fellow, Univ of Miami Dept of Neurological Surgery (2026-27)",agrees_with_db=True,disagreement="",checks=G,
 sources=[{"url":"https://med.miami.edu/departments/neurosurgery/education/clinical-fellowship-programs/current-fellows","type":"program_page","evidence":"During his residency he completed an enfolded skull base fellowship at UC Davis"},
 {"url":"https://www.doximity.com/pub/jared-clouse-md","type":"doximity","evidence":"Resident Physician Sacramento CA; Indiana University School of Medicine Class of 2019; FL license 2026-2028"}],searches_used=1)
add("77:mat:kercher",identity="confirmed",identity_basis="Doximity/WebMD: Univ Nebraska MD 2019, CA license, UC Davis co-authors (Kulubya, Moskalik, Waldau) on 2022 papers; Neurosurgery Albuquerque NM 2026",
 residency_stated=[{"institution":"UC Davis Health","specialty":"neurosurgery","start":2019,"end":2026}],outcome="completed",
 outcome_detail="Listed as Neurosurgery at 2211 Lomas Blvd NE Albuquerque (UNM) with NM license 2026-27, consistent with finishing UC Davis 2026 and moving on (fellowship/faculty); residency years not stated on Doximity",
 current="Neurosurgery, Albuquerque NM (UNM address)",agrees_with_db=True,disagreement="",checks=G,
 sources=[{"url":"https://www.doximity.com/pub/matthew-kercher-md","type":"doximity","evidence":"Neurosurgery, Albuquerque NM; University of Nebraska College of Medicine Class of 2019; CA license 2022-2028; NM license 2026-2027"}],searches_used=1)
add("77:anz:moskalik",identity="confirmed",identity_basis="WebMD/ResearchGate/UC Davis news: UConn MD 2020, UC Davis neurosurgery resident, 4th-year in Nov 2023; also lists Bellevue/NYU Langone affiliations",
 residency_stated=[{"institution":"UC Davis Health","specialty":"neurosurgery","start":2021,"end":None}],outcome="in_training",
 outcome_detail="UC Davis news Jan 2024 calls her a fourth-year resident (2023-24), so class of 2020 slot; affiliated with NYU/Bellevue (possible PGY-1 there, consistent with DB transfer at PGY-2 2021-22, unconfirmed). Still in training per DB 2026-27.",
 current="Neurosurgery resident, UC Davis",agrees_with_db=True,disagreement="",checks=N,
 sources=[{"url":"https://health.ucdavis.edu/news/headlines/alum-funded-travel-and-research-award-allows-residents-to-improve-access-to-neurosurgery-care-in-bolivia/2024/01","type":"news","evidence":"fourth-year neurosurgery resident ... traveled to Bolivia (snippet summary)"},
 {"url":"https://doctor.webmd.com/doctor/anzhela-moskalik-af7687e4-9aa3-4c95-a3a7-bbd6177374f3-overview","type":"bio","evidence":"UConn School of Medicine 2020; affiliated with UC Davis Medical Center, Bellevue Hospital, NYU Tisch, NYU Langone Kimmel"}],searches_used=2)
add("77:jos:castillo",identity="confirmed",identity_basis="Doximity Resident Physician at 4860 Y St Sacramento (UC Davis Neurosurgery), VCU MD 2020; UC Davis news/LinkedIn: Jose Castillo, PGY-5 neurosurgery, from Oakland, med school in Virginia. Name is common but details match.",
 residency_stated=[{"institution":"UC Davis Health","specialty":"neurosurgery","start":2020,"end":None}],outcome="in_training",
 outcome_detail="Neurosurgery resident UC Davis (4th-year Nov 2023, PGY-5 in late 2024 posts); DB 2026-27 PGY-7",current="Neurosurgery resident, UC Davis",agrees_with_db=True,disagreement="",checks=G,
 sources=[{"url":"https://www.doximity.com/pub/jose-castillo-md-de01a7f7","type":"doximity","evidence":"Resident Physician Sacramento CA, 4860 Y St Ste 3740; Virginia Commonwealth University School of Medicine Class of 2020"},
 {"url":"https://www.linkedin.com/posts/uc-davis-department-of-neurological-surgery_pgy-5-jose-castillo-md-recently-published-activity-7258172456354361344-g4SG","type":"search_snippet","evidence":"PGY-5 Jose Castillo, MD recently published"}],searches_used=2)
add("77:ara:ghaffari-rafi",identity="confirmed",identity_basis="WebMD/vitals: neurological surgery resident, UC Davis, 4860 Y St Sacramento; Univ Hawaii; co-author with UC Davis residents (Goodrich pub)",
 residency_stated=[{"institution":"UC Davis Health","specialty":"neurosurgery","start":2021,"end":None}],outcome="in_training",
 outcome_detail="Neurological surgery resident, UC Davis (third year as of 2023-24 snippet)",current="Neurosurgery resident, UC Davis",agrees_with_db=True,disagreement="",checks=N,
 sources=[{"url":"https://doctor.webmd.com/doctor/arash-ghaffari-rafi-36d52c40-9a9b-4ccd-8eb7-824b14c298e9-overview","type":"bio","evidence":"Neurological Surgery, Sacramento CA, 4860 Y St (snippet)"}],searches_used=2)
