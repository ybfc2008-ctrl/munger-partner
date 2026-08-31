from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("prepare", ROOT / "scripts" / "prepare_transcript.py")
PREPARE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(PREPARE)


class PrepareTranscriptTest(unittest.TestCase):
    def test_cleaning_is_loss_minimizing(self) -> None:
        self.assertEqual(PREPARE.clean_text("A  B\r\nC\x02\n"), "A  B\nC\n")

    def test_chunks_preserve_line_order(self) -> None:
        text = "\n".join(f"line {index}: " + "x" * 40 for index in range(20)) + "\n"
        chunks = PREPARE.chunk_lines(text, "MTP-TEST", 220)
        restored = "".join(str(chunk["text"]) for chunk in chunks)
        self.assertEqual(restored, text)
        self.assertEqual(chunks[0]["start_line"], 1)
        self.assertEqual(chunks[-1]["end_line"], 20)

    def test_run_writes_reproducible_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.txt"
            source.write_text("first\r\nsecond\n", encoding="utf-8")
            first = PREPARE.run(source, root / "one", "MTP-TEST", 200)
            second = PREPARE.run(source, root / "two", "MTP-TEST", 200)
            public_index = (root / "one" / "chunk-index.json").read_text(encoding="utf-8")
        self.assertEqual(first, second)
        self.assertFalse(first["semantic_rewriting"])
        self.assertFalse(first["chunk_index_contains_text"])
        self.assertNotIn('"text"', public_index)


if __name__ == "__main__":
    unittest.main()
