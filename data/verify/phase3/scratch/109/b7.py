from mk import *
R="https://neurosurgery.medicine.uiowa.edu/education/neurological-surgery-residency/our-people/residents"
add("85:asa:lak","confirmed","Iowa residents page PGY-5 (Gujranwala, Pakistan); Doximity: Resident, Dept of Neurosurgery, Iowa license 2022-2029, King Edward MU 2018",
 [{"institution":IA,"specialty":"neurosurgery","start":2022,"end":None}],"in_training","Current PGY-5 resident at Iowa","PGY-5 neurosurgery resident, University of Iowa","found",False,
 [(R,"program_page","PGY-5: Asad Lak - Hometown: Gujranwala, Pakistan; Skull base; neuro-oncology"),
  ("https://www.doximity.com/pub/asad-lak-md","doximity","Resident, Department of Neurosurgery; King Edward Medical University Class of 2018; IA license 2022 - 2029")])
add("85:kat:jensen","confirmed","Common name resolved: Doximity lists Iowa neurosurgery residency 2022-2029, UT Health San Antonio MD 2022; Iowa residents page PGY-5; Iowa co-authors (Sandhu, Rosinski)",
 [{"institution":IA,"specialty":"neurosurgery","start":2022,"end":2029}],"in_training","Current PGY-5 resident at Iowa (Doximity projects 2029 completion)","PGY-5 neurosurgery resident, University of Iowa","found",False,
 [(R,"program_page","PGY-5: Katherine Jensen - The Woodlands, TX (Chemical and Biomolecular Engineering)"),
  ("https://www.doximity.com/pub/katherine-jensen-md","doximity","University of Iowa Health Care Medical Center Residency, Neurological Surgery, 2022 - 2029; UT Health San Antonio Class of 2022")])
add("85:man:sandhu","confirmed","Iowa residents page PGY-4 (Chandigarh, India); Doximity: Govt Medical College Chandigarh, Iowa license 2023-2030; Iowa co-author",
 [{"institution":IA,"specialty":"neurosurgery","start":2023,"end":None}],"in_training","Current PGY-4 resident at Iowa","PGY-4 neurosurgery resident, University of Iowa","found",False,
 [(R,"program_page","PGY-4: Mani Ratnesh Sandhu - Chandigarh, India"),
  ("https://www.doximity.com/pub/mani-ratnesh-sandhu-md","doximity","Government Medical College Chandigarh; IA State Medical License 2023 - 2030 (unclaimed profile)")])
add("85:lin:hillembrand","confirmed","Iowa residents page PGY-3 (Barranquilla, Colombia, Universidad del Norte); Doximity: Universidad del Norte 2016, Iowa license 2024-2031",
 [{"institution":IA,"specialty":"neurosurgery","start":2024,"end":None}],"in_training","Current PGY-3 resident at Iowa (matched March 2024)","PGY-3 neurosurgery resident, University of Iowa","found",False,
 [(R,"program_page","PGY-3: Lina Marenco Hillembrand - Barranquilla, Colombia (Universidad del Norte)"),
  ("https://www.doximity.com/pub/lina-marenco-hillembrand-md","doximity","Universidad del Norte Class of 2016; IA State Medical License 2024 - 2031")])
add("85:saa:javeed","confirmed","Iowa residents page PGY-3 (Kot Addu, Pakistan); Doximity: Resident Physician, Iowa license 2024-2031, MBBS 2017; prior WashU postdoc",
 [{"institution":IA,"specialty":"neurosurgery","start":2024,"end":None}],"in_training","Current PGY-3 resident at Iowa","PGY-3 neurosurgery resident, University of Iowa","found",False,
 [(R,"program_page","PGY-3: Saad Javeed - Kot Addu, Pakistan; Neurotrauma, spinal cord injury, spine surgery"),
  ("https://www.doximity.com/pub/saad-javeed-md","doximity","Resident Physician; MBBS Class of 2017; IA State Medical License 2024 - 2031")])
add("85:jor:krieg","confirmed","Iowa residents page PGY-2 (Dickinson ND); Doximity: Univ of North Dakota MD 2024, Iowa license 2025-2032",
 [{"institution":IA,"specialty":"neurosurgery","start":2025,"end":None}],"in_training","Current PGY-2 resident at Iowa (entered 2025)","PGY-2 neurosurgery resident, University of Iowa","found",False,
 [(R,"program_page","PGY-2: Jordan Krieg - Dickinson, North Dakota (Neuroscience)"),
  ("https://www.doximity.com/pub/jordan-krieg-md","doximity","University of North Dakota School of Medicine Class of 2024; IA State Medical License 2025 - 2032")])
import collections
print(collections.Counter(o['outcome'] for o in out), collections.Counter(o['checks']['doximity'] for o in out))
print([x['key'] for x in inp if x['key'] not in {o['key'] for o in out}])
