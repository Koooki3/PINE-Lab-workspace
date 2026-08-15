from __future__ import annotations
import argparse, os, shutil, subprocess
from pathlib import Path

def find_katex() -> Path:
    candidates=[]
    code=shutil.which('code')
    if code:
        install=Path(code).resolve().parent.parent
        candidates.extend(install.glob('*/resources/app/extensions/markdown-language-features/markdown-editor-out/katex-*.js'))
        candidates.extend(install.glob('resources/app/extensions/markdown-language-features/markdown-editor-out/katex-*.js'))
    if os.name=='nt':
        for base in (Path(os.environ.get('LOCALAPPDATA',''))/'Programs'/'Microsoft VS Code',Path('D:/Microsoft VS Code')):
            candidates.extend(base.glob('*/resources/app/extensions/markdown-language-features/markdown-editor-out/katex-*.js'))
    if not candidates: raise FileNotFoundError('VS Code bundled KaTeX module not found')
    return sorted(candidates,key=lambda p:p.stat().st_mtime,reverse=True)[0]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('markdown',nargs='+'); a=ap.parse_args()
    script=Path(__file__).with_name('validate_vscode_markdown.mjs')
    result=subprocess.run(['node',str(script),str(find_katex()),*a.markdown],check=False)
    return result.returncode
if __name__=='__main__': raise SystemExit(main())
