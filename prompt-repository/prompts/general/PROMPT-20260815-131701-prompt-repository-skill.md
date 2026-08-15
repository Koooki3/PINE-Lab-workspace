---
schema_version: "1.0"
id: "PROMPT-20260815-131701"
name: "建立自动提示词仓库技能"
slug: "prompt-repository-skill"
description: >
  建立仓库级提示词归档技能，按 Markdown 与 YAML 元数据保存每次任务的用户原始输入，并提供索引、去重、更新、检查与过程文件清理逻辑。
category: ["general", "prompt-management"]
tags: ["prompt-repository", "yaml-front-matter", "index", "automation", "repository-skill"]
language: ["zh-CN", "en"]
model:
  provider: "OpenAI"
  model_name: "Codex"
  model_version: null
  mode: null
model_parameters: {temperature: null, top_p: null, max_tokens: null, other: {}}
created_at: "2026-08-15T13:17:01+08:00"
updated_at: "2026-08-15T13:17:01+08:00"
timezone: "Asia/Shanghai"
source: {type: "user_input", conversation_id: null, original_author: "User", source_url: null}
version: "1.0.0"
status: "active"
duplicate_of: null
use_case: >
  每个仓库任务结束前自动归档实质性用户输入，或显式管理、搜索、更新提示词仓库时使用。
expected_output: >
  Prompt Repository Skill、模板、分类归档文件、JSON 索引、验证工具和仓库级自动执行约束。
variables: []
dependencies: ["Git 仓库", "用户任务输入"]
notes: >
  原始输入必须保持可追溯；规范化版本不能覆盖原文。当前归档保留了本指令的完整正文于下方 Full Prompt，YAML source_prompt 使用等价引用以避免同一超长模板在单文件内重复两次。
source_prompt: |-
  见本文“2. 完整提示词 / Full Prompt”；该代码块为用户原始输入的逐字保存版本。
normalized_prompt: |-
  为本仓库建立自动提示词归档技能：每个实质性用户任务均以时间戳 ID、YAML 元数据和 Markdown 正文保存原文，可选保存规范化版本；自动维护 JSON 索引、SHA-256 去重关系、语义版本和变更记录；验证后删除过程文件。通过根 AGENTS.md 强制后续线程执行，并补存首次 references 指令和本指令。
---

# 建立自动提示词仓库技能

## 1. 基本作用 / Purpose

为仓库提供完整、可搜索、可版本化、自动维护的提示词资产管理机制，并确保所有后续任务线程都执行归档。

## 2. 完整提示词 / Full Prompt

`````text
同时新增提示词保存仓库级skill，用以保存每一次任务用户输入的提示词，具有完成的更新逻辑的过程文件删除逻辑，新增后需要补全含本指令和前述指令的保存。参考以下建议和模板构建skill，检查无误后执行一次补全保存，后续所有线程都应自动完成提示词保存工作。建议和模板：
如果你的目标是构建一个 **Prompt Repository Skill**，让它在每次用户提供一个值得保存的提示词时，都按照统一格式归档，我建议采用 **Markdown + YAML Front Matter**。这样既方便人类阅读，也方便未来程序化检索、Git 版本管理、Skill 自动解析和迁移到数据库。

下面这个模板可以直接作为仓库的标准格式：

````markdown
---
schema_version: "1.0"

# =========================
# 基础标识 Basic Metadata
# =========================
id: "PROMPT-YYYYMMDD-HHMMSS"
name: "<提示词名称>"
slug: "<prompt-name-in-kebab-case>"

description: >
  <用 1–3 句话说明该提示词的基本作用、解决的问题以及预期用途。>

category:
  - "<主分类>"
  - "<子分类>"

tags:
  - "<tag-1>"
  - "<tag-2>"
  - "<tag-3>"

language:
  - "zh-CN"
  - "<如包含英文则填写 en>"

# =========================
# 模型信息 Model Information
# =========================
model:
  provider: "<OpenAI / Anthropic / Google / xAI / Local / Other>"
  model_name: "<模型名称，例如 GPT-5.6 Sol>"
  model_version: "<如已知则填写，否则 null>"
  mode: "<如 Instant / Thinking / Reasoning / Standard / null>"

model_parameters:
  temperature: null
  top_p: null
  max_tokens: null
  other: {}

# =========================
# 时间信息 Timestamp
# =========================
created_at: "YYYY-MM-DDTHH:MM:SS+08:00"
updated_at: "YYYY-MM-DDTHH:MM:SS+08:00"
timezone: "Asia/Singapore"

# =========================
# 来源与版本 Source & Version
# =========================
source:
  type: "<user_input / assistant_generated / adapted / imported>"
  conversation_id: null
  original_author: "<User / Assistant / Unknown>"
  source_url: null

version: "1.0.0"
status: "active"

# =========================
# 使用信息 Usage
# =========================
use_case: >
  <描述什么情况下应该使用这个提示词。>

expected_output: >
  <描述该提示词预期让模型生成什么样的结果。>

variables:
  - name: "<变量名称>"
    placeholder: "<例如 {{COURSE_NAME}}>"
    description: "<变量作用>"
    required: true

dependencies:
  - "<需要上传的文件、上下文、工具、知识库或其他依赖；如无则填写 none>"

notes: >
  <其他说明、限制、已知问题、使用技巧等。>
---

# <提示词名称>

## 1. 基本作用 / Purpose

<详细说明该提示词的用途。包括：>

- 解决什么问题
- 面向什么场景
- 适合什么用户
- 输入通常是什么
- 预期输出是什么

---

## 2. 完整提示词 / Full Prompt

```text
<在这里原样保存完整提示词正文。

不要摘要。
不要省略。
不要自动修改措辞。
尽量保持用户原始提示词的格式、换行、编号、Markdown 和占位符。>
````

---

## 3. 输入变量 / Input Variables

| 变量               | 是否必填 | 说明   | 示例   |
| ---------------- | ---- | ---- | ---- |
| `{{VARIABLE_1}}` | Yes  | <说明> | <示例> |
| `{{VARIABLE_2}}` | No   | <说明> | <示例> |

如无变量：

> None.

---

## 4. 推荐使用方式 / Recommended Usage

<说明如何使用该 Prompt，例如：>

1. 准备所需材料或上下文。
2. 替换 Prompt 中的变量。
3. 将完整 Prompt 提交给指定模型。
4. 如有附件，在 Prompt 执行前上传。
5. 检查模型输出是否满足预期格式。

---

## 5. 预期输出 / Expected Output

<说明理想情况下模型应该输出什么，例如：>

- 输出语言：
- 输出格式：
- 内容结构：
- 详细程度：
- 是否需要引用来源：
- 是否需要表格：
- 是否需要文件：
- 是否允许模型补充外部知识：

---

## 6. 模型信息 / Model Information

- **Provider:** <OpenAI>
- **Model:** <GPT-5.6 Sol>
- **Model Version:** <如未知填写 N/A>
- **Mode:** <如适用>
- **Temperature:** <如已知>
- **其他参数:** <如有>

---

## 7. 测试记录 / Test History

### Test 1

- **Date:** YYYY-MM-DD
- **Model:** <模型>
- **Result:** <Success / Partial / Failed>
- **Score:** <可选，例如 9/10>
- **Notes:**
  <测试结果以及发现的问题。>

---

## 8. 修改记录 / Changelog

### v1.0.0 — YYYY-MM-DD

- 创建初始版本。
- 保存原始完整提示词。

### v1.1.0 — YYYY-MM-DD

- <修改内容>

---

## 9. 备注 / Notes

<记录 Prompt 的特殊要求、潜在问题、未来优化方向等。>

```

```

其中我特别建议你**不要只保存名称 + Prompt 正文**，因为仓库规模一旦超过几十个 Prompt，后期真正有价值的是 metadata。至少应该强制保存这几个字段：

`id`、`name`、`description`、`tags`、`model`、`created_at`、`version`、`full_prompt`。

### 推荐的仓库结构

如果之后是 GitHub/Git 仓库，可以采用：

```text
prompt-repository/
│
├── prompts/
│   ├── education/
│   │   ├── PROMPT-20260815-110200-week1-course-review.md
│   │   └── ...
│   │
│   ├── coding/
│   ├── research/
│   ├── writing/
│   ├── career/
│   └── general/
│
├── templates/
│   └── prompt-template.md
│
├── index/
│   └── prompts-index.json
│
├── SKILL.md
└── README.md
```

文件名则可以统一为：

```text
PROMPT-{YYYYMMDD}-{HHMMSS}-{slug}.md
```

例如你之前那个“根据字幕、课件和附加资料生成 Week 1 中英双语完整课程复习资料”的 Prompt，可以存成：

```text
PROMPT-20260815-110200-bilingual-course-review.md
```

其中 `id` 使用时间戳的一个重要好处是，**即便两个 Prompt 名称完全相同，也不会发生 ID 冲突**。

如果你的 Skill 最终会负责“监听用户输入 → 判断是否为 Prompt → 自动提取元数据 → 保存到仓库”，我还建议额外区分两个字段：

```yaml
source_prompt: |
  # 用户原始输入，完全不修改

normalized_prompt: |
  # Skill 整理、优化后用于实际复用的版本
```

这样可以同时满足**原始记录可追溯性**和**Prompt 工程优化**。尤其适合你以后做 Prompt 版本迭代，不会出现“优化之后已经不知道用户当初到底输入了什么”的问题。

如果准备把它正式做成一个可安装的仓库 Skill，我会进一步建议把数据结构分成 **`SKILL.md + prompt-template.md + prompts-index.json + 单 Prompt Markdown 文件`** 四层，这样后续让 AI 自动执行保存、搜索、更新、去重和版本控制会比较干净。
`````

## 3. 输入变量 / Input Variables

> None.

## 4. 推荐使用方式 / Recommended Usage

该技能由仓库根 `AGENTS.md` 自动要求，无需用户重复调用；也可显式要求保存、搜索或更新提示词。

## 5. 预期输出 / Expected Output

原始提示词 Markdown、规范化提示词、完整元数据、JSON 索引、重复关系、版本记录和无过程文件的仓库状态。

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
- **Notes:** 已补存前述指令和本指令，并建立自动执行约束。

## 8. 修改记录 / Changelog

### v1.0.0 — 2026-08-15

- 创建初始版本。
- 保存原始完整提示词。

## 9. 备注 / Notes

超长原文完整保存在 Full Prompt；后续归档应在 YAML 与正文均保存原文，除非为避免模板递归膨胀而明确记录等价引用。
