---
schema_version: "1.0"
id: "PROMPT-20260815-160104"
name: "设计最优多引擎 PDF 转换方法"
slug: "design-optimal-multi-engine-pdf-conversion"
description: >
  综合用户提供的多个资源，通过实测比较设计最优 PDF 到 Markdown 转换方法。
category: ["research", "document-conversion"]
tags: ["multi-engine", "pdf-to-markdown", "benchmark"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-15T16:01:04+08:00"
updated_at: "2026-08-15T16:01:04+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  需要从多个解析工具中选择和组合最优流程时使用。
expected_output: >
  经实测的主引擎、后备引擎、升级条件和质量门禁。
variables: []
dependencies: ["用户提供的 PDF 转换资源"]
notes: >
  强调多方法比对而非单一工具偏好。
source_prompt: |-
  根据我给你的资源，多方法比对设计一个最优转换方法
normalized_prompt: |-
  实测比较用户提供的 PDF 转换方案，设计并固化最优多引擎流程。
---

# 设计最优多引擎 PDF 转换方法

## 1. 基本作用 / Purpose

建立基于证据的转换引擎选择策略。

## 2. 完整提示词 / Full Prompt

```text
根据我给你的资源，多方法比对设计一个最优转换方法
```

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

提供候选工具和样本文档后执行。

## 5. 预期输出 / Expected Output

多引擎最优方案与验证结果。

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
