# GROUP QUA: QUALIFIERS AND POPULATION SELECTION

### SD-QUA-01 Classify the phrase by TYPE before searching any column
- Rule: route the phrase to a column family first, then search only that family's
  columns.
- Mechanism: a cue-to-type-to-columns routing table. "Classifying before
  searching is what makes a miss recoverable: a phrase routed to a column family
  has a column to report and near-values to offer, while an unrouted phrase has
  neither."
- Prevents: a misspelling and an uninterpretable word looking identical, which
  makes a resolver widen the report.
- Source: P-D85; R-D20
- Applies: PLANNING, REVIEW, SCORECARD

### SD-QUA-02 Never run a match across the whole sheet
- Rule: confine every match to the columns the routing step selected. "Whole-sheet
  substring matching is how an execution flag reading age-verification code on
  all registers gets attributed to a product as a volume result, and how a county
  name lands in a city column."
- Source: R-D20; P-D89
- Applies: PLANNING, REVIEW, SCORECARD

### SD-QUA-03 Two axes, because a single label routes flags into arithmetic
- Rule: classify every column on two axes at once: the ENTITY it describes, and
  its MEASURE TYPE. Only a measure typed as a rate or volume may enter
  arithmetic. A column naming an entity and typed as a flag is never a volume
  metric.
- Source: R-D20
- Applies: PLANNING, REVIEW, SCORECARD

### SD-QUA-04 Resolve absence phrases by RULE, before any value search
- Rule: some qualifiers are represented by an empty cell, and a value search
  cannot find an absence. These are resolved by rule and the rule overrides any
  text match.
- Mechanism: the self-determined subset is a BLANK grouping field after null
  normalization; the managed subset is its complement; an unbenchmarked entity is
  one with no benchmark column present.
- Prevents: "Searching for the literal word finds nothing in any file, because
  the thing is represented by an empty field rather than by the word. A resolver
  that value-searches it falls through and silently widens to every unit in
  scope." Named as the single most consequential absence, because the
  self-determined subset is the top-tier signal for a direct-tier person.
- Mechanism, THE PROPER-SUBSET GUARD: an absence rule yields a usable subset only
  where the complement is a PROPER, NON-EMPTY subset. Where the field is blank on
  every row in scope, or populated on every row in scope, the distinction does not
  exist in this population. Record the subset as NOT PRESENT, skip every cut,
  filter and gate that depends on it, and name it in the audit. A subset equal to
  the whole population is not a cut; it is the population under a second name.
  This is the mirror of SD-PRS-18: a resolved-but-EMPTY column is absent, and a
  resolved-but-FULL absence rule is no distinction. reference/field-resolution.md 3.12 holds
  the map and the guard.
- General form: a category defined by an absence cannot be found by searching for
  its name.
- Source: P-D86; R-D21; guard added from report 1 D10
- Applies: PLANNING, REVIEW, SCORECARD

### SD-QUA-05 Convert a name to its stored code through a table; substring matching cannot do the conversion
- Rule: normalize a name to the stored code form through
  JURISDICTION_NAME_TO_CODE, then match exactly, and confirm the code is actually
  present in the column before filtering.
- Mechanism: "Coincidental substring containment is never evidence." One
  two-letter code happens to sit inside its own long name; most do not.
- Source: P-D87; R-D1 sub-doctrine 1b
- Applies: PLANNING, REVIEW, SCORECARD

### SD-QUA-06 An administrative suffix is a routing cue, not noise
- Rule: strip the suffix before matching and route the phrase to that one column
  and nothing else. "Left in, the suffix causes a miss; routed loosely, the bare
  stem can match a like-named locality and silently scope the report to one
  hamlet inside the area the user asked for."
- Source: P-D88
- Applies: PLANNING, SCORECARD

### SD-QUA-07 The match cascade, in order, confined to routed columns
- Rule: exact, then normalized-exact, then prefix, then bidirectional substring.
  Case-fold, strip punctuation, collapse whitespace first. Never run it across
  the whole sheet.
- Source: P-D89; R-D20
- Applies: PLANNING, REVIEW, SCORECARD

### SD-QUA-08 A compound phrase splits before classification and applies with AND
- Rule: a separator splits the phrase; both halves are classified and matched
  independently and then applied together. Do not tokenize a multi-word value.
  "Place names repeat across jurisdictions, which is exactly why the second half
  is not optional when the user supplied it."
- Source: P-D90
- Applies: PLANNING, SCORECARD

### SD-QUA-09 Qualifiers are applied in the scope stage, before every exclusion and before the percentile
- Rule: the qualified set becomes the population for everything downstream. "The
  qualifier changes who is in the population; it never changes the method applied
  to that population." Applying it later "would rank them against a population
  they are not being compared to, and the front panel would describe a percentile
  that means nothing."
- Source: P-D91
- Applies: PLANNING, SCORECARD

### SD-QUA-10 A miss is reported loudly, with three outcomes that must never be collapsed
- Rule: matched, proceed and disclose. Routed to a column type but no value
  matched: stop before ranking and ask, reporting the phrase, the column tested
  and the MISS_SUGGESTION_COUNT nearest values present, ranked by ascending
  normalized edit distance with alphabetical tie-break so the same miss always
  returns the same list. Routed to no column type at all: say which columns were
  tested, run the request without that term, and label the report unqualified.
- Rule: "Never take the second row for a phrase that classified successfully."
- Prevents: "an empty report looks like a finished one."
- Source: P-D92
- Applies: PLANNING, REVIEW, SCORECARD

### SD-QUA-11 Distinguish "the column is absent" from "the value is not in it"
- Rule: they read identically in the output and have completely different fixes.
- Source: P-D93
- Applies: PLANNING, REVIEW, SCORECARD

### SD-QUA-12 Never silently widen
- Rule: if a qualifier cannot be applied, the report must say so on its face. "A
  report that quietly covers the user's whole span when they asked for one place
  is wrong in the way that destroys trust, because every number in it is
  internally consistent."
- General form: this is the general statement of the whole failure model. Any
  silent widening is worse than a loud failure.
- Source: P-D94
- Applies: PLANNING, REVIEW, SCORECARD

### SD-QUA-13 Downstream guards work unmodified on a qualified population
- Rule: a qualifier that leaves few units hits the existing degenerate-scope
  guards. Nothing new is needed.
- Source: P-D95
- Applies: PLANNING, SCORECARD

### SD-QUA-14 Record what was routed, resolved and matched, with counts
- Rule: for every routed column record the phrase, its resolved entity and
  measure type, the column, the operator, and the matched value set with row
  counts. "This is what makes a disputed number traceable."
- Source: R-D20
- Applies: PLANNING, REVIEW, SCORECARD

---
