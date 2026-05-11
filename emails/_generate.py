#!/usr/bin/env python3
"""
Generate pre-class emails for a Dutch course quarter.

Usage:
    python3 emails/_generate.py

Output goes to emails/<quarter>/ — edit QUARTER and SESSIONS below for a new course run.
"""

import os

QUARTER = "2026-Q2_Apr-Jun"

SESSIONS = [
    # (slug, date, day, time, code, title, unit, pages, [topics])
    ("s01", "20 April 2026", "Monday", "4:45–6:45 pm", "S1", "Hallo, kom binnen!", "Unit 01", "pages xi and 1–10",
     ["Dutch pronunciation: key sounds (aa, ij, ui, g/ch)",
      "Greetings and introductions: *hoe heet u?, ik kom uit…, aangenaam*",
      "The verb *zijn* (to be) and basic sentence structure",
      "Formal (*u*) vs informal (*jij/je*) address",
      "Vocabulary: drinks, asking how someone is, saying goodbye"]),

    ("s02", "23 April 2026", "Thursday", "4:45–6:45 pm", "S2", "Wat doe je?", "Unit 02", "pages 11–20",
     ["The verb *hebben* (to have) — full conjugation",
      "Talking about jobs, family and relationships",
      "Languages and nationalities",
      "Question formation (inversion) and negation (*niet / geen*)",
      "Vocabulary: family members, professions"]),

    ("s03", "26 April 2026", "Sunday", "10:00 am–12:00 pm", "S3", "Waar woon je?", "Unit 03", "pages 21–36",
     ["*De* and *het* articles — rules and patterns",
      "Adjective endings and the *-e* rule",
      "Describing your home, flat or neighbourhood",
      "*Er is / er zijn* (there is / there are)",
      "Vocabulary: rooms, housing types, neighbourhood words"]),

    ("s04", "27 April 2026", "Monday", "4:45–6:45 pm", "S4", "De boodschappen", "Unit 04", "pages 37–50",
     ["Shopping at the market and in a supermarket",
      "Quantities and weights: *een ons, een pond, een kilo*",
      "Modal verbs: *willen, kunnen, mogen, moeten*",
      "Dutch plural forms",
      "Vocabulary: food, packaging, money, market phrases"]),

    ("s05", "30 April 2026", "Thursday", "4:45–6:45 pm", "S5", "Weet u de weg?", "Unit 05", "pages 51–63",
     ["Asking for and giving directions",
      "Imperative (command) forms: *ga, loop, neem, sla af*",
      "Prepositions of place: *tegenover, naast, voorbij, aan de linkerkant*",
      "Vocabulary: places in town — station, church, hospital, town hall"]),

    ("s06", "3 May 2026", "Sunday", "10:00 am–12:00 pm", "S6", "Leuke schoenen!", "Unit 06", "pages 64–77",
     ["Clothing and colours vocabulary",
      "Adjective endings: the *-e* rule in detail (comparative review)",
      "Expressing opinions: *ik vind het…, ik hou van…, ik vind het te…*",
      "Shopping for clothes: sizes, trying on, paying",
      "Demonstratives: *deze / die / dit / dat*"]),

    ("s07", "4 May 2026", "Monday", "4:45–6:45 pm", "S7", "Mag ik een retourtje Wageningen?", "Unit 07", "pages 78–92",
     ["Buying train tickets: *enkeltje / retourtje, eerste / tweede klas*",
      "Public transport vocabulary: *spoor, perron, sneltrein, stoptrein, overstappen*",
      "Separable verbs: *opstaan, aankomen, overstappen, meebrengen*",
      "Telling the time (Dutch clock system — *half vier* = 3:30!)",
      "Dialogue practice: at the ticket window"]),

    ("s08", "7 May 2026", "Thursday", "4:45–6:45 pm", "S8", "Herhaling Units 1–7", "Review", None,
     ["Telling the time — consolidation drill",
      "Separable verbs in context",
      "Grammar rapid-fire: *zijn/hebben, de/het*, adjectives, modals",
      "Units 1–7 written test",
      "Review of your weak spots from the first three weeks"]),

    ("s09", "10 May 2026", "Sunday", "10:00 am–12:00 pm", "S9", "Heeft u een leuke vakantie gehad?", "Unit 08", "pages 93–108",
     ["The perfect tense (*voltooid tegenwoordige tijd*): *hebben / zijn* + past participle",
      "Past participle formation and the *'t kofschip* rule",
      "*Hebben* vs *zijn* as auxiliary — motion and change of state verbs",
      "Booking a hotel room: vocabulary and dialogue",
      "Talking about holidays: what you did, where you went, what you saw"]),

    ("s10", "11 May 2026", "Monday", "4:45–6:45 pm", "S10", "Midpunttoets — Units 01–08", "Midpoint review + test", None,
     ["2-hour written midpoint test covering Units 01–08",
      "Sections: vocabulary (EN→NL), grammar, reading, listening and writing",
      "Please review all vocabulary from Units 01–08 before class",
      "Bring your textbook for reference after the test"]),

    ("s11", "14 May 2026", "Thursday", "4:45–6:45 pm", "S11", "Ik heb bloemen voor je meegebracht", "Unit 09", "pages 109–120",
     ["Inviting someone to dinner: *Zou je zin hebben om…?*",
      "The verb *zullen* (shall/will) — offers, suggestions, future plans",
      "Expressing preferences: *liever, het liefst, ik geef de voorkeur aan*",
      "*Om + te + infinitive* to express purpose",
      "Vocabulary: invitations, dinner, food and dining"]),

    ("s12", "17 May 2026", "Sunday", "10:00 am–12:00 pm", "S12", "Vroeger", "Unit 10", "pages 121–133",
     ["Time expressions: *gisteren, vorige week, vroeger, toen, altijd, soms*",
      "Introduction to the simple past (*onvoltooid verleden tijd / imperfect*)",
      "Regular imperfect: stem + *-te* or *-de* ('t kofschip rule)",
      "*Vroeger + imperfect* = 'used to'",
      "Vocabulary: daily routines, the past, countryside, moving house"]),

    ("s13", "18 May 2026", "Monday", "4:45–6:45 pm", "S13", "Onvoltooid verleden tijd (verdieping)", "Unit 10 (continued)", "pages 121–133",
     ["Simple past in depth: regular and key irregular verbs",
      "Irregular imperfects: *was, had, ging, kwam, zag, wist*",
      "Perfect tense vs imperfect — when to use which",
      "Narrative structure: perfectum to introduce, imperfect for background",
      "Extended writing practice: a story about the past"]),

    ("s14", "21 May 2026", "Thursday", "4:45–6:45 pm", "S14", "Laten we naar Antwerpen gaan", "Unit 11", "pages 134–151",
     ["Making suggestions: *laten we…, zullen we…, wat dacht je van…*",
      "Expressing likes and dislikes: *houden van, een hekel hebben aan*",
      "Talking about food preferences and restaurant vocabulary",
      "Relative clauses: *die / dat* (introduction)",
      "Vocabulary: going out, food, leisure activities"]),

    ("s15", "24 May 2026", "Sunday", "10:00 am–12:00 pm", "S15", "Ik stuur je wel een sms-je", "Unit 12", "pages 152–173",
     ["Making and receiving phone calls in Dutch",
      "The conditional *zouden* (would): introduction and forms",
      "Prepositions in depth: *op, aan, in, bij, van, met, voor*",
      "Texting and informal written language",
      "Vocabulary: phone, messages, making appointments"]),

    ("s16", "25 May 2026", "Monday", "4:45–6:45 pm", "S16", "Zouden (verdieping)", "Unit 12 (continued)", "pages 152–173",
     ["*Zouden* (would) in depth: polite requests, hypotheticals, reported speech",
      "Preposition practice: collocations and fixed expressions",
      "Review of subordinate clauses with *dat, omdat, als*",
      "Conversation drill: polite and conditional language in context"]),

    ("s17", "28 May 2026", "Thursday", "4:45–6:45 pm", "S17", "Ik weet echt niet wat ik wil", "Unit 13", "pages 174–192",
     ["Subordinate clauses: *dat, omdat, als, toen, terwijl*",
      "Word order in subordinate clauses (verb to the end)",
      "Talking about career, ambitions and skills",
      "Vocabulary: work, education, abilities"]),

    ("s18", "31 May 2026", "Sunday", "10:00 am–12:00 pm", "S18", "Ik begrijp precies hoe je je voelt", "Unit 14", "pages 193–208",
     ["Reflexive verbs: *zich voelen, zich vervelen, zich verheugen*",
      "Health and body vocabulary: symptoms, at the doctor",
      "Expressing emotions and empathy",
      "Vocabulary: health, feelings, the body"]),

    ("s19", "1 June 2026", "Monday", "4:45–6:45 pm", "S19", "Units 15–16 Survey + Herhaling", "Units 15–16", "pages 209–243",
     ["Survey of Units 15–16: internet, money, media and opinion",
      "Expressing opinions and comparisons: *vinden, denken, menen*",
      "Adverbs and sentence connectors",
      "Revision of all major grammar from the course",
      "Vocabulary: technology, media, current affairs"]),

    ("s20", "4 June 2026", "Thursday", "4:45–6:45 pm", "S20", "Eindgesprek en feedback", "Final session", None,
     ["Oral conversation test: free discussion on topics from the whole course",
      "Written self-assessment: what has improved, what needs more work",
      "Feedback session: your progress over 20 sessions",
      "Advice and resources for continuing your Dutch independently"]),
]

TEMPLATE = """\
# Email — {code} — {title}

**To:** [student email]
**Subject:** Dutch class today — {date}

---

Dear Students,

Here is the meetup link for today's class, {date} ({day}, {time}):

[GOOGLE_MEET_URL]

---

**Today's session: {code} — {title} ({unit})**

In today's class we will cover:
{bullets}

{textbook_line}

See you soon!
Jasper
"""


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(script_dir, QUARTER)
    os.makedirs(out_dir, exist_ok=True)

    for data in SESSIONS:
        slug, date, day, time, code, title, unit, pages, topics = data
        bullets = "\n".join(f"- {t}" for t in topics)
        if pages:
            textbook_line = f"Please have your textbook open to {pages}."
        else:
            textbook_line = "No new textbook pages for this session."

        content = TEMPLATE.format(
            date=date,
            day=day,
            time=time,
            code=code,
            title=title,
            unit=unit,
            bullets=bullets,
            textbook_line=textbook_line,
        )
        path = os.path.join(out_dir, f"{slug}-email.md")
        with open(path, "w") as f:
            f.write(content)
        print(f"  wrote {slug}-email.md")

    print(f"\nDone — {len(SESSIONS)} emails in emails/{QUARTER}/")


if __name__ == "__main__":
    main()
