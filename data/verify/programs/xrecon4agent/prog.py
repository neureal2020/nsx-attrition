import json,sys
d=json.load(open('data/verify/phase3/merged_final.json'))
for pid in map(int,sys.argv[1:]):
  print('==',pid)
  for r in sorted([r for r in d if r['program_id']==pid],key=lambda r:r['entry_year']):
    if r['entry_year']<=2019: print(' ',r['name'],r['entry_year'],r['first_seen'],r['last_seen'],r['outcome'])
