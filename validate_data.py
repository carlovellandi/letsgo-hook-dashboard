#!/usr/bin/env python3
import csv, sys
from collections import defaultdict
from pathlib import Path
p=Path(sys.argv[1] if len(sys.argv)>1 else 'data/variants_log.csv')
required=['Variant ID','Round ID','Review Cycle','Variant Category','Predicted Best Performing Hook','Prediction Confidence','Views 48h','3-Sec Retention % 48h','Winner of Round (Y/N)','Promoted to Feed (Y/N)','Views 7d','7d Distribution Context']
with p.open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.DictReader(f)); fields=rows[0].keys() if rows else []
missing=[x for x in required if x not in fields]
if missing: raise SystemExit('Missing headers: '+', '.join(missing))
by=defaultdict(list)
for r in rows: by[r['Round ID']].append(r)
errors=[]
expected={'Credential','Numbered / Specific','POV / Direct-address','Contrarian / Pattern-break','Cold Open / Visual-only'}
for rid,rs in by.items():
    cats={r['Variant Category'] for r in rs}
    if len(rs)!=5: errors.append(f'{rid}: expected 5 variants, found {len(rs)}')
    if cats!=expected: errors.append(f'{rid}: hook categories do not match Phase 1 set')
    if sum(r['Predicted Best Performing Hook']=='Y' for r in rs)!=1: errors.append(f'{rid}: expected exactly one human prediction')
    if sum(r['Winner of Round (Y/N)']=='Y' for r in rs)!=1: errors.append(f'{rid}: expected exactly one winner')
    if sum(r['Promoted to Feed (Y/N)']=='Y' for r in rs)!=1: errors.append(f'{rid}: expected exactly one promoted reel')
    win=next((r for r in rs if r['Winner of Round (Y/N)']=='Y'),None)
    if win and win['Promoted to Feed (Y/N)']!='Y': errors.append(f'{rid}: winner must be promoted')
    if win and not win['Date Promoted']: errors.append(f'{rid}: promoted winner missing Date Promoted')
if errors:
    print('\n'.join(errors)); raise SystemExit(1)
print(f'Validated {len(rows)} rows across {len(by)} complete 5-variant rounds.')
