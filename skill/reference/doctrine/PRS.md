# GROUP PRS: PARSING AND RESOLUTION

The mechanics live in reference/field-resolution.md. The rules live here.

### SD-PRS-01 The published table is authoritative for dates, types and eligibility; parse it, do not infer
- Rule: read the published columns and use them. Infer nothing the source states.
- Source: P-D125
- Applies: PLANNING, SCORECARD

### SD-PRS-02 Plan for a document built for the eye, not for a parser
- Rule: extract with layout preserved first. If layout mode is unavailable or the
  pairing is ambiguous, read the page as an image and treat that as a normal tool
  rather than a last resort. Pair by proximity, then CONFIRM against a second
  reading, and report the confidence. "Two agreeing readings is a confirmed pair;
  one reading is a candidate." Report how many were confirmed by two readings,
  how many rest on one, and how many could not be paired.
- Prevents: giving up on a table because the first extraction looked like noise.
- Source: P-D126
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-03 An unreadable date is banded down, never defaulted up
- Rule: apply the descending CLOSE_WEIGHTS ladder by how much is known.
  "Silently defaulting an unparsed date to closes this period is the exact
  over-weighting bug this rule exists to prevent, and it is invisible in the
  output."
- General form: never default an unknown to the value that maximizes its score.
- Source: P-D127
- Applies: PLANNING, SCORECARD

### SD-PRS-04 Read the date; never assume the window
- Rule: the published due date is per item and frequently falls outside the
  period window. On one real file that error applied full weight to the single
  largest item in the file.
- Source: P-D128
- Applies: PLANNING, SCORECARD

### SD-PRS-05 An unreadable window is derived, not fatal
- Rule: derive the window from OPERATING_WINDOW_DERIVATION_RULE, say plainly it
  was derived, and continue. "A derived window dates the items correctly in
  almost every case; an unread window would zero the entire alignment term and
  the workload term at once."
- Source: P-D129
- Applies: PLANNING, SCORECARD

### SD-PRS-06 Anchor a structural block on the DATA, not on the dictionary
- Rule: resolve the block of work-item columns before matching any data concepts,
  using a structural marker in the data itself, and stop before an exactly
  matched boundary. Three ordered fallbacks when the marker is absent, ending in
  "no block exists", which is a valid outcome.
- Prevents: two symmetrical failures. Greedy substring matching consumes work-item
  columns as data concepts, because "more than half of the work-item columns match
  some data-concept stem if they are offered to the matcher." Defining the block
  as everything to the right of the last mapped concept fails from the opposite
  end.
- General form: a rule about ordering a greedy resolver against a structural
  boundary.
- Source: P-D130
- Applies: PLANNING, SCORECARD

### SD-PRS-07 Match a boundary token EXACTLY and take the RIGHTMOST match
- Rule: normalize case, compare the whole normalized header for equality, and if
  more than one matches take the rightmost. Record the resolved anchor index.
- Mechanism: the documented harm. A decoy header contained the boundary token as
  a substring and sat forty-one columns to the left of the real boundary. "A
  substring search stops at the decoy and cuts the block from 72 columns to 31,
  discarding 57 percent of the work-item set."
- Prevents: a silent large data loss that leaves the output looking complete.
- Source: P-D131
- Applies: PLANNING, SCORECARD

### SD-PRS-08 Never use an optional metadata prefix as the admission test
- Rule: an originator prefix is optional metadata for weighting only.
- Mechanism: "41 of 72 work-item columns, well over half, carry no prefix at all,
  and they hold 96.8 percent of the unit-level signal. A prefix-based detector
  discards nearly the entire set and produces a ranking built on 3 percent of the
  data."
- Source: P-D132
- Applies: PLANNING, SCORECARD

### SD-PRS-09 A global count row is never used for scoring
- Rule: a count row scoped to the whole organization is a structural marker only.
  "Using it as a narrowness signal inverts the ranking."
- General form: a globally scoped statistic must never be used as a locally
  scoped one.
- Source: P-D133
- Applies: PLANNING, SCORECARD

### SD-PRS-10 Compute per-item counts from the FILTERED scope yourself
- Rule: "A narrow item is a sharper priority than a blanket one, and that judgment
  is only valid against counts drawn from the user's own units."
- Source: P-D134
- Applies: PLANNING, SCORECARD

### SD-PRS-11 Never take the first sheet on faith, and a name match still needs a column check
- Rule: score every candidate by resolvable required concepts. A name-matching
  sheet is taken only after confirming it resolves the required concepts, and
  falls through if it does not. Ignore documentation-named sheets. A sheet named
  after a person is a working extract, not the data sheet. Break ties by record
  count, never by the reported extent.
- Mechanism: one real file reported ten thousand rows against two thousand real
  records.
- Prevents: "A silent wrong-sheet pick produces a complete, confident, entirely
  wrong artifact: the worst failure this method has."
- Source: P-D136
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-12 When no single source covers the requested scope, concatenate rather than choose
- Rule: take every sheet whose resolved column set matches, concatenate,
  de-duplicate on identifier keeping the highest-measure row, and report how many
  were combined and how many duplicates collapsed. Concatenate only when one is
  genuinely not enough.
- Rule: this covers files of the SAME SHAPE, which add ROWS. A file of a DIFFERENT
  shape that shares an identifier adds COLUMNS, and that is a join, governed by
  SD-PRS-48. Never perform one under the name of the other.
- Source: P-D137
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-13 Detect the header row rather than assuming it
- Rule: read the first HEADER_SCAN_DEPTH rows, score each by the count of
  non-empty STRING cells, take the highest, and confirm the choice by resolving
  the required concepts before accepting it. Record the row chosen and its
  runner-up.
- Source: P-D138
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-14 Three matching passes, each run to completion before the next
- Rule: exact, then prefix, then substring, across the whole header list. Within
  a pass, first hit wins and ties prefer leftmost. "Run each pass to completion
  over every stem before starting the next, so an exact match anywhere in the
  sheet always beats a substring match."
- Source: P-D139
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-15 A short-string guard on fuzzy matching
- Rule: whenever either side is shorter than MIN_STEM_LENGTH normalized
  characters, only an exact match counts. Exact matching is never suppressed.
- Mechanism: a two-letter stem matches every header containing a longer word that
  happens to contain it, "and one such hit silently mis-maps the lookup key the
  whole artifact is built on."
- Source: P-D140
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-16 Confirm a resolved column by its VALUES, not only by its name
- Rule: check that a scope column's values look like codes and a measure column's
  values are numbers. A column that resolves by name but fails its value check is
  the wrong column: fall through and record both.
- Mechanism: a value-classification ladder. All digits of consistent length is an
  identifier or code; a decimal between 0 and 1 is a rate; a bare number above 1
  is a count or a measure; a short repeating value set is a status field; free
  text is a name.
- Quote: "Header says measure and the values are decimals between 0 and 1: it is
  a rate, not a measure, and the header is misleading. Trust the values."
- Source: P-D141
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-17 Coerce before comparing; a typed comparison against the wrong type fails silently
- Rule: read numeric-looking text as a number, parse date-looking text as a date
  across a named set of formats, and compare identifiers as normalized text.
- Mechanism: "A typed comparison against the wrong type fails silently and returns
  nothing: it does not raise, and it looks exactly like a file with no data in
  that column." And: "Subtracting a date from a string does not raise; it produces
  nothing, and a recency flag that silently never fires looks identical to a scope
  with no gaps."
- Source: P-D142
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-18 A resolved but EMPTY column is an absent column
- Rule: check each resolved column's non-null count within scope before using it.
  If it is zero, exclude it from every flag, gate, weight and benchmark it feeds,
  and list it as resolved but empty.
- Prevents: the single most damaging false-positive class. "A wholly empty
  commitment column would otherwise report every eligible unit as missing every
  commitment, and a wholly empty breadth column would put every unit on the
  breadth section."
- Source: P-D143
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-19 Normalize null-like VALUES, not just empty cells
- Rule: treat an empty cell, whitespace only, and every literal in
  NULL_LIKE_VALUES as missing.
- Mechanism: "a grouping cell reading null would otherwise classify a
  self-determined unit as a managed one, inverting the self-determined-only
  contract and every gate built on it."
- Source: P-D144
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-20 Register the STEM, never the full literal
- Rule: strip trailing period tokens, rate markers and leading originator
  prefixes before storing a dictionary entry, and keep every stem at
  MIN_STEM_LENGTH normalized characters or more. "A stem catches every dated
  variant automatically while a literal catches exactly one period."
- Source: P-D145
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-21 Unit and time-basis markers are interchangeable and must be recorded
- Rule: treat the rate suffixes as equivalent and strip the trailing period token
  before comparing, then record the suffix found, because together they are the
  unit and the time basis and both must be reported.
- Source: P-D146
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-22 A header that does not resolve is a skill defect, not a user error
- Rule: log the literal header text, continue with what did resolve, name it in
  the audit section, and report it so the stem joins the dictionary.
- Source: P-D147
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-23 Record every ambiguous resolution and who decided it
- Rule: the header text, the values seen, what it was resolved to, and whether
  the user or the value check decided it. "This is what lets the owner add the
  stem so the next person is never asked."
- Source: P-D148
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-24 Never analyze a partial source, and count RECORDS rather than the reported extent
- Rule: confirm the file opens, then count rows carrying a non-blank identifier
  rather than trusting the reported extent, which routinely overstates by
  thousands. A record count of zero is a hard gate. A small non-zero count is not
  measurable against any expectation, "because this method is forbidden to carry
  one, so do not guess at a threshold."
- Source: P-D149
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-25 The admission test for an input is column coverage, not its title
- Rule: a file is usable when it resolves an identifier, a measure and any one
  scope column. Everything else degrades gracefully. Refuse only when one of the
  minimum three is absent, and say which one was missing and what the file did
  contain. "The header dictionary is the test, not the filename."
- Mechanism: one scope column is enough because finer levels are read off it by
  prefix and coarser ones by truncation.
- Quote: "Do not attempt a ranking from a file with no measure: the measure is
  the one term the entire method rests on."
- Source: P-D150
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-26 Escalate up the hierarchy for an input, then filter down
- Rule: look for the coarser-level file, then coarser still. Each level up
  contains the level below, so a coarse file fully answers a narrow question once
  filtered. State which level was used.
- Source: P-D151
- Applies: PLANNING, SCORECARD

### SD-PRS-27 Decide which of several inputs is which BEFORE parsing
- Rule: resolve each file's period from its filename, banner rows and time basis.
  Never silently merge two sources, and never pick by upload order or filename
  sort.
- Source: P-D152
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-28 Do not caveat a matching supplied input
- Rule: if the uploaded file matches the referenced attachment on name and size,
  it is the same file. Say so plainly and move on. Treat it as the expected path,
  not a degraded one.
- Source: P-D153
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-29 Duplicate identifiers: MERGE the signals, do not just keep the best row
- Rule: keep the highest-measure row as the base, then merge the survivors'
  signals into it. A flag on any duplicate is a flag on the merged row, a match
  on any row matches the merged row, and a populated field on any row fills a
  blank on the base.
- Prevents: "Keeping only the highest-measure row without merging silently drops
  work items and directives that belong to the unit."
- Source: P-D154
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-30 Sanitize text at the boundary, on the way IN, not as a cleanup pass
- Rule: normalize every value read from the source before it reaches a cell. "A
  value sanitized at the boundary cannot reach a cell dirty; a value sanitized at
  the end has already been copied into intermediate structures the final scan may
  not walk."
- Mechanism: three entry points: source text, quoted third-party text, and text
  the skill writes itself.
- Source: P-D155
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-31 A valid join key is near-unique in both files and produces a one-to-one match
- Rule: require uniqueness at or above JOIN_UNIQUENESS_FLOOR in both files and
  reject many-to-many candidates. Prefer a column whose name or profile suggests
  a unit identifier over a geographic or personnel code, because those overlap
  heavily and are not unit keys.
- Mechanism: normalize before joining: trim whitespace, strip leading zeros,
  casefold, remove non-alphanumeric separators. "A code stored as text with a
  leading zero must still match its integer twin."
- Source: R-D24
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-32 The overlap floor is a hard stop
- Rule: matched rows must be at least JOIN_OVERLAP_FLOOR of the row count of the
  smaller file. Below that, stop and report both rosters.
- Prevents: "Without this floor, a near-empty intersection produces metrics that
  both verifiers derive identically from the same empty set, agree on perfectly,
  and promote to CONFIRMED. A fabricated rank would ship carrying two-method
  validation."
- Source: R-D24
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-33 With three or more files, chain pairwise against one anchor and report what was used
- Rule: the period-end file is the anchor. Report which files were used and which
  were not. "Never silently discard a file the user supplied."
- Source: R-D24
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-34 Orient before you test for unit drift
- Rule: compute the ratio per matched unit, orient it so the median is at or
  above one, and only then test concentration. "Without orientation the result
  depends on which file was divided by which."
- Mechanism: three co-required conditions before a factor may be declared: at
  least UNIT_DRIFT_MIN_PAIRS positive pairs; the oriented median within
  UNIT_DRIFT_TOLERANCE of a candidate factor; and at least
  UNIT_DRIFT_CONCENTRATION of oriented ratios within UNIT_DRIFT_BAND of that
  factor.
- Source: R-D23
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-35 Concentration near the factor is the test, not tightness
- Rule: do not test dispersion with a tight interquartile band. "Unit-level
  business metrics are naturally dispersed." On real data a genuine conversion
  showed an interquartile range of 18 to 24 percent of the median while being an
  unambiguous factor of ten. "A 5 percent dispersion ceiling is unsatisfiable by
  construction for any unit-level metric and would miss every real unit change."
- Source: R-D23
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-36 Restrict the drift test to columns already typed as measures
- Rule: run it only on pairs both classified as rate or volume. "Running it
  across all numeric columns produces false positives on identity columns: on
  real files an account number against a scope code fires at factor 2."
- Source: R-D23
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-37 A small factor might be a real result; never correct it silently
- Rule: auto-normalize only the factors in UNIT_DRIFT_AUTONORM_FACTORS. For a
  small validated factor, do not normalize automatically: ask. "A genuine
  doubling produces a magnitude near two, and silently correcting it would erase
  the user's best result of the year and never tell them."
- Source: R-D23
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-38 A header token mismatch is evidence, not an automatic block
- Rule: a header mismatch says a conversion is likely; the test says what it is.
  A letter inside a rate marker is often a category hint, not a unit conversion,
  and treating it as one blocks most real pairs and produces no output at all.
- Source: R-D23
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-39 Rate, unit and lookback are three separate properties, and conflating them is fatal
- Rule: separate the RATE DENOMINATOR (the time base the value is expressed per),
  the UNIT (what is being counted) and the LOOKBACK LENGTH (how much history the
  average covers). "Conflating them either blocks every legitimate comparison or
  permits a catastrophic one."
- Mechanism, in order: the rate denominator MUST match, with no override. The
  unit MUST match, or a validated recorded normalization must have been applied.
  The lookback MAY differ, and when the first two hold a differing lookback is a
  RUN-RATE COMPARISON, permitted, recorded, and never used to open a report.
- Why the third is permitted: "Both a year-to-date weekly average and a
  thirteen-week weekly average express the same quantity: units per week. The
  lookback changes how much history is smoothed, not what the number measures.
  Blocking on lookback alone would reject every real pair of files."
- Prevents: "a number that is wrong by an order of magnitude while tracing
  perfectly to real cells."
- Source: R-D22
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-40 On a block, compute nothing for that pair until it resolves
- Rule: mark the pair unpaired, fire the relevant question, and compute nothing
  for it. Do not substitute a nearby column.
- Source: R-D22
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-41 Alias matching is normalized, not literal
- Rule: before matching, casefold the header, collapse underscores and
  punctuation to spaces, and strip parenthetical unit and period tokens. "A
  literal table lookup misses the single most important column in a real file."
- Source: R-D1 sub-doctrine 1a
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-42 An alias that is a common word or carries punctuation needs a sentinel
- Rule: replace such an alias with a sentinel token BEFORE stripping punctuation,
  then match the sentinel. Never register the bare remainder as an alias.
- Mechanism: the documented harm: a bare two-letter remainder falsely attributed
  more than two hundred rows of unrelated flags to one entity.
- Source: R-D1 sub-doctrine 1b
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-43 A sub-entity inherits its parent; an unrecognized alias is flagged, never guessed
- Rule: a sub-entity inherits its parent entity and its parent's benchmark. "If
  an alias is unrecognized, do not guess the parent. Flag it and ask."
- Source: R-D1 sub-doctrine 1c
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-44 Confirm the SCALE of a column by reading its own maximum, every run
- Rule: never assume a column is a fraction or a points value. If the maximum is
  at or below one it is fractional; if above one it is in points.
- Prevents: "Against a fractional column a literal threshold of 25 matches zero
  rows, silently."
- Source: P-D268
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-45 Null handling changes the count and must be STATED
- Rule: pick a rule, either zero-fill our own side or require the other side
  non-null, and say which rule was used.
- Source: P-D269
- Applies: PLANNING, SCORECARD

### SD-PRS-46 Check that two periods match before dividing, and say what you found
- Rule: prefer a denominator whose period token matches the numerator's. If none
  exists, use what is there, state both period tokens in the audit AND in the
  section's own narrative wording, and treat the result as directional rather
  than exact. Never silently divide across two periods, and never invent a
  scaling factor to reconcile them.
- Mechanism: "The count over the longer window includes items the unit held
  earlier in the period and may no longer carry, so it runs high, and the ratio
  therefore runs low", biasing the classification and understating the upside.
- Source: P-D286
- Applies: PLANNING, SCORECARD

### SD-PRS-47 No stem belongs to two concepts, and a tie on a strict concept is never broken by position
- Rule, at build time: no stem appears in the seed set of two concepts. Where two
  concepts would share a stem, the stem is removed from the LESS SPECIFIC concept
  and the removal is recorded, so a binding owner adding a local stem can see the
  precedent. The seed dictionary is held to the same standard as the runtime
  learning mechanism, which already refuses to promote a colliding stem.
- Rule, at run time: where two concepts both produce an exact match on the same
  header, and either is marked strict_exact_only, NEITHER resolves. The header is
  reported as ambiguous, both candidates are named, and every feature both feed is
  skipped and named. A tie on a strict concept is never broken by column position,
  by dictionary order, or by which pass happened to reach it first.
- Prevents: the failure no downstream gate can catch. The named case: a generic
  status stem sits in both the not-actionable exclusion concept and the pipeline
  stage concept. A file with one column of stage values resolves to the exclusion
  concept, the exclusion removes a stage, the funnel reconciles, and every
  invariant passes. The only defence is resolving the right column in the first
  place, and the only way to guarantee that is to refuse to guess.
- Source: report 2 D9; enforces SD-POP-05
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRS-48 A second file that carries the evidence is JOINED on a shared identifier, not left unread
- Rule: where a source in the input set carries columns the run needs and cannot
  resolve in the ranking source, and both files carry the SAME IDENTIFIER, the run
  ENRICHES the ranking source with those columns by joining on that identifier. It is
  a permitted operation, it is not a concatenation, and leaving the file unread is not
  the conservative choice: it is a decision to compute a term as zero when the data to
  compute it truthfully was in the same input set.
- **THE FAILURE THIS RULE ANSWERS.** A file keyed on the unit identifier, one column
  per requirement, sat beside the ranking source. Four gap terms and three exception
  flags needed exactly that evidence. The admission test was written for column
  coverage on ONE container, and the concatenation rule covers two containers of the
  SAME SHAPE, so nothing covered two containers of DIFFERENT shape sharing a key. Every
  one of those seven terms contributed nothing to every row, the funnel reconciled, and
  no gate fired.
- **A JOIN IS NOT A CONCATENATION.** Concatenation adds ROWS from files of the same
  shape, per SD-PRS-12, and de-duplicates. A join adds COLUMNS from a file of a
  different shape and adds no row to the population. The two are never substituted for
  each other, and a run states which it did.
- Mechanism, and every condition must hold before a join is performed:
  1. **BOTH SIDES RESOLVE THE SAME IDENTIFIER CONCEPT**, by the ordinary resolution
     rules, on the strict reading. A key matched by position, by row order, by name
     similarity or by any fuzzy comparison is NOT a join key. A compound key is
     permitted where every part of it resolves on both sides.
  2. **THE KEY IS UNIQUE ON THE ENRICHING SIDE.** Count the distinct key values against
     the row count. Where the enriching file holds more than one row per key, the join
     is refused unless a stated rule collapses the duplicates, and the rule and the
     collapse count are printed. A one-to-many join silently multiplies rows, which is
     the way a join corrupts a ranked population.
  3. **THE KEY IS COMPARED AS TEXT**, trimmed, with the identifier's own formatting
     preserved, per SD-SPN-06. Leading zeros survive. A numeric read of an identifier
     is not a key.
  4. **THE JOIN IS LEFT, FROM THE RANKING SOURCE.** The ranked population is fixed
     before the join and is not changed by it.
- Mechanism, the two non-matching sides, and both are reported rather than one:
  - **A RANKED ROW WITH NO MATCH keeps its place in the population** and the enriched
    columns are UNRESOLVED for that row, written blank per SD-CTR-13, never zero and
    never a default. A term computed over those columns is NOT SCORED for that row and
    says so, because an absent record is not evidence of a negative.
  - **AN ENRICHING ROW WITH NO MATCH is counted and named, never silently discarded.**
    A large unmatched remainder on the enriching side is evidence that the two files
    key differently, or cover different scopes, and it is the only warning a run gets
    before it trusts a bad key.
- **Rule: A JOIN NEVER DROPS A ROW FROM THE RANKED POPULATION, AND NEVER ADDS ONE.**
  The row count before the join equals the row count after it. Assert it; a change in
  either direction is a defect and blocks, rather than a result to be explained.
- **Rule: A JOIN THAT LANDS AND CANNOT BE SCORED HAS NOT ANSWERED THE FAILURE ABOVE.**
  The joined columns must then RESOLVE to the concepts the terms need, by the ordinary
  resolution routes. Where the enriching file carries ONE COLUMN PER MEMBER of a
  published requirement set, which is the commonest shape a real evidence file has,
  those columns TIE WITH EACH OTHER for the same concept by construction, and a
  uniqueness test written to refuse an ambiguous PAIR refuses the whole SET: measured, a
  second time, eight boolean columns each clearing the value check and the fill floor,
  none adopted, and the same four gap terms and three exception flags unevaluated on all
  190 rows with the file joined and sitting beside the book. The resolution rules carry
  a SIBLING SET route for exactly this shape. **The join is half the fix and that route
  is the other half**, and a run that stops at the join has moved the failure rather
  than closed it.
- Rule: the enrichment is DISCLOSED wherever the enriched terms are used: the file
  joined, the key used, the columns added, the MATCH RATE as matched of ranked, the
  unmatched count on each side, **and whether each joined column RESOLVED to a concept
  or was carried unread**, because a joined column nothing reads is indistinguishable in
  the artifact from a file that was never opened. A term whose evidence arrived by join
  is readable as such, so a reader who distrusts the key can see exactly how much of the
  answer depends on it.
- Rule: where any condition above fails, the run does NOT join. It records the file as
  READ AND NOT JOINED, names the condition that failed, and names the terms that go
  unevaluated as a consequence, so the cost is visible rather than invisible.
- Prevents: seven scored terms contributing nothing on every row while the evidence sat
  in the same input set; and the opposite failure, a run silently multiplying or
  deleting rows of a ranked population by joining on a key that was never unique.
- Source: the demonstration run, planning D20
- Applies: PLANNING, REVIEW, SCORECARD

---
