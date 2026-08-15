from __future__ import annotations
import argparse, json, re
from pathlib import Path

REQ=['schema_version','id','name','slug','description','created_at','updated_at','version','status','source_prompt']
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); a=ap.parse_args(); root=Path(a.root).resolve(); base=root/'prompt-repository'; errors=[]; ids=set()
    idx=base/'index'/'prompts-index.json'
    if not idx.exists(): errors.append('missing prompts-index.json')
    for p in sorted((base/'prompts').rglob('PROMPT-*.md')):
        t=p.read_text(encoding='utf-8')
        if not t.startswith('---\n') or '\n---\n' not in t[4:]: errors.append(f'{p}: invalid front matter')
        for k in REQ:
            if not re.search(rf'^{k}:',t,re.M): errors.append(f'{p}: missing {k}')
        m=re.search(r'^id:\s*"?([^"\n]+)',t,re.M)
        if m:
            if m.group(1) in ids: errors.append(f'duplicate id {m.group(1)}')
            ids.add(m.group(1))
        if '## 2. 完整提示词 / Full Prompt' not in t: errors.append(f'{p}: missing full prompt section')
    if idx.exists() and json.loads(idx.read_text(encoding='utf-8')).get('count')!=len(ids): errors.append('index count mismatch')
    print(f'prompts={len(ids)} errors={len(errors)}'); [print('ERROR '+e) for e in errors]; return bool(errors)
if __name__=='__main__': raise SystemExit(main())
