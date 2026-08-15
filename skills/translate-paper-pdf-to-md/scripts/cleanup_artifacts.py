from __future__ import annotations
import argparse, os, shutil, stat, tempfile
from pathlib import Path

def within(path: Path, parent: Path) -> bool:
    try: path.resolve().relative_to(parent.resolve()); return True
    except ValueError: return False
def remove(path: Path, allowed: Path, removed: list[str]):
    if not path.exists(): return
    if not within(path,allowed): raise RuntimeError(f'refusing cleanup outside {allowed}: {path}')
    if path.is_dir():
        def clear_readonly(func, target, exc):
            os.chmod(target,stat.S_IWRITE); func(target)
        shutil.rmtree(path,onexc=clear_readonly)
    else: path.unlink()
    removed.append(str(path))
def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); a=ap.parse_args(); root=Path(a.root).resolve(); removed=[]; ref=root/'references'; mdroot=ref/'Markdown'
    source_stems={p.stem for p in ref.glob('*.pdf')}
    if mdroot.exists():
        for d in mdroot.iterdir():
            if d.is_dir() and d.name not in source_stems: remove(d,mdroot,removed)
        for pattern in ('*_work','*.tmp','source_layout.txt','source_raw.txt','crops.json'):
            for p in mdroot.rglob(pattern): remove(p,mdroot,removed)
    remove(ref/'Knowledge graph'/'PINE.docx',root,removed)
    remove(root/'tmp',root,removed)
    remove(root/'.tools'/'pdf-md-env',root,removed)
    temp_root=Path(tempfile.gettempdir()).resolve()
    for name in ('pine-pdf-md','pine-pdf-latex','pine-markitdown-qa'):
        remove(temp_root/name,temp_root,removed)
    tools_dir=root/'.tools'
    if tools_dir.exists() and not any(tools_dir.iterdir()): tools_dir.rmdir(); removed.append(str(tools_dir))
    print(f'removed={len(removed)}'); [print('  '+x) for x in removed]; return 0
if __name__=='__main__': raise SystemExit(main())
