---
type: repository-role-candidate
status: proposed
program: YHOS3
version: "0.1"
date: "2026-09-03"
repository: yuanli-life/yuanli-health
---

# YHOS3｜Public Repository Role v0.1

> **`yuanli-life/yuanli-health` = Public Health Office Constitution + Capability Map + Invocation Contract.**

## 1. Mission

本仓库是面向企业家 Principal 与学员的原力健康公共 Front Door。它负责让人理解、调用和审查原力健康的公共法、能力地图、调用契约与安全边界。

它不承担私有 Health Runtime，不保存个人健康事实，不复制上游可执行 Skill 实现，也不成为第二套 Health Domain Canon。

## 2. Allowed Content

允许进入本仓库：

- Health Office Constitution / product constitution candidates
- Health Optionality / Principal sovereignty projections
- YHOS architecture specifications
- Personal Health CBM / capability maps
- Founder Intent / invocation contracts
- public journey definitions
- synthetic-only examples / benchmark cases
- safety / authority / privacy contracts
- evaluation constitutions / non-claim receipts
- upstream pointers / pinned source identities

## 3. Forbidden Content

禁止进入本仓库：

- 真实或可重识别 Principal 健康数据
- 体检、病历、影像、化验原件或其可重识别摘录
- 真实 Runtime outcome ledger / reuse receipt
- API secrets / access tokens / private service credentials
- 将 AI synthesis 写成 Clinical Finding / Diagnosis 的材料
- 第二套个人 Health Truth / parallel SSOT
- 复制 `yuanli-health-skills` 的完整执行实现
- 复制 private Health Engine 的数据/runtime internals

## 4. Federated Organ Model

```text
PUBLIC FRONT DOOR
────────────────────────────────────────
yuanli-life/yuanli-health
Constitution / CBM / Invocation / Journey / Safety / Evaluation

            references / contracts
                     ↓

EXECUTABLE CAPABILITY SOURCE
────────────────────────────────────────
moonstachain/yuanli-health-skills
Skill contracts / adapters / synthetic qualification

                     ↓

PRIVATE HEALTH ENGINE / DOMAIN RUNTIME
────────────────────────────────────────
moonstachain/yuanli-health-apple
Private evidence / domain engineering / runtime / reality validation
```

原则：

> **Public Law × Private Reality**
>
> **One Health Truth × Federated Organs**
>
> **No Parallel SSOT**

## 5. Recommended Repository Shape

```text
yuanli-health/
├── README.md
├── constitution/
├── architecture/
├── capabilities/
├── invocation/
├── journeys/
├── safety/
├── evaluation/
├── synthetic-cases/
├── governance/
└── docs/specs/
```

目录是职责边界，不要求一次性填满。YAGNI：只有被实际 YHOS3 Journey 拉动的对象才新增。

## 6. Front Door Principle

普通 Founder 不应被要求理解：

- C1/C2/C3/C4 缩写
- H01–H12 Domain IDs
- 16 Skill IDs
- Evidence graph internals
- governance receipts

自然语言是第一入口；本仓库提供机器可读 Invocation Contract，使 ChatGPT / Codex / future surfaces 可以把自然语言安全路由到受治理的 Health Office 能力。

## 7. Repository Success Test

本仓库成功，不以文件数量衡量。

它必须让一个陌生的合格调用方能够回答：

1. 原力健康最终保护什么？
2. 本人、AI、医生、Steward 各有什么法权？
3. 一个自然语言健康请求应该如何进入系统？
4. 应调用哪些 Capability / Journey？
5. 什么情况必须停止、等待、升级或找专业人员？
6. 什么时候可以宣称 ACT / OUT / LRN / REUSE？
7. 哪些数据永远不应进入 public GitHub？

如果这些问题需要去 private runtime 猜答案，则 Public Front Door 尚未成立。
