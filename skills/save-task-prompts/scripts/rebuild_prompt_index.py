from __future__ import annotations
import argparse, hashlib, json, re
from datetime import datetime, timezone
from pathlib import Path

def field(text,name):
    m=re.search(rf'^{re.escape(name)}:\s*["\']?([^\n"\']+)',text,re.M); return m.group(1).strip() if m else None
def source_prompt(text):
    m=re.search(r'^source_prompt:\s*\|-\s*\n(?P<body>(?:^[ ]{2}.*\n?)*)',text,re.M)
    return '\n'.join(x[2:] for x in m.group('body').splitlines()) if m else ''
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); a=ap.parse_args(); root=Path(a.root).resolve(); base=root/'prompt-repository'; entries=[]; hashes={}
    for p in sorted((base/'prompts').rglob('PROMPT-*.md')):
        t=p.read_text(encoding='utf-8'); raw=source_prompt(t); h=hashlib.sha256(raw.encode('utf-8')).hexdigest(); pid=field(t,'id')
        duplicate_of=hashes.get(h); hashes.setdefault(h,pid)
        entries.append({'id':pid,'name':field(t,'name'),'slug':field(t,'slug'),'version':field(t,'version'),'status':field(t,'status'),'path':p.relative_to(root).as_posix(),'sha256':h,'duplicate_of':duplicate_of})
    out={'schema_version':'1.0','generated_at':datetime.now(timezone.utc).isoformat(),'count':len(entries),'prompts':entries}
    (base/'index').mkdir(parents=True,exist_ok=True); (base/'index'/'prompts-index.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(f'indexed {len(entries)} prompts')
if __name__=='__main__': main()
