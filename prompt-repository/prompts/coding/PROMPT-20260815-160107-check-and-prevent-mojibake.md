---
schema_version: "1.0"
id: "PROMPT-20260815-160107"
name: "检查并预防 Markdown 乱码"
slug: "check-and-prevent-mojibake"
description: >
  检查仓库生成 Markdown 中的乱码、控制字符和异常字体映射，并建立后续自动预防逻辑。
category: ["coding", "document-conversion"]
tags: ["mojibake", "utf-8", "pdf", "validation"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-15T16:01:07+08:00"
updated_at: "2026-08-15T16:01:07+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  PDF 转换结果或知识库 Markdown 出现乱码、异常字形或编码问题时使用。
expected_output: >
  清理后的 UTF-8 Markdown，以及阻止乱码再次进入成果的编码质量门禁。
variables: []
dependencies: ["references Markdown", "PDF 转换技能"]
notes: >
  不猜测无法可靠恢复的字体映射内容，保留页图并明确标记省略。
source_prompt: |-
  检查乱码，并在之后避免这些问题
normalized_prompt: |-
  全面扫描并修复生成 Markdown 中的乱码、控制字符和私用区字形，更新转换与验收逻辑以自动阻止问题复发。
---

# 检查并预防 Markdown 乱码

## 1. 基本作用 / Purpose

维护 PDF 转换与知识库 Markdown 的 UTF-8 编码完整性。

## 2. 完整提示词 / Full Prompt

```text
检查乱码，并在之后避免这些问题
```

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

转换或更新 references 后运行严格编码检查。

## 5. 预期输出 / Expected Output

零乱码的 Markdown 和自动编码回归检查。

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

编码统一使用 UTF-8。
