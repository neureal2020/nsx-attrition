import sys; sys.path.insert(0,'scratch')
from add052 import add
add("52:pau:mcmahon",identity="confirmed",identity_basis="Doximity Paul J McMahon: Univ. of Miami MD 2014, OHSU Neurological Surgery residency from 2014 (matches 2014 entry); WebMD lists him with Neurological Surgery and Psychiatry at OHSU",
 residency_stated=[{"institution":"OHSU","specialty":"neurosurgery","start":2014,"end":2017},{"institution":"OHSU","specialty":"psychiatry","start":2017,"end":2020}],
 outcome="switched_specialty",outcome_detail="Doximity: OHSU neurosurgery residency 2014-2017, then OHSU psychiatry residency 2017-2020 (a further duplicate line 'Neurological Surgery 2014-2021' also appears, apparently an unclosed record); ABPN psychiatry certified; practices psychiatry (neuropsychiatry) in Portland OR.",
 year_left=2017,destination_program="OHSU psychiatry (internal switch)",destination_start_year=2017,current="psychiatrist (neuropsychiatry/TBI), Portland OR",
 agrees_with_db=True,disagreement="DB: did not complete; now resolved: switched to psychiatry at OHSU 2017",
 checks={"google":"found","doximity":"found"},abns_certified=False,
 sources=[{"url":"https://www.doximity.com/pub/paul-mcmahon-md","type":"doximity","evidence":"OHSU Residency, Neurological Surgery, 2014 - 2017; OHSU Residency, Psychiatry, 2017 - 2020; ABPN Psychiatry; University of Miami Class of 2014"}],searches_used=2)
add("52:yim:lin",identity="confirmed",identity_basis="OHSU Neurological Surgery resident Yimo Lin (ResearchGate OHSU affiliation, pediatric neurosurgery papers); OHSU Neurosurgery Facebook memorial post; distinctive name",
 residency_stated=[{"institution":"OHSU","specialty":"neurosurgery","start":2015,"end":None}],
 outcome="unknown",outcome_detail="Search results (OHSU Neurological Surgery Facebook memorial post, GoFundMe memorial, legacy.com) indicate Dr. Yimo Lin died on March 6, 2018 while an OHSU neurosurgery resident. Not a voluntary departure; no Doximity profile. Attrition should be classified as died/other, not transfer or switch.",
 year_left=2018,destination_program=None,destination_start_year=None,current="deceased March 2018 (resident at time)",
 agrees_with_db=True,disagreement="DB: LEFT did not complete; cause was death in training (not transfer/switch/left medicine)",
 checks={"google":"found","doximity":"not_found"},abns_certified=False,
 sources=[{"url":"https://www.facebook.com/OHSUNeurologicalSurgery/posts/recently-we-were-all-deeply-saddened-to-learn-of-the-passing-of-one-of-our-dear-/1729333807089922/","type":"search_snippet","evidence":"Remembering Dr. Yimo Lin with memorial tree donations (OHSU Neurological Surgery post)"},{"url":"https://www.researchgate.net/profile/Yimo-Lin","type":"search_snippet","evidence":"Yimo LIN | Oregon Health & Science University, Portland | OHSU | Department of Neurological Surgery"}],searches_used=2)
add("52:bri:stedelin",identity="confirmed",identity_basis="OHSU Brain Institute X post: Match 2023 neurosurgery interns Jefferson Abaricia, Joe Nugent, Brittany Stedelin (@OHSUNews); OHSU medical student; OHSU Neurosurgery Campagna Scholar",
 residency_stated=[{"institution":"OHSU","specialty":"neurosurgery","start":2023,"end":None}],
 outcome="unknown",outcome_detail="Absent from current OHSU neurosurgery roster while classmates Abaricia and Nugent are PGY-4 (checked ohsu.edu current-residents page). Oregon Medical Board record for Brittany Ann Stedelin appears (search result title 'OR License Verification 09/21/2026'), so likely still in Oregon; destination specialty/program not found. No Doximity profile.",
 year_left=2025,destination_program=None,destination_start_year=None,current="unknown; Oregon licensed physician",
 agrees_with_db=True,disagreement="",
 checks={"google":"found","doximity":"not_found"},abns_certified=False,
 sources=[{"url":"https://x.com/OHSUBrain/status/1636802702498725889","type":"search_snippet","evidence":"newest #neurosurgery #interns who will be joining the program in July 2023 ... Brittany Stedelin (@OHSUNews)"},{"url":"https://www.ohsu.edu/school-of-medicine/neurosurgery/current-residents","type":"program_page","evidence":"PGY-4: Jefferson Abaricia, Jacob Greisman, Joe Nugent; Stedelin not listed"}],searches_used=3)
