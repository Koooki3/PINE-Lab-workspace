---
schema_version: "1.0"
id: "PROMPT-20260818-000000"
name: "构建 openpi 知识库、技能与 kooki 环境"
slug: "openpi-knowledge-environment"
description: >
  基于本地 openpi 源码、网络资源和论文，构建中文知识库与知识图谱，同步 references，并验证 kooki Python 环境。
category: ["research", "coding"]
tags: ["openpi", "embodied-ai", "vla", "knowledge-graph", "kooki"]
language: ["zh-CN"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-18T00:00:00+08:00"
updated_at: "2026-08-18T00:00:00+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  学习、开发、部署或维护 Physical Intelligence openpi 项目时使用。
expected_output: >
  openpi_knowledge 知识库、图谱、完整中文讲解、references 同步、仓库技能以及经过验证的 kooki 环境。
variables: []
dependencies: ["local openpi source", "official web sources", "research papers", "conda kooki"]
notes: >
  原始提示词逐字保存；完整提示词放在 text 围栏中。
source_prompt: |-
  仓库中新增openpi开源库，是后续项目学习、开发等重要的支持库之一，接下来完成几件事：1、以“具身小白，中文讲解一下/mnt/new\_ssd/wenkai/openpi，从数据层、模型层、推理部署层讲解openpi这个库”为基础，搜索网络资源和相关论文，在D:\桌面\PINE-Lab-workspace构建openpi\_knowledge文件夹，并在其中完整详细地整理openpi的知识库知识图谱并生成一份完整的讲解文件openpi.md，最后更新D:\桌面\PINE-Lab-workspace\references中的知识库；2、整理完成后，将openpi知识库和图谱作为技术记忆或技能添加到仓库中；3、建立记忆：仓库主用python环境kooki，并检查kooki是否完整支持运行openpi，如有缺失的库则补全；4、清除过程文件。根据上述需求制定计划，检查无误后执行。
normalized_prompt: |-
  以本地 openpi 源码为主体、官方网络资料与论文为证据，面向具身智能初学者，从数据、模型、训练、推理和部署层建立中文知识库及图谱；同步 references；固化仓库级 openpi 技能和 kooki 环境约定；验证并补齐依赖；清理过程文件。
---

# 构建 openpi 知识库、技能与 kooki 环境

## 1. 基本作用 / Purpose

为 openpi 的后续学习、开发、训练与部署建立可检索、可追溯、可复用的仓库级技术底座。

## 2. 完整提示词 / Full Prompt

```text
仓库中新增openpi开源库，是后续项目学习、开发等重要的支持库之一，接下来完成几件事：1、以“具身小白，中文讲解一下/mnt/new\_ssd/wenkai/openpi，从数据层、模型层、推理部署层讲解openpi这个库”为基础，搜索网络资源和相关论文，在D:\桌面\PINE-Lab-workspace构建openpi\_knowledge文件夹，并在其中完整详细地整理openpi的知识库知识图谱并生成一份完整的讲解文件openpi.md，最后更新D:\桌面\PINE-Lab-workspace\references中的知识库；2、整理完成后，将openpi知识库和图谱作为技术记忆或技能添加到仓库中；3、建立记忆：仓库主用python环境kooki，并检查kooki是否完整支持运行openpi，如有缺失的库则补全；4、清除过程文件。根据上述需求制定计划，检查无误后执行。
```

## 3. 输入变量 / Input Variables

- 本地源码目录：`openpi/`
- 主 Python 环境：`kooki`

## 4. 推荐使用方式 / Recommended Usage

后续 openpi 相关任务优先从知识图谱定位主题，再查阅对应源码路径与一手来源。

## 5. 预期输出 / Expected Output

- `openpi_knowledge/` 中文知识库与图谱。
- references 知识库同步。
- 仓库级 openpi 技能。
- kooki 兼容性报告和可复现验证。

## 6. 模型信息 / Model Information

- **Provider:** OpenAI
- **Model:** Codex

## 7. 测试记录 / Test History

- **Date:** 2026-08-18
- **Result:** Completed with documented platform and dependency constraints

## 8. 修改记录 / Changelog

### v1.0.0 — 2026-08-18

- 创建初始归档。

## 9. 备注 / Notes

不得删除本地 openpi 源码或 references 源 PDF。
