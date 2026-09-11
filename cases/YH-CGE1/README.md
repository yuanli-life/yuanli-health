# YH-CGE1｜Sleep Recovery First End-to-End Compounding Proof

Status: `GATE_A_EXECUTION_CANDIDATE`

Authority parent: `YH2-C1-HEALTH-CONSTITUTION.md`

## Purpose

验证的不是“AI 会不会分析睡眠”，而是一个健康问题能否在不发生 Split Brain、法权越界或 PHI 外溢的条件下，完成：

`CTX → EVD → DEC → WPK → ACT → OUT → LRN → REUSE`

Gate A 只使用 `D2 Synthetic` 数据。真实 Apple Health / Watch 数据不得进入 Hugging Face、GitHub、Notion 或 OB LLM Wiki。

## Seven-plane discipline

| Capability interface | Current adapter | Only responsibility | Must never become |
|---|---|---|---|
| `RealityStore` | Local Health Kernel | 原始健康现实 / Canon | SaaS projection |
| `RuntimeRelay` | Supabase | Observed State / events / receipts | Health Canon / Law |
| `LawRegistry` | GitHub | Protocol / schema / policy / tests / admission | PHI store |
| `KnowledgeAdapter` | OB LLM Wiki | Evidence absorption / provenance | executable Law |
| `IntelligenceProvider` | Hugging Face | Model / embedding / eval / jobs | medical authority / Health SSOT |
| `ReasoningInterface` | ChatGPT | synthesis / explanation / orchestration | SSOT / autonomous authority |
| `HumanReviewSurface` | Notion | Principal cockpit / explicit review | machine Canon |

## Non-negotiable invariants

1. `Data ≠ Diagnosis`; `Knowledge ≠ Authority`; `Intelligence ≠ Authority`.
2. GitHub stores Desired State; Supabase stores Observed State; Local Health Kernel owns Reality State.
3. Hugging Face artifacts must resolve to an exact immutable revision before an eval receipt can pass.
4. D4/D5 is deny-by-default for cloud AI. D4-derived embeddings inherit D4 until independently reclassified.
5. Any unavailable SaaS may reduce capability or freshness, but must not invalidate the protocol. New privileged changes fail closed.
6. Local Health Kernel is not a replaceable SaaS. If RealityStore is unavailable, real-health decisions fail closed; only synthetic/shadow testing may continue.
7. Gate B (real N=1 sleep intervention) requires explicit Principal approval after Gate A receipt review.

## Gate A PASS

`PASS = Data Truth × Authority Truth × Intelligence Truth × Action Truth × Reality Truth × Learning Truth`

Any Critical gate = 0 ⇒ overall `FAIL`.

Gate A may prove architecture and replaceability, but it cannot claim real-world health benefit. Gate B is the first N=1 Reality experiment.