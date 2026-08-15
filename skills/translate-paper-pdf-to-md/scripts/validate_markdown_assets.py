from __future__ import annotations
import argparse,re
from pathlib import Path

IMAGE_RE=re.compile(r'!\[[^\]]*\]\(([^)]+)\)')
def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('markdown',type=Path); a=ap.parse_args(); p=a.markdown.resolve()
    if not p.exists(): print('missing markdown:',p); return 2
    text=p.read_text(encoding='utf-8'); links=IMAGE_RE.findall(text); missing=[x for x in links if '://' not in x and not (p.parent/x).resolve().exists()]; anchors=[int(x) for x in re.findall(r'<!-- source-page: (\d+) -->',text)]; declared=re.search(r'^pages:\s*(\d+)',text,re.M); expected=int(declared.group(1)) if declared else None
    errors=[]
    if missing: errors += ['missing image '+x for x in missing]
    if expected is None: errors.append('missing pages metadata')
    elif anchors!=list(range(1,expected+1)): errors.append('page anchors are incomplete or unordered')
    if len(links)!=expected: errors.append(f'image count {len(links)} != pages {expected}')
    print(f'markdown={p} pages={expected} anchors={len(anchors)} images={len(links)} missing={len(missing)}')
    for e in errors: print('ERROR '+e)
    return bool(errors)
if __name__=='__main__': raise SystemExit(main())
