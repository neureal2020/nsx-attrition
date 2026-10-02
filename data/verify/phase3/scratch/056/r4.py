import sys; sys.path.insert(0,'scratch/056')
from add import add
def S(u,t,e): return {"url":u,"type":t,"evidence":e}
add([
{"key":"111:phi:tatman","name":"Philip Tatman","program_id":111,"identity":"confirmed",
 "identity_basis":"University of Utah neurosurgery site has a resident page for Philip Tatman (MD PhD, University of Colorado; search summary of that page); matches DB (Utah PGY-1 2024, Colorado MSTP)",
 "residency_stated":[{"institution":"University of Utah","specialty":"neurosurgery","start":2024,"end":None}],
 "outcome":"unknown","outcome_detail":"A Utah 'residents' page for him exists in search results (page returns 403, undated); no evidence of leaving or of a destination. Likely still at Utah (roster capture may have missed him) but unconfirmed",
 "year_left":None,"destination_program":None,"destination_start_year":None,
 "current":"neurosurgery resident, University of Utah (per Utah resident page, undated)","agrees_with_db":False,"disagreement":"DB says left after PGY-1; Utah resident page still exists - possible he is still in the program; recommend re-check current Utah roster",
 "checks":{"google":"found","doximity":"not_found","usnews":"deferred"},"abns_certified":False,
 "sources":[S("https://medicine.utah.edu/neurosurgery/residents/philip-tatman","program_page","Philip Tatman | Neurosurgery Department (residents page; direct access 403)")],"searches_used":2},
{"key":"112:ada:strand","name":"Adam Strand","program_id":112,"identity":"probable",
 "identity_basis":"WebMD/Vitals: Adam Theodore Strand, Georgetown MD 2014, residency University of Vermont Medical Center; LinkedIn snippet: Emergency Medicine Chief Resident at Henry Ford Health, prior Resident Physician in Radiology at UVM Health Network, 'clinical experience in radiology and neurosurgery'. (Adam O. Strand, internist, is a different person)",
 "residency_stated":[{"institution":"University of Vermont Medical Center","specialty":"neurosurgery","start":2014,"end":None},{"institution":"University of Vermont Medical Center","specialty":"diagnostic radiology (resident)","start":None,"end":None},{"institution":"Henry Ford Health","specialty":"emergency medicine","start":None,"end":None}]
 ,"outcome":"switched_specialty","outcome_detail":"left UVM neurosurgery (~2017); later listed as radiology resident at UVM and then Emergency Medicine chief resident at Henry Ford Health, Detroit; WebMD lists neurological surgery, diagnostic radiology and emergency medicine for him. Exact years not found",
 "year_left":2017,"destination_program":"Henry Ford Health (emergency medicine) after UVM radiology","destination_start_year":None,
 "current":"emergency medicine physician / chief resident, Henry Ford Health, Detroit MI","agrees_with_db":True,"disagreement":"DB unknown (NPI hint other specialty); found switch to radiology then emergency medicine",
 "checks":{"google":"found","doximity":"not_found","usnews":"deferred"},"abns_certified":False,
 "sources":[S("https://www.linkedin.com/in/adam-strand-339505134/","search_snippet","Emergency Medicine Chief Resident, Henry Ford Health; Resident Physician in Radiology at University of Vermont Health Network"),S("https://doctor.webmd.com/doctor/adam-strand-b2fac0f8-666e-43ac-b67d-b713130b6c64-overview","search_snippet","Georgetown University School of Medicine 2014; residency University of Vermont Medical Center; Detroit MI")],"searches_used":3},
{"key":"112:jam:weinberg","name":"James Weinberg","program_id":112,"identity":"confirmed",
 "identity_basis":"Doximity: University of South Carolina School of Medicine class of 2015, UVM Neurological Surgery residency starting 2015 (matches DB entry 2015 and USC MD); WebMD snippet: two years of neurosurgical training at UVM",
 "residency_stated":[{"institution":"University of Vermont Medical Center","specialty":"neurosurgery","start":2015,"end":2017},{"institution":"University of Michigan","specialty":"anesthesiology","start":2018,"end":2021}],
 "outcome":"switched_specialty","outcome_detail":"left UVM neurosurgery after ~2 years (VT license ended 2018); anesthesiology residency at University of Michigan 2018-2021 then pain medicine fellowship; ABA anesthesiology and pain medicine certified. (Doximity lists UVM neurosurgery as 2015-2022, which conflicts with 'two years' and is likely an entry artifact)",
 "year_left":2017,"destination_program":"University of Michigan (anesthesiology)","destination_start_year":2018,
 "current":"interventional pain physician (anesthesiology), Wesley Chapel / Dade City FL","agrees_with_db":True,"disagreement":"DB unknown; found switch to anesthesiology",
 "checks":{"google":"found","doximity":"found","usnews":"deferred"},"abns_certified":False,
 "sources":[S("https://www.doximity.com/pub/james-weinberg-md-65aa53d5","doximity","Residency, Anesthesiology, 2018-2021 University of Michigan; Residency, Neurological Surgery, 2015-2022 UVM; ABA Anesthesiology & Pain Medicine"),S("https://doctor.webmd.com/doctor/james-weinberg-450c938b-2b21-4902-8851-9e20049ddf83-overview","search_snippet","completed two years of neurosurgical training at the University of Vermont; anesthesiology residency Univ. of Michigan")],"searches_used":1},
])
