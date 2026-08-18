---
schema_version: "1.0"
id: "PROMPT-20260818-163500"
name: "查找 openpi 完整控制代码参考"
slug: "openpi-control-code-reference"
description: "盘点 openpi 仓库中仿真与真机完整控制代码参考及调用链。"
category: ["education", "coding"]
tags: ["openpi", "control", "aloha", "droid", "libero"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-18T16:35:00+08:00"
updated_at: "2026-08-18T16:35:00+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: "选择可复用的 openpi 控制示例。"
expected_output: "控制示例清单、完整程度、阅读顺序与推荐入口。"
variables: []
dependencies: ["local openpi source"]
notes: "原始提示词逐字保存。"
source_prompt: |-
  代码库中有没有控制的完整代码参考
normalized_prompt: |-
  检查 openpi 代码库是否包含完整的机器人或仿真控制示例，并说明使用方式。
---

# 查找 openpi 完整控制代码参考

## 2. 完整提示词 / Full Prompt

```text
代码库中有没有控制的完整代码参考
```

## 5. 预期输出 / Expected Output

列出本地源码中最接近完整闭环的控制入口和依赖关系。
