---
schema_version: "1.0"
id: "PROMPT-20260818-164500"
name: "生成 DROID 控制代码中文注释版"
slug: "droid-control-chinese-comments"
description: "基于用户提供的 DROID openpi 控制代码生成保留原意的中文注释版本。"
category: ["coding", "education"]
tags: ["openpi", "droid", "chinese-comments", "robot-control"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-18T16:45:00+08:00"
updated_at: "2026-08-18T16:45:00+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: "供中文初学者阅读和调试 DROID 真机控制流程。"
expected_output: "带完整中文说明和安全提示的独立 Python 文件。"
variables: []
dependencies: ["user attached pasted-text.txt", "openpi DROID example"]
notes: "代码附件作为任务输入，原始请求逐字保存。"
source_prompt: |-
  给一个含中文注释的新版本
normalized_prompt: |-
  以用户提供的 DROID 控制脚本为基线，创建保留原文件的中文注释版本。
---

# 生成 DROID 控制代码中文注释版

## 2. 完整提示词 / Full Prompt

```text
给一个含中文注释的新版本
```

## 5. 预期输出 / Expected Output

独立、可检查、带中文注释的 DROID 控制脚本。
