# openpi 学习路径

1. 先读 `openpi.md` 的“最小心智模型”和术语表，理解 VLA、观测、动作块、策略与本体。
2. 跑 `openpi-client` 的数组/图像单元测试，理解机器人侧只需要发送观测、接收动作。
3. 读 `policies/*_policy.py` 与 `transforms.py`，手工画出自己机器人字段到统一模型字段的映射。
4. 读 `training/data_loader.py` 和 `training/config.py`，用 fake dataset 走通形状与批处理，不先下载大数据或权重。
5. 对照 `models/pi0.py`，理解视觉语言前缀、状态/动作后缀、流匹配训练目标和 10 步 ODE 采样。
6. 再比较 `models/pi0_fast.py`，理解连续动作生成与 FAST 自回归 token 生成的差异。
7. 选择一个官方例子（优先 LIBERO 仿真），完成数据转换、统计量计算、小批训练和策略服务。
8. 最后接真机：先限幅、急停和离线回放，再低速闭环；不要直接把未经验证的动作送入执行器。

