# Reference Sheets

Standalone grammar and vocabulary reference sheets for use alongside the session handouts.
These are not tied to a single session — they can be handed out any time the topic comes up.

## Contents

| File | Topic | Related session |
|------|-------|-----------------|
| [reference-numbers-10-100.md](reference-numbers-10-100.md) | Numbers 10–100 | S2 (getallen 0–20), S4 (boodschappen) |
| [reference-je-jij-jou.md](reference-je-jij-jou.md) | Je / Jij / Jou — tweede persoon enkelvoud | S1–S2 (eerste lessen) |
| [reference-bijvoeglijke-naamwoorden.md](reference-bijvoeglijke-naamwoorden.md) | Bijvoeglijke naamwoorden — de -e regel | S6 (leuke schoenen) |

## DOCX versions

DOCX exports are in [`../docx/references/`](../docx/references/).

Generate or update a single file:
```bash
pandoc handouts/references/reference-bijvoeglijke-naamwoorden.md \
  -o handouts/docx/references/reference-bijvoeglijke-naamwoorden.docx
```

Regenerate all:
```bash
for f in handouts/references/reference-*.md; do
  pandoc "$f" -o "handouts/docx/references/$(basename ${f%.md}).docx"
done
```
