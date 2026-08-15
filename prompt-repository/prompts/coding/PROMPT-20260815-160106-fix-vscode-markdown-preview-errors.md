---
schema_version: "1.0"
id: "PROMPT-20260815-160106"
name: "修复 VS Code Markdown 报错与预览失败"
slug: "fix-vscode-markdown-preview-errors"
description: >
  修复仓库生成 Markdown 在 VS Code 中的诊断错误和预览失败，并将兼容性检查写入后续生成流程。
category: ["coding", "document-conversion"]
tags: ["vscode", "markdown", "katex", "validation"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-15T16:01:06+08:00"
updated_at: "2026-08-15T16:01:06+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  生成的论文或知识库 Markdown 在 VS Code 中出现公式诊断或无法预览时使用。
expected_output: >
  可被 VS Code Markdown 预览和 KaTeX 严格解析的文件，以及阻止问题复发的自动验证。
variables: []
dependencies: ["VS Code", "references Markdown", "PDF 转换技能"]
notes: >
  不通过关闭诊断掩盖错误，应修复生成内容并加入质量门禁。
source_prompt: |-
  用vscode打开.md文件时发现有很多报错，并且无法预览，请解决这些报错并在之后避免这些问题
normalized_prompt: |-
  定位并修复 VS Code 中 Markdown 文件的全部解析与公式预览错误，更新生成器和验收逻辑，确保后续生成自动通过同版本 VS Code 的严格预览验证。
---

# 修复 VS Code Markdown 报错与预览失败

## 1. 基本作用 / Purpose

修复生成 Markdown 的结构和公式兼容性，并建立持续验证。

## 2. 完整提示词 / Full Prompt

```text
用vscode打开.md文件时发现有很多报错，并且无法预览，请解决这些报错并在之后避免这些问题
```

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

在 VS Code 中出现 Markdown 或 KaTeX 诊断时运行兼容性检查并修复生成源。

## 5. 预期输出 / Expected Output

零 KaTeX 错误、可正常预览的 Markdown，以及自动回归检查。

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

验证目标为 VS Code 自带 KaTeX 的严格模式。
