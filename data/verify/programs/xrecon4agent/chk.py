import json,sys
d=json.load(open('data/verify/phase3/merged_final.json'))
for q in sys.argv[1:]:
  q=q.lower()
  for r in d:
    if q in r['name'].lower():
      print(q,'|',r['name'],r['program_id'],r['program'][:40],r['entry_year'],r['first_seen'],r['last_seen'],r['outcome'])
