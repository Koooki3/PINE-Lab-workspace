---
schema_version: "1.0"
id: "PROMPT-20260818-170000"
name: "DROID 控制一图流"
slug: "droid-control-one-page-flow"
description: "用一张中文流程图概括 DROID 与 openpi 的观测、推理、动作块执行和评估闭环。"
category: ["education", "coding"]
tags: ["droid", "openpi", "control-flow", "visualization"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-18T17:00:00+08:00"
updated_at: "2026-08-18T17:00:00+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: "快速理解 DROID 真机控制全链路。"
expected_output: "一张带源码映射和安全边界的中文闭环图。"
variables: []
dependencies: ["openpi DROID example"]
notes: "原始提示词逐字保存。"
source_prompt: |-
  droid控制一图流
normalized_prompt: |-
  生成 DROID openpi 控制闭环的一图式中文流程说明。
---

# DROID 控制一图流

## 2. 完整提示词 / Full Prompt

```text
droid控制一图流
```

## 5. 预期输出 / Expected Output

单张、可直接阅读的 DROID 控制闭环图。
