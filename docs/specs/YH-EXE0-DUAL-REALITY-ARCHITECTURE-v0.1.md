# YH-EXE0｜Dual Reality Architecture v0.1

Status: `IMPLEMENTATION_CANDIDATE`
Date: `2026-09-11`
Owner: `yuanli-health`
Upstream: `YH2-C1 Health Constitution`

## 0. Governing Thesis

> 原力健康必须同时证明两件事：**想对**，以及**做成**。

因此冻结双 Reality Loop：

```text
Loop A｜Intelligence Reality
Golden Cases → Model/Prompt/Context Compiler → Eval → ADMIT/REJECT

Loop B｜World Reality
Real Principal → Decision → Authorization → Action Contract → API/Ego → Receipt → OUT → LRN → REUSE
```

二者不得互相替代：通过模型评测不等于现实动作成功；现实动作成功也不证明判断正确。

## 1. Canon Alignment

本架构继承 `YH2-C1-HEALTH-CONSTITUTION.md`：

- `Principal` 保留人生目标、价值排序、重大健康选择与最终授权；
- 医疗诊断、处方、停药、侵入性检查与需专业医学判断的处置进入 Clinical Authority Gate；
- AI 只产生候选解释、候选决策与候选行动；
- 数据读取坚持最小必要、来源可追溯、投影不升级为真源；
- `Data ≠ Diagnosis`、`Knowledge ≠ Authority`、`Intelligence ≠ Authority`。

## 2. Plane Responsibilities

| Plane | System | One job only |
|---|---|---|
| Law | GitHub | Protocol / Schema / Policy / Test / Admission |
| Reality | Local Health Canon | 原始健康事实与正式临床证据 |
| Projection | Supabase | 受控状态、事件、Receipt、队列 |
| Intelligence | Hugging Face | 候选模型、Eval、Jobs、实验 |
| Reasoning | ChatGPT / approved LLM | 综合推理与解释，不做 SSOT |
| Orchestration | n8n | Trigger / state machine / approval / retry / timeout |
| Last Mile | Ego Lite | 已授权浏览器动作，不持有健康判断法权 |

## 3. End-to-End Spine

```text
GitHub Law
  ↓
Context Projection
  ↓
Loop A Eval Admission ─────── FAIL → reject build
  ↓ PASS
Decision Candidate
  ↓
Authority Classification
  ↓
Human / Clinician / Principal Gate
  ↓
Action Contract
  ↓
n8n Orchestration
  ├─ API Adapter
  └─ Ego Local Runner → Browser
  ↓
Action Receipt
  ↓
Observed State / OUT
  ↓
Adjudicated Learning
  ↓
Task2 Preload
  ↓
Reuse Receipt
```

## 4. Hard Boundaries

1. Hugging Face 不保存 Health Canon、原始病历、身份信息或生产凭证。
2. n8n 不成为 Health Canon，不直接生成临床事实。
3. Ego 不接收自然语言无限任务；只接收 schema-valid、未过期、已授权的 Action Contract。
4. 浏览器自动化默认 `prepare-only`；提交、取消、购买、医疗授权等动作按 contract 明确要求人工批准。
5. n8n 不通过 `Execute Command` 获得任意宿主机 shell 权限作为生产默认路径。
6. 所有现实动作必须留下 Receipt；无 Receipt 不得声明 ACT verified。
7. 无 observed OUT 不得升级 Learning；无 Task2 reuse receipt 不得声明 compounding。

## 5. P0 Invariants

以下任一发生即整个 build `FAIL`：

- cross-principal data leakage；
- unauthorized clinical action；
- fabricated clinical fact；
- secret/token leakage；
- browser action outside allowlisted domain/action；
- expired/revoked contract 被执行；
- action 成功但无可验证 Receipt；
- Observation 静默升级为 diagnosis / treatment authority。

## 6. Runtime States

```text
PROPOSED
→ EVAL_ADMITTED
→ AUTHORITY_CLASSIFIED
→ APPROVAL_PENDING | APPROVED | REJECTED
→ QUEUED
→ EXECUTING
→ RECEIPT_PENDING
→ COMPLETED | FAILED | EXPIRED | CANCELLED
→ OUTCOME_PENDING
→ OUTCOME_OBSERVED
→ LEARNING_CANDIDATE
→ LEARNING_ADJUDICATED
→ REUSE_ELIGIBLE
→ REUSED
```

任何状态只允许声明式转换并记录 `from_state / to_state / actor / authority / timestamp / evidence_ref`。

## 7. 90-Day Validation

- R0 Synthetic: 60 Golden + 20 Hard Negatives；
- R1 RAY read-only shadow: 真实 context，禁止自动执行；
- R2 3 Founder shadow: 三类不同健康任务，Steward/Clinician gate；
- R3 5 Paying Principals: 生产 Surface 与 HF Shadow 分离，每个 release 先过 Loop A，再进入 Loop B。

## 8. North Star

最高系统判据不是 DAU，也不是“AI 回答很好”，而是：

> **Verified Health Learning Loop：一次被授权的判断进入真实行动，产生可观察结果，形成经有权主体裁决的 Learning，并在下一次适用任务开始前被准确加载、真实改变 DEC/WPK/ACT，留下 reuse receipt。**
