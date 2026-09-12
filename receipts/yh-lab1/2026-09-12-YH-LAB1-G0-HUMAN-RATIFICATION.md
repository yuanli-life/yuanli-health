# YH-LAB1-G0｜Human Ratification Receipt

Date: `2026-09-12`

Decision: `ACCEPT_YH_LAB1_G0_WRITTEN_SPEC`

Artifact ratified:

- `docs/superpowers/specs/2026-09-12-yh-lab1-experimental-intelligence-lab-design.md`

Ratified strategic role:

> `YH-LAB1` is the experimental intelligence and product-admission laboratory subordinate to `YH-STRAT2｜Repeatable Principal Health Office`.

Ratified mission:

> Before a new intelligence route, Blueprint revision, prompt, context compiler, learning rule, or ProductRelease affects a real Principal, it must first survive reproducible evaluation and human adjudication.

Ratified v0.1 surface:

- Private Gradio Space: `Hay2045/yh-lab1-intelligence-lab`
- Private Eval Dataset: `Hay2045/yh-lab1-evals`
- Space hardware: `cpu-basic`
- HF Jobs for batch evaluation
- MCP-enabled Space read surface
- 20 Golden Cases
- 20 Hard Negatives
- 10 Synthetic Principals
- exactly 3 intelligence routes in the first comparison run
- Blind Human Adjudication
- Admission verdict: `ADMIT | HOLD | FAIL`

Ratified hard boundaries:

- raw Principal PHI is prohibited from the lab by default;
- YH-LAB1 is not Health Canon;
- YH-LAB1 is not Product State;
- YH-LAB1 does not execute real health actions;
- YH-LAB1 does not own clinical authority;
- YH-LAB1 may recommend admission but may not mutate Product Canon automatically;
- no fine-tuning or custom Health LLM is admitted in v0.1;
- all real-product admission still requires GitHub/Human governance.

Authority granted by this receipt:

- write the implementation plan;
- create the private HF Space and private Eval Dataset once write authorization is available;
- build and deploy the synthetic-only Gradio lab;
- run synthetic/de-identified batch experiments on HF Jobs;
- create the first v0.1 evaluation fixtures and admission dashboard;
- perform live smoke tests and MCP-read verification;
- write Reality Receipts back to the existing Draft PR branch.

Authority not granted:

- merge PR #11 to `main`;
- upload raw Apple Health or clinical PHI to Hugging Face;
- run autonomous clinical/commit/destructive health actions;
- fine-tune a Health LLM;
- auto-promote an intelligence route into `YH-MANAGED` without a later Human Gate.
