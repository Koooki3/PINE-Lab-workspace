---
schema_version: "1.0"
id: "PROMPT-YYYYMMDD-HHMMSS"
name: "<提示词名称>"
slug: "<prompt-name-in-kebab-case>"
description: >
  <1-3 句话说明作用、问题与用途。>
category: ["<主分类>", "<子分类>"]
tags: ["<tag-1>", "<tag-2>"]
language: ["zh-CN"]
model:
  provider: "OpenAI"
  model_name: "Codex"
  model_version: null
  mode: null
model_parameters:
  temperature: null
  top_p: null
  max_tokens: null
  other: {}
created_at: "YYYY-MM-DDTHH:MM:SS+08:00"
updated_at: "YYYY-MM-DDTHH:MM:SS+08:00"
timezone: "Asia/Shanghai"
source:
  type: "user_input"
  conversation_id: null
  original_author: "User"
  source_url: null
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  <何时使用。>
expected_output: >
  <预期输出。>
variables: []
dependencies: ["none"]
notes: >
  <限制、技巧与问题。>
source_prompt: |-
  <用户原始输入，完全不修改>
normalized_prompt: |-
  <可选的复用版本；不得覆盖 source_prompt>
---

# <提示词名称>

## 1. 基本作用 / Purpose

<用途、场景、用户、输入与输出。>

## 2. 完整提示词 / Full Prompt

```text
<原样保存完整提示词，不摘要、不省略、不改写。>
```

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

1. 准备依赖材料。
2. 替换变量。
3. 提交完整提示词。
4. 检查输出。

## 5. 预期输出 / Expected Output

<语言、格式、结构、详细程度、引用、表格和文件要求。>

## 6. 模型信息 / Model Information

- **Provider:** OpenAI
- **Model:** Codex
- **Model Version:** N/A
- **Mode:** N/A

## 7. 测试记录 / Test History

### Test 1

- **Date:** YYYY-MM-DD
- **Model:** Codex
- **Result:** Not tested
- **Notes:** 初始归档。

## 8. 修改记录 / Changelog

### v1.0.0 — YYYY-MM-DD

- 创建初始版本并保存用户原始完整提示词。

## 9. 备注 / Notes

<补充说明。>
