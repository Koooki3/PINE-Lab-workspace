---
schema_version: "1.0"
id: "PROMPT-20260815-131700"
name: "建立并维护 references 知识库与知识图谱"
slug: "references-knowledge-management"
description: >
  基于仓库 references 中持续变化的论文和文件，构建由易到难的详细知识库、知识图谱与 PINE.docx，并固化增量更新、检查和清理流程。
category: ["research", "knowledge-management"]
tags: ["references", "knowledge-base", "knowledge-graph", "docx", "repository-skill"]
language: ["zh-CN", "en"]
model:
  provider: "OpenAI"
  model_name: "Codex"
  model_version: null
  mode: null
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-15T13:17:00+08:00"
updated_at: "2026-08-15T13:17:00+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  首次创建或后续更新 references 学术知识库、图谱和学习文档时使用。
expected_output: >
  仓库级技能、详细 Markdown 知识库、机器可读知识图谱、PINE.docx、差异检测和验证脚本，且无过程文件。
variables: []
dependencies: ["references 文件夹", "网络检索", "DOCX 渲染工具"]
notes: >
  要求后续由“更新references知识库”等指令触发严格的增删检测、补链、检查、文档更新和清理流程。
source_prompt: |-
  references中会经常更新加入新的参考文件、论文等，建立一个仓库级skill帮我管理references并完成以下要求：1、成体系化建立基于references的详细知识库和知识图谱，基于其中文件的内容，并通过广泛全面的网络搜索和查阅分析，补全所需的详细前置知识，构建一个从易到难知识库，然后做一次检查；2、在references中新建Knowledge graph子文件夹用以保存详细知识库和知识图谱，同时新建一个PINE.docx用以输出可视化结果，便于初学者随时查阅学习；3、构建完整的更新逻辑：本次新建完成后，后续遇到类似“更新references知识库”的指令时依次完成（1）查找新增或删除文件；（2）根据新增或删除内容更新知识库和知识图谱；（3）检查知识库和知识图谱，补全前置知识并完善知识链，然后做一次检查；（4）更新PINE.docx；（5）删除过程文件；4、首次新建完成后注意删除过程文件
normalized_prompt: |-
  在仓库内建立并维护 references 知识系统：扫描 references 的增删改，基于本地一手材料与权威网络来源更新由易到难的知识库、证据账本和知识图谱，检查前置知识链，重建并逐页验证 references/Knowledge graph/PINE.docx，最后接受清单并删除所有过程文件。将完整流程固化为仓库级技能，并由“更新references知识库”等语义触发。
---

# 建立并维护 references 知识库与知识图谱

## 1. 基本作用 / Purpose

将不断变化的参考文献组织为可追溯、可增量维护、适合初学者学习的知识系统和可视化文档。

## 2. 完整提示词 / Full Prompt

```text
references中会经常更新加入新的参考文件、论文等，建立一个仓库级skill帮我管理references并完成以下要求：1、成体系化建立基于references的详细知识库和知识图谱，基于其中文件的内容，并通过广泛全面的网络搜索和查阅分析，补全所需的详细前置知识，构建一个从易到难知识库，然后做一次检查；2、在references中新建Knowledge graph子文件夹用以保存详细知识库和知识图谱，同时新建一个PINE.docx用以输出可视化结果，便于初学者随时查阅学习；3、构建完整的更新逻辑：本次新建完成后，后续遇到类似“更新references知识库”的指令时依次完成（1）查找新增或删除文件；（2）根据新增或删除内容更新知识库和知识图谱；（3）检查知识库和知识图谱，补全前置知识并完善知识链，然后做一次检查；（4）更新PINE.docx；（5）删除过程文件；4、首次新建完成后注意删除过程文件
```

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

将论文或参考文件放入 `references/`，然后发出本提示或“更新references知识库”。

## 5. 预期输出 / Expected Output

中文知识库、引用来源、可视化知识图谱、PINE.docx 和可重复运行的增量更新逻辑。

## 6. 模型信息 / Model Information

- **Provider:** OpenAI
- **Model:** Codex
- **Model Version:** N/A
- **Mode:** N/A

## 7. 测试记录 / Test History

### Test 1

- **Date:** 2026-08-15
- **Model:** Codex
- **Result:** Success
- **Notes:** 首次建立知识库与自动化脚本。

## 8. 修改记录 / Changelog

### v1.0.0 — 2026-08-15

- 创建初始版本。
- 保存原始完整提示词。

## 9. 备注 / Notes

后续更新须保留证据链并删除过程文件。
