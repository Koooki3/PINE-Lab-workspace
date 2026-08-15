from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path

CHAPTERS=['00-index.md','01-foundations.md','02-reinforcement-learning.md','03-robot-learning.md','04-paper-guides.md','05-knowledge-graph.md','06-source-ledger.md','07-learning-path.md']
def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); a=ap.parse_args(); root=Path(a.root).resolve(); kg=root/'references'/'Knowledge graph'
    parts=['---','title: "PINE 机器人学习 References 知识库与知识图谱"','schema_version: "1.1"',f'generated_at: "{datetime.now(timezone.utc).isoformat()}"','source_mode: "validated-pdf-derived-markdown-with-canonical-latex"','math_renderer: "latex-dollar-delimiters"','---','','# PINE 机器人学习 References 知识库与知识图谱','', '> 本文件由分章知识库自动汇总。论文内容首先转换为逐页可追溯 Markdown；数学公式以经验证的论文 TeX 源码为准，行内公式使用 `$...$`，块级公式使用 `$$...$$`；源 PDF 仅作为版式与视觉核对依据。','', '## 目录','']
    for f in CHAPTERS:
        title=next((x[2:].strip() for x in (kg/f).read_text(encoding='utf-8').splitlines() if x.startswith('# ')),f)
        parts.append(f'- [{title}](#{title.lower().replace(" ", "-")})')
    for f in CHAPTERS:
        text=(kg/f).read_text(encoding='utf-8').strip(); parts += ['', '---', '', f'<!-- chapter-source: {f} -->', '', text]
    body='\n'.join(parts).rstrip()+'\n'; (kg/'PINE.md').write_text(body,encoding='utf-8')
    hashes={f:hashlib.sha256((kg/f).read_bytes()).hexdigest() for f in CHAPTERS}; (kg/'pine-build.json').write_text(json.dumps({'schema_version':1,'chapters':CHAPTERS,'chapter_sha256':hashes},ensure_ascii=False,indent=2)+'\n',encoding='utf-8'); print(kg/'PINE.md'); return 0
if __name__=='__main__': raise SystemExit(main())
