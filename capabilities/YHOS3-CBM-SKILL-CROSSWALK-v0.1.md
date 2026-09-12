---
type: cbm-skill-crosswalk
status: proposed
program: YHOS3
version: "0.1"
date: "2026-09-03"
---

# YHOS3｜Personal Health CBM × Existing 16 Skills Crosswalk v0.1

## 0. Non-Identity Rule｜先消除一个高风险歧义

> **CBM 的 `4 × 4 = 16` 指 16 个 capability cells；它与 `yuanli-health-skills` 当前恰好 16 个 source capabilities 不是一一对应关系。**

两者数量相同只是当前阶段的偶合，不得推导：

```text
one CBM cell = one existing source skill
```

正确关系是：

```text
CBM Cell
= stable product capability need

Source Skill
= executable atomic / experience / meta capability

Journey
= composition across multiple cells and skills
```

因此一个 Skill 可以服务多个 CBM Cell；一个 CBM Cell 也可以由多个 Skill 共同实现。

## 1. Kernel Skill Crosswalk

| Source Skill | Primary CBM Contribution | Secondary Contribution | Boundary |
|---|---|---|---|
| `yuanli.health.kernel.ctx` | Evidence × Observe | Intervention × Observe | normalize context; not a complete health profile |
| `yuanli.health.kernel.evd` | Evidence × Observe / Decide | Risk × Observe | evidence candidate; not clinical finding |
| `yuanli.health.kernel.dec` | Risk × Decide | Intervention × Decide | decision candidate; not authorization |
| `yuanli.health.kernel.wpk` | Intervention × Decide | System × Act | work package; not ACT |
| `yuanli.health.kernel.act` | Intervention × Act | System × Act | verified action boundary |
| `yuanli.health.kernel.out` | Intervention × Learn | Risk × Learn | observed outcome; not attribution |
| `yuanli.health.kernel.lrn` | Intervention × Learn | System × Learn | learning candidate; not reuse |

## 2. Experience Skill Crosswalk

| Source Skill | Primary CBM Contribution | Gold Theme | YHOS3 Journey Role |
|---|---|---|---|
| `yuanli.health.experience.first-health-session` | Evidence Observe/Decide + Risk Decide | Evidence Packaging precursor | Founder Health Office Intake |
| `yuanli.health.experience.ninety-day-health-experiment` | Intervention Decide/Act + System Act | Minimum-friction Design / Managed Execution / Orchestration | Managed Health Cycle |
| `yuanli.health.experience.weekly-health-checkpoint` | System Observe/Decide + Intervention Learn | Attention Gate / Managed Execution | Low-Burden Checkpoint |
| `yuanli.health.experience.doctor-visit-prep` | Evidence Act + Risk Act | Evidence Packaging / Expert Handoff | Clinical Collaboration |
| `yuanli.health.experience.outcome-review` | Intervention Learn | Outcome Settlement | Settlement & Reuse Journey |
| `yuanli.health.experience.learning-reuse` | System Learn | Learned Default / Reuse | Settlement & Reuse Journey |

## 3. Meta Skill Crosswalk

`yuanli.health.meta.build` / `review` / `qualify` 不映射到 Founder Health CBM 主图。

原因：它们属于 **Capability Engineering Plane**，负责 build / review / synthetic qualification，而不是 Principal Health Office 对外提供的健康能力。

因此它们在 YHOS3 中：

```text
upstream engineering = KEEP
learner invocation = DEFER
CBM front-door mapping = none
```

## 4. CBM Cell → Existing Skill Coverage

### Evidence × Observe｜Zero-friction Intake

现有覆盖：`kernel.ctx` + `kernel.evd` + `first-health-session`。

缺口：真实 multi-source zero-friction ingestion 属 private runtime / adapters，不应在 public repo 伪装已经具备。

### Evidence × Decide｜Evidence Adjudication

现有覆盖：`kernel.evd` + `first-health-session`。

缺口：跨来源冲突仲裁、证据成熟度和 clinical evidence authority 继续依赖上游 Health Domain contracts。

### Evidence × Act｜Clinician-ready Evidence Package

现有覆盖：`doctor-visit-prep` + `kernel.evd`。

方向：GOLD。

### Evidence × Learn｜Longitudinal Baseline

现有覆盖：`kernel.out` + `kernel.lrn` 的部分沉淀逻辑。

缺口：长期 private memory persistence 不属于 public Skill Core 当前 ephemeral contract。

### Risk × Observe｜Risk / Debt Sensing

现有覆盖：`kernel.evd` / `first-health-session` 的候选信号组织。

缺口：silent risk、screening debt、follow-up debt 的完整扫描属于 Healthspan / private Domain Runtime。

### Risk × Decide｜Priority

现有覆盖：`kernel.dec` + `first-health-session`。

方向：从 generic decision candidate 强化到 Primary Battle / Priority，但不改变 source ID。

### Risk × Act｜Clinical Escalation / Expert Handoff

现有覆盖：`doctor-visit-prep`。

缺口：专家搜索、匹配、预约、支付等现实 orchestration 尚不能被现有 Skill 自动宣称；先作为 Health Office Journey composition 验证。

### Risk × Learn｜Personal Risk Model

现有覆盖：`kernel.out` + `kernel.lrn` + `learning-reuse` 的部分链路。

缺口：必须依赖 distinct longitudinal outcomes，不能通过 synthetic benchmark 直接获得。

### Intervention × Observe｜Behavior / Constraint Baseline

现有覆盖：`kernel.ctx` + `first-health-session` + `weekly-health-checkpoint`。

### Intervention × Decide｜Minimum-friction Action Design

现有覆盖：`kernel.wpk` + `ninety-day-health-experiment`。

方向：GOLD。

### Intervention × Act｜Managed Execution

现有覆盖：`kernel.act` + `ninety-day-health-experiment` + `weekly-health-checkpoint`。

关键缺口：现实服务执行、提醒、配送、预约等 orchestration 必须由 Runtime/Service Graph 提供；public Skill contract 不能伪造 ACT。

### Intervention × Learn｜Outcome Response / Personal Rule

现有覆盖：`kernel.out` + `outcome-review` + `kernel.lrn`。

方向：GOLD。

### System × Observe｜Freshness / Continuity

现有覆盖：`weekly-health-checkpoint` 的节奏层；真实数据 freshness 属 private runtime。

### System × Decide｜Authority + Attention Gate

现有覆盖：所有 Skill contract 的 authority boundary + `weekly-health-checkpoint`。

方向：Gold Journey 必须把“无需打扰本人”视为合法成功状态。

### System × Act｜Orchestration / Friction Removal

现有覆盖：`ninety-day-health-experiment` + `weekly-health-checkpoint` 的 orchestration skeleton。

关键缺口：真实 AI Brain × Steward × Expert × Service Graph 尚需 Reality Build；不得因已有 orchestration 词汇宣称全托管已成立。

### System × Learn｜Learned Default / Reuse

现有覆盖：`kernel.lrn` + `learning-reuse` + `outcome-review`。

方向：最高 GOLD；只有 distinct Task2 preload + actual use + receipt 才算成立。

## 5. Strategic Conclusion

现有 16 Skills 的真正状态不是“16 格已经被实现”，而是：

> **我们已经拥有一组覆盖 CTX→EVD→DEC→WPK→ACT→OUT→LRN 以及六类 Founder Experience 的合格 synthetic source candidates；YHOS3 现在要用 Reality 把它们编译成 Health Office 能力，而不是因为 CBM 也有 16 格就错误地做一一命名映射。**

下一阶段判断新增能力的规则：

```text
Reality Gap
→ existing composition cannot safely close the gap
→ prove missing capability is stable/reusable
→ only then consider Skill 17 candidate
```
