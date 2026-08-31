# PHASE 1C Batch 3｜独立 Critic Review

- Reviewer: `codex-independent-critic:/root/rd_0001_critic`
- Reviewed at: `2026-08-31`
- Scope: `MTP-2016-DJCO`、`MTP-2019-WSJ`、`MTP-1999-WESCO` 的 L0/L1，以及三条拟议关联。
- Constraint: 不修改 L0/L1/Verified/Model；不新增 KU 或模型。

## 总裁决

| 对象 | 裁决 | 核心原因 |
|---|---|---|
| `MTP-2016-DJCO/source.md` | `ACCEPT` | 2016-02-11、Tilson 录制转录、Koltes 编辑归属均可由具名 PDF 首页核对，B 级正确。 |
| `CU-2016-DJCO-0001` | `REVISE` | 页码错误；短句不是所列 Tilson PDF 的逐字文本；并省略了专精与综合之间的重要边界。 |
| `2016 → KU-0001/M01` | `REVISE` | 方向相关且有增量，但须先修复逐字性和边界；不能只挑一句把 Munger 写成无条件反对专精。 |
| `MTP-2019-WSJ/source.md` | `REVISE` | 应明确区分 4 月 23 日主访谈、日期不明的后续电话、5 月 3 日 WSJ 发布和 5 月 5 日作者页转载。 |
| `CU-2019-WSJ-0001` | `REVISE` | 两句不是“同一连续回答”；公开定位不足；第二句中文漏掉“他们从未想到”的认识缺口。 |
| `2019 → KU-0002` | `ACCEPT` | 直接补强激励强度可能诱发行为偏移，但只能证明 Munger 的持续观点，不能单独验证 Wells Fargo 因果。 |
| `MTP-1999-WESCO/source.md` | `REVISE` | `simpleinvestor` 只是未识别真实身份的用户名，原 Motley Fool 帖未恢复；必须把保存链限制写得更明确并保持 C。 |
| `CU-1999-WESCO-0001` | `ACCEPT` | 已明确标为笔记者转述、非 Munger 逐字原话，页码可复现且 C 级正确。 |
| `1999 → KU-0001/M01` | `REJECT` | 只重复“latticework / models”，没有新增机制或边界；来源又弱于 1994 与 2016，合并只会稀释证据链。 |

## 一、2016 Daily Journal

### L0：MTP-2016-DJCO

**裁决：`ACCEPT`**

- Tilson PDF 首页明确写明：会议于 `2016-02-11` 在 Daily Journal 洛杉矶总部举行。
- 首页明确写明 `Recording and transcript by Whitney Tilson`，并列出 `Edited for clarity by Jesse Koltes`。当前 L0 对录制、转录与编辑的归属准确。
- “edited for clarity”意味着它不是未经编辑的官方逐字稿；没有保存并对齐原始录音，因此 `B-named-transcript` 正确，不得升级为 A。
- L0 没有把 Jesse Koltes 写成共同采访者或原始记录者，也没有隐去编辑行为。

### L1：CU-2016-DJCO-0001

**裁决：`REVISE`**

#### 阻断问题

1. **页码不正确。** 所列 Tilson PDF 中，这段问答位于文件第 8 页、印刷页码 `-8-`（网页解析为零基 `P7`），不是 `pp. 10-11 / PDF pages 9-10`。私有提取行号也必须重新核对，不能用错误页码掩盖。
2. **不是所列来源的逐字文本。** 当前写：`Synthesis is reality because we live in a world with multiple factors and models.` Tilson PDF 实际为：`Synthesis is reality, because we live in a world of multiple models, and of course we’ve got to have synthesis to understand the situation.` “multiple factors and models”来自其他转录版本或编辑，不应在链接指向 Tilson 时冒充其逐字内容。
3. **上下文被截得过度有利。** Munger 随后明确说，多数人的职业道路应当高度专精；跨学科综合“对一些人很有帮助”，却“不是多数人的正确职业建议”。他又说综合是一种防御性的第二重手段，避免人在生活其他领域被突袭。只保留第一句，会把有限主张误读成无条件的跨学科职业处方。

#### 中文

当前“由多种因素和模型共同作用的世界”与 Tilson 原文不一致；原文只明确说 `world of multiple models`。修订后的翻译不应额外加入“共同作用”这一因果描述。

#### 最小必要修改

1. 把 locator 改为 Tilson PDF 文件第 8 页 / 印刷 `-8-`，并重新确认 Drive 私有行号。
2. 使用一个来源版本的准确文字，不拼接不同 transcript。若以 Tilson 为锚，应采用 Tilson 版本。
3. 增加最短边界片段，至少保留“综合对一些人有帮助，但不是多数人的正确职业建议”或“综合是防御性的第二重手段”之一。
4. 中文随英文逐字锚点重新翻译，保持 `ai_draft`。

### 与 KU-0001 / M01 的关系

**裁决：`REVISE`，修复后可接受。**

- 2016 证据确实是跨时期补强：它再次明确谈到多个模型、跨学科综合，并补充了 M01 现有边界——广度不能替代专业能力。
- 它的真正增量不是再次出现“多个模型”四个字，而是把**专精作为主要职业能力、综合作为防御性第二层能力**并置。
- 若修订后加入 `KU-0001.corpus_ids`，正文必须说明这一有限增量；不得改写 M01，不得另建“综合思维”模型。
- `KU-0001` 已 Verified，增加证据后须对完整新版本重新独立验证，不能沿用旧批准直接合并。

## 二、2019 Wall Street Journal

### L0：MTP-2019-WSJ

**裁决：`REVISE`**

#### 可确认事实

- Jason Zweig 的作者页和 WSJ 编辑文本均说明：主访谈是在 Munger 洛杉矶家中于 `2019-04-23` 进行，时长约六小时。
- 文章还包含一次后续电话讨论，但当前证据没有给出该电话的确切日期。
- WSJ 正文标注发布日期为 `2019-05-03 9:59 p.m. ET`。
- Jason Zweig 的作者维护页标注 `2019-05-05`，这是其页面发布或转载日期，不是访谈日期，也不是 WSJ 首发日期。

#### 必须修改

1. 在 Identity 中新增 `WSJ publication date: 2019-05-03`。
2. 明确 `Author-maintained page date: 2019-05-05`，不得把它写成采访日期。
3. 对 follow-up telephone discussion 标 `date not stated`，禁止推定也发生在 4 月 23 日。
4. 保留 `B-publisher-edited-transcript`。这是由 WSJ 发布者编辑、插入说明并整理过的问答文本，可以归属 Munger 的已编辑回答，但不是未经剪辑的录音逐字稿。
5. 建议补入公开对照 PDF及页码定位；当前仅给 WSJ 付费文章和私有 Drive 行号，不利于开源审阅者复现。

### L1：CU-2019-WSJ-0001

**裁决：`REVISE`**

#### 引文与语境

- 两句英文都能在 WSJ 编辑文本中找到，归属真实。
- 第一段出现在“经纪人与银行家应如何获得报酬”的回答中，Munger 先谈佣金制销售员，继而用 Wells Fargo 作类比。
- 第二段出现在随后关于 Wells Fargo CEO 的另一个问答中。两句属于同一连续讨论，但不是“同一连续回答”。现有说明不准确。
- WSJ 文本中的 Wells Fargo 方括号说明和编辑注是发布者插入内容；不能把这些编辑补充误认为 Munger 逐字说过。

#### 中文

- `You get the incentives too tough and too many people will yield.` 译为“激励压力过强，就会有太多人屈从”基本准确；这里的 `yield` 是屈从于压力并作出不当行为，不是“提高产量”。
- `their own incentive system could be a mistake` 所在原句是：管理层“从未想到自己的激励制度本身也可能有错”。现译“问题可能出在他们自己的激励制度上”遗漏了认知盲点，并把 `a mistake` 改成更笼统的“问题出在”。建议译为：`他们从未想到，自己的激励制度本身也可能是个错误。`

#### 最小必要修改

1. 把“同一连续回答”改为“同一连续讨论中的两个回答片段”。
2. locator 区分 `main conversation date: 2019-04-23` 与 `WSJ publication: 2019-05-03`；增加公开对照 PDF 文件第 2–3 页定位，或提供可复现的同等定位。
3. 修正第二句中文，并继续标 `B / ai_draft`。
4. 在 L1 说明这是 WSJ publisher-edited transcript 中的 Munger 回答，不能暗示存在未经编辑录音。

### 与 KU-0002 的关系

**裁决：`ACCEPT`，但只能作为补强。**

- 2019 证据直接重复并具体化 KU-0002 的核心：激励强度容易被管理层低估，并可能使普通人在压力下改变行为。
- 它的增量是“佣金 / 额度压力 + 仅加强合规而不改激励”的组织情境，不应被提炼为新 KU 或新模型。
- Wells Fargo 事实、违规原因及 CEO 责任并未在本条独立查证；因此只能说“这是 Munger 在已编辑访谈中的解释”，不能把它升级为已验证失败案例或排他因果。
- 完成 L0/L1 修订并通过 Verifier 后，可把该 CU 加入 `KU-0002.corpus_ids`，同时保留现有因果边界与 `models: []`；合并后的 Verified 条目须重新验证。

## 三、1999 Wesco

### L0：MTP-1999-WESCO

**裁决：`REVISE`**

#### 证据身份

- 现存 PDF 自称转存自 Motley Fool，并把作者标为用户名 `simpleinvestor`。正文以第一人称描述亲临 Pasadena、做笔记和参观 See’s 工厂，形式上符合现场第三方笔记。
- 但 `simpleinvestor` 是未识别真实姓名与身份的账号名，不能称为“充分具名的记录者”。
- 原始 Motley Fool 帖本轮未恢复，无法验证原始发布时间、URL、账号主页、后续编辑或现存 PDF 是否完整无改动。当前 Worldly Partners PDF 是后来的保存副本，不是原站证据。

#### 等级

- 必须保持 `C`，绝不能升为 B。它没有录音、逐字稿或完整身份链。
- 在现有材料下，C 是**带明显来源限制的最高可接受等级**：理由是文本自称现场笔记、保留稳定用户名和具体会议观察。若未来发现保存副本与原帖不一致，应降为 `NEEDS_REVIEW` 或仅作线索。
- L0 应把 `named notes` 改写为更准确的 `pseudonym-attributed third-party notes`，并明确真实身份未知、原帖未恢复、保存链未独立验证。

### L1：CU-1999-WESCO-0001

**裁决：`ACCEPT`**

- locator 准确：现存 PDF 文件第 4 页 / 印刷页 `-135-`，相关内容位于 `INVESTMENT SUCCESS` 与 `HOW TO MAKE YOUR LIFE BETTER`。
- `speaker` 已写成 `Charlie Munger (reported by simpleinvestor; not verbatim)`，并在正文再次说明是笔记者转述。这是必须保留的防误用标签。
- 两段英文是笔记作者的文字，不是 Munger 逐字原话；目前没有用第一人称或引号宣称 Munger 原封不动说过，处理正确。
- 中文明确加“笔记者转述”，译义没有明显扩大。
- `source_level: C` 必须永久保留，除非未来找到更强独立来源；恢复原 Motley Fool 帖本身也不会自动把第三方摘要升级为 B。

**非阻断增强：** 可把 `## 原文` 改成更明确的 `## 笔记原文（非 Munger 逐字）`，但现有双重警示已经足以避免当前版本被合理地误读为逐字引文。

### 与 KU-0001 / M01 的关系

**裁决：`REJECT`。**

- 它只重复 `latticework of models` 和 `master life's models`，没有增加多学科、现实扭曲、模型选择、适用边界或新的可检验判断。
- `KU-0001` 已由 1994 B 级连续论述直接支撑；2016 B 级材料在修订后还能提供真正的专精 / 综合边界。1999 C 级转述既弱又无增量。
- 将它加入 `KU-0001.corpus_ids` 会让低质量来源看起来与核心证据并列，降低而不是提高可信度。
- 可以保留这条 C 级 Corpus candidate 作为来源历史与检索线索，但不得合并进 Verified `KU-0001`，不得成为 M01 evidence anchor，也不得据此新建任何模型。

## 最终结论

1. 2016 的来源身份通过，但 L1 必须修正页码、逐字文本和专精边界后，才能补强 M01。
2. 2019 必须拆开采访、电话补访、WSJ 发布和作者页日期；修订后可作为 KU-0002 的具体补强，但不是 Wells Fargo 因果验证。
3. 1999 必须永久保持 C，并明确用户名与转存链限制；L1 可留在 Corpus，但与 KU-0001/M01 的拟议关联应拒绝。
4. 本批不新增 KU、不新增模型，也不改变 M01 定义。
