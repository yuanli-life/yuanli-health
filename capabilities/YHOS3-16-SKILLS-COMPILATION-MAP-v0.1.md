---
type: capability-compilation-map
status: proposed
program: YHOS3
version: "0.1"
date: "2026-09-03"
source_repository: moonstachain/yuanli-health-skills
source_registry: registry/source-capabilities.json
source_registry_blob_sha: cb762e88e27a25ac3ece15a35715d8696933f3ca
member_count: 16
mutates_upstream_skills: false
runtime_effect: none
---

# YHOS3｜16 Skills Compilation Map v0.1
## KEEP / RENAME / MERGE / DEFER / GOLD

> **目标不是重做 16 Skills，而是把已经存在的 Skill Core 编译进 Sovereign Principal Health Office。Source capability ID 保持稳定；所有 RENAME 默认只指产品语义/显示名，除非未来另有独立受治理迁移。**

## 0. Mapping Rules

### Disposition

- **KEEP**：现有边界与 YHOS3 一致，继续作为底层原子能力。
- **RENAME**：保留 source capability ID / contract 边界，只升级产品语义或 display label。
- **MERGE**：只允许在用户 Surface / Journey 层合并；不得合并本来需要独立证据门的 epistemic objects。
- **DEFER**：保留上游能力，但不进入当前 Founder learner invocation / Gold Journey 主战役。
- **GOLD**：正交优先级标记，表示下一阶段优先进入 Reality Qualification；它不是新的生命周期状态。

### Hard Rule

```text
RENAME != source-id migration
MERGE != object collapse
DEFER != delete
GOLD != clinically validated
```

尤其保持：

```text
ACT ≠ OUT ≠ LRN ≠ REUSE
```

不得为了产品体验把这些法权/证据门合并。

## 1. Source Inventory｜现有 16 个能力

当前 upstream registry 明确包含：

### Kernel × 7

1. `yuanli.health.kernel.ctx`
2. `yuanli.health.kernel.evd`
3. `yuanli.health.kernel.dec`
4. `yuanli.health.kernel.wpk`
5. `yuanli.health.kernel.act`
6. `yuanli.health.kernel.out`
7. `yuanli.health.kernel.lrn`

### Experience × 6

8. `yuanli.health.experience.first-health-session`
9. `yuanli.health.experience.ninety-day-health-experiment`
10. `yuanli.health.experience.weekly-health-checkpoint`
11. `yuanli.health.experience.doctor-visit-prep`
12. `yuanli.health.experience.outcome-review`
13. `yuanli.health.experience.learning-reuse`

### Meta × 3

14. `yuanli.health.meta.build`
15. `yuanli.health.meta.review`
16. `yuanli.health.meta.qualify`

## 2. Compilation Summary

| # | Source Capability | Class | Disposition | GOLD | YHOS3 Product Meaning |
|---:|---|---|---|:---:|---|
| 1 | `yuanli.health.kernel.ctx` | kernel | KEEP |  | Context normalization / minimum sufficient Principal context |
| 2 | `yuanli.health.kernel.evd` | kernel | RENAME |  | Evidence assembly & adjudication candidate |
| 3 | `yuanli.health.kernel.dec` | kernel | RENAME |  | Priority / primary battle decision candidate |
| 4 | `yuanli.health.kernel.wpk` | kernel | RENAME |  | Minimum-friction work package candidate |
| 5 | `yuanli.health.kernel.act` | kernel | KEEP |  | Verified ACT boundary / action receipt candidate |
| 6 | `yuanli.health.kernel.out` | kernel | RENAME |  | Outcome settlement candidate |
| 7 | `yuanli.health.kernel.lrn` | kernel | KEEP |  | Learning candidate with explicit scope / uncertainty |
| 8 | `yuanli.health.experience.first-health-session` | experience | RENAME | ★ | Founder Health Office Intake / first thesis candidate |
| 9 | `yuanli.health.experience.ninety-day-health-experiment` | experience | RENAME | ★ | Managed Health Cycle; 90-day remains one compatible cadence, not universal ontology |
| 10 | `yuanli.health.experience.weekly-health-checkpoint` | experience | RENAME | ★ | Low-burden Health Checkpoint / Attention Gate |
| 11 | `yuanli.health.experience.doctor-visit-prep` | experience | RENAME | ★ | Clinician-ready Evidence Package / expert handoff preparation |
| 12 | `yuanli.health.experience.outcome-review` | experience | MERGE | ★ | Surface-merge into Settlement & Reuse Journey; OUT gate remains independent |
| 13 | `yuanli.health.experience.learning-reuse` | experience | MERGE | ★ | Surface-merge into Settlement & Reuse Journey; REUSE gate remains independent |
| 14 | `yuanli.health.meta.build` | meta | DEFER |  | Engineering-only capability construction support |
| 15 | `yuanli.health.meta.review` | meta | DEFER |  | Engineering/governance review support |
| 16 | `yuanli.health.meta.qualify` | meta | DEFER |  | Synthetic qualification support; not a learner-facing health capability |

## 3. Kernel Compilation｜7 个底层原子能力

### 3.1 `kernel.ctx` → KEEP

保留理由：YHOS3 仍然需要在任何判断前建立 minimum sufficient context，并显式保留 known / unknown / assumptions。

YHOS3 投影：

> **Context Intake / Normalize**

不应升级为完整个人档案，也不应把“已有数据”误当成“完整背景”。

### 3.2 `kernel.evd` → RENAME

source ID 与 contract 保持不变；产品语义从抽象 EVD 输出升级为：

> **Evidence Assembly & Adjudication Candidate**

它回答：当前 Evidence 是否足以进入下一判断？哪些来源冲突？哪些只能保持 unknown？

注意：Clinician-ready Evidence Package 是更高层 Journey 能力，不应把 EVD 原子对象本身改写成“医生病例包”。

### 3.3 `kernel.dec` → RENAME

产品语义：

> **Primary Battle / Priority Decision Candidate**

C3 不是生成更多建议，而是在 Health Optionality、Safety、Context、Clock 和 Evidence 下选择真正值得押注的问题。

### 3.4 `kernel.wpk` → RENAME

产品语义：

> **Minimum-friction Work Package Candidate**

WPK 的质量不只看理论最优，还看 Safety、Expected Value、Executability、Principal Burden。

候选评价 Lens：

```text
safe enough
+ evidence-linked
+ low friction
+ observable ACT
+ measurable OUT window
```

### 3.5 `kernel.act` → KEEP

继续承担强边界：

> **Recommendation / Plan / Reminder ≠ ACT**

YHOS3 Managed Execution 可以帮助推进 Reality，但 ACT 必须有真实执行证据，不允许 Office “正在处理”冒充 Principal / clinician / service 已经完成现实行为。

### 3.6 `kernel.out` → RENAME

产品语义：

> **Outcome Settlement Candidate**

继续保留：OUT ≠ Attribution。系统可以记录发生了什么，但不能因为时间相邻就自动宣称因果。

### 3.7 `kernel.lrn` → KEEP

Learning 继续保持独立对象，并必须包含：适用 Context、Evidence basis、uncertainty、disconfirming evidence 与 future reuse conditions。

LRN approved 仍然不等于 REUSE。

## 4. Experience Compilation｜6 个 Gold Entry / Journey Capabilities

这 6 个现有 Experience capability 全部标记为 **GOLD Reality Qualification Priority**。原因不是它们都已成熟，而是它们最接近 Founder 能感知价值的端到端 Journey。

### 4.1 `first-health-session` → RENAME + GOLD

新产品语义：

> **Founder Health Office Intake｜第一次健康办公室起盘**

目标不再是“做一次健康分析”，而是最小建立：

- Principal intent / important context
- known / unknown evidence
- one primary battle candidate
- one next safe decision boundary
- whether expert / clinical escalation is required

它仍然不能伪造 WPK、ACT 或 Outcome。

### 4.2 `ninety-day-health-experiment` → RENAME + GOLD

新产品语义：

> **Managed Health Cycle｜托管健康周期**

“90 天”保留为兼容 cadence / 常用实验窗口，不再作为所有健康问题的产品本体。

YHOS3 需要把它从 plan orchestration 推向：

```text
DEC
→ low-friction WPK
→ orchestration
→ verified ACT
→ OUT window
```

但任何需要临床法权的部分继续升级专业人员。

### 4.3 `weekly-health-checkpoint` → RENAME + GOLD

新产品语义：

> **Low-Burden Health Checkpoint / Attention Gate**

它的目标不是增加每周复盘负担，而是回答：

1. 本周是否出现改变现有判断的新证据？
2. 当前计划是否需要调整？
3. 是否有事情必须占用 Principal 注意力？
4. 若没有，能否继续 silent operation？

成功状态可以是：

> **No principal action required.**

### 4.4 `doctor-visit-prep` → RENAME + GOLD

新产品语义：

> **Clinician-ready Evidence Package / Expert Handoff Preparation**

现有 contract 仍只允许准备 CTX/EVD/DEC 相关材料；YHOS3 不把它越权改成自动诊断或自动替医生做专业判断。

未来若 Reality 证明需要“专家匹配/预约编排”，优先先作为 Health Office Orchestration composition，而不是立即新增第 17 个 Skill。

### 4.5 `outcome-review` → MERGE(surface only) + GOLD

与 `learning-reuse` 在用户 Surface 合并成：

> **Settlement & Reuse Journey｜结算与复用旅程**

但底层严格保持：

```text
ACT → OUT
OUT → LRN candidate
LRN → later Task2 preload
```

OUT gate 不能因为 Surface 合并而消失。

### 4.6 `learning-reuse` → MERGE(surface only) + GOLD

与 `outcome-review` 共用一个用户 Journey，但它承担最难的最后一跳：

> **上一轮 Learning 是否在 distinct Task2 的 DEC 之前被 preload，并实际改变下一次判断/行为？**

没有这一证据，Journey 最多停在 Learning，不能结算 Compounding。

## 5. Meta Compilation｜3 个能力 DEFER 出 Founder Front Door

### `meta.build` / `meta.review` / `meta.qualify`

三者继续存在于 `yuanli-health-skills` 工程与 synthetic qualification plane，但从 `yuanli-life/yuanli-health` 的 learner-facing Capability Map 中移出主入口。

理由：

- 它们回答“如何构建/审查/资格化一个 Skill candidate”；
- 不回答企业家真实健康问题；
- 暴露给 Founder 会把工程控制面错误投影成产品能力。

因此：

> **DEFER from learner invocation, KEEP upstream engineering authority.**

## 6. Six Gold Capability Themes｜不是新增 6 个 Skill

YHOS3 下一阶段要打穿的 Gold Reality Themes 为：

1. **Evidence Packaging**｜把证据编译给下一决策者使用
2. **Expert Handoff / Routing**｜把正确问题交给正确专业角色
3. **Minimum-friction Design**｜设计最低摩擦、足够有效的行动
4. **Managed Execution**｜把 Advice 推进到 Reality
5. **Orchestration**｜协调 AI、人、服务、设备与时间
6. **Learned Default / Reuse**｜让过去 Learning 降低下一次管理负担

这些是横跨现有 16 Skills 的产品能力主题，不创建新的 capability ID。

## 7. Gold Journey Compilation

### Journey A｜Founder Health Office Intake

```text
first-health-session
+ kernel.ctx
+ kernel.evd
+ kernel.dec
```

### Journey B｜Managed Health Cycle

```text
kernel.dec
→ kernel.wpk
→ ninety-day-health-experiment
→ weekly-health-checkpoint
→ kernel.act
```

### Journey C｜Clinical Collaboration

```text
kernel.ctx
→ kernel.evd
→ doctor-visit-prep
→ authority handoff
→ later evidence ingest
```

### Journey D｜Settlement & Reuse

```text
kernel.act
→ kernel.out
→ outcome-review
→ kernel.lrn
→ learning-reuse
→ distinct Task2 preload
```

## 8. What We Do NOT Merge

以下对象永不因产品简化而合并：

- CTX 与 EVD
- Evidence 与 Clinical Finding
- DEC 与 Authorization
- WPK 与 ACT
- ACT 与 OUT
- OUT 与 Attribution
- OUT 与 LRN
- LRN 与 REUSE
- AI synthesis 与 Canon

用户旅程可以极简；证据与法权合同不能极简到失真。

## 9. Reality Qualification Priority

下一阶段不做 Skill 17。

先以 6 个 Experience Skills 作为 Gold entry points，在一个受治理 Founder Journey 中证明：

```text
real request
→ correct routing
→ minimum sufficient evidence
→ safe decision candidate
→ lower-friction WPK
→ verified ACT
→ observed OUT
→ LRN
→ later reuse
```

同时结算：

- Health Outcome
- Risk Closure
- Principal Time Cost
- Decision Count
- Manual Actions
- Attention Interruptions
- Health Asset Delta

## 10. Final Compilation Decision

```text
7 Kernel Skills
= KEEP core identities; 4 receive product-semantic RENAME

6 Experience Skills
= ALL GOLD; 4 RENAME; 2 MERGE at Surface only

3 Meta Skills
= DEFER from learner front door; remain upstream engineering capabilities
```

因此 YHOS3 的结论不是“替换旧 16 Skills”，而是：

> **保留原子能力法权，重编产品语义，减少前台暴露，把 16 Skills 编译成少数 Health Office Journeys，并让 Reality 决定未来是否需要新的 capability。**
