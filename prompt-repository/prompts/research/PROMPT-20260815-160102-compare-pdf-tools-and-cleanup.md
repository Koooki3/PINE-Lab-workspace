---
schema_version: "1.0"
id: "PROMPT-20260815-160102"
name: "参考 MarkItDown 并完善转换检查与清理"
slug: "compare-pdf-tools-and-cleanup"
description: >
  参考 MarkItDown 等第三方工具，检查转换结果并完善过期文件和过程文件自动清理。
category: ["research", "document-conversion"]
tags: ["markitdown", "pdf", "cleanup", "quality-assurance"]
language: ["zh-CN", "en"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-15T16:01:02+08:00"
updated_at: "2026-08-15T16:01:02+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  比较 PDF 转换工具并强化质量门禁和清理逻辑时使用。
expected_output: >
  多工具比较、源 PDF 对照、完善后的自动清理技能。
variables: []
dependencies: ["https://dashen-tech.com/dev-tools/markitdown-guide/"]
notes: >
  目标完成后必须删除过期和过程文件。
source_prompt: |-
  其他可用的工具或第三方库参考（[https://dashen-tech.com/dev-tools/markitdown-guide/](https://dashen-tech.com/dev-tools/markitdown-guide/)）。注意转换后要对照源文件pdf做一次效果检查，上述目标完成后注意删除过期文件，如果当前仓库的过期文件、过程文件的自动清理不完善请补充skill完善。
normalized_prompt: |-
  评估 MarkItDown 等第三方工具，转换后与源 PDF 对照，并完善技能的过期/过程文件自动清理。
---

# 参考 MarkItDown 并完善转换检查与清理

## 1. 基本作用 / Purpose

比较工具并强化清理与验收。

## 2. 完整提示词 / Full Prompt

```text
其他可用的工具或第三方库参考（[https://dashen-tech.com/dev-tools/markitdown-guide/](https://dashen-tech.com/dev-tools/markitdown-guide/)）。注意转换后要对照源文件pdf做一次效果检查，上述目标完成后注意删除过期文件，如果当前仓库的过期文件、过程文件的自动清理不完善请补充skill完善。
```

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

用于转换方案评估与维护。

## 5. 预期输出 / Expected Output

工具比较、质量报告和自动清理。

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
