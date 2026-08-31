#!/usr/bin/env python3
"""Validate JSON-frontmatter Markdown knowledge units using only stdlib."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "corpus"
VALID_STATUS = {"candidates": "candidate", "verified": "verified", "rejected": "rejected"}
REQUIRED_SECTIONS = ["原话", "原理", "反例", "边界", "出处"]
ID_RE = re.compile(r"^KU-[0-9]{4,}$")


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, flags=re.DOTALL)
    if not match:
        raise ValueError("missing --- delimited frontmatter")
    try:
        meta = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise ValueError(f"frontmatter must be valid JSON: {exc}") from exc
    meta["_body"] = text[match.end():]
    return meta


def validate(path: Path, expected_status: str) -> list[str]:
    errors: list[str] = []
    try:
        meta = frontmatter(path)
    except (OSError, ValueError) as exc:
        return [str(exc)]

    for field in ("id", "status", "kind", "title", "models", "source", "review"):
        if field not in meta:
            errors.append(f"missing field: {field}")

    if not ID_RE.match(str(meta.get("id", ""))):
        errors.append("id must match KU-0001")
    if meta.get("status") != expected_status:
        errors.append(f"status must be {expected_status!r} in this directory")
    if meta.get("kind") not in {"quote", "principle", "model", "case"}:
        errors.append("invalid kind")
    if not isinstance(meta.get("models"), list):
        errors.append("models must be an array")

    source = meta.get("source", {})
    if not isinstance(source, dict):
        errors.append("source must be an object")
        source = {}
    for field in ("tier", "speaker_or_author", "title", "locator"):
        if field not in source:
            errors.append(f"missing source.{field}")
    if source.get("tier") not in {"primary", "secondary", "lead"}:
        errors.append("source.tier must be primary, secondary, or lead")

    review = meta.get("review", {})
    if not isinstance(review, dict):
        errors.append("review must be an object")
        review = {}
    checks = ("context_checked", "attribution_checked", "duplicate_checked", "causality_checked")
    for field in checks:
        if not isinstance(review.get(field), bool):
            errors.append(f"review.{field} must be boolean")

    reviewers = review.get("reviewers")
    if not isinstance(reviewers, list):
        errors.append("review.reviewers must be an array")
        reviewers = []

    if expected_status == "verified":
        if source.get("tier") == "lead":
            errors.append("verified unit cannot use a lead-only source")
        if not all(review.get(field) is True for field in checks):
            errors.append("all review checks must be true for verified units")
        if not reviewers:
            errors.append("verified unit needs at least one reviewer")
        if not review.get("reviewed_at"):
            errors.append("verified unit needs review.reviewed_at")
        if not source.get("url") and source.get("locator") in {None, "", "待核实"}:
            errors.append("verified unit needs a reproducible source locator")

    if expected_status == "rejected" and not review.get("rejection_reason"):
        errors.append("rejected unit needs review.rejection_reason")

    body = meta.get("_body", "")
    positions = []
    for section in REQUIRED_SECTIONS:
        token = f"## {section}"
        index = body.find(token)
        if index < 0:
            errors.append(f"missing section: {section}")
        positions.append(index)
    existing = [position for position in positions if position >= 0]
    if existing != sorted(existing):
        errors.append("sections must follow 原话 → 原理 → 反例 → 边界 → 出处")
    return errors


def main() -> int:
    failures = 0
    seen: dict[str, Path] = {}
    files = 0
    for folder, status in VALID_STATUS.items():
        for path in sorted((CORPUS / folder).glob("*.md")):
            files += 1
            errors = validate(path, status)
            try:
                unit_id = frontmatter(path).get("id")
            except (OSError, ValueError):
                unit_id = None
            if unit_id in seen:
                errors.append(f"duplicate id; first seen in {seen[unit_id].relative_to(ROOT)}")
            elif unit_id:
                seen[unit_id] = path
            if errors:
                failures += 1
                print(f"FAIL {path.relative_to(ROOT)}")
                for error in errors:
                    print(f"  - {error}")
            else:
                print(f"OK   {path.relative_to(ROOT)}")
    if failures:
        print(f"\n{failures} file(s) failed validation.")
        return 1
    print(f"Validated {files} knowledge unit(s); no errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
