from __future__ import annotations
import argparse,hashlib,json,subprocess,sys
from pathlib import Path

def digest(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()
def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); a=ap.parse_args(); root=Path(a.root).resolve(); ref=root/'references'; base=ref/'Markdown'; errors=[]
    pdfs=sorted(ref.glob('*.pdf'))
    for pdf in pdfs:
        d=base/pdf.stem; meta=d/'conversion.json'; md=d/f'{pdf.stem}.md'
        if not meta.exists() or not md.exists(): errors.append(f'missing conversion for {pdf.name}'); continue
        info=json.loads(meta.read_text(encoding='utf-8'))
        if info.get('source_sha256')!=digest(pdf): errors.append(f'stale conversion for {pdf.name}')
        if info.get('converter')!='poppler-26.07.0': errors.append(f'non-primary converter requires review for {pdf.name}: {info.get("converter")}')
        if info.get('formula_mode')!='canonical-arxiv-tex': errors.append(f'non-canonical formula mode for {pdf.name}')
        if not isinstance(info.get('formula_count'),int) or info.get('formula_count',0)<=0: errors.append(f'no canonical LaTeX formulas for {pdf.name}')
        body=md.read_text(encoding='utf-8')
        forbidden=[ch for ch in body if (ord(ch)<32 and ch not in '\n\t\r') or 0x80<=ord(ch)<=0x9f or 0xe000<=ord(ch)<=0xf8ff]
        markers=[x for x in ('Ã','Â','â€','ðŸ','ï»¿','�') if x in body]
        if forbidden: errors.append(f'forbidden control/private-use characters in {pdf.name}: {len(forbidden)}')
        if markers: errors.append(f'mojibake markers in {pdf.name}: {markers}')
        if body.count('$$') % 2: errors.append(f'unbalanced display math delimiters for {pdf.name}')
        if '## Canonical LaTeX formula registry' not in body: errors.append(f'missing formula registry for {pdf.name}')
        rc=subprocess.run([sys.executable,str(Path(__file__).with_name('validate_markdown_assets.py')),str(md)],check=False).returncode
        if rc: errors.append(f'asset validation failed for {pdf.name}')
        preview=subprocess.run([sys.executable,str(Path(__file__).with_name('validate_vscode_preview.py')),str(md)],check=False).returncode
        if preview: errors.append(f'VS Code Markdown/KaTeX preview validation failed for {pdf.name}')
    extras=[d.name for d in base.iterdir() if d.is_dir() and not (ref/(d.name+'.pdf')).exists()]
    errors += ['orphan conversion '+x for x in extras]
    print(f'pdfs={len(pdfs)} errors={len(errors)}'); [print('ERROR '+e) for e in errors]; return bool(errors)
if __name__=='__main__': raise SystemExit(main())
