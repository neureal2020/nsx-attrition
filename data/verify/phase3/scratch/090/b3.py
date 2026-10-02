import sys; sys.path.insert(0,'/Users/neureal/Documents/Residency Application Study/data/verify/phase3/scratch/090')
from add import add
from b2 import E, UB, IT, cur
a=E("69:ale:aguirre","Alex Aguirre","confirmed","Doximity: Jacobs MD 2024, UB neurosurgery residency 2024-2025, then Barrow Neurological Institute 2025-2031; LinkedIn/ZoomInfo snippet 'Resident Physician at Barrow'; UB co-authors",
 [{"institution":UB,"specialty":"neurosurgery","start":2024,"end":2025},{"institution":"Barrow Neurological Institute at St Joseph's Hospital and Medical Center","specialty":"neurosurgery","start":2025,"end":2031}],"transferred",
 "Transferred after PGY-1 (2024-25) from UB to Barrow Neurological Institute neurosurgery (Doximity: Barrow 2025-2031).","neurosurgery resident (PGY-2/3), Barrow Neurological Institute, Phoenix AZ",None,"found",
 [{"url":"https://www.doximity.com/pub/alexander-aguirre-md","type":"doximity","evidence":"Residency, Neurological Surgery, 2025 - 2031, Barrow Neurological Institute; Residency, Neurological Surgery, 2024 - 2025, University at Buffalo"},{"url":"https://www.linkedin.com/in/alexander-aguirre-396251123/","type":"search_snippet","evidence":"Alexander Aguirre - Neurosurgery Resident at Barrow"}],2)
a["year_left"]=2025;a["destination_program"]="Barrow Neurological Institute (program 4)";a["destination_start_year"]=2025
add([a,
IT("69:jus:williams","Justin Williams","confirmed","UB current residents page (Thomas Jefferson MD) and Doximity residency UB 2024-2031, Sidney Kimmel Class of 2024",2024,2031,"found",
 [{"url":cur,"type":"program_page","evidence":"PGY-2 Justin Williams, MD | Sidney Kimmel Medical College at Thomas Jefferson University"},{"url":"https://www.doximity.com/pub/justin-williams-md-924c1d88","type":"doximity","evidence":"Residency, Neurological Surgery, 2024 - 2031, University at Buffalo"}],2),
IT("69:mic:moran","Michael Moran","confirmed","UB current residents page (Mike Moran, Drexel MD) and Doximity Drexel Class of 2023; UB bio: preliminary general surgery year at Penn State Hershey before matching at UB",2024,None,"found",
 [{"url":cur,"type":"program_page","evidence":"PGY-2 Mike Moran, MD | Drexel University College of Medicine"},{"url":"https://www.doximity.com/pub/michael-moran-md-e6fb5543","type":"doximity","evidence":"Drexel University College of Medicine Class of 2023; Buffalo, NY Neurosurgery"}],2,
 extra="Preliminary intern year in general surgery at Penn State Health (Hershey) before UB."),
])
