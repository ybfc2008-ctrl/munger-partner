# PHASE 1C Batch 6｜独立 Critic Review

- Reviewer: `codex-independent-critic:/root/rd_0001_verifier`
- Reviewed at: `2026-09-01`
- Scope: `MTP-2017-DJCO`、`MTP-2017-DJCO-FIRESIDE`、`MTP-2022-SINGLETON` 的 L0/L1，`KU-0010`，以及 `sources/source-manifest.csv` 对应三行。
- Constraint: 本报告不修改生产文件、Candidate、Verified 条目或 manifest；不新增结构、KU 或模型。

## 总裁决

| 对象 | 裁决 | 核心判断 |
|---|---|---|
| `MTP-2017-DJCO/source.md` | `VERIFIED` | CNBC 活动身份与日期、Santangel's Review publisher transcript 身份可复现；A 活动 / B 文字分层正确。 |
| `CU-2017-DJCO-0001` | `REVISE` | 页码、英文和翻译方向正确，但缺少 Circle of Competence 问题语境，且当前两段摘录合计略超最小版权需要。 |
| `2017 main → KU-0007` | `REVISE` | 不是新原则；修订后可窄幅补强“复杂系统中的能力边界会随时间变化”，但不能证明任何具体边界。 |
| manifest `MTP-2017-DJCO` | `VERIFIED` | B 级 publisher transcript 与待 CNBC 对齐的行动项准确。 |
| `MTP-2017-DJCO-FIRESIDE/source.md` | `VERIFIED` | Richard Lewis 具名、明确基于 1 小时 48 分录音转录，日期、地点和发布信息可复现，B 级正确。 |
| `CU-2017-DJCO-FIRESIDE-0001` | `REVISE` | 页码和原文准确，但代词 `them` 依赖问题语境；“cheaper”应译为学习代价更低，而非泛指便宜。 |
| `fireside → KU-0008` | `REJECT` | 选段支持“从他人和错误中学习”，不支持“终身学习是一项持续责任”；上联会扩大 KU-0008。 |
| manifest `MTP-2017-DJCO-FIRESIDE` | `VERIFIED` | 具名、录音驱动的 transcript 与 B 等级准确；不得升级为官方 Daily Journal transcript。 |
| `MTP-2022-SINGLETON/source.md` | `REVISE` | 官方资料只旁证 2022 Prize 活动日期；未知 transcriber、未知原始发布者、非官方转存录像且未对齐，不足以让当前文字达到 B。 |
| `CU-2022-SINGLETON-0001` | `REVISE` | locator 可复现 comparison PDF，但来源应暂降 D；第一句漏掉能力限定，第二句漏掉“逐渐碰到答案”的结果。 |
| `KU-0010` | `NEEDS_REVIEW` | 概念独立且有决策价值，但 D 级证据不能支撑上层条目；须先完成录音对齐或恢复可靠发布链。 |
| manifest `MTP-2022-SINGLETON` | `REVISE` | 应恢复 D-lead / needs_source，不能把“未来可比对”当成已经完成的 B 级验证。 |

## 一、2017 Daily Journal 主会

### `MTP-2017-DJCO/source.md`

**裁决：`VERIFIED`**

- CNBC 活动页确认 Charlie Munger 在 `2017-02-15` Daily Journal 年会讲话；这足以确认活动、讲话者和日期。
- 公开 PDF 标为 Santangel's Review 发布的完整 transcript；虽然所检查页面没有披露个人 transcriber，但 publisher 身份稳定、文本完整、公开可复现，并有 CNBC 活动记录可供后续核对。
- 当前选段尚未与 CNBC 录影做时间戳和逐字对齐，所以 `A-broadcaster-event-record / B-publisher-transcript` 分层正确；A 只属于活动记录，不自动传递给文字。
- 不得把 Santangel's Review 文本称为 CNBC transcript 或 Daily Journal 官方 transcript。

### `CU-2017-DJCO-0001`

**裁决：`REVISE`**

#### Locator 与上下文

- 当前 locator 正确：Santangel's Review PDF 文件第 32 页，公开解析行 1122–1131；Drive 行 1122–1131 与该段对应。
- 提问者明确问的是 Circle of Competence 的边界如何识别、是否会重画、扩张或收缩。Munger 的回答先指出人会把错误认识当真，再说明复杂系统中的经验法则会随文明变化而失效。
- 缺少这个问题语境时，第二个片段无法独立说明“两类”分别指什么，也不能自然连接 KU-0007。

#### 引文、翻译与版权

现有两段均是来源中的连续文字，中文方向正确。但第一段加第二段合计没有必要地超过了表达本机制所需的最短篇幅。建议使用带明确省略号的两个短片段：

> `the rules of thumb … in year one may not work in year 40`
>
> `you have to live with both kinds of uncertainty`

中文可对应为：

> `某套经验法则在第一年有效，到第四十年未必仍然有效；`
>
> `人必须面对这两类不确定性。`

这里的省略号必须明确表示从同一句中删去了不影响该机制的重复修饰，不得把拼接后的短语冒充连续完整句。继续保持 `translation_status: ai_draft`。

### `CU-2017-DJCO-0001 → KU-0007`

**裁决：`REVISE`；L1 修订并通过 Verifier 后，可有限补强。**

- KU-0007 现有边界已写“能力边界会变化”。2017 选段的增量是直接给这条边界增加 Munger 文本支持：复杂系统和文明变化可能使旧经验法则失效。
- 它不是新的“动态能力圈”原则，也没有给出判断某项能力何时扩张或收缩的方法。
- 它不证明经验越老越差，不适用于物理定律等来源明确区分的稳定规律，也不证明四十年是固定更新周期。

**机械合并边界：**

1. L1 增加 Circle of Competence 的最短问题语境，并按上节缩短引文。
2. L1 通过独立 Verifier 后，将 `CU-2017-DJCO-0001` 加入 `KU-0007.corpus_ids`。
3. 只在 KU-0007 边界或原话说明中增加：`2017 年 B 级文本补充：复杂系统与环境变化可能使过去有效的经验法则失效，因此能力边界需要重新校准。`
4. 保留 KU-0007 标题、原理、反例、既有边界和 `models: []`；不得另建 KU 或模型。
5. 合并后的完整 KU-0007 必须重新独立验证。

### manifest `MTP-2017-DJCO`

**裁决：`VERIFIED`**

- `broadcaster_context_plus_publisher_transcript` 和 `B-traceable-transcript` 准确。
- CNBC 活动页可作为 canonical event context；`next_action` 正确要求把 Santangel 选段与录影对齐。

## 二、2017 年会后 Fireside Chat

### `MTP-2017-DJCO-FIRESIDE/source.md`

**裁决：`VERIFIED`**

- 保存 PDF 记录原始文章为 Richard Lewis 于 `2017-04-03` 发布，并给出原 Latticework Investing URL。
- Lewis 明确称其从 1 小时 48 分钟的录音转录完整谈话，并尽可能准确；这满足具名、录音驱动 transcript 的 B 级条件。
- 文本把事件定位为 `2017-02-15` Daily Journal 年会后的 informal chat，并给出 `949 E 2nd St, Los Angeles`。当前 L0 没有把它冒充正式年会或 Daily Journal 官方记录。
- 录音片段本批未独立复听，因此不能升级为 A，也不能去掉 `recording-based transcript` 限定。

### `CU-2017-DJCO-FIRESIDE-0001`

**裁决：`REVISE`**

- locator 正确：PDF 文件第 29 页、解析行 848–854；选段位于 `Video 20 of 22 7:39` 标记之前。
- 问题是如何系统地从错误中学习、避免重复，以及是否做 post-mortem。Munger 回答他们既从他人的经历中间接学习，也从令人不快的亲身经验中学习；`them` 指此前所说的 mistakes。
- 当前第一句和第二句均可逐字复现，合计是短摘录，版权范围适当。
- `cheaper` 在此比较的是从他人经验学习与亲身付出错误代价；建议译为“因为这种学习的代价低得多”，而不是口语化的“便宜得多”。
- L1 必须增加一行上述问题语境，否则把 `Nobody can avoid them` 翻译成“错误”缺少文本内锚点。

### `CU-2017-DJCO-FIRESIDE-0001 → KU-0008`

**裁决：`REJECT`**

- KU-0008 的命题是把终身学习视为持续责任，证据锚点是 `moral duty` 与 `lifetime learning`。
- Fireside 选段只讨论学习来源：借助他人经验、亲身错误和事后复盘。它没有谈终身、持续责任或长期知识更新。
- 把它加入 KU-0008 会把“如何从错误中学习”误写成“终身学习义务”的重复证据；并不会提高 KU-0008 的可追溯性。
- 修订后的 Fireside L1 可作为 B 级 standalone Corpus 进入 Verifier，但不得加入 `KU-0008.corpus_ids`，不得改变 KU-0008，也不得据此新建 KU 或模型。

### manifest `MTP-2017-DJCO-FIRESIDE`

**裁决：`VERIFIED`**

- `named_recording_based_transcript`、`B-traceable-transcript`、Richard Lewis 归属与 replay 行动项准确。
- canonical URL 当前指保存 PDF而非原始已失效页面，这一限制已在 L0 中通过原始发布信息补足；不是升级障碍。

## 三、2022 Singleton Prize Conversation

### `MTP-2022-SINGLETON/source.md`

**裁决：`REVISE`**

#### 可确认与不可确认

- Singleton Foundation 的同期发布确认 2022 Prize 活动于 `2022-04-19` 在 Los Angeles 举行，并列出 Todd Combs 为评审成员。它能旁证活动日期和组织者。
- 当前 comparison PDF 内部写有 Charlie Munger、Todd Combs、日期和 The Maybourne Beverly Hills；非官方平台保存的影音也与这场对话的外观和声音相符。
- 但官方发布没有确认这段 Munger–Combs 对话、具体 venue 或当前 transcript；PDF 没有 transcriber、原始 publisher 或保存链；所列 YouTube 也不是 Singleton Foundation、Million Stories Media 或活动方官方频道。
- 本批没有实际复听并把选段对齐到该转存录像。因此“未来可以比较”只是验证路径，不是已经完成的验证。

#### 来源等级

当前 `B-traceable-event-transcript` 不成立。项目 B 要求可靠完整 transcript、采访记录或授权转载；未知转录者加未知发布链，不能仅凭一个未对齐的非官方录像转存跨过该门槛。

最小修订为：

- L0 活动背景可写 `A-official-prize-event-date`；
- 当前 transcript/选段改为 `D-unattributed-transcript-lead`；
- 明确官方资料只确认 Prize 活动日期，不确认 transcript 的发布链；
- 增加 Singleton Foundation 同期活动公告作为 event context；
- 保留非官方录像链接作为待核对材料，不称为 official 或 surviving primary source。

若以后实际复听，确认 Munger 和 Combs 的说话者身份、选段文字及精确时间戳，并说明录像中的 Million Stories Media 或活动方制作标识，可重新提交 B 级审查；不得在完成前预先升级。

### `CU-2022-SINGLETON-0001`

**裁决：`REVISE`，修订后仍只能作为 D 级 research lead。**

#### Locator

- PDF `pp. 7-8` 过宽且略显混乱：第一段位于文件第 7 页（解析行 176–182），第二段位于文件第 8 页（解析行 185–194）。应分别标明两个页码或统一写 `PDF file pp. 7-8, lines 176-194`。
- `extracted lines 179-194` 会漏掉第一段的上文限定，包括 temperament 和持续投入背景。若依赖 Drive 行号，应改为覆盖 176–194。

#### 引文与翻译

- 第一段当前删掉“如果你具备合理程度的聪明”这一显式限定，容易把长期注意力写成充分条件。
- 第二段当前只保留持续处理重要问题，删去了逐渐碰到答案的经验性结果；这正是 KU-0010 原理所依赖的部分。
- 在保持短摘录的前提下，可改为：

> `a long attention span will help you a lot, if you’re reasonably smart.`
>
> `you keep working over the serious problems, that you’ll stumble into an answer.`

中文可为：

> `如果你具备基本的理解能力，长时间保持注意力会很有帮助；`
>
> `持续反复处理重要问题，可能会逐渐碰到答案。`

原句采用带偶然性的“碰到答案”措辞，并不保证找到答案；中文必须保留“可能”，不得把 Munger 的回顾性经验总结写成独立验证的因果规律。

#### 必须同步修改

- `source_level: B → D`；
- `speaker` 改为 `Charlie Munger (reported; wording not independently aligned)` 或同等明确表述；
- locator 加 `nonofficial recording timestamp not yet aligned`；
- 不改 `verification_status: candidate`，也不迁移 verified。

### `KU-0010-long-attention-on-serious-problems.md`

**裁决：`NEEDS_REVIEW`，不是概念性 `REJECT`。**

#### 独立性与决策价值

- 它不重复 KU-0008：KU-0008 是持续学习与知识更新；KU-0010 是把有限注意力长期投入少数可推进的重要问题。
- 它不重复 KU-0007：KU-0007 检查本人是否有能力理解问题；KU-0010 处理通过长期、反复注意推进问题。
- 它也不重复 KU-0009：KU-0009 处理无法消除但仍需承认和应对的问题；KU-0010 主动筛掉来源判断为不可修复的问题，集中于仍可能推进者。
- 作为决策规则，它有清楚的触发条件和停止边界：问题重要、存在反馈、仍可推进，同时长期注意不是无限坚持。因此具有独立价值。

#### 当前阻断点

- 唯一证据目前只能按 D 级处理；项目规则禁止 D 级材料支撑上层 Knowledge Unit。
- 当前原理中的“比在大量问题间快速切换更可能……”没有出现在来源中，是未经比较证据支撑的新增因果比较。
- `source.tier: B` 与出处“按 B 处理”必须同步降为 D，并把 review 状态保持未通过。

#### 来源修复后才可采用的机械文本

只有当 CU 经录音对齐并重新审定为 B 后，KU-0010 才可继续 Verifier。届时：

- 标题 `把长期注意力留给重要且可能推进的问题` 可保留；
- 原理收窄为：

  `AI 推断：对少数仍可推进的重要问题，持续或间歇性地反复投入注意力，可能逐步形成答案；长期注意本身不是充分条件。`

- 删除与“在大量问题间快速切换”的无来源比较；
- 保留现有反例；
- 保留“不可控、无反馈、机会成本上升时应停止”的边界；
- 保持 `models: []`，不得新建核心模型。

如果无法恢复可靠发布链或完成选段录音对齐，则 KU-0010 应停止在 research candidate，不得进入 Verified。

### manifest `MTP-2022-SINGLETON`

**裁决：`REVISE`**

机械修改：

1. `source_class: traceable_event_transcript → unattributed_transcript_plus_unofficial_recording`。
2. `evidence_level: B-traceable-transcript → D-lead`。
3. `ingest_status: ready_candidate → needs_source`。
4. `canonical_url` 不应把 Worldly Partners 保存 PDF 暗示为原始出版者；可留作 comparison URL，但 L0 必须另列 Singleton Foundation 官方活动公告。若 manifest 的 canonical 严格指原始发布者，则暂时留空。
5. `next_action` 改为：`Identify original publisher or transcriber; replay and timestamp-align selected excerpt to the surviving nonofficial recording before considering B.`

不新增新的 manifest 字段即可表达这些限制。

## 机械修订总清单

1. 2017 主会 L1：补 Circle of Competence 问题语境，使用明确带省略号的最短摘录，保留 B。
2. 2017 主会 → KU-0007：L1 通过后仅增加“复杂系统会使旧经验法则失效、边界需校准”的窄幅补强；不新增 KU/模型。
3. Fireside L1：补 post-mortem/错误学习语境，把 `cheaper` 译为“学习代价低得多”，保留 B。
4. Fireside → KU-0008：拒绝关联；修订后只作为 standalone Corpus。
5. Singleton L0/L1：把当前文字 B 降为 D，加入官方 Prize 日期背景，保留未知 transcriber、未知 publisher、非官方录像和未对齐限制。
6. Singleton L1：修正页码/行号范围，补回能力限定和经验性结果，继续 candidate，不迁移 verified。
7. KU-0010：标 `NEEDS_REVIEW`；删除无来源的“优于快速切换”比较。只有 CU 将来升回 B 后才进入下一道门。
8. Singleton manifest：改为 D-lead / needs_source，并记录恢复发布链及录音时间戳对齐的下一步。

## 最终结论

1. 2017 主会提供 KU-0007 的有用边界证据，不是新原则，也不只是无价值重复。
2. Fireside 是可靠 B 级 transcript，但当前选段不应上联 KU-0008；证据真实不等于模型关系成立。
3. Singleton 的活动大概率真实且文本可研究，但当前出处链没有达到 B；必须把“可验证”与“已验证”分开。
4. KU-0010 概念上独立且有决策价值，当前因证据等级而 `NEEDS_REVIEW`；这不是新增模型的理由。
5. 本批全部问题可通过现有 Markdown、metadata 和 manifest 字段修复，不新增系统或结构。
