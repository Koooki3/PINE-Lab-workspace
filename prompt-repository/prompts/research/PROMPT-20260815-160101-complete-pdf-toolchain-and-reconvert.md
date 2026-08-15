---
schema_version: "1.0"
id: "PROMPT-20260815-160101"
name: "补全 PDF 工具链并重新转换核验"
slug: "complete-pdf-toolchain-and-reconvert"
description: >
  安装缺失的 Poppler/ImageMagick，重新转换 references，并与源 PDF 对照检查。
category: ["research", "document-conversion"]
tags: ["poppler", "imagemagick", "quality-assurance"]
language: ["zh-CN", "en"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-15T16:01:01+08:00"
updated_at: "2026-08-15T16:01:01+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  PDF 转换环境缺失或后备转换质量需要重新核验时使用。
expected_output: >
  完整工具环境、重转文件和源 PDF 对照结论。
variables: []
dependencies: ["Poppler", "ImageMagick"]
notes: >
  要求重新转换并对照源文件。
source_prompt: |-
  注意到“原技能依赖 Poppler/ImageMagick，但本机只有失效的 pdfinfo 包装器，缺少 pdftotext 与 pdftocairo”补全环境后重新更新一遍转换，然后对照源文件pdf判断转换效果
normalized_prompt: |-
  补全 Poppler/ImageMagick 环境，强制重新转换全部 references PDF，并与源 PDF 做自动和视觉质量检查。
---

# 补全 PDF 工具链并重新转换核验

## 1. 基本作用 / Purpose

修复环境并重做转换质量验收。

## 2. 完整提示词 / Full Prompt

```text
注意到“原技能依赖 Poppler/ImageMagick，但本机只有失效的 pdfinfo 包装器，缺少 pdftotext 与 pdftocairo”补全环境后重新更新一遍转换，然后对照源文件pdf判断转换效果
```

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

在工具缺失时执行。

## 5. 预期输出 / Expected Output

成功重转与对照报告。

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
