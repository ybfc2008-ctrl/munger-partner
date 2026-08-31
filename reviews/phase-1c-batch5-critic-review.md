# PHASE 1C Batch 5｜独立 Critic Review

- Reviewer: `codex-independent-critic:/root/rd_0001_verifier`
- Reviewed at: `2026-08-31`
- Scope: `MTP-1986-HARVARD`、`MTP-2003-UCSB`、`MTP-2019-DJCO` 的 L0/L1，`KU-0009`，以及 `sources/source-manifest.csv` 对应三行。
- Constraint: 本报告不修改生产文件、Candidate、Verified 条目或 manifest；不新增结构、KU 或模型。

## 总裁决

| 对象 | 裁决 | 核心判断 |
|---|---|---|
| `MTP-1986-HARVARD/source.md` | `VERIFIED` | 作为 D 级来源记录准确；学校、日期和讲话者仍只是现存文本的内部归属，不是独立核验事实。 |
| `CU-1986-HARVARD-0001` | `VERIFIED` | 仅验证其 D 级 research-lead 身份、公开页码和短摘录；不授权把 `verification_status` 改为 verified。 |
| `1986 → 任何 KU/模型` | `REJECT` | D 级材料按项目规则只能用于寻找更强来源，不能成为上层原理或模型证据。 |
| manifest `MTP-1986-HARVARD` | `REVISE` | `ready_candidate` 与“research lead only”矛盾，应恢复 `needs_source`。 |
| `MTP-2003-UCSB/source.md` | `VERIFIED` | 日期、讲座身份、Tilson 转录和 Munger 后续轻度编辑均由 PDF 首页直接支持，B 级正确。 |
| `CU-2003-UCSB-0001` | `REVISE` | 页码正确，但两处摘录都截掉关键尾部；应只保留一条完整短摘录以减少重复和版权暴露。 |
| `2003 → KU-0004` | `REVISE` | 方向直接相关，但只能补强“后果继续产生后果”的一般规则，不验证 Medicare 数字或任何具体因果。 |
| manifest `MTP-2003-UCSB` | `VERIFIED` | 来源身份、B 等级、公开链接和后续行动均准确。 |
| `MTP-2019-DJCO/source.md` | `VERIFIED` | 日期与 CNBC 原始录影可核对；未具名公开 transcript 的选段保持 B 且待录像对齐，分层诚实。 |
| `CU-2019-DJCO-0001` | `REVISE` | 页码和现有短语准确，但选段漏掉“问题无法消除、却被当作不存在”的关键逻辑。 |
| `KU-0009` | `REVISE` | 与 KU-0005 相邻但不重复；当前“仍可改善/解决”误读来源，应改为“无法消除但仍需应对”。 |
| manifest `MTP-2019-DJCO` | `VERIFIED` | A 录影 / B 选段、未识别 transcriber 和待时间对齐均已保留。 |

## 一、1986 Harvard School

### `MTP-1986-HARVARD/source.md`

**裁决：`VERIFIED`，仅限 D 级 research-lead 来源记录。**

- 现存公开 PDF 的标题页写有 `Speech by Charlie Munger to the Harvard School` 和 `JUNE 13, 1986`。
- PDF 本身没有转录者、首发出版者、版次、学校档案编号或保存链；本轮也没有找到 Harvard-Westlake 官方节目单、录音或学校档案页。
- 因此当前 L0 使用 `Reported speaker`、`Reported event date`，并把来源标为 `D-unattributed-transcript-lead`，处理正确。
- 文本内部提到 Headmaster Berrisford、本人是长期 trustee 等细节，只能增强内部一致性，不能替代外部来源验证。
- 不能因为该演讲被广泛转载、后来收入书籍或存在 2022 年印刷版本，就倒推当前 PDF 是可靠的原始 transcript。

### `CU-1986-HARVARD-0001`

**裁决：`VERIFIED`，但只授权保留为 D 级 research lead。**

- locator 正确：两段文字位于现存四页 PDF 的文件第 3 页，公开解析行 104–108；Drive 行 98–108 可作为私有辅助定位。
- `Invert, always invert.` 与 `many hard problems are best solved only when they are addressed backward` 都是所列 PDF 的连续短片段。
- 中文方向准确；第二句更自然且不扩大的译法可为“许多难题，只有反向处理时才能得到更好的解决”，但当前版本没有构成必须阻断的事实错误。
- 两段合计属于必要的短摘录，没有复制长段落；`link_and_excerpt` 符合当前版权边界。
- `speaker` 中的 `attribution not independently verified`、正文“不作为已验证的 Munger 原话”、`source_level: D` 必须永久保留，直到找到更强的独立来源。

这里的 `VERIFIED` 只表示“D 级线索的身份、定位和转写已被审查”，**不授权**：

- 把 `verification_status` 从 `candidate` 改为 `verified`；
- 迁移到 `/verified`；
- 用于证明“Munger 认为 X”；
- 关联任何 KU、核心模型、Case 或 Decision Engine 结论。

### `1986 → KU / 模型`

**裁决：`REJECT`。**

- 项目规则明确规定 D 级只作为寻找 A/B/C 的线索。
- 即使“逆向思考”在其他可靠 Munger 材料中可能存在，也不能用本条 D 级文本建立或补强上层条目。
- 若未来恢复学校档案、原始节目单、可靠录音或有明确保存链的授权文本，应建立更强 L0/L1 后重新审查；不得直接升级当前文件。

### manifest `MTP-1986-HARVARD`

**裁决：`REVISE`**

唯一必要修改：

- 将 `ingest_status` 从 `ready_candidate` 改回 `needs_source`。

以下字段保持：

- `source_class: unattributed_transcript`；
- `evidence_level: D-lead`；
- 当前公开 PDF 仅作 comparison copy；
- `next_action: Research lead only; locate official school archive program or recording before higher-layer use`。

不得为解决状态冲突而新增 `research_lead` schema；现有 `needs_source` 已足够。

## 二、2003 UCSB 与 KU-0004

### `MTP-2003-UCSB/source.md`

**裁决：`VERIFIED`**

- Tilson PDF 首页直接列出完整讲题、`Herb Kay Undergraduate Lecture`、UCSB Economics Department、Charles T. Munger 和日期 `2003-10-03`。
- 首页同时写明 `Transcript by Whitney Tilson`、Tilson 做了原始轻度编辑和链接，之后由 speaker 再做轻度编辑。当前 L0 对编辑链的描述准确。
- 这使其符合 B 级可靠具名 transcript；但它不是 UCSB 官方录影，也不是未经编辑的逐字稿，不能升级为 A。
- `B-named-speaker-edited-transcript`、`link_and_excerpt` 与“未确认存留官方录影”均应保留。

### `CU-2003-UCSB-0001`

**裁决：`REVISE`**

#### 定位

- 当前 locator 正确：文件第 17 页、印刷页码 `-14-`，公开 PDF 解析行 587–602；标题为 `Too Little Attention to Second and Higher Order Effects`。
- Drive `extracted lines 587-602` 与公开 PDF 解析恰好接近，但两套提取行号属于不同介质；locator 应继续同时保留页码，不能只依赖行号。

#### 摘录问题

- 第一处原句完整为：`the consequences have consequences, and the consequences of the consequences have consequences, and so on.` 当前删掉 `and so on`，虽不改变主要方向，却没有标省略。
- 第二处当前截在第二层 effect，删掉了来源中紧随其后的第三层及延续语，恰好削弱了本条要证明的高阶后果。
- 两句表达同一机制。为简洁、减少版权摘录并避免人为拼接，最小方案不是同时扩长两句，而是只保留第一条完整短句；第二条及 Medicare 叙述留在上下文说明，不作为第二段逐字引文。

#### 翻译

建议与唯一完整短句对应：

`后果还会产生后果，而后果所产生的后果又会继续产生后果，如此延续。`

不得把这句话扩写为“所有后果都会无限连锁”或“二阶后果一定比一阶后果更重要”。

### `CU-2003-UCSB-0001 → KU-0004`

**裁决：`REVISE`；完成 L1 修订并通过 Verifier 后，可有限并入既有 KU-0004。**

- 该句直接支持 KU-0004 的核心：评估不能在直接结果处停止，后续结果还可能继续产生影响。
- 它没有提供传导机制、方向、时间尺度或可观察指标；KU-0004 现有边界“不能无限联想”必须完整保留。
- 源文随后以 Medicare 成本预测说明激励改变行为，但本单元没有独立核验原始预测、实际成本、`1000%` 数字或排他因果。因此不得把 Medicare 写成 verified case，也不得把它当作 KU-0004 的因果证明。
- 本条只补强既有原则，不创建“高阶后果”“连锁效应”或其他新 KU/模型。

**修复后的机械合并授权边界：**

1. 先按上节只保留第一条完整短摘录，并保持 `source_level: B`、`translation_status: ai_draft`。
2. L1 通过独立 Verifier 后，将 `CU-2003-UCSB-0001` 加入 `KU-0004.corpus_ids`。
3. 在 KU-0004 只增加一句：`2003 年 B 级文本直接补充：后果还会继续产生后果，但没有说明所有后续影响都应无限纳入。`
4. 在出处加入 Tilson PDF、文件第 17 页 / 印刷第 14 页和 speaker-edited transcript 限定。
5. 不改变 KU-0004 标题、原理、反例、边界或 `models: []`；合并后的完整版本必须重新独立验证。

### manifest `MTP-2003-UCSB`

**裁决：`VERIFIED`**

- `named_speaker_edited_transcript` 与 `B-traceable-transcript` 准确反映编辑链。
- `canonical_url` 直接指向 Tilson PDF，开源审阅者可复现首页身份和选段页码。
- `next_action` 正确保留 Tilson 与 Munger 后续编辑归属，并继续寻找 UCSB 档案或录影。

## 三、2019 Daily Journal 与 KU-0009

### `MTP-2019-DJCO/source.md`

**裁决：`VERIFIED`**

- CNBC 页面和其频道录影把活动标为 `2019-02-14` Daily Journal Annual Meeting；日期与视频身份一致。
- 当前公开 comparison transcript 是完整会议文本，但在所检查部分未给出 transcriber。L0 已披露这一限制。
- 因 CNBC 完整录影是原始讲话证据，活动身份可为 A；当前摘录只在公开文本中定位、尚未与录像逐字和时间戳对齐，因此保持 B 是可接受的上限。
- 若未来发现公开 transcript 与录像不一致，应以录像为准；manifest 的 A 不得自动升级 L1 文字。

### `CU-2019-DJCO-0001`

**裁决：`REVISE`**

#### 定位与文本

- locator 正确：公开 PDF 文件第 3 页，解析行 99–108；当前 Drive 行 99–108 与该段一致。
- 两个现有短语都可在来源中复现，中文基本准确。
- 但来源的决定性结构不是一般的“否认不利表现”，而是：Munger 认为主动投资管理行业面对一个**无法彻底消除**的问题，却把它当作不存在；他随后区分解决问题与改善应对。当前摘录删除了这个限制，直接诱发 KU-0009 的过度抽象。

#### 最小必要摘录

为同时保留关键限制并控制版权摘录，可替换为两条合计仍很短的原句：

> `They have a horrible problem they can’t fix, so they just treat it as nonexistent.`
>
> `this problem thoroughly understood is half solved or better coped with.`

对应中文可为：

> `他们有一个无法彻底解决的严重问题，于是干脆把它当作不存在。`
>
> `充分理解这个问题，等于解决了一半，或至少能更好地应对。`

继续保留语境：这是 Munger 对主动投资管理行业面对指数投资表现时反应的判断，不是本项目已经独立验证的行业事实或普遍因果结论。

### `KU-0009`

**裁决：`REVISE`，保留为独立候选；不合并进 KU-0005。**

#### 当前过度抽象

- 标题“仍可应对”本身不算错误，但文件名和原理多处使用 `fixable / 仍能通过行动改善`，容易被理解为问题可以解决。
- 原文明确把该问题描述为无法修复，并只主张理解有助于改善应对。因此本条必须围绕“无法消除但仍需面对”，而不是“有可执行修复方案”。

#### 建议机械收窄

- 标题改为：`不要用否认回避无法消除但仍需应对的问题`。
- 文件 slug 同步机械改为 `KU-0009-denial-does-not-remove-practical-problems.md`，避免 `fixable-problems` 与来源冲突；这只是重命名，不是新增结构。
- 原理改为：

  `AI 推断：现实问题即使无法彻底消除，也可能需要诊断、适应或降低损失；把它当作不存在会阻断理解与应对。承认问题不保证解决，但使更好应对成为可能。`

- 当前反例中“没有独立证明行业所有参与者都在否认”应保留。
- 当前边界应调整措辞但保留实质：对死亡等真正不可控且无需现实调整的事实，控制注意力或接受可能合理；本条不要求对所有不可解问题持续投入。
- `models: []` 和“不关联核心模型”保持。

#### 与 KU-0005 的重复检查

KU-0009 与 KU-0005 相邻，但不是换名重复：

| 条目 | 触发状态 | 要求的动作 |
|---|---|---|
| `KU-0005` | 原判断仍可能错误，需要主动检验 | 寻找、识别并吸收削弱原判断的证据，必要时退出原结论 |
| `KU-0009` | 问题已经显现，但因不愉快或难以消除而被当作不存在 | 先承认并理解问题，再选择适应、退出或降低损失 |

2019 选段没有要求主动寻找反证，也没有描述信念因新证据而更新。强行并入 KU-0005 会把“否认一个已显现的问题”误写成“主动证伪”。因此：

- 不合并进 `KU-0005.corpus_ids`；
- 不改变 KU-0005；
- 不创建核心模型；
- KU-0009 修订后仍须单独通过 Verifier。

### manifest `MTP-2019-DJCO`

**裁决：`VERIFIED`**

- `broadcaster_recording_plus_transcript`、`A-primary` 可描述组合来源身份。
- `next_action` 已明确选段只是 B、需与 CNBC 录影对齐、transcriber 未识别，边界充分。
- L1 必须继续按 B 处理，不能因 manifest 为 A 而升级。

## 机械修订总清单

1. manifest 1986：`ready_candidate → needs_source`；其余 D 级限制不变。
2. 1986 L0/L1：不需改内容；保留为 D 级 research lead，不迁移 verified、不关联任何上层资产。
3. 2003 L1：只保留第一条完整句，中文同步，页码与 B 级不变。
4. 2003 → KU-0004：仅在 L1 经 Verifier 后按上述一句窄域说明合并；不把 Medicare 变成案例，不新增 KU/模型。
5. 2019 L1：用“无法彻底解决却当作不存在”与“理解后更好应对”两句短摘录替换当前组合，保留行业语境、B 级和未对齐录像限制。
6. KU-0009：修改标题、文件 slug、原理和边界措辞，使其从“可解决问题”收窄为“无法消除但仍需应对的问题”；保持 `models: []`。
7. KU-0009 不合并 KU-0005；两者的触发状态和动作边界必须保留。

## 最终结论

1. 1986 只是一条经过定位核对的 D 级 research lead；任何 KU、模型或 Verified 关联一律拒绝。
2. 2003 是可靠的 B 级 speaker-edited transcript；精简并修复摘录后，只可有限补强 KU-0004。
3. 2019 的来源链可以支持 B 级文字候选；KU-0009 有独立决策价值，但必须忠实保留“无法彻底解决、仍需更好应对”的原始边界。
4. 本批不新增系统、字段、KU 或模型；所有问题均可通过现有 Markdown、文件名和 manifest 字段机械修复。
