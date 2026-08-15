from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path

SUPPORTED = {'.pdf', '.docx', '.md', '.txt', '.bib', '.html', '.htm', '.pptx'}

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''): h.update(block)
    return h.hexdigest()

def scan(root: Path) -> dict:
    ref, out = root / 'references', {}
    for p in sorted(ref.iterdir()):
        if not p.is_file() or p.suffix.lower() not in SUPPORTED: continue
        rel = p.relative_to(root).as_posix()
        out[rel] = {'source_id': 'src-' + hashlib.sha1(rel.encode()).hexdigest()[:10], 'sha256': digest(p), 'bytes': p.stat().st_size, 'suffix': p.suffix.lower()}
    return out

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--accept',action='store_true'); a=ap.parse_args()
    root=Path(a.root).resolve(); kg=root/'references'/'Knowledge graph'; kg.mkdir(parents=True,exist_ok=True); mp=kg/'manifest.json'
    old=json.loads(mp.read_text(encoding='utf-8')).get('files',{}) if mp.exists() else {}; cur=scan(root)
    changed=sorted(k for k in set(old)&set(cur) if old[k].get('sha256')!=cur[k]['sha256'])
    report={'generated_at':datetime.now(timezone.utc).isoformat(),'added':sorted(set(cur)-set(old)),'changed':changed,'deleted':sorted(set(old)-set(cur)),'unchanged':sorted((set(old)&set(cur))-set(changed))}
    report['requires_update']=bool(report['added'] or report['changed'] or report['deleted'])
    (kg/'change-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    if a.accept or not mp.exists(): mp.write_text(json.dumps({'schema_version':1,'accepted_at':report['generated_at'],'files':cur},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2)); return 0
if __name__=='__main__': raise SystemExit(main())
