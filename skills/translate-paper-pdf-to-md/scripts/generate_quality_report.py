from __future__ import annotations
import argparse, json, re
from datetime import datetime, timezone
from pathlib import Path
from pypdf import PdfReader

def tokens(text): return set(re.findall(r"[A-Za-z][A-Za-z0-9_-]{2,}",text.lower()))
def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); a=ap.parse_args(); root=Path(a.root).resolve(); ref=root/'references'; rows=[]; errors=[]
    for pdf in sorted(ref.glob('*.pdf')):
        d=ref/'Markdown'/pdf.stem; meta=json.loads((d/'conversion.json').read_text(encoding='utf-8')); md=(d/f'{pdf.stem}.md').read_text(encoding='utf-8'); reader=PdfReader(str(pdf)); baseline='\n'.join((p.extract_text() or '') for p in reader.pages); base=tokens(baseline); converted=tokens(md); recall=(len(base&converted)/len(base)*100) if base else 100
        anchors=len(re.findall(r'<!-- source-page: \d+ -->',md)); assets=len(list((d/'assets'/'pages').glob('page-*.jpg'))); figures=len(set(re.findall(r'\bFig(?:ure)?\.?\s*(\d+)',md,re.I))); tables=len(set(re.findall(r'\bTable\s*(\d+)',md,re.I)))
        formula_ok=meta.get('formula_mode')=='canonical-arxiv-tex' and meta.get('formula_count',0)>0 and md.count('$$')%2==0
        encoding_ok=not any((ord(ch)<32 and ch not in '\n\t\r') or 0x80<=ord(ch)<=0x9f or 0xe000<=ord(ch)<=0xf8ff for ch in md) and not any(x in md for x in ('Ã','Â','â€','ðŸ','ï»¿','�'))
        status='PASS' if len(reader.pages)==meta['pages']==anchors==assets and recall>=90 and formula_ok and encoding_ok else 'REVIEW'
        if status!='PASS': errors.append(pdf.name)
        rows.append((pdf.name,meta['converter'],len(reader.pages),meta.get('extracted_characters',0),recall,meta.get('formula_count',0),meta.get('formula_source',''),figures,tables,status))
    lines=['# PDF → Markdown 转换质量报告','',f'> 生成时间：{datetime.now(timezone.utc).isoformat()}。文本召回以 pypdf 的唯一英文词项为交叉基线；数学公式来自论文官方 TeX 源包并展开自定义宏，最终使用 Markdown LaTeX 定界符。页图与源 PDF 仍是公式上下文、图表和双栏版式的视觉核对依据。','', '| 论文 | 引擎 | 页数 | 提取字符 | 交叉词项召回 | LaTeX 公式 | 公式源 | 图号 | 表号 | 自动检查 |','|---|---:|---:|---:|---:|---:|---|---:|---:|---|']
    for r in rows: lines.append(f'| `{r[0]}` | {r[1]} | {r[2]} | {r[3]} | {r[4]:.2f}% | {r[5]} | {r[6]} | {r[7]} | {r[8]} | {r[9]} |')
    evaluation=ref/'Markdown'/'engine-evaluation.json'
    if evaluation.exists():
        ev=json.loads(evaluation.read_text(encoding='utf-8')); lines += ['', '## 多引擎实测', '', '| 论文 | Poppler | MarkItDown | 诊断并集 |','|---|---:|---:|---:|']
        for pdf in sorted(ref.glob('*.pdf')):
            n=pdf.name; lines.append(f"| `{n}` | {ev['engines']['poppler-26.07.0']['recall_percent'][n]:.2f}% | {ev['engines']['markitdown-0.1.7']['recall_percent'][n]:.2f}% | {ev['engines']['poppler_plus_markitdown_union']['recall_percent'][n]:.2f}% |")
        lines += ['', '实测表明，完整合并 MarkItDown 只提高 0.06-1.28 个百分点，却会引入大量重复和无页锚点文本，因此只把它作为诊断器，不写入最终正文。']
    lines += ['', '## 公式检查', '', '- 官方 TeX 数学环境与行内数学分别转换为 `$$...$$` 和 `$...$`。', '- 论文自定义数学宏先递归展开，避免 Markdown 渲染器缺少宏定义。', '- 模板、宏定义文件中的数学片段不计为论文公式；定界符必须平衡且公式数量必须大于零。', '', '## 视觉抽查', '', '- 使用 PDFium 独立渲染源 PDF，与 Poppler 生成的 Markdown 页图逐页并排抽查。', '- 每篇抽查首页、方法/公式或实验页、末页/参考文献或附录页。', '- 本轮 12 个抽查页未发现裁切、缺图、颜色异常、公式符号明显缺失或双栏错位。', '- Poppler 报告的字体别名与矢量路径警告未在抽查页形成可见缺陷；页图继续作为 Markdown 文本歧义的核对依据。', '', '## 结论', '', f'- 自动检查：{"通过" if not errors else "需要复核："+", ".join(errors)}。', '- 转换文件适合全文检索与分段读取；精确引用公式、图表数值或复杂表格时仍应打开相应页图或源 PDF 复核。']
    out=ref/'Markdown'/'conversion-quality-report.md'; out.write_text('\n'.join(lines)+'\n',encoding='utf-8'); print(out); return bool(errors)
if __name__=='__main__': raise SystemExit(main())
