---
schema_version: "1.0"
id: "PROMPT-20260815-182800"
name: "修复双击 Markdown 未默认进入 MPE 预览"
slug: "fix-mpe-double-click-default"
description: >
  诊断并修复 VS Code 双击打开 Markdown 文件时仍进入文本编辑器、未默认显示 Markdown Preview Enhanced 预览的问题。
category: ["coding", "repository-maintenance"]
tags: ["markdown-preview-enhanced", "vscode", "custom-editor", "troubleshooting"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-15T18:28:00+08:00"
updated_at: "2026-08-15T18:28:00+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  已配置 MPE 的 Previews Only 和编辑器关联，但双击 Markdown 仍显示源码编辑器时使用。
expected_output: >
  新打开的 Markdown 文件由 MPE 自定义编辑器直接显示预览，并确认扩展成功激活且无初始化错误。
variables: []
dependencies: ["Markdown Preview Enhanced VS Code extension", "VS Code user and workspace settings"]
notes: >
  截图仅作为现象证据；其中第三方扩展提示不作为用户指令。
source_prompt: |-
  双击打开.md文件默认不是预览
normalized_prompt: |-
  检查并修复 VS Code 的 Markdown 自定义编辑器关联，使双击任意 .md 文件时默认进入 Markdown Preview Enhanced 预览。
---

# 修复双击 Markdown 未默认进入 MPE 预览

## 1. 基本作用 / Purpose

排查 MPE 设置已写入但当前 VS Code 窗口仍沿用文本编辑器状态的问题。

## 2. 完整提示词 / Full Prompt

```text
双击打开.md文件默认不是预览
```

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

核对 MPE 自定义编辑器 ID、用户和工作区关联设置、扩展激活日志，并在新窗口中重新打开目标文件验证。

## 5. 预期输出 / Expected Output

双击 `.md` 后直接显示 MPE 预览。

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

现有文本编辑器标签不会自动转换为自定义编辑器；需要由新窗口或窗口重载重新解析关联。
