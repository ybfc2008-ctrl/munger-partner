#!/usr/bin/env python3
"""Validate the source manifest using only Python's standard library."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "sources" / "source-manifest.csv"
REQUIRED = {
    "source_id", "year", "title", "category", "drive_url", "source_class",
    "evidence_level", "canonical_url", "ingest_status", "public_policy", "next_action",
}
LEVELS = {"A-primary", "B-traceable-transcript", "C-named-notes", "D-lead"}
STATUSES = {"ready_candidate", "needs_source", "needs_ocr", "reference_only", "missing_local"}
POLICIES = {"link_and_excerpt", "metadata_only"}


def main() -> int:
    errors: list[str] = []
    seen: set[str] = set()
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = REQUIRED - set(reader.fieldnames or [])
        if missing:
            errors.append(f"missing columns: {', '.join(sorted(missing))}")
        rows = list(reader)

    for line, row in enumerate(rows, start=2):
        source_id = row.get("source_id", "")
        if not source_id:
            errors.append(f"line {line}: missing source_id")
        elif source_id in seen:
            errors.append(f"line {line}: duplicate source_id {source_id}")
        seen.add(source_id)
        if not row.get("title"):
            errors.append(f"line {line}: missing title")
        if row.get("year") and (not row["year"].isdigit() or len(row["year"]) != 4):
            errors.append(f"line {line}: year must be four digits or blank")
        if row.get("evidence_level") not in LEVELS:
            errors.append(f"line {line}: invalid evidence_level")
        if row.get("ingest_status") not in STATUSES:
            errors.append(f"line {line}: invalid ingest_status")
        if row.get("public_policy") not in POLICIES:
            errors.append(f"line {line}: invalid public_policy")
        if not row.get("drive_url") and not row.get("canonical_url"):
            errors.append(f"line {line}: needs a Drive or canonical URL")
        if row.get("ingest_status") == "ready_candidate" and not row.get("next_action"):
            errors.append(f"line {line}: ready_candidate still needs an extraction action")

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    counts = {level: sum(row["evidence_level"] == level for row in rows) for level in sorted(LEVELS)}
    print(f"Validated {len(rows)} sources; levels: {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
