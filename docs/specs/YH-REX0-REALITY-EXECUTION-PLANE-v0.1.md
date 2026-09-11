# YH-REX0｜Reality Execution Plane v0.1

Status: `IMPLEMENTATION_CANDIDATE`
Date: `2026-09-11`

## 1. Purpose

把“正确候选判断”安全地推进成“真实世界可验证动作”，并以 Receipt 关闭每一个 Action。

YH-REX0 不负责决定医学真相；它负责：

```text
Trigger → Context Fetch → Policy Check → Authority Gate → Action Contract
→ Orchestrate → Execute → Receipt → Observed State → Follow-up
```

## 2. Components

### 2.1 n8n Orchestrator

唯一职责：工作流状态机。

允许：
- webhook / schedule / event trigger；
- 读取最小 Projection；
- schema validation；
- approval / wait / retry / timeout；
- 调用 API adapter 或 Local Ego Runner；
- 写入 Receipt / execution state。

禁止：
- 保存完整 Health Canon；
- 通过任意 shell 命令绕过 Action Contract；
- 自动把 LLM 文本升级成医疗决策；
- 在没有 Authority Gate 的情况下提交高风险动作。

### 2.2 Ego Last-Mile Runner

唯一职责：在真实、已登录浏览器里执行 allowlisted browser action。

Ego Runner 必须：
1. 接收 Action Contract，而非开放式自然语言；
2. 创建/复用隔离 Task Space；
3. 校验 `allowed_domains`；
4. 执行 `allowed_actions`；
5. 在 `requires_approval` 处停住；
6. 生成结构化 Receipt；
7. 不保存浏览器 cookie / token 到 GitHub、日志或 Receipt。

### 2.3 Action Queue

n8n 与 Ego 之间不得直接共享任意 shell 权限。推荐：

```text
n8n → signed Action Contract → queue/service → local ego-runner → Receipt → n8n
```

开发阶段可直接调用；生产阶段必须通过最小权限的 runner boundary。

## 3. Action Classes

| Class | Examples | Default authority |
|---|---|---|
| READ | 查询排班、读取状态、抓取公开/本人授权信息 | system / steward |
| PREPARE | 填表草稿、准备预约、上传前预览 | steward |
| COMMIT | 提交预约、发送材料、确认服务 | principal / explicit delegate |
| CLINICAL | 诊断、处方、停药、治疗选择 | clinician + principal as applicable |
| DESTRUCTIVE | 取消、删除、撤回、支付不可逆费用 | explicit principal approval |

`CLINICAL` 不允许由 Ego 或 n8n 自行决定。

## 4. Contract Admission

Action Contract 进入队列前必须满足：

- schema valid；
- `principal_ref` 非空且与 runtime context 一致；
- `contract_id` 唯一；
- 未过期、未撤销；
- target domain 在 allowlist；
- action 在 allowlist；
- 所需批准均已满足；
- sensitivity 与最小必要 payload 相符；
- `receipt_required=true`。

失败即 `REJECTED`，不得尝试“自动修复后执行”。

## 5. Receipt Semantics

Receipt 不是日志摘要，而是现实执行证据。至少包含：

- contract_id / execution_id；
- actor / executor / authority；
- started_at / finished_at；
- attempted_actions[]；
- external reference（如预约编号，允许脱敏）；
- result status；
- evidence hash / screenshot hash（如适用）；
- error class；
- next required gate；
- no-secret attestation。

浏览器截图若含敏感数据，不进入公开仓库；Receipt 只保存受治理引用与哈希。

## 6. Failure Policy

可重试：网络超时、页面暂时不可用、元素 transient missing。

不可自动重试：
- 权限不足；
- target domain drift；
- 页面语义改变导致 selector 不可信；
- 费用、取消、医疗授权等不可逆步骤；
- principal / clinician approval 缺失；
- contract expired/revoked。

## 7. Initial Reality Probe｜2026-09-11

已实测当前授权 Mac：

- `ego-browser` 存在并可调用；
- ego lite Browser Process 正在运行；
- 创建隔离 Task Space 成功，smoke receipt: `taskSpaceId=30`；
- 本机未发现全局 `n8n` CLI；
- 检测到多个 `n8n-mcp` 进程，但这不等于 n8n production runtime 已验证；
- Docker 当前未发现运行中的 n8n 容器。

因此当前裁决：

```text
EGO_LOCAL_RUNNER_CAPABILITY = PASS
N8N_ORCHESTRATOR_RUNTIME    = NOT_YET_PROVEN
YH_REX0                     = PARTIAL_PASS
```

下一 Reality Gate：明确现有 n8n 实例地址/运行方式，或在隔离开发环境启动 n8n，并完成 `Action Contract → n8n → Ego dry-run → Receipt` 首条闭环。
