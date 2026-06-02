# Setting Up a New Course Quarter

This runbook explains how to spin up a new course quarter from the existing
materials. The textbook never changes (Quist & Strik, 16 units), so the
*teaching content* (handouts, tests, lesson-plan bodies) is fully reusable —
only the **dates** and **session numbers** differ each quarter.

There are two ways to do it. Pick based on how often you expect to reuse:

| Path | What it is | When to use |
|------|-----------|-------------|
| **A — Copy & re-date** | Copy the quarter folder, keep session-numbered files (`s15-…`, `**Datum:**`), update every date by hand | One-off, or you like session numbers in filenames |
| **B — Refactor to unit-based, date-free content** | One-time refactor so handouts/tests carry **no session number and no date** — only the unit. After that, a new quarter = edit `schedule.md` + the email dates and regenerate. Nothing else moves. | You'll run this course repeatedly and want each future setup to take minutes |

> **Important:** Do **not** apply Path B to a quarter that is currently running.
> Students are anchored to session numbers (S15, S16…) and may already have
> docx/Google-Docs named that way. Leave the running quarter as its faithful,
> session-numbered archive. Adopt Path B only when starting a fresh quarter.

---

## Where dates & session numbers are embedded

This is the map of everything that is quarter-specific. It's also the list that
drifted out of sync this quarter, so treat it as the pre-flight checklist for
either path.

| Location | What's quarter-specific |
|----------|-------------------------|
| `lessons/<Q>/schedule.md` | Session map (dates), finish date, progress tracker, grammar progression |
| `lessons/<Q>/README.md` | Period, total duration (weeks), week range |
| `lessons/<Q>/week-XX/lesson-plan.md` | Per-session dates, session numbers, agendas |
| `emails/<Q>/sNN-email.md` | Generated — date + session content (don't hand-edit; regenerate) |
| `emails/_generate.py` | `QUARTER` + the `SESSIONS` list (dates, codes, titles, units, pages, topics) — **single source for emails** |
| `handouts/sNN-*.md` | Filename (session number), `# Handout SNN` heading, `**Datum:**` line |
| `handouts/tests/sNN-test-*.md` | Filename, heading, any date line |
| `handouts/docx/**` | Gitignored — regenerated from markdown, never hand-edited |
| `handouts/README.md`, `handouts/docx/README.md` | Session-list tables |
| `docs/handout-review-process.md` | Session → unit → OCR-file mapping table |
| `README.md` (root) | "Current course" block, session-map quick reference, directory tree |

Lesson: every date or session number that lives in **more than one** file is a
drift risk. Path B exists to collapse those into one source (`schedule.md` +
`_generate.py`).

---

## Path A — Copy & re-date (pragmatic, keeps session numbers)

1. **Copy the lessons folder**
   ```bash
   cp -r lessons/2026-Q2_Apr-Jun lessons/YYYY-Q#_MMM-MMM
   ```
2. **Reset the schedule** — in `lessons/YYYY-Q#_MMM-MMM/schedule.md` update the
   first-session date, the whole session map (dates), total hours / finish date,
   the progress tracker, and the header notes. This is the source of truth; get
   it right first.
3. **Clear or re-date the lesson plans** — either reset each `week-XX/lesson-plan.md`
   from the template, or update the dates/session headers in place:
   ```bash
   for d in lessons/YYYY-Q#_MMM-MMM/week-*/; do
     cp lessons/templates/lesson-plan-template.md "$d/lesson-plan.md"
   done
   ```
4. **Reuse handouts & tests as-is** — same units, same content. Update the
   `**Datum:**` line at the top of each handout/test to the new session dates.
5. **Regenerate emails** — edit `emails/_generate.py` (`QUARTER` + `SESSIONS`
   dates) and run it (see *Regenerate artifacts* below).
6. **Update the READMEs** — root `README.md` ("Current course" + session map +
   directory tree), `lessons/<Q>/README.md`, both handout README tables, and the
   `docs/handout-review-process.md` mapping if session→unit changed.
7. **Add a diaries folder** for the new year if needed: `mkdir -p diaries/YYYY`.
8. **Regenerate docx** (see below).

Cost: a couple of hours, mostly mechanical re-dating across the files above.

---

## Path B — Refactor to unit-based, date-free content (fast forever after)

Do this **once**, when starting a fresh quarter. Afterwards every new quarter is
a `schedule.md` + email-dates edit and a regenerate — no file renames, no
header re-dating.

### The convention

- **Handouts and tests are named by unit, not session**, and carry **no date**:
  - `handouts/unit-11-laten-we-naar-antwerpen-gaan.md`
  - `handouts/tests/unit-11-test-laten-we-naar-antwerpen-gaan.md`
  - Non-unit sessions get stable descriptive slugs: `review-units-1-7.md`,
    `midpoint-review.md`, `final-session.md`.
- **Headings drop the session number**: `# Handout — Unit 11: …` (not `# Handout S15`).
- **Remove the `**Datum:**` line** from handout/test bodies. Keep only stable
  fields: `**Unit:**`, `**Boek:**` (book pages), `**Duur:**`.
- **`schedule.md` becomes the single mapping** of *session → date → unit(s) → handout*.
  It's the only place a session number meets a date.

### One-time refactor steps

1. **Rename handouts and tests by unit** (use `git mv` so history follows):
   ```bash
   git mv handouts/s15-laten-we-naar-antwerpen-gaan.md handouts/unit-11-laten-we-naar-antwerpen-gaan.md
   # …repeat per handout; map the session-named files to their unit
   git mv handouts/tests/s15-test-laten-we-naar-antwerpen-gaan.md handouts/tests/unit-11-test-laten-we-naar-antwerpen-gaan.md
   ```
2. **Strip session numbers and dates from the bodies** — change `# Handout SNN —`
   to `# Handout — Unit NN:` and delete the `**Datum:**` line in every handout and test.
3. **Update both handout README tables** so the "Filename" column is unit-based
   and drop the date/session coupling (keep a "Typically taught in" note pointing
   at `schedule.md` rather than a fixed session).
4. **Make `schedule.md` the source of truth** — its session map already lists
   *session → date → unit → pages*. Keep it; everything else references it.
5. **Decide on lesson plans (optional, heavier):** the cleanest end-state is to
   organise lesson-plan *content* by unit too (e.g. `lessons/units/unit-11.md`
   holding objectives/agenda/vocab) and keep only the dated week-by-week skeleton
   in `lessons/<Q>/`. If that's too much, just strip embedded dates from the
   week files and let `schedule.md` hold the dates. You can defer this and still
   get most of the benefit from the handout/test refactor alone.
6. **Keep emails generated** — `emails/_generate.py` already centralises dates in
   its `SESSIONS` list. That's the right model; leave it. Emails are inherently
   date-specific, so dates belong there, not in reusable content.

### Each new quarter *after* the refactor

1. Copy `lessons/<old-Q>` → `lessons/<new-Q>`, edit `schedule.md` dates + the
   session→unit mapping.
2. Edit `emails/_generate.py` (`QUARTER` + `SESSIONS` dates) and run it.
3. Regenerate docx.
4. Handouts and tests need **no changes** — they're unit-keyed and date-free.

That's the payoff: the renumber/re-date scramble that this quarter's holiday
caused becomes a single edit to `schedule.md`.

---

## Regenerate artifacts

**Emails** — after editing `emails/_generate.py`:
```bash
python3 emails/_generate.py
```

**DOCX** (gitignored; regenerate from markdown — requires `pandoc`):
```bash
# Session handouts
for f in handouts/*.md; do pandoc "$f" -o "handouts/docx/$(basename "${f%.md}").docx"; done
# Tests
for f in handouts/tests/*.md; do pandoc "$f" -o "handouts/docx/tests/$(basename "${f%.md}").docx"; done
```
After renaming markdown, delete any orphaned old-named docx so the export folder
doesn't accumulate stale files.

---

## Gotchas (learned the hard way)

- **`_generate.py` drifts silently.** If you renumber email files by hand but
  forget the `SESSIONS` list, the next `python3 emails/_generate.py` overwrites
  your files with stale dates. Always update the generator, not just the output.
- **READMEs lag behind renames.** Both handout README tables, the root README
  session map, and `docs/handout-review-process.md` carry session lists that are
  easy to forget. They're in the pre-flight map above for a reason.
- **Skipped / missed sessions break 1:1 numbering.** A skipped session (like
  S14 this quarter) or a holiday gap means session numbers no longer line up with
  units. Path B sidesteps this entirely — units don't care which session they land in.
- **Don't renumber a running course toward units.** See the warning at the top:
  it desyncs the materials students already hold.
