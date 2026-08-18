---
schema_version: "1.0"
id: "PROMPT-20260818-160500"
name: "openpi-client 数组图像实验操作指南"
slug: "openpi-client-experiment-guide"
description: >
  说明如何自行运行 openpi-client 的数组和图像单元测试，并理解机器人端观测请求与动作响应的数据流。
category: ["education", "coding"]
tags: ["openpi-client", "unit-test", "websocket", "robotics"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-18T16:05:00+08:00"
updated_at: "2026-08-18T16:05:00+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  初学者在本地验证 openpi-client 数据协议和图像预处理时使用。
expected_output: >
  可自行执行的步骤、流程、预期结果与注意事项。
variables: []
dependencies: ["conda kooki", "openpi-client", "pytest"]
notes: "原始提示词逐字保存。"
source_prompt: |-
  “跑 openpi-client 的数组/图像单元测试，理解机器人侧只需要发送观测、接收动作”怎样具体去完成实验？我自己来操作，告诉我具体步骤，流程和注意事项即可
normalized_prompt: |-
  给出自行运行 openpi-client 数组序列化与图像处理测试、观察数据协议并进一步完成客户端回环实验的具体操作指南。
---

# openpi-client 数组图像实验操作指南

## 2. 完整提示词 / Full Prompt

```text
“跑 openpi-client 的数组/图像单元测试，理解机器人侧只需要发送观测、接收动作”怎样具体去完成实验？我自己来操作，告诉我具体步骤，流程和注意事项即可
```

## 预期输出 / Expected Output

提供命令、代码定位、预期结果、数据流解释和安全注意事项。
