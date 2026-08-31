#!/usr/bin/env python3
"""Normalize and chunk a transcript without interpreting its content."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def clean_text(text: str) -> str:
    """Perform loss-minimizing normalization only; never paraphrase."""
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    normalized = CONTROL_RE.sub("", normalized)
    normalized = "\n".join(line.rstrip() for line in normalized.split("\n"))
    return normalized.strip() + "\n"


def chunk_lines(text: str, source_id: str, max_chars: int) -> list[dict[str, object]]:
    if max_chars < 200:
        raise ValueError("max_chars must be at least 200")
    lines = text.splitlines()
    chunks: list[dict[str, object]] = []
    start = 0
    current: list[str] = []
    size = 0

    def flush(end_index: int) -> None:
        nonlocal start, current, size
        if not current:
            return
        body = "\n".join(current).strip() + "\n"
        number = len(chunks) + 1
        chunks.append({
            "id": f"{source_id}-CHUNK-{number:04d}",
            "source_id": source_id,
            "start_line": start + 1,
            "end_line": end_index,
            "sha256": sha256(body),
            "text": body,
        })
        current = []
        size = 0

    for index, line in enumerate(lines):
        line_size = len(line) + 1
        if current and size + line_size > max_chars:
            flush(index)
            start = index
        if not current:
            start = index
        current.append(line)
        size += line_size
    flush(len(lines))
    return chunks


def run(input_path: Path, out_dir: Path, source_id: str, max_chars: int) -> dict[str, object]:
    raw = input_path.read_text(encoding="utf-8")
    cleaned = clean_text(raw)
    chunks = chunk_lines(cleaned, source_id, max_chars)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "cleaned.txt").write_text(cleaned, encoding="utf-8")
    with (out_dir / "chunks.jsonl").open("w", encoding="utf-8") as stream:
        for chunk in chunks:
            stream.write(json.dumps(chunk, ensure_ascii=False) + "\n")
    public_index = [
        {key: value for key, value in chunk.items() if key != "text"}
        for chunk in chunks
    ]
    (out_dir / "chunk-index.json").write_text(
        json.dumps(public_index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    manifest = {
        "source_id": source_id,
        "input_file": input_path.name,
        "raw_sha256": sha256(raw),
        "cleaned_sha256": sha256(cleaned),
        "raw_characters": len(raw),
        "cleaned_characters": len(cleaned),
        "cleaned_lines": len(cleaned.splitlines()),
        "chunk_count": len(chunks),
        "max_chars": max_chars,
        "semantic_rewriting": False,
        "chunk_index_contains_text": False,
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--max-chars", type=int, default=6000)
    args = parser.parse_args()
    manifest = run(args.input, args.out_dir, args.source_id, args.max_chars)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
