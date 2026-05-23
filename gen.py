#!/usr/bin/env python3
"""
Iconeme generator and sound-symbolic assigner.

Phonotactics: (C)V(V)(N|L), iconemes are 2-4 phonemes.

Valid shapes:
  CV    - 85 forms
  VN    - 10 forms
  VL    - 10 forms
  CVN   - 170 forms
  CVL   - 170 forms
  CVV   - 340 forms (heterogeneous vowel pairs)
  CVVC  - 1360 forms (CVV + nasal/liquid coda)

Total: 2145 valid iconemes.

Sound-symbolic assignment:
  Each iconeme has a sharpness score based on its phonemes.
  Concepts are pre-classified as SHARP, SOFT, or NEUTRAL.
  Assignment draws each concept randomly from its matching pool.
"""

import random
import json
from pathlib import Path

CONSONANTS = list("pbtdkgmnfshcxlrwy")
VOWELS = list("aeiou")
NASALS = list("mn")
LIQUIDS = list("lr")
CODAS = NASALS + LIQUIDS

# ---------------------------------------------------------------------------
# Sound symbolism: per-phoneme sharpness weights
# ---------------------------------------------------------------------------
# Based on the bouba/kiki literature and cross-linguistic phonosemantic
# patterns. Front close vowels and voiceless stops/sibilants score sharp;
# back round vowels, sonorants, and voiced stops score soft.
SHARPNESS = {
    # Vowels
    "i": +2, "e": +1, "a": 0, "o": -1, "u": -2,
    # Voiceless stops (sharp)
    "k": +2, "t": +2, "p": +1,
    # Voiced stops (mildly soft)
    "g": -1, "d": 0, "b": -1,
    # Sibilants and affricates (sharp)
    "s": +1, "c": +2, "x": +1,
    # Other fricatives (neutral)
    "f": 0, "h": 0,
    # Sonorants (soft)
    "m": -2, "n": -1, "l": -2, "r": 0,
    # Glides (mildly soft)
    "w": -1, "y": 0,
}


def sharpness(form):
    return sum(SHARPNESS[ch] for ch in form)


# ---------------------------------------------------------------------------
# Iconeme generation
# ---------------------------------------------------------------------------
def gen_cv():
    return [c + v for c in CONSONANTS for v in VOWELS]


def gen_vn():
    return [v + n for v in VOWELS for n in NASALS]


def gen_vl():
    return [v + l for v in VOWELS for l in LIQUIDS]


def gen_cvn():
    return [c + v + n for c in CONSONANTS for v in VOWELS for n in NASALS]


def gen_cvl():
    return [c + v + l for c in CONSONANTS for v in VOWELS for l in LIQUIDS]


def gen_cvv():
    pairs = [(v1, v2) for v1 in VOWELS for v2 in VOWELS if v1 != v2]
    return [c + v1 + v2 for c in CONSONANTS for v1, v2 in pairs]


def gen_cvvc():
    pairs = [(v1, v2) for v1 in VOWELS for v2 in VOWELS if v1 != v2]
    return [
        c + v1 + v2 + coda
        for c in CONSONANTS
        for v1, v2 in pairs
        for coda in CODAS
    ]


def all_iconemes():
    return {
        "CV": gen_cv(),
        "VN": gen_vn(),
        "VL": gen_vl(),
        "CVN": gen_cvn(),
        "CVL": gen_cvl(),
        "CVV": gen_cvv(),
        "CVVC": gen_cvvc(),
    }


def is_valid_iconeme(s):
    if len(s) < 2 or len(s) > 4:
        return False
    if not all(ch in CONSONANTS + VOWELS for ch in s):
        return False
    if len(s) == 2:
        if s[0] in CONSONANTS and s[1] in VOWELS:
            return True
        if s[0] in VOWELS and s[1] in CODAS:
            return True
        return False
    if len(s) == 3:
        if s[0] in CONSONANTS and s[1] in VOWELS:
            if s[2] in CODAS:
                return True
            if s[2] in VOWELS and s[2] != s[1]:
                return True
        return False
    if len(s) == 4:
        if (
            s[0] in CONSONANTS
            and s[1] in VOWELS
            and s[2] in VOWELS
            and s[1] != s[2]
            and s[3] in CODAS
        ):
            return True
        return False
    return False


# ---------------------------------------------------------------------------
# Concept classification
# ---------------------------------------------------------------------------
SHARP_CONCEPTS = [
    "SMALL", "SHARP", "BRIGHT", "HOT", "FIRE", "NARROW", "HARD",
    "HIGH", "LOUD", "SUDDEN", "BREAK", "BEGIN", "PUSH", "HARM",
]

SOFT_CONCEPTS = [
    "BIG", "SOFT", "DARK", "WIDE", "LOW", "HEAVY", "DEEP", "LONG",
    "COLD", "QUIET", "WATER", "EARTH", "STILL", "CONTINUE", "WEAK",
]

ALL_CONCEPTS = [
    # 1. Existence & identity
    "BE", "SAME", "OTHER", "ONE", "MANY",
    # 2. Self & other
    "SELF", "YOU", "THEY", "ALL", "NONE",
    # 3. Space & motion
    "HERE", "THERE", "TOWARD", "AWAY", "UP", "DOWN",
    "INSIDE", "OUTSIDE", "PATH", "STILL", "ACROSS", "AROUND",
    # 4. Time & change
    "NOW", "BEFORE", "AFTER", "BEGIN", "END", "CHANGE",
    "CONTINUE", "AGAIN", "SUDDEN",
    # 5. Quantity & degree
    "BIG", "SMALL", "MORE", "LESS", "ENOUGH", "EMPTY", "FULL",
    # 6. Quality & valence
    "GOOD", "BAD", "TRUE", "FALSE", "BEAUTIFUL", "UGLY",
    # 7. Mind & sensation
    "KNOW", "WANT", "FEEL", "SEE", "HEAR", "SAY", "THINK", "REMEMBER",
    # 8. Action & effect
    "DO", "GIVE", "TAKE", "JOIN", "PART", "MAKE", "BREAK",
    "CAUSE", "ALLOW", "PREVENT", "TRY",
    # 9. Substance & form
    "THING", "LIVE", "WATER", "FIRE", "EARTH", "AIR",
    # 10. Sensory qualities
    "HOT", "COLD", "BRIGHT", "DARK", "LOUD", "QUIET",
    "WET", "DRY", "HARD", "SOFT", "SHARP", "HEAVY",
    # 11. Dimensional qualities
    "LONG", "SHORT", "WIDE", "NARROW", "DEEP", "HIGH", "LOW",
    "NEAR", "FAR",
    # 12. Force & power
    "STRONG", "WEAK", "PUSH", "PULL",
    # 13. Logical relations
    "IF", "BECAUSE", "BUT", "OR", "WITH", "BELONG",
    # 14. Modal & meta
    "POSSIBLE", "NECESSARY", "ASK",
    # 15. Social & relational
    "HELP", "HARM", "SHARE", "TRUST",
    # 16. Body
    "HEAD", "HAND", "EYE", "MOUTH", "HEART", "FOOT",
    # 17. Generic categories
    "PERSON", "PLACE", "TIME", "WAY",
]


def concept_class(concept):
    if concept in SHARP_CONCEPTS:
        return "SHARP"
    if concept in SOFT_CONCEPTS:
        return "SOFT"
    return "NEUTRAL"


# ---------------------------------------------------------------------------
# Frequency tiers
# ---------------------------------------------------------------------------
# Tier 1: most-spoken words (pronouns, particles, basic function words).
#         Drawn from CV/VN/VL only — 2 phonemes, no vowel pair.
# Tier 2: common content words (frequent verbs, nouns, qualities).
#         Drawn from CV/VN/VL/CVN/CVL — 2-3 phonemes, no vowel pair.
# Tier 3: specialized concepts. Full pool, including CVV and CVVC.

TIER_1_CONCEPTS = [
    # Pronouns
    "SELF", "YOU", "THEY",
    # Quantifiers used as particles
    "ONE", "MANY", "ALL", "NONE", "SAME", "OTHER",
    # Demonstratives
    "HERE", "THERE",
    # Polarity
    "TRUE", "FALSE",
    # Tense particles (optional but very common when used)
    "NOW", "BEFORE", "AFTER",
    # Conjunctions and subordinators
    "JOIN", "OR", "BUT", "IF", "BECAUSE",
    # Modals
    "POSSIBLE", "NECESSARY", "ASK",
    # Linking
    "WITH", "BELONG",
    # Existence and basic action
    "BE", "DO",
]

TIER_2_CONCEPTS = [
    # Common verbs
    "SEE", "HEAR", "SAY", "KNOW", "WANT", "FEEL", "THINK",
    "GIVE", "TAKE", "MAKE", "PART",
    # Generic nouns
    "THING", "PERSON", "PLACE", "TIME", "WAY",
    # Substances and life
    "WATER", "FIRE", "EARTH", "AIR", "LIVE",
    # Basic quantities
    "MORE", "LESS",
    # Basic qualities
    "GOOD", "BAD", "BIG", "SMALL",
    # Common spatial
    "TOWARD", "AWAY", "UP", "DOWN", "INSIDE", "OUTSIDE",
    # Common temporal
    "BEGIN", "END", "CHANGE", "AGAIN",
]

# Everything else falls into Tier 3 by default (full pool available).


def concept_tier(concept):
    if concept in TIER_1_CONCEPTS:
        return 1
    if concept in TIER_2_CONCEPTS:
        return 2
    return 3


# Per-tier shape allowlists
TIER_SHAPES = {
    1: ["CV", "VN", "VL"],
    2: ["CV", "VN", "VL", "CVN", "CVL"],
    3: ["CV", "VN", "VL", "CVN", "CVL", "CVV", "CVVC"],
}


# ---------------------------------------------------------------------------
# Manual pins — the authoritative lexicon. Every concept currently in the
# language has a pinned iconeme here, so re-running this script is stable:
# a small change (renaming one concept, adding a new one) doesn't reshuffle
# the rest of the vocabulary. The random-assignment path below only fires
# for concepts in ALL_CONCEPTS that aren't pinned here, which happens when
# the language is extended with a new concept that hasn't yet been given a
# fixed form.
#
# To edit the lexicon: change a value here, then run `python3 gen.py`.
# To add a new concept: add it to ALL_CONCEPTS (and to its tier/class list
# if it's not the default NEUTRAL/tier-3); on the next run it gets a
# random assignment that satisfies its constraints — promote that into
# MANUAL_PINS once you're happy with it.
#
# Etymology of the language's name "yamul":
#   yam = THINK  (mental content, idea)
#   ul  = JOIN   (connect, bind, link)
#   yamul = "thoughts joined" = language
# Head-initial: THINK is the head (a cognitive thing), JOIN is the
# modifier (mutually connected). Longest-match parsing greedily takes
# *yam* first, so the etymology and the parse agree without any
# blocked-forms workaround.
# ---------------------------------------------------------------------------
MANUAL_PINS = {
    # 1. Existence & identity
    "BE": "ro", "SAME": "me", "OTHER": "ha", "ONE": "er", "MANY": "he",
    # 2. Self & other
    "SELF": "xu", "YOU": "ku", "THEY": "su", "ALL": "na", "NONE": "le",
    # 3. Space & motion
    "HERE": "we", "THERE": "da",
    "TOWARD": "hil", "AWAY": "com", "UP": "rar", "DOWN": "yim",
    "INSIDE": "yar", "OUTSIDE": "xam",
    "PATH": "keu", "STILL": "yal", "ACROSS": "kau", "AROUND": "yeor",
    # 4. Time & change
    "NOW": "ho", "BEFORE": "pu", "AFTER": "cu",
    "BEGIN": "pe", "END": "sen", "CHANGE": "pal", "CONTINUE": "man",
    "AGAIN": "rim", "SUDDEN": "sier",
    # 5. Quantity & degree
    "BIG": "sul", "SMALL": "ker", "MORE": "sil", "LESS": "to",
    "ENOUGH": "fian", "EMPTY": "gaen", "FULL": "caon",
    # 6. Quality & valence
    "GOOD": "li", "BAD": "el", "TRUE": "ra", "FALSE": "ba",
    "BEAUTIFUL": "coa", "UGLY": "neor",
    # 7. Mind & sensation
    "KNOW": "mi", "WANT": "win", "FEEL": "del",
    "SEE": "gar", "HEAR": "den", "SAY": "bil",
    "THINK": "yam", "REMEMBER": "koal",
    # 8. Action & effect
    "DO": "re", "GIVE": "rer", "TAKE": "ner",
    "JOIN": "ul", "PART": "fim", "MAKE": "kam", "BREAK": "pier",
    "CAUSE": "suer", "ALLOW": "teu", "PREVENT": "gai", "TRY": "giu",
    # 9. Substance & form
    "THING": "fer", "LIVE": "sim",
    "WATER": "fon", "FIRE": "xin", "EARTH": "bum", "AIR": "xim",
    # 10. Sensory qualities
    "HOT": "ciam", "COLD": "gao", "BRIGHT": "kae", "DARK": "miul",
    "LOUD": "taer", "QUIET": "guar", "WET": "nein", "DRY": "tal",
    "HARD": "peim", "SOFT": "boa", "SHARP": "die", "HEAVY": "xuor",
    # 11. Dimensional qualities
    "LONG": "taul", "SHORT": "coel", "WIDE": "moar", "NARROW": "pie",
    "DEEP": "rual", "HIGH": "ceim", "LOW": "nua",
    "NEAR": "raem", "FAR": "pium",
    # 12. Force & power
    "STRONG": "gaim", "WEAK": "tul", "PUSH": "wei", "PULL": "fel",
    # 13. Logical relations
    "IF": "im", "BECAUSE": "fe", "BUT": "ko", "OR": "sa",
    "WITH": "wa", "BELONG": "il",
    # 14. Modal & meta
    "POSSIBLE": "yo", "NECESSARY": "gi", "ASK": "tu",
    # 15. Social & relational
    "HELP": "hean", "HARM": "tiar", "SHARE": "rue", "TRUST": "her",
    # 16. Body
    "HEAD": "loi", "HAND": "foe", "EYE": "taor", "MOUTH": "xuim",
    "HEART": "haor", "FOOT": "xil",
    # 17. Generic categories
    "PERSON": "sem", "PLACE": "an", "TIME": "cur", "WAY": "lin",
}

# Forms that must NOT be assigned to any concept. Currently empty — *yam*
# used to live here to keep the random assigner from breaking the
# *yamul = ya + mul* parse, but now that yamul = yam + ul, that form is
# pinned (THINK) and no longer needs protection. Add forms here when
# you need to protect a future compound from accidental random assignment.
BLOCKED_FORMS = set()


# ---------------------------------------------------------------------------
# Assignment
# ---------------------------------------------------------------------------
SHARP_MIN = 2
SOFT_MAX = -2


def assign(seed=42):
    rng = random.Random(seed)
    shapes = all_iconemes()

    used = set()
    assignments = {}

    # First, place all manual pins. Validate them against constraints.
    for concept, form in MANUAL_PINS.items():
        if concept not in ALL_CONCEPTS:
            raise ValueError(f"Pinned concept {concept!r} not in ALL_CONCEPTS")
        if not is_valid_iconeme(form):
            raise ValueError(f"Pinned form {form!r} for {concept} is not a valid iconeme")
        if form in used:
            raise ValueError(f"Pinned form {form!r} duplicates an earlier pin")
        if form in BLOCKED_FORMS:
            raise ValueError(f"Pinned form {form!r} is in BLOCKED_FORMS")
        used.add(form)
        tier = concept_tier(concept)
        cls = concept_class(concept)
        assignments[concept] = (form, cls, tier, sharpness(form))

    # Block forbidden forms from being randomly chosen
    for f in BLOCKED_FORMS:
        used.add(f)

    def pool_for(tier, cls):
        allowed_shapes = TIER_SHAPES[tier]
        candidates = []
        for shape in allowed_shapes:
            candidates.extend(shapes[shape])
        if cls == "SHARP":
            candidates = [w for w in candidates if sharpness(w) >= SHARP_MIN]
        elif cls == "SOFT":
            candidates = [w for w in candidates if sharpness(w) <= SOFT_MAX]
        else:
            candidates = [w for w in candidates if -1 <= sharpness(w) <= 1]
        return candidates

    # Now fill the rest by tier order
    by_tier = {1: [], 2: [], 3: []}
    for concept in ALL_CONCEPTS:
        if concept in assignments:
            continue  # already pinned
        by_tier[concept_tier(concept)].append(concept)

    for tier in [1, 2, 3]:
        for concept in by_tier[tier]:
            cls = concept_class(concept)
            candidates = pool_for(tier, cls)
            free = [w for w in candidates if w not in used]
            rng.shuffle(free)
            chosen = free[0] if free else None
            used.add(chosen)
            assignments[concept] = (chosen, cls, tier, sharpness(chosen))

    return assignments


def write_assignment_file(assignments, path, seed):
    sharp_count = sum(1 for c in assignments if concept_class(c) == "SHARP")
    soft_count = sum(1 for c in assignments if concept_class(c) == "SOFT")
    neutral_count = len(assignments) - sharp_count - soft_count

    tier_counts = {1: 0, 2: 0, 3: 0}
    for c in assignments:
        tier_counts[concept_tier(c)] += 1

    pinned = sum(1 for c in assignments if c in MANUAL_PINS)
    random_count = len(assignments) - pinned

    with open(path, "w") as f:
        f.write("# Iconeme Assignments — draft v2\n\n")
        if random_count == 0:
            f.write(
                "All assignments below are pinned in `gen.py`. "
                "Edit `MANUAL_PINS` and re-run `python3 gen.py` to change "
                "the lexicon.\n\n"
            )
        else:
            f.write(
                f"{pinned} concepts pinned in `gen.py`; "
                f"{random_count} filled in by seeded random assignment "
                f"(seed={seed}). Promote any random pick you want to keep "
                "into `MANUAL_PINS`.\n\n"
            )
        f.write("## Constraints\n\n")
        f.write("**Sound-symbolic class** (selects iconemes with appropriate sharpness):\n")
        f.write(f"- {sharp_count} SHARP concepts (sharpness ≥ +2)\n")
        f.write(f"- {soft_count} SOFT concepts (sharpness ≤ -2)\n")
        f.write(f"- {neutral_count} NEUTRAL concepts (sharpness in [-1, +1])\n\n")
        f.write("**Frequency tier** (restricts iconeme shapes to keep common words short):\n")
        f.write(f"- Tier 1 ({tier_counts[1]} concepts): CV/VN/VL only — 2 phonemes, no vowel pair\n")
        f.write(f"- Tier 2 ({tier_counts[2]} concepts): adds CVN/CVL — 2-3 phonemes, no vowel pair\n")
        f.write(f"- Tier 3 ({tier_counts[3]} concepts): full pool, including CVV/CVVC\n\n")
        f.write("## Assignments\n\n")
        f.write("| Concept | Iconeme | Tier | Class | Sharpness |\n")
        f.write("|---------|---------|:----:|-------|----------:|\n")
        for concept, (form, cls, tier, sharp) in assignments.items():
            f.write(f"| {concept} | **{form}** | {tier} | {cls} | {sharp:+d} |\n")


# ---------------------------------------------------------------------------
# Longest-match tokenizer / glosser
# ---------------------------------------------------------------------------
# Given an assignment (concept → form), build the inverse map (form → concept)
# and split a written word back into its constituent iconemes by greedy
# left-to-right longest match. This is the canonical parser for compounds:
# it tells you how a yamul reader will hear a word, which may or may not
# match what the coiner intended. Used to verify lexicon entries.
ICONEME_MAX_LEN = 4


def build_inventory(assignments):
    return {form: concept for concept, (form, *_) in assignments.items()}


def tokenize(word, inventory, max_len=ICONEME_MAX_LEN):
    """Decompose `word` into iconemes by greedy longest match.

    Returns a list of (form, concept) on success, or None if any segment
    of `word` doesn't appear in `inventory`.
    """
    parts = []
    i, n = 0, len(word)
    while i < n:
        match = None
        for length in range(min(max_len, n - i), 1, -1):
            piece = word[i:i + length]
            if piece in inventory:
                match = piece
                break
        if match is None:
            return None
        parts.append((match, inventory[match]))
        i += len(match)
    return parts


def gloss_word(word, assignments):
    inv = build_inventory(assignments)
    parts = tokenize(word, inv)
    if parts is None:
        return f"{word}: PARSE FAILED (no iconeme matches at some position)"
    return word + " = " + " + ".join(f"{f} ({c})" for f, c in parts)


import sys


def cli_tokenize(args):
    if not args:
        print("usage: gen.py tokenize <word> [<word> ...]")
        return 2
    assignments = assign(seed=42)
    rc = 0
    for word in args:
        result = gloss_word(word, assignments)
        print(result)
        if "PARSE FAILED" in result:
            rc = 1
    return rc


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "tokenize":
        sys.exit(cli_tokenize(sys.argv[2:]))

    shapes = all_iconemes()
    total = sum(len(v) for v in shapes.values())

    print("Iconeme generator (with CVVC + frequency tiers)")
    print("=" * 50)
    for shape, forms in shapes.items():
        print(f"  {shape:5s}: {len(forms):5d} forms")
    print(f"  {'TOTAL':5s}: {total:5d} forms")
    print()

    print("Tier pool sizes (before sound-symbolic filtering):")
    for tier, allowed in TIER_SHAPES.items():
        size = sum(len(shapes[s]) for s in allowed)
        print(f"  Tier {tier}: {size:4d} iconemes from shapes {allowed}")
    print()

    print(f"Concepts to assign: {len(ALL_CONCEPTS)}")
    by_tier = {1: 0, 2: 0, 3: 0}
    for c in ALL_CONCEPTS:
        by_tier[concept_tier(c)] += 1
    for tier, count in by_tier.items():
        print(f"  Tier {tier}: {count} concepts")
    print()

    seed = 42
    assignments = assign(seed=seed)
    out = Path(__file__).resolve().parent / "iconemes.md"
    write_assignment_file(assignments, out, seed)
    print(f"Wrote assignments (seed={seed}) to: {out}")
    print()

    print("Sample assignments (most-common words first):")
    for c in ["SELF", "YOU", "THEY", "TRUE", "FALSE", "ASK", "BELONG",
              "NOW", "BEFORE", "AFTER", "IF", "BUT", "OR",
              "WATER", "FIRE", "BIG", "SMALL", "GOOD", "BAD",
              "SEE", "KNOW", "WANT",
              "BRIGHT", "DARK", "HOT", "COLD", "BREAK", "STILL"]:
        form, cls, tier, sharp = assignments[c]
        print(f"  {c:12s} -> {form:6s}  (tier {tier}, {cls}, sharpness {sharp:+d})")