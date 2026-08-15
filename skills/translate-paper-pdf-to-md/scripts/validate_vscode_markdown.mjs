import fs from 'node:fs';
import { pathToFileURL } from 'node:url';

const [katexPath, ...files] = process.argv.slice(2);
if (!katexPath || files.length === 0) process.exit(2);
const katex = await import(pathToFileURL(katexPath).href);

const blank = match => match.replace(/[^\r\n]/g, ' ');

function maskNonRenderedMarkdown(source) {
  let text = source;
  text = text.replace(/^---\s*\r?\n[\s\S]*?\r?\n---\s*(?:\r?\n|$)/, blank);
  text = text.replace(/<!--[\s\S]*?-->/g, blank);
  text = text.replace(/^( {0,3})(`{3,}|~{3,})[^\n]*\n[\s\S]*?^\1\2\s*$/gm, blank);
  text = text.replace(/(`+)(?!`)([^\r\n]*?)\1(?!`)/g, blank);
  return text;
}

function isEscaped(text, index) {
  let slashes = 0;
  for (let i = index - 1; i >= 0 && text[i] === '\\'; i--) slashes++;
  return slashes % 2 === 1;
}

function lineAt(source, offset) {
  return source.slice(0, offset).split('\n').length;
}

function scanMath(source) {
  const text = maskNonRenderedMarkdown(source);
  const expressions = [];
  const errors = [];
  const occupied = new Uint8Array(text.length);

  for (let i = 0; i < text.length; i++) {
    if (text[i] !== '$' || isEscaped(text, i)) continue;
    const displayMode = text[i + 1] === '$';
    const width = displayMode ? 2 : 1;
    let close = -1;
    for (let j = i + width; j < text.length; j++) {
      if (!displayMode && (text[j] === '\n' || text[j] === '\r')) break;
      if (text[j] !== '$' || isEscaped(text, j)) continue;
      if (displayMode && text[j + 1] === '$') { close = j; break; }
      if (!displayMode && text[j + 1] !== '$' && text[j - 1] !== '$') { close = j; break; }
    }
    if (close < 0) {
      errors.push({ line: lineAt(source, i), expression: '', error: `unclosed ${displayMode ? '$$' : '$'} delimiter` });
      continue;
    }
    const value = text.slice(i + width, close);
    if (!value.trim()) {
      errors.push({ line: lineAt(source, i), expression: value, error: 'empty math expression' });
    } else if (!displayMode && (/^\s|\s$/.test(value))) {
      errors.push({ line: lineAt(source, i), expression: value, error: 'inline math must not start or end with whitespace' });
    } else {
      expressions.push({ displayMode, value: value.trim(), offset: i });
    }
    occupied.fill(1, i, Math.min(close + width, occupied.length));
    i = close + width - 1;
  }

  const legacy = /\\(?:\(|\)|\[|\])/g;
  for (const match of text.matchAll(legacy)) {
    if (!occupied[match.index]) errors.push({
      line: lineAt(source, match.index), expression: match[0],
      error: 'legacy math delimiter is disabled; use $...$ or $$...$$',
    });
  }
  const bareEnvironment = /\\begin\{(?:equation\*?|align\*?|alignat\*?|gather\*?|multline\*?|split|aligned|alignedat|gathered|matrix|[pbBvV]?matrix|cases|array)\}/g;
  for (const match of text.matchAll(bareEnvironment)) {
    if (!occupied[match.index]) errors.push({
      line: lineAt(source, match.index), expression: match[0],
      error: 'math environment is outside $/$$ delimiters',
    });
  }
  return { expressions, errors };
}

let failures = 0;
for (const file of files) {
  const source = fs.readFileSync(file, 'utf8');
  const { expressions, errors } = scanMath(source);
  for (const expression of expressions) {
    try {
      katex.renderToString(expression.value, {
        displayMode: expression.displayMode,
        throwOnError: true,
        strict: 'error',
        trust: false,
      });
    } catch (error) {
      errors.push({
        line: lineAt(source, expression.offset),
        expression: expression.value.slice(0, 160),
        error: String(error.message || error),
      });
    }
  }
  failures += errors.length;
  console.log(JSON.stringify({ file, formulas: expressions.length, errors }, null, errors.length ? 2 : 0));
}
process.exit(failures ? 1 : 0);
