#!/usr/bin/env python3
"""The cross-repository figures gate.

This site states manifest-identity's test and decision counts.
manifest-identity counts them with a test of its own (its D-031 and the
figures rule), but the copy here was typed by hand and went stale
twice in a month. This reads manifest-identity's README on main and
refuses a mismatch; with --fix it rewrites the figures here to match.

The test count is stated as a floor, "more than 400 tests", because
the exact count moves with every pull request that adds a test, and a
site that had to be pushed for each of those was stale within the hour
of being fixed. The floor is the round hundred at or below the count,
so the sentence stays true and stays close; the decisions count is
stated exactly, because it moves rarely and is worth its number.
"""
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = "https://raw.githubusercontent.com/manifest-identity/manifest-identity/main/README.md"
STATED = re.compile(r"more than (\d+) tests, (\d+) recorded(\s+)decisions")
FILES = ["README.md", "index.html"]
STEP = 100


def source_figures() -> tuple[int, int]:
    with urllib.request.urlopen(SOURCE, timeout=30) as response:  # noqa: S310  (https, fixed host)
        text = response.read().decode()
    tests = re.search(r"\*\*(\d+) tests in \d+ files\*\*", text)
    decisions = re.search(r"\*\*(\d+) recorded decisions\*\*", text)
    if not tests or not decisions:
        print("manifest-identity's README no longer states its figures in the expected form")
        raise SystemExit(2)
    return int(tests.group(1)), int(decisions.group(1))


def floor_for(tests: int) -> int:
    return (tests // STEP) * STEP


def main() -> int:
    fix = "--fix" in sys.argv
    tests, decisions = source_figures()
    floor = floor_for(tests)
    failures = 0
    for name in FILES:
        path = ROOT / name
        text = path.read_text()
        found = STATED.search(text)
        if not found:
            print(f"{name}: states no figures in the expected form")
            failures += 1
            continue
        stated = (int(found.group(1)), int(found.group(2)))
        if stated == (floor, decisions):
            continue
        if fix:
            new = STATED.sub(
                lambda m: f"more than {floor} tests, {decisions} recorded{m.group(3)}decisions",
                text, count=1,
            )
            path.write_text(new)
            print(f"{name}: more than {stated[0]} tests, {stated[1]} decisions -> {floor}, {decisions}")
        else:
            print(
                f"{name}: states more than {stated[0]} tests and {stated[1]} decisions; "
                f"manifest-identity reports {tests} tests (floor {floor}) and {decisions}"
            )
            failures += 1
    if failures and not fix:
        return 1
    print(f"figures match manifest-identity: more than {floor} tests ({tests}), {decisions} decisions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
