---
schema_version: "1.0"
id: "PROMPT-20260815-183500"
name: "全仓库规范 Markdown Preview Enhanced 数学格式"
slug: "enforce-mpe-math-format"
description: >
  全量检查并修复仓库 Markdown，使数学和公式完全符合 Markdown Preview Enhanced 的 KaTeX/MathJax 要求，并强化相关 skill 的生成与输出规范。
category: ["coding", "document-conversion"]
tags: ["markdown-preview-enhanced", "katex", "mathjax", "latex", "validation"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-15T18:35:00+08:00"
updated_at: "2026-08-15T18:35:00+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  仓库 Markdown 需要统一数学定界符、LaTeX 兼容性与 MPE 渲染质量门禁时使用。
expected_output: >
  全仓库 Markdown 通过严格数学格式检查，相关 skill 自动约束后续转换、生成和导出。
variables: []
dependencies: ["Markdown Preview Enhanced", "KaTeX", "repository Markdown validator"]
notes: >
  原始提示词逐字保存；完整提示词放在 text 围栏中，避免其中的数学术语被当作待渲染公式。
source_prompt: |-
  由于Markdown Preview Enhanced中的数学要求为Math (KaTeX/MathJax)，因此需要完成对全仓库的.md文件做一次格式检查和更新，使之完全符合Markdown Preview Enhanced的要求，特别是数学和公式。检查并完成修改，然后更新相关skills进一步规范转换生成及输出的.md格式文件。
normalized_prompt: |-
  严格扫描全仓库 Markdown 的数学定界符、LaTeX 环境和 KaTeX 渲染兼容性，修复全部错误，并将相同规则固化到 PDF 转换、references 管理和提示词归档 skill。
---

# 全仓库规范 Markdown Preview Enhanced 数学格式

## 1. 基本作用 / Purpose

统一 Markdown Preview Enhanced 数学格式并建立可重复执行的严格质量门禁。

## 2. 完整提示词 / Full Prompt

```text
由于Markdown Preview Enhanced中的数学要求为Math (KaTeX/MathJax)，因此需要完成对全仓库的.md文件做一次格式检查和更新，使之完全符合Markdown Preview Enhanced的要求，特别是数学和公式。检查并完成修改，然后更新相关skills进一步规范转换生成及输出的.md格式文件。
```

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

修改或生成 Markdown 后运行仓库级 MPE 检查器，并修复所有数学和结构错误。

## 5. 预期输出 / Expected Output

- 全部公式严格通过 KaTeX。
- 不存在失配、旧式或逃逸的数学定界符与环境。
- 后续 skill 自动执行相同验收。

## 6. 模型信息 / Model Information

- **Provider:** OpenAI
- **Model:** Codex

## 7. 测试记录 / Test History

- **Date:** 2026-08-15
- **Result:** Success

## 8. 修改记录 / Changelog

### v1.0.0 — 2026-08-15

- 创建初始版本并保存原始完整提示词。

## 9. 备注 / Notes

KaTeX 作为默认兼容性基线；仅在明确需要时才允许记录 MathJax 专属依赖。
