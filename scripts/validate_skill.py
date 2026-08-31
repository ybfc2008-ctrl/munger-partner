#!/usr/bin/env python3
"""Check the repository's Codex skill without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skill" / "munger-partner"
SKILL_MD = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"


def quoted_value(text: str, key: str) -> str | None:
    match = re.search(rf"^\s*{re.escape(key)}:\s*[\"'](.*)[\"']\s*$", text, re.MULTILINE)
    return match.group(1) if match else None


def main() -> int:
    errors: list[str] = []
    skill = SKILL_MD.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", skill, re.DOTALL)
    if not match:
        errors.append("SKILL.md is missing YAML frontmatter")
        frontmatter = ""
    else:
        frontmatter = match.group(1)

    name_match = re.search(r"^name:\s*([^\n]+)$", frontmatter, re.MULTILINE)
    description_match = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    name = name_match.group(1).strip() if name_match else ""
    description = description_match.group(1).strip() if description_match else ""
    if name != SKILL_DIR.name:
        errors.append("skill name must match its directory")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append("skill name must be lowercase letters, digits, or hyphens")
    if not description or "TODO" in description:
        errors.append("skill description is missing or unfinished")
    if "TODO" in skill:
        errors.append("SKILL.md contains unfinished TODO text")

    interface = OPENAI_YAML.read_text(encoding="utf-8")
    display_name = quoted_value(interface, "display_name")
    short_description = quoted_value(interface, "short_description")
    default_prompt = quoted_value(interface, "default_prompt")
    if not display_name:
        errors.append("agents/openai.yaml needs display_name")
    if not short_description or not 25 <= len(short_description) <= 64:
        errors.append("short_description must be 25-64 characters")
    if not default_prompt or f"${name}" not in default_prompt:
        errors.append("default_prompt must mention the skill with $skill-name")

    if errors:
        for error in errors:
            print(f"FAIL {error}")
        return 1
    print("Skill structure validation: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
