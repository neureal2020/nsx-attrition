exec(open('scratch/144/build.py').read())
def ros(pgy,n): d=dict(ROSTER); d["evidence"]=d["evidence"]%(pgy,n); return d
add(0,identity="confirmed",identity_basis="UVA program page: Grace Garcia PGY-5, MD Univ of Kansas 2022; Doximity 'Gracie Garcia' (KU 2022, UVA Neurological Surgery 2022-2029)",
 residency_stated=[{"institution":"University of Virginia","specialty":"neurosurgery","start":2022,"end":2029}],
 outcome="unknown",outcome_detail="CONFLICT: UVA program site (2026-27 roster) lists Grace Garcia as current PGY-5 resident, and she co-authored 2026 UVA spine papers. But Doximity profile 'Gracie Garcia, Topeka KS' lists UVA Neurological Surgery 2022-2029 AND UT Southwestern Family Medicine residency 2024-2027, KS/TX licences, ABFM family medicine listed. Could not confirm on UTSW current-resident page (only classes 2028/2029 shown). Needs manual review: possible switch to family medicine in 2024.",
 year_left=None,destination_program="possibly UT Southwestern Family Medicine (unconfirmed)",destination_start_year=2024,
 current="UVA neurosurgery PGY-5 per program site; Doximity says family medicine resident UTSW/Topeka KS",
 agrees_with_db=False,disagreement="DB says IN TRAINING at UVA; Doximity suggests family medicine residency at UTSW from 2024 (unresolved conflict)",
 checks={"google":"found","doximity":"found"},abns_certified=False,
 sources=[ros(5,"Grace Garcia"),{"url":"https://www.doximity.com/pub/gracie-garcia-md","type":"doximity","evidence":"Residency, Neurological Surgery, University of Virginia Medical Center 2022-2029; Residency, Family Medicine, UT Southwestern 2024-2027; American Board of Family Medicine; KU School of Medicine Class of 2022"},{"url":UVA+"grace-garcia-md/","type":"bio","evidence":"MD University of Kansas School of Medicine 2022; listed among current UVA neurosurgery residents"}],searches_used=3)
add(1,identity="confirmed",identity_basis="Doximity and UVA page: Divine Nwafor MD PhD, WVU 2023, UVA neurosurgery resident",
 residency_stated=[{"institution":"University of Virginia","specialty":"neurosurgery","start":2023,"end":2030}],outcome="in_training",outcome_detail="PGY-4 at UVA 2026-27; Doximity residency 2023-2030",current="neurosurgery resident PGY-4, UVA",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"found"},abns_certified=False,
 sources=[ros(4,"Faraz Farzad, Divine Nwafor"),{"url":"https://www.doximity.com/pub/divine-nwafor-md","type":"doximity","evidence":"Residency, Neurological Surgery, University of Virginia Medical Center, 2023 - 2030; WVU School of Medicine Class of 2023"}],searches_used=1)
add(2,identity="confirmed",identity_basis="UVA program page PGY-4; WebMD/search: UVA School of Medicine grad 2023, UVA neurosurgery resident",
 residency_stated=[{"institution":"University of Virginia","specialty":"neurosurgery","start":2023,"end":None}],outcome="in_training",outcome_detail="PGY-4 at UVA 2026-27; med school UVA 2023; no Doximity profile found",current="neurosurgery resident PGY-4, UVA",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"not_found"},abns_certified=False,
 sources=[ros(4,"Faraz Farzad"),{"url":"https://med.virginia.edu/neurosurgery/resident-training/current-residents/faraz-farzad-md/","type":"bio","evidence":"UVA neurosurgery resident page (search snippet: PGY-4 resident, graduated UVA School of Medicine 2023)"}],searches_used=3)
add(3,identity="confirmed",identity_basis="Doximity David Loftus: UVA Neurological Surgery residency 2024-2031, Charlottesville; UVA page PGY-3",
 residency_stated=[{"institution":"University of Virginia","specialty":"neurosurgery","start":2024,"end":2031}],outcome="in_training",outcome_detail="PGY-3 at UVA 2026-27",current="neurosurgery resident PGY-3, UVA",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"found"},abns_certified=False,
 sources=[ros(3,"David Loftus"),{"url":"https://www.doximity.com/pub/david-loftus-md-96abf1fe","type":"doximity","evidence":"Residency, Neurological Surgery, University of Virginia Medical Center, 2024 - 2031"}],searches_used=1)
add(4,identity="confirmed",identity_basis="Doximity Emily Dunbar: UVA Neurological Surgery 2024-2031, VCU MD 2024; UVA page PGY-3",
 residency_stated=[{"institution":"University of Virginia","specialty":"neurosurgery","start":2024,"end":2031}],outcome="in_training",outcome_detail="PGY-3 at UVA 2026-27",current="neurosurgery resident PGY-3, UVA",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"found"},abns_certified=False,
 sources=[ros(3,"Emily Dunbar"),{"url":"https://www.doximity.com/pub/emily-dunbar-md","type":"doximity","evidence":"PGY1 UVA Health; Residency, Neurological Surgery, UVA 2024 - 2031; VCU School of Medicine Class of 2024"}],searches_used=2)
add(5,identity="confirmed",identity_basis="Doximity Nicholas Cassimatis: UVA neurosurgery resident, Hackensack-Meridian/Seton Hall MD 2024; UVA page PGY-3",
 residency_stated=[{"institution":"University of Virginia","specialty":"neurosurgery","start":2024,"end":2031}],outcome="in_training",outcome_detail="PGY-3 at UVA 2026-27",current="neurosurgery resident PGY-3, UVA",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"found"},abns_certified=False,
 sources=[ros(3,"Nicholas Cassimatis"),{"url":"https://www.doximity.com/pub/nicholas-cassimatis-md","type":"doximity","evidence":"Residency, Neurological Surgery, University of Virginia Medical Center, 2024 - 2031"}],searches_used=1)
add(6,identity="confirmed",identity_basis="UVA page PGY-2; Google: Georgios Mantziaris MD (Athens MD 2014, Greek neurosurgery training, UVA research/clinical fellow 2021-25)",
 residency_stated=[{"institution":"University of Virginia","specialty":"neurosurgery","start":2025,"end":None}],outcome="in_training",outcome_detail="Listed PGY-2 at UVA 2026-27. Note: previously trained in Greece (Hellenic Red Cross Hospital 2014-2020) and UVA fellow 2021-25 per search snippets; joined UVA residency 2025.",current="neurosurgery resident PGY-2, UVA",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"not_found"},abns_certified=False,
 sources=[ros(2,"Georgios Mantziaris"),{"url":"https://www.linkedin.com/in/georgios-mantziaris/","type":"search_snippet","evidence":"Clinical Fellow, Neuro-oncology CAST Fellowship, Dept of Neurosurgery UVA (2023-25); MD University of Athens 2014"}],searches_used=2)
add(7,identity="confirmed",identity_basis="UVA page PGY-2 Katelyn Salotto MD; Doximity Kate Salotto (Dartmouth Geisel 2025) now Charlottesville neurosurgery; co-author Dartmouth neurosurgery",
 residency_stated=[{"institution":"University of Virginia","specialty":"neurosurgery","start":2025,"end":None}],outcome="in_training",outcome_detail="PGY-2 at UVA 2026-27; MD Dartmouth 2025",current="neurosurgery resident PGY-2, UVA",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"found"},abns_certified=False,
 sources=[ros(2,"Katelyn Salotto"),{"url":"https://www.doximity.com/pub/kate-salotto-md","type":"doximity","evidence":"Neurosurgery, Charlottesville VA; Geisel School of Medicine at Dartmouth Class of 2025 (no residency listed)"}],searches_used=2)
add(8,identity="confirmed",identity_basis="UVA page PGY-2 Satvir Saggi MD; search: UCSF MD, 2025 Steinhart Award for incoming surgical residents at UNC",
 residency_stated=[{"institution":"University of North Carolina","specialty":"neurosurgery","start":2025,"end":2026},{"institution":"University of Virginia","specialty":"neurosurgery","start":2026,"end":None}],outcome="in_training",outcome_detail="Consistent with DB: PGY-1 at UNC 2025-26 then joined UVA PGY-2 2026-27. UVA page: Resident Physician in Neurological Surgery; snippet notes 2025 Steinhart Award for incoming residents at UNC.",current="neurosurgery resident PGY-2, UVA",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"not_found"},abns_certified=False,
 sources=[ros(2,"Satvir Saggi"),{"url":"https://med.virginia.edu/neurosurgery/resident-training/current-residents/satvir-saggi-md/","type":"search_snippet","evidence":"MD UCSF; Resident Physician in Neurological Surgery UVA; 2025 Steinhart Award For Incoming Surgical Residents at UNC"}],searches_used=2)
add(9,identity="confirmed",identity_basis="UVA page PGY-1 Hayden Dux MD; LinkedIn 'Neurosurgery Resident'; VCU School of Medicine",
 residency_stated=[{"institution":"University of Virginia","specialty":"neurosurgery","start":2026,"end":None}],outcome="in_training",outcome_detail="PGY-1 at UVA 2026-27",current="neurosurgery resident PGY-1, UVA",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"not_found"},abns_certified=False,
 sources=[ros(1,"Hayden Dux"),{"url":"https://www.linkedin.com/in/hayden-dux-40a57214a/","type":"search_snippet","evidence":"Hayden Dux - Neurosurgery Resident"}],searches_used=2)
add(10,identity="confirmed",identity_basis="UVA page PGY-1 Nathaniel Rolfe MD; Columbia P&S student neurosurgery research",
 residency_stated=[{"institution":"University of Virginia","specialty":"neurosurgery","start":2026,"end":None}],outcome="in_training",outcome_detail="PGY-1 at UVA 2026-27",current="neurosurgery resident PGY-1, UVA",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"not_found"},abns_certified=False,
 sources=[ros(1,"Nathaniel Rolfe"),{"url":"https://med.virginia.edu/neurosurgery/resident-training/current-residents/nathaniel-rolfe-md/","type":"bio","evidence":"Nathaniel Rolfe, MD - Neurosurgery (UVA resident page)"}],searches_used=2)
add(11,identity="confirmed",identity_basis="UVA page PGY-1 Ryan Sindewald MD; UCSD medical student neurosurgery research",
 residency_stated=[{"institution":"University of Virginia","specialty":"neurosurgery","start":2026,"end":None}],outcome="in_training",outcome_detail="PGY-1 at UVA 2026-27",current="neurosurgery resident PGY-1, UVA",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"not_found"},abns_certified=False,
 sources=[ros(1,"Ryan Sindewald"),{"url":"https://www.linkedin.com/in/ryan-sindewald-62660b1b9","type":"search_snippet","evidence":"Ryan Sindewald - M.D. Candidate (UCSD)"}],searches_used=2)
