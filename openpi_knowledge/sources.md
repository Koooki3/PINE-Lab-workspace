# openpi 来源台账

访问日期：2026-08-18。优先级依次为本地源码、仓库内已验证论文 Markdown、上游官方仓库/项目页、原始论文页面。

## 本地一手证据

- [L1] `openpi/README.md`：支持模型、硬件/系统要求、安装、检查点、微调和远程推理入口。
- [L2] `openpi/pyproject.toml`：Python 与精确依赖、JAX CUDA 版本、工作区包和 RLDS 可选组。
- [L3] `openpi/src/openpi/training/data_loader.py`、`config.py`、`transforms.py`：LeRobot/RLDS 数据入口、动作窗口、变换和归一化。
- [L4] `openpi/src/openpi/models/pi0.py`、`pi0_config.py`：π0/π0.5 的视觉语言前缀、动作专家、流匹配损失和采样 ODE。
- [L5] `openpi/src/openpi/models/pi0_fast.py`、`tokenizer.py`、`utils/fsq_tokenizer.py`：FAST 离散动作 token 路径。
- [L6] `openpi/src/openpi/policies/policy.py`、`policy_config.py`：原始观测到动作的运行时封装。
- [L7] `openpi/scripts/serve_policy.py`、`openpi/src/openpi/serving/websocket_policy_server.py`、`openpi/packages/openpi-client/`：策略服务、消息协议和轻量客户端。
- [L8] `openpi/scripts/train.py`、`train_pytorch.py`、`compute_norm_stats.py`：JAX/PyTorch 训练与统计量计算。

## 本地论文

- [P1] Black et al. *π0: A Vision-Language-Action Flow Model for General Robot Control*. arXiv:2410.24164v4. 本地阅读：`references/Markdown/2410.24164v4/2410.24164v4.md`；源 PDF：`references/2410.24164v4.pdf`。

## 官方网页与原始论文

- [W1] Physical Intelligence/openpi: https://github.com/Physical-Intelligence/openpi
- [W2] π0 项目页：https://www.pi.website/blog/pi0
- [W3] π0 论文：https://arxiv.org/abs/2410.24164
- [W4] π0.5 论文：https://arxiv.org/abs/2504.16054
- [W5] π0.5 项目页：https://www.pi.website/blog/pi05
- [W6] FAST action tokenization：https://www.pi.website/research/fast
- [W7] LeRobot：https://github.com/huggingface/lerobot
- [W8] DROID：https://droid-dataset.github.io/
- [W9] LIBERO：https://libero-project.github.io/
- [W10] ALOHA/ACT：https://tonyzhaozh.github.io/aloha/
- [W11] Open X-Embodiment：https://robotics-transformer-x.github.io/

## 证据规则

- 实现行为以 [L1]–[L8] 为准；论文动机和实验结论以 [P1]、[W3]、[W4] 为准。
- “适合本仓库/本机”的建议属于综合判断，不冒充论文结论。
- 版本、检查点和硬件要求会变化，升级源码后需重跑环境审计并更新提交号。

