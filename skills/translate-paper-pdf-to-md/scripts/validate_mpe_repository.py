from __future__ import annotations
import argparse, json, re, subprocess, sys
from pathlib import Path
from urllib.parse import unquote
import yaml
from markdown_it import MarkdownIt

MAX_NOTE_SIZE=5*1024*1024
EXCLUDED_DIRS={'.git','node_modules','tmp','.venv','venv'}
def extension_info() -> tuple[Path,str]:
    matches=list((Path.home()/'.vscode'/'extensions').glob('shd101wyy.markdown-preview-enhanced-*'))
    if not matches: raise FileNotFoundError('Markdown Preview Enhanced is not installed')
    ext=sorted(matches,key=lambda p:p.stat().st_mtime,reverse=True)[0]
    version=json.loads((ext/'package.json').read_text(encoding='utf-8'))['version']
    return ext,version

def fence_errors(text: str) -> list[str]:
    stack=[]
    for number,line in enumerate(text.splitlines(),1):
        match=re.match(r'^ {0,3}(`{3,}|~{3,})',line)
        if not match: continue
        marker=match.group(1)
        if stack:
            if marker[0]==stack[-1][0][0] and len(marker)>=len(stack[-1][0]): stack.pop()
            continue
        stack.append((marker,number))
    return [f'unclosed fence from line {line}' for _,line in stack]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); a=ap.parse_args(); root=Path(a.root).resolve(); errors=[]
    try: _,version=extension_info()
    except Exception as exc: print('ERROR '+str(exc)); return 1
    files=sorted(p for p in root.rglob('*.md') if not EXCLUDED_DIRS.intersection(p.relative_to(root).parts))
    parser=MarkdownIt('commonmark',{'html':True}).enable('table')
    for path in files:
        rel=path.relative_to(root)
        if path.stat().st_size>MAX_NOTE_SIZE: errors.append(f'{rel}: exceeds MPE maxNoteFileSize')
        try: text=path.read_text(encoding='utf-8',errors='strict')
        except UnicodeError as exc: errors.append(f'{rel}: invalid UTF-8: {exc}'); continue
        errors += [f'{rel}: {item}' for item in fence_errors(text)]
        if text.startswith('---\n'):
            end=text.find('\n---\n',4)
            if end<0: errors.append(f'{rel}: unterminated YAML front matter')
            else:
                try: yaml.safe_load(text[4:end])
                except yaml.YAMLError as exc: errors.append(f'{rel}: invalid YAML front matter: {exc}')
        try: tokens=parser.parse(text)
        except Exception as exc: errors.append(f'{rel}: markdown-it parse error: {exc}'); continue
        for token in tokens:
            for child in token.children or []:
                if child.type!='image': continue
                target=child.attrGet('src') or ''
                if not target or re.match(r'^(?:https?:|data:|#)',target,re.I): continue
                resolved=(path.parent/unquote(target.split('#',1)[0])).resolve()
                if not resolved.exists(): errors.append(f'{rel}: missing image {target}')
    preview=Path(__file__).with_name('validate_vscode_preview.py')
    if subprocess.run([sys.executable,str(preview),*[str(p) for p in files]],check=False).returncode:
        errors.append('one or more files fail MPE-compatible KaTeX rendering')
    print(f'mpe_version={version} markdown_files={len(files)} errors={len(errors)}')
    for error in errors: print('ERROR '+error)
    return bool(errors)
if __name__=='__main__': raise SystemExit(main())
