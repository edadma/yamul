# yamul

A constructed natural language. In English the name is a backronym
for **y**et **a**nother **m**ade-**u**p **l**anguage; in yamul itself
it parses as *yam* + *ul* = THINK + JOIN = "thoughts joined" and is
the language's own word for *language*.

yamul is built around **iconemes** — short phoneme sequences carrying
a vague semantic hue, combined head-first into compound words. Each
phoneme has a sound-symbolic weight on the bouba/kiki axis, so WATER
ends up feeling watery (*fon*), FIRE feels fiery (*xin*), and so on.

## Files

- **[design.md](design.md)** — design philosophy, iconeme system,
  sound-symbolic palette, open issues
- **[grammar.md](grammar.md)** — phonology, writing system, sentence
  grammar, sample sentences
- **[iconemes.md](iconemes.md)** — single-iconeme dictionary
- **[lexicon.md](lexicon.md)** — compound-word dictionary, all
  tokenizer-verified
- **[examples.md](examples.md)** — sentence catalogue organised by
  grammatical device, plus proposed subordinator extensions
- **[genesis.md](genesis.md)** — Genesis 1:1–5 in yamul, with
  commentary on what each verse forced the language to invent
- **[gen.py](gen.py)** — generates iconemes.md from a pinned data
  table, and exposes `python3 gen.py tokenize <word>` for verifying
  new coinings under longest-match parsing
