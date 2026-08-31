# KU-0007 / Batch 2｜独立 Verifier 最终裁决

- Verifier: `codex-independent-verifier:/root/rd_0001_verifier`
- Verified at: `2026-08-31`
- Inputs: `reviews/KU-0007-batch2-critic-review.md`、三条 L0、三条 L1、`candidates/KU-0007-competence-boundary.md`、`verified/KU-0005-disconfirming-evidence.md`
- Scope: 只裁决 L1、KU-0007 及两条证据与 KU-0005 的并入边界；不创建模型，不升级 B

## 总裁决

| 对象 | 裁决 | 授权 |
|---|---|---|
| `CU-2020-CALTECH-0001` | `VERIFIED` | 可将 `verification_status` 机械改为 `verified`。 |
| `CU-2021-DJCO-0001` | `VERIFIED` | 可将 `verification_status` 机械改为 `verified`。 |
| `CU-2023-ACQUIRED-0001` | `VERIFIED` | 可将 `verification_status` 机械改为 `verified`。 |
| `KU-0007` | `VERIFIED` | 可机械迁移至 `/verified`。 |
| `CU-2021-DJCO-0001 → KU-0005` | `VERIFIED` | 可并入，直接支持“准确呈现反方论证并主动寻找削弱原结论的证据”。 |
| `CU-2023-ACQUIRED-0001 → KU-0005` | `VERIFIED`（有限并入） | 可有限并入，只支持“识别错误后及时退出”。 |

三条 L0 的身份、日期和 `A-primary-recording / B-text-excerpt` 分层均可接受。任何机械迁移或并入都不得把三条 L1 升为 `A`，不得改变 `translation_status: "ai_draft"`，也不得新增模型。

## 一、CU-2020-CALTECH-0001

**裁决：`VERIFIED`**

- Caltech 官方活动页确认活动发生于 `2020-12-14`，讲话者身份和官方录影出处可追溯。第三方 transcript 页面显示的 12 月 16 日是发布或转录日期，不覆盖官方活动日期。
- 公开 transcript PDF pp. 6–7、lines 145–163 可复现完整语境：主持人询问接受自身限制是否有助于避免偏误，Munger 回答知道自己胜任与不胜任之处以及能力边界。
- 两个短引文连续、准确；中文没有把 `competency` 扩写为资格认证、道德能力或已验证预测记录。
- 当前文字来自未与录影逐字对齐的公开 transcript，`source_level: "B"` 正确。

允许的机械变更只有：

- `verification_status: "candidate"` → `verification_status: "verified"`。

必须保持：

- `source_level: "B"`，不得因官方录影存在而自动升级。
- `translation_status: "ai_draft"`。
- 当前问题语境和两个短引文，不扩写为“能力边界可保证避免错误”。

## 二、KU-0007｜把能力边界作为重大判断的检查项

**裁决：`VERIFIED`**

- Critic 指出的必要条件过度已经删除：标题不再称其为“前提”。
- Critic 指出的固定顺序已经删除：原理改为“应同时检查”，没有声称任何决定都必须先完成独立能力审计。
- `AI 推断` 标签保留；“可降低风险”没有升级成确定结果。
- 反例诚实留空；边界保留能力变化、拒绝学习、自我校准可能过度自信或过度保守等限制。
- 它不重复 `M01`，也不重复 KU-0002 至 KU-0006；但本裁决只批准知识单元，不批准“能力圈”模型。

允许机械迁移：

1. 从 `/candidates` 移入 `/verified`。
2. `status: "candidate"` → `status: "verified"`。
3. 四项 review check 改为 `true`，加入本 Verifier 标识和 `reviewed_at: "2026-08-31"`。

迁移时必须保持：

- 当前标题和 `AI 推断` 原理，不得恢复“前提”“先判断”或“必然避免错误”。
- `source.tier: "B"`、`models: []`。
- 反例待研究和全部边界。
- 不创建或批准“能力圈”一级模型。

## 三、CU-2021-DJCO-0001

**裁决：`VERIFIED`**

- `2021-02-24` 的事件日期、Daily Journal 年会和 Munger 讲话者身份可追溯；L0 已披露工作 transcript 中存在重复区块。
- 公开 transcript PDF p. 16、首次出现的 lines 508–520 可复现完整问题和连续回答。
- 第一条引文准确支持“能比反方更好地陈述反对自己结论的论证”；第二条直接支持 `looking for disconfirming evidence`。
- 中文“寻找反证”在本项目中应继续理解为寻找削弱或反驳原结论的证据，不是任意反对意见或严格形式逻辑反例。
- 尚未对齐录影时间戳，因此 `source_level: "B"` 正确。

允许的机械变更只有：

- `verification_status: "candidate"` → `verification_status: "verified"`。

必须保持 `source_level: "B"`、`translation_status: "ai_draft"`、首次出现的 locator 和问题语境。

## 四、CU-2021-DJCO-0001 并入 KU-0005

**裁决：`VERIFIED`**

2021 证据与 KU-0005 不是泛泛主题相似，而是直接补强其原理的前半部分：主动寻找会削弱原判断的证据。它还增加一项相关但不同的纪律：在评论前尽可能准确地呈现反方论证。

授权以下精确并入：

1. 在 `KU-0005.corpus_ids` 加入 `CU-2021-DJCO-0001`。
2. 在正文增加且仅增加这一事实说明：`2021 年证据直接支持准确呈现反方论证并主动寻找削弱原结论的证据。`
3. 在出处中加入 2021 年会的 B 级公开 transcript 定位。

必须保持的限制：

- 该证据不证明 Munger 在某一具体决定中实际更新了信念。
- 该证据不证明该做法改善了投资回报或其他决策绩效。
- 不把“能陈述反方论证”写成真理保证，也不把任意反对意见当成反证。
- 保留 KU-0005 的 `models: []`、反例待研究和全部边界。

若只执行以上限定变更，可视为本 Verifier 已授权的机械证据合并；不得借合并重写 KU-0005 的标题、扩大因果或建立模型。

## 五、CU-2023-ACQUIRED-0001

**裁决：`VERIFIED`**

- Acquired 官方 episode 页面确认讲话者、长访谈身份与发布日期 `2023-10-30`。
- 第三方 timestamped transcript 在 `00:10:34–00:11:03` 明确记载 Diversified Retailing 收购 Baltimore 一家百货连锁、竞争激烈、意识到严重错误以及决定撤回的连续语境。
- 修订后的 L1 已交代 `it` 所指交易，不再把引文悬空成一般抽象信念。
- `terrible mistake` 译作“严重错误”、`take the hits to look foolish rather than go broke` 译作“宁可承担看起来很愚蠢的代价，也不要破产”，语义准确且没有声称破产必然发生。
- 因本轮文字依赖第三方 transcript 且未独立复听，`source_level: "B"` 正确。

允许的机械变更只有：

- `verification_status: "candidate"` → `verification_status: "verified"`。

必须保持：

- `source_level: "B"`、`translation_status: "ai_draft"`。
- Diversified Retailing、Baltimore 百货连锁和“随后决定撤回交易”的语境。
- “尚未独立复听”的 locator 限定。
- `rather than go broke` 是 Munger 当时的风险判断与行动理由，不是已经验证的反事实。

## 六、CU-2023-ACQUIRED-0001 有限并入 KU-0005

**裁决：`VERIFIED`（仅限下述有限并入）**

该证据可以补强 KU-0005 原理的后半部分：意识到原决定严重错误后，愿意承担难堪和现实代价退出。它没有交代发现了什么新证据，也没有提到主动寻找反证，因此不能支持 KU-0005 标题的完整命题。

授权以下精确有限并入：

1. 在 `KU-0005.corpus_ids` 加入 `CU-2023-ACQUIRED-0001`。
2. 必须在正文紧邻关联处加入原句：`2023 年证据只支持识别错误后及时退出，不支持主动寻找反证。`
3. 在出处中加入 Acquired 访谈的 B 级文字定位及未独立复听限制。

必须保持的限制：

- 不把该证据写成“主动寻找反证”的第二次证明。
- 不将其放入 KU-0005 的反例或成功案例字段。
- 不宣称撤回交易创造了后来成功，也不宣称不撤回必然破产。
- 只可写成 Munger 对该决定的回顾性自述；实际交易结果与反事实未在本单元独立核验。
- 保留 KU-0005 当前反例、边界、`models: []` 和 B 级分层。

若不能完整保留上述限定语，则不得把 `CU-2023-ACQUIRED-0001` 加入 KU-0005。

## 七、KU-0005 精确机械修订边界

若同时并入两条新证据，允许将：

```json
"corpus_ids": ["CU-2020-DJCO-0001"]
```

机械改为：

```json
"corpus_ids": [
  "CU-2020-DJCO-0001",
  "CU-2021-DJCO-0001",
  "CU-2023-ACQUIRED-0001"
]
```

并在正文保留这两句不可删减的功能区分：

> 2021 年证据直接支持准确呈现反方论证并主动寻找削弱原结论的证据。
>
> 2023 年证据只支持识别错误后及时退出，不支持主动寻找反证。

除增加上述 IDs、两句功能说明和对应出处外，不授权改变 KU-0005 的标题、原理主句、反例、边界、模型映射或来源等级。执行后可保持 Verified，但 review 记录应体现本次证据合并已由本独立 Verifier 审查。

## 最终限制

- 三条 L1 全部维持 `B`；存在 A 级录影不等于当前文字片段是 A。
- 本批不新增模型；KU-0007 和 KU-0005 均保持 `models: []`。
- Verified 表示引文、分层和受限推断通过，不表示 Munger 的回顾性因果叙述已经获得外部验证。
- 不增加新结构；只使用现有 Markdown、目录和字段完成迁移与并入。
