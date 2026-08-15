from __future__ import annotations
import argparse
from pathlib import Path

MARKERS=('Ã','Â','â€','ðŸ','ï»¿','�')
def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('paths',nargs='+'); a=ap.parse_args(); errors=[]
    files=[]
    for raw in a.paths:
        path=Path(raw); files.extend(path.rglob('*.md') if path.is_dir() else [path])
    for path in files:
        try: text=path.read_text(encoding='utf-8',errors='strict')
        except UnicodeError as exc: errors.append(f'{path}: invalid UTF-8: {exc}'); continue
        for line_no,line in enumerate(text.splitlines(),1):
            bad=[ch for ch in line if (ord(ch)<32 and ch!='\t') or 0x80<=ord(ch)<=0x9f or 0xe000<=ord(ch)<=0xf8ff]
            markers=[m for m in MARKERS if m in line]
            if bad or markers: errors.append(f'{path}:{line_no}: invalid characters={len(bad)} markers={markers}')
    print(f'files={len(files)} encoding_errors={len(errors)}')
    for error in errors: print('ERROR '+error)
    return bool(errors)
if __name__=='__main__': raise SystemExit(main())
