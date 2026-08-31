#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re
import sys

TEXT_SUFFIXES = {".md", ".yaml", ".yml", ".json", ".py", ".txt", ".toml"}
FORBIDDEN_SUFFIXES = {".db", ".sqlite", ".sqlite3"}
FORBIDDEN_DIR_NAMES = {"private-data", "runtime-data", "real-health-data"}

PATTERNS = {
    "github_token": re.compile(r"(?:ghp_|github_pat_)[A-Za-z0-9_\-]{12,}"),
    "openai_key": re.compile(r"sk-[A-Za-z0-9_\-]{16,}"),
    "bearer_token": re.compile(r"Bearer\s+[A-Za-z0-9._\-]{20,}", re.IGNORECASE),
    "cn_mobile": re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)"),
    "cn_id": re.compile(r"(?<!\d)\d{17}[0-9Xx](?!\d)"),
    "absolute_user_path": re.compile(r"(?:/Users/|/home/)[^\s`'\"]+"),
}

ALLOWLIST_SUBSTRINGS = {
    "tests/test_repository_contract.py",
    "scripts/scan_public_content.py",
}


def scan_repository(root: Path) -> list[str]:
    root = Path(root)
    findings: list[str] = []

    for path in root.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()

        if any(part in FORBIDDEN_DIR_NAMES for part in path.parts):
            findings.append(f"{rel}: forbidden private/runtime data directory")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            findings.append(f"{rel}: forbidden database artifact in public repository")

        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"AGENTS.md", "README.md", "README-CANDIDATE.md"}:
            continue

        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"{rel}: non-UTF8 content requires explicit review")
            continue

        if rel in ALLOWLIST_SUBSTRINGS:
            # Scanner/test source necessarily contains detection regex examples.
            continue

        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{rel}: possible sensitive content ({label})")

    return findings


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    findings = scan_repository(root)
    if findings:
        print("F0.1 PUBLIC PRIVACY SCAN: FAIL")
        for finding in findings:
            print(f"- {finding}")
        return 1
    print("F0.1 PUBLIC PRIVACY SCAN: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
