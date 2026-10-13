#!/usr/bin/env python3
"""Local-only search dashboard for course test exports. Python 3.9+ / stdlib."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import json
import html

ROOT = Path(__file__).resolve().parent
EXPORTS = ROOT / 'dataExports'
SERVICES = ['gmail', 'github', 'notion', 'google-calendar']
LABELS = {'gmail': 'Gmail', 'github': 'GitHub', 'notion': 'Notion', 'google-calendar': 'Google Calendar'}


def load_records():
    records = []
    for service in SERVICES:
        directory = EXPORTS / service
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob('*.json')):
            try:
                data = json.loads(path.read_text(encoding='utf-8'))
                if not isinstance(data, dict):
                    continue
                headline = str(data.get('subject') or data.get('title') or data.get('name') or path.stem)
                records.append({'service': service, 'headline': headline, 'data': data, 'filename': path.name})
            except (OSError, ValueError, UnicodeError):
                continue
    return records


def esc(value):
    return html.escape(str(value), quote=True)


def render(query='', service='all'):
    records = load_records()
    needle = query.casefold().strip()
    matched = [r for r in records if (service == 'all' or service == r['service']) and
               (not needle or needle in json.dumps(r['data'], ensure_ascii=False).casefold())]
    chips = []
    for key, label in [('all', 'All services')] + [(x, LABELS[x]) for x in SERVICES]:
        count = len(records) if key == 'all' else sum(r['service'] == key for r in records)
        selected = ' selected' if key == service else ''
        chips.append('<option value="%s"%s>%s (%d)</option>' % (esc(key), selected, esc(label), count))
    cards = []
    for r in matched:
        d = r['data']
        details = []
        fields = ('from', 'to', 'owner', 'visibility', 'start', 'end', 'timezone', 'description', 'body', 'body_excerpt', 'content', 'content_summary', 'note')
        for field in fields:
            if field in d and d[field] not in (None, '', []):
                value = d[field]
                if isinstance(value, list):
                    value = ', '.join(map(str, value))
                details.append('<div class="detail"><strong>%s:</strong> %s</div>' % (esc(field.replace('_', ' ').title()), esc(value)))
        url = d.get('url')
        source_link = ('<a href="%s" target="_blank" rel="noopener noreferrer">View source ↗</a>' % esc(url)) if isinstance(url, str) and url.startswith(('https://','http://')) else ''
        cards.append('<article class="result"><div class="top"><span class="tag %s">%s</span><span class="file">%s</span></div><h3>%s</h3>%s%s</article>' % (esc(r['service']), esc(LABELS[r['service']]), esc(r['filename']), esc(r['headline']), ''.join(details), '<div class="link">'+source_link+'</div>' if source_link else ''))
    empty = '<div class="empty">No matching records. Try a different term or service.</div>'
    body = '\n'.join(cards) if cards else empty
    return '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Third Party Services Dashboard</title><style>
:root{color-scheme:light;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif;color:#19283b;background:#f5f7fb}*{box-sizing:border-box}body{margin:0}header{background:#172c4d;color:white;padding:36px 22px}header .wrap,main{max-width:1060px;margin:auto}h1{font-size:clamp(26px,4vw,38px);margin:0 0 8px}header p{margin:0;color:#d2dce9}.eyebrow{font-size:12px;text-transform:uppercase;letter-spacing:2px;color:#92c8ff;margin-bottom:8px}.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:24px 0}.stat{border:1px solid #e2e9f1;background:white;padding:18px;border-radius:14px;box-shadow:0 3px 12px #1c2f4310}.stat b{display:block;font-size:28px}.stat span{font-size:13px;color:#53647b}form{display:flex;gap:10px;padding:16px;background:white;border:1px solid #dfe6ef;border-radius:14px;box-shadow:0 3px 12px #1c2f4310}input,select,button{font:inherit;border-radius:9px;padding:13px 12px}input{flex:1;min-width:80px;border:1px solid #d0d9e3}select{border:1px solid #d0d9e3;max-width:220px}button{border:0;background:#255fc3;color:white;font-weight:600;cursor:pointer}.section-heading{margin:25px 0 12px;display:flex;align-items:center;justify-content:space-between}.section-heading h2{font-size:20px;margin:0}.section-heading span{font-size:13px;color:#687992}.results{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin-bottom:40px}.result{background:white;border:1px solid #e2e8f0;border-radius:14px;padding:20px;overflow-wrap:anywhere;box-shadow:0 3px 12px #1c2f430d}.top{display:flex;justify-content:space-between;align-items:center;gap:12px}.file{color:#8a96a6;font-size:11px}.tag{border-radius:6px;background:#e7efff;color:#1a4eaf;padding:5px 9px;font-size:11px;font-weight:700}.tag.gmail{background:#fff0ed;color:#a23f30}.tag.notion{background:#f0f0f0;color:#303030}.tag.github{background:#ede8fa;color:#6242a4}.tag.google-calendar{background:#e7f7ec;color:#167446}h3{font-size:18px;margin:16px 0 12px}.detail{font-size:13px;line-height:1.55;margin:7px 0;color:#526176;white-space:pre-wrap}.detail strong{color:#27374b}.link{padding-top:12px}.link a{color:#255fc3;text-decoration:none;font-size:13px;font-weight:600}.empty{background:white;padding:35px;border-radius:12px;grid-column:1/-1;color:#64748b}footer{text-align:center;color:#738198;font-size:12px;padding:0 20px 30px}@media(max-width:670px){.stats{grid-template-columns:repeat(2,1fr)}.results{grid-template-columns:1fr}form{flex-direction:column}select{max-width:none}}
</style></head><body><header><div class="wrap"><div class="eyebrow">Local · Course Test Data</div><h1>Third Party Services Dashboard</h1><p>Search your exported Gmail, GitHub, Notion, and Google Calendar records in one place.</p></div></header><main><div class="stats">%s</div><form method="get" action="/"><input type="search" name="q" aria-label="Search exported data" placeholder="Search budget, fitness, property, marketing..." value="%s"><select name="service" aria-label="Choose service">%s</select><button type="submit">Search</button></form><div class="section-heading"><h2>Search results</h2><span>%d record(s) found</span></div><div class="results">%s</div></main><footer>Reads local JSON files at each request · No external API calls · Preliminary test data</footer></body></html>''' % (''.join('<div class="stat"><b>%d</b><span>%s</span></div>' % (sum(r['service']==s for r in records),esc(LABELS[s])) for s in SERVICES), esc(query), ''.join(chips), len(matched), body)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path != '/':
            self.send_error(404)
            return
        params = parse_qs(parsed.query)
        query = params.get('q', [''])[0][:200]
        service = params.get('service', ['all'])[0]
        if service not in SERVICES and service != 'all':
            service = 'all'
        content = render(query, service).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(content)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(content)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Run the local dashboard')
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()
    print('Dashboard: http://127.0.0.1:%d' % args.port, flush=True)
    print('Press Control+C to stop.', flush=True)
    ThreadingHTTPServer(('127.0.0.1', args.port), Handler).serve_forever()
