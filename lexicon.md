# Lexicon — coined compounds

A starter dictionary of multi-iconeme words. Every entry has been
verified to round-trip through `gen.py`'s longest-match tokenizer:
running `python3 gen.py tokenize <word>` on any form below decomposes
back to the iconemes shown in its **Composition** column.

This file is intended as the agreed stock of coinages — once a compound
appears here, it shouldn't be re-coined ad hoc. New coinings can be
proposed and verified with `python3 gen.py tokenize <candidate>`; if the
parse matches the intended composition, add the entry under the right
category.

For the single-iconeme dictionary, see [iconemes.md](iconemes.md).

---

## Sky, weather, celestial

| Word | Composition | Meaning |
|---|---|---|
| *kaecur* | BRIGHT + TIME | day |
| *miulcur* | DARK + TIME | night |
| *kaecurpe* | BRIGHT + TIME + BEGIN | morning |
| *miulpe* | DARK + BEGIN | evening |
| *kaecurcu* | BRIGHT + TIME + AFTER | tomorrow |
| *kaecurpu* | BRIGHT + TIME + BEFORE | yesterday |
| *kaetaor* | BRIGHT + EYE | sun |
| *miultaor* | DARK + EYE | moon |
| *kaeker* | BRIGHT + SMALL | star |
| *ceimxim* | HIGH + AIR | sky |
| *fonxim* | WATER + AIR | cloud |
| *ximcom* | AIR + AWAY | wind |
| *fonyim* | WATER + DOWN | rain |
| *fongao* | WATER + COLD | snow |
| *fonpeim* | WATER + HARD | ice |
| *kaefer* | BRIGHT + THING | light |
| *miulfim* | DARK + PART | shadow |

## Land and water

| Word | Composition | Meaning |
|---|---|---|
| *fonkeu* | WATER + PATH | river |
| *fonyal* | WATER + STILL | lake |
| *fonsul* | WATER + BIG | sea |
| *bumceim* | EARTH + HIGH | mountain |
| *bummoar* | EARTH + WIDE | field, plain |
| *bumpeim* | EARTH + HARD | stone |

## Living things

| Word | Composition | Meaning |
|---|---|---|
| *simfer* | LIVE + THING | animal |
| *simximhil* | LIVE + AIR + TOWARD | bird |
| *fonsim* | WATER + LIVE | fish |
| *ceimsim* | HIGH + LIVE | tree |

Note the head-first ordering on *fonsim* vs *simfon*: WATER + LIVE is
"water-thing-that-lives" (fish), while LIVE + WATER is "life-water"
(blood — see Body, below).

## People and society

| Word | Composition | Meaning |
|---|---|---|
| *semker* | PERSON + SMALL | child |
| *semli* | PERSON + GOOD | friend |
| *semul* | PERSON + JOIN | family, bonded people |
| *semhe* | PERSON + MANY | group, crowd |
| *semceim* | PERSON + HIGH | leader |
| *semha* | PERSON + OTHER | stranger |
| *semyar* | PERSON + INSIDE | guest |

## Gender and kinship

yamul has no grammatical gender, but it can refer to gendered concepts
via the MALE / FEMALE iconemes (*tan* / *dan*) used as head-first
modifiers. The unmodified term is gender-neutral and is the default
form — gender marking is only added when context calls for it.

| Word | Composition | Meaning |
|---|---|---|
| *semtan* | PERSON + MALE | man |
| *semdan* | PERSON + FEMALE | woman |
| *semkertan* | PERSON + SMALL + MALE | boy |
| *semkerdan* | PERSON + SMALL + FEMALE | girl |
| *sempu* | PERSON + BEFORE | parent |
| *semputan* | PERSON + BEFORE + MALE | father |
| *sempudan* | PERSON + BEFORE + FEMALE | mother |
| *semcu* | PERSON + AFTER | offspring |
| *semcutan* | PERSON + AFTER + MALE | son |
| *semcudan* | PERSON + AFTER + FEMALE | daughter |
| *semme* | PERSON + SAME | sibling |
| *semmetan* | PERSON + SAME + MALE | brother |
| *semmedan* | PERSON + SAME + FEMALE | sister |

The same MALE/FEMALE modifier composes onto any noun where gender
matters — for example *simfer tan* "male animal," *simfer dan* "female
animal" — but those needn't be lexicalized.

## Body

| Word | Composition | Meaning |
|---|---|---|
| *denfer* | HEAR + THING | ear |
| *loifer* | HEAD + THING | hair |
| *foefim* | HAND + PART | finger |
| *foetaul* | HAND + LONG | arm |
| *xiltaul* | FOOT + LONG | leg |
| *xamfim* | OUTSIDE + PART | skin |
| *ceimfim* | HIGH + PART | face, surface |
| *peimyar* | HARD + INSIDE | bone |
| *simfon* | LIVE + WATER | blood |
| *simxim* | LIVE + AIR | breath |

## Dwelling and path

| Word | Composition | Meaning |
|---|---|---|
| *bumyar* | EARTH + INSIDE | house |
| *keuyar* | PATH + INSIDE | door |
| *keutaul* | PATH + LONG | road |

## Action and motion

| Word | Composition | Meaning |
|---|---|---|
| *rehil* | DO + TOWARD | go, walk |
| *gaimhil* | STRONG + TOWARD | run |
| *yalxim* | STILL + AIR | hover, float |
| *yimyal* | DOWN + STILL | sit |
| *yalrar* | STILL + UP | stand |
| *yalman* | STILL + CONTINUE | sleep |
| *yalyam* | STILL + THINK | dream |
| *pegar* | BEGIN + SEE | wake |
| *nerxuim* | TAKE + MOUTH | eat |
| *fonner* | WATER + TAKE | drink |
| *yimre* | DOWN + DO | fall |
| *rarre* | UP + DO | rise |
| *reman* | DO + CONTINUE | work |
| *kamfer* | MAKE + THING | build, construct |
| *kambil* | MAKE + SAY | write |
| *garbil* | SEE + SAY | read |

The motion pair *yimre* / *rarre* is direction-first: putting *re* (DO)
first would form *reyim* / *rerar*, and *rerar* in particular fails to
parse — longest-match greedily takes *rer* (GIVE), stranding *ar*. The
direction-first ordering is the one that survives the tokenizer.

## Objects

| Word | Composition | Meaning |
|---|---|---|
| *xuimfer* | MOUTH + THING | food |
| *foefer* | HAND + THING | tool |

## Mind and feeling

| Word | Composition | Meaning |
|---|---|---|
| *yamfer* | THINK + THING | idea |
| *yamrer* | THINK + GIVE | message |
| *yamyar* | THINK + INSIDE | consider, ponder |
| *garmi* | SEE + KNOW | recognize |
| *tulman* | WEAK + CONTINUE | tired |
| *rowa* | BE + WITH | have |
| *bilfer* | SAY + THING | word |
| *biltu* | SAY + ASK | question |
| *bilman* | SAY + CONTINUE | story |
| *bilba* | SAY + FALSE | lie |
| *winyo* | WANT + POSSIBLE | hope |
| *deltiar* | FEEL + HARM | fear |
| *delxin* | FEEL + FIRE | anger |
| *delli* | FEEL + GOOD | joy |
| *delul* | FEEL + JOIN | love |
| *yalli* | STILL + GOOD | peace |
| *tiaryo* | HARM + POSSIBLE | dangerous |

## Religion and cosmology

| Word | Composition | Meaning |
|---|---|---|
| *kamna* | MAKE + ALL | God, creator-of-all |
| *pecur* | BEGIN + TIME | the beginning |


## Quantity, time, and place expressions

| Word | Composition | Meaning |
|---|---|---|
| *nacur* | ALL + TIME | always |
| *lecur* | NONE + TIME | never |
| *tocur* | LESS + TIME | sometimes |
| *hecur* | MANY + TIME | often |
| *nayeor* | ALL + AROUND | everywhere |
| *toan* | LESS + PLACE | somewhere |
| *lean* | NONE + PLACE | nowhere |
| *nafer* | ALL + THING | everything |
| *tofer* | LESS + THING | something |
| *lefer* | NONE + THING | nothing |
| *nasem* | ALL + PERSON | everyone |
| *tosem* | LESS + PERSON | someone |
| *lesem* | NONE + PERSON | no one |

There's no direct ALL + PLACE compound: *naan* (NA + AN) would
concatenate two /a/ vowels across the iconeme boundary, which the
phonology doesn't admit, and reversing the order to *anna* gives a
geminate /nn/, which is also excluded. *nayeor* (ALL + AROUND) covers
the intended meaning without that collision.
