import numpy as np

from openpi_client.websocket_client_policy import WebsocketClientPolicy


def main() -> None:
    policy = WebsocketClientPolicy(
        host="127.0.0.1",
        port=8000,
    )

    print("服务器元数据:")
    print(policy.get_server_metadata())

    obs = {
        "state": np.array([0.1, 0.2, 0.3], dtype=np.float32),
        "image": np.random.randint(
            0,
            256,
            size=(224, 224, 3),
            dtype=np.uint8,
        ),
        "prompt": "pick up the cup",
    }

    print("\n发送观测:")
    print("state:", obs["state"].shape, obs["state"].dtype)
    print("image:", obs["image"].shape, obs["image"].dtype)
    print("prompt:", obs["prompt"])

    result = policy.infer(obs)

    print("\n收到服务器响应:")
    print("字段:", list(result.keys()))
    print("message:", result["message"])
    print("actions:")
    print(result["actions"])
    print("actions shape:", result["actions"].shape)
    print("actions dtype:", result["actions"].dtype)
    print("server timing:", result.get("server_timing"))
    print("policy timing:", result.get("policy_timing"))

    assert result["actions"].shape == (5, 3)
    assert result["actions"].dtype == np.float32
    assert np.isfinite(result["actions"]).all()

    print("\nWebSocket 回环验证通过")


if __name__ == "__main__":
    main()