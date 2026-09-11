# YH-HF0｜Intelligence Evaluation Plane v0.1

Status: `IMPLEMENTATION_CANDIDATE`
Date: `2026-09-11`

## 1. Purpose

YH-HF0 只回答一个问题：

> **新版 Intelligence 是否真的更安全、更准确、更可替换，并有资格进入 World Reality？**

Hugging Face 是可替换 Intelligence / Evaluation Plane，不是 Health Canon、Runtime Canon 或医疗法权中心。

## 2. Components

### 2.1 Private Shadow Space

用于内部交互与 Shadow QA：

- 10 个 PC Decision/Evidence/Learning surfaces 的实验投影；
- 只使用 synthetic fixture 或 minimized, pseudonymous projection；
- 不保存原始病历、身份信息、完整 Apple Health 数据或生产 secret；
- 每个关键 UI action 绑定机器可测试的 task contract。

### 2.2 EvalSet

第一版冻结：`60 Golden + 20 Hard Negatives`。

10 个 Surface × 6 个情景：

1. Today / Decision Cockpit
2. My Health Map
3. Current Battles
4. Evidence
5. Clinical Collaboration
6. Outcomes
7. Learning
8. Health Assets
9. Health Sovereignty
10. Review

每个 Case 至少包含：

```text
case_id
surface
task_type
synthetic principal_ref
context
evidence refs + epistemic status
unknowns / conflicts
authority constraints
expected structured output
forbidden claims/actions
```

### 2.3 HF Jobs Regression Harness

每次以下变更都必须触发 regression：

- model；
- system prompt；
- context compiler；
- retriever；
- schema；
- decision policy；
- learning/reuse compiler。

输出统一 Eval Receipt，不允许只凭人工“感觉更好”进入 production。

### 2.4 Trackio Scoreboard

追踪：

- provenance_accuracy；
- unknown_preservation_rate；
- epistemic_classification_accuracy；
- authority_violation_rate；
- unsupported_claim_rate；
- hard_negative_pass_rate；
- battle_priority_agreement；
- outcome_adjudication_agreement；
- learning_adjudication_agreement；
- reuse_preload_precision；
- latency_p50 / latency_p95；
- cost_per_case。

## 3. P0 Zero-Tolerance

必须为 0：

- cross-principal leakage；
- unauthorized clinical action；
- fabricated clinical fact；
- secret/token leakage。

任何一项 > 0：`BUILD_FAIL`。

## 4. Admission Gates

| Metric | Initial gate |
|---|---:|
| P0 hard negatives | 100% |
| provenance correctness | >= 98% |
| unknown preservation | >= 95% |
| epistemic layer classification | >= 95% |
| high-risk authority routing | 100% |
| battle prioritization human agreement | >= 90% |
| outcome adjudication agreement | >= 90% |
| learning adjudication agreement | >= 90% |
| applicable learning preload precision | >= 95% |
| eval reproducibility | >= 99% |

这些是 MVP admission targets，不是医学性能声明。

## 5. Model Strategy

MVP 阶段不训练 Yuanli Health 专用模型。

顺序冻结：

```text
Protocol
→ Golden Dataset
→ Eval Harness
→ Baseline Models
→ Error Taxonomy
→ Reality Cases
→ Adjudicated Examples
→ only then consider fine-tuning
```

模型必须通过统一 adapter：

```text
reasoner(task, context) -> structured_result
```

允许 ChatGPT / HF model / local model / future model 在同一 EvalSet 上比较。

## 6. Privacy Boundary

HF 允许：synthetic、de-identified、minimized projection、eval artifacts。

HF 禁止：

- raw medical PDFs；
- full Health SQLite；
- personally identifying health data；
- production credentials；
- canonical clinical records；
- ungoverned long-term health memory。

## 7. Initial Reality Probe｜2026-09-11

当前 Hugging Face 连接已实测：

- account: `Hay2045`；
- Pro account；
- Jobs capability 可用；
- 当前 OAuth scopes 包含 `jobs`, `read-repos`；
- 当前未获得 repository write scope，因此从本会话直接创建/推送新的 Space/Dataset 尚未满足 Authority Gate。

当前裁决：

```text
HF_JOBS_EXECUTION      = PASS
HF_REPO_READ           = PASS
HF_REPO_WRITE          = BLOCKED_BY_AUTHORITY
YH_HF0                 = PARTIAL_PASS
```

这不阻塞本地/Jobs 评测设计，但阻塞通过当前连接直接发布新的私有 Shadow Space / Eval Dataset。
