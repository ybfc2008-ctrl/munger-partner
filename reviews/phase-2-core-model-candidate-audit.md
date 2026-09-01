# PHASE 2｜Core Model Candidate Audit

- Status: `CANDIDATE_REVIEW`
- Scope: `KU-0001`–`KU-0009`
- Constraint: 本文件只做候选审计；不新增正式 Model，不改变 KU，不建立 Case 关系。

## 审计问题

每个候选只检查四件事：

1. 是否在不同时期、不同场景的 Corpus 中重复出现？
2. 是否具有独立决策功能？
3. 是否能被现有 `M01` 无损解释？
4. 当前证据是否足以承担一级模型，而不是只做枝条、检查规则或例证？

## 候选结论

### Candidate A｜激励的行为力量容易被系统性低估

- Evidence anchor: `KU-0002`
- Corpus span: `1995 / 2002 / 2015 / 2019`
- Source mix: `B / C / C / B`
- Decision function: 检查制度实际奖励、惩罚和衡量什么，以及这些安排会把行为推向哪里。
- Independence from M01: `M01` 说明如何组织多个模型；本候选说明一种独立的行为驱动机制，不能被 `M01` 无损替代。
- Audit result: `STRONG CORE MODEL CANDIDATE`
- Boundary: 不得把激励当作行为的唯一原因；具体案例仍须证明“激励结构 → 行为变化 → 结果”。

### Candidate B｜把能力边界作为重大判断的检查项

- Evidence anchor: `KU-0007`
- Corpus span: `2003 / 2017 / 2020 / 2022`
- Source mix: `C / B / B / B`
- Decision function: 在行动前判断本人或顾问是否具备可靠理解问题所需的知识、经验和判断能力。
- Independence from M01: 多模型知识并不等于对具体问题具有胜任能力；本候选决定何时应行动、学习、求助或放弃。
- Audit result: `STRONG CORE MODEL CANDIDATE`
- Boundary: 能力边界会变化；不能用它合理化拒绝学习，也不能仅凭自我感觉划界。

### Candidate C｜一阶结论正确，不代表总体判断正确

- Evidence anchor: `KU-0004`
- Corpus span: `2003 / 2017`
- Source mix: `B / B`
- Decision function: 检查直接效果之后的反馈、适应和后续影响，避免在第一步停止判断。
- Independence from M01: `M01` 要求多角度组织事实；本候选要求沿因果链继续追踪后果，具有不同的检查动作。
- Audit result: `CORE MODEL CANDIDATE — NEEDS COMPARATIVE REVIEW`
- Boundary: 不能把“二阶后果”变成无限联想；必须说明传导机制、时间尺度和可观察结果。

## 暂不升级

| KU | 当前处理 | 原因 |
|---|---|---|
| `KU-0003` 交易压力 | `MERGE CANDIDATE INTO KU-0002` | 成交压力本质上是制度激励把“完成交易”替代“只做足够好的交易”；当前只有一条 A 级来源，不足以另建树干。 |
| `KU-0005` 主动用反证更新信念 | `HOLD` | 独立决策功能很强，但现有证据集中在 `2020–2023`；先检查更早 Corpus 是否重复出现。 |
| `KU-0006` 渠道标签不足以证明回报 | `HOLD / EXAMPLE` | 当前是一条窄检查规则，且 KU 自身已注明可能只是 `KU-0005` 的例证。 |
| `KU-0008` 终身学习 | `HOLD / POSSIBLE M01 SUPPORT` | 当前只有一条 C 级文字证据；尚不足以证明它应作为独立一级模型。 |
| `KU-0009` 不要用否认回避问题 | `HOLD` | 当前只有一条 B 级文字证据，且尚未形成跨时期重复证据。 |

## 对 M01 的结论

`M01` 保持不变。`KU-0002`、`KU-0007` 和 `KU-0004` 不能仅因都属于“思考方法”就并入 `M01`；但本审计也不授权把它们直接编号为正式模型。

## 建议人工门

正式模型只建议在以下选择后进入 Critic / Verifier：

1. 是否批准 Candidate A 进入正式模型审查；
2. 是否批准 Candidate B 进入正式模型审查；
3. Candidate C 是现在审查，还是先寻找第三个跨时期证据锚点。

在人工选择前，不修改 `models/`、KU 的 `models` 字段或任何 Case 关系。
