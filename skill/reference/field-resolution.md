# FIELD RESOLUTION

How the bundle finds the data it needs inside a file it has never seen.

This file is the generalized form of the column-resolution appendix from the
planning skill. It is shared by all three skills, because all three read the same
kind of file and all three fail the same way when they read it by literal header.

---

# PART 0: THE GENERAL RULE

**F0. Fields resolve by CONCEPT, never by literal header.**

The skill never asks "is there a column called X". It asks "which column, if
any, holds the concept the method needs here", and it answers that question with
a dictionary of stems, a set of matching passes, and a check against the
column's own values.

Three consequences follow, and they are the reason the rule exists:

- **F0.1. The source is never the same shape twice.** Two exports of the same
  file five months apart will differ on the header row position, the sheet count,
  the naming of the same column, the measure basis, the identifier type, the
  presence of a work-item block, the presence of a status flag and the total
  column count. A resolver written against literals breaks on the second file and
  breaks silently.
- **F0.2. A header that does not resolve is a skill defect, not a user error.**
  Log the literal, continue with what did resolve, name it in the audit section,
  and register the stem so the next person is never asked.
- **F0.3. The dictionary is a starting point, not a specification.** Everything
  in Part 6 is SEED data. It is expected to be incomplete on first contact with
  any real business, and the mechanism for extending it at runtime is Part 7.

**F0.4. The portability test.** Hold two real exports of the same source from
different periods. A change to this dictionary that would break either one is
wrong. Run both before shipping any change.

---

# PART 1: SHEET AND CONTAINER SELECTION

Applies to any multi-container source: a workbook with several sheets, an export
with several tables, a database response with several result sets.

### F1.1 Never take the first container on faith
Score every candidate. Do not read the first one and proceed.

### F1.2 Score by resolvable REQUIRED concepts, not by name
For each container, attempt to resolve the three required concepts: the unit
identifier, a ranking measure, and any one scope column. The score is the count
resolved. A container that resolves all three is a candidate; one that resolves
fewer is not.

### F1.3 A name match still needs a column check
A container whose name matches the expected source name is taken only after
confirming it resolves the required concepts, and falls through if it does not.
A name is a hint, never evidence.

### F1.4 Break ties by RECORD COUNT, never by the reported extent
Count rows carrying a non-blank identifier. The reported extent of a container
routinely overstates the real record count by thousands, because trailing
formatting and phantom rows are counted in the extent and not in the data.

### F1.5 Ignore documentation-named containers
A container named for notes, a glossary, definitions, a legend, a cover page,
instructions or a change log is documentation. Score it zero and move on.

### F1.6 A container named after a person is a working extract
It is somebody's filtered copy, not the data. Score it below any
non-person-named candidate that resolves the same concepts, and take it only if
nothing else does. Record that a working extract was used.

### F1.7 Concatenate only when one container is genuinely not enough
Where no single container covers the requested scope, take every container whose
resolved column set matches, concatenate them, de-duplicate on the identifier
keeping the highest-measure row, and MERGE the survivors' signals into it: a
flag on any duplicate is a flag on the merged row, a match on any row matches the
merged row, and a populated field on any row fills a blank on the base. Report
how many containers were combined and how many duplicates collapsed.

### F1.8 Name the container in the audit
Record which container was selected, its score, its record count, and the score
and record count of the runner-up. A silent wrong-container pick produces a
complete, confident, entirely wrong artifact, which is the worst failure this
method has.

---

# PART 2: HEADER ROW DETECTION

### F2.1 Detect, never assume
Read the first HEADER_SCAN_DEPTH rows. A fixed header assumption breaks on the
next period's export.

### F2.2 Score by non-empty STRING cells
For each candidate row, count cells that are non-empty AND are text rather than
numbers or dates. Take the highest score.

### F2.3 Tie-breaks, in order
1. All values in the row are distinct.
2. The row contains no numeric cells.
3. There is at least one non-empty row beneath it.
4. Topmost.

### F2.4 Confirm before accepting
Attempt to resolve the required concepts against the chosen row. If they do not
resolve, fall to the runner-up and try again before asking anything.

### F2.5 Record the choice and the runner-up
Both go in the audit, with their scores.

### F2.6 Rows above the header are metadata, never data
A count row, a banner, a period stamp or a total row above the header is
structural information. It may be read as a marker. It is never scored, and a
count row scoped to the whole organization is never used as a local statistic.

---

# PART 3: MATCHING

## 3.1 Normalization, applied to both sides before any comparison

In this order:

1. Casefold.
2. Collapse underscores, hyphens, slashes, periods and other punctuation to
   single spaces.
3. Collapse runs of whitespace to one space, and trim.
4. Strip parenthetical unit and period tokens.
5. Strip a leading originator prefix, where ORIGINATOR_PREFIX_MAP defines one.
6. Strip a trailing period token from MEASURE_LOOKBACK_TOKENS.
7. Strip a trailing rate marker from MEASURE_RATE_TOKENS, and RECORD which one
   was found. The rate marker is the time basis and must be reported even though
   it is stripped for matching.

Protect sentinels before step 2. An alias that is a common short word on its own,
or that carries meaningful punctuation, is replaced by a sentinel token BEFORE
punctuation is stripped, then matched as the sentinel. Never register the bare
remainder as an alias.

## 3.2 Route before you match

Classify a phrase or a target concept to a column FAMILY first, then search only
that family's columns. Never run a match across the whole sheet.

Whole-sheet substring matching is how a flag column reading like a task name gets
attributed to a measure, and how an area name lands in a locality column.

Classify on two axes at once, because a single label routes flags into
arithmetic:

- **entity**: which creditable entity, benchmark population, outside party, or
  none.
- **measure type**: rate or volume; proportion; count; flag; identity; date;
  text.

Only a column typed as rate or volume may enter arithmetic. A column that names
an entity and is typed as a flag is never a measure.

## 3.3 The three passes, each run to completion before the next

Across the whole header list:

1. **Exact** on the normalized strings.
2. **Prefix**, bidirectional.
3. **Substring**, bidirectional.

Run each pass to completion over every stem before starting the next, so an exact
match anywhere in the container always beats a substring match anywhere else.
Within a pass, first hit wins and ties prefer the leftmost column, subject to
3.5.

### 3.3a PASS ZERO: a header matching a BOUND name is matched before any seed stem

**A NAME THE ORGANIZATION BOUND OUTRANKS EVERY STEM THIS BUNDLE SHIPPED.** Before
the three passes run, match every header against the DISPLAY NAMES AND KEYS THE
ORGANIZATION ACTUALLY BOUND, exactly and then by prefix, in this order:

| Order | Bound names matched | Concept the header resolves to |
|---|---|---|
| 1 | SCOPE_LEVELS display names and keys | the scope concept for THAT level, by its rank |
| 2 | POPULATION_SHAPE unit_singular and unit_plural | the unit identifier or unit name concept, by shape |
| 3 | ROLE_LADDER display names | the scope concept for that role's scope_level |
| 4 | MEASURE_UNIT_TOKENS and the bound measure name | the tier-1 measure concept |
| 5 | Any other bound taxonomy display name whose variable names a concept | that concept |

**WHY IT IS PASS ZERO AND NOT A FALLBACK.** An organization that has just told the
interview its levels are called by a particular set of words, and then hands over a
file with a column headed one of those exact words, has already answered the
question the seed dictionary is guessing at. The observed cost of not having this
rule: a bound level name appeared as a column header, matched no seed stem in any
scope concept, and the frontline user's own scope column was invisible, so a person
could not be scoped to their own book at a company that had just named that level
in the interview. The precedence rule already says a bound value outranks a
default, per SD-CTR-24, and the seed dictionary is a default. This rule is that
precedence applied where it was missing.

**HOW A MATCH IS SCORED, AND THE DISTINCTION IS LOAD BEARING.** A bound name
matches a header in one of exactly two ways, and they do different things:

| Kind | Test | What it determines |
|---|---|---|
| EXACT | the whole normalized header equals the bound name | the CONCEPT. The header is that thing. |
| PREFIX WITH RESIDUE | the bound name is a leading run of whole tokens and at least one token remains | the SUBJECT ONLY, never the concept. The residue carries the meaning and the three seed passes decide it. |

**A BOUND NAME THAT MATCHES ONLY PART OF A HEADER DOES NOT GET TO NAME THE WHOLE
COLUMN.** A bound unit noun prefixes the header of the identifier column, the name
column and the status column alike, and those are three different concepts. What
the prefix establishes is that all three are ABOUT the unit; what the residue
establishes is which of the three each one is. So a pass-zero prefix match records
the subject, hands the header to the three seed passes, and NARROWS them: a
concept whose subject contradicts the established one is refused. It never resolves
the header on its own.

**THE GUARDS, and all four are mandatory.**

1. A pass-zero match is still subject to the forbidden-neighbour refusal of 3.7
   and to the value check of 3.6, so a bound name cannot force a column of the
   wrong shape into a concept.
2. **TWO BOUND NAMES THAT RESOLVE TO THE SAME CONCEPT ARE CORROBORATION, NOT
   AMBIGUITY, AND THE HEADER RESOLVES.** Record both sources. Refusing a header
   because two independent parts of an organization's own configuration AGREE about
   it is the exact opposite of what precedence is for.
3. **ONLY TWO BOUND NAMES POINTING AT DIFFERENT CONCEPTS ARE A REAL TIE.** There
   the bound-name resolution is refused and both candidates are named.
4. **A PASS-ZERO REFUSAL REMOVES THE BOUND-NAME RESOLUTION ONLY. IT IS NEVER
   TERMINAL.** The header then goes to the three seed passes exactly as though no
   bound name had matched it. A tie between two of the organization's own words
   must never cost a header that a shipped stem would have resolved, and it must
   never refuse a run.

**WHEN ARE TWO TARGETS THE SAME CONCEPT.** Either of these, and both are ordinary
rather than exotic:

- They are literally the same concept key. This is what happens whenever a role is
  named after the level it owns, which is the normal naming convention in field
  organizations, so orders 1 and 3 agree.
- One is the scope concept for the level that EQUALS UNIT_LEVEL_KEY, and the other
  is the unit identifier concept. **At the unit level those are the same column.**
  This is not a coincidence to be tolerated; it is forced by the schema, because
  UNIT_LEVEL_KEY must be a key in SCOPE_LEVELS, so the unit noun equals the finest
  scope level's display name at nearly every organization, and orders 1 and 2 agree.

**WHY THIS GUARD HAD TO BE REWRITTEN, RECORDED SO IT IS NOT RE-TIGHTENED.** As
first written, the guard refused any header matched by two bound names, by analogy
with a strict tie. Both cases above are the NORMAL case rather than the exceptional
one, so the guard fired on the ordinary shape of an ordinary organization and
refused the very headers pass zero was built to resolve. Read literally it left the
REQUIRED unit identifier unresolved, which fails the source admission test and
refuses the run outright on an ordinary file; and it left the status column
unresolved, which returns every never-started unit to the ranked list, one of them
to the top of it. A guard that fires on the normal case is not a guard, it is a
fault.

**THE GUARD, VERIFIED RATHER THAN ASSERTED.** SD-POP-29 requires that a rule whose
notice names example inputs runs them and prints the results. Against an ordinary
five-level chain whose finest level is the unit, with roles named for the levels
they own:

| Header | Bound names that matched | Pass-zero outcome | Final concept |
|---|---|---|---|
| Producer | level display name, level key, role display name, all three pointing at the SAME scope concept | RESOLVED, CORROBORATED | the scope concept for that level |
| Account ID | level name and key pointing at the unit-level scope concept, unit noun pointing at the unit identifier, which are the SAME concept at the unit level | SUBJECT ONLY, residue decides | the unit identifier, by exact seed stem |
| Account Name | as above | SUBJECT ONLY, residue decides | the unit name, by exact seed stem |
| Account Status | as above | SUBJECT ONLY, residue decides | the not-actionable flag, by exact seed stem |
| A level name that a role of a DIFFERENT level is also named for | two bound names pointing at TWO DIFFERENT scope concepts | REFUSED AT PASS ZERO, both named | whatever the three seed passes make of it, and the run continues |

Four of the five resolve, and the fifth is refused without being terminal. The
first row is the case pass zero exists for: no seed stem reaches that header at
all, so without pass zero the frontline reader's own scope column is invisible.
The middle three are the case the first version of the guard broke: the required
identifier and the status column both resolve correctly, by the seed dictionary,
with the bound names narrowing rather than deciding.

**RECORD IT AS PASS ZERO in the audit**, naming the bound variable that supplied
the name, whether the match was EXACT or PREFIX, whether two names corroborated,
and where a tie was refused, so a reader can see the resolution came from their own
configuration rather than from this bundle's vocabulary.

**AND FEED IT BACK.** A header resolved at pass zero is offered as a learned stem
under Part 7, so the organization's own words enter the dictionary rather than
being rediscovered every run.

## 3.4 The short-string guard

Whenever either side is shorter than MIN_STEM_LENGTH normalized characters, only
an exact match counts. Fuzzy matching on a two or three character stem will match
any header that happens to contain those letters, and one such hit silently
mis-maps the lookup key the whole artifact is built on. Exact matching is never
suppressed by this guard.

## 3.5 The leftmost tie-break is a live trap; test the own-measure stems first

A generic leftmost tie-break systematically produces the wrong answer where a
wider population's column sits immediately to the left of the entity's own
column, which is a common export layout.

The rule: for any concept that has both an OWN form and a WIDER form, test every
own-measure stem to exhaustion before considering a wider stem. If only a wider
measure exists, say so plainly and never present it as the entity's own figure.

## 3.6 Confirm a resolved column by its VALUES, not only by its name

**ONE VOCABULARY, AND IT IS THIS ONE.** The classifier below emits exactly one
SHAPE TOKEN per column, from the closed set named here. Every concept's
`value_check` in the seed dictionary is a SET OF THESE TOKENS and nothing else.
The two are not two opinions about what a column is; they are a measurement and a
declaration, in the same units. See the precedence rule below, which exists
because an earlier revision had them in two different vocabularies and a reader
had to prefer one to proceed.

**THE LADDER IS RUN IN THE CONTEXT OF THE CONCEPT BEING TESTED**, first match
wins, and where the concept's permitted set includes DATE the two date rungs are
tried FIRST. Run it on a sample of the resolved column:

| # | Value shape | SHAPE TOKEN |
|---|---|---|
| 1 | Every non-null value is exactly four digits and inside YEAR_PLAUSIBLE_RANGE, and the concept under test permits DATE | DATE, granularity YEAR |
| 2 | Parses as a date across the known formats | DATE |
| 3 | All digits, consistent length, AND either near-unique across rows or at least IDENTIFIER_MIN_WIDTH characters wide | IDENTIFIER_OR_CODE |
| 4 | **Consistent length or a consistent pattern, AND at least one of: letters and digits both present in every value, or a separator character in every value at the same position.** Worked shapes: a letter prefix with a number; a number with a checksum letter; a segmented code with a separator; a short all-letter code carrying a separator. Consistent length ALONE is never sufficient, because that types every fixed-width category column as an identifier. | IDENTIFIER_OR_CODE |
| 5 | Two-valued after normalization, or drawn from a two-member set such as true and false, yes and no, one and zero | BOOLEAN_LIKE |
| 6 | Decimal between 0 and 1 | RATE_OR_PROPORTION |
| 7 | Bare number above 1, or all digits of a width below IDENTIFIER_MIN_WIDTH with many repeats | COUNT_OR_MEASURE |
| 8 | Short repeating value set, more than two members | STATUS_OR_CATEGORY |
| 9 | Anything else | FREE_TEXT |

**RUNG 4 IS THE ONE THAT WAS MISSING, AND ITS ABSENCE COULD STOP A RUN.** An
identifier of the form three letters, a hyphen and five digits is the commonest
identifier shape there is. Without rung 4 it is not digits, not a number, not
two-valued, not short-repeating and not a date, so it fell to FREE_TEXT, the
REQUIRED unit-identifier concept failed its own value check on an EXACT header
match, no alternative candidate resolved by name, and a literal reading refused
the only required concept in the file and stopped the run on an ordinary book of
business. Rung 4 is tested BEFORE the free-text rung and it is not optional.

**RUNG 3'S SECOND CONDITION IS ALSO LOAD BEARING.** Digits of consistent length
alone made every small integer column an identifier: a count of two or three
policies, a count of open items, a bare year. The distinctness-or-width test
separates a code from a count without a special rule per column, and a column that
fails it falls through to rung 7, which is where a count belongs.

A column that resolves by name but fails its concept's `value_check` is the wrong
column. Fall through to the next candidate and record both, the rejected one and
the reason.

The operative case: a header that says measure and whose values are decimals
between 0 and 1 is a rate, not a measure, and the header is misleading. Trust the
values.

### 3.6a Precedence: which governs when the classifier and a value_check disagree

They cannot disagree about WHAT AN IDENTIFIER LOOKS LIKE, because only one of them
defines it. Stated as three rules, in order:

1. **THE CLASSIFIER DEFINES THE SHAPES. THE VALUE_CHECK SELECTS AMONG THEM.** The
   classifier is a measurement of the data and it is the only place a shape is
   defined. A `value_check` is a declaration by a concept about which measured
   shapes it accepts. A column PASSES its value check when the classifier's token
   for it is in that concept's permitted set, and fails otherwise. There is no
   second definition of "identifier" anywhere in this bundle, and no concept may
   introduce one in prose.
2. **A VALUE_CHECK NAMING A SHAPE THE CLASSIFIER CANNOT EMIT IS A DEFECT IN THE
   DICTIONARY, AND IT NEVER FAILS A COLUMN.** Where a value_check names an
   unrecognized shape, the resolver records a DICTIONARY DEFECT naming the concept
   and the unrecognized token, treats that clause as UNSATISFIABLE RATHER THAN
   FAILED, and continues on the clauses it can evaluate. A vocabulary mismatch
   between two parts of this bundle is never allowed to refuse a user's column.
   That is the failure this rule exists to prevent: the bundle disagreeing with
   itself and the run paying for it.
3. **A REQUIRED CONCEPT IS NEVER REFUSED ON SHAPE ALONE WHEN THE NAME MATCHED
   EXACTLY AND NOTHING ELSE IS AVAILABLE.** Where all of: the concept is required;
   the header was an EXACT stem match; no other candidate resolves for that
   concept by name or by shape; and the observed shape is one that is only ever
   CARRIED, compared or printed rather than computed with, then take the column,
   and print a SHAPE CONFLICT notice naming the concept, the header, the expected
   set and the observed token. The choice there is between running with a
   disclosed conflict and not running at all, and refusing the run is the worse
   error by a wide margin.

   **THE GUARD ON RULE 3, AND IT IS ABSOLUTE: IT NEVER APPLIES TO A MISMATCH THAT
   CHANGES ARITHMETIC.** A column whose observed token is RATE_OR_PROPORTION where
   COUNT_OR_MEASURE was expected, or the reverse, is REFUSED as before, however
   exact the header and however required the concept, because taking it changes
   every number computed from it and the disclosure cannot repair that. The
   relaxation covers identifiers, names, codes, categories and dates, which are
   carried rather than multiplied. "Trust the values" is untouched for the case it
   was written for.

**THE BARE-YEAR TRAP, AND IT COSTS A WHOLE TEST.** A column of four-digit years
matches "all digits, consistent length" and classifies as an identifier or code
BEFORE the date rung is ever reached, so a column that plainly holds a date is
rejected as the wrong shape for a date concept. The observed cost: a column of
years since a relationship began failed the entry-date value check, the entry
test of the cold-start detector became NOT EVALUABLE, and the population reached
the right answer only because no other test fired. That is luck, not design.

The rule: **a bare four-digit value in a plausible year range is a DATE at
year granularity, not an identifier**, wherever the concept being tested is a
date concept. Test it BEFORE the identifier rung and only for date concepts, so
an ordinary numeric code is not turned into a year for a non-date concept. Two
conditions, both required: every non-null value is exactly four digits, and every
one of them falls inside YEAR_PLAUSIBLE_RANGE. Where both hold, the column passes
a date value check with GRANULARITY recorded as YEAR, and every downstream rule
that reads it uses the year alone and says so. Nothing that needs a day may claim
one from it: a year-granular date answers "before or after this window" and
answers nothing finer.

## 3.7 Strict-exact-only concepts and forbidden neighbours

Some concepts must resolve by exact name and must never fall back to a
neighbouring column in the same semantic group, because a wrong resolution there
is a failure no downstream gate can catch.

The named case: an exclusion flag resolved to a neighbouring type column removes
a different population, and because the intended class is a subset of the
neighbouring class, every downstream invariant still passes. The only defence is
resolving the right column in the first place.

**THE TIE GUARD.** Where two concepts both produce an EXACT match on the same
header, and either is marked strict_exact_only, NEITHER resolves. The header is
reported as ambiguous, both candidates are named, and every feature both feed is
skipped and named. A tie on a strict concept is never broken by column position,
by dictionary order, or by which pass reached it first. See SD-PRS-47.

**THE CONVERSE, STATED EXPLICITLY, BECAUSE THE ENFORCEMENT PATH HAD A HOLE.** The
refusal mechanism used to be written as though it reached only strict concepts.
It does not, and it must not, because most concepts have to resolve by prefix and
substring to work at all. The rule is in two halves and both are mandatory:

1. **THE REFUSAL REACHES EVERY CONCEPT THAT NAMES A NEIGHBOUR, strict or not.** A
   forbidden-neighbours declaration is a refusal list, and the resolver refuses
   those candidates for that concept in every pass, exact, prefix and substring.
   A concept that declares a neighbour it must never be confused with, and gets
   no enforcement because it is not strict, has declared a rule with nothing
   behind it. That was the hole.
2. **A CONCEPT WHOSE NEIGHBOUR CONFUSION WOULD BE INVISIBLE DOWNSTREAM IS MARKED
   STRICT.** Strictness is the stronger and narrower instrument: it also forbids
   prefix and substring matching, so it is reserved for the concepts where a
   wrong resolution passes every later check. The date concepts are the clearest
   case, because headers there differ by tense rather than by subject, and a past
   event scored as a future obligation is invisible in the output.

The tie guard in the paragraph below fires where two concepts both match a header
exactly AND either is strict, OR the two name each other as forbidden neighbours.
A validator over the dictionary tests two things: every strict entry names at
least one neighbour, and every named neighbour is a concept that exists.

Every concept marked `strict_exact_only` in COLUMN_CONCEPT_DICTIONARY names at
least one `forbidden_neighbour`, and the resolver refuses those candidates even
when they are the only match. Where the exact name is absent, the concept is
UNRESOLVED and the feature it feeds is skipped and named. It is never
approximated.

## 3.8 A resolved but EMPTY column is an absent column

After resolution, check the non-null count within scope. If it is zero, exclude
the column from every flag, gate, weight and benchmark listed in that concept's
`feeds`, and list it in the audit as resolved but empty.

An empty commitment column would otherwise report every eligible unit as missing
every commitment. An empty breadth column would put every unit on the breadth
section. This is the single most damaging false-positive class in the bundle.

## 3.9 Normalize null-like VALUES, not just empty cells

Treat as missing: an empty cell, whitespace only, and every literal in
NULL_LIKE_VALUES.

A grouping cell containing the text "null" would otherwise classify a
self-determined unit as a managed one and invert every rule built on that
distinction.

## 3.10 Coerce before comparing

Read numeric-looking text as a number. Parse date-looking text as a date across
the known format set. Compare identifiers as normalized text on both sides.

A typed comparison against the wrong type fails silently and returns nothing. It
does not raise, and it looks exactly like a container with no data in that
column. Subtracting a date from a string produces nothing, and a recency flag
that silently never fires looks identical to a scope with no gaps.

## 3.11 Read the scale from the column's own maximum

Never assume a column is a fraction or a points value. If its maximum within
scope is at or below 1, it is fractional; if above 1, it is in points. A
threshold written for one scale matches zero rows against the other, silently.

## 3.12 Absences resolve by RULE, before any value search

A population defined by the absence of an attribute is resolved as the complement
of a populated field, never by searching for a word.

| Concept | Resolves to |
|---|---|
| The self-determined subset | The grouping field is BLANK after null normalization |
| The managed subset | The grouping field is POPULATED |
| An unbenchmarked entity | No benchmark column exists for that entity |

**THE PROPER-SUBSET GUARD.** An absence rule yields a usable subset only where
the complement is a PROPER, NON-EMPTY subset. Where the grouping field is blank
on every row in scope, or populated on every row in scope, the distinction does
not exist in this population: record the subset as NOT PRESENT, skip every cut,
filter and gate that depends on it, and name it in the audit. A subset equal to
the whole population is not a cut; it is the population under a second name.

This is the mirror of 3.8. There, a resolved-but-EMPTY column is treated as
absent. Here, a resolved-but-FULL absence rule is treated as no distinction.
Without it, a population whose grouping column is blank on every row resolves the
self-determined subset to one hundred percent of itself, and every comparison
drawn from that cut compares a number against itself while every gate passes.

Searching for the literal word finds nothing in any file, because the thing is
represented by an empty field rather than by the word, and a resolver that
value-searches it falls through and silently widens to every unit in scope.

## 3.13 Convert a name to its stored code through a table

Where a person types a long name and the data stores a short code, convert
through JURISDICTION_NAME_TO_CODE and then match exactly. Coincidental substring
containment is never evidence: one or two codes happen to sit inside their own
long names, and most do not, so a substring resolver works by coincidence on some
values and fails silently on the rest.

## 3.14 An administrative suffix is a routing cue, not noise

Strip the suffix before matching and route the phrase to that one column and
nothing else. Left in, the suffix causes a miss. Routed loosely, the bare stem
can match a like-named locality and silently scope the report to one place inside
the area the user asked for.

## 3.15 A compound phrase splits before classification and applies with AND

A separator splits the phrase. Both halves are classified and matched
independently, then applied together. Do not tokenize a multi-word value.

---

# PART 4: ANCHORING A STRUCTURAL BLOCK

Where the source carries a contiguous block of work-item columns, that block is
resolved BEFORE any data concept is matched.

### F4.1 Anchor on the DATA, not on the dictionary
Use a structural marker in the data itself. The normal marker is a row above the
header that carries a number over every column of the block and nothing else.

### F4.2 Stop before an exactly matched boundary
Match ACTIVITY_BLOCK_TERMINATOR_CONCEPT by exact comparison of the whole
normalized header. If more than one column matches, take the RIGHTMOST. Record
the resolved anchor index.

A substring search for a boundary token stops at the first decoy header that
happens to contain it. The documented case cut a 72-column block to 31 and
discarded 57 percent of the work-item set, with nothing in the output looking
wrong.

### F4.3 Three ordered fallbacks when the marker is absent
1. The block is the contiguous run of columns to the right of the last
   confidently resolved data concept and to the left of the boundary.
2. The block is the contiguous run of columns whose values are predominantly
   flags across the population.
3. No block exists. This is a valid outcome, not a failure.

### F4.4 Why the ordering matters in both directions
Matching data concepts first and greedily consumes work-item columns as data
concepts, because more than half of the work-item columns in a real file match
some data-concept stem if they are offered to the matcher. Defining the block as
everything to the right of the last mapped concept fails from the opposite end.
Anchoring on a structural marker is the only approach that fails neither way.

### F4.5 An originator prefix is metadata, never an admission test
A prefix on a work-item header is optional metadata used for weighting. It is
never used to decide whether a column belongs to the block. In the documented
case, 41 of 72 work-item columns carried no prefix at all and those 41 held 96.8
percent of the unit-level signal, so a prefix-based detector produced a ranking
built on 3 percent of the data.

---

# PART 5: WHEN A CONCEPT WILL NOT RESOLVE

### F5.1 Work the ladder before asking
1. Try the three passes across every stem in the concept's seed set.
2. Try the concept's own value check against every unresolved column, so a
   correctly shaped column with an unrecognized header can still be found.
2b. Where step 2 is reached for a STRICT concept, see the precedence rule
   immediately below. It is not skipped and it is not silently taken.
3. Look for the concept in a coarser container, then a coarser file.
4. Check whether the concept is derivable from two others already resolved.
5. Only then ask.

**PRECEDENCE BETWEEN STEP 2 AND 3.7, BECAUSE THEY APPEAR TO DISAGREE AND ONE OF
THEM MUST WIN.** 3.7 says a strict concept whose exact name is absent is
UNRESOLVED and is never approximated. Step 2 says a correctly shaped column with
an unrecognized header can still be found by its values. Read literally, a header
that is plainly the right column to any human reader, but is not an exact stem,
gets two opposite answers, and two competent readers produce two different
artifacts off one file. The precedence, in three parts:

1. **3.7 WINS OVER SILENT ADOPTION, ALWAYS.** Step 2 NEVER binds a strict concept
   on its own authority. A value check confirms a SHAPE; it cannot confirm a
   SUBJECT, and strictness exists precisely for the concepts whose wrong subject
   is invisible downstream. Every date column in a file passes a date value check,
   which is exactly why a date value check may not choose between them.
2. **STEP 2b: FOR A STRICT CONCEPT, A SINGLE VALUE-CHECK CANDIDATE BECOMES A
   QUESTION, NOT A BINDING.** Where the value check leaves EXACTLY ONE unresolved
   candidate column for a strict concept, and that column is refused by none of
   the concept's forbidden neighbours, the resolver does not adopt it and does not
   discard it. It carries it forward as the offered candidate for F5.1a. Where the
   value check leaves TWO OR MORE, the concept is UNRESOLVED and no question is
   spent, because a question that offers a menu of dates is asking the user to do
   the resolver's job.
3. **A NON-STRICT CONCEPT WITH SEVERAL VALUE-CHECK CANDIDATES HAS A STATED
   TIE-BREAK, AND FOR A REQUIRED CONCEPT AN UNBROKEN TIE IS A QUESTION, NEVER A
   PICK.** Step 2 previously said what to try and never what to do when it worked
   more than once. On a real file the ranking measure resolved by value check alone
   with FOUR candidates and no rule to choose among them, so the measure the whole
   plan was ranked on was chosen by a tie-break the bundle did not contain. One of
   the other three was a ratio that only just failed the rate rung; had it been
   taken, every figure would have ranked on it, every gate would have passed, and
   the front panel would have faithfully printed the wrong column's name. A
   confident wrong answer produced through the front door is the failure this whole
   bundle exists to prevent, so the leftmost-column tie-break of 3.3, which is
   written for the stem passes, is NOT extended here by analogy.

   Apply these tests in order, and STOP at the first that leaves exactly one
   candidate:

   | # | Test | Why it is above the next one |
   |---|---|---|
   | 1 | Discard every candidate that is a FORBIDDEN NEIGHBOUR of the concept, in either direction. | A concept that has said what it must never be confused with has already answered this. |
   | 2 | Discard every candidate already RESOLVED to another concept this run. | A column has one meaning, and the concept that got it by NAME outranks one reaching it by shape. |
   | 3 | Discard every candidate whose shape token is only a PERMISSIVE member of the concept's set, keeping those matching its FIRST-NAMED token. | A value check listing two tokens names the expected one first. |
   | 4 | Discard every candidate whose header resolved to NO concept at all AND whose values are near-constant or near-unique. | Neither shape can carry a ranking, and a column nothing recognizes is a poor guess. |
   | 5 | Prefer the candidate whose header shares a normalized token with ANY stem of the concept, even below the matching threshold. | A partial word match is weak evidence, and weak evidence beats none. |

   **WHAT HAPPENS AT THE END DEPENDS ON WHETHER THE CONCEPT IS REQUIRED.**
   - REQUIRED concept, one candidate left: take it, and print a RESOLVED BY SHAPE
     notice naming the column, the candidates discarded and the test that discarded
     each. It is never silent.
   - REQUIRED concept, still more than one: **ASK.** This is the one place a
     required concept may spend a question on a tie, and it spends it as a
     PERSON-tier file question under F5.1a's mechanics, so no binding authority is
     needed. Offer the surviving candidates by header with a sample of their values
     and the ranked-list consequence stated plainly. Where no answer arrives, the
     concept is UNRESOLVED and the run takes the required-concept-absent path. **It
     never picks one and proceeds.** A ranking is the one output where an
     undisclosed wrong column is invisible in every downstream check.
   - OPTIONAL concept, still more than one: UNRESOLVED, the feature it feeds is
     skipped and named, and no question is spent.

   **AND A MEASURE IS NEVER TAKEN FROM A COLUMN THAT LOOKS LIKE A RATIO.** Test 1
   already does this where the ratio concept resolved, and it holds even where it
   did not: a candidate for a ranking measure whose values are bounded near 1, or
   whose header carries a ratio, rate or percentage token, is discarded from the
   measure tie-break and recorded. A ratio that just misses the rate rung is the
   trap this rule was written from.

4. **A CANDIDATE THAT IS NEVER ASKED ABOUT IS STILL REPORTED.** Where no question
   can be spent, the audit names the concept, the single candidate column, and the
   sentence that the column was NOT used. A user reading that line can bind the
   header in one move at their next opportunity. This is the difference between
   failing closed and failing silently, and only the first is acceptable.

The step 2 wording therefore stands for NON-strict concepts unchanged, and is
routed through 2b for strict ones. Nothing about this weakens 3.7: no strict
concept is ever resolved by shape alone, in any path.

### F5.1a One question may be spent on a strict concept that feeds more than one thing
F5.2 limits questions to REQUIRED concepts, and that limit is correct for the
ordinary optional concept whose failure costs one feature. It is wrong for the
narrow case where a single strict optional concept fails and a MATERIAL PART OF
THE CONTRACT goes with it.

**THE TEST, ALL THREE PARTS:** the concept is strict; step 2b left exactly one
offered candidate; and the concept feeds MORE THAN ONE named output, where a
section, an alert line, a membership flag, an exception flag and a column are each
one output. Where all three hold, ONE question may be spent, and it is batched
into the same single message as the required-concept questions under F5.3.

**THE QUESTION NAMES THE COLUMN AND THE COST, and it never asks the user to
choose between columns:**

> Your file has a column headed {candidate header}. Its values are dates. Is that
> the date this {unit noun} was last {engaged, serviced, contacted, or the
> organization's own word}? If it is, I can fill in {the named outputs}. If it is
> not, or you are not sure, say so and I will leave all of that out and say why.

Three outcomes, and all three are recorded: YES binds the concept for this run
and is offered as a learned stem under Part 7; NO or NOT SURE leaves the concept
UNRESOLVED, and the offered candidate is recorded as refused so it is not offered
again in the same run; NO ANSWER is treated as NOT SURE.

**THIS QUESTION IS PERSON-TIER, NOT ORG-TIER, AND IT IS NOT GATED ON A BINDING
OWNER.** It asks what a column IN THE FILE THE USER JUST SUPPLIED means. It does
not ask what the organization's levels are, what its policy is, or what any
threshold should be, and it never writes to the ORG config. The wall in
reference/binding-interview.md I1 is therefore not crossed, the binding-authority
constraint C1 does not apply, and a frontline user on a completely unbound
first run may be asked it. That is the point of the rule: the case it exists for
IS the first run, where no binding owner exists yet by definition, and gating a
file question behind an owner would mean the mechanism could never fire when it
is most needed. A YES is used FOR THIS RUN and is offered to Part 7 as a
candidate learned stem, which is a proposal, not a binding.

**AT MOST ONE SUCH QUESTION PER RUN, ACROSS ALL CONCEPTS.** Where two strict
concepts both qualify, spend the question on the one feeding the most outputs,
with a tie broken by the order of the concepts in COLUMN_CONCEPT_DICTIONARY so
the same file always spends it the same way. The other is reported unasked under
part 3 of the precedence rule. This question sits INSIDE the deferred-request
budget the skill is already holding, and never in addition to it.

### F5.1b Confirming a value-level default on the user's own file
**THIS SECTION DOES NOT SETTLE WHETHER THE EXCLUSION RUNS. THE
UNIT_ACTIONABLE_NOW_VALUES ROW IN reference/schema/ SECTION A1 SETTLES IT.** What
this section owns is HOW TO ASK about a value-level default on the user's own file.
An earlier revision left the question of whether a resolved column with an unbound
value list produces an exclusion to be inferred from this section, in this file, by
implication, while two rows in the schema disagreed about it. A rule that decides
POPULATION MEMBERSHIP may not live by implication in a third file: two readings
produce two populations and therefore every number in the artifact differs.

A resolved column supplies a CONCEPT. It does not supply the VALUES that concept's
downstream rule needs, and the two are separate bindings. The named case is the
not-actionable status column: the column resolves, the values are visible, and
nothing is excluded because the VALUE LIST is a different unbound variable. That
produced an artifact that put a prospect at rank one of a working plan, disclosed
three times and still not fit to hand anybody.

Where a value-level default is about to be applied to a column IN THE USER'S OWN
FILE, and the run can ask, it asks first, ONCE, batched with the other questions
under F5.3. Like F5.1a, this is PERSON-TIER: it asks what the values in the file
in hand mean, never what the organization's policy is, so the wall in
reference/binding-interview.md I1 is not crossed and no binding authority is required. A
frontline user on a completely unbound first run may be asked it.

**THE QUESTION SHOWS THE WHOLE DECISION, NOT A YES-OR-NO:**

> Your file has a column headed {header} with {k} distinct values. I am going to
> treat these as not workable this period and leave them out: {each value the
> default matched, with its count}. I am going to keep these: {each other value,
> with its count}. Tell me if I have any of that the wrong way round.

Three outcomes: a correction, which governs this run; a confirmation, which
proceeds; and NO ANSWER, which proceeds ON THE DEFAULT and says in the artifact
that it was not confirmed. **Silence never reverts to excluding nothing.** The
whole point of the rule is that including a plainly unworkable unit is the more
damaging error, and a user who did not reply has not asked for that.

**WHERE THE RUN CANNOT ASK**, because the budget is spent or the channel does not
allow it, the default still applies and the artifact carries the full
EXCLUDED-and-KEPT listing. An unanswered question does not suspend the rule.

A correction is used FOR THIS RUN and offered as a proposal for the eventual
ignition interview. It is never written to the ORG config by a run.

### F5.2 Ask only for REQUIRED concepts
Required means the minimum set the method cannot run without: the unit
identifier, a ranking measure, and any one scope column. For an optional concept,
skip the feature it feeds, name it in the audit, and continue. A missing breadth
column costs one section; a question costs the user's attention and the run's
momentum.

### F5.3 Batch every question into one message
If three concepts are ambiguous, ask about all three at once, offering the
candidate headers with a sample of their values beside each. Never ask, work,
then ask again.

### F5.4 A miss has three outcomes that must never be collapsed
1. **Matched.** Proceed and disclose.
2. **Routed to a column family, no value matched.** Stop before ranking and ask,
   reporting the phrase, the column tested, and the MISS_SUGGESTION_COUNT nearest
   values present, ranked by ascending normalized edit distance with an
   alphabetical tie-break, so the same miss always returns the same list.
3. **Routed to no column family at all.** Say which columns were tested, run the
   request without that term, and label the output as unqualified.

Never take the third outcome for a phrase that classified successfully.

### F5.5 Distinguish "the column is absent" from "the value is not in it"
They read identically in the output and have completely different fixes.

### F5.6 Never silently widen
If a concept cannot be resolved and the feature it feeds would otherwise cover a
broader population than the user asked for, the output says so on its face. A
report that quietly covers the user's whole span when they asked for one slice is
wrong in the way that destroys trust, because every number in it is internally
consistent.

---

# PART 6: THE SEED DICTIONARY

**THE REQ LEGEND.** There are exactly THREE required concept GROUPS, not three
required entries. A group is satisfied when any one of its members resolves.

1. The unit identifier.
2. Any one of the ranking measures.
3. Any one of the scope columns.

Two further concepts, the entry date and the stage, are required only when the
population's mode is FLOW. The not-actionable flag is required only when the
organization has bound one. Everything else is optional, and a concept that does
not resolve costs the feature it feeds and nothing more.

**NO STEM BELONGS TO TWO CONCEPTS.** Where two seed concepts would share a stem,
the stem is removed from the LESS SPECIFIC concept and the removal is recorded
below, so a binding owner adding a local stem can see the precedent. The seed
dictionary is held to the same standard as the runtime learning rule in 7.5,
which already refuses to promote a colliding stem. Recorded removals:

- The bare stem "branch" was removed from the finest scope concept. It collided
  with the mid scope concept, where it is the more natural reading, and the tie
  guard does not reach a prefix collision between two non-strict concepts, so the
  resolver fell through to leftmost-column, which is arbitrary. The two scope
  concepts now name each other as forbidden neighbours.
- The stem "region code" was removed from the jurisdiction concept. It is an
  EXACT match for an ordinary scope-code header, exact passes run first, so the
  resolver's first answer was that a scope code is a legal jurisdiction, which
  would have fed the compliance stage a jurisdiction set made of scope codes.
- The bare stems "state", "district", "group", "programme", "tier" and "band" were
  each removed from the less specific of the two concepts that carried them:
  "state" from the stage concept, "district" from the subregion concept, "group"
  from the top scope concept, "programme" from the parent-group concept, and
  "tier" and "band" from the unit-type concept.
- The bare stem "status" was removed from the not-actionable flag. It collided
  with the stage concept, and "closed" is a stage name in almost every pipeline.
  A file with one column headed with that word and stage values would otherwise
  resolve to the exclusion concept, the exclusion would remove a stage, the funnel
  would reconcile, and every downstream invariant would pass. That is the failure
  SD-POP-05 names as the one no gate can catch. The not-actionable flag now
  carries only qualified forms, and the two concepts name each other as forbidden
  neighbours.

**Everything in this part is SEED data: a starting dictionary, not a
specification.** It is deliberately generic, deliberately incomplete, and
deliberately industry-neutral. Every business replaces and extends it with its
own vocabulary during the ORG binding interview and at runtime under Part 7.

Each entry lists SEVEN fields, and every table in this part carries all seven as
STRUCTURED COLUMNS: the concept key, whether it is required, its stems, its value
check, whether it is strict-exact-only, its forbidden neighbours, and what it
feeds.

**EVERY VALUE CHECK IS WRITTEN IN THE SHAPE TOKENS OF 3.6 AND IN NOTHING ELSE.**
The permitted tokens are DATE, IDENTIFIER_OR_CODE, BOOLEAN_LIKE,
RATE_OR_PROPORTION, COUNT_OR_MEASURE, STATUS_OR_CATEGORY and FREE_TEXT. A cell may
combine them with "or" and may add a qualifier that is not itself a shape, such as
"carried as text", "often blank" or "scale read from data". It may NOT introduce a
shape word of its own. An earlier revision wrote these cells in ordinary English,
so the classifier and the dictionary described the same column in two different
vocabularies, a required identifier failed a check it plainly satisfied, and a
reader had to prefer one of the two to proceed at all. A value check naming a
token the classifier cannot emit is a DICTIONARY DEFECT under 3.6a rule 2: it is
recorded, it is UNSATISFIABLE rather than FAILED, and it never refuses a column.

**THE VALIDATOR FOR THIS PART TESTS FIVE THINGS**, and it is cheap enough to run on
every change: every row carries all seven columns; every forbidden neighbour names
a concept that exists; every strict entry names at least one neighbour; no stem
appears in two concepts; and every value check parses into the token set above.

**A field written as prose inside another cell is an EMPTY field.** A run building
COLUMN_CONCEPT_DICTIONARY from these tables reads columns, so a declaration
written as a sentence inside the Feeds cell sets its own field to nothing, and
every rule that tests that field then reads an empty value and does not fire. Two
tables in an earlier revision carried five columns for this reason and the rule
that depends on the forbidden-neighbours field could never fire. Where a concept
genuinely has no neighbour to refuse, the cell is empty and the concept is not
strict; that is a declaration too, and it is made in the column.

## 6.1 Identity and location

| Concept | Req | Seed stems | Value check | Strict | Forbidden neighbours | Feeds |
|---|---|---|---|---|---|---|
| concept_unit_id | YES | account number, account no, account id, unit id, unit number, record id, case id, case number, ticket id, ticket number, claim number, work order, order number, site id, site number, asset id, asset tag, customer id, member id, patient id, file number, reference number | IDENTIFIER_OR_CODE | yes | concept_parent_group_name, concept_contact, concept_filer | joins, ranking, dedup, tie-break, spot check |
| concept_unit_name | no | account name, customer name, site name, facility name, location name, insured, client name, description, title | FREE_TEXT | no | concept_parent_group_name | display, matching a named directive |
| concept_secondary_unit_id | no | alternate id, legacy id, external id, source system id | IDENTIFIER_OR_CODE | no | concept_unit_id | recorded only, never joined or ranked on |
| concept_address | no | address, street, street address, address line, service address, loss location | FREE_TEXT | no |  | display, matching a named directive |
| concept_city | no | city, town, municipality, locality | STATUS_OR_CATEGORY | no | concept_subregion | display, qualifier routing |
| concept_jurisdiction | no | state, province, country, jurisdiction, licence state, regulatory state, filing state | IDENTIFIER_OR_CODE or STATUS_OR_CATEGORY | no | concept_scope_upper, concept_scope_top | compliance check, qualifier routing |
| concept_postal | no | postal code, post code, zip, zip code | IDENTIFIER_OR_CODE, carried as text | no |  | display, qualifier routing |
| concept_subregion | no | county, parish, borough, catchment, service area, postal district | STATUS_OR_CATEGORY | no | concept_city | qualifier routing |
| concept_coordinates | no | latitude, longitude, lat, lon, geocode | RATE_OR_PROPORTION or COUNT_OR_MEASURE | no |  | present and deliberately unused |

## 6.2 Scope

| Concept | Req | Seed stems | Value check | Strict | Forbidden neighbours | Feeds |
|---|---|---|---|---|---|---|
| concept_scope_finest | one of the scope concepts is required | territory, route, book of business, patch, portfolio, caseload, queue, cell, workcentre, assignment, seat | IDENTIFIER_OR_CODE or STATUS_OR_CATEGORY | no | concept_filer, concept_scope_mid | scope filter, span block, peer set |
| concept_scope_mid | see above | market, branch, office, site group, sector, cluster, hub | IDENTIFIER_OR_CODE or STATUS_OR_CATEGORY | no | concept_filer, concept_scope_finest | scope filter, span block |
| concept_scope_upper | see above | section, district, division, area, zone | IDENTIFIER_OR_CODE or STATUS_OR_CATEGORY | no | concept_filer | scope filter, span block |
| concept_scope_top | see above | region, national, enterprise, company, whole organization | IDENTIFIER_OR_CODE or STATUS_OR_CATEGORY | no | concept_filer | scope filter, span block |
| concept_filer | no | submitter, submitted by, owner, assigned to, handler, rep, adviser, technician | STATUS_OR_CATEGORY | no | concept_scope_finest, concept_scope_mid, concept_scope_upper, concept_scope_top | recorded only, never scoped on |

Note on the scope concepts: exactly one of them must resolve for a source to be
usable. Finer levels are read off a resolved code by prefix, and coarser ones by
truncation, so one column is enough.

## 6.3 Grouping and class

| Concept | Req | Seed stems | Value check | Strict | Forbidden neighbours | Feeds |
|---|---|---|---|---|---|---|
| concept_parent_group_name | no | parent, parent account, group name, parent group, chain, network, franchise, master account | FREE_TEXT, often blank | no | concept_unit_name | the self-determined subset by absence, aggregate cuts |
| concept_parent_group_flag | no | is grouped, has parent, is chain, group flag | BOOLEAN_LIKE | no |  | cross-check on the name, never the definition |
| concept_unit_type | no | type, class, category of unit, channel, segment, unit class | STATUS_OR_CATEGORY | no | concept_creditable_entity | display, qualifier routing |
| concept_creditable_entity | no | line of business, business line, primary line, line of coverage, product line, product family, service line, book segment, creditable entity, category of business | STATUS_OR_CATEGORY | no | concept_unit_type, concept_distinct_entity_count, concept_item_count | the entity_weight factor of the alignment term, entity cuts, the entity focus column |
| concept_unit_unavailable_flag | see the Req legend | temporarily closed, permanently closed, inactive, suspended, on hold, legal hold, do not contact, terminated, dormant, account status, client status, customer status, record status, lifecycle status, relationship status | BOOLEAN_LIKE or STATUS_OR_CATEGORY | yes | concept_unit_type, concept_parent_group_flag, concept_stage | the not-actionable exclusion |
| concept_out_of_model_flag | no | different model flag, managed elsewhere, self serve, partner managed, third party administered, out of scope programme | BOOLEAN_LIKE | yes | concept_unit_type, concept_parent_group_flag | the class exclusion and its three escapes |

The two strict entries are strict for the same reason: resolving either to a
neighbouring type column removes the wrong population, and because the intended
class is usually a subset of the neighbouring class, every downstream invariant
still passes.

**`concept_creditable_entity` IS THE COLUMN THAT SAYS WHICH ENTITY A ROW BELONGS
TO, AND IT EXISTS BECAUSE A SCORING FACTOR HAD NO WAY TO BE FOUND.** The entity
taxonomy in reference/schema/ Group 7 carries the entities and their weights, and
`entity_weight` is a multiplicative factor of the alignment term on every row of
every ranked list. Nothing said which column of the source file carries the
entity. One live run matched the bound entity names against the distinct values of
every candidate column, found one that carried all eight, used it, and recorded
that it had invented the procedure. That was the right answer and the wrong way to
get it: on a file with two overlapping category columns the same run had no rule
to choose between them, on a factor that multiplies every score in the workbook.

**THE VALUE TEST IS THE DISCRIMINATOR AND IT OUTRANKS THE NAME.** A header alone
cannot separate the entity column from an ordinary type or segment column, so no
column is taken as the entity column on a name match alone. Before it is used:

1. Take the column's DISTINCT VALUES, normalized by 3.1, and measure what share of
   the keys and aliases of CREDITABLE_ENTITIES they cover.
2. A column qualifies only where that coverage is at or above
   ENTITY_COLUMN_MIN_COVERAGE and at least a tenth above the runner-up's coverage.
3. Where two columns both clear the floor and neither beats the other by that
   margin, NEITHER is taken. Both are named with their coverages and the concept is
   reported unresolved, exactly as 6.5 does for the two count concepts.
4. The chosen column, its coverage, and the runner-up with its coverage, are
   printed in the audit. A multiplicative factor whose source column is not named
   is a number the reader cannot check.

**THE TWO STEM OVERLAPS THIS ENTRY CREATES ARE DECLARED RATHER THAN LEFT TO THE
RESOLVER.** `product line` here sits beside `product lines` in the entity-count
concept, and `book segment` here sits beside `segment` in the unit-type concept.
Neither pair is an exact duplicate, so the dictionary validator passes them, and
the exact pass separates the ordinary headers cleanly. What makes them safe rather
than lucky is that all three concepts now name each other as forbidden neighbours
RECIPROCALLY, so 3.7's refusal reaches every pass and its tie guard reaches the
exact one. This is the same treatment the recorded stem removals in Part 6's
preamble received, written down for the same reason.

**WHERE IT DOES NOT RESOLVE, THE TERM TAKES A STATED NEUTRAL AND NOT A GUESS.**
`entity_weight` is 1.0 on every row: the identity multiplier, so the alignment term
reduces to its other factors and no unit is ranked up or down by an entity nobody
could identify. It is never zero, which would delete the term, and never the
weight floor, which would rank every unit as if it carried the least valued entity.
The absence is stated in the artifact with the candidates and their coverages.


## 6.4 Measures

| Concept | Req | Seed stems | Value check | Strict | Forbidden neighbours | Feeds |
|---|---|---|---|---|---|---|
| concept_measure_tier_1 | one measure required | total value, total volume, normalized value, standard value, weighted value, exposure, incurred, revenue, throughput, premium, annual premium, written premium, earned premium, billings, billed amount, fees, fee income, contract value, annual contract value, annual value, total contract value, spend, annual spend, sales, net sales, gross sales, turnover, bookings, invoiced, invoiced amount, amount, value, size of book, book value, account value | COUNT_OR_MEASURE | no | concept_benchmark_measure, concept_rate_or_ratio | ranking, percentile, tie-break, all weighting |
| concept_measure_tier_2 | see above | gross value, paid, billed, units, count of items, cases handled, commission, commission income, margin, gross margin, gross profit, recurring revenue, subscription value | COUNT_OR_MEASURE | no | concept_benchmark_measure, concept_rate_or_ratio | fallback ranking |
| concept_measure_tier_3 | see above | own value, own volume, own units | COUNT_OR_MEASURE | no | concept_benchmark_measure | last-resort ranking |
| concept_measure_composite | see above | per-entity value stems, summed under the composite construction | COUNT_OR_MEASURE or RATE_OR_PROPORTION | no | concept_benchmark_measure | synthesized ranking when no single measure resolves |
| concept_benchmark_measure | no | total category, total market, all units, industry, whole population, benchmark, addressable | COUNT_OR_MEASURE | yes | concept_measure_tier_1, concept_measure_tier_2, concept_measure_tier_3 | the counterfactual denominator, never the ranking |
| concept_rate_or_ratio | no | ratio, rate, loss ratio, combined ratio, hit ratio, close rate, win rate, retention rate, conversion rate, margin percent, percentage, percent, index, score index, utilisation, utilization | RATE_OR_PROPORTION or COUNT_OR_MEASURE | yes | concept_measure_tier_1, concept_measure_tier_2, concept_measure_tier_3, concept_benchmark_measure | recorded and reportable, NEVER the ranking measure |
| concept_eligible_population | no | eligible, in scope count, target list, flagged population, addressable count, assigned count | COUNT_OR_MEASURE | no | concept_benchmark_measure | the bare denominator rung |

Rate markers and lookback tokens are stripped for matching and recorded after:
per week, per day, per month, weekly, daily, monthly, ytd, mtd, qtd, rolling,
trailing, last 13 weeks, last 26 weeks, last 52 weeks.

## 6.5 Breadth, presence and benchmarks

| Concept | Req | Seed stems | Value check | Strict | Forbidden neighbours | Feeds |
|---|---|---|---|---|---|---|
| concept_item_count | no | items carried, distinct items, item count, modules, seats, services, products held, breadth, policies, policies in force, policy count, active policies, items in force | COUNT_OR_MEASURE | no | concept_range_satisfaction, concept_distinct_entity_count | the breadth section, admission pair half one |
| concept_distinct_entity_count | no | lines of business, lines carried, distinct lines, line count, lines in force, distinct products, product lines, distinct categories, distinct services, coverage lines, number of lines, cross sell count, lines written, lines of coverage, coverages, distinct lines of business, count of lines, number of products, distinct entities, entity count | COUNT_OR_MEASURE | yes | concept_item_count, concept_measure_tier_2, concept_creditable_entity | the breadth of the creditable-entity set per unit, and any objective or requirement stated in terms of how many ENTITIES a unit carries |
| concept_range_satisfaction | no | satisfaction, coverage percent, assortment, completeness, adoption percent, penetration | RATE_OR_PROPORTION or COUNT_OR_MEASURE, scale read from data | no | concept_item_count, concept_benchmark_satisfaction | the breadth section, admission pair half two |
| concept_presence_ours | no | present, carried, deployed, installed, active flag, has | BOOLEAN_LIKE | no | concept_presence_other | the binary presence gap term |
| concept_presence_other | no | competitor present, alternative deployed, incumbent, other provider | BOOLEAN_LIKE | no | concept_presence_ours | the presence gap pair |
| concept_benchmark_satisfaction | no | competitor coverage, alternative penetration, other provider share | RATE_OR_PROPORTION or COUNT_OR_MEASURE | no | concept_range_satisfaction | the degree-of-completeness gap term |
| concept_units_per_item | no | derived: measure divided by item count | COUNT_OR_MEASURE or RATE_OR_PROPORTION | no |  | the intensity classification |

**WHY `concept_distinct_entity_count` IS STRICT AND WHY ITS FORBIDDEN NEIGHBOUR IS
THE ITEM COUNT.** These two concepts hold small integers, sit next to each other in
a file, and are named with the same handful of words, and they are not the same
number. **A unit can carry THREE of the countable things and ONE creditable entity**:
three policies on one line of business, three seats of one product, three tickets in
one category. Counting the items and calling the result the entity breadth overstates
it, on every row, by a factor nobody can see in the output. It is the wrong direction
too: an objective phrased as carrying more than one ENTITY is scored as already met by
a unit that carries several items of one entity, so the very thing the objective asks
for is reported as done.

**The value check is the discriminator, and it is not optional here.** A header alone
cannot separate them, so before either column is used for an entity-breadth figure,
run both halves of the check:

1. **Against a stated figure.** Where any supplied document states an average or a
   share for the entity breadth, compare it with the column's own mean. A column whose
   mean sits materially above a stated average is the item count, not the entity count.
2. **Against the other candidate's ordering.** Where both columns resolve, rank the
   units by each. Where the two orderings differ, the columns are measuring different
   things and the mapping cannot be settled by the header. Take neither on a guess:
   report the concept as unresolved, name both candidate columns with their means, and
   raise it as a question.

Because the entry is marked strict, 3.7's refusal mechanism and its tie guard both
reach it, so a header that matches an item stem and an entity stem at once is REFUSED
rather than silently scored. **A refusal here is the correct outcome and is reported
as a resolved question rather than as a failure:** the figure that would have been
published was wrong, and saying so costs one line where publishing it costs the
reader's trust in every breadth number on the artifact.

The stem `lines carried` moved OUT of `concept_item_count` and into this entry in the
same edit, because it is the single most ambiguous stem of the set and leaving it in
both would have made every resolution of it a tie.

**BOTH STEM LISTS WERE WIDENED AFTER A RUN IN WHICH THE DISCRIMINATOR HAD NOTHING
TO DISCRIMINATE BETWEEN.** A book of business carried its countable thing in a
column named for the instrument the business actually sells, and neither concept
carried that word: the entity stems named lines and the item stems named items,
modules, seats and services, and the file said neither. So the column resolved to
NOTHING. The discriminator above never ran, because it runs BETWEEN two candidates
and there were none, and the organization's own first published priority for the
period, which was phrased in exactly this quantity, reached zero rows on every
sheet and was disclosed only as a zero in a source count seventy rows into the
method section.

The seed lists now carry the ordinary trade words on both sides: the item side
takes the words a business uses for the countable instrument it issues, and the
entity side takes the words it uses for the KINDS of thing it sells. The
discriminator is unchanged and is what still separates them, and it now has
candidates to separate. **A SEED LIST THAT MISSES A CONCEPT BY ONE WORD IS NOT A
NARROW MATCH, IT IS NO MATCH**, and the failure is silent because an unresolved
concept produces a zero rather than an error. That is the general lesson and it is
why 7.4a exists.

**AND THE UNEVALUATED DECISION IS ANNOUNCED WHERE THE DECISION LIVES.** Where a
named priority, requirement or predicate cannot be evaluated because a concept did
not resolve, the audit line is necessary and is not sufficient: it is named in the
section that decision belongs to, in its own row, with the reason and the header
candidates that were considered. An unevaluated priority is a fact about the plan,
not a footnote about the method.


## 6.6 Commitments, programmes and status

| Concept | Req | Seed stems | Value check | Strict | Forbidden neighbours | Feeds |
|---|---|---|---|---|---|---|
| concept_unit_commitment_date | no | renewal date, renewal, expiration date, expiry date, expires, term end, end of term, contract end, contract expiry, next review date, review due, anniversary date, certification expiry, licence expiry, license expiry, permit expiry, unit due date, due date | DATE | yes | concept_last_engagement_date, concept_last_evidence_date, concept_exit_date | the unit-level close weight and the workload count |
| concept_commitment | no | contract, agreement, commitment, terms, plan level, tier, subscription | STATUS_OR_CATEGORY or BOOLEAN_LIKE | no | concept_premium_commitment | the commitment gap term |
| concept_premium_commitment | no | premium tier, enhanced agreement, advanced plan, accelerator, upgraded terms | STATUS_OR_CATEGORY | no | concept_commitment | the extra weight on a missing premium commitment |
| concept_programme_election | no | election, enrolment, opt in, participation, programme, scheme | BOOLEAN_LIKE or STATUS_OR_CATEGORY | no | concept_commitment | programme-adoption cuts |
| concept_price_alignment | no | price alignment, pricing status, rate alignment, promotional alignment | STATUS_OR_CATEGORY | no | concept_passthrough | shown, never scored |
| concept_passthrough | no | pass through, pass thru, applied, implemented, honoured | STATUS_OR_CATEGORY | no | concept_price_alignment | execution counts |
| concept_perf_bucket | no | performance identifier, opportunity identifier, segment identifier, quadrant, priority marker | STATUS_OR_CATEGORY, on two axes | no | concept_segment_band | the graduated bucket term |
| concept_segment_band | no | decile, quartile, quintile, band, tier band, rank band | STATUS_OR_CATEGORY, never COUNT_OR_MEASURE | no | concept_perf_bucket | display, segment cuts |

**THE FEEDS LIST IS THE SWITCH FOR THE UNIT-LEVEL COMMITMENT RULE.** Some
businesses carry their most important date on the UNIT rather than on a work
item: a renewal, an expiry, a term end, an anniversary, a next review, a licence
lapse. Such a source often has no work-item block at all, and Part 4 correctly
returns "no block exists". Without a resolvable unit-level date concept, every
route into the alignment and workload terms is closed, both terms are zero for
every unit, and the ranked list silently reduces to the population sorted by
size, which contradicts the commitment-date-first rule in SD-SCO-01 and the
never-rank-on-activity-count rule in SD-WGT-17.

`concept_unit_commitment_date` above is the seed entry that closes that path. Its
`feeds` value names the unit-level close weight and the workload count, and that
feeds value IS the switch: a date concept whose feeds list names them is admitted
as an implicit unit-level commitment; one whose feeds list does not is recorded,
displayed, and scores nothing. No separate on-off variable exists and none should
be invented.

**Its `strict` and `forbidden_neighbours` fields are STRUCTURED FIELDS, not
prose, and both are load bearing.** The rule that reads this entry tests three
things and all three must hold, so a declaration written as a sentence inside the
Feeds cell is an empty field when the dictionary is built from these tables, and
the rule never fires. The three neighbours are declared RECIPROCALLY here and in
6.7: a date recording when something last happened, a date recording when
evidence was captured, and a date recording when a unit LEFT are none of them
dates on which something falls due. Because the entry is marked strict, 3.7's
refusal mechanism and its tie guard both reach it, so a header such as a last
renewal date, which matches a commitment stem and a recency stem at once, is
refused rather than silently scored as a future obligation.

## 6.7 Recency and evidence

| Concept | Req | Seed stems | Value check | Strict | Forbidden neighbours | Feeds |
|---|---|---|---|---|---|---|
| concept_last_engagement_date | no | last contact, last contact date, last call, last call date, last visit, last visit date, last touch, last touchpoint, last service touch, last service date, last serviced, last interaction, last activity, last activity date, last engagement, last reviewed, date of last contact, most recent contact, most recent activity | DATE | yes | concept_unit_commitment_date, concept_last_evidence_date | the recency membership flag, the flat alert, the coverage-stale exception flag and the days-since column |
| concept_last_evidence_date | no | photo date, evidence date, image date, inspection date, audit date | DATE | no | concept_unit_commitment_date, concept_last_engagement_date | evidence-of-work cuts |
| concept_entry_date | see the Req legend | opened, created, received, first notice, intake date, start date, submitted, client since, customer since, member since, account since, since, onboarded, onboarded date, relationship start, relationship since, date joined, joined, joined date, first engaged, acquisition date, date acquired, established, established date, inception date, effective date, date opened, open date, signup date, enrolled date | DATE | no | concept_exit_date | cohorting, aging |
| concept_exit_date | no | resolved date, completed date, settled date, closed date, disposition date, date closed | DATE | yes | concept_unit_commitment_date, concept_entry_date, concept_stage | the open-set rule, cycle time |
| concept_stage | see the Req legend | stage, phase, step, disposition, pipeline stage, workflow stage | STATUS_OR_CATEGORY | yes | concept_unit_unavailable_flag, concept_exit_date | the open-set rule, stage cuts |
| concept_next_action | no | next action, next step, follow up, follow up action, next task, action required, planned action, next contact | FREE_TEXT or STATUS_OR_CATEGORY | no | concept_stage | the no-next-action gap term under FLOW |

**Why three of these five are strict.** A date column is the easiest thing in a
file to resolve to the wrong concept, because the words differ by tense rather
than by subject: a date recording when something HAPPENED, and a date recording
when something is DUE, are one word apart in a header and opposite in meaning.
Reading one as the other dates the wrong thing and scores a past event as a
future obligation. Marking them strict is what makes 3.7's refusal mechanism and
its tie guard reach them.

## 6.8 Supply, contact and other

| Concept | Req | Seed stems | Value check | Strict | Forbidden neighbours | Feeds |
|---|---|---|---|---|---|---|
| concept_supplier | no | supplier, vendor, distributor, wholesaler, provider, carrier, third party | STATUS_OR_CATEGORY | no | concept_parent_group_name | display, qualifier routing |
| concept_contact | no | contact email, decision maker, primary contact, consent, verification status | FREE_TEXT or BOOLEAN_LIKE | no | concept_filer | checked for fill rate before anything is built on it |
| concept_period_change | no | change versus prior, prior period, delta, movement | COUNT_OR_MEASURE or STATUS_OR_CATEGORY | no | concept_measure_tier_1 | comparison, never a measure |
| concept_row_total | no | total, grand total, row total, sum | COUNT_OR_MEASURE or RATE_OR_PROPORTION | yes | concept_measure_tier_1, concept_benchmark_measure | the structural boundary anchor, matched exactly, rightmost wins |

## 6.9 What is deliberately NOT in the seed dictionary

- Any product, brand, programme or system name from any specific business.
- Any internal document number, code scheme or endpoint.
- Any threshold. Thresholds live in reference/schema/, and every one that can be
  computed from the file in hand is computed from the file in hand.
- Any name list used as a substitute for a flag. Use the source's own flag so the
  rule travels without a list to maintain.

---
# PART 7: EXTENDING THE DICTIONARY AT RUNTIME

The dictionary is designed to grow. This is the mechanism.

## 7.1 The trigger

A learning event fires when any of these happens:

- A header did not resolve to any concept.
- A concept resolved only through an ask, and the user named the column.
- A concept resolved by the value check after failing the name match.
- A resolved column failed its value check and a different column was taken
  instead.
- A stem matched but the run recorded the resolution as ambiguous.

## 7.2 What gets registered: the STEM, never the literal

Before registering, apply the full normalization in 3.1, then additionally:

1. Strip a trailing period token.
2. Strip a trailing rate marker.
3. Strip a leading originator prefix.
4. Strip a leading or trailing entity name that belongs in the entity taxonomy
   rather than in the concept dictionary.
5. Reject the candidate if what remains is shorter than MIN_STEM_LENGTH
   normalized characters. A short stem will over-match and is worse than no
   entry.

A stem catches every dated and prefixed variant automatically. A literal catches
exactly one period's export.

## 7.3 What is recorded, per learning event

    {
      "event": "UNRESOLVED | ASKED | VALUE_MATCH | REJECTED | AMBIGUOUS | ADOPTED_PROVISIONAL",
      "literal_header": "<exactly as it appeared>",
      "normalized": "<after 3.1>",
      "proposed_stem": "<after 7.2>",
      "resolved_to_concept": "<concept key, or null>",
      "decided_by": "USER | VALUE_CHECK | RESOLVER | NOBODY",
      "confidence": "HIGH | MEDIUM | LOW",
      "sample_values": [ "<3 to 5 sampled values, sanitized>" ],
      "value_classification": "<from the ladder in 3.6>",
      "container": "<container name>",
      "column_index": <n>,
      "source_period": "<period the file covers>",
      "run_id": "<id>",
      "rejected_candidates": [ "<concept keys considered and why not>" ]
    }

Appended to CONCEPT_LEARNING_LOG_PATH. Never written to OUTPUT_DIR.

## 7.4 Which learnings may be used inside the same run

- **Decided by USER**: used immediately for the rest of this run. The user is the
  authority on their own file.
- **Decided by VALUE_CHECK at HIGH confidence**: used immediately, and recorded
  as a value-check resolution so a reader can see the name did not match.
- **Decided by RESOLVER at MEDIUM confidence**: used, and flagged in the audit as
  an ambiguous resolution with both candidates named.
- **LOW confidence**: not used. The concept stays unresolved, the feature it
  feeds is skipped and named, and the event is logged for the binding owner. A
  low-confidence inference never becomes a binding.

## 7.4a The first-run route: a strong candidate the dictionary does not carry

**THE GAP THIS CLOSES.** Every route in 7.4 is keyed on WHO decided, and two of
the four decide nothing on a first run at an organization that has bound nothing:
there is no bound dictionary to match against, and where INTERACTIVE is absent or
the user is not the person who knows the file, there is nobody to ask. A run could
therefore see a column that plainly answers a concept, be unable to name a route
that permits using it, and publish a zero. A zero from an unresolved concept looks
exactly like a zero from a genuine absence, which is why this was silent for as
long as it was.

**WHAT A RUN MAY DO: PROVISIONAL ADOPTION, FOR THIS RUN ONLY.** A candidate column
may be adopted for a concept the dictionary does not carry a matching stem for,
when ALL SIX of these hold. They are the evidence bar, and no five of them are
enough:

1. **The concept is NEEDED FOR A NAMED DECISION this run**: a member of a required
   concept group, a term of a published score, or the attribute of an admitted
   direction, priority or requirement. Convenience and enrichment do not qualify.
2. **The concept is NOT `strict_exact_only`.** A strict concept is never adopted
   provisionally, for the same reason 7.6 never promotes a strict stem: a wrong
   resolution there passes every downstream check. Where a strict concept has a
   strong candidate, the run reports the candidate, the evidence, and the fact that
   the concept remains unresolved, and it computes nothing from it.
3. **The candidate PASSES THE CONCEPT'S OWN VALUE CHECK** at 3.6, on the shape
   token the dictionary declares, computed from the column's values and not from
   its header.
4. **The candidate is POPULATED**: its non-null share within scope is at or above
   PROVISIONAL_ADOPTION_MIN_FILL, and the share is printed. A column resolved and
   empty is an absent column under 3.8 and this does not change that.
5. **The candidate is UNIQUE, OR THE TIE IS A DECLARED SIBLING SET UNDER 7.4b**:
   exactly one column clears tests 3 and 4 for that concept. Where two or more do,
   NEITHER is adopted, both are named with their evidence, and the concept stays
   unresolved. There is no leftmost tie-break here. **The ONE exception is a
   SIBLING SET, decided by 7.4b and by nothing else.** A sibling set is N columns
   that tie for one concept BECAUSE EACH ANSWERS IT ABOUT A DIFFERENT MEMBER of a
   member set the run has already admitted, which is not the ambiguity this test
   exists to catch. 7.4b's tests are ADDITIONAL to these six and never instead of
   them: every column in a sibling set clears tests 1, 2, 3, 4 and 6 on its own,
   exactly as a lone candidate would.
6. **No FORBIDDEN NEIGHBOUR of the concept also matches the candidate**, by name or
   by value check. The refusal list in 3.7 reaches this route exactly as it reaches
   every other.

**WHAT IT IS RECORDED AS.** Event `ADOPTED_PROVISIONAL`, `decided_by` RESOLVER,
`confidence` MEDIUM, with the six tests' results in `rejected_candidates` and
`value_classification` as usual. Where test 5 cleared as a sibling set rather than
as a unique candidate, the record says so in those words and carries 7.4b's mapping
inside the same event. It is used for every feature that concept feeds in
THIS RUN, and every one of those features is named in the disclosure, so a reader
can see the full reach of one adoption rather than discovering it a figure at a
time.

**WHAT IT MUST DISCLOSE, AND WHERE.** Two places, both mandatory. In the audit: the
header verbatim, the concept it was adopted for, the shape token it satisfied, its
fill share, the runner-up it beat or the statement that there was none, and the
words that it was adopted provisionally rather than resolved from a stem. And
BESIDE THE FIGURE OR SECTION IT FED, in one line, because a reader who never opens
the audit is entitled to know that a number they are about to act on rests on a
column this method matched by its values rather than by its name.

**WHAT IT MAY NEVER DO.** It never writes back to COLUMN_CONCEPT_DICTIONARY, to the
ORG config, or to any standing dictionary, on its own authority or on anybody's:
promotion is an ORG-tier act under 7.5, which requires a USER decision or a
VALUE_CHECK at HIGH confidence, and a provisional adoption is neither. What the run
MAY do is PROPOSE, in the closing summary, in the form the binding owner pastes,
with the evidence attached, so the second run at that organization resolves by
binding rather than by inference. It never raises its own confidence between runs,
and seeing the same header twice is not evidence: two provisional adoptions are two
inferences, not a confirmation.

**WHERE THE BAR IS NOT CLEARED, NOTHING IS ADOPTED AND THE CONSEQUENCE IS NAMED.**
The concept stays unresolved, every decision that needed it is reported as not
attempted rather than as zero, and the report says which column was closest and
which test it failed. That sentence is the whole difference between a run that
could not answer a question and a run that answered it wrongly.


## 7.4b The SIBLING SET: N columns that tie because they are siblings, which is not an ambiguity

**WHY TEST 5 REFUSED SOMETHING IT WAS NOT WRITTEN TO REFUSE, MEASURED.** A servicing
evidence file of 190 rows, joined on the unit identifier, carried eight boolean
columns mapping one to one onto the eight numbered requirements of the
organization's own published standard. Eight of them passed the concept's value
check at test 3 and cleared PROVISIONAL_ADOPTION_MIN_FILL at test 4, on measured
fills from 0.7526 to 1.0000 against a floor of 0.60. Test 5 asked for exactly one,
saw eight, and adopted none. Four gap terms and three exception flags were
therefore never evaluated on any row, and 114 of the 190 rows read that no action
could be derived, two columns away from a file that answered the question account
by account. **The refusal gets MORE certain as the evidence file gets more
complete**: a file carrying one boolean column can be adopted and a file carrying
one per requirement cannot, which is the wrong way round.

**WHAT TEST 5 IS FOR, AND IT STILL IS.** Test 5 exists to stop a run PICKING
ARBITRARILY BETWEEN TWO COLUMNS THAT MEAN DIFFERENT THINGS. Two candidates for one
concept are a coin flip: whichever is taken, the other was equally entitled, the
two can disagree on a row, and nothing in the run can say which disagreement is
right. That refusal is correct and nothing here weakens it. **The distinction this
section draws is between columns that COMPETE for a concept and columns that
PARTITION it.** Two columns compete when both purport to answer the same question
about the same unit; picking one is a guess. N columns partition when each answers
the same KIND of question about a DIFFERENT MEMBER of a set the run already holds;
picking one would be the mistake, because the answer is the whole table. The first
is a coin flip and is refused. The second is a table, and a run that holds the
table reads it.

**HOW A RUN TELLS THE TWO APART. ALL FIVE MUST HOLD, and no four are enough.**

S1. **THE MEMBER SET WAS ADMITTED, NEVER INVENTED.** The run has already ADMITTED,
this run and by its own admission test, a set of members: the numbered requirements
of a published standard, the enumerated items of an admitted direction or priority,
or a bound programme list. It is attributable, it is dated, and it was read from a
source. **IT IS NEVER DERIVED FROM THE CANDIDATE HEADERS THEMSELVES.** N similar
headers do not get to declare themselves a set; that is how a run would talk itself
into any tie it liked. Where the only evidence for the set is the columns, test 5's
uniqueness stands and nothing is adopted.

S2. **THE CONCEPT IS ONE THE MEMBER SET INSTANTIATES.** The concept the candidates
tie for must be per-member by nature: each member has its own answer for each unit.
Where the concept can hold only ONE answer per unit, which is the ordinary case for
an identifier, a measure, a date or a scope code, a sibling set does not exist,
test 5 stands unchanged, and the tie is the ambiguity it was written for.

S3. **THE MAPPING IS ONE TO ONE, AND IT IS BUILT BY THE ORDINARY PASSES.** Each
candidate maps to exactly one member and each member takes at most one candidate,
established by running PART 3's own passes with the MEMBER'S OWN NAME on one side
and the COLUMN HEADER on the other: the same normalization, the same route order,
the same short-string guard, the same tie-break rules. Two candidates mapping to
one member is the original ambiguity inside the set and voids it. A mapping built
by position, by column order or by eye is not a mapping.

S4. **NO CANDIDATE IS LEFT OVER.** Every column that cleared tests 3 and 4 maps to
a member. **ONE UNMAPPED CANDIDATE BREAKS THE SET**, the tie is a genuine ambiguity
again, nothing is adopted, and the report names the unmapped column. This test is
the door: a column that answers the concept and belongs to no member of the
admitted set is precisely the second, different meaning test 5 refuses, and its
presence is evidence that the run does not in fact know what these columns mean.

S5. **THE SIBLINGS ARE COMMENSURABLE, AND EACH CLEARS THE BAR ALONE.** Every
candidate carries the SAME shape token, passed the SAME value check at test 3, and
clears test 4's fill floor on its own, with its own share printed. Tests 1, 2 and 6
of 7.4a are also run against each candidate individually. A column tripping a
forbidden neighbour at test 6 is STRUCK from the set and named, and the member it
mapped to is then a member with no column, which is an ordinary outcome; it does
not void the set, because striking it removes a meaning rather than leaving one
unaccounted for. A set half of whose columns are booleans and half rates is not a
sibling set at all.

**WHAT MAY THEN BE DONE WITH IT, AND IT IS A TABLE RATHER THAN A COLUMN.**

- **THE ADOPTION IS OF THE SET.** The concept resolves PER MEMBER. No column is
  elected to represent the others, the set is never collapsed into one column, and
  there is no such thing as adopting four of the eight.
- **EVERY FIGURE IS EVALUATED ONCE PER MEMBER**, against that member's own column,
  and **CARRIES THE MEMBER'S NAME BESIDE IT WHEREVER IT IS PRINTED**: every gap
  term, every flag, every count, every action and every cell. A figure from a
  sibling set that does not name its member is a figure the reader cannot check
  against the standard it came from, which is the only thing that makes the
  adoption safe.
- **NO ROLLUP IS INVENTED.** Where a feature needs ONE answer per unit rather than
  one per member, the run does NOT synthesize it by AND, by OR, by majority, by
  count or by any rule of its own. It may aggregate ONLY where the ADMITTED SOURCE
  ITSELF STATES THE AGGREGATION, and it then prints the aggregation rule and the
  source's own words for it beside the figure. Otherwise the per-unit answer stays
  UNRESOLVED and is reported as not attempted, and the per-member answers still
  ship. A partial answer named per member is worth more than a rollup nobody
  authorized, and the two are not close.
- **IT IS ONE ADOPTION, RECORDED ONCE.** Event `ADOPTED_PROVISIONAL`, `decided_by`
  RESOLVER, `confidence` MEDIUM, exactly as 7.4a, with the whole mapping inside the
  one event. It is never recorded as N separate adoptions, because the columns
  stand or fall together and N records would hide that.

**WHAT IT MUST DISCLOSE.** Everything 7.4a's disclosure rule requires, per column,
and four more, all mandatory:

1. **THE MEMBER SET**, named with its source, its date and its originator, and the
   words that it was ADMITTED this run rather than assumed.
2. **THE MAPPING IN FULL**, member to header, one row per member, **including every
   member that got no column**, named as such. A reader who sees eight answers must
   never be left to read them as the whole standard.
3. **THE MEMBER, BESIDE EVERY FIGURE THE SET FED.** 7.4a requires one line beside
   the figure; on a sibling set that line is per member and not per set.
4. **THE AGGREGATION, WHERE ANY WAS APPLIED**: the rule, and where in the admitted
   source it is stated. Where none was applied because the source stated none, that
   is disclosed too, beside the per-unit answer that was not attempted.

**THE DOOR THIS DOES NOT OPEN, SAID PLAINLY SO IT IS NOT REOPENED.** It does not
admit two columns that both answer ONE member: that is S3, and it is the original
coin flip, unchanged. It does not admit a set the run assembled out of the headers
in front of it: that is S1. It does not admit a leftover column by calling the rest
a set: that is S4. It does not admit a per-unit answer the source never authorized:
that is the rollup rule. It does not lower the evidence bar on any single column,
because every column in the set clears every test it would have had to clear alone.
And it never promotes: 7.4a's promotion rule governs unchanged, so a sibling set is
PROPOSED to the binding owner as a mapping, with its evidence, and is never written
back to any standing dictionary by the run.

**WHERE THE SET IS NOT ESTABLISHED, THE CONSEQUENCE IS NAMED.** 7.4a's closing rule
governs word for word: nothing is adopted, every decision that needed the concept is
reported as NOT ATTEMPTED rather than as zero, and the report additionally names
which columns tied, which member set was considered, and which of S1 to S5 failed.

## 7.5 Which learnings are promoted into the standing dictionary

Promotion is an ORG-tier act, never a PERSON-tier one. A run proposes; the
binding owner accepts.

A stem is proposed for promotion when all of these hold:

1. It was decided by USER, or by VALUE_CHECK at HIGH confidence.
2. It is at least MIN_STEM_LENGTH normalized characters.
3. It does not collide with an existing stem in a different concept. A collision
   is reported rather than resolved by the run.
4. It does not name an entity, a period, a rate or an originator, all of which
   belong in their own taxonomies.
5. It has been seen in at least two distinct source periods, OR it was named
   directly by a user.

The proposal is written into the closing summary of the run in the same form the
binding owner will paste into the config, so one file stays authoritative for the
whole organization rather than every user relearning the same header.

## 7.6 Which learnings are never promoted

- A stem shorter than MIN_STEM_LENGTH.
- A stem that would resolve for a strict-exact-only concept. Those concepts grow
  only by an explicit ORG decision, because a wrong resolution there is invisible
  downstream.
- A stem derived from a working extract named after a person.
- A stem that appeared only in a container the run scored as documentation.
- Anything the run inferred at LOW confidence.

## 7.7 The reporting rule

Every run reports, in the audit section:

- Every header that did not resolve, by literal text.
- Every concept that resolved through an ask, and who decided it.
- Every concept that resolved by the value check after failing the name match.
- Every concept that resolved and was empty.
- Every ambiguous resolution, with both candidates and the reason one won.
- Every column adopted provisionally under 7.4a, with the six tests' results, and
  every feature it fed.
- Every SIBLING SET adopted under 7.4b, as ONE entry: the member set with its
  source, its date and its originator; the full member-to-header mapping including
  every member that got no column; any column struck at test 6 and why; the
  aggregation rule and the source's own words for it where any aggregation was
  applied; and every feature the set fed, per member.
- Every concept left unresolved that a named decision needed, with the decision it
  cost and the closest candidate with the test it failed.
- Every stem proposed for promotion.

A header that does not resolve is a skill defect, not a user error, and this
report is how the defect gets fixed once for everybody instead of being worked
around silently by every user in turn.


---

# CHANGE LOG: ACCEPTANCE TEST REMEDIATION

Two corrections after two hostile acceptance tests.

1. **A stem collision in the seed dictionary, removed.** The not-actionable flag
   and the pipeline stage concept both carried the bare stem for a status column,
   and the not-actionable flag also carried a stem that is a stage name in almost
   every pipeline. The three passes in 3.3 run exact first across the whole header
   list, both concepts offered an exact match, and the tie was settled by column
   position. Where the exclusion concept won, the exclusion silently removed a
   stage, the funnel reconciled, and every downstream invariant passed. That is
   the failure SD-POP-05 names as the one no gate can catch, and the seed
   dictionary was shipping it. The stem is removed from the less specific concept,
   the two concepts now name each other as forbidden neighbours, and 3.7 gains a
   tie guard: where two concepts both match exactly and either is strict, neither
   resolves. Reported as report 2 D9.
2. **The Req column now matches the schema's validation of it.** The schema
   requires "exactly three entries carry required true"; the seed dictionary
   carried eleven entries with some form of required, because the intent was three
   required CONCEPT GROUPS satisfied by any member. A binding owner validating the
   config against the schema got a failure on a dictionary nobody wrote. Part 6
   now opens with a Req legend naming the three groups explicitly, and the two
   files read the same way. Reported as report 2 D10.

## Third pass, round 2 regression

- **The unit-level commitment date concept was added, N8.** The scoring rule that
  needs it was built correctly in the planning skill and resolves through this
  dictionary, using the `feeds` list as its switch, but no seed concept fed it, so
  on a default binding, which is every first run, the rule could not fire and a
  ranked list silently reduced to the population sorted by size. The entry sits in
  6.6 with the exact feeds value the rule tests for, plus forbidden-neighbour
  declarations against the last-contact and exit-date concepts.
- **The proper-subset guard was moved here, N3.** It had been written into one
  skill only, while this file owns the absence map that the other skills resolve
  through, so two skills resolved the same wholly blank grouping column
  differently off the same file. It now sits directly under the 3.12 table, where
  the map is, and SD-QUA-04 carries it as a mechanism bullet.

## Fourth pass, final regression

- **Every seed table in Part 6 now carries all seven declared columns, N9.** Only
  6.1 and 6.3 did. 6.2 was missing forbidden neighbours; 6.4, 6.5, 6.6, 6.7 and
  6.8 were missing both strict and forbidden neighbours, so those two fields had
  been written as sentences inside the Feeds cell. A run building the dictionary
  from these tables reads columns, so both fields were EMPTY when built, and the
  unit-level commitment rule, whose third test reads the forbidden-neighbours
  field and which requires all three of its tests to hold, could never fire. The
  Part 6 preamble now states that a field written as prose inside another cell is
  an empty field, and says so with the case that proved it.
- **concept_unit_commitment_date is marked strict and declares its neighbours
  reciprocally.** Its neighbours are concept_last_engagement_date,
  concept_last_evidence_date and concept_exit_date, and all three name it back.
  Without strictness a header naming a last renewal date matched the commitment
  stem with nothing to refuse it, and a past event scored as a future obligation.
- **3.7 now states the converse, in the form that does not break resolution.** The
  refusal mechanism reaches EVERY concept that names a forbidden neighbour,
  strict or not, because most concepts must resolve by prefix and substring to
  work at all and forcing strictness on every neighbour-declaring
  concepts would break them. Strictness is the narrower instrument and is reserved
  for concepts whose wrong resolution is invisible downstream, which is why the
  date concepts carry it. The tie guard fires where either candidate is strict OR
  the two name each other.

## Fifth pass, live end-to-end run against an undescribed file

Four of fifteen columns in an ordinary operational export resolved to nothing,
and the two that cost the most, a last-contact date and a status field, are
columns that appear in essentially every operational export in every industry.

- **"branch" removed from the finest scope concept, N-defect 2.** It was a stem in
  TWO seed scope concepts. The tie guard does not reach a prefix collision between
  two non-strict concepts, so the resolver fell through to leftmost-column, which
  is arbitrary. The two concepts now name each other as forbidden neighbours.
- **"region code" removed from the jurisdiction concept, N-defect 3.** It is an
  EXACT match for an ordinary scope-code header and exact passes run first, so the
  resolver's first answer was that a scope code is a legal jurisdiction.
- **The last-engagement stems were broadened to about nineteen, N-defect 4**,
  including the ordinary service-industry forms. A header any human reads
  instantly was resolving to nothing and taking a section, an alert line, a
  membership flag, an exception flag and a column with it.
- **The unit-unavailable stems now cover the qualified status forms, N-defect
  5**, so an ordinary status header no longer leaves the exclusion concept unbound
  and a dozen unworkable units ranked at full weight.
- **Six further stem collisions were found by validating the dictionary rather
  than by reading it, and removed:** "state" from the stage concept, "district"
  from the subregion concept, "group" from the top scope concept, "programme" from
  the parent-group concept, and "tier" and "band" from the unit-type concept.
- **Eleven forbidden-neighbour cells were written in bare English rather than as
  concept keys, and are now typed.** A cell reading "unit name" resolves to no
  concept, so every rule reading that field read an empty value and did not fire.
  The schema field spec now says the field holds concept keys and nothing else.
- **F5.1 step 2 and 3.7 gave OPPOSITE instructions for the same column and neither
  cited the other.** Step 2 says a correctly shaped column with an unrecognized
  header can still be found by its values; 3.7 says a strict concept whose exact
  name is absent is never approximated. Two competent readers produced two
  different artifacts off one file. The precedence now says 3.7 wins over silent
  adoption ALWAYS, because a value check confirms a SHAPE and cannot confirm a
  SUBJECT, and introduces step 2b: for a strict concept, a SINGLE value-check
  candidate is carried forward as an offered candidate, never adopted, and two or
  more candidates leave the concept unresolved with no question spent.
- **F5.1a is new: one question may be spent on a strict concept that feeds more
  than one thing.** The tester's own closing point was that a strict concept which
  fails should fire a question and that the only question mechanism available was
  gated behind a binding owner a first run does not have. F5.1a is explicitly
  PERSON-tier: it asks what a column in the user's own file means, never what the
  organization is, so the wall in reference/binding-interview.md I1 is not crossed and no
  binding authority is required. At most one such question per run, batched with
  the required-concept questions, inside the run's existing budget, with a
  deterministic tie-break so the same file always spends it the same way.
- **A candidate that cannot be asked about is still REPORTED**, with the concept,
  the column and the sentence that it was not used, which is the difference
  between failing closed and failing silently.

The seed dictionary now validates clean: every entry carries all seven columns as
structured columns, every forbidden neighbour resolving to an existing concept
key, every strict entry naming at least one neighbour, and no stem appearing in
two concepts.

## Sixth pass, confirmation run at three altitudes

- **F5.1b is new: confirming a VALUE-level default on the user's own file.** A
  resolved column supplies a concept, not the values its downstream rule needs,
  and the two are separate bindings. The gap put a prospect at rank one of a
  working plan. F5.1b shows the whole decision, every value the default matched
  and every value it did not, each with its count, and invites a correction.
  Like F5.1a it is PERSON-tier, so it needs no binding authority and a frontline
  user on a first run may be asked it. **Silence proceeds on the default and is
  recorded as unconfirmed; it never reverts to excluding nothing.**
- **The entry-date concept gains the relationship-start stems**, including client
  since, customer since, member since, onboarded, relationship start, joined and
  established. Their absence silently disabled the cold-start entry test, so the
  corroboration rule added in the previous pass had nothing to corroborate with
  and the right answer arrived by luck rather than by design.
- **3.6 gains the BARE-YEAR TRAP rule.** A column of four-digit years matched "all
  digits, consistent length" and classified as an identifier before the date rung
  was reached, so a column that plainly held a date failed a date value check. A
  bare four-digit value inside YEAR_PLAUSIBLE_RANGE is now read as a DATE at YEAR
  granularity, tested before the identifier rung and ONLY for date concepts, with
  the granularity recorded so nothing downstream can claim a day from it.

## Seventh pass, final acceptance run at three altitudes

- **3.6 gains the alphanumeric identifier rung, and it is the fix that stops a run
  from stopping.** An identifier of the form three letters, a hyphen and five
  digits is the commonest identifier shape there is. It was not digits, not a
  number, not two-valued, not short-repeating and not a date, so it fell to free
  text; the REQUIRED unit-identifier concept then failed its own value check on an
  EXACT header match, no alternative resolved, and a literal reading refused the
  only required concept in the file and stopped the run. Rung 4 is tested before
  the free-text rung. Rung 3 also gained a second condition, distinctness or
  IDENTIFIER_MIN_WIDTH, because digits of consistent length alone had made every
  small integer column an identifier.
- **The classifier and the dictionary now speak ONE vocabulary.** The ladder emits
  a SHAPE TOKEN from a closed set of seven, and every value check in Part 6 was
  retyped into those tokens. Previously the two described the same column in two
  different vocabularies, which is why a reader had to prefer one to proceed.
- **3.6a states the precedence, in three rules.** The classifier DEFINES the
  shapes; a value check SELECTS among them, so they cannot disagree about what an
  identifier looks like. A value check naming a shape the classifier cannot emit is
  a DICTIONARY DEFECT: it is recorded, treated as UNSATISFIABLE rather than FAILED,
  and never refuses a column. And a REQUIRED concept is never refused on shape
  alone where the name matched exactly and nothing else is available, with an
  absolute guard: the relaxation never applies to a mismatch that changes
  arithmetic, so a rate taken for a measure is refused exactly as before.
- **The Part 6 validator now tests five things**, adding that every value check
  parses into the token set.

## Eighth pass, release acceptance run

- **The measure concepts gain the money-quantity stems they were missing**:
  premium and its written, earned and annual forms, billings, fees, contract value,
  annual value, spend, sales, turnover, bookings, invoiced, commission, margin,
  recurring revenue and the usual variants. Without them the ranking measure
  resolved by value check alone at an ordinary business.
- **concept_rate_or_ratio is added, strict, naming every measure concept as a
  forbidden neighbour in both directions.** A ratio is recordable and reportable and
  is NEVER the ranking measure. The trap that produced it: a ratio column whose
  maximum just exceeded 1 missed the rate rung, satisfied the same count-or-measure
  test as the real measure, and was one tie-break away from becoming the axis the
  entire plan was ranked on, with every gate passing and the front panel faithfully
  printing the wrong column's name.
- **F5.1 step 2 gains a real tie-break for a multi-candidate value-check
  resolution.** Five ordered tests, stopping at the first that leaves one candidate,
  and 3.3's leftmost-column rule is explicitly NOT extended here by analogy. For a
  REQUIRED concept an unbroken tie is a PERSON-tier QUESTION, and where no answer
  arrives the concept is UNRESOLVED and the run takes the required-concept-absent
  path. **It never picks one and proceeds**, because a ranking is the one output
  where an undisclosed wrong column is invisible to every downstream check. A
  single surviving candidate is taken with a RESOLVED BY SHAPE notice naming what
  was discarded and by which test.
- **3.3a adds PASS ZERO: a header matching a name the ORGANIZATION BOUND is matched
  before any seed stem this bundle shipped.** Scope level display names and keys,
  the population's unit nouns, role display names and the bound measure name. An
  organization that has just told the interview what its levels are called, and then
  supplies a file with a column headed one of those exact words, has already
  answered the question the seed dictionary was guessing at; without this rule a
  frontline user's own scope column was invisible. Pass zero is still subject to the
  forbidden-neighbour refusal and the value check, two bound names matching one
  header is an ambiguity, and every pass-zero match is recorded as such and offered
  as a learned stem.
- **Classifier rung 4 is disambiguated.** Consistent length ALONE is never
  sufficient, because that types every fixed-width category column as an identifier.
  The rung now requires consistent length or pattern AND either letters and digits
  both present in every value, or a separator at the same position in every value.
  Verified: a letter-prefixed account code and a short separated region code both
  type as identifiers, and a fixed-width category column does not.
- **concept_next_action is added**, so the no-next-action gap term has the source
  concept its definition now names.

The Part 6 validator passes on all five tests over every concept in the seed
dictionary: seven columns each, every forbidden neighbour resolving, every strict
entry naming a neighbour, no stem in two concepts, and every value check parsing
into the shape-token set. The number of concepts is not stated here; it is the
row count of the Part 6 tables and changes whenever one is added.

## Ninth pass, ship-or-no-ship run

- **The pass-zero ambiguity guard fired on the NORMAL case and refused the headers
  pass zero exists to resolve. Rewritten in three parts.**
  - **Two bound names resolving to the SAME concept are CORROBORATION, and the
    header resolves.** Refusing a header because two independent parts of an
    organization's own configuration agree about it is the opposite of what
    precedence is for. Two targets are the same concept when they are the same
    concept key, which is what happens whenever a role is named for the level it
    owns; or when one is the scope concept for the level equal to UNIT_LEVEL_KEY
    and the other is the unit identifier, because at the unit level those are the
    same column. That second equality is FORCED by the schema rather than being a
    coincidence, since UNIT_LEVEL_KEY must be a SCOPE_LEVELS key, so the unit noun
    equals the finest level's display name at nearly every organization.
  - **A bound name matching only a PREFIX of a longer header determines the
    SUBJECT, never the concept.** A unit noun prefixes the identifier column, the
    name column and the status column alike, and those are three different things.
    The prefix establishes what the column is ABOUT and narrows the seed passes;
    the residue decides which concept it is.
  - **A pass-zero refusal removes the bound-name resolution ONLY, and is never
    terminal.** The three seed passes still run. A tie between two of an
    organization's own words must never cost a header a shipped stem would have
    resolved, and must never refuse a run.
- **The guard is verified rather than asserted**, against the four real headers and
  a genuine-conflict case, with the table printed in 3.3a.

## Tenth pass, final ship run

- **The Part 6 validator gains a sixth test, and it applies to EVERY table in the
  bundle rather than only to this file's dictionary: CELL COUNT AGAINST THE
  TABLE'S OWN HEADER.** A malformed row in a table read by column position is
  SILENT. Nothing looks wrong, no gate fires, and a run simply reads the wrong cell
  and prints it in the wrong place. One such row survived several rounds of review
  in the schema's own defaults appendix and was live on a shipping artifact. The
  check restarts at each header row rather than assuming one table per section,
  because a section holding twenty-five group tables is the normal shape here.

## Release sweep

- **The change-log line stating the dictionary's size no longer states it.** The
  count of concepts is the row count of the Part 6 tables and changes whenever one
  is added, so it is derived rather than restated. This is the same defect class
  the schema's maintainer note names, found in this file by the release sweep.

## Later pass, the unknown column and the entity column

- **The seed lists on both sides of the entity-versus-item discriminator were
  widened, because the discriminator had nothing to discriminate between.** A book
  of business named its countable instrument with a trade word neither concept
  carried, so the column resolved to nothing at all, the organization's own first
  published priority for the period reached zero rows on every sheet, and the only
  trace was a zero in a source count deep in the method section. A seed list that
  misses a concept by one word is not a narrow match, it is no match, and the
  failure is silent because an unresolved concept produces a zero rather than an
  error. The discriminator itself is unchanged; it now has candidates.
- **7.4a is new: what a run may do with a strong candidate the dictionary does not
  carry, on a first run where nothing is bound.** Every route in 7.4 is keyed on
  who decided, and on a first run at an unbound organization two of the four decide
  nothing: there is no bound dictionary and often nobody to ask. A run could see a
  column that plainly answered a concept and have no rule permitting it to use it,
  so it published a zero that looked exactly like a genuine absence. Provisional
  adoption now has six mandatory tests, a recorded event, a two-place disclosure,
  and an absolute prohibition on writing anything back to a standing dictionary or
  to the organization's configuration. A strict concept is never adopted this way.
- **`concept_creditable_entity` is new, and it is the column a scoring factor was
  multiplied by with no stated way to find it.** `entity_weight` is a factor of the
  alignment term on every row of every ranked list, the entity taxonomy said what
  the entities were worth, and nothing said which column carried them. One run
  invented the procedure, correctly, and said so. The concept now carries seed
  stems, a value check, reciprocal forbidden neighbours with the unit-type and the
  two count concepts, a coverage fallback with a threshold and a margin, and a
  STATED NEUTRAL of 1.0 for the case where nothing resolves, which is the identity
  multiplier rather than a floor or a zero.
- **The reporting rule gains the unevaluated decision.** A named priority,
  requirement or predicate that could not be evaluated is announced in the section
  the decision belongs to, not only in the audit. An unevaluated priority is a fact
  about the plan, not a footnote about the method.

## Seventeenth pass, the evidence file that could never be scored

- **7.4b is new, and it is the reason 7.4a's whole route was unreachable on the
  commonest shape of evidence file there is.** Test 5 asked for a UNIQUE candidate,
  and a real keyed evidence file carries one boolean column per numbered
  requirement, so the columns always tie with each other and the tie gets more
  certain as the file gets more complete. Measured on a live run: eight candidates,
  fills from 0.7526 to 1.0000 against a floor of 0.60, none adopted, four gap terms
  and three exception flags never evaluated, 114 of 190 rows reading that no action
  could be derived. Test 5 now clears on a UNIQUE candidate or on a DECLARED
  SIBLING SET, and 7.4b states the five tests that separate a sibling set from the
  ambiguity test 5 was written to refuse: the member set is admitted rather than
  invented, the concept is per-member, the mapping is one to one and built by
  PART 3's own passes, no candidate is left unmapped, and every column clears the
  bar alone. The adoption is OF THE SET, resolves PER MEMBER, names its member
  beside every figure, and invents no rollup: an aggregation is applied only where
  the admitted source itself states one, and otherwise the per-unit answer stays
  unresolved while the per-member answers still ship.
- **The door test 5 was closing stays closed, and 7.4b says so in its own
  paragraph** so that a later reader does not widen it: two columns answering ONE
  member is still a coin flip and still refused; a set assembled out of the headers
  in front of the run is refused; one leftover candidate voids the whole set; and
  nothing is promoted to a standing dictionary by any of it.
