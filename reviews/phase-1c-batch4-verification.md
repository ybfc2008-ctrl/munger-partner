# PHASE 1C Batch 4｜独立 Verifier 最终裁决

- Verifier: `codex-independent-final-verifier:/root/usc_1994_final_verifier (phase-1c-batch4)`
- Verified at: `2026-08-31`
- Inputs: `reviews/phase-1c-batch4-critic-review.md`、修订后的 3 条 L0、3 条 L1、`KU-0008`、既有 Verified `KU-0007`，以及 manifest 对应三行
- Scope: 只裁决现有条目、精确机械修订和既有 KU 的有限证据并入；不修改生产文件或状态，不新增 KU、模型、字段或目录结构

## 总裁决

| 对象 | 裁决 | 机械授权 |
|---|---|---|
| `MTP-2007-USC/source.md` | `VERIFIED` | L0 无需再改；永久保持“活动身份 A / 文字笔记 C”分层。 |
| `CU-2007-USC-0001` | `REVISE` | 当前不得改为 `verified`；按本报告指定的两处完整英文与对称中文修复后，可机械设为 `verified`。 |
| `KU-0008` | `REVISE` | L2 本身的收窄已通过，但依赖未通过的 L1；完成指定 L1 修复后，可按本报告机械迁移至 `/verified`。 |
| `MTP-2022-DJCO/source.md` | `VERIFIED` | 无需修改；活动录影 A、当前文字摘录 B。 |
| `CU-2022-DJCO-0001` | `VERIFIED` | 可机械将 `verification_status` 改为 `verified`，保持 B 与 `ai_draft`。 |
| `CU-2022-DJCO-0001 → KU-0007` | `VERIFIED`（有限并入） | 仅允许按本报告的准确最小改法并入；不得改写 KU-0007 的原则或建立模型。 |
| `MTP-2000-WESCO/source.md` | `VERIFIED` | Part 1 / Part 2 分工与 C 级转述警示已正确。 |
| `CU-2000-WESCO-0001` | `VERIFIED` | 仅作为 standalone C 级 Corpus；可机械设为 `verified`。 |
| `CU-2000-WESCO-0001 → KU-0001/M01` | `REJECT` | 禁止关联 KU-0001、M01 或任何新 KU/模型。 |
| manifest 三行 | `VERIFIED`（登记字段） | 当前分类、等级、URL 和行动说明均通过；`ingest_status` 的精确后续动作见末节。 |

## 一、2007 USC

### `MTP-2007-USC/source.md`

**裁决：`VERIFIED`。**

- USC Gould 官方页确认 2007 年 5 月 13 日毕业典礼和 Munger 主旨演讲者身份。
- 公开 PDF 首页明确写有 `Notes by Joe Koster`；它是具名第三方笔记，不是 USC 官方逐字稿。
- L0 已正确写成 `A-official-event-identity / C-named-third-party-notes`，并明确选段尚未与存留录像逐句对齐。
- `link_and_excerpt` 与不提交完整笔记或录像的做法符合版权边界。

不得因为存留录像存在，就在未完成时间戳对齐时把文字从 C 自动升级为 B。

### `CU-2007-USC-0001`

**裁决：`REVISE`。**

已通过的部分：

- `source_level: "C"`、Joe Koster 署名、PDF 页码、提取行号与“录像时间戳未对齐”均正确。
- 第一条英文可在 Joe Koster PDF 第 1 页复现。
- 当前毕业典礼语境、`translation_status: "ai_draft"` 和短摘录策略正确。

剩余阻断问题：

- 第二条英文只留下 `hooked for lifetime learning`，第三条只留下 `what you learn after you leave here`；两者虽是原文子串，却不是 Critic 要求恢复的完整句子。
- 对应中文仍分别加入“从此必须”和“人生的进步来自”等被英文引文省略的语义。L1 因此形成“英文短语 / 中文完整命题”不对称，读者无法只依靠当前英文锚点复核中文。

允许且仅允许以下机械修复：

1. 第一条英文与中文保持不变。
2. 第二、第三条英文分别恢复为 `phase-1c-batch4-critic-review.md` 的“2007 最小机械修订清单”第 3 项所列 Joe Koster PDF 完整句子；不得拼接其他 transcript 或录像版本。
3. 第二条中文改为：`这意味着你必须坚持终身学习。`
4. 第三条中文改为：`你将凭离开这里以后学到的东西，在人生中取得进步。`
5. 保持当前语境说明、locator、`source_level: "C"`、`translation_status: "ai_draft"` 和录像未对齐限制。

完成以上逐字机械修复后，无需新增结构或另建条目，授权：

- `verification_status: "candidate"` → `verification_status: "verified"`。

任何不同于上述两句来源版本的英文替换、语义扩写或来源升级都不在授权内。

### `KU-0008-lifelong-learning.md`

**裁决：`REVISE`，原因仅为当前 L1 依赖尚未通过。**

L2 本身的 Critic 修订已经通过：

- 标题由道德责任与终身学习连续论述支撑。
- 原理已收窄为 Critic 指定的 AI 推断，不再加入“环境变化使知识失效”的未明说机制。
- `source.tier: "C"` 与出处分层一致。
- `models: []` 正确；本条与 M01、KU-0007 均不重复，也不授权建立“终身学习”模型。
- 反例诚实留空，边界明确不把学习数量等同判断质量，也不把回顾性成功归因变成外部因果证明。
- 当前短摘录总量对一份五页笔记而言仍属必要、克制的 `link_and_excerpt`；修复完整句子后也不得扩展为段落转载。

完成上一节对 `CU-2007-USC-0001` 的精确修复并先把 L1 设为 `verified` 后，授权对当前 KU-0008 做以下机械迁移：

1. 从 `/candidates` 移入 `/verified`。
2. `status: "candidate"` → `status: "verified"`。
3. 四项 `review.*_checked` 全部设为 `true`。
4. `review.reviewers` 加入 `codex-independent-final-verifier:/root/usc_1994_final_verifier (phase-1c-batch4)`，`review.reviewed_at` 设为 `2026-08-31`，保留 `rejection_reason: null`。

迁移时必须保持正文、`source.tier: "C"`、`models: []`、反例待研究和全部边界不变。该授权不批准核心模型，也不证明终身学习与长期成功的因果关系。

## 二、2022 Daily Journal

### `MTP-2022-DJCO/source.md`

**裁决：`VERIFIED`。**

- 日期、会议身份、Yahoo Finance 录影与 Richard Lewis 具名文本可追溯。
- 文本首页明确披露主持人问题经常被概括，而 Munger 与 Gerry Salzman 的发言按记录者能力尽量准确转录。
- L0 的 `A-primary-recording / B-text-excerpt` 分层正确；未对齐的文字不会因录影存在而自动成为 A。

### `CU-2022-DJCO-0001`

**裁决：`VERIFIED`。**

- 完整英文可在公开 transcript PDF 文件 pp. 27–28、解析 lines 824–834 复现，已经补回本人或顾问能力两部分。
- 中文与英文对称；“纳入选择”准确限定在投资方式判断，而非扩写成所有决策的普遍规则。
- 语境明确说明问题由 transcript 概括、不是逐字提问，并保留 Munger 回答“没有一刀切”的范围。
- locator、`source_level: "B"`、录影时间戳未对齐限制与 `translation_status: "ai_draft"` 均正确。
- 只保存一个必要短句，没有重新发布完整 transcript。

授权机械执行：

- `verification_status: "candidate"` → `verification_status: "verified"`。

不得同时把 `source_level` 升为 A、把问题改写成逐字提问、把翻译标为人工审核，或宣称某种投资风格普遍更好。

### `CU-2022-DJCO-0001 → KU-0007`

**裁决：`VERIFIED`，只允许有限并入。**

这条证据给 KU-0007 增加的是窄域应用：在选择投资方式时，本人或顾问的能力水平应进入判断。它不新增原则，不证明能力自评准确，也不证明顾问能力或任何投资风格的绩效。

先将 L1 设为 `verified`，随后允许对 `verified/KU-0007-competence-boundary.md` 做且只做以下最小修改：

1. `corpus_ids` 从 `["CU-2020-CALTECH-0001"]` 改为 `["CU-2020-CALTECH-0001", "CU-2022-DJCO-0001"]`。
2. “原话”首句改为：`见 Corpus：CU-2020-CALTECH-0001、CU-2022-DJCO-0001。`，其中两个 ID 继续使用现有 Markdown 代码格式。
3. 紧随该句增加且仅增加：`2022 年 B 级文本在投资选择语境中补充：本人或顾问的能力水平应进入判断；它不把任何具体投资风格判为普遍最优。`
4. “出处”保留现有 2020 来源，并增加 2022 Richard Lewis transcript 链接、文件 pp. 27–28、证据等级 B、问题经概括且录影时间戳未对齐的限制。
5. `review.reviewers` 追加本 Verifier 标识；四项 review check 保持 `true`，`reviewed_at` 保持 `2026-08-31`。

不得修改 KU-0007 的标题、原理、反例、边界、`models: []` 或主来源 front matter；不得新建 KU、能力圈模型或投资风格模型。按上述精确限定并入后，KU-0007 可继续保持 `verified`。

## 三、2000 Wesco

### `MTP-2000-WESCO/source.md`

**裁决：`VERIFIED`。**

- Part 1 可复现 Whitney Tilson 的亲临会议、笔记蒸馏和部分内容属于 paraphrase 的说明。
- L0 已新增 Selected excerpt page，并正确指向 Part 2 的 `Mental Models for Investing`。
- `C-named-third-party-notes` 正确；文章发布日期与未知的精确会议日期没有混用。
- 无原始录音或官方 transcript，不能升级到 B，更不能称作已验证的 Munger 逐字稿。

### `CU-2000-WESCO-0001`

**裁决：`VERIFIED`，仅作为 standalone C 级 Corpus。**

- 两个英文片段均可在 Motley Fool Part 2 的 `Mental Models for Investing` 直接复现。
- `source_url`、section locator 和 Drive 提取行号现已互相一致。
- `speaker` 与正文均保留“Whitney Tilson 报告、可能转述”的警示；中文没有增加因果结论。
- `source_level: "C"`、事件年份 `2000`、`translation_status: "ai_draft"` 均正确。
- 两个必要短片段符合 `link_and_excerpt`，没有复制完整笔记。

授权机械执行：

- `verification_status: "candidate"` → `verification_status: "verified"`。

必须永久保持 C、可能转述、精确会议日期未知和没有原始录音/官方 transcript 的限制。

### `CU-2000-WESCO-0001 → KU-0001/M01`

**裁决：`REJECT`。**

禁止：

- 把 `CU-2000-WESCO-0001` 加入 `KU-0001.corpus_ids`、原话、边界或出处；
- 写入 `models: ["M01"]`；
- 作为 M01 evidence anchor；
- 据此创建任何 KU、一级模型或下级模型。

原因不变：该 C 级转述只重复 1994 B 级证据已经更直接表达的多模型与单一模型警告，也没有提供 2016 B 级证据那样的新增边界。它的价值是 standalone 来源历史与检索，不是削弱更强证据链的并列锚点。

## 四、Manifest 状态

三行当前 `source_class / evidence_level / canonical_url / public_policy / next_action` 均通过结构与语义核验：

- `MTP-2007-USC`：`official_context_plus_named_notes / C-named-notes` 正确；官方页作为活动身份入口，L0/L1 另给 Joe Koster 笔记直链。
- `MTP-2022-DJCO`：`official_recording_plus_transcript / A-primary` 正确描述组合来源；该 A 只属于录影和来源组合，不传递给 B 级 L1 文字。
- `MTP-2000-WESCO`：`named_third_party_notes / C-named-notes`、Part 2 canonical URL 与选段提示均正确。

当前三行的 `ingest_status: ready_candidate` 与尚未执行状态迁移的工作树一致。授权按以下顺序机械更新：

1. `MTP-2022-DJCO`：在 CU-2022 设为 `verified` 后，把 `ingest_status` 改为 `verified_sample`；`next_action` 改为明确“一条 B 级文字摘录已验证，仍待与官方录影对齐，并保留问题经概括警示”的同义短句。
2. `MTP-2000-WESCO`：在 CU-2000 设为 standalone `verified` 后，把 `ingest_status` 改为 `verified_sample`；`next_action` 改为明确“一条 standalone C 级转述已验证，仍需寻找精确会议日期或原始录音，且不得关联 M01”的同义短句。
3. `MTP-2007-USC`：当前不得先改 `verified_sample`。只有完成本报告指定的 CU-2007 英文/中文修复、把 L1 设为 `verified`，并按条件迁移 KU-0008 后，才可把 `ingest_status` 改为 `verified_sample`；`next_action` 必须继续说明一条 C 级具名笔记摘录已验证、仍需与存留录像对齐后才能评估升级。

Manifest 的 `verified_sample` 只表示该来源已有一个通过审查的摘录样本，不升级来源等级，也不表示整个来源已完整处理。

## 五、结构与机械边界

当前工作树的检查结果：

- `scripts/validate_sources.py`：46 条来源全部通过。
- `scripts/validate_corpus.py`：24 个知识/Corpus/案例单元全部通过。
- 单元测试：11 项全部通过。

执行上述获授权的精确机械变更后，生产者必须重新运行三组检查。若出现任何结构错误，或实际修改超出本报告列出的字符串、状态、review 身份和既有 KU 证据并入范围，则本授权失效并回到 `NEEDS_REVIEW`。

本报告不授权修改 M01，不授权新建任何模型、KU、案例、字段、目录或 Agent，也不授权把任何 `ai_draft` 翻译改为 `human_checked`。
