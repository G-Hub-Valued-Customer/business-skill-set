# GROUP 3: THE SCOPE HIERARCHY

TAXONOMY SHAPE, SCOPE_LEVELS. An ordered containment chain, coarsest first. Each
level carries:
- `key`: stable id, never renamed.
- `display_name`: the word the business actually uses.
- `rank`: 0 for the whole organization, increasing as the unit narrows.
- `id_width`: unpadded digit or character count of a code at this level, or null
  where codes are not numeric.
- `column_concepts`: the concept keys in COLUMN_CONCEPT_DICTIONARY that may hold
  this level.
- `peer_level`: the level whose sibling units form the peer set for a unit at
  this level. Normally the level one step coarser.
- `is_owned_by_roles`: the role keys whose own scope is this level. **The FINEST
  level, the unit level, carries an EMPTY list. Nobody's scope is one row**, and a
  role recorded as owning it is reported as a binding error under SD-POP-26.

The depth is configuration. Two levels is legal. Six is legal. Nothing in the
method assumes four.

**THE CHAIN ENDS AT THE THING BEING RANKED, NOT AT THE SMALLEST THING ONE PERSON
OWNS. THOSE ARE TWO DIFFERENT LEVELS AND CONFLATING THEM SUPPRESSES A FRONTLINE
READER'S ENTIRE LIST.** The LAST level of SCOPE_LEVELS is the level at which ONE
ROW of the ranked population sits: one account, one claim, one site, one work
order. The finest level anybody OWNS is the level immediately ABOVE it, and it has
its own name, SCOPE_FINEST_KEY. Two concepts, two variables, and they are never
the same level on a chain of more than two.

**WHY THE OLD WORDING WAS WRONG, STATED IN FULL SO NOBODY RESTORES IT FROM
INSTINCT.** An earlier revision defined this chain as running to the finest OWNED
unit, and the interview asked for it in those words. Answer that honestly at an
organization whose smallest owned thing is one person's book and the chain is
organization, region, branch, book, and it STOPS THERE. UNIT_LEVEL_KEY is then
detected as the level whose distinct value count over the in-scope population
equals that population's record count. Over one producer's forty-eight accounts,
book has one distinct value, branch one, region one, organization one. NO LEVEL
EQUALS FORTY-EIGHT. The detection falls to its documented fallback, the finest
level in the chain, which is the BOOK, which is also the reader's own level. The
run then concludes that the reader's scope holds exactly one unit and suppresses
the ranked list, the percentile and every comparative sentence, on a reader with
forty-eight live units. No gate catches it: the funnel reconciles, every invariant
passes, and the artifact is internally consistent and wrong.

**AND IT BREAKS THE ROLE ANCHOR IN THE OTHER DIRECTION AT THE SAME TIME.**
ROLE_LADDER.scope_level anchors the most junior role at the level immediately
COARSER than UNIT_LEVEL_KEY. With UNIT_LEVEL_KEY wrongly resolved to the book, the
most junior role is anchored on the BRANCH, so a producer is recorded as owning a
branch and their claims are worded at AGGREGATE strength. SD-SPN-09 calls that
fatal in both directions, and here one bad chain produces both directions at once.

**ON A CHAIN THAT ENDS AT THE UNIT, THE SAME DETECTION IS CORRECT ON THE FIRST
TRY.** The unit level has forty-eight distinct values over forty-eight records,
the test matches, the fallback never fires, and when it does fire it lands on the
unit level, which is the right answer rather than the catastrophic one.

**THE TEST A BINDING OWNER CAN APPLY IN ONE SENTENCE.** Read the last level of the
chain aloud and ask: is ONE of these ONE LINE on the report? If a person can own
several of them, it is not the last level and the chain is one level short.

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| SCOPE_LEVELS | The ordered containment chain from the whole organization DOWN TO AND INCLUDING the level at which one ranked unit sits. It does NOT stop at the finest owned unit; that level is one step coarser and is named separately by SCOPE_FINEST_KEY. | ORG | IGNITION | taxonomy | At least 2 levels. Ranks strictly increasing, no gaps. Every level key unique. THE FINEST LEVEL IS THE UNIT LEVEL: UNIT_LEVEL_KEY resolves to it, and no role's scope_level may be it. | Region; District; Branch; Adjuster Book; Claim |
| SCOPE_TOP_KEY | The key of the level that means no filter at all. | ORG | DEFERRED | scalar | Must be a key in SCOPE_LEVELS with rank 0. | enterprise |
| SCOPE_FINEST_KEY | The key of the finest OWNED level: the smallest thing one person's scope covers. It is NOT the last level of the chain, which is the unit itself. | ORG | DEFERRED | scalar | Must be a key in SCOPE_LEVELS, and must be the level immediately COARSER than UNIT_LEVEL_KEY. On a chain of exactly 2 levels it is the rank-0 level. | adjuster_book |
| SCOPE_CODE_SCHEME | Whether scope codes are hierarchical strings, opaque ids, or absent. | ORG | DEFERRED | scalar | One of: hierarchical, opaque, none. | hierarchical |
| SCOPE_CODE_WIDTH | Total width a code is padded to when the scheme is hierarchical. | ORG | CONDITIONAL | scalar | Positive integer. Required when SCOPE_CODE_SCHEME is hierarchical. | 8 |
| SCOPE_CODE_PAD_DIRECTION | Which end a short code is padded on. | ORG | CONDITIONAL | scalar | One of: right, left. Required when the scheme is hierarchical. | right |
| SCOPE_CODE_PAD_CHARACTER | The padding character. | ORG | CONDITIONAL | scalar | Exactly one character. | 0 |
| SCOPE_LEVEL_ID_WIDTHS | Map from scope level key to its unpadded code width. | ORG | CONDITIONAL | mapping | Widths strictly increasing with rank. Required when the scheme is hierarchical. | region 1; district 3; branch 5; book 8 |
| SCOPE_CODE_AMBIGUITY_THRESHOLD | Count of trailing pad characters at or above which a code is ambiguous between levels and must be resolved against the data. | ORG | CONDITIONAL | scalar | Integer, at least 2, at most SCOPE_CODE_WIDTH minus 1. Derived from the widths above and never hard-coded independently. | 4 |
| SCOPE_PLAIN_LANGUAGE_MAP | Phrases a person may type, mapped to a scope level and, where fixed, a code. | ORG | DEFERRED | mapping | Every value names a level key present in SCOPE_LEVELS. SEED, extended at runtime. | my branch; the whole district; everything; my book |
| WIDE_SCOPE_TOKENS | Title tokens that name a scope wider than a front-line role and therefore outrank a junior role word. | ORG | DEFERRED | list | At least 1 entry. Lowercased, punctuation stripped. | region; regional; division; national; enterprise; group |
| SCOPE_ATTRIBUTION_IS_TREE | Whether every unit of business belongs to exactly one owner at each level. | ORG | DEFERRED | scalar | Boolean. False means the span-of-control block holds a set per unit rather than a single value. | true |
| SPAN_BLOCK_MAX_COLUMNS | Ceiling on how many scope columns the span-of-control block may add before the skill reports the block as wide rather than dropping columns. | ORG | OPTIONAL | scalar | Integer at least 1. Defaults to the depth of SCOPE_LEVELS MINUS ONE, because the finest level of the chain is the unit itself and a unit is a row rather than a span column. | 4 |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 3: The scope hierarchy

| Variable | Documented default | Degradation notice |
|---|---|---|
| SCOPE_LEVELS.rank | DERIVED from the ORDER the answerer gave: 0 for the level they named first, increasing by one as the unit narrows. | The ranks were taken from the order you listed the levels in rather than stated separately. |
| SCOPE_LEVELS.id_width | DERIVED from the data: the modal character count of the codes actually present at that level, or null where the codes are not fixed width. Where no data has been seen, null, and no padding is attempted. | Code widths were read from your file rather than declared, so a short code is padded only where every other code at that level is the same length. Where nothing could be read, no padding is attempted and a short code resolves only if it appears in the file exactly as given. |
| SCOPE_LEVELS.column_concepts | DERIVED: the scope concepts in COLUMN_CONCEPT_DICTIONARY that resolved to a column whose distinct values nest inside the next coarser level's values. | Which columns hold each level was read from your file rather than declared, by testing which columns nest inside which. The columns chosen are named in the audit. |
| SCOPE_LEVELS.peer_level | DERIVED: the level one step coarser, so a unit is compared with its siblings and never with its own children. At the top level the peer set is EMPTY and no peer comparison is attempted. | Peer groups were not stated, so each unit is compared with the other units under the same parent one level up. Nothing at the top of the hierarchy is given a peer comparison at all. |
| SCOPE_LEVELS.is_owned_by_roles | DERIVED: the inverse of ROLE_LADDER.scope_level, computed once and checked for consistency in both directions. | Which roles own which levels was not stated separately; it was inverted from the role list. |
| SCOPE_TOP_KEY | The rank-0 level in SCOPE_LEVELS. | Derived from the bound hierarchy rather than stated. |
| SCOPE_FINEST_KEY | The level immediately COARSER than UNIT_LEVEL_KEY, which on a well formed chain is the SECOND-highest rank in SCOPE_LEVELS. Never the highest-rank level: that level is one unit of business, and nobody's scope is one row. Where the chain holds exactly two levels, the rank-0 level. | The smallest thing anybody owns was derived from the bound hierarchy rather than stated: it is the level immediately above the one a single {unit noun} sits at. If your chain was written to stop at the smallest owned thing rather than at one {unit noun}, this derivation returns the wrong level and the ranked list is suppressed for every frontline reader; the chain is what to fix, and GROUP 3 says how. |
| SCOPE_CODE_SCHEME | Detected from the data: if every finer code in the file carries a coarser code as a left-anchored prefix, hierarchical; otherwise opaque, matched exact. | The code scheme was detected from the file rather than declared. Plain-language scope requests resolve only against codes actually present, and a short code will not be padded. |
| SCOPE_PLAIN_LANGUAGE_MAP | Empty. Scope phrases resolve only against the distinct values present in the file. | No plain-language scope phrases have been bound, so a request such as a scope named in ordinary words is resolved against the values in the file and, if it fails, you are offered the values present. |
| WIDE_SCOPE_TOKENS | The generic set: region, regional, division, national, enterprise, group, area, zone, country. | No organization-specific wide-scope title words have been bound, so a generic list was used. A senior title using local vocabulary may be read at too narrow a scope; the token that decided the role is named in the audit. |
| SCOPE_ATTRIBUTION_IS_TREE | true, meaning each unit is assumed to have exactly one owner at each level. | Unit ownership is assumed to be single-owner at each level. If units in your organization are jointly owned, the attribution column shows only one owner and undercounts shared work. |

---

## CONDITIONAL DEFAULTS AND NOTICES ONCE TRIGGERED, FOR THIS GROUP

Moved here from APPENDIX A2 for the same reason. The text is unchanged.

### Group 3: The scope hierarchy

| Variable | Trigger | Documented default | Degradation notice |
|---|---|---|---|
| SCOPE_CODE_WIDTH | SCOPE_CODE_SCHEME resolves to hierarchical | The longest code observed in the data at the finest level. | The total width of a scope code was detected from your data rather than declared, so a code shorter than the widest one seen is padded to that width. The width used is named in the audit. |
| SCOPE_CODE_PAD_DIRECTION | as above | Right, because a hierarchical code is read left to right and a coarser code is a left-anchored prefix of a finer one. | The padding direction was assumed rather than declared. If your codes pad on the other end, a short code will not resolve and you will be offered the values present instead. |
| SCOPE_CODE_PAD_CHARACTER | as above | The character zero. | The padding character was assumed. A code that pads with anything else will not resolve and you will be offered the values present. |
| SCOPE_LEVEL_ID_WIDTHS | as above | Detected: for each level, the length of the shortest distinct code observed at that level. | Code widths per level were detected from your data rather than declared, so a level whose codes vary in length may be read at the wrong level. Every ambiguous code is resolved against the data rather than against its pattern, and the level chosen is named. |
| SCOPE_CODE_AMBIGUITY_THRESHOLD | as above | Derived from the detected widths: the count of trailing pad characters at which two levels become indistinguishable. | Derived rather than declared. A code at or above that many trailing pad characters is resolved by testing it against each level's own column and taking the level that returns rows, never by its pattern. |
