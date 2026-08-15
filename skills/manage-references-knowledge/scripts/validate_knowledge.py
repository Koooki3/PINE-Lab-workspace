from __future__ import annotations
import argparse, json, re
from pathlib import Path

REQ=['00-index.md','01-foundations.md','02-reinforcement-learning.md','03-robot-learning.md','04-paper-guides.md','05-knowledge-graph.md','06-source-ledger.md','07-learning-path.md','graph.json','manifest.json']
def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); a=ap.parse_args(); kg=Path(a.root).resolve()/'references'/'Knowledge graph'; errors=[]; warnings=[]
    for n in REQ:
        if not (kg/n).is_file(): errors.append('missing '+n)
    if errors: print('\n'.join('ERROR '+e for e in errors)); return 1
    man=json.loads((kg/'manifest.json').read_text(encoding='utf-8')); g=json.loads((kg/'graph.json').read_text(encoding='utf-8')); ids=[n['id'] for n in g['nodes']]; known=set(ids)
    if len(ids)!=len(known): errors.append('duplicate graph node id')
    srcids={v['source_id'] for v in man['files'].values()}
    for n in g['nodes']:
        if n.get('kind')=='paper' and n.get('source_id') not in srcids: errors.append('unknown source_id on '+n['id'])
    incoming={i:0 for i in ids}
    for e in g['edges']:
        if e.get('source') not in known or e.get('target') not in known: errors.append('broken edge '+str(e))
        else: incoming[e['target']]+=1
        if not e.get('why'): errors.append('edge lacks why '+str(e))
    for n in g['nodes']:
        if n.get('level',0)>=3 and n.get('kind')!='paper' and incoming[n['id']]==0: warnings.append('advanced node lacks prerequisite '+n['id'])
    md='\n'.join((kg/n).read_text(encoding='utf-8') for n in REQ if n.endswith('.md')); cited=set(re.findall(r'\[(S\d+)\]',md)); ledger=set(re.findall(r'^\[(S\d+)\]',(kg/'06-source-ledger.md').read_text(encoding='utf-8'),re.M))
    for c in sorted(cited-ledger): errors.append('citation missing from ledger '+c)
    for p in man['files']:
        if Path(p).name not in md: warnings.append('source filename not mentioned '+p)
    print(f'nodes={len(ids)} edges={len(g["edges"])} citations={len(cited)}')
    for x in warnings: print('WARNING '+x)
    for x in errors: print('ERROR '+x)
    return bool(errors)
if __name__=='__main__': raise SystemExit(main())
