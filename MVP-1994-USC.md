# 1994 USC MVP report

## Scope completed

- Drive PDF registered as `MTP-1994-USC`, source level `B`.
- Private extraction normalized without semantic rewriting: 92,765 characters including the terminal newline.
- Full transcript split into 16 private chunks with line ranges and SHA-256 hashes.
- Public repository contains provenance, a no-text chunk index and the reproducible standard-library pipeline, but not the copyrighted full transcript.
- One L1 Corpus unit and one L2 principle completed the full Candidate → Critic → revision → Verifier → revision → Final Verifier → Verified path.

This is a pipeline proof, not a claim that the whole 1994 lecture has been distilled into verified knowledge.

## North-star metrics

### Traceability

`1 / 1 = 100%` for the current Verified sample. `KU-0001` points to `CU-1994-USC-0001`, which points to the L0 source record, Drive file, section/page/line locator and private extraction hash.

### Compression

`Not yet measurable.` The owner-approved core-model registry is intentionally empty. The pipeline keeps `models: []` and records `UNKNOWN_NO_APPROVED_MODEL_REGISTRY` instead of inventing a model.

### Correction capability

Two promotion attempts were blocked before the third independent verification passed. The review trail corrected an unsupported temporal rule, insufficient context, inference labeling, source-tier vocabulary, a paragraph-location error and an extraction-count convention.

## Deliberate unknowns

- Exact lecture date and an official USC record remain unconfirmed.
- No verified recording is known; public transcripts only corroborate the `B` source.
- Chinese translation remains `ai_draft`.
- No verified historical failure case has been attached.
- No canonical core model has been approved.
- The remaining lecture sections have not been promoted into L1/L2 knowledge units.

## Gate for the next source

Do not begin 1995 Psychology until the owner accepts this MVP's structure and decides whether `KU-0001` maps to an approved core model. The 1994 source may continue to produce additional Candidates, but each must repeat the same independent review gates.
