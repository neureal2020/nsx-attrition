from add import add
US={"google":"found","doximity":"found","usnews":"deferred"}
add("77:tej:karnati",identity="confirmed",identity_basis="Search snippet: Pitt MD 2017, neurosurgery residency UC Davis (2024) + spine fellowship; Doximity Pitt 2017, co-author with UC Davis residents",
 residency_stated=[{"institution":"UC Davis Health","specialty":"neurosurgery","start":2017,"end":2024}],outcome="completed",outcome_detail="Completed UC Davis neurosurgery 2024, complex spine fellowship UC Davis 2024; now practising spine neurosurgeon",
 current="Neurosurgeon (spine), Baylor Scott & White, Dallas TX",agrees_with_db=True,disagreement="",checks=US,
 sources=[{"url":"https://www.doximity.com/pub/tejas-karnati-md","type":"doximity","evidence":"Neurosurgery Dallas TX; University of Pittsburgh School of Medicine Class of 2017"},
 {"url":"https://www.bswhealth.com/physician/tejas-karnati","type":"search_snippet","evidence":"Residency in Neurological Surgery at UC Davis (2024), Fellowship in Complex and Minimally Invasive Spine Surgery at UC Davis (2024)"}],searches_used=1)
add("77:cla:gerndt",identity="confirmed",identity_basis="Doximity: UC Davis Health Neurological Surgery residency 2018-2025, Medical College of Wisconsin 2018",
 residency_stated=[{"institution":"UC Davis Health","specialty":"neurosurgery","start":2018,"end":2025}],outcome="completed",outcome_detail="Residency 2018-2025 then endovascular neurosurgery fellowship UC Davis 2024-2025; listed as neurosurgeon at UC Davis",
 current="Neurosurgeon (cerebrovascular/endovascular), UC Davis, Sacramento CA",agrees_with_db=True,disagreement="",checks=US,
 sources=[{"url":"https://www.doximity.com/pub/clayton-gerndt-md","type":"doximity","evidence":"University of California Davis Health Residency, Neurological Surgery, 2018 - 2025; Neurosurgery Sacramento"}],searches_used=1)
add("77:kri:nosova",identity="confirmed",identity_basis="Doximity Louisville MD 2018, Phoenix AZ (1111 E McDowell = Banner UMC); UA Phoenix pages name Nosova, residency Banner-UMC Phoenix; ResearchGate Louisville",
 residency_stated=[{"institution":"Banner - University Medical Center Phoenix","specialty":"neurosurgery","start":None,"end":None}],outcome="transferred",
 outcome_detail="Now neurosurgery resident at Banner-University Medical Center Phoenix (UA College of Medicine-Phoenix) per search snippet; joining Pilitsis stereotactic/functional fellowship. Start year at Banner not stated (DB says after UC Davis 2021-22).",
 year_left=2022,destination_program="Banner - University Medical Center Phoenix (Univ of Arizona-Phoenix)",destination_start_year=2022,current="Neurosurgery resident / incoming functional neurosurgery fellow, Banner-UMC Phoenix",agrees_with_db=True,disagreement="",checks=US,
 sources=[{"url":"https://www.doximity.com/pub/kristin-nosova-md","type":"doximity","evidence":"Phoenix AZ; University of Louisville School of Medicine Class of 2018; AZ license 2022-2028"},
 {"url":"https://phoenixmed.arizona.edu/newsroom/news/neurosurgery-department-research-hub-innovating-care","type":"search_snippet","evidence":"Kristin Nosova, MD (Residency-Banner-University Medical Center Phoenix) will be joining Dr. Pilitsis' Stereotactic and Functional Neurosurgery Fellowship Program"}],searches_used=1)
add("77:fre:beato",identity="confirmed",identity_basis="WebMD: UPR MD 2019, UC Davis Medical Center affiliation; UC Davis news Apr 2026 calls him UC Davis neurosurgery resident",
 residency_stated=[{"institution":"UC Davis Health","specialty":"neurosurgery","start":2021,"end":None}],outcome="in_training",
 outcome_detail="UC Davis news (Apr 2026) describes him as a UC Davis neurosurgery resident; DB shows PGY-7 in 2025-26 (terminal); graduation not directly confirmed. WebMD lists Neurological Surgery specialty. Transfer-in from UPR per DB not independently confirmed.",
 current="UC Davis neurosurgery resident (as of Apr 2026)",agrees_with_db=True,disagreement="DB says COMPLETED; sources only show resident status as of Apr 2026, graduation not confirmed",
 checks={"google":"found","doximity":"not_found","usnews":"deferred"},
 sources=[{"url":"https://health.ucdavis.edu/news/headlines/comprehensive-guidance-on-surgical-management-of-ossified-posterior-longitudinal-ligament/2026/04","type":"news","evidence":"a UC Davis neurosurgery resident and the first author of the review"},
 {"url":"https://doctor.webmd.com/doctor/freddie-rodriguez-beato-5ceedc60-8f7f-4170-9e58-6cf18772a9af-overview","type":"bio","evidence":"Graduated from University Of Puerto Rico School Of Medicine in 2019; Neurological Surgery; UC Davis Medical Center"}],searches_used=2)
