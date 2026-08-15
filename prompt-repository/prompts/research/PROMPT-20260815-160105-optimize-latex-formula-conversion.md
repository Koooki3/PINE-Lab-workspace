---
schema_version: "1.0"
id: "PROMPT-20260815-160105"
name: "优化 PDF 数学公式 LaTeX 转换与知识库导出"
slug: "optimize-latex-formula-conversion"
description: >
  优化 references PDF 转换和知识库导出的数学公式处理，统一使用 LaTeX 格式并重新生成全部成果。
category: ["research", "document-conversion"]
tags: ["latex", "math-formula", "pdf-to-markdown", "knowledge-graph"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-15T16:01:05+08:00"
updated_at: "2026-08-15T16:01:05+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  需要确保论文、知识库和汇总 Markdown 中数学公式可用标准 LaTeX 渲染时使用。
expected_output: >
  重新转换的论文 Markdown、更新后的知识库与知识图谱，以及使用 LaTeX 公式的 PINE.md。
variables: []
dependencies: ["references 中的 PDF", "论文官方 TeX 源码"]
notes: >
  公式必须可追溯，并使用 Markdown 数学定界符。
source_prompt: |-
  转换逻辑和导出针对所有数学公式做一次优化，基于latex格式最终在.md文件中也用latex格式显示。重新做一次references中的pdf文件转换，重新生成知识库和知识图谱，重新导出PINE.md
normalized_prompt: |-
  优化 PDF 到 Markdown 的公式处理，从可靠来源恢复公式并统一为 LaTeX，重新转换全部 references PDF，随后重建知识库、知识图谱和 PINE.md，并完成验证与清理。
---

# 优化 PDF 数学公式 LaTeX 转换与知识库导出

## 1. 基本作用 / Purpose

建立可追溯、可渲染的数学公式转换与知识库导出流程。

## 2. 完整提示词 / Full Prompt

```text
转换逻辑和导出针对所有数学公式做一次优化，基于latex格式最终在.md文件中也用latex格式显示。重新做一次references中的pdf文件转换，重新生成知识库和知识图谱，重新导出PINE.md
```

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

在 references 中存在含公式 PDF，且需要重建知识成果时执行。

## 5. 预期输出 / Expected Output

全部论文的 LaTeX 公式 Markdown、更新后的知识库、知识图谱和 PINE.md。

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

数学公式使用 `$...$` 或 `$$...$$`。
