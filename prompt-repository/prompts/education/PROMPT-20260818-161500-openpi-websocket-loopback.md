---
schema_version: "1.0"
id: "PROMPT-20260818-161500"
name: "openpi-client WebSocket 假策略回环实验"
slug: "openpi-websocket-loopback"
description: "指导完成客户端发送观测、假策略服务器返回模拟动作、客户端解析动作的回环实验。"
category: ["education", "coding"]
tags: ["openpi-client", "websocket", "loopback", "robotics"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-18T16:15:00+08:00"
updated_at: "2026-08-18T16:15:00+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: "在不加载模型权重和不连接真机的情况下验证 openpi WebSocket 推理协议。"
expected_output: "两个终端可运行的假服务器与客户端步骤，以及成功判据和注意事项。"
variables: []
dependencies: ["conda kooki", "openpi-client", "websockets"]
notes: "原始提示词逐字保存。"
source_prompt: |-
  客户端发送 obs
    → 假策略服务器接收
    → 服务器返回模拟 actions
    → 客户端解析动作
normalized_prompt: |-
  给出 openpi-client WebSocket 假策略服务器回环实验的完整操作方法。
---

# openpi-client WebSocket 假策略回环实验

## 2. 完整提示词 / Full Prompt

```text
客户端发送 obs
  → 假策略服务器接收
  → 服务器返回模拟 actions
  → 客户端解析动作
```

## 5. 预期输出 / Expected Output

可安全执行的无模型、无真机网络回环实验。
