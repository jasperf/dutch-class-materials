# Pre-class Emails

This directory contains emails sent to students before each session of the Dutch course.
Each quarter has its own subdirectory matching the `lessons/` naming convention.

## Structure

```
emails/
├── README.md              ← this file
├── _template.md           ← blank template for a one-off or new quarter
├── _generate.py           ← script to regenerate all emails for a quarter
└── 2026-Q2_Apr-Jun/       ← Q2 2026 (20 Apr – 4 Jun)
    ├── s01-email.md       ← 20 Apr 2026
    ├── s02-email.md       ← 23 Apr 2026
    ├── ...
    └── s20-email.md       ← 4 Jun 2026
```

## Format

Each email:
- Opens with `Dear Students,` and the Google Meet link
- States the date, day and time of the session
- Gives a short summary of what will be covered
- Notes which book pages to have open

## Before sending

1. Open the relevant `sXX-email.md`
2. Replace `[GOOGLE_MEET_URL]` with the session's Google Meet link
3. Adjust the bullet summary if the lesson plan has changed
4. Copy the body into your email client and send

## Generating emails for a new quarter

Edit `_generate.py` — update `QUARTER` and the `SESSIONS` list — then run:

```bash
python3 emails/_generate.py
```

New files will be written to `emails/<QUARTER>/`.
