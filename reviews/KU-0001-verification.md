# Verification: KU-0001

- Verifier: `codex-independent-verifier:/root/usc_1994_verifier`
- Verified at: `2026-08-31`
- Candidate revision checked: `sha256:c89def7ad34f31d607e440cc083ae5b44d9d7de743cc1e65532d786110e6c71e`
- Private extraction checked: `sha256:55cd4dd22ea0ef2f74a8a70c323fc753db44035e967457e94b594462a5e5422b`
- Decision: `revise`
- Mechanical promotion to `/verified`: `not_allowed`
- Scope: independent verification of the revised Candidate and its L0/L1 evidence chain; this file does not alter Candidate, Corpus, model registry, or pipeline state.

## Verdict

The revision fixes the Critic's most serious title error: it no longer instructs users to select a framework before collecting facts. It also harmonizes the source tier to `B`, explicitly labels the principle and boundary as AI inference, keeps the unapproved model mapping empty, and does not invent a counterexample.

It is not yet safe to promote mechanically. The L1 excerpt still omits direct textual support for two material parts of the L2 Candidate, and one provenance count is inconsistent across the L0 record and the reproducible pipeline manifest.

## Checks

| Check | Result | Evidence and reasoning |
|---|---:|---|
| L0 / L1 / L2 separation | Pass | `source.md` and `pipeline-run.json` record provenance and extraction facts; the private full extraction is excluded. The Corpus unit contains only English evidence and Chinese translation. Principle, boundary, and source interpretation remain in the Candidate. No upper-layer inference rewrites L0. |
| Source identity and A/B/C/D level | Pass | The private extraction header identifies Charlie Munger, the USC Marshall lecture context, and the May 5, 1995 *Outstanding Investor Digest* edition. Its SHA-256 matches the L0 record and pipeline manifest. The same opening passage appears in the public Farnam Street transcript, while Whitney Tilson's public compilation independently describes a 1994 USC presentation whose transcript came from the May 5, 1995 OID. These are appropriate corroborations for `B`, not grounds for `A`. |
| Source locator | Pass, with public reproducibility limitation | The relevant source text is at normalized private extraction lines 128–146, under `WITHOUT MODELS FROM MULTIPLE DISCIPLINES`, article p. 3 / scan printed p. 38. The current locator spans lines 124–146 and is precise. Because the normalized extraction is private, the public URL and section/page locator remain necessary. |
| Quote accuracy | Pass | Both English quotations in `CU-1994-USC-0001` match the private extraction. The first is at lines 129–130; the second occurs at line 143 and substantively also at line 136. |
| Context sufficiency in L1 | Fail | The Candidate says the passage warns that a person will force reality into too few models, but the L1 excerpt omits the warning at lines 136–143. The Candidate title says `多学科模型网络`, but L1 also omits the explicit multiple-disciplines statement at lines 144–146. A private line-range locator is not a substitute for carrying the shortest evidence needed by the public L1 anchor. |
| Candidate title | Pass against the source, but depends on the L1 fix | `用多学科模型网络组织事实与经验` is faithful to the full source context and removes the former unsupported temporal ordering. Its `多学科` element must be represented in the L1 evidence excerpt before promotion. |
| Principle / inference separation | Revise | `AI 推断` is explicit, which is correct. However, `放在同一段` is literally inaccurate: the latticework statement, the multiple-model warning, and the multiple-disciplines statement span consecutive paragraphs/turns in the extraction. Use `同一连续论述` or `同一节`. The warning itself is faithful once its supporting excerpt is added to L1. |
| Boundary / inference separation | Pass | The boundary is explicitly labeled `AI 推断（项目规范）` and does not pretend to be Munger's wording. It is concise and consistent with the project's anti-model-proliferation rule. |
| Chinese translation | Pass as `ai_draft` | The translation preserves the practical meaning and does not add a decision claim. `可用的知识` is slightly interpretive for `have them in a usable form`, so it must not be relabeled `human_checked` without a human translation review. A more literal wording would reduce ambiguity, but this is not by itself a rejection ground. |
| Existing-model authorization and duplication | Pass | `models/README.md` deliberately leaves the canonical registry empty. The Candidate's `models: []` and pipeline state `UNKNOWN_NO_APPROVED_MODEL_REGISTRY` comply with the rule; this verification does not authorize a new model. |
| Counterexample honesty and causality | Pass | `待研究` and the pipeline state `UNKNOWN_NO_VERIFIED_CASE` truthfully state the gap. No case or causal chain was fabricated. This satisfies the rule that a missing reliable counterexample may remain empty or unknown. |
| Copyright / redistribution | Pass | The repository excludes the full transcript and publishes only two short quotations with locators and source links. This is consistent with `link_and_excerpt`. The required context fix should still add only the shortest sentences necessary. |
| Provenance consistency | Fail | `source.md` records `92764` extracted characters, while `pipeline-run.json` records `92765`, and the checked private file is 92,765 characters/bytes with the recorded SHA-256. This is plausibly a trailing-newline counting difference, but the L0 record currently does not state that convention. |

## Independent source comparison

- Private evidence: `work/usc-1994-extracted.txt`, lines 124–146; checked SHA-256 `55cd4dd22ea0ef2f74a8a70c323fc753db44035e967457e94b594462a5e5422b`.
- Public context: [Farnam Street transcript](https://fs.blog/great-talks/a-lesson-on-worldly-wisdom/) reproduces the latticework, too-few-models, reality-distortion, and multiple-disciplines sequence.
- Public metadata corroboration: [Whitney Tilson compilation](https://tilsonfunds.com/Mungerwritings2001.pdf) describes the 1994 USC presentation and attributes its transcript to the May 5, 1995 *Outstanding Investor Digest*.

Neither public source is treated as an official USC record or verified recording. They corroborate the declared `B` transcript; they do not upgrade it to `A`.

## Required changes before re-verification

1. Expand `CU-1994-USC-0001` with the shortest source text needed to show both safeguards currently used by the Candidate: too few models can cause reality to be forced to fit them, and the models must come from multiple disciplines. Keep the excerpt short and retain the existing section/page/line locator.
2. In the Candidate principle, replace `放在同一段` with an accurate phrase such as `放在同一连续论述中` or `在同一节连续说明`.
3. Resolve the `92764` versus `92765` character-count mismatch in `source.md` and `pipeline-run.json`, either by using one count or explicitly documenting that one excludes the terminal newline. Do not change the verified SHA-256.
4. Recompute the Corpus and Candidate revision hashes after those edits, then run a fresh independent verification. Until that succeeds, keep both units `candidate` and leave every `review.*_checked` field unchanged.

## Promotion decision

`revise` — no field may be mechanically flipped to `true` in the current Candidate, and the file must not be moved or copied to `/verified`. Attribution, duplicate/model-registry, and no-fabricated-causality checks have substantively passed, but the repository's review booleans are promotion gates for the whole revision rather than partial progress markers. They should be updated only after the required L0/L1/L2 corrections are reviewed together.
