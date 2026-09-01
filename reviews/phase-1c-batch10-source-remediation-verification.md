# PHASE 1C Batch 10｜Source Remediation 最终独立 Verification

- Reviewer: `codex-independent-final-verifier:/root/usc_1994_final_verifier (phase-1c-batch10-source-remediation)`
- Reviewed at: `2026-09-01`
- Scope: `MTP-1986-HARVARD`、`MTP-1996-STANFORD`、`MTP-2010-WESCO`、`MTP-2013-DJCO`、`MTP-2014-DJCO`、`MTP-2022-SINGLETON` 的修订 L0、相关 L1/KU、`phase-1c-batch10-source-remediation-critic.md` 与 manifest。
- Constraint: 本报告只作来源修复终审和机械授权；未修改生产文件或状态；未新增 KU、模型、字段或系统。

## 总裁决

| Source ID | L0 当前裁决 | 证据上限 | L1 / 上层结果 | Manifest 状态 |
|---|---|---|---|---|
| `MTP-1986-HARVARD` | `VERIFIED` 为 D 级记录；来源修复仍 `NEEDS_REVIEW` | D | 既有 L1 保持 D/candidate，不得上联 | `needs_source` |
| `MTP-1996-STANFORD` | `VERIFIED` | C，OID publisher-edited excerpts | L1 当前 `REVISE`；修正 exact OID page 后可 standalone verified；上联 `REJECT` | 修正 L1 前 `ready_candidate`；修正后可 `verified_sample` |
| `MTP-2010-WESCO` | `VERIFIED` | C，Ben Claremon/TII named notes | 当前零 L1；不自动生成或上联 | `ready_candidate` |
| `MTP-2013-DJCO` | `VERIFIED` 为 D 级记录；来源修复仍 `NEEDS_REVIEW` | D | 保持零 L1 | `needs_source` |
| `MTP-2014-DJCO` | `VERIFIED` | C，Phil DeMuth/Forbes named notes | 当前零 L1；不自动生成或上联 | `ready_candidate` |
| `MTP-2022-SINGLETON` | `VERIFIED` 为 D 级记录；来源修复仍 `NEEDS_REVIEW` | D | L1 与 KU-0010 均保持 D/candidate | `needs_source` |

本轮确实修复三条来源链：1996 OID 编辑摘录、2010 Ben Claremon 具名手打笔记、2014 Phil DeMuth/Forbes 具名笔记。其余三条仅把证据缺口写得更精确，没有升级。

## Validator 兼容边界

1996 manifest 的以下组合是有意设计，不是来源语义变化：

- `source_class: publisher_edited_excerpts`
- `evidence_level: C-named-notes`

`C-named-notes` 是当前 manifest validator 允许的 C 级枚举；它不得在说明文字、L0、L1 或产品层被解释为现场 note taker 笔记。真实来源类型必须始终表述为：`Outstanding Investor Digest publisher-edited excerpts; incomplete and non-verbatim`。

## 冻结版本与结构校验

### SHA-256

| 文件 | SHA-256 |
|---|---|
| `raw/speeches/MTP-1986-HARVARD/source.md` | `0f1b8f0972a38ccf72e80441358d5ef22888634cda24a7627a949a632fb8a579` |
| `raw/speeches/MTP-1996-STANFORD/source.md` | `643cb247caf90e2bcbfefbe0356b11fb229a0fb1cae216fff1d05b41d44e7259` |
| `corpus/MTP-1996-STANFORD/chunks/CU-1996-STANFORD-0001.md` | `1d384e9cccc48e5936384000339847854f9ea171a47aa6607bf67394901483f9` |
| `raw/wesco/MTP-2010-WESCO/source.md` | `38de4192a5944eed1f0ba392cb8202f93064ff889c432306107ccb27d33861da` |
| `raw/djco/MTP-2013-DJCO/source.md` | `0809fe3e9b359726450663e0b730dcc2cdc52ea26e7033c5631df8d26872db39` |
| `raw/djco/MTP-2014-DJCO/source.md` | `aac3409df1b234ea0f927389ac69e23b28820b1c69e4767632b69c2005e484d4` |
| `raw/interviews/MTP-2022-SINGLETON/source.md` | `eba06e87ed4367073757a6b3d7f22138fffc539bd3b4600551d5e9aeffa070cf` |
| `corpus/MTP-2022-SINGLETON/chunks/CU-2022-SINGLETON-0001.md` | `329adef0b886a1102182d4f6ba55b2a4a90540e9f51547ed2fc3c3fbb189cf65` |
| `candidates/KU-0010-long-attention-on-serious-problems.md` | `d5afbad5c5149816f826452197e768c738e6af5a8cc98390c3e2c0eb13f0ee6e` |
| `sources/source-manifest.csv` | `b691265e23f7af48ce0ac3943f5e02dab3a5ff1defc725dc589baa59b9c6e543` |
| `reviews/phase-1c-batch10-source-remediation-critic.md` | `0158d84a22f4e3903c7fcfd3f9517ab33e369e91d4a6d22b161d41eddf8edd85` |

除本报告明确授权的 1996 L1 locator/status 和随后 manifest status 外，任一被冻结文件发生实质变化都需要重新审查。

### 自动校验

- `validate_sources.py`: 通过；46 sources，`A=8 / B=9 / C=17 / D=12`。
- `validate_corpus.py`: 通过；45 knowledge units，无错误。
- `python -m unittest discover -s tests -v`: 11 项测试全部通过。

结构通过不代表 locator 足够精确。1996 L1 的 OID 页码范围问题正是 validator 未覆盖、由本次语义终审发现的缺口。

## 1986 Harvard School

### L0

**裁决：`VERIFIED` 为 D 级来源记录；修复结果仍 `NEEDS_REVIEW`。**

- 后续书目支持这场讲话的标题、学校和 `1986-06-13`，但没有恢复 Harvard-Westlake 官方档案、节目单、原稿、录音或可逐页核对的授权正文。
- Worldly Partners 保存件仍无 transcriber、publisher、edition 或保存链。
- 因而 `D-unattributed-transcript-lead` 是正确上限。书目存在不能验证当前 transcript wording。

### L1 与关系

`CU-1986-HARVARD-0001` 必须保持 `verification_status: candidate`、`source_level: D`。不得迁移、不得关联任何 KU、模型、Case 或 Decision Engine。

## 1996 Stanford / OID

### L0：`MTP-1996-STANFORD/source.md`

**裁决：`VERIFIED`，证据上限 C。**

- L0 已恢复核心出版身份：`Outstanding Investor Digest`, Vol. XII No. 3, `1997-12-29`, pp. 24–31，并记录 `1998-03-13` 续载。
- 它明确把 32 页 Worldly Partners 文件降为 preservation compilation，并限定只有开头已对齐部分属于 OID Stanford excerpts；后续边界仍混杂。
- 日期诚实写为 `1996`、OID `last year`，`1996-04-19` 未确认。
- evidence 明确为 `C-publisher-edited-excerpts / exact event date unresolved`，并写明既不完整也非逐字。不得升 B。

L0 首句仍使用 `unresolved transcript lead` 的旧措辞，但后续 Identity、Extraction 与 Evidence 已明确覆盖并收窄其含义；后续机械清理可以改成 `publisher-edited excerpt record`，但这不是本批阻断项，也不得借此改等级。

### L1：`CU-1996-STANFORD-0001`

**当前裁决：`REVISE`；修正后可 C 级 standalone verified。**

- 引文确实位于 OID 1997-12-29 原刊 **p. 24**；原刊 p.25 从 Darwin 段落续页开始。
- 当前 locator 写 `original pp. 24-31`，只是整篇 OID excerpt 的范围，没有精确指出选句所在原刊页。Critic 已要求 locator 改为 OID 原刊页，当前修订没有完全落实。
- preservation compilation p.2 和 Drive 47–56 行能辅助定位，但不能替代升级后核心来源的 exact original page。
- 英文短句、中文、C 级 publisher-edited 警示和版权短摘录均合格。

**唯一允许的最小修订：**把 frontmatter `locator` 精确改为：

> `Outstanding Investor Digest Vol. XII No. 3, 1997-12-29, original p. 24; preservation compilation file p. 2; Drive extraction lines 47-56`

完成这一替换且文件其余内容不变后，本报告授权把 `verification_status` 从 `candidate` 改为 `verified`。文件继续留在 L1 Corpus 原路径。

### 上层关系

**裁决：`REJECT`。**

该句与 KU-0001/M01 的更强、完整证据重复，没有新增机制、反例或边界。即使 L1 通过，也不得加入 `KU-0001.corpus_ids`、原话或出处，不得标 M01，不得新增 KU/模型。

## 2010 Wesco

### L0

**裁决：`VERIFIED`，证据上限 C。**

- 当前 Drive 416 行文件与公开 12 页、416 行 preservation PDF 在标题、Part I/II 和 Q&A 结构上构成文档级同一性。
- Ben Claremon/The Inoculated Investor 原始发布页称这是本人在 Pasadena 周三活动中的 `hand-typed notes`；近同期 GuruFocus 与 RBCPA 保存了相同归属。
- `2010-05-05`、作者/原 publisher、公开保存件和非逐字限制均已写入 L0。
- 因无录音、无逐字承诺，只能是 `C-named-third-party-notes`，不得升 B。

### L1 与关系

当前没有 L1。本终审不授权自动生成、迁移或上联；未来候选必须使用公开 PDF 的 exact page/line locator、短摘录，并重新走 Critic/Verifier。

## 2013 Daily Journal

### L0

**裁决：`VERIFIED` 为 D 级来源记录；修复结果仍 `NEEDS_REVIEW`。**

RBCPA 的早期保存页明确称不知道作者，Worldly Partners 文件也没有 note taker、原 publisher 或转录方法。早期传播只能确认这是当时流通的归属线索，不能恢复作者。当前 `D-unattributed-notes-lead`、零 L1和作者未知警示正确。

### L1 与关系

保持零 L1。恢复原始 note taker 或可靠录音前，不得创建 Candidate Corpus、KU、模型或 Case 关系。

## 2014 Daily Journal

### L0

**裁决：`VERIFIED`，证据上限 C。**

- 当前 971 行 Drive 文件与 37 页公开保存件的 971 行及独特编辑插注一致。
- Phil DeMuth 的 Forbes 四部分 `A Fan's Notes` 具名发布链可复现；其本人明确称为 notes 而非 transcript，并承担可能错误。
- SEC DEF 14A 只独立确认 `2014-09-10 10:00` 的活动日期和地点，不证明 transcript wording。L0 已正确区分。
- `C-named-third-party-notes` 正确；不得把 Farnam Street 的同场独立版本合并为当前文本，也不得升 B。

### L1 与关系

当前没有 L1。本终审不授权自动生成、迁移或上联。未来候选须保留 Phil DeMuth/Forbes、非逐字和错误警示，并单独审查。

## 2022 Singleton

### L0

**裁决：`VERIFIED` 为 D 级来源记录；修复结果仍 `NEEDS_REVIEW`。**

- L0 已把早期视频 ID `aciej48jbFk`、待确认的 Million Stories Media production credit 和 candidate transcript Drive ID `132Aul_OH0hNP3B00S5jcIEtgAnbdV1Cq` 放入 `Candidate original chain (not yet verified)`。
- 它没有把频道所有权、制作身份或 transcript publisher 写成已确认事实，也明确 selected excerpt 尚未 replay/timestamp-aligned。
- 官方 Singleton 页面只确认 Prize 日期；当前 transcript wording 与非官方录影仍为 D 级研究线索。

### L1、KU 与关系

- `CU-2022-SINGLETON-0001` 保持 `candidate / D`。
- `KU-0010` 保持 `candidate / tier D / review booleans false`。
- 不得迁移、不得上联、不得关联模型。只有确认视频上传/制作所有权、识别 transcript publisher/transcriber 并完成选段复听和精确时间戳后，才可重新提交 B 级审查。

## Manifest 精确动作

| source_id | 精确状态 | 必须保持的字段与边界 |
|---|---|---|
| `MTP-1986-HARVARD` | 保持 `needs_source` | 保持 `unattributed_transcript / D-lead`；当前收窄后的 `next_action` 保持不变。 |
| `MTP-1996-STANFORD` | 当前保持 `ready_candidate`；完成本报告规定的 L1 locator/status 修订后改为 `verified_sample` | `source_class` 保持 `publisher_edited_excerpts`；`evidence_level` 保持 validator-compatible `C-named-notes`；`canonical_url` 保持 preservation PDF；`next_action` 保持 OID volume/date/pages、excerpt limitation、日期和非逐字警示。 |
| `MTP-2010-WESCO` | 保持 `ready_candidate` | 保持 `named_notes / C-named-notes`、公开 PDF URL及 Ben Claremon/TII hand-typed non-verbatim `next_action`；没有 L1，故不得改 `verified_sample`。 |
| `MTP-2013-DJCO` | 保持 `needs_source` | 保持 `unattributed_notes / D-lead`、RBCPA negative-provenance URL 与作者未知 `next_action`。 |
| `MTP-2014-DJCO` | 保持 `ready_candidate` | 保持 `named_notes / C-named-notes`、公开 PDF URL及 Phil DeMuth/Forbes 错误警示；没有 L1，故不得改 `verified_sample`。 |
| `MTP-2022-SINGLETON` | 保持 `needs_source` | 保持 `unattributed_transcript_plus_unofficial_recording / D-lead`；当前包含视频 ID、制作权、复听和 transcript Drive ID 的 `next_action` 保持不变。 |

1996 即使 manifest 写 `C-named-notes`，任何相邻说明必须继续称 `publisher-edited excerpts`。不得为了枚举一致性把 L0、L1 或 README 改写成“具名现场笔记”。

## 允许的机械执行顺序

1. 只修订 `CU-1996-STANFORD-0001.locator` 为 OID original p.24，并将该 L1 status 改为 verified；不修改正文、不上联。
2. 将 1996 manifest `ready_candidate` 改为 `verified_sample`；其 source class、evidence level 和 next action 不变。
3. 2010、2014 两条 C 级 manifest 继续 `ready_candidate`；不得因为 L0 已修复而制造 verified sample。
4. 1986、2013、2022 三条 D 级 manifest 继续 `needs_source`；对应 L1/KU 状态保持。
5. 不修改任何 KU、模型、Case 或其他来源等级。
6. 重新运行 sources validator、corpus validator 与全部测试；三者全绿后机械执行才完成。

## 最终门禁

- **已修复为 C：**1996 OID publisher-edited excerpts、2010 Claremon notes、2014 DeMuth notes。
- **1996 L1：**当前 `REVISE`；exact OID p.24 修订后可 C 级 standalone verified；上联永久 `REJECT`。
- **继续 D：**1986、2013、2022。
- **D 级对象状态：**1986 L1、2022 L1 与 KU-0010 均保持 candidate；2013 保持零 L1。
- **C manifest：**1996 条件式 `verified_sample`；2010、2014 保持 `ready_candidate`。
- **禁止事项：**不得新增或修改 KU、模型、Case、字段或系统；不得把 C 级 excerpts/notes 称为逐字原稿或把 D 级线索上联。
