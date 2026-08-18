---
schema_version: "1.0"
id: "PROMPT-20260818-173000"
name: "构建本机 Policy Server 端到端单测"
slug: "local-policy-server-integration-test"
description: "在仓库中构建本机 openpi Policy Server 集成测试并生成七项运行证据。"
category: ["coding", "education"]
tags: ["openpi", "policy-server", "integration-test", "latency", "safety"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-18T17:30:00+08:00"
updated_at: "2026-08-18T17:30:00+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: "验证本机服务器网络栈、客户端协议、动作块、延迟、录像和断连安全停止。"
expected_output: "可运行 pytest、JSON/Markdown 证据和 MP4 回放。"
variables: []
dependencies: ["openpi WebsocketPolicyServer", "openpi-client", "pytest", "imageio-ffmpeg"]
notes: "合并用户连续两条消息为一个完整任务，逐字保存两部分输入。"
source_prompt: |-
  在仓库中将本机作为Policy Server构建一个单测，完成：
  1. 一条真实 Policy Server 启动记录
  2. 一次客户端成功连接
  3. 一条完整观测字段及 shape 清单
  4. 一个动作块的 shape、dtype、范围
  5. 一段执行回放视频
  6. 平均和 P95 推理延迟
  7. 一次主动断开后的安全停止结果
normalized_prompt: |-
  构建本机 openpi Policy Server 端到端集成测试，使用真实 WebSocket 网络栈并生成七类可检查证据。
---

# 构建本机 Policy Server 端到端单测

## 2. 完整提示词 / Full Prompt

```text
在仓库中将本机作为Policy Server构建一个单测，完成：
1. 一条真实 Policy Server 启动记录
2. 一次客户端成功连接
3. 一条完整观测字段及 shape 清单
4. 一个动作块的 shape、dtype、范围
5. 一段执行回放视频
6. 平均和 P95 推理延迟
7. 一次主动断开后的安全停止结果
```

## 5. 预期输出 / Expected Output

通过 pytest 验证，并保留启动、连接、协议、动作、视频、延迟与安全停止证据。
