---
schema_version: "1.0"
id: "PROMPT-20260815-160108"
name: "配置 Markdown Preview Enhanced 默认预览与仓库兼容检查"
slug: "configure-markdown-preview-enhanced-default"
description: >
  检查并修正仓库全部 Markdown 文件，使其符合 Markdown Preview Enhanced 的预览与编译要求，并将兼容性检查纳入相关仓库级 skill；同时配置 VS Code 默认直接使用 MPE 打开 Markdown 预览。
category: ["coding", "repository-maintenance"]
tags: ["markdown-preview-enhanced", "vscode", "markdown", "validation"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-15T16:01:08+08:00"
updated_at: "2026-08-15T16:01:08+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: "https://shd101wyy.github.io/markdown-preview-enhanced/#/"}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  需要统一仓库 Markdown 渲染质量，并让 VS Code 自动以 Markdown Preview Enhanced 预览 Markdown 文件时使用。
expected_output: >
  全部 Markdown 通过兼容性检查，相关 skill 固化检查规则，VS Code 工作区与用户级设置默认关联 MPE。
variables: []
dependencies: ["Markdown Preview Enhanced VS Code extension", "repository Markdown validator"]
notes: >
  原始提示词逐字保存；预览模式采用 MPE 的 Previews Only，并保留异常文件可回到编辑器排错的能力。
source_prompt: |-
  我将使用Markdown Preview Enhanced（[https://shd101wyy.github.io/markdown-preview-enhanced/#/](https://shd101wyy.github.io/markdown-preview-enhanced/#/)）作为我在vscode中的默认Markdown预览工具，即打开任意.md格式文件时默认用Markdown Preview Enhanced给出预览结果，不需要我再操作切换到预览视图，除非存在报错无法正常生成预览视图。完成两步操作：1、检查确保仓库中当前所有.md格式文件符合Markdown Preview Enhanced预览、编译标准，如有误则修正，检查完成后将此规则补充进相关skills中；2、配置好本地vscode的默认设置；
normalized_prompt: |-
  全量验证并修复仓库 Markdown 的 MPE、UTF-8、YAML、围栏、资源链接与 KaTeX 兼容性，将该质量门禁写入相关仓库级 skill，并将 VS Code 的 .md 文件默认编辑器配置为 Markdown Preview Enhanced 的 Previews Only 模式。
---

# 配置 Markdown Preview Enhanced 默认预览与仓库兼容检查

## 1. 基本作用 / Purpose

统一仓库 Markdown 的 MPE 渲染标准，并配置 VS Code 自动打开增强预览。

## 2. 完整提示词 / Full Prompt

```text
我将使用Markdown Preview Enhanced（[https://shd101wyy.github.io/markdown-preview-enhanced/#/](https://shd101wyy.github.io/markdown-preview-enhanced/#/)）作为我在vscode中的默认Markdown预览工具，即打开任意.md格式文件时默认用Markdown Preview Enhanced给出预览结果，不需要我再操作切换到预览视图，除非存在报错无法正常生成预览视图。完成两步操作：1、检查确保仓库中当前所有.md格式文件符合Markdown Preview Enhanced预览、编译标准，如有误则修正，检查完成后将此规则补充进相关skills中；2、配置好本地vscode的默认设置；
```

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

在仓库新增或修改 Markdown 后运行 MPE 全量检查；VS Code 打开 `.md` 时由 MPE 直接显示预览。

## 5. 预期输出 / Expected Output

- 仓库 Markdown 零兼容性错误。
- 相关 skill 自动执行 MPE 质量门禁。
- VS Code 用户级与工作区级默认使用 MPE。

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

默认解析器为 markdown-it，数学渲染器为 KaTeX。
