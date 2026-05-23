# yamul — grammar and usage

How to read, write, and compose yamul. For the language's design
philosophy and the iconeme system that underlies its vocabulary, see
[design.md](design.md). For the dictionaries, see
[iconemes.md](iconemes.md) (single iconemes) and
[lexicon.md](lexicon.md) (compounds).


---

## 1. Phonology

### Vowels (5)
Universal five-vowel system. No length, no nasalization, no tone.

| Letter | IPA | Like |
|---|---|---|
| a | /a/ | father |
| e | /e/ | bet |
| i | /i/ | machine |
| o | /o/ | go (pure, no glide) |
| u | /u/ | boot |

### Consonants (17)

| Letter | IPA | Like |
|---|---|---|
| p | /p/ | pin |
| b | /b/ | bin |
| t | /t/ | ten |
| d | /d/ | den |
| k | /k/ | kin |
| g | /g/ | go |
| m | /m/ | man |
| n | /n/ | no |
| f | /f/ | fan |
| s | /s/ | sun |
| h | /h/ | hat |
| c | /tʃ/ | **ch**air |
| x | /ʃ/ | **sh**oe |
| l | /l/ | leaf |
| r | /ɾ/ | Spanish *pe**r**o* (single tap) |
| w | /w/ | win |
| y | /j/ | yes |

**Total: 22 phonemes.** Letters *j q v z* are not used.

### Phonotactics
Syllable shape: **(C)V(V)(N|L)**
- Optional onset (one consonant max — no clusters ever)
- Mandatory vowel nucleus, optionally a second different vowel
- Optional coda: only nasals (m, n) or liquids (l, r) — never stops or
  fricatives

### Stress
Penultimate, predictable, non-contrastive. *yamul* is /ˈja.mul/,
*kaecur* is /ˈkae.tʃuɾ/, *fonkeu* is /ˈfon.keu/. No memorization needed.


---

## 2. Writing system

- **Latin alphabet, 22 letters.** One letter ↔ one phoneme. No silent
  letters, no diacritics, no digraphs.
- **Letters used:** a b c d e f g h i k l m n o p r s t u w x y
- **Letters not used:** j q v z
- **No capitalization at all.** Single case only. Sentence boundaries are
  marked by punctuation. Proper nouns get no special treatment.
- **Punctuation:** standard international set — . , ? ! : ; " ( ) — used
  as in English.
- **Numbers:** Arabic numerals 0–9.
- **Word boundaries:** spaces between words, as in English/most
  European languages.

Spelling is fully transparent: anyone who can sound out the letters has
pronounced the word correctly. Anyone who has heard a word can spell it.


---

## 3. Word formation

### Standalone iconemes
Most iconemes can stand alone as one-word lexical items expressing their
bare hue — *xu* = SELF = "I," *ku* = YOU, *fon* = WATER. Pronouns,
particles, and basic substances are typically single iconemes.

### Compounds (multi-iconeme words)
Specificity comes from combining iconemes into longer words:

| Compound | Iconemes | Meaning |
|---|---|---|
| *fonkeu* | WATER + PATH | river |
| *fonyim* | WATER + DOWN | rain |
| *bumyar* | EARTH + INSIDE | house |
| *fonxinyar* | WATER + FIRE + INSIDE | drunkenness (lit. internal fiery water) |

Compounds are written as one word — no hyphen, no internal space — and
their parts are recovered by the parser, not by the writer. The full
compound dictionary is in [lexicon.md](lexicon.md).

### Head-first compound rule
The **first iconeme is the head**; each subsequent iconeme modifies the
running compound. WATER + FIRE = *fonxin* "fiery water" (alcohol);
FIRE + WATER = *xinfon* "watery fire" (ember). Order matters. Long
compounds (5+ iconemes) are fully supported.

### Longest-match parsing
Word interiors are parsed by greedy left-to-right longest match against
the iconeme inventory — exactly like a programming language lexer. At
each position the reader takes the longest sequence that is a valid
iconeme, then continues. The iconeme inventory is therefore a fixed,
ordered, authoritative lexicon; adding a new iconeme can re-parse
existing words (as in natural-language reanalysis: English *hamburger*
→ *ham* + *burger*).

### Parse-sensitivity in coining
Because parsing is greedy, coining is parse-sensitive. For example,
KNOW + JOIN = *mi* + *ul* would form *miul*, but the iconeme *miul*
already means DARK — longest-match silently re-parses the compound as
the unrelated existing word. The `gen.py` tokenizer catches this:
`python3 gen.py tokenize miul` reports `miul (DARK)`, not `mi + ul`.
Any new coinage should be run through the tokenizer before it's added
to the lexicon.


---

## 4. Sentence grammar

### Typological profile
Isolating–agglutinative hybrid · head-initial · strict SVO · no
inflection of any kind · no gender · no articles · no agreement · no
obligatory tense · no obligatory plural.

### Word order

```
SUBJECT  VERB  OBJECT  [adverbials]  [sentence-final particles]
```

Position alone marks subject and object. No case marking on core
arguments.

### Modification (all head-initial)

| Construction | Order | Example |
|---|---|---|
| Noun + adjective | N Adj | *fon ciam* "hot water" |
| Verb + adverb | V Adv | *gar li* "see well" |
| Noun + relative clause | N [il …] | *fonkeu il xu mi* "the river that I know" |
| Possessed + possessor | N il N | *yamul il xu* "my language" |

The particle *il* (BELONG) is a general-purpose attributive linker doing
the work of genitive, relative-clause marker, and complementizer
(similar to Mandarin 的 *de*). *il* is fixed by manual pin so this role
is stable across re-seedings of the vocabulary.

### Tense, aspect, mood (TAM)
All optional. Particles before the verb. Default (unmarked) is
present/neutral; context provides time when it matters. Particles use
existing iconemes:

| Function | Iconeme | Role |
|---|---|---|
| past | BEFORE | "did" |
| future | AFTER | "will" |
| progressive | CONTINUE | "is doing" |
| inchoative | BEGIN | "starts to do" |
| perfective | END | "has finished" |
| iterative | AGAIN | "does again" |
| potential | POSSIBLE | "can, may" |
| deontic | NECESSARY | "must" |
| conditional | IF | "would, if…" |

Multiple particles stack; order matches scope.

### Negation
Particle *ba* (FALSE) before whatever is negated:
- *xu ba gar ku* — "I don't see you"
- *xu gar ba ku* — "I see [something], not you"

### Affirmation
*ra* (TRUE) for emphasis: *xu ra gar ku* — "I do see you."
Bare *ra* / *ba* = "yes" / "no" as one-word answers.

### Questions
Sentence-final particle *tu* (ASK) marks yes/no questions, word order
unchanged. Content questions use derived question words formed by
BASE + ASK as a single compound:

| Question | Compound | Form |
|---|---|---|
| what | THING + ASK | *fertu* |
| who | PERSON + ASK | *semtu* |
| where | PLACE + ASK | *antu* |
| when | TIME + ASK | *curtu* |
| why | BECAUSE + ASK | *fetu* |
| how | WAY + ASK | *lintu* |

Question words sit in their natural slot — no fronting.

### Pronouns
Three base pronouns, pluralized with MANY:

| | Singular | Plural |
|---|---|---|
| 1st | SELF | SELF MANY (we) |
| 2nd | YOU | YOU MANY (you all) |
| 3rd | THEY | THEY MANY (they) |

No gender. No formality distinction. No subject/object case (position
determines role).

### Plural marking
Optional particle MANY after the noun, only when number isn't clear from
context. Default is unmarked. ONE before a noun marks explicit singular.

### Conjunctions

| Particle | Use |
|---|---|
| JOIN | and |
| OR | or |
| BUT | but |

Used between the things they connect.

### Subordination
Clause-initial particles introduce subordinate clauses:
- *im* (IF) for conditionals
- *fe* (BECAUSE) for causal clauses
- *il* (BELONG) for relative clauses and complement clauses

### Imperatives
Bare verb (no subject) = imperative: *gar!* "Look!"
Negative imperative: *ba gar!* "Don't look!"
Polite: prepend the addressee — *ku gar* "you (please) look."

### Comparatives
Use *il* as the comparison standard marker:
- *X sil Y il Z* — "X is more Y than Z" (sil = MORE)

### Existentials
Single-argument BE-clause: *el fer ro* — "There is a problem." (lit.
"bad thing is.")

### Politeness
Purely lexical. No grammatical honorifics. Politeness is conveyed by
word choice, hedging, and modal verbs — additive, not inflectional.


---

## 5. Sample sentences

Using the current vocabulary (seed=42 in gen.py). BELONG (*il*) is
pinned, so these examples stay stable across re-seedings; other
iconemes may shift if the seed changes.

| Meaning | yamul |
|---|---|
| I see you | *xu gar ku* |
| You see me | *ku gar xu* |
| Did you see me? | *ku gar xu tu* |
| I don't see you | *xu ba gar ku* |
| I will see you | *xu cu gar ku* |
| The water is cold | *fon gao* |
| I want water | *xu win fon* |
| my language | *yamul il xu* |
| this is a good language | *we ro yamul li* |
| yamul is a language | *yamul ro yamul* |
| I speak yamul | *xu bil yamul* |
| If it rains, I won't go outside | *im fonyim, xu ba rehil xam* |
| Where do you live? | *ku sim antu* |
| I know that you saw the fire | *xu mi il ku pu gar xin* |


---

## 6. Quick reference

- **Phonemes:** 22 (5 vowels + 17 consonants); one letter ↔ one phoneme
- **Stress:** penultimate, predictable
- **Word order:** strict SVO, head-initial throughout
- **Modification:** head N + modifier; *N il N* for genitive,
  *N il [clause]* for relative clauses
- **TAM:** preverbal particles (BEFORE, AFTER, CONTINUE, BEGIN, END,
  AGAIN, POSSIBLE, NECESSARY, IF), all optional
- **Negation:** *ba* before whatever is negated
- **Questions:** sentence-final *tu* for yes/no; *base + tu* compound
  for content questions, in situ
- **Conjunctions:** *ul* (and), *sa* (or), *ko* (but), between connected
  items
- **Pronouns:** *xu* (I), *ku* (you), *su* (they); + *he* (MANY) for
  plural
- **No:** capitalization, gender, articles, agreement, inflection,
  obligatory tense, obligatory plural, irregular forms
- **Yes:** optional TAM particles, optional plural marker,
  postpositional linkers, mandatory pronouns
