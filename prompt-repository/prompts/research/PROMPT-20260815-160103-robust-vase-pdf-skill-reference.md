---
schema_version: "1.0"
id: "PROMPT-20260815-160103"
name: "参考 robust-vase PDF-To-MarkDown 技能"
slug: "robust-vase-pdf-skill-reference"
description: >
  提供 MinerU 驱动 PDF-To-MarkDown 技能仓库作为转换方案参考。
category: ["research", "document-conversion"]
tags: ["mineru", "pdf-to-markdown", "skill-reference"]
language: ["zh-CN", "en"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-15T16:01:03+08:00"
updated_at: "2026-08-15T16:01:03+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  设计多方法 PDF 转换方案时参考 MinerU 实现。
expected_output: >
  对该仓库方案的评估和适用集成。
variables: []
dependencies: ["https://github.com/robust-vase/PDF-To-MarkDown-skills"]
notes: >
  仅提供资源链接。
source_prompt: |-
  [https://github.com/robust-vase/PDF-To-MarkDown-skills](https://github.com/robust-vase/PDF-To-MarkDown-skills)
normalized_prompt: |-
  将 robust-vase/PDF-To-MarkDown-skills 纳入转换方案比较。
---

# 参考 robust-vase PDF-To-MarkDown 技能

## 1. 基本作用 / Purpose

提供 MinerU 方案参考。

## 2. 完整提示词 / Full Prompt

```text
[https://github.com/robust-vase/PDF-To-MarkDown-skills](https://github.com/robust-vase/PDF-To-MarkDown-skills)
```

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

纳入方案调研。

## 5. 预期输出 / Expected Output

适用性分析。

## 6. 模型信息 / Model Information

- **Provider:** OpenAI
- **Model:** Codex

## 7. 测试记录 / Test History

- **Date:** 2026-08-15
- **Result:** Success

## 8. 修改记录 / Changelog

### v1.0.0 — 2026-08-15

- 创建初始版本。

## 9. 备注 / Notes

无。
