# Dutch Course Handouts

This directory contains **markdown handouts** for each session of the Dutch language course (Q2 2026).

## Structure

```
handouts/
├── README.md                    # This file
├── s01-hallo-kom-binnen.md      # Session 1 handout (markdown)
├── s02-wat-doe-je.md           # Session 2 handout (markdown)
├── s03-waar-woon-je.md         # Session 3 handout (markdown)
├── ...
└── docx/                       # DOCX versions for Google Docs
    ├── .gitignore
    ├── README.md
    ├── s01-hallo-kom-binnen.docx
    ├── s02-wat-doe-je.docx
    └── ...
```

## Session List (20 sessions)

| # | Filename | Topic | Unit | Book pp. |
|---|----------|-------|------|----------|
| S1 | s1-hallo-kom-binnen.md | Pronunciation + Introductions | 01 | xi + 1–10 |
| S2 | s2-wat-doe-je.md | Family, jobs, nationality | 02 | 11–20 |
| S3 | s3-waar-woon-je.md | Housing, neighbourhood | 03 | 21–36 |
| S4 | s4-de-boodschappen.md | Shopping, groceries | 04 | 37–50 |
| S5 | s5-weet-u-de-weg.md | Directions, places in town | 05 | 51–63 |
| S6 | s6-leuke-schoenen.md | Clothing, opinions | 06 | 64–77 |
| S7 | s7-mag-ik-een-retourtje-wageningen.md | Transport, telling time | 07 | 78–92 |
| S8 | s8-units-1-7-review.md | Week 1–3 Review | — | — |
| S9 | s9-heeft-u-een-leuke-vakantie-gehad.md | Past tense, holidays | 08 | 93–108 |
| S10 | s10-midpoint-review.md | Midpoint Review | — | — |
| S11 | s11-ik-heb-bloemen-voor-je-meegebracht.md | Invitations, dinner | 09 | 109–120 |
| S12 | s12-vroeger.md | Past habits, time | 10 | 121–133 |
| S13 | s13-simple-past-in-depth.md | Imperfect tense | 10 | 121–133 |
| S14 | s14-laten-we-naar-antwerpen-gaan.md | Suggestions, likes | 11 | 134–151 |
| S15 | s15-ik-stuur-je-wel-een-sms-je.md | Phone, zou(den) | 12 | 152–173 |
| S16 | s16-zouden-in-depth.md | Conditionals, prepositions | 12 | 152–173 |
| S17 | s17-ik-weet-echt-niet-wat-ik-wil.md | Career, clauses | 13 | 174–192 |
| S18 | s18-ik-begrijp-precies-hoe-je-je-voelt.md | Health, emotions | 14 | 193–208 |
| S19 | s19-units-15-16-survey.md | Internet, media, revision | 15–16 | 209–243 |
| S20 | s20-final-session.md | Final test + feedback | — | — |

## Usage

### Markdown Version
- **Editable**: Use in any markdown editor (Obsidian, VS Code, Typora)
- **Version control**: Commit the `.md` files to git
- **Quick search**: Use `grep` or `ripgrep` to search across all handouts

### DOCX Version
See [handouts/docx/README.md](docx/README.md) for DOCX files that can be imported into Google Docs.

## Generating DOCX

```bash
# Convert all markdown handouts to DOCX
cd handouts
for f in *.md; do
  pandoc "$f" -o "docx/${f%.md}.docx"
done
```

Requires: `pandoc` (see [docs/pdf-export.md](../../docs/pdf-export.md))

## Handout Structure

Each handout contains:
- Date, unit, book pages, duration
- Learning objectives (✅ checklist)
- Vocabulary (Dutch/English table)
- Grammar explanation + examples
- Lesson plan (time breakdown)
- Homework assignments

## Preparation for Class

1. Print the DOCX version or open in Google Docs
2. Add notes in the "Lesson plan" section
3. Use the vocabulary table as a reference during class
