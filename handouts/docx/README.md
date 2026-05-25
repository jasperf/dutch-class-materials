# Dutch Course Handouts — DOCX Version

This directory contains **DOCX versions** of all handouts, ready for import into **Google Docs**.

> ⚠️ **Git Ignore**: DOCX files are **not** committed to git (see `.gitignore`).
> The markdown source files are in [../](..)

## Quick Import into Google Docs

### Method 1: Drag & Drop (Recommended)
1. Go to [docs.google.com](https://docs.google.com)
2. Drag the `.docx` file **directly** into your browser
3. Files open **automatically** as a Google Document, preserving:
   - Headings
   - Tables
   - Lists
   - Bold/italic

### Method 2: Via Google Drive
1. Go to [drive.google.com](https://drive.google.com)
2. Click **"New" → "File upload"**
3. Select the `.docx` file
4. Double-click to open in Google Docs

### Method 3: Via Google Docs Menu
1. Go to [docs.google.com](https://docs.google.com)
2. Click the **folder icon** ("Open file picker")
3. Go to the **"Upload"** tab
4. Select your `.docx` file

---

## File List

### Session handouts

| # | DOCX Filename | Topic | Unit |
|---|---------------|-------|------|
| S1 | s1-hallo-kom-binnen.docx | Pronunciation + Introductions | 01 |
| S2 | s2-wat-doe-je.docx | Family, jobs, nationality | 02 |
| S3 | s3-waar-woon-je.docx | Housing, neighbourhood | 03 |
| S4 | s4-de-boodschappen.docx | Shopping, groceries | 04 |
| S5 | s5-weet-u-de-weg.docx | Directions, places | 05 |
| S6 | s6-leuke-schoenen.docx | Clothing, opinions | 06 |
| S7 | s7-mag-ik-een-retourtje-wageningen.docx | Transport, time | 07 |
| S8 | s8-units-1-7-review.docx | Week 1–3 Review | — |
| S9 | s9-heeft-u-een-leuke-vakantie-gehad.docx | Past tense, holidays | 08 |
| S10 | s10-midpoint-review.docx | Midpoint Review | — |
| S11 | s11-ik-heb-bloemen-voor-je-meegebracht.docx | Invitations, dinner | 09 |
| S12 | s12-vroeger.docx | Past habits, time | 10 |
| S13 | s13-simple-past-in-depth.docx | Imperfect tense | 10 |
| S15 | s15-laten-we-naar-antwerpen-gaan.docx | Suggestions, likes, reflexive verbs | 11 |
| S16 | s16-ik-stuur-je-wel-een-sms-je.docx | Phone, zou(den) | 12 |
| S17 | s17-zouden-in-depth.docx | Conditionals, prepositions | 12 |
| S18 | s18-ik-weet-echt-niet-wat-ik-wil.docx | Career, clauses | 13 |
| S19 | s19-ik-begrijp-precies-hoe-je-je-voelt.docx | Health, emotions | 14 |
| S20 | s20-units-15-16-survey.docx | Internet, media, revision | 15–16 |
| S21 | s21-final-session.docx | Final test + feedback | — |

### Reference sheets (`references/`)

| Filename | Description |
|----------|-------------|
| references/reference-numbers-10-100.docx | Numbers 10–100 in Dutch |
| references/reference-je-jij-jou.docx | Je / Jij / Jou — tweede persoon enkelvoud |
| references/reference-bijvoeglijke-naamwoorden.docx | Bijvoeglijke naamwoorden — de -e regel |

### Teacher materials (`teacher/`)

| Filename | Session | Description |
|----------|---------|-------------|
| teacher/s8-luistertoets-leraar.docx | S8 | Listening script + answer key (directions/shopping) |
| teacher/s9-luistertoets-leraar.docx | S9 | Listening script + answer key (vacation/holidays) |
| teacher/s10-luistertoets-leraar.docx | S10 | Listening script + full answer key for midpoint test |
| teacher/s12-luistertoets-leraar.docx | S12 | Listening script + answer key (past tense/vroeger) |

### Teacher materials — Student questions (`teacher/student-questions/`)

| Filename | Session | Description |
|----------|---------|-------------|
| teacher/student-questions/s8-luistertoets-student.docx | S8 | Student worksheet — listening + exercises |
| teacher/student-questions/s9-luistertoets-student.docx | S9 | Student worksheet — listening + exercises |
| teacher/student-questions/s12-luistertoets-student.docx | S12 | Student worksheet — listening + exercises |
| teacher/student-questions/s16-icebreaker-weekend.docx | S16 | Icebreaker — weekend conversation questions (vrijdag + zaterdag) |

### Tests (`tests/`)

| Filename | Session | Topic |
|----------|---------|-------|
| s1-test-hallo-kom-binnen.docx | S1 | Pronunciation, introductions, zijn |
| s2-test-wat-doe-je.docx | S2 | Family, jobs, hebben, inversion |
| s3-test-waar-woon-je.docx | S3 | Housing, de/het, er is/zijn |
| s4-test-de-boodschappen.docx | S4 | Shopping, quantities, modals |
| s5-test-weet-u-de-weg.docx | S5 | Directions, imperatives |
| s6-test-leuke-schoenen.docx | S6 | Clothing, adjectives, opinions |
| s7-test-retourtje-wageningen.docx | S7 | Transport, separable verbs, time |
| s8-test-herhaling-units-1-7.docx | S8 | Review Units 1–7 |
| s9-test-heeft-u-een-leuke-vakantie-gehad.docx | S9 | Perfect tense, holidays |
| s10-test-midpunt-toets-units-1-8.docx | S10 | **Midpoint test — Units 01–08 (2 hr)** |
| s11-test-ik-heb-bloemen-voor-je-meegebracht.docx | S11 | Invitations, separable verbs, om + te |
| s15-test-laten-we-naar-antwerpen-gaan.docx | S15 | Suggestions, reflexive verbs, laten, vergelijkingen |

---

## Generating / Updating DOCX Files

DOCX files are generated from the markdown source files using [Pandoc](https://pandoc.org/).
All commands are run from the **project root**.

### Requirements
- Pandoc installed: `brew install pandoc`
- See [../../docs/pdf-export.md](../../docs/pdf-export.md) for full install instructions

---

### Session handouts

Single file:
```bash
pandoc handouts/s1-hallo-kom-binnen.md -o handouts/docx/s1-hallo-kom-binnen.docx
```

All session handouts at once:
```bash
for f in handouts/s*.md; do
  base=$(basename "$f" .md)
  pandoc "$f" -o "handouts/docx/${base}.docx"
done
```

---

### Tests

Single test:
```bash
pandoc handouts/tests/s1-test-hallo-kom-binnen.md -o handouts/docx/tests/s1-test-hallo-kom-binnen.docx
```

All tests at once:
```bash
for f in handouts/tests/*.md; do
  base=$(basename "$f" .md)
  pandoc "$f" -o "handouts/docx/tests/${base}.docx"
done
```

---

### Teacher materials

Single file:
```bash
pandoc handouts/teacher/s10-luistertoets-leraar.md -o handouts/docx/teacher/s10-luistertoets-leraar.docx
```

All teacher materials at once:
```bash
for f in handouts/teacher/*.md; do
  base=$(basename "$f" .md)
  pandoc "$f" -o "handouts/docx/teacher/${base}.docx"
done
```

### Teacher student questions

Single file:
```bash
pandoc handouts/teacher/student-questions/s8-luistertoets-student.md -o handouts/docx/teacher/student-questions/s8-luistertoets-student.docx
```

All student questions at once:
```bash
for f in handouts/teacher/student-questions/*.md; do
  base=$(basename "$f" .md)
  pandoc "$f" -o "handouts/docx/teacher/student-questions/${base}.docx"
done
```

---

### Reference sheets

Single file:
```bash
pandoc handouts/references/reference-je-jij-jou.md -o handouts/docx/references/reference-je-jij-jou.docx
```

All reference sheets at once:
```bash
for f in handouts/references/reference-*.md; do
  pandoc "$f" -o "handouts/docx/references/$(basename ${f%.md}).docx"
done
```

---

### Everything at once

```bash
# Session handouts
for f in handouts/s*.md; do
  pandoc "$f" -o "handouts/docx/$(basename ${f%.md}).docx"
done

# Tests
for f in handouts/tests/*.md; do
  pandoc "$f" -o "handouts/docx/tests/$(basename ${f%.md}).docx"
done

# Reference sheets
for f in handouts/references/reference-*.md; do
  pandoc "$f" -o "handouts/docx/references/$(basename ${f%.md}).docx"
done
```

---

## Formatting Preserved

Pandoc preserves the following formatting on conversion:
- ✅ **Headings** (H1–H6)
- ✅ **Tables** (with borders)
- ✅ **Lists** (numbered/unordered)
- ✅ **Bold/Italic**
- ✅ **Code blocks** (for commands)
- ✅ **Horizontal rules** (---)

---

## Source Files

The **markdown source files** are in [../](..):
- Are committed to git
- Can be edited in any text editor
- Contain the most recent version

Use the markdown files for:
- Version control and collaboration
- Search and replace
- Generating a fresh DOCX version

---

## Troubleshooting

If formatting is incorrect in Google Docs:
1. Check that the file has a `.docx` extension
2. Try a different browser
3. Upload manually via Google Drive
4. Check that Pandoc is up to date
