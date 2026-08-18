# 本机 openpi Policy Server 单测报告

生成时间：2026-08-18T09:57:49.874780+00:00

## 七项验收结果

1. Policy Server 启动：`healthz_passed`，PID `12788`，端口 `63570`。
2. 客户端连接：`connected_and_metadata_received`。
3. 完整观测字段与 shape：见下节。
4. 动作块：shape `[10, 8]`，dtype `float32`，范围 `[-0.248550, 1.000000]`。
5. 回放视频：`openpi_knowledge/evidence/local_policy_server_test/execution_replay.mp4`，共 `30` 帧。
6. 推理延迟：平均 `1.952 ms`，P95 `4.363 ms`。
7. 主动断开安全停止：`safe_stop_latched`，原因 `policy_connection_closed_by_client`，安全动作全零 `True`。

## 观测字段

- `observation/exterior_image_1_left`: `{"shape": [224, 224, 3], "dtype": "uint8", "min": 0.0, "max": 220.0}`
- `observation/wrist_image_left`: `{"shape": [224, 224, 3], "dtype": "uint8", "min": 0.0, "max": 220.0}`
- `observation/joint_position`: `{"shape": [7], "dtype": "float32", "min": -0.20000000298023224, "max": 0.20000000298023224}`
- `observation/gripper_position`: `{"shape": [1], "dtype": "float32", "min": 0.0, "max": 0.0}`
- `prompt`: `{"type": "str", "value": "move the end effector safely"}`

## 边界

本测试使用真实 `WebsocketPolicyServer` 和 `WebsocketClientPolicy`，但策略为确定性测试替身，未加载 π0/π0.5 权重，也未驱动真实机器人。它验证网络协议和安全控制外壳，不代表模型推理或真机控制验收。
