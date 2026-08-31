# Review: KU-0001

- Reviewer: `codex-independent-reviewer:/root/usc_1994_reviewer`
- Reviewed at: `2026-08-31`
- Candidate revision: `sha256:37a73d87918fc54dc9d54024267a4e18e8eb90644f18827098bf010a0aa173d5`
- Decision: `revise`
- Scope: evidence and reverse review only; this review does not approve a core model or promote the Candidate.

## Checks

| Check | Pass | Evidence or problem |
|---|---:|---|
| Source is authentic enough for its declared tier | Yes, with metadata correction required | The private extraction identifies Charlie Munger, USC, and the May 5, 1995 *Outstanding Investor Digest* publication. Its surrounding text says the editors attended the lecture and had permission to share it. The quoted passage matches the public Farnam Street transcript. A separate public scan/compilation also identifies the lecture as April 14, 1994 and the transcript as coming from the May 5, 1995 OID. This supports the repository's `B` classification, not an official-record or verified-recording claim. The Candidate's `secondary` label does not use the A/B/C/D vocabulary required by `RULES.md`; the schema mapping must be made explicit or harmonized. |
| Locator is reproducible | Yes, with a limitation | In the private normalized extraction, the relevant section begins at lines 124–127, the quoted sentence is at line 131, and the multiple-model warning continues through lines 136–146. The section is article p. 3 / scan printed p. 38. The same sequence appears under the public transcript's opening “What is elementary, worldly wisdom?” passage. The private line numbers cannot be independently reproduced from the public repository because that extraction is intentionally excluded, so the public URL and section-level locator should remain part of the evidence trail. |
| Quote preserves its surrounding meaning | No | The seven-word quote is genuine, but it is too narrow to support the Candidate's title and full interpretation by itself. The immediately preceding text says isolated facts are unusable unless they hang together on a latticework of theory; the following text says experience should be arrayed on that latticework and then warns that one or two models can cause a person to force reality to fit them. Most importantly, the title “先建立解释框架，再收集孤立事实” adds a temporal procedure—choose a framework first, then collect facts—that the passage does not state. |
| Interpretation is separated from evidence | No | The principle paragraph is marked `AI 解释`, which is good, but the title presents the unsupported “先……再……” ordering without an inference label. The boundary paragraph also introduces prediction, risk exposure, and falsifiability criteria that are not stated in this passage and are not explicitly labeled as reviewer/AI-derived guidance. |
| Existing-model duplication was checked | Yes, within the present repository | Repository-wide search found no approved model entry to merge into; `models/README.md` says the canonical list is intentionally empty pending project-owner approval, and the Candidate correctly leaves `models` empty. This does not establish that a new model should be created, and this review makes no such decision. |
| Causal claims are supported | Not applicable as a case claim; wording still needs care | No real-world counterexample or case is asserted, so there is no fabricated case-causality chain to reject. The tendency to force reality into one or two models is present as Munger's claim in the surrounding passage, but it is not independently established by this source as an empirical causal finding. Any stronger causal wording should remain attributed or labeled as inference. |
| Copyright and redistribution policy are followed | Yes | The repository does not redistribute the full transcript. The Candidate contains only a seven-word quotation plus links and locators, consistent with `link_and_excerpt`. Expanding the evidence for revision should still use only the shortest context needed to support the claim. |

## Source comparison

- Private extraction: `work/usc-1994-extracted.txt`, especially lines 124–146; normalized SHA-256 recorded as `55cd4dd22ea0ef2f74a8a70c323fc753db44035e967457e94b594462a5e5422b`.
- L0 record: `raw/speeches/MTP-1994-USC/source.md`.
- L1 unit: `corpus/MTP-1994-USC/chunks/CU-1994-USC-0001.md`.
- Public context check: https://fs.blog/great-talks/a-lesson-on-worldly-wisdom/
- Public scan/metadata corroboration: https://tilsonfunds.com/Mungerwritings2001.pdf

## Strongest way this could mislead

The current title can be read as advice to select an explanatory framework first and only then gather facts. That workflow invites confirmation bias and fact selection. It is materially different from the passage's stronger, two-sided point: facts need an organizing latticework, but the latticework must contain multiple models from multiple disciplines so the thinker does not torture reality to fit a narrow frame. Because the quoted evidence is only one sentence, a user may never see this safeguard.

## Required changes

1. Replace or expand the L1 excerpt with the shortest passage that directly supports both parts of the claim: isolated facts are not usable without a latticework, and relying on too few models can distort reality. Keep the excerpt short and retain the page/section locator.
2. Remove the unsupported temporal ordering from the title and principle. A faithful direction would be “用多学科模型网络组织事实与经验”; exact naming remains the producer/project owner's choice.
3. Label the principle and boundary separately as AI inference. Either remove the prediction/risk/falsifiability criteria or identify them as project-level normative guidance rather than words or implications established by this passage.
4. Harmonize `source.tier: secondary` with the A/B/C/D source levels in `RULES.md`, or document an explicit schema mapping showing that this Candidate refers to the L1 unit's `B` rating.
5. After revision, run a new independent review. Do not promote this revision to `verified` on the strength of the present review.
