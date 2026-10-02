from mk import *
X="https://x.com/IowaNeurosurg/status/1937882188768489704"
add("85:dav:christianson","confirmed","Iowa neurosurgery X post names him a 2025 graduate; Iowa Clinic bio; Doximity lists Univ South Dakota MD (Class 2018) and Iowa license from 2025",
 [{"institution":IA,"specialty":"neurosurgery","start":2018,"end":2025}],"completed","Completed Iowa residency 2025 and joined The Iowa Clinic; Doximity training section lists only medical school (no residency, no ABNS yet)",
 "Neurosurgeon (spine/functional), The Iowa Clinic, Des Moines IA","found",False,
 [(X,"news","Congratulations to our 2025 Graduates - Dr. David Christianson and Dr. Mark Dougherty"),
  ("https://www.iowaclinic.com/doctors/david-christianson/","bio","The Iowa Clinic Neurological & Spinal Surgery"),
  ("https://www.doximity.com/pub/david-christianson-md-57513568","doximity","University of South Dakota, Sanford School of Medicine, Class of 2018; IA license 2025-2027")])
add("85:mar:dougherty","confirmed","Iowa X post names him a 2025 graduate; Doximity Iowa residency 2018-2025, Pritzker MD 2018; Iowa GME page",
 [{"institution":IA,"specialty":"neurosurgery","start":2018,"end":2025}],"completed","Completed Iowa residency 2025; now skull base neurosurgery fellow at Johns Hopkins (per search summary); alumni page shows 'TBD'",
 "Skull base neurosurgery fellow, Johns Hopkins (2025-26)","found",False,
 [(X,"news","Congratulations to our 2025 Graduates - Dr. David Christianson and Dr. Mark Dougherty"),
  ("https://www.doximity.com/pub/mark-dougherty-md-cda2da76","doximity","University of Iowa Health Care Medical Center Residency, Neurological Surgery, 2018 - 2025; Class of 2018 Pritzker"),
  ("https://gme.medicine.uiowa.edu/neurological-surgery-residency/our-people/current-residents/mark-dougherty-md","program_page","Iowa GME resident/alumnus page (search snippet)")])
add("85:nah:teferi","confirmed","Iowa GME resident page and MSK fellows page; Addis Ababa MD 2013; Iowa neurosurgery residency alumnus",
 [{"institution":IA,"specialty":"neurosurgery","start":2019,"end":2026}],"completed","Completed Iowa residency 2026; Neurosurgical Oncology Fellow at Memorial Sloan Kettering 2026-2027 (per search summary of Iowa GME page); not yet on alumni page",
 "Neurosurgical oncology fellow, Memorial Sloan Kettering (2026-27)","not_found",None,
 [("https://gme.medicine.uiowa.edu/neurological-surgery-residency/our-people/current-residents/nahom-teferi-md","program_page","Neurosurgical Oncology Fellow 2026-2027 with residency from University of Iowa Hospitals and Clinics (search summary)"),
  ("https://www.mskcc.org/departments/neurosurgery/neurosurgical-oncology/fellows","program_page","MSK neurosurgical oncology fellows page listed in results")],searches=3)
add("85:tim:woodiwiss","confirmed","Doximity: Iowa residency 2019-2026, UW MD 2019; Iowa GME page (started June 24, 2019)",
 [{"institution":IA,"specialty":"neurosurgery","start":2019,"end":2026}],"completed","Completed Iowa residency 2026; Iowa license through 2026, MO license 2026; neurosurgical oncology fellow at Washington University (St. Louis)",
 "Neurosurgical oncology / skull base fellow, Washington University, St. Louis MO","found",False,
 [("https://www.doximity.com/pub/timothy-woodiwiss-md","doximity","University of Iowa Health Care Medical Center Residency, Neurological Surgery, 2019 - 2026; St. Louis MO, Skull Base"),
  ("https://gme.medicine.uiowa.edu/neurological-surgery-residency/our-people/current-residents/timothy-woodiwiss-md","program_page","started June 24, 2019 (search summary)")])
