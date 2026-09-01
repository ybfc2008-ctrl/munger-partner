# PHASE 3｜RD-0002 Wells Fargo 销售实践最终独立 Verification

- Reviewer: `codex-independent-final-verifier:/root/usc_1994_final_verifier (phase-3-rd-0002)`
- Reviewed at: `2026-09-02`
- Scope: 修订后的 `RP-0002`、`RD-0002`、冻结的 `reviews/phase-3-rd-0002-critic.md` 六源身份与 locator 审计、`M02` 与 `KU-0002`。
- Review basis: 按窄范围任务要求，不重复全量外部检索；六份案件来源的法律身份、证据能力与 locator 以 Critic 审计为冻结底座。本报告只核对两份修订稿是否完整落实十项条件、是否形成非循环模型关联，以及现有结构校验是否通过。
- Constraint: 只写本报告；未修改 Research Pack、Real Decision、Model、KU、状态或路径；未生成 Master Content，未新增字段、模型、KU、Case、Agent、系统或自动化。

## 总裁决

**`VERIFIED`**

| 对象 | 裁决 | 精确结论 |
|---|---|---|
| `RP-0002` | `VERIFIED` as evidence pack | Critic 十项条件已落实；保持原路径及 `candidate research pack`，Research Pack 不迁移为 Case。 |
| `RD-0002` | `VERIFIED` | 准入为 `source_level: "A"` 的有限强证据案例；授权 `candidate → verified`。 |
| 文件迁移 | `VERIFIED` | 从 `cases/real-decisions/candidates/` 机械移动到 `cases/real-decisions/verified/`，文件名不变。 |
| `RD-0002 → M02` | `VERIFIED` | 保留 `model_ids: ["M02"]`；案件事实独立于 Munger 评论，关联不循环。 |
| `CU-2019-WSJ-0001` 作为案件证据 | `REJECT` | 继续只证明 Munger 的观点，不进入案件 `corpus_ids`，不证明 Wells Fargo 事实或因果。 |
| Master Content | `VERIFIED AFTER MIGRATION` | 仅在 RD 完成迁移、frontmatter 修改并通过校验后，才可开始制作候选 Master Content；本轮不生成。 |

本批没有待修对象；无 `REVISE` 或 `HOLD`。`source_level: A` 只评价本条目所保留的有限命题：强证据支持“销售目标—绩效评价—管理压力—奖惩后果”组合、反复内部信号和延迟根本修正之间的链条。它不表示激励薪酬是唯一原因、不确定每位员工的主观动机，也不把协商解决等同于庭审判决。

## 冻结版本与自动校验

### SHA-256

| 文件 | SHA-256 |
|---|---|
| `research-packs/RP-0002-wells-fargo-sales-practices.md` | `bd95cf26aeccdb28fdb675c084eb15a61d7c056462471d5fc4a83415da6f02fa` |
| `cases/real-decisions/candidates/RD-0002-wells-fargo-sales-practices.md` | `456398ca8b656949faf06465305b2a158e46f4ce09ad7e52d1a47eb5131c53dd` |
| `reviews/phase-3-rd-0002-critic.md` | `c8ba18acf240147ae5eee309fb799137e8febdd5baf6629c15e84f78c5e0ed4b` |
| `models/M02-incentives.md` | `cbcbbb880dbb16977b707757f6e02710929669851dac33b05e3ffda5f358a012` |
| `verified/KU-0002-incentives-are-easy-to-underestimate.md` | `9bcb818c2b1e126ac7b49fa7188db7624ef1349e8ab4b77bb346cb326f962539` |

若 RP、RD、M02、KU-0002 或冻结 Critic 在执行迁移前发生实质变化，本报告对受影响对象的机械授权失效，须重新审查。状态和路径按本报告执行所产生的预期哈希变化不视为实质变化。

### 自动校验

- `validate_sources.py`: 通过；46 sources，`A=8 / B=9 / C=17 / D=12`。
- `validate_corpus.py`: 通过；48 knowledge units，无错误，当前 Candidate RD 结构合法。
- `python3 -m unittest discover -s tests -p 'test_*.py'`: 11 项测试全部通过。
- 内容目录与知识关系搜索：未发现 RD-0002 的 Master Content 或其他提前派生内容；案件仅存在于 RP、Candidate RD 及已审查的 M02/KU 隔离说明中。

## Critic 十项条件逐项核验

| # | 条件 | 修订落实 | 裁决 |
|---:|---|---|---|
| 1 | 单次二元决定改为至少从 2012 年起反复出现的决策门槛 | RP Core question、事实重建第 3–4 项及 RD“问题/发生了什么”均使用反复升级、持续未根本改变和渐进修补，不虚构一次有明确日期的会议。 | `VERIFIED` |
| 2 | 主体限定为 Community Bank senior leadership，不把 Board 写成历年拥有相同信息 | RP 与 RD 均锁定主要主体；RP 明确不能假定所有层级在所有年份掌握相同信息，RD 边界禁止把事后报告自动回填为当时全部决策者知识。 | `VERIFIED` |
| 3 | 分开 2016 CFPB/OCC findings 与 2020 DOJ 公司同意事实 | RP 对 S1/S2 写明 `without admitting or denying`；S4 写明公司承认、接受并确认 Statement of Facts；RD“发生了什么”和边界保持同样区分。 | `VERIFIED` |
| 4 | 修正 S1、S3、S4、S5、S6 locator | S1 已含 p.2 ¶2、pp.4–5 ¶¶8–16；S3 已含 printed/PDF 双页码、调查范围和 pp.45–49；S4 已含 DPA p.4 ¶¶4–5、Exhibit A pp.18–25 ¶¶14–32；S5 已将 SEC Order 设为 primary document 并列 pp./¶¶；S6 已列 John Stumpf 与 printed pp.5–9。 | `VERIFIED` |
| 5 | 从狭义奖金扩展为组合机制 | RP 与 RD 统一使用“数量目标—绩效评价/后果—管理压力—奖惩后果”，并明确不把 incentive compensation 单列为主要或唯一原因。 | `VERIFIED` |
| 6 | 保留治理、监督、文化、信息升级和个体选择 | RP 建立“共同原因、替代解释与边界”；RD 关键错误和边界保留各因素的独立与交互作用，并明确系统压力不取消个人选择和责任。 | `VERIFIED` |
| 7 | 保留 CU-2019 不证明案件的隔离 | RP 单列“与 Munger Corpus 的隔离”；RD 明确 CU 不作为案件证据；KU-0002 和 M02 也继续声明该访谈不验证 Wells Fargo 因果。 | `VERIFIED` |
| 8 | 不用处罚金额、事后失败或 Munger 评论反推因果 | RD 明确禁止由最终处罚金额反推因果份额，并限制事后报告的知识回填；核心链条来自冻结六源中的同期信号与 DOJ 公司同意事实。 | `VERIFIED` |
| 9 | 不新增 Case 字段、模型、KU、Agent 或自动化 | RD 使用现有五项 frontmatter 与既有极简正文结构；`model_ids` 仅引用已批准 M02，`corpus_ids` 保持空数组。 | `VERIFIED` |
| 10 | Verifier 通过前不生成 Master Content | 当前未发现 RD-0002 Master Content；本报告也未生成内容。 | `VERIFIED` |

## 六源身份与定位的落实情况

本节不重做来源调查，只核对两份修订稿是否忠实承接冻结 Critic 审计。

### S1 / S2｜2016 CFPB 与 OCC consent orders

- 两份文件均被写成监管机构 findings，而不是 Wells Fargo 全面承认。
- RP 对“不承认也不否认”的适用范围及具体 locator 可追溯；RD 在“发生了什么”和边界中保留法律身份差异。
- S1/S2 支持销售目标、激励、具体不当实践以及监督/投诉/审计缺陷，但没有被用于证明所有账户或所有员工共享同一动机。

**裁决：`VERIFIED`。**

### S3｜2017 Independent Directors report

- 身份准确限定为董事会委托、独立董事和外部律师执行的事后公司内部调查，不写成法院认定。
- printed page 与 PDF page、调查方法、根因概览及 Community Bank 领导层章节已精确分开。
- “销售压力更常被员工提及、补偿激励有所贡献”的区别已经进入机制边界，阻止“奖金导致一切”的误读。

**裁决：`VERIFIED`。**

### S4｜2020 DOJ DPA / Statement of Facts

- RP 准确承接 Critic 的关键差异：DPA 虽是协商解决，但公司接受责任、确认 Statement of Facts 真实准确并受公开否认限制；同时不将其升级为庭审判决或自然人责任判定。
- locator 已缩到 DPA ¶¶4–5、Statement of Facts ¶¶14–32，决策重建进一步限定 ¶¶20–29。
- 这是 `source_level: A` 的主要依据：它直接承载目标与压力、不当行为、反复内部警示、替代建议、拒绝根本改变、个体归因和损害的连续事实链。

**裁决：`VERIFIED — PRIMARY CASE ANCHOR`。**

### S5｜2020 SEC Order

- 正式 Order 已取代事项页成为 primary document；事项页和 release 只作入口/辅助。
- RP 明确这是特定 SEC 程序中的同意 order，不等同于 DOJ 式一般事实承认，也不证明每位员工心理原因。
- locator 覆盖 settlement 身份、Summary 及销售模型、压力、升级信号和披露段落。

**裁决：`VERIFIED`。**

### S6｜2016 Senate hearing record

- 使用范围已收窄为“同期公开解释和争议”，并定位 John Stumpf 的 sworn statement 与 printed pp.5–9。
- RP 明确区分质询、开场陈述、证人证词和监管说明；没有把议员立场写成委员会 finding，也没有让听证单独承担因果证明。

**裁决：`VERIFIED — CONTEXTUAL SUPPORT`。**

## 真实决策与因果结构

### 反复决策重建

RD 没有宣称存在一次“维持还是取消目标”的单一会议。它重建的是至少自 2012 年起，在目标过高、低质量账户、misconduct、内部异议与替代方案反复升级之后，Community Bank senior leadership 多次面对的纠偏门槛。可选动作也没有被伪造为“全有或全无”：文本保留了渐进降标、处分个人、修改评价与奖惩、加强监督和信息升级等中间方案。

**裁决：`VERIFIED`。**这一重建有当时信号和替代建议作支撑，不是只凭 2016 后果的事后诸葛亮。

### 一个组合机制

条目只保留一个核心机制：当数量目标、绩效评价、管理压力与奖惩后果共同推动销售，而客户同意、产品质量和长期风险不能同等改变员工结果时，公开要求与实际环境发生错配；若反复异常仍被缩小为个体问题，系统修正被延迟。

治理、风险、审计、文化、组织结构、信息流和个体选择没有被新建成额外模型，而是作为共同原因、放大机制和因果边界保存。现有证据不分离估计各因素份额，条目也不声称该组合是每一行为的必要、充分或唯一原因。

**裁决：`VERIFIED`。**机制压缩符合“一个案例尽量只表达一个关键机制”，又没有用压缩消灭真实的共同原因。

## M02 关联与非循环性

**`model_ids: ["M02"]` 获准保留并随 RD 迁移生效。**

理由：

1. M02 已是 `owner-approved core model`，不是本案为自己新建的解释标签。
2. 六份案件材料独立支持实际销售目标、绩效后果、管理压力、激励设计、行为信号和延迟修正；即使删除 `CU-2019-WSJ-0001`，案例事实与核心机制仍成立。
3. KU-0002 和 M02 只证明 Munger 的激励观点与项目触发规则，并都明确拒绝把 2019 评论当成 Wells Fargo 因果调查。
4. RD 给 M02 提供真实增量：反复异常、当时提出的替代方案、组织把系统信号缩小为个体 misconduct，以及何时应从处分个人转向检查制度。

因此这不是“因为 Munger 说是激励，所以案件属于 M02”的循环证明。关联仍是非排他的：不得把 RD 改写为“Wells Fargo 证明激励决定行为”或“员工主要为奖金造假”。

`corpus_ids: []` 必须保持。不得把 `CU-2019-WSJ-0001` 或 KU-0002 加进案件事实关系字段。

## Source level 裁决

**授权 `source_level: "NEEDS_REVIEW" → "A"`。**

本案达到项目 A 级案例定义的有限含义：

- 强证据：官方监管、司法、证券执法、公司独立董事调查和官方听证记录相互补充；其中 DOJ DPA 保存公司明确同意真实准确的 Statement of Facts。
- 因果链清晰：销售目标/绩效/压力/奖惩环境，与不当行为、反复内部警示、具体替代建议、拒绝根本改变和持续损害之间存在可追溯链条。
- 非排他：A 级不表示单一原因、精确因果份额或每个自然人的责任已经确定。RD 当前边界是 A 级准入不可删除的组成部分。

若未来删除 DOJ 公司同意事实、把组合机制缩成单一奖金解释，或取消共同原因与个体责任边界，A 级授权立即失效。

## 精确机械迁移授权

按以下顺序执行，不作顺手改写：

1. 在当前 Candidate 文件 frontmatter 中只改两项：
   - `"status": "candidate"` → `"status": "verified"`
   - `"source_level": "NEEDS_REVIEW"` → `"source_level": "A"`
2. 保持：
   - `"corpus_ids": []`
   - `"model_ids": ["M02"]`
3. 将文件机械移动：
   - From: `cases/real-decisions/candidates/RD-0002-wells-fargo-sales-practices.md`
   - To: `cases/real-decisions/verified/RD-0002-wells-fargo-sales-practices.md`
4. 文件名和正文全部保持，不改标题、问题、事实、关键错误、原理、警报、关联模型、反证或来源。
5. `RP-0002` 保持 `candidate research pack`、原路径和当前内容；Research Pack 是可复用证据资产，不随 RD 移动，也不需要升级状态。
6. 重新运行 `validate_sources.py`、`validate_corpus.py` 与 11 项测试；只有全部通过，迁移才完成。

## Master Content 门禁

**迁移和校验完成后，可以开始候选 Master Content。**

授权范围仅是“开始制作”，不是自动发布或免审：

- 必须从迁移后的 Verified RD、RP 与已批准 M02 派生；
- 必须继续区分 CFPB/OCC findings、DOJ 公司同意事实、公司事后调查和听证陈述；
- 必须保留组合机制、共同原因、非排他因果和个体责任边界；
- Munger 2019 评论只能作为相关思想证据，不能承担案件事实；
- 不得把标题或叙事改成“奖金让 5300 名员工造假”“芒格解释/预言 Wells Fargo”或其他被本审查拒绝的强因果版本；
- Master Content 仍是内容候选，须按 `CONTENT-RULES.md` 独立完成事实、反证与发布质量检查。

在 RD 仍位于 Candidate 目录、frontmatter 尚未改为 `verified/A`，或迁移后校验未通过时，Master Content 保持 `HOLD`。

## 最终门禁

- **最终裁决：**`VERIFIED`。
- **证据等级：**`A`，仅限当前有限、组合且非排他的因果命题。
- **Candidate → Verified：**授权。
- **文件迁移：**授权移动至 `cases/real-decisions/verified/`，不改文件名。
- **M02 关联：**授权保留 `model_ids: ["M02"]`；`corpus_ids: []` 必须保持。
- **RP 状态：**保持 `candidate research pack`，不迁移。
- **额外修订：**无；除 status/source_level 与路径外不得修改生产内容。
- **Master Content：**仅在迁移和全量现有校验通过后可以开始；本轮不生成。

