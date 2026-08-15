from __future__ import annotations
import argparse, hashlib, json, re, shutil, subprocess, tempfile
from datetime import datetime, timezone
from pathlib import Path
import pdfplumber
import pypdfium2 as pdfium
from extract_latex_formulas import download_arxiv_source, extract_formulas, render_formula_registry, unpack_source

ARXIV_IDS = {
    '1801.01290v2': '1801.01290v2',
    '2410.24164v4': '2410.24164v4',
    '2507.07969v4': '2507.07969v4',
    'hil-serl-paper': '2410.21845',
}

PRIVATE_GLYPH_MAP = str.maketrans({
    '\ue239':'𝓜','\ue23f':'𝒮','\ue22d':'𝒜','\ue23c':'𝒫',
    '\ue238':'ℒ','\ue234':'ℋ','\ue241':'𝒰','\ue242':'𝒱',
    '\uf8ee':'[','\uf8f0':'[','\uf8f9':']','\uf8fb':']',
})
MOJIBAKE_MARKERS=('Ã','Â','â€','ðŸ','ï»¿','�')

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()

def clean_text(text: str) -> str:
    text=text.replace('\ufb01','fi').replace('\ufb02','fl')
    lines=[]; warning_active=False; warning='> [Extraction warning] One or more lines using an invalid PDF font map were omitted. Use the rendered source page and canonical LaTeX registry.'
    for raw in text.splitlines():
        invalid_control=any((ord(ch)<32 and ch!='\t') or 0x80<=ord(ch)<=0x9f for ch in raw)
        suspicious=any(marker in raw for marker in MOJIBAKE_MARKERS)
        if invalid_control or suspicious:
            if not warning_active: lines.append(warning); warning_active=True
            continue
        line=raw.translate(PRIVATE_GLYPH_MAP)
        line=''.join(ch if not 0xe000<=ord(ch)<=0xf8ff else '�' for ch in line)
        if '�' in line:
            if not warning_active: lines.append(warning); warning_active=True
            continue
        lines.append(line.rstrip())
        if line.strip(): warning_active=False
    return '\n'.join(lines).strip()

def title_from(text: str, stem: str) -> str:
    lines=[re.sub(r'\s+',' ',x).strip() for x in text.splitlines() if x.strip()]
    candidates=[x for x in lines[:20] if 8<=len(x)<=180 and not re.match(r'^(arXiv|Figure|Fig\.|Table|Abstract$)',x,re.I)]
    return candidates[0] if candidates else stem

def section_index(full: str) -> list[str]:
    found=[]
    patterns=[r'^(?:\d+(?:\.\d+)*\.?|[IVX]+\.)\s+[A-Z][^\n]{2,100}$',r'^(Abstract|Introduction|Related Work|Method|Methods|Experiments|Results|Conclusion|References|Acknowledg(?:e)?ments)\s*$']
    for line in full.splitlines():
        s=re.sub(r'\s+',' ',line).strip()
        if any(re.match(p,s,re.I) for p in patterns) and s not in found: found.append(s)
    return found[:80]

def poppler_tools(root: Path) -> dict[str,Path] | None:
    bindir=Path.home()/'.codex'/'tools'/'pdf-md-env'/'Library'/'bin'
    tools={n:bindir/(n+'.exe') for n in ['pdfinfo','pdftotext','pdftocairo','pdfimages']}
    return tools if all(p.exists() for p in tools.values()) else None

def extract_poppler(pdf: Path, root: Path, out_dir: Path, dpi: int) -> tuple[list[str],dict]:
    tools=poppler_tools(root)
    if not tools: raise RuntimeError('repository Poppler toolchain is unavailable')
    work=Path(tempfile.gettempdir())/'pine-pdf-md'/pdf.stem
    if work.exists(): shutil.rmtree(work)
    work.mkdir(parents=True,exist_ok=True); ascii_pdf=work/'source.pdf'; shutil.copy2(pdf,ascii_pdf)
    layout=work/'source_layout.txt'; raw=work/'source_raw.txt'
    subprocess.run([str(tools['pdftotext']),'-layout','-enc','UTF-8',str(ascii_pdf),str(layout)],check=True)
    subprocess.run([str(tools['pdftotext']),'-raw','-enc','UTF-8',str(ascii_pdf),str(raw)],check=True)
    info=subprocess.run([str(tools['pdfinfo']),str(ascii_pdf)],check=True,capture_output=True,text=True,encoding='utf-8',errors='replace').stdout
    images=subprocess.run([str(tools['pdfimages']),'-list',str(ascii_pdf)],check=True,capture_output=True,text=True,encoding='utf-8',errors='replace').stdout
    pages=[clean_text(x) for x in layout.read_text(encoding='utf-8',errors='replace').split('\f')]
    if pages and not pages[-1]: pages.pop()
    page_count=int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1))
    pages += ['']*max(0,page_count-len(pages)); pages=pages[:page_count]
    pages_dir=out_dir/'assets'/'pages'; pages_dir.mkdir(parents=True,exist_ok=True); rendered=work/'rendered'; rendered.mkdir(); prefix=rendered/'page'
    subprocess.run([str(tools['pdftocairo']),'-jpeg','-r',str(dpi),'-jpegopt','quality=82',str(ascii_pdf),str(prefix)],check=True)
    for p in sorted(rendered.glob('page-*.jpg')):
        number=int(p.stem.split('-')[-1]); target=pages_dir/f'page-{number:03d}.jpg'
        shutil.copy2(p,target)
    meta={'pdfinfo':info.strip(),'embedded_image_rows':max(0,len(images.splitlines())-2),'raw_text_bytes':raw.stat().st_size}
    shutil.rmtree(work); parent=work.parent
    if parent.exists() and not any(parent.iterdir()): parent.rmdir()
    return pages,meta

def convert(pdf: Path, out_dir: Path, root: Path, engine: str, scale: float, dpi: int) -> dict:
    out_dir.mkdir(parents=True,exist_ok=True); pages_dir=out_dir/'assets'/'pages'; pages_dir.mkdir(parents=True,exist_ok=True)
    extra={}
    if engine=='poppler' or (engine=='auto' and poppler_tools(root)):
        texts,extra=extract_poppler(pdf,root,out_dir,dpi); converter='poppler-26.07.0'
    else:
        texts=[]
        with pdfplumber.open(pdf) as doc:
            for page in doc.pages: texts.append(clean_text(page.extract_text(x_tolerance=2,y_tolerance=3,layout=True) or ''))
        rendered=pdfium.PdfDocument(str(pdf))
        for i in range(len(rendered)):
            image=rendered[i].render(scale=scale).to_pil().convert('RGB'); image.save(pages_dir/f'page-{i+1:03d}.jpg',quality=82,optimize=True)
        converter='pdfplumber+pypdfium2'
    arxiv_id=ARXIV_IDS.get(pdf.stem)
    if not arxiv_id: raise RuntimeError(f'no verified TeX source mapping for {pdf.name}')
    latex_work=Path(tempfile.gettempdir())/'pine-pdf-latex'/pdf.stem
    if latex_work.exists(): shutil.rmtree(latex_work)
    latex_work.mkdir(parents=True,exist_ok=True); archive=latex_work/'source.tar'; source_dir=latex_work/'source'
    if not source_dir.exists(): download_arxiv_source(arxiv_id,archive); unpack_source(archive,source_dir)
    formulas=extract_formulas(source_dir)
    if not formulas: raise RuntimeError(f'no LaTeX formulas recovered for {pdf.name}')
    source_hash=sha256(pdf); title=title_from(texts[0] if texts else '',pdf.stem); sections=section_index('\n'.join(texts)); now=datetime.now(timezone.utc).isoformat()
    rel_pdf='../../'+pdf.name
    lines=['---','schema_version: "1.0"',f'title: "{title.replace(chr(34), chr(39))}"',f'source_pdf: "{rel_pdf}"',f'source_sha256: "{source_hash}"',f'pages: {len(texts)}','content_mode: "source-faithful-page-anchored"','source_language: "en"',f'converted_at: "{now}"',f'converter: "{converter}"','---','',f'# {title}','',f'> Source: [`{pdf.name}`]({rel_pdf}). This Markdown preserves extracted source text page by page. Rendered pages remain the visual authority for figures, tables, equations, and ambiguous reading order.','', '## Generated section index','']
    lines += [f'- {s}' for s in sections] if sections else ['- No reliable section headings were detected automatically; search page text directly.']
    lines += ['', *render_formula_registry(formulas,arxiv_id)]
    for i,text in enumerate(texts,1):
        lines += ['', '---', '', f'<!-- source-page: {i} -->', f'## Source page {i}', '', f'![Rendered source page {i}](assets/pages/page-{i:03d}.jpg)', '', '*Rendered source page for visual verification.*', '']
        if text: lines += [text]
        else: lines += ['> [Extraction warning] No selectable text was recovered from this page. Use the rendered page above.']
    md=out_dir/f'{pdf.stem}.md'; md.write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
    meta={'schema_version':1,'source_pdf':pdf.name,'source_relative_path':pdf.as_posix(),'source_sha256':source_hash,'pages':len(texts),'converter':converter,'converted_at':now,'markdown':md.name,'assets':'assets/pages','section_index':sections,'extracted_characters':sum(map(len,texts)),'formula_mode':'canonical-arxiv-tex','formula_source':f'arxiv:{arxiv_id}','formula_count':len(formulas),**extra}
    (out_dir/'conversion.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); return meta

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--force',action='store_true'); ap.add_argument('--engine',choices=['auto','poppler','python'],default='auto'); ap.add_argument('--scale',type=float,default=1.25); ap.add_argument('--dpi',type=int,default=120); a=ap.parse_args()
    root=Path(a.root).resolve(); ref=root/'references'; base=ref/'Markdown'; base.mkdir(parents=True,exist_ok=True); pdfs=sorted(ref.glob('*.pdf')); stems={p.stem for p in pdfs}
    for d in sorted(base.iterdir()):
        if d.is_dir() and d.name not in stems: shutil.rmtree(d); print('removed deleted-source conversion:',d.name)
    changed=0
    for pdf in pdfs:
        out=base/pdf.stem; meta_path=out/'conversion.json'; current=sha256(pdf)
        if not a.force and meta_path.exists() and json.loads(meta_path.read_text(encoding='utf-8')).get('source_sha256')==current and (out/f'{pdf.stem}.md').exists(): print('unchanged:',pdf.name); continue
        if out.exists(): shutil.rmtree(out)
        meta=convert(pdf,out,root,a.engine,a.scale,a.dpi); changed+=1; print(f"converted: {pdf.name} -> {meta['markdown']} ({meta['pages']} pages, {meta['converter']})")
    print(f'pdfs={len(pdfs)} converted={changed}'); return 0
if __name__=='__main__': raise SystemExit(main())
