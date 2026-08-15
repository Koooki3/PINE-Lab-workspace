---
schema_version: "1.0"
id: "PROMPT-20260815-160100"
name: "将 references PDF 转换为 Markdown 并更新知识工作流"
slug: "pdf-markdown-reference-workflow"
description: >
  引入论文 PDF 转 Markdown 仓库技能，批量转换 references，改造知识库更新逻辑，并以 PINE.md 取代 DOCX。
category: ["research", "knowledge-management"]
tags: ["pdf-to-markdown", "references", "knowledge-graph", "repository-skill"]
language: ["zh-CN", "en"]
model: {provider: "OpenAI", model_name: "Codex", model_version: null, mode: null}
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-15T16:01:00+08:00"
updated_at: "2026-08-15T16:01:00+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  references 中 PDF 需要先转换为可检索 Markdown，再维护知识库时使用。
expected_output: >
  PDF 对应 Markdown、更新后的仓库技能、知识库、知识图谱和 PINE.md。
variables: []
dependencies: ["references PDF", "translate-paper-pdf-to-md"]
notes: >
  用户要求不再使用 DOCX 输出。
source_prompt: |-
  注意到从pdf直接获取信息或支持会产生不必要的信息丢失或者token冗余，因此我想更新优化references和相关skills：通过引入如下pdf转markdown仓库级skill（[https://liumengxuan04.github.io/%E6%8A%80%E6%9C%AF/2026/05/16/%E6%8A%80%E6%9C%AF-translate-paper-pdf-to-md/#:~:text=Use%20%24translate-paper-pdf-to-md%20to%20translate%20%2Fpath%2Fto%2Fpaper.pdf%20into%20Chinese%20Markdown.,%E5%A6%82%E6%9E%9C%E6%B2%A1%E6%9C%89%E6%8F%90%E4%BE%9B%E8%BF%99%E4%BA%9B%E4%BF%A1%E6%81%AF%EF%BC%8Cskill%20%E4%BC%9A%E8%A6%81%E6%B1%82%20Codex%20%E5%9C%A8%E6%AD%A3%E5%BC%8F%E7%BF%BB%E8%AF%91%E5%89%8D%E5%85%88%E7%A1%AE%E8%AE%A4%EF%BC%9A%20%E7%9B%AE%E6%A0%87%E8%AF%AD%E8%A8%80%E6%88%96%E5%9C%B0%E5%8C%BA%E3%80%82%20%E8%AE%BA%E6%96%87%E9%A2%86%E5%9F%9F%E6%88%96%E5%AD%90%E9%A2%86%E5%9F%9F%E3%80%82%20%E7%9B%AE%E6%A0%87%E8%AF%BB%E8%80%85%E5%92%8C%E8%AF%AD%E6%B0%94%E9%A3%8E%E6%A0%BC%E3%80%82%20%E6%9C%AF%E8%AF%AD%E4%BF%9D%E7%95%99%E7%AD%96%E7%95%A5%E3%80%82](https://liumengxuan04.github.io/%E6%8A%80%E6%9C%AF/2026/05/16/%E6%8A%80%E6%9C%AF-translate-paper-pdf-to-md/#:~:text=Use%20%24translate-paper-pdf-to-md%20to%20translate%20%2Fpath%2Fto%2Fpaper.pdf%20into%20Chinese%20Markdown.,%E5%A6%82%E6%9E%9C%E6%B2%A1%E6%9C%89%E6%8F%90%E4%BE%9B%E8%BF%99%E4%BA%9B%E4%BF%A1%E6%81%AF%EF%BC%8Cskill%20%E4%BC%9A%E8%A6%81%E6%B1%82%20Codex%20%E5%9C%A8%E6%AD%A3%E5%BC%8F%E7%BF%BB%E8%AF%91%E5%89%8D%E5%85%88%E7%A1%AE%E8%AE%A4%EF%BC%9A%20%E7%9B%AE%E6%A0%87%E8%AF%AD%E8%A8%80%E6%88%96%E5%9C%B0%E5%8C%BA%E3%80%82%20%E8%AE%BA%E6%96%87%E9%A2%86%E5%9F%9F%E6%88%96%E5%AD%90%E9%A2%86%E5%9F%9F%E3%80%82%20%E7%9B%AE%E6%A0%87%E8%AF%BB%E8%80%85%E5%92%8C%E8%AF%AD%E6%B0%94%E9%A3%8E%E6%A0%BC%E3%80%82%20%E6%9C%AF%E8%AF%AD%E4%BF%9D%E7%95%99%E7%AD%96%E7%95%A5%E3%80%82)）先将references中的pdf文件转成markdown格式的对应文件，然后再读取markdown格式的对应文件完成前述任务和skill要求。先在仓库中引入这个skill，然后对references中所有pdf做一次转换，并将转换写入references的更新逻辑中，转换完成后按照之前的要求更新一边reference、知识库、知识图谱并导出PINE.md，不再使用.docx格式的输出。
normalized_prompt: |-
  引入 translate-paper-pdf-to-md；先把 references PDF 增量转换并验证为 Markdown，再从 Markdown 更新知识库与图谱，导出 PINE.md，清理 DOCX 和过程文件。
---

# 将 references PDF 转换为 Markdown 并更新知识工作流

## 1. 基本作用 / Purpose

建立 Markdown-first 的论文知识维护流程。

## 2. 完整提示词 / Full Prompt

```text
注意到从pdf直接获取信息或支持会产生不必要的信息丢失或者token冗余，因此我想更新优化references和相关skills：通过引入如下pdf转markdown仓库级skill（[https://liumengxuan04.github.io/%E6%8A%80%E6%9C%AF/2026/05/16/%E6%8A%80%E6%9C%AF-translate-paper-pdf-to-md/#:~:text=Use%20%24translate-paper-pdf-to-md%20to%20translate%20%2Fpath%2Fto%2Fpaper.pdf%20into%20Chinese%20Markdown.,%E5%A6%82%E6%9E%9C%E6%B2%A1%E6%9C%89%E6%8F%90%E4%BE%9B%E8%BF%99%E4%BA%9B%E4%BF%A1%E6%81%AF%EF%BC%8Cskill%20%E4%BC%9A%E8%A6%81%E6%B1%82%20Codex%20%E5%9C%A8%E6%AD%A3%E5%BC%8F%E7%BF%BB%E8%AF%91%E5%89%8D%E5%85%88%E7%A1%AE%E8%AE%A4%EF%BC%9A%20%E7%9B%AE%E6%A0%87%E8%AF%AD%E8%A8%80%E6%88%96%E5%9C%B0%E5%8C%BA%E3%80%82%20%E8%AE%BA%E6%96%87%E9%A2%86%E5%9F%9F%E6%88%96%E5%AD%90%E9%A2%86%E5%9F%9F%E3%80%82%20%E7%9B%AE%E6%A0%87%E8%AF%BB%E8%80%85%E5%92%8C%E8%AF%AD%E6%B0%94%E9%A3%8E%E6%A0%BC%E3%80%82%20%E6%9C%AF%E8%AF%AD%E4%BF%9D%E7%95%99%E7%AD%96%E7%95%A5%E3%80%82](https://liumengxuan04.github.io/%E6%8A%80%E6%9C%AF/2026/05/16/%E6%8A%80%E6%9C%AF-translate-paper-pdf-to-md/#:~:text=Use%20%24translate-paper-pdf-to-md%20to%20translate%20%2Fpath%2Fto%2Fpaper.pdf%20into%20Chinese%20Markdown.,%E5%A6%82%E6%9E%9C%E6%B2%A1%E6%9C%89%E6%8F%90%E4%BE%9B%E8%BF%99%E4%BA%9B%E4%BF%A1%E6%81%AF%EF%BC%8Cskill%20%E4%BC%9A%E8%A6%81%E6%B1%82%20Codex%20%E5%9C%A8%E6%AD%A3%E5%BC%8F%E7%BF%BB%E8%AF%91%E5%89%8D%E5%85%88%E7%A1%AE%E8%AE%A4%EF%BC%9A%20%E7%9B%AE%E6%A0%87%E8%AF%AD%E8%A8%80%E6%88%96%E5%9C%B0%E5%8C%BA%E3%80%82%20%E8%AE%BA%E6%96%87%E9%A2%86%E5%9F%9F%E6%88%96%E5%AD%90%E9%A2%86%E5%9F%9F%E3%80%82%20%E7%9B%AE%E6%A0%87%E8%AF%BB%E8%80%85%E5%92%8C%E8%AF%AD%E6%B0%94%E9%A3%8E%E6%A0%BC%E3%80%82%20%E6%9C%AF%E8%AF%AD%E4%BF%9D%E7%95%99%E7%AD%96%E7%95%A5%E3%80%82)）先将references中的pdf文件转成markdown格式的对应文件，然后再读取markdown格式的对应文件完成前述任务和skill要求。先在仓库中引入这个skill，然后对references中所有pdf做一次转换，并将转换写入references的更新逻辑中，转换完成后按照之前的要求更新一边reference、知识库、知识图谱并导出PINE.md，不再使用.docx格式的输出。
```

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

在 references 更新前自动执行。

## 5. 预期输出 / Expected Output

逐页可追溯 Markdown、知识库、知识图谱和 PINE.md。

## 6. 模型信息 / Model Information

- **Provider:** OpenAI
- **Model:** Codex

## 7. 测试记录 / Test History

- **Date:** 2026-08-15
- **Result:** Success

## 8. 修改记录 / Changelog

### v1.0.0 — 2026-08-15

- 创建初始版本并保存原始输入。

## 9. 备注 / Notes

无。
