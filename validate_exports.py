#!/usr/bin/env python3
"""Validate local JSON structure and report missing full-fidelity metadata; Python 3.9+."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parent / 'dataExports'
SPECS = {
    'github': ['service','name','owner','url','source_id','exported_at'],
    'gmail': ['service','subject','from','to','body','source_id','email_ts','exported_at'],
    'notion': ['service','title','page_id','content','exported_at'],
    'google-calendar': ['service','title','start','end','calendar_id','source_id','exported_at'],
}
errors = 0
for service, fields in SPECS.items():
    files = sorted((ROOT/service).glob('*.json'))
    print('%s: %d JSON files' % (service, len(files)))
    if len(files) < 5:
        print('  WARNING: Fewer than five service records')
        errors += 1
    for file in files:
        try:
            obj=json.loads(file.read_text(encoding='utf-8'))
            if not isinstance(obj,dict): raise ValueError('Not an object')
            missing=[field for field in fields if not obj.get(field)]
            if obj.get('service')!=service: missing.append('service must match folder name')
            if missing:
                print('  %s: missing %s' % (file.name, ', '.join(missing)))
                errors += 1
        except (OSError,ValueError) as exc:
            print('  %s: invalid JSON (%s)' % (file.name,exc))
            errors += 1
print('Validation: %s' % ('NEEDS ENRICHMENT (%d record errors)' % errors if errors else 'PASS'))
sys.exit(1 if errors else 0)
