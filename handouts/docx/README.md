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
| S14 | s14-laten-we-naar-antwerpen-gaan.docx | Suggestions, likes | 11 |
| S15 | s15-ik-stuur-je-wel-een-sms-je.docx | Phone, zou(den) | 12 |
| S16 | s16-zouden-in-depth.docx | Conditionals, prepositions | 12 |
| S17 | s17-ik-weet-echt-niet-wat-ik-wil.docx | Career, clauses | 13 |
| S18 | s18-ik-begrijp-precies-hoe-je-je-voelt.docx | Health, emotions | 14 |
| S19 | s19-units-15-16-survey.docx | Internet, media, revision | 15–16 |
| S20 | s20-final-session.docx | Final test + feedback | — |

---

## Generating / Updating DOCX Files

DOCX files are generated from the markdown source files.

### Single file (from project root):
```bash
pandoc handouts/s1-hallo-kom-binnen.md -o handouts/docx/s1-hallo-kom-binnen.docx
```

### All files (from project root):
```bash
for f in handouts/*.md; do
  base=$(basename "$f" .md)
  pandoc "$f" -o "handouts/docx/${base}.docx"
done
```

### Requirements
- [Pandoc](https://pandoc.org/) installed (`brew install pandoc`)
- See [../../docs/pdf-export.md](../../docs/pdf-export.md) for installation instructions

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
