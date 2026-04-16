# Dutch Class Materials

Personal archive of materials for Dutch language instruction (2023–present).

---

## Directory structure

```
dutch-class/
├── admin/                 # Private — gitignored (contracts, receipts, bank scans)
├── books/                 # Gitignored (copyrighted — not distributed)
├── diaries/               # Gitignored (may contain personal information)
├── handouts/              # Student-facing handout materials
├── lessons/
│   ├── 2026-Q2_Apr-Jun/          # Active course (Apr–Jun 2026)
│   │   ├── README.md             # Quarter overview and quick links
│   │   ├── schedule.md           # Full 20-session schedule with dates, units, and topics
│   │   └── week-01/ … week-10/   # Per-week lesson plans (two sessions each, full content)
│   └── templates/
│       └── lesson-plan-template.md
└── notes/
    └── teaching-notes.md  # Course overview and PDF split map
```

> **Note on the PDF:** The textbook is a scanned image (two book pages per PDF page).
> PDF page numbers ≠ book page numbers. Lesson plans reference **book page numbers**.

---

## Textbook — unit overview

*Dutch* by Gerdi Quist & Dennis Strik — Teach Yourself series (2003)

> The textbook is not included in this repository (copyrighted). Search for
> **"Teach Yourself Dutch Quist Strik"** on Amazon, AbeBooks, or your local
> bookshop. Second-hand copies are widely available.

| Unit | Dutch title | English | Book pp |
|------|------------|---------|---------|
| — | Pronunciation | — | xi |
| 01 | hallo, kom binnen! | hello, come in! | 1 |
| 02 | wat doe je? | what do you do? | 11 |
| 03 | waar woon je? | where do you live? | 21 |
| 04 | de boodschappen | groceries | 37 |
| 05 | weet u de weg? | do you know the way? | 51 |
| 06 | leuke schoenen! | nice shoes! | 64 |
| 07 | mag ik een retourtje Wageningen? | may I have a return to Wageningen? | 78 |
| 08 | heeft u een leuke vakantie gehad? | did you have a nice holiday? | 93 |
| 09 | ik heb bloemen voor je meegebracht | I've brought you flowers | 109 |
| 10 | vroeger | in the past | 121 |
| 11 | laten we naar Antwerpen gaan | let's go to Antwerp | 134 |
| 12 | ik stuur je wel een sms-je | I'll send you a text | 152 |
| 13 | ik weet echt niet wat ik wil | I really don't know what I want | 174 |
| 14 | ik begrijp precies hoe je je voelt | I know exactly how you feel | 193 |
| 15 | ik zit zowat de hele dag te computeren | I'm on the computer all day | 209 |
| 16 | tv wordt steeds banaler | tv is becoming more and more banal | 224 |
| — | Key to exercises | — | 244 |
| — | Appendix + glossaries | — | 262 |

---

## Current course — April–June 2026

- **Period:** Wed 22 Apr – Sun 28 Jun 2026
- **Total hours:** 40 (20 sessions × 2 hrs)
- **Pattern:** Wednesday + Sunday, 2 hrs each
- **Spare session:** Wed 1 Jul (buffer if a session is missed)
- **Main textbook:** *Dutch* — Gerdi Quist & Dennis Strik (Teach Yourself)
- **Full schedule:** `lessons/2026-Q2_Apr-Jun/schedule.md`

### Session map (quick reference)

| Sessions | Dates | Unit(s) | Topic |
|----------|-------|---------|-------|
| S1 | Wed 22 Apr | Pronunciation + 01 | Introductions, greetings |
| S2 | Sun 26 Apr | 02 | Jobs, family, languages |
| S3 | Wed 29 Apr | 03 | Housing, neighbourhood |
| S4 | Sun 3 May | 04 | Groceries, shopping |
| S5 | Wed 6 May | 05 | Directions |
| S6 | Sun 10 May | 06 | Clothes, colours, opinions |
| S7 | Wed 13 May | 07 | Transport, buying tickets |
| S8 | Sun 17 May | 07 cont. + review | Time, separable verbs, Units 1–7 review |
| S9 | Wed 20 May | 08 | Past tense (perfect), holidays |
| S10 | Sun 24 May | — | Midpoint review |
| S11 | Wed 27 May | 09 | Invitations, dinner, zullen |
| S12 | Sun 31 May | 10 | Times, simple past (imperfect) |
| S13 | Wed 3 Jun | 10 cont. | Simple past in depth, vroeger |
| S14 | Sun 7 Jun | 11 | Suggestions, likes/dislikes |
| S15 | Wed 10 Jun | 12 | Phone calls, zouden |
| S16 | Sun 14 Jun | 12 cont. | Conditionals, prepositions |
| S17 | Wed 17 Jun | 13 | Subordinate clauses, career |
| S18 | Sun 21 Jun | 14 | Health, emotions, reflexive verbs |
| S19 | Wed 24 Jun | 15–16 survey + revision | Overview + full grammar review |
| S20 | Sun 28 Jun | — | Final conversation test + feedback |

---

## Adding a new course quarter

### 1. Copy the quarter folder

```bash
cp -r lessons/2026-Q2_Apr-Jun lessons/YYYY-Q#_MMM-MMM
```

Replace `YYYY-Q#_MMM-MMM` with the new period, e.g. `2027-Q1_Jan-Mar`.

### 2. Reset the schedule

Open `lessons/YYYY-Q#_MMM-MMM/schedule.md` and update:
- **First session date** and session pattern (Wed/Sun or whatever applies)
- **All session dates** in the session table
- **Total hours / finish date**

### 3. Clear lesson plan content

Each `week-XX/lesson-plan.md` contains content specific to the 2026 course.
Either clear the body of each file back to the blank template, or regenerate from
`lessons/templates/lesson-plan-template.md`:

```bash
for d in lessons/YYYY-Q#_MMM-MMM/week-*/; do
  cp lessons/templates/lesson-plan-template.md "$d/lesson-plan.md"
done
```

### 4. Update this README

- Change the **Current course** section (dates, period, schedule path).
- Replace the **Session map** table with the new session dates.

### 5. Add a diaries folder for the new year (if needed)

```bash
mkdir -p diaries/YYYY
```

### 6. File handouts

Put any new student-facing materials under `handouts/` as you prepare each session.
