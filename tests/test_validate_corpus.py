from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validator", ROOT / "scripts" / "validate_corpus.py")
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VALIDATOR)


class CorpusValidatorTest(unittest.TestCase):
    def test_candidate_template_is_valid(self) -> None:
        errors = VALIDATOR.validate(ROOT / "templates" / "knowledge-unit.md", "candidate")
        self.assertEqual(errors, [])

    def test_candidate_cannot_be_placed_in_verified(self) -> None:
        errors = VALIDATOR.validate(ROOT / "templates" / "knowledge-unit.md", "verified")
        self.assertTrue(any("status must be 'verified'" in error for error in errors))
        self.assertTrue(any("review checks" in error for error in errors))

    def test_rejected_requires_reason(self) -> None:
        template = (ROOT / "templates" / "knowledge-unit.md").read_text(encoding="utf-8")
        template = template.replace('"status": "candidate"', '"status": "rejected"')
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "rejected.md"
            path.write_text(template, encoding="utf-8")
            errors = VALIDATOR.validate(path, "rejected")
        self.assertIn("rejected unit needs review.rejection_reason", errors)

    def test_frontmatter_is_json(self) -> None:
        text = (ROOT / "templates" / "knowledge-unit.md").read_text(encoding="utf-8")
        payload = text.split("---", 2)[1]
        self.assertEqual(json.loads(payload)["id"], "KU-0001")


if __name__ == "__main__":
    unittest.main()
