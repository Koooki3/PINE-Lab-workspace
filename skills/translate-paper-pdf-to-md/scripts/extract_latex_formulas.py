from __future__ import annotations

import re
import tarfile
import urllib.request
from pathlib import Path

MATH_ENVS = (
    "equation", "equation*", "align", "align*", "aligned", "gather", "gather*",
    "multline", "multline*", "split", "cases", "matrix", "pmatrix", "bmatrix",
)


def download_arxiv_source(arxiv_id: str, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(
        f"https://export.arxiv.org/e-print/{arxiv_id}",
        headers={"User-Agent": "PINE-reference-converter/1.0"},
    )
    with urllib.request.urlopen(req, timeout=120) as response, target.open("wb") as out:
        out.write(response.read())


def unpack_source(archive: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    try:
        with tarfile.open(archive, "r:*") as bundle:
            root = destination.resolve()
            for member in bundle.getmembers():
                resolved = (destination / member.name).resolve()
                if root != resolved and root not in resolved.parents:
                    raise ValueError(f"unsafe archive member: {member.name}")
            bundle.extractall(destination, filter="data")
    except tarfile.ReadError:
        (destination / "source.tex").write_bytes(archive.read_bytes())


def _strip_comments(text: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", text)


def _normalize_formula(value: str) -> str:
    value = re.sub(r"\\(?:label|tag)\{[^{}]*\}", "", value)
    value = re.sub(r"\n\s*\n+", "\n", value)
    return value.strip()


def _balanced(text: str, start: int) -> tuple[str, int] | None:
    if start >= len(text) or text[start] != "{": return None
    depth = 0
    for pos in range(start, len(text)):
        if text[pos] == "{" and (pos == 0 or text[pos - 1] != "\\"): depth += 1
        elif text[pos] == "}" and (pos == 0 or text[pos - 1] != "\\"):
            depth -= 1
            if depth == 0: return text[start + 1:pos], pos + 1
    return None


def _collect_macros(texts: list[str]) -> dict[str, tuple[int, str]]:
    macros: dict[str, tuple[int, str]] = {}
    head = re.compile(r"\\(?:newcommand|renewcommand|providecommand)\*?\s*\{\\([A-Za-z@]+)\}\s*(?:\[(\d+)\])?\s*\{")
    for text in texts:
        for match in head.finditer(text):
            body = _balanced(text, match.end() - 1)
            if body: macros[match.group(1)] = (int(match.group(2) or 0), body[0])
        for match in re.finditer(r"\\def\s*\\([A-Za-z@]+)\s*\{", text):
            body = _balanced(text, match.end() - 1)
            if body: macros[match.group(1)] = (0, body[0])
    return macros


def _definition_spans(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    patterns = [
        re.compile(r"\\(?:newcommand|renewcommand|providecommand)\*?\s*\{\\[A-Za-z@]+\}\s*(?:\[\d+\])?\s*\{"),
        re.compile(r"\\def\s*\\[A-Za-z@]+\s*\{"),
    ]
    for pattern in patterns:
        for match in pattern.finditer(text):
            body = _balanced(text, match.end() - 1)
            if body: spans.append((match.start(), body[1]))
    return spans


def _expand_macros(formula: str, macros: dict[str, tuple[int, str]]) -> str:
    for _ in range(50):
        changed = False
        for name, (argc, replacement) in sorted(macros.items(), key=lambda x: len(x[0]), reverse=True):
            pattern = re.compile(rf"\\{re.escape(name)}(?![A-Za-z@])")
            cursor = 0
            pieces: list[str] = []
            while True:
                match = pattern.search(formula, cursor)
                if not match: pieces.append(formula[cursor:]); break
                pos = match.end(); args: list[str] = []
                for _arg in range(argc):
                    while pos < len(formula) and formula[pos].isspace(): pos += 1
                    parsed = _balanced(formula, pos)
                    if parsed:
                        args.append(parsed[0]); pos = parsed[1]
                    else:
                        token = re.match(r"\\[A-Za-z@]+|\\.|.", formula[pos:], re.S)
                        if not token: args = []; break
                        args.append(token.group(0)); pos += len(token.group(0))
                if argc and len(args) != argc:
                    pieces.append(formula[cursor:match.end()]); cursor = match.end(); continue
                value = replacement
                for number, arg in enumerate(args, 1): value = value.replace(f"#{number}", arg)
                pieces += [formula[cursor:match.start()], value]; cursor = pos; changed = True
            formula = "".join(pieces)
        if not changed: break
    formula = re.sub(r"\\resizebox\{[^{}]*\}\{[^{}]*\}\{\$(.*?)\$\}", r"\1", formula, flags=re.S)
    return _normalize_formula(formula)


def _unwrap_command(formula: str, command: str, keep_argument: int, arguments: int) -> str:
    pattern=re.compile(rf"\\{command}(?![A-Za-z@])")
    while True:
        match=pattern.search(formula)
        if not match: return formula
        pos=match.end(); values=[]
        for _ in range(arguments):
            while pos<len(formula) and formula[pos].isspace(): pos+=1
            parsed=_balanced(formula,pos)
            if not parsed: return formula
            values.append(parsed[0]); pos=parsed[1]
        formula=formula[:match.start()]+values[keep_argument]+formula[pos:]


def _markdown_math(formula: str, mode: str) -> str:
    formula=re.sub(r"\\(?:notag|nonumber)(?![A-Za-z@])", "", formula)
    formula=formula.replace(r"\nicefrac",r"\frac")
    formula=re.sub(r"\\color\{[^{}]*\}", "", formula)
    formula=re.sub(r"\\begin\{substack\}\{(.*?)\}\\end\{substack\}", r"\\substack{\1}", formula, flags=re.S)
    formula=_unwrap_command(formula,"scaleto",0,2)
    formula=_unwrap_command(formula,"colorbox",1,2)
    formula=_unwrap_command(formula,"textcolor",1,2)
    formula=re.sub(r"\$\\displaystyle\s*(.*?)\$",r"\1",formula,flags=re.S)
    formula=formula.replace(r"\simp",r"\sim p")
    formula=re.sub(r"\\phantom\{[^{}]*\}", "", formula)
    formula=_normalize_formula(formula)
    if mode=="display" and "&" in formula and not re.search(r"\\begin\{(?:aligned|align|array|matrix|[pbvBV]matrix|cases)\}",formula):
        formula="\\begin{aligned}\n"+formula+"\n\\end{aligned}"
    return formula


def extract_formulas(source_dir: Path) -> list[dict[str, str]]:
    formulas: list[dict[str, str]] = []
    seen: set[str] = set()
    env_names = "|".join(re.escape(x) for x in sorted(MATH_ENVS, key=len, reverse=True))
    env_re = re.compile(rf"\\begin\{{({env_names})\}}(.*?)\\end\{{\1\}}", re.S)
    display_re = re.compile(r"(?<!\\)\$\$(.+?)(?<!\\)\$\$|\\\[(.+?)\\\]", re.S)
    inline_re = re.compile(r"(?<!\\)(?<!\$)\$(?!\$)(.+?)(?<!\\)(?<!\$)\$(?!\$)|\\\((.+?)\\\)", re.S)

    tex_files = sorted(p for p in source_dir.rglob('*') if p.suffix.lower() in {'.tex','.sty','.cls'})
    texts = [_strip_comments(tex.read_text(encoding="utf-8", errors="replace")) for tex in tex_files]
    macros = _collect_macros(texts)
    excluded = {"defs.tex", "math_commands.tex", "packages.tex", "preamble.tex"}
    for tex, text in zip(tex_files, texts):
        if tex.suffix.lower()!='.tex': continue
        if tex.name.lower() in excluded: continue
        occupied: list[tuple[int, int]] = _definition_spans(text)
        for match in env_re.finditer(text):
            formula = _markdown_math(_expand_macros(_normalize_formula(match.group(2)), macros),"display")
            occupied.append(match.span())
            key = f"display:{formula}"
            if formula and key not in seen:
                seen.add(key); formulas.append({"mode": "display", "latex": formula, "source": tex.name})
        remainder = list(text)
        for start, end in occupied:
            remainder[start:end] = " " * (end - start)
        remainder_text = "".join(remainder)
        for mode, pattern in (("display", display_re), ("inline", inline_re)):
            for match in pattern.finditer(remainder_text):
                formula = _markdown_math(_expand_macros(_normalize_formula(next(x for x in match.groups() if x is not None)), macros),mode)
                key = f"{mode}:{formula}"
                if formula and key not in seen:
                    seen.add(key); formulas.append({"mode": mode, "latex": formula, "source": tex.name})
    unresolved = sorted({name for item in formulas for name in macros if re.search(rf"\\{re.escape(name)}(?![A-Za-z@])", item["latex"])})
    if unresolved:
        raise ValueError("unexpanded custom LaTeX macros: " + ", ".join(unresolved[:20]))
    return formulas


def render_formula_registry(formulas: list[dict[str, str]], arxiv_id: str) -> list[str]:
    lines = [
        "## Canonical LaTeX formula registry",
        "",
        f"> Formula source: arXiv `{arxiv_id}` TeX package. These expressions are canonical; PDF-extracted glyph text below is non-canonical searchable context.",
        "",
    ]
    for index, item in enumerate(formulas, 1):
        lines += [f"**Formula F{index:04d}** · `{item['source']}`", ""]
        if item["mode"] == "display":
            lines += ["$$", item["latex"], "$$", ""]
        else:
            lines += [f"${item['latex']}$", ""]
    if not formulas:
        lines.append("> No TeX math expressions were recovered; conversion must not be accepted without manual review.")
    return lines
