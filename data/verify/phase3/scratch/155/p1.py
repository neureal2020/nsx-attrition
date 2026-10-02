import sys; sys.path.insert(0,'scratch/155')
from add import add
W="https://school.wakehealth.edu/residents-and-fellows/"
add("119:jon:gordon",identity="confirmed",identity_basis="Wake Forest School of Medicine resident directory lists Jonah Phillip Gordon, Neurological Surgery Residency PGY-2, MD USF 2025",
 residency_stated=[{"institution":"Wake Forest Baptist Medical Center","specialty":"neurosurgery","start":2025,"end":2032}],
 outcome="in_training",outcome_detail="PGY-2, projected graduation 2032",current="neurosurgery resident PGY-2, Wake Forest",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"not_found"},abns_certified=False,
 sources=[{"url":W+"g/jonah-phillip-gordon","type":"program_page","evidence":"Neurological Surgery Residency, PGY-2, projected graduation 2032, USF MD 2025"}],searches_used=2)
add("119:jua:giraldo",identity="confirmed",identity_basis="Wake Forest resident page: Juan Pedro Giraldo PGY-2 neurological surgery, MD Universidad CES 2020; Barrow bio/LinkedIn consistent",
 residency_stated=[{"institution":"Wake Forest Baptist Medical Center","specialty":"neurosurgery","start":2025,"end":2032}],
 outcome="in_training",outcome_detail="PGY-2, projected graduation 2032",current="neurosurgery resident PGY-2, Wake Forest",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"not_found"},abns_certified=False,
 sources=[{"url":W+"g/juan-pedro-giraldo","type":"program_page","evidence":"Neurological Surgery Residency PGY-2, projected 2032, Universidad CES MD 2020"},{"url":"https://www.linkedin.com/in/juan-p-giraldo-md-5a50bb22b/","type":"search_snippet","evidence":"Juan P. Giraldo, MD - PGY-2 Neurosurgery Resident"}],searches_used=2)
add("119:wum:shali",identity="confirmed",identity_basis="Wake Forest resident page: Wumairehan Shali, Neurological Surgery PGY-2, MD Shanghai Jiao Tong 2017 (distinctive name)",
 residency_stated=[{"institution":"Wake Forest Baptist Medical Center","specialty":"neurosurgery","start":2025,"end":2031}],
 outcome="in_training",outcome_detail="PGY-2, projected graduation 2031",current="neurosurgery resident PGY-2, Wake Forest",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"not_found"},abns_certified=False,
 sources=[{"url":W+"s/wumairehan-shali","type":"program_page","evidence":"Neurological Surgery Residency PGY-2, projected graduation 2031"}],searches_used=2)
add("119:bra:benedict",identity="confirmed",identity_basis="Wake Forest resident page: Braeden Christopher Benedict PGY-1 neurological surgery, MD WashU 2026; WashU med student neurosurgery-interested per Greenberg lab page",
 residency_stated=[{"institution":"Wake Forest Baptist Medical Center","specialty":"neurosurgery","start":2026,"end":2033}],
 outcome="in_training",outcome_detail="PGY-1, projected graduation 2033",current="neurosurgery resident PGY-1, Wake Forest",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"not_found"},abns_certified=False,
 sources=[{"url":W+"b/braeden-christopher-benedict","type":"program_page","evidence":"Neurological Surgery Residency PGY-1, projected 2033, WashU MD 2026"}],searches_used=3)
add("119:bri:freeman",identity="probable",identity_basis="Bridger H. Freeman, UTHealth Houston med student with neurosurgery (Vivian L. Smith Dept) research; no Wake Forest resident page found (direct URL 404), so program not directly confirmed",
 residency_stated=[],outcome="in_training",outcome_detail="No contradicting evidence; recorded roster PGY-1 2026-27; no public page confirms Wake placement",current="probable neurosurgery PGY-1 (unconfirmed publicly)",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"not_found"},abns_certified=False,
 sources=[{"url":"https://www.linkedin.com/in/bridger-freeman-958aa4199/","type":"search_snippet","evidence":"Bridger Freeman - 4th-Year Medical Student at UTHealth"}],searches_used=4)
add("119:jac:midtlien",identity="confirmed",identity_basis="Wake Forest resident page and Doximity: Jackson Porter Midtlien, Wake Forest MD 2026, Winston-Salem",
 residency_stated=[{"institution":"Wake Forest Baptist Medical Center","specialty":"neurosurgery","start":2026,"end":2033}],
 outcome="in_training",outcome_detail="PGY-1, projected graduation 2033",current="neurosurgery resident PGY-1, Wake Forest",agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"found"},abns_certified=False,
 sources=[{"url":W+"m/jackson-porter-midtlien","type":"program_page","evidence":"Neurological Surgery Residency PGY-1, projected 2033"},{"url":"https://www.doximity.com/pub/jackson-midtlien-md","type":"doximity","evidence":"Wake Forest School of Medicine Class of 2026; NC license 2026; no residency listed"}],searches_used=1)
