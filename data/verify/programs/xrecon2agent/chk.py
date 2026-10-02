import json,sys
d=json.load(open('/Users/neureal/Documents/Residency Application Study/data/verify/phase3/merged_final.json'))
for q in sys.argv[1:]:
    ql=q.lower()
    hits=[r for r in d if ql in r['name'].lower()]
    if q.isdigit():
        hits=[r for r in d if r['program_id']==int(q)]
    for r in sorted(hits,key=lambda r:(r['program_id'],r['entry_year'])):
        print(q,'|',r['program_id'],r['name'],r['entry_year'],r['first_seen'],r['last_seen'],r['last_pgy'],r['outcome_2025'])
    if not hits: print(q,'| NOT FOUND')
