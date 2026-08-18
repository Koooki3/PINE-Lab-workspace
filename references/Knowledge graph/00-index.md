# PINE References 知识库

## 定位

本知识库把当前四篇论文组织成一条面向初学者的机器人学习路线，而非按文件名堆叠摘要。论文首先转换为 `references/Markdown/` 下逐页可追溯的 Markdown；数学内容从论文官方 TeX 源包恢复，自定义宏展开为可独立渲染的标准 LaTeX，行内公式使用 `$...$`，块级公式使用 `$$...$$`。知识更新只检索这些 Markdown，遇到公式上下文、图表或双栏顺序歧义时再核对链接页图或源 PDF。主问题是：机器人怎样从数据、奖励与人类反馈中获得可泛化、可精细执行且能在真实世界持续改进的策略？

转换采用官方 TeX 公式层、Poppler 主文本提取、pypdf 文本覆盖交叉基线、MarkItDown 诊断对比和 PDFium 独立视觉验收。完整实测见 `Markdown/conversion-quality-report.md`；验收同时检查公式来源、公式数量、LaTeX 定界符、页数、哈希、图片链接、90% 交叉词项召回阈值和视觉抽查。

## 一张路线图

1. 数学与控制：概率、期望、梯度、动态系统、反馈与坐标系。
2. 学习基础：监督学习、表示学习、序列模型与生成模型。
3. 强化学习：MDP、价值函数、Bellman 方程、actor-critic、off-policy、最大熵。
4. 数据范式：模仿学习、离线 RL、离线到在线 RL、人类示范与纠正。
5. 时间抽象：单步动作、动作块、n 步回报与长时程稀疏奖励。
6. 通用机器人：视觉-语言-动作模型、跨本体数据、流匹配动作专家。
7. 真实系统：感知、低层控制、安全、奖励、重置、actor-learner 与人类介入。
8. 工程实现：openpi 的 LeRobot/RLDS 数据管线、π0 系列模型、Policy 封装和远程推理。

## 当前材料

- `Markdown/1801.01290v2/1801.01290v2.md`（源：`1801.01290v2.pdf`）：SAC，以最大熵目标把稳定探索和 off-policy actor-critic 结合起来。[S1]
- `Markdown/2410.24164v4/2410.24164v4.md`（源：`2410.24164v4.pdf`）：π0，以预训练 VLM 加流匹配动作专家建立跨机器人通用策略。[S2]
- `Markdown/2507.07969v4/2507.07969v4.md`（源：`2507.07969v4.pdf`）：Q-chunking，把动作块直接纳入 TD 学习以改善离线到在线探索和价值传播。[S3]
- `Markdown/hil-serl-paper/hil-serl-paper.md`（源：`hil-serl-paper.pdf`）：HIL-SERL，把示范、纠正、稀疏奖励、样本高效 RL 和真实机器人基础设施整合为系统。[S4]
- `../openpi_knowledge/openpi.md`：基于本地 openpi 源码、π0 论文和官方资料的数据层—模型层—部署层中文导读。[S10]

## 推荐阅读方式

首次阅读可直接打开汇总版 `PINE.md`，或依次阅读 `01-foundations.md`、`02-reinforcement-learning.md`、`03-robot-learning.md`、`04-paper-guides.md`。需要快速定位关系时看 `05-knowledge-graph.md`，要执行学习计划时看 `07-learning-path.md`。文中 `[S#]` 均可在 `06-source-ledger.md` 追溯。

## 三条贯穿全库的问题

- 数据从哪里来：随机交互、历史数据、人类示范/纠正、跨本体数据分别解决什么问题？
- 策略怎样表示：高斯单步动作、动作序列分布、流匹配生成器与 VLA 模型分别带来什么能力？
- 真实部署怎样闭环：如何同时处理探索效率、分布偏移、延迟、安全、奖励与恢复？
