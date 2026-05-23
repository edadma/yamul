# yamul — language design specification

A constructed natural language built around a phonosemantic palette
("iconemes") and designed for international learnability.

The name **yamul** has two readings. In English it's a backronym for
**y**et **a**nother **m**ade-**u**p **l**anguage — yamul is part of
the long tradition of conlangs that don't really need to exist. In
yamul itself it parses as *yam* + *ul* = THINK + JOIN = "thoughts
joined," which describes what language *is*: the act of joining minds
through shared cognitive content. The name is both the language's
proper name and its common noun for "language."

This document covers the *design rationale*: why yamul is shaped the
way it is, the iconeme system that underlies its vocabulary, the
mechanisms that protect parsing, and the open design questions still
to be resolved. For *how to read, write, and compose yamul*, see
[grammar.md](grammar.md); for the dictionaries, see
[iconemes.md](iconemes.md) (single iconemes) and
[lexicon.md](lexicon.md) (compounds).


---

## 1. Design philosophy

- **Iconemes**, not arbitrary words, are the building blocks. Each iconeme
  is a short phoneme sequence carrying a vague semantic "hue." Words are
  coined by combining iconemes; meaning is fixed by usage, not strictly by
  composition.
- **Connotational, not denotational.** The phonemes color a word with
  associations rather than determining its meaning. Multiple iconeme
  combinations can converge on the same concept, with subtle differences
  in feel that usage will eventually distinguish.
- **Easy to learn.** No *grammatical* gender (no agreement, no gendered
  articles, no noun-class inflection), no other inflection, no obligatory
  tense or plural, no irregular forms. One letter per phoneme. No
  capitalization. Strict word order so no case marking is needed.
  Referential gender — talking about a sister vs. a brother — is fully
  expressible via the MALE / FEMALE iconemes (*tan* / *dan*) as
  head-first modifiers; the unmodified term is gender-neutral by
  default, so non-gendered usage stays short.
- **Head-initial throughout.** Verbs precede objects, nouns precede
  modifiers, heads precede dependents in every construction.
- **Isolating–agglutinative hybrid.** Content words are agglutinative
  (iconemes glue together inside words); grammatical relationships are
  isolating (separate particles between words). No fusional morphology.


---

## 2. Iconeme system

An **iconeme** is the basic semantic unit of the language. It's a short
phoneme sequence (2–4 phonemes) carrying a vague semantic hue. The
phonemic inventory and phonotactics that constrain iconeme shapes are
documented in [grammar.md §1](grammar.md#1-phonology).

### Valid iconeme shapes

| Shape | Examples | Count |
|---|---|---|
| CV | *ka, mu, lo* | 85 |
| VN | *am, on* | 10 |
| VL | *al, ar* | 10 |
| CVN | *kam, son* | 170 |
| CVL | *kar, mol* | 170 |
| CVV | *kai, mou* (heterogeneous vowel pairs only) | 340 |
| CVVC | *kain, moul* | 1360 |

**Total possible iconemes: 2,145 forms.** Current language uses ~115.

### Rules
- **No single-phoneme iconemes.** Minimum 2 phonemes for acoustic
  robustness.
- **CVV pairs must be heterogeneous** (no *kaa, kee* etc.) — doubled
  vowels collapse perceptually into long vowels, which the phonology
  doesn't admit.
- **Iconemes form a fixed lexicon.** Adding new iconemes is deliberate;
  doing so can re-parse existing words.

### Sound-symbolic palette (sharpness)
Each phoneme carries a sharpness score on the bouba/kiki axis:

| Sharp end (+) | Neutral | Soft end (−) |
|---|---|---|
| i (+2), e (+1) | a, h, f, r, y, d | u (−2), o (−1) |
| k (+2), t (+2), p (+1) | (mid) | g (−1), b (−1) |
| s (+1), c (+2), x (+1) | (mid) | m (−2), n (−1), l (−2), w (−1) |

An iconeme's sharpness is the sum of its phonemes' scores. Concepts are
classified as SHARP, SOFT, or NEUTRAL, and assignments draw from the
matching sound-symbolic pool. This makes WATER feel watery (e.g., *fon*,
−2), FIRE feel fiery (e.g., *xin*, +2), HOT feel hot (e.g., *ciam*, +2),
COLD feel cold (e.g., *gao*, −2), etc.

### Frequency tiers
Common words must have simple shapes (Zipf-like compression):

| Tier | Allowed shapes | Use |
|---|---|---|
| 1 | CV, VN, VL only (2 phonemes, no vowel pair) | Pronouns, particles, basic function words |
| 2 | + CVN, CVL (no vowel pair) | Common verbs, nouns, qualities |
| 3 | + CVV, CVVC (full pool) | Specialized concepts |

This guarantees the most-spoken words are the shortest.


---

## 3. Blocked forms

Forms can be deliberately reserved as unassignable to protect compound
words from parser ambiguity under longest-match. None are currently
blocked — *yam* used to be, to keep an earlier *yamul = ya + mul* parse
intact, but the etymology was switched to *yam + ul* so longest-match
agrees with the intended parse natively. The blocked-forms mechanism
stays in the tooling (`gen.py`'s `BLOCKED_FORMS` set) for future use
when new coinings turn out to need it.


---

## 4. Pinned vocabulary

The following iconemes are fixed by manual pin (not randomized):

| Concept | Iconeme | Why |
|---|---|---|
| THINK | *yam* | First half of *yamul* |
| JOIN | *ul* | Second half of *yamul* |
| BELONG | *il* | Structural attributive linker — used in every genitive, relative-clause, and complement-clause example, so its form is held stable across re-seedings. |

Beyond these three, every other concept currently in the language is
also pinned in `gen.py`'s `MANUAL_PINS` map — the lexicon is now a
frozen, hand-edited table, and the random-assignment path only fires
for newly-added concepts that haven't yet been pinned. This means small
edits (renaming one concept, adding one new entry) don't reshuffle the
rest of the vocabulary.


---

## 5. Tooling

**gen.py** — generates the iconeme pool, applies sound-symbolic and
tier constraints, and emits an assignment file. The current lexicon is
fully pinned in `MANUAL_PINS`, so running it just rewrites iconemes.md
from those pins; the seeded-random path only fires for newly-added
concepts that haven't yet been pinned. Also exposes a tokenize
subcommand: `python3 gen.py tokenize <word>` decomposes a written form
back into its iconemes by longest match — use this to verify any
coinage parses the way you intended.

**iconemes.md** — the single-iconeme dictionary (~115 entries).
Generated from gen.py.

**lexicon.md** — the multi-iconeme dictionary of agreed compounds
(~90 entries seeded). Every entry is verified to round-trip through
`gen.py tokenize`. New coinings go here once their parse is confirmed.

**grammar.md** — the use-facing reference: phonology, writing system,
word formation in practice, sentence grammar, sample sentences.


---

## 6. Open issues / next steps

1. **Override accidental cognates.** Some seed runs produce assignments
   that collide with English/Spanish/etc. words. Add them to
   MANUAL_PINS as they're caught.
2. **Extend the parser/glosser to sentences.** A word-level glosser
   ships in `gen.py` (`python3 gen.py tokenize <word>` decomposes a
   compound back to its iconemes); the natural next step is a
   sentence-level tool that segments a yamul string, looks up
   compounds in lexicon.md, and renders an interlinear gloss.
3. **Extend the lexicon.** A starter dictionary lives in lexicon.md,
   all tokenizer-verified, including kinship terms built on the
   PERSON + relation + (MALE/FEMALE) pattern. Gaps to fill: numerals
   beyond ONE/MANY, weather verbs, common foods, anything else needed
   by item 4 below.
4. **Write extended text** — a paragraph, a story, a poem — to stress
   the design in connected discourse and surface weaknesses that
   sentence-level examples won't show.
5. **Consider lexical irregularities to allow.** All real languages have
   some. Currently yamul has none, which may make it feel sterile.
   Decide whether a small set of irregular high-frequency forms is
   desirable.
6. **Decide on adjective-as-predicate vs. copula.** Currently *fon gao*
   "water cold" works as predicate without copula, but grammar.md §5
   also uses *ro* (BE) in *we ro yamul li*, *yamul ro yamul*. Clarify
   when the copula is required vs. optional.
7. **Word boundary in writing.** Spaces are required even with
   longest-match parsing, since the parser only knows where words end at
   spaces. Document this and consider whether continuous writing could
   ever work (probably not; words can grow long enough that human
   readers benefit from spaces).
