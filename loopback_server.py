import time

import numpy as np

from openpi.serving.websocket_policy_server import WebsocketPolicyServer
from openpi_client.base_policy import BasePolicy


class DummyPolicy(BasePolicy):
    """不加载模型，只根据输入返回固定模拟动作。"""

    def infer(self, obs: dict) -> dict:
        start = time.perf_counter()

        print("\n收到一条观测")
        print("字段:", list(obs.keys()))

        state = obs["state"]
        image = obs["image"]
        prompt = obs["prompt"]

        print("state:", state.shape, state.dtype, state)
        print("image:", image.shape, image.dtype)
        print("prompt:", prompt)

        # 模拟未来 5 个控制步，每步 3 维动作。
        actions = np.array(
            [
                [0.10, 0.00, 0.00],
                [0.10, 0.01, 0.00],
                [0.10, 0.02, 0.00],
                [0.05, 0.02, 0.00],
                [0.00, 0.00, 0.00],
            ],
            dtype=np.float32,
        )

        elapsed_ms = (time.perf_counter() - start) * 1000

        return {
            "actions": actions,
            "message": "dummy policy response",
            "policy_timing": {
                "infer_ms": elapsed_ms,
            },
        }


if __name__ == "__main__":
    policy = DummyPolicy()

    server = WebsocketPolicyServer(
        policy=policy,
        host="127.0.0.1",
        port=8000,
        metadata={
            "policy_name": "dummy-policy",
            "action_shape": [5, 3],
            "description": "Local loopback test without model weights",
        },
    )

    print("假策略服务器已启动：ws://127.0.0.1:8000")
    print("按 Ctrl+C 停止")
    server.serve_forever()