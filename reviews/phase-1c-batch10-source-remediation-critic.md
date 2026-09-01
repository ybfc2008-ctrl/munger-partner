# PHASE 1C Batch 10｜Source Remediation Critic

- Reviewer: `codex-independent-critic:/root/rd_0001_verifier`
- Reviewed at: `2026-09-01`
- Scope: 六个 `needs_source`：`MTP-1986-HARVARD`、`MTP-1996-STANFORD`、`MTP-2010-WESCO`、`MTP-2013-DJCO`、`MTP-2014-DJCO`、`MTP-2022-SINGLETON`
- Constraint: 本报告只做来源修复审计；不修改 L0、L1、manifest 或上层知识文件，不新增字段、系统、KU 或模型。

## 总裁决

| Source ID | 当前 | 本轮裁决 | 可否升级 | 结论 |
|---|---:|---|---|---|
| `MTP-1986-HARVARD` | D | `NEEDS_REVIEW` | 否 | 找到后续出版线索，但没有恢复学校档案、原始稿或可与当前文本核对的授权版本。 |
| `MTP-1996-STANFORD` | D | `REVISE` | **可升 C，限 OID 已出版摘录** | 已恢复 `Outstanding Investor Digest` 1997-12-29 原刊扫描身份；不能确认 `1996-04-19` 精确活动日，也不能把 OID 编辑摘录称为逐字稿。 |
| `MTP-2010-WESCO` | D | `REVISE` | **可升 C** | 当前 416 行文件与公开 416 行 PDF 全文结构一致；同期页面把笔记归于 Ben Claremon / The Inoculated Investor，并明确为 hand-typed notes。 |
| `MTP-2013-DJCO` | D | `NEEDS_REVIEW` | 否 | 公开早期保存页反而明确说不知道作者；未恢复录音或原发布者。 |
| `MTP-2014-DJCO` | D | `REVISE` | **可升 C** | 当前 971 行文件与 Phil DeMuth 在 Forbes 发布的四部分具名 `A Fan's Notes` 文本及编辑插注相符；SEC 可确认活动日。 |
| `MTP-2022-SINGLETON` | D | `REVISE`（来源线索） | 暂否 | 找到更早的完整视频 ID、制作方标识线索和原 transcript Drive ID，但尚未独立确认上传频道所有权，也未对选段做时间戳复听。 |

这里的升级只恢复来源身份，不自动授权 L1、KU、模型或产品结论。C 级仍是第三方记录，不是 Munger 逐字原稿；D 级仍不得上联。

## 一、`MTP-1986-HARVARD`

### 新找到的材料

1. Open Library 的书目记录确认 Charles T. Munger 署名的 *On Success*（Donning Company Publishers, 2009）目录包含 `Harvard School commencement speech June 13, 1986`。
2. *Poor Charlie's Almanack*、*On Success* 和多个后续档案均把该讲话列为 1986-06-13 Harvard School commencement speech。
3. 本轮仍未找到 Harvard-Westlake 官方节目单、学校档案页、录音、Munger 原稿，或可公开逐页核对的授权出版版本。

### 裁决：`NEEDS_REVIEW`，不得升级

书目记录能提高“这场讲话存在”的可信度，但不能证明仓库中 Worldly Partners PDF 的具体文字就是授权版本。项目规则又明确要求书籍拆分并回溯来源；仅凭后续书目和广泛转载不能把当前无署名文本升级。

保持：

- `D-unattributed-transcript-lead`；
- L1 继续 `candidate / D`；
- 不关联任何 KU、模型、Case 或 Decision Engine。

### 仍缺什么

- Harvard-Westlake 官方 archive/program；或
- Munger/出版社可核对的授权正文版本；或
- 原稿、录音及可复现定位。

### Manifest / L0 精确建议

不改等级、class 或 ingest status。只可把 `next_action` 收窄为：

> Locate a Harvard-Westlake archive/program or a page-verifiable authorized edition; bibliographic listings of *On Success* and *Poor Charlie's Almanack* confirm the speech title/date but do not authenticate the current transcript wording.

L0 可增加一条“后续授权书目确认事件与篇名，但本轮未对照其正文”的负责任说明；不能写成来源链已经恢复。

## 二、`MTP-1996-STANFORD`

### 新恢复的原刊身份

公开可找到 `Outstanding Investor Digest`（OID）`Volume XII, Number 3, December 29, 1997` 的原刊扫描。扫描的目录、页眉和正文把 Munger 部分标为：

- `WORLDLY WISDOM REVISITED`；
- `Excerpts from a lecture and answers to student questions thereafter during a visit last year to a Stanford Law School Course ... “Business: What Lawyers Should Know.”`；
- course taught by Professor William Lazier；
- Munger 内容位于原刊 pp. 24–31，并在 1998-03-13 期续载。

仓库当前 32 页 compilation 的开头也保存同一 OID 署名段落。`CU-1996-STANFORD-0001` 的 latticework 句位于这一明确的 OID 摘录边界内，而不是来自汇编中其他未分篇材料。

### 裁决：`REVISE`；可从 D 升至 C，但边界必须冻结

OID 是可识别的第三方出版者，原刊扫描比“无署名 compilation”恢复了发布身份。因此，对能够定位到 OID pp. 24–31 的文字，可以按 `C-publisher-edited-excerpts` 处理。

不得升级到 B，原因是：

- OID 自称 `Excerpts`，不是完整 transcript；
- 没有个人 transcriber 或录音核对；
- OID 只说 `a visit last year`，不能独立证明 `1996-04-19`；
- 后续 *Poor Charlie's Almanack* 又明确说明编辑者做过删节和评论，不能用其重编本反向制造逐字性。

### 机械修订授权建议

L0：

1. 把核心来源身份改为 `Outstanding Investor Digest, Vol. XII No. 3, 1997-12-29, pp. 24-31; continued 1998-03-13`。
2. 把现有 Worldly Partners 32 页 PDF降为 preservation/compilation copy，不再作为唯一 canonical provenance。
3. Evidence 改为 `C-publisher-edited-excerpts / exact event date unresolved`。
4. 日期改为 `1996 (OID says “last year”); 1996-04-19 remains reported, not independently established`。
5. 明确 `not a complete or verbatim transcript`。

Manifest 建议精确改为：

- `source_class: publisher_edited_excerpts`
- `evidence_level: C-publisher-excerpts`
- `alternate_url:` 填入当前 Worldly Partners preservation PDF；canonical 应指可复现的 OID 原刊扫描，若仓库政策不接受 Scribd 作为 canonical，则 canonical 留现有 Drive、并在 L0 记录原刊扫描 URL。
- `ingest_status: ready_candidate`
- `next_action: Preserve OID volume/date/pages and excerpt limitation; do not claim 1996-04-19 or verbatim status without Stanford records or recording.`

L1：可重新提交为 C 级 standalone Corpus，但因与 `KU-0001/M01` 重复，**本轮仍不授权上联**。其 locator 必须改为 OID 原刊页，而不是只写 compilation p.2。

## 三、`MTP-2010-WESCO`

### 同一性与作者链

公开 Worldly Partners PDF：

- 题名从 `Wesco 2010 Meeting Notes, Part I` 开始；
- 共 12 个文件页、416 个解析行；
- 包含 Part I、Part II 及连续 Q&A。

仓库 Drive extraction 同为 416 行，题名、Part I/II 结构与公开件一致。这不是仅凭主题或零散句子判断相似，而是完整文档级对齐。

同期/近同期发布链进一步恢复作者：

- GuruFocus 于 2010-05-08 保存发布说明，作者自称这是其 `hand-typed notes`，署名 `Inoculated Investor`，并链接原 Blogspot；
- RBCPA 于 2010-05-10 收录为 `Wesco 2010 Annual Meeting Notes by Innoculated Investor Blogspot`；
- Rational Walk 于 2010-05-11 明确感谢 `Ben of The Inoculated Investor` 提供详细 Wesco notes。

### 裁决：`REVISE`；D → C

这足以恢复为 Ben Claremon / The Inoculated Investor 的具名现场笔记。正确上限是 C，不是 B：作者称 hand-typed notes，没有把它表示为逐字 transcript，也没有录音对齐。

### 机械修订授权建议

L0：

1. Title 改为 `Wesco 2010 Annual Meeting Notes`，说明文件同时含 Part I/II。
2. Event date 增加 `2010-05-05`，并注明同期发布页称 meeting occurred on Wednesday；若要求官方日期锚点，可再链接 Wesco proxy。
3. Author/original publisher 改为 `Ben Claremon / The Inoculated Investor`。
4. 加入公开 12 页 PDF及 GuruFocus、RBCPA、Rational Walk 三条 provenance URL。
5. 明确 `hand-typed, non-verbatim third-party notes; no recording alignment established`。
6. Evidence 改为 `C-named-third-party-notes`。

Manifest 建议精确改为：

- `source_class: named_notes`
- `evidence_level: C-named-notes`
- `alternate_url: https://worldlypartners.com/wp-content/uploads/2024/01/2010-wesco-annual-meeting-notes-of-charlie-mungers-remarks.pdf`
- `ingest_status: ready_candidate`
- `next_action: Preserve Ben Claremon / The Inoculated Investor attribution and hand-typed, non-verbatim limitation; any L1 must use exact public PDF page/line locator.`

当前没有 L1。本裁决只允许以后从 C 级来源提出 candidate，不授权自动生成、迁移或上联。

## 四、`MTP-2013-DJCO`

### 公开来源的实际结果

RBCPA 的早期 archive 页面（2013-02-28 收录）明确写：

> `Alleged Daily Journal Corp Annual Meeting Notes (Feb 6, 2013)`，并说明不知道是谁准备这些笔记，且笔记不是 rbcpa.com 所写。

这条公开记录确认 2013-02-06 的归属曾被当时传播，但同时明确保留作者断点。Worldly Partners 29 页保存件也没有 note taker、首发 publisher 或转录方法。仓库 extraction 为 1091 行，当前公开解析为 1098 行；不能在未完成差异核对前声称全文同一。

### 裁决：`NEEDS_REVIEW`，不得升级

早期 archive 是有价值的负面 provenance 证据，但它没有恢复作者。保持 D、零 L1、禁止上联。

### Manifest / L0 精确建议

Manifest 等级和状态保持：

- `unattributed_notes`
- `D-lead`
- `needs_source`

可补：

- `alternate_url: https://www.rbcpa.com/wp-content/uploads/2017/01/DJCO_Meeting_Detailed_Notes_2013.pdf`
- `next_action: Identify the original note taker or a recording; RBCPA's 2013 archive explicitly says attribution was unknown and cannot support an upgrade.`

L0 可增加 RBCPA archive 页作为“作者未知”的公开佐证，并记录公开 PDF 当前 1098 行与 Drive 1091 行尚需差异比对。不得把“早期保存”写成“原始出版”。

## 五、`MTP-2014-DJCO`

### 原始发布者与文本同一性

仓库 Drive extraction 为 67,866 字符、971 行；Worldly Partners 37 页 PDF 公开解析也为 971 行。其独特编辑插注，例如 `[DJCO Board Member] Peter Kaufman`、ticker 注释与分段，能逐段对应 Phil DeMuth 在 Forbes 发布的四部分系列：

- `Charlie Munger And The 2014 Daily Journal Annual Meeting: A Fan's Notes`（2014-09-19）；
- Part Two（2014-09-25）；
- 后续 Part Three / Part Four。

Forbes 页面具名 Phil DeMuth，并明确警示：`If it sounds smart, it's Munger; if it's wrong, it's me.` 这说明它是具名第三方笔记，不是官方逐字 transcript。相比之下，Farnam Street 2016 年 53 页 production 是另一份更完整、同场但不同编辑结构的 notes，不能冒充当前 37 页文件的原件。

SEC 的 Daily Journal definitive proxy 可独立确认活动为 `2014-09-10 10:00`，地点 949 E. 2nd Street, Los Angeles。

### 裁决：`REVISE`；D → C

具名作者、原始 Forbes 发布链、文档级行数和独特编辑插注共同建立了足够的来源链。升级限于 `C-named-third-party-notes`。不得称 B transcript，也不得把 Farnam Street 版本和 Phil DeMuth 版本合并成一个文本。

### 机械修订授权建议

L0：

1. Event date 改为 `2014-09-10`，以 SEC DEF 14A 为活动锚点。
2. Note taker/original publisher 改为 `Phil DeMuth / Forbes, four-part “A Fan's Notes” series`。
3. Public preservation copy 增加 Worldly Partners 37 页 PDF；说明其 971 行与 Drive 971 行及编辑插注对齐。
4. 加入 SEC proxy 与四个 Forbes 原文 URL。
5. Evidence 改为 `C-named-third-party-notes`，并保留 DeMuth 自己的误差警示。
6. 明确 Farnam Street 2016 production 是同场独立版本，只可用于交叉检查，不是当前文件的 publisher。

Manifest 建议精确改为：

- `source_class: named_notes`
- `evidence_level: C-named-notes`
- `alternate_url: https://worldlypartners.com/wp-content/uploads/2024/01/2014-daily-journal-corp-annual-meeting-notes-of-charlie-mungers-remarks.pdf`
- `ingest_status: ready_candidate`
- `next_action: Preserve Phil DeMuth/Forbes four-part attribution and the author's error disclaimer; cite SEC only for event date, not transcript wording.`

当前没有 L1。来源升级后可提出 C 级 candidate，但仍须按页/行定位、短摘录并单独 Critic/Verifier；本报告不预授权上联。

## 六、`MTP-2022-SINGLETON`

### 新恢复的发布线索

本轮找到比仓库现有非官方复制件更早、更接近原发布链的两项：

1. 完整视频 ID `aciej48jbFk`，公开嵌入标题为 `Charlie Munger in Conversation with Todd Combs | Singleton Prize for CEO Excellence`。多个 2023 年同期页面把它称为 Million Stories Media 的 45 分钟制作，并记录 `Filmed on April 19, 2022 at The Maybourne Beverly Hills`。
2. Transcript Google Drive ID `132Aul_OH0hNP3B00S5jcIEtgAnbdV1Cq`，文件名包含 `Singleton Prize for CEO Excellence_ Charlie Munger in Conversation with Todd Combs_020623.pdf`；它与仓库 comparison PDF 的文本相符。

公开网页还逐字保存了 `CU-2022-SINGLETON-0001` 的两段 selected wording，因此内容复现性明显提高。

### 裁决：`REVISE`（修复线索），暂不升级

仍不能从 D 升 B，原因是：

- 本批无法从可抓取的 YouTube metadata 独立确认 `aciej48jbFk` 的上传频道确为活动制作方，而不是第三方重传；
- transcript Drive 文件仍未显示具名 transcriber 或明确 original publisher；
- 尚未实际复听视频并记录两段选文的精确起止时间；
- Singleton Foundation 官方页只确认 Prize 日期，不确认当前 transcript 或其发布链。

多家网页引用同样文字，只能提高“值得复听”的优先级，不能用内容相似替代来源升级。

### Manifest / L0 精确建议

等级和状态保持：

- `unattributed_transcript_plus_unofficial_recording`
- `D-lead`
- `needs_source`

但应修订 next action，加入已经恢复的具体对象：

> Verify ownership/provenance of YouTube video `aciej48jbFk` and its Million Stories Media production credit; replay and timestamp-align CU-2022-SINGLETON-0001; identify the publisher/transcriber of Drive transcript `132Aul_OH0hNP3B00S5jcIEtgAnbdV1Cq` before considering B.

L0 应把 `aciej48jbFk` 与 transcript Drive ID 加入“candidate original chain”小节，同时明确它们尚未验证；现有 `m7CkqR8CLhs` 继续只作为 nonofficial copy。不得把 `Million Stories Media` 写成已确认 publisher，除非频道所有权或视频片尾/片头制作标识经独立复看确认。

L1 和 `KU-0010` 必须继续 `candidate / D / NEEDS_REVIEW`，不得迁移或上联。

## 七、执行边界与最小顺序

1. 先机械修订 1996、2010、2014 三条 L0/manifest 的来源身份、等级和限定语。
2. 1986、2013、2022 保持 D/`needs_source`；只补更具体的 provenance gap 与已检查线索。
3. 1996 现有 L1 即使升 C，也只可 standalone；它与 KU-0001/M01 重复，本报告不授权上联。
4. 2010、2014 当前没有 L1；不要因来源升级自动生成上层知识。
5. 2022 只有完成频道/制作方确认和实际时间戳复听后，才可重新提交 B 级审查；不能机械升级。
6. 任一 C 级条目不得被改写成“芒格逐字原话”；引用旁必须保留第三方 notes/excerpts 身份。

## 最终结论

本轮真正恢复了三条来源链：

- 1996：OID 原刊编辑摘录；
- 2010：Ben Claremon / The Inoculated Investor 具名手打现场笔记；
- 2014：Phil DeMuth / Forbes 具名四部分现场笔记，并由 SEC 独立确认活动日期。

1986 与 2013 没有新证据足以升级。2022 找到了更接近原始制作的具体视频和 transcript 标识，但仍差最后两道证据门：上传/制作所有权确认与选段时间戳复听。因此仍保持 D。没有任何 D 级材料获得上联授权，也没有新增 KU、模型、字段或系统。
