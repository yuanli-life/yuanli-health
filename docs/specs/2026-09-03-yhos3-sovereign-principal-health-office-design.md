---
type: architecture-written-spec
status: proposed
program: YHOS3
version: "0.1"
date: "2026-09-03"
repository: yuanli-life/yuanli-health
canon_effect: none
runtime_effect: none
creates_clinical_authority: false
creates_second_health_truth: false
accepts_real_health_data_in_git: false
---

# YHOS3｜Sovereign Principal Health Office Architecture Candidate
## Written Spec v0.1

> **目标不是让企业家管理更多健康信息，而是在本人保持最大主权的前提下，让一个长期 Health Office 持续替本人吸收健康世界的复杂度，并让过去的真实结果提高下一次健康决策质量。**

## 0. Status 与法权

本文件是 `yuanli-life/yuanli-health` 的 YHOS3 架构候选规格，不自动修改当前已 ratify 的 C1 Health Constitution，不替代上游 Health Domain / Clinical Authority，不创建第二套个人健康真相，也不授权任何真实个人健康数据进入公开 GitHub。

在 Human Review 与后续受治理合并完成前：

- `status = proposed`
- 不宣称 YHOS3 已成为 Canon
- 不宣称任何 Skill 已发布、部署或获得临床验证
- 不宣称任何真实健康 Outcome、Attribution、Learning 或 Reuse

## 1. North Star｜Health Optionality

原力健康最高目标保持：

> **Health Optionality｜长期生命选择权**
>
> 让身体有余量，让人生有余地。

它由两个一级账户共同保护：

1. **Deployable Capacity｜今日可调用能力**：今天与眼前重要情境中，还能安全调用多少身体、认知、恢复、应变和心理能力。
2. **Sustainable Healthspan｜长期生命底盘**：哪些结构性风险、疾病风险、筛查债务、随访债务与能力缺口正在关闭未来十年、二十年的重要人生选项。

Performance 与 Healthspan 不是两套健康真相；它们是同一 Principal Health Reality 上的两种判断模式。

## 2. Product First Principle｜Maximum Sovereignty × Minimum Management

YHOS3 的产品第一性冻结为：

> **Maximum Sovereignty × Minimum Management｜最大主权 × 最小管理负担。**

可外包：资料整理、证据编译、研究、提醒、协调、日程、服务编排、候选方案、执行摩擦消除。

不可外包：本人生命目标、价值排序、风险偏好、重大选择、最终授权；诊断、处方与需要专业医学判断的事项仍属于适当的医疗专业人员。

因此 YHOS3 不是 AI Doctor，也不是 Dashboard；它是一个受法权约束的 **Sovereign Principal Health Office OS**。

## 3. Mother Architecture｜一核 · 两引擎 · 一图 · 一环 · 一办公室

```text
                         HEALTH OPTIONALITY
                               │
              ┌────────────────┴────────────────┐
              │                                 │
      PERFORMANCE ENGINE                HEALTHSPAN ENGINE
      Deployable Capacity             Sustainable Healthspan
              │                                 │
              └────────────────┬────────────────┘
                               │
                     SOVEREIGN HEALTH KERNEL
                   C1 → C2 → C3 → C4
                               │
                     PERSONAL HEALTH CBM
                         4 × 4 = 16
                               │
                    HEALTH OFFICE RUNTIME
          AI Brain × Steward × Expert × Service Graph
                               │
       CTX → EVD → DEC → WPK → ACT → OUT → LRN → REUSE
                               │
                          BODY REALITY
                               └────────────────────↺
```

### 3.1 One Sovereign Health Kernel｜C1–C4

| Kernel | Identity | 唯一问题 |
|---|---|---|
| C1 | Sovereignty / Health Kernel | 我为什么健康？什么不能被牺牲？ |
| C2 | Truth / Living Health State | 我的身体现在真实怎样？ |
| C3 | Judgment / Health Priority Map | 现在什么最值得解决？ |
| C4 | Reality / Reality Loop | 做了什么、发生什么、学到什么、下次是否复用？ |

硬边界继续保持：

```text
Data ≠ Diagnosis
Knowledge ≠ Authority
Intelligence ≠ Authority
Signal ≠ Fact ≠ Decision ≠ Action ≠ Outcome
ACT ≠ OUT ≠ Attribution ≠ LRN ≠ REUSE
```

### 3.2 Two Engines｜同核双引擎

**Performance Engine** 使用六大 Human Functional Capacities 作为功能投影：

- Recover｜恢复
- Adapt｜应变
- Energize｜供能
- Move｜身体储备
- Think｜认知表现
- Connect｜心理与意义

六项是功能投影，不是第二套医学本体、六个页面或六条产品线。

**Healthspan Engine** 负责长期完整性扫描：silent risk、screening debt、follow-up debt、unresolved structural risk、longitudinal reserve。

短期 Performance 优化不能越过 Safety / Clinical Authority / Irreversible Long-term Risk。

### 3.3 Orthogonal Coordinates｜不再增加顶层树

以下维度保持正交身份：

- **12 Health Domains** = Scientific Completeness Backbone，回答“专业上不能漏什么”；退出用户前台。
- **6 Human Functional Capacities** = Human Function Projection，回答“健康最后在人身上表现为什么”。
- **5 Founder Intents** = Invocation Vocabulary，仅用于自然语言路由。
- **Context × Health Clock** = 现实情境与时间尺度纪律。
- **Evidence × Authority** = 凭什么知道、谁有资格决定。

一个真实健康问题应视为这些维度的交叉切片，而非进入一个单一“模块”。

## 4. Personal Health CBM v1.1｜Health Office Capability Map

YHOS3 不新增第 17 个 Skill。4×4 CBM 继续作为能力地图，但语义从“软件能做什么”升级为“Health Office 如何把现实事务推进到底”。

|  | Observe｜看见 | Decide｜判断 | Act｜推进现实 | Learn｜变得更聪明 |
|---|---|---|---|---|
| **Evidence** | Zero-friction Intake | Evidence Adjudication | Clinician-ready Evidence Package | Longitudinal Baseline |
| **Risk** | Risk / Debt Sensing | Severity × Reversibility × Window × Uncertainty | Clinical Escalation / Expert Routing | Personal Risk Model |
| **Intervention** | Behavior / Constraint Baseline | Minimum-friction Action Design | Managed Execution | Outcome Response / Personal Rule |
| **System** | Freshness / Continuity | Authority + Attention Gate | Orchestration / Friction Removal | Learned Default / Reuse |

CBM 是地图；Skill 是地图上的可执行能力；Pathway 是穿过多个 Skill 的真实路线；Battle 是某一时期真正要赢的问题。

## 5. Health Office Runtime｜责任结构

YHOS3 的产品层不是“一个 AI”，而是一套责任结构：

### Principal

拥有 Purpose、风险偏好、重大选择、数据主权与最终授权。

### AI Health Brain

负责观察、整理、检索、比较、证据编译、候选判断、记忆与路由；不得独立取得临床法权。

### Health Steward

负责长期连续性、现实跟进、协调、提醒、交接和低认知负担体验；不得冒充医生。

### Expert Network

医疗与其他专业角色承担各自法定/专业边界内的判断。

### Service Graph

检查、医院、营养、训练、康复、配送、日程、旅行等现实服务可以被编排，但不因此取得 Health Truth 或 Authority。

## 6. Reality Learning Loop｜从 Advice 到 Learned Default

唯一现实脊柱保持：

```text
CTX → EVD → DEC → WPK → ACT → OUT → LRN → REUSE
```

严格条件：

- Plan / Recommendation 不得冒充 ACT。
- 没有 verified ACT，不得宣称 OUT。
- OUT 不自动等于 Attribution。
- OUT 不自动等于 Learning。
- LRN approved 不等于 REUSE。
- 没有 distinct Task2 的事前 preload + 实际使用 + reuse receipt，不得宣称 Compounding。

YHOS3 的长期终态不是更多 Advice，而是 **Learned Default**：过去经过现实验证的 Learning 在匹配 Context 下被事前加载，降低重复决策与管理负担；例外和高风险事件才升级本人注意力。

## 7. Invocation Contract｜自然语言是唯一前门

企业家不需要理解 C1/C2/C3/C4、H01–H12、CBM 或 Skill ID。

一级 Founder Intent 继续保持五类调用词汇：

1. `today_capacity`｜我今天状态怎么样？
2. `key_moment`｜明天有关键会议/路演，怎么安排？
3. `body_signal`｜最近身体有个信号，要不要处理？
4. `life_disruption`｜出差、熬夜、宴请、疾病把节奏打乱了怎么办？
5. `long_game`｜未来几年我最该防什么、练什么？

标准调用过程：

```text
Natural Language
→ Intent / Context / Clock
→ C1 boundary
→ C2 minimum sufficient evidence
→ C3 primary battle candidate
→ CBM route / Skill composition
→ Authority gate
→ C4 reality work package
→ ACT / OUT / LRN / REUSE
```

用户前台原则：**User language simple, machine contract strict.**

## 8. Principal Surface｜不要把后台复杂度投影给本人

前台默认只回答三件事：

1. **Need Me｜需要我**：0–1 个真正需要本人决定/授权的事项。
2. **Office Is Handling｜办公室正在处理**：系统正在替本人推进什么。
3. **Body Today｜今天的身体**：一条真正影响今日可调用能力的结论。

理想正常态允许显示：

> **今天，你不用操心健康。**

健康系统的价值之一，是让大量正常健康管理不再占用本人注意力。

## 9. Battle Sequencing Pattern｜UNLOAD → BUILD → TARGET

从真实 Founder 经验抽取一个可调用但非医学本体的策略模式：

```text
UNLOAD｜降低当前过载
→ BUILD｜建设恢复、肌肉、心肺、代谢等储备
→ TARGET｜处理剩余独立风险与局部问题
```

该模式只能作为 C3 Strategy Pattern。任何个人应用仍需 Evidence / Risk / Authority 判断，不得机械套用。

## 10. System KPI｜Management Burden Delta

除 Health Outcome / Risk Closure / Health Asset Delta 外，YHOS3 必须测量：

- Principal Time Cost
- Decision Count
- Manual Actions
- Attention Interruptions

目标是：

> **Better Outcome with Lower Principal Burden.**

候选价值公式：

```text
Health Office Value
= Outcome
+ Risk Closed
+ Time Saved
+ Attention Saved
+ Health Asset Delta
```

该公式是产品评估框架，不是医学效力公式。

## 11. Repository Architecture｜Public Law, Federated Reality

`yuanli-life/yuanli-health` 的长期角色冻结候选为：

> **Public Health Office Constitution + Capability Map + Invocation Contract**

它不是大型 Runtime/应用代码仓，不保存真实 Principal Health Reality，不复制上游 Skill implementation，不复制 private Health Engine。

推荐器官分工：

```text
yuanli-life/yuanli-health
= PUBLIC FRONT DOOR
  Constitution / Architecture / CBM / Invocation / Journey / Safety / Evaluation

moonstachain/yuanli-health-skills
= EXECUTABLE CAPABILITY SOURCE
  Skill contracts / adapters / synthetic qualification

moonstachain/yuanli-health-apple
= PRIVATE HEALTH ENGINE / DOMAIN RUNTIME
  Evidence / private runtime / health-domain engineering / reality validation
```

原则：**One Health Truth, federated organs, no parallel SSOT.**

## 12. Development Discipline｜三个 STOP

在 FIRST_FOUNDER_HEALTH_REUSE_PROVEN 前：

1. **STOP ontology expansion**：不再增加顶层本体。
2. **STOP equal investment across 16 Skills**：不平均发展所有 Skill，先打穿 Gold Journey。
3. **STOP app-first**：PC / Phone / Watch / Site / ChatGPT 都是 Surface，不作为主战役。

架构需求必须由 Reality 拉动，而不是由控制面自然膨胀。

## 13. Reality Maturity Gates

| Gate | 要证明什么 | 最低 PASS |
|---|---|---|
| G0 Law | 主权、临床、隐私、公共/私有边界稳定 | governed contracts |
| G1 Managed Gold Loop | Health Office 能推进一件真实事务 | verified ACT + observed OUT |
| G2 First Reuse | 上轮 Learning 改变下一轮 | preloaded LRN + changed Task2 + receipt |
| G3 Zero-Management | 显著降低本人管理负担 | burden delta evidence |
| G4 N=5–10 Founder Beta | 能迁移到不同企业家 | safety + usefulness + continuity |
| G5 Health Steward | 人+AI连续性价值 | closure / handoff evidence |
| G6 Expert Graph | 专业资源匹配产生学习 | expert-route → outcome trace |
| G7 Distribution | 学员可自然语言随时调用 | low-friction invocation |
| G8 Compounding | 系统随人持续变聪明 | repeated distinct-task reuse |

当前优先级：**G1 → G2 → G3**。

## 14. Non-goals

YHOS3 v0.1 不做：

- 不新增 Health Domain Ontology。
- 不新增第 17 个 Skill。
- 不在 public repo 保存真实健康数据、病例或 Reality Receipt。
- 不创建 AI clinical authority。
- 不证明医学疗效。
- 不要求一次构建完整 PC / iPhone / Watch App。
- 不把 12 Domains、6 Capacities 或 16 Skills 暴露为普通用户导航。

## 15. Success Definition

YHOS3 的第一个真正系统胜利不是“架构合并”，而是：

> **FIRST_FOUNDER_HEALTH_REUSE_PROVEN**

即一位真实企业家的 Task1 产生授权行动与观察结果，形成受审 Learning；在 distinct Task2 的 Decision 之前被正确 preload，并真实改变下一次判断或行动，留下可追溯 Reuse Receipt。

只有到这里，才允许宣称 Health OS 开始产生个人复利。
