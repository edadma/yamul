# Genesis 1:1–5 in yamul

A stress-test of the language on real connected text. Translating the
opening verses of Genesis forces yamul to handle: a cosmogonic narrative
voice (past throughout), the verb of creation, the abstract subject
"God," locative and existential predicates, formulaic naming, and
ordinal numbering — much of which the sentence-level grammar hasn't
exercised before.

This file uses six new coinings (added to lexicon.md as part of this
translation). All parse cleanly under `python3 gen.py tokenize`:

| Compound | Composition | Meaning |
|---|---|---|
| *kamna* | MAKE + ALL | God, creator |
| *pecur* | BEGIN + TIME | the beginning |
| *kaecurpe* | BRIGHT + TIME + BEGIN | morning |
| *miulpe* | DARK + BEGIN | evening |
| *ceimfim* | HIGH + PART | face, surface |
| *yalxim* | STILL + AIR | hover, float |


---

## Verse 1

> In the beginning, God created the heavens and the earth.

> *pecur, kamna pu kam ceimxim ul bum.*

- *pecur* = "the beginning" (used as a bare temporal NP; yamul drops
  the locative preposition, so this serves as "in the beginning")
- *kamna* = "God" — the creator, lit. "all-maker"
- *pu kam* = past-make = "created"
- *ceimxim ul bum* = "the heavens and the earth"


---

## Verse 2

> And the earth was formless and empty, darkness was over the face of
> the deep, and the Spirit of God was hovering over the waters.

> *ul bum pu ro gaen, ul miul pu ro rar ceimfim il rual, ul simxim il
> kamna pu yalxim rar fon.*

- *bum pu ro gaen* = "the earth was empty" — *gaen* (EMPTY) absorbs
  Hebrew *tohu va-vohu* (formless-and-void) into a single word, which
  is more consonant with yamul's compact-content style than coining a
  separate FORM iconeme.
- *miul pu ro rar ceimfim il rual* = "darkness was above [the]
  surface of [the] deep" — *rar* (UP) used as a preposition "over,"
  *ceimfim il rual* = "face of the deep."
- *simxim* = "spirit / breath" — yamul collapses the two senses the
  same way Hebrew *ruach*, Greek *pneuma*, and Latin *spiritus* do.
- *yalxim* = "to hover" — head-first STILL + AIR; the action of
  being-still-in-air.


---

## Verse 3

> And God said, "Let there be light!" And there was light.

> *ul kamna pu bil, "ro kaefer!" ul kaefer pu ro.*

- *"ro kaefer!"* — the imperative existential. yamul's normal
  existential is *X ro* ("X exists"); fronting the verb to *ro X*
  produces the let-there-be / fiat reading. Bare-verb imperative
  (no subject), parallel to grammar.md §4's *gar!* "Look!".
- *kaefer pu ro* = "[the] light was/came-to-be" — existential past.


---

## Verse 4

> And God saw that the light was good, and God divided the light from
> the darkness.

> *ul kamna pu gar il kaefer ro li. ul kamna pu fim kaefer com miul.*

- *gar il [clause]* = "saw that [clause]" — standard complement-clause
  construction with *il*.
- *fim X com Y* = "divided X from Y" — *fim* (PART) used as a verb
  "to divide / set apart," *com* (AWAY) used as the preposition
  "from."


---

## Verse 5

> And God called the light "Day," and the darkness he called "Night."
> And there was evening, and there was morning — the first day.

> *ul kamna pu bil il kaefer ro kaecur, ul miul ro miulcur. ul miulpe
> pu ro, ul kaecurpe pu ro — kaecur er.*

- *bil il X ro Y* = "said that X is Y" — yamul's idiom for "called X
  Y" / "named X Y." This is a more general "naming construction"
  worth lexicalising as a grammar pattern.
- *miulpe pu ro, ul kaecurpe pu ro* = "evening came-to-be, and
  morning came-to-be" — parallel existential statements.
- *kaecur er* = "day one" / "the first day" — *er* (ONE) used as a
  postnominal ordinal modifier (head-first: head = DAY, mod = ONE).


---

## What this surfaced

**Gaps closed by this translation:**

1. A word for the divine creator (*kamna*) — yamul previously had no
   theological vocabulary.
2. A nominal "the beginning" (*pecur*) — distinct from the TAM
   particle *pe* "starts to."
3. "Evening" (*miulpe*) and "morning" (*kaecurpe*) — completing the
   diurnal cycle.
4. "Face / surface" (*ceimfim*) — a body-of-water surface word, but
   generalisable.
5. "Hover" (*yalxim*) — a motion verb that's neither walking, flying,
   nor running.

**Gaps remaining:**

- **"Without form" vs "empty."** Hebrew *tohu va-vohu* is two distinct
  words; yamul collapsed both into *gaen* "empty." If the language
  needs a separate FORM iconeme (for "shape, configuration") that's
  a candidate addition.
- **Naming construction.** *bil il X ro Y* "say that X is Y" works
  but is wordy for the frequent "X is called Y" pattern. Worth
  considering a dedicated naming particle, or formalising the idiom.
- **Ordinals beyond ONE.** *er* serves as "first" here; ordinal forms
  for second / third / etc. are unspecified. The lexicon's note about
  numerals beyond ONE/MANY (open issue #3 in design.md) is now
  pressing.
- **Locative copula.** Verse 2 uses *pu ro rar X* "was over X." This
  works but the "X ro PP" pattern hasn't been formally documented in
  grammar.md §4.
