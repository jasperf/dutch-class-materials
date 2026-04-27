# Handout Review Process

This document describes how to cross-check session handouts against the OCR'd book content to identify gaps and improve quality.

## Overview

Each session handout (`handouts/sNN-*.md`) covers a specific book unit. The book's OCR text lives in `books/ocr/`. The OCR was produced by Tesseract from PDFs, so the text is imperfect — use it to spot missing vocabulary and grammar, not as a verbatim source.

## Session → Unit → OCR File Mapping

| Session | Unit | Book pages | OCR file |
|---------|------|-----------|----------|
| S5  | 05 — Weet u de weg?                     | blz. 51–63   | `02_Lessons_01-10.md` |
| S6  | 06 — Leuke schoenen!                    | blz. 64–77   | `02_Lessons_01-10.md` |
| S7  | 07 — Mag ik een retourtje Wageningen?   | blz. 78–92   | `02_Lessons_01-10.md` |
| S8  | Units 1–7 review                        | blz. 78–92 (vervolg) | `02_Lessons_01-10.md` |
| S9  | 08 — Heeft u een leuke vakantie gehad?  | blz. 93–108  | `02_Lessons_01-10.md` |
| S10 | Midpoint review                         | —            | all |
| S11 | 09 — Ik heb bloemen voor je meegebracht | blz. 109–120 | `02_Lessons_01-10.md` |
| S12 | 10 — Vroeger                            | blz. 121–133 | `02_Lessons_01-10.md` |
| S13 | 10 vervolg — Simple past in depth       | blz. 121–133 | `02_Lessons_01-10.md` |
| S14 | 11 — Laten we naar Antwerpen gaan!      | blz. 134–151 | `03_Lessons_11-20.md` |
| S15 | 12 — Ik stuur je wel een sms-je         | blz. 152–173 | `03_Lessons_11-20.md` |
| S16 | 12 vervolg — Zouden + voorzetsels       | blz. 152–173 | `03_Lessons_11-20.md` |
| S17 | 13 — Ik weet echt niet wat ik wil       | blz. 174–192 | `03_Lessons_11-20.md` |
| S18 | 14 — Ik begrijp precies hoe je je voelt | blz. 193–208 | `03_Lessons_11-20.md` |
| S19 | 15–16 survey + revision                 | blz. 209–243 | `03_Lessons_11-20.md` |
| S20 | Final session                           | all          | all |

**Note:** OCR `## Pagina NN` numbers are the physical PDF page numbers, not the book's printed page numbers. Use keyword search to locate the right section.

## Step-by-Step Review

### 1. Read the handout

Open `handouts/sNN-*.md`. Note:
- Which unit and book page range it covers
- What leerdoelen (learning objectives) it lists
- What vocabulary tables it contains
- What grammar sections it covers
- Whether it has a dialogue section
- What homework is assigned

### 2. Find the unit in the OCR

Search the appropriate OCR file for distinctive words from the unit title or dialogue:

```bash
grep -n "key phrase from unit" books/ocr/02_Lessons_01-10.md
# e.g. for unit 05:
grep -n "Weet u de weg\|stoplichten\|parkeergarage" books/ocr/02_Lessons_01-10.md
```

Identify the `## Pagina` range that covers the unit (typically 3–5 OCR pages per unit).

### 3. Read the OCR content for that unit

```bash
sed -n 'START,ENDp' books/ocr/02_Lessons_01-10.md
```

Note the following from the OCR (ignoring OCR noise):
- **Key vocabulary words** — especially any not in the handout
- **Grammar rules or tables** — verb conjugations, spelling rules, etc.
- **Dialogue phrases** — market phrases, travel phrases, etc.
- **Exercise topics** — what skills the book practises

### 4. Cross-check vocabulary

Compare the handout's vocabulary tables against the OCR. Flag words that:
- Are in the book but **missing from the handout**
- Are in the handout but phrased differently than the book (minor: only fix if genuinely confusing)

Focus on the most common/useful words. Don't aim for 100% coverage — handouts are curated, not exhaustive.

### 5. Cross-check grammar

Compare grammar sections. Flag:
- Grammar points covered in the book but **absent from the handout**
- Grammar rules stated incorrectly or incompletely
- Missing examples

### 6. Check the dialogue section

Verify:
- Does the handout reference or quote the book's main dialogue?
- Are key phrases from the dialogue captured in the vocabulary tables?

### 7. Check homework alignment

Does the homework assignment match the book's suggested exercises or extend logically from the unit content?

### 8. Write up gaps

For each handout, note gaps in a short list:
- Missing vocabulary (with Dutch term and English gloss)
- Missing grammar points
- Dialogue phrases not captured
- Suggested improvements

### 9. Update the handout

Edit the handout file to fill confirmed gaps. Keep additions concise — the handout is a teaching aid, not a textbook chapter.

### 10. Commit

One commit per session handout updated. Commit message format:

```
Update SNN handout: add missing vocabulary/grammar from unit NN
```

## What the OCR Can and Cannot Tell You

**Can:** spot vocabulary words present in the book, identify grammar topics covered, find dialogue phrases.

**Cannot:** reliably reproduce tables, exercise numbering, or heavily formatted sections — these appear garbled. When the OCR is unclear, the handout content takes precedence unless there is strong evidence of a gap.

## Reference: Previously Reviewed

| Session | Commit | Notes |
|---------|--------|-------|
| S4 | `b03759f` | Added pronouns, expanded vocabulary, market phrases, new test |
