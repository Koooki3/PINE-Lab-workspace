# kooki 环境审计

审计日期：2026-08-18。

## 主环境约定

本仓库日常 Python 命令默认使用 Conda 环境 `kooki`，解释器为 `C:\anaconda\envs\kooki\python.exe`。openpi 相关命令也先在该环境做源码、数据和客户端验证。

## 机器与上游边界

- 操作系统：Windows 11；上游 openpi 只声明测试 Ubuntu 22.04。
- Python：3.12.9；核心项目声明 Python 3.11+，但 RLDS 组的 TensorFlow 2.15 只有 CPython 3.11 wheel。
- GPU：RTX 4060 Laptop，8 GB；上游推理要求严格大于 8 GB。
- JAX：Windows 可安装 CPU wheel，但 `jax[cuda12]` 不是受支持的原生 Windows CUDA 路径。

结论：`kooki` 可作为客户端、源码、数据工具和 CPU 冒烟环境，不能认证为完整 GPU 训练/推理环境。完整路径应建立 Ubuntu 22.04/WSL2 + Python 3.11 + `uv sync` 的独立锁定环境。

## 已执行的补全

- 安装 `uv`、`pynvml`、`hatchling`、`editables`。
- editable 安装本地 `openpi` 与 `openpi-client`。
- 安装 JAX 0.5.3 CPU wheel、Flax 0.10.2、Equinox、Orbax、Chex、Tyro、SentencePiece、Gym ALOHA 等 Windows 可用核心依赖。
- 固定 NumPy 1.26.4，以满足 openpi 的 `<2.0.0` 约束。
- `openpi-client` 单元测试 21 项通过。

## 未完成与冲突

- LeRobot 锁定 Git 提交因 GitHub 连接超时未能安装；因此训练数据加载模块不能标为完整。
- RLDS/DROID 组不应安装到 Python 3.12 主环境。
- 原环境的 `surya-ocr`、`swanlab`、`torchaudio` 与 openpi 的 Pillow/Rich/Transformers/Torch 固定版本存在冲突。共享单环境无法同时满足全部声明，应为完整 openpi 运行建立隔离环境，避免继续破坏主环境中的其他工作流。

## 验收命令

```powershell
conda run -n kooki python -m pip check
conda run -n kooki python -c "import jax; print(jax.devices())"
conda run -n kooki python -m pytest openpi/packages/openpi-client/src/openpi_client -q
```

只有 `pip check` 无冲突、LeRobot 可导入、JAX 枚举到目标 GPU、fake-data 模型测试和检查点推理均通过，才可称为完整支持。
