# GROUP FMT: FORMATTING AS A CORRECTNESS PROPERTY

### SD-FMT-01 Formatting is verified, not asserted, and is never traded for speed
- Rule: every element in FORMATTING_ELEMENTS is verified programmatically per
  section, and a section failing any one is a defect that blocks publication.
- Mechanism: elements that do not apply to a section score not applicable, and an
  N/A cell is a pass, not a failure.
- Prevents: shipping an artifact that is correct in every number and looks
  unfinished.
- Quote: "Formatting is not cosmetic and is never traded for speed."
- Source: P-D22
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-02 Checking a subset and calling it verified is the defect
- Rule: test every element per section and record a full pass matrix.
- **Rule: A CHECK IS SCOPED TO THE WHOLE OF THE RULE IT ENFORCES, AND A CHECK SCOPED
  MORE NARROWLY THAN ITS RULE IS WORSE THAN NO CHECK, BECAUSE IT CERTIFIES THE DEFECT.**
  With no check, a defect is merely unnoticed and the next reader may still find it.
  With a too-narrow check, the defect ships with a recorded PASS standing behind it, and
  the pass is the thing everyone downstream relies on instead of looking.
- Mechanism: "A build whose action sections were fully styled and whose reference
  section was bare passed a four-property check cleanly, because none of the four
  properties it tested was a visual one."
- **Mechanism: where a rule names a SHEET and its check walks a TABLE, the check is
  stale and is widened rather than explained.** Measured: the full-gridline element
  requires a border on all four sides of every populated cell, its verification walked
  the table range, and three delivered workbooks passed it while shipping a populated,
  merged, completely unbordered note band directly beneath a fully bordered table. The
  element and its verification disagreed about what "every populated cell" meant, and
  the narrower of the two was the one that ran.
- Prevents: a gate that cannot fail on the thing it exists to catch, and the worse case
  of a gate that passes the artifact the reader is about to complain about.
- Source: P-D23; extended by the delivered-workbook readability report
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-03 The freeze point is computed, not fixed, and no free-text column is inside it
- Rule: compute the freeze cell as the first column after
  IDENTITY_BLOCK_ANCHOR_COLUMN, on the first data row. Do not hard-code it.
  Verify by reading the header row and finding the anchor by name.
- **Rule: THE REASON-FOR-RANK COLUMN HAS ONE POSITION, and it is the first column
  after the identity columns.** It closes the identity block and every measure, count,
  status, date and narrative column follows it. A skill whose own column order puts it
  at the far right of the sheet, beside the narrative column, is stale: the reason a
  unit sits where it does is read WITH the unit's identity, and twenty columns to the
  right it answers a question the reader stopped asking.
- **Rule: the anchor is the last FROZEN identity column, so the freeze lands ON the
  reason column and the reason column is OUTSIDE the frozen span.** The identity
  block's last column and the identity block's last FROZEN column are two different
  columns. Reading them as one column is what made the anchor rule, the freeze rule
  and the no-free-text-in-the-frozen-span rule irreconcilable, so that no assignment of
  the anchor satisfied all three and every correctly built sheet failed one of them.
- **Rule: THE FROZEN SPAN IS BOUNDED, in the same width unit the columns are set in,
  and the bound is checked against the SUMMED BUILT WIDTHS of the frozen columns.**
  Walk the identity columns left to right; the span ends at the last one that keeps the
  sum inside the bound; the first column is always frozen even if it alone exceeds it.
  Columns left outside keep their positions unfrozen, nothing is moved, dropped or
  narrowed to make the block fit, and the truncation is recorded where the reader can
  see it. The identity block is ordered MOST-IDENTIFYING FIRST so a truncated span
  keeps the columns that say which unit the row is.
- **Rule: THE WALK RUNS ONCE FOR THE ARTIFACT, FROM THE WIDEST CASE, NEVER ONCE PER
  SHEET.** Take each identity column's MAXIMUM built width across every grid in the
  artifact that carries the block, walk those, and apply the resulting anchor by NAME
  everywhere. A built width depends on the longest data value on that sheet, so a
  per-sheet walk stops in a different place on every sheet: one workbook froze three
  identity columns on its three merit sheets and five on its three empty ones, because
  an empty sheet's name column falls back to its own header floor and leaves room for
  two more. Every sheet was individually conformant and the workbook was not. **A
  sheet whose own block is genuinely narrower freezes the SAME COLUMNS in fewer width
  units, which costs nothing; what it must never do is freeze MORE.** The truncation
  record is then ONE line for the artifact rather than one per sheet, because six
  records of one identity block are worse than none.
- Rule: the frozen span bound says what stays on screen and says nothing about how
  wide the sheet is. **The TOTAL width of the grid is bounded separately, by
  SD-FMT-28**, and neither bound substitutes for the other.
- **THE FAILURE THE BOUND ANSWERS, MEASURED:** a census workbook built entirely to the
  contract came out 21 columns and 659 character-widths across, and freezing its whole
  identity block pinned 17 of 21 columns and every one of those 659 widths, so
  scrolling right reached nothing. A frozen span wide enough to fill the window does
  not keep the identity on screen; it keeps everything on screen, which is the same as
  freezing nothing while also costing the reader the scroll. **A freeze that costs the
  reader more than it saves is worse than no freeze**, and the arithmetic of the
  contract's own element cannot see that, so the bound is stated separately.
- Prevents: the span-of-control block changing the column position by role and
  silently breaking the freeze; a free-text paragraph pinned to the left edge on
  every horizontal scroll, eating the window the frozen span exists to preserve; and an
  unbounded frozen span that pins the whole readable width of a wide sheet. The
  frozen span keeps the unit's IDENTITY on screen, and a paragraph is not an identity.
- Source: P-D24; extended by the demonstration run, planning D5 and scorecard D1 and D9
- Applies: PLANNING, SCORECARD

### SD-FMT-04 Direct cell formatting outranks a style, so the header band must be explicit, and the style must not oppose it
- Rule: apply the header band explicitly on every header cell rather than leaving
  it to the table style, because direct cell formatting outranks the style.
- **Rule: THE STYLE'S OWN HEADER BAND MUST AGREE IN DIRECTION WITH THE DIRECT ONE:
  light band, dark text, in both.** Outranking a style is not the same as being alone
  on the sheet. The style is still in the file, still applied, and still what a renderer
  that honours the style and drops the direct formatting will show. A renderer honouring
  the STYLE and a renderer honouring the DIRECT FORMATTING must both produce a readable
  header, and they cannot while the two pull in the same wrong direction.
- General form: a lower-precedence style is not a guarantee, **and it is not free
  either**. What a lower-precedence layer says still matters, because precedence is
  decided by the renderer and not by the author.
- Mechanism: bind the table style to a family whose own header band is light under dark
  text, and reject a style whose header band opposes the direct band at validation
  rather than at read time. Row stripes stay on; they are not what is being traded.
- **THE FAILURE THIS ANSWERS, MEASURED:** three delivered workbooks carried a
  medium-weight table style whose own header band is a solid dark fill under white text,
  beneath a direct dark fill under white text. The two agreed on darkness, so when the
  direct fill failed to render there was nothing readable underneath it, and the
  workbook's belt and its braces failed together.
- Prevents: a header that is readable only in the one renderer where the higher-
  precedence layer arrives, with the lower-precedence layer offering the same defect
  again rather than a fallback.
- Source: P-D25; extended by the delivered-workbook readability report
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-05 The right-align list is CLOSED at run time, and its MEMBERSHIP is decided by a rule
- Rule: right-align exactly the columns in RIGHT_ALIGN_COLUMNS, centre exactly the
  columns that qualify as a STATUS GRID COLUMN, and left align every other column. Do
  not infer additional count columns AT RUN TIME, and do not centre a column on a
  judgment made during a run.
- **CLOSED IS ABOUT WHEN, NOT ABOUT HOW THE LIST IS BUILT.** It forbids a RUN from
  adding a column on its own judgment. It does NOT mean the list is assembled from
  memory at authoring time, and reading it that way is what left numeric columns
  ranged left beside numeric columns ranged right in one table, which reads to the
  person holding it as a broken export.
- **THE MEMBERSHIP RULE, WHICH IS TOTAL OVER THE SHAPE TOKENS AND THEREFORE LEAVES
  NOTHING TO JUDGMENT:** right align a column whose shape token is
  COUNT_OR_MEASURE, RATE_OR_PROPORTION or DATE; left align one whose token is
  IDENTIFIER_OR_CODE, STATUS_OR_CATEGORY, BOOLEAN_LIKE or FREE_TEXT. The seven
  tokens of 3.6 are exhaustive, so every column this contract can emit lands on
  one side by construction, and a numeric column added later joins the list
  because of what it is rather than because somebody remembered.
- **Rule: THERE IS A THIRD CLASS, IT IS CENTRE, AND IT IS ADMITTED ONLY ON A CONDITION
  A CHECK CAN READ.** A column whose token is STATUS_OR_CATEGORY is centred where all
  three hold, and left aligned where any one of them fails: it is DECLARED a status
  grid column; every populated value comes from a CLOSED, PUBLISHED vocabulary; and the
  longest member of that vocabulary is inside the bound character length. A block of
  adjacent columns each holding one short code out of the same small set is read across
  the row and down the column as a PATTERN, and a ragged left edge of unequal codes
  hides the shape of the failures the reader came for. **The gain disappears the moment
  a cell holds a sentence**, which is ragged on both sides, cannot be scanned down a
  column, and is centred nowhere else in the bundle. The bound on the vocabulary is what
  keeps the exception where the gain is.
- **Rule: A SKILL THAT WANTS ITS STATUS GRID CENTRED PUTS THE CODE IN THE GRID AND THE
  SENTENCE IN THE NARRATIVE COLUMN.** That is the remedy, and it is the same remedy
  that keeps a status grid from widening every one of its columns to the data cap. An
  instruction to centre a column of sentences is not implementable by a workbook that
  publishes, because the alignment verification tests every populated cell of the table
  block and fails on all of them.
- Rule: the bound list is the MATERIALISED result of that rule. VALIDATE it
  whenever any column is added to the contract: no column with a numeric or date
  token is missing from the list, and no column with a text, identifier, category
  or boolean token is in it. A list that fails that check is wrong even if every
  entry in it is individually defensible.
- Rule: an identifier is written as TEXT so leading zeros survive, per SD-SPN-06,
  and it is LEFT aligned. That is not an exception to the rule; it is the rule,
  because its token is IDENTIFIER_OR_CODE.
- General form: where a closed list has a describable membership, state the rule
  AND materialise the list, and check one against the other. Closing the list
  without stating the rule is how a list goes stale; stating the rule without
  closing the list is how a run starts improvising.
- Source: P-D26; extended by final ship run, MEDIUM 2
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-21 A column the contract makes MANDATORY is never eligible for constant-column removal
- Rule: a rule that drops a column carrying one repeated value NEVER applies to a
  column the output contract declares mandatory. The mandatory set is decided by
  the contract; the constant test is an optimisation over the columns that remain.
  An optimisation may never delete a guarantee.
- The named case: every cell of a required action column held the same string on a
  run where no priority source could be read, so the degenerate-constant test fired
  on a column that three separate parts of the contract declare mandatory. A rule
  written to drop dead columns could delete a required one, and the collision was
  invisible because each rule was correct read alone.
- **A MANDATORY COLUMN CARRYING ONE REPEATED VALUE IS A FINDING ABOUT THE DATA,
  NOT A DEFECT IN THE COLUMN.** It is the correct and useful outcome, and it is
  reported as one: the column ships, at full width, with its header, and ONE LINE
  in the Method section states that every row carries the same value and why. A
  reader learning that every unit got the same instruction has learned something
  real about their run. Deleting the column hides it.
- Mechanism, and it is an ORDERING not a new test: resolve the mandatory set from
  the contract FIRST, then apply the constant test only to columns outside it. Any
  rule that removes a column states, in its own text, that the mandatory set is
  exempt, so the exemption cannot be lost by reading one rule alone.
- Rule: this generalises to every removal rule, present and future, not only the
  constant test. A column may be removed for being empty, constant, unresolved or
  unreached, and none of those reaches a mandatory column. Where a mandatory
  column's source does not resolve at all, SD-CTR-13 already governs: it ships with
  its header present and its cells blank and the failure named.
- Prevents: an optimisation silently deleting a contract guarantee, which is a
  shape change that every gate reading by header name would then fail.
- Source: final ship run, MEDIUM 3
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-22 The output contract is ONE file, and a rule stated in prose is not enforced
- Rule: the output contract lives in reference/output-contract.md and nowhere else. Every skill
  CITES an element by number and none restates its standard. A skill that appears to
  disagree with that file is stale and the file governs.
- **THE FAILURE THIS RULE ANSWERS: the formatting elements existed as prose in an
  earlier bundle, survived into it only as passing mentions, and were therefore never
  enforced.** A scorecard shipped with no autofilter on any sheet, no rank column on
  its main sheet, no consolidated reason column and no cap. A planning workbook put a
  title banner in row 1 and pushed its headers to rows 4 through 6. Every one of those
  violated a rule the bundle already contained. **Prose is not a contract. A contract
  is a named element, a stated standard, and a verification that runs before
  publication and blocks it on failure.**
- Rule: an element without a programmatic verification is not an element. Where a
  standard cannot be checked by reading the built artifact, either find a way to check
  it or do not claim it.
- Rule: the OUTPUT MEDIUM is keyed per skill, never shared. A ranked worklist and a
  review are different documents and a single container assumption is what let one
  skill's section list and artifact name become the default for another.
- Rule: a skill may add a sheet, and the new sheet inherits every element
  automatically. It may not add an element, restate a standard, state a count of the
  elements, or emit an entity sheet exempt from them.
- **Rule: an element BINDS A SHEET CLASS, not a workbook.** A verification row that
  says "on every sheet" fails a correct workbook on the first panel it meets, because
  a panel has no header row and its cell A1 is a title by the panel element itself.
  Every element and every verification row names the class it applies to, and every
  sheet is declared into a class.
- **Rule: a closed list of NOT-APPLICABLE reasons must be able to express every
  exemption the elements themselves state.** Where an element's own text names the
  condition under which it does not apply, that condition IS a qualifying reason. A
  list that cannot express it turns a correct workbook into a blocked one, and the
  list is the defect. The named case: the alert element states that it does not apply
  to a sheet with no elapsed-time column, and a closed list offering only "no rows",
  "the container cannot express it" and "a different sheet family" had no member for
  it, so every workbook without an elapsed-time column failed at the final gate on a
  wording gap.
- Prevents: a contract that reads as complete and enforces nothing.
- Source: originals review, C4 and C6
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-23 A header must never be hidden, clipped or half-shown
- Rule: three separate failures share one cause, a width or a height chosen from
  something other than the thing being displayed, and each gets its own element.
  1. **A COLUMN IS NEVER NARROWER THAN ITS OWN HEADER NEEDS, PLUS THE FILTER CARET.**
     The header's requirement is computed in CHARACTERS as a FLOOR that the data may
     raise and may never lower, and it is converted into a width ONCE, in the widening
     direction only, per SD-FMT-08. Computing width from the data alone gives a narrow
     column under a long header, and an autofilter caret then sits on top of the last
     word of the one row that must never be ambiguous.
     **THE HEADER'S CHARACTER REQUIREMENT IS THE NARROWEST LINE THE HEADER CAN LIVE ON
     INSIDE ITS LINE BUDGET, and it is found by asking the wrap.** "Wrap it to the
     budget and take the longest line" is not a computation: text wraps to a WIDTH and
     the line count is what comes out, so a rule that names no width to wrap at can only
     be read as wrapping against the width it is about to produce, which is a circle.
     The requirement is floored at the header's longest single word, without which a
     one-word header appears to fit on one line at every width down to one character.
     **The width a column is given and the characters read back out of that width must
     be the same quantity, or the width element and the header-height element are
     asserting different things about one number and a correct workbook fails one of
     them.**
  2. **EVERY ROW HEIGHT IS COMPUTED FROM ITS OWN WRAPPED CONTENT** against its own
     column widths. Never a fixed number, never autofit, because autofit does not
     account for wrap on styled cells and clips silently on some engines.
  3. **THE HEADER ROW HEIGHT IS COMPUTED FROM THE HEADER NEEDING THE MOST LINES**, so
     a two-line header shows both lines. One header showing one of its two lines is
     the defect, and it is invisible to anyone who does not already know the full
     header text.
- Rule: wrap is ON for every cell, so height is always a computed consequence rather
  than a guess.
- Rule: a header needing more than the bound line budget is REPORTED so it can be
  shortened, rather than silently clipped or silently making every row taller.
- Prevents: a delivered workbook whose column headings cannot be read, which is the
  first thing a reader notices and the thing that makes them doubt everything under
  it.
- Source: originals review, reported header failure
- Applies: PLANNING, SCORECARD

### SD-FMT-24 Every entity sheet carries a rank and a reason for that rank
- Rule: every sheet with one row per unit carries a POSITION column in first position,
  in the identity block, and a REASON-FOR-RANK column saying in plain language why
  that unit sits where it does. **No entity sheet ships without both, in any skill.**
  A grid whose rows are not units of business carries them too: a reader of a summary
  or a legend asks the same question in the same order.
- Rule: the reason column is NOT the narrative column and does not replace it. The
  narrative says what to DO about the unit; the reason says why the unit is HERE. A
  sheet may carry both, under different headers.
- **THE ARGUMENT, AND IT IS PRACTICAL RATHER THAN AESTHETIC:** a ranked list whose
  ordering cannot be explained row by row is a list the reader re-sorts by hand, and a
  list that gets re-sorted by hand has already lost. A census with no rank column
  leaves a reader with data and no answer to the only question they came with, which
  is what to do first.
- Rule: where a sheet's order is not a merit order, the first column is still a
  position column, is HEADED FOR WHAT IT IS, and still carries a reason. A sheet
  ordered by something other than merit and headed as a rank is a contract violation.
- **Rule: A BAND LABEL IS NOT A POSITION HEADER, and the variable that names one is
  never used for the other.** The header of a priority BAND column carries values of
  the High, Medium, Low kind. Put over a column of 1, 2, 3 it tells every reader who
  has met a band anywhere else in the bundle that they are looking at bands. Each
  concept gets its own variable and the two never substitute.
- **Rule: neither header is written as a LITERAL.** A header string written into a
  skill is a second source of truth that nothing updates, and an organization that
  rebinds the header then finds the artifact unchanged.
- Prevents: a census nobody can act on, an ordering nobody can check, and a column of
  positions read as a column of bands.
- Source: originals review, the rank and reason decision
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-25 A derived last rank is not a row cap, and each capped sheet is capped independently
- Rule: ranks form ONE UNBROKEN SEQUENCE across the merit tiers: the first tier starts
  at 1, the second resumes at the next rank, the reference tier resumes after that. No
  gaps, no duplicates, no restart at 1.
- **Rule: the DERIVED LAST MERIT RANK is `last_visit_rank + REFERENCE_CAP`, it is a
  DERIVED RANK, and it is NEVER carried as a literal.** A resize of either tier
  recomputes it. A check asserting a stale figure against a resized run tests the
  wrong number and fails a correct artifact.
- **Rule: NEVER read a derived last rank as a ROW CAP.** Doing so ships the cap plus
  the tier sizes in rows, overrunning the cap that every showing-note reconciliation
  checks against, and failing a correct-looking artifact at the final gate.
- **Rule: every capped sheet is capped INDEPENDENTLY, not against a shared budget.**
  Later sheets hold wildly different populations, routinely differing by an order of
  magnitude off one scope, and a shared budget silently starves whichever sheet was
  built last.
- Rule: the reference tier's authoritative size is the ROW-COUNT form,
  `min( REFERENCE_CAP , eligible_count - last_visit_rank )`, and a zero-row result is
  a complete and correct sheet carrying its header and one explanatory row. Never emit
  a negative count and never treat it as a failure.
- Rule: a directed sheet is not a merit tier: its units rank among themselves and
  never consume a merit rank.
- **Rule: A MERIT TIER SET IS NOT THE ONLY SHAPE A RANKED SHEET COMES IN, and the
  tier arithmetic above describes only one of them.** A CENSUS is one sheet holding
  every unit in scope, ranked worst first; it starts at rank 1 and there is no tier
  before it to resume from. An EXTRACT carries the top of a census and repeats the
  census's own rank numbers rather than re-ranking from 1, so a unit found on both
  sheets carries one number. A skill declares which kind each ranked sheet is.
- **Rule: the no-duplicate-identifier assertion is scoped to MERIT TIERS.** Two merit
  tiers sharing a unit is still a defect and still blocks publication, because the
  tiers partition one population and a unit in two partitions has two ranks. A census
  and an extract of that census share every identifier on the extract BY
  CONSTRUCTION, and asserting the merit-tier rule across them fails a correct
  workbook for doing exactly what an extract is for.
- **Rule: a quantity defined on one shape is not evaluated against another.** The
  tier sizes and the derived last merit rank exist only on a merit tier set; a check
  reading them against a census is testing a number that workbook never produced,
  which is SD-RNK-03 arriving through a different door.
- Prevents: two readers producing different row counts off one configuration, a
  correct artifact failing its own reconciliation, and a verification with no defined
  answer for a sheet the contract permits.
- Source: originals review, C5; extended by the demonstration run, scorecard D3
- Applies: PLANNING, SCORECARD

### SD-FMT-26 A note that belongs to a grid has ONE place, and the elements that forbid it elsewhere say so themselves
- Rule: a note about a grid, the showing note above all, has exactly ONE permitted
  location: a NOTE BAND below the grid, separated from it by one blank row, merged
  across the grid's full column span, left aligned, in the panel label styling, with
  its height computed against the summed width of the merged span.
- **THE FAILURE THIS RULE ANSWERS: three elements between them forbade every place a
  note could go, while a fourth rule made the note mandatory and verified.** Above the
  header row is forbidden, because the header row is row 1 and everything downstream
  of it breaks when it moves. Inside the table is forbidden, because a row that is not
  a unit sorts, filters and counts as though it were one. A sentence in the first
  column collides with the alignment element, which right-aligns the position column
  and left-aligns everything else, and that collision was measured on a real build as
  exactly one violation on exactly one cell. A note in the trailing narrative column
  breaks nothing at all and is invisible, twenty columns right of where the reader is
  looking.
- Mechanism: the elements that could be read to forbid the note band say so in their
  own text. The header-row element governs what sits ABOVE the header row and nothing
  else. The table element forbids a populated DATA row outside the table range, which
  is what it was always for: a unit row outside the table is a row that does not sort,
  does not filter and is not seen. The alignment element governs the table block. None
  of the three has to be weakened, and a reader of any one of them learns the note
  band is permitted without going to look.
- Rule: the note band does not replace the front panel or the method section. The
  title, the scope, the period and the caveats stay on the front panel; the showing
  note is still repeated in the method section and still reconciled against the sheet.
  What the note band carries is the note that must sit BESIDE THE GRID IT IS ABOUT.
- **Rule: THE EXPLANATORY ROW OF AN EMPTY SECTION IS NOT A NOTE AND DOES NOT GO HERE.**
  It is that section's content, it sits inside the table range as SD-FMT-07 states, and
  the note band of the same sheet still carries that sheet's showing note. One sheet
  can hold both, and neither is a substitute for the other.
- **Rule: A STATEMENT REQUIRED IN TWO PLACES IS RECONCILED, NEVER MERELY REPEATED.**
  The showing note is required on the sheet and in the method section BECAUSE a gate
  reads both and asserts they agree; the duplication is load bearing. Where an
  instruction requires the same sentence in two places and nothing reconciles them, one
  location is named PRIMARY and the other cross-references it. Two unreconciled copies
  of one figure make the reader ask which is current, and eventually only one of them
  will be.
- Prevents: a mandatory, verified note with no legal location, which forces every
  implementer to invent one and guarantees that two of them invent differently.
- Source: the demonstration run, scorecard D6 and planning D8; extended by planning N9
  and N12
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-27 A verification never scans its own record, and one colour never carries two meanings
- Rule: a verification that SEARCHES FOR STRINGS excludes its own record from its own
  scan, and says in that record that it did so. Its record has to name what it searched
  for, or it is not auditable; if the record then lives inside the artifact the scan
  covers, the row finds its own evidence and fails itself.
- **THE FAILURE THIS RULE ANSWERS, MEASURED:** the row that scans a workbook for a
  hard-coded unit noun requires its own matrix entry to state the nouns it searched for.
  Writing them in took the raw occurrence count from 22 to 44 and turned a passing gate
  into a failing one. **A run that recorded its evidence failed and a run that hid its
  evidence passed**, which is the exact inversion an audit trail exists to prevent, and
  the only remedy available to the run was to move its evidence out of the artifact.
- Mechanism: the verification matrix occupies a DECLARED CELL RANGE, the artifact states
  that range, and every string-searching row skips it. The exclusion costs nothing,
  because the range is written by the verification pass and read by no consumer of the
  data. It is the ONLY permitted exclusion: no row may exclude a range in order to pass.
- Rule: the exclusion is for STRING SEARCHES ONLY. A character-set gate still reads every
  cell including that range, because a forbidden character is a defect wherever it sits
  and cannot be planted by a record of itself. A row reading a structural attribute is
  unaffected.
- **Rule, the same shape one step over: A COLOUR IS A VARIABLE WITH ONE BINDING.** Where
  a grid carries a classification fill per value of a declared vocabulary, that palette
  is DISJOINT from the alert-band palette, so no colour means an approaching deadline in
  one column and an unassessable cell in the next. The collision is invisible on the run
  where it is authored, because a workbook with no elapsed-time column scores the alert
  element not applicable everywhere and nothing overlaps; the same skill run at an
  organization that does track elapsed time paints both meanings on one grid.
- Rule: a cell carries at most one fill, and where a classification fill and an alert
  band would both apply, the alert governs and the precedence is stated in the legend.
- **Rule: THE FILL IS NEVER CONDITIONAL ON THE CENTRING TEST, because centring and
  shading answer different questions.** Centring asks whether a short token reads
  better centred, and a character bound is the right test for it. Shading asks whether
  a reader can find the failures WITHOUT READING, and a long cell value does not harm
  that; it is the cell the eye can least triage on its own. Hanging the fill on the
  centring bound made the fill unreachable: a scorecard whose shortest possible gap
  cell is 15 characters, against a centring bound of 12, could never qualify, so 1520
  status cells shipped with no colour at all, correctly under the rule and contrary to
  everything the same contract said the workbook looked like. **A cell can be too long
  to centre and still be exactly the kind of cell that needs a fill.** The two carry
  separate conditions and are verified by separate rows.
- Rule: what a fill is keyed on is a CLOSED DECLARED SET OF STATES, and the set of
  states is not the set of distinct cell values. Where a cell value is a state plus a
  reason code or a qualifier, the vocabulary is the STATE SET, every populated cell
  resolves to exactly one state by a declared total mechanical rule published beside
  it, and shading prose by keyword is still not a classification fill.
- General form: any record a check writes into the thing it checks is part of what it
  checks, and any palette read by two rules is a variable bound twice.
- Prevents: an audit trail that can only be completed by emptying it; and two meanings
  sharing one colour on one grid, which a reader has no way to disambiguate.
- Source: the demonstration run, scorecard D5 and D15
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-28 A grid's TOTAL width is bounded too, and what gives is a repeated qualifier, never a column, a header floor or a meaning
- Rule: bound the SUMMED BUILT WIDTH of every column on a grid, in the same width unit
  the columns are set in and the frozen span is bounded in. **The bound is declared
  BEFORE the columns are built and is never raised to clear a grid that failed it**,
  exactly as the header line budget is never raised to clear a failing header gate. A
  bound discovered after the measurement is not a bound.
- **Rule: THREE THINGS NEVER GIVE.** No column is dropped, mandatory or not, because a
  dropped column is a fact the reader cannot recover and cannot know to look for. No
  column goes below its own header floor, because a narrowed header is the failure the
  width rules exist for. No value that carries meaning is shortened, truncated,
  abbreviated or reworded: a name, a date, an identifier, a finding and a per-row
  reason are untouchable. This is a readability bound and it never buys width with
  correctness.
- **Rule: WHAT GIVES IS A STANDING QUALIFIER.** A standing qualifier is a phrase inside
  a cell that qualifies the cell's own answer rather than stating it, is drawn from a
  CLOSED DECLARED set, and is written in the SAME WORDS every time that member appears.
  It costs its full length on every row while carrying one piece of information, WHICH
  MEMBER IT IS, so it is representable by a code. **A phrase unique to its own row is
  not one and is never touched.**
- Mechanism: the relief ladder, run in order before publication. 1. Move every standing
  qualifier out of the cell into the LEGEND, leaving the cell its own answer plus a
  short declared code, and publishing that code against the qualifier's full wording in
  the words it had in the cell; the legend entry is MANDATORY, because a code with no
  legend row is an abbreviation the reader must decode and costs more than the width it
  saved. 2. Move remaining per-row prose that is not the cell's own answer into the
  TRAILING NARRATIVE COLUMN, which is last, widest and never truncated: a sentence
  belongs in one wide column read once, not across eight columns read eight times.
  3. Recompute every width from the width rule, from the top, never by hand and never
  by a conversion the width rule does not name. 4. Where the grid is still over, it
  SHIPS OVER AND SAYS SO: the bound, the measured total, the overage and the columns
  that account for it in descending width order, with one line telling the reader the
  sheet is wider than the bound and that the freeze and the filter are how it is meant
  to be read.
- **THE FAILURE THIS ANSWERS, MEASURED:** the frozen span bound was in force and
  correctly honoured, three columns stayed pinned, and the census sheet was still 21
  columns and 749.12 width units across, worse than the 659 the same contract already
  called a measured failure, because a newly mandated cell qualifier 50 characters long
  repeated on every row of fourteen columns. The reader read the sheet THROUGH THE
  FILTER, one column at a time, rather than by moving across it.
- **WHERE A QUALIFIER BELONGS, DECIDED ONCE SO NO RUN DECIDES IT ALONE:** the LEGEND,
  where it comes from a closed set and the cell can carry its code; the TRAILING
  NARRATIVE COLUMN, where it is per-row prose that is not the cell's own answer; the
  CELL, only where it IS the cell's own answer. Those three are exhaustive over what a
  cell can hold, so the step is a lookup rather than a judgment.
- Prevents: a grid nobody can traverse, whose relationships between columns are
  invisible because it is read one column at a time through a dropdown; and the three
  wrong ways out of it, a dropped column, a hidden header and a truncated meaning, each
  of which pays for width with correctness.
- Source: the demonstration run, scorecard 14-D9, reported partially fixed and measured
  worse; companion to SD-FMT-03, which bounds the span rather than the sheet
- Applies: PLANNING, SCORECARD

### SD-FMT-29 Formatting must degrade safely, because the author verifies in one renderer and the reader opens another
- Rule: **EVERY PIECE OF FORMATTING THAT CARRIES MEANING IS CHOSEN SO THAT IT STAYS
  READABLE WHEN ANY ONE HALF OF IT FAILS TO ARRIVE**, and not so that it looks its best
  when everything arrives. The author verifies in the engine that built the file. The
  reader opens something else: a preview pane, a viewer, a converter, a browser, a
  printer. A property that is correct in the first and absent in the second is not a
  cosmetic difference; it is the whole artifact, seen by the only person it was made for.
- **Rule: A TEXT-AND-BAND PAIR IS ASSERTED THREE TIMES, NOT ONCE.** Assert the intended
  pair; assert the text against the container's default ground, which is what a renderer
  shows when THE FILL fails; and assert the container's default ink against the band,
  which is what a renderer shows when THE FONT COLOUR fails. Asserting only the intended
  pair is the blind spot, and it is a blind spot that passes every dark band under light
  text: such a pair scores handsomely on the intended reading and scores zero the moment
  the fill drops out, leaving light text on a light sheet. **Dark ink on a light band is
  the only pairing that can clear all three**, which is why a header band's direction is
  a rule and not a preference.
- **Rule: A COLOUR IS WRITTEN WITH AN EXPLICIT OPAQUE ALPHA, AND A TRANSPARENT ALPHA IS A
  PUBLICATION-BLOCKING FAILURE.** Where the container's colour field carries an alpha
  byte, the run writes it, and it is opaque. Never a default, never inherited, never
  padded on.
- Mechanism: the arithmetic, the floors and the three assertions live in one place in the
  output contract, in the greyscale unit the palette separation rule already uses; the
  colour variables carry the alpha form in their own validation in the binding schema;
  and both are verified against the BUILT artifact under SD-FMT-06, because a value that
  was right in the variable and wrong in the cell is the case that ships.
- **THE FAILURE THIS ANSWERS, MEASURED, AND IT IS THE PUREST CASE OF THE PRINCIPLE.**
  Three delivered workbooks wrote every header fill as `001F3864` and every header font
  colour as `00FFFFFF`. The leading byte of each is the ALPHA byte and its value is `00`.
  The common spreadsheet engine treats `00RRGGBB` as fully OPAQUE, so the workbooks were
  correct to the run that built them, correct to the verification that read them back,
  and correct to anyone opening them in that one engine. Many other renderers honour `00`
  as FULLY TRANSPARENT, so the dark fill dropped out and bold WHITE header text landed on
  a white sheet, where the reader could not see a single column name. **The run verified a
  readable artifact and delivered an unreadable one, and nothing in the pipeline was
  capable of noticing**, because every check it ran was run in the renderer that made the
  file. Three failures compounded it and each is the same shape: the header pairing had no
  tolerance for one half failing, the table style pulled in the same dark direction so
  there was no readable fallback underneath, and the gridline was too faint against white
  to give the grid any structure of its own once the band was gone.
- **THE GENERAL FORM, WHICH IS THE PART THAT OUTLIVES THIS PALETTE:** where two layers
  can produce a property, they must AGREE IN DIRECTION rather than merely both be
  present; where a property has two halves, EITHER half must be sufficient; and a
  verification that runs only in the authoring renderer must assert the DEGRADED
  renderings explicitly, because it can never observe them.
- **Rule: THE MECHANISM IS CHOSEN FOR THE READER'S ENGINE, NEVER FOR THE ONE THE FILE
  WAS BUILT IN.** Where a property can be expressed two ways and only one of them is
  read by the renderers the artifact is actually opened in, the widely read one wins,
  even where the other is the more correct expression in the authoring tool. **AND THE
  CHECK READS THE PROPERTY BACK FROM WHERE THE READER MEETS IT**, not from the
  container that happens to describe it; a property found only in a container the
  reader's engine does not open is ABSENT.
- **THE SECOND FAILURE, MEASURED, AND IT IS THE SAME SHAPE AS THE FIRST.** The filter
  was required to be the TABLE OBJECT'S OWN, with a sheet-level filter forbidden, which
  is the more correct expression in the engine that built the files and is unread by
  much of what opens them. Every workbook shipped with NO VISIBLE FILTER CONTROL ON ANY
  SHEET, on the one feature the element itself calls the most-used in a delivered
  workbook, and the verification certified them because it read the filter back out of
  the table container instead of off the sheet. The artifact and its record agreed with
  each other and disagreed with the reader, which is this rule's whole subject.
- Prevents: an artifact that passes every gate, satisfies every element, and is unreadable
  to the person who opens it, with the run's own verification record standing behind it.
- Source: the delivered-workbook readability report, three workbooks, every header cell;
  extended by the delivered-workbook reading report, the filter absent on every sheet
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-30 A word is never broken by a cell line, and there are exactly two ways it happens
- Rule: **NO WORD IN A DELIVERED ARTIFACT IS EVER CUT BY A CELL BOUNDARY.** A reader
  meeting half a word with a border through it stops reading the sheet and starts
  doubting the file, exactly as an unreadable header does.
- **Rule, cause one: TEXT NEVER OVERFLOWS A CELL BOUNDARY. Any string needing more
  width than its own cell is placed in a MERGED REGION spanning exactly the width it
  needs.** That binds a panel title row, a section header band, a per-sheet note band,
  the explanatory row of an empty section and any banner. A merged region carries its
  border on the outside of the region, so once merged there is no interior line left
  inside the band for a word to be cut by.
- **Rule: A BAND STYLED ACROSS A SPAN AND NOT MERGED ACROSS IT IS THE DEFECT, AND THE
  TWO ARE EASY TO CONFUSE BECAUSE THEY LOOK IDENTICAL UNTIL A BORDER IS DRAWN.**
  Styling a run of cells gives each of them the fill and gives the string no extra
  room: the text still lives in the first cell, still overflows, and the next cell's
  own border is now certain to be drawn through wherever the string happens to be.
  Merging is what supplies the width; styling only supplies the appearance of it.
- **Rule, cause two: A COLUMN IS AT LEAST AS WIDE AS THE LONGEST UNBREAKABLE TOKEN IT
  MUST DISPLAY**, taken over its header and over the data it will carry, so the wrap
  never has to break a word to fit. The wrap breaks on SPACES ONLY, in a body cell
  exactly as in a header cell. The token floor is what makes the wrap's own
  overflow case unreachable rather than merely documented.
- **Rule: A TOKEN LONGER THAN THE COLUMN CAP IS REPORTED, NEVER BROKEN.** The column
  takes the width the token needs and the method sheet names the column, the token,
  its length and the width it forced, exactly as an over-long header is reported.
  Every disguised break is forbidden with the plain one: an inserted line break, an
  inserted hyphen, an ellipsis, a truncation and a smaller font are the same act.
- Mechanism: the placement rule, the width floor, the arithmetic and both assertions
  live in one section of the output contract and are verified against the BUILT
  artifact under SD-FMT-06; a skill cites the section and restates none of it.
- **THE FAILURE THIS ANSWERS, MEASURED:** a delivered workbook carried a title band
  across the top of a sheet whose own text was longer than the cell it was written
  into. The band was STYLED across three cells and MERGED across none, so the string
  overflowed and the neighbouring cell's left border was drawn straight through the
  middle of a word. Nothing in the bundle could see it: the width rules governed a
  grid column and had no opinion about a band, the border rule required exactly the
  border that did the cutting, and a visual pass could not tell a styled span from a
  merged one until the grid went on.
- **THE GENERAL FORM:** where a rule supplies APPEARANCE and a different mechanism
  supplies ROOM, the two must be required together, or every implementation will
  supply the appearance and discover the room is missing only after a later rule
  draws a line through it.
- Prevents: an artifact that satisfies every width, height and border element and
  still shows the reader a word cut in half.
- Source: the delivered-workbook reading report, the title band and the word it cut
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-06 Read formatting back through the engine, and refuse to publish if you cannot
- Rule: verify by opening the built artifact and reading structural attributes
  directly, not by a value-only read. "If the environment cannot expose those
  attributes, the element gate cannot run and the artifact must not be published:
  say so plainly rather than publishing unverified."
- Mechanism: this is a hard gate.
- Source: P-D27
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-07 An empty section is a finished section with nothing in it
- Rule: an empty section carries the full styling of a populated one, including
  the table, the freeze pane, the style, the font, the widths and the full grid on
  its header row and its single explanatory row.
- Mechanism: border the explanatory row across the full width of the block, not
  just the one cell carrying text.
- **Rule: THE EXPLANATORY ROW SITS INSIDE THE TABLE RANGE, AS THE ONLY DATA ROW, AND
  IT IS NOT A UNIT ROW.** It is placed there rather than in the note band because a
  table over a header row with no data rows is degenerate, and an engine that repairs
  or drops it takes the style, the stripes and the filter with it, which is the empty
  section ceasing to look like a finished one. The objection that normally forbids a
  non-unit row inside a table, that it sorts and filters and counts as a unit, cannot
  arise: it is the only row on the sheet.
- **Rule: A COUNT OF ROWS COUNTS THE SHEET'S OWN DATA ROWS, so the explanatory row is
  counted by nothing.** On a grid of units that is a unit row; on a reference table,
  whose rows are not units, it is the sheet's own row, and the two are one rule because
  the bound, the note and the reconciliation must count the same thing. An empty
  section's showing note reads zero of zero while the sheet holds one written row, and
  the reconciliation counts data rows and passes. **A run that clears the
  mismatch by writing "one of one" has told the reader a unit exists that does not**,
  which is the one outcome this rule forbids. A counter tells the two apart without
  judgment: the explanatory row carries no value in the sheet's FIRST IDENTITY COLUMN,
  which every grid has, and is the only data row; both hold together on an empty sheet
  and on nothing else. The test reads the first identity column rather than a unit
  identifier, because a reference table has no unit identifier and the narrower wording
  gave it no test at all.
- **Rule: THE EXPLANATORY ROW CARRIES ITS SENTENCE, AND A ROW THAT DOES NOT IS A
  FAILURE RATHER THAN AN EMPTY SECTION.** The cell it begins in holds a NON-EMPTY string
  saying, in plain words, why the section qualified nothing. A row that exists, is
  bordered, is sized to a computed height and holds no string at all fails more loudly
  than a missing row would: a missing row is visibly missing, and a blank one looks
  finished. **The sentence begins in the table's SECOND column, the first column after
  the position column, and the position column stays empty because the counter's test
  reads that emptiness.** Measured on a delivered workbook: the section said the row
  begins in the table's FIRST column and, four paragraphs later, that it carries no value
  in the first identity column, which is that same column; both could not hold, every
  correct run had to break one of them on its own judgment, and three empty sections
  resolved it by putting the sentence in the SEVENTH column of a 23-column sheet. The rows
  shipped bordered at 117, 117 and 180.75 points tall with their first six columns empty,
  so what the reader meets at the left edge, which is where the eye lands, is a tall
  bordered empty box with the explanation off to the side of it. **The height, the
  borders and the styling are what make the section LOOK finished; the sentence is what
  makes it finished.** An empty section is a finished section with a sentence in it,
  never a blank box, and the sentence is never a placeholder, a dash or a space.
- Prevents: a correct empty section failing its own reconciliation gate, the likelier
  repair of that failure, which is a false count, and the opposite defect of a section
  styled to look complete while explaining nothing.
- Source: P-D28; extended by the demonstration run, planning N9, and by the
  delivered-workbook readability report
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-08 Row height is computed per cell against that cell's own column width, and the constant is padding
- Rule: a row's height is the height required by the cell in it that needs the most
  wrapped lines, measured against THAT CELL'S OWN column width. Every fixed height in
  the contract is a MINIMUM, never a ceiling.
- **THE ARITHMETIC IS STATED ONCE, IN THE OUTPUT CONTRACT'S ROW-HEIGHT SECTION, AND
  IS NOT RESTATED HERE.** An earlier version of this rule carried its own formula, it
  disagreed with the contract's in two places, and a reader of the doctrine and a
  reader of the contract got different heights off one file. What lives here is the
  reason the computation has the shape it has.
- Mechanism: the per-line constant is DELIBERATE PADDING and is a floor, not an
  estimate of rendered line height. It is ADDED to the computed line height, never
  multiplied by the line count in place of it.
- **Rule: CHAR_WIDTH_FACTOR RUNS IN ONE DIRECTION ONLY. It converts a COLUMN WIDTH
  INTO USABLE CHARACTERS PER LINE, by multiplying the width.** It is less than one, so
  it yields fewer usable characters than the width number and makes rows slightly
  taller than strictly needed, which is the safe direction for a rule whose assertion
  is a FLOOR on height. Its single home, where its value is defined, is the BINDING
  SCHEMA.
- **Rule: A WIDTH BEING SET IS NEVER MULTIPLIED BY IT.** That narrows every column
  below its own header floor, which is the exact defect the width element exists to
  prevent, and it then blocks publication of a correct workbook by correctly detecting
  the damage it just caused.
- **Rule: THE ONE PERMITTED INVERSION IS THE ONE THAT SETS THE WIDTH, AND IT IS A
  DIVISION.** A requirement expressed in CHARACTERS is turned into the WIDTH that
  supplies those characters by dividing it by the factor, once, at the single step the
  output contract names. It can only widen, so it cannot produce the defect the ban was
  written to stop. **Banning that division as well is the opposite failure and it was
  measured:** a width set to the header's character requirement was then read back as
  `width times factor, less the caret allowance`, which is strictly below the
  requirement for every factor under one, so every header needed more lines than its
  budget and the header-line assertion failed on 14 of 29 columns of a workbook built
  exactly to the width rule. **The rule is a DIRECTION, not a ban on arithmetic:
  multiply a width and you have narrowed it; divide a character count and you have
  widened it; only one of those can hide a header.**
- **Rule: THE LINE COUNT IS A WRAP, NEVER A DIVISION OF TEXT LENGTH BY THE USABLE
  COUNT.** The two disagree: seventeen characters as three five-letter words at nine
  usable characters is two lines by division and three by wrapping, because no two of
  those words share a line. The wrap governs, because it is what the renderer does, and
  the division under-counts exactly where the words are long, which is exactly where a
  cell clips. A formula that names both algorithms in one sentence lets two faithful
  implementations disagree about whether one correct workbook passes.
- Prevents: rows "correct on average and clipped on exactly the longest, most
  information-dense entries, which are the rows most worth reading." Computing
  from one column alone is the specific named mistake; a factor applied in the wrong
  direction is the second.
- Source: P-D29; extended by the demonstration run, scorecard D1, D11 and planning D9,
  N3
- Applies: PLANNING, SCORECARD

### SD-FMT-09 State the check in a falsifiable form
- Rule: do not state a check as "no cell clips". State it as the deterministic
  arithmetic test on values the engine reports, "because true clipping depends on
  proportional font metrics the engine does not expose, so that phrasing is not
  verifiable and would make the gate unfalsifiable."
- General form: this is a rule about how to write any gate, in any skill.
- Source: P-D30
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-10 Sampling density must be stated, never assumed
- Rule: walk every populated cell on sections of FULL_WALK_ROW_LIMIT rows or
  fewer. On larger sections apply SAMPLING_DENSITY and state on the record that
  the check was sampled and at what density.
- Prevents: reducing a check to three cells and calling it verified.
- Source: P-D31
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-11 Never put a paragraph in a narrow label column
- Rule: labels in the first column, prose in the second. A label that cannot fit
  in two lines belongs in the prose column with a short label beside it. Do not
  solve overflow by shrinking the font or letting text run under the next cell.
- Source: P-D302
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-12 Verify readability programmatically, not by eye
- Rule: check every cell against the arithmetic test. "Doing this by inspection
  misses cells; a first pass on one artifact found 28 issues."
- **Rule: CONTRAST IS PART OF THAT ARITHMETIC AND IS MEASURED IN THE SAME UNIT THE
  PALETTE SEPARATION RULE ALREADY USES**, which is greyscale value, so the bundle has
  one way of talking about colour rather than two. Text against the surface under it
  holds one floor; a border against every surface it is drawn on holds a higher one,
  because a hairline lays down a fraction of the ink a glyph does. The floors and the
  arithmetic live in the output contract and are cited here rather than restated.
- Mechanism: the check runs on the colours READ BACK from the built artifact, never on
  the colours the build intended to write, per SD-FMT-06.
- Prevents: a palette that was chosen by eye in one renderer, at one zoom, on one
  screen, and is illegible on paper, in a preview pane, or to a reader who does not see
  the hues apart.
- Source: P-D303; extended by the delivered-workbook readability report
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-13 Title Case every heading, every sheet name and every column header, in one stated convention
- Rule: **EVERY HEADING, EVERY SHEET NAME AND EVERY COLUMN HEADER THIS BUNDLE WRITES
  IS TITLE CASE.** That reaches a composed section title, a panel heading, a message
  heading, the string written on a tab, and the string written into a header cell.
- **Rule: THE EXEMPTION FOR TABLE COLUMN HEADERS IS WITHDRAWN.** It rested on the
  claim that "Title-Casing them makes a wide table harder to scan", and the author of
  the method has overruled it: the delivered workbooks were read and the mixed casing
  is what a reader meets first, on the one row that is read on every sheet. A tab and
  a column header are the two shortest labels in the artifact and the two most often
  compared side by side, which is exactly where one convention pays and two do not.
- **Rule: THE ONE EXEMPTION THAT STAYS IS A STRING THE ORGANIZATION BOUND**, which
  ships in the case it was bound in, because a case rule that rewrites an
  organization's own words is a rename nobody asked for. **A DOCUMENTED DEFAULT IS NOT
  A BOUND STRING**: it is this bundle's own words, so it is WRITTEN in Title Case
  where it is documented and needs no re-casing at run time. That is what closes the
  old contradiction, in which one rule required Title Case and another forbade
  altering a documented default, and nothing said which yielded.
- **Rule: THE CONVENTION IS STATED PRECISELY ENOUGH THAT TWO IMPLEMENTATIONS PRODUCE
  ONE STRING**, and it is stated in exactly one place: the validation of
  TITLE_CASE_HEADINGS in the binding schema. It is cited here and never restated,
  because a convention written twice is two conventions.
- Mechanism: a run never re-cases anything at build time. It ships a bound string as
  bound, ships a documented default as documented, and applies the convention only to
  a heading it composes itself. The output contract carries the guarantee and the
  verification.
- Prevents: an artifact whose tabs and column headers disagree with each other and
  with the panels above them, which is the first thing a reader notices and which no
  element could see while one family of strings was exempt.
- Source: P-D301; the exemption withdrawn on the delivered-workbook reading report
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-14 The character gate tests BOTH bounds
- Rule: assert that every character satisfies the lower and upper bounds of
  ALLOWED_CHARACTER_RANGE, across every cell value, sheet name, table name and
  the file name.
- Mechanism: "a bare upper-bound test passes tabs, newlines, vertical tabs and
  every other control character below the lower bound, which are exactly as
  damaging in a cell as a typographic dash." A single violation blocks
  publication and must be repaired, not noted.
- General form: a one-sided bound is not a range check.
- Source: P-D157; R-D40
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-15 Transliterate, never drop, and never truncate a name
- Rule: any character outside the permitted range is transliterated to its
  closest permitted equivalent. Where no reasonable equivalent exists it is
  dropped and the substitution is logged. "This rule is exhaustive by
  construction, so no character class can slip through." A name carrying an
  accent is transliterated to its base letters, never dropped and never
  truncated: losing a name is worse than losing an accent.
- Source: R-D40
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-16 Quote the words faithfully and transliterate the characters
- Rule: when quoting a source, the WORDS are quoted exactly and the CHARACTERS
  are normalized. "Character fidelity never outranks system compatibility."
- Source: R-D40
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-17 Source contamination is the main character risk; sweep on the way IN
- Rule: sweep any text taken from a source BEFORE it enters a draft, not after.
  An export that writes a typographic minus sign produces a sign error waiting to
  happen.
- Source: R-D40; P-D155
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-18 Character verification is mechanical, not visual
- Rule: never approve output by reading it. Scan every authored string
  programmatically. "A visual pass will not catch a non-breaking space, a
  zero-width space, or a byte order mark."
- Source: R-D40
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-19 The character gate applies to authored text, not to binary container bytes
- Rule: the gate applies to every character of text the skill authors, including
  strings placed inside binary containers. It does not apply to the raw bytes of
  the container itself.
- Source: R-D40
- Applies: PLANNING, REVIEW, SCORECARD

### SD-FMT-20 Never drop the row and never blank the field to fix a character problem
- Rule: "a unit the user cannot find is worse than an imperfect spelling." Log
  any value you had to change.
- Source: P-D156
- Applies: PLANNING, REVIEW, SCORECARD

---
