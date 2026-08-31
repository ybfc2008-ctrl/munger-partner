# PHASE 1C Batch 4｜独立 Critic Review

- Reviewer: `codex-independent-critic:/root/rd_0001_verifier`
- Reviewed at: `2026-08-31`
- Scope: 本批新增的 3 个 L0、3 个 L1、`KU-0008`，以及 `sources/source-manifest.csv` 对应三行。
- Constraint: 本报告不修改 L0、L1、Candidate、Verified、manifest 或模型；不新增 KU、模型或目录结构。

## 总裁决

| 对象 | 裁决 | 核心判断 |
|---|---|---|
| `MTP-2007-USC/source.md` | `REVISE` | 活动身份和日期可靠，但未对齐录像的 Joe Koster 具名笔记应为 C，不是 B transcript。 |
| `CU-2007-USC-0001` | `REVISE` | 来源等级应降为 C；两处英文不是所列公开笔记的精确文字，中文也需随精确英文调整。 |
| `KU-0008` | `REVISE` | 原则候选有独立价值且不重复 M01，但来源等级依赖 L1，原理又加入了来源没有明说的环境变化机制。 |
| `MTP-2022-DJCO/source.md` | `VERIFIED` | 日期、Yahoo Finance 原始录影、Richard Lewis 文本身份和 A 录影 / B 摘录分层均诚实。 |
| `CU-2022-DJCO-0001` | `REVISE` | 英文摘录删掉了 `or the level of skill your adviser has`，与中文不对称；还需明示问题由 transcript 概括。 |
| `2022 → KU-0007` | `REVISE` | 只可作为“能力边界进入投资选择”的窄域补强；L1 修复后可合并，不得另建 KU/模型。 |
| `MTP-2000-WESCO/source.md` | `REVISE` | C 级和转述警示正确，但应补出含选段的 Motley Fool Part 2 精确公开页。 |
| `CU-2000-WESCO-0001` | `REVISE` | 选段位于 Part 2，不在当前 `source_url` 指向的 Part 1；公开 locator 尚不能直接复现。 |
| `2000 standalone Corpus` | `REVISE` | 修复公开定位后，可仅作为 C 级独立 Corpus；不得称为 Munger 逐字原话。 |
| `2000 → KU-0001/M01` | `REJECT` | 只重复既有更强证据，来源较弱且没有新增机制或边界；合并会稀释而非增强证据链。 |

## 一、2007 USC 与 KU-0008

### `MTP-2007-USC/source.md`

**裁决：`REVISE`**

#### 可确认事实

- USC Gould 官方页面确认 Charlie Munger 为该届毕业典礼演讲者，日期为 `2007-05-13`。活动身份可以按 A 级处理。
- 公开 PDF 首页明确标为 `Notes by Joe Koster`。它是具名第三方笔记，不是 USC 官方稿，也没有自称完整逐字 transcript。
- 存留录像使未来逐字复核成为可能，但“录像存在”不等于“未对齐的笔记已经按录像验证”。当前选段没有时间戳，不能据此把文字证据升为 B。

#### 来源等级

项目 `RULES.md` 把 B 定义为可靠完整 transcript、采访记录或授权转载，把 C 定义为有明确记录者身份的现场第三方笔记。当前材料明确属于后一类。因此：

- `A-official-event-identity` 可保留；
- `B-text-excerpt` 必须改为 `C-named-third-party-notes`；
- 不得用 `traceable text` 或可检查录像的潜在能力绕过等级规则；只有实际复听并对齐选段后，才可另行评估升级。

### `CU-2007-USC-0001`

**裁决：`REVISE`**

#### 阻断问题

1. `source_level: B` 不符合来源身份，应改为 `C`。
2. 当前第二句 `you’re hooked for lifetime learning` 不是所列 Joe Koster PDF 的完整精确文字；公开笔记写的是：`it means that you are hooked for lifetime learning.`
3. 当前第三句 `advance in life by what you’re going to learn` 不是该 PDF 的文字；公开笔记写的是：`You’re going to advance in life by what you learn after you leave here.`
4. 第一处短语 `wisdom acquisition is a moral duty` 可在公开笔记复现，但如果使用引号，大小写和句号也应与锚定版本一致，不应把多个版本拼成一组看似逐字引文。

#### 中文与上下文

- “这意味着必须终身学习”可以表达原意，但应在英文恢复 `it means` 后与之对应；`hooked` 在这里是“从此必须持续学习”，不是成瘾诊断。
- “人生的进步来自此后继续学到的东西”方向正确，但英文需先恢复 `after you leave here` 的毕业典礼语境。
- 最短语境应说明：Munger 在毕业典礼中把获取智慧称为道德责任，并由此引出离校后的终身学习；本条不是经录像核准的逐字稿。

### `KU-0008-lifelong-learning.md`

**裁决：`REVISE`，不 `REJECT`**

#### 可保留

- “把终身学习作为持续责任”由 `moral duty` 与 `lifetime learning` 直接支撑，是与 M01 不同的候选原则。
- 它不重复 `KU-0007`：后者处理能力边界校准，本条处理长期继续学习的责任。
- `models: []`、反例待研究、因果边界和“不关联核心模型”均应保留。不得为了归入 Munger Partner 而关联 M01，也不得新建一级模型。

#### 必须收窄

- `source.tier` 与出处中的文字摘录等级必须从 B 改为 C，直到完成录像对齐。
- 原理中“已有知识会随环境与问题变化而变得不充分”是合理的现代解释，却不是这段选文明确提出的机制。为避免过度抽象，可机械收窄为：

  `AI 推断：现有知识不足以支撑一生的判断；把持续学习视为责任，使知识在长期中不断更新。`

- 不得把这项主张写成已经证实“终身学习导致长期成功”的因果规律。当前反例和边界已经正确承认这一点。

### 2007 最小机械修订清单

1. L0：把 `A-official-event-identity / B-text-excerpt` 改为 `A-official-event-identity / C-named-third-party-notes`；解释同步改为“选段尚未与录像对齐，不能作为 B transcript”。
2. L1：把 `source_level` 改为 `C`；locator 保留 PDF 页码和“录像时间戳未对齐”。
3. L1：把三处英文统一为 Joe Koster PDF 的精确文本：
   - `Wisdom acquisition is a moral duty.`
   - `it means that you are hooked for lifetime learning.`
   - `You’re going to advance in life by what you learn after you leave here.`
4. L1：中文随精确英文调整，并补一行最短毕业典礼语境；继续保持 `translation_status: ai_draft`。
5. KU-0008：把 `source.tier` 和出处中的摘录等级改为 C，收窄原理；保留 `models: []`、反例和全部边界。
6. manifest：把 `MTP-2007-USC` 的 `source_class` 改为 `official_context_plus_named_notes` 对应的明确笔记表述，并把 `evidence_level` 从 `B-traceable-transcript` 改为 `C-named-notes`；`next_action` 继续要求与录像对齐后才能评估升级。

## 二、2022 Daily Journal 与 KU-0007

### `MTP-2022-DJCO/source.md`

**裁决：`VERIFIED`**

- 活动日期 `2022-02-16`、Yahoo Finance 录影与 Daily Journal 年会身份相符。
- Richard Lewis 文本明确披露：观众问题经常被概括，而 Munger 与 Gerry Salzman 的陈述尽可能准确转录。当前 L0 没有把概括后的问题冒充逐字提问。
- `A-primary-recording / B-text-excerpt` 分层正确。录影是 A；尚未时间对齐的文字摘录仍是 B。
- 该 L0 不需要修改，也不得把其 A 级录影身份自动传递给 L1 摘录。

### `CU-2022-DJCO-0001`

**裁决：`REVISE`**

#### 引文与翻译

- 公开 transcript 的完整相关短语是：`you have to figure out your level of skill, or the level of skill your adviser has, and that should enter the equation.`
- 当前英文只保留本人能力，却在中文加入“或顾问”，造成引文与翻译不对称。
- `that should enter the equation` 在这里不是抽象的所有决策规则，而是回答不同投资方式并无一刀切时，应把本人或顾问能力纳入选择。

#### 语境限制

公开 transcript 将主持人问题概括为：如何为一名 22 岁投资者选择投资方式，涉及缓慢积累收入/股息与追逐 AI、成长股等路径。该问题不是逐字转录。L1 应增加一行最短语境并明确 `question summarized by transcript`。

#### 最小必要修改

1. 将英文合并为一个精确句子：`So I think you have to figure out your level of skill, or the level of skill your adviser has, and that should enter the equation.`
2. 中文可改为：`所以我认为，你必须判断自己或顾问的能力水平，并把这一点纳入选择。`
3. 增加语境：问题由 transcript 概括，回答针对投资方式没有一刀切；不得扩写成对任何具体投资风格的普遍优劣结论。
4. 保持 `source_level: B`、`translation_status: ai_draft` 和“官方录影时间戳未对齐”。

### `CU-2022-DJCO-0001 → KU-0007`

**裁决：`REVISE`；完成上述修订并通过 Verifier 后，只可有限合并。**

- 这段话直接补强 `KU-0007`：在选择投资方式时，本人或顾问的能力水平应进入判断。
- 它没有证明某种投资方式普遍更好，也没有验证顾问能力、投资绩效或能力自评的准确性。
- 它不构成新原则或新模型；只允许并入现有 `KU-0007`，且 `models: []` 必须保持。

**修复后的机械合并边界：**

1. 将 `CU-2022-DJCO-0001` 加入 `KU-0007.corpus_ids`。
2. 只增加一句窄域说明：`2022 年 B 级文本在投资选择语境中补充：本人或顾问的能力水平应进入判断；它不把任何具体投资风格判为普遍最优。`
3. 在出处加入 2022 transcript 链接、页码及未对齐录影的限制。
4. 不改变 KU-0007 的标题、原理、反例、边界或 `models: []`；合并后的完整条目仍需重新独立验证。

### manifest 的 2022 行

**裁决：`VERIFIED`**

- `official_recording_plus_transcript`、`A-primary` 可以描述该 L0 组合来源；`next_action` 已明确选段仍需对齐并须保留概括问题警示。
- 必须继续在 L1 单独标 B，不得因 manifest 的 A 自动升级摘录。

## 三、2000 Wesco 与 M01 关联

### `MTP-2000-WESCO/source.md`

**裁决：`REVISE`**

#### 来源身份与等级

- Motley Fool 第一页明确表明 Whitney Tilson 亲临会议，并披露部分内容因记录速度不足而属于 paraphrase。
- 因而 `C-named-third-party-notes` 正确，且不得升级为 B 或把选段称为 Munger 逐字原话。
- 精确会议日期和原始录音仍未恢复；`2000` 只能作为事件年份，`2000-05-15` 是文章发布日期，不得混用。

#### 公开定位问题

当前 Identity 只列 Part 1：

`https://www.fool.com/archive/boringport/2000/05/15/charlie-munger-speaks.aspx`

但本批选段实际位于 Part 2 的 `Mental Models for Investing`：

`https://www.fool.com/archive/boringport/2000/05/15/charlie-munger-speaks-part-2.aspx`

L0 必须增加 `Selected excerpt page` 指向 Part 2；Part 1 可继续作为整组文章的起始页与转述警示证据。

### `CU-2000-WESCO-0001`

**裁决：`REVISE`**

- 当前英文片段可以在 Part 2 复现，中文没有明显扩大；C 级和“可能为转述”的双重警示正确。
- 当前 `source_url` 指向 Part 1，而 locator 声称该页含 `Mental Models for Investing`，开源审阅者无法按此路径直接复现选段。这是阻断性定位错误。
- `source_url` 应机械改为 Part 2，locator 改为 `Motley Fool Part 2, section 'Mental Models for Investing'; Drive readable-text extraction lines 186-190`。
- 如继续使用引号，正文必须紧邻保留“以下是 Whitney Tilson 现场笔记，部分内容可能是转述”，不得在上层把它改写成 verbatim Munger quote。

### 作为独立 Corpus

**裁决：`REVISE`；修复 Part 2 定位后可作为 C 级 standalone Corpus 进入后续 Verifier。**

允许保留的价值是来源历史和检索线索，而不是新增一个已验证原则。必须永久保留：

- `source_level: C`；
- `Charlie Munger (reported by Whitney Tilson; may be paraphrased)`；
- 文章发布日期不等于会议日期；
- 无录音或官方 transcript 的限制。

### `CU-2000-WESCO-0001 → KU-0001/M01`

**裁决：`REJECT`**

- 内容只重复“重要学科中的重要思想”和“单一模型”的警告，已被 1994 B 级连续论述更直接地支撑。
- 2016 B 级材料已经为 KU-0001 增加真正的边界：专精是主要职业能力，综合是补充和防御层。2000 C 级转述没有增加新的机制、冲突或适用边界。
- 将它并入 `KU-0001.corpus_ids` 会使较弱转述看起来与核心证据并列，降低可读性和证据压缩率。
- 因此不得把它加入 KU-0001，不得标注 `models: ["M01"]`，不得成为 M01 evidence anchor，也不得据此新建 KU 或模型。

### manifest 的 2000 行

**裁决：`REVISE`**

1. `evidence_level: C-named-notes` 保持不变。
2. `source_class` 建议机械统一为更明确的 `named_third_party_notes`，避免被误读为 transcript。
3. `canonical_url` 可保留 Part 1 作为文章入口，但 `next_action` 必须补充：`selected excerpt is on Motley Fool Part 2`；L0/L1 则必须给 Part 2 的直接链接。若项目将 manifest 的 canonical 定义为选段锚点，也可直接换成 Part 2，但不得同时声称 Part 1 含该选段。
4. 保留 `Preserve paraphrase warning; locate precise meeting date or primary recording`。

## 最终结论与下一道门

1. 本批目前没有任何 L1 或 KU 可直接机械迁移到 Verified；先完成上述最小修订，再交独立 Verifier。
2. 2007 活动身份可靠，但当前文字必须按 C 级 Joe Koster 第三方笔记处理；KU-0008 可保留为独立候选，不关联 M01。
3. 2022 L0 与 manifest 行通过；L1 补回顾问短语并保留概括问题警示后，只能有限补强 KU-0007。
4. 2000 修正 Part 2 精确定位后，可作为 C 级 standalone Corpus；与 KU-0001/M01 的关系明确拒绝。
5. 本批不新增 KU、模型、Agent、字段或目录；全部问题可用现有 Markdown、metadata 和 manifest 机械修复。
