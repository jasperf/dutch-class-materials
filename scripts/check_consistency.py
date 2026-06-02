#!/usr/bin/env python3
"""
Consistency checks for a course quarter — catches the two drift modes that have
actually bitten this repo (stale session dates, README tables lagging renames).

It does NOT rewrite anything. The session-map tables carry editorial structure
(SKIPPED / MISSED / "S15 cont." rows, the S17a/S17b split) that no generator
should own — so this only *reports* disagreement and leaves the prose to you.

Run:  python3 scripts/check_consistency.py   (or: make check)
Exits non-zero if any drift is found, so it can gate a commit later if wanted.

Two checks:
  A. Date drift  — every session that has an email (emails/_generate.py SESSIONS)
     must carry the same date in lessons/<Q>/schedule.md. These are the two
     runbook-designated sources of truth (docs/new-quarter.md).
  B. Rename drift — every committed handout/test/teacher/reference markdown
     source must be referenced in a README table, and every filename mentioned
     in those tables must resolve to a real source file.
"""

import glob
import importlib.util
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}


def parse_date(text):
    """'20 April 2026' / '3 May' / 'Mon 20 Apr' -> (day, month) or None."""
    m = re.search(r"(\d{1,2})\s+([A-Za-z]{3,9})", text)
    if not m:
        return None
    day = int(m.group(1))
    month = MONTHS.get(m.group(2)[:3].lower())
    if month is None:
        return None
    return (day, month)


def load_sessions():
    """Import emails/_generate.py and return {code: 'date string'}."""
    path = os.path.join(ROOT, "emails", "_generate.py")
    spec = importlib.util.spec_from_file_location("_generate", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # SESSIONS tuple layout: (slug, date, day, time, code, title, unit, pages, topics)
    return {s[4]: s[1] for s in mod.SESSIONS}, mod.QUARTER


def parse_schedule_dates(quarter):
    """Return {code: 'date string'} from the schedule.md session-map table."""
    path = os.path.join(ROOT, "lessons", quarter, "schedule.md")
    if not os.path.exists(path):
        return None, path
    out = {}
    in_map = False
    with open(path) as f:
        for line in f:
            if line.startswith("## "):
                in_map = line.strip().lower().startswith("## session map")
                continue
            if not in_map or not line.lstrip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            code, date = cells[0], cells[1]
            # skip header/separator and non-session rows (— , "S15 cont.")
            if not re.fullmatch(r"S\d+", code):
                continue
            out.setdefault(code, date)  # first row wins; cont. rows are separate
    return out, path


def check_dates():
    problems = []
    sessions, quarter = load_sessions()
    schedule, sched_path = parse_schedule_dates(quarter)
    if schedule is None:
        return [f"schedule.md not found at {sched_path}"]
    for code, email_date in sessions.items():
        if code not in schedule:
            problems.append(
                f"{code}: in emails ({email_date!r}) but no matching row in schedule.md"
            )
            continue
        e, s = parse_date(email_date), parse_date(schedule[code])
        if e and s and e != s:
            problems.append(
                f"{code}: email says {email_date!r} but schedule.md says {schedule[code]!r}"
            )
    return problems


def check_renames():
    problems = []
    sources = []
    for pat in (
        "handouts/s*.md",
        "handouts/tests/*.md",
        "handouts/teacher/*.md",
        "handouts/teacher/student-questions/*.md",
        "handouts/references/*.md",
    ):
        sources += glob.glob(os.path.join(ROOT, pat))
    source_stems = {os.path.splitext(os.path.basename(p))[0] for p in sources}

    # Scan every README under handouts/ (the top-level table, the docx catalog,
    # and per-folder ones like references/README.md — the reference sheets' home).
    readme_text = ""
    for p in glob.glob(os.path.join(ROOT, "handouts", "**", "README.md"), recursive=True):
        with open(p) as f:
            readme_text += f.read() + "\n"

    # A. every source referenced somewhere in the README tables
    for stem in sorted(source_stems):
        if stem == "README":
            continue
        if stem not in readme_text:
            problems.append(f"handout source '{stem}.md' is in git but listed in no README table")

    # B. every *handout-like* filename mentioned in the READMEs resolves to a
    #    real source. Restrict to course-material names (sNN-…, reference-…) so
    #    plain doc cross-links (docs/pdf-export.md, new-quarter.md) aren't flagged.
    handout_like = re.compile(r"^(?:s\d+[a-z]?-|reference-)")
    referenced = set(re.findall(r"([A-Za-z0-9][\w-]*?)\.(?:md|docx)", readme_text))
    for stem in sorted(referenced):
        if stem in source_stems or not handout_like.match(stem):
            continue
        problems.append(f"README references '{stem}' but no matching source file exists")
    return problems


def main():
    sections = [
        ("Date drift (emails vs schedule.md)", check_dates),
        ("Rename drift (sources vs README tables)", check_renames),
    ]
    total = 0
    for title, fn in sections:
        problems = fn()
        total += len(problems)
        mark = "OK " if not problems else "!! "
        print(f"{mark}{title}")
        for p in problems:
            print(f"     - {p}")
    print()
    if total:
        print(f"{total} issue(s) found.")
        return 1
    print("All consistency checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
