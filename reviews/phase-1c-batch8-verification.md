# PHASE 1C Batch 8｜最终独立 Verification

- Reviewer: `codex-independent-final-verifier:/root/usc_1994_final_verifier (phase-1c-batch8)`
- Reviewed at: `2026-09-01`
- Scope: 修订后的 `MTP/CU-2004-WESCO` 至 `MTP/CU-2009-WESCO`、`reviews/phase-1c-batch8-critic-review.md` 与 source manifest 对应六行。
- Constraint: 本报告只作独立裁决和机械授权；未修改任何生产文件或状态；未新增系统、字段、KU、模型或 Agent。

## 总裁决

| 年份 | L0 | L1 | 上层关系 | 允许动作 |
|---|---|---|---|---|
| 2004 | `VERIFIED` | `VERIFIED` | `REJECT` | L1 可改 `verified`，仅 standalone；不得并入 KU-0005。 |
| 2005 | `VERIFIED` | `VERIFIED` | `REJECT` | L1 可改 `verified`，仅 standalone；不得新增或映射信任 KU。 |
| 2006 | `VERIFIED` | `VERIFIED` | `REJECT` | L1 可改 `verified`，仅 standalone；不得映射任何现有 KU。 |
| 2007 | `VERIFIED` | `VERIFIED` | `REJECT` | L1 可改 `verified`，仅 standalone；不得关联 KU-0001/M01。 |
| 2008 | `VERIFIED` | `VERIFIED` | `REJECT` | L1 可改 `verified`，仅 standalone；不得新建从众模型。 |
| 2009 | `VERIFIED` | `VERIFIED` | `REJECT` | L1 可改 `verified`，仅 standalone；不得映射领导力、信任或能力圈 KU。 |

六组 L0/L1 均以 `C` 为不可突破的证据上限。`VERIFIED` 表示在完整保留具名或归属链、非逐字警示、locator 和语境边界的条件下，可以作为 L1 Corpus 证据使用；不表示其为逐字 transcript，不验证会议中提到的具体案例或结果，也不自动产生 L2 关系。

本批没有 `NEEDS_REVIEW` L1，也没有获准的上层关系。

## 冻结版本与结构检查

### SHA-256

| 文件 | SHA-256 |
|---|---|
| `raw/wesco/MTP-2004-WESCO/source.md` | `8b636115fc7cf7baeac554b47f11cda083af5998c71c58eeef071bf927fed5d5` |
| `corpus/MTP-2004-WESCO/chunks/CU-2004-WESCO-0001.md` | `1a41bfc32ba909fb9e2074029d3d13714bb08ec28aaa6a8d6128aa561bd3b808` |
| `raw/wesco/MTP-2005-WESCO/source.md` | `4fe2ba4bef18e389ef8c8226ad3ccfbc057995dc8076d558f41debb5715e62cd` |
| `corpus/MTP-2005-WESCO/chunks/CU-2005-WESCO-0001.md` | `8626bf975ae383620b2b56cdba42d9eb9dabb4ff61a6d66bab8909a78d52762a` |
| `raw/wesco/MTP-2006-WESCO/source.md` | `094ed70147a43c6788bc343bb04604ddfc8caef5044001dd8e272c3718478a9a` |
| `corpus/MTP-2006-WESCO/chunks/CU-2006-WESCO-0001.md` | `924e33332ce275e4cae5f60c4a9a2f82dff9925d893896d11d16043067c005b2` |
| `raw/wesco/MTP-2007-WESCO/source.md` | `d9f4d37e40bf998aa2e21eb7a864e2fc11355adfd0893a227dbd681b0ccea635` |
| `corpus/MTP-2007-WESCO/chunks/CU-2007-WESCO-0001.md` | `b45ae28cd3a23682619e2c636e990d8201eefee7f6a8e1d979715ac379ea98ab` |
| `raw/wesco/MTP-2008-WESCO/source.md` | `1f41333ebe0ee1bbed1deccb79261ebf776cb1def611b8353c21ee7f17bce3d1` |
| `corpus/MTP-2008-WESCO/chunks/CU-2008-WESCO-0001.md` | `58caed1c29ab8fb4804c6a4c85f03912e36124572fc69caa08f576a590dc4cf4` |
| `raw/wesco/MTP-2009-WESCO/source.md` | `4faef923eaf38ad8ebe9ef0e09a5935026bb113b7a7bb50f0e9c2c8b86059c9f` |
| `corpus/MTP-2009-WESCO/chunks/CU-2009-WESCO-0001.md` | `e10957f1936d864fa05ce485dbb40f57336e9bee3031eb0c8a896ffe8c0c2193` |
| `reviews/phase-1c-batch8-critic-review.md` | `019ed8a69d473be443c6776b2e22e6ea38a3085af2f9bffbb1e26592c5524366` |
| `sources/source-manifest.csv` | `56040bf5c8a9f6f64341730658e1684238f87bf7bb1f010c2ae9dff4256dcb0f` |

任一被审 L0/L1 在执行机械动作前若发生实质变更，本授权失效。

### 自动校验

- `validate_sources.py`: 通过；46 sources，`A=8 / B=9 / C=14 / D=15`。
- `validate_corpus.py`: 通过；44 knowledge units，无错误。
- `python -m unittest discover -s tests -v`: 11 项测试全部通过。

自动校验只证明结构合规；来源、翻译、上下文与关系由以下独立裁决负责。

## 2004 Wesco

### L0：`MTP-2004-WESCO/source.md`

**裁决：`VERIFIED`。**

公开保存件给出 `2004-05-05` 和 Whitney Tilson；其首页明确说明不是 transcript、禁止录音，并由快速打字、记忆、编辑和事后按主题重组形成。L0 对 23 个文件页、提取规模与 `C-named-third-party-notes` 的记录一致。引号形式不能把该来源升级为 B。

### L1：`CU-2004-WESCO-0001`

**裁决：`VERIFIED`。**

- locator 指向保存 PDF 第 14 页及 Drive 484–492 行，可覆盖 `Proper Thinking` 语境和短引文。
- 引文旁已标明 C 级非逐字笔记；中文忠实保留“推翻钟爱观念”的规范性表达，没有把“一年”改造成有实证依据的更新频率。
- 17 个英文词属于必要短摘录，符合 `link_and_excerpt`。

**机械授权：**仅将 L1 frontmatter 的 `verification_status` 从 `candidate` 改为 `verified`；文件留在原 L1 路径。

### 上层关系

**裁决：`REJECT`。**

该句没有要求主动寻找、准确呈现或衡量反证，也没有提供新边界。不得加入 `KU-0005.corpus_ids`、原话或出处，不得改变 KU-0005，不得新建 KU/模型。

## 2005 Wesco

### L0：`MTP-2005-WESCO/source.md`

**裁决：`VERIFIED`。**

公开保存件给出 `2005-05-04`、Whitney Tilson，并明确非 transcript、禁止录音、快速记录加记忆且按主题重排。30 页文件和 C 级来源描述一致。

### L1：`CU-2005-WESCO-0001`

**裁决：`VERIFIED`。**

- locator 指向保存 PDF 第 9 页及 Drive 293–305 行；语境限定为 Berkshire 管理方式。
- 短句中的 `deserved trust` 被保留为“应得信任”，没有改成无条件信任；“效率”仍是笔记中的主张，不冒充独立比较结果。
- 仅摘录 13 个英文词，版权处理合格。

**机械授权：**仅将 L1 `verification_status` 改为 `verified`。

### 上层关系

**裁决：`REJECT`。**

该句没有给出筛选、建立或监督信任的机制，也没有失效边界。只可 standalone；不得新建或映射信任、领导力 KU/模型。

## 2006 Wesco

### L0：`MTP-2006-WESCO/source.md`

**裁决：`VERIFIED`。**

标题给出 Whitney Tilson 与 `2006-05-11`；来源披露方括号可能来自笔记者的评论、编辑或漏记时的最佳猜测，没有声称录音核验。C 是正确上限。

### L1：`CU-2006-WESCO-0001`

**裁决：`VERIFIED`。**

- locator 指向保存 PDF 第 20 页及 Drive 688–702 行，覆盖 K-Mart、Freddie Mac/Fannie Mae 和 omission mistakes 的完整语境。
- 修订已明确：这是对错失投资机会的回顾性反事实自评，本单元不验证当时能否行动或若行动后的收益。
- 中文“因没有行动而造成的错误”对应 omission mistakes；上述边界阻止它被误用为已验证损失或一般拖延结论。
- 引文只有 9 个英文词，版权无问题。

**机械授权：**仅将 L1 `verification_status` 改为 `verified`。

### 上层关系

**裁决：`REJECT`。**

未行动错误不等于 KU-0005 的主动反证，也不等于 KU-0003 的成交压力、KU-0004 的二阶后果或 KU-0007 的能力边界。只可 standalone；不新增 omission KU/模型。

## 2007 Wesco

### L0：`MTP-2007-WESCO/source.md`

**裁决：`VERIFIED`。**

标题给出 Whitney Tilson 与 `2007-05-09`；来源把方括号限定为笔记者评论、编辑或最佳猜测，未声称官方 transcript。22 页文件和 C 级描述一致。

### L1：`CU-2007-WESCO-0001`

**裁决：`VERIFIED`。**

- locator 指向保存 PDF 第 16 页及 Drive 528–532 行。
- 修订已明确 `Using mental checklists` 是 Tilson 的小节标题，而非已证明的 Munger 逐字术语。
- 中文已把 `something important` 改为中性的“重要之处”，不再擅自收窄成“因素”；英文与翻译均保留可能及不太可能答案的范围。
- 19 个英文词属于必要短摘录。

**机械授权：**仅将 L1 `verification_status` 改为 `verified`。

### 上层关系

**裁决：`REJECT`。**

候选答案清单不等于多学科模型格栅。不得加入 `KU-0001.corpus_ids`、原话或出处，不得标 `M01`，不得新建 checklist KU/模型。

## 2008 Wesco

### L0：`MTP-2008-WESCO/source.md`

**裁决：`VERIFIED`。**

公开件同时区分 Shai Dardashti 的发布/byline 与 Peter Boodell 的记录身份；Boodell 明确写明未使用录音、文本只是 recollections、不是 quotes 或 literal transcript。`C-named-third-party-recollections` 正确。

### L1：`CU-2008-WESCO-0001`

**裁决：`VERIFIED`。**

- locator 指向保存 PDF 第 2 页及 Drive 55–69 行，覆盖银行、坏会计、竞争模仿及顺从压力语境。
- 英文短句与来源一致；中文中的“同行做法”由紧邻语境支持。
- 已明确这不是对抵押贷款危机的独立因果验证，没有把 C 级回忆升级成案例调查。
- 仅 9 个英文词，版权处理合格。

**机械授权：**仅将 L1 `verification_status` 改为 `verified`。

### 上层关系

**裁决：`REJECT`。**

同行模仿和顺从压力不能无损等同于 KU-0002 的报酬/惩罚/衡量方式，也不是 KU-0003 的成交压力、KU-0007 的能力边界或 M01。只可 standalone；不得新建从众模型。

## 2009 Wesco

### L0：`MTP-2009-WESCO/source.md`

**裁决：`VERIFIED`。**

- 日期 `2009-05-06` 和 11 页文件可复现。
- 修订已把正文可见身份限定为 `PB`，并明确 Peter Boodell 全名来自保存文件名、没有印在 PDF 正文。
- `C-attributed-third-party-recollections; full-name attribution depends on the preservation chain` 准确保存了归属强度。来源称其为 recollections、不是 quotes，不得升 B。

L0 中“Boodell explicitly calls the text recollections”只能结合前述保存链理解为“以 PB 签署者作此声明”，不能据此声称 PDF 正文拼出了 Peter Boodell 全名。

### L1：`CU-2009-WESCO-0001`

**裁决：`VERIFIED`。**

- locator 指向保存 PDF 第 7 页及 Drive 254–264 行，覆盖领导者培养问题、信任、判断力和随后能力范围语境。
- 引文前已醒目标明 PB 签署、全名依赖保存文件名且不是逐字引述；speaker 字段必须继续受这段限制。
- 中文以“无论才华如何”完整保留 `regardless of talent`，没有再弱化为先后顺序。
- 18 个英文词属于必要短摘录。

**机械授权：**仅将 L1 `verification_status` 改为 `verified`。不得删除或弱化 PB/全名归属链警示。

### 上层关系

**裁决：`REJECT`。**

人员选择偏好没有提供信任核验方法、误判风险或适用边界；同段出现能力范围也不使本摘录成为 KU-0007 证据。只可 standalone；不得映射或新建领导力、信任、人才选择、能力圈 KU/模型。

## Manifest 精确修改授权

先把对应 L1 status 改为 `verified`，再执行下表。`verified_sample` 只表示该来源已有一个通过审查的短摘录，不表示全文、会议事实或来源逐字准确性已经验证。

| source_id | `ingest_status` | `next_action` 精确替换文本 |
|---|---|---|
| `MTP-2004-WESCO` | `ready_candidate` → `verified_sample` | `One standalone C-grade named-notes excerpt verified; preserve Whitney Tilson attribution, the non-transcript warning and later topical reorganization; locate corroborating notes or a recording; do not link it to KU-0005` |
| `MTP-2005-WESCO` | `ready_candidate` → `verified_sample` | `One standalone C-grade named-notes excerpt verified; preserve Whitney Tilson attribution and the non-transcript warning; locate corroborating notes or a recording; do not create or map a trust or leadership KU` |
| `MTP-2006-WESCO` | `ready_candidate` → `verified_sample` | `One standalone C-grade named-notes excerpt verified; preserve Whitney Tilson attribution, bracketed-edit and best-guess warnings, and the unverified-counterfactual boundary; do not map it to an existing KU` |
| `MTP-2007-WESCO` | `ready_candidate` → `verified_sample` | `One standalone C-grade named-notes excerpt verified; preserve Whitney Tilson attribution, the non-verbatim warning and the checklist-heading distinction; do not link it to KU-0001 or M01` |
| `MTP-2008-WESCO` | `ready_candidate` → `verified_sample` | `One standalone C-grade third-party recollection verified; preserve Shai Dardashti publisher/byline and Peter Boodell notes attribution; retain the recollections-not-quotes warning and locate corroborating notes; do not create an upper-layer relation` |
| `MTP-2009-WESCO` | `ready_candidate` → `verified_sample` | `One standalone C-grade PB-signed recollection verified; preserve the recollections-not-quotes warning; verify the full-name attribution to Peter Boodell from the original publication or another explicit source; do not create an upper-layer relation` |

除 `ingest_status` 与 `next_action` 外，不授权修改这六行的 `source_class`、`evidence_level`、`canonical_url` 或 `public_policy`。特别是 2009 不得因 L1 通过而把“PB → Peter Boodell”改成正文已直接具名。

## 允许的机械执行顺序

1. 六个 L1 frontmatter 的 `verification_status` 分别从 `candidate` 改为 `verified`；不移动文件。
2. 六个 L1 全部保持 standalone；不编辑任何 KU、Model 或 Case。
3. 按上表更新 manifest 六行。
4. 重新运行 sources validator、corpus validator 和全部测试；只有三者全绿，机械执行才完成。

## 最终门禁

- **L1 可改 verified：**2004、2005、2006、2007、2008、2009 Wesco。
- **必须保持 candidate：**无。
- **上层关系：**六组全部 `REJECT`，确认全部 standalone。
- **来源上限：**六组全部 C；不得把引号版式、笔记者小节标题、事后回忆或保存文件名当成 B 级逐字/直接署名证据。
- **禁止事项：**不得新增或修改 KU、模型、Case、字段、系统或 Agent；不得把未验证的投资反事实、管理效率、危机因果或人员筛选效果写成事实结论。
