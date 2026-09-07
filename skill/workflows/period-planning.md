---
name: period-planning
description: Builds a prioritized work list for the coming operating period, ranked by business impact and weighted against three sources of direction that are read on every run: the user's own supervisor chain, the organization's central or headquarters publications, and the organization's standing priority hierarchy. Priorities are validated against the governing compliance standard before anything is weighted. Works with no training for any employee from frontline to chief executive and needs no configuration from the user: span of control decides the size of the list, the altitude of the claims, and which comparisons are permitted. Handles both a fixed enumerable population such as locations, accounts, facilities, machines, routes or territories, and a flowing pipeline such as deals, tickets, cases, claims, candidates or work orders. Use when someone asks what to work on next period, for a visit plan, a call plan, a route plan, a territory or account plan, a priority list, a target list, a coverage plan, a caseload plan, a pipeline focus list, what their team should cover this month, cycle or quarter, which accounts or cases matter most, how to spend the coming period, or asks for that same list scoped to a place, narrowed to a subset, or leaned toward a product line, a service line or a named initiative. Also use for a period-over-period comparison of the same population when two source files are supplied and the user asks what moved. Do not use to rank or evaluate people.
---

# PERIOD PLANNING

Build the prioritized work list for the coming operating period.

---

# PART 0: WHAT THIS IS AND HOW TO READ IT

## 0.1 What the skill does, in one paragraph

It takes the organization's own periodic source of record for a population of
units, resolves who is asking and what they own, reads every source of direction
that bears on the coming period, validates those directions against the
governing compliance standard, scores every unit in the requester's scope
against a published formula, and emits ONE deliverable in a fixed shape whose
only variation is three counts decided by the requester's span of control. The
list leads. Everything explanatory follows it. Every number it publishes can be
recomputed by hand from the artifact itself.

## 0.2 The five rules that govern every other rule

- G1. One declared contract per deliverable, superior to every other section of
  this file. Any later instruction that disagrees with the contract in PART 1 is
  the defect, not the contract.
- G2. Fail closed. Unknown is not pass.
- G3. Never default an unknown to the value that maximizes its score.
- G4. Every number carries a second number the writer did not choose.
- G5. A rule that costs nothing when it does not fire and keeps the method
  portable is worth carrying.
- G6. Precedence runs downhill from evidence to convention, and an UNBOUND value
  never overrides a BOUND one. SD-CTR-24. In order: a value the answerer bound at
  IGNITION; a value the answerer bound later; a value DERIVED FROM THE DATA THIS
  RUN; a documented default. A documented default may NARROW what the run
  attempts. It may never contradict, replace or silently supersede a value the
  organization actually bound. Before applying any documented default, test
  whether it would change a decision a bound value already decided; if it would,
  the default is not applied to that decision, the bound value stands, and the
  notice names the NARROWING rather than the substitution.

## 0.3 How doctrine is cited

Shared doctrine lives in reference/doctrine/ and is cited here by stable ID, for example
SD-CTR-01. A citation means the rule is in force at that point exactly as
written there. This file does not restate a cited rule except where the
operative wording is load bearing and a paraphrase would lose it, in which case
the wording is reproduced verbatim and the ID is still cited.

Every doctrine rule whose Applies list includes PLANNING is in force in this
skill. PART 27 is the complete coverage index and names where each one is
honoured. Their NUMBER is not stated here or anywhere outside that index, because
a count restated outside the table that derives it drifts the moment a rule is
added, and this one has been added to four times. A rule not visibly cited in the
body is still in force; the index is the proof it was carried, not a suggestion.

## 0.4 The companion files this skill invokes and does not duplicate

| File | What it owns | How this skill uses it |
|---|---|---|
| reference/schema/ | The variable dictionary, the four binding states, standing rule S9 on precedence, and SECTION A1 and A2, split for DEFERRED variables and A2 for CONDITIONAL variables, each holding a documented default and an exact degradation notice. | Every employer-specific value in this file is one of those variable NAMES. Never a literal. When a default is applied, the notice printed is the one in A1 or A2, verbatim, and a CONDITIONAL variable whose trigger has been met uses A2. |
| reference/binding-interview.md | The staged binding: the IGNITION set, every DEFERRED variable, the four constraints on when a deferred question may fire, the PERSON script, and the first-run-at-an-unbound-company sequence. Variable COUNTS are not stated here or anywhere in this file; they live in the COUNTS block of reference/schema/ alone, because a count restated outside its own table is a second source of truth that nothing updates. | Invoked at run start (PART 3) and at each of the deferred decision points in PART 22. This file never repeats a question script; it names the catalogue entry. |
| reference/capability-probe.md | The probe, the per-capability degradation ladders, the combination rules, and the announcement rule. | Invoked as stage 0 of every run (PART 3.1). Degradation behaviour is read from there, not decided here. |
| reference/field-resolution.md | Container selection, header detection, the three matching passes, the value checks, the strict-exact-only rule, the seed concept dictionary, and the runtime learning mechanism. | Invoked at the parse stage (PART 10). This file never restates a stem list. |
| reference/output-contract.md | **THE UNIVERSAL OUTPUT CONTRACT.** The output medium keyed per skill; the formatting elements with their standards and their programmatic verifications; the caret allowance and the computed column widths, row heights and header row height; the rank and reason-for-rank columns; rank continuity and the derived last rank; the per-sheet cap and the exact showing-note wording; the unit noun. | Invoked before publication, on every run. **This skill CITES an element by number and never restates its standard**, because a restated contract is how the elements degraded to passing mentions and stopped being enforced. Where this file and the contract appear to disagree, the contract governs and this file is stale. |

If a companion file and this file disagree on something the companion file owns,
the companion file governs. If they disagree on the shape of the output, PART 1
governs, per G1 and SD-CTR-01.

## 0.5 No literals, ever

Every employer-specific value is a named variable defined in reference/schema/.
No company, division, product, system, brand, place, document number, code
scheme, path, endpoint or identifier appears in this file, and none may be
written into a rule at bind time. The binding interview records values; skill
text references names. Where a rule needs a concrete illustration to be
understood, the illustration is invented and neutral and is labelled as a worked
example.

## 0.6 When to use

Every one of these resolves without a follow-up question, because SCOPE,
QUALIFIER and STEER (PART 2) compose freely:

- A plain request for the coming period's work list, at any level of the
  organization.
- The same request with a scope named in ordinary words rather than a code.
- The same request narrowed by any attribute the source carries: a place, a
  group, a class, a band, a supplier, a stage.
- The same request leaned toward a product line, a service line, a programme or
  a named initiative.
- A request for a specific list size.
- A request from a leader asking what one of their units or teams is carrying.
- A period-over-period comparison, when two source files are available AND the
  user asked for a comparison.

## 0.7 When not to use

- Ranking, evaluating, comparing or scoring PEOPLE. Declined outright, in every
  phrasing, at every level. SD-LNG-02. This skill ranks units of business.
- Editing, charting or reformatting a spreadsheet for its own sake: route to the
  destination named in SIBLING_SKILLS.
- Writing a narrative document, a recap or a review: route to the destination
  named in SIBLING_SKILLS, or to the review skill in this bundle.
- Producing a capability another system already owns, for example routing,
  scheduling, dispatch or forecasting. SD-EXC-24, and the exclusions are named
  in SYSTEM_OF_RECORD_EXCLUSIONS.
- No source of record and none supplied: ask for it, naming every location
  attempted. Never improvise a population. SD-SRC-11, SD-SRC-12.

## 0.8 There is no time limit on this task

SD-EFF-01 governs every decision below it. Length of run is not a cost this
skill recognizes. A run that takes twenty-five minutes and is right is a
complete success. A run that returns in four minutes with an unverified number,
a fabricated action or a missing section is a failure no matter how fast it
returned. Never shorten a list, skip a verification, drop a section or summarize
because the work is taking a while. Never stop at a partial result and describe
what you would have done. A very large input gets the same treatment as a small
one. Work the retry paths. Only a gate named in HARD_GATES stops a run
(SD-EFF-02), and fatigue, run length, retry count and output size are not on
that list and never will be.

---

# PART 1: THE OUTPUT CONTRACT

This part is the single declared source of truth for the shape of the output.
Read it before stage 1 and verify it at the final gate. Where any later
instruction disagrees with this contract, the contract governs and the later
instruction is the defect. SD-CTR-01.

The reason is not stylistic. Defects live at the seam between two individually
correct sections, because no single place states the whole shape of the output.
This part is that place.

**ONE EXCEPTION, AND IT IS ABOVE THIS PART RATHER THAN INSIDE IT.**
reference/output-contract.md is the bundle's single statement of the output contract, and
where this part and that file appear to disagree, THAT FILE GOVERNS AND THIS ONE
IS STALE. This part cites it by element number and by part number and never
restates a standard it carries, because a restated contract is how the formatting
elements degraded into passing mentions and stopped being enforced. SD-FMT-22.

**THE HEADER ROW IS ROW 1 ON EVERY ITEM SECTION OF THIS ARTIFACT, PER
reference/output-contract.md ELEMENT 1, AND THIS FILE ADDS NOTHING TO THAT STANDARD.** The
only thing this file states is the consequence for THIS skill, which is which
sections it reaches and where the displaced material goes instead:

- **Which sections.** Every section in 1.2 whose rows are data rows: the
  priorities section, the directed section, the first action list, the second
  action list, the reference list, the breadth section and the exception section.
  Each one begins with its header strings in row 1. There is no title row, no
  banner row, no scope row, no period row, no note row and no spacer row above
  any of them, on any run, ever.
- **Where the title goes instead.** The report title, the scope, the period and
  every caveat live on the FRONT PANEL, per 19.3.1 block 1. That is where a
  reader looks for them and where they can be read without scrolling a grid
  sideways.
- **Where the section-level notes go instead.** The showing note, the shortfall
  note and the ordering note of 1.6 go in the NOTE BAND, which
  reference/output-contract.md PART 5.3 defines exactly and which is the ONE place a
  per-sheet note lives: one blank spacer row below the table's last row, then one
  merged row per note across the full column span of the table, left aligned, at
  the panel label fill, with its height computed against the summed width of the
  merged span. Never as a row above the header row, never inside the table range,
  and never in a single column below it. SD-FMT-26. **An earlier revision of this
  file said those notes sat "beside the section heading", and that placement did
  not exist.** Element 1 forbids any row above the header row, element 3 forbids a
  populated data row inside the table range, and 19.3.1 puts the title on the
  front panel and nowhere else, so there is no section heading on an item section
  for a note to sit beside. The wording is deleted rather than reinterpreted.
  1.6.1 states which notes this skill emits, where each one goes and in what
  order.

**THE INCOMPLETE BANNER OF PART 21 IS A DIFFERENT THING AND IS NOT AN EXCEPTION
TO ANY OF THAT.** INCOMPLETE_BANNER_TEXT is announced in the three places PART 21
names, the FRONT PANEL, the METHOD section and the FIRST LINE of the reply, and
in no other place. It is never written as row 1 of an item section, never as a
row above a header row, and never as a merged cell spanning a table. A banner
above a header row pushes the headers down and breaks the freeze pane, the table
range, the autofilter and every header-name lookup at once, which is exactly the
failure element 1 exists to prevent, and a degraded run is the run that can least
afford a broken artifact on top of a reduced one. SD-FMT-22, SD-FMT-23.

## 1.1 One format, two sizes

There are exactly two deliverable lines and no others. Every run emits exactly
one artifact, in the line that matches the resolved role. The two lines are
identical in every respect except three counts. SD-CTR-02.

| Element | Junior line, REPORT_LINE_JUNIOR_KEY | Senior line, REPORT_LINE_SENIOR_KEY |
|---|---|---|
| Who receives it | Roles whose claim_tier is DIRECT | Roles matching SENIOR_TIER_PREDICATE |
| First action section size | DELIVERABLE_LINES junior tier_1_size | DELIVERABLE_LINES senior tier_1_size |
| Second action section size | junior tier_2_size | senior tier_2_size |
| Reference section depth | the line's own reference_cap | the line's own reference_cap, which the standing defaults set to the same number as the junior line's |
| Everything else | identical | identical |

The line boundary is a single cut in the ordered ROLE_LADDER, named once in
SENIOR_TIER_PREDICATE. Never restate the predicate as a list of titles; a
restated list drops a member the first time a title changes.

**The action list gets SHORTER RELATIVE TO SPAN as scope widens.** SD-RNK-09. A
more senior person has less time, not more, so the list is NEVER proportional to
span: it grows far more slowly than the span it covers, and as a SHARE of what
the reader owns it shrinks sharply. The reference depth stays constant.

**READ THAT AS A SHARE, NOT AS ROWS. THE SENIOR PAIR IS THE LARGER PAIR IN
ROWS.** The standing sizes are 10 and 25 for the junior line and 20 and 50 for
the senior line, and that is the design, not a contradiction of the sentence
above. A direct-tier reader owning a hundred units receives a first tier of ten,
a tenth of their span. An aggregate-tier reader owning several thousand receives
a first tier of twenty, a fraction of one percent. The second is by far the
shorter list in the only sense that matters to the person holding it. Any reading
that hands a senior leader FEWER rows than a frontline reader off the same file
is a misreading of SD-RNK-09 and is wrong.

If a binding owner proposes senior sizes proportional to span, push back once
with that sentence, then record whatever they say. Q-N1.

## 1.2 The section set: every section, in order, every run

**TAB_CONTRACT AND DELIVERABLE_NAME ARE KEYED PER SKILL, AND THIS SKILL READS THE
PLANNING KEY.** SD-CTR-30. Both are read by three skills that produce three
different documents, so a single shared default holding one skill's sections and
one skill's title is that skill's contract wearing a shared name: a literal
implementer of either other skill ships a document titled and shaped like a work
plan. TAB_CONTRACT is a keyed set with one ordered section list per skill;
DELIVERABLE_NAME is a mapping from skill to name and a single string is rejected
at validation. This file reads the PLANNING entry of each and never inherits
another skill's list or name, and where the planning key is absent the run says so
rather than falling back to whichever list is present.

The same rule governs any shared default this file relies on whose NOUN differs by
skill: the default names the ROLE rather than one skill's word. What a compliance
gate holds back is THE VALIDATED ITEMS, which are this skill's priorities and
another skill's requirements, and 9.2 reads it that way.

The ordered list is TAB_CONTRACT, at its planning key. It has at least four entries and its order is
fixed. Every section ships every run, even with nothing to report, carrying its
header plus exactly one row stating the reason in plain language from
MSG_EMPTY_SECTION. Never drop a section, never renumber around one, never
reorder them. SD-CTR-07.

The standing set, when the planning key of TAB_CONTRACT is unbound, is these
sections in this order,
and their families decide which rules apply to each:

| # | Section | family | Capped at | Purpose |
|---|---|---|---|---|
| 1 | Front Panel | panel | not applicable | The ask; the do-this-week block; what changes how to read the numbers; how the list was built, what is in the artifact, how to read the columns, the alert line, the degradation notices, the contact line. Its five blocks and their order are 19.3.1, and its language is 19.3.2. |
| 2 | Priorities | direction | REFERENCE_CAP | Every direction found, quoted verbatim with sender and date, plus every direction that could not be matched or was held back. |
| 3 | Directed | mandatory | REFERENCE_CAP | Units named on a directive list. Ranked among themselves. Outside the merit tiers. |
| 4 | First Action List | identity_and_rank | tier_1_size | Ranks 1 upward. |
| 5 | Second Action List | identity_and_rank | tier_2_size | Resumes at the next rank. |
| 6 | Reference List | reference | REFERENCE_CAP | A lookup, not a plan. Resumes after the second action list. |
| 7 | Breadth | derived | REFERENCE_CAP | Breadth of adoption. Never touches the ranking. |
| 8 | Exceptions | exception | REFERENCE_CAP | Quiet problems no other report surfaces. Membership is tripping at least one SCORED flag. |
| 9 | Method | panel | not applicable | The exhaustive audit trail. Last, always. |

An empty section is a FINISHED section with nothing in it, and it carries the
full styling of a populated one. SD-FMT-07. A section that FAILED TO BUILD is
incomplete and blocks publication. These two meanings of empty must never be
confused. SD-EFF-06. **Where the section qualified zero units, its one
explanatory row is placed and counted by reference/output-contract.md PART 5.4 and this
file does not restate that standard**: the row sits INSIDE the table range as the
only data row, it is NOT a unit row, and n and N are both zero in the showing
note. 1.6.1 carries the consequence for this skill's own notes.

**EVERY SECTION TITLE HERE BECOMES A SHEET NAME, AND THE SHEET-NAME CONSTRAINT IS
STATED ONCE IN reference/schema/ GROUP 15.** OUTPUT_MEDIUM at the planning key is
xlsx, so each TAB_CONTRACT entry's `title_variable` is not only a heading: it is
the name of a sheet, and a sheet name is one of the few strings in this bundle a
container engine REJECTS OUTRIGHT rather than renders badly. GROUP 15 states the
four conditions, the six forbidden characters, the length bound and the
DETERMINISTIC TRUNCATION RULE that applies where a BOUND value violates them.
**This file cites that constraint and never restates it, and a run never invents
its own shortening.** Three consequences are this skill's own and are stated here:
the run tests every title variable it will use AT BINDING TIME rather than at
build time, so the failure surfaces before a sheet is created; where the
truncation rule fires, the rename is disclosed in the Method section with the
original value beside it and raised as one open request against the binding that
carried the illegal value, per PART 22; and the section itself is never dropped,
never merged and never renumbered to avoid the problem, because a section that
ships every run does not stop shipping because its title was too long. The
failure this closes was measured: a documented default carrying a colon and
running past the length bound raised an exception in the container engine and
produced a file the reader's spreadsheet would not open, and the only remedy
available to the run was to shorten the label itself and disclose it.

### 1.2.1 The CLASS of every section, and the KIND of every ranked one

**reference/output-contract.md PART 2.0 requires a skill to DECLARE the sheet CLASS of every
sheet it emits, and PART 4.2 requires it to declare the KIND of every ranked one.
This is that declaration, made once, here, and recorded on the Method section of
every artifact.** Without it, a reader of the verification matrix has to work out
for themselves which elements were expected to run where, and R1 through R5 of
PART 7.2 do not resolve at all, because every one of them is scoped to a class or
to a kind.

| Section | Sheet CLASS, per PART 2.0 | Ranked KIND, per PART 4.2 |
|---|---|---|
| Front Panel | PANEL SHEET | not a ranked sheet |
| Priorities | REFERENCE TABLE, because it is a GRID whose rows are DIRECTIONS rather than units of business | not a ranked sheet. Its order is stated in 1.2.2 |
| Directed | ENTITY SHEET | NONE OF THE THREE, which PART 4.2 states of a directed sheet in those words: its units are ranked 1 to N among themselves, are excluded from the merit tiers and from eligible_count, and never consume a merit rank |
| First Action List | ENTITY SHEET | MERIT TIER, the first tier of the set |
| Second Action List | ENTITY SHEET | MERIT TIER, the second tier of the set |
| Reference List | ENTITY SHEET | MERIT TIER, the reference tier of the set |
| Breadth | ENTITY SHEET | NONE OF THE THREE. It is neither a partition of the ranked population nor a census of it: membership is the PAIR test of 15.2 and the order is BREADTH_SORT_KEYS |
| Exceptions | ENTITY SHEET | NONE OF THE THREE. Membership is by flag and the order is flag weight, per 16.2 and 16.3 |
| Method | PANEL SHEET | not a ranked sheet |

**THIS ARTIFACT EMITS A MERIT TIER SET AND NEVER A CENSUS AND NEVER AN EXTRACT.**
The three merit sections partition the ranked population into one unbroken
sequence, per 1.6 and PART 4.2.1, so `tier_1_size`, `last_visit_rank` and the
derived last merit rank are all meaningful here and are read exactly as PART 4.2.1
gives them. The census arithmetic of PART 4.2.2 and the extract arithmetic of
PART 4.2.3 are NOT APPLICABLE to any section of this artifact, and that is
RECORDED with this declaration as its reason rather than left silent, because a
check that applies a census form to a merit tier set is testing a number this
workbook never produced.

**WHAT FOLLOWS FROM THE DECLARATION, and it is the contract's answer rather than
this file's:** an ENTITY SHEET and a REFERENCE TABLE take elements 1 to 14 and 16;
a PANEL SHEET takes elements 7, 15 and 16 and records the REMAINING elements of 1
to 14 NOT APPLICABLE with the sheet class as the stated reason. **ELEMENT 7 IS THE
ONE GRID ELEMENT THAT ALSO REACHES A PANEL**, because its scope is every populated
cell of the SHEET'S USED RANGE and a panel row is a populated cell, per PART 7.2
row 7.

**THE R ROWS ARE SCOPED BY PART 7.2 ROW BY ROW, AND WHERE PART 2.0's CLASS TABLE
GIVES A SCOPE MORE LOOSELY, THE MATRIX ROW GOVERNS.** PART 2.0 says so in those
words, and the reason is that two of the R rows are not scoped by sheet class at
all. Read this way for this artifact:

| Row | Where it runs here |
|---|---|
| R1 | Every ENTITY SHEET and the REFERENCE TABLE, which is every section except the two panels |
| R2 | The MERIT TIERS alone, so the directed, breadth, exception and priorities sections sit outside it and that exemption is RECORDED rather than assumed |
| R3 | EVERY BOUNDED SECTION whatever its class, per PART 5.1.1 and the table in 1.6, which is every section of this artifact except the two panels, and which reaches a panel too wherever a panel is itself bounded |
| R4 | The ranked sheet set, reading PART 4.2.1's merit-tier form on this workbook, because this workbook is a merit tier set |
| R5 | THE WHOLE WORKBOOK, panels included, because it scans for a hard-coded unit noun anywhere |

Neither R3 nor R5 becomes inapplicable because a section is a reference table or a
panel, and a run that records either as NOT APPLICABLE on a panel has read the
class table where it should have read the matrix.

### 1.2.2 The priorities section is a REFERENCE TABLE, and what that settles

**PART 2.0 says a grid whose rows are not units of business is a REFERENCE TABLE,
that a skill DECLARES which it is, and that declaring neither is the defect.** The
priorities section is a grid: one row per direction, byte-identical headers from
HDR_ variables, a header row in row 1. It is therefore declared a REFERENCE TABLE
and not a panel, and three things follow that this file used to get wrong.

1. **It takes every grid element, 1 to 14 and 16**, exactly as an item section
   does. It is not exempt from the widths, the heights, the gridlines, the
   autofilter or the table object because its rows are not units.
2. **R1 RUNS ON IT, in the POSITION-column form of PART 4.1.** A reference table
   carries a POSITION column and a REASON-FOR-RANK column, and PART 4.1 admits no
   sheet of either class without both. So this section carries exactly two
   identity columns and no others: `HDR_POSITION` in first place, holding the
   direction's position in the stated order below, and `HDR_RANK_REASON` closing
   the pair, saying why the direction sits at that position. **It is headed
   HDR_POSITION and never HDR_RANK**, because the order is not a merit order and
   PART 4.1 makes a non-merit order headed as a rank a contract violation.
3. **It still carries NO UNIT identity block**, and that is a different statement
   from carrying no identity columns. A direction has no unit identifier, no unit
   name, no address, no measure and no percentile, and SD-CTR-08 binds the unit
   identity block across the sections whose rows are UNITS. Writing those columns
   here would ship a wall of blanks on every row, which is the failure 1.3b
   describes.

**THE ORDER OF THIS SECTION, stated once, here, because a position column with no
stated order is a column of arbitrary integers.** Sort the directions by, in
order: the source band of PART 8's table, A then B then C then D, so the reader's
own current chain leads and the directions swept up from below sit last, per the
band D paragraph in PART 8; then chain distance, nearest namer first, by the
CHAIN_DISTANCE_WEIGHTS entry that 8.4 resolved; then the direction's own date,
most recent first; then the sender identifier ascending; then the direction's
POSITION WITHIN ITS OWN SOURCE DOCUMENT, earlier first, and then that document's
own title or filename ascending, which are the fourth and fifth keys of the
direction tie-break chain stated once in 8.8.1 and which make the order TOTAL
even for two numbered priorities written by one sender in one document on one
date, per SD-RNK-10. The reason column names the
keys that placed the row, in that order, in the reader's own words per SD-LNG-07.

**A DIRECTION THAT MATCHED NO UNIT STILL TAKES A POSITION AND A REASON**, per
SD-PRI-16. Its position is its place in the same order; its reason says it was
published, was read, and matched no row in this scope, with MSG_UNMATCHED_MANDATORY
carried in its status column. Nothing about the merit ranking moves.

## 1.3 The identity block

The same identity columns, in the same order, on every item section without
exception. SD-CTR-08. The columns are IDENTITY_BLOCK_COLUMNS. It is verified by
header NAME and relative order, never by fixed column number, because the
block's width changes with the requester's level: a check written against
columns one to nine passes a wrongly built junior artifact and fails a correct
senior one.

Header strings are byte-identical between runs. Do not rename, reorder, add,
omit or improve a header for readability. SD-CTR-09. Every HDR_ variable is a
config string, never a phrasing choice.

The rank-within-scope column carries SCOPE_RANK_HEADER, the same string at every
scope level, never retitled for the requester's own level. SD-CTR-11.

A column whose source does not resolve is still written, header present and
cells blank, with the failure named in the Method section. Dropping it changes
the shape of the artifact and is a contract violation. SD-CTR-13.

Identifier and postal-style columns are written as TEXT on both the source side
and the artifact side, because codes carry leading zeros in some units and a
spreadsheet strips them silently. SD-SPN-06.

**THE RANK COLUMN AND THE REASON-FOR-RANK COLUMN ARE BOTH MANDATORY, ON EVERY
SECTION WHOSE ROWS ARE UNITS.** reference/output-contract.md PART 4.1 makes the POSITION
column an identity column and PART 4.1.1 places the REASON column immediately
after the identity columns, and this file does not restate either standard. What
this file states is what this skill puts in them, and how the header string for
the second one is resolved while the schema has no entry for it. SD-FMT-24.

**THE POSITION, DECIDED IN reference/output-contract.md 4.1.1 AND CITED HERE, USED
EVERYWHERE IN THIS FILE:**

> **The POSITION column is the FIRST column of the identity block. HDR_RANK_REASON
> IS THE FIRST COLUMN AFTER THE IDENTITY COLUMNS**, immediately after the final
> identity column and immediately before the section-specific block of 1.3b. It is
> not itself an identity column, and it is NEVER inside the frozen span.

So the row reads: the position column, then the columns that say who the unit is,
then the sentence saying why it sits where it does, then the section-specific
block. Position first, identity in the middle, rank reason closing the identity
columns off from the outside. **THERE IS NO OTHER PERMITTED POSITION FOR IT**, and
in particular it is never placed at the far right beside the narrative column. The
position column is headed `HDR_RANK` where the section's order IS the merit order
and `HDR_POSITION` where it is not, per reference/output-contract.md PART 4.1 and the family
table in 1.3b.

**AN EARLIER REVISION OF THIS FILE CALLED HDR_RANK_REASON THE LAST COLUMN OF THE
IDENTITY BLOCK, AND THAT WORDING IS RETIRED RATHER THAN REINTERPRETED.** It read
as if the reason were one of the identity columns, which made
IDENTITY_BLOCK_COLUMNS and the frozen span disagree about whether a paragraph was
part of a unit's identity. It is not. The contract's position and this one are the
same column on a sheet whose whole identity block is frozen, and they are
different columns the moment 4.1.2's bound truncates the span, which is exactly
the case the old wording could not express.

**THE FREEZE POINT IS DERIVED FROM THE BOUND, NEVER CHOSEN, AND
reference/output-contract.md 4.1.2 IS THE ONLY STATEMENT OF THE WALK.** This file cites it
and does not restate the arithmetic: `IDENTITY_BLOCK_ANCHOR_COLUMN` is the LAST
identity column whose inclusion keeps the SUMMED BUILT WIDTH of the frozen span at
or under `FROZEN_SPAN_MAX_WIDTH`, walking the identity columns left to right, with
the FIRST column always frozen even where it alone exceeds the bound, and element
2's freeze set at row 2 and at the first column after that anchor. Two cases and
both are ordinary:

- **The whole identity block fits inside the bound.** The anchor is the last
  identity column, the freeze lands ON the reason column, and the reason column is
  the first column outside the frozen span.
- **The bound truncates the span.** The anchor is EARLIER, the freeze lands on the
  first identity column that did not fit, and the reason column is still outside
  the span, because truncation only ever SHORTENS it. **Nothing is moved, nothing
  is dropped and nothing is narrowed to make the block fit**, and in particular no
  column is ever narrowed below its own 2.2 floor to buy a longer freeze, which
  would trade a readable freeze for an unreadable header.

**THE WALK RUNS ONCE FOR THE WHOLE ARTIFACT, FROM THE WIDEST CASE, AND NEVER ONCE
PER SECTION.** 4.1.2 owns this and this file states only what it means here. A
built width depends on the longest DATA value in that column ON THAT SECTION, per
PART 2.2, so a per-section walk stops in a different place on every section of one
workbook. Measured on this skill's own run: an identity block that was the same six
columns everywhere froze THREE identity columns on the three merit sections and
FIVE on the three that qualified zero units, because an empty section's name column
holds no value, falls back to its own header floor and leaves room for two more.
Every one of those sections passed element 2 individually. **The WORKBOOK failed**,
and nothing could see it: a reader scrolling right on one tab kept three columns
pinned and on the next tab kept five, for a reason invisible on the face of the
artifact, and the Method section carried SIX different truncation statements for
ONE identity block. So, in this skill:

- The walk runs AFTER every width on every section is built and BEFORE any freeze
  is set, over each identity column's MAXIMUM built width across every section of
  this artifact that carries the full identity block, per 4.1.2 step 1.
- It yields ONE `IDENTITY_BLOCK_ANCHOR_COLUMN` for the artifact, and that anchor is
  located BY HEADER NAME on every section, per SD-FMT-03 and SD-CTR-08. **A freeze
  landing in a different place per section is not a structurally identical identity
  block**, because what a reader experiences moving between sections is the pin.
- **A SECTION WHOSE OWN BLOCK IS GENUINELY NARROWER FREEZES THE SAME COLUMNS IN
  FEWER WIDTH UNITS, AND THAT COSTS NOTHING.** The anchor is a COLUMN, not a width.
  A section that qualified zero units and falls back to its header floors uses less
  of the bound and pins the same columns. **What no section may ever do is freeze
  MORE columns than the widest case allows**, which is exactly the defect this
  closes.
- A section that does NOT carry the whole identity block is OUTSIDE the walk and
  never shortens it for the sections that do; it freezes at the last identity
  column it does carry, subject to the same bound, and the Method section names it
  and says which identity columns it lacks. Under 1.2.1 the only families in that
  position are the ones whose rows are not units, so this is the rare case.

**THE IDENTITY BLOCK IS ORDERED MOST-IDENTIFYING FIRST, WHICH IS THIS SKILL'S OWN
DECLARATION OF ITS OWN ORDER**, so that a truncated span keeps the columns that
answer which unit a row is: the position column, then the unit's own identifier,
then the unit's name, then the parent group where one resolves, then the
span-of-control columns in the position SPAN_BLOCK_POSITION gives them, then every
remaining identity column in the order IDENTITY_BLOCK_COLUMNS carries. Where
IDENTITY_BLOCK_COLUMNS is bound in a different order the BOUND ORDER GOVERNS,
because it is the organization's own declaration and SD-CTR-24 puts a bound value
above a derived one; the run then says in the Method section that the bound order
was used and which columns the bound order leaves outside the frozen span.

**THE TRUNCATION IS RECORDED ONCE FOR THE ARTIFACT, because a silently shortened
freeze is indistinguishable from a broken one and six records of one identity block
are worse than none.** Where the bound truncates the span, the Method section
states, IN ONE LINE: the bound; the summed WIDEST-CASE built width of the frozen
span; WHICH SECTION supplied the widest case for each identity column the walk
read; and the identity columns left outside the span BY HEADER NAME. Where it does
not truncate, that same one line states the summed widest-case width and that the
whole identity block is frozen ON EVERY SECTION. **It is ONE LINE FOR THE WORKBOOK
AND NEVER ONE LINE PER SECTION**, per reference/output-contract.md 4.1.2, because the walk
that produced it ran once; a run emitting one record per section has performed the
per-section walk that rule forbids, whatever its records say. Both forms ship every
run and both are verified by element 2 at 18.2. **A zero here is the evidence the
walk ran**, exactly as it is everywhere else in this file.

**Why the reason sits immediately after the identity columns rather than beside
the rank or beside the narrative, because the choice is not arbitrary and a later
reader will otherwise move it.** Three reasons, and the second is the one that
decides it:

1. It sits in one FIXED position on every section that carries the identity
   block, so the row reads the same way everywhere. SD-CTR-08 binds the identity
   block itself, and a reason column that drifted between sections would be the
   same defect one column over.
2. **It must sit OUTSIDE the frozen span, and any position among the identity
   columns risks putting it inside.** Everything up to the anchor is frozen to the
   left edge on every screen. A free-text column in second position would be
   pinned there permanently, and a paragraph beside the position column costs the
   reader most of their horizontal space for a sentence they read once per row.
   That is a defect the reader cannot fix and cannot scroll away from. **The
   frozen span exists to keep the unit's IDENTITY on screen, and a paragraph is
   not an identity.** Placing it immediately after the identity columns puts it
   outside the span under BOTH branches of 4.1.2, because truncation only ever
   shortens the span.
3. That position is also the boundary where the reader crosses from WHO the unit
   is to WHAT TO DO about it, which is the question the reason answers on the way
   past. Twenty columns to the right, beside the narrative, it answers a question
   the reader stopped asking fifteen columns ago.

Every other place in this file that names the column uses this position: 1.3b for
its per-family content, 1.9 and 18.1 for the gate, 1.10 for its shape token,
which the schema's own membership rule already carries as a left-aligned
free-text header, 1.11 for the degraded container and PART 22 for its binding. Nothing in this file
places it anywhere else, and nothing in this file places it inside the frozen
span.

**THE HEADER STRING.** HDR_RANK_REASON is a GROUP 24 variable like every other
header, requested from the binding owner at the same point of need, per PART 22
decision 48. Where it is bound, the bound string ships. Where it is unbound, the
run applies the documented default in reference/schema/ SECTION A1 and prints
that appendix's exact degradation notice IN THE ARTIFACT, counting it in the
count of defaulted headers 48 already requires. The string is byte-identical
between runs either way, per SD-CTR-09, and it is not restated here: a header
string written into this file is a second source of truth that nothing updates,
which is the defect 1.3b retired when GROUP 24 took over HDR_COMMITMENT_DATE.
Where a default of its own fails the header test, the correction runs through
1.3e like every other correction, disclosed with the string it replaced and
raised as one open request, and never as a second declaration.

**WHAT THE CELL HOLDS.** The reason names, IN PLAIN LANGUAGE, THE TERMS THAT
ACTUALLY DECIDED THE POSITION, IN THE ORDER THEY CONTRIBUTED. The terms are not
invented for the column and are never a general description of the method: they
are the terms of the scoring formula in 12.1, which this artifact already prints
in full in the Method section, so every reason is traceable to an arithmetic the
reader can redo by hand and dispute term by term rather than in general.
SD-CTR-21.

**The standing form of the string:**

> `{the term that contributed most, with its own figure}; {the next term, with
> its figure}; {the next}; {the tie-break, only where one decided the position}`

Semicolon-joined, in contribution order, largest contribution first, each term
named in the reader's own words rather than by its variable name, per 19.3.2 and
SD-LNG-07. Where the deterministic tie-break of 12.13 is what settled the
position against an adjacent row, the string names the key that settled it; where
no tie-break was reached, the tie-break is not mentioned at all, because naming a
term that contributed nothing is the same defect as omitting one that did.

**A TERM WITH THE SAME VALUE ON EVERY ROW EXPLAINS NO POSITION AND IS NEVER NAMED
AS ONE, WHICH IS WHAT "DECIDED THE POSITION" MEANS.** The ordering above is by
CONTRIBUTION, and a term's contribution to a SCORE is not the same quantity as its
contribution to a PLACE. Measured: a run decomposed each term's contribution
correctly, printed the rule so it could be reproduced, and on rows where the
alignment term was small the largest single contributor was BASE_TERM, so the
leading clause of a first-position row read that the base every unit carries put it
there. That is arithmetically true and useless, because the base is identical on
every row of the population and can never explain why one row outranks another.
**A reason that survives being true of every row has not answered the question the
column exists for.** So:

- **THE CONTRIBUTION ORDERING IS COMPUTED ON THE DIFFERENCE FROM THE POPULATION'S
  OWN MEDIAN VALUE OF THAT TERM, not on the term's absolute value.** The population
  is the full ranked population, the same one every other figure in this file is
  computed over. That is what separates a term into the part that is a property of
  the METHOD and the part that is a property of the ROW.
- **A TERM WHOSE VALUE IS IDENTICAL ON EVERY ROW OF THE RANKED POPULATION IS
  EXCLUDED FROM THE ORDERING ENTIRELY AND IS NEVER NAMED IN THE STRING.** Its
  difference from the median is zero on every row by construction, so the rule above
  already excludes it; this states the consequence so nobody restores it as a
  leading clause. BASE_TERM is the standing case, and it is not the only one: any
  term whose input did not resolve, or whose multiplier came out at its neutral
  floor for the whole population, is in the same position.
- **NOTHING BECOMES UNDISCLOSED, AND THE SCORE DOES NOT MOVE.** The excluded term is
  still IN the score, still printed in the formula in the Method section, and still
  reproducible from the published number of 26.1. What changes is only which terms
  the sentence NAMES. Where the exclusion would empty the string, which happens on a
  population uniform in every term, the string says THAT instead, and the
  uniform-column rule of 1.3b carries the finding to the front panel.
- **THE RULE IS PRINTED IN THE METHOD SECTION with the population median of each
  term**, so a reader can redo the ordering by hand and dispute it term by term,
  which is what SD-CTR-21 asks of this column.

**A WORKED EXAMPLE, BUILT FROM THIS SKILL'S OWN SCORING TERMS.** The file is
invented and so is the business: a chain of neighbourhood bakeries, ranking on
monthly retail units, with a regional manager one level up the chain. The row
sits at rank 4:

> `Measure at the 93rd percentile of your scope, 4,180 units; commitment date 11
> days after this window opens, which is the near band; two build items, both
> typed as growth work; named on your regional manager's list of 14 March; one
> gap term open on the seasonal range; workload of 3 open items, under the cap.`

Read that back against 12.1 and every clause is a NAMED TERM of the formula, in
the order it contributed:

| Clause in the string | The term it names |
|---|---|
| the 93rd percentile and the figure behind it | the measure and its percentile from 11.5, applied to the score exactly once per 12.12 |
| 11 days after this window opens, the near band | the close weight from 12.3, banded by the vocabulary of 12.3.1 |
| two build items, typed as growth work | the work-type weight from 12.5 |
| named on your regional manager's list | the supervisor scope boost of 12.6, with the source boost and chain distance of 12.7 behind it |
| where a level of the chain carried its own weight | the standing hierarchy weight of 12.8, named only where it moved the row |
| one gap term open on the seasonal range | a gap term from 12.10 |
| workload of 3 open items, under the cap | the workload term from 12.11 |

Where a steer was in force per PART 13, the steer term is named in the same way
and in its own contribution position. Where the zero bucket or a percentile floor
placed the row, the string says that instead, because that is what decided it.

**THE REASON COLUMN IS NOT THE NARRATIVE COLUMN, DOES NOT REPLACE IT, AND BOTH
SHIP ON EVERY ITEM SECTION.** HDR_NARRATIVE says what to DO about the unit and
carries the three per-row facts 1.3b requires of it. HDR_RANK_REASON says WHY THE
UNIT IS HERE. They are different columns with different headers in different
places: the reason sits immediately after the identity columns, and the narrative is last and widest
per reference/output-contract.md element 11. A section carrying one and calling it the
other has failed R1 of PART 7.2, and so has a section that folds the reason into
the narrative, because a reader who wants to interrogate the ORDERING cannot
filter or sort on a paragraph that is also carrying instructions.

## 1.3b The section-specific block

After the identity block, each section family carries its OWN columns, in a
fixed order, with byte-identical headers from the HDR_ variables. The families
and their standing columns:

| Family | Columns after the identity block |
|---|---|
| identity_and_rank (the action lists) | HDR_COMMITMENT_DATE, HDR_CLOSE_STATE, HDR_CLOSE_WEIGHT, HDR_MEASURE, HDR_MEASURE_PCTILE, HDR_SCORE, HDR_MUST_CLOSE, HDR_ENTITY_FOCUS, HDR_ACTION, HDR_NARRATIVE |
| reference (the reference list) | the same set, in the same order, so a unit reads identically wherever it appears |
| direction (the priorities section) | HDR_DIRECTED_BY as the source and sender, HDR_DIRECTED_DATE, HDR_INSTRUCTION quoted verbatim, HDR_DIRECTIVE_STATUS holding what became of the direction, taken from the CLOSED SET OF FOUR VALUES SECTION A1 states for that variable and never from a string this file writes. **This family carries NO UNIT identity block**, because its rows are directions and not units. It DOES carry the two columns PART 4.1 requires of a reference table, HDR_POSITION as its one identity column and HDR_RANK_REASON immediately after it, per 1.2.2. |
| mandatory (the directed section) | HDR_DIRECTED_BY, HDR_DIRECTED_DATE, HDR_INSTRUCTION, HDR_COMMITMENT_DATE, HDR_CLOSE_STATE, HDR_CLOSE_WEIGHT, HDR_MEASURE, HDR_SCORE. The trailing rule below supplies the rest and this row never restates it |
| derived (the breadth section) | HDR_ITEM_COUNT, HDR_PEER_NORM, HDR_ITEM_GAP, HDR_EST_UPSIDE, HDR_PLAY |
| exception | HDR_PRIORITY_BAND holding the BAND LABEL from PRIORITY_BAND_LABELS, then HDR_FLAGS, HDR_LAST_ENGAGEMENT, HDR_DAYS_SINCE. Its position column is HDR_POSITION and is an identity column, not a section-specific one |
| panel | label column and prose column only; see SD-FMT-11 |

**HDR_RANK_REASON IS NOT IN THIS TABLE, BECAUSE ITS POSITION IS FIXED BY THE
CONTRACT AND IS NOT A SECTION-SPECIFIC CHOICE.** It is the FIRST COLUMN AFTER the
identity columns on every family that carries them, in the position 1.3 cites from
reference/output-contract.md 4.1.1, and it is outside the frozen span on every one of them.
It is not itself an identity column and is not a member of
IDENTITY_BLOCK_COLUMNS. What it SAYS, however,
depends entirely on what ordered the section, and three of these families are not
ordered on merit at all:

| Family | The position column, and what it is headed | What HDR_RANK_REASON carries there |
|---|---|---|
| identity_and_rank, the two action lists | HDR_RANK, a merit rank | The scoring terms of 12.1 that decided the position, in contribution order, in the standing form 1.3 gives |
| reference | HDR_RANK, the same merit rank resumed | The same, so a unit reads identically wherever it appears |
| mandatory, the directed section | HDR_POSITION. This section is NOT a merit tier: its rows are named by a directive, are ranked 1 to N among themselves and never consume a merit rank, per 1.7 and reference/output-contract.md PART 4.2 | The DIRECTIVE that put the unit here, which is why it sits there: the sender, the date, and the clause naming the unit quoted as the sender wrote it per SD-LNG-07. Then the key that settled its place among the other directed rows |
| derived, the breadth section | HDR_POSITION, because BREADTH_SORT_KEYS order this section by estimated value and never by merit or by the classification label, per 15.7 and SD-RNK-11 | The sort keys of 15.7 that placed the row, in their own order: the estimated value with its arithmetic, then the measure, then the play PLAY_RULES assigned it and which rule matched first |
| exception | HDR_POSITION, because membership is by flag and the order is flag weight, per SD-WGT-20. The BAND LABEL itself is a separate column, HDR_PRIORITY_BAND, in the section-specific block | The FLAGS that produced the band: each flag that tripped with the weight it carried, largest first, then the measure multiplier of 16.3 and the band it landed in. A flag that did NOT trip is never named, and the raw count is never given in place of the weights, per SD-EXC-09 |
| direction, the priorities section | HDR_POSITION, holding the direction's place in the order 1.2.2 states. R1 RUNS on it, because PART 2.0 makes it a REFERENCE TABLE and PART 4.1 admits no reference table without both columns | The keys of 1.2.2 that placed the direction, in their own order: the source band, the chain distance with the namer named, the date, and the sender identifier only where it was the key that settled the position |
| panel | none, and R1 does not apply | Nothing. A PANEL SHEET has no header row and no grid of units, so elements 1 to 6 and 8 to 14, R1 and R2 are NOT APPLICABLE on it with the sheet class as the stated reason, per 1.2.1 and PART 2.0. **ELEMENT 7 IS NOT AMONG THEM AND DOES REACH IT**, because its scope is every populated cell of the SHEET'S USED RANGE, per PART 7.2 row 7. **R3 and R5 still reach it**, per PART 7.2: R3 wherever a panel is itself capped, R5 because it scans the whole workbook. This is the ONLY family exempt from R1 |

**A position column is HEADED FOR WHAT IT IS.** reference/output-contract.md PART 4.1 says
a section ordered by something other than merit and headed `Rank` is a contract
violation, and the three substitutions above are that rule applied to the three
sections of this artifact whose order is not the merit order. The substitution
changes the HEADER STRING in that slot and changes nothing else: the column still
sits first, the identity block still has the same shape on every section, and
SD-CTR-08 is satisfied by relative order rather than by a shared header string.

**AND THE SUBSTITUTE IS HDR_POSITION, NEVER HDR_PRIORITY_BAND.** PART 4.1 states
it in those words: `HDR_PRIORITY_BAND` heads the exception BAND LABEL column,
whose values are the members of PRIORITY_BAND_LABELS, and heading a column of
integers with it is as much a contract violation as heading a non-merit order
`Rank`, because a reader who has met that word as a band label elsewhere in the
artifact reads 1, 2, 3 as the band names. An earlier revision of this file headed
all three non-merit sections with the band-label variable, so the directed and
breadth sections carried a column of integers under a band name and the exception
section carried its position and its band under ONE header. `HDR_POSITION` exists
for exactly this slot, is a numeric column and is right aligned by the membership
rule; `HDR_PRIORITY_BAND` is a category column and is left aligned. The two name
two different things and neither substitutes for the other. **On the exception
section BOTH ship**: HDR_POSITION first, in the identity block, holding the
position in the flag-weight order, and HDR_PRIORITY_BAND in the section-specific
block, holding the band label 16.3 assigned.

Three rules bind this block:

1. The headers are byte-identical between runs. SD-CTR-09. **Every column in
   every family is a named HDR_ variable, with no exceptions.** A column described
   in prose rather than named by a variable has no byte-identity guarantee, so a
   reader must invent its header string and two runs can differ. The direction
   family's fourth column was described that way and is now HDR_DIRECTIVE_STATUS.
2. HDR_SCORE is present on every item section, to SCORE_DECIMAL_PLACES, and is
   never omitted. SD-CTR-10, and 26.1.
3. A column whose source does not resolve is written BLANK with its header
   present. SD-CTR-13. Dropping it is a contract violation.

**THE TWO UNIVERSAL COLUMNS ARE NOT REPEATED IN EVERY ROW OF THE TABLE, AND WHERE
A ROW OMITS ONE THE UNIVERSAL RULE GOVERNS AND THE ROW IS THE DEFECT.**
HDR_MEASURE ships on every item section and HDR_SCORE ships on every item section,
both without exception and both stated in their own paragraphs below. A family row
that does not NAME them still carries them: they ship at the END of that family's
section-specific block, HDR_MEASURE then HDR_SCORE, immediately before the
trailing order stated further down. That is a stated, deterministic position, so
two implementers building one family off one contract build the same columns in
the same places. The identity_and_rank, reference and mandatory rows name both
explicitly and take their own stated positions instead; the derived and exception
rows do not name them and take the rule in this paragraph.

**THE UNIT IDENTITY BLOCK IS CARRIED BY THE FAMILIES WHOSE ROWS ARE UNITS, AND BY
NO OTHER.** SD-CTR-08 says the identity block is structurally identical on every
ITEM section, and an item section is one whose rows are units of business. The
families whose rows are units are identity_and_rank, reference, mandatory,
derived and exception. The families whose rows are NOT units are `panel`, whose
rows are labels and prose, and `direction`, whose rows are DIRECTIONS: a source,
a sender, a date and a quoted instruction.

**THAT IS A STATEMENT ABOUT THE UNIT COLUMNS AND NOT ABOUT THE POSITION PAIR.**
The `direction` family carries no unit identifier, no unit name, no address, no
measure and no percentile, and it never has. It DOES carry HDR_POSITION and
HDR_RANK_REASON, because PART 2.0 makes it a REFERENCE TABLE and PART 4.1 requires
both columns of every reference table, per 1.2.2. Two columns saying where a
direction sits and why are not a unit identity block and do not make its rows into
units.

Assigning the priorities section to the `reference` family was a structural
error, and it was wrong whatever the data said. Taken literally with SD-CTR-13 it
required a section of quoted instructions to carry a unit identifier, a unit
name, an address, a measure, a percentile, a score and a workload count, every
one of them blank on every row, because a direction has no unit identifier. That
is a section that cannot be built correctly, so an implementer either ships a
wall of blank unit columns or silently deviates. The `direction` family exists so
neither is necessary.

Where a direction NAMES units, those units appear on the mandatory section, which
IS an item section and does carry the identity block. The priorities section
records the direction; the directed section records the units. That separation is
also what lets a direction that matched no unit still be published, with a blank
identifier and its wording quoted, per SD-PRI-16.

**HDR_MEASURE SHIPS ON EVERY ITEM SECTION, AND IT IS NOT OPTIONAL.** The measure
is the value the ranking is built on, and a ranked list that shows a percentile
of a number it never prints asks the reader to trust an ordering they cannot
check. RIGHT_ALIGN_COLUMNS already names the measure as a right-aligned column
and HDR_MEASURE exists for exactly this purpose; an earlier revision of this
table omitted it, which left two competent readers building different column sets
off one contract. It is written as the source carries it, not rounded, because
rounding a measure changes the number the ranking is defended by; the unit is
named once on the front panel from MEASURE_UNIT_TOKENS rather than repeated in
every cell.

**THE COMMITMENT DATE SHIPS AS ITS OWN NAMED COLUMN, IN BOTH CASES.** The date
the plan is built on is HDR_COMMITMENT_DATE. It sits FIRST in the
section-specific block of the identity_and_rank and reference families,
immediately after the identity block and immediately before HDR_MEASURE, and on
the mandatory family it sits in the section-specific block, ahead of the trailing order stated above, beside the thing the
reader is being asked to do about it. This is general and it is not about any one
industry: whatever a commitment date is called at a given organization, a
renewal, an expiry, a term end, a review due date, a permit lapse or a published
due date on a work item, it is the axis this method builds the plan on.

The reason is the scoring rule itself. 12.2 rule 1 and rule 1b make the date the
FIRST and sufficient input to the close weight, and SD-SCO-01 forbids ordering on
activity count instead. A ranked list whose ordering is decided by a date that
appears nowhere on the row except as a clause inside a narrative cell asks the
reader to trust an ordering they cannot check, which is exactly the defect that
put HDR_MEASURE on every item section. The date and the measure are the two
numbers the ordering is defended by, and both are printed.

**What the cell holds: the date the ROW'S CLOSE WEIGHT WAS TAKEN FROM. Three
cases, and they are the three rules of 12.2:**

| Case | What the cell holds |
|---|---|
| Rule 1, a work item carrying a published due date | That due date, written as a date |
| Rule 1b, a unit-level commitment date, per 12.2.1 | The unit's own commitment date, written as a date. The row is still NAMED AS IMPLICIT and still counted separately in the rule-split report, per 12.2.1 and SD-LNG-04 |
| Rule 2, a period token resolved through the operating window | The resolved window's label, written as text, with the Method section naming the token it was resolved from and the window it resolved to |

Where the row is state 9 of 12.3.1, `no_derivable_date`, the cell is written BLANK
with its header present, per SD-CTR-13, and the row still carries that state's
wording from CLOSE_STATE_VOCABULARY. A blank cell here is a true statement that no date could be derived, and
it is the same statement the score already makes by dropping that row from
scoring. The column is never dropped because some rows are blank.

Where more than one dated work item sits on a unit, the cell holds the date of
the item that SET the close weight, which is the highest-weighted scoring item on
that row per 12.3, ties broken by the earliest date and then by the item
identifier ascending, so two runs on one file agree. Every other item is
unaffected and still counted wherever it is counted; the column reports which
date the ordering used, not how many dates exist.

**The column does NOT replace the row wording the state carries and does not repeat it.**
The date alone does not say whether it falls before the planned window opens or
beyond the near horizon, and the wording alone is not a sortable, filterable date
in a cell. Column and wording are the fact and its meaning, and the artifact
carries both.

**The header string.** HDR_COMMITMENT_DATE is a GROUP 24 variable like every
other header, requested from the binding owner at the same point of need, per
PART 22 decision 48, with its documented default and exact notice in SECTION A1.
Where that default is unbound it is corrected under 1.3e to the resolved source
column's own name, so the artifact heads the column with the organization's own
word for the date rather than one this method chose, per SD-LNG-07, and the
correction is disclosed with the string it replaced.

**THE SCHEMA NOW CARRIES ALL THREE, AND THE LOCAL DECLARATION IS RETIRED.**
GROUP 24 defines HDR_COMMITMENT_DATE, HDR_CLOSE_STATE and HDR_CLOSE_WEIGHT, and
SECTION A1 holds each one's documented default and exact degradation notice. This
skill reads all three from there, exactly as it reads every other header string,
and the table that used to stand here declaring them locally is DELETED rather
than kept alongside, because two documented defaults for one variable is the
defect it would have become: a binding owner reading A1 and an implementer reading
this file would ship different headers off one configuration. Where a default of
theirs fails the header test, the correction runs through 1.3e like every other
correction, disclosed and raised as one open request, and never as a second
declaration. The open requests these three were raised as are CLOSED, and the
Method section records that they were adopted.

**Every column in every family is a named HDR_ variable, INCLUDING the
span-of-control columns.** Those are headed by HDR_SPAN_PREFIX plus the
SCOPE_LEVELS display name of the level the column carries plus HDR_SPAN_SUFFIX,
which is one derivation rather than one variable per level, so a hierarchy of any
depth needs no new bindings and the byte-identity guarantee of SD-CTR-09 reaches
the span block too. Before those two variables existed the span headers took the
source file's own text, and their stability rested on nobody renaming a column.

**THE CLOSE STATE AND ITS WEIGHT SHIP AS COLUMNS, SO THE ORDERING EXPLAINS
ITSELF ON SIGHT.** HDR_CLOSE_STATE and HDR_CLOSE_WEIGHT sit immediately after
HDR_COMMITMENT_DATE on every family that carries it, in that order.

The failure they close is not a wrong number, it is a correct number that looks
wrong. A reader opens a plan headed with one period, finds at rank five a unit
whose commitment date falls in a later period, and concludes the file is broken.
The ordering is RIGHT: 12.1 multiplies the measure percentile into the score and
12.3 BANDS the date rather than filtering on it, so a large unit committing later
can outrank a small one committing sooner, deliberately. Correct and unexplained
is indistinguishable from wrong at the moment of reading, and the explanation
currently sits in a sentence the reader has to go and find, in a cell, several
columns away. The row already knows both facts. PRINT THEM.

- **HDR_CLOSE_STATE** carries the SHORT LABEL for that row's state, looked up in
  CLOSE_STATE_VOCABULARY by the state key 12.3.1 assigned, one fixed string per
  state, byte-identical between runs, so the column can be sorted and scanned.
- **HDR_CLOSE_WEIGHT** carries the weight that state contributed to the score, to
  SCORE_DECIMAL_PLACES. A reader who sees a floor weight beside a large measure
  can read the trade the score made instead of inferring it, and can see at a
  glance that the ordering is a deliberate trade rather than an error.
- **Neither column changes anything.** They print values the score has already
  used. No weight, rank, membership, count or cap moves because they are
  published, and the two columns are never inputs to anything themselves.
- **The row wording for that state still ships**, unchanged, in the narrative
  column. The short label is for sorting and scanning; the wording is the true
  sentence about that date, including the day count on the rows that fall due
  before the plan starts. A label never replaces the wording, and nothing that was
  disclosed becomes undisclosed.

**HDR_ACTION SHIPS ON THE ACTION LISTS, THE REFERENCE LIST AND THE DIRECTED
SECTION, WHICH IS EVERY FAMILY THE TABLE ABOVE NAMES IT ON, AND WHERE NOTHING
NAMED AN ACTION IT SAYS SO.**

**THE TRAILING COLUMN ORDER IS STATED HERE AND NOWHERE ELSE, BECAUSE TWO PLACES
STATING IT IS HOW TWO READERS BUILD TWO SHAPES.** After the section-specific
block, every item section ends in exactly this order:

> the carried context block, per 1.3d; then HDR_ACTION; then HDR_NARRATIVE.

Context first because it is what the reader decides with, then what to do, then
why. 1.3d states the block's membership and its cap and defers its position to
this rule; where the two ever disagree, this rule governs and the other is the
defect. **THE FAMILY TABLE ABOVE NEVER RESTATES THIS ORDER AND MAY NOT CONTRADICT
IT.** An earlier revision of the mandatory row ended
`HDR_ACTION, HDR_SCORE, HDR_NARRATIVE`, which puts HDR_ACTION before HDR_SCORE and
so before the carried context block, and that is the one thing this rule forbids;
two competent implementers built two different directed sections off one contract,
which is the exact failure a single statement of the order exists to prevent. The
row now stops at the last column that is genuinely section-specific and lets this
rule supply the rest. A section that omits the carried context block or HDR_ACTION closes the
gap rather than leaving a blank, and the order of what remains does not change. A document called a work plan whose every
column explains a ranking and none of which names a next step is thin, and the
absence is invisible: a reader cannot tell whether the method had no action or
forgot to carry one. A named absence beats silence, which is the same standard
SD-EFF-06 and 1.3c already hold every other omission to.

**The sources, in precedence order, first that names an action wins:**

| # | Source | What is carried |
|---|---|---|
| 1 | A DIRECTIVE that names an action for this unit, matched by NAME on one of the four rungs of 8.8 | The instruction's action clause, quoted as the sender wrote it per SD-LNG-07, with the sender named. Two directives naming actions are resolved by THE DIRECTION TIE-BREAK CHAIN, stated once in 8.8.1 and cited here rather than restated, which runs chain distance, then date, then sender identifier, then position within the source document, then the document's own title |
| 1b | A DIRECTION that names an action and states a TESTABLE PREDICATE this row satisfies, matched on the fifth rung in 8.8.1 | The same action clause, quoted the same way, with the row marked PREDICATE-MATCHED rather than NAMED in its narrative. Subordinate to source 1: where a named directive supplies an action for the same row, the named one wins outright. Two predicates are resolved by the same chain, in full, per 8.8.1. It supplies an action and NOTHING ELSE: no mandatory status, no source boost, no multiplier and no movement in the ranking |
| 2 | A COMPLIANCE REQUIREMENT that names a required step | The step as the governing standard states it |
| 3 | A WORK ITEM that names the work | The item's own name, as the source carries it |

**A direction HELD BACK by the compliance gate NEVER supplies an action.** The
gate fails closed on the priorities, per 9.2, and harvesting an action out of a
held-back direction would put it back on the row through a side door. Where the
gate held a direction back, the row falls through to source 3 or to the standing
absence text, and the Method section says which direction was held and why.

**Where no source names an action, the cell carries MSG_NO_ACTION_DERIVED**,
which is a GROUP 24 message variable with its documented default and its exact
degradation notice in SECTION A1, read exactly as every other message string in
this file is read. **The string is NOT written into this file.** It used to be,
and that was the same second source of truth 1.3 and reference/output-contract.md PART 8
forbid for a header: nothing updated it and no organization could change it, so an
organization whose people read an absence text differently had no way to say so.
Its notice states the thing the cell must never be read as: that this method
DERIVED nothing for the row, not that there is nothing to do about the unit. The
SECTION then carries one line in its NOTE BAND naming
WHY, in the reader's own words, every run, per 1.6.1 and reference/output-contract.md
PART 5.3: `No action could be derived for {n}
{row|rows} on this section: {the sources that were read} were read, and {the
sources that could not be reached} could not be reached. The ranking is
unaffected, and the next step is yours.` Where every row on the section carries
an action the line is the zero sentence, `Every row on this section carries an
action, and where it came from is named in the Method section`, because a reader
who cannot see the test ran cannot tell the difference between none missing and
not checked. Where no source was reachable at all the line names that instead, in
the three-part form of PART 21. The cell is never left blank and the column is never dropped, per SD-CTR-13.

**AN ACTION IS NEVER INVENTED.** SD-CNF-06, in full: where no evidence
correlates to an action, RETRY ONCE over a widened source set, which here means
the next step outward on the supervisor chain and the next window back on the
directive sweep, then proceed WITHOUT the clause and route the gap to an OPEN
QUESTION recorded in the Method section beside the other open questions. The
result ships without an action and says so; a plausible next step written by this
method is a fabrication carrying a work plan's authority. The column
NEVER enters the score, NEVER confers membership on any section, NEVER reorders
anything and is never read back as evidence of anything. SD-EXC-22. Where the
action text exceeds the field budget the compression order of SD-LNG-10 applies
and the full text is carried verbatim in the Method section, per SD-LNG-11.

**THE NARRATIVE VARIES BY CONSTRUCTION, OR IT IS A NOTE RATHER THAN A COLUMN.**
A column repeating the same two sentences on every row carries no information per
row: it costs the width of a paragraph and tells the reader nothing they could not
have learned once. HDR_NARRATIVE therefore NAMES THE ROW'S OWN FACTS, and at
minimum three of them, every one of which varies between rows by construction:

1. The row's exact close-date wording, from the CLOSE_STATE_VOCABULARY entry for
   the state key 12.3.1 assigned, which carries its own date and, in state 6, its
   own day count.
2. The row's own measure figure, written as the source carries it, with the
   endpoint phrasing of SD-LNG-12 where it sits at either end of the scale.
3. The row's own position: its rank, and the term that moved it there, named from
   12.1 rather than described in general terms.

Where the flags, the gap terms, the steer or a directive contributed, the
narrative names which one and what it did, per SD-LNG-05 and 12.1. Where two rows
would still carry identical narrative text after that, the cause is that their
facts are identical, which is a finding about the data and is reported under the
uniform-column rule below rather than hidden.

**A MANDATORY COLUMN THAT SAYS THE SAME THING ON EVERY ROW IS REPORTED ONCE,
PROMINENTLY, AND IT STILL SHIPS.** SD-FMT-21. The column is never dropped, never
blanked and never narrowed: 1.3c's removal test cannot reach it, per the ordering
in 1.3c. What changes is that the artifact SAYS SO, at the top, instead of leaving
the reader to infer it from forty identical cells:

- **The test is run TWICE, on two populations, and either one firing ships the
  line.** First over the FULL RANKED POPULATION, computed once. Then over EACH
  RENDERED SECTION independently, because the columns are rendered PER SECTION and
  a reader works a section rather than a population.
- **WHY THE SECOND READING IS NOT OPTIONAL, and it is a measured failure rather
  than a hypothetical.** A reader whose directed section carries four real actions
  quoted from a directive and whose forty merit rows all carry the standing
  absence text has a column that is NOT uniform over the ranked population, so the
  first test does not fire and no line ships. On the two sections that reader
  actually works, forty of forty cells say the same thing. The prominent
  disclosure the rule exists to force went missing on exactly the artifact that
  needed it, while an artifact whose population happened to be uniform end to end
  carried it. The population test alone is the wrong axis.
- The finding ships in the front panel, per 19.3.1 block 1, naming the
  column, what every row says, WHY it says it, WHICH SECTIONS it is uniform on,
  and what would have to be bound or supplied for the column to carry per-row
  information. Where the column is uniform over the whole ranked population the
  line says so instead of listing every section, because naming all of them is the
  same fact said longer. **The FORM of the line, at zero columns, at one and at
  many, and with the section list variable in each, is given once in 19.3.1 block 1
  item 7 and is not composed here.** The action column's own wording is there too.
- **THE TWO AXES COMBINE, AND THE SHAPE OF THE LINE IS DECIDED IN ONE PLACE.** This
  rule reads per COLUMN and names the sections; 19.3.1 block 1's seventh line reads
  per LINE and names the columns together rather than multiplying. Two uniform
  columns over three sections therefore has no form unless one place composes both,
  and block 1 is a CLOSED enumeration that a line is never invented into. **19.3.1
  block 1 item 7 is that place**, it carries the composed form with both lists
  variable, and this section defers to it rather than stating a second shape.
- The Method section carries the full entry: the column, the constant value, the
  sources read and the sources that could not be reached, the bindings that would
  fill it with their owner and contact, and the count of rows.
- The cells still carry the value. A reader scanning one row must still be able to
  read what that row says without cross-referencing the front panel, and blanking
  the cells would break the guarantee in 1.9 that HDR_ACTION is never blank.

**A uniform mandatory column is a FINDING ABOUT THE DATA, not a defect in the
column.** A reader learning that no source in their file supplied an action, or
that every unit got the same instruction, has learned something real about their
run. Deleting the column hides it, and repeating it silently forty times buries
it; naming it once at the top is what makes it usable.

**HDR_RANK AND HDR_SCOPE_RANK: BOTH SHIP WHERE THEY DIFFER ON ANY ROW; ONE SHIPS
WHERE THEY ARE IDENTICAL ON EVERY ROW.** Two columns of identical numbers side by
side read as a broken export, and a reader who distrusts the export distrusts the
ranking it carries. The decision is made by a test, not by taste.

**THE RANK-COINCIDENCE TEST, computed ONCE over the full ranked population,
exactly as 1.3c's test and the span-of-control column set are:** the two columns
COINCIDE when the within-scope rank equals the overall rank on EVERY row of the
ranked population. It is a row-by-row equality on the values actually built,
never an inference from how the scope was described, so a run where a coarser
unit of business, a directed set or a multi-scope request makes them differ on
even one row keeps both columns.

- Where they DIFFER on any row, BOTH columns ship, in their standing order, with
  their standing headers. Nothing changes and nothing is merged.
- Where they COINCIDE on every row, ONE column ships. The survivor is HDR_RANK,
  byte-identical, never a merged or invented header string, and the column that
  stands down is the one carrying SCOPE_RANK_HEADER.
- The decision is made ONCE and applied IDENTICALLY to every item section, so the
  identity block remains structurally identical across the artifact, per SD-CTR-08
  and SD-SPN-03. One computation, one column set.
- NEITHER column is ever dropped where they differ, and the two are never dropped
  at once. A rank column always ships. SD-CTR-10, and 26.1.
- The exception section is unaffected, because its position column is
  HDR_POSITION and not a merit rank at all, and that substitution covers the
  within-scope rank for the same reason it covers the overall rank: on a section
  ordered by flag weight rather than by merit, neither rank would mean what the
  same header means elsewhere. **The directed section and the breadth section are
  unaffected for the same reason and by the same substitution**, per the family
  table above: neither is ordered on merit, so neither carries a merit rank for
  the coincidence test to compare, and the test is run over the merit sections
  alone.
- HDR_RANK_REASON is NEVER stood down by this test, on any section. It is not a
  duplicate of anything: no other column on the row says why the row is where it
  is. reference/output-contract.md PART 4.1 makes it mandatory and PART 8 forbids emitting
  an item section without it.

**The disclosure, and it is MORE than the duplicate column carried.** The Method
section states in one line, every run, which way the test went, on what evidence,
and which column shipped: `Rank and Scope rank held the same value on all {N}
{row|rows} of this run, because the ranked population is exactly the scope you
asked for, so one column shipped, headed {HDR_RANK}`, or `Rank and Scope rank
differed on {k} of {N} {row|rows}, so both columns shipped`. The front panel's column glossary
names the surviving column and says in the reader's own words that it is both
the rank in the whole list and the rank inside their scope. A reader comparing two
runs can therefore see WHY a column is present in one and absent in the other,
which is the same standard 1.3c is held to.

**This is NOT the degenerate-constant test of 1.3c, and neither test licenses the
other.** 1.3c removes a column whose every cell holds one NOT-RESOLVED MARKER,
and it is forbidden from ever touching a rank column; that prohibition stands
unchanged. This test stands down a column whose every cell holds a TRUE VALUE
that another shipped column already holds, and it is the ONLY rule in this file
that may stand a rank column down.

THREE families replace HDR_RANK with HDR_POSITION, and they are exactly the
three whose order is not the merit order: the EXCEPTION section, whose membership
is by flag and whose order is flag weight; the DIRECTED section, whose rows are
named by a directive and ranked among themselves outside the merit tiers; and the
BREADTH section, which BREADTH_SORT_KEYS order by estimated value. A rank column
on a section whose order is not the merit order would mean something different
from the same header elsewhere, which is what reference/output-contract.md PART 4.1 forbids
when it requires a position column to be headed for what it is. On all three the
reason column still ships and still says why the unit sits there, in the words
the family table above gives it. SD-WGT-20, SD-FMT-24.

### 1.3c A column that says the same nothing on every row does not ship

SD-CTR-13 says a column whose SOURCE DID NOT RESOLVE is written blank with its
header present, and that rule is untouched: a blank cell under a present header
is a true statement that the source held nothing there, and the reader can see
the shape of what was attempted.

A DIFFERENT case is not covered by it and must not be resolved by it. A column
can resolve, build without error, and carry an IDENTICAL NOT-RESOLVED MARKER on
every row, because the binding that would populate it is unbound. It is correct
under every rule in this file and it reads as a bug to the person holding it, and
a column that says the same nothing on every row costs width, costs trust, and
tells the reader less than one sentence would.

**THE CASE THAT MOTIVATED THIS RULE IS NO LONGER GOVERNED BY IT, AND SAYING SO
MATTERS MORE THAN KEEPING THE EXAMPLE.** The rule was written from an
entity-focus column carrying the same unmapped marker on every row of a real
artifact. That column is in the mandatory set, so under SD-FMT-21's ordering it
is resolved before this test is reached and it now SHIPS, with the finding stated
in one line instead. That is the correct outcome: a mandatory column is part of
the shape a reader learns once, and dropping it to spare them a repeated marker
trades a permanent inconsistency for a temporary tidiness. An example that
contradicts the rule it illustrates is worse than no example, so the eligible
case is stated instead.

**The eligible worked case.** A carried-context or optional derived column that
resolved, is NOT in the mandatory set, and carries this method's own
not-resolved marker on every row because the binding behind it is unbound. It has
no fixed place in the reader's mental model of the section, nothing downstream
requires its presence, and its whole content is one fact that a sentence states
better. That column is omitted and its information is moved, per below.

**THE DEGENERATE-CONSTANT TEST.** A column is DEGENERATE-CONSTANT when ALL THREE
hold, and it is tested once, over the full ranked population, exactly as the
span-of-control column set is:

1. Every populated cell in the column holds the SAME value.
2. That value is a NOT-RESOLVED MARKER produced by this method, not a value read
   from the source. A constant read from the SOURCE is a fact about the business
   and it SHIPS: a population genuinely all in one entity is information.
3. The marker is constant because a BINDING is unbound or a taxonomy resolved
   nothing, rather than because the population happens to be uniform.

A degenerate-constant column is OMITTED from the item sections, and its
information is not lost, it is MOVED and made larger:

- The FRONT PANEL carries one line naming the column, the constant marker it
  would have carried, and the binding that would populate it.
- The METHOD section carries the full entry: the column, the marker, the binding
  by NAME, its exact degradation notice from reference/schema/ SECTION A1 or A2, what it
  would have changed, and the addressee in the form MSG_AUTHOR_LINE gives it:
  BINDING_OWNER_NAME with BINDING_OWNER_CONTACT where an address is bound, and
  BINDING_OWNER_NAME with the plain statement that no address is recorded where
  one is not. BINDING_OWNER_CONTACT is DEFERRED rather than IGNITION, so an
  unbound address is an ordinary disclosed gap and never a blank in the middle of
  a sentence.
- The omission itself is stated, so a reader comparing two runs can see why a
  column is present in one and absent in the other.

**This is strictly MORE disclosure than the dead column**, which is the test any
change of this kind has to pass. A column of forty-six identical markers tells
the reader that something is unmapped; the two entries above tell them WHICH
binding, WHAT it would have changed and WHO can set it. Nothing that must be
disclosed becomes undisclosed. SD-EFF-08 still holds: the unresolved item
propagates to the audit and nothing quietly disappears.

**THE ORDERING, AND IT IS THE WHOLE OF THE PROTECTION. SD-FMT-21.** RESOLVE THE
MANDATORY SET FROM THE CONTRACT FIRST, THEN APPLY THIS TEST ONLY TO THE COLUMNS
THAT REMAIN. The mandatory set is decided by PART 1; this test is an optimisation
over what is left, and an optimisation may never delete a guarantee.

**The mandatory set is COMPUTED, never enumerated here, because an enumeration
goes stale the first time a column is added.** It is exactly:

1. Every column in IDENTITY_BLOCK_COLUMNS, plus the rank columns the coincidence
   test in 1.3b left standing.
2. Every column named in the 1.3b family table for the family being built.

That is the whole set, and it is read off the contract at build time. The failure
this ordering closes was exactly an enumeration going stale: an action column was
added to the contract by a later pass and was not added to the exemption list
here, so a column that 1.3b, 1.9 and 18.1 all declare mandatory became eligible
for deletion, and on a run where no priority source resolved every one of its
cells held the same string and the test fired. Each rule was correct read alone.

**A MANDATORY COLUMN CARRYING ONE REPEATED VALUE IS A FINDING ABOUT THE DATA,
NOT A DEFECT IN THE COLUMN.** It ships, at full width, with its header and its
cells, and ONE LINE says that every row carries the same value and why, per the
uniform-column rule in 1.3b and 19.3.1 block 1. A reader learning that every unit
got the same instruction, or that no source supplied one, has learned something
real. Deleting the column hides it.

**THIS GENERALISES TO EVERY REMOVAL RULE IN THIS FILE, PRESENT AND FUTURE.** A
column may be removed for being empty, constant, unresolved or unreached, and
none of those reaches a mandatory column. Where a mandatory column's source does
not resolve at all, SD-CTR-13 already governs and it ships with its header
present, its cells blank and the failure named. The removal rules in force here
are this one and the carried-context membership rule in 1.3d, whose rule 5 drops
an empty or degenerate candidate; both are subject to this ordering, and 1.3d's
candidates are by construction outside the mandatory set because its rule 3
excludes anything already displayed. The rank-coincidence test in 1.3b is NOT a
removal rule and is not licensed by this one: it decides WHICH of two identical
rank columns the contract declares mandatory in the first place, before this test
runs at all, which is why it appears in step 1 above rather than as an exception
to it.

Two further constraints, and they are what stop the test eating a real column
outside the mandatory set:

- A constant read from the SOURCE ships, per condition 2 of the test. Only a
  marker this method produced can make a column degenerate.
- It is computed ONCE over the full ranked population and applied IDENTICALLY to
  every item section, so the section-specific block does not differ between two
  sections of one artifact. One computation, one column set. SD-SPN-03.

### 1.3d THE CARRIED CONTEXT BLOCK. The ranking is not the product.

**The ranking plus enough context to act is the product.** A correct ordering
that withholds the two or three numbers the reader decides with is a list they
will re-sort by hand, and a ranking that gets re-sorted by hand has already lost.

At every organization there are columns that RESOLVE and are then dropped
silently, because they are not the ranking measure, not in the identity block,
not the commitment date and not an input to any scored term. They are, very
often, exactly what the reader needs to decide what to do about a row. Under the
rules as they stood, such a column appeared nowhere but a line in the audit
saying its header did not map to a scored concept, and the person holding the
plan had to go back to the source file to act on it.

This is a general failure and it is fixed generally. It is not about any one
industry, and the block never carries a named column: it carries whatever
qualifies in the file in hand, recomputed every run, per SD-IDN-06.

**Position.** Stated in 1.3b, not here, so the trailing order lives in one place:
the block sits after the section-specific block, before HDR_ACTION, and before
HDR_NARRATIVE, on every item section, in the same order on every one of them.

**Membership. A column qualifies when ALL FIVE hold:**

1. It RESOLVED, or it is an unresolved header that passed a value check well
   enough to be typed. Both are known to the parse stage. **A CLEAN TYPE IS
   SUFFICIENT HERE AND A RESOLVED CONCEPT IS NOT REQUIRED**, which is the whole
   point of the block: the columns a reader most often needs are exactly the ones
   no dictionary carries. **The column may have arrived in the ranking source or
   by the enrichment join of 10.1.1, on the same terms either way**, and where it
   arrived by join its SOURCE FILE is named beside its header in the Method
   section per 10.1.1, so a reader never wonders where a column they do not
   recognize came from. This test and 10.1.1's admission of a second file are the
   SAME TEST read from two ends, and they are stated to agree: a clean-typed
   column that would be carried from the container is a clean-typed column worth
   joining from a second file, and refusing to reach it there while carrying it
   here was a contradiction that cost a real run four gap terms and three
   exception flags.
2. It is NOT the ranking measure, NOT a member of IDENTITY_BLOCK_COLUMNS, NOT the
   unit identifier or a secondary identifier, and NOT a scope column.
3. It is NOT already displayed anywhere else on the item sections: not in the
   identity block, not in the section-specific block, and not the commitment
   date, which ships as HDR_COMMITMENT_DATE in the section-specific block per
   1.3b, in both the unit-level case and the work-item case. A column already on
   the row is a duplicate rather than context.
4. It is NOT an input to any scored term AND NOT AN INPUT TO POPULATION
   MEMBERSHIP: not a gap-term source, not an exception flag source, not the entity
   resolution, not the work-item block, **and not a source the pipeline of 11.1
   read to EXCLUDE a unit from the population.** The exclusion sources are named
   by the pipeline itself and are at least these: the not-actionable column of
   11.2 and 11.2.1, the different-operating-model class column of 11.3, and under
   FLOW the stage or open-set column of 11.9 and PART 23. **Why the population
   sources belong in this list and were missing from it.** The exclusion has
   already run by the time this block is built, so every surviving row carries the
   one value that SURVIVED it: a full-width column repeating one word on every row
   of the artifact, correct under every other rule and worth nothing to the
   reader. It is not degenerate under 1.3c either, because 1.3c's condition 2
   requires the constant to be a marker THIS METHOD produced and this one is a
   value read from the source, which 1.3c says ships. Neither rule could reach it
   and both were right. The exclusion decision it drove is already published in
   the funnel of 11.6 and in the EXCLUDED and KEPT listing of 11.2.1, which is
   where a reader learns it, so nothing is lost by leaving the column out and a
   column of width is saved. Where such a column is NOT constant over the
   surviving population, it is still excluded by this rule and the Method section
   names it with its distinct values, because a column that decided membership is
   reported as a membership decision rather than smuggled back in as context.
5. It is populated on at least one row in scope. A wholly empty column is an
   absent column and does not qualify, per SD-PRS-18, and a degenerate-constant
   column does not qualify either, per 1.3c.

**Cap: SIX columns.** Six is a standing value of this method, stated once, here.
The reason is bounded output rather than taste: six columns of context sit beside
the identity block without pushing the trailing narrative column off a reader's
screen, and a bounded set keeps the section shape stable enough that two runs on
the same source are comparable. Where more than six qualify, publish the top six
by the order below and write the showing note in the same form every capped
thing in this file uses: `carrying {n} of {m} available context {column|columns}`,
where n is the cap, per SD-RNK-06. **That note goes in the section's NOTE BAND
like every other per-sheet note, per 1.6.1 and reference/output-contract.md PART 5.3**, and
NAME the ones not carried in the Method section with their figures,
so a reader can ask for one by name. **Where SIX OR FEWER qualify, carry them all
and write no note, because there was no shortfall.** Six is the boundary and it
belongs to the second branch, not to neither: a rule reading "more than six" and
"fewer than six" leaves exactly six undecided, and exactly six is the commonest
interesting case at the cap. Where NONE qualifies, the block is absent and the
Method section says so in one line.

**Ordering, and it is defensible, deterministic and recomputed every run:**

**KEY 0, THE CLASS, AND IT IS APPLIED BEFORE EVERY OTHER KEY.** SD-BRD-07. A raw
distinct count compares two kinds of usefulness that are not comparable: a tenure
year carrying 28 distinct values outranked a line of business carrying 8, and a
year tells a reader almost nothing about what to do with a row while the line of
business tells them what kind of conversation to have. Sort into these four
classes first:

| Class | What is in it | Shape tokens |
|---|---|---|
| 1 | QUANTITIES THE READER DECIDES WITH, the per-row facts they reach for first | COUNT_OR_MEASURE, RATE_OR_PROPORTION |
| 2 | GROUPERS, which say what KIND of thing this row is, with at least 2 and at most CONTEXT_GROUPER_MAX_DISTINCT distinct values | STATUS_OR_CATEGORY, BOOLEAN_LIKE |
| 3 | DATES | DATE |
| 4 | EVERYTHING ELSE, including any column that would be a grouper but holds more distinct values than the grouper maximum, which makes it a label rather than a group | FREE_TEXT, IDENTIFIER_OR_CODE |

Then, WITHIN each class, the three existing keys unchanged and in order:

| # | Key | Direction | Why it is the right key |
|---|---|---|---|
| 1 | FILL RATE within the in-scope population | descending | A column populated on most rows can be acted on for most rows. A column populated on a handful cannot, and SD-EXC-25 already refuses to build on a thin field. |
| 2 | DISTINCT VALUE COUNT within the in-scope population | descending | Within one class this is a fair comparison: it separates a quantity that varies row by row from one that barely moves, and one grouper from another. Across classes it is not a fair comparison, which is why key 0 runs first. |
| 3 | POSITION IN THE SOURCE | ascending | Deterministic, and it is the order the business itself chose when it built the export. It is a tie-break, never a ranking argument. |

**This changes ORDER only.** No membership test changes, the cap does not change,
and nothing about the block being carried and never scored changes. PRINT THE
CLASS beside the fill rate and the distinct count for every candidate, carried and
not carried, so a reader who disagrees with the order can see which rule produced
it.

The third key makes the order a TOTAL order, so two runs on the same file carry
the same six columns in the same order, per SD-RUN-15. Print the fill rate and
the distinct count for every candidate, carried and not carried, in the Method
section, so the selection can be checked rather than trusted.

**What the block is NOT, and these are the failsafes:**

- **It NEVER enters the ranking.** No carried column contributes to the score, to
  any term inside the bracket, to the measure percentile, or to any tie-break.
  SD-WGT-19 forbids a factor entering twice and these have not entered once.
- **It NEVER confers membership.** A carried column cannot put a unit on a
  section, cannot trip a flag and cannot admit a unit to the directed set.
- **It is CARRIED, NOT SCORED, and it says so on its face.** The block is
  introduced in the front panel and again in the Method section with that phrase:
  these columns are carried from your source because they help you decide what to
  do about a row; they were not scored and they did not change the order.
  SD-EXC-22's shown-never-scored discipline is the model, and this is the same
  contract widened from a single named status to the whole class.
- **It is never interpreted.** Print the value as the source carries it. Do not
  band it, do not label it good or bad, do not infer what it implies. Where its
  meaning varies by jurisdiction, SD-EXC-23 applies unchanged: report what the
  data says, attribute it, and leave the judgment to the person who knows their
  jurisdiction.
- **It does not relax any other rule.** SD-CTR-08 still binds the identity block,
  which the carried block sits outside of. SD-CTR-09 still binds every header
  string, and a carried column's header is the SOURCE's own header text, sanitized
  on the way in per SD-PRS-30 and gated on both bounds of ALLOWED_CHARACTER_RANGE
  per SD-FMT-14. The formatting elements apply to it exactly as to any other
  column, and its alignment follows the membership rule in 1.10 from the SHAPE
  TOKEN the parse stage already established for it: a carried column whose token
  is COUNT_OR_MEASURE, RATE_OR_PROPORTION or DATE ranges right, and one whose
  token is IDENTIFIER_OR_CODE, STATUS_OR_CATEGORY, BOOLEAN_LIKE or FREE_TEXT
  ranges left. Nothing is inferred at run time, because the token was established
  before any formatting decision was taken. SD-FMT-05.

A worked example, neutral and invented: a source resolves an identifier, a
measure, two scope columns and a commitment date, and also carries a ratio
column, two count columns and a category column that map to no scored concept.
All four qualify and all four are carried. KEY 0 runs FIRST, so the ratio and the
two counts sort into class 1, quantities the reader decides with, and the category
column into class 2, groupers; only THEN do fill rate, distinct count and source
position order the columns WITHIN each class. The category column therefore sits
after all three quantities however many distinct values it holds, which is the
whole point of key 0: a raw distinct count would have compared two kinds of
usefulness that are not comparable. The reader can see at a glance which of the
rows they are being asked to work carries the ratio that makes it the hard
conversation of the period. The ordering of the plan is unchanged; what changed is
that it can be acted on without opening the source file.

### 1.3e THE HEADER SAYS WHAT THE NUMBER IS, IN WORDS THE READER USES

A header can be exactly accurate to the METHOD and actively misleading to the
READER, and when it is, the number under it is read as its opposite. The worked
case, and it is the reason this rule exists: a workload-count column headed with
an imperative, holding a count of items certain to close inside the window. On
the largest unit in a real plan it held zero, and the reader read the header as
an instruction and the zero as DO NOT WORK THIS ACCOUNT, which is the reverse of
what the row said. The count was right, the ladder was right, the ranking was
right; the header made all three into a lie at the only moment that mattered.

**THE TEST. Three questions, asked of every header in the contract. Any yes
corrects the DEFAULT:**

1. Does the header read as an INSTRUCTION where the cell holds a FACT?
2. Does the header name a DIFFERENT QUANTITY than the cell holds, or name no
   quantity at all, so the reader has to guess what the number counts?
3. Is the header THIS METHOD'S vocabulary rather than a word the reader would use
   for the same thing?

**THE SCOPE OF THE RULE, and it is the whole of it:**

- **A BOUND header string is NEVER changed.** SD-CTR-24. The organization's
  decision governs, always. Where a BOUND header fails the test, the run says so
  once in the Method section, names the question it failed, invites the binding
  owner to reconsider, and then ships the organization's string unaltered.
- **The rule applies to the DOCUMENTED DEFAULT only**, which is a fallback rather
  than an organizational decision, and it NARROWS what that fallback asserts
  rather than contradicting anything anybody bound.
- **NO CORRECTED HEADER STRING IS WRITTEN INTO THIS FILE, AND THE TABLE BELOW
  CARRIES NONE.** An earlier revision of this section wrote six replacement
  strings into its own verdict table and declared that where it and SECTION A1
  differed, this file won. That is exactly the second source of truth 1.3 forbids
  and reference/output-contract.md PART 8 forbids in the same words: a header string written
  into a skill is a second source of truth that nothing updates, a binding owner
  reading A1 and an implementer reading this file would ship different headers off
  one configuration, and which of the two won was decided by whichever document
  the reader opened. The corrections themselves were good; their HOME was wrong.
  What this section owns is the TEST, the VERDICT and the COMPOSITION RULE. What
  it does not own, and never owns, is a string.
- **A header that is TRUE but terse is KEPT.** Churning a true header costs
  comparability between two runs and buys the reader nothing. Only a header that
  fails a question moves.
- **Every correction is DISCLOSED.** The Method section names the header, the
  string shipped, the A1 string it replaced, and which question failed. The front
  panel's column glossary carries a one-line gloss for every corrected header, per
  19.3.1 block 4.
- **Every correction is also an OPEN REQUEST against GROUP 24**, recorded in the
  Method section with the other open requests, so the shared schema and this
  contract converge deliberately rather than drifting.

**THE COMPOSITION RULE, WHICH IS WHAT REPLACES THE STRINGS. It is mechanical, it
runs at build time, and it composes from what the run already resolved rather than
from anything written here.** Apply it to the DOCUMENTED DEFAULT only, and only
where the test failed:

| Question failed | What the run composes, and out of what |
|---|---|
| 1, the header reads as an INSTRUCTION where the cell holds a FACT | Replace the imperative with a NOUN PHRASE naming what the cell actually counts, built from the quantity's own subject and the basis it is counted over, both of which the scoring stage already resolved: the work-item subject for a count of items, and the operating window of 7.2 for the basis. Never a verb in the imperative mood |
| 2, the header names a DIFFERENT quantity than the cell holds, or names no quantity at all | Name the quantity, and where the quantity is OF something, name that something with the SOURCE'S OWN WORD for it, which the parse stage resolved and which is already sitting in the header of the column it was derived from. A percentile takes the resolved measure column's own name; a days-since count takes the resolved engagement column's own name; a gap takes the name of the norm it is a gap against |
| 3 ALONE, the header is THIS METHOD'S vocabulary and no source word exists for the quantity | **KEEP the documented default and GLOSS it.** There is nothing in the file to borrow, and a word this file invents to replace one A1 already carries is the second source of truth the scope rules above forbid. A quantity this method itself computed, such as the published score, is the ordinary case here |

**THE VERDICT TABLE. Every header in the contract, checked, with its verdict
recorded so a reader can see the test ran on all of them and not only on the ones
that moved. It names no default string, because SECTION A1 is where a default
string lives:**

| Header | Verdict | What happens where the header is unbound |
|---|---|---|
| HDR_MUST_CLOSE | KEPT. The A1 default now names a QUANTITY over the operating window and no longer reads as an imperative, so it passes all three | The A1 default. Where the run resolved a word for the work items themselves, A1 itself defers to the composition rule and the composition is disclosed |
| HDR_MEASURE_PCTILE | KEPT. The A1 default now names what the percentile is OF | The A1 default. Where the ranking measure resolved to a named source column, A1 itself defers to the composition rule and the composition is disclosed |
| HDR_DAYS_SINCE | KEPT. The A1 default is now shape dependent and names what the count is since, matching HDR_LAST_ENGAGEMENT | The A1 default for this population's shape. Where the engagement column resolved to a named source column, A1 itself defers to the composition rule and the composition is disclosed |
| HDR_ITEM_GAP | KEPT. The A1 default now names the comparison the gap is against | The A1 default. Where the norm is named differently in the source, A1 itself defers to the composition rule and the composition is disclosed |
| HDR_COMMITMENT_DATE | CORRECTED, fails 3, and rule 2 supplies the material anyway | The RESOLVED SOURCE COLUMN'S OWN NAME, sentence-cased, per SD-LNG-07. Where the date was DERIVED rather than read from a named column there is no source word to take, so the A1 default is kept and glossed |
| HDR_SCORE | KEPT. The A1 default now says whose score it is and what it orders, and A1 states that there is no word in the file to borrow because this method composes the number | The A1 default, glossed in the column glossary rather than replaced at run time |
| HDR_RANK, HDR_SCOPE_RANK, HDR_POSITION | KEPT, true and plain | The A1 default |
| HDR_PRIORITY_BAND | KEPT, and it heads BAND LABELS and never a position column, per 1.3b | The A1 default |
| HDR_UNIT_ID and HDR_UNIT_NAME | KEPT, and they are the organization's own noun | The A1 default |
| HDR_MEASURE | KEPT, and it is the source's own word, per SD-LNG-07 | The A1 default |
| HDR_CLOSE_STATE | KEPT, true and plain, and its VALUES are what carry the meaning | The A1 default |
| HDR_CLOSE_WEIGHT | KEPT | The A1 default |
| HDR_SPAN_PREFIX and HDR_SPAN_SUFFIX | KEPT, and the level names they wrap are the organization's own words | The A1 default |
| HDR_ACTION | KEPT, and it is already the reader's phrasing | The A1 default |
| HDR_NARRATIVE | KEPT | The A1 default |
| HDR_RANK_REASON | KEPT, and it is already the reader's question | The A1 default |
| HDR_ENTITY_FOCUS | KEPT, terse and true; glossed on the front panel | The A1 default |
| HDR_FLAGS | KEPT | The A1 default |
| HDR_LAST_ENGAGEMENT | KEPT, and it is shape dependent in A1 already | The A1 default |
| HDR_ITEM_COUNT | KEPT | The A1 default |
| HDR_PEER_NORM | KEPT | The A1 default |
| HDR_EST_UPSIDE | KEPT | The A1 default |
| HDR_PLAY | KEPT, because its VALUES are the organization's own vocabulary and renaming the column would not make them clearer; glossed on the front panel | The A1 default |
| HDR_DIRECTED_BY, HDR_DIRECTED_DATE, HDR_INSTRUCTION, HDR_DIRECTIVE_STATUS | KEPT | The A1 default |

**The corrections are all one kind of change: a header that named a quantity
badly now names it plainly, in a word the run found in the reader's own file.**
Not one cell value changes, not one weight, not one rank, and no disclosure is
lost. A reader who has two runs from either side of this change sees the same
numbers under clearer names, and the Method section names the swap on the later
one.

**EVERY COMPOSED STRING IS RAISED AS ONE OPEN REQUEST AGAINST GROUP 24**, recorded
in the Method section with the other open requests, naming the variable, the
question that drove the composition and the string this run composed. That is how
a correction reaches SECTION A1, which is where a default string belongs, instead
of being written into this file where nothing updates it.

**FIVE OF THOSE OPEN REQUESTS ARE NOW CLOSED, AND SAYING SO MATTERS AS MUCH AS
RAISING THEM.** SECTION A1 now carries corrected defaults for HDR_MUST_CLOSE,
HDR_MEASURE_PCTILE, HDR_SCORE, HDR_DAYS_SINCE and HDR_ITEM_GAP, each one naming
its quantity plainly, and HDR_DAYS_SINCE is shape dependent there for the same
reason HDR_LAST_ENGAGEMENT is. They no longer fail the test, they are no longer
routed through the composition rule, and their verdicts above are KEPT. The
Method section records that the requests were adopted, exactly as it already
records the adoption of HDR_COMMITMENT_DATE, HDR_CLOSE_STATE and HDR_CLOSE_WEIGHT.

**THE COMPOSITION RULE STAYS, AND IT IS NOT VESTIGIAL.** Each of those A1 rows
now DEFERS to it for the case where a genuine source word resolves: where the run
resolved the organization's own word for the work items, for the measure, for the
engagement column or for the norm, the header composes off that word and the
composition is disclosed, because SD-LNG-07 prefers the reader's own vocabulary to
any default. What changed is that a run with no source word to borrow now ships a
good default instead of composing one, and a run with a source word still prefers
it.

## 1.4 The span-of-control block

Show the levels BELOW the requester, never their own. A reader already knows
their own level; what they need is the level beneath it, so they know whose work
each unit is. Omit the requester's own level and everything coarser as
redundant. SD-SPN-01.

The inclusion test is mechanical, three conditions, all must hold. SD-SPN-02:

1. The scope column is strictly finer than the requester's own resolved level.
2. It carries more than one distinct value in the report population.
3. It is NOT the unit level itself.

Condition two is the empirical backstop and it settles every awkward case
without a special rule. Worked example, neutral: a mid-level owner whose unit
happens to contain exactly one finer unit gets no column for that level, and no
special rule was needed to decide that.

**CONDITION THREE, AND IT IS NOT OPTIONAL: THE UNIT LEVEL IS NEVER AN ATTRIBUTION
COLUMN.** The span block exists to say which finer things INSIDE this row the
reader owns. The unit itself IS the row, and its identifier is already in the
identity block by SD-CTR-08. For the most junior role in a ladder whose finest
scope level is the unit, which is the common shape and not an exotic one,
conditions one and two both pass and the block would restate the identifier under
a second header, reading as a second and disagreeing identity column.

**Where condition three strikes the only surviving candidate, the span block is
EMPTY, and an empty span block is a FINISHED span block.** It is not a failure,
it is not a degradation, and it carries no notice beyond one line in the Method
section naming the level that was struck and why.

Compute the column set ONCE, over the full ranked population N that supplies the
percentile, and apply it identically to every item section. One computation, one
column set, matching sections. SD-SPN-03. Compute the distinct-value count from
the FILTERED population, not the whole file, because a qualifier or a
restriction can collapse a level to one value. SD-SPN-04.

When the requester's own level cannot be resolved, include every scope column
with more than one value. Err toward more columns, never toward omitting the
block. An extra column costs a little width; a missing one costs a manager the
ability to tell whose units they are looking at. SD-SPN-05.

Position: SPAN_BLOCK_POSITION, inside the identity block, in hierarchy order
coarsest to finest, all text formatted. If SCOPE_ATTRIBUTION_IS_TREE is false,
a unit may have more than one owner at a level, and the cell holds the set
rather than a single value; when the resulting block would exceed
SPAN_BLOCK_MAX_COLUMNS, report the block as wide rather than dropping columns.

The block is for attribution, not delegation. SD-SPN-08. It tells a manager
whose units are on their list so they can route a conversation, brief by name,
and see distribution across the units beneath them.

**Filtering a manager's section to one sub-unit does NOT produce that sub-unit's
report.** SD-SPN-07. This is absolute and no part of this skill may imply
otherwise. Two independent reasons: the sections hold only the rows that were
published, and rank is relative to the population it was computed over, and
filtering does not recompute it. It answers which of MY units are in that
sub-unit, never what are that sub-unit's top units. The remedy is to run the
skill at that subordinate's scope. The caps make this structural, and widening
scope makes it sharper: on a very large file the published rows are well under
one percent of the eligible set. A manager who believes a filter equals a
subordinate's report will under-serve every unit that happens not to appear in
their published rows.

## 1.5 Two claim tiers, and what each line may say

ROLE_LADDER.claim_tier decides. A DIRECT tier person personally changed the unit
and the narrative may name unit-level results. An AGGREGATE tier person did not;
someone on their team did, and the narrative speaks in aggregates, team outcomes
and systems. Getting it wrong in either direction is fatal: a frontline person
who hides behind aggregates looks passive, and a leader who claims a single unit
looks like they do not understand their own job. SD-SPN-09.

At the aggregate tier a named unit may appear only as an ILLUSTRATION inside an
aggregate statement, with the credit staying with the team, and only when
ILLUSTRATION_RULE_ENABLED is true. Where PERSON_SECONDARY_SCOPES records a mixed
role, the two grains are claimed separately and never blended in one sentence.

Altitude: a narrative line may ladder no higher than ROLE_LADDER.altitude_ceiling
for the resolved role. Above the ceiling the wording must use a verb from
CONTRIBUTION_VERBS and must NOT use a verb from OWNERSHIP_VERBS. Enforcement is
lexical, not judgment: the gate tests the verb lists. SD-CLM-09, SD-CLM-10 as
carried into PLANNING through the narrative column.

## 1.6 Rank continuity and the caps

**reference/output-contract.md GOVERNS RANK CONTINUITY AND THE CAPS. THIS SECTION CITES IT
AND DOES NOT RESTATE IT.** Three citations carry what used to be written out
here, and each one keeps the doctrine ID that carried it so no rule is lost with
the wording:

- **RANK CONTINUITY ACROSS THE MERIT SECTIONS, AND THE DERIVED LAST MERIT RANK:**
  reference/output-contract.md PART 4.2. In this skill the merit sections are the FIRST
  ACTION SECTION, the SECOND ACTION SECTION and the REFERENCE SECTION, in that
  order, and the DIRECTED section is not one of them. A unit's rank is its
  position in the whole scope and means the same thing on every section it
  appears on. The last merit rank is DERIVED, is recomputed whenever a resize
  moves a tier size, and is never carried as a literal in this file, in a gate or
  in a message. SD-RNK-01, SD-RNK-02, SD-FMT-25.
- **THE REFERENCE SECTION'S SIZE, THE AUTHORITATIVE ROW-COUNT FORM, AND THE
  ZERO-ROW CASE:** reference/output-contract.md PART 4.3. That row-count form is
  AUTHORITATIVE wherever any statement in this file gives the size differently.
  The zero-row case ships the section with its header plus exactly one
  explanatory row from MSG_REFERENCE_SECTION_EMPTY: it is a complete and correct
  section, never a failure, and never a negative count. SD-CTR-03, SD-RNK-05.
- **THE CAP, AND THE EXACT WORDING OF THE SHOWING NOTE:** reference/output-contract.md
  PART 5.1 and PART 5.2. **PART 5.1 is why every capped section named in 1.2 is
  capped at REFERENCE_CAP INDEPENDENTLY rather than drawn from one shared budget
  across the artifact.** That matters more in this skill than anywhere else in
  the bundle, because the later sections of this artifact hold populations that
  differ by an order of magnitude off one scope: a reference list, a breadth list
  and an exception list built from the same reader's units routinely do, and one
  shared budget would silently starve whichever section was built last. The
  showing note is written in the exact form PART 5.2 gives, unchanged, with no
  word interpolated inside it. SD-FMT-25.

**THE IMPLEMENTATION MISTAKE THE ROW-COUNT FORM EXISTS TO PREVENT, WHICH IS THIS
SKILL'S OWN AND IS NOT IN THE CONTRACT.** Take
`ranked[last_action_rank : last_action_rank + REFERENCE_CAP]`, and only then
confirm the section holds the number PART 4.3 gives, before writing a row.
Slicing the ranked list AT the cap and THEN removing the action tiers yields a
short section and silently drops that tier's worth of units, which reconciles
against nothing and looks like a small scope. SD-RNK-05.

**A GATE MUST ASSERT THE NUMBER THE CONTRACT ACTUALLY PRODUCES.** SD-RNK-03. A
gate asserting a tier size where the contract produces the derived last merit
rank is testing the wrong number, and that exact error has shipped an unstyled
artifact by sending a healthy build into a retry loop that consumed the budget
the formatting pass needed. 18.1 asserts the derived figure and never a literal.

**WHICH SECTIONS ARE BOUNDED, AND WHAT N IS ON EACH: reference/output-contract.md PART
5.1.1 IS THE ONLY STATEMENT OF IT AND THIS FILE READS IT RATHER THAN DECIDING FOR
ITSELF.** 5.1.1 names exactly THREE bounds a row count can have and gives n and N
under each, and every section of this artifact is bounded by one of the first two:

| This skill's section | Its bound, per 5.1.1 | n | N |
|---|---|---|---|
| First Action List | its TIER SIZE, `tier_1_size` | rows written to it | units still eligible for it when it was filled, which is eligible_count less the ranks consumed above it, and above the first tier nothing is |
| Second Action List | its TIER SIZE, `tier_2_size` | rows written to it | eligible_count less the ranks consumed by the first tier |
| Reference List, Directed, Priorities, Breadth, Exceptions | `REFERENCE_CAP` | rows written to it | the units, or the directions, that QUALIFIED for that section before the cap was applied |
| Front Panel, Method | not bounded, so no showing note | not applicable | not applicable |

**A TIER SIZE IS A BOUND AND ITS NOTE IS NOT VACUOUS, WHICH SETTLES A
DISAGREEMENT THIS FILE USED TO CARRY.** 1.2's section table gives the action
lists' `Capped at` as their tier sizes, and an earlier reading of the contract
said the action tiers carry no separate cap; two readers read that as meaning the
tiers were not bounded at all, took N to be the tier's own row count and the
eligible population behind it respectively, and printed two different notes off one
run. 5.1.1 resolves it in one direction:
what the tiers carry no separate cap FROM is `REFERENCE_CAP`, which is not applied
to them a second time on top of their sizes, and the size itself IS a bound
because it cuts a real population down to a stated number of rows. **N on an
action tier is the population it cut, never the number it cut to**, so a tier
note whose N merely repeats that tier's own row count, while a far larger eligible
population stood behind it, is wrong and blocks at R3.

**AND CAPPED MEANS SUBJECT TO A CAP, NOT CUT BY ONE**, per PART 5.1 in those
words. A section holding 13 rows under a cap of 500 is a capped section that lost
nothing, and it carries every obligation a capped section carries, the showing
note included. Reading `capped` as `cut` is what leaves an under-filled section
with no note and leaves R3 with nothing to reconcile against.

**TWO NOTES, NOT ONE. THEY MEAN DIFFERENT THINGS BY N AND THEY MUST NOT BE
COLLAPSED INTO EACH OTHER.** SD-RNK-06. The contract owns one of them; this skill
adds the other.

| Case | n | N | Which note ships, and in whose words |
|---|---|---|---|
| CAP | rows written to the section | what 5.1.1 gives for THAT section's own bound, read from the table above | The CONTRACT'S note, in the exact form reference/output-contract.md PART 5.2 gives, written in that section's NOTE BAND per PART 5.3 and again in the Method section, the two agreeing and the agreement verified |
| SHORTFALL | rows written to the section | the section's OWN NAMED SIZE, which is its tier size or its cap | A SEPARATE note this skill adds, in different words, saying the section holds fewer rows than its size allows and naming why it does |

- **The CAP note ships on every BOUNDED section on every run, INCLUDING where
  nothing was cut and n equals N.** A showing note is the evidence the bound was
  evaluated, exactly as a zero count is the evidence a check ran. That is
  PART 5.2 and it is not conditional on a shortfall. Its name in this file stays
  CAP because that is what 1.6.1 and 18.1 call it; what it discloses is whichever
  of 5.1.1's bounds that section carries.
- **ON A SECTION THAT QUALIFIED ZERO UNITS, n AND N ARE BOTH ZERO AND THE NOTE
  STILL SHIPS.** The single explanatory row of PART 5.4 is not a unit row and is
  counted by neither, so the note reads zero of zero while the section holds one
  written row, and R3 reconciles zero against zero and passes. **A run that clears
  a mismatch there by writing one of one has told the reader a unit exists that
  does not**, which is the one outcome PART 5.4 exists to forbid.
- **The SHORTFALL note ships IF AND ONLY IF n is strictly less than N** on the
  second reading of N above. Announcing a shortfall that did not occur sends the
  reader looking for missing units that do not exist.
- **N is never the eligible pool and never the scope population**, in either
  reading, and the two notes are never merged into one sentence. A section can
  carry both at once: it was cut by the cap AND still holds fewer rows than its
  named size, and those are two different facts about the same section.

**THE ORDERING NOTE SHIPS ON EVERY RANKED SECTION, EVERY RUN, AND IT IS ONE
LINE.** It sits in that section's NOTE BAND, per 1.6.1 and reference/output-contract.md
PART 5.3, never inside the table, because element 3 puts the table object over
exactly the populated block with no blank row inside it and a grouping row would
break rank continuity as well as the table range, and never above the header row,
because element 1 forbids it. It is written in the reader's words, per 19.3.2, and
its standing form is:

> `Ordered by score, which combines {the measure's own name} with how soon the
> commitment date falls. A larger {unit noun} committing later can outrank a
> smaller one committing sooner. {k} of these {n} {row|rows} {has|have} a
> commitment date outside {the planned window, as dates}, and {j} {falls|fall}
> inside it; the {HDR_CLOSE_STATE} column says which is which.`

**EVERY TEMPLATED SENTENCE IN THIS FILE AGREES WITH ITS OWN COUNT AT ZERO, AT ONE
AND AT MANY.** SD-LNG-13. A generated line carrying a number WILL meet that number
at one, and far sooner than a template author expects: one exception, one
unresolved column, one excluded unit, one peer. A line reading "1 of them fall
inside it" tells a reader the file is machine-written and unread, at exactly the
moment they are most inclined to doubt the tool.

- **THE NOTATION, and it is used everywhere in this file:** the `{a|b}` form
  carries the singular and the plural together and selects on the count
  IMMEDIATELY GOVERNING it, singular where that count is exactly one and plural
  otherwise, INCLUDING at zero, which takes the plural in English. It applies to
  nouns and to verbs alike, `{row|rows}` and `{has|have}`, and a noun supplied by a
  binding is written `{unit singular|unit plural}` and selected the same way.
- **ZERO USUALLY GETS ITS OWN SENTENCE**, not the plural form with a nought in it.
  "0 rows were excluded" is correct and reads as a machine; "nothing was excluded"
  is the same fact in the reader's language. Every zero sentence this contract
  needs is written out beside its template, and the zero clause is NEVER dropped
  to avoid the wording: a zero is the evidence the count was made.
- **WHERE A SENTENCE CANNOT BE MADE TO AGREE, IT IS REWRITTEN TO PUT THE COUNT
  LAST**, in the form "rows excluded: 1", which agrees at every value.
- **TEST EVERY TEMPLATE AT THREE VALUES, zero, one and many, before it ships.**
  That is the whole check and it takes seconds. This binds every generated line in
  this file and in the artifact: front-panel lines, section notes, showing notes,
  empty-section rows, degradation notices and audit lines alike, whether the line
  is quoted here in full or described in prose.

**BOTH COUNTS SHIP, AND THEY ARE DIFFERENT NUMBERS WITH DIFFERENT CONSEQUENCES.**
k is how many rows ON THIS SECTION fall outside the window. j is how many rows on
this section fall INSIDE it. Neither one answers the reader's other question,
which is how many of the window's own commitments landed OFF this section, and
that one is answered once, for the whole artifact, by the commitments-in-window
line in 19.3.1 block 1. A section-level note cannot answer it, because the rows it
would have to count are not on that section.

Where k is zero the note still ships and says so, because a reader who cannot see
the test ran cannot tell the difference between none and not checked. The
directed section carries its own one-line note instead, saying that its rows were
named by a direction, are ranked among themselves and sit outside the merit
tiers, per 1.7. The note is prose in that section's NOTE BAND, changes no number
and appears in the audit as written.

**THE SECOND ACTION SECTION'S NOTE ALSO SAYS WHAT THE SECTION IS FOR, because a
reader who cannot tell why a row is on a list they are meant to work concludes
the list is padding.** Its standing second sentence, every run:

> `This is the rest of the ranked population within reach this period rather than
> a second plan: work the first list first, then pick from this one using the
> {HDR_CLOSE_STATE} column. {j} of these {n} {row|rows} {has|have} a commitment
> date inside {the planned window}.`

**AND WHERE THE ACTION SECTIONS COVER MOST OF THE POPULATION, THE ARTIFACT SAYS
SO AND ASKS THE QUESTION.** The section sizes are BOUND values, from
DELIVERABLE_LINES, and a bound value is never resized at run time: resizing one
would break the two-line contract of 1.1, every showing-note reconciliation and
every derived ceiling in 1.6 at once. At a SMALL scope those sizes cover most of
the reader's population, which is a real finding about the fit between the sizes
and this reader rather than a defect in the run, so it is disclosed and put to the
person who can change it:

- The test, computed once: the two action sections together hold more than HALF of
  eligible_count. Half is a standing value of this method, stated once, here.
- Where it fires, the second section's note carries one further sentence:
  `These two lists together cover {p} of your {N} {unit singular|unit plural}, which at this
  scope is most of what you own; what makes it a plan rather than a roster is the
  ordering, and the first list is where this period's work is.`
- Where it fires, the run also RAISES THE QUESTION ONCE with the binding owner,
  per PART 22 and the Q-N1 form in 1.1: at this scope, should the second section
  be shorter. It is asked once, the answer is recorded, and silence proceeds on
  the bound sizes unchanged.
- Nothing about the ranking, the membership or the caps moves either way. This is
  a disclosure and a question, never a resize.

This is the fix for the single most predictable objection to a correct artifact:
four of a reader's top ten committing in other periods, with the reason for it
three columns and one paragraph away. The column pair in 1.3b makes the reason
visible on the row; this note makes it visible on the section, before the reader
has read a single row.

Do not extend the action lists to absorb overflow. A long ranked list is a
roster, not a plan. SD-RNK-08.

Every sort that feeds a capped section ends with the unit identifier ascending.
Without a total order a tie straddling the cap makes the surviving set differ
between runs, which breaks the repeatability guarantee. SD-RNK-10.

Sort by the value, never by a classification label. A label tells the reader
what to do; it is an attribute, not a priority, and sorting on it inverts the
value order. SD-RNK-11.

### 1.6.1 Where a section note lives, and the order the band carries them in

**reference/output-contract.md PART 5.3 DEFINES THE NOTE BAND AND THIS FILE DOES NOT
RESTATE IT.** SD-FMT-26. One blank spacer row below the table's last row, then one
merged row per note across the table's full column span, starting in the table's
first column, left aligned, wrapped, in the body font, at the panel LABEL fill of
element 15, **carrying ELEMENT 7's BORDER ON ALL FOUR OUTER EDGES OF ITS MERGED
REGION exactly as every other populated cell of the sheet carries it**, and with
each row's height computed by PART 2.3 against the SUMMED width of the merged span
rather than against one column's width. It is outside the table range, so a sort of
the table does not reach it and element 3 is satisfied; it is below the header row,
so element 1 is untouched; it is outside the table block, so element 9's alignment
rule does not test it. **SITTING OUTSIDE THE TABLE RANGE EXEMPTS IT FROM NOTHING IN
ELEMENT 7**, whose scope is the SHEET'S USED RANGE and never the table: a band that
is populated, merged across the section's width and unbordered on every side is the
measured failure PART 5.3 and PART 7.2 row 7 were widened to catch.

**WHAT THIS FILE OWNS IS WHICH NOTES IT EMITS AND IN WHAT ORDER**, because PART 5.3
requires a stated order and does not know this skill's notes. On every section
that carries any of them, in this order, one merged row each:

| # | The note | Which sections carry it | Where it is stated |
|---|---|---|---|
| 1 | The CAP note, in the exact wording of PART 5.2, with N read from PART 5.1.1 for that section's own bound | every BOUNDED section per 5.1.1, which is every section of this artifact except the two panels, every run, including where nothing was cut and including where the section qualified nothing | 1.6 |
| 2 | The SHORTFALL note | any section where n is strictly less than its own named size | 1.6 |
| 3 | The ORDERING note | every ranked section, every run | 1.6 |
| 4 | The DIRECTED section's own note, saying its rows were named by a direction and sit outside the merit tiers | the directed section | 1.6 and 1.7 |
| 5 | The SECOND ACTION section's purpose sentence, and the coverage sentence where its test fires | the second action section | 1.6 |
| 6 | The ACTION-ABSENCE line, naming how many rows carry no derived action and why | every section carrying HDR_ACTION | 1.3b |
| 7 | The CARRIED CONTEXT showing note, where more than six columns qualified | every item section | 1.3d |
| 8 | The RECENCY MEDIAN RECONCILIATION, which is the PRIMARY location of that statement: the median that set the membership threshold, the count of rows that entered it, and the counts excluded as future-dated, as blank and as unparseable, each named separately | the exception section | 16.4 |
| 9 | The RECENCY_LAG_DISCLAIMER | the exception section | 16.4 |
| 10 | The UNEVALUATED-DIRECTION line, naming how many admitted directions could not be evaluated this run and that each is published as its own row on the section | the priorities section | 8.8.1 |

**A SECTION CARRYING NONE OF THEM HAS NO NOTE BAND, AND THAT IS NOT AN OMISSION.**
The band exists where there is a note to put in it. Every section that ships a
BOUNDED grid carries at least note 1, so in practice only a panel sheet has none,
and a panel sheet has no table for a band to sit under.

**WHAT DOES NOT GO IN THE BAND, STATED SO IT IS NOT PUT THERE BY ANALOGY.** The
EXPLANATORY ROW OF AN EMPTY SECTION is not a note and is not a band row: it is
that section's own content, it sits INSIDE the table range as the only data row,
and reference/output-contract.md PART 5.4 places, styles and counts it. SD-FMT-26 says so in
those words. That reaches one sentence this file used to route here, the exception
section's reconciliation of an empty section against a non-zero alert count in
16.4: it is written into the explanatory row, not into the band. **One sheet can
carry both**, and on an empty exception section it does: the explanatory row says
why the section is empty, and the band above still carries the showing note
reading zero of zero, the ordering note, notes 8 and 9 and nothing else. Neither
substitutes for the other, and a run that writes the explanation into the band
leaves the table degenerate and loses the style, the stripes and the filter that
every other section carries.

**THE BAND IS NEVER A SUBSTITUTE FOR THE FRONT PANEL OR THE METHOD SECTION.** The
title, the scope, the period and every caveat stay on the front panel per 19.3.1;
the showing note is still repeated in the Method section and still reconciled
against the sheet, per R3. What the band carries is the note that must sit BESIDE
THE GRID IT IS ABOUT, which is the one thing the front panel cannot do.

## 1.7 The two population figures, published separately

N is every unit in the ranked population, INCLUDING directed ones, and is what
every percentile, median and peer norm was computed over.

eligible_count is the merit remainder that sized the action sections.

Publish both. A funnel showing only one of them cannot be reconciled against the
section sizes. SD-CTR-04. Whenever a population is split for routing, both the
whole and the remainder are published.

The directed section is not a merit section and never consumes a merit slot.
Directed units are ranked among themselves, excluded from the merit sections,
and never enter eligible_count. A second action section holds its full count of
merit-ranked units whether the directive named none or named thirty.
SD-RNK-04, SD-MND-04. Otherwise a directive covering thirty units consumes a
manager's entire first tier and pushes out genuine opportunity.

## 1.8 A user-requested size overrides the role default, and nothing else moves

Honour the number the user asked for. Split it by USER_SIZE_TIER_1_FRACTION,
rounded up, to the first tier, with the remainder to the second. Keep every cap
and gate unchanged. Rename the sections for the counts they now hold. The last
merit rank becomes requested_size plus
min(REFERENCE_CAP, eligible_count minus requested_size). SD-CTR-05.

USER_SIZE_OVERRIDE_ALLOWED governs whether this is permitted at all;
PERSON_PREFERRED_LIST_SIZE is bound only when a user states a size in a request,
and is then remembered.

## 1.9 What the contract guarantees, and what the final gate checks

Every one of these is verified on every run, against the CURRENT artifact:

1. Every section in TAB_CONTRACT is present, in order.
2. Every element of reference/output-contract.md PART 2.1, which is what
   FORMATTING_ELEMENTS binds, is satisfied where applicable, PER SECTION,
   recorded as a full pass matrix in the form PART 7.2 gives. Not applicable is
   a pass and carries its reason; not applicable with no reason is not
   implemented, which is a failure.
3. The identity block is structurally identical across every item section,
   verified by header name and relative order.
4. Rank continuity holds with no cross-section duplicate identifier.
5. Every item row has a populated identity block, a populated HDR_RANK_REASON
   and a populated narrative column; HDR_MEASURE and HDR_SCORE are present with
   their headers on EVERY item section without exception, per 1.3b; and
   HDR_COMMITMENT_DATE, HDR_CLOSE_STATE, HDR_CLOSE_WEIGHT and
   HDR_ACTION are present with their headers on every section whose family
   carries them. HDR_COMMITMENT_DATE is blank only on rows where no date was
   derivable; HDR_ACTION is never blank, carrying its standing absence text
   instead, and its section carries the line saying why.
6. Identifier and postal-style columns read as TEXT.
7. Every authored character satisfies both bounds of ALLOWED_CHARACTER_RANGE.
8. Every heading, every SECTION NAME written to a tab and every COLUMN HEADER is
    Title Case, in the one convention `TITLE_CASE_HEADINGS` states. **THE EXEMPTION
    FOR TABLE COLUMN HEADERS IS WITHDRAWN.** One exemption remains and it is the
    organization's: **a string the ORGANIZATION BOUND ships in the case it was bound
    in.** A DOCUMENTED DEFAULT is not a bound string, so it is already written in
    Title Case where it is documented and this skill re-cases nothing at run time.
    Per 1.10 under SD-FMT-13.
9. Each BOUNDED section, per reference/output-contract.md PART 5.1.1 and the table in 1.6,
    reconciles against its own showing note, which sits in
    that section's NOTE BAND per 1.6.1 and reference/output-contract.md PART 5.3, and
    against the Method section's note for it.
10. SPOT_CHECK_SAMPLE_SIZE units re-read from the source match the artifact
    exactly.
11. R1 through R5 of reference/output-contract.md PART 7.2, in full, on every section
    whose rows are units: a position column in first place with a populated
    reason for that position in the FIRST COLUMN AFTER the identity columns and
    outside the frozen span, per reference/output-contract.md 4.1.1; ranks continuous across
    the merit sections with no gap, no duplicate, no restart and no
    cross-section duplicate identifier; each BOUNDED section reconciled against
    its own showing note and the Method section's note for it; the reference
    section's row count equal to the authoritative form in PART 4.3, including
    the zero-row case; and no hard-coded unit noun anywhere that disagrees with
    the bound value. **R1 also runs on the priorities section, which is a
    REFERENCE TABLE and not a panel, per 1.2.1 and 1.2.2.** The ONE family exempt
    from R1 is `panel`, whose rows are labels and prose, and the exemption is
    RECORDED with its reason, per 18.2. R2 runs on the MERIT TIERS alone, per
    PART 7.2, so the directed, breadth and exception sections are outside it and
    that exemption is recorded too.
12. The header row of every item section is ROW 1, with cell A1 holding a header
    string rather than a title, a scope, a period, a note or a banner. That is
    element 1 of reference/output-contract.md and every other element depends on it.
13. Every section's sheet CLASS is declared per reference/output-contract.md PART 2.0 and,
    where the section is ranked, its KIND per PART 4.2, both from the declaration
    in 1.2.1, both recorded on the Method section, and every NOT APPLICABLE that
    follows from a class carries the class as its stated reason.
14. Every per-sheet note sits in that section's NOTE BAND, per 1.6.1 and
    reference/output-contract.md PART 5.3: below the table, after one blank spacer row,
    merged across the table's span, with its height computed against the summed
    width of the span. No note sits above a header row, inside a table range, or
    in a single column below the table. SD-FMT-26. **The one row permitted inside
    a table range that carries no unit is the explanatory row of a section that
    qualified zero units**, placed and counted by PART 5.4, and it is present on
    every such section and on no other. SD-FMT-07.
15. The FROZEN SPAN record is present in the Method section on every run, **as ONE
    LINE FOR THE ARTIFACT and never one line per section**: the bound
    `FROZEN_SPAN_MAX_WIDTH`, the summed WIDEST-CASE built width of the frozen span,
    which section supplied the widest case for each identity column walked, and
    either the identity columns left outside the span by header name or the
    statement that the whole identity block is frozen on every section. **The walk
    ran ONCE for the artifact and the same anchor was applied BY NAME everywhere**,
    so a run carrying more than one such record, or two sections freezing different
    numbers of identity columns, fails this item. Per 1.3, SD-CTR-08 and
    reference/output-contract.md 4.1.2.
16. Every admitted direction whose predicate or attribute COULD NOT BE EVALUATED
    this run is present as its OWN ROW on the priorities section, with its status
    from the closed set and the reason beside it, and the section's note band
    carries the count. An unevaluated priority disclosed only in the Method
    section fails this item. Per 8.8.1 and reference/field-resolution.md 6.5.
17. Every direction the downward sweep of 8.4.1 returned is classified by the
    ACTOR TEST of 8.7 with a RESOLVED recipient rather than an assumed one, none
    of them carries MANDATORY_MULTIPLIER unless the resolved actor is the reader,
    and the directed section holds no row placed there by an assignment. Per 8.7
    and 8.4.1.

## 1.10 Formatting is a correctness property

**reference/output-contract.md PART 2 GOVERNS THIS SECTION IN FULL, ELEMENT BY ELEMENT, AND
THIS FILE DOES NOT RESTATE IT.** OUTPUT_MEDIUM at the planning key is xlsx, so
PART 2 applies entire and PART 3 does not. Every element is verified
PROGRAMMATICALLY against the BUILT artifact before publication, per PART 7, and a
failure BLOCKS publication. Where anything in this file appears to state one of
those elements differently, THE CONTRACT GOVERNS AND THIS FILE IS STALE.
SD-FMT-22.

**AND FORMATTING IS VERIFIED IN THE RENDERER THAT BUILT THE FILE WHILE THE READER
OPENS ANOTHER ONE, SO EVERY BAND IS HELD TO ITS DEGRADED RENDERINGS AS WELL AS TO
ITS INTENDED ONE.** SD-FMT-29. A band and the ink on it are asserted three times
per PART 2.8, the intended pairing and the two renderings in which one half of the
formatting fails to arrive, and every colour this run writes carries an explicit
OPAQUE alpha per PART 2.9. The arithmetic, the floors and the colour values live
there and in reference/schema/ and are cited here rather than restated, because a
second copy of a value is exactly how the delivered header band came to be
unreadable with a recorded pass beside it.

**WHY THIS SECTION SHRANK, SO NOBODY RESTORES THE WORDING.** It used to write out
the freeze point, the header band, the right-align rule, the row-height
arithmetic and the character gate in its own words. Every one of those is an
element standard, and reference/output-contract.md PART 8 forbids a skill from restating
one: a second copy of a standard is a second source of truth that nothing
updates, and it is precisely how the elements drifted into passing mentions and
stopped being enforced. The rules did not go anywhere. They are cited below, and
the citation is binding in exactly the way the paragraph was.

**WHAT THIS SECTION STILL OWNS, because none of it is in the contract:** the
SHAPE TOKEN of every column THIS skill emits, the rule for a carried context
column, the validation that runs when a column is added here, and the doctrine
rules that follow the tables, every one of which is this method's own. Everything
else on this page is a citation.

**THE CITATIONS, ONE LINE EACH, SO EVERY DOCTRINE ID STILL RESOLVES TO THE
STANDARD THAT NOW OWNS IT:**

| Doctrine, and the rule it carries | Now owned by |
|---|---|
| SD-FMT-01, formatting is verified rather than asserted, is never traded for speed, and an element that cannot apply to a section scores not applicable, which is a pass | reference/output-contract.md PART 2 preamble and PART 7 |
| SD-FMT-03, the freeze point is COMPUTED by reading the header row and locating IDENTITY_BLOCK_ANCHOR_COLUMN BY NAME, never a fixed cell reference, because the span-of-control block moves the column position by role; the reason-for-rank column has ONE position and is never inside the frozen span; and the span itself is BOUNDED by the summed built width of its columns | reference/output-contract.md element 2, 4.1.1 and 4.1.2, with the anchor derived by the walk 1.3 cites and `FROZEN_SPAN_MAX_WIDTH` as the bound |
| SD-FMT-04, the header band is DIRECT cell formatting on every header cell rather than left to the table style, because a lower-precedence style is not a guarantee, AND the style's OWN header band must AGREE IN DIRECTION with element 5's band rather than oppose it, so that a renderer honouring the style and a renderer honouring the direct formatting each produce a readable header | reference/output-contract.md element 5 for the direct band and element 4 for the style's own, with TABLE_STYLE_NAME's own validation in reference/schema/ rejecting a style that opposes it |
| SD-FMT-05, the alignment lists are CLOSED at run time and their membership is decided by a rule that is total over the shape tokens, with a third class, CENTRE, admitted only on a declared STATUS GRID COLUMN | reference/output-contract.md element 9 and PART 2.5, which governs CENTRING ONLY, with the shape tokens of this skill's own columns in the table below |
| SD-FMT-27, a verification never scans its own record, and one colour never carries two meanings, so a classification palette is INJECTIVE and disjoint from the alert palette | reference/output-contract.md PART 7.1 for the declared range and PART 2.6 for the classification column and its palette; the exclusion is applied at 18.2, and 1.10's second declaration below says why no such palette is in force here |
| SD-FMT-28, a grid's TOTAL width is bounded as well as each column's, the bound is declared before the columns are built and never raised to clear a failure, and what gives is a repeated standing qualifier and never a column, a header floor or a meaning | reference/output-contract.md PART 2.7 and element 10, declared and measured at 17.3 and asserted at 18.2; it is a SECOND bound and `FROZEN_SPAN_MAX_WIDTH` does not substitute for it |
| SD-FMT-29, formatting is chosen to DEGRADE SAFELY, so a text-and-band pair is asserted against the intended pairing AND against both degraded renderings, every colour is written with an explicit OPAQUE alpha, where two layers can produce one property they agree in direction, and the MECHANISM is chosen for the engine the READER opens rather than the one the file was built in, with the check reading the property back from where the reader meets it | reference/output-contract.md PART 2.8 for the arithmetic, the floors and the three assertions, PART 2.9 for the alpha form, elements 4, 5 and 15 for the direction, element 6 and element 3 for the filter mechanism and which of the two gives, and PART 7.2 rows 3, 5, 6, 7, 15 and C1 for the verification |
| SD-FMT-30, no word is ever broken by a cell line, so any string wider than its own cell is placed in a MERGED region spanning exactly what it needs rather than merely styled across it, every column is floored at the LONGEST UNBREAKABLE TOKEN it must display, and a token past the column cap is REPORTED rather than broken | reference/output-contract.md PART 2.10 for the placement rule and both assertions, PART 2.2.1 primitive 4 and PART 2.2.2 step 3b for the width floor, elements 7, 8, 10 and 15 for where each half binds, and PART 7.2 rows 7, 10 and C3 for the verification |
| SD-FMT-06, formatting is read back through the ENGINE and an unverifiable container is never published as verified | reference/output-contract.md PART 7.1 |
| SD-FMT-08, row height is COMPUTED from wrapped content against each cell's own final column width, never fixed and never left to autofit | reference/output-contract.md element 12, computed per PART 2.3 |
| SD-FMT-14, the character gate tests BOTH bounds of ALLOWED_CHARACTER_RANGE across every cell value, every sheet name, every table name and the file name, and a single violation blocks publication rather than being noted | reference/output-contract.md element 16 |
| SD-FMT-23, a header is never hidden, clipped or half-shown, because the width, the row height and the header row height are each computed from the thing being displayed rather than from something else | reference/output-contract.md elements 10, 12 and 14, computed per PART 2.2, 2.3 and 2.4 |
| SD-FMT-24, every item section carries a position column and a reason for the position | reference/output-contract.md PART 4.1, positioned by 1.3 of this file |
| SD-FMT-25, the derived last merit rank is not a row cap, and each capped section is capped independently | reference/output-contract.md PART 4.2 and PART 5.1, cited at 1.6 |

**WHERE THE ELEMENTS CANNOT BE READ BACK AT ALL, the element gate CANNOT RUN, and
an element gate that cannot run HAS FAILED**, per reference/output-contract.md PART 7.1 and
SD-EFF-03. That is a hard failure and not a skipped check, because a formatting
defect is invisible in the data and a reader has no way to notice it. The
resolution is the `shared.formatting_unverifiable` gate in 20.1.2, conditional on
DELIVERABLE_CONTAINER_REQUIRED, with the ladder in reference/capability-probe.md 2.2.
Never publish silently either way. SD-FMT-06.

Checking a subset and calling it verified IS the defect. SD-FMT-02. A build whose
action sections were fully styled and whose reference section was bare passed a
four-property check cleanly, because none of the four properties it tested was a
visual one. Test every element PER SECTION and record the matrix, which is the
matrix in reference/output-contract.md PART 7.2 and is checked at 18.2.

**CLOSED MEANS NO COLUMN IS INFERRED INTO THE LIST AT RUN TIME. IT NEVER MEANT
THE LIST IS ASSEMBLED FROM MEMORY.** The schema owns the list and states its
MEMBERSHIP RULE, which is total over the seven shape tokens and therefore decides
every column by construction, leaving none to whoever remembers:

| Shape token | Side |
|---|---|
| COUNT_OR_MEASURE | RIGHT |
| RATE_OR_PROPORTION | RIGHT |
| DATE | RIGHT |
| IDENTIFIER_OR_CODE | LEFT |
| STATUS_OR_CATEGORY | LEFT |
| BOOLEAN_LIKE | LEFT |
| FREE_TEXT | LEFT |

The rule is applied at BINDING time and the bound list is the materialised result
of it, which lives in the schema and is NOT restated here, because a list restated
outside its own table is a second source of truth that nothing updates. What this
contract owns is the SHAPE TOKEN of every column it emits, and the token decides
the side:

| Column | Shape token | Side |
|---|---|---|
| HDR_RANK, HDR_POSITION, HDR_SCOPE_RANK, HDR_SCORE, HDR_MUST_CLOSE, HDR_ITEM_COUNT, HDR_PEER_NORM, HDR_ITEM_GAP, HDR_EST_UPSIDE, HDR_CLOSE_WEIGHT | COUNT_OR_MEASURE | RIGHT |
| HDR_MEASURE, HDR_MEASURE_PCTILE | COUNT_OR_MEASURE or RATE_OR_PROPORTION, per the resolved measure | RIGHT |
| HDR_COMMITMENT_DATE, HDR_LAST_ENGAGEMENT, HDR_DIRECTED_DATE, HDR_DAYS_SINCE | DATE, and HDR_DAYS_SINCE is the count derived from one | RIGHT |
| HDR_UNIT_ID and any secondary identifier | IDENTIFIER_OR_CODE, and written as TEXT so leading zeros survive, per SD-SPN-06 | LEFT |
| HDR_UNIT_NAME, HDR_PARENT_GROUP, HDR_ENTITY_FOCUS, HDR_ADDRESS, HDR_CITY, HDR_JURISDICTION, HDR_POSTAL, the span-of-control columns | IDENTIFIER_OR_CODE, because they are names, places or codes, and the postal-style ones are written as TEXT per SD-SPN-06 | LEFT |
| HDR_CLOSE_STATE, HDR_PRIORITY_BAND, HDR_FLAGS, HDR_DIRECTIVE_STATUS, HDR_PLAY | STATUS_OR_CATEGORY | LEFT |
| HDR_RANK_REASON, HDR_NARRATIVE, HDR_ACTION, HDR_INSTRUCTION, HDR_DIRECTED_BY | FREE_TEXT | LEFT |
| A carried context column | the token the PARSE stage established for it, per 1.3d | by that token |

**A carried context column takes its side from the token the parse stage already
established, never from a guess about its header**, which is why a numeric carried
column ranges right without anything being inferred at run time.

**THIS ARTIFACT MAKES TWO DECLARATIONS, NOT ONE, BECAUSE CENTRING AND SHADING ARE
NOW DECOUPLED AND NEITHER FOLLOWS FROM THE OTHER.** reference/output-contract.md PART 2.5
governs CENTRING ONLY and admits a third alignment class on a declared STATUS GRID
COLUMN, whose third condition bounds its vocabulary's longest member by
`CENTRE_ALIGN_MAX_CHARS`. PART 2.6 separately defines a CLASSIFICATION COLUMN,
which carries a fill per state of `CLASSIFICATION_VOCABULARY` through
`CLASSIFICATION_FILLS`, **reads no length bound at all**, and is set independently
of alignment: a left-aligned column carrying a classification fill is the ordinary
case there. So the old single declaration, which took the absence of a status grid
column as the absence of a fill, no longer answers the second question and this
file answers both.

**DECLARATION 1: THIS ARTIFACT DECLARES NO STATUS GRID COLUMN, so no column of it
is CENTRED.** Every STATUS_OR_CATEGORY column this file emits fails at least one of
2.5's three conditions: HDR_CLOSE_STATE and HDR_DIRECTIVE_STATUS carry closed
published vocabularies whose members are phrases rather than codes, HDR_FLAGS
carries a list of tripped flags and not one member of a set, HDR_PLAY carries a
rule name, and HDR_PRIORITY_BAND is a band label read down a column of three values
where centring buys nothing. Every column of this artifact is therefore right
aligned or left aligned by the membership rule above.

**DECLARATION 2: THIS ARTIFACT DECLARES NO CLASSIFICATION COLUMN EITHER, and the
reason is NOT the one above and NOT a length.** 2.6 is explicit that a cell can be
far too long to centre and still be exactly the cell that most needs a fill, so
declaration 1 is not evidence for this one and must not be read as it. The reason
is that no column this file emits satisfies 2.6's condition 1, and it is a property
per column:

- **`CLASSIFICATION_VOCABULARY` IS ONE ORG-TIER BINDING SHARED ACROSS THE BUNDLE,
  AND IT BINDS STATES THAT NO COLUMN OF THIS ARTIFACT IS WRITTEN FROM.** This
  skill's closed sets live in their own taxonomy variables:
  CLOSE_STATE_VOCABULARY carries the nine states of 12.3.1 and HDR_DIRECTIVE_STATUS
  carries its own closed set. Binding the shared variable to one of those would
  rebind an organization-wide value for one column of one skill and repaint another
  skill's grid with it, which is the second-source-of-truth failure 0.5 exists to
  prevent. **The route to a fill here is a schema change that gives this skill's own
  vocabularies a fill map, not a run-time reinterpretation of a shared one**, and it
  is raised as an open request rather than taken.
- **HDR_FLAGS FAILS THE TOTALITY TEST OUTRIGHT, WHICH IS A REAL FAIL AND NOT A
  TECHNICALITY.** 2.6 requires every populated cell to resolve to EXACTLY ONE state
  by one total mechanical rule. A cell listing two tripped flags resolves to two,
  and a cell listing none resolves to none. A rule that leaves one populated cell
  unresolved is not total, so the column is not a classification column and carries
  no fill at all.
- **HDR_PLAY CARRIES A RULE NAME FROM AN OPEN SET**, so there is no closed declared
  state set to key a fill on, and a run never invents a state.
- **A CARRIED CONTEXT COLUMN NEVER CARRIES ONE**, whatever its token. Its values
  come from a source rather than from a declared vocabulary, it is CARRIED AND NOT
  SCORED under 1.3d, and shading it would give a column this method does not read a
  visual weight the reader would take as a finding.

**SO EVERY CONDITIONAL FILL ON AN ENTITY SECTION OF THIS ARTIFACT IS THE ALERT
SHADING OF ELEMENT 13 AND NOTHING ELSE.** Both declarations are recorded in the
formatting matrix at 18.2 as POSITIVE STATEMENTS rather than as absences, and
recorded SEPARATELY, because a reader of the matrix cannot otherwise tell a skill
that considered each exception from one that never met either, and cannot tell
which of the two questions was answered. Where a later revision declares either, it
declares it on the Method section and does not infer one from the other: a status
grid column is declared against 2.5's three conditions, and a classification column
against 2.6's four, with `CLASSIFICATION_VOCABULARY` and `CLASSIFICATION_FILLS`
bound for the purpose, the map INJECTIVE so no two states share one fill, the
palette disjoint from `COLOR_ALERT_WARN` and `COLOR_ALERT_OVERDUE`, and the
alert-wins precedence 2.6 requires stated once in the legend. Nothing here licenses
doing any of that at run time.

**VALIDATION, and it runs whenever a column is ADDED to this contract:** every
column this file can emit whose token is COUNT_OR_MEASURE, RATE_OR_PROPORTION or
DATE appears in the bound list, and no column whose token is IDENTIFIER_OR_CODE,
STATUS_OR_CATEGORY, BOOLEAN_LIKE or FREE_TEXT appears in it. A column added here
without that check is the defect: it is how a numeric column ends up ranged left
beside a right-ranged one, which reads as a broken export. Never add a column to
the bound list at run time on the run's own judgment, and never restyle a column
outside it; where the validation fails, it is the BINDING that is repaired, and
the run says so.

Every fixed height in this contract is a MINIMUM, never a ceiling, and computing
a height from ONE column alone is the named mistake: it produces rows correct on
average and clipped on exactly the longest, most information-dense entries, which
are the rows most worth reading. The arithmetic that avoids it is
reference/output-contract.md PART 2.3 and is not repeated here. SD-FMT-08.

State the check in a falsifiable form. SD-FMT-09. Do not write "no cell clips";
write the deterministic arithmetic test on values the engine reports, because
true clipping depends on proportional font metrics the engine does not expose
and that phrasing would make the gate unfalsifiable.

Sampling density is stated, never assumed. SD-FMT-10. Walk every populated cell
on sections of FULL_WALK_ROW_LIMIT rows or fewer. Above it apply
SAMPLING_DENSITY and record that the check was sampled and at what density.

Never put a paragraph in a narrow label column. SD-FMT-11. Labels in the first
column, prose in the second. Do not solve overflow by shrinking the font or
letting text run under the next cell.

Verify readability programmatically, not by eye. SD-FMT-12. Inspection misses
cells; a first pass on one real artifact found twenty-eight issues.

Title Case every heading, every SECTION NAME and every COLUMN HEADER, in the one
convention `TITLE_CASE_HEADINGS` states and validates. SD-FMT-13. **THE EXEMPTION FOR
TABLE COLUMN HEADERS IS WITHDRAWN**: it rested on a claim that Title-Casing them makes
a wide table harder to scan, and the method's author has overruled it after reading the
delivered workbooks. A tab and a column header are the two shortest labels in the
artifact and the two most often read side by side, which is where one convention pays
and two do not.

**THE ONE EXEMPTION THAT REMAINS, AND IT RESOLVES WHAT USED TO BE A COLLISION RATHER
THAN CARVING OUT A SECOND RULE.** `TITLE_CASE_HEADINGS` defaults true. GROUP 15 makes
every TAB_CONTRACT title variable a SHEET NAME, and a sheet name is a heading. The
collision was this: 0.5 says this skill never rewrites a string it does not own, and
SD-CTR-24 says a documented default is never contradicted, so one title variable whose
documented default was written in sentence case failed item 8 if shipped verbatim and
altered a documented default if re-cased, and nothing said which rule yielded. **THE
RESOLUTION, DECIDED IN THE SHARED LAYER AND READ HERE:**

- **A STRING THE ORGANIZATION BOUND SHIPS IN THE CASE IT WAS BOUND IN.** That is the
  exemption, and it is the whole of it. **The case of a bound string is the
  organization's decision, not this skill's**, exactly as its wording is, and re-casing
  it is the same act as rewording it: a second source of truth for one string.
- **A DOCUMENTED DEFAULT IS NOT A BOUND STRING.** It is the shared layer's own words,
  so every documented default is WRITTEN in Title Case where it is documented and this
  skill ships it verbatim. Item 8 and SD-CTR-24 then agree by construction and neither
  has to yield, because there is nothing left to re-case: the run ships a bound string
  as bound, ships a default as documented, and applies the convention only to a heading
  it composes itself.
- **THE CONVENTION IS STATED IN ONE PLACE AND IS NOT RESTATED HERE.** It is the
  validation of `TITLE_CASE_HEADINGS`, seven steps that are total over every token, so
  that this skill and the shared layer cannot produce two different strings from one
  heading.
- **NOTHING IS RE-CASED AND NOTHING IS RENAMED.** The only text change a title
  variable ever takes is GROUP 15's own deterministic truncation rule where the value
  is illegal as a sheet name, and that rename is disclosed and raised, per 1.2. Case is
  never one of those changes, in either direction.

**THE SECTION NAMES IN 1.2's TABLE ARE THE STRINGS WRITTEN TO THE TABS** and they are
written in that convention, which is why they appear there in Title Case rather than in
the sentence case an earlier revision carried.

Transliterate, never drop, and never truncate a name. SD-FMT-15. Any character
outside the permitted range is transliterated to its closest permitted
equivalent; where no reasonable equivalent exists it is dropped and the
substitution is logged. A name carrying an accent is transliterated to its base
letters: losing a name is worse than losing an accent. When quoting a source,
the WORDS are quoted exactly and the CHARACTERS are normalized; character
fidelity never outranks system compatibility. SD-FMT-16.

Sweep on the way IN, not after. SD-FMT-17, SD-PRS-30. Source contamination is
the main character risk: an export that writes a typographic minus sign produces
a sign error waiting to happen. Three entry points: source text, quoted
third-party text, and text this skill writes itself.

Character verification is mechanical, not visual. SD-FMT-18. A visual pass will
not catch a non-breaking space, a zero-width space or a byte order mark. The
gate applies to every character of text this skill authors, including strings
placed inside binary containers, and not to the raw bytes of the container
itself. SD-FMT-19.

Never drop the row and never blank the field to fix a character problem: a unit
the user cannot find is worse than an imperfect spelling. Log any value changed.
SD-FMT-20.

## 1.11 The same contract without a spreadsheet

If SPREADSHEET_WRITE is ABSENT, or if formatting cannot be verified and
DELIVERABLE_CONTAINER_REQUIRED is false, the deliverable is structured markdown
carrying IDENTICAL INFORMATION, per reference/capability-probe.md 2.1.1. Where
DELIVERABLE_CONTAINER_REQUIRED is TRUE the container is not substitutable, and an
unverifiable container is the `shared.formatting_unverifiable` gate in 20.1.2.
The choice is a NAMED BINDING, never a judgment. A different container is
not a reduced deliverable. What changes is presentation only. What does not
change: the sections, their order, the columns, the byte-identical headers, the
rank continuity, the caps, the showing notes, the published score, the
disclosures and the audit trail. Element checks that have no meaning in markdown
are recorded as not applicable, which is a pass, per SD-FMT-01.

**THE THREE NEW ELEMENTS UNDER DEGRADATION, STATED SO NOBODY SCORES A MARKDOWN
RENDERING AGAINST A SPREADSHEET AND REPORTS THREE FAILURES.** Elements 10, 12 and
14 of reference/output-contract.md are a column width, a body row height and a header row
height. A markdown rendering has none of the three: there is no column width to
set, no row height to compute, and no autofilter caret to leave room for. All
three are recorded NOT APPLICABLE **with that reason stated**, which is a pass,
per PART 7.2 and SD-FMT-01. The reason is drawn from the same closed set every
other not-applicable entry uses, and it is the second of them: the container
cannot express the element. An entry recorded not applicable with NO reason is
recorded NOT IMPLEMENTED instead, which is a failure, exactly as it is on a
spreadsheet.

**WHAT IS NOT EXCUSED: reference/output-contract.md PART 4's TWO COLUMNS, AND PART 5's
SHOWING NOTE.** The position column and HDR_RANK_REASON are INFORMATION, not
formatting. They say where a unit sits and WHY it sits there, and a reader of a
markdown table needs that answer at least as much as a reader of a workbook,
because they have no autofilter to interrogate the ordering with and no column to
sort. Both columns therefore ship in markdown, populated on every row, in the
positions 1.3 gives them, with the per-family content 1.3b gives them. R1 through
R5 of PART 7.2 are checked on the markdown exactly as they are on a workbook, and
so is the showing-note reconciliation. **A degraded container is a PRESENTATION
fallback and never an INFORMATION fallback**, which is the same sentence as the
paragraph above and is the whole point of this section. SD-FMT-24, SD-FMT-25.

The degraded run announces its degradation in the artifact, in three places:
the front panel, the Method section, and the first line of the reply. **It never
announces it as a row on an item section**, because the header row of every item
section is row 1 with nothing above it, per reference/output-contract.md element 1 and
PART 1 of this file.

---

# PART 2: THE THREE REQUEST AXES

Three independent axes compose freely, in any order and any combination.
SD-CTR-06. They change the population and the weighting. They NEVER change the
sections, the formatting elements, or the two sizes.

| Axis | What it answers | What it resolves against |
|---|---|---|
| SCOPE | Whose units | SCOPE_LEVELS and the resolved scope column |
| QUALIFIER | Which subset of those units | any other column, matched on its values |
| STEER | What to lean on | CREDITABLE_ENTITIES, or a named initiative |

A request naming all three is one request, not three. Never ask the user to
restate a multi-axis request. SD-IDN-11.

---

# PART 3: RUN START

## 3.1 Stage 0: the capability probe. Assume no tooling.

Invoke reference/capability-probe.md PART 1 once, at the start of every run, before the
first stage. It is not a stage and it has no gate; it writes one record that
every later stage reads. It is never skipped to save time, because SD-EFF-01
says run length is not a cost, and because a run that discovers halfway through
that it cannot write a workbook has already spent the budget the fallback
needed.

Two rules from that file govern everything downstream:

- C0. Probe, never assume. A capability named in the environment description but
  not probed is UNKNOWN, and unknown is treated as absent.
- C1. A degraded run announces its degradation in the OUTPUT, not only in the
  chat, which scrolls away.

The probe order, its per-capability tests, its ladders and its combination rules
are owned by that file. This skill adds nothing to them and subtracts nothing.
The one probe-time hard stop is: FILE_READ absent AND SYSTEM_OF_RECORD absent
AND no source supplied inline. Everything else degrades.

Two combination rules bite hardest here and are restated because a reader of
this file must not have to look them up:

- P2. CODE_EXECUTION absent DOMINATES. No ranked list is produced regardless of
  what else is present, because a rank computed by impression is a fabricated
  number. SD-CNF-07 and SD-SCL-03 are not negotiable. Emit the population, the
  identifiers, the resolved priorities and the qualitative sections, and say
  plainly that no ranked list could be produced because no computation was
  available.
- P3. **"No priority source resolved" is a conclusion about REACHABILITY and is
  reached only by walking the whole PRIORITY SOURCE LADDER and finding every rung
  empty.** reference/capability-probe.md P3 states that ladder and this file does not restate
  it: the mailbox where MAIL is present, the document store where DOC_STORE is
  present, then **priority documents SUPPLIED AS FILES in the input set, discovered
  by CONTENT, wherever FILE_READ is present**, and only then nothing. Rung 3 admits
  a file on three content tests, never on a filename and never on a path, and a
  candidate that fails one is READ AND RECORDED AS NOT ADMITTED with the test it
  failed named. Authority is unchanged by the rung: a direction is weighted by WHO
  issued it under PRIORITY_SOURCES and never by HOW it reached the run, so a rung-3
  document from a manager in the chain is a directive exactly as the same document
  in the mailbox would be. Where all three rungs return nothing, the ranked list
  still ships on the measure and the resolved signals alone, labelled as built with
  NO STATED PRIORITIES, and it is never labelled "no priorities this period".
  SD-PRI-04.
- P3b. **A run that had FILE_READ PRESENT and did not attempt rung 3 has
  MISLABELLED ITSELF**, whatever it printed, because the label asserts the ladder
  was walked. This skill therefore treats rung 3 as MANDATORY WORK on every run
  with FILE_READ present, exactly as 8.10 treats an attachment and 8.11 treats the
  central publication: it is attempted, its result is recorded, and where it is
  skipped the run says that priorities were not looked for in the input set rather
  than that none were stated. **This is the rung that was missing, and its absence
  was measured**: three priority documents sat in one input set, readable, naming
  directives, published period priorities and annual objectives, and a run that
  stopped at the two channels discarded all of them and labelled itself as built
  with no stated priorities while every one was one read away.
- **WHERE RUNG 3 SUPPLIES THE SOURCE, PART 8 IS UNCHANGED FROM END TO END.** The
  sweep, the actor test of 8.7, the matching ladder of 8.8 and its predicate rung
  in 8.8.1, the compliance gate of PART 9 and the source boost of 12.7 all run on a
  rung-3 direction exactly as they run on a rung-1 one. What the artifact records
  in addition is the rung each direction arrived on, per P3's own recording list,
  so a reader can see how the direction reached the run without that changing what
  it weighed. Documents so admitted are still read for EVIDENCE ONLY and never for
  format, phrasing or structure, per 26.2 and SD-PRI-33.

## 3.2 Binding state, and the run that happens anyway

Read the bound config. Classify each needed variable as bound, declined,
defaulted or unbound. Then:

**A FULLY ANSWERED INTERVIEW MUST PRODUCE A FULLY BOUND RUN.** SD-CTR-26. Where a
competent answerer answered every question the interview asked, in the way a
competent person naturally answers it, the run that follows is NOT provisional.
Where it is, the defect is in the bundle and never in the answerer. So a variable
counts as BOUND for the purpose of this test when it is in ANY of three states,
and all three satisfy ignition:

| State | Confidence | What it is |
|---|---|---|
| ANSWERED | HIGH | a turn elicited it directly |
| DERIVED | MEDIUM | a documented derivation computed it from what the turns DID elicit, named in that variable's own documented-default row |
| DEFAULTED | LOW | its documented default applied and its notice prints |

**A DERIVED sub-field is NOT an unbound sub-field**, and a run that stamps
PROVISIONAL because a sub-field was derived rather than typed is wrong. A working
interview that silently produces a permanently degraded product is worse than an
interview that fails, because nobody goes back to fix it.

Two limits on that, and they are the failsafes. A medium-confidence value may be
written to an organization's configuration ONLY by an interview that read the
derived values back to the answerer before it closed and got a yes; **a RUN may
never do it**, and SD-CNF-01 is untouched for inference during a run. And the
close of any binding interview states what was answered, what was derived and
what was defaulted, with a count of each, because an interviewer who is told
nothing was left out is entitled to believe it.

- If the IGNITION set is bound: normal run.
- If any of the IGNITION set is unbound: **PROVISIONAL RUN**, per
  reference/binding-interview.md PART 6. **BINDING_OWNER_CONTACT IS NOT IN THAT SET AND AN
  UNBOUND ADDRESS NEVER MAKES A RUN PROVISIONAL.** It is DEFERRED, with the
  consequence it carries in its own SECTION A1 row, and the reason is stated in
  the schema's ignition table: it is the one value a DOCUMENT can never supply, so
  a first run bound faithfully and completely from an organization's own published
  documents was stamped PROVISIONAL at full prominence forever, on the one binding
  no amount of care could clear, and the label stopped distinguishing a run that
  was missing something recoverable from one that was not. The disclosure is not
  lost, it moved to its own line: the artifact still says, at the standing
  prominence and on every run until an address is bound, that the invitation in
  this report names no way to reach anybody. The frontline user is never asked an ORG
  question, including an ignition one. The correct response to a blocking state
  the user cannot clear is not to hand them the block. It is to produce the most
  useful honest thing available and route the block to somebody who can clear it.

A provisional run infers what it can, silently, before anything is asked: the
user's identity, title and manager from the directory if reachable; the
container, header row and the three required concepts from the file; the scope
columns present and their distinct value counts, from which a containment chain
can be read straight out of the data because a column whose values nest inside
another column's values is a hierarchy, and **an inferred chain ENDS AT THE LEVEL
ONE RANKED UNIT SITS AT, never at the finest level somebody owns**, per
reference/schema/ GROUP 3 and 11.7.2; the level at which one unit of business
sits, which is UNIT_LEVEL_KEY detected as the scope level whose distinct value
count over the in-scope population equals that population's record count, taking
the FINEST level where more than one matches and asserting no binding error over a
population of one record, per 11.7.2 and SD-POP-26; the SHAPE of the population being scored, per 3.2.1 below; whether
the population is COLD, per 14.8 and SD-CLM-28, which is detected from the data
on every run whether or not anything is bound; and the period the file covers
from its own stamps.

None of that is written to the ORG config. A medium-confidence inference never
becomes a binding. SD-CNF-01. It is written to a provisional record with its
evidence, so the eventual ignition interview opens with those inferences as
proposals and is faster for having waited.

The provisional label appears at the SAME PROMINENCE on every provisional run.
It is never softened because it has appeared before. reference/capability-probe.md 4.4.

### 3.2.1 Inferring the shape on a provisional run, and what follows from it

SD-POP-23 settles what shape IS: it is a property of the POPULATION being
scored, not of the company. POPULATION_SHAPE is a KEYED SET of declared
populations, each with its own mode, its own unit noun and its own fields. A run
never asks whether this company is FIXED or FLOW. It asks WHICH POPULATION IT IS
SCORING and WHAT SHAPE THAT POPULATION HAS.

On a BOUND run the shape is READ from the declared population the run resolved.
It is never inferred and never guessed.

On a PROVISIONAL run, where POPULATION_SHAPE is unbound, the shape is INFERRED
from the columns present, at MEDIUM confidence, using the three tests in
SD-POP-24 as far as the data can answer them:

1. THE ROSTER TEST, answerable from the data: a stable identifier set that a
   complete list could be taken from, without reference to a stage.
2. THE ENTRY AND EXIT TEST, answerable from the data: an entry-date concept and
   an exit-date concept both resolve and populate.
3. THE REPLACEMENT TEST, which DECIDES and which the data cannot answer. When one
   of them leaves, does it leave a HOLE somebody notices and moves to fill, or
   does the next one take its place in a QUEUE? A hole means a FIXED roster whose
   members happen to be dated, and the dates are unit ATTRIBUTES rather than a
   pipeline. A queue means FLOW.

Tests one and two BOTH passing is the COMMON case, not the ambiguous one. A
roster of dated standing positions passes both; so does a pipeline held inside a
stable set of containers. Do not reach for a tie-break there.

**WHEN THE TIE-BREAK MAY BE CONSULTED, AND IT IS NARROWER THAN IT LOOKS.**
SD-POP-24 owns this and it is restated here only because a provisional run is
where it bites. The tie-break is reached ONLY where tests one and two DID NOT
DISCRIMINATE, meaning both passed or both failed, AND test three could not be
answered. The three cases:

| What tests one and two did | Outcome | Tie-break |
|---|---|---|
| Test 1 passes, test 2 FAILS | FIXED, DECIDED | NOT consulted. Do not prefer FLOW. |
| Test 2 passes, test 1 FAILS | FLOW, DECIDED | NOT consulted. |
| Both pass, or both fail | Test 3 decides; where test 3 cannot be answered from the data, and on a provisional run it usually cannot | consulted, prefers FLOW, and the artifact says TIE-BROKEN |

A shape recorded as tie-broken when it was in fact decided by test one or test
two is as much a defect as the reverse, because it invites a binding owner to
overturn a correct reading.

Four things follow on a provisional run, all mandatory:

- The inference, the tests that fired and the evidence for each are printed in
  the front panel AND in the Method section, at MEDIUM confidence.
- Where test three cannot be answered from the data, the shape is taken on the
  TIE-BREAK, which prefers FLOW, and the artifact SAYS it was taken on the
  tie-break rather than answered. A tie-break that leaves no trace is a guess.
- Where the roster test passes over CONTAINERS and the entry-exit test passes
  over the things moving across them, that is NOT a conflict. It is TWO
  populations. Say so, score the one the request is about, name it, and record
  both for the eventual ignition interview.
- Every sub-key of POPULATION_SHAPE that could not be inferred is treated as
  UNBOUND. In particular, `reopen_allowed` CANNOT be inferred from columns alone
  and is therefore ALWAYS unbound on a provisional run, so PART 23 divergence 2
  takes the UNRESOLVED DUPLICATES path rather than merging on a guess.

## 3.3 The person script

Four questions, asked in ONE message, on the user's first run, then remembered.
The script is owned by reference/binding-interview.md PART 4 and is not restated here.
Everything resolvable from the user's own record is resolved silently and
presented as a confirmation, never as an open prompt. SD-IDN-19.

Before any of the four fires, work the ladder and stop at the first hit
(SD-IDN-12): the request itself; the user's own directory record read in FULL,
not only the title; their manager's record; stored memory; the file itself,
including its distinct values; the filename or the message that carried the
file; and only then ask. Never ask for a number the records already hold.

If MEMORY is ABSENT, ask, use the answers, and tell the person plainly that the
answers could not be saved and will be asked again. SD-IDN-15.

The person script never asks an ORG question in any phrasing, including as a
confirmation. The forbidden list is in reference/binding-interview.md PART 4 and includes
what the levels are, how codes are padded, which entities exist, what the
benchmark is, which metrics carry which weights, how many items a role should
receive, and any threshold, factor, cap or weight from the schema.

## 3.4 The deferred-request budget for this run

At most TWO deferred bindings may be requested in one run, and never more than
ONE before the first output is produced. reference/binding-interview.md I3 and C2. A run
that stops four times to bind configuration is an interview wearing a report's
clothes.

Selection is by COST, not by interest: fire the outstanding request whose
documented default moves a published number furthest. C3, and SD-CTR-28.

**COST IS COMPUTED ON THIS RUN. IT IS NOT READ FROM PART 22.** Every default has
already been applied by the time this run could publish anything, so the
counterfactual is cheap: for each outstanding request, count what its default
changed in the artifact about to be produced, and sort into four classes.

| Rank | Class | Test |
|---|---|---|
| 1 | CHANGES MEMBERSHIP of a ranked list | the default added or removed a row from a published action, reference or exception list. JUMPS THE QUEUE ahead of every class below. |
| 2 | CHANGES A PUBLISHED ORDER OR FIGURE | a rank, score, percentile, weight, count or printed number moved. Order within the class by published rows affected, descending. |
| 3 | CHANGES SOMETHING NOT PUBLISHED this run | a section with no members, a feature not reached, a label not printed. |
| 4 | PROVABLY CHANGED NOTHING | the artifact is identical either way. **Does not fire this run.** It stays queued. |

**PART 22's ORDER IS THE TIE-BREAK, NOT THE ORDER.** Where two requests land in
the same class with the same measured effect, break the tie by PART 22's order and
then by variable name, so the same file always spends its budget the same way.

The failure this replaces is concrete: a run spent its whole budget on a question
whose default changed nothing observable, while the question deciding whether
eleven units that had already given notice of exit sat inside the published plan
was pushed out of budget. Record every outstanding request, its class and its row
count in the audit, not only the one that fired.

Four constraints, all of them:

- C1. Right answerer only, and AUTHORITY IS ADDITIVE. A deferred ORG question
  fires only to a user whose role carries organizational authority for that
  binding, or to the binding owner. Authority resolves as a UNION of two standing
  grants, per SD-CTR-25 and the ROLE_LADDER.binding_authority default: the named
  BINDING_OWNER_NAME holds ALL, AND the most senior role on ROLE_LADDER holds ALL,
  whether or not an owner is named. Naming an owner NEVER removes an answerer.
  Never read the senior-role grant as a fallback that lapses once a name exists;
  read it as a grant that always stands. Where the run fires a question, it names
  which grant authorized it. To anyone holding neither grant: apply the documented
  default, print the exact notice from reference/schema/ SECTION A1 or A2 in the
  artifact, and queue the request to BINDING_OWNER_NAME at
  BINDING_OWNER_CONTACT. Where BINDING_OWNER_CONTACT is unbound the request is
  STILL queued and still recorded against the owner by NAME: authority is computed
  from BINDING_OWNER_NAME and the standing senior-role grant, neither of which
  reads an address, so every deferred question still fires and still finds an
  authorized answerer. What an unbound address costs is the ability to post a
  notice BETWEEN runs, and the artifact says so in the line MSG_AUTHOR_LINE gives
  it rather than printing an empty placeholder.
- C2. At most two per run, at most one before the first output.
- C3. Highest-cost gap first, where cost is COMPUTED on this run by the four classes above and PART 22's order is only the tie-break. A request that provably changed nothing does not fire.
- C4. Once, then never. A bound or declined variable does not fire again. A
  declined one may fire once more only if a later run reaches a decision where
  the default is materially worse than at the first firing, and then never again
  outside the Stage 3 audit.

When a request does fire, it says four things in this order and then asks: the
DECISION it is facing, not the variable name; why the value is needed for that
decision; what it will do if the answerer declines, quoting the documented
default and the degradation notice in plain words; and the question.

When it does not fire, or is declined, the run applies the documented default
and SAYS SO IN THE OUTPUT. Never in the chat alone.

## 3.5 The one-line heads-up

On a large input, say the row count, the scope and that the build will take a
while, so the user knows the silence is work and not a hang. SD-CTR-17. Quote
the band from RUN_ESTIMATE_BANDS and say plainly that the estimate is generic
rather than measured on their data.

---

# PART 4: THE STAGES

A supervised swarm, not one long script. SD-RUN-01. The supervisor owns the
gates and never does the work. Workers own exactly one stage each and are
disposable. Every worker writes a checkpoint. A worker failure is isolated to
its own partition.

Every stage has the same six-field contract: PRECONDITION, ACTION,
POSTCONDITION, ON FAIL, WAIT, STOP. SD-RUN-02. Uniform failure semantics across
every stage removes the need for per-stage judgment.

| # | Stage | Depends on | Worker output | Supervisor gate |
|---|---|---|---|---|
| 0 | Capability probe | nothing | probe record | the one probe-time stop |
| 1 | Identity, role, scope | 0 | resolved role, line, scope level and code | scope purity: every row carries the resolved code |
| 2 | Qualifiers and restriction | 1 | the qualified population | qualifier membership: every row satisfies every applied term |
| 3 | Period resolution | 0 | the operating window being planned | the window is dated and its derivation is named |
| 4 | Priorities, all sources | 1, 3 | the priority inventory and the directed candidate set | the retrieval gate: every detected attachment resolved to one of three states |
| 5 | Compliance validation | 3, 4, 6 jurisdiction column | validated priorities with findings | no unvalidated priority carries weight |
| 6 | Acquire and parse | 0 | the concept map, the record count, the work-item inventory | the three required concepts resolved; record count above zero |
| 7 | Population | 2, 4, 5, 6 | the ranked population, N, eligible_count, medians | the pipeline order held; exclusions reconcile |
| 8 | Score | 7 | a score and a deterministic rank per unit | the formula's terms all evaluated or named as not evaluated |
| 9 | Steer | 1, 7, 8 | the weight vector, the measure basis, the mode | a lean did not silently become a restriction |
| 10 | Assemble | 8, 9 | every section built and styled | per-section rows plus format pass |
| 11 | Verify | 10 | the pass matrix and the reconciliation | the guarantees in 1.9 |
| 12 | Publish and reply | 11 | the artifact and the short reply | published once, at the end |

Only stages that are genuinely independent run in parallel, and never across a
gate. SD-EFF-16. Stage 0 and the person script are independent; almost nothing
else is. The named trap: priorities need the resolved supervisor, the compliance
check needs the parsed jurisdiction column, the scope ladder reads distinct
values out of the parsed file, and the period resolution reads the file. Three
stages once claimed independent were all dependent, at once, and the result was
a central-only, unvalidated priority set that silently dropped both the
restricted exclusions and the directed matches. Do not parallelize across a gate
to save time. The gate is the only thing standing between a small error and a
confidently wrong artifact.

Every gate from stage 6 onward re-checks REGRESSION_INVARIANTS against the
CURRENT artifact, never against an earlier checkpoint's claim about it.
SD-EFF-07. The standing eight: record count reconciles; scope purity holds; the
not-actionable exclusion holds; the class exclusion holds and its ordering held;
no measure floor was applied; qualifier membership holds; the directed set was
resolved before the class filter; sampled percentiles are stable. Silent
re-admission of excluded rows is the failure this check exists to catch, and it
becomes more likely with every additional worker, which is exactly why it runs
at every gate rather than once at the end.

Any unresolved item propagates to the Method section. Nothing quietly disappears
between stages. SD-EFF-08.

Every gate resolves to PASS, FAIL or NOT APPLICABLE, and not applicable never
blocks emit. SD-EFF-37. Bind explicitly which gates are not applicable in which
run mode, so a path that skips a stage is not killed by a gate inspecting an
artifact that path does not produce.

Route every failure to a stage that can REMEDIATE it, never to one that only
evaluates. SD-EFF-34. A chain that stops at the stage which computes labels
cannot fix a sentence; the chain continues through the drafting stage, or the
re-gate inspects unchanged text and fails identically. Remediation never re-asks
a question already answered. SD-EFF-35.

Ask questions to buy time. SD-EFF-38. Stopping to ask is free; it costs no
correctness and converts dead waiting into useful input. Ask a stage's questions
while that stage runs, subject to the budget in 3.4.

---

# PART 5: STAGE 1, IDENTITY, ROLE AND SCOPE

## 5.1 Resolve the person before anything else

Batch the identity calls: the self lookup named by DIRECTORY_SELF_LOOKUP, the
manager lookup named by DIRECTORY_MANAGER_LOOKUP, and the current date. Do NOT
batch the priority sweep in with them; the sweep depends on the resolved
supervisor and batching them is the parallel-across-a-gate error.

**The manager lookup is mandatory and non-substitutable.** SD-IDN-01. Use the
call that returns the MANAGER RELATIONSHIP and nothing else. A profile record
that carries no manager field can never answer who someone reports to, and using
it for that purpose returns a confident wrong answer rather than an error.
Concluding "no supervisor" from a profile record is the single most damaging
error this method can make, because it silently deletes the nearest priority
sources and produces an artifact that ranks on the central source alone while
telling the reader the supervisor published nothing. The general form: never
infer an absence from a source that does not carry the field.

Only one person in the organization has no supervisor. SD-IDN-02. Before
recording "no supervisor", BOTH must hold: the manager call was actually made
and returned empty, AND the person's own title names the top of the house. An
error is a failed lookup, not an absent manager. Do not convert a data gap into
a claim about the organization.

**WHERE NO DIRECTORY EXISTS AT ALL, THE PERSON IS ASKED, AND THEIR ANSWER IS AN
ANSWER.** The two-part test above governs what may be inferred from a directory
that FAILED. It does not require a person to be recorded as UNRESOLVED when they
have told you the answer themselves. Where the directory capability is ABSENT
rather than failing, the manager call cannot be made at all, so the first half of
the test can never be satisfied and by the letter even the head of the
organization would be recorded as having an unresolved supervisor. That reads as
ridiculous and costs the artifact more credibility than the precision buys. In
that state the person-tier supervisor question is the instrument, and it has
three outcomes: a NAME, which binds; a statement that they are the TOP OF THE
HOUSE, recorded as such on that person's own account with the source named
SELF-REPORTED rather than as a directory reading; and NO ANSWER, which is
UNRESOLVED.

Whichever outcome is recorded, the SOURCE is recorded with it: directory,
self-reported, or unresolved. A self-reported top of house never suppresses the
priority sweep for anybody below them, and it is never written back to the
organization tier by a run.

Losing the directory costs the shortcuts, not the deliverable. SD-IDN-05. Infer
role and scope from the file, note what was assumed, and carry on.

## 5.2 Resolve the role

Order of operations, and the order is load bearing:

1. Normalize the title: match case-insensitively, ignore punctuation, expand
   ROLE_TITLE_ABBREVIATIONS. SD-IDN-04. Real directory titles are written in
   shorthand, and a table lookup that misses the abbreviation falls through to
   inference on a record that was unambiguous all along.
2. **The wide-scope test runs FIRST.** If the title carries any token from
   WIDE_SCOPE_TOKENS anywhere in it, the role is the senior tier regardless of
   what follows. Only a title whose most senior token is a junior role AND which
   names no wider scope gets the junior shape. Record the token that decided it.
   SD-IDN-03. This prevents demoting a senior title to a narrower scope than the
   file supports.
3. Then the title table in ROLE_LADDER.titles, taking the most senior token
   present.
4. If it resolves to nothing, ask ONCE, offering the ladder's display names as a
   numbered list with one line each describing what that role owns, and accept a
   number. SD-IDN-13.
5. If the directory was unreachable and the user did not answer, take
   ROLE_FALLBACK_KEY, which is bound to the NARROWEST role so an unknown never
   inflates a claim or a list size. Q-C5, P4.

**WHERE ROLE SCOPE LEVELS ARE DERIVED BY POSITION, ANCHOR THE MAPPING AT BOTH
ENDS, AND NEVER ON THE UNIT ITSELF.** SD-CTR-27. The most junior role maps to the
FINEST OWNABLE level, which is the level immediately COARSER than UNIT_LEVEL_KEY.
The most SENIOR role maps to the COARSEST level in the chain. Surplus levels in
the middle are absorbed by the senior roles; surplus roles share the finest
levels.

**THIS ANCHOR IS NOW CORRECT BY CONSTRUCTION, AND SAYING WHY IS THE POINT OF THIS
PARAGRAPH.** reference/schema/ GROUP 3 defines SCOPE_LEVELS as the containment
chain running from the whole organization DOWN TO AND INCLUDING the level at which
ONE RANKED UNIT sits, and reference/binding-interview.md Turn 2 now asks for the chain in
exactly those words and checks the last level back with the answerer. The finest
OWNED level is one step coarser and has its own name, SCOPE_FINEST_KEY. Two
concepts, two variables, never the same level on a chain of more than two. So
"the level immediately COARSER than UNIT_LEVEL_KEY" and "the finest OWNED level"
now resolve to the SAME level on a correctly bound chain, and the junior anchor
lands where it should on the first try.

**THE FAILURE THIS USED TO PRODUCE, STATED IN FULL SO NOBODY RESTORES THE OLD
READING FROM INSTINCT.** An earlier revision defined the chain as running to the
finest OWNED unit and asked for it in those words. Answered honestly at an
organization whose smallest owned thing is one person's book, the chain stops at
the book, one level short of the thing on the row. UNIT_LEVEL_KEY is then detected
rather than read off the chain, no level's distinct value count matches the record
count over one person's units, the detection falls to its documented fallback, and
the fallback returns the finest level in the chain, which is the BOOK, which is
also the reader's own level. Two things then break in opposite directions off one
binding: 11.7.2's unit-level-equals-the-reader's-level row fires and suppresses
the ranked list, the percentile and every comparative sentence for a reader with
dozens of live units; and this anchor maps the most junior role onto the BRANCH,
so a person who works units with their own hands is recorded as leading people who
do, which SD-SPN-09 calls fatal in both directions. No gate catches either one:
the funnel reconciles, every invariant passes, and the artifact is internally
consistent and wrong.

**THE ONE-SENTENCE TEST A BINDING OWNER CAN APPLY, and it is the same one GROUP 3
gives:** read the last level of the chain aloud and ask whether ONE of those is
ONE LINE on the report. If a person can own several of them, it is not the last
level and the chain is one level short. Where a run finds the chain in that state,
the correct response is to report the CHAIN as the binding error, addressed to
BINDING_OWNER_NAME, and never to work around it by re-anchoring the roles.

**Nobody owns ONE unit of business as their scope. The unit is the ROW, not a
span.** Anchoring the junior end on the finest level outright maps the most junior
role onto the unit level, which says that person owns exactly one unit. Read
literally that fires the unit-level-equals-the-reader's-level row of 11.7.2,
which suppresses the ranked list, the percentile and every comparative statement,
and hands the frontline reader this method was built for a report with no ranking
in it. SD-SPN-02 and SD-POP-26 both already say the unit level is not a span.

**A single-anchored mapping is off by one at EVERY role, not only the first.** The
top of the house comes out owning one level below the top, the top level comes
out owned by nobody, and a role that LEADS people who work units comes out as a
role that WORKS units. That last one survives into an artifact, because it flips
a claim tier, and SD-SPN-09 calls that error fatal in both directions.

**THE TELL, and treat it as a diagnosis rather than a coincidence: where a
derivation that knows MORE produces a worse answer than the fallback that knows
LESS, the extra knowledge is being applied at the wrong end.** The fallback used
when UNIT_LEVEL_KEY is unbound says the most junior role is DIRECT and every
other role is AGGREGATE. Derive, then CHECK the two paths against each other:
where the positional derivation and the fallback disagree about ANY role's claim
tier, the derivation is wrong, THE FALLBACK STANDS, and the disagreement is
recorded for the binding owner. Both paths must agree on a well formed ladder.

Exactly ONE level is DIRECT, the finest ownable level, and every level coarser
than it is AGGREGATE without exception. A person who owns a group of the things
that own units does not touch the units.

The resolved role decides three things and only three: the deliverable line, the
claim tier, and the altitude ceiling. It does not change the sections, the
formatting, or the method.

## 5.3 Resolve the scope

The user speaks naturally; the skill does the arithmetic. SD-IDN-11. Accept a
short code or a plain phrase, identify the level from the code width or the word
used, and pad it yourself. Never ask the user to pad and never reject a short
code.

Resolution ladder:

1. If the request named a scope in words, resolve through
   SCOPE_PLAIN_LANGUAGE_MAP, then against the distinct values present in the
   file. Q-B3 fires only when a phrase resolves to nothing.
2. If the request named a code, classify its level. Where SCOPE_CODE_SCHEME is
   hierarchical, pad by SCOPE_CODE_WIDTH in SCOPE_CODE_PAD_DIRECTION using
   SCOPE_CODE_PAD_CHARACTER, and read the level from SCOPE_LEVEL_ID_WIDTHS.
3. **An ambiguous identifier is resolved against the DATA, never against its own
   pattern.** SD-IDN-07. Where a padded code carries
   SCOPE_CODE_AMBIGUITY_THRESHOLD or more trailing pad characters it is
   ambiguous between levels: test the candidate against EACH level's own column
   and take the level that returns rows. Trailing-pad classification is decisive
   only below that threshold. This is an explicit precedence that overrides the
   pattern rules above it. Worked example, neutral: in a scheme where a coarse
   unit is one character and a fine unit is six, coarse unit 1 pads to the same
   six-character string as mid-level unit 10 padded once more; classifying that
   by trailing pad characters silently scopes a mid-level owner to an entire
   coarse unit.
4. When more than one reading returns rows, use the single tie-break used
   everywhere: the level named by the WORD the user used, then the level their
   own ROLE implies. Ask only when no reading returns rows. SD-IDN-08.
5. Compare identifiers as TEXT on both sides. SD-IDN-09. Cast both the column
   value and the resolved code to text, trim whitespace, drop any decimal tail,
   strip separators, and pad the column value to the code's length. A typed
   comparison between a resolved code and the wrong one of those returns zero
   rows and looks exactly like an empty scope. Apply the same treatment to unit
   identifiers and postal-style codes.
6. If the requested scope is at or above everything the file contains, apply NO
   filter: test whether every in-scope row already carries the requested code as
   a left-anchored prefix, and if so skip the filter, rank the whole file, and
   say so. This is a normal path, not a degraded one. SD-IDN-10.

**Zero rows means the filter is wrong before it means the scope is empty.**
SD-IDN-16. Re-test the comparison as text on both sides and re-test the level
reading first. Only then stop and list the distinct values present at every
level.

Narrow before asking. SD-IDN-14. If a coarser level resolves but a finer one
does not, use the coarser level to narrow the question, turning a question about
eleven options into a question about a handful.

When you must ask, ask in the USER's language, not the file's. SD-IDN-13. Offer
the distinct values present, each labelled with something a person recognizes
and a count beside it, and accept a name or a list position as the answer, not
only a code. ASK_LANGUAGE_RULE requires it; a bare code is not an acceptable
option label.

Batch every question into one message. SD-IDN-17. If three things are ambiguous,
ask about all three at once. Never ask, work, then ask again; that is the
pattern that makes a tool feel like an interrogation. Question batching is
arithmetic, not judgment: fire every blocking question whose trigger is met,
count them as B, and fill the remainder of the round with
max(0, QUESTION_BATCH_MAX minus B) non-blocking questions by weight, ordering
ties by position in QUESTION_BANK. SD-IDN-22. A question never fires before the
stage that supplies its context. SD-IDN-25.

Blocking and non-blocking questions have different failure semantics.
SD-IDN-21. A non-blocking question is freely skippable and an empty answer means
SKIP, never cancel. A blocking question is not ignorable: if the user declines
or does not answer, the run terminates through the bannered incomplete path in
SD-EFF-05. The skill never fabricates the missing value and never silently
proceeds as if the question had been answered.

Ask only for REQUIRED concepts; never ask for optional ones. SD-IDN-18. Required
means the minimum the method cannot run without. A missing breadth column costs
one section; a question costs the user's attention and the run's momentum.

Persist a settled answer and verify the save succeeded. SD-IDN-15. Save
immediately, confirm the call returned success, retry once, and tell the user
plainly if it still will not stick, because a failed save means they get asked
again every run.

Nothing may be hard-coded from any reference data. SD-IDN-06. No row count,
column count, unit list, median or item count. Every threshold is computed from
the file in hand and the actual figures are reported. The source is never the
same size twice.

Every question must be answerable in under thirty seconds, must carry the
findings that prompted it, and must never ask for something the tools could have
resolved. SD-IDN-20.

## 5.4 What stage 1 hands downstream

The resolved role key; the deliverable line key; the claim tier; the altitude
ceiling; the scope level key and code; the filtered population; the supervisor
and the resolved upline chain, with every level named including levels that
published nothing.

---

# PART 6: STAGE 2, QUALIFIERS AND RESTRICTIONS

A qualifier selects which subset of the scoped units the report is about. It
changes WHO is in the population; it never changes the METHOD applied to that
population.

## 6.1 Classify the phrase by TYPE before searching any column

SD-QUA-01. Route the phrase to a column FAMILY first, then search only that
family's columns. Classifying before searching is what makes a miss recoverable:
a phrase routed to a column family has a column to report and near-values to
offer, while an unrouted phrase has neither.

Classify on TWO axes at once, because a single label routes flags into
arithmetic. SD-QUA-03. The ENTITY the column describes, and its MEASURE TYPE:
rate or volume; proportion; count; flag; identity; date; text. Only a column
typed as a rate or a volume may enter arithmetic. A column naming an entity and
typed as a flag is never a volume metric.

**Never run a match across the whole sheet.** SD-QUA-02. Whole-sheet substring
matching is how an execution flag gets attributed to a product as a volume
result, and how a wider area name lands in a narrower locality column.

## 6.2 Resolve absence phrases by RULE, before any value search

SD-QUA-04. Some qualifiers are represented by an EMPTY CELL, and a value search
cannot find an absence. These are resolved by rule and the rule overrides any
text match. reference/field-resolution.md 3.12 holds the map. The three standing cases:

| Concept | Resolves to |
|---|---|
| The self-determined subset | the grouping field is BLANK after null normalization |
| The managed subset | the grouping field is POPULATED |
| An unbenchmarked entity | no benchmark column exists for that entity |

**THE PROPER-SUBSET GUARD, and this stage executes it.** reference/field-resolution.md
3.12 carries it. An absence rule yields a usable subset ONLY where the complement
is a PROPER, NON-EMPTY subset. Where the grouping field is BLANK ON EVERY ROW in
scope, or POPULATED ON EVERY ROW in scope, the distinction DOES NOT EXIST in this
population: record the subset as NOT PRESENT, skip every cut, filter and gate that
depends on it, and NAME IT IN THE AUDIT. **A subset equal to the whole population
is not a cut; it is the population under a second name.** This is the mirror of
SD-PRS-18: there, a resolved-but-EMPTY column is treated as absent; here, a
resolved-but-FULL absence rule is treated as no distinction. Without it, a
population whose grouping column is blank on every row resolves the
self-determined subset to one hundred percent of itself, the qualifier reports a
subset that is the whole scope, and every comparison drawn from that cut compares
a number against itself while every gate passes.

Searching for the literal word finds nothing in ANY file, because the thing is
represented by an empty field rather than by the word, and a resolver that
value-searches it falls through and SILENTLY WIDENS to every unit in scope.
This is named as the single most consequential absence, because the
self-determined subset is the highest-evidence cut available to a direct-tier
person. SD-SPN-12: it isolates skill from inherited advantage, so where the
narrative names it, surface it first and say so explicitly. The general form: a
category defined by an absence cannot be found by searching for its name.

## 6.3 Convert a name to its stored code through a TABLE

SD-QUA-05. Normalize a long name to the stored code form through
JURISDICTION_NAME_TO_CODE, then match EXACTLY, and confirm the code is actually
present in the column before filtering. Coincidental substring containment is
never evidence: one or two codes happen to sit inside their own long names and
most do not, so a substring resolver works by coincidence on some values and
fails silently on the rest.

An administrative suffix is a routing cue, not noise. SD-QUA-06. Strip the
suffix in SUBREGION_SUFFIXES before matching, and route the phrase to that ONE
column and nothing else. Left in, the suffix causes a miss; routed loosely, the
bare stem can match a like-named locality and silently scope the report to one
place inside the area the user asked for.

A compound phrase splits before classification and applies with AND.
SD-QUA-08. A separator splits it; both halves are classified and matched
independently and then applied together. Do not tokenize a multi-word value.
Place names repeat across jurisdictions, which is exactly why the second half is
not optional when the user supplied it.

## 6.4 The match cascade, confined to the routed columns

SD-QUA-07. Case-fold, strip punctuation, collapse whitespace, then: exact, then
normalized-exact, then prefix, then bidirectional substring. Never across the
whole sheet.

## 6.5 Where a qualifier sits in the pipeline

Qualifiers are applied in the SCOPE stage, before every exclusion and before the
percentile. SD-QUA-09. The qualified set becomes the population for everything
downstream. Applied later, units would be ranked against a population they are
not being compared to, and the front panel would describe a percentile that
means nothing.

A restriction, which is the STEER mode that narrows the population, is applied
in the same step for the same reason, and it changes the measure basis with it.
SD-STR-06.

## 6.6 A miss is reported loudly, and the three outcomes never collapse

SD-QUA-10:

| Outcome | Behaviour |
|---|---|
| Matched | Proceed and disclose the column, the operator and the matched value set with row counts. |
| Routed to a column type, no value matched | STOP before ranking and ask. Report the phrase, the column tested, and the MISS_SUGGESTION_COUNT nearest values present, ranked by ascending normalized edit distance with an alphabetical tie-break, so the same miss always returns the same list. |
| Routed to NO column type at all | Say which columns were tested, run the request WITHOUT that term, and label the report unqualified. |

Never take the third row for a phrase that classified successfully. An empty
report looks like a finished one.

Distinguish "the column is absent" from "the value is not in it". SD-QUA-11.
They read identically in the output and have completely different fixes.

**Never silently widen.** SD-QUA-12. If a qualifier cannot be applied, the
report must say so ON ITS FACE. A report that quietly covers the user's whole
span when they asked for one place is wrong in the way that destroys trust,
because every number in it is internally consistent. This is the general
statement of the whole failure model of this skill, and it applies to a missing
CAPABILITY exactly as it applies to a missing column.

Downstream guards work unmodified on a qualified population. SD-QUA-13. A
qualifier that leaves few units hits the existing degenerate-scope guards in
PART 20. Nothing new is needed.

Record what was routed, resolved and matched, with counts. SD-QUA-14. For every
routed column record the phrase, its resolved entity and measure type, the
column, the operator, and the matched value set with row counts. This is what
makes a disputed number traceable.

---

# PART 7: STAGE 3, THE PERIOD BEING PLANNED

## 7.1 Resolve the period being PLANNED, not "the latest"

SD-SRC-15. Planning happens AHEAD of the period. Match sources on the PERIOD,
because the next period's source sits alongside this one's rather than replacing
it.

**A relative phrase is not a named period.** Phrases like this period, this
cycle and now fall through to the calendar rules rather than being read as the
period the run happens to start in.

The decision ladder, worked without asking:

1. The user named a period explicitly. Use it.
2. PLAN_AHEAD_RULE decides between the current window and the next. The standing
   rule: if today falls in the last third of the current window, plan the next
   one. Q-L4 fires only when the run falls near a window boundary. **A period
   reached by this step is PROVISIONAL and is confirmed against the sources at
   stage 4, per the correction below**, because this step reads the CALENDAR and
   the sources have not been swept yet.
3. Read the actual window dates from OPERATING_WINDOW_SOURCE.
4. If the published window cannot be read, derive it from
   OPERATING_WINDOW_DERIVATION_RULE and say plainly that it was DERIVED.
   SD-PRS-05. A derived window dates the items correctly in almost every case;
   an unread window would zero the entire alignment term and the workload term
   at once.

A run that quietly plans the wrong period is indistinguishable from a correct
one until the person is standing in front of the work. That is why
PLANNING_PERIOD_NAME and PLANNING_PERIOD_LENGTH_DAYS are ignition bindings and
not deferred ones.

**THE PERIOD A SOURCE NAMES OUTRANKS THE PERIOD THE CALENDAR SUGGESTS, AND THE
LADDER DID NOT IMPLEMENT ITS OWN OPENING SENTENCE.** SD-SRC-15 opens by saying
MATCH SOURCES ON THE PERIOD, and steps 2 to 4 read only the calendar and the
operating window. **The failure that leaves, measured:** at one organization the
only published priority document was titled for the month AFTER the one step 2
would have chosen and said in its first line that that month was the period it
addressed. Step 1 saved that run because the user had named the period. Where a
user does not, step 2 plans one month against another month's priorities, every
alignment term in the artifact is computed against a document about a period the
plan is not for, and no gate can see it because every date in the artifact is
individually correct.

**WHY THIS IS A CORRECTION AT STAGE 4 AND NOT A RUNG ABOVE STEP 2, WHICH IS AN
ORDERING FACT AND NOT A PREFERENCE.** Stage 3 depends on stage 0 alone and stage 4
depends on stage 3, per PART 4: at the moment this ladder runs, NO SOURCE HAS BEEN
SWEPT and no source has been admitted, so there is nothing here to read a period
off. A rung that asked for one would be a rung that can never fire, which is the
same defect 10.1.1's limb 1 was written to escape. So the period a source names is
applied where the source exists:

- **A PERIOD FROM STEP 1 IS FINAL.** The user named it, and no source overrides a
  person, per G6. Where an admitted source names a different period, that is a
  DISCLOSURE and not a correction: the Method section names the source, its sender,
  its date and the period it names, beside the period the user asked for.
- **A PERIOD FROM STEP 2 IS PROVISIONAL UNTIL STAGE 4 CONFIRMS IT.** At the close of
  PART 8, where any source ADMITTED as a direction, a priority or a requirement
  names the period it is FOR, in its title, its own words or its stated effective
  period, **that named period is the period being planned**, and the run RE-ENTERS
  this section with it, re-resolves the operating window from step 3 onward, and
  re-runs every stage that reads the window. The Method section names the source
  that supplied the period and the provisional period it replaced.
- **WHERE TWO ADMITTED SOURCES NAME DIFFERENT PERIODS, PLAN THE NEAREST FUTURE
  ONE**, and name which sources named which, with their senders and dates, so the
  reader sees the disagreement rather than inheriting its resolution.
- **THE CORRECTION FIRES AT MOST ONCE, AND THAT BOUND IS WHAT KEEPS IT FROM
  LOOPING.** The sweep window of PART 8 is derived from the planned period, so a
  corrected period re-runs the sweep and the re-run can surface further sources. A
  SECOND correction is never applied: where the re-run's admitted sources name a
  period different again from the corrected one, the run STOPS correcting, plans
  the corrected period, and states in the Method section and on the front panel
  that the sources disagree about which period this plan is for, naming each source
  and the period it names. **Two periods disagreeing is a fact about the
  organization's own publications and is reported, never resolved by a third pass.**
- **WHERE NO ADMITTED SOURCE NAMES A PERIOD, NOTHING FIRES AND NOTHING IS SAID
  BEYOND ONE LINE**, which is the ordinary case for a standing register or an
  undated list. The provisional period becomes final and the Method section records
  that it came from the calendar rule and that no source named a period, because a
  reader who cannot see that the check ran cannot tell it from a check that was
  skipped.
- **THE COVERING INVARIANT BELOW IS RE-VALIDATED AFTER ANY CORRECTION**, not
  inherited from the provisional window, and so is the expiry gate of 7.3.

**THE COVERING INVARIANT: A WINDOW NAMED FOR A PERIOD COVERS EVERY DAY OF THAT
PERIOD.** SD-SCO-17. Where the window is NAMED for a calendar period, every day
inside that period falls inside the window that names it. A derivation that leaves
a day of the named month outside the month's own window is a BINDING ERROR,
rejected at validation, and it is never resolved by a disclosure.

The named case, and it is arithmetic rather than judgment: a nominal period length
of thirty days anchored on the first day of a calendar month leaves the
thirty-first day of a thirty-one day month outside the window. A commitment
falling on the last day of the month being planned is then banded as belonging to
the NEXT window and weighted down, on a plan whose own title names that month.
Every date in the artifact is individually correct, so no gate that checks dates
can see it, and the reader who loses the day is the one holding the plan.

**THE NAME IS THE AUTHORITY, AND IT SELECTS THE DERIVATION:**

- Where PLANNING_PERIOD_NAME denotes a CALENDAR unit, a month, a quarter, a half
  or a year, THE WINDOW IS THAT UNIT ENTIRELY, first day to last, and
  PLANNING_PERIOD_LENGTH_DAYS is used only for horizon arithmetic such as the near
  horizon of 12.3 or a lookahead.
- Where the name denotes a ROLLING or fiscal window that is not a calendar unit, a
  four-week cycle or a thirteen-period year, the nominal length sets the
  boundaries and the invariant is satisfied trivially, because no calendar unit is
  being named.
- A nominal length that disagrees with the calendar unit it is bound alongside is
  NOT an error and is NOT corrected. It is retained, because it is what the
  business calls the length of its period; it is simply not used to cut the
  window. Where the two differ by more than a few days, say so ONCE: the business
  may have meant a rolling window and named it loosely.
- Never resolve a covering failure by shortening the period, by moving the anchor,
  or by silently extending the window past the unit it names. The window is the
  unit; the arithmetic bends to it.

The invariant is VALIDATED, not disclosed: the run checks that every day of the
named period lies inside the resolved window before any item is banded, and where
it does not, the window is rebuilt from the name and the Method section records
both the rejected derivation and the one used.

## 7.2 The operating window is the only authority for when work is due

SD-SCO-03. Resolve every period token against the OPERATING window, never
against the calendar or fiscal quarter. A calendar or fiscal quarter end is
never an authority at any level; it is only ever an input the window converts.
REPORTING_CALENDAR_IS_NOT_AUTHORITY must be true.

A reporting quarter ends on a month boundary because that is how finance divides
the year. The operation does not stop on that boundary, and the days between are
a reporting artifact that carry no work. A token whose calendar end falls on or
before the current window's close, or in the gap before the next window opens,
bands to FULL weight. Banding a token down on the strength of a quarter end
moved a unit from rank 4 to rank 1 between two real runs.

PERIOD_TOKEN_MAP holds the tokens that may appear in a work item name. Every
value resolves THROUGH the operating window. A token that cannot be resolved
through the window is dropped from scoring and NAMED, never guessed at.

## 7.3 Cached references and the expiry gate

Cache what does not vary; fetch live what does. SD-SRC-16. The classification
test is: does this source vary per person or per period. If yes it is live and
can never be cached. If no it is cacheable behind a validity date. Re-crawling
everything on every run for every user is the single largest waste and the main
reason a run overruns.

The supervisor's own direction is the highest-value LIVE source and can never be
cached, because it is different for every user and changes weekly.

The expiry gate is BLOCKING, per cached block. SD-SRC-17. Compare today against
the block's entry in REFERENCE_VALIDITY_PERIODS. Within validity, use the block;
do not crawl and do not verify. Past validity the block is STALE and may not be
used until refreshed from the source named in that block's own header. Running
on expired doctrine is how a plan gets built against last period's weights. The
gate is not advisory.

If a re-fetch fails after the retry ladder, USE the stale block, record that it
is past its validity date and could not be refreshed, and CONTINUE. SD-SRC-18. A
stale reference is a disclosed limitation; a halted run is a dead end. When a
block IS refreshed, report the new content in the closing summary so the shared
configuration can be updated rather than every user re-crawling the same
documents forever. SD-SRC-19.

---

# PART 8: STAGE 4, PRIORITIES. ALWAYS ALL THREE SOURCES

Three sources of direction are read on EVERY run. Not the best available. All of
them. SD-PRI-01.

| Source | What it is | Cadence | Order of authority |
|---|---|---|---|
| A | The user's own supervisor chain, current period | live, never cached | read FIRST, outranks everything |
| B | The user's own supervisor chain, prior period | live | carry-forward, per 8.5 |
| C | The organization's central or headquarters publication for the period | cached behind a validity date | the cross-check and the fallback, NEVER the starting point |
| D | ISSUED BELOW THE READER AND SWEPT UP, by the downward sweep of 8.4.1, which fires at the top of the ladder and nowhere else | live, same windows as A | LAST, after C, and it is not an instruction to the reader at all |

**BAND D IS NAMED HERE BECAUSE 8.4.1 CREATED A FOURTH KIND OF DIRECTION AND THE
PRIORITIES SECTION IS ORDERED BY BAND.** 1.2.2 sorts that section by source band
first, and on a top-of-house run half its rows can come from the downward sweep;
an unnamed band leaves half the section with no defined value on the primary sort
key, so the ordering of half the reader's priorities rests on a decision nobody
made and two runs need not agree. **Band D sorts LAST, after C**, and the reason is
stated rather than left to taste: bands A, B and C are direction ADDRESSED TO the
reader, in descending authority over their own period; a direction swept up from
below is not addressed to them at all, is classified under 8.7 as an ASSIGNMENT
in every case where its actor is somebody else, and carries no mandatory status,
no source boost and no multiplier. **A row that moves no rank does not lead a
section that exists to say what the reader must do.** The band is printed in the
reason-for-rank cell like every other sort key, so a reader who sees a direction
from their own branch manager above one from their director can see which key put
it there.

Plus the standing hierarchy in CREDITABLE_ENTITIES, which is not a message but a
weight, applied in PART 12.

PRIORITY_SOURCES holds the bound set and PRIORITY_SOURCE_COUNT its size, at
least two. SOURCE_AUTHORITY_MAP maps QUESTION to the one artifact that settles
it, never a ranking of documents. SD-PRI-32. The seven questions: who defines
the deliverable form; who defines the goal methodology; who defines the quality
bar; who defines strategy; who defines priority ranking; who defines local
targets; and what counts as evidence.

## 8.1 Sweep everything by SENDER. Never filter the sweep by keyword.

SD-PRI-02. RETRIEVE EVERY MESSAGE FROM EVERY MANAGER IN THE CHAIN, FROM EVERY
FOLDER IN MAIL_SWEEP_FOLDERS INCLUDING THE DELETED-ITEMS EQUIVALENT, OVER BOTH
BOUND WINDOWS, EVERY RUN. NO KEYWORD FILTER. NO EXCEPTIONS.

Filter by SENDER only. Read the subjects yourself. A keyword search runs
afterward only as a SUPPLEMENT, to catch other senders quoting a manager.

The documented failure: a keyword search returned one message; a sender search
on the same mailbox and window returned twenty-two. The keyword search missed
roughly ninety-five percent of the supervisor's direction, and every missed
message was more on point than the one it found. The reason generalizes cleanly:
real managers do not write in planning vocabulary, and a keyword list built from
how a specification talks will never match how a manager talks.

Windows: SUPERVISOR_SWEEP_WINDOW_CURRENT days back for the current period, and
SUPERVISOR_SWEEP_WINDOW_PRIOR days back for the carry-forward sweep.

## 8.2 Classify by CONTENT, not by keyword and not by length. When in doubt, KEEP.

SD-PRI-03. A message is DIRECTION when it does any one of: names units to cover;
names work to do; states what matters this period; sets or restates a target;
forwards or attaches a list; or repeats direction from further up. It is
discarded only when it does NONE of those and is purely conversational or
administrative.

Never discard on the subject line alone. Report the count swept, the count read
as direction, and the count discarded with a one-word reason each. Reading one
extra logistics message costs nothing; discarding a one-line list of twelve
units that need attention costs the plan.

Reading and acting are two separate decisions. SD-PRI-05. Sweep everything;
direct selectively. The longer window is always read into the inventory; its
lists become directives only under the carry-forward rule.

## 8.3 Never conclude an absence from the wrong instrument

SD-PRI-04. "No supervisor communication" requires the SENDER search to have
returned ZERO messages. If it returned messages and none read as direction, say
THAT instead, naming the count retrieved and the window covered.

## 8.4 Walk the chain upward, and weight by distance

SD-PRI-06. Resolve up to CHAIN_WALK_DEPTH levels or until the chain returns
empty. Search each level. Weight by CHAIN_DISTANCE_WEIGHTS, whose first entry is
1.00 and whose values strictly decrease. These weights are not decoration: they
SCALE the source boost inside the scoring formula.

Where levels disagree, follow the IMMEDIATE supervisor and name the
disagreement, because the nearer manager knows the units.

Record EVERY level, including the ones that published nothing. SD-PRI-07. A
level that published nothing is a normal result and is not a missing supervisor.
Record "resolved, no communication found this period" against that person by
name. A reader must be able to SEE that the chain was walked, not assume it.

### 8.4.1 The top of the house, whose upline is empty by construction

**THE SWEEP WALKS UPWARD, AND EXACTLY ONE PERSON IN AN ORGANIZATION HAS NOBODY
ABOVE THEM.** SD-IDN-02. For that reader 8.1 retrieves nothing, 8.4 resolves no
levels, 8.5 has no manager to evaluate and 8.6 has no list to admit, so the
directed section is empty BY CONSTRUCTION rather than by evidence. On a real run
that shipped a head of an organization an empty directed section in a month when
nine unit-level directives had been issued inside their own scope, by their own
subordinate managers, naming nine units by identifier. **The most senior reader in
any organization was getting the thinnest priority handling of anybody, and no
gate fired, because a zero produced by an empty chain is indistinguishable from a
zero produced by a quiet one.**

**THE RULE: WHERE THE READER SITS AT THE TOP OF THE RESOLVED ROLE_LADDER, THE
SWEEP ADDITIONALLY READS DOWNWARD EXACTLY ONE LEVEL.** One level, not the whole
subtree: one level is a standing value of this method, stated once, here, and the
reason is that a head of an organization needs to see what their own direct
managers are directing, not to inherit every instruction issued anywhere beneath
them. The downward sweep is the same sweep: by SENDER, no keyword filter, both
bound windows, every folder, per 8.1, run over the people whose ROLE_LADDER
scope_level sits one level finer than the reader's own and whose scope sits inside
the reader's.

**WHAT COMES BACK IS CLASSIFIED BY 8.7's ACTOR TEST, WITH ITS RECIPIENT RESOLVED
BY 8.7.1 FIRST, AND THAT PAIR IS WHAT KEEPS THE THREE KINDS APART.** SD-PRI-12,
SD-DUP-02. The actor test is already line-independent and already runs on every
list at every level; this rule gives it one more set of messages to run on and
changes nothing about how it decides. **What it does change is that a message the
downward sweep found was never addressed to the reader**, because the sweep
searches by SENDER among people below them, so 8.7's `names no actor at all`
clause can never resolve to the reader here and 8.7.1's ladder runs on every row
this sweep returns, without exception.

| What the downward sweep found | Reading | Where it goes |
|---|---|---|
| A direction ISSUED TO the reader by somebody below them, which is unusual but happens: a compliance officer, a controller or a specialist function writing upward, and which 8.7.1 rung 1 resolves to the reader by name, role or scope | DIRECTIVE, exactly as 8.7 already reads it, because the recipient IS the actor and the actor IS the reader | The ordinary directive path. It is weighted like any other directive and its source boost is scaled by the chain-distance weight of the level it came from, per 8.4 |
| A direction issued BY a subordinate manager TO THEIR OWN PEOPLE, naming units inside the reader's scope, where a person or role is named | **ASSIGNMENT**, because the message names another person or role as the one who will work the items | The assignment path of 12.9 and SD-DUP-03, and NOWHERE ELSE |
| A direction naming units inside the reader's scope and NAMING NOBODY, which is what a directive register with a sender column and no recipient column produces | **ASSIGNMENT**, on 8.7.1 rung 2 where the unit's owner resolves to somebody other than the reader, and on rung 3 where no actor resolves at all, in which case it is additionally reported as unresolved | The same assignment path, and NOWHERE ELSE. It never reaches the directed section and never takes MANDATORY_MULTIPLIER |

**AN ASSIGNMENT FOUND THIS WAY NEVER GAINS WEIGHT, AND THAT IS THE WHOLE OF THE
SAFETY OF THIS RULE.** SD-DUP-03 already says what happens to an assignment on the
senior line: it is IDENTIFIED and REPORTED and NOT WEIGHTED, because it is the
reader's own deployment showing up in their own report and what they must not see
is those units pushed around the ranking for it. So, exactly and without
exception:

- It confers NO mandatory status. SD-MND-01 is untouched: a unit becomes mandatory
  only when a message names specific units TO THE READER, and a manager's list to
  their own team is not that. The directed section is not populated from the
  downward sweep.
- It confers NO source boost, NO narrowness multiplier and NO own-action
  multiplier. It enters no term of 12.1 and moves no rank. SD-DUP-01 already
  forbids the coverage-duplication discount on the aggregate tier, which is the
  same units seen from the other side; this rule adds nothing in the opposite
  direction either.
- It changes NO count that sizes a section, NO cap and NO percentile denominator.

**WHAT THE READER ACTUALLY GETS, AND IT IS THE POINT OF THE RULE.** Three places,
and all three ship:

1. **On the ROW.** Every unit named by a downward assignment carries, in its
   narrative column, one clause naming WHO assigned WHAT to WHOM: the subordinate
   manager who issued it, the person or role it was issued to, the date, and the
   instruction's own wording quoted as the sender wrote it, per SD-LNG-07. The row
   keeps whatever merit rank it earned, unchanged.
2. **On the PRIORITIES section.** Every downward direction is published there like
   any other, quoted verbatim with its sender and date, with HDR_DIRECTIVE_STATUS
   saying it was read and recorded as an assignment rather than applied as a
   directive, and the reason. SD-PRI-16's discipline applies unchanged to one that
   matched no row.
3. **On the front panel and in the Method section.** One line naming how many
   directions the downward sweep found, from how many managers, covering how many
   units in scope, and stating plainly that none of them moved a rank.

**AND THE ZERO STILL SHIPS.** Where the downward sweep finds nothing, the artifact
says the sweep RAN, over which managers, over which windows, and returned nothing,
exactly as 8.4 requires of every level of the upward walk. A zero is the evidence
the check ran, and it is the difference between a top-of-house reader whose
subordinates issued no direction and one whose report never looked. SD-PRI-04's
instrument rule applies here in full: "no direction from below" requires the
SENDER search to have returned zero messages.

**THE RULE FIRES ON THE TOP OF THE LADDER AND NOWHERE ELSE.** A reader with a
supervisor gets the upward sweep and only the upward sweep, because the units their
own subordinates were assigned are already covered by 12.9's de-duplication on the
direct line and by SD-DUP-03 on the aggregate line, and because a downward sweep at
every level would turn every manager's report into a digest of their whole subtree.
Where the reader's position at the top is SELF-REPORTED rather than resolved from a
directory, per 5.1, the rule still fires and the artifact names the evidence the
top-of-house finding rested on.

## 8.5 Carry-forward is evaluated MANAGER BY MANAGER, and the narrower test runs first

SD-PRI-08. Three ordered rules. Stop at the first that fires. Evaluate them per
manager, not once for the whole chain.

| Order | Condition | Effect |
|---|---|---|
| Rule 1 | Published this period AND signalled continuation | The lookback runs and the recovered list is directed at FULL weight |
| Rule 2 | Published this period with NO continuation signal | Nothing older carries forward |
| Rule 3 | Published nothing this period | The prior period carries forward IN FULL |

The continuation test is rule 1 and that ordering is LOAD BEARING: a manager who
published this period AND said the priorities continue satisfies the conditions
of BOTH rule 1 and rule 2, so the narrower test must run first. Putting the
plain current-direction test first would swallow every carry-forward case and
the continuation rule would never fire at all. Rule 2 prevents reaching past a
current instruction to revive an older one.

**Rule 2 is the rule an implementer will skip, and this sentence exists because
of it.** SD-PRI-09. Two independent runs split precisely on the middle rule and
produced different top tens off identical data. Where one rule in a ladder is
the one most likely to be dropped, say so explicitly in the text, with the
evidence. That is a documentation practice, not a computation, and it is
doctrine.

A mandatory item's weight never decays with the age of the instruction.
SD-PRI-10. Carry-forward is a yes-or-no ADMISSION test, not a discount. Once
admitted, the items carry full weight. Do not invent a partial weight for older
direction: either the list is live or it is not.

## 8.6 Any list from anyone in the chain is a must-cover

SD-PRI-11. A manager who sends a list of units is telling the person to cover
those units. That is the default reading and it needs NO keyword to activate it.
Requiring a trigger phrase requires vocabulary the sender never uses.

The ONLY thing that releases an item is an explicit instruction not to cover it,
matched against DIRECTIVE_RELEASE_PHRASES. Nothing else releases an item.

## 8.7 The ACTOR TEST, before treating a list as a directive

SD-PRI-12. The test is WHO the message names as the ACTOR, and it is the only
test. ACTOR_TEST_ENABLED must be true.

| The message | Reading |
|---|---|
| Names another person or role as the one who will work the items | ASSIGNMENT. Routes to the de-duplication weight in PART 12.9. |
| Names the recipient, or names no actor at all, including a bare list with no framing, **AND WAS ADDRESSED TO THE READER**, per 8.7.1 | DIRECTIVE |
| Carries NO addressing evidence at all, because it was read out of a register or swept from below rather than received | **UNDECIDED AT THIS TABLE.** 8.7.1 resolves the recipient before this table is read, and this table then runs on the resolved answer |

Two independent runs against the same mailbox split on exactly this message, and
the one that read it as a directive inverted the weighting on those units by a
factor of four. The rule is fully universal and belongs in any skill that reads
instructions out of prose.

Classification is line-INDEPENDENT; only the WEIGHT is gated. SD-DUP-02. Run the
actor test on every list at every level, so a directive is never mistaken for an
assignment on a senior report either. The classification decides which SECTION;
the line decides whether the multiplier applies.

When in doubt, treat it as DIRECTED. SD-PRI-13. The cost of covering a unit the
manager mentioned in passing is ONE UNIT OF ATTENTION; the cost of missing a unit
they expected covered is the person's credibility with their boss. An
asymmetric-cost tie-break.

**AND SD-PRI-13 IS A TIE-BREAK ABOUT WHETHER TO COVER A UNIT, NEVER ABOUT WHO
MUST ACT.** Read as the second it inverts its own cost argument: covering a unit
the manager mentioned in passing costs one unit of attention, but treating nine of
a subordinate's instructions as the reader's own mandatory work costs the reader
their first nine actions of the period and pushes everything they actually own
below them. 8.7.1 states where each reading applies, and neither doubt is resolved
by guessing.

### 8.7.1 THE RECIPIENT IS RESOLVED, NEVER ASSUMED, WHERE THE SOURCE CARRIES NO RECIPIENT

**THE GAP THIS CLOSES, MEASURED ON A REAL RUN AT THE TOP OF A HOUSE.** A directive
register carried one row per direction with columns for the sender and the
sender's role and NO RECIPIENT COLUMN. Nine directions, issued by two managers one
level below the reader, each naming a unit. 8.4.1 swept them upward correctly.
8.7's table was then asked which of its two rows they fell in, and neither fitted:
they named no other person, so the ASSIGNMENT row did not match, and they named no
recipient either, so the run took the second row's `names no actor at all` clause
and read all nine as DIRECTIVES for the reader. **The result was measured in the
published file: the head of the organization opened his plan and the first section
telling him to do anything was nine tasks belonging to people two levels down,
every one of them carrying MANDATORY_MULTIPLIER, the single highest score in a
190-unit workbook among them, and the directed section sitting ahead of the first
action list in the section order.** Nothing was a wrong number. The whole plan was
wrong, and it was wrong silently.

**THE RULE. WHERE A DIRECTION CARRIES NO STATED RECIPIENT, THE ACTOR IS RESOLVED
BY THE LADDER BELOW BEFORE 8.7's TABLE IS READ. IT IS NEVER ASSUMED TO BE THE
READER.**

**FIRST, THE TEST THAT DECIDES WHICH DOUBT THIS IS.** A direction carries
ADDRESSING EVIDENCE when any one of these holds, and 8.7's table runs unchanged on
it, `bare list with no framing` included, exactly as SD-PRI-12 states:

1. It arrived in the reader's own mailbox, addressed to them, on any rung of 8.1.
2. It names the reader, their role or their scope as the addressee.
3. The source carries a recipient field, an addressee, a salutation or a
   distribution list, and the reader is on it.

**A direction carrying none of the three has NO addressing evidence**, and there
are exactly two ways this happens in practice: it was read out of a REGISTER, a
file or a document that lists directions with their senders and no recipients; or
it was found by the DOWNWARD SWEEP of 8.4.1, which searches by SENDER among people
BELOW the reader and therefore cannot, by construction, have found a message
addressed to the reader at all. In both cases the reader's name is not evidence of
anything, because the reader is not in the record.

**THEN THE LADDER, IN ORDER, STOPPING AT THE FIRST RUNG THAT RESOLVES:**

| Rung | What is read | The actor it yields |
|---|---|---|
| 1 | An explicit recipient, addressee or named role INSIDE the direction's own wording, matched as normalized text | that person or role |
| 2 | The OWNER OF THE UNIT the direction names, read from the same scope or owner column the population is built on, per the scope concepts of REFERENCE 3 and 5.3 | the resolved owner |
| 3 | Nothing resolved | **UNIDENTIFIED**, which is a stated outcome and not a default |

**AND THE READING THAT FOLLOWS FROM EACH, WHICH IS 8.7's TABLE RUN ON A RESOLVED
ANSWER RATHER THAN ON A GUESS:**

| The resolved actor | Reading | What it may carry |
|---|---|---|
| THE READER | DIRECTIVE | Everything a directive carries: mandatory status, the directed section, the source boost, and MANDATORY_MULTIPLIER on the finished score per 12.8 |
| ANYBODY ELSE, including a subordinate, a peer, the sender themselves, or a role | **ASSIGNMENT** | Nothing that moves a rank. It goes where 8.4.1 already sends an assignment: the priorities section, the row's narrative clause, and the front-panel and Method lines, per 12.9 and SD-DUP-03 |
| UNIDENTIFIED | **ASSIGNMENT, and additionally reported as unresolved** | The same as above, plus the direction is published on the priorities section with the closed-set status saying it was recorded and not applied and the reason naming that no actor could be identified |

**THREE STATEMENTS THAT ARE THE WHOLE SAFETY OF THIS RULE, AND EACH IS ABSOLUTE:**

1. **OWNERSHIP OF A UNIT IS NOT EVIDENCE OF ADDRESSING.** Rung 2 resolves who is
   likely to ACT, and that is all it resolves. An instruction to re-quote the unit
   with a stated identifier, written by a manager who owns the part of the
   organization that unit sits in, could be an instruction to the person who owns
   the unit or a note to himself, and the ownership column cannot tell those
   apart. What rung 2 settles is that the actor is
   somebody OTHER THAN THE READER, which is the only question the weighting turns
   on. Where rung 2 resolves the owner AS the reader, on their own unit, the
   direction is a DIRECTIVE and takes the ordinary path.
2. **MANDATORY_MULTIPLIER NEVER APPLIES TO A DIRECTION WHOSE ACTOR IS NOT THE
   READER, AND NEVER APPLIES TO ONE WHOSE ACTOR COULD NOT BE IDENTIFIED.** Not at
   a reduced value, not at the floor, not once. The multiplier is what says the
   reader was told to do this, and a direction that named somebody else, or named
   nobody, did not say that. SD-WGT-04 is untouched: what changes is which rows
   are in the set it multiplies.
3. **THE DIRECTED SECTION IS POPULATED ONLY BY DIRECTIVES.** SD-MND-01 already
   says a unit becomes mandatory when a message names specific units TO THE
   READER, and an assignment is precisely a message that does not. A run whose
   directed section holds a row placed there by an assignment fails at 18.1.

**WHAT THE READER GETS INSTEAD, BECAUSE NOTHING IS DROPPED.** Every one of these
directions is still published, in the three places 8.4.1 already names: quoted
verbatim on the priorities section in band D with its sender, its date, its status
and its reason; as a clause in the narrative of every unit it names, saying who
directed what to whom; and as one line on the front panel and in the Method
section naming how many were found, from how many senders, over how many units in
scope, and stating plainly that none of them moved a rank. **The reader of the
whole house learns exactly what their managers are directing, which is what they
need, and does not inherit it as their own homework, which is what they were
being given.**

**WHY RUNG 2 RATHER THAN A FLAT REFUSAL.** Refusing to resolve at all and calling
every unaddressed direction UNIDENTIFIED would be safe and would throw away a real
answer: on the run that produced this rule, every one of the nine named a unit
whose owner resolved cleanly, and naming the owner is what let the report say WHO
was expected to act rather than only that the reader was not. Both branches end in
the same weighting, so the extra rung costs nothing and buys the reader a name.

## 8.8 Matching a named item to a row

SD-PRI-14. A stated ladder, in order: identifier if present; then name plus
locality; then name plus address; then name alone when unique in scope. Compare
as normalized TEXT. **Those four rungs match a direction that NAMES a unit. A
direction that names a CLASS of units by a testable rule takes the FIFTH rung in
8.8.1, which runs only after all four of these have matched nothing, produces a
PREDICATE match rather than a NAMED one, and carries an action without conferring
mandatory status, a source boost or any movement in the ranking.**

Any named item that cannot be matched is listed with a BLANK rank and a note
from MSG_UNMATCHED_MANDATORY, and the count is repeated in the opener. A
directive the user cannot see was received is worse than one that arrives with a
gap in it.

**Never infer an item's identity from an aggregate.** SD-PRI-15. A message
reporting a count, a percentage or a summary figure without naming an item has
not named one. Do not reverse-engineer which row it must have meant, however
uniquely it appears to resolve. Two runs against the same mailbox will infer two
different units and both will look confident. That is confident non-determinism.

Unresolvable direction is SURFACED and changes nothing about the ranking.
SD-PRI-16. Record it with a blank identifier and the quoted wording, report it
in the opener, and leave the merit ranking untouched.

### 8.8.1 A direction that names a CLASS of units, by a testable predicate

**A DIRECTION THAT NAMES NO UNIT AND STATES A TESTABLE RULE OVER A RESOLVED COLUMN
IS MATCHED TO EVERY ROW THAT SATISFIES THE RULE.** This is the FIFTH rung of
8.8's ladder, it runs only after all FOUR of the named rungs have been tried and
have matched nothing, and it produces a PREDICATE MATCH, which is a strictly
weaker thing than a NAMED match.

**THE FAILURE IT CLOSES, and it emptied a whole column on a real run.** An
organization published three priorities for a period. Each one named an explicit
action and each one stated a rule over a column sitting in the same file: units
carrying exactly one of something; units whose commitment date falls on or after a
stated date; units carrying open service items. None of the three named a unit,
because that is not how a priority document is written, so none of them could be
matched by any rung of the ladder, so none supplied an action to any row, so every
merit row on a document called a work plan fell through to the standing absence
text and the reader was told the next step was theirs on all of it. The direction
was not vague. It was PRECISE, in a form the ladder had no rung for.

**AND IT DOES NOT WEAKEN SD-PRI-15, WHICH IS THE RULE THIS RUNG WILL BE ACCUSED OF
BREAKING.** SD-PRI-15 forbids inferring an ITEM'S IDENTITY FROM AN AGGREGATE: a
message reporting a count, a percentage or a summary figure has not named a unit,
and reverse-engineering which row it must have meant is confident
non-determinism, because two runs infer two different units and both look
confident. This rung infers NOTHING. The direction states the rule itself, in its
own words; the run evaluates that rule against a column; every row satisfying it
is matched and every row not satisfying it is not; and two runs on one file return
the same set every time. **A stated rule is evidence. A summary figure is not, and
this rung never reads one.** Where a direction gives only a count, a share or a
summary, it is NOT a predicate, it takes no rung, and SD-PRI-15 governs unchanged.

**THE ADMISSION TEST. All four must hold, and a failure of any one is reported
rather than worked around:**

1. **The direction states a CONDITION over units, in its own words**, of the form
   an attribute compared with a value or a range: equal to, at least, at most,
   before, on or after, greater than zero, present, absent, one of a named set. It
   is not a count of units, not a share of a population, and not a summary figure
   about the period.
2. **The attribute RESOLVES to exactly one column**, through reference/field-resolution.md
   and the COLUMN_CONCEPT_DICTIONARY, by the same value checks every other column
   resolution uses. The strict exact-only rule and the forbidden-neighbour rule
   apply here exactly as they do everywhere else: a near miss is a miss.
   **THE ROUTES ARE ORDERED, THEY ARE TRIED IN THIS ORDER, AND THE ROUTE USED IS
   RECORDED PER PREDICATE.** An earlier statement of this test said only that the
   attribute resolves "by the same three passes", which can be read two ways, and
   the two readings differ by a third of the priorities on a real file: one run
   resolved 1 of 3 published priorities and put a predicate-derived instruction on
   69 of 190 rows, the other resolved 2 of 3 and reached 106 of 190, off one skill
   and one input, and neither was detectably wrong. The order is stated so that
   cannot happen again:

   | Route | What is matched against what | When it is tried |
   |---|---|---|
   | a. THE CONCEPT ROUTE | the attribute's words are resolved to a CONCEPT, and that concept's already-resolved column is taken | FIRST, always |
   | b. THE HEADER ROUTE | the attribute's own words are run through the three passes DIRECTLY AGAINST THE HEADER TEXT of the source, with the same normalization, the same short-string guard and the same value check | ONLY where route a resolves the attribute to no concept |
   | c. THE PROVISIONAL ROUTE | reference/field-resolution.md 7.4a, whose first test is a concept needed for a named decision and names the attribute of an admitted direction in those words | ONLY where routes a and b both fail, and only where all six of 7.4a's tests pass. It is barred outright for a `strict_exact_only` concept, per 7.4a test 2 |
   | d. THE SIBLING SET ROUTE | reference/field-resolution.md 7.4b, where route c stalled at 7.4a test 5 because N columns tied, and those columns PARTITION the concept by mapping one to one onto the members of a set THIS RUN ADMITTED, which is the ordinary shape of a keyed evidence file | ONLY where route c reached test 5 and tied, and only where all five of 7.4b's tests hold as well as 7.4a's other five. The concept then resolves PER MEMBER, every figure names its member, and no rollup is invented |

   **The route used is printed beside the predicate on the priorities section and
   in the Method section**, with the column it reached, so two runs can be compared
   line by line rather than only in their totals. A predicate resolved by route b
   is not weaker than one resolved by route a and takes exactly the same
   consequences; what differs is only that a reader can see the organization
   writes its priorities in a word the dictionary does not carry, which is a
   binding gap worth one line to the binding owner. A predicate resolved by route c
   additionally carries 7.4a's own two-place disclosure, MEDIUM confidence, and its
   absolute bar on writing anything back to the dictionary. **A predicate resolved
   by route d carries all of that plus 7.4b's own four further disclosures, and it
   is recorded as ONE adoption of the set rather than as N**, because the columns
   stand or fall together and N records would hide that. **Route d is the route a
   published requirement set most often takes**, since an organization names its
   evidence columns after its own numbered requirements, and it is the route that
   was missing when a file answering a requirement row by row reached no row at
   all.
3. **The comparison is EVALUABLE against that column's resolved shape token**: a
   date comparison against a DATE column, a magnitude comparison against
   COUNT_OR_MEASURE or RATE_OR_PROPORTION, a membership comparison against
   STATUS_OR_CATEGORY, IDENTIFIER_OR_CODE or BOOLEAN_LIKE. A magnitude comparison
   demanded of a free-text column is not evaluable.
4. **The direction also names an ACTION**, because that is what the rung exists to
   carry. A predicate with no action names a class and asks for nothing; it is
   recorded on the priorities section as read and unapplied, and it supplies
   nothing to any row.

**WHERE IT FAILS, IT FAILS LOUDLY AND NEVER SILENTLY. G2.** A direction that
states a predicate whose attribute resolves to NO column is the case that must
never pass quietly, because the run has in hand an instruction it can read and
cannot execute. The direction is published on the priorities section, quoted
verbatim, with HDR_DIRECTIVE_STATUS carrying the closed-set value that says it was
recorded and not applied; the Method section names the concept the predicate asked
for, the routes of test 2 that were run, the columns that were considered and why
each was rejected; and it is raised as ONE OPEN QUESTION addressed to
BINDING_OWNER_NAME, because a concept the organization writes its priorities in
and the dictionary does not carry is a binding gap and is fixed in one line. The
same treatment applies where the attribute resolves to MORE THAN ONE column, which
is ambiguity rather than absence, and where the comparison is not evaluable against
the resolved shape token. **In none of those cases does the run guess a column,
widen a comparison, or fall back to matching the direction against every row.**

**AND THE UNEVALUATED DIRECTION IS ANNOUNCED WHERE THE DECISION LIVES, NOT ONLY IN
THE AUDIT.** reference/field-resolution.md 6.5 states the general rule in those words and
7.7 states the audit line that is necessary and not sufficient. For this skill the
decision lives on the PRIORITIES SECTION, so:

- **ITS OWN ROW, ON THE PRIORITIES SECTION, EVERY RUN.** The direction is not
  folded into another row, not summarized in a count and not left to the Method
  section. It takes a position in the 1.2.2 order like every other direction, its
  instruction quoted verbatim, its status from the closed set, and its
  reason-for-rank cell naming the keys that placed it exactly as every other row's
  does.
- **THE REASON IS IN THE CELL, NOT IN A FOOTNOTE.** Beside the status, in the
  reader's own words per SD-LNG-07: what the predicate asked for, that no column
  of this source answers it, the closest candidate column by header and the test it
  failed, and that the priority was therefore NOT ATTEMPTED rather than attempted
  and found empty. **A zero and a not-attempted are different facts and the
  artifact never prints one for the other.**
- **THE SECTION'S NOTE BAND CARRIES THE COUNT**, per 1.6.1 note 10, so a reader
  who scans the band before the rows sees that some of what they published could
  not be tested.
- **THE COUNT IS NOT ZERO-SUPPRESSED.** Where every admitted direction was
  evaluated, the line says so, because a zero is the evidence the check ran.

**WHY THIS IS A SECTION-LEVEL OBLIGATION AND NOT AN AUDIT ONE, MEASURED.** An
organization published three priorities for a period and its FIRST one could not be
evaluated, because the quantity it was phrased in resolved to no column. The run
disclosed it correctly, in the Method section, seventy rows down, as a zero in a
source count. The head of the organization opened his plan and nothing on it told
him that his own first priority for the period had not been attempted. **An
unevaluated priority is a fact about the plan, not a footnote about the method.**

**WHAT A PREDICATE MATCH IS, AND EVERY WAY IT IS WEAKER THAN A NAMED MATCH:**

| | A NAMED match, rungs 1 to 4 of 8.8 | A PREDICATE match, this rung |
|---|---|---|
| Confers mandatory status | YES, per 8.6 and SD-MND-01 | **NEVER.** SD-MND-01 is untouched: a unit becomes mandatory only when a message NAMES specific units, and a rule over a column is exactly the aggregate pointing SD-MND-01 refuses to convert into a unit-by-unit callout. The directed section is never populated from this rung |
| Confers a source boost | YES, per 12.7 | **NEVER.** The row's source boost is unchanged, at whatever value the named sources gave it, and SOURCE_BOOST_NONE where none did |
| Takes NARROWNESS_MULTIPLIER or OWN_ACTION_MULTIPLIER | Where its own test fires | **NEVER, on either.** Neither multiplier is reachable from this rung |
| Moves the rank | Through the alignment term | **NEVER.** No term of 12.1 reads it, no percentile denominator changes, no section size changes and no cap changes |
| Supplies HDR_ACTION | YES, at precedence 1 | **YES, and this is the only thing it does.** It enters the precedence table of 1.3b at source 1b, and where a NAMED directive also supplies an action for the same row the named one wins outright |
| Survives the compliance gate | Must, per 9.2 | Must, identically. A predicate inside a direction the gate held back supplies nothing, per 9.2 and the held-back rule in 1.3b |

**HOW IT IS SHOWN, AND THE READER CAN CHECK EVERY PART OF IT.** Three places:

1. **On the ROW.** The action cell carries the direction's action clause quoted as
   the sender wrote it, per SD-LNG-07, and the narrative names that the row was
   matched by PREDICATE rather than by name. A reader can always tell which of the
   two put an action on their row.
2. **On the PRIORITIES section.** The direction is published like any other, and
   its status column carries the PREDICATE VERBATIM as the direction stated it,
   the column it resolved to by that column's own header, and the MATCH COUNT: how
   many rows of the ranked population satisfied it, out of how many. Printing the
   predicate beside its count is what lets a reader check the rule rather than
   trust it, and a count that looks wrong is then traceable to a rule they can
   read in one line.
3. **On the front panel and in the Method section.** One line per predicate,
   naming the predicate, the resolved column, the count matched and the statement
   that a predicate match carried an action and moved no rank. The Method section
   additionally records the resolution evidence for the column, so a wrong column
   is visible rather than invisible.

**A PREDICATE MATCHING MOST OF THE POPULATION IS STILL REPORTED, AND IT IS STILL
ONLY AN ACTION.** There is no breadth ceiling on this rung, because there is
nothing to protect: 8.12's breadth limit exists to stop a broad flag conferring
CENTRALLY NAMED status and the weight that comes with it, and this rung confers no
status and no weight at all. What a broad predicate produces is the same action
text on many rows, which is a uniform column, which 1.3b already detects on the
full ranked population AND per rendered section and reports in one prominent line.
The reader is told, once, that the organization asked for the same thing
everywhere, which is a true and useful finding rather than a defect.

**THE DIRECTION TIE-BREAK CHAIN, STATED ONCE HERE AND CITED FROM EVERYWHERE
ELSE.** It resolves two directives naming an action for one row, two predicates
matching one row, and a directive against a predicate; 1.3b's precedence table
cites it and does not restate it, and 1.2.2's sort of the priorities section
continues into its last two keys. **FIVE KEYS, IN ORDER, AND THE CHAIN IS TOTAL:**

| # | Key | Direction | Why it is a key at all |
|---|---|---|---|
| 1 | CHAIN DISTANCE, by the CHAIN_DISTANCE_WEIGHTS entry 8.4 resolved | nearest namer first | The nearer manager knows the units, which is 8.4's own reason |
| 2 | THE DIRECTION'S OWN DATE | most recent first | A later instruction from one sender supersedes an earlier one |
| 3 | THE SENDER IDENTIFIER | ascending | Deterministic across two senders at one distance on one date |
| 4 | **POSITION WITHIN THE SOURCE DOCUMENT** | earlier first | A numbered list is already its author's own ordering, and honouring it costs nothing and reproduces what the sender meant |
| 5 | **THE SOURCE DOCUMENT'S OWN TITLE OR FILENAME** | ascending, compared as normalized text | Terminates the chain across two documents from one sender on one date |

**KEYS 4 AND 5 ARE NOT AN EXOTIC CASE; THEY ARE THE COMMONEST INPUT THIS METHOD
WILL EVER SEE.** On a real run, priorities 2 and 3 came from one sender, in one
document, on one date, at one chain distance. Keys 1 to 3 all tied. Twenty rows on
one workbook and seven on another satisfied both predicates, and the chain was
exhausted with the run still holding two candidate action clauses and no rule to
choose between them. A single priorities memo with several numbered priorities is
the NORMAL SHAPE of the input to this skill, so a chain that stops at key 3 stops
on the ordinary case rather than on the edge case. **Where even key 5 ties, which
means one document listed one priority twice, the run takes the first occurrence,
records that the chain was exhausted, and names both occurrences in the Method
section**, because a chain that can exhaust must say so rather than pick silently.

Every predicate that matched the row is still named in the narrative and still
counted on the priorities section; what the tie-break decides is only which action
clause the cell carries.

## 8.9 An attached list is the highest-value object in the mailbox

Retrieving an attached list is MANDATORY WORK, not best effort. SD-SRC-01. Run
the full retrieval ladder for EVERY attachment on EVERY message from EVERY
manager, retrying each path at least twice before moving to the next. Failing to
open an attachment is not a reason to report no direction; it is a reason to try
the next retrieval path. A list from the user's own manager outranks every other
input this method reads.

Never decide from a subject line whether a message carries a file. SD-SRC-07.
Enumerate attachments on every candidate message; the attachment filename is
often the real content even when the subject says nothing.

An encoded size is not a file size. SD-SRC-08. A reported attachment size is
roughly MIME_ENCODING_FACTOR times the real file. Never use it to decide a file
is too big to fetch.

A spilled response is not an empty response. SD-SRC-09. Where a tool writes a
large result to a file rather than returning it, READ THE FILE. A run that
treats a spilled response as empty will report no mail from a manager who wrote
twenty messages.

Do not select a field you were told to read; request the resource and read the
payload out of what comes back. SD-SRC-05. Reading a field name in the
documentation and then asking for it by name is the single most common way this
step fails, and it has failed a real run. The resulting error text then points at
a call that returns metadata only, so a reader who follows it loops and concludes
the attachment is unreachable.

The same address is correct STREAMED and corrupt DECODED AS TEXT. SD-SRC-06. A
raw-bytes endpoint handed to a streaming file reader is the primary method. The
difference is whether the bytes are streamed to a file or decoded as text.

FORBIDDEN_RETRIEVAL_PATHS enumerates the approaches that look reasonable, were
tested, and fail, each with its failure mode named. SD-SRC-04. At least one of
them does not error at all and silently corrupts a large share of the bytes: the
file appears retrieved, opens as garbage or fails to open, and nothing in the
response says why. The documentation pattern of enumerating the
plausible-but-wrong approaches, and naming which one fails silently, is itself
doctrine and survives whatever the specific paths become.

A file referenced rather than attached is resolved by filename in the document
store, but a file sent hours ago will NOT be in search yet; do not conclude from
a search miss that it does not exist. SD-SRC-10.

Asking the user to fetch it is the LAST step, and it names everything attempted:
the filename, the sender, the date and every path tried. SD-SRC-11. Never ask
the user to fetch something the skill can read. SD-SRC-12. Asking a manager to
go fetch a document is the kind of friction that gets a tool abandoned.

## 8.10 THE RETRIEVAL GATE

SD-SRC-02. Before writing the directed section, confirm for EVERY detected
attachment on a supervisor or upline message that exactly one of three is true:

1. It was read and folded into the ledger.
2. It was read and contains nothing in scope, which is stated in the
   verification list.
3. It could not be read after the FULL ladder, in which case the run does NOT
   report zero. It names the file, the sender and the date, states every path
   attempted, and says plainly in the opening summary that a named source could
   not be opened and the directed ledger is therefore incomplete.

A count of zero directives is only ever a valid result when NO manager sent a
list. The general form: a zero must be provably a REAL zero, not an unattempted
one. This is the single most damaging retrieval failure, because a clean-looking
report that silently omits the boss's instructions is indistinguishable from a
correct one.

A partial recovery is treated as partial, but a partial FETCH is not the same as
partial DATA. SD-SRC-03. Report a partial recovery by name and treat only what
was read as directed. But FIRST reconcile the recovered row count against any
per-group count the message body prints; when they agree exactly, the list is
complete for scope and should be reported as complete, with a note about how the
recovery was confirmed. A real file declared thousands of rows and carried a
hundred and twenty-three real ones, so a truncated fetch recovered one hundred
percent of the actual data.

## 8.11 The central source is never optional and never a reason to stop

SD-SRC-13. Read it every run. A search that comes back empty means the exact
folder was not matched, not that nothing was published. Walk the fallback
ladder: the target period's publication, then the current period's, then the
most recently published one, dated honestly. Only an unreachable library falls
back to supervisor priorities alone, with the artifact prominently labelled.

A publication one period old is worth far more than no plan. Stopping the run
over a folder-name mismatch is the worse failure. CENTRAL_BRIEF_REQUIRED must be
false.

**Reading the published source is MANDATORY, NEVER ASSUMED, and NEVER A STOP.**
SD-SRC-21. Mandatory means it is READ every run: never assumed, never remembered
from a previous run as authoritative, never replaced by this method's own idea of
what the priorities are. It does NOT mean the run stops. A publication that
cannot be reached after the full retrieval ladder DEGRADES: the run continues on
the fallback ladder above, BANNERS itself as source unconfirmed, NAMES the exact
release it used and its date, and never presents the result as authoritative.
The correct heading for such a step is MANDATORY, NEVER ASSUMED, not MANDATORY,
NEVER SKIPPED; the second reads as a stop and will be implemented as one.
Reading the published source is not a member of any HARD_GATES group, per
20.1.4. Worked example, neutral: an organization publishes next period's brief on
the twenty-fifth for a period beginning on the first, so somebody running on the
twenty-second cannot reach it because it does not exist yet. Score against the
current release, name it and its date, banner the run, and continue.

**Discover the path every run; never hard-code it.** SD-SRC-14. Read the actual
folder list and select by NAME CONTENT, ignoring leading numerals, punctuation
and spacing. Reference values are a starting point for discovery, not a path,
and fall back to search whenever any fail to resolve.
DOC_STORE_PATH_DISCOVERY_REQUIRED must be true. Worked example, neutral: two
consecutive periods' folders in the same library differed only by a space after
a numeral. A literal path breaks the first period somebody types it differently,
and it breaks silently.

The published table is authoritative for dates, work types and eligibility.
SD-PRS-01. Parse CENTRAL_BRIEF_TABLE_COLUMNS and USE them. Infer nothing the
source states.

Attachments on a live source message are part of the source, not an extra.
SD-SRC-20. A manager who writes "here are the priorities, make them your own"
and attaches a document has put the entire priority ledger in that attachment.

## 8.12 Central per-unit targeting flags

A per-unit targeting flag published by the central source counts as CENTRALLY
NAMED only when it is carried by LESS THAN HQ_FLAG_BREADTH_LIMIT of the scope. A
flag on most of the population is not a priority, it is a population.

## 8.13 What the priority stage records

For every source: what was read, over what window, from which folders, with
counts. For every message classed as direction: sender, date, and the wording
QUOTED VERBATIM. SD-CNF-07. For every level of the chain: resolved, and whether
it published anything. For every directive: the units named, the ones matched,
and the ones that could not be matched. For every priority: whether it survived
the compliance gate in PART 9.

**AND, FOR EVERY ADMITTED SOURCE, THE PERIOD IT NAMES, WHICH IS WHERE 7.1's
PROVISIONAL PERIOD IS CONFIRMED OR CORRECTED.** Record the period each admitted
direction, priority or requirement is FOR, from its title, its own words or its
stated effective period, or that it names none. Where the planned period came from
7.1 step 2 and an admitted source names a different one, the correction in 7.1
fires here, once, and the stages that read the operating window re-run. Where it
came from step 1 the disagreement is disclosed and the user's period stands. Where
no source names a period, that is recorded too, in one line, because a check whose
result is invisible is indistinguishable from a check that did not run.

---

# PART 9: STAGE 5, VALIDATE THE PRIORITIES BEFORE ANYTHING IS WEIGHTED

**Compliance is checked BEFORE weighting, and it is a guardrail rather than an
optimization.** SD-EXC-28. An item that cannot lawfully or contractually be
executed in the unit's jurisdiction is not an opportunity and must never be
weighted as one. Recommending work that cannot be done is worse than
recommending nothing.

This stage runs on every run where COMPLIANCE_CHECK_ENABLED is true. It sits
between the priority sweep and the scoring, and no priority reaches the scoring
stage unvalidated.

## 9.1 The procedure

1. Resolve the DISTINCT set of jurisdictions present in the scoped population
   from JURISDICTION_CONCEPT. Not the file's set; the scope's set.
2. Check each distinct jurisdiction ONCE and cache the reading for the run.
   Apply the cached finding per unit.
3. For each jurisdiction, read the jurisdiction-specific reference in
   COMPLIANCE_GUIDE_SET. Where none exists for that jurisdiction, read
   COMPLIANCE_GUIDE_MASTER. Where a priority names a topic that has its own
   reference in COMPLIANCE_GUIDE_SUPPLEMENTS, read that too.
4. Apply COMPLIANCE_FINDINGS, which has exactly five findings, each naming its
   effect on weight AND on membership:

| Finding | Effect on weight | Effect on membership |
|---|---|---|
| Permitted | none | none |
| Restricted | weight ZERO | REMOVED from the ranking, with the rule named |
| Permitted with condition | none | none; the condition is printed on the row |
| Source unreachable | the priority is HELD BACK | not ranked on; named as held back |
| No document for the jurisdiction | falls to the master reference; if that is absent, held back | named |

## 9.2 The gate fails closed on the PRIORITIES, not on the run

SD-EXC-29. COMPLIANCE_FAILS_CLOSED_ON must name THE VALIDATED ITEMS, which in
this skill are the priorities; the variable is shared with skills whose items are
called something else, so it names the role rather than this skill's noun, per
SD-CTR-30. If the compliance source is unreachable, hold back every priority that
could not be validated,
rank without them, and report which were held back. Everything else in this
skill fails closed and a compliance gate must not be the one exception, but an
unreachable reference is not a reason to withhold the artifact.

## 9.3 A directive from a supervisor never skips this gate

SD-PRI-17. Automatic admission means an item does not need a published match. It
does not mean it skips the compliance gate. A supervisor cannot authorize what
the local rules do not permit.

## 9.4 Never silently drop a priority

SD-EXC-30. List every dropped priority with the REASON. A person whose top
initiative does not appear needs to know it was excluded for a local rule rather
than assume the method missed it.

A local exception written in a reference field is honoured and never guessed at.
SD-EXC-31. A scope caveat in a supporting-resources field is read and obeyed. An
item restricted to a jurisdiction the user does not operate in is dropped
entirely and the drop is NAMED. Never guess at an abbreviation in a title when
the resources field spells it out.

## 9.5 When the check is not enabled

COMPLIANCE_CHECK_ENABLED defaults to false. The run then prints the exact notice
from reference/schema/ SECTION A1 or A2: no priority in this report was checked against
local restrictions, and if something here cannot lawfully or contractually be
done in a given place, this report does not know it. That notice appears in the
front panel and in the Method section, at the same prominence every run.

---

# PART 10: STAGE 6, ACQUIRE AND PARSE

## 10.1 Acquire

Look in SOURCE_WORKBOOK_LOCATIONS in order. The admission test for an input is
COLUMN COVERAGE, not its title. SD-PRS-25. A source is usable when it resolves
an identifier, a ranking measure, and any ONE scope column. Everything else
degrades gracefully. Refuse only when one of those three is absent, and say
WHICH one was missing and what the file did contain. The concept dictionary is
the test, not the filename. One scope column is enough because finer levels are
read off it by prefix and coarser ones by truncation.

Do not attempt a ranking from a source with no measure. The measure is the one
term the entire method rests on.

Escalate UP the hierarchy for an input, then filter DOWN. SD-PRS-26. Look for
the coarser-level file, then coarser still. Each level up contains the level
below, so a coarse file fully answers a narrow question once filtered. State
which level was used.

Decide which of several inputs is which BEFORE parsing. SD-PRS-27. Resolve each
file's period from its filename, banner rows and time basis. Never silently
merge two sources, and never pick by upload order or filename sort.

Do not caveat a matching supplied input. SD-PRS-28. If an uploaded file matches
the referenced attachment on name and size, it is the same file. Say so plainly
and move on. Treat it as the expected path, not a degraded one.

### 10.1.1 A second file that carries the evidence is JOINED, not left unread

**SD-PRS-48 GOVERNS THIS AND THIS FILE DOES NOT RESTATE IT.** Where a file in the
input set carries columns this run needs and cannot resolve in the ranking source,
and both files resolve the SAME IDENTIFIER, the ranking source is ENRICHED with
those columns by a LEFT join on that identifier. It is a permitted operation, it is
not a concatenation, and leaving the file unread is not the conservative choice: it
is a decision to compute a term as zero when the evidence was in the same input
set. Read the four preconditions, the two non-matching sides, the row-count
assertion and the disclosure list there, and apply them exactly as written.

**WHY IT NEEDED A RULE AT ALL, AND IT IS THIS SKILL'S OWN MEASURED FAILURE.**
10.1's admission test is COLUMN COVERAGE ON ONE CONTAINER, and SD-PRS-12 covers
concatenating two containers OF THE SAME SHAPE. Nothing covered two containers of
DIFFERENT shape sharing a key. A file keyed on the unit identifier with one column
per requirement sat beside the ranking source on a real run; four gap terms and
three exception flags needed exactly that evidence; all seven contributed nothing
to every row; the funnel reconciled and no gate fired.

**WHERE IT RUNS, AND WHICH STAGE OWNS IT. STAGE 6, PART 10, AND NOWHERE ELSE.**
The join is an ACQUISITION and PARSE operation, not a population operation:

1. The ranking source is admitted by 10.1 on its own column coverage. **A second
   file never rescues a ranking source that fails that test**, because a join adds
   columns to a population and cannot create one.
2. The ranking source is parsed by 10.2, which is what establishes the identifier,
   the shape tokens and which needed concepts DID NOT resolve.
3. **Only then** is each remaining readable file in the input set considered as an
   ENRICHING candidate, against the ADMISSION TEST stated immediately below. A file
   that offers neither a needed concept nor a column this run could carry is not
   joined, because a join that adds nothing is width without evidence.
4. The join is performed, its row-count assertion is run, and the enriched columns
   are typed by 10.2's own value checks exactly as if they had arrived in the
   ranking source. A joined column is an ORDINARY column from that point on.
5. **PART 11 then runs on the enriched source, unchanged from step 1 of 11.1.**

**THE ADMISSION TEST FOR AN ENRICHING FILE, STATED IN TWO LIMBS BECAUSE ONE LIMB
COULD NOT FIRE IN THE CASE THE RULE EXISTS FOR.** A second file keyed on the same
identifier is joined where EITHER limb holds. The preconditions of SD-PRS-48, the
key tests and the row-count assertion apply to both limbs identically and are not
relaxed by either:

| Limb | What the second file must offer | What the joined columns may then be used for |
|---|---|---|
| 1. IT RESOLVES A NEEDED CONCEPT | a column that resolves, on the enriching side, to a concept a NAMED DECISION of this run needs and step 2 could not resolve in the ranking source, **by ANY route reference/field-resolution.md permits**: a bound name, a seed stem, a value check, the FIRST-RUN PROVISIONAL ADOPTION of 7.4a where all six of its tests pass, or **the SIBLING SET of 7.4b, where the tie at 7.4a test 5 is a declared sibling set and all five of 7.4b's tests hold IN ADDITION to 7.4a's six** | Everything an ordinary resolved column may be used for: a gap term, an exception flag, an entity resolution, a work-item source, and the carried context block. Where the route was 7.4b the concept resolves PER MEMBER and every figure carries its member's name, per 7.4b |
| 2. IT CARRIES CLEAN-TYPED COLUMNS THE CONTAINER DOES NOT | a column that resolves to NO concept at all but PASSES A VALUE CHECK well enough to be typed, and that no column of the ranking source already carries | **CARRIED CONTEXT ONLY**, on exactly the terms of 1.3d, with its source file named. It is not scored, confers no membership, trips no flag and enters no term |

**WHY LIMB 1 COULD NOT FIRE ON A REAL EVIDENCE FILE UNTIL 7.4b EXISTED, AND WHY
THAT IS THE HALF OF THIS SECTION THAT DECIDES WHAT SHIPS.** Limb 1 was already
written to admit a provisional adoption, and on the file this section exists for
it still resolved nothing, because of the SHAPE a real evidence file has rather
than because of anything either limb says. Measured on this skill's own run: 190
rows keyed on the unit identifier, EIGHT boolean columns mapping one to one onto
the eight numbered requirements of the organization's own published standard,
every one of them passing the concept's value check at 7.4a test 3 and clearing
PROVISIONAL_ADOPTION_MIN_FILL at test 4. Test 5 asks for exactly one candidate,
saw eight, and adopted none. Four gap terms and three exception flags were then
NOT EVALUATED on all 190 rows, and most of the population read that no action
could be derived, two columns away from a file answering the question account by
account. **The refusal got MORE certain the more complete the evidence file was**,
because one boolean column can be adopted and one per requirement cannot, which is
the wrong way round. reference/field-resolution.md **7.4b, THE SIBLING SET**, is the route
that closes it, and this file cites it rather than restating its five tests: a set
of columns that PARTITION a concept, each answering it about a different member of
a member set THIS RUN ALREADY ADMITTED, is not the ambiguity test 5 was written to
refuse. Test 5 is unchanged for two columns that COMPETE for one concept, which is
still a coin flip and is still refused.

**WHAT A GAP TERM AND AN EXCEPTION FLAG DO WHEN A SIBLING SET RESOLVES.** The set
resolves the concept PER MEMBER and never as one column, so:

- **A gap term reads the MEMBER'S OWN COLUMN and is evaluated ONCE PER MEMBER**,
  per 12.10 and 7.4b. It is scored on the enriched column exactly as limb 1 already
  provides, and **every figure it produces names the member beside it**, wherever
  that figure is printed: on the row, in the section's note band, in the front
  panel and in the Method section. A figure from a sibling set that does not name
  its member is a figure the reader cannot check against the standard it came from,
  and 7.4b makes that naming the condition of the adoption rather than a courtesy.
- **NO ROLLUP IS INVENTED to give the term one answer per unit.** Where a term
  needs ONE answer per unit and the admitted source states no aggregation, the
  per-unit answer stays UNRESOLVED and is reported as NOT ATTEMPTED under 12.10 and
  SD-SCO-11, and the per-member answers still ship. The run never synthesizes the
  per-unit answer by AND, OR, majority or count. Where the ADMITTED SOURCE ITSELF
  states the aggregation, the term takes it and prints the rule and the source's
  own words for it beside the figure. **GAP_TERM_CAP is not raised and no term is
  added to the closed set of 12.10**: a sibling set changes what a standing term
  can READ, never how many terms there are or what they may sum to.
- **An exception flag runs PER MEMBER on the same terms**, per 16.2, and the
  section states which members its flags ran on and which members had no column.
  A flag that would need a per-unit rollup the source did not authorize does not
  run, and it is named as not evaluated rather than run on a rollup this method
  invented.
- **The adoption is disclosed as ONE event and the mapping ships in full**, per
  7.4b: the member set with its source, its date and its originator and the words
  that it was ADMITTED this run; the full member-to-header mapping INCLUDING EVERY
  MEMBER THAT GOT NO COLUMN; any column struck at 7.4a test 6 and why; and every
  feature the set fed, per member. This skill places that in the Method section
  beside the join disclosure and carries one front-panel line naming that a second
  file supplied the evidence, which requirement set it was mapped against and what
  share of rows it reached.

**WHAT A GAP TERM AND AN EXCEPTION FLAG DO WHEN THE SIBLING SET IS REFUSED, AND
IT IS EXACTLY WHAT A MISSING COLUMN ALREADY DOES.** Where any of 7.4b's five tests
fails, or where 7.4a's own six do not all hold for every member, **NOTHING IS
ADOPTED**, and the run takes the path it already had for an unresolved source and
takes no other:

- The concept stays UNRESOLVED. Every gap term over it is NOT SCORED and is NAMED
  as not evaluated, per 12.10 and SD-SCO-11; it never becomes a default and never
  becomes a zero. Every exception flag over it does not run and is named, per 16.2.
- **No column of the set is elected to stand for the others**, and no four of eight
  are adopted. There is no partial sibling set, per 7.4b.
- The columns are still eligible for LIMB 2, and land in the carried context block
  on 1.3d's terms and inside 1.3d's cap like any other candidate: CARRIED, NOT
  SCORED. **Carrying them restores no term and trips no flag, and the artifact says
  so rather than implying otherwise.**
- The report names which columns tied, which member set was considered, and which
  of S1 to S5 failed, per 7.4b's closing rule and reference/field-resolution.md 7.7.

**So a refused sibling set is not a new failure mode either.** It is the ordinary
unresolved-source state of the block below, reached one step later and explained
one step better, and every rule downstream of it is unchanged.

**WHY LIMB 2 EXISTS, AND IT IS THE EXACT CASE THIS SECTION WAS WRITTEN FOR.** An
earlier statement of step 3 gated the join on the second file resolving a concept
the parse stage left UNRESOLVED, and read strictly that gate can never open for a
file whose headers resolve to no concept at all: those are not concepts left
unresolved, they are columns with no concept, and the gate has nothing to be
unresolved about. It was measured. A file of 190 rows keyed on the unit identifier
carried eight boolean columns mapping one to one onto the eight numbered
requirements of the organization's own published standard; every one of them was
readable, well typed and decision-relevant; none of them matched a seed stem; the
file was never joined; four gap terms evaluated to zero on all 190 rows and three
exception flags printed that they could not be evaluated, beside a file that
answered one of them outright, row by row, for every unit in the book. **That is
every real evidence file**, because an organization names its evidence columns
after its own requirements and not after this method's concepts.

**AND IT AGREES WITH 1.3d RULE 1 RATHER THAN CONTRADICTING IT.** 1.3d admits a
column to the carried context block on a CLEAN TYPE ALONE, with no concept
required, and it was already the rule for a column of exactly this shape sitting
in the ranking source. Two rules disagreed about one column depending only on
which file it arrived in, and the disagreement resolved in the direction that
printed `could not be evaluated` beside a readable answer. **The worst of both is
refusing to reach a column and then reporting the absence as a finding.** The two
rules now state the same test.

**WHAT LIMB 2 DOES NOT DO, AND THIS IS WHERE THE SAFETY IS.** A limb-2 column is
CARRIED, NEVER SCORED. **To be SCORED it must clear limb 1**, which means it must
resolve to the concept a term reads, by a stated route, with that route recorded.
There is no path from `it is well typed and it looked relevant` to a number in the
alignment product, and a run that scores a limb-2 column has widened a
resolution silently, which SD-QUA-12 forbids in its general form and which is the failure limb 2 is
carefully shaped to avoid. Where a limb-2 column plainly answers a needed concept
and neither 7.4a's six tests nor 7.4b's five all pass, the correct outcome is the
one 7.4a states: the concept stays unresolved, the term is reported as NOT
ATTEMPTED rather than as zero, and the report names the column that was closest
and the test it failed.

**AND A LIMB-2 COLUMN MAY NOT RESOLVE A PREDICATE ATTRIBUTE, WHICH IS STATED
EXPLICITLY BECAUSE THE TEXT ONCE PERMITTED TWO READINGS OF IT AND THEY PRODUCE TWO
DIFFERENT ARTIFACTS OFF ONE INPUT.** Step 4 says a joined column is an ORDINARY
column from that point on, and 8.8.1 test 2 route b runs a direction's own words
DIRECTLY AGAINST THE HEADER TEXT of the source. Read loosely, a limb-2 header
matching a published requirement's own wording by route b would supply HDR_ACTION
on every row the column answers. **It does not, and the closed list is this:** a
limb-2 column may not resolve a PREDICATE ATTRIBUTE under 8.8.1, may not be a
gap-term source under 12.10, may not be a flag source under 16.2, may not be an
entity resolution under 12.8, may not be a work-item source under 10.3, and may
not enter any term of 12.1. **It may be carried under 1.3d and read by a human,
and that is the whole of it.** The reason is limb 2's own safety argument rather
than a new one: a column admitted on a CLEAN TYPE ALONE, with no concept and no
recorded route, must not reach anything that DECIDES AN OUTPUT, **and an action is
an output** -- it is the column a reader acts on, it is mandatory under 1.3b, and
it is never blank. The route that puts a real evidence column into HDR_ACTION is
LIMB 1, through 7.4a or through 7.4b's sibling set, where the resolution is
recorded, the member is named beside the figure and the reader can check it against
the standard it came from. **Where the sibling set is refused and the columns fall
to limb 2, the priorities section carries each affected requirement as its own row,
its HDR_DIRECTIVE_STATUS cell holding the member of that variable's closed set that
says the direction could not be evaluated, with the test that refused it named
beside it**, per 8.8.1 and 1.9 item 16, so the reader is told that a published
requirement reached no row and why, rather than being left to notice its absence.

**A LIMB-2 JOIN IS BOUNDED BY THE CONTEXT CAP AND BY NOTHING ELSE.** 1.3d's cap of
six governs how many context columns ship, from both files together, ordered by
1.3d's own keys; a second file cannot widen the artifact past that cap, and the
columns it offered that were not carried are named in the Method section with
their figures like any other candidate.

**THE JOIN IS COMPLETE BEFORE THE PIPELINE STARTS, AND THAT ORDERING IS LOAD
BEARING.** SD-PRS-48 fixes the ranked population before the join and asserts the
row count is identical after it, and running the join inside or after the pipeline
would put a row-count-changing operation downstream of the funnel of 11.6, where a
change reconciles against nothing. So: the population funnel counts a population
the join has already finished touching, every count in it is unaffected by the
join by construction, and the funnel says so in one line.

**A JOINED COLUMN IS NEVER A SCOPE COLUMN, NEVER AN IDENTIFIER AND NEVER THE
MEASURE.** Those three are the admission test of 10.1 and they are settled on the
ranking source alone. A joined column may be a gap-term source, an exception-flag
source, an entity resolution source, a work-item source or a carried context
candidate, and nothing else. This keeps a join from silently changing which file
the run is actually ranking.

**A JOINED COLUMN IS ELIGIBLE FOR THE CARRIED CONTEXT BLOCK ON THE SAME TERMS AS
ANY OTHER**, per 1.3d, including its rule 4: where it is an input to a scored
term it is excluded from the block, and where it is not, it qualifies and is
ordered by the same keys. Its header is the ENRICHING SOURCE's own header text,
sanitized on the way in, and the Method section names which file it came from, so
a reader never has to wonder why a column they do not recognize is on the row.

**WHERE THE JOIN IS REFUSED, IT DEGRADES EXACTLY AS A MISSING COLUMN ALREADY
DOES, THROUGH THE EXISTING PATH AND NEVER THROUGH A NEW ONE.** This is the part
to get right, because a new degradation path is a new way for a run to be wrong.
SD-PRS-48 refuses the join where any precondition fails and requires the file to
be recorded READ AND NOT JOINED with the failed condition named. From that point
the run behaves as though the second file had never existed, which is precisely
the state every rule in this skill was already written for:

- **A gap term whose source concept did not resolve is NOT SCORED and is NAMED as
  not evaluated**, per 12.10 and SD-SCO-11. It never becomes a default and never
  becomes a zero.
- **An exception flag whose source concept did not resolve does not run**, per
  16.2, and the section states which flags ran and which did not, per 16.7's
  shown-never-scored discipline and SD-EXC-25's refusal to build on a thin field.
- **A column whose source did not resolve is written blank with its header
  present**, per SD-CTR-13, on any section whose family carries it.
- **Nothing about the ranked population, the funnel, the caps or the section sizes
  moves**, because none of them ever read the second file.

What the refusal ADDS to that existing behaviour is disclosure and nothing else:
the Method section names the file, the condition that failed, and the terms that
went unevaluated as a consequence, so the cost is visible rather than invisible.
**A refused join is therefore never a new failure mode; it is the ordinary
unresolved-source state, with a better explanation of why the source is
unresolved.**

**AND A JOIN THAT LANDS AND RESOLVES NOTHING TAKES THE SAME FOUR BULLETS, WHICH IS
WHY SD-PRS-48 CALLS THE JOIN HALF THE FIX.** A refused join and a landed join whose
columns adopted nothing are different events with the SAME downstream state, and
the four bullets above are that state in both cases: not scored and named, the flag
skipped and named, the column blank under its own header, nothing about the
population moved. **The two are never collapsed in the DISCLOSURE, because they
send the reader to different remedies:** a refused join is fixed by the key or the
file, and a landed join that resolved nothing is fixed by admitting the member set
or by binding the headers, which is a different person doing a different thing. So
the Method section says which of the two happened, and where it was the second it
names the columns that tied, the member set considered and which of 7.4b's tests
failed. **A run that reports `the file was read` and stops there has moved the
failure rather than closed it**, per SD-PRS-48.

**AND A PERFORMED JOIN IS DISCLOSED WHEREVER ITS EVIDENCE IS USED.** Per
SD-PRS-48's disclosure list: the file joined, the key used, the columns added, the
MATCH RATE as matched of ranked, the unmatched count on EACH side, **and whether
each joined column RESOLVED to a concept or was CARRIED UNREAD, column by column**,
because a joined column nothing reads is indistinguishable in the artifact from a
joined column that scored a term, and the whole reason this section exists is that
one of those two states was mistaken for the other. This skill
places those on the Method section beside the funnel, and adds one front-panel line
naming that a second file supplied the evidence for the named terms and what share
of rows it reached, because a reader deciding whether to trust a gap term needs to
know that a fifth of the rows had no record on the enriching side. A ranked row
with no match keeps its place and its enriched columns are UNRESOLVED for that row,
blank rather than zero, and any term over them is not scored for that row and says
so: an absent record is not evidence of a negative.

## 10.2 Parse

reference/field-resolution.md owns the mechanics in full. This skill invokes it and adds
nothing. The rules that matter enough to be visible from here, each cited:

- Fields resolve by CONCEPT, never by literal header. F0.
- Never take the first container on faith, and a name match still needs a column
  check. Score every candidate by resolvable required concepts; break ties by
  RECORD COUNT, never the reported extent; ignore documentation-named
  containers; a container named after a person is a working extract.
  SD-PRS-11. A silent wrong-container pick produces a complete, confident,
  entirely wrong artifact: the worst failure this method has.
- Where no single container covers the requested scope, CONCATENATE rather than
  choose, de-duplicate on identifier, and report how many were combined and how
  many duplicates collapsed. SD-PRS-12.
- Detect the header row rather than assuming it, scoring HEADER_SCAN_DEPTH rows
  by non-empty STRING cells, confirming by resolving the required concepts, and
  recording the choice AND its runner-up. SD-PRS-13.
- Three matching passes, each run to completion before the next: exact, prefix,
  substring, across the whole header list, so an exact match anywhere always
  beats a substring match anywhere. SD-PRS-14.
- A short-string guard: below MIN_STEM_LENGTH normalized characters, only an
  exact match counts, and exact matching is never suppressed. SD-PRS-15.
- **No stem belongs to two concepts, and a tie on a strict concept is never
  broken by position.** SD-PRS-47. Where two concepts both produce an EXACT match
  on the same header and EITHER is marked strict_exact_only, **NEITHER RESOLVES**:
  the header is reported as ambiguous, both candidates are named, and every
  feature both feed is skipped and named. A tie on a strict concept is never
  broken by column position, by dictionary order, or by which pass reached it
  first. The named case is the one no downstream gate can catch: a generic status
  stem sitting in both the not-actionable exclusion concept and the pipeline stage
  concept, so a file with one column of stage values resolves to the exclusion
  concept, the exclusion removes a STAGE, the funnel reconciles, and every
  invariant passes. The only defence is refusing to guess.
- Confirm a resolved column by its VALUES, not only by its name, through the
  value-classification ladder. SD-PRS-16. A header that says measure and whose
  values are decimals between zero and one is a RATE, not a measure, and the
  header is misleading. Trust the values.
- Coerce before comparing. SD-PRS-17. A typed comparison against the wrong type
  fails SILENTLY: it does not raise, and it looks exactly like a file with no
  data in that column. Subtracting a date from a string produces nothing, and a
  recency flag that silently never fires looks identical to a scope with no gaps.
- **A resolved but EMPTY column is an ABSENT column.** SD-PRS-18. Check each
  resolved column's non-null count WITHIN SCOPE. If it is zero, exclude it from
  every flag, gate, weight and benchmark in that concept's feeds list, and list
  it as resolved but empty. This is the single most damaging false-positive
  class: a wholly empty commitment column would report every eligible unit as
  missing every commitment, and a wholly empty breadth column would put every
  unit on the breadth section.
- Normalize null-like VALUES, not just empty cells, against NULL_LIKE_VALUES.
  SD-PRS-19. A grouping cell reading the literal text "null" would otherwise
  classify a self-determined unit as a managed one and invert every rule built
  on that distinction.
- Register the STEM, never the full literal. SD-PRS-20. A stem catches every
  dated variant automatically; a literal catches exactly one period.
- Unit and time-basis markers are interchangeable and must be RECORDED.
  SD-PRS-21. Strip the trailing period token before comparing, then record the
  suffix found, because together they are the unit and the time basis and both
  must be reported.
- A header that does not resolve is a SKILL DEFECT, not a user error. SD-PRS-22.
  Log the literal, continue with what did resolve, name it in the Method
  section, and propose the stem for the dictionary.
- Record every ambiguous resolution and WHO decided it. SD-PRS-23. This is what
  lets the binding owner add the stem so the next person is never asked.
- Never analyze a partial source, and count RECORDS rather than the reported
  extent, which routinely overstates by thousands. SD-PRS-24. A record count of
  zero is a hard gate. A small non-zero count is not measurable against any
  expectation, because this method is forbidden to carry one, so do not guess at
  a threshold.
- Alias matching is normalized, not literal. SD-PRS-41. An alias that is a common
  word or carries punctuation needs a SENTINEL, replaced BEFORE punctuation is
  stripped; never register the bare remainder. SD-PRS-42. A bare two-character
  remainder falsely attributed more than two hundred rows of unrelated flags to
  one entity in a real run.
- A sub-entity inherits its parent and its parent's benchmark. An unrecognized
  alias is FLAGGED, never guessed. SD-PRS-43. ENTITY_ALIAS_UNRECOGNIZED_ACTION is
  flag_and_ask or flag_and_floor, never guess_parent.
- Confirm the SCALE of a column by reading its own maximum, every run.
  SD-PRS-44. Against a fractional column a literal points threshold matches zero
  rows, silently.
- Null handling changes the count and must be STATED. SD-PRS-45.
- **Duplicate identifiers: MERGE the signals, do not just keep the best row.**
  SD-PRS-29. Keep the highest-measure row as the base, then merge the survivors'
  signals into it: a flag on any duplicate is a flag on the merged row, a match
  on any row matches the merged row, and a populated field on any row fills a
  blank on the base. Keeping only the highest-measure row without merging
  silently drops work items and directives that belong to the unit. See PART 23
  for the FLOW exception, which is the one place this rule does not hold.
- Sanitize text at the boundary, on the way IN. SD-PRS-30.

## 10.3 The work-item block

Where the source carries a contiguous block of work-item columns, resolve THAT
BLOCK BEFORE matching any data concept. SD-PRS-06.

Anchor on the DATA, not on the dictionary. The normal marker is a structural
row above the header carrying a number over every column of the block and
nothing else. Stop before an exactly matched boundary from
ACTIVITY_BLOCK_TERMINATOR_CONCEPT.

**Match the boundary token EXACTLY and take the RIGHTMOST match.** SD-PRS-07.
Normalize case, compare the WHOLE normalized header for equality, and if more
than one matches take the rightmost. Record the resolved anchor index. The
documented harm: a decoy header contained the boundary token as a substring and
sat forty-one columns to the left of the real boundary; a substring search stops
at the decoy and cuts the block from seventy-two columns to thirty-one,
discarding fifty-seven percent of the work-item set with nothing in the output
looking wrong.

Three ordered fallbacks when the marker is absent, per reference/field-resolution.md F4.3,
ending in "no block exists", which is a VALID outcome and is stated.

The ordering matters in BOTH directions. Matching data concepts first and
greedily consumes work-item columns as data concepts, because more than half of
the work-item columns in a real file match some data-concept stem if they are
offered to the matcher. Defining the block as everything to the right of the
last mapped concept fails from the opposite end. Anchoring on a structural
marker is the only approach that fails neither way.

**Never use an optional metadata prefix as the admission test.** SD-PRS-08. An
originator prefix from ORIGINATOR_PREFIX_MAP is optional metadata for WEIGHTING
ONLY. In the documented case forty-one of seventy-two work-item columns carried
no prefix at all, and those forty-one held ninety-six point eight percent of the
unit-level signal; a prefix-based detector discards nearly the entire set and
produces a ranking built on three percent of the data.

## 10.4 Counts and count rows

A global count row is NEVER used for scoring. SD-PRS-09. A count row scoped to
the whole organization is a structural marker only; using it as a narrowness
signal INVERTS the ranking. A globally scoped statistic must never be used as a
locally scoped one. Rows above the header are metadata, never data.

Compute per-item counts from the FILTERED scope yourself. SD-PRS-10. A narrow
item is a sharper priority than a blanket one, and that judgment is only valid
against counts drawn from the user's own units.

## 10.5 Foreign-unit tags

An item flagged on a record IN SCOPE is work on that record regardless of which
unit authored it. SD-PRI-21. It gets no local boost and no automatic admission,
and it scores only if it matches a stated priority on its own merits. Record the
authoring tag and report the count. Never silently dropped, and never used as an
admission test in either direction.

## 10.6 Learning

CONCEPT_LEARNING_ENABLED governs whether a run may propose a newly learned stem.
The trigger set, what is registered, which learnings may be used inside the same
run, and which may be promoted, are owned by reference/field-resolution.md PART 7. Two
rules from it are load bearing here: a LOW-confidence inference is never used
and never promoted, and promotion is an ORG-tier act, never a PERSON-tier one. A
run proposes; the binding owner accepts.

---

# PART 11: STAGE 7, THE POPULATION

## 11.1 THE PIPELINE ORDER, stated once and authoritative

SD-POP-02. One ordering that satisfies every rule in this file that claims to
run first. No stage may be reordered. Several rules each claim primacy, and
without one authoritative ordering an implementer resolves the conflict
differently every time.

1. SCOPE and QUALIFIERS, including a STEER that restricts.
2. The NOT-ACTIONABLE exclusion.
3. Normalize the measure.
4. Compute the class-escape median with the excluded class INCLUDED.
5. Resolve the MANDATORY set.
6. Apply the CLASS exclusion and its escapes. The result is the RANKED
   POPULATION.
7. Compute percentiles, every other median and every peer norm over the ranked
   population, with mandatory units INCLUDED.
8. Split the ranked population into the mandatory section and the merit tiers.
   This is a ROUTING step and not a population change.

**ANY ENRICHMENT JOIN IS COMPLETE BEFORE STEP 1, AND IS NEVER A STEP OF THIS
PIPELINE.** SD-PRS-48 and 10.1.1. A join adds COLUMNS and never a row, its row
count before equals its row count after as a blocking assertion, and it belongs to
stage 6 rather than to this stage precisely so that no step here can change a
count for a reason the funnel of 11.6 cannot express. A run that performs a join
inside or after this pipeline has put a row-count-changing operation downstream of
the funnel that would have to catch it.

**The same phrase can mean two different medians, and the difference must be
stated.** SD-POP-03. "Scope median" means the step 7 median EVERYWHERE except in
the class escape, which uses the step 4 median. On one real scope the two
differed by more than fifty percent, so a run that uses the wrong one either
admits units that should not be admitted or excludes ones that should. An
overloaded term silently changing a threshold is a defect class in its own
right. Name both, once, and this is that place.

## 11.2 Step 2, exclude what cannot be acted on right now

**Exclude unreachable units before anything else, with no exception.**
SD-POP-01. Drop every unit whose UNIT_ACTIONABLE_NOW_CONCEPT value is in
UNIT_ACTIONABLE_NOW_VALUES, from EVERY list including the mandatory section.
REPORT THE COUNT so the omission is visible rather than silent. If the column is
missing, SAY SO; do not assume every unit is available.

The universal core is that A LAGGING MEASURE SURVIVES THE THING IT MEASURES. A
unit that cannot be touched still reads as a strong performer and ranks high.
Worked examples, neutral and invented: an account in a contractual freeze still
shows last quarter's revenue and would rank top of a renewal list; a person
discharged from a service still carries the utilization history that would put
them on an outreach list; a client on a legal hold is unreachable and reads as
strong. Sending someone to a locked door on the strength of this report destroys
its credibility on the spot.

**THIS TEST IS FORWARD LOOKING, AND UNDER THIS SKILL THAT IS THE WHOLE OF IT.**
SD-POP-30. The question here is CAN THIS BE WORKED IN THE PERIOD BEING PLANNED, so
a unit that cannot is removed, and the state read is the CURRENT one against the
window 7.1 resolved. It is stated because the same doctrine rule asks a DIFFERENT
question in a retrospective, where the test becomes whether the unit was workable
at any point in the period under review and a unit that became unworkable partway
is included and marked; applying the planning reading there deletes from somebody's
own review every unit they worked and then lost, silently, because the unit is
simply not there to be missed. **The mode is a property of the RUNNING SKILL and is
never inferred from the data or from a phrase in the request**, so this skill takes
the forward-looking reading on every run and says so in the Method section beside
the excluded count. The one place the other reading touches this file is its
mirror: a FORWARD-LOOKING statement inside a retrospective takes the reading here,
which is that skill's problem and not this one's, and neither skill applies a
reading without naming which one it applied.

### 11.2.1 The two bindings are separate, and the value list has a real default

**RESOLVING THE COLUMN AND BINDING ITS VALUES ARE TWO DIFFERENT BINDINGS.**
SD-POP-28. UNIT_ACTIONABLE_NOW_CONCEPT says WHICH COLUMN. UNIT_ACTIONABLE_NOW_VALUES
says WHICH VALUES IN IT mean not workable. A run can have the first and not the
second, and that is the ordinary state on a first run. Take the two cases
separately and never collapse them:

**CASE A, THE CONCEPT DID NOT RESOLVE.** There is no column to read. No exclusion
is applied, and the SECTION A1 notice for UNIT_ACTIONABLE_NOW_CONCEPT is printed:
no field has been bound that says which units cannot be acted on right now, so
none were excluded, and some units on this list may be closed, suspended or on
hold with their history still ranking them high.

**CASE B, THE CONCEPT RESOLVED AND THE VALUE LIST IS UNBOUND. THE DEFAULT IS NOT
"INCLUDE EVERYTHING".** Match the distinct values present in the column against
UNIT_NOT_ACTIONABLE_SEED_VALUES and EXCLUDE every match, by the mechanism below.
Three guards then apply and all three are mandatory:

**HOW A VALUE MATCHES A LISTED ENTRY, AND IT IS NEVER BY LENGTH.** SD-POP-29. A
character count cannot tell a meaningful short token from a fragment of a longer
word, and a length floor fails in BOTH directions at once: too loose, so a short
word sitting inside a longer seed entry matches an ordinary word in a live status
and a workable unit is silently removed; too tight, so a three-character negating
token falls below the floor and the exclusion the rule exists for does not fire
at all. Raising the floor worsens the second and lowering it worsens the first,
which is the proof that the floor is the wrong instrument. No rule anywhere in
this skill admits a match because a token is at least N characters long. The
mechanism is whole-token phrase matching, four steps, and this is the whole rule:

**THE UNIT_ACTIONABLE_NOW_VALUES ROW IN reference/schema/ SECTION A1 IS THE SINGLE
STATEMENT OF THIS MATCH RULE AND OF WHEN THE EXCLUSION RUNS AT ALL, AND SD-POP-29
STATES THE PRINCIPLE. What follows restates it for reading convenience and is stale
wherever it differs.**

1. NORMALIZE both sides: lowercase, every non-alphanumeric character becomes a
   space, collapse runs of spaces, split into tokens.
2. THE PHRASE TEST: an entry matches when its token sequence appears as a
   CONTIGUOUS RUN inside the cell's token sequence, tokens compared by EXACT
   EQUALITY. A one-token entry matches only an identical whole token. Word
   boundaries come free, because a token cannot match inside another token.
3. THE SINGLE-TOKEN OVERRIDE: where the cell carries a token marking a LIVE
   relationship, a match by a ONE-TOKEN entry is REFUSED and only a multi-token
   entry may fire. A compound status that names a live relationship needs the
   exit stated as a phrase, never implied by one word.
4. REPORT THE REFUSAL on its own line, naming the cell value, the entry and the
   marker that refused it, inside the same EXCLUDED and KEPT listing the naming
   guard prints. A near miss the reader cannot see is the same as no rule.

**Morphological variants are LISTED, never derived.** Dropping prefix matching
means a stem no longer reaches its own plural or participle, so every form that
must match is an entry in its own right. That is more lines and it is the correct
trade: a list is auditable and a derivation is not.

**Where this governs and where it does not.** It governs every match of a CELL
VALUE against a LISTED ENTRY anywhere in this skill: the seed exclusion values
here, controlled-vocabulary lists, flag value sets and directive value sets. It
does NOT govern header-stem resolution, which runs reference/field-resolution.md's own
cascade over column NAMES with its own short-string guard, and it does NOT govern
the scope-code prefix test, which compares positional HIERARCHICAL CODES rather
than words. Those are different instruments on different objects, and neither of
them admits a match on a length threshold either.

**A claim that a rule was verified against named traps is TESTED, not asserted.**
Where any notice in this skill names example inputs, those exact inputs are run
and their results printed. A document that asserts a test it does not pass spends
the reader's trust to hide the defect.

1. **THE STAGE GUARD.** Under FLOW, a value that is also a stage name in
   POPULATION_SHAPE.stages is NEVER excluded from an unbound default. A terminal
   stage is the open-set rule's business, not the exclusion's, and letting an
   exclusion delete a stage is the failure SD-PRS-47 exists to prevent.
2. **THE MAJORITY GUARD.** Where the seed set would remove more than
   EXCLUSION_SANITY_CEILING of the in-scope population, exclude NOTHING, and say
   the column was read and looked wrong. A default that removes most of a
   population has almost certainly read the wrong column. This guard applies only
   to a DEFAULT; a bound exclusion is never refused on volume.
3. **THE NAMING GUARD.** Print every distinct value in the column under exactly
   two headings, EXCLUDED and KEPT, each with its count, in the funnel and in the
   Method section. The reader sees the whole decision, not its result. A local
   status word that means the same thing as a seed value will not be in the
   generic set and will show up under KEPT, which is exactly where somebody spots
   it in one glance.

**ASK FIRST WHERE YOU CAN, AND IT IS A PERSON-TIER QUESTION.** Per
reference/field-resolution.md F5.1b, show the user the EXCLUDED and KEPT lists with counts
and invite a correction, batched into the same single message as any other
question this run is asking. It asks what values in the user's own file mean, not
what the organization's policy is, so it does not cross I1's wall and it needs NO
binding authority: a frontline user on a fully unbound first run may be asked it.
A correction governs this run and is offered as a proposal for the eventual
ignition interview, never written to the org config.

**SILENCE PROCEEDS ON THE DEFAULT.** No answer, no channel, or a spent question
budget all mean the exclusion is applied anyway and the artifact records that it
was unconfirmed. Silence NEVER reverts to excluding nothing.

**WHY THE DEFAULT IS NOT NEUTRAL, AND WHY THAT IS CORRECT.** The two errors are
not symmetric. Including a unit nobody can work sends a person to a locked door
and costs the whole list its credibility, which is the failure 11.2 opens by
naming. Excluding a workable unit costs one row, is visible in the KEPT and
EXCLUDED listing printed in the same artifact, and is recoverable in a sentence.
Disclosure does not redeem a wrong instruction: an artifact that ranks a
prospect at position one of a working plan is not fit to hand anybody, however
many times it says so on the front panel.

**WHERE THE VALUE LIST IS BOUND, THE BOUND LIST GOVERNS COMPLETELY** and the seed
set is not consulted at all. SD-CTR-24 is untouched: a default may narrow what a
run attempts and may never contradict what the organization bound.

Either case is decision point 3 in PART 22. Fire it if an authorized answerer is
present, per the additive authority rule in 3.4 C1.

## 11.3 Step 4 and step 6, the different-operating-model class

**A class served under a different operating model is REMOVED from the
population, not down-weighted.** SD-POP-17. It should not compete for the
person's time at all. The concept is OUT_OF_MODEL_CLASS_CONCEPT and its plain
word is OUT_OF_MODEL_CLASS_LABEL. Worked examples, neutral and invented:
accounts on a self-serve or partner-led motion that a named owner neither owns
nor should be measured against; people attributed to another team under a
different protocol; clients on a standing retainer rather than a project
engagement.

**Resolve the exclusion flag by EXACT column name only.** SD-POP-05. Then by
named alternates, and nothing else. NEVER fall back to a neighbouring column in
the same synonym group; COLUMN_CONCEPT_DICTIONARY.forbidden_neighbours names the ones that must be
refused. Matching the wrong one removed roughly three times the intended
population in a real run. Critically:

> A gate cannot catch this error: every unit of the intended class also carries
> the neighbouring flag, so removing on the neighbour removes all of them too
> and the invariant still passes. The only defence is resolving the right column
> in the first place.

That is the sharpest statement in the corpus of a failure NO GATE CAN CATCH. Any
concept whose mis-resolution is invisible downstream is marked strict_exact_only
with named forbidden neighbours, and the resolver refuses those candidates even
when they are the only match.

Use the SOURCE'S OWN FLAG rather than a maintained name list. SD-POP-07. The
rule then travels to any unit without a name list to maintain, and a maintained
list rots and does not port.

A MISSING exclusion flag means NO exclusion, stated plainly. SD-POP-06. Apply no
exclusion, say so in the Method section and in the opener, and rank the whole
population. The same when the column resolves but is empty for every row. A
missing flag is a reason to REPORT, never a reason to guess.

**Three escapes from the exclusion, and only three.** SD-POP-08:

1. The unit was NAMED by a supervisor. This is why step 5 runs BEFORE step 6.
2. The unit reaches the UPPER HALF of its scope by the ranking measure computed
   with the class INCLUDED, which is the step 4 median. Computing it after the
   exclusion would mean "half the excluded class" and would readmit roughly half
   of them, defeating the rule.
3. The REQUEST named the class by name.

OUT_OF_MODEL_ESCAPES_ENABLED says which are live; all three default true. All
three are evaluated per run against live data, never from a stored list.

**Keep escape 2 even where it admits nothing.** SD-POP-09. In the reference data
it admitted nothing anywhere, and the best candidate fell four percent short of
the threshold. It is kept because a denser population will fire it. A rule that
costs nothing when it does not trigger and keeps the method portable is worth
carrying. This is G5 and it is a portability argument, not a hedge.

Report the exclusion every run: counts removed, counts readmitted PER ESCAPE,
and the threshold used. SD-POP-10. Someone who wonders where a third of their
units went must find the answer in the artifact rather than assume the file is
broken.

## 11.4 Step 5, resolve the mandatory set BEFORE the class exclusion

SD-POP-04. The ordering is MANDATORY. Resolve directed units from the priority
sources FIRST, then apply the class exclusion to everything that is not
directed. Reversing those two steps silently deletes a unit the user's own
manager told them to cover, which is the most damaging failure this method can
produce and it produces NO ERROR when it happens. State in the Method section
that the ordering held, and carry it as a regression invariant re-checked at
every gate.

**A mandatory set is built from an explicit LIST, never from a per-unit flag
column.** SD-MND-01. A unit becomes mandatory only when a message NAMES specific
units. A per-unit work flag is loaded work that scores through the alignment
term; it does not confer mandatory status. Never synthesize a directed set from a
flagged population: converting a flag into a unit-by-unit callout the supervisor
did not make inverts the weight by up to a factor of five on units the
supervisor only pointed at in aggregate, and it floods the mandatory section,
pushing real merit units off the action lists.

Two doors for the same work is not two mandatory sets. SD-MND-02. When one
message loads work AND attaches a list, the mandatory set is the ATTACHMENT and
the flag column scores separately. A unit on both receives the multiplier ONCE
and an alignment contribution ONCE. This is correct because the multiplier
multiplies the FINISHED score while alignment is an ADDITIVE term inside the
bracket.

Mandatory membership NEVER depends on the score. SD-MND-03. The score only
orders the mandatory section among itself. A unit with no measure, no work and a
score at the floor is still mandatory and still listed; it is never filtered out
for scoring low. This is the guarantee the measure-rank cut in 11.8 exists to
protect.

Mandatory units sit in their own section, outside the ranked lists, ranked among
themselves. SD-MND-04.

## 11.5 Step 3 and step 7, the measure and the percentile

**There is NO measure floor. Rank the whole population.** SD-POP-11. No fraction
cut, no median cut, no minimum to be ranked. The section sizes decide what
appears, and a unit that does not appear ranked BELOW THE CUT rather than being
removed by a threshold.

The documented harm: a two-thirds floor dropped several genuine mid-size units
while the unit one place above the line survived on a trivial difference. The
floor had been calibrated when a third of the population was a low-value class
dragging the distribution down. Remove them and the same rule starts amputating
real business. A threshold calibrated against a population that has since
changed is the general failure.

> A floor answers the wrong question. The measure tells you what a unit is worth
> ATTENDING TO; it does not tell you whether it NEEDS attention.

And: capacity is already the constraint, and it is the honest one.

A unit with no history is RANKED LAST, never dropped. SD-POP-12. A newly created
unit has no measure yet, so it should rank at the bottom and be VISIBLE there,
not vanish until it accumulates history.

USABLE MEASURE, redefined and exact. SD-POP-13. A blank, null, non-numeric, zero
or negative measure is INCLUDED in the population and treated as ZERO. It is
counted in N, receives the lowest percentile, and ranks last in the zero bucket.
ZERO_MEASURE_TREATMENT must be include_as_zero; excluding is forbidden. Only the
not-actionable gate and the class exclusion remove anything.

The percentile definition is mandatory and exact. SD-POP-16. Rank the in-scope
population ASCENDING by the ranking measure, AVERAGE the ranks of tied values,
divide by N. PERCENTILE_DEFINITION must be average_rank_over_n. Tied values
receive an IDENTICAL percentile, which is what makes a rerun reproduce the same
list. Never compute over a subset, never over a sample.

The percentile never reaches zero, which is exactly why the ZERO BUCKET is
mandatory. SD-POP-14. With k units tied at the minimum, each receives
(k + 1) divided by (2N), so no unit is annihilated to a hard zero score and
ordering among the smallest is still decided by the other terms. Someone sent to
a unit with no activity ahead of a unit with real activity would rightly stop
trusting the list. The general lesson: a multiplicative term with a positive
floor does NOT enforce a last-place guarantee; a SORT KEY does.

The bucket is a SORT KEY, never a score adjustment. SD-POP-15. Do not zero the
score, do not add a penalty term, and PUBLISH THE UNIT'S REAL SCORE.
ZERO_MEASURE_SORT_KEY must be sort_key.

Resolve the measure through MEASURE_TIERS, taking the FIRST tier that resolves
AND is populated, then report the tier, the exact column name, the unit and the
time-basis suffix.

**Rank on the OWN measure, never the segment measure, and never let position
decide it.** SD-WGT-09. Every entity has an own measure and a wider segment
measure and they are not interchangeable. Test the own-measure stems TO
EXHAUSTION before considering a segment stem. If only a segment measure exists,
say so plainly and never present it as the entity's own figure. The documented
trap: in one real file the segment column sat IMMEDIATELY LEFT of the entity's
own column for every entity, and the matcher's tie-break prefers the leftmost
column, so a naive resolve picks the segment column every single time, for every
entity. The user then receives a ranking on a competitor-inclusive measure while
the front panel faithfully prints the wrong column's name. This is a live trap
where a generic tie-break rule systematically produces the wrong answer.

## 11.6 The population funnel

SD-POP-20. Each step publishes TWO numbers: the count remaining after it and the
count dropped by it, both measured INSIDE THE SCOPE AS IT STOOD at that step. A
file-wide figure never appears in the funnel, because reporting units that were
never in scope makes the funnel fail to reconcile.

Publish N and eligible_count as two separate figures, per 1.7.

## 11.7 Degenerate scopes: guard every divisor before dividing

SD-POP-18. A closed table of conditions and behaviours:

| Condition | Behaviour |
|---|---|
| Zero rows after filtering | Re-test the filter first (SD-IDN-16). Then report the distinct values present at every level. Never an empty artifact without an explanation. |
| A qualifier matched no rows | Stop before ranking and ask, with the nearest values. |
| A qualifier resolved to no column | Run without the term and label the report unqualified. |
| Blank, zero or negative measures | Included at zero, in the zero bucket. |
| Phantom trailing rows | Count records by non-blank identifier, not the reported extent. |
| **The requester's scope holds fewer than MIN_POPULATION_FOR_RANKING units** | A SMALL POPULATION. Take the whole of 11.7.1. SD-POP-25. |
| **The unit of business is COARSER than the requester's own scope level** | A BINDING MISMATCH, not a small population. Take the whole of 11.7.2. SD-POP-26. |
| **The ranking measure is identical across the whole population** | The measure factor is INERT. Take the whole of 11.7.3. SD-POP-27. |
| Fewer eligible units than the list size, with the population at or above MIN_POPULATION_FOR_RANKING | A normal SHORT LIST. Deliver every eligible unit, say so, and NEVER pad the list. This is not the same thing as a population too small to order; do not conflate them. |
| **A TARGET OF ZERO**, which is a divisor of zero arriving from the PLAN rather than from the population | Attainment against it is UNDEFINED. No ratio is emitted and none is approximated, the win-or-miss classifier does not fire, and the measure ships with its count and its denominator population. **NEVER substitute a small number for the zero and NEVER invert the measure to make it divide.** A target of zero is a legitimate and common target, and it is the one divisor a population guard never sees, because it is not drawn from the population at all. |

Never emit a number you could not compute. A median over fewer than
MIN_POPULATION_FOR_NORM units is NOT a norm: print the figure with the count
beside it and skip the comparison rather than presenting a fragile number as a
benchmark. SD-POP-19.

The row that used to sit here, "a one or two unit scope needs no special rule
because the average-rank percentile is well defined there", was true
arithmetically and false operationally, and it is replaced by 11.7.1 and 11.7.2.
The arithmetic argument is kept and answered rather than deleted: an average-rank
percentile over one unit IS well defined and equals a constant, and a rank of one
out of one IS well defined. **The test is not whether the number computes. It is
whether the number carries information.** SD-POP-25.

### 11.7.1 A population too small to order. SD-POP-25.

MIN_POPULATION_FOR_RANKING is the population below which ranking, percentile,
median, distribution and peer language are MEANINGLESS. It is tested against the
population the READER'S OWN SCOPE contains, not against the file. Below it the
run does NOT emit a ranked list, does NOT print a percentile, and does NOT use
comparative language, however well the arithmetic behaves.

What the output becomes instead, and it is not nothing. All five, in this order:

1. Say it on the FRONT PANEL, BEFORE the content, in plain words: this scope
   contains n units, so nothing here is ranked, no percentile is printed, and no
   comparison is drawn.
2. DELIVER THE ROWS. Everything that DESCRIBES a unit rather than ORDERING it
   survives: the identity block, the open work, the directed items, the
   exceptions, the narrative column. Every section in TAB_CONTRACT still ships,
   per SD-CTR-07; the rank column and the percentile column are written blank with
   their headers present, per SD-CTR-13, and the front panel says why.
3. NAME EVERY SUPPRESSED COMPARISON BY NAME, so the reader can see what was not
   attempted rather than assuming it was attempted and came back empty.
4. NAME THE SCOPE LEVEL, or the finer thing, that WOULD produce a rankable
   population for this reader, so the answer is actionable rather than a refusal.
5. Where another skill in the bundle scores a unit the reader genuinely chooses
   between, SAY WHICH ONE AND WHY. A scorecard whose scoring unit is the
   REQUIREMENT rather than the ENTITY produces a real deliverable for a reader
   who owns exactly one entity, and routing there is an answer rather than a
   deflection. SIBLING_SKILLS names the destination.

Never pad. Never present a one-row or two-row list as a plan. Never print a
percentile of a population of one.

### 11.7.2 The unit of business is coarser than the reader's scope. SD-POP-26.

This is a DIFFERENT failure from 11.7.1 and it needs a DIFFERENT answer. A small
population is a real population that is simply small. A coarser unit of business
means the reader owns a PART of a unit and cannot receive a ranked list of units
AT ALL, however many units the file holds.

**THE BOUND CHAIN ANSWERS THIS BEFORE ANY DETECTION RUNS, AND THAT IS THE ORDER.**
SCOPE_LEVELS ends at the UNIT level, per reference/schema/ GROUP 3, so where the
chain is bound, UNIT_LEVEL_KEY is its FINEST level and NOTHING IS DETECTED. The
detection below is the FALLBACK for a run with no bound chain, which on a
provisional run is the ordinary case, per 3.2.

Detection, where no chain is bound: the scope level whose DISTINCT VALUE COUNT over
the in-scope population equals the RECORD COUNT of that population is the level at
which one unit sits. Compare it against the reader's own resolved level:

| Relationship | Meaning | Behaviour |
|---|---|---|
| Unit level is COARSER than the reader's level | The reader owns a part of a unit | Say so BEFORE the content, NAME BOTH LEVELS, and take 11.7.1 steps 1, 3, 4 and 5. This is reported as a BINDING ERROR, addressed to BINDING_OWNER_NAME, not as a thin scope. |
| Unit level EQUALS the reader's level | The reader owns exactly one unit | Both 11.7.1 and this row fire. Say both things: the scope holds one unit, and at this level the ranked list ranks nothing. |
| Unit level is FINER than the reader's level | Normal | Proceed. |

**THE TIE-BREAK, and it is not optional.** Where MORE THAN ONE level satisfies
the test, take the FINEST matching level. More than one level always satisfies it
when the in-scope population holds exactly ONE RECORD, because every level then
has exactly one distinct value, and the stated fallback for no level matching
does not apply because they all match. The finest is the right tie-break because a
finer level can never be the wrong answer for a reader who owns it.

**THE SECOND TEST, before any binding error is reported.** A binding error is
reported ONLY where the reader's own level is strictly FINER than EVERY level that
satisfies the test over a population of MORE THAN ONE RECORD. Where the population
holds one record the detection is UNINFORMATIVE: the run says the scope holds one
unit and does NOT assert a configuration mismatch it cannot distinguish. Without
this, the coarsest reading tells a reader who owns exactly one unit that their
correct configuration is a binding error, and the finest reading never tells the
binding owner that the unit of business is coarser than the reader's scope, and
both artifacts pass every gate.

Where UNIT_LEVEL_KEY is unbound, the detected value is used and the detection is
NAMED in the audit, per its reference/schema/ SECTION A1 notice. Where no level
matches, the finest level in the chain is assumed and the assumption is named.

**THAT FALLBACK IS CORRECT BY CONSTRUCTION NOW, AND IT WAS CATASTROPHIC BEFORE.**
It is correct because the chain ENDS AT THE UNIT: the finest level in the chain is
the unit level, so assuming it lands on the right answer rather than on the
reader's own level. It was catastrophic on a chain wrongly bound to stop at the
finest OWNED level, because the fallback then returned the reader's OWN level, the
row below concluded that the reader owned exactly one unit, and the ranked list,
the percentile and every comparative sentence were removed from the artifact of a
person holding dozens of live units. **NO GATE CATCHES IT, WHICH IS WHY IT IS
STATED HERE RATHER THAN LEFT TO THE SCHEMA.** The second test on this page does not
fire, because it reports a binding error only where the reader's level is strictly
finer than every level SATISFYING the test, and in that state NO level satisfies
the test at all. The funnel reconciles, every invariant passes, and the artifact is
internally consistent and wrong. GROUP 3 states why the chain must include the
unit; 5.2 states what the same bad chain does to the role anchor at the other end;
this is where the cost lands on the ranked list.

**SO WHERE THE FALLBACK FIRES, NAME WHAT IT ASSUMED AND NAME THE TEST THE BINDING
OWNER CAN RUN.** The run says which level it assumed, that it assumed it because
no level's distinct value count matched the record count, and that the assumption
is right if and only if one of those is one line on this report. Where the run
ALSO concludes the scope holds a single unit off that fallback, it says both
things in one place, because a reader who is told only the conclusion cannot tell a
genuinely single-unit scope from a chain that is one level short.

### 11.7.3 A uniform measure contributed nothing, and the output says so. SD-POP-27.

Where the ranking measure takes the SAME VALUE for every unit in the population,
every unit receives the same percentile, the measure factor becomes a CONSTANT,
and the ordering is decided ENTIRELY by the other terms in the bracket. That is
often the correct behaviour. It is NEVER an acceptable silence.

Three things, all mandatory:

1. State it on the front panel IN THOSE WORDS: the measure was identical across
   every unit, so it contributed nothing to the ordering.
2. NAME THE TERMS THAT ACTUALLY DECIDED THE ORDER: the base term, the alignment
   term, the gap terms, the workload term and the steer, with the count of units
   each moved.
3. NEVER print a measure percentile column of identical values without that
   statement beside it.

**AND AT THE ENDS OF THE SCALE, SAY THE PLAIN THING.** SD-LNG-12. The percentile
is average rank over N, so the largest unit sits at exactly 1.0. The figure is
printed unchanged in its column, and it is never rounded, capped or suppressed,
because rounding it down is a lie and capping it breaks the reconciliation. What
changes is the SENTENCE: the narrative for the top row says the measure is THE
LARGEST IN THIS LIST, naming the list, with the figure beside it; the bottom row
says THE SMALLEST IN THIS LIST. Where the endpoint is shared, name the tie: the
largest in this list, tied with the stated number of others. A superlative
asserted over a tie is the one falsehood this rewrite could introduce, and naming
the tie is what prevents it. The substitution fires at the exact endpoints only:
one place inside, "the 99th percentile" is a phrase people understand and it
stands.

This is also one of the three cold-start detection tests, per SD-CLM-28 test 3
and 14.8: a population with no measure history looks exactly like this when it
has no entry date to read either. Where the uniformity test fires AND the
population is detected COLD, take 14.8 as well as this section.

## 11.8 The mandatory section cap, cut on the honest axis

SD-RNK-07. When the directed set exceeds REFERENCE_CAP, cut it by MEASURE rank,
never by score. Publish the top REFERENCE_CAP by measure, order the DISPLAYED
rows by score, and say MEASURE in the disclosure.

The reason: score multiplies by the measure percentile and the zero bucket
forces every no-measure unit to the bottom, so a score-ranked cut deletes exactly
the directed units the guarantee in SD-MND-03 protects, silently, and the
showing note discloses a count without disclosing the bias. Writing
"highest-scoring" in that disclosure is both false and dangerous, because an
implementer reading the sentence as the instruction would cut by score.

The general form: **a cap must be applied on an axis that does not interact with
a protection elsewhere in the method.**

## 11.9 FIXED and FLOW inside this stage

Both shapes rank, both exclude, and both produce the same sections. What changes
is what "the population" MEANS. SD-POP-21. The full treatment of both paths is
PART 23, which is not an appendix: read it before implementing this stage.

Under FLOW, units removed because they are closed, withdrawn or outside the open
set are reported with their counts IN THE FUNNEL exactly as any other exclusion
is. They are never silently absent. SD-POP-22.

---

# PART 12: STAGE 8, SCORING. THE HEART OF THIS SKILL.

Everything in this part is doctrine. Every constant is a bound variable. The
SHAPE is portable as written; the numbers are configuration.

## 12.1 The formula, written out and implemented exactly

SD-SCO-14. SCORE_FORMULA_SHAPE holds it and it reads:

    score = ( BASE_TERM
            + alignment
            + gap
            + min(workload_count, WORKLOAD_COUNT_CAP) times WORKLOAD_MULTIPLIER
            + steer )
            times ( measure_pct raised to the power MEASURE_EXPONENT )

    where alignment = the sum, over SCORING work items only, of
            entity_weight
            times close_weight
            times source_boost
            times work_weight
            times local_boost
            times narrowness_multiplier
            times own_action_multiplier

    and the ZERO BUCKET is applied AFTER the score and BEFORE the rank.

**SEVEN FACTORS, NOT FIVE, AND THE LAST TWO ARE NEUTRAL UNTIL THEIR OWN TEST
FIRES.** This is where NARROWNESS_MULTIPLIER and OWN_ACTION_MULTIPLIER multiply,
stated here and nowhere else, because 12.7 and SD-PRI-24 and SD-PRI-23 declare
both mandatory and an earlier statement of this product named only five, so a
reader following 12.1 as exact applied neither and a reader following 12.7 applied
them somewhere of their own choosing. Both readings were defensible off one
contract, which is the failure a single written-out formula exists to prevent.

- `narrowness_multiplier` is NARROWNESS_MULTIPLIER where the item is flagged on
  LESS THAN NARROWNESS_THRESHOLD of the ranked in-scope population, using the same
  N that supplies the percentile denominator, and is the NEUTRAL VALUE ONE
  otherwise. SD-PRI-24.
- `own_action_multiplier` is OWN_ACTION_MULTIPLIER where the published marker
  OWN_ACTION_MARKER_CONCEPT is present on the item, and is the NEUTRAL VALUE ONE
  otherwise, including on every run where no column carries the marker at all.
  SD-PRI-23.
- **Both are PER ITEM and both multiply the item's own alignment contribution,
  inside the sum and before it.** Neither multiplies the finished score, neither
  multiplies the bracket, and neither is applied twice: SD-WGT-19 forbids a factor
  entering twice and each of these enters exactly once, at one place, on one item.
- **Neither is reachable from a PREDICATE match.** A row matched by 8.8.1 takes
  neither multiplier, because it takes no alignment contribution at all.
- **The neutral value is ONE and it is never a penalty.** SD-WGT-02's floor
  discipline: an item that is not narrow and carries no marker scores exactly what
  it scored before, so doing the work of publishing a narrow instruction or a
  marker can only ever RAISE a result and never lower one.
- **Both are PRINTED.** The Method section's worked example carries all seven
  factors with the value each took on that item, and any row where either
  multiplier was other than neutral says so in its reason-for-rank string, per
  1.3, because a term that moved the position is named in the order it
  contributed.

Every constant is referenced BY NAME. Every term below has a named source so two
implementers score the same units. The formula and a worked example are printed
in the Method section of every artifact, so a disagreement can be traced to a
specific term and corrected rather than argued. SD-CTR-21.

**Say what the multiplicative shape actually does.** SD-SCO-15. The bracket
ranges from its base to roughly an order of magnitude. The measure factor ranges
from zero to one and can ONLY SCALE THE BRACKET DOWN. Among the units competing
for the top, the measure varies only slightly while the bracket can vary
several-fold. The measure is therefore the TIE-SHAPER rather than the sole rank
driver. Do NOT describe it as the dominant term in the ordering, because it is
not. Describe the model's actual behaviour, not its intended emphasis.

## 12.2 CLOSE DATE FIRST, and never activity count

**Rule 1 is primary and sufficient on its own.** SD-SCO-01. Work three rules in
order and stop at the first that fires:

| Order | Rule | Effect |
|---|---|---|
| 1 | Read the PUBLISHED due date for the item. **Supervisor naming and local loading are not triggers here and never set a close weight**, per the note below. | The close weight comes from the date, per 12.3 and the state ladder of 12.3.1 |
| 1b | THE UNIT'S OWN COMMITMENT DATE. Where a unit-level commitment date RESOLVES, POPULATES and passes its date value check, per 12.2.1, the UNIT carries ONE implicit work item at WORK_TYPE_BASELINE_KEY, dated by that date. **There is no in-window condition on the firing of rule 1b.** | The close weight comes from that date, per 12.3, and 12.3 bands it wherever it falls. Subordinate to rule 1: a published due date on a real work item always wins. |
| 2 | Read a PERIOD TOKEN in the item's own name, resolved THROUGH the operating window | The close weight comes from the resolved window |
| 3 | No derivable date | DROPPED from scoring entirely |

**WHO NAMED AN ITEM IS NOT A FACT ABOUT ITS DATE, AND THIS LADDER NEVER READS IT.
STATED ONCE, HERE, AND CITED EVERYWHERE ELSE.** An earlier statement of rule 1 gave
a supervisor-named or locally loaded item the full close weight outright, and 12.6
consequence 3 said the same thing one section over, while 12.3.1's state ladder
assigns a state PURELY FROM A DATE, exhaustively over the number line, and 18.1
gates on the label and the weight AGREEING. Measured: four accounts named by a
branch manager's directive, three of them with dates outside the planned window,
had no assignment that satisfied both readings. Following the old rule 1 put the
full weight beside a label saying the date falls after the next window, which 18.1
fails; following the ladder made the old trigger unreachable for any date at all.
**A correct artifact failed its own gate whichever text the run believed.** The
reconciliation is the one 12.3.1's own opening already implies, and it is a single
direction:

- **THE CLOSE WEIGHT COMES FROM THE DATE AND FROM NOTHING ELSE.** 12.3.1 is the
  SOURCE of the state and, through CLOSE_WEIGHTS, of the weight; 12.3's table is a
  READING of it. There is no second assignment path and no tenth state.
- **SUPERVISOR NAMING AND LOCAL LOADING ARE CARRIED ON THE TERMS THAT ARE ABOUT
  THE SENDER**, which is where they belong and where they were always strongest:
  the local boost and the work-type override of 12.6, the source boost, the chain
  distance and the narrowness of 12.7, and MANDATORY_MULTIPLIER where 8.7.1's
  ladder resolves the reader as the actor. **Not one of those reads the close
  weight, so nothing is lost and the directive still outranks unnamed work.**
- **A LOCALLY LOADED OR SUPERVISOR-NAMED ITEM IS NEVER DROPPED FOR WANT OF A DATE**,
  which is the failsafe the old trigger was carrying and which is kept in the one
  place it belongs. Being loaded against the reader's own unit, or named in a
  directive for the planned window, IS the naming that state 2 of 12.3.1 tests for.
  So where such an item's own date cannot be read, it takes state 2 and state 2's
  weight, rather than falling to rule 3 and out of the scoring. Where a date IS
  read, the state and the weight come from that date like every other row, and the
  row says what is true of that date.
- **THE ROW STAYS TRUE AND THE GATE HAS ONE NUMBER TO CHECK.** 18.1's agreement
  assertion now compares the label, the weight and the wording against ONE
  assignment, so a row that passes it is a row whose date and whose weight say the
  same thing.

This is named as the most damaging way to implement scoring wrongly, and the
reason is stated so it cannot be re-derived wrongly: rule 2 is the one with
concrete mechanics, a token to search for, so an implementer naturally reaches
for it and treats rule 1 as commentary. That INVERTS the ladder.

> The absence of a date token in a column header is NOT evidence that the item
> has no close date; it is the normal case, because sources name work by what to
> do rather than by when.

The documented harm: the two largest live items in a real file carried no token,
so a rule-2-first implementation scored them at ZERO, and nothing in the output
looked wrong.

### 12.2.1 A commitment date carried on the UNIT is first class

Some businesses carry their most important date on the UNIT, not on a work item.
A renewal, an expiry, a term end, an anniversary, a next review, a licence
lapse: the date that decides what a person does next period is an ATTRIBUTE OF
THE UNIT, and there is no work-item block in the export at all. FIELD-RESOLUTION
PART 4 correctly returns "no block exists", which is a valid outcome.

Without rule 1b, every route into the alignment term and the workload term runs
through a work item, so both terms are ZERO for every unit, the gap terms are
zero too because the source carries none of their concepts, and the score
collapses to the base term times the measure percentile raised to the exponent.
**The list is then the population sorted by size.** That is not wrong and it is
not a plan, and it silently contradicts this skill's own core rule, which is
commitment date FIRST and never activity count. SD-SCO-01, SD-WGT-17.

**The unit-level commitment concept, and the exact wiring this rule reads.**
Resolve it through COLUMN_CONCEPT_DICTIONARY exactly as any other concept
resolves. The shipped seed entry is `concept_unit_commitment_date` in
reference/field-resolution.md 6.6, and rule 1b reads THREE things, all of which must hold:

| # | What rule 1b reads | Required value |
|---|---|---|
| 1 | The concept's value check | `date` |
| 2 | The concept's `feeds` list | It must name THE UNIT-LEVEL CLOSE WEIGHT AND THE WORKLOAD COUNT. That exact feeds value IS the switch. |
| 3 | The concept's forbidden neighbours | `concept_last_engagement_date` and `concept_exit_date`, declared reciprocally on all three entries, so a last-contact column is never read as a date something is DUE, and an exit date recording when a unit LEFT is never read as a date on which something on a standing unit FALLS DUE |

**The match is on the FEEDS VALUE, not on the concept KEY.** An organization that
adds its own unit-level date concept under a different key fires rule 1b if and
only if that entry's feeds list names the unit-level close weight and the workload
count. The seed key is the entry the shipped dictionary provides; it is not the
test.

**The `feeds` list IS the switch.** A concept dictionary entry already declares
which flags, gates, weights and benchmarks it supplies. A unit-level date concept
whose feeds list names those two is admitted by rule 1b. One whose feeds list does
not is recorded, DISPLAYED, and scores nothing. No separate on-off variable is
needed and none is invented: the decision is where the schema already puts it.

The seed dictionary is a starting dictionary and not a closed list, per standing
rule S4 and FIELD-RESOLUTION F0.3. Where an organization's own column matches none
of the seed stems, the run resolves it by the concept's own value check against
the unresolved date columns, per FIELD-RESOLUTION F5.1 step 2, then proposes the
stem for promotion under PART 7 and names it in the audit. **Promotion is a
later-run improvement and is never what rule 1b depends on. On a FIRST run against
an unbound dictionary the seed entry above is what makes rule 1b fire, and if that
entry were absent from the shipped dictionary the rule could not fire at all and
the ranked list would silently reduce to the population sorted by size.**

**THE FIRING CONDITION, STATED ONCE.** Rule 1b fires for a unit when, and only
when, all three of these hold, and nothing else is tested:

1. A unit-level commitment date concept RESOLVES, per the wiring above.
2. It POPULATES for that unit and the value passes its date VALUE CHECK.
3. The unit is in the ranked population.

**There is NO in-window condition and there never was one to apply.** An earlier
revision of the rule-1b table row added "and it falls inside the operating
window", which contradicted this paragraph and gave two competent readers two
different populations and two different published orderings. The in-window
reading is the wrong one and it is now deleted rather than reconciled, for four
reasons: the table row points here with "per 12.2.1", so this paragraph governs;
12.3's ladder is written to be EXHAUSTIVE over the number line, which is
meaningless if only in-window dates can ever reach it; SD-SCO-06 requires expired
work to stay VISIBLE at the floor weight, which requires out-of-window items to
exist as items; and under the in-window reading every implicit item would carry a
close weight of 1.00 by construction, the five-band ladder would be unreachable
for any unit-attribute source, and the ranked list would collapse back to the
population sorted by size, which is the exact defect rule 1b exists to fix.

**Precedence, and it is data-derived rather than defaulted.** Per G6 and
SD-CTR-24, a value DERIVED FROM THE DATA THIS RUN outranks a documented default.
A resolving, populated, date-checked unit-level commitment concept IS that
derived evidence. The presence or absence of a work-item block does NOT gate rule
1b: where no block exists it is the only route into the alignment and workload
terms, and where a block DOES exist both routes are live at once, with rule 1
winning for the work items themselves and rule 1b still contributing the unit's
own one implicit item.

**Six constraints, all of them, and they are what stop this becoming a weighted
attribute count:**

1. EXACTLY ONE implicit item per unit, never more, whatever number of date
   columns resolve. A unit never climbs on the volume of its own attributes.
   SD-WGT-17.
2. It takes WORK_TYPE_BASELINE_KEY, never a higher type, because no verb was
   read and SD-WGT-15 forbids defaulting an unclassified item upward.
3. It is subject to the SAME three scoring conditions in 12.4, with condition (a)
   satisfied by the unit carrying the date.
4. It is dated ONLY by the unit's own date. An unreadable or absent unit date
   produces NO implicit item; it is never defaulted to this window. SD-PRS-03.
5. It is NAMED AS IMPLICIT on the row and in the audit, and THE DATE ITSELF IS
   PUBLISHED on the row in HDR_COMMITMENT_DATE, per 1.3b, because a unit whose
   whole position in the ranking comes from a date it carries must show that date
   in a column rather than only inside a sentence. It is counted SEPARATELY in
   the rule-split report required by SD-LNG-04, so a reader can see how much of
   the ordering came from unit dates rather than from work items.
6. **This is the ONLY circumstance in which a unit attribute becomes a work
   item.** Do not generalize it to any other attribute. A commitment date is a
   commitment; a segment label, a status, a band and a score are not.

Where the concept resolves but the run is not confident it is a commitment rather
than a record-keeping date, that is decision point 67 in PART 22. Fire it if the
answerer is authorized. If declined, the concept is recorded and DISPLAYED in the
identity block and scores nothing, and the artifact says that no unit-level
commitment date was scored and which column would have supplied one. That is the
floor of the scale and binding it later can only raise a result, per SD-WGT-02.

Report the count of items dated by EACH rule SEPARATELY, including rule 1b.
SD-LNG-04. Naming the split is what makes the rule-inversion bug VISIBLE: a run reporting zero items
dated by rule 1, on a period whose central publication named several, has
inverted the ladder. Instrument the audit trail specifically so the known
failure mode has an observable signature.

**Admission and weight are separate answers from ONE matcher.** SD-SCO-02.
Matching the published source decides ADMISSION. The published date then decides
the CLOSE WEIGHT independently. Use one matcher; read two things from it:
membership, and the date. Never assume the date from the membership. A matched
item is always admitted and is not always closing this period.

Precedence, stated once so nothing has to be re-derived. SD-SCO-04: the
published due date always wins; then the operating window; then a period token in
the name, resolved THROUGH the window.

Read the date; never assume the window. SD-SCO-01 and SD-PRS-04. The published
due date is PER ITEM and frequently falls outside the period window. On one real
file that error applied full weight to the single largest item in the file.

## 12.3 The close weights, each with exactly one trigger

SD-SCO-07. CLOSE_WEIGHTS holds the permitted values and NO OTHERS. The standing
set and its triggers:

**12.3.1 IS THE SOURCE OF THE WEIGHT AND THIS TABLE READS IT.** Every trigger below
is a fact about a DATE, and each one is the plain-language reading of one state of
12.3.1, whose ladder assigns the state and whose CLOSE_WEIGHTS entry carries the
weight. Where this table and 12.3.1 appear to differ, **12.3.1 GOVERNS**, because it
is exhaustive over the number line and it is what 18.1 gates on. Nothing about who
named an item, who loaded it or where it came from appears here: those act on the
terms 12.2's note names, and never on the close weight.

| Weight | The one trigger |
|---|---|
| 1.00 | Confirmed to close in this window by a date that was read, which is state 1 of 12.3.1 |
| 0.75 | Named in THIS window's publication and the date could not be read |
| 0.50 | The text implies the NEXT window, or a read date falls inside it |
| 0.35 | A read date falls AFTER the next window but still inside the near horizon: ninety days measured from the CLOSE OF THE PLANNED WINDOW, never from the run date |
| 0.20 | Beyond the near horizon, or a date falling BEFORE the planned window opens. The single weight covers several DIFFERENT date facts, and 12.3.1 gives each of them its own true row label. |

**EVERY BAND IS ANCHORED ON THE PLANNED WINDOW, NEVER ON THE RUN DATE.** "This
window" in the 1.00 band means the window BEING PLANNED, not the window the run
happens to be executing in, and every other band inherits that anchor so the
ladder cannot contradict itself. The near horizon is therefore
CLOSE_HORIZON_DAYS, default ninety, counted forward from the LAST DAY OF THE
PLANNED WINDOW. A plan for the coming period built a few weeks early must not
band its items differently from the same plan built on the first morning of that
period, and anchoring on the run date does exactly that.

This is not a hair being split. On one real file of a couple of hundred records,
the two anchors moved 8 percent of the population between the 0.35 and the 0.20
band, which reorders the published list and hands two competent readers two
different top-twenty lists off the same file and the same configuration. Print
the anchor date itself in the Method section, as a date, so the banding can be
reproduced without inferring it.

**THE LADDER IS EXHAUSTIVE OVER THE NUMBER LINE, AND IT IS CHECKED FOR GAPS
BEFORE ANY CHANGE SHIPS.** A closed set of weights is only closed if every
derivable date falls in exactly ONE band. The 0.35 band exists because an earlier
standing set ran from the next window straight to the far horizon, leaving dates
after the next window but inside ninety days in NO band. Those items were then
either dropped or banded to the floor on an implementation's own judgment, and
two implementations differed off the same file. When a band is added or a
boundary moved, re-check the ladder for gaps first.

**Never produce an intermediate weight from a date you successfully read, and
never default an unreadable date to full weight.** An unreadable date is BANDED
DOWN, never defaulted up. SD-PRS-03. Silently defaulting an unparsed date to
"closes this period" is the exact over-weighting bug this rule exists to
prevent, and it is invisible in the output. This is G3 in its sharpest form.

The probable-this-period weight contributes ZERO to the workload count, because
that count requires CERTAINTY, and the weight exists precisely to record that
this period is probable rather than confirmed.

Anything with no derivable date is DROPPED from scoring entirely, not
down-weighted. SD-SCO-05. UNDATED_ITEM_TREATMENT must be dropped_from_scoring. A
unit is not more important because it carries five undated flags.

Expired prior-period work stays VISIBLE at the floor weight and contributes ZERO
to workload. SD-SCO-06. A token resolving to a window that closed strictly
before the current window opened bands to the floor weight and zero toward the
workload count, labelled with CARRYOVER_LABEL on the row, so a person who still
owes the work can see it, but it can never outrank current-period work and never
inflates the workload count. Only current-period work is ever at full weight.

### 12.3.1 THE CLOSE-DATE VOCABULARY. The label must be TRUE of the date it describes.

**A weight is not a state, and the floor weight is reached by several different
date facts that a reader acts on differently.** One weight, several truths. The
reader is not holding a weight; the reader is holding a date, and the row must
say what is true of THAT DATE.

The failure this closes, and it is the kind that destroys a report on first
reading: an item falling due EIGHT DAYS AFTER the run, before the planned window
opens, correctly banded at the floor weight for a plan about a later window, and
labelled EXPIRED. It has not expired. It expires next week. Somebody reading that
beside a date in the future concludes the report does not know what it is looking
at, and they are right to. The banding was defensible; the word was false.

**The four anchors.** All four are computed and all four are printed as dates in
the Method section, so a label can be reproduced without inferring anything:

| Anchor | Meaning |
|---|---|
| R | the run date |
| the CURRENT window | the window R falls inside |
| the PLANNED window | the window this plan covers, which may or may not be the current one, per PLAN_AHEAD_RULE |
| the NEAR HORIZON | CLOSE_HORIZON_DAYS forward from the LAST DAY of the planned window |

**The states, evaluated in this order, first match wins, exhaustive over the
number line.** Each row gives the STATE KEY, the test that assigns it, and the
weight it carries. **THE WORDS ARE NOT HERE.** Both strings a state ships, the
SHORT LABEL that goes in the HDR_CLOSE_STATE column and the EXACT WORDING that
goes on the row, are looked up in CLOSE_STATE_VOCABULARY by the state key, and
this file writes neither. The states, their tests, their weights and their order
are METHOD and belong here; what a state is CALLED is wording and belongs to the
binding, exactly as every header string does under 0.5.

| # | State | STATE KEY | Test on a date D | Weight |
|---|---|---|---|---|
| 1 | DUE THIS PLAN | `due_this_plan` | D inside the planned window | 1.00 |
| 2 | DATE UNREADABLE | `date_unreadable` | named for the planned window, D could not be read | 0.75 |
| 3 | DUE NEXT WINDOW | `due_next_window` | D inside the window after the planned one | 0.50 |
| 4 | DUE ON THE NEAR HORIZON | `due_on_near_horizon` | D after the next window and on or before the near horizon | 0.35 |
| 5 | DUE BEYOND THE HORIZON | `due_beyond_horizon` | D after the near horizon | 0.20 |
| 6 | **DUE BEFORE THIS PLAN STARTS** | `due_before_plan_starts` | D on or after R, and D before the planned window opens | 0.20 |
| 7 | **PASSED, IN THE WINDOW NOW CLOSING** | `passed_this_window` | D before R, and D inside the current window | 0.20 |
| 8 | **PASSED IN AN EARLIER WINDOW** | `passed_earlier_window` | D before R, and D before the current window opened | 0.20 |
| 9 | NO DERIVABLE DATE | `no_derivable_date` | no date could be derived at all | not scored |

**Both strings ship on every row and neither replaces the other**, per the
CLOSE_STATE_VOCABULARY entry for the state. A label short enough to sort a column
by cannot carry the day count, the horizon date or the carryover label, and a
sentence long enough to carry them cannot be sorted or scanned. Publishing only
the label would drop disclosure; publishing only the sentence is what left a
reader unable to see, at a glance, why a later-dated unit outranks an earlier one.
The label is byte-identical between runs for a given binding, per SD-CTR-09.

**A ROW NEVER SHIPS WITH AN UNLABELLED CLOSE STATE.** Every derivable date lands
in exactly one of the nine keys, and the vocabulary is required by its own
validation to be total over all nine, so a lookup cannot miss. Where a BOUND
vocabulary fails that validation, whether by a missing key, a repeated key, an
added key, an empty label, an empty wording, a placeholder inside a label, or the
carryover placeholder appearing anywhere other than `passed_earlier_window`, the
run does NOT fall back to writing its own words and does NOT ship the state key
raw as a label. It REJECTS the binding, applies the reference/schema/ SECTION A1
default for the whole set rather than for the failed entry alone, prints that
appendix's exact degradation notice, names in the Method section which validation
the bound set failed and on which key, and raises it once with the binding owner
per PART 22. Repairing one entry from a bound set and keeping the rest would ship
a row in the organization's words beside a row in the default's, which is the
second source of truth 0.5 exists to prevent.

**CARRYOVER_LABEL attaches to state 8, `passed_earlier_window`, and to NOTHING ELSE**, which CLOSE_STATE_VOCABULARY's own validation enforces rather than leaving to whoever writes the wording. It is the label for
work that has genuinely passed in an earlier window, which is what SD-SCO-06 is
about. Applying it to state 6 or state 7 is what produced the false word. States
6 and 7 are also not "carryover" in the ordinary meaning, because state 6 has not
happened yet and state 7 happened inside the window the reader is standing in.

**Three things this does NOT change, and they are failsafes:**

1. **No weight moves.** States 5 through 8 all sit at the floor weight, exactly as
   the bound CLOSE_WEIGHTS ladder puts them. The published ordering is byte for
   byte what it was. This fix changes only what the row SAYS about the date.
2. **Nothing that was disclosed becomes undisclosed.** Every state is still
   printed on the row, still counted in the Method section, and states 5 through 9
   still contribute ZERO to the workload count, because that count requires
   certainty of closing inside the planned window.
3. **The ladder stays exhaustive.** Every derivable date falls in exactly one of
   states 1 through 8, and every non-derivable one in state 9. States 6, 7 and 8
   partition the old merged floor band with no gap and no overlap: 6 is on or
   after R and before the planned window opens, 7 is before R and inside the
   current window, 8 is before R and before the current window. Where the planned
   window IS the current window, state 6 is empty by construction and the run says
   so rather than leaving a reader to wonder.

**The front panel carries the state 6 count as a lead figure**, per 19.3.1 block
1, in these words: `{n} {item|items} {falls|fall} due BEFORE this plan starts,
between {R} and {the day before the planned window opens}`, and where n is zero
in its own sentence, `Nothing falls due before this plan starts`. **The rows themselves ship in the
do-this-week block, 19.3.1 block 2**, which lists them with their ranks and the
sections they sit in, changes no weight, no rank and no membership, and prints
the line that stops a reader counting them twice. That is a real instruction to a reader, it
changes what they do this week rather than next period, and burying it under a
label that said EXPIRED is what made the artifact indefensible. It changes NO
weight and NO rank; it is a disclosure, not a re-weighting.

Report the count of items in EACH state separately, per SD-LNG-04 and SD-LNG-05,
naming states 6, 7 and 8 apart from one another rather than reporting one merged
floor-band figure.

Name every item that took a FALLBACK weight and the weight it took. SD-LNG-05.
Name every item weighted ZERO, by name and count. SD-LNG-06. A large item that
scored nothing must be visible, so a person can see that it was deliberately
scored low rather than wonder why their biggest number moved nothing.

## 12.4 What counts as a SCORING item: three conditions, and one subsumes another

SD-SCO-08. An item contributes to the alignment term only when ALL THREE hold:

(a) the item is FLAGGED at this unit, OR the item is the ONE implicit item
    generated by the unit's own commitment date under rule 1b, in which case the
    unit itself is what carries it;
(b) it has a DERIVABLE CLOSE DATE;
(c) it MATCHES A STATED PRIORITY, or it carries the user's own scope code, or it
    is the implicit item under rule 1b, whose priority is the commitment itself.

Condition (c) automatically satisfies (b), so (b) never independently rejects an
item that (c) accepted.

The rule 1b extension of (a) and (c) is deliberately narrow and is the ONLY
extension either condition takes. It exists because a commitment the organization
made on a unit is a stated priority by construction: nobody has to name it for it
to be due. Its entity weight resolves from the unit's own entity where one
resolves, and takes ENTITY_WEIGHT_FLOOR where none does, per SD-WGT-02, so
resolving the entity can only raise the score.

> An item the unit carries that matches no stated priority contributes NOTHING
> to this term, however many of them there are.

That is what stops the term becoming a weighted item count, which is forbidden.
SD-WGT-17: never rank on how many work items a unit carries. Rank on the
measure, the alignment and the number that must close this period. A high-measure
unit with two closing-now items outranks a mid-measure unit with nine undated
ones.

## 12.5 Work-type weighting: not all work builds the business

**Weight by WORK TYPE on a closed graduated scale.** SD-WGT-10. Exactly one type
per work item. No extra type. No "other". WORK_TYPES holds between three and
eight entries with strictly decreasing weights and exactly one marker at weight
zero.

The scale orders work by HOW MUCH THE STATE OF THE WORLD CHANGES BECAUSE THE
PERSON SHOWED UP. The standing six-rung ladder, with neutral invented examples:

| Rank | Type | Weight | What it is | Neutral worked examples |
|---|---|---|---|---|
| 1 | change_a_decision | 1.25 | Persuade a counterparty to commit to something new | Get a decision maker to agree to a trial, an expansion, a renewal uplift, a review |
| 2 | change_a_state | 1.00 | Physically or systemically alter something | Configure, migrate, install, deploy, set up, replace |
| 3 | change_knowledge | 0.75 | Change what someone knows | Train, enable, brief, demonstrate |
| 4 | confirm_state | 0.50 | Confirm an existing state | Audit, verify, inspect, health check. Necessary, but nothing changes because the person went |
| 5 | produce_record | 0.25 | Produce a record | Log, survey, form, record hygiene |
| 6 | label_only | 0.00 | A LABEL, not an instruction | A segmentation marker naming the unit's standing |

The binary that this scale replaced collapsed all of that into two buckets and
MIS-TYPED THE SINGLE HIGHEST-VALUE ITEM in the file. That is why it is a
graduated scale.

**A marker is not an instruction.** SD-WGT-11. The bottom rung admits the unit
to the population and appears on its row, but it ASKS FOR NOTHING, so it scores
nothing. It is considered; it is not scored. This is one of the sharpest
distinctions in the corpus and is entirely universal.

Work-type weight multiplies the ALIGNMENT term and nothing else. SD-WGT-12. A
zero-weighted marker still counts toward the workload count if it carries a
close date, still appears in the inventory, and still shows on the row.

**Classify by the VERB, not by the SUBJECT.** SD-WGT-16.
WORK_TYPE_CLASSIFY_BY must be "verb". The most expensive single classification
error in the corpus came from typing an item by its subject rather than its
verb. **Persuading someone to accept a change, making the change, and confirming
the change is still in place are three different jobs, and only the VERB
distinguishes them.** Typing by subject zeroed the highest-leverage conversation
in the period.

Scan the WHOLE name for every verb, then take the HIGHEST type present.
SD-WGT-13. This is deliberate: when a header asks for two things, the person has
to do the harder one, so the harder one sets the weight.

A generic verb sets no type of its own and only promotes UPWARD FROM BELOW.
SD-WGT-14. A verb in GENERIC_COMPLETION_VERBS promotes a low type one step,
resolves to WORK_TYPE_BASELINE_KEY when no specific verb is present, and NEVER
promotes a type already at or above that baseline. One generic verb appeared in
sixteen headers of a real file and would otherwise have stamped all sixteen with
one type. This is the general pattern for handling a semantically empty token.

Verbless names are classified by the NOUN, never defaulted and never dropped.
SD-WGT-15. Roughly half the work-item columns in a real file carry no verb. The
noun rules: a GAP or OPPORTUNITY noun paired with a PHYSICAL-OBJECT noun is
state-changing work; otherwise it is persuasion work, because a gap is something
a person closes by persuading someone. A noun naming only the unit's STANDING is
a marker. Nothing matched is reported BY NAME and weighted at the baseline.
Never silently discount an item the rules did not recognize; surface it so the
dictionary can be extended.

**A published external classification is EVIDENCE, not an override.**
SD-PRI-22. EXTERNAL_WORK_TYPE_IS_EVIDENCE_ONLY must be false, meaning the
external type never overrides. Record it, use it to break a GENUINE TIE, follow
the local ladder where they disagree, and note the disagreement. A central
source types an initiative ONCE while the operating file may carry that
initiative as two or three separate columns asking for DIFFERENT work, and a
single central type cannot be right for both.

Freeze a ground-truth classification and gate on reproducing it EXACTLY.
SD-RUN-11. REFERENCE_CLASSIFICATION_FIXTURE starts EMPTY and is populated from
the first real dataset: apply the classifier to every item of one real dataset,
freeze the result, run the classifier against the fixture BEFORE scoring
anything, and report the match rate. Anything under a perfect match is a FAILING
gate when REFERENCE_FIXTURE_MATCH_REQUIRED is true. An implementation that does
not reproduce the table exactly has a DEFECT IN ITS CLASSIFIER, not a difference
of opinion. Companion rule: on a dataset the fixture does not cover, THE LADDER
IS THE AUTHORITY AND THE FIXTURE IS THE WORKED EXAMPLE.

## 12.6 The supervisor scope boost: locally tagged work is the strongest signal

**Locally tagged work is the strongest signal in the file, and the test runs on
UNPADDED digits.** SD-PRI-18. Extract any scope token from the work item name,
normalize it, and test whether the RAW characters are a LEFT-ANCHORED PREFIX of
the user's own code.

> Do NOT run the prefix test on the padded value.

Padding is for comparing a tag against a scope COLUMN; the prefix test uses raw
characters. Different purposes, and swapping them breaks the rule SILENTLY.
Worked example, neutral: in a scheme padded on the right to six characters, a
mid-level tag of two characters padded becomes a six-character string that is not
a prefix of the user's own six-character code, so every local item fails the test
and the strongest signal in the file evaluates to nothing, with no error.

The three consequences of a local tag:

1. AUTOMATIC ADMISSION. The item does not need to match a published priority.
2. LOCAL_BOOST applied to that item's alignment contribution.
3. **NO CLOSE WEIGHT OF ITS OWN, AND THE ITEM IS NEVER DROPPED FOR WANT OF A
   DATE.** This consequence once read FULL close weight, which contradicted 12.3.1
   and failed 18.1 on any locally loaded item whose date fell outside the planned
   window; 12.2's note reconciles the two and this is the reading it gives. **Local
   loading is a fact about the sender and the close weight is a fact about the
   date**, so the state and the weight come from 12.3.1's ladder like every other
   row. What local loading DOES supply is the naming state 2 tests for: the item
   counts as named for the planned window, so where its own date cannot be read it
   takes state 2 rather than falling out of the scoring under 12.2 rule 3. The
   strength of the signal is carried by consequences 1 and 2 and by 12.7's source
   boost, which is where it belongs and where nothing has to be untrue for it to
   count.

**A DIRECT local tag overrides a work-type zero; a BROADER one does not.**
SD-PRI-20. A tag at the user's own finest LOCAL_OVERRIDE_DEPTH levels overrides
the work-type weight. A tag at a coarser level gives the BOOST but not the
OVERRIDE. The reason: when your own supervisor loads a low-weight task against
your own unit, it is a cannot-miss and it scores; when it arrives tagged to a
whole coarse unit it does not, because many peers load work at coarser levels,
so a coarse tag is closer to a central instruction than to a personal one.

**A top-level user has no scope code, so nothing is local to them.** SD-PRI-19.
Set the local boost to NEUTRAL throughout, admit items on the published and
supervisor tests alone, and SAY SO. An empty code prefixes everything and would
hand the boost plus automatic admission to every tagged item in the file.

A locally admitted item is still subject to the compliance gate. SD-PRI-17.

Foreign-unit tags: no boost, no automatic admission, kept, scored on their own
merits, labelled, counted. SD-PRI-21.

## 12.7 Source boost, distance and narrowness

Source boost. SD-PRI-25:

- SOURCE_BOOST_NONE when NO source named the item. It is the neutral floor, 1.0,
  and it is NOT optional to have a value here: on a run where no message store
  and no document store could be reached, which is the ordinary shape of a first
  run, NO source names ANY item and this is the multiplier applied to every row
  in the file. It is a floor rather than a penalty, per SD-WGT-02, so that doing
  the work of naming a priority can only ever RAISE a result and never lower one,
  and the front panel says which boost was applied and why.
- SOURCE_BOOST_ONE when ONE source named the item.
- SOURCE_BOOST_BOTH when TWO INDEPENDENT sources named it, and it is strictly
  greater than SOURCE_BOOST_ONE.
- Then SCALED by the naming level's CHAIN_DISTANCE_WEIGHTS entry when a
  SUPERVISOR named it. A CENTRAL naming is NOT distance-scaled, because it is
  organization-wide by construction.
- Where several levels named the same item, use the NEAREST namer's weight.

**Two distinctive tokens, or one SPECIFIC name; a family name never matches
alone.** SD-PRI-26. Normalize, drop MATCH_STOPWORDS and short tokens, and
require at least TWO shared distinctive tokens, OR one shared token that is in
SPECIFIC_INITIATIVE_NAMES. A name in FAMILY_NAMES is never a specific name and
always requires a second token.

The documented harm, and it is the reason this rule is not negotiable: a single
message about a family, read as a one-token match, links that message to EVERY
item in that family, so every one of them becomes supervisor-named AND centrally
named and jumps from one source boost to BOTH AT ONCE. One of three runs read
the family token as a match and scored every top-ten unit measurably higher,
which reordered the list. A manager mentioning a family has named a FAMILY, not
an INITIATIVE.

A family-level mention still COUNTS, just not as a MATCH. SD-PRI-27. It enters
the audit as a family-level priority, it steers the weighting, and it can admit
an item when combined with a second token. What it does not do is manufacture a
match against every item in that family. Record family-level and specific-level
mentions separately, with counts.

Stem before comparing. SD-PRI-28. Compare on a normalized stem of at least
MIN_STEM_LENGTH characters, the same rule the column dictionary uses. A match
that depends on plural agreement is not a rule, it is a coin flip.

Show the tokens, or you did not run the test. SD-PRI-29. Record one line per
matched item naming the priority it matched, the shared tokens, whether each is
a family or a specific name, and the resulting boost.

A run where NOTHING matched is a real result and must be visible. SD-PRI-30.
Report items examined, matched to each source, matched to both, and flagged but
matching nothing. Not a silent zero across the alignment term.

Narrowness. SD-PRI-24. Apply NARROWNESS_MULTIPLIER when the item is flagged at
LESS THAN NARROWNESS_THRESHOLD of the ranked in-scope population, using the SAME
N that supplies the percentile denominator. A narrow instruction is a sharper
priority than a blanket one. **WHERE IT MULTIPLIES IS 12.1's ALIGNMENT PRODUCT,
which names it as one of the seven factors, and this section does not state a
second home for it.** It scales the ITEM's alignment contribution, once, and the
neutral value where the test does not fire is one.

"Requires my action" is a PUBLISHED marker, not a reading of the sentence.
SD-PRI-23. Test for OWN_ACTION_MARKER_CONCEPT and nothing else, and apply
OWN_ACTION_MULTIPLIER only where the marker is present, **in the slot 12.1's
alignment product gives it and in no other slot**, with the neutral value one
where the marker is absent. Do not infer it from
verbs in the item name; the marker is a published originator marker, not a
reading of the sentence. When no column carries the marker, NO item takes the
multiplier, and that is RECORDED rather than approximated from verbs.

Priority ranking comes from the organization's OWN PUBLISHED WEIGHTS, not from
anybody's opinion about which item is biggest. SD-PRI-31. Where METRIC_SET
publishes weighted metrics, that ordering IS the priority ranking, and the
weight is named alongside the item wherever the ordering was used.

## 12.8 The standing hierarchy weight

**The entity hierarchy has NO DEFAULT ROW.** SD-WGT-01. An entity that resolves
to none of the entries in CREDITABLE_ENTITIES is not assigned the top weight and
is not assigned anything else either. It is reported as UNMAPPED and takes no
entity weight. Defaulting an unknown to the top weight silently promotes it
above every real entry AT ONCE. That is exactly what happened in a real build,
where the unmapped item became the single largest per-unit contributor in a
scope where it should have been the smallest.

**When a default IS correct, tie it to the hierarchy FLOOR, not to a literal.**
SD-WGT-02. For an item whose entity cannot be resolved but which is admitted on
a local or supervisor test, apply ENTITY_WEIGHT_FLOOR and RECORD that the floor
was applied. Tie the default to the floor so it moves if the table's lowest
weight changes; never hard-code a number that is also a real entry's weight.

> What the floor guarantees is that resolving the entity can only RAISE the
> score, never lower it, because every real weight is at or above the floor.
> Defaulting to the top does the opposite, which rewards giving up.

The general form: A DEFAULT MUST BE POSITIONED SO THAT DOING THE WORK CAN ONLY
HELP. That sentence is the whole of G3 stated positively.

Protect the item while flooring its weight. SD-WGT-03. An item admitted on a
local or supervisor test is STILL admitted automatically, STILL takes full close
weight, STILL takes the source boost and STILL keeps the local boost, so the
floor can never zero it or drop it from scoring. Never let an unresolved entity
remove a local item from scoring.

Entity weight scales the ALIGNMENT TERM ONLY, and never reorders the list by
itself. SD-WGT-05. The final order is the combined score. This is why a
high-measure unit in a lower-ranked entity can and should outrank a small unit in
the top entity. Never let entity rank alone reorder the list.

The user is never expected to know the internal taxonomy. SD-WGT-06. Map any
brand, product, programme or category word in the request to its parent entity
before applying a steer, matching case-insensitively and tolerating the
punctuation people actually type. Nobody says the internal code; they say the
name they see.

A word naming a whole SEGMENT steers to our entry in it, but its measure
includes others. SD-WGT-07. Rank on our OWN measure, use the segment measure
only to SIZE the opportunity, and say which was which.

The mandatory multiplier. SD-WGT-04. MANDATORY_MULTIPLIER is applied ONCE, on
the FINISHED score, never also inside a term. Applying it in both places SQUARES
it. It is listed alongside the entity weights for comparison only and is not one
of them. Because every mandatory unit receives the same multiplier it does not
reorder its own section either; it is applied so the score a reader sees matches
the published formula.

**WHICH COLUMN CARRIES THE ROW'S ENTITY: `concept_creditable_entity`, RESOLVED
THROUGH REFERENCE 3 LIKE EVERY OTHER COLUMN, AND THIS FILE INVENTS NOTHING
HERE.** `entity_weight` is a multiplicative factor of the alignment term on every
row of every ranked section, and until reference/field-resolution.md carried a concept for
it there was no stated way to find the column it reads: the taxonomy held the
entities and their weights, and nothing said which column of the source said which
entity a row belonged to. A live run matched the bound entity names against the
distinct values of every candidate column, found the one that carried them all,
used it, and recorded that it had invented the procedure. That was the right
answer and the wrong way to reach it, because on a file carrying two overlapping
category columns the same run had no rule to choose between them, on a factor that
multiplies every score in the workbook.

The concept, its seed stems, its forbidden neighbours, its VALUE TEST, its
coverage fallback bounded by `ENTITY_COLUMN_MIN_COVERAGE`, the margin the winner
must beat the runner-up by, and the treatment of a tie are stated once in
reference/field-resolution.md 6.3. **This file cites them and restates none of them.** Four
consequences are this skill's own:

- **THE VALUE TEST OUTRANKS THE NAME, AND NO COLUMN IS TAKEN ON A NAME MATCH
  ALONE.** A header cannot separate the entity column from an ordinary type or
  segment column, and 6.3 says so; the run measures what share of the keys and
  aliases of CREDITABLE_ENTITIES the column's own distinct values cover before it
  uses the column for anything.
- **WHERE THE CONCEPT DOES NOT RESOLVE, `entity_weight` IS THE STATED NEUTRAL OF
  1.0 ON EVERY ROW.** Not zero, which would delete the term and with it the close
  weight, the source boost and every other factor in the same product; and not
  `ENTITY_WEIGHT_FLOOR`, which would rank every unit as though it carried the least
  valued entity the organization has. The alignment term reduces to its other
  factors and no unit is ranked up or down by an entity nobody could identify.
  **This is the one place in PART 12 where a missing input takes the identity
  multiplier rather than the floor**, and it is stated here so nobody reads
  SD-WGT-02's floor discipline as reaching it: SD-WGT-02 floors the weight of an
  item whose ENTITY IS UNRESOLVED against a taxonomy that was read, and this is the
  case where the taxonomy could not be read against anything at all.
- **THE CHOSEN COLUMN AND ITS COVERAGE ARE PRINTED**, with the runner-up and its
  coverage, in the Method section beside the other resolution evidence, and the
  front panel carries the absence in one line where nothing resolved. A
  multiplicative factor whose source column is not named is a number the reader
  cannot check.
- **HDR_ENTITY_FOCUS DISPLAYS THAT COLUMN'S VALUE AND IS NOT A SECOND
  RESOLUTION.** The column the concept resolved is the column the entity focus
  cell reads, so the reader can see on the row which entity the weight was taken
  for. Where the concept did not resolve the cell is written blank with its header
  present, per SD-CTR-13, and the neutral is disclosed rather than the cell being
  filled with a guess.

### 12.8.1 An organization that publishes an ORDER and no weights

**A PUBLISHED ORDER OVER THE ENTITIES IS THE COMMONEST FORM THE ANSWER TAKES, AND
IT IS NOT WEIGHTS.** SD-PRI-31 says priority ranking comes from the organization's
own published weights and that where a weighted metric set is published, that
ordering IS the priority ranking. What a real organization publishes far more
often is a SENTENCE: the things it wants grown, listed in the order it wants them
grown, signed and dated, for this period. That is an ORDER over creditable
entities. It is not a set of numbers, and inventing numbers for it is fabrication
under SD-CNF-07.

**THE FAILURE THIS CLOSES.** On a real run the organization published an order
over eight entities in its priority document for the period. Nothing converted an
order to weights, so every entity carried the single implicit weight of the
CREDITABLE_ENTITIES documented default, the organization's clearest published
statement of what it wanted grown moved nothing on any row, and the order was
recorded in the Method section and marked unused. The document was read, was
understood, and was inert.

**THE DERIVATION LIVES IN THE SCHEMA AND THIS FILE DOES NOT RESTATE IT.** The
SECTION A1 row for `CREDITABLE_ENTITIES.standing_weight` carries the rank-to-weight
LINEAR RAMP, its four mandatory conditions, its confidence, its read-back and its
treatment of an entity the published order does not name. It is stated there
rather than here for the reason every shared standard is: three skills read the
same taxonomy off one configuration, and a ramp written into one of them would
have produced three weight matrices from one published order. Read it there, apply
it exactly as it is written, and print what it requires printed.

**AND IT NOW RUNS ON THE DOCUMENTED DEFAULTS, WHICH IS THE CHANGE THAT MATTERS.**
`ENTITY_WEIGHT_FLOOR`'s default is shape dependent on the entity count, and where
two or more entities are in play it is strictly below the ceiling, with the
validation requiring exactly that wherever the floor is bound. So the ramp
actually ramps on an unbound configuration, and the degenerate case is closed at
its source rather than guarded against here. **The failure that guard existed for
was real and is worth keeping on the page:** an earlier default put the floor
equal to the ceiling, every derived weight came out at the top, and an
organization's published ordering of eight entities moved nothing on the artifact
while the method reported that the derivation had been applied. A flat ramp is
worse than no ramp, because it looks like it ran.

**WHAT IS THIS SKILL'S OWN, AND IT IS ONLY THIS:**

- **WHICH DIRECTIONS COUNT AS A PUBLISHED ORDER HERE.** An order admitted by this
  skill is one carried by a direction that PART 8 admitted for the period being
  planned, on any rung of the priority source ladder, and that survived the
  compliance gate of PART 9. A direction the gate held back publishes no order,
  for the same reason it supplies no action: 9.2 fails closed on the priorities and
  harvesting a weight out of a held-back direction would put it back into the score
  through a side door.
- **WHERE THE DERIVED WEIGHT ENTERS.** Exactly where a bound one would, as
  `entity_weight` in the alignment product of 12.1, one factor, once. SD-WGT-05
  still holds: entity weight scales the alignment term only and never reorders the
  list by itself, so a high-measure unit in a lower-ranked entity can and should
  outrank a small unit in the top one.
- **THAT A BOUND WEIGHT IS NEVER OVERWRITTEN.** SD-CTR-24 and G6: a value the
  organization bound outranks a value derived this run, always. Where the taxonomy
  already carries weights the derivation does not run, and where it carries weights
  for SOME entities it does not run for any of them, because a ramp mixed with
  bound values is neither the organization's ordering nor its weights.
- **THAT UNMAPPED STILL MEANS UNMAPPED.** SD-WGT-01's no-default-row rule is
  untouched end to end: an entity outside the taxonomy takes no weight from this
  section and no position in the ramp, and an entity the published order does not
  name is unmapped rather than quietly given the floor, which would rank it against
  entities the organization actually ordered.
- **THAT IT IS A RUN-LOCAL DERIVATION.** The weights are MEDIUM confidence,
  exactly as 3.2 defines DERIVED, and a RUN never writes them to the organization's
  configuration. SD-CNF-01 is untouched. Only an interview that reads the derived
  values back and gets a yes may do that.
- **THAT THE READ-BACK IS RAISED HERE.** The request goes to PART 22 decision 10,
  once, recorded with the other open requests, so an organization can replace the
  whole ramp with its own weights in one line.

## 12.9 The de-duplication of effort

**The coverage-duplication down-weight applies to the DIRECT-ACTION LINE ONLY.**
SD-DUP-01. COVERAGE_DUPLICATION_APPLIES_TO must be the junior line. Check which
line is being built BEFORE discounting anything.

The reason: a manager DEPLOYS the second party. Those units are covered because
that manager scheduled them to be covered, so showing them discounted
misrepresents the manager's own resource deployment back to them. The general
form: a de-duplication discount is meaningful to the person choosing where to
spend a day and MISLEADING to the person who assigned the other resource. Worked
examples, neutral and invented: an account already worked this period by a
specialist or a partner should be discounted on the individual owner's list and
shown at FULL weight on the leader's; a person already enrolled in a managed
programme should be discounted on the practitioner's outreach list and not on
the programme director's.

On the senior line the assignment is still IDENTIFIED and REPORTED, just not
weighted. SD-DUP-03. Name the list, its sender and date, and note the affected
units on their rows, because that is their own deployment showing up in their
own report. What they must not see is those units pushed down the ranking for it.

Derive the other actor's unit set from the CODE; do not pattern-match the
characters. SD-DUP-04. SECOND_ACTOR_RESOLUTION_LADDER, in order:

1. A DERIVABLE identifier, where SCOPE_CODE_SCHEME supports one, constructed by
   SECOND_ACTOR_UNIT_SUFFIX from the user's own coarser code, and tested by
   EQUALITY against that ONE derived code. Not a suffix search across the file: a
   unit ending in the same characters under a DIFFERENT parent is a different
   parent's specialist and is irrelevant.
2. An explicit ASSIGNMENT LIST from the priority sweep.
3. A PER-UNIT FLAG naming the other actor.

An absent second actor is a NORMAL result, not a failure. SD-DUP-05. When the
derived code matches zero rows, say exactly that, fall to the next source, and
if none resolve apply NO discount and record that none was identified. Never
invent the set, never assume the pattern holds, never treat the absence as a
reason to stop.

**Discount only when the unit's ONLY open work is the other actor's.**
SD-DUP-06. A unit carrying the other actor's work ALONGSIDE its own actionable
work is NOT down-weighted, because the person has their own reason to be there.
Check the unit's own open work before applying the discount; never discount on
list membership alone.

Scale rather than exclude, so a big opportunity still surfaces. SD-DUP-07. The
unit stays on the list and stays visible, because a genuinely big opportunity
should still surface THROUGH the discount: that is the point of scaling rather
than excluding. State on the row WHY it ranks low so the person can override on
their own judgment.

## 12.10 The gap terms

**Every gap term has a NAMED SOURCE so two implementers score the same units.**
SD-SCO-09. GAP_TERM_DEFINITIONS is a CLOSED set of flat terms, each at
GAP_TERM_WEIGHT, each with an explicit source concept and test, plus at most one
GRADUATED_BUCKET, summing to GAP_TERM_CAP.

The flat set is COMPLETE: there is no additional term. Do not cap below the
reachable maximum, and do not add a term without raising the cap to match. A cap
set under the reachable maximum silently CLIPS THE HIGHEST-SIGNAL UNITS, which
are the units this method exists to surface.

The standing four flat terms, generalized: coverage absent; presence absent;
benchmark shortfall; commitment missing. The graduated bucket, where bound,
bands on two axes with its largest weight not greater than GAP_TERM_WEIGHT.

A shared source column does NOT mean a shared test. SD-SCO-10. Two terms may
read the same column and still have different tests, and any double count is
BOUNDED and must be COMPUTED from both columns, never assumed. In one real file
the two tests disagreed on 133 of 354 units, so reading the identifier alone
would grant the second term to all 354 and over-count 133 of them. ONE intended
double count may be declared explicitly; no other term may be double-counted.

A term whose source does not resolve is NOT scored and NEVER becomes a default.
SD-SCO-11. It is NAMED as not evaluated.

**AND BEFORE A TERM IS DECLARED UNRESOLVED, THE INPUT SET IS CHECKED FOR A FILE
THAT CARRIES IT.** SD-PRS-48 and 10.1.1. A gap term whose source concept does not
resolve in the ranking source but DOES resolve in a second file sharing the unit
identifier is scored on the enriched column, because the alternative is computing
the term as nothing while the evidence sits in the same input set, which is what
happened on a real run to four of the four flat terms at once. **Where the join
was performed**, the term is scored, and every figure it produces is disclosed as
arriving by join with the match rate beside it.

**AND WHERE THE CONCEPT RESOLVED THROUGH A SIBLING SET, THE TERM IS EVALUATED ONCE
PER MEMBER AND NAMES ITS MEMBER.** reference/field-resolution.md 7.4b and 10.1.1. A real
evidence file carries one column per member of a published requirement set, so the
concept resolves PER MEMBER rather than as one column: the term reads the member's
own column, is evaluated once for each member, and **carries the member's name
beside every figure it produces, wherever that figure is printed**. **NO ROLLUP IS
INVENTED to give the term one answer per unit.** Where the term needs one and the
admitted source states no aggregation, the per-unit answer stays UNRESOLVED and is
reported as not attempted under the rule above, while the per-member answers still
ship; where the source itself states the aggregation, the term takes it and prints
the rule and the source's own words for it. **This changes what a standing term can
READ and never how many terms there are:** the flat set stays complete, GAP_TERM_CAP
is not raised, and a sibling set never adds a term. **Where the join was REFUSED**, the
term takes this rule unchanged: not scored, never defaulted, NAMED as not
evaluated, with the additional line naming the file and the condition that refused
the join. A row that matched no record on the enriching side is in the same state:
the term is not scored FOR THAT ROW and says so, because an absent record is not
evidence of a negative and a blank is not a zero.

## 12.11 The workload term

Cap the COUNT first, then multiply; never cap the product. SD-SCO-12. The term
contributes min(count, WORKLOAD_COUNT_CAP) times WORKLOAD_MULTIPLIER. This is
what stops a unit climbing on volume of work alone.

**Alignment and workload are different populations ON PURPOSE, and neither is a
subset of the other.** SD-SCO-13. The workload count counts EVERY item closing
this period, whatever its type and whether or not it matched a stated priority.
The alignment term counts ONLY the ones that matched, and scales each by work
type.

> Alignment asks how much of what leadership asked for is open here. Workload
> asks how much work is open here at all.

A unit carrying four items that close this period is a busy unit even if nobody
named them, and the person still has to do them. An item dated by rule 2 with no
priority match contributes to workload and nothing to alignment: that is
correct, not a leak.

## 12.12 Applying the measure exactly once

Apply the measure exactly ONCE per output. SD-WGT-19. Score a cost-gated term
FLAT and let the measure enter once through that section's own multiplier. Never
scale a term by the percentile separately; doing so applies the measure twice and
buries the very units the section publishes. Double-counting the same factor in
two places is named three separate times in the corpus. It is a defect class,
not an occasional slip.

The measure weighting is universal and any new signal inherits it. SD-WGT-18. It
applies to every opportunity the method surfaces, on every section, without
exception, with a stated form per output.

A membership gate belongs only where membership is BY FLAG. SD-WGT-20. An "only
flag is X" test is meaningful on an exception list and UNDEFINED on a ranked
list, where a unit appears because of its measure, alignment and workload rather
than because of a flag. One weight everywhere; one membership gate, on one
section.

## 12.13 The deterministic tie-break

SD-SCO-16. TIE_BREAK_KEYS, in order and mandatory:

1. score DESCENDING
2. the MEASURE descending, where "the measure" means WHICHEVER COLUMN SUPPLIED
   THE PERCENTILE FOR THIS RUN. One key, defined by the run's own basis, so the
   tie-break never silently switches measures.
3. the unit IDENTIFIER ascending.

Without a total order a rerun on the same file can return a different list,
which breaks the repeatability guarantee. Ties are real rather than
hypothetical: several units share the exact measure value at a section cut line
in real data. SD-RUN-15: a run that cannot be reproduced cannot be trusted, and
if a rerun on identical inputs differs, find the non-determinism BEFORE the
report is used.

## 12.14 Compute every figure with a tool

SD-RUN-14. Every arithmetic result in an artifact is computed by code, never
mentally. Where CODE_EXECUTION is absent, no ranked list is produced at all, per
reference/capability-probe.md P2.

---

# PART 13: STAGE 9, THE STEER

## 13.1 Four modes, and a lean is not a restriction

SD-STR-01. Four modes: LEAN, RESTRICT, INITIATIVE, NONE. Decided from the
GRAMMAR of the request and NAMED in the output so the reader can tell at a glance
which list they are holding. A possessive or "for" construction naming the
entity is a RESTRICTION; an explicit lean phrase is a LEAN.

Filler words are stripped BEFORE reading the mode. SD-STR-09. Strip the filler
nouns first, then decide on the grammar that remains. Do not let a filler noun
trigger the ambiguity rule.

**When genuinely ambiguous, prefer the RECOVERABLE reading and say so in one
line.** SD-STR-10. Prefer the LEAN. A lean still surfaces the entity's best
units near the top, so an over-broad list is recoverable by the reader; a
restriction that should have been a lean silently hides opportunity they will
never know existed. Do not stop to ask: deliver the lean and note the reading.
The general form: when in doubt, choose the error the reader can DETECT and
CORRECT.

## 13.2 The lean transform

SD-STR-02. Set the named entity's weight to STEER_TILT_TARGET_WEIGHT and
multiply EVERY OTHER entity's weight by STEER_TILT_OTHERS_FACTOR. Print the
resulting weight matrix IN FULL, so nobody has to derive it and so the
consequence is visible.

STEER_TILT_TARGET_WEIGHT must sit STRICTLY ABOVE the maximum standing weight in
CREDITABLE_ENTITIES. SD-STR-03. If the named entity already sits at the standing
top and is left there, the lean changes nothing at all and returns the unsteered
list under a steered label. That is a no-op labelled as an action.

A lean toward a low-ranked entity DELIBERATELY INVERTS the standing hierarchy,
and that is correct. SD-STR-04. The standing hierarchy is the default ordering
when nobody has said otherwise; a user naming an entity HAS said otherwise, and
the lean is how the method honours it. Print the row of the table that was used
so a reader who expects the default to lead can see why it did not.

Verify a lean did not silently become a restriction. SD-STR-05. If EVERY unit in
the result carries the named entity, you ran the wrong mode. A large unit with
strong opportunity in another entity must still surface; that is the entire
point of a lean.

## 13.3 The restriction

SD-STR-06. A restriction changes the POPULATION and the MEASURE BASIS, and is
applied in the SCOPE stage, exactly as a qualifier is, before every exclusion and
before the percentile, because the median and the percentile must be computed
over the set the report is actually about. Applied later, a unit with strong
standing in the named entity but modest total measure would be cut before its
standing was ever considered, which is precisely backwards for a request asking
for the biggest units in that entity. The other three modes do not restrict the
population and stay where they are.

Never refuse an entity request because one column is absent. SD-STR-07. Fall back
in order: another measure for that entity, then membership by flags alone ranked
on the scope measure. Name the basis used and say plainly when membership came
from work flags rather than from that entity's own measure.

Zero survivors switches to the LEAN, and the measure basis reverts WITH it.
SD-STR-08. Flip both together and NAME the reverted column. If the mode flips
and the basis does not, the ranking runs on a column that just proved to be
empty across the population, every percentile collapses toward zero, and the
list is meaningless. Fewer survivors than the list size is FINE: deliver every
one and say how many cleared. Zero survivors is not.

> An empty artifact is never an acceptable answer to a reasonable question.

## 13.4 The initiative steer

A named initiative is a STEER and is NOT an entity. SD-WGT-08. Match against
resolved column names and published initiative titles, on the DISTINCTIVE words
rather than the whole title, and treat a match as a lean toward the units
carrying it. If it matches nothing, say so in one line and run without it. NEVER
stop.

INITIATIVE_STEER_TERM is the ONLY additive steer in the formula. SD-STR-12. An
ENTITY-level steer never enters as an additive term: a lean acts by changing the
entity weight INSIDE the alignment term, and a restriction acts by changing the
population and the measure basis. A named initiative is a MEMBERSHIP FACT about
the unit rather than a re-weighting of a whole entity. Adding an entity steer as
a separate additive term as well would apply the same preference TWICE.

## 13.5 A steer never overrides leadership

SD-STR-11. Every mode still honours supervisor and central priorities and never
releases a mandatory unit.

---

# PART 14: COMPARISON MODE

## 14.1 Only when asked, and two branches when they do ask

**Never infer change from one snapshot, and say nothing about trend unless
asked.** SD-CMP-01. If the user did not ask, rank the single input and deliver.
Do not mention trend, do not ask for a second file, do not caveat the absence of
one. Never substitute gap indicators for measured change.

If they DID ask, and only one input exists, the run takes ONE OF TWO BRANCHES.
The branch is decided by the population, from the data, before the one-input stop
is allowed to fire. SD-CMP-08.

**The warm branch. The stop survives, unchanged.** Where the population is WARM,
meaning more than COLD_START_MIN_PRIOR_SHARE of in-scope units carry a prior
period, a comparison request with one input is a HARD GATE: stop and ask for the
second file. This is a correct gate against a user who forgot an attachment and
it is not weakened. It is the `comparison_single_input` gate in 20.1.

**The cold branch. The stop is replaced by an answer.** Where the population is
COLD, per the detection in 14.8 and SD-CLM-28, a second file does not exist and
never will, and asking for it is a dead end at exactly the altitude that most
needs an answer. Do NOT stop. Do the following, in this order:

1. SAY that no prior period exists for this population, and NAME THE EVIDENCE:
   which cold-start test fired, the figure that fired it, and the earliest entry
   date found in the population.
2. OFFER THE SECOND NUMBERS THAT DO EXIST, per SD-CLM-32 and SD-CLM-29:
   attainment against a plan set before the period by somebody other than the
   writer, and the bare denominator population. Name which is in force.
3. EMIT the current state, ranked by the terms that ARE computable, and the
   ABSOLUTE BUILD to date: what exists now that did not exist at the start of the
   period, as a count with its unit and its period.
4. Emit NO win, miss or flat label anywhere in that population, per SD-CLM-31.
   The state emitted instead is NO BASELINE, which is a real, printed, distinct
   state. Plan attainment keeps its own three states and is exempt.
5. The deliverable SHAPE does not change. Same sections, same sizes, same caps.
   SD-CMP-05.

Do not over-correct into refusing to answer. A cold population is a normal thing
for a business to have, and the method's job is to say true things about it.
SD-CLM-27.

## 14.2 Make two inputs apples to apples first

SD-CMP-02. Map each file's columns INDEPENDENTLY. Filter both to the same scope
using EACH FILE'S OWN column. Confirm the metric matches on CONCEPT and on TIME
BASIS. Join on the identifier. Note units present in one file only rather than
dropping them silently. A mismatched basis is not a comparison: report it and
compare only on metrics that align.

**Rate, unit and lookback are three separate properties, and conflating them is
fatal.** SD-PRS-39:

| Property | Meaning | Rule |
|---|---|---|
| RATE DENOMINATOR | the time base the value is expressed per | MUST match, with NO override. RATE_DENOMINATOR_MUST_MATCH is true. |
| UNIT | what is being counted | MUST match, or a validated and recorded normalization must have been applied |
| LOOKBACK LENGTH | how much history the average covers | MAY differ. When the first two hold, a differing lookback is a RUN-RATE COMPARISON: permitted, recorded, and never used to open a report. LOOKBACK_MAY_DIFFER is true. |

Both a year-to-date weekly average and a thirteen-week weekly average express
the same quantity: units per week. The lookback changes how much history is
smoothed, not what the number measures. Blocking on lookback alone would reject
almost every real pair of files. Conflating the three either blocks every
legitimate comparison or permits a catastrophic one, and the catastrophic one is
a number wrong by an order of magnitude while tracing perfectly to real cells.

On a block, compute NOTHING for that pair until it resolves. SD-PRS-40. Mark the
pair unpaired, fire the relevant question, and do not substitute a nearby column.

### 14.2.1 THE EXIT TEST, run BEFORE anything is computed on the pair. SD-CMP-09.

**Under FIXED, like-for-like is NOT established by roster overlap alone.** Overlap
tests the ENTRY side: whether the units in the prior file are still here. It
cannot see the units that LEFT, because they are absent from both sides of the
test. Run the exit test first, as a separate named test with a named result.

**THE PATHOLOGY, and it is the one input that scores perfectly while being
unusable.** A prior-period file containing ONLY the units that survived into the
current period yields full overlap, zero churn out, and passes JOIN_OVERLAP_FLOOR
at its maximum. The test that exists to decide whether two files describe the same
population CERTIFIES it as ideally comparable. Every retention figure computed on
it is 100 percent by construction and every same-unit growth figure is biased
upward by exactly the units that left, and both are arithmetically true.

**THE TEST: count the units present in the PRIOR file and ABSENT from the current
one. That count is the number of exits the pair can see.** Where it is ZERO, the
run is in one of exactly two states, and they are NOT the same state:

1. A SURVIVOR-ONLY EXTRACT: the prior file is the current roster valued at an
   earlier date, not the roster as it stood at that date.
2. A POPULATION THAT GENUINELY LOST NOTHING: real, and rare above a small
   population.

**The run DECIDES between them, says WHICH it believes and WHY, and does so
BEFORE it computes anything on the pair.** The evidence that separates them:
the population size, since zero attrition over a large population is
extraordinary and over a handful is unremarkable; whether the prior file's row
count equals the current count minus the units created since; whether any
independent source disagrees with the prior file's counts; and whether the prior
file's own period stamp precedes the units it contains.

**WHAT MAY BE CLAIMED FROM A SURVIVOR-ONLY PAIR, AND IT IS A CAP RATHER THAN A
REFUSAL:**

| Quantity | Treatment |
|---|---|
| RETENTION and CHURN | NOT COMPUTABLE. Not zero, and not 100 percent. The file cannot answer the question, and the artifact says so where the figure would have gone. |
| SAME-UNIT GROWTH | Computable, SURVIVOR-BIASED, and never published as a bare figure. It ships only BESIDE the total movement across the whole population, with the gap between them named for what it is: the part of the change that left. |
| TOTAL MOVEMENT across the whole current population | Computable and unaffected, because it never depended on the join. |
| Any RANKING of units by survivor growth | NOT PUBLISHED. The bias is not uniform across units, so the ordering is not recoverable. |

A GENUINE no-attrition population is stated as such WITH ITS EVIDENCE, and its
retention figure IS published, at 100 percent, with the population size beside it
so a reader can weigh it.

**This is a NAMED test with a NAMED result, not a reconciliation habit.** In the
case that produced the rule the catch happened only because two sources disagreed
on a count and a general rule against publishing a value whose derivations
disagree fired; had the counts agreed, nothing would have caught it. A trap caught
by luck is not caught, so the exit test runs on every FIXED pair, its count is
printed, and its verdict is printed with the evidence that decided it, including
when exits are plentiful and the verdict is unremarkable.

**Under FLOW the exit test is not this test.** A pipeline replaces most of its
rows every period by design, so units absent from the current file are the normal
case rather than a signal; the like-for-like question there is the cohort basis of
PART 23 divergence 1, and the exit-side question is answered by the exit dates the
FLOW path already reads. The FIXED test above is never applied to a FLOW
population and never used to disqualify one.

## 14.3 Unit drift between two files

Orient BEFORE you test. SD-PRS-34. Compute the ratio per matched unit, orient it
so the median is at or above one, and only THEN test concentration. Without
orientation the result depends on which file was divided by which.

Three co-required conditions before a factor may be declared: at least
UNIT_DRIFT_MIN_PAIRS positive pairs; the oriented median within
UNIT_DRIFT_TOLERANCE of a candidate factor in UNIT_DRIFT_CANDIDATE_FACTORS; and
at least UNIT_DRIFT_CONCENTRATION of oriented ratios within UNIT_DRIFT_BAND of
that factor.

Concentration near the factor is the test, NOT tightness. SD-PRS-35. Do not test
dispersion with a tight interquartile band: unit-level business metrics are
naturally dispersed. On real data a genuine conversion showed an interquartile
range of eighteen to twenty-four percent of the median while being an
unambiguous factor of ten. A five percent dispersion ceiling is unsatisfiable by
construction for any unit-level metric and would miss every real unit change.

Restrict the drift test to columns already typed as MEASURES. SD-PRS-36. Run it
only on pairs both classified as rate or volume. Running it across all numeric
columns produces false positives on identity columns.

A header token mismatch is EVIDENCE, not an automatic block. SD-PRS-38. A header
mismatch says a conversion is likely; the TEST says what it is. A letter inside
a rate marker is often a category hint, not a unit conversion, and treating it
as one blocks most real pairs and produces no output at all.

**A small factor might be a real result; never correct it silently.**
SD-PRS-37. Auto-normalize ONLY the factors in UNIT_DRIFT_AUTONORM_FACTORS, which
deliberately excludes the small ones. For a small validated factor, do not
normalize automatically: ASK. A genuine doubling produces a magnitude near two,
and silently correcting it would erase the user's best result of the year and
never tell them.

## 14.4 Joining two files

A valid join key is near-unique in BOTH files and produces a one-to-one match.
SD-PRS-31. Require uniqueness at or above JOIN_UNIQUENESS_FLOOR in EACH file and
reject many-to-many candidates. Name the column chosen and its uniqueness in each
file in the audit. Prefer a column whose name or profile suggests a
UNIT identifier over a geographic or personnel code, because those overlap
heavily and are not unit keys. Normalize before joining: trim whitespace, strip
leading zeros, casefold, remove non-alphanumeric separators. A code stored as
text with a leading zero must still match its integer twin.

The overlap floor is a HARD STOP **under FIXED only**. SD-PRS-32.
JOIN_OVERLAP_FLOOR is CONDITIONAL on the population's mode being FIXED. Under
FIXED, matched rows must be at least JOIN_OVERLAP_FLOOR of the row count of the
SMALLER file; below that, stop and report both rosters. **Passing this floor is
not evidence that the two files describe the same population**: it tests the entry
side only, and 14.2.1's exit test runs separately and before anything is computed
on the pair, per SD-CMP-09. **Under FLOW it is never
applied and is never a gate**, per PART 23 divergence 1: a healthy pipeline
replaces most of its rows every period, so any reasonable floor declares every
real comparison invalid, and the resulting stop is correct-looking and reads as a
data problem rather than as a method that does not handle pipelines. Set the
floor low even under FIXED, because a real roster churns. Without this floor, a near-empty intersection produces metrics that
both verifiers derive identically from the same empty set, agree on perfectly,
and promote to CONFIRMED: a fabricated rank would ship carrying two-method
validation.

With three or more files, chain PAIRWISE against ONE anchor and report what was
used. SD-PRS-33. The period-end file is the anchor. Report which files were used
and which were not. Never silently discard a file the user supplied.

## 14.5 Scoring a comparison

A zero baseline is a NEW-ENTRY case, not an infinity. SD-CMP-03. When the
baseline is zero and the current is non-zero, list the unit as a new case and
leave the change BLANK rather than infinite.

The comparison score carries the FULL BRACKET, not just the measure weighting.
SD-CMP-04. Multiply the change term by the SAME bracket the normal score uses,
computed over the CURRENT period. A unit that declined AND carries open directed
work outranks one that merely declined, which is the intent.

**A comparison changes the ranking BASIS, never the deliverable SHAPE.**
SD-CMP-05. Same sections, same sizes, same caps. Nothing about a comparison
suspends the other rules.

## 14.6 The peer set and the second number

**A peer set is drawn from SIBLINGS, never from SUBORDINATES.** SD-SPN-14. This
is the rule the schema's own argument for binding the hierarchy at ignition
depends on, and it is enforced here in two mechanical tests, both of which must
pass before a peer set may be used at all:

1. THE DIRECTION TEST. Resolve the peer level from ROLE_LADDER.peer_level, or
   from PEER_SET_LEVEL_DEFAULT where the role names none. Then TEST IT: the
   resolved level must be STRICTLY COARSER than the requester's own resolved
   level. A resolved level AT or FINER than the requester's own is WRONG, and it
   is DISCARDED, never used. Walking outward is the only permitted direction.
2. THE INTERSECTION TEST. No member of the resolved peer set may sit INSIDE the
   requester's own scope. A peer set that intersects the requester's own span is
   not a peer set.

Worked case, neutral: a top-of-house executive owns nine facilities. The only
level the default names is the facility, so an untested resolution groups by
facility and ranks her among her OWN nine facilities. Every number is internally
consistent, the comparison is meaningless, and it reads to the leader as an
accusation.

**A role at the top of the chain has NO INTERNAL PEER SET, and that is a stated
result, not a failure.** SD-SPN-15. Where the requester's own level is the
coarsest in SCOPE_LEVELS there is no coarser level, therefore no sibling set.
SAY SO PLAINLY. Do not manufacture one. Then, in order:

1. If PEER_SET_IS_EXTERNAL is true, use the published comparison group named by
   EXTERNAL_PEER_SET_SOURCE. NAME the publication AND its refresh cadence, and
   STATE HOW STALE the release is relative to this run. A group refreshed
   annually and read quarterly is stale for three quarters of the year. An
   external group is a legitimate answer to "the spread across peers doing the
   same job" and is the most likely real answer at any regulated or benchmarked
   business; it is bound as a publication and a cadence and is NEVER forced into
   the organization's own containment chain, which holds only units the
   organization owns.
2. Otherwise DROP the peer rung for that run, fall to the HIGHEST REMAINING BOUND
   rung, and NAME THE DROP beside every affected figure, per SD-CTR-24. Never
   past the highest remaining bound rung to the floor.
3. Where no rung remains but the floor, the figures ship with a denominator
   population and no achievement wording, which is a legitimate gate-passing
   state, not a failure.

**A peer set below the minimum rankable population is not a peer set.**
SD-POP-25 and SD-POP-19 both apply here: below MIN_POPULATION_FOR_RANKING no peer
language is emitted at all, and below MIN_POPULATION_FOR_NORM a peer median is
printed with its count beside it and no comparison is drawn from it. Where
SD-POP-26 finds the unit of business COARSER than the reader's own scope, there
is no peer set to compute because there is no set of units at that reader's
level; say so and take 11.7.2.

**A PEER SET THAT IS NON-EMPTY AND BELOW THE ANONYMITY FLOOR IS A THIRD STATE
WITH ITS OWN RUNG, AND IT IS NOT THE SAME AS NO PEER SET.** SD-SPN-16, in force
here in full and not restated. SD-SPN-15 above answers a peer set of ZERO. Where
the resolved peer level yields a set that EXISTS and is smaller than
ANONYMITY_FLOOR, the run WALKS OUTWARD one level at a time until the set reaches
the floor or the chain is exhausted, stops at the FIRST level that meets it, and
keeps both tests above in force at every step: the level stays strictly coarser
than the reader's own, and no member may sit inside the reader's scope. Where the
chain is exhausted, take SD-SPN-15's mechanism from its step 1. The floor is never
lowered to fit the set, a set below the floor is never published in any form a
reader can invert, and a comparison drawn at a superseded level is published as
what it is, with the level used and the count it yielded printed beside every
figure that reads it and the derived level named as superseded. The three states
are told apart in three different sentences, per SD-SPN-16's own table, and the
suppressed comparison is NAMED rather than omitted: a reader who is told nothing
assumes the comparison was attempted and came back unremarkable, which is the one
reading that is false in all three.

ANONYMITY_FLOOR still applies on top of all of this: below it, GENERALIZE rather
than rank, because a positional statement in a small peer set names someone by
elimination. SD-CLM-12.

Once a peer set survives both tests, PEER_SET_ANCHOR_PERIOD defines it, which for
a two-period comparison is normally the period-end file. SD-CMP-06. Group by the
resolved peer level, compute every metric for every peer, rank the user's unit,
and COUNT how many peers share the same value. Every comparison runs on the
same-unit intersection used for the user's own metrics. Rosters change between
periods, and ranking against a roster that includes peers absent from one file
produces a rank that cannot be reproduced. State the peer count and the unit
basis alongside every rank.

Under FLOW the peer set is sibling CONTAINERS at the resolved peer level, with
the cohort basis stated alongside, per PART 23. The direction and intersection
tests are unchanged.

A two-pass split must NOT change the denominator, and two passes is not
sampling. SD-CMP-07. The first pass retains the full sorted distribution or an
exact rank index and carries it into the second pass as part of the checkpoint;
the second pass LOOKS PERCENTILES UP rather than recomputing them. Both passes
read every row. If the second pass ranked the survivors among themselves, every
percentile would shift upward and a large-tier run would rank the same units
differently from a small-tier run on the same data. A unit's percentile must be
identical whichever tier processed it. Verify directly by re-reading a sample.

## 14.7 The label, and the ground that moved

**Every number carries a second number the writer did not choose.** G4,
SD-CLM-04. The counterfactual ladder, best first, is fixed and is not
configurable; what is configurable is which rungs the business HAS
(COUNTERFACTUAL_AVAILABLE_RUNGS), which rung each metric uses
(COUNTERFACTUAL_BY_METRIC), and how strongly each rung lets a claim be worded
(CLAIM_STRENGTH_BY_RUNG):

| Rung | Name | What it is |
|---|---|---|
| 1 | SHARE_OF_ADDRESSABLE | share of a bounded addressable population |
| 2 | MATCHED_CONTROL | an untouched, unassigned or later-treated segment inside the same business |
| 3 | PEER_DISTRIBUTION | the distribution of sibling units at the peer level |
| 4 | PLAN_ATTAINMENT | percent of a target set before the period by someone other than the writer |
| 5 | OWN_PRIOR_RUN_RATE | the writer's own prior-period run rate, weakest, carry the warning |
| 6 | BARE_DENOMINATOR | a population count that bounds the magnitude. The FLOOR. No number ever ships alone. |

RUNG_DISCLOSURE_REQUIRED should be true: the output NAMES which rung each figure
used.

**Rung availability is scoped, and a rung named but undefined is not available.**
COUNTERFACTUAL_AVAILABLE_RUNGS is the ORGANIZATION-WIDE DEFAULT.
COUNTERFACTUAL_RUNG_SCOPES overrides it for one population or segment, and where
a scoped entry exists it GOVERNS for that population. A rung named as available
whose own definition is unbound is NOT available: it is struck, the striking is
said out loud, and the metric falls to the highest rung whose definition IS
bound. The ten rung-definition variables, one or two per rung, are PART 22 row
65, which fires at COST RANK 2. SD-CLM-29.

**Falling from a rung falls to the next BOUND rung, never past it to the floor.**
SD-CTR-24 and G6. An unbound value that supplies ONE rung removes only THAT
rung. The named case, and it must not recur: ENTITY_BENCHMARK_MAP is deferred and
at a business with no wider population it will never be bound, CORRECTLY. Its
absence removes rungs 1 and 2 ONLY. Every figure then falls to the highest rung
COUNTERFACTUAL_AVAILABLE_RUNGS still supplies, which is NAMED beside it, and the
claim strength drops with it. A figure routes to the bare denominator ONLY when
NO OTHER BOUND RUNG RESOLVES. A weaker rung is never silently substituted for a
stronger one that failed, and an unbound deferred value never overrides a rung
the organization bound at ignition.

**Every business must name what its ground is.** SD-CLM-05. MOVING_GROUND_NAME
is an ignition binding for exactly this reason: a business with no external
market is not a business without a benchmark, it is a business whose benchmark
is internal, and the ground-moved failure arrives there as a RISING BASELINE
rather than as a rising market. A claim may not ship at achievement strength
until the business has named its ground. MOVING_GROUND_SOURCE says where the
movement is read from each period; where it is unread, the named ground is
printed WITHOUT a movement figure and every affected statement drops to
qualified wording.

**The RUNG decides the arithmetic, and a quantity that does not exist is never
approximated.** SD-CLM-33 carries the rung table and it is the MECHANISM of
SD-CLM-07. It governs all three skills in this bundle, so that two skills cannot
produce two different answers off the same configuration and the same data. Read
it there; it is not restated here, and this file adds nothing to it and subtracts
nothing. What it settles, in summary and by citation only:

- Which comparative quantities EXIST at each rung, and which are UNDEFINED and
  therefore never emitted rather than approximated by a neighbour.
- That at plan attainment the quantity is ATTAINMENT, not a rate delta, and the
  flat state is named ON PLAN.
- That at own prior run rate the movement carries the uncontrolled-movement
  warning.
- That UNPAIRED is reached ONLY at the floor rung, where no comparative quantity
  is defined.
- The claim strength permitted at each rung.

**A missing benchmark POPULATION is not UNPAIRED** where a peer set, a control
group or a plan is bound. A peer set, a control group and a plan each supply a
comparative quantity WITHOUT a benchmark population. The floor rung is reached
only where no other bound rung resolves. SD-CLM-33 and SD-CTR-24.

Classify by FORMULA, not by a direction table, using the quantity SD-CLM-33
defines for the rung in force. SD-CLM-07:

**DEADBAND IS A MAPPING PER RUNG, EACH BAND WITH ITS UNIT NAMED, AND A BARE
SCALAR IS REJECTED AT VALIDATION.** SD-CLM-34. The unit of the delta genuinely
differs by rung: percentage points of SHARE at rung 1, percentage points of the
treated-minus-control GAP at rung 2, percentage points of GROWTH at rungs 3 and
5, and PERCENT OF TARGET at rung 4. One scalar described as being in the unit of
that delta names four different quantities depending on which rung read it, and a
band read in the wrong unit either labels noise as a result or silences a real
one. Read the band for the RUNG IN FORCE, and never copy a band between rungs.

**AND THOSE FOUR ARE THE UNITS OF A MOVEMENT. A LEVEL COMPARED AGAINST A LEVEL IS
A FIFTH UNIT AND CARRIES ITS OWN BAND.** SD-CLM-34. Comparing one rate LEVEL with
another, a rate for this scope against a comparator median of the same rate, is the
commonest comparison a service business makes, and its delta is in PERCENTAGE
POINTS OF THE MEASURE'S OWN RATE. It is not share points, not growth points and not
percent of target, so under a four-unit mapping no band existed for it, and with no
band the failsafe below silenced the label and shipped the three figures a reader
most wants labelled with a raw delta and nothing else.

- **The level-delta band is DATA-DERIVED from the comparator set's own spread**,
  the same way the rung-3 band is, and it is subject to every rule that governs a
  comparator set: not emitted where the set is below ANONYMITY_FLOOR, per
  SD-SPN-16 and 14.6, and not emitted where the set was built by the writer, per
  SD-CLM-30 and 14.8.4.
- **A level delta and a movement delta are NEVER banded against each other's band,
  and the two are never emitted as one finding.** A rate that is flat in movement
  and below the comparator level is TWO facts, and the artifact says both.

- Rung 3 is COMPUTED FROM THE DATA, from the spread of period-over-period movement
  across the peers. Where it cannot be computed, NO win or miss label is emitted on
  that rung and the raw delta is printed with its unit, per decision point 41.
- **Rung 4 carries a FIXED band in PERCENT OF TARGET and is therefore ALWAYS
  COMPUTABLE. It never depends on a peer spread.** The target IS the comparison and
  it was set before the period by somebody else, so plan attainment does not need
  to know how anybody else did in order to say that a figure well short of target
  is short. This is what keeps the most senior reader, who has no peers at all,
  from receiving a headline attainment and a worst failure both shipped unlabelled.
  On rung 4 the delta is attainment minus 100 percent of target and the label
  follows directly.
- Rung 6 has NO band, because a bare count carries no delta to band. That is a
  stated absence rather than a missing entry, and it is printed as one.
- The band AND ITS UNIT are printed beside every labelled figure, so a reader can
  see what was treated as noise and in what unit.

- WIN when the delta for the rung in force exceeds plus that rung's band.
- MISS when it falls below minus that rung's band.
- FLAT when its absolute value is at or under that rung's band, and ON PLAN where
  the rung in force is plan attainment.
- UNPAIRED at the floor rung only.
- NO BASELINE where the population is COLD, per SD-CLM-31 and 14.8, which
  overrides the label column at every rung except plan attainment. Plan attainment
  is exempt precisely because its band is fixed in percent of target: a cold
  population with a plan still gets labelled figures.

Benchmark movement is NEVER itself a label. An entity that grew while its
benchmark grew faster is a MISS, regardless of how large the raw growth looks.
That is the environment-credit trap, the most seductive error in this data: it
reads as a triumph and it is a miss.

**Two comparative quantities, and never interchange them.** SD-CLM-06. A RATE
DELTA is entity growth minus benchmark growth, in PERCENTAGE POINTS OF GROWTH. A
PROPORTION DELTA is end share minus start share, in SHARE POINTS, where share is
entity value divided by benchmark value. They are not the same and they have
different units. Confusing them produces overclaims of several multiples.

> EVERY EMITTED FIGURE MUST NAME ITS UNIT. Never write a bare "points".

A reviewer who reads share points as growth points sees a claim several times
larger than the truth. The never-interchange rule and the mandatory unit naming
survive any rebinding verbatim and are the single most valuable pair to preserve
exactly.

A rank never SUBSTITUTES for the counterfactual denominator where an external
environment exists. SD-CLM-16. Where the environment can move underneath
everyone, a peer rank is SUPPLEMENTAL and never a substitute, because a unit can
rank first among peers while lagging its benchmark, which is a MISS. Where there
is no such shared environment, the peer distribution IS the primary control.
Which case applies is a BINDING, not a judgment.

Show the benchmark, never CLAIM it. SD-CLM-14. Every benchmark present in the
data appears in the output, either as the comparison attached to a figure or as
the denominator of a proportion, and NEVER as the subject of an achievement
sentence. The SUBJECT of the sentence decides: if the subject is not something
the reader is accountable for, the sentence does not belong in the body. A
benchmark whose metric is unresolved or unpaired appears only in the
verification list and never in the body, since its number is not trustworthy.
Both placements satisfy the visibility requirement, and nothing is dropped for
being unflattering. SD-CLM-26.

Credit attaches only to what the person is accountable for. SD-CLM-03. No credit
for the movement of the wider population a creditable entity sits in.
NON_CLAIMABLE_ENTITIES is the explicit denylist and its general form is: you may
not claim the movement of any population you did not choose the composition of.

A results list is a set of true, quantified, orphaned facts. SD-CLM-02. A true
number does not say what action produced it, whether it beat anyone, or why the
organization should care, and in a review room nobody supplies that context. The
narrative column exists to stop the numbers being orphans.

Tie handling is mandatory. SD-CLM-11. SUPERLATIVE_REQUIRES_TIE_COUNT is true.
Compute the count of peers at the same value BEFORE writing any superlative.
"Tied best in scope" is honest; "led the scope" is an overclaim when six peers
matched the result. A superlative a reviewer can disprove in one query destroys
the credibility of every other statement in the artifact.

No named third parties, including by indirect identification. SD-CLM-12.
NAMED_THIRD_PARTIES_ALLOWED must be false. Below ANONYMITY_FLOOR peers,
GENERALIZE rather than rank, because in a small peer set a positional statement
names someone by elimination and a compound identifier resolves to one person.

Work performed by a direct report is TEAM credit, never first-person action.
SD-CLM-13. Where the evidence identifies WHO performed the work, tag it, and use
ATTRIBUTION_TEAM_PHRASES. A leader whose record claims personal execution of a
subordinate's work has an integrity problem if it is ever checked against the
logs.

Never infer a target to manufacture a completion percentage. SD-CLM-21. A
measure with no stated target cannot produce a completion percentage: mark it
ungradable and ask. Values above one hundred percent are legitimate and ship as
achieved-over-target, never clipped. COMPLETION_ABOVE_100_ALLOWED is true.

Activity is not claimable. SD-CLM-22. Where the narrative states an outcome, the
enforced shape is verb plus metric plus population plus deadline, and the four
failure patterns are flagged automatically: no metric, no deadline, no
population, and activity rather than outcome. The last is the most common and
most damaging.

An illustrative number in a template is never a value. SD-CLM-24. Every figure,
population and date must trace to the ledger, an answer, or the data. Anything
unsourced is emitted as a bracketed placeholder.

Under-finding is a real failure mode. SD-CLM-17. Where the narrative or the
front panel summarizes, enumerate the cuts the role and the data permit rather
than reporting one total number, and record an impossible cut as UNAVAILABLE
rather than halting. Present findings as a WORKING LIST the person edits, and
DROP MEANS DROP: a dropped item leaves the candidate list entirely and is never
carried into a closing section as consolation. SD-CLM-18.

THE PERMANENT RECORD PRINCIPLE. SD-CLM-01. Anything this skill emits can travel
into a permanent record. Every rule that constrains a statement exists because an
overclaim, a misattributed peer result or an invented figure can damage a career.
When a rule and convenience conflict, THE RULE WINS.

---

## 14.8 THE COLD START

**Governing.** SD-CLM-27. A COLD START is a run in which the POPULATION BEING
SCORED has no prior period of its own. It is a first-class operating condition,
not an arithmetic edge case. Where this section and any other instruction in
this file disagree about a cold population, this section governs, subject only
to PART 1.

A cold population is a NORMAL thing for a business to have: a launch, a new
line, a new market, a new site, an acquisition still on its own systems, a
person who took over a book last period. The method's job is to say TRUE THINGS
about it, not to refuse. **Do not over-correct into refusing to answer.**

### 14.8.1 Two kinds, never conflated

| Kind | What it is | Handling |
|---|---|---|
| A COLD UNIT inside a WARM population | One unit is new; the population around it has history | The existing rules already handle it correctly and NOTHING here changes them: the unit is included at the floor of the measure (SD-POP-13), ranks last by the sort key and is VISIBLE there rather than dropped (SD-POP-12, SD-POP-15), and its period-over-period change is left BLANK rather than infinite (SD-CMP-03). |
| A COLD POPULATION | No unit, or almost no unit, has a prior period | Everything in 14.8.2 through 14.8.6. |

The test that separates them is the share of the in-scope population carrying a
prior period, measured against COLD_START_MIN_PRIOR_SHARE. Above it the
population is WARM and any unit below it is a cold UNIT. At or below it the
POPULATION is cold.

### 14.8.2 A cold start is DETECTED, never declared. SD-CLM-28.

The run detects a cold population FROM THE DATA. It does not wait for the user
to say so, does not ask, and does not rely on a binding. A user living inside a
launch does not think of themselves as an edge case and will not volunteer it,
and an executive answering a binding interview answers for the mature business,
because that is the business they run.

Three tests. ANY ONE marks the population COLD. All three run on EVERY run,
BEFORE scoring, and they run on a provisional run exactly as on a bound one:

1. THE HISTORY TEST, AND IT IS ONLY EVALUABLE WHERE A PRIOR-PERIOD COLUMN
   RESOLVED. The share of in-scope units carrying a usable prior-period value is
   at or below COLD_START_MIN_PRIOR_SHARE. **Where NO prior-period column
   resolved at all, the share is UNDEFINED, not zero, and this test DOES NOT FIRE
   and DOES NOT PASS: it is recorded NOT EVALUABLE with the reason.** A file
   carrying no history column is the ordinary shape of a single-snapshot export,
   which is what almost every first run is handed. Reading its absence as evidence
   of a young population would mark nearly every first run COLD and would strike
   the own-prior-run-rate rung by definition on a twenty-year-old book. Absence of
   a column is a fact about the export. It is not a fact about the business.
2. THE ENTRY TEST. No in-scope unit has an entry date before the current window
   opened, or the earliest entry date found sits inside the current or the
   immediately preceding window.
3. THE UNIFORMITY TEST. The ranking measure is zero, blank or IDENTICAL across
   the whole in-scope population, which is what a population with no history
   looks like when it has no entry date to read either. This is the same firing
   as 11.7.3, and when it fires both sections apply.

RECORD which test fired and the FIGURE that fired it, in the front panel AND in
the audit. A detection nobody can see is a guess with better manners.

**THE CORROBORATION RULE. A SINGLE FIRING TEST THAT ANOTHER EVALUABLE TEST FLATLY
CONTRADICTS DOES NOT MARK THE POPULATION COLD ON ITS OWN.** Where exactly one
test fires and a DIFFERENT test that WAS evaluable points the other way, record
the population COLD-CONTESTED rather than COLD. Name the contradiction on the
front panel with both figures. The claim restrictions still apply, because the
safe reading is the restrictive one, but rung re-evaluation does NOT strike a
rung whose only ground for striking is the contested test. The worked
contradiction, neutral: a file with no prior-period column at all and an earliest
entry date two decades before the current window. The entry test is answerable
from the data and is evidence of a long-established population; nothing about the
missing column outranks it.

Where TWO OR MORE tests fire, or where the only firing test is uncontradicted by
any evaluable test, the population is COLD, full stop, and no corroboration is
required.

**Record every test that was NOT EVALUABLE, and why.** A reader cannot weigh a
detection without knowing how many of the three tests could actually speak.

Detection is SCOPED TO THE POPULATION BEING SCORED, per SD-POP-23. A business may
be warm in one declared population and cold in another on the same morning, and
usually is.

### 14.8.3 Rung availability is RE-EVALUATED, never inherited. SD-CLM-29.

A cold population does NOT inherit the rung availability of the mature business
around it. On detection, the available rungs are re-evaluated for THAT POPULATION
ALONE. Where a COUNTERFACTUAL_RUNG_SCOPES entry exists for the population it
governs; where none exists and the population is cold, each rung is tested on its
own terms and struck where it fails:

| Rung | Test against a cold population |
|---|---|
| Share of an addressable set | STRUCK unless the addressable set is bounded by something outside the writer's own action. See 14.8.4. |
| Matched control | Available only if a genuine untreated segment exists INSIDE the cold population itself. A control drawn from the mature business is not a control for the launch. |
| Peer distribution | Available only if the PEERS ARE ALSO COLD. Ranking a cold unit against warm peers measures AGE, not performance. The direction and intersection tests in 14.6 still apply on top. |
| Plan attainment | Normally AVAILABLE, and usually the STRONGEST rung a cold population has, provided the plan was set before the period by somebody other than the writer. |
| Own prior run rate | STRUCK by definition. There is no prior run rate. |
| Bare denominator | ALWAYS available. It is the floor and it is never struck. |

NAME every rung struck, and why, beside the figures it would have carried.

### 14.8.4 The INDEPENDENCE TEST. SD-CLM-30.

A comparison is only a comparison when the second number was not chosen, and is
not being CREATED, by the person making the claim. Where the denominator of a
share is itself under construction by the work being claimed, that share is not a
counterfactual. **It is the numerator wearing a second name.**

The test runs PER METRIC, on EVERY run, and NOT only on a resolution failure:

1. Does the denominator column resolve and populate? **A denominator that
   resolves and populates is NOT thereby independent.** The old guard fired only
   on a resolution failure, and that is exactly why it missed: at a launch the
   category denominator resolves, populates, and is meaningless.
2. Is the denominator a SUM THAT INCLUDES the numerator? If so, compute the
   numerator's share of it.
3. Where that share exceeds ADDRESSABLE_SELF_SHARE_CEILING, OR where the
   denominator's own period-over-period movement TRACKS the numerator's within
   DEADBAND across the population, the set is SELF-BUILT. STRIKE the rung, say
   so, and NAME THE FIGURE that fired the test.

Where the addressable set is being created by the work being claimed, the
share-of-addressable rung is UNAVAILABLE for that metric REGARDLESS of what
COUNTERFACTUAL_AVAILABLE_RUNGS says, and the metric drops to the highest rung
whose denominator was not chosen or built by the writer.

A denominator whose value is being created by the writer's own team CAPS CLAIM
STRENGTH AT BOUNDED for every figure computed against it, whatever rung the
organization bound. Bounded means a number with its denominator population and no
achievement wording.

The failure this prevents, stated so it cannot recur: a launch computes share of
a category that is the SUM OF THE AUTHORIZATIONS THE WRITER'S OWN TEAM HAS JUST
WON, arrives at a share near one hundred percent BY CONSTRUCTION, and ships it at
achievement strength with a WIN label. Every gate passes. That must be
impossible, and 14.8.4 plus 14.8.5 is what makes it impossible.

### 14.8.5 No prior period means NO WIN and NO MISS. SD-CLM-31.

The win, miss and flat classifier REQUIRES a prior period for the population.
Where the population is COLD the classifier DOES NOT FIRE. No figure in that
population carries a WIN label, a MISS label or a FLAT label.

This is NOT the same as the floor rung turning the classifier off. It is an
INDEPENDENT block, and it applies even where a rung that normally supports a
label is in force, because the label asserts MOVEMENT and there is nothing to
have moved from.

The state emitted instead is **NO BASELINE**. It is a real state, it is printed,
and it is DISTINGUISHABLE from UNPAIRED, from FLAT and from a suppressed label. A
reader must be able to tell the difference between "this did not move", "this
cannot be compared" and "this has nothing to be compared to yet".

A PLAN ATTAINMENT figure is EXEMPT from this block and keeps its own three
states, because attainment compares against a TARGET rather than against a prior
period, and a launch normally has a target. That is the point of the exemption.

### 14.8.6 What a person may honestly claim during a cold start. SD-CLM-32.

The cold-start rules forbid a SPECIFIC CLASS of claim. They do not forbid
claiming. A launch is often the hardest work a person does all year and the
method must be able to say so. Three kinds of claim survive intact, and the run
SURFACES ALL THREE rather than waiting to be asked:

1. **ABSOLUTE BUILD.** What exists NOW that did not exist at the start of the
   period, stated as a COUNT with its UNIT and its PERIOD. Neutral examples:
   accounts activated, sites certified, programmes live, requirements
   implemented, doors opened. It carries NO comparison and needs none, because it
   is a statement of CONSTRUCTION rather than of relative performance.
2. **SEQUENCING AGAINST PLAN.** Attainment against a target set before the period
   by somebody other than the writer, in PERCENT OF TARGET, with the three-state
   classifier that belongs to attainment, per SD-CLM-33 rung 4. This is normally
   the STRONGEST claim a cold population supports and it is a genuinely strong
   one: exceeding a launch plan is a real result.
3. **EXECUTION AGAINST A DENOMINATOR POPULATION.** The floor rung, and it is a
   legitimate, gate-passing claim. So many of so many eligible, where the
   eligible set is NAMED and BOUNDED. It has a bound, a population and a scope.

**A cold-start run that produces none of these three has not done its job.
Absence of a comparison is not absence of a finding.**

State the sequencing claim in the writer's own altitude and with a CONTRIBUTION
verb where it ladders above their scope, exactly as any other claim. Nothing
about a cold start relaxes the altitude ceiling. SD-CLM-10 as carried in 1.5.

The FRONT PANEL says, in plain words: that this population has no prior period;
that no win or miss labels were computed for that reason; which cold-start test
fired and the figure that fired it; which rungs were struck and why; and WHICH OF
THE THREE CLAIM KINDS the figures below are.

### 14.8.7 What a cold start does NOT change

The section set, their order, the identity block, the caps, the rank continuity,
the showing notes, the formatting elements and the two sizes. SD-CMP-05 and
SD-CTR-06. The pipeline order in 11.1. The percentile definition and the zero
bucket. The absence of any measure floor. The scoring formula, term for term. The
retrieval gate, the actor test and every priority rule in PART 8. The compliance
stage. The audit specification. A cold start changes what may be SAID about the
numbers, and it changes nothing about how the artifact is built.

---

# PART 15: THE DERIVED BREADTH SECTION

## 15.1 It never touches the ranking

SD-BRD-01. Breadth of adoption and allocation of time are DIFFERENT QUESTIONS.
Keep them separate and say so on the section and in the Method section.

## 15.2 The PAIR is the admission test, not a name

SD-CTR-12, SD-BRD-01, BREADTH_ADMISSION_IS_THE_PAIR must be true. The section is
built ONLY where BOTH inputs resolve: a distinct-item COUNT
(BREADTH_COUNT_CONCEPT) and a satisfaction PERCENTAGE
(BREADTH_SATISFACTION_CONCEPT). Test every candidate entity against the PAIR. If
two qualify, take the highest ranked in the standing hierarchy. If none
qualifies, SHIP THE SECTION with one explanatory row.

The entity is NOT a free choice. Building it against a count that does not exist
computes a gap, a peer norm and an upside estimate against nothing, so every
number is blank or invented. Any derived metric whose formula needs two inputs is
admitted on the PAIR, never on a name.

Neutral worked example: a unit adopting three of eleven available modules
against a peer norm of seven is an ADD; a unit on nine modules whose per-module
usage sits well below the median is a DRIVE-USAGE story, not an add story.

## 15.3 Know what your measure actually measures

SD-BRD-02. A measure derived from throughput is NOT a physical audit. A unit that
holds the full range but moves little registers low even though the thing is
present. Ranking on satisfaction percentage alone produces FALSE GAPS and sends
people to add something that is ALREADY THERE. This is mistaking a velocity
problem for a distribution problem.

## 15.4 The one size floor in the method, and the departure is stated

SD-BRD-03. This section carries the ONLY size floor left in the method, at
BREADTH_FLOOR_FRACTION of the ranked population, computed with FLOOR and never
round or ceiling, so two implementations never differ by one unit, with a
boundary tie-break on the identifier ascending.

It is DELIBERATELY STRICTER than the action lists, which carry no floor at all,
because a breadth recommendation only pays at genuine scale. Without it the
section fills with small units that carry few items BECAUSE they are small.

State the departure in the Method section, using
BREADTH_FLOOR_DEPARTURE_STATEMENT, so the floor here and the no-floor rule in
11.5 are never mistaken for an inconsistency. **Where the method breaks its own
rule, it says so and gives the reason.**

## 15.5 Two different populations, both stated

SD-BRD-04. The PEER NORM is the median count among units CLEARING THIS SECTION'S
OWN FLOOR, counting only units with a non-zero count. Bigger units carry more, so
comparing a big unit to the whole-scope median understates the gap.

The INTENSITY median is computed over IN-SCOPE units with a NON-ZERO count, not
over all in-scope units and not only over those above the floor. Units with no
items have no intensity value and cannot enter a median of one.

Report the gap only where it is at least MIN_BREADTH_GAP.

## 15.6 Check the periods before dividing

SD-PRS-46. Prefer a denominator whose period token matches the numerator's. If
none exists, use what is there, state BOTH period tokens in the Method section
AND in the section's own narrative wording, and treat the result as DIRECTIONAL
rather than exact. Never silently divide across two periods, and never invent a
scaling factor to reconcile them. A count over a longer window includes items the
unit held earlier and may no longer carry, so it runs high and the ratio runs
low, biasing the classification and understating the upside.

## 15.7 Classification and sort

Evaluate PLAY_RULES in order, stop at the first match, and state which overrides
which. SD-BRD-05. The first rule overrides the others: a unit well below the
range is an ADD regardless of how slowly it moves.

Show the upside arithmetic so it can be checked. SD-BRD-06. One named formula per
play, using the SAME figure the classification compares against.

BREADTH_SORT_KEYS: estimated value DESCENDING, then the measure descending, then
the identifier ascending. NEVER by the classification label. SD-RNK-11.

Note when a unit appears on two sections, because that is two independent reads
on the same problem and the two can usually be handled in ONE CONTACT.
SD-EXC-17.

---

# PART 16: THE EXCEPTION SECTION

## 16.1 A different question, and it never touches the ranking

SD-EXC-01. Not "where is the opportunity" but "where is something quietly wrong
that no other report will surface". Membership is TRIPPING AT LEAST ONE SCORED
FLAG, drawn from the same population the ranked lists use. It is an EXCEPTION
list, never the full roster.

## 16.2 Which flags run, and which flags EXIST

**EXCEPTION_FLAGS is bindable and its standing set is SHAPE-DEPENDENT. The four
flags this skill inherited are SEED ENTRIES, not the definition of the section.**

The four inherited flags, taken together, describe a place that stocks things and
is visited on a cadence. On a flowing population none of the four resolves,
because a transient item is not a place that stocks things, so the section would
ship a single explanatory row on EVERY run FOREVER: honest, and dead weight in
every artifact the organization ever receives. Meanwhile the exceptions that DO
matter in a pipeline exist in the data and have no home. That is a generalization
failure, not a data problem, and it is fixed here.

**The standing set when EXCEPTION_FLAGS is unbound, by the shape of the
population being scored, per SD-POP-23 and PART 23:**

| Mode | Flag | The general form | The test |
|---|---|---|---|
| FIXED | coverage stale | The unit has not been meaningfully engaged within its own cadence | Days since the recency concept above max(RECENCY_FLOOR_DAYS, RECENCY_MEDIAN_FACTOR times the LOCAL median interval), per 16.4 |
| FIXED | presence absent | A thing the unit should carry is absent, as a BINARY | The presence concept is false or blank where the unit is eligible |
| FIXED | benchmark shortfall | A thing the unit carries is materially behind its benchmark, as a DEGREE | The shortfall exceeds BENCHMARK_GAP_THRESHOLD on the column's OWN scale, read from its own maximum |
| FIXED | commitment missing | A commitment the unit is eligible for is not in place | The commitment concept is absent where the size gate qualifies the unit |
| FLOW | stage age | The item has sat in its current stage longer than that stage's own norm | Days in stage above the LOCAL MEDIAN STAGE DWELL for that stage, computed from the population in hand |
| FLOW | past due and open | The committed exit date has passed and the item is still open | Exit or commitment date earlier than the run date AND the item satisfies FLOW_OPEN_DEFINITION |
| FLOW | no next action | Nothing is recorded as the next thing to do | The next-action concept resolves and is blank for that item |
| FLOW | date moved repeatedly | The committed date has been pushed more than once | The count of recorded date changes exceeds one, where the source records history |

Every one of the eight is a SEED. A business binds its own set and these are the
starting dictionary, exactly as the concept dictionary is a starting dictionary.
Where a business declares BOTH a fixed population and a flowing one, per
SD-POP-23, each declared population takes its own flag set and the front panel
names which set ran.

Three rules the shape-dependence does not touch:

- A flag whose column does not resolve or carries no data is SKIPPED and NAMED,
  never treated as a gap. SD-EXC-08, SD-PRS-18. That is true of the FLOW four
  exactly as of the FIXED four.
- **A flag's column may have arrived by an ENRICHMENT JOIN**, per SD-PRS-48 and
  10.1.1, and once joined it is an ordinary resolved column and the flag runs on
  it normally. **A flag runs only on a column that cleared LIMB 1 of 10.1.1's
  admission test**, which means the column resolved to the concept that flag reads
  by a stated route, the first-run provisional adoption of reference/field-resolution.md 7.4a
  included where all six of its tests pass, **and the SIBLING SET of 7.4b where the
  tie at 7.4a test 5 is a declared sibling set and all five of 7.4b's tests hold as
  well.** A LIMB 2 column, admitted on a clean type alone, is CARRIED and never
  trips a flag. **WHERE THE ROUTE WAS 7.4b THE FLAG RUNS ONCE PER MEMBER, against
  that member's own column, and every count and every named row carries the member's
  name beside it**, per 7.4b and 10.1.1; the section states which members its flags
  ran on and which members had no column. **Where the flag would need ONE answer per
  unit and the admitted source states no aggregation, the flag does NOT run and is
  named as not evaluated**, because a rollup this method invented is not evidence
  and a flag scored on one would be a finding nobody authorized. Three of the four
  FIXED flags read
  exactly the kind of per-unit evidence a second file keyed on the identifier
  typically carries, and on a real run all three went unevaluated with that file
  sitting in the same input set and one of them answered in it row by row.
  **Where the join was REFUSED, the flag takes the rule above unchanged**: its
  column did not resolve, so it is SKIPPED and NAMED, never treated as a gap and
  never scored as a zero, and the section additionally names the file and the
  condition that refused the join. A flag is never run on a partly joined column:
  a ranked row that matched no record on the enriching side has that column
  UNRESOLVED, so the flag does not fire for that row and the row is counted among
  the not-evaluated rather than among the clean.
- The section ships every run whatever happens, carrying one explanatory row when
  nothing could be evaluated. SD-CTR-07. That row is placed, styled and counted by
  reference/output-contract.md PART 5.4: inside the table range as the only data row, not a
  unit row, with n and N both zero in the showing note. SD-FMT-07.

Run ONLY the flags in EXCEPTION_FLAGS whose columns RESOLVED and CARRY DATA.
SD-EXC-08. Skip the rest entirely, NAME each as not evaluated and why, and score
the remaining flags normally. If no flag can be evaluated at all, ship the
section with one row saying so. An unpopulated commitment column would otherwise
put every eligible unit on this section flagged for missing every commitment,
which is the single most damaging false positive this method can produce.

**A gap the person cannot close is not a gap worth printing, and there are TWO
TESTS.** SD-EXC-14, as refined. The rule has been read as one test and it is two,
and **ONLY THE SECOND SUPPRESSES SCORING.** Separate the AUTHORITY to set a
requirement from the ABILITY to affect the measured value:

| # | Test | Question | Effect |
|---|---|---|---|
| 1 | THE ENGAGEMENT TEST | Does the reader engage this unit AT ALL? | If not, the item is not theirs: SHOWN rather than scored. |
| 2 | THE INFLUENCE TEST | Can the reader's OWN ACTIONS MOVE the measured value, WHOEVER SET the requirement? | If YES, it is SCORED, however far above them the requirement was set. |

A requirement set by a regulator, a parent organization or a central function is
shown rather than scored **ONLY WHERE COMPLIANCE WITH IT IS ALSO DETERMINED ABOVE
THE READER**, such as a contract term, a purchased configuration or a decision
taken at a level the reader cannot reach.

Read as ONE test the rule fails in the second direction, and that failure is as
damaging as the first: it moves most of a centrally set requirement set to
shown-never-scored, leaving a rate computed over a handful of items and a
near-empty list that reads as "you are fine". **The one number the reader would
act on, the count of things to go and fix, is then suppressed by a rule written
to protect them.** Neutral worked example: an external body sets a standard; the
reader's own unit absolutely affects compliance with it; the requirement is
therefore SCORED.

Neutral worked examples of gaps that fail the INFLUENCE test and are shown rather
than scored: a procurement term set by a parent organization; a master agreement
signed above the unit; a partner of record chosen elsewhere; a configuration
purchased centrally.

**Where MORE THAN HALF the flag or requirement set falls to shown-never-scored,
STOP and SAY SO on the front panel BEFORE any rate:** this section evaluates n of
m flags, and the rate covers only those.

The flag field is EXCEPTION_FLAGS.requires_decision_authority_at_unit, and it is
now read as the INFLUENCE test rather than the authority test.

Two flags are needed because one cannot fire where the other applies.
SD-EXC-15. A binary PRESENCE flag and a DEGREE-OF-COMPLETENESS flag are
siblings. A unit failing the presence flag cannot fail the degree flag, because
it has no figure at all, which is exactly why both flags are needed. The general
form: A RATIO METRIC CANNOT SEE A ZERO DENOMINATOR.

## 16.3 Weight the flags, do not count them

SD-EXC-09. A raw count treats a long-standing minor note as equal to a serious
absence. Each flag carries its own weight in EXCEPTION_FLAGS.

**The measure multiplier has a HALF FLOOR so a real problem at a small unit
stays visible.** SD-EXC-10. Multiply the summed flag weight by

    FLAG_MEASURE_MULTIPLIER_FLOOR
      + (1 minus FLAG_MEASURE_MULTIPLIER_FLOOR) times measure_percentile

Without this a bottom-percentile unit lands in the top band on two flat flags,
which contradicts the whole premise. The half floor keeps a genuine problem at a
smaller unit VISIBLE rather than erasing it. This is the precise statement of how
to weight by size without erasing the small.

**Band AFTER the multiplier, and set PRIORITY_BAND_THRESHOLDS against the
POST-multiplier range.** SD-EXC-11. Thresholds set at the RAW flag weights are
wrong, because every score is multiplied by a factor that never exceeds one. A
single top-weight flag lands at its full value only for the highest-measure unit
in scope, at three quarters for a median unit and at half at the bottom, so under
a raw threshold the top band silently requires TWO flags and the column the
reader sorts on is deflated across the board. A threshold calibrated against the
pre-transform scale is a very common real bug.

**A BAND NOBODY CAN REACH IS NOT A BAND, AND THRESHOLDS ARE RELATIVE TO WHAT
ACTUALLY EVALUATED.** SD-EXC-32. A band is only real if the score that reaches it
is ATTAINABLE given the flags that evaluated ON THIS RUN. Where fewer flags
resolve than the thresholds were calibrated against, an absolute threshold set
for the full set becomes unreachable by construction and the top band silently
ceases to exist. Nothing fails, nothing is reported as failing, and the section
ships empty run after run.

Mechanism, and it is recomputed every run because which flags evaluate is a
property of the FILE and not of the configuration:

1. Compute the ATTAINABLE MAXIMUM: the sum of the weights of the flags that
   EVALUATED, times the largest multiplier in play.
2. Express the DEFAULT bands as SHARES of that attainable maximum, then resolve
   them to absolute numbers for this run.
3. PRINT the attainable maximum and the resulting absolute thresholds in the
   audit, so a reader can see what the bands meant on this file.

A flag that could not be evaluated is REMOVED FROM THE ATTAINABLE MAXIMUM, never
counted as a zero contribution. Counting it as zero makes the denominator lie: it
says the population was measured against four tests when it was measured against
one.

An ABSOLUTE threshold binding is legal and, where an organization binds one, it is
USED AS GIVEN. It is REJECTED AT VALIDATION where the top band exceeds the
attainable maximum of the flag set it is bound alongside, because a configuration
that cannot reach its own top band is a configuration error and belongs caught at
binding time rather than discovered three runs later in an empty section.

**Every flag carries an EXPLICIT WEIGHT.** A taxonomy that says each flag carries
its own weight and then ships a default naming no weights forces every
implementer to invent one, and two implementers invent differently off one
configuration. A weight is not an optional refinement of a flag; it is half of
what a flag is. Where a standing flag set ships without weights, this method
assigns each evaluated flag a weight of one, states that it did, and computes the
attainable maximum from that.

PRIORITY_BAND_LABELS supplies one label per threshold plus the residual.

## 16.4 Recency: the membership flag SCALES, the alert does NOT

**A recency threshold SCALES with the local cadence.** SD-EXC-02. Flag above

    max(RECENCY_FLOOR_DAYS,
        RECENCY_MEDIAN_FACTOR times the LOCAL median interval)

Cadences differ sharply by unit, so a flat line means very different things in
each: it floods a fast unit and hides real gaps in a slow one.

**An ALERT is a different instrument from a MEMBERSHIP flag, and it does NOT
scale.** SD-EXC-03. ALERT_SCALES must be false. The alert answers "has this been
left too long by ANY reasonable standard" and uses the flat thresholds
ALERT_WARN_DAYS and ALERT_OVERDUE_DAYS. A scaled alert in a fast unit would fire
at eight weeks and stop meaning anything.

Count the alert over the WHOLE ranked population, not over displayed rows.
SD-EXC-04. ALERT_COUNT_POPULATION must be whole_population. A unit can trip the
alert and still be absent from the section, because the membership flag scales
and because the cap can push it off. STATE that the counts are population-wide
and may exceed the shaded rows visible. Counting only displayed rows would
under-report the exact units the alert exists to catch.

**A gate must allow a subset relationship it created itself.** SD-EXC-05. Do NOT
require the shaded cell count to equal the reported figures: shaded cells are a
SUBSET of the reported counts and the gate must allow that. What the gate DOES
check: every displayed row in a band carries the right fill, and no row outside a
band carries any. A self-contradictory gate blocks every run.

Report a ZERO count, because it is the evidence the check ran. SD-EXC-06. Print
MSG_ALERT_LINE every run INCLUDING when both counts are zero. A zero-count line
is not noise.

**A CHECK THAT COULD NOT RUN IS NOT A ZERO. THERE ARE THREE STATES, NEVER TWO: A
COUNT, A ZERO, AND NOT EVALUATED.** Where the column the check reads did not
resolve, or resolved and carries no data, the line STILL prints and it prints NOT
EVALUATED in place of the counts, with the reason and the column named. Printing
a zero there asserts that nothing is overdue when nothing was looked at, which is
the one thing a reader of an alert line cannot recover from, and it is
indistinguishable in the artifact from a clean result. This is the ordinary case
on a first run where the recency concept did not resolve, not an exotic one.

Date arithmetic, stated explicitly including the error case. SD-EXC-07. Whole
days from the recorded date to the run date. A blank, null or unparseable date
is NOT counted in either band and is reported separately. A FUTURE-dated value is
a data error: report it, do not shade it, and do not treat it as zero.

**AND A DATA ERROR IS EXCLUDED FROM THE LOCAL MEDIAN THAT SETS THE MEMBERSHIP
THRESHOLD, WHICH IS STATED HERE BECAUSE SD-EXC-07 DOES NOT REACH IT.** The
threshold above is computed against the LOCAL MEDIAN INTERVAL, and SD-EXC-07 says
what to do with a future-dated value in the BANDS without saying whether it enters
the MEDIAN. Two implementers therefore produced two different exception sections
off one file, which is not a rounding difference: it moves the membership
threshold and so moves which units are on the section at all. The rule, stated
once:

- **A future-dated recency value does NOT enter the local median.** It is not an
  interval, it is a date that cannot be one, and admitting it pulls the median
  DOWN and TIGHTENS the threshold, which floods the section on the strength of
  values the same rule has already called errors. Excluding a value the method has
  declared an error is the same discipline that excludes a blank and an
  unparseable date from the bands.
- **A blank, null or unparseable value does not enter it either**, for the same
  reason and by the same rule that already keeps it out of both bands.
- **The exclusion is REPORTED, never silent, AND IT HAS ONE PRIMARY LOCATION.**
  The statement is the median used, the count of rows that entered it, and the
  counts excluded as future-dated, as blank and as unparseable, each named
  separately. A median computed over a different population from the one the
  reader is looking at is a number they must be told about.
  **THE PRIMARY LOCATION IS THE EXCEPTION SECTION'S OWN NOTE BAND**, note 8 of
  1.6.1, because that is where the reader is standing when the median becomes a
  question. It is COMPUTED and PUBLISHED there.
  **THE METHOD SECTION'S ENTRY IS A RECONCILIATION AGAINST IT, NEVER A SECOND
  COPY.** Per reference/output-contract.md PART 5.2 and SD-FMT-26, a statement this file
  requires in two places is reconciled rather than merely repeated: the Method
  section at 19.4 item 15 carries the same four figures AND asserts they equal the
  ones in the band, the assertion is checked at 18.1, and a disagreement blocks
  publication exactly as a disagreeing showing note does. **Two unreconciled
  copies of one figure make a reader ask which is current, and eventually only one
  of them will be**; a reconciled pair makes the duplication load bearing, which is
  the only thing that earns it. Where the reader wants the number and the reader
  wants the audit, they are two readers standing in two places, and each gets it
  where they stand.
- **The count is not zero-suppressed.** Where nothing was excluded the line says
  so, because a zero is the evidence the check ran, per SD-EXC-06.
- **This changes no band and no alert.** The flat alert thresholds are unaffected,
  the shading is unaffected, and the future-dated rows are still reported as data
  errors on their own line exactly as SD-EXC-07 requires.

**A signal that lags reality is disclosed, and weighted only where it is the
subject.** SD-EXC-12. A lagging recency field carries weight INSIDE the exception
section and ZERO everywhere else. It never touches the action lists, and the
section must say so on its face, printing RECENCY_LAG_DISCLAIMER as a visible
note. Weighting it would steer people back to units they just left. See PART 23
divergence 3 for what changes when the recency signal is a COMPUTED age rather
than a maintained contact field.

**WHERE THE SECTION IS EMPTY AND THE ALERT LINE IS NOT, THE SECTION SAYS WHY ON
ITS FACE.** The two instruments answer different questions and are permitted to
disagree, per SD-EXC-03 and SD-EXC-05, and a gate that demanded they agree would
block every run. But an artifact carrying an empty exception section a few lines
under an alert line reporting a dozen stale units reads as broken, and a reader on
a hurried morning reads the empty section and not the note somewhere else.

So where the section ships empty AND either alert count is above zero, the
section's single explanatory row carries the reconciliation itself, in one
sentence: the membership flag SCALES with this population's own median interval,
which is n days, so the flag fires above m days, and the alert does NOT scale and
fires at the flat bands, so k units are past the flat band and none is past the
scaled one. That is a true statement, it is one row, and it is the difference
between an artifact that looks wrong and one that explains itself. No weight, no
threshold and no count changes.

**THAT ROW IS THE EXPLANATORY ROW OF AN EMPTY SECTION, AND
reference/output-contract.md PART 5.4 PLACES IT, STYLES IT AND COUNTS IT.** This file
restates none of that standard and states only which sentence goes in it. Read
5.4 for the three things a run gets wrong here otherwise: the row sits INSIDE the
table range as the first and only data row, styled exactly as a populated row with
the full grid across the whole width of the block; **it is NOT a unit row**, so n
and N in the showing note are both zero and the section holds one written row; and
**a run that clears the resulting mismatch by writing one of one has told the
reader a unit exists that does not**. The counter tells the two apart without
judgment, because the explanatory row carries no value in the section's FIRST
IDENTITY COLUMN, which is the POSITION column R1 puts in first position, and is the
only data row on the sheet; the test reads that column rather than an IDENTIFIER
column, because the priorities section is a REFERENCE TABLE and carries no unit
identifier to read. **THE SENTENCE ITSELF BEGINS IN THE TABLE'S SECOND COLUMN**,
which is the first column after the position column and the leftmost place it can
legally begin, and the cell there holds a NON-EMPTY string saying in plain words
why the section qualified nothing. A bordered, computed-height row holding no
string at all is a FAILURE under 5.4 and PART 7.2 row C2, and so is a sentence
placed further right than the second column behind a run of empty cells. The section's NOTE BAND still ships above
nothing and carries the showing note reading zero of zero, the ordering note and
notes 8 and 9 of 1.6.1, per 5.4's own last paragraph: the explanation of WHY the
section is empty lives in the row, the count lives in the band, and neither
substitutes for the other.

Do not re-sort the section by staleness. Sort by the banded priority and then by
the standing keys.

## 16.5 Benchmarks on this section

Report the local benchmark ALONGSIDE each figure so an outlier is legible as
one. SD-EXC-13. Report it ONCE, not per row. SD-EXC-21.

Benchmark ONE LEVEL WIDER than the user's own slice. SD-EXC-20. A unit against
its parent, a parent against its parent. When the file holds nothing wider,
benchmark against the whole file and SAY SO, because a slice compared only to
itself cannot see that it is the weakest one.

Show BOTH SIDES, never the delta alone. SD-EXC-16. The pair is the conversation.
Include the sizing figure so the reader can size it.

## 16.6 Economics, not geography

**The economics gate, not a geography gate.** SD-EXC-18. Adoption of a
cost-bearing programme tracks SIZE, not location, so the qualifying rule is
SIZE_GATED_PROGRAM_TEST, a size test computed from the user's own file every run,
and never a location test. A small unit declining is a rational business
decision, not an execution gap. Recompute the size figures from the user's own
file every run and never quote reference figures.

**Do NOT suppress an opportunity because most local peers also lack it.**
SD-EXC-19. Low penetration is exactly what an opportunity looks like. The measure
weighting already handles genuine regional differences. Do not build a hard-coded
regional table: it cannot be validated from a single-region file, and it rots
silently.

## 16.7 Shown, never scored

SD-EXC-22. Values in SHOWN_NEVER_SCORED_CONCEPTS are displayed in their own
column for every row, given ZERO weight, and their population share is reported
as a single figure. They never confer membership.

State NO interpretation of a value whose meaning varies by jurisdiction.
SD-EXC-23. Print the status and the benchmark; do not tell the reader what it
implies, because the rules that give it meaning differ by place and the method
runs in all of them.

> Report what the data says, attribute it, and leave the judgment to the person
> who knows their jurisdiction.

## 16.8 Exemptions as belt and braces

SD-EXC-26. Once a class is removed upstream, per-flag exemptions in
FLAG_EXEMPTIONS never fire, but they REMAIN as a second line of defence in case a
future change re-admits the class. A unit of that class appearing on this section
is treated as EVIDENCE THE UPSTREAM EXCLUSION FAILED, and the artifact should
not be published. That is a defence-in-depth pattern with an explicit tripwire
reading.

Do not extend a narrow exemption by analogy. SD-EXC-27. If someone says another
group behaves the same way in their area, that is a change to REQUEST, not one to
INFER from the data.

## 16.9 Fill rate, and not duplicating a system of record

Check a field's FILL RATE before building on it. SD-EXC-25. A field populated for
a small fraction of units is too thin to be useful. Check the rate rather than
assuming, and say so if a future file is materially better populated.

Do not build a second version of something that already has a system of record.
SD-EXC-24. Even where the inputs are present, do not duplicate a capability
another system owns, because a second version competes with the system of record.
SYSTEM_OF_RECORD_EXCLUSIONS names them.

---

# PART 17: STAGE 10, ASSEMBLY AND BUILD RELIABILITY

## 17.1 Persist the result before building

SD-EFF-27. Save the computed ranking to a scratch file so a failed build RESUMES
rather than RECOMPUTES. Recomputation risks a different result and makes the
failure harder to diagnose. A rerun on the same inputs must produce the same
result.

Write CONTINUOUSLY; never hold more than one stage in memory. SD-EFF-30. After
every stage that produces a finding, a number or a paragraph, append it to the
checkpoint before starting the next stage.

The checkpoint holds LEDGERS ONLY and is never mistakable for a result.
SD-EFF-31. Raw findings, computed values, ranks, tie counts, matches and the
parse log. No assembled prose, no copy blocks. If it contains nothing that looks
finished, it cannot be mistaken for finished. It is written under SCRATCH_DIR,
never under OUTPUT_DIR, and it is deleted when the real artifact publishes and
RETAINED on a bannered partial. CHECKPOINT_DELETE_ON_PUBLISH governs.

A checkpoint failure degrades DURABILITY, not CORRECTNESS. SD-EFF-33. Retry the
write once, then continue and warn the user that an interruption will require
restarting. A checkpoint failure never stops a run.

A stage that cannot write its checkpoint HAS FAILED. SD-EFF-14. Absence of the
checkpoint file is a failure signal, not an ambiguity, regardless of what the
worker says.

## 17.2 Build order is by ACTUAL size, largest first

SD-EFF-22. Count the rows each section will hold, build in DESCENDING order of
that count, then the summary panels, with the front panel LAST. Do not hard-code
the resulting sequence; sort by the real count every run.

Building smallest first spends the run's budget on the small sections and
reaches the largest with nothing left, which is precisely how an artifact ships
with styled action sections and a bare reference section. The biggest section is
built while the run is freshest.

Finish each unit COMPLETELY before starting the next. SD-EFF-23. One section
fully drafted, verified and checkpointed, then the next. Never draft everything
shallowly and return to deepen it, which produces an artifact with three
polished parts and a bare fourth.

Last in the order NEVER means finished with less care. SD-EFF-24. The summary
panels are built last for a stated reason, that the front panel must name what
was ACTUALLY built, but they carry the same completion rule: each styled and
verified before the next begins, each recording its own format pass. Otherwise
the pages a manager opens first are the only ones with no gate behind them.

A unit is not complete until its data AND its formatting are verified.
SD-EFF-25. Record per-section completion as rows written PLUS a format-pass
flag. A section whose format pass is false is as incomplete as one missing rows,
and the run does not advance past it. Never defer formatting to a trailing pass.

## 17.3 Writing mechanics

The two failure modes look identical and must be told apart by WAITING.
SD-EFF-10. A call can return success and land nothing; a read service can lag
its own write. Treat BOTH as UNCONFIRMED, never as failed. Wait
WRITE_CONFIRM_WAIT_SECONDS and read again before concluding anything.

Read back the TAIL of a chunk, never the head. SD-EFF-19. Verify the last
WRITE_VERIFY_TAIL_ROWS rows of each chunk of WRITE_CHUNK_SIZE. A partial write
fills the head and drops the tail, so reading the top proves nothing.

Never mix data writes with structural operations in one call. SD-EFF-20. One
kind of operation per call. A table applied in the same call as a failed write
left a sheet PERMANENTLY UNWRITABLE: every later write to it returned ok and
landed nothing.

Data first, structure second, PER SECTION, never one structural call for the
whole artifact. SD-EFF-21. Write and verify every row of one section, apply that
section's structure in its own call or calls, verify those landed, and only then
start the next section. One structural call spanning every section is exactly
the shape this rule warns against, and it is how a single dropped call un-styles
half an artifact.

Never let a worker's optimism advance the run. SD-EFF-13. The supervisor
advances on evidence READ FROM THE ARTIFACT, never on a worker's report. Where
the two disagree, the FILE WINS. "Wrote 250 rows" is a claim; a read showing 250
populated rows is evidence.

**THE HEADER ROW IS WRITTEN INTO ROW 1 AND NOTHING IS EVER WRITTEN ABOVE IT.**
reference/output-contract.md element 1. The build never opens a section by writing a title,
a scope line, a period line, a note or a banner and then starting the headers
underneath, and it never inserts a row above a header row later to make room for
one. Every one of those breaks the freeze pane, the table range, the autofilter
and every header-name lookup at once, and they break them SILENTLY, after the
rows have already been verified. Where any of that text has to go somewhere, it
goes to the front panel per 19.3.1.

**THE WIDTHS AND THE TWO HEIGHTS ARE COMPUTED AS PART OF THE BUILD, NEVER AS A
FINISHING PASS.** Column widths come from reference/output-contract.md PART 2.2, body row
heights from PART 2.3 and the header row height from PART 2.4, which are elements
10, 12 and 14. **The three computations are not restated here and are not
approximated at build time.** Two mechanics follow from the rules already in this
section:

- **They are applied in that SECTION'S OWN structural call**, alongside the rest
  of that section's structure, per SD-EFF-21. A width or a height applied in one
  later sweep across every section is exactly the single whole-artifact
  structural call SD-EFF-20 and SD-EFF-21 forbid, and it is how one dropped call
  leaves a single section with clipped rows and a header hidden behind a filter
  caret while every other section looks correct.
- **The order inside the section matters, because element 12 depends on element
  10.** A row height is computed from wrapped content against each cell's FINAL
  column width, so the widths are set and read back FIRST and the heights are
  computed from the widths the file actually carries, never from the widths the
  build intended to set. Computing a height against an intended width is the same
  class of error as verifying against the build intention rather than the
  artifact, which PART 7.1 forbids outright.
- **THE WIDTH IS THE ONE PART 2.2 COMPUTES, AND THE RULE ABOUT CHAR_WIDTH_FACTOR
  IS A DIRECTION RATHER THAN A BAN ON ARITHMETIC.** PART 2.2.1 defines the three
  primitives, 2.2.2 gives the seven steps, and 2.2.3 states the direction; this
  file restates none of them and reproduces no formula. What the build must hold on
  to is the direction itself, because both mistakes have now been made and both
  blocked a correct workbook:
  **MULTIPLYING A WIDTH BY CHAR_WIDTH_FACTOR IS FORBIDDEN, ALWAYS AND
  EVERYWHERE.** The factor is less than one, so it NARROWS the column below the
  header floor computed two steps earlier. Measured: element 10 failed on every
  column whose data requirement did not exceed its header requirement, publication
  was blocked on a workbook that was right, and the columns were genuinely narrowed
  below their own headers, which is the defect element 10 exists to prevent.
  **DIVIDING A CHARACTER REQUIREMENT BY CHAR_WIDTH_FACTOR TO OBTAIN THE WIDTH THAT
  HOLDS IT IS PERMITTED, AT 2.2.2 STEP 5, ONCE PER COLUMN, AND NOWHERE ELSE.** It
  is the arithmetic inverse of primitive 2 and it can only ever WIDEN, so it cannot
  produce the defect the ban was written to stop. **Banning it as well was the
  opposite failure and was also measured**: with the width set to the character
  requirement itself, the width and the usable-character count became two different
  quantities wearing one number, 2.4 read the built width back as
  `width times factor less the caret allowance`, which is strictly below the
  requirement for every factor under one, and 14 of 29 columns needed three lines
  against a two-line budget on a workbook built exactly to the width rule.
  **APPLYING ANY FACTOR TO A WIDTH AFTER STEP 5 IS FORBIDDEN.** Step 7 sets the
  number unchanged and nothing scales it afterwards.
  **THE CONSEQUENCE THE BUILD RELIES ON, WHICH IS 2.2.4's COMPOSITION AND NOT THIS
  FILE'S CLAIM:** the quantities run in one direction, from the header text to `H`
  to the character requirement to `W` to the usable counts to the line counts to
  the heights, and nothing reads a value produced to its right. So a build that
  follows 2.2, 2.3 and 2.4 in order satisfies elements 10, 12 and 14 BY
  CONSTRUCTION. **There is no case in which this skill widens a column beyond what
  2.2 prescribes in order to pass element 14**, and any local rule that once
  licensed doing so is deleted rather than kept alongside: element 14's assertion
  follows from element 10's, so a failure at 14 is a report that some width was NOT
  set by 2.2, and the remedy is the width. **RAISING HEADER_MAX_LINES TO CLEAR IT
  IS FORBIDDEN**, per PART 2.4 and PART 8, because it clears the check by lowering
  the standard the check exists to hold.

- **AND THE WIDTH CARRIES A SECOND FLOOR: THE LONGEST UNBREAKABLE TOKEN THE COLUMN
  MUST DISPLAY**, taken over the header and over the data the column will carry, which
  is `T` at PART 2.2.1 primitive 4 and PART 2.2.2 step 3b. It is a floor and nothing
  lowers it, the column cap included, so the wrap is never asked to fit a word into
  less room than the word takes and **NO WORD IS EVER CUT BY A CELL EDGE.** The wrap
  breaks on spaces only, in a body cell exactly as in a header cell. Where one token
  genuinely exceeds the column cap the column takes the width the token needs and
  Method REPORTS it, naming the column, the token, its length and the width it forced;
  **breaking the token is forbidden and so is every disguised break, an inserted line
  break, an inserted hyphen, an ellipsis, a truncation or a smaller font.** The floor
  enters the arithmetic to the LEFT of the width, alongside `H`, so PART 2.2.4's chain
  stays one-directional and nothing here reads a value produced to its right.
  SD-FMT-30, PART 2.10.

All three are then read back through the engine and verified at 18.2. SD-FMT-23.

**EVERY BAND WIDER THAN ITS OWN CELL IS MERGED ACROSS EXACTLY THE SPAN IT NEEDS, NEVER
MERELY STYLED ACROSS IT.** reference/output-contract.md PART 2.10 and SD-FMT-30. That binds every
band this artifact writes: a front panel or Method title row, a panel section header
band, a section's NOTE BAND under 1.6.1, the explanatory row of an empty section, and
any banner. **A BAND STYLED ACROSS A SPAN AND NOT MERGED ACROSS IT LEAVES ITS TEXT IN
THE FIRST CELL, OVERFLOWING INTO THE NEXT**, and element 7's border on that next cell is
then drawn through whatever word is crossing it, which is what was reported on a
delivered workbook: a title band whose text ran past its own cell, with the neighbouring
cell's left border through the middle of a word. **THE TWO LOOK IDENTICAL UNTIL THE GRID
GOES ON**, so the build never treats a shared fill as evidence that a band is merged; it
merges the region and reads the merge back. Element 7 then carries the border on the
OUTSIDE of the merged region and no interior line exists to cut anything.

**THE FROZEN-SPAN WALK IS THE ONE STRUCTURAL COMPUTATION THAT IS NOT PER SECTION,
AND ITS PLACE IN THE BUILD ORDER IS LOAD BEARING.** Everything else in this section
is written and verified one section at a time, per SD-EFF-21, and the walk of
reference/output-contract.md 4.1.2 cannot be, because it reads each identity column's MAXIMUM
built width ACROSS EVERY SECTION. So the build runs it in one place: **after every
section's widths are set and read back, and before any freeze is set anywhere.**
It yields ONE `IDENTITY_BLOCK_ANCHOR_COLUMN` for the artifact. Each section's
freeze is then set in THAT SECTION'S own structural call, per SD-EFF-21, at row 2
and at the first column after the anchor **located by header name on that section**,
so one computation reaches every section without one structural call spanning them.
A build that sets a section's freeze inside that section's first structural pass,
before the later sections' widths exist, has performed the per-section walk 4.1.2
forbids, and it will pass every per-section check while failing 18.1 and 18.2. The
ONE truncation record of 1.3 is written from that one walk. SD-CTR-08, SD-FMT-03.

**THE TOTAL WIDTH OF A GRID IS BOUNDED TOO, AND THE BOUND IS DECLARED BEFORE THE
COLUMNS ARE BUILT.** reference/output-contract.md 2.7 and SD-FMT-28 own it and this file
restates neither the ladder nor the arithmetic. What the build does:

- **READ `GRID_MAX_TOTAL_WIDTH` FIRST AND RECORD THE VALUE BEING BUILT TO**, in the
  Method section, before any column of any section is set. It bounds the SUMMED
  BUILT WIDTH of one entity section or the reference table, in the SAME width unit
  2.2 sets column widths in and `FROZEN_SPAN_MAX_WIDTH` bounds the frozen span in.
  It binds a SECTION, never a column and never the workbook.
- **MEASURE IT PER SECTION, from the widths read back through the engine**, in the
  same read-back that feeds elements 10, 12 and 14, and never from the widths the
  build intended to set.
- **NEVER RAISE IT TO CLEAR A SECTION THAT FAILED IT.** A bound discovered after
  the measurement is not a bound, exactly as HEADER_MAX_LINES is never raised to
  clear a failing element 14 and no column is ever widened past 2.2 to clear one.
- **WHERE A SECTION IS OVER, RUN 2.7's RELIEF LADDER IN ORDER, BEFORE PUBLICATION,
  AND RECORD THE RESULT.** The ladder is 2.7's and is cited rather than restated;
  its step 3 recomputes every width from 2.2 from the top, which is the only thing
  that sets a width here, so nothing is adjusted by hand to bank a saving. **The
  three things that never give are 2.7's and hold absolutely in this artifact:** no
  column is dropped, mandatory or carried; no column goes below its own header
  floor; and no value that carries meaning is shortened, which here means that a
  unit name, an identifier, a date, a quoted instruction, a per-row reason and a
  narrative sentence are untouchable. A section still over the bound after the
  ladder SHIPS OVER IT AND SAYS SO, per 2.7 step 4, and 18.2 passes it on the
  record rather than on the total.
- **THIS SKILL'S OWN INTERACTION WITH THE LADDER, STATED ONCE:** the standing
  qualifiers this artifact can carry are the closed-set members of
  CLOSE_STATE_VOCABULARY's exact wording and of HDR_DIRECTIVE_STATUS, and step 1
  moves those to the legend against a short declared code with a mandatory legend
  row. Step 2's destination is the narrative column of element 11, whose own bound
  is unchanged and is never raised to absorb the traffic. **A per-row reason under
  1.3 is unique to its own row and is therefore NOT a standing qualifier**, so the
  ladder never touches HDR_RANK_REASON.

**THE NARRATIVE COLUMN'S BOUND IS READ AS WIDTH UNITS, WHICH IS WHAT ELEMENT 11
SAYS AND WHAT 2.2 STEP 6 APPLIES, DESPITE HOW THE VARIABLES ARE NAMED.**
reference/output-contract.md element 11 states the range as WIDTH UNITS twice and applies it
to the width DIRECTLY with no conversion of any kind. The two variables carrying it
are named for characters and their SECTION A1 defaults are worded in characters, so
three statements read one way and the governing one reads the other, and at the
bound conversion factor the two readings differ by more than a tenth of the widest
column in the workbook. **ELEMENT 11 AND 2.2 STEP 6 GOVERN: the value is applied to
the width directly, and no factor is applied to it in either direction.** The
column is still never set below its own header floor. The naming is raised once
with the binding owner as an open request under PART 22, per 1.3e's discipline for
a shared-layer string this file cannot fix, and it is never resolved locally by
converting the number.

**ONE FILTER PER SECTION, AND IT IS THE ONE THE READER'S OWN ENGINE LOOKS FOR.**
Element 6 requires a live filter on every column of every entity section, and it now
fixes the MECHANISM as well: **the SHEET'S OWN FILTER, declared on the sheet, over the
populated block element 3 fixes, with EXACTLY ONE filter object over that range.** The
build sets that filter and sets no second one. **IT DOES NOT CARRY THE FILTER INSIDE
THE TABLE OBJECT AND CALL THE ELEMENT SATISFIED**, which is what the previous mechanic
here said to do, and the consequence was measured by opening the delivered files: no
visible filter control on any sheet of any workbook, on the feature element 6 itself
calls the most-used in a delivered workbook, with the verification certifying it
because it read the filter back out of the table container rather than off the sheet.
**THE MECHANISM IS CHOSEN FOR THE ENGINE THE READER OPENS AND NEVER FOR THE ONE THE
FILE WAS BUILT IN. SD-FMT-29.** That is the same principle already governing this
artifact's header band direction and its alpha bytes, applied one layer out.

**WHERE THE ENGINE CANNOT CARRY BOTH A TABLE OBJECT AND A VISIBLE FILTER OVER ONE RANGE
WITHOUT SETTING TWO OBJECTS, THE VISIBLE FILTER WINS AND ELEMENT 3 GIVES**, per element
3's own text, and the conflict is named in Method. Element 3's stated purpose is a sort
that keeps a row's cells together and the filter's own sort serves it; element 6's
purpose is served by nothing else, and a filter nobody can see serves nothing at all.
The build never resolves that trade in the other direction. 18.2 asserts the filter by
reading it back FROM THE SECTION of the built artifact, spanning every column, one
object over the range: a filter found only inside the table container is scored ABSENT.

## 17.4 The only permitted deletion

SD-EFF-26. Recreating ONE damaged, unpublished section inside the in-progress
scratch artifact. Never delete a published file, a user's source data, or a
section holding verified rows, and never recreate a section to start clean when
the real problem is a failed chunk.

Confirm the unwritable state is real first: wait WRITE_CONFIRM_WAIT_SECONDS and
confirm TWO CONSECUTIVE writes landed nothing. If a recreated section fails the
same way twice, STOP and do not delete a third time.

## 17.5 Fan-out inside a stage

Partition DETERMINISTICALLY, and verify the MERGE rather than the workers.
SD-EFF-17. Split into contiguous blocks of PARTITION_SIZE by identifier
ascending, cap concurrency at MAX_CONCURRENT_WORKERS, write one checkpoint per
worker, and have the supervisor confirm that every partition index is present
with no gaps, that the row counts SUM to the expected total, and that no
identifier appears in two partitions. A missing partition is the failure mode
that looks most like success: the run completes, the counts are internally
consistent within each worker, and a whole block of units simply are not there.

**Nothing that needs the whole population may be computed inside a partition.**
SD-EFF-18. Percentiles, medians and peer norms are GLOBAL. Workers return raw
values; the supervisor computes the distribution ONCE over the merged set. A
percentile computed per partition is a different number wearing the same name,
and it is the single most likely way a large run silently diverges from a small
one.

A worker failure is isolated to its own partition. SD-EFF-15. Retry that
partition alone through the graduated ladder, leaving every other partition's
verified output untouched. A stage fails only when a partition has exhausted the
ladder AND one rebuild. Never discard the work of eight healthy workers because
the ninth stalled: that is how a long run on a large file turns into no run at
all.

## 17.6 Publish once, at the end

SD-EFF-28. Never publish a partially built artifact to show progress.

---

# PART 18: STAGE 11, THE VERIFICATION GATE

This stage IS the contract gate. It verifies 1.9 in full, against the current
artifact.

## 18.1 Reconciliation

- Row count exact per section against that section's own expected number,
  computed by the arithmetic in 1.6, never by a literal.
- The user-requested-size split, where one applies, is
  USER_SIZE_TIER_1_FRACTION rounded UP to the first tier.
- The last merit rank is the DERIVED ceiling, not the tier size. SD-RNK-02,
  SD-RNK-03.
- Rank continuity across the merit sections, with no cross-section duplicate
  identifier.
- Scope purity: every row carries the resolved scope code.
- The rank columns: either both ship or exactly one does, the SAME choice on
  every item section, and where one ships, the two ranks were equal on every row
  of the ranked population. Per 1.3b.
- The header row of every item section is ROW 1, and cell A1 holds a header
  string. No title, scope line, period line, note or banner appears above any
  header row, on any section, including on a degraded run. Per PART 1 and
  reference/output-contract.md element 1.
- HDR_RANK_REASON present with its header, in the FIRST COLUMN AFTER the identity
  columns and OUTSIDE the frozen span, per 1.3 and reference/output-contract.md 4.1.1, and
  POPULATED on every row of every section whose rows are
  units, AND on every row of the priorities section, which is a REFERENCE TABLE
  and carries both columns per 1.2.2. Its content matches the family it sits on,
  per the table in 1.3b: the scoring terms on the merit sections, the directive on
  the directed section, the sort keys on the breadth section, the tripped flags on
  the exception section, the ordering keys of 1.2.2 on the priorities section.
  Blank is not permitted and neither is a copy of the narrative cell. Per
  reference/output-contract.md PART 4.1 and R1 of PART 7.2.
- The position column is headed HDR_RANK on the merit sections and HDR_POSITION on
  the directed, breadth, exception and priorities sections, and a section ordered
  on something other than merit that is headed with the rank string fails the
  gate. **A position column headed HDR_PRIORITY_BAND fails the gate on every
  section**, because that variable heads a column of BAND LABELS and never a
  column of numbers; on the exception section the band label ships as its own
  separate column beside the position column. Per 1.3b and reference/output-contract.md
  PART 4.1.
- HDR_COMMITMENT_DATE, HDR_CLOSE_STATE, HDR_CLOSE_WEIGHT and HDR_ACTION present
  with their headers on every section whose family carries them, in their contract
  positions; a missing column is not permitted. HDR_COMMITMENT_DATE may be blank
  where no date was derivable; HDR_ACTION is never blank. Per 1.3b and SD-CTR-13.
- Every HDR_CLOSE_STATE cell holds the CLOSE_STATE_VOCABULARY label for one of the
  nine state keys in 12.3.1, and the label on each row agrees with that row's
  weight in HDR_CLOSE_WEIGHT and with the wording in its narrative column. A row
  whose label, weight and wording disagree fails the gate, and so does a cell
  holding a raw state key, an empty string or a string outside the bound set.
- The ordering note is present on every ranked section, its {k} figure equals the
  count of rows on that section whose commitment date falls outside the planned
  window, and it is present where that count is zero. Per 1.6.
- Every corrected header from 1.3e ships its corrected string where the header is
  unbound, its bound string where it is bound, and carries a gloss in the front
  panel's column glossary.
- No column in the mandatory set of 1.3c was removed by any rule, and every
  mandatory column that carried one repeated value ships with its cells and is
  named in the front panel's uniform-column line. Per SD-FMT-21.
- Alignment: every column whose shape token is COUNT_OR_MEASURE,
  RATE_OR_PROPORTION or DATE is right aligned and every column whose token is
  IDENTIFIER_OR_CODE, STATUS_OR_CATEGORY, BOOLEAN_LIKE or FREE_TEXT is left
  aligned, checked column by column against the bound list, and NO COLUMN IS
  CENTRED, because this artifact declares no STATUS GRID COLUMN under
  reference/output-contract.md 2.5, per 1.10 declaration 1. **Alignment is checked against
  2.5 alone**: 1.10's second declaration, that this artifact carries no
  CLASSIFICATION COLUMN under 2.6, is a different statement about fills and is
  checked at 18.2, and neither declaration is evidence for the other. Per 1.10 and
  SD-FMT-05.
- The FROZEN SPAN, **checked as ONE property of the ARTIFACT and not as a property
  of each section**: the walk of reference/output-contract.md 4.1.2 ran ONCE, over each
  identity column's MAXIMUM built width across every section carrying the full
  identity block; the summed widest-case built width of the frozen columns is at or
  below FROZEN_SPAN_MAX_WIDTH or the span is exactly one column; the anchor is the
  last identity column that walk admitted; **EVERY section carrying the full
  identity block freezes THE SAME COLUMNS, located by header name, so two sections
  of one artifact never freeze different numbers of identity columns** and a
  genuinely narrower section freezes the same columns in fewer width units and
  never more columns; the reason column is outside the span on every section; and
  the Method section carries **exactly ONE** record of the walk either way, naming
  which section supplied the widest case for each identity column. **More than one
  such record, or a second anchor anywhere, fails the gate**, because it is the
  evidence that the walk ran per section. Per 1.3, 1.9 item 15, SD-CTR-08,
  SD-FMT-03 and reference/output-contract.md 4.1.2.
- The DIRECTED section holds only rows placed there by a DIRECTIVE. No row on it
  was placed by an assignment, and no row anywhere carries MANDATORY_MULTIPLIER
  whose resolved actor is not the reader or whose actor could not be identified.
  Every direction the downward sweep of 8.4.1 returned was put through 8.7.1's
  ladder and the rung that resolved it is recorded. Per 8.7.1.
- Every admitted direction that could not be evaluated has its own row on the
  priorities section, with its status, its reason and its closest candidate column
  named, and the section's note band carries the count, including where the count
  is zero. Per 8.8.1 and 1.6.1 note 10.
- The RECENCY MEDIAN RECONCILIATION agrees between its primary location, the
  exception section's note band, and the Method section entry that reconciles
  against it: the median, the count that entered it, and the three excluded counts
  are equal in both, and a disagreement blocks publication. Per 16.4 and 19.4.
- The commitments-in-window line is present, its per-section counts sum to its own
  total, each count equals the number of rows in state 1 of 12.3.1 on that
  section, and every one of those rows is named with its rank in the Method
  section. Per 19.3.1 block 1.
- The ordering note on each ranked section carries BOTH counts, and j plus k
  equals the number of rows on that section carrying a derivable date. Per 1.6.
- The narrative column carries the three per-row facts of 1.3b on every row, and
  where two rows carry identical narrative text the uniform-column finding is
  present.
- The covering invariant holds: every day of the named planning period lies inside
  the resolved operating window. Per 7.1 and SD-SCO-17.
- The do-this-week block: every entry's identifier appears at the rank the entry
  names, in the section the entry names; the block added no row and removed none;
  and every section row count reconciles exactly as it would with the block
  absent. Per 19.3.1 block 2.
- No blank required cells, with the exemptions named explicitly and no others.
- Every exclusion still holds. Every ordering invariant still holds.
- Types preserved: identifier and postal-style columns read as text.
- SPOT_CHECK_SAMPLE_SIZE units re-read from the source and compared to the
  artifact.

## 18.2 The formatting matrix

**THE MATRIX IS THE ONE IN reference/output-contract.md PART 7.2 AND THIS FILE DOES NOT
DEFINE A SECOND ONE.** It is recorded as ONE ROW PER SECTION PER ELEMENT, over
every element of PART 2.1 and over R1 THROUGH R5 AS WELL, read back from the
BUILT artifact through the engine per PART 7.1 and never from the build's own
intention. Not applicable is a PASS and carries its stated reason; not applicable
with no reason recorded is NOT IMPLEMENTED, which is a FAILURE. **A gate that
cannot run HAS FAILED**, per PART 7.1 and SD-EFF-03, and the resolution is the
`shared.formatting_unverifiable` gate in 20.1.2 with the ladder in
reference/capability-probe.md 2.2. The counts of all three states, per section, are
published in the Method section, because a section reporting many not-applicable
entries is either genuinely simple or quietly unbuilt and only the counts beside
their reasons let a reader tell which. SD-FMT-22, SD-FMT-01.

**ELEMENTS 10, 12 AND 14 ARE VERIFIED BY RECOMPUTING THE REQUIREMENT AND
COMPARING IT TO WHAT WAS BUILT**, per reference/output-contract.md PART 2.2, PART 2.3 and
PART 2.4 respectively. Those computations are not restated here. What this file
adds is WHERE each one is checked in this artifact:

| Element | Checked against, on every item section |
|---|---|
| 10, column width | every column: recompute `H` from the header string by PART 2.2's primitive 3, read the BUILT width `W` back through the engine, and assert `floor( usable_header( W ) ) >= H`, which is PART 2.2.4's own verification and is equivalently `W >= ( H + CARET_ALLOWANCE_CHARS ) / CHAR_WIDTH_FACTOR` at two decimal places. Additionally assert that no width was MULTIPLIED by CHAR_WIDTH_FACTOR and that the only conversion applied was 2.2.2 step 5's single division, per PART 7.2 row 10. A column that cannot show its own header inside its own line budget fails |
| 12, row height | every populated row, THE NOTE BAND'S ROWS INCLUDED, against the wrapped content of its own cells at their FINAL BUILT widths, never at the widths the build intended. CHAR_WIDTH_FACTOR converts each built width into usable characters here, which is the MULTIPLYING direction of PART 2.2.1 primitive 2 and is what a height computation reads; the one DIVISION that sets a width happens at 2.2.2 step 5 and nowhere else, per PART 2.2.3. A merged note band row is measured against the SUMMED width of its merged span, per PART 5.3 |
| 14, header row height | the header row, against the header needing the most wrapped lines at the BUILT widths, and additionally that no header on the section exceeds HEADER_MAX_LINES. **This assertion follows from element 10's**, per PART 2.2.4, so a failure here reports a width that was not set by 2.2 and the remedy is the width. HEADER_MAX_LINES is NEVER raised to clear it, and no column is widened past what 2.2 prescribes to clear it either |

A header that needs more lines than the budget allows is a header to be
SHORTENED, which routes to 1.3e and to PART 22 decision 48 as a header
correction, disclosed with the string it replaced. It is never fixed by making
the row taller. SD-FMT-23.

**R1 IS CHECKED ON EVERY ENTITY SHEET AND ON THE REFERENCE TABLE, AND THE ONE
EXEMPTION IS RECORDED RATHER THAN SKIPPED.** Per 1.2.1, the ENTITY SHEETS are the
sections of the identity_and_rank, reference, mandatory, derived and exception
families, and the REFERENCE TABLE is the priorities section. On every one of them:
the position column is first and is headed for what it is, HDR_RANK on a merit
order and HDR_POSITION otherwise and never HDR_PRIORITY_BAND, and HDR_RANK_REASON
is present and populated in the first column after the identity columns. **The ONE
family exempt from R1 is `panel`**, because a PANEL SHEET has no header row and no
grid of units, and the exemption is written into the matrix WITH THE SHEET CLASS
as its reason, because a not-applicable with no reason is a not-implemented. The
`direction` family is NO LONGER exempt: PART 2.0 makes it a REFERENCE TABLE and
PART 4.1 admits no reference table without both columns, per 1.2.2. SD-FMT-24.

**R2 IS CHECKED ON THE MERIT TIERS ALONE**, which are the first action, second
action and reference sections, per 1.2.1. The directed, breadth and exception
sections are NOT merit tiers and are outside the assertion, and that exemption is
recorded with the KIND declaration as its reason rather than assumed. A unit
appearing on a directed section and on no merit tier is not a duplicate; a unit
appearing on two merit tiers is, and it blocks publication.

**THE SHEET CLASS AND THE RANKED KIND OF EVERY SECTION ARE RECORDED IN THE MATRIX
ITSELF**, from the declaration in 1.2.1, so a reader can see which elements were
expected to run where instead of inferring it from what the verification happened
to check. PART 2.0 and PART 4.2 both require the declaration; this is where it is
carried into the record.

**R2 through R5 are checked as PART 7.2 states them**, against the reconciliation
already run at 18.1: rank continuity with no cross-section duplicate identifier;
every BOUNDED section against its own showing note and the Method section's note
for it, with N read from PART 5.1.1 for that section's own bound per the table in
1.6, and with the explanatory row of an empty section counted by neither n nor N
per PART 5.4; the reference section's row count against the authoritative form of
PART 4.3; and no hard-coded unit noun anywhere disagreeing with the bound value,
per reference/output-contract.md PART 6.

**AND R5 NEVER SCANS ITS OWN RECORD, WHICH IS THE ONE EXCLUSION THIS GATE
PERMITS.** SD-FMT-27 and reference/output-contract.md PART 7.1. R5 is a STRING-SEARCHING
row: it scans the workbook for a hard-coded unit noun, and its own record has to
NAME THE NOUNS IT SEARCHED FOR or it is not auditable. Written into the Method
section, those terms are then found by the scan itself. **It was measured
elsewhere in this bundle: recording the searched terms took the raw occurrence
count from 22 to 44 and turned a passing gate into a failing one, so a run that
recorded its evidence failed and a run that hid its evidence passed**, which is
the exact inversion an audit trail exists to prevent. So, in this artifact:

- **THE FORMATTING MATRIX OCCUPIES A DECLARED CELL RANGE ON THE METHOD SECTION,
  AND THE METHOD SECTION STATES THAT RANGE**, in one line, beside the matrix.
- **EVERY STRING-SEARCHING ROW OF THIS GATE EXCLUDES THAT RANGE FROM ITS OWN SCAN
  AND SAYS IN ITS OWN RECORD THAT IT DID.** R5 is the row that has it today; any
  string-searching row added later is scoped the same way and for the same reason.
  The record states the terms searched, the count found, the result, and that the
  exclusion was applied.
- **THE EXCLUSION IS FOR STRING SEARCHES AND FOR NOTHING ELSE.** Element 16, the
  character gate, still reads EVERY cell of EVERY section including that range,
  because a character outside the permitted range is a defect wherever it sits and
  a character scan cannot be tripped by a record of itself. A row that reads a
  structural attribute is unaffected.
- **NO OTHER RANGE IS EVER EXCLUDED FROM ANY CHECK, and no range is ever excluded
  in order to pass.** The only permitted exclusion is a row's own record of its own
  search. A run that excludes a range to clear a failure has disabled the gate,
  which 18.4 already treats as a gate that did not run and therefore failed.

**WHAT THIS SKILL ADDS ON TOP OF THE MATRIX, because each of these is its own and
none is in the contract:**

- The SAMPLING DENSITY: a full walk of every populated cell on sections of
  FULL_WALK_ROW_LIMIT rows or fewer, SAMPLING_DENSITY above it, with the density
  stated on the record. SD-FMT-10.
- The IDENTITY BLOCK verified by header NAME and relative order across every item
  section, never by fixed column number, because the block's width changes with
  the requester's level. SD-CTR-08.
- The FREEZE POINT verified by finding IDENTITY_BLOCK_ANCHOR_COLUMN by NAME and
  by re-running the bounded walk of reference/output-contract.md 4.1.2 against the BUILT
  widths. **THE RE-RUN IS ONE WALK FOR THE ARTIFACT, FROM THE WIDEST CASE, AND A
  VERIFICATION THAT RE-RUNS IT PER SECTION REPRODUCES THE DEFECT IT IS CHECKING
  FOR:** read each identity column's MAXIMUM built width across every section
  carrying the full identity block, walk those, and compare the ONE anchor that
  yields against the freeze actually set on EVERY such section. **THE ASSERTION HAS
  TWO BRANCHES AND BOTH ARE ORDINARY**, so a check written for one of them fails a
  correct artifact built under the other: where the summed widest-case built width
  of the identity block is at or under FROZEN_SPAN_MAX_WIDTH, the anchor is the LAST
  identity column and the freeze column IS HDR_RANK_REASON's own column; where the
  bound truncated the span, the anchor is the last identity column the walk
  admitted, the freeze column is the FIRST IDENTITY COLUMN THAT DID NOT FIT, and the
  Method section carries the truncation record naming the bound, the summed
  widest-case width, the section supplying each widest case and the columns left
  outside by header name. **In both branches assert the same five things:** the
  summed widest-case built width of the frozen columns is at or under the bound OR
  the span is exactly one column; **every section carrying the full identity block
  freezes the SAME COLUMNS, by header name**; **no section freezes MORE identity
  columns than the widest-case walk admitted**, while a section using fewer width
  units for the same columns is a PASS and not a finding; HDR_RANK_REASON is
  OUTSIDE the frozen span on every section; and no free-text column sits inside it.
  **The Method section carries EXACTLY ONE record of the walk**, and a second one,
  or a per-section count of frozen identity columns that is not constant, is a
  FAILURE that blocks publication. An assertion that hard-codes either branch, that
  reads the anchor as the last identity column OUTRIGHT in every case, or that
  scores this row section by section against that section's own widths, is testing
  the wrong column. SD-CTR-08, SD-FMT-03.
- **THE TOTAL BUILT WIDTH OF EVERY GRID, against `GRID_MAX_TOTAL_WIDTH`.**
  reference/output-contract.md 2.7 and element 10, SD-FMT-28. For every entity section and
  for the reference table, sum the BUILT widths of every column read back through
  the engine and compare the total to the bound the build declared and recorded at
  17.3. **This is a SECOND bound and it never substitutes for the frozen-span
  bound**: one says what stays on screen, the other says how much there is, and a
  section can honour the first perfectly and still be ten screens wide. Three
  assertions, and the relief ladder itself is 2.7's and is not restated here: the
  value asserted against is the one DECLARED BEFORE THE COLUMNS WERE BUILT, so a
  bound that changed between the declaration and the measurement is a FAILURE and
  never a pass; **no column was dropped, no column sits below its own header floor
  and no meaning-carrying value was shortened**, which are 2.7's three things that
  never give and are checked directly rather than inferred from the total; and
  where any section is still over the bound after 2.7's ladder ran, the Method
  section carries the bound, the measured total, the overage and the columns
  accounting for it in DESCENDING built width, and the front panel carries the one
  line telling the reader that section is wider than the bound. **A section over
  the bound WITH that record is a PASS**, because an honest overage is 2.7's
  correct last outcome; **a section over the bound with NO record is a FAILURE**,
  because a silently over-wide section is indistinguishable from a broken one.
  **Verified under element 10, not as an element of its own**, per 2.7, since the
  total is a property of the widths element 10 sets.
- **THE FULL GRID, WALKED OVER THE SHEET'S USED RANGE AND NEVER OVER THE TABLE
  RANGE.** Element 7 and PART 7.2 row 7: every populated cell of a section's USED
  RANGE carries a thin border in COLOR_GRIDLINE on ALL FOUR SIDES, and the walk
  covers the header row, every data row, the explanatory row of PART 5.4, **EVERY
  NOTE-BAND ROW of PART 5.3 and EVERY POPULATED ROW OF BOTH PANEL SECTIONS**. A
  MERGED REGION is walked as ONE cell and its border is asserted on the OUTSIDE of
  the region, on all four outer edges, which is the form every note-band row takes.
  **THE BORDER COLOUR IS ASSERTED TOO**, on the floor PART 2.8 sets for a LINE,
  against the default sheet ground and against the header band, which is the
  darkest surface it is drawn over. **A WALK SCOPED TO THE TABLE BLOCK PASSES A
  SECTION WHOSE NOTE BAND HAS NO BORDER ON ANY SIDE**, and a check scoped more
  narrowly than the rule it enforces certifies the defect rather than merely
  missing it. SD-FMT-02, SD-FMT-29.
- **ALIGNMENT, INCLUDING THE THIRD CLASS.** Element 9 and PART 2.5: every column
  named in the bound right-align list is right aligned and no other is; **NO
  COLUMN ON ANY SECTION IS CENTRED**, because this artifact declares no STATUS GRID
  COLUMN and 1.10 records the declaration with its reason; every remaining column
  is left aligned; and the note band, being outside the table block, is not tested
  by this row. A centred column found on any section is a FAILURE and blocks
  publication, because a column centred at run time is exactly the run-time
  inference SD-FMT-05 forbids.
- **CONDITIONAL FILLS, CHECKED AGAINST 1.10's SECOND DECLARATION AND NEVER AGAINST
  ITS FIRST.** Element 13 and PART 2.6: the only conditional fill on any entity
  section of this artifact is the ALERT SHADING of element 13, in COLOR_ALERT_WARN
  and COLOR_ALERT_OVERDUE at the bands ALERT_BAND_THRESHOLDS gives, and there is no
  classification fill anywhere **because 1.10 declares no CLASSIFICATION COLUMN,
  per column, on 2.6's own conditions**. It is NOT because there is no status grid
  column: 2.5's centring test and 2.6's fill conditions are decoupled, this row
  reads only 2.6, and the alignment row above reads only 2.5. Both declarations are
  recorded as POSITIVE and SEPARATE statements in the matrix rather than as one
  absence. Any conditional fill found on an entity section other than the two alert
  fills is a FAILURE; so is a fill drawn from `CLASSIFICATION_FILLS` on a run where
  no classification column was declared. SD-FMT-27.
- **THE FILTER, AND THE MECHANISM IT IS SET IN.** Elements 3 and 6: the section
  carries a real table over exactly the populated block, and the filter is read back
  FROM THE SECTION of the built artifact, in the form the reader's engine looks for
  it, spanning every column, with EXACTLY ONE filter object over that range. **A
  filter found only inside the table object is scored ABSENT and is a FAILURE**, and
  so is no filter at all, and so are two filter objects over one range. Where the
  engine could not carry both a table object and a visible filter over one range,
  element 3 is recorded NOT APPLICABLE with the conflict named and this assertion
  still runs and still blocks publication. Per 17.3, SD-FMT-29.
- **THE NARRATIVE COLUMN'S WIDTH, IN WIDTH UNITS.** Element 11: its built width
  read back through the engine sits inside the bound range read as WIDTH UNITS and
  applied directly per PART 2.2 step 6, it is at or above that column's own header
  floor, and it is the WIDEST column on the section. A check that converts the
  bound before comparing is testing a different quantity and fails a correct
  section. Per 17.3.
- TITLE CASE on every heading, every SECTION NAME written to a tab and every COLUMN
  HEADER, in the one convention `TITLE_CASE_HEADINGS` states, with the single
  exemption of 1.10 applied and recorded with its reason: a string the ORGANIZATION
  BOUND ships in the case it was bound in. **The exemption for table column headers is
  withdrawn and a column header in sentence case is a FAILURE**, as is a tab name in
  sentence case and an authored heading that is not Title Case. A bound string
  re-cased away from its binding is a failure in the other direction. SD-FMT-13.
- **NO WORD BROKEN BY A CELL LINE**, asserted two ways, per PART 2.10 and SD-FMT-30.
  Every populated cell whose string needs more room than its own cell supplies is read
  back as a MERGED REGION spanning at least the columns that supply it; an unmerged
  cell overflowing its boundary fails, and so does a band whose cells share a fill
  without being merged. And every column's built width is at or above `T`, the longest
  unbreakable token it displays, recomputed from the header string and the built
  values. Where `T` exceeded the column cap, Method carries the over-long-token record.
- NO PARAGRAPH in a narrow label column on any panel section. SD-FMT-11.
- No blank or interpolated row inside any table, and every per-sheet note sitting
  in that section's NOTE BAND, per 1.6.1 and reference/output-contract.md PART 5.3:
  verified by reading back that the band begins exactly one blank spacer row below
  the table's last row, that each note is one row merged across the table's full
  column span from the table's first column, that it carries the panel label fill
  and the body font, **that it carries ELEMENT 7's BORDER on all four outer edges of
  its merged region**, that its height satisfies element 12 against the summed width
  of the merged span, and that the table range stops at the spacer row so element
  3 sees no populated data row outside it. A note found above a header row, inside
  a table range, or in a single column below the table is a FAILURE and blocks
  publication. SD-FMT-26.
- The checks stated in FALSIFIABLE ARITHMETIC on values the engine reports, never
  as "no cell clips". SD-FMT-09, SD-FMT-12.

## 18.3 Two verifiers are independent only when they answer DIFFERENT questions

SD-RUN-03. If two checkers both emit computed metrics, each does the same
arithmetic on the same cells, and their agreement proves only that they picked
the same columns. Independence is real only when the two methods answer
DIFFERENT questions: one answers what a column MEANS, from names and vocabulary;
the other answers what a column's DATA LOOKS LIKE, from distribution,
cardinality, range, null pattern and cross-file ratio behaviour. The arithmetic
is then done once, deterministically, by the orchestrator.

Never reconcile against a single ledger. SD-RUN-04. A single verifier produces
an UNVERIFIED result, which does not meet the standard for a record with
consequence.

Reconcile only what BOTH verifiers can independently emit. SD-RUN-05. Split
reconciled items into MUST MATCH EXACTLY and CORROBORATED, NOT MATCHED. For a
corroborated item, one verifier is authoritative and the other runs a REJECTION
TEST only. Demanding that two differently-instructed verifiers produce identical
semantic output is unsatisfiable and would hard-stop every data-bearing run.
Count UNRESOLVED only for items both verifiers actually emit or corroborate.

NOT REFUTED is not confirmation. SD-RUN-06. A rejection test is a necessary
condition, never a sufficient one. In the case that produced this rule the test
failed to refute eighteen of twenty deliberately WRONG pairings, since almost
any part is smaller than almost any whole. A test that can only catch a gross
error must never be reported as a confirmation.

A declared incompatibility outranks any corroboration verdict. SD-RUN-07.
Corroboration never overrides a declared rate or unit incompatibility.

A sparse population is not a mispairing. SD-RUN-08. A median of exactly zero
means the entity is thinly distributed, not mispaired. Report the zero share and
mark the verdict INCONCLUSIVE, never REFUTED.

Never average two disagreeing derivations, and never publish a disputed value.
SD-RUN-09. On disagreement, the authoritative side re-derives ONCE, showing its
work. Still refuted, mark UNRESOLVED and exclude that item's metrics. At or above
UNRESOLVED_STOP_COUNT unresolved items, stop. The threshold is named as a
variable and never written as a number in this file.

## 18.4 Fail closed

Unknown is not pass. SD-EFF-03. A gate that cannot be evaluated HAS FAILED.

A labelled partial is still a partial. SD-EFF-04. Partial output is never
delivered silently, and a partial that LOOKS FINISHED is never delivered at all.
If a section cannot be repaired, stop and publish nothing, name the section and
the exact ranks affected, and preserve the checkpoint. An artifact that is eighty
percent populated and silently published is worse than one that failed loudly.

A bannered partial that names what is missing is BETTER THAN NOTHING.
SD-EFF-05. Where a run has already spent the user's time and a blocking answer
never arrived, emit the appropriate blocks with INCOMPLETE_PLACEHOLDER_TEXT in
every field whose blocking input is missing, banner the whole output with
INCOMPLETE_BANNER_TEXT, name what is outstanding and which question resolves
each, exempt the placeholder fields from the gates that inspect content, and do
NOT delete the checkpoint.

The two are not in conflict. A silent partial that reads as finished is
forbidden. A partial that is unmistakably bannered, enumerates its own gaps and
cannot be mistaken for a finished document is the correct terminal state after a
long run with an unanswered blocking question. **The distinguishing test is
whether a reader could submit it by accident.**

---

# PART 19: STAGE 12, DELIVERY, THE REPLY AND THE AUDIT SECTION

## 19.1 The artifact

Named by OUTPUT_FILENAME_PATTERN, which must carry a scope LABEL, its
identifying CODE, the PERIOD and any QUALIFIER, so two runs never collide. Named
with the PLANNING entry of DELIVERABLE_NAME, which is a mapping per skill and
never a single shared string, per SD-CTR-30 and 1.2. Written to OUTPUT_DIR.

**Do not send or share the artifact automatically.** SD-CTR-18. Produce it, name
it, hand it over. Never mail it, post it or share it without being asked.

## 19.2 The reply

At most CHAT_REPLY_MAX_LINES. SD-CTR-16. It names: the scope and the period; the
source used; the mode in plain words; the priorities found, or plainly that none
were; the directed count; the top three with one line each; and the filename.
Anything else belongs in the artifact. NEVER paste the full list.

Where the run was degraded, the FIRST line of the reply names the count of
degradations and the single most consequential effect.

## 19.3 Order within the artifact

The items come first; everything explanatory goes after. SD-CTR-14. The opener
is a few lines, not a page. This governs order inside a section and inside the
reply, and does not reorder the sections.

Never open with methodology, caveats or reconciliation. SD-LNG-03. Those are
internal. The finding leads.

### 19.3.1 THE FRONT PANEL LEADS WITH THE ANSWER

The section ORDER is fixed and does not change: the front panel is first and the
Method section is last, per TAB_CONTRACT and SD-CTR-07. What was wrong was the
front panel's own INTERNAL order, which opened on methodology and left the reader
to reach the finding several sections later. A reader who opens the artifact and
lands on paragraphs of method sees PROCESS BEFORE ANSWER, which is the opposite
of what SD-CTR-14 and SD-LNG-03 promise and the opposite of what a busy person
needs. **The fix is the order of the front panel, not the structure of the
deliverable.**

The front panel is written in FIVE BLOCKS, in this order, and every block ships
every run:

**BLOCK 1: THE ASK. What you are being asked to do this period.** SIX lines
every run, plus a SEVENTH that ships only where its test fires; where more than
one mandatory column is uniform, that seventh line names them together rather
than multiplying. The three statements named at the end of this section, where
they apply, come BEFORE all of them and are counted separately, because in each
case the ask itself would otherwise be misread. Nothing else may precede the
block, including a title band's worth of methodology. It carries, and carries
nothing else:

1. **THE REPORT TITLE**, then the scope in the reader's own words, then the
   PERIOD this plan covers, as dates. **The title lives HERE and nowhere else in
   the artifact.** reference/output-contract.md element 1 puts the header row of every item
   section in row 1 with nothing above it, so there is no banner row for a title
   to sit in on any section and there is never going to be one. This is the line
   a reader looks at to know what document they are holding, and it is the first
   thing on the first section for that reason. SD-FMT-22.
2. What to act on: the count on the first action list, the count on the second,
   and the count on the directed section, each as a number the reader can hold.
3. The count of items falling due BEFORE this plan starts, per 12.3.1 state 6,
   because it changes what the reader does THIS WEEK rather than next period.
   The count is the ask; block 2 is the list behind it.
4. The total ranked population N, so the counts above have a denominator.
5. One line naming the top three units and why each is there, one clause each.
6. **THE COMMITMENTS-IN-WINDOW LINE, and it ships every run.** How many of the
   reader's own commitments fall INSIDE the window this plan covers, and WHERE
   EACH OF THEM SITS. This is the question a real reader asks first, and it is
   not the one the section-level ordering note answers: that note counts rows on a
   section that fall outside the window, and this line counts the window's own
   commitments that landed outside a section. A commitment inside the window
   sitting at a rank deep in the reference list is correct, is disclosed on its
   own row, and is still a fact the reader must be TOLD rather than left to
   discover. Its standing form is:

   > `{m} of your {unit singular|unit plural} {has|have} a commitment date
   > inside {the planned window, as dates}: {a} on the first action list, {b} on
   > the second, {c} on the reference list, {d} on the directed section, and {e}
   > on no published section. The furthest down sits at rank {r}. Every one of
   > them is named with its rank in the Method section.`

   Membership is exactly state 1 of 12.3.1 over the whole ranked population, and
   nothing else is tested. Where any row is in state 2, named for this window with
   a date that could not be read, the line carries one further clause,
   `Plus {k} more named for this window whose {date|dates} could not be read`,
   because those
   are commitments the reader also owns and the artifact must not lose them in a
   rounding of the question. Where m is zero the line still ships, in this form:
   `No {unit singular} of yours has a commitment date inside {the planned
   window}; the {n} {row|rows} on this plan {is|are} ordered by score, and the
   {HDR_CLOSE_STATE} column says when each one falls.` The counts reconcile exactly against the
   section row counts, and the Method section lists every one of the m rows with
   its rank and its section, exactly as the do-this-week block lists its own.
7. CONDITIONAL, and it ships only where the test in 1.3b fires: the
   UNIFORM-COLUMN LINE. **ONE LINE, HOWEVER MANY COLUMNS AND HOWEVER MANY SECTIONS
   FIRED**, because block 1 is a closed enumeration and a line is never invented
   into it, and because the same finding said twice is not two findings.

   **THE COMPOSED FORM, WITH BOTH LISTS VARIABLE, STATED ONCE HERE BECAUSE TWO
   RULES OTHERWISE GIVE TWO SHAPES FOR ONE CASE.** 1.3b's test runs per COLUMN over
   two populations and names the SECTIONS; this line reads per LINE and names the
   COLUMNS together. A run with two uniform columns across three sections had no
   stated form to write. It has this one:

   > `{n} {column|columns} on this plan {carries|carry} the same value on every
   > row {it is|they are} shown on: {for each column: the column's header, what
   > every row says, and why}. {Where a column is uniform over the whole ranked
   > population: "on every section."} {Where it is uniform on some sections only:
   > "on {the named sections}."} To fill {it|them}, bind {the named bindings} or
   > supply {the named sources}; until then the ranking is unaffected.`

   **TESTED AT ZERO, AT ONE AND AT MANY, per SD-LNG-13**, like every other
   templated sentence in this file. **At ZERO the line does not ship at all**, which
   is the conditional in the enumeration and is the ordinary case; nothing is
   printed saying no column was uniform, because block 1 carries findings and not
   the absence of findings, and the Method section records that the test ran and
   found none. **At ONE** the clause list has one member and the plural forms take
   their singular branch, so the line reads exactly as the single-column form
   below. **At MANY** the clause list carries one clause per column, in the column
   order the section's own contract gives them so two runs order them identically,
   and each clause carries its OWN section list, because two columns can be uniform
   on different sections and merging their section lists would assert something
   neither test found. **The section list itself is tested the same three ways:**
   uniform over the whole ranked population takes the whole-population branch and
   never lists sections; uniform on one section names that one; uniform on several
   names them in TAB_CONTRACT order.

   Its standing form for the action column, which is the case that produced the
   rule and which is the one-column reading of the form above:

   > `No source in this file supplied an action for any row. {The sources that
   > were read} were read and {the sources that could not be reached} could not be
   > reached. To fill the {HDR_ACTION} column, bind {the named bindings} or supply
   > {the named source}; until then the ranking is unaffected and the next step on
   > every row is yours.`

   Saying it once, at the top, is what makes forty identical cells legible instead
   of alarming. The cells still carry their value, the column still ships at full
   width per SD-FMT-21, and the Method section still carries the full entry with
   the bindings, their owner and their contact.

**BLOCK 2: DO THIS WEEK. The items that fall due BEFORE this plan starts.** This
block is A VIEW OF THE RANKED LIST AND NOT AN ADDITION TO IT, and it ships every
run.

Membership is exactly state 6 of 12.3.1 and nothing else is tested: a date on or
after the run date and before the planned window opens. It is drawn from the
WHOLE ranked population N, directed units included, because the reader owes that
work whichever section the row was routed to. Those rows are already
ranked, already published and already banded at the floor weight by 12.3, and
that banding is correct, because the plan is about a later window. The reader
still has to act on them THIS WEEK. A count buried in a line of the ask is not an
action; the rows are.

- **No re-ranking, no re-weighting, no membership change, no exception.** Not one
  weight, rank, score, count, cap, percentile or section membership moves because
  this block exists. Every figure elsewhere in the artifact is byte for byte what
  it would be without it. This block SURFACES A SLICE OF THE RANKING; it does not
  alter the ranking. SD-RNK-01 is untouched.
- **Every entry names the RANK the row holds and the SECTION it sits in**, so the
  reader can find it in place rather than hunting for it. One line each, in the
  panel family's label and prose columns per SD-FMT-11: the rank, the unit as the
  identity block names it, the date from HDR_COMMITMENT_DATE, and the exact state
  6 row wording from 12.3.1. Where a row's rank falls BEYOND every published
  section, the entry says so and still gives the rank, because the work falls due
  this week whether or not the row made a list.
- **THE ANTI-DOUBLE-COUNT LINE SHIPS EVERY RUN, immediately under the block
  heading, in these words:** `Every row here also appears at its rank in the lists
  below. This is a view of the same list, not extra work.` A reader who adds this
  block to the action lists and gets a number larger than the plan has been
  misled by the artifact's own shape, and one printed line prevents it. It is
  printed even when the block holds one row.
- **Ordering:** the date ascending, then the rank ascending, then the unit
  identifier ascending, which is the total order SD-RNK-10 requires so two runs
  on one file agree.
- **Cap:** the first action section's own size in force on this run, its
  tier_1_size, which is a value already bound for this run rather than a new one.
  Where more rows qualify, publish that many and write the showing note in the
  standing form every capped thing in this file uses, `showing {n} of {m}
  {item|items} falling due before this plan starts`, and name the remainder by count in the
  Method section. Where fewer qualify, carry them all and write no note, because
  there was no shortfall. SD-RNK-06.
- **Both empty cases ship a line rather than nothing, and they are different
  facts.** Where no row is in state 6, the block carries one line saying that
  nothing falls due before this plan starts. Where the planned window IS the
  current window, state 6 is empty BY CONSTRUCTION per 12.3.1, and the block says
  that instead, so a reader is never left wondering whether the test ran.

**BLOCK 3: WHAT CHANGES HOW TO READ THESE NUMBERS.** At most TWO entries, and
the selection is arithmetic rather than judgment, using the same cost test the
deferred-binding budget uses. A disclosure qualifies for this block ONLY IF IT
CHANGED A PUBLISHED THING: a number, a membership or an ordering that appears in
this artifact. Rank the qualifying disclosures by HOW MANY published rows, ranks
or figures each changed, descending, with the section order as the tie-break so
the selection is reproducible. Lead with at most the top two. Each is written in
the three-part form of PART 21: what was unavailable or unbound, what it CHANGED,
and what the reader should do about it.

Where NOTHING qualifies, this block ships one line saying that no missing
capability or unbound value changed any number in this report, which is a real
statement and is the evidence the test ran. SD-EXC-06.

**BLOCK 4: WHAT IS IN THIS ARTIFACT AND HOW TO READ IT.** The section map with
ACTUAL row counts, the column glossary, the alert line printed every run
including when both counts are zero, and the population funnel.

The column glossary carries, in the reader's words, per 19.3.2: the carried
context block introduced as CARRIED, NOT SCORED per 1.3d; a one-line gloss for
every header corrected under 1.3e, naming what the number counts; a one-line
gloss for the timing pair, saying that the score combines size with how soon the
commitment date falls and that the timing weight is how much the date
contributed; the action column, saying where an action comes from and that
MSG_NO_ACTION_DERIVED means the sources named none rather than that the row needs
no work; the measure's unit, named ONCE here from MEASURE_UNIT_TOKENS rather than
repeated in every cell, per 1.3b; and the line required by 1.3c for every
degenerate-constant column omitted, naming the column, the constant marker it
would have carried and the binding that would populate it.

**BLOCK 5 IS THE CATCH-ALL, SO NO REQUIRED LINE IS EVER HOMELESS.** Where any
rule in this file requires a statement on the front panel and names no block, it
belongs to block 5, in the order those rules appear. Blocks 1 and 4 are closed
enumerations and a line is never invented into them, but a required disclosure is
never dropped for want of a slot either: block 5 takes it, and the Method section
carries it in full as it always did.

**BLOCK 5: EVERYTHING ELSE, UNDROPPED.** Every remaining disclosure that did not
reach block 3, in its existing order: the shape decision and how it was reached,
the cold-start test results, the exclusion decision with every distinct value
under EXCLUDED and KEPT, the provisional label where one applies, every remaining
degradation, every remaining unbound-value notice, the method-owner statement and
the contact line.

**THE RULE THAT GOVERNS THE WHOLE REORDER: MOVING A DISCLOSURE LATER IS
PERMITTED, AND REWORDING ONE FOR ITS AUDIENCE IS PERMITTED; DROPPING ONE IS
NOT.** Every line that was in the front panel before is still in the front panel.
Nothing moved to the Method section, nothing was summarized away, and no notice
was softened. Block 3 does not REPLACE the disclosures, it PROMOTES two of
them. The rule that a degradation is announced at
the same prominence on every run until it is bound still holds: prominence is
satisfied by the front panel, and blocks 3 and 5 are both the front panel.

Three failsafes that survive verbatim and are checked at the final gate:

- Every announcement still appears in all THREE places: the front panel, the
  Method section, and the first line of the reply. reference/capability-probe.md PART 4.
- A provisional run's label still appears at the SAME PROMINENCE every run, and
  it sits in block 1 rather than block 5, because it changes what the whole
  artifact is.
- Where a population is below MIN_POPULATION_FOR_RANKING, or the unit of business
  is coarser than the reader's scope, or the population is COLD, those statements
  come BEFORE the content and therefore sit in block 1, per 11.7.1, 11.7.2 and
  14.8.6. Those three are the only statements that outrank the ask, because in
  each case the ask itself would otherwise be misread.

### 19.3.2 THE FRONT PANEL IS WRITTEN FOR THE READER; THE METHOD SECTION IS WRITTEN FOR THE BINDING OWNER

Both carry every disclosure. They differ in WORDS, never in CONTENT.

The defect this closes: a front panel that discloses everything honestly in the
vocabulary of the people who maintain the method. Cold-start detection.
Tie-broken. Bare denominator. Provisional binding. Degenerate column. Shape
inference. Rung three. Every one of those is exact, and to the person holding the
plan, none of them names a thing they can do. A disclosure the reader cannot act
on has been made to the file rather than to the reader, and the reader is who the
front panel is for. SD-LNG-03 and SD-CTR-14 put the answer first; this puts it in
the reader's language.

**THE RULE.** Every line of blocks 1 through 5 is written so that a person who
has never read this file, this method's vocabulary or the schema can act on it.
Each keeps the three-part form of PART 21: what happened, what it CHANGED on the
list in their hands, and what they can DO about it. A term of this method never
appears at a reader without its meaning in the same sentence.

**NOTHING IS DROPPED, AND THE TECHNICAL FORM SURVIVES WHERE ITS AUDIENCE IS.**
The variable name, the exact degradation notice from reference/schema/ A1 or A2,
the doctrine ID, the concept key, the rung number and the test that decided a
branch all keep their exact form in the METHOD section, per 19.4, which is the
part written for the binding owner and the reviewer. Where the binding owner also
needs the technical name in the front panel in order to act, it is RETAINED, in a
trailing clause AFTER the plain sentence, never in place of it. The test is
one-for-one: every disclosure present in the front panel before this rewrite is
present in the front panel after it, and the audit is unchanged in every respect.

**THE BOUNDARY AGAINST SD-LNG-07, and it matters.** SD-LNG-07 says use the
ORGANIZATION'S exact vocabulary and never paraphrase a term of art, and it is
untouched here. The organization's words ARE the reader's words and are never
translated, softened or replaced. What is translated is THIS METHOD'S OWN
vocabulary, which is nobody's term of art and belongs to the people who maintain
the method rather than to the person holding the plan.

**Worked translations. Neutral, and the pattern generalizes; the left column is
what the Method section keeps, the right column is what the front panel says:**

| Written for the binding owner, kept verbatim in the Method section | Written for the reader, in the front panel |
|---|---|
| Cold start detected: no prior-period column resolved, so the independence test could not run | There is no earlier period in this file to compare against, so everything below is measured inside this period only, and nothing here claims a trend |
| Ranks 14 and 15 tie-broken on the unit identifier ascending, per SD-RNK-10 | Two rows scored exactly the same, so they were put in identifier order; which of the two comes first carries no meaning |
| The share is published as a bare denominator, per the small-population rule | This share is out of {n} units, singular where the count is 1, not a large population, so read it as a count rather than as a percentage |
| EXCEPTION_FLAGS is unbound; the standing set for this shape was applied with its standing weights | Nobody has told this method which problems your organization wants flagged, so a standard set was used; ask {BINDING_OWNER_NAME} to set yours, and the flags used are listed in the Method section |
| The measure resolved at tier 2; it is a proxy for the intended measure | The number this list is ordered by is {name}, which is a stand-in: the one normally used was not in the file |
| Population shape resolved to FLOW on test two | These rows are items moving through stages rather than a standing list of units, so time here means time sitting in a stage |
| A degenerate-constant column was omitted under 1.3c | One column would have read the same placeholder on every row, so it was left out; it was {column}, and setting {binding} would fill it |
| Rank and Scope rank coincided on all rows; one column shipped | Your scope is the whole list in this report, so the rank and the rank inside your scope are the same number, and one column carries both |
| The measure sits at the 100th percentile | It is the largest in this list, named with any tie, and the figure is printed unchanged beside it. The rule is SD-LNG-12 and it is stated once, in 11.7.3; this row is the same rule seen from the reader's side |
| HDR_MUST_CLOSE holds 0 | Nothing on this row is certain to close inside the window this plan covers. It is a count, not an instruction, and a zero is not a reason to skip the row |

The self-check, answered before publication and recorded beside the PART 21 one:

> Could the person this artifact is addressed to act on every line of the front
> panel without knowing one word of this method's vocabulary, and does the Method
> section still let a binding owner find the exact variable, notice and test
> behind each of those lines?

Both halves have to be yes. A yes to the first alone means something was dropped;
a yes to the second alone is the defect this rule closes.

## 19.4 The audit section is exhaustive BY DESIGN and sits at the VERY END

SD-CTR-15. It is complete to the point of tedium and it is placed LAST, after
the lists, where it costs a hurried operator nothing but lets a skeptical
manager reconstruct every number. The tension between brevity for the operator
and auditability for the reviewer is resolved by PLACEMENT, not by omission.

The ordered specification. Every run, every item, even when the answer is none:

1. The probe record in full: every capability, its state, the evidence, and the
   rung taken. Plus every degradation, on its own line, naming what was
   unavailable, what it changed, and what the reader should do about it.
2. Unbound and declined bindings, **in two parts, because a verbatim list of
   every one of them is between one and three hundred notices on a first run and
   nobody reads it**:

   **2a. IN FULL, VERBATIM: every unbound or declined binding that CHANGED A
   PUBLISHED NUMBER.** A binding changed a published number where its documented
   default altered membership of any list, any rank, any score, any count, any
   percentile, any weight, or any figure printed anywhere in the artifact. Each
   gets its exact degradation notice from reference/schema/ SECTION A1 or A2, the
   name and address of the binding owner who can set it, and one line naming WHAT
   IT CHANGED. This part is never summarized, never capped and never abbreviated,
   however long it runs, because these are the notices that explain the numbers on
   the page. On a typical first run it is a handful of entries, not a hundred.

   **2b. BY COUNT, WITH THE LIST AVAILABLE ON REQUEST: every other unbound or
   declined binding.** These are the ones whose default changed nothing that was
   printed: a formatting constant, a label, a feature that was not reached, a
   threshold for a section that had no members. Give the COUNT, grouped by schema
   group with a group name and a count each, one line per group, followed by the
   single sentence that the full verbatim list of all of them is available on
   request and how to ask for it. Naming the groups matters: a reader scanning
   them can see that thirty of the forty sit in formatting and stop worrying.

   **THE TEST IS MECHANICAL AND IT IS NOT A JUDGMENT CALL.** Did the default
   change a number, a membership or an ordering that appears in this artifact? Yes
   goes in 2a, no goes in 2b. Where it cannot be determined, it goes in 2a. A
   binding is never moved to 2b to shorten the section, and the two counts always
   reconcile to the DENOMINATOR defined immediately below, which is also printed.

   **THE DENOMINATOR IS DEFINED, AND IT IS TAKEN FROM THE APPENDIX RATHER THAN
   REMEMBERED.** "Used this run" was undefined and is not a decidable question: a
   planning run never reaches the review form's variables at all, so a run must
   either count variables it had no contact with or decide per variable whether a
   threshold that never fired was reached, and neither is checkable. **THE
   DENOMINATOR IS EVERY DEFERRED VARIABLE IN THE SCHEMA, WHETHER OR NOT THIS RUN
   REACHED IT, LESS THE ONES THIS RUN BOUND.** That is decidable, it is the same
   number every run at one organization, and 2a plus 2b reconcile to it exactly.
   Two rules make it checkable rather than asserted:

   - **THE COUNT IS READ OFF reference/schema/ SECTION A1 AND A2 AT RUN TIME, ROW
     BY ROW, GROUP BY GROUP, AND IS NEVER RESTATED FROM MEMORY.** A count restated
     from memory is the exact defect that appendix's own maintainer note warns
     about repeatedly. The run prints the per-group counts it read, so the total is
     reproducible by anyone holding the same appendix, and it reconciles its own
     total against that appendix's COUNTS block, naming any difference and its
     stated cause rather than silently preferring one figure.
   - **VARIABLES THIS RUN NEVER REACHED ARE COUNTED IN 2b AND ARE NAMED AS SUCH**,
     with their count, in one line. They belong to features this skill does not
     run, their defaults changed nothing here by construction, and saying how many
     of the total they are is what stops a reader reading a large denominator as a
     large number of unmade decisions about THIS artifact.

   The reason for the split is that exhaustiveness in this section is a means, not
   an end. SD-CTR-15 places the audit last so completeness costs a hurried reader
   nothing, but two hundred verbatim notices cost a SKEPTICAL reader everything:
   the twelve that explain the numbers are buried among the hundred and eighty
   that do not, and the section stops being auditable in the only sense that
   matters. Nothing is deleted here. Everything remains retrievable. What changes
   is which part of it is printed by default.
3. Sources checked: every location, every folder, every window, with counts.
4. Identity and scope resolution: the title read, the token that decided the
   role, the level resolved, the code as given and as padded, and the tie-break
   used if any.
4a. The commitment-date column, per 1.3b: the concept that resolved it, the
    literal source column name, the header string used and whether it was the
    documented default, the counts of rows dated by rule 1, by rule 1b and by
    rule 2 reported separately per SD-LNG-04, the count of cells left blank with
    the state 9 rows named, and the open request against the shared schema naming
    HDR_COMMITMENT_DATE and what it heads.
4b. The carried context block, per 1.3d: every candidate column with its fill
    rate and distinct-value count, which six were carried and in what order,
    which were not carried and why, and the phrase CARRIED, NOT SCORED beside
    them. Plus every degenerate-constant column omitted under 1.3c, with its
    constant marker, the binding that would populate it, that binding's exact
    degradation notice, and the owner who can set it.
4c. The do-this-week block, per 19.3.1 block 2: the state 6 count, every row it
    carried with the rank and section that row holds elsewhere, the cap and the
    showing note where one applied with the remainder named by count, and the
    statement that no weight, rank, score, count or membership changed because the
    block was published.
4d. The rank-coincidence line, per 1.3b: which way the test went, on how many
    rows of how many, and which column shipped.
4e. The close-state column, per 1.3b and 12.3.1: the count of rows in EACH of the
    states in 12.3.1, named apart from one another, the short label used for each, the
    weight each contributed, and the ordering note as written on each ranked
    section with its {k} of {n} {figure or figures, selected on n}, per SD-LNG-13.
4f. The action column, per 1.3b: the count of rows whose action came from a
    directive, from a compliance requirement and from a work item, reported
    separately; the count carrying the standing absence text; every direction held
    back by the compliance gate that therefore supplied no action, with the reason;
    and any action text compressed to fit its field, carried here in full and
    verbatim per SD-LNG-11.
4h. The commitments-in-window figures, per 19.3.1 block 1: the count in state 1
    over the whole ranked population, the split by section, every one of those
    rows named with its identifier, its rank and the section it sits on, the count
    in state 2 where any, and the reconciliation of the split against the section
    row counts.
4i. The uniform-column findings, per 1.3b and SD-FMT-21: every mandatory column
    whose cells all held one value, the value, the count of rows, the sources read
    and the sources that could not be reached, the bindings that would fill it
    with owner and contact, and the statement that the column shipped rather than
    being removed.
4j. The second-section coverage figure, per 1.6: the rows on the two action
    sections as a share of eligible_count, whether the more-than-half test fired,
    the sentence it added, and the question raised with the binding owner with the
    answer or the silence recorded.
4g. The header verdicts, per 1.3e: every header CORRECTED, with the string
    shipped, the A1 string it replaced and the question it failed; every BOUND
    header that failed the test, with the note that the organization's string
    shipped unaltered; and every correction raised as an open request against
    GROUP 24, together with the note that the three headers this file once
    declared locally are now schema-owned and their earlier requests are closed. Plus the alignment check of 1.10, column by column: every column
    this run emitted, its shape token, the side it took, and the confirmation that
    the two token sets are exhaustive so no column was left to judgment.
4k. The ENRICHMENT JOIN, per 10.1.1 and SD-PRS-48: every readable file in the
    input set with the verdict JOINED or READ AND NOT JOINED; for a joined file,
    which LIMB admitted it, the key used, the columns added with the concept or the
    shape token each carried, the MATCH RATE as matched of ranked, and the unmatched
    count on EACH side; for a refused file, the condition that failed and the terms
    that went unevaluated as a consequence; and the row-count assertion before and
    after, which are equal. Plus every column ADOPTED PROVISIONALLY under
    reference/field-resolution.md 7.4a, with the six tests' results, its fill share, the
    runner-up it beat or the statement that there was none, and every feature it
    fed, exactly as 7.4a's disclosure list requires; and beside each figure that
    adoption fed, the one line 7.4a requires there as well. **Plus every SIBLING SET
    adopted under reference/field-resolution.md 7.4b, as ONE entry and never as N adoptions**,
    with everything 7.4a requires per column and 7.4b's four further items: the
    MEMBER SET with its source, its date, its originator and the words that it was
    ADMITTED this run; the FULL member-to-header mapping, one row per member,
    INCLUDING EVERY MEMBER THAT GOT NO COLUMN, named as such; any column struck at
    7.4a test 6 and why; and any aggregation applied, with the rule and where in the
    admitted source it is stated, or the statement that none was applied because the
    source stated none, beside the per-unit answer that was not attempted. Where a
    sibling set was CONSIDERED and refused, the columns that tied, the member set
    considered, and which of 7.4b's five tests failed. Every figure the set fed is
    listed PER MEMBER, because a reader who sees N answers must never be left to
    read them as the whole standard.
4l. The CREDITABLE-ENTITY COLUMN, per 12.8: the column the concept resolved with
    its coverage of CREDITABLE_ENTITIES, the runner-up with its coverage, the
    threshold and margin applied, and which of the two the run used. Where nothing
    resolved, the statement that `entity_weight` took the stated neutral of 1.0 on
    every row, with the candidates and their coverages named, so a reader can see
    that no unit was ranked up or down by entity rather than inferring it from a
    term that appears not to move.
4m. The FROZEN SPAN, per 1.3 and reference/output-contract.md 4.1.2, **as ONE ENTRY FOR THE
    ARTIFACT and never one entry per section**: the bound in force, the summed
    WIDEST-CASE built width of the frozen span, which section supplied the widest
    case for each identity column walked, the single anchor column by header name,
    and either the identity columns left outside the span by header name or the
    statement that the whole identity block is frozen on every section. Plus, where
    any section does not carry the whole identity block, that section named with
    the identity columns it lacks. Plus the DECLARED CELL RANGE
    the formatting matrix occupies, per 18.2, and the statement that every
    string-searching verification excluded it.
4n. The GRID TOTAL WIDTH record, per 17.3 and reference/output-contract.md 2.7: the value of
    `GRID_MAX_TOTAL_WIDTH` DECLARED BEFORE THE COLUMNS WERE BUILT, the measured
    summed built width of every entity section and of the reference table, and,
    for any section over the bound after 2.7's relief ladder ran, the overage and
    the columns accounting for it in descending built width. Where the ladder moved
    a standing qualifier to the legend, the code, its full wording and its legend
    row. Where no section exceeded the bound, that is stated in one line, because a
    bound whose measurement is invisible is indistinguishable from a bound nobody
    checked.
5. Source parsing: the container selected with its score and record count and
   the runner-up's; the header row chosen and its runner-up; every concept
   resolved and how; every header that did NOT resolve, by literal text; every
   concept resolved and EMPTY; every ambiguous resolution with both candidates
   and who decided it; every concept left UNRESOLVED that a named decision needed,
   with the decision it cost and the closest candidate with the test it failed;
   every stem proposed for promotion.
6. The population funnel: two numbers per step, both measured inside the scope
   as it stood, reconciling exactly. N and eligible_count published separately.
7. The measure: which tier resolved, the exact column name, its unit, its time
   basis, and its scale read from its own maximum.
8. The work-item inventory: the block boundary and how it was anchored, the
   count of items, and the count carrying an originator prefix.
9. Local-tag detection: how many items carried a scope tag, how many were direct
   and how many broader, and what the prefix test compared.
10. Work-type weighting: the count per type, every item that fell to the
    baseline BY NAME, and every fixture mismatch.
11. Close-date derivation split BY RULE, with the count dated by each rule
    separately, SD-LNG-04, AND the count in each of the nine close-date states in
    12.3.1 reported separately, with states 6, 7 and 8 named apart from one
    another rather than merged into one floor-band figure. The four anchors are
    printed as dates: the run date, the current window, the planned window and
    the near horizon.
12. Every item that took a fallback close weight and the weight it took, and
    every item weighted zero, by name and count.
13. Priorities: every source, every level of the chain including levels that
    published nothing, every message classed as direction with sender and date
    and the wording quoted verbatim, the matched tokens per item, the
    family-level and specific-level mention counts, and every priority held back
    or dropped, with the reason. Plus, per 8.7.1, the ACTOR TEST for every
    direction that carried no addressing evidence: the rung of the ladder that
    resolved it, the actor it resolved to, the resulting classification, and the
    count of directions classified ASSIGNMENT and UNIDENTIFIED, each named
    separately, together with the statement that none of them took
    MANDATORY_MULTIPLIER or reached the directed section. Plus, per 8.8.1, every
    predicate with the ROUTE of test 2 that resolved its attribute and the column
    it reached, and every admitted direction that could not be evaluated with the
    reason, RECONCILED against the rows carrying the same statement on the
    priorities section, which is where that statement is primary.
14. The compliance findings, per jurisdiction, with the finding and its effect.
15. Exclusions: counts removed, counts readmitted per escape, and the threshold
    used, with the step 4 median and the step 7 median NAMED SEPARATELY. Plus the
    RECENCY MEDIAN RECONCILIATION, which is a RECONCILIATION AGAINST ITS PRIMARY
    LOCATION AND NEVER A SECOND COPY OF IT, per 16.4 and reference/output-contract.md PART
    5.2: it repeats the median, the count of rows that entered it and the counts
    excluded as future-dated, as blank and as unparseable, AND asserts that each
    equals the figure in the exception section's own note band, and a disagreement
    blocks publication.
16. The scoring formula written out in full, every constant named, and a WORKED
    EXAMPLE taken end to end so a reader can recompute one unit by hand.
17. Overrides applied: the steer mode, the weight matrix in full, the requested
    size and its split, and any qualifier.
18. The formatting pass matrix, per section, with the sampling density where the
    check was sampled.
19. Known limitations, and the method-owner statement plus the contact line.

## 19.5 The contact line and the invitation to tune

SD-CTR-19. Every artifact carries METHOD_OWNER_STATEMENT and MSG_AUTHOR_LINE:
two sentences in plain business language, free of jargon, stating what the
method computed from the user's own data, what was supplied as a binding, and
how to reach BINDING_OWNER_NAME, in the exact form MSG_AUTHOR_LINE gives it:
at BINDING_OWNER_CONTACT where an address is bound, and where none is, naming the
owner and stating plainly that no address is recorded, never an empty placeholder
and never an omitted line. BINDING_OWNER_CONTACT is DEFERRED, so an unbound
address is a disclosed gap on its own line and never a provisional run. Plus
TUNING_INVITATION. A user who opens the file months from now still knows who to
ask and what is adjustable.

**The method is built to be calibrated, and local reality is an INPUT rather
than a guess.** SD-CTR-20. Everything the method can compute from the data, it
computes at run time. Everything it cannot infer is left as an input. A wrong
assumption stated confidently is worse than a stated gap. That sentence is the
design principle the whole binding schema exists to serve.

## 19.6 Language

Measure impact; do not judge the remainder. SD-LNG-01. Use
IMPACT_LANGUAGE_RULE. Every unit matters to the person who owns it; this method
measures which units carry the most business impact, and that is a MEASUREMENT,
not a judgment about the rest. The ranking already communicates priority;
commentary that ranks units against each other in words is editorializing.
BANNED_PHRASES holds the phrasings that must never appear. Write toward impact,
never toward shame.

Use the organization's exact vocabulary. SD-LNG-07. CONTROLLED_VOCABULARY terms
are used exactly as the business writes them, never paraphrased.

Refuse to rank or evaluate PEOPLE. SD-LNG-02.

## 19.7 Never fabricate

SD-CNF-07. Never invent a unit, a number, a date, a target, a priority or a
quote. Quote priorities VERBATIM with sender and date. Never emit a rank, score
or benchmark you could not compute: leave it blank with a stated reason.

> A visibly missing number is recoverable; a fabricated one is not.

Every number traces to a cell or a tool result; everything else is a bracketed
placeholder NAMING ITS SOURCE. SD-CNF-08.

Every inference carries a CONFIDENCE, and confidence decides whether you PROPOSE
or ASK. SD-CNF-01:

- HIGH, evidence unambiguous and pointing one way: propose it and ask for a
  light confirm.
- MEDIUM, a competing reading exists: present BOTH readings and ask which.
- LOW, thin, conflicting or absent: do NOT propose prose. Ask an open question.

> LOW CONFIDENCE NEVER BECOMES A SENTENCE. It becomes a question.

An agent that writes a confident sentence from thin evidence produces exactly
the plausible-sounding filler that makes a reviewer distrust the whole document.
Calibration, all three from the same shape of evidence: one clear reading is
HIGH; two live readings both supported is MEDIUM; nothing correlating above
chance is LOW.

Ask plainly when unsure. SD-CNF-02. "Did this actually happen" is a better
question than a confident wrong sentence. Users correct a draft far more readily
than they catch a fabrication that reads well.

Confidence is RECORDED, not just used. SD-CNF-03. Every candidate carries its
confidence into the checkpoint and into the verification list, so a MEDIUM
inference the user confirmed is distinguishable later from a HIGH one that never
needed confirming.

The proposal state machine, and silence defaults to REMOVED. SD-CNF-04.
Inference sets everything to PROPOSED. Drafting accepts any state, because
confirmation is a POSTCONDITION of the confirmation stage, never a PRECONDITION
of the drafting stage. The confirmation stage resolves every proposal to
CONFIRMED or REMOVED, and a proposal whose question was skipped or never fired
is REMOVED, not carried forward. Re-assembly strips every REMOVED proposal,
deleting the clause it produced, and a removed action clause leaves the result
standing on its own rather than leaving an unconfirmed action in the text.
Silence defaults to REMOVED, not to CONFIRMED, and that asymmetry is the whole
point.

Correlation is weak evidence for causation; present diagnoses as CANDIDATES.
SD-CNF-05. Here is what stands out, does this ring true.

Never invent an action. SD-CNF-06. Where no evidence correlates to an outcome,
emit the result WITHOUT an action clause and route it to an open question. Retry
once with a widened set, then proceed without the clause.

Show the person the whole thing before it is final where the run is
interactive. SD-CNF-09. Flag inline every statement resting on a MEDIUM or LOW
inference, every superlative and its tie count, and every remaining placeholder.
Offer the out: anything here you would remove or soften.

Never present incomplete work as finished, in chat or in the file. SD-EFF-32. In
conversation, never say the findings are ready; say the crawl is done, then ask
the questions.

---

# PART 20: FAILURE HANDLING, GATES, RETRY AND SCALE

## 20.1 The stop list is CLOSED and enumerated, and HARD_GATES is ONE variable with a PER-SKILL SHAPE

SD-EFF-02. Only a gate named in HARD_GATES stops a run. Fatigue, run length,
retry count and output size are explicitly EXCLUDED and never will be members. A
missing central source is explicitly NOT a stop, and neither is reading the
published standard, per SD-SRC-21.

**The count of gates is stated in exactly ONE place.** A document that says five
in one section and ten in another has an internal inconsistency that will be
resolved differently by every reader. That lesson was recorded and then the
bundle reproduced the defect at BUNDLE scope: one shared organization variable
with a different standing set declared in each skill, so a binding owner who
binds it once cannot satisfy every skill, and a binding owner who leaves it
unbound gets a different closed set depending on which skill is running.

**This section owns the reconciliation. What follows is the convention, and the
other two skills conform to it as written.**

### 20.1.1 THE HARD_GATES CONVENTION

HARD_GATES is ONE organization variable and it is a TAXONOMY of FOUR KEYED
GROUPS. It is never a flat list again.

    HARD_GATES:
      shared:    [ gate, gate, ... ]     enforced by ALL THREE skills
      planning:  [ gate, ... ]           enforced by the planning skill only
      review:    [ gate, ... ]           enforced by the review skill only
      scorecard: [ gate, ... ]           enforced by the scorecard skill only

**C1. The gate record.** Every gate, in every group, carries exactly these six
fields, and a gate missing any of them is not a gate:

| Field | Meaning |
|---|---|
| `key` | Stable, lower snake case, unique across ALL FOUR groups. Never renamed, never reused. |
| `group` | One of: shared, planning, review, scorecard. In a skill file this field is carried by the HEADING of the table the record sits in, not by a sixth column, and that encoding is the same in all three skills. In the BOUND taxonomy it is the key the record is filed under. Either way the record has all six fields; none is omitted. |
| `fires_at` | The named stage or probe step at which it is evaluated, with any condition. **This is the ONE field of a SHARED gate that a skill MAY localize**, because stage names are local and a shared gate fires at a differently named stage in each skill. Key, behaviour, reads and doctrine on a shared gate are declared once and are copied VERBATIM by any skill that reproduces the record. A skill that does not reproduce the record inherits the generic step name from 20.1.2 and states nothing of its own. |
| `behaviour` | Exactly one of: `stop_outright`, or `ask_one_question_then_stop`. No third value. |
| `reads` | The schema VARIABLE whose value the gate tests, or the literal `none`. Never a threshold written as a literal in skill text. |
| `doctrine` | The doctrine ID that justifies the gate. It MUST carry an Applies list covering every skill in whose group the gate sits. |

**C2. The effective set.** A skill's effective stop list is `shared` PLUS ITS OWN
GROUP. Nothing else. A skill NEVER enforces another skill's group and never
reads it.

**C3. Promotion, and the single-declaration rule.** A gate enforced by MORE THAN
ONE skill is promoted to `shared`. It is never restated inside a SKILL group, and
a gate appearing in two skill groups is a defect in the binding, not a duplicate.

The shared group itself is DECLARED ONCE IN THE BUNDLE, in 20.1.2 of this file,
which owns the convention. A conforming skill may reproduce the shared table for
its own readers, and two of the three currently do; where it does, it copies
`key`, `behaviour`, `reads` and `doctrine` VERBATIM and supplies only its own
`fires_at`, per C1. **A reproduced shared table that differs from 20.1.2 in any
field other than `fires_at` is a defect in that skill, not a variant**, and the
right repair is to delete the reproduction and cite the group by name. This is
the drift vector that produced a competing fourth gate set, and naming it is what
stops it recurring.

**C4. No skill may remove a shared gate.** Where a shared gate cannot apply to a
skill's run mode, it resolves NOT APPLICABLE per SD-EFF-37, which is a PASSING
state, and it is recorded as not applicable with the reason. It is never silently
dropped and never redefined locally.

**C5. Counts live in the taxonomy and nowhere else.** No skill file states a
count of THE MEMBERS OF ANY HARD_GATES GROUP, in a table, in prose, in a heading,
in a parenthesis or in a summary line. A numeral describing something that is not
stop-list membership, such as the remediation budget in 20.2, is untouched by this
rule. The phrase "the N standing hard gates" does not appear in any skill
file, and neither does any numeral attached to a group name. A skill that wants
to refer to the set refers to it BY GROUP NAME. The schema states the record
shape, the four group names and the two behaviour values, and states no
membership and no count. The bound taxonomy is the only place a count exists.
**This file is the reference implementation of C5 and carries no count anywhere,
including in the headings of 20.1.2 and 20.1.3.**

**C6. Additions are BOUND, never invented.** A skill that needs a stop condition
not in its group requests it through the deferred-binding mechanism, naming the
decision, and until it is bound the condition DEGRADES and is DISCLOSED rather
than stopping. An implementer inventing a stop condition is the exact failure
SD-EFF-02 exists to prevent, and a companion file inventing one is the same
failure wearing a different hat: the capability probe's absent-reference rung and
a step described as a hard gate with no skip are both non-members and both
degrade instead.

**C7. Conditional gates name their condition.** A gate that fires only under a
condition carries the condition in `fires_at`, and the condition names a bound
value. A gate conditional on population shape names the mode.

**C8. The unbound default.** Where HARD_GATES is unbound, the standing sets in
20.1.2 and 20.1.3 apply, both are printed in the Method section, and the artifact
names them as standing rather than bound. reference/schema/ Group 22 owns the
RECORD SHAPE, the four group names and the two behaviour values; it states no
membership and no count, and its reference/schema/ SECTION A1 default points here for membership.
**Where the schema and this section appear to disagree about MEMBERSHIP, this
section governs, because the schema declares that it states none.** Where they
appear to disagree about the record SHAPE, the schema governs, per 0.4.

### 20.1.2 THE SHARED CORE. Enforced by all three skills.

| key | fires_at | behaviour | reads | doctrine |
|---|---|---|---|---|
| `source_unreadable` | probe step 1, and again at acquire | `ask_one_question_then_stop`: name every location attempted, then ask for the file | `SOURCE_WORKBOOK_LOCATIONS` | SD-PRS-25, reference/capability-probe.md 1.6 |
| `record_count_zero` | parse, after counting rows by non-blank identifier | `stop_outright` | `none` | SD-PRS-24 |
| `scope_unresolvable` | scope, after the text re-test and the level re-test in SD-IDN-16 | `ask_one_question_then_stop`: offer the distinct values present at every level | `none` | SD-IDN-16, SD-IDN-13 |
| `formatting_unverifiable` | verify, and ONLY where `DELIVERABLE_CONTAINER_REQUIRED` is true | `stop_outright`: do not publish as verified | `DELIVERABLE_CONTAINER_REQUIRED` | SD-FMT-06, reference/capability-probe.md 2.2 |
| `character_gate_unrunnable` | verify | `stop_outright`: unknown is not pass | `ALLOWED_CHARACTER_RANGE` | SD-FMT-14, SD-FMT-18, SD-EFF-03 |

`formatting_unverifiable` is the one shared gate with a condition, and the
condition matters: where `DELIVERABLE_CONTAINER_REQUIRED` is FALSE, which is its
documented default, the run does NOT stop. It falls back to structured markdown
carrying identical information, per reference/capability-probe.md 2.1.1 and 1.11 of this
file, and the gate resolves NOT APPLICABLE.

### 20.1.3 THE PLANNING EXTENSION. This skill only.

| key | fires_at | behaviour | reads | doctrine |
|---|---|---|---|---|
| `no_measure_column` | parse | `stop_outright`: say which of the three required concepts was missing and what the file did contain | `MEASURE_TIERS` | SD-PRS-25 |
| `qualifier_matched_no_value` | qualifier, where the phrase ROUTED to a column family and no value matched | `ask_one_question_then_stop`: report the phrase, the column tested, and the `MISS_SUGGESTION_COUNT` nearest values | `MISS_SUGGESTION_COUNT` | SD-QUA-10 |
| `comparison_single_input_warm` | comparison, and ONLY where the population is WARM | `ask_one_question_then_stop`: ask for the second file | `COLD_START_MIN_PRIOR_SHARE` | SD-CMP-01, SD-CMP-08 |

`comparison_single_input_warm` carries its condition in its key on purpose. It
fires ONLY on a warm population. On a COLD population it does not fire at all and
14.1 answers instead, per SD-CMP-08. A gate that asks for a file which cannot
exist is a dead end at exactly the altitude that most needs an answer.

### 20.1.4 Where the other two skills' currently declared gates belong

Stated so the other two skills can conform without further negotiation. Each is
placed by the C1 doctrine test, which is whether the justifying rule applies to
every skill in the group:

| Currently declared as | Goes to | Why |
|---|---|---|
| No source could be read | `shared.source_unreadable` | All three read a source. |
| Record count zero | `shared.record_count_zero` | SD-PRS-24 applies to all three. |
| Formatting could not be verified | `shared.formatting_unverifiable` | With the container condition above. |
| Character sweep unrunnable | `shared.character_gate_unrunnable` | SD-FMT-14 applies to all three. |
| Scope irresolvable | `shared.scope_unresolvable` | SD-IDN-16 applies to all three. |
| No measure column resolved | `planning.no_measure_column` and a scorecard twin in `scorecard` | The review skill's no-data path is its product and must not be blocked by a gate inspecting an artifact it does not produce, per SD-EFF-37. NOT shared. |
| A qualifier matched no value | `planning.qualifier_matched_no_value` and a scorecard twin | SD-QUA-10 does not carry REVIEW. NOT shared. |
| A comparison was asked for and only one input exists | `planning.comparison_single_input_warm` | Warm populations only. |
| The data period does not cover the period written about | `review` | Review-specific. |
| The join overlap is below the floor | `review`, and it MUST carry `fires_at` naming FIXED mode only and `reads` naming `JOIN_OVERLAP_FLOOR`. | Under FLOW it is never applied at all, per PART 23 divergence 1 and the variable's own validation. A healthy pipeline fails any reasonable floor. |
| Three or more unresolved reconciliation items | `review`, with `reads` naming `UNRESOLVED_STOP_COUNT` and the literal three deleted from skill text | A threshold in skill text is a literal, which standing rule S1 forbids. |
| Review mode with no objectives | `review` | Review-specific. |
| Reading the published standard | **NOT A GATE IN ANY GROUP.** | SD-SRC-21: mandatory, never assumed, never a stop. It degrades under a banner naming the exact release scored against and its date. |
| A required reference has no cached equivalent | **NOT A GATE IN ANY GROUP.** | SD-SRC-18 and SD-SRC-13: a stale or absent reference is a disclosed limitation; a halted run is a dead end. |

## 20.2 Retry is GRADUATED, not counted

SD-EFF-09. Classify the failure FIRST, then respond:

| Class | Response |
|---|---|
| TRANSIENT | Wait with escalating backoff per RETRY_BACKOFF_SCHEDULE. NO attempt limit. |
| SCOPED | Narrow the unit and retry up to SCOPED_RETRY_LIMIT, then rebuild it, then degrade THAT UNIT ONLY. |
| LOGICAL | Repair in place and re-verify, up to REPAIR_CYCLE_LIMIT cycles PER INVARIANT. |
| HARD GATE | Stop. |

The old rule, two attempts then stop, treated a replication lag identically to a
genuine defect and abandoned runs that would have succeeded on the third read.

An empty or failed read is UNCONFIRMED, never failed, until the ladder says
otherwise. SD-EFF-10.

**One constraint relaxed per retry, and a doctrine rule is NEVER a relaxable
constraint.** SD-EFF-11. Relax exactly one, in this order of preference: widen a
date window; lower a match threshold; drop an optional filter; fall back from
exact to fuzzy matching. Never relax a doctrine rule as a retry step.

"No forward progress" is the termination condition, and it is measured
RELATIVELY. SD-EFF-12. Define forward progress per stage type, record the measure
in the checkpoint on EVERY attempt, and compare against the PREVIOUS ATTEMPT'S
recorded measure, never against an absolute:

| Stage type | Forward progress |
|---|---|
| Reading or writing rows | the count is higher |
| Resolving references | at least one item resolved OR one candidate eliminated |
| Computing | more records scored |
| Assembling | more sections with rows AND formatting verified |
| Validating | fewer FAILING checks |

A fixed row threshold neither scales nor terminates: on a very large file a stage
can dribble a handful of rows forever and never be declared stuck, while on a
small scope the same threshold declares a healthy stage stuck immediately.

Per-gate and global remediation budgets BOTH exist. SD-EFF-36.
PER_GATE_FAILURE_LIMIT failed returns on ONE gate routes to the bannered
partial. GLOBAL_REMEDIATION_BUDGET cycles across ALL gates ends remediation
regardless of which gate is failing. Without a global cap, alternating failures
between two gates can cycle far longer than any user will wait.

## 20.3 Resuming a broken run

SD-EFF-29. On re-entry, read the checkpoints FIRST and resume at the first stage
whose checkpoint is MISSING or whose INVARIANTS NO LONGER HOLD. Re-verify; do
not assume.

**A stale checkpoint is worse than none.** If the source file changed in name,
size or row count, DISCARD EVERY DOWNSTREAM CHECKPOINT and rebuild from the parse
stage. Never resume past a gate that has not passed. An artifact assembled half
from a previous period's numbers is the worst thing this method can produce,
because it LOOKS COMPLETE.

## 20.4 Scale

**Nothing about the method changes at scale; only the mechanics of reading and
writing do.** SD-SCL-01. SCALE_TIER_BOUNDARIES sets the tiers by record count.
The method, the sections, the formatting elements, the caps and every gate are
IDENTICAL in all of them.

The output is bounded by the CAPS, not by the input. SD-SCL-02. The largest
possible artifact is roughly the same in every tier, so the build phase is a
fixed amount of writing at any scale. That is exactly why the caps exist and why
they are never raised to cover more of a big file.

**Sampling and estimating are prohibited at EVERY scale.** SD-SCL-03. Never
sample rows, estimate a threshold, extrapolate a percentile from part of the
file, lower a cap, drop a section, or shorten a list. A percentile taken over a
sample is a different number wearing the same name.

"In-scope population" means AFTER scope, after every qualifier and after any
restriction. SD-SCL-04. The distribution is built over THAT set, not over the raw
file. A large qualified run and a small one must both compute the percentile over
the same conceptual population.

Checkpoint MORE often as the tier rises, not less. SD-SCL-05. Write a stage
checkpoint after every PARTITION_SIZE records read and after every scoring block,
CARRYING THE DISTRIBUTION, so a resumed run never rebuilds it and never risks
rebuilding it differently.

## 20.5 The failure-to-response table

| Failure | Response |
|---|---|
| The scope filter returns zero rows | Re-test as text on both sides and re-test the level reading; then list the distinct values present at every level. SD-IDN-16. |
| No source found at the finest level | Escalate up the hierarchy, then filter down, and state which level was used. SD-PRS-26. |
| No measure column resolves | Hard gate. Say which of the three required concepts was missing and what the file did contain. |
| The central publication cannot be found | Walk the fallback ladder; use a prior period's, dated honestly; never stop. SD-SRC-13. |
| An attachment cannot be read after the full ladder | The third state of the retrieval gate: name the file, sender, date and every path attempted, and say the directed ledger is incomplete. Never report zero. SD-SRC-02. |
| A required concept will not resolve | Ask ONCE, batched, offering candidate headers with sampled values. Never ask for an optional concept. SD-IDN-18. |
| A header does not resolve | Log the literal, continue, name it in the Method section, propose the stem. SD-PRS-22. |
| A qualifier matches no value | Stop before ranking and ask, with MISS_SUGGESTION_COUNT nearest values. SD-QUA-10. |
| Two files have incompatible schemas | Map each independently; compare only on metrics that align; report the rest. SD-CMP-02. |
| Duplicate identifiers | MERGE the signals; see PART 23 for the FLOW exception. SD-PRS-29. |
| Several candidate containers | Score by resolvable required concepts, tie-break by record count. SD-PRS-11. |
| No single measure resolves | Synthesize the composite defined in MEASURE_TIERS, and say that it was synthesized. |
| No supervisor in the directory | Only record none when the manager call was made, returned empty, AND the title names the top of the house. SD-IDN-02. |
| The role title will not resolve | Ask once from the ladder's display names; else ROLE_FALLBACK_KEY, the narrowest role. |
| A transient tool failure | Wait and retry with no attempt limit. SD-EFF-09. |
| A section will not build after the ladder and one rebuild | Publish nothing, name the section and the exact ranks affected, preserve the checkpoint. SD-EFF-04. |
| A blocking question is never answered | The bannered incomplete path. SD-EFF-05. |

---

# PART 21: DEGRADED RUNS

Assume no tooling. The ladders are owned by reference/capability-probe.md PART 2 and this
skill takes the highest rung it can reach, records which rung it took, and
ANNOUNCES IT IN THE OUTPUT.

The shape of every ladder: do the full thing; do the same thing by another
route; produce a DIFFERENT ARTIFACT CARRYING IDENTICAL INFORMATION; produce a
reduced artifact and name exactly what is missing; produce nothing and say why,
naming every path attempted. Rung three is where most of the work is, and a
different container is NOT a reduced deliverable.

The three announcement places, all of them, every time: the FRONT PANEL of the
artifact, the METHOD section of the artifact, and the FIRST LINE of the reply.
The artifact is the copy that survives; a degradation announced only in chat is
NOT announced.

Each announcement line names THREE things, in this order: what was unavailable,
what it CHANGED, and what the reader should DO about it. Never only the first.
MSG_DEGRADED_RUN carries two slots and BOTH are filled; a message naming one
without the other is not compliant.

Sufficient, as neutral worked examples:

> The mailbox could not be reached, so no supervisor priorities were read. The
> ranking below uses the measure and the published signals only. Priorities set
> by your manager this period are not reflected.

> Formatting could not be verified in this environment, so the artifact is
> published unverified. Every number is complete; the presentation may be
> inconsistent between sections.

Not sufficient: "Some sources were unavailable." "Note: reduced functionality."
"Best effort."

What a degraded run may NEVER do:

- Present the degraded output as complete.
- Fill a gap with an estimate, an average, a plausible value, or a value carried
  over from a previous run.
- Silently widen a population, a scope or a claim to compensate for a missing
  filter. SD-QUA-12 applies to a missing CAPABILITY exactly as to a missing
  column.
- Omit a section because the capability that populated it was absent. The
  section ships with its explanatory row NAMING THE CAPABILITY.
- Write INCOMPLETE_BANNER_TEXT, or any other banner, title or note, AS A ROW ON
  AN ITEM SECTION. The three places named above are the only places it goes. The
  header row of every item section is ROW 1 with nothing above it, per
  reference/output-contract.md element 1 and PART 1 of this file, and a banner written
  above a header row breaks the freeze pane, the table range, the autofilter and
  every header-name lookup at once. A degraded run is the run that can least
  afford a broken artifact on top of a reduced one, and a banner that destroys
  the reader's ability to filter is not a warning, it is a second failure.
  SD-FMT-22, SD-FMT-23.
- Downgrade its own announcement between runs. A degradation announced last run
  and still present is announced again, at the same prominence.
- Let a degraded number ship at full claim strength. Where the missing capability
  was the counterfactual denominator's source, every affected statement drops to
  BOUNDED phrasing: a number with a denominator population and no achievement
  wording.

The self-check, answered and RECORDED before publication:

> If a reader opened this artifact six months from now with no memory of the
> conversation, could they tell from the artifact ALONE which parts of it were
> produced with less than the full method, and what that cost them?

If the answer is no, the announcement is not finished.

---

# PART 22: THE DEFERRED BINDING REQUESTS

Every entry in the table below fires ONLY when the run reaches that decision
and the value is unbound, subject to the four constraints in 3.4: right answerer
only, at most two per run and at most one before the first output, highest-cost
gap first, and once then never.

When one fires it names the DECISION, not the variable. When it does not fire,
or is declined, the run applies the documented default from reference/schema/
reference/schema/ SECTION A1 or A2 and prints that appendix's exact degradation notice IN THE ARTIFACT.

The table is ordered by cost, which is how far the default moves a published
number. That order is the firing order.

Rows 65, 66 and 67 were added after acceptance testing. They are NOT appended to
the end of the cost order: each row names the COST RANK at which it fires, and
the run inserts it there. The row numbers are stable identifiers, not positions.

| # | Decision the run is facing | Catalogue entry | Bindings requested | If declined |
|---|---|---|---|---|
| 1 | Which column identifies a unit, and can it carry leading characters that must survive | Q-H3 | UNIT_ID_CONCEPT, UNIT_ID_IS_TEXT | The seed dictionary's identifier concept, handled as text; the column used is named |
| 2 | Which number to rank on | Q-G1 | MEASURE_TIERS | First seed stem that resolves and is populated; the column, unit and time basis named in the audit |
| 3 | Which units cannot be worked right now and must be excluded before anything else | Q-D6 | UNIT_ACTIONABLE_NOW_CONCEPT, UNIT_ACTIONABLE_NOW_VALUES, UNIT_NOT_ACTIONABLE_SEED_VALUES, EXCLUSION_SANITY_CEILING | Concept unresolved: no exclusion, and the report says some units may be closed, suspended or on hold with their history still ranking them high. Concept resolved and values unbound: the seed value set is applied under the three guards of 11.2.1, every distinct value is printed as EXCLUDED or KEPT with counts, and the user is offered the person-tier correction of F5.1b |
| 4 | Which columns hold the levels of the hierarchy | Q-H4 | the scope concepts in COLUMN_CONCEPT_DICTIONARY | Whichever single scope column resolves; finer read by prefix, coarser by truncation; the level used is stated |
| 5 | Whether a group of units is served by a completely different operating model | Q-D7 | OUT_OF_MODEL_CLASS_CONCEPT, OUT_OF_MODEL_CLASS_LABEL, OUT_OF_MODEL_ESCAPES_ENABLED | No class exclusion; the whole population is ranked, stated in the funnel |
| 6 | Which units are OPEN right now, on a flowing population | Q-D3 | POPULATION_SHAPE.stages, FLOW_OPEN_DEFINITION | Open is a blank exit date; where no exit column resolves every unit is treated as open and the report says so, overstating workload rather than hiding it |
| 7 | Where a person here learns what matters this period | Q-J1 | PRIORITY_SOURCES, SOURCE_AUTHORITY_MAP, PRIORITY_SOURCE_COUNT | Only the supervisor chain is read; the report says nothing in it reflects an organization-wide priority |
| 8 | How work items are typed, because not all work builds the business | Q-I1 | WORK_TYPES | The generic ladder and its standing weights; every unrecognized item named at the baseline rather than discounted |
| 9 | How the entities that credit attaches to are ORDERED | Q-F2 | CREDITABLE_ENTITIES ranks | Nothing weighted up or down by entity; ranking rests on measure, alignment and workload alone |
| 10 | What weight each entity carries relative to the top one | Q-F3 | CREDITABLE_ENTITIES standing weights, ENTITY_WEIGHT_FLOOR | A single implicit entity at weight one |
| 11 | Whether a priority might be unlawful or non-permitted somewhere | Q-M1 | COMPLIANCE_CHECK_ENABLED, JURISDICTION_CONCEPT | No compliance check runs; the report says that if something in it cannot lawfully or contractually be done somewhere, the report does not know it |
| 12 | Where the compliance reference lives, once the check is enabled | Q-M2 | COMPLIANCE_GUIDE_SET, COMPLIANCE_GUIDE_MASTER, COMPLIANCE_GUIDE_SUPPLEMENTS | The check cannot run and every priority it would have validated is HELD BACK and named, never silently permitted |
| 13 | Whether an unreachable compliance source holds back the priorities or the report | Q-M4 | COMPLIANCE_FAILS_CLOSED_ON | The priorities are held back and named, which is the only permitted setting |
| 14 | Which mail folders a sweep of a manager's messages must cover | Q-P2 | MAIL_SWEEP_FOLDERS | Every folder the mailbox exposes is swept, and the folders covered are named with message counts |
| 15 | How far up the chain to read, and whether distance matters | Q-J4 | CHAIN_WALK_DEPTH, CHAIN_DISTANCE_WEIGHTS | Standing depth and distance weights; every level resolved is named including levels that published nothing |
| 16 | What phrases release a unit from a directive list | Q-J3 | DIRECTIVE_RELEASE_PHRASES, confirms ACTOR_TEST_ENABLED | Generic release phrases; a stand-down in different wording will not be recognized, which is stated |
| 17 | Whether a central function publishes a periodic priority document | Q-J2 | CENTRAL_BRIEF_NAME, CENTRAL_BRIEF_TABLE_COLUMNS, confirms CENTRAL_BRIEF_REQUIRED false | No central publication is read and the report says so |
| 18 | How many items each line should act on | Q-N1 | DELIVERABLE_LINES | The standing sizes, named in the front panel |
| 19 | Whether one role covers a subset of another's units under direction | Q-C3 | ROLE_LADDER.is_specialist, SECOND_ACTOR_RESOLUTION_LADDER, SECOND_ACTOR_UNIT_SUFFIX, COVERAGE_DUPLICATION_FACTOR, COVERAGE_DUPLICATION_APPLIES_TO | No duplication discount; recorded as a normal result, not a failure |
| 20 | Where the real start and end dates of the window are published | Q-L1 | OPERATING_WINDOW_SOURCE | The window is derived and the dates used are printed, with a note that every due-date weighting shifts with them |
| 21 | What rule gives the right dates when the published window cannot be read | Q-L2 | OPERATING_WINDOW_DERIVATION_RULE | The standing derivation; the exact dates printed |
| 22 | Whether the run plans the current window or the next | Q-L4 | PLAN_AHEAD_RULE | The standing rule; the period covered named at the top of the report |
| 23 | Whether the operating window lines up with the reporting quarter | Q-L3 | PERIOD_TOKEN_MAP, confirms REPORTING_CALENDAR_IS_NOT_AUTHORITY | Generic tokens; any token that cannot be resolved through the window is dropped from scoring and NAMED, never guessed |
| 24 | Which verbs appear in local work item names for each type | Q-I2 | WORK_TYPES trigger_verbs, trigger_nouns | Generic verbs; every unrecognized item surfaced by name so the vocabulary can be extended once for everybody |
| 25 | Which verbs mean nothing on their own | Q-I3 | GENERIC_COMPLETION_VERBS | The generic list; a local completion verb may type an item one rung too high, visible in the audit |
| 26 | Which spellings of an entity appear in the data | Q-F4 | CREDITABLE_ENTITIES.aliases | Unmatched names are flagged and asked about rather than guessed |
| 27 | Whether any alias is a common short word or carries punctuation | Q-F5 | SENTINEL_TOKENS | No aliases protected; every matched value set and its row count listed in the audit so an over-match is visible |
| 28 | Which initiative names are distinctive enough to match on one word | Q-F2-INIT | SPECIFIC_INITIATIVE_NAMES | Two distinctive shared words required for every match; every unmatched priority reported by name |
| 29 | Which words are too common in local headers to count as distinctive | Q-F2-STOP | MATCH_STOPWORDS | The generic stopword set plus the generic completion verbs; every match shows its shared tokens |
| 30 | Whether a published marker says an item needs this role's action | Q-J5 | OWN_ACTION_MARKER_CONCEPT, OWN_ACTION_MULTIPLIER | No item takes the marker multiplier, and that is recorded rather than approximated from verbs |
| 31 | Where the block of work-item columns starts and stops | Q-H5 | the work-item block concepts, ACTIVITY_BLOCK_TERMINATOR_CONCEPT | The ordered fallbacks in reference/field-resolution.md; "no block exists" is a valid outcome that is stated |
| 32 | Whether work-item headers carry an originator prefix | Q-H6 | ORIGINATOR_PREFIX_MAP | Prefixes ignored entirely, which costs weighting nuance and nothing else |
| 33 | Which file this reads and where it comes from each period | Q-H1 | SOURCE_WORKBOOK_NAME, SOURCE_WORKBOOK_LOCATIONS | Standing locations searched in order; the file used, its record count and the container within it are named |
| 34 | Which title words mean a wider scope than a frontline role | Q-B4 | WIDE_SCOPE_TOKENS | The generic token list; the token that decided a role is named in the audit |
| 35 | What titles and abbreviations the directory records carry | Q-C4 | ROLE_LADDER.titles, ROLE_TITLE_ABBREVIATIONS | The generic abbreviation set; an unresolved title causes the user to be asked once to pick their role from a list |
| 36 | Which role to assume when identity cannot be resolved at all | Q-C5 | ROLE_FALLBACK_KEY | The narrowest role, producing a shorter list and narrower claims, and that is stated |
| 37 | Whether levels have codes and whether a wider code sits inside a narrower one | Q-B2 | SCOPE_CODE_SCHEME, SCOPE_CODE_WIDTH, SCOPE_CODE_PAD_DIRECTION, SCOPE_CODE_PAD_CHARACTER, SCOPE_LEVEL_ID_WIDTHS, and by derivation SCOPE_CODE_AMBIGUITY_THRESHOLD | The scheme is detected from the data; if undetectable, codes are opaque and matched exactly, a short code is not padded, and the user is offered the values present |
| 38 | How people here actually phrase a scope request | Q-B3 | SCOPE_PLAIN_LANGUAGE_MAP | Scope phrases resolve only against the distinct values in the file; a failed phrase produces the list of values present rather than a refusal |
| 39 | How to group flowing units into comparable cohorts | Q-D4 | FLOW_COHORT_BASIS | Entry date; the basis is named beside every comparison |
| 40 | At what point two periods' rosters are no longer the same thing | Q-D5 | FIXED_ROSTER_CHURN_TOLERANCE | A ten percent tolerance; any comparison beyond it is labelled not like for like rather than suppressed |
| 41 | How much movement is noise | Q-E5 | DEADBAND | Computed from the data; where it cannot be computed, no win or miss label is emitted and only the raw delta with its unit is printed |
| 42 | How strongly a figure may be worded on each comparison basis | Q-E4 | CLAIM_STRENGTH_BY_RUNG | The offered defaults, printed beside each figure |
| 43 | What units the numbers come in and whether a header says total or per-period | Q-G2 | MEASURE_UNIT_TOKENS, MEASURE_RATE_TOKENS | Generic tokens; a comparison whose basis cannot be confirmed is BLOCKED and reported rather than computed |
| 44 | Whether headers mark how much history a number covers | Q-G3 | MEASURE_LOOKBACK_TOKENS | Generic tokens; an undetected difference is not labelled, which is stated as a limitation |
| 45 | Whether a detected factor between two files is a unit change or a real result | Q-G4 | UNIT_DRIFT_CANDIDATE_FACTORS, UNIT_DRIFT_AUTONORM_FACTORS | Small factors are never corrected silently and the user is asked at the moment one is detected |
| 46 | How deep the reference list behind the action lists should go | Q-N2 | REFERENCE_CAP | The standing depth; the showing note discloses the cut |
| 47 | What sections the deliverable has and what each empty row says | Q-N3 | TAB_CONTRACT at its planning key, MSG_EMPTY_SECTION | The standing PLANNING sections and generated empty messages, each naming the binding or column that would have filled it |
| 48 | What columns identify an item and what each is called, INCLUDING what the reason-for-rank column is called | Q-N4 | IDENTITY_BLOCK_COLUMNS and the HDR_ strings, all of which GROUP 24 now carries, including HDR_RANK_REASON, HDR_COMMITMENT_DATE, HDR_CLOSE_STATE, HDR_CLOSE_WEIGHT and the span pair HDR_SPAN_PREFIX and HDR_SPAN_SUFFIX | Plain English defaults from SECTION A1, stable between runs, with the count of defaulted headers named once, and every header corrected under 1.3e disclosed with the string it replaced and raised as one open request |
| 49 | Which column should stay on screen when someone scrolls, and how much of the width the freeze may take | Q-N5 | IDENTITY_BLOCK_ANCHOR_COLUMN, SPAN_BLOCK_POSITION, FROZEN_SPAN_MAX_WIDTH | The anchor is DERIVED rather than chosen, by the bounded walk of reference/output-contract.md 4.1.2 that 1.3 cites: the last identity column whose inclusion keeps the summed WIDEST-CASE built width at or under the standing bound, with the first column always frozen. The walk runs ONCE FOR THE ARTIFACT, over each identity column's maximum built width across every section carrying the block, and the one anchor is applied BY NAME everywhere, so the pin lands in the same place on every section; the truncation is recorded in the Method section as ONE line for the workbook |
| 49b | How wide a whole grid may be before a reader stops traversing it | Q-N5 | GRID_MAX_TOTAL_WIDTH | The standing bound, DECLARED BEFORE THE COLUMNS ARE BUILT and never raised to clear a section that failed it, per reference/output-contract.md 2.7 and 17.3. It is a SECOND bound and FROZEN_SPAN_MAX_WIDTH does not substitute for it: one says what stays on screen, the other how much there is. Where a section is still over after 2.7's relief ladder, it ships over the bound and records the overage rather than dropping a column, narrowing a header below its floor or shortening a value |
| 50 | What the file should be called so two runs never collide | Q-N6 | OUTPUT_FILENAME_PATTERN, DELIVERABLE_NAME at its planning key | The standing pattern and the generic PLANNING artifact name, never another skill's |
| 51 | What a user should be told is computed from their own data and what was supplied | Q-A3 | METHOD_OWNER_STATEMENT, TUNING_INVITATION | A generic statement is printed |
| 52 | What must never be said about the units that did not make the list | Q-Q1 | IMPACT_LANGUAGE_RULE, BANNED_PHRASES | The standing phrasing; no comparative editorializing is written |
| 53 | What the class of thing credit attaches to is called | Q-F1 | CREDITABLE_ENTITY_CLASS_NAME | A generic phrase in headings; nothing else changes |
| 54 | What wider population each entity should be compared against | Q-F6 | ENTITY_BENCHMARK_MAP, BENCHMARK_POPULATIONS | Every entity is unbenchmarked FOR RUNGS 1 AND 2 ONLY, so no share-of-addressable and no matched-control comparison is computed. Figures then fall to the HIGHEST RUNG COUNTERFACTUAL_AVAILABLE_RUNGS STILL SUPPLIES, which is named beside each one, and the claim strength drops with it. A figure routes to the bare denominator ONLY when no other bound rung resolves. An unbound deferred value never overrides a rung the organization bound at ignition. SD-CTR-24, G6. |
| 55 | What must never be claimed as an achievement even when it is going well | Q-F7 | NON_CLAIMABLE_ENTITIES | Nothing marked unclaimable; the report cannot warn when a figure describes a population the person did not compose, which is stated |
| 56 | Whether a place name a person types is the same string the data stores | Q-M3 | JURISDICTION_NAME_TO_CODE, SUBREGION_SUFFIXES | Place names resolve only on exact match, and a miss returns the nearest values present rather than widening |
| 57 | Where reference documents live and whether folder names are stable | Q-P1 | DOC_STORE_NAME, DOC_STORE_SITE_VARIABLE, DOC_STORE_LIBRARY_VARIABLE, confirms DOC_STORE_PATH_DISCOVERY_REQUIRED true | Discovery runs against whatever container resolves, and a failure to find a reference is reported by name |
| 58 | Whether another system already owns a job this run is about to duplicate | Q-P3 | SYSTEM_OF_RECORD_EXCLUSIONS, SIBLING_SKILLS | Nothing is withheld on that ground; the user is invited to say if something duplicates a system they already run |
| 59 | Whether a term of art may be paraphrased in output prose | Q-Q2 | CONTROLLED_VOCABULARY | No term is protected and paraphrase is possible, which is stated once |
| 60 | Which division these reports cover, as distinct from the company | Q-A1 | OPERATING_UNIT_NAME, OPERATING_UNIT_LONG_NAME, ORG_SHORT_NAME | Reports are headed with the organization name and cannot distinguish two divisions using this toolkit |
| 61 | How long to keep trying when something goes wrong mid-run | Q-R1 | RETRY_BACKOFF_SCHEDULE, SCOPED_RETRY_LIMIT, REPAIR_CYCLE_LIMIT | The standing ladder |
| 62 | What should stop a run outright, per skill | Q-R2 | HARD_GATES, as the four-group taxonomy defined in 20.1.1 | The standing shared core in 20.1.2 and the standing planning extension in 20.1.3 apply, both are printed in the Method section, and the artifact names them as standing rather than bound |
| 63 | Whether a partial report may ever be published | Q-R3 | INCOMPLETE_BANNER_TEXT, INCOMPLETE_PLACEHOLDER_TEXT | The standing banner and placeholder |
| 64 | Whether to look at a real file now and learn its headers | Q-S1 | COLUMN_CONCEPT_DICTIONARY additions, NULL_LIKE_VALUES, MIN_STEM_LENGTH, HEADER_SCAN_DEPTH, CONCEPT_LEARNING_ENABLED | The seed dictionary is used unchanged and every unresolved header is still logged |
| 65 | COST RANK 2. What exactly the set is, and which column counts it, for a rung already named as available. Fires when a figure is about to be compared on a rung above the floor and that rung's OWN definition is unbound. | Q-E6 | ADDRESSABLE_POPULATION_DEFINITION, ADDRESSABLE_POPULATION_CONCEPT, CONTROL_GROUP_DEFINITION, PEER_SET_LEVEL_DEFAULT, PEER_SET_ANCHOR_PERIOD, PEER_SET_IS_EXTERNAL, EXTERNAL_PEER_SET_SOURCE, PLAN_SOURCE_NAME, PLAN_SET_BY_ROLE, PRIOR_PERIOD_BASIS, one or two per available rung | That rung is marked UNAVAILABLE for this run. Every figure assigned to it drops to the HIGHEST RUNG WHOSE OWN DEFINITION IS BOUND, the drop is stated beside the figure, and the claim strength drops with it. A rung NAMED but not DEFINED is not an available rung. |
| 66 | COST RANK 6. Which comparisons a part of the business genuinely cannot produce, once a population has been DETECTED as cold. | Q-E7 | COUNTERFACTUAL_RUNG_SCOPES, and by consequence COLD_START_MIN_PRIOR_SHARE and ADDRESSABLE_SELF_SHARE_CEILING | The organization-wide rung list is NOT inherited by the cold population. Each rung is re-tested against that population alone per 14.8.3 and struck where it fails, every strike is named beside the figures it would have carried, and the standing threshold values are used and named. |
| 67 | COST RANK 4. Whether a date the unit itself carries is a COMMITMENT the person must act on, or a record-keeping date. Fires when a unit-level date concept resolves and populates and no work-item block exists. | An extension of Q-H5, routed to the binding owner as a proposed catalogue entry, binding through COLUMN_CONCEPT_DICTIONARY and that concept's `feeds` list | COLUMN_CONCEPT_DICTIONARY entry for a unit-level commitment date, and its `feeds` list | No unit-level commitment date is scored. The column is RECORDED and DISPLAYED in the identity block, the artifact says plainly that no unit-level commitment date was scored and NAMES the column that would have supplied one, and the ranking rests on the measure, the alignment and the workload alone. That is the floor of the scale, so binding it later can only raise a result. SD-WGT-02. |

## 22.1 Six things this skill NEVER stops a run to ask

These are the composite catalogue entries whose variables have standing values
that are safe, published in the artifact, and reviewable only in the Stage 3
audit or when a user disputes a specific number:

| Entry | Covers |
|---|---|
| Q-SCORING-REMAINDER | Every scoring constant: the formula shape, the base term, the exponent, the gap weight and cap and definitions, the workload cap and multiplier, the source boosts, the mandatory multiplier, the local boost and override depth, the narrowness threshold and multiplier, the central-flag breadth limit, the steer weights, the initiative term, the tie-break keys, the zero-measure sort key, the percentile definition, the zero-measure treatment, the minimum population for a norm, the close weights, the undated treatment and the carryover label. |
| Q-EXCEPTION-REMAINDER | Every exception constant: the flags, the multiplier floor, the band thresholds and labels, the recency floor and factor, the alert bands and their non-scaling, the alert population, the benchmark gap threshold, the size-gated programme test, the lag disclaimer and the flag exemptions. It is offered ONCE, at the first exception section, as one question about which of these are real problems here and whether anything on it is something a person cannot fix themselves. |
| Q-FORMAT-REMAINDER | The formatting elements, the table style, the palette, the fonts, the row heights, the narrative width range, the character-width factor, the line-height padding, the right-align list, the heading case, the character range, the full-walk limit and the sampling density. A volunteered colour or font is recorded immediately. |
| Q-RUNCTL-REMAINDER | The write chunk size, the tail verification, the confirm wait, the partition size, the concurrency cap, the scale tiers, the checkpoint paths, the checkpoint deletion rule, the regression invariants, the spot-check size, the regression cases, the global and per-gate budgets, the forbidden retrieval paths, the inline fetch ceiling and the encoding factor. |
| Q-QUESTIONS-REMAINDER | The question bank, the batch ceiling, the non-blocking budget formula, the composite question set, the exempt questions, the anomaly cap, the headline threshold, the miss suggestion count, the evidence floor, the synthesis minimum and maximum, the run estimate bands and the ask-language rule. |
| Q-N-REMAINDER | The user size fraction and override flag, the scope-rank header, the score column requirement and precision, the unresolved-column treatment, the reply length, the submission banner, and the four directory variables. |

Because the artifact publishes the FORMULA and the SCORE, a disagreement about
any of these can be traced to a specific term and corrected rather than argued.
That is what makes never asking about them safe. SD-CTR-21.

---

# PART 23: FIXED AND FLOW

## 23.0 What shape IS, and where the run gets it

**Shape is a property of the POPULATION BEING SCORED, not of the company.**
SD-POP-23. FIXED and FLOW are not a fact about an organization. Many real
businesses are genuinely BOTH: a stable roster of units with work items flowing
across them, or a roster of containers with a stream moving through them.
Forcing one answer for the whole company IS ITSELF THE ERROR.

POPULATION_SHAPE is therefore a KEYED SET of declared populations, each with its
own mode, its own unit noun and its own fields. A business may declare one; it
may declare three. Where only one is declared it is the default for every run and
nothing else changes.

**A run never asks whether this company is FIXED or FLOW. It asks WHICH
POPULATION IT IS SCORING, and WHAT SHAPE THAT POPULATION HAS.** The population is
resolved from the request and from the source in hand, and the run READS that
population's shape. The run NAMES the population it scored in its own front
panel.

Two consequences follow and both are stated in the artifact:

- Two skills in this bundle running the same morning on the same business may
  legitimately be in DIFFERENT shapes, and each names the population it scored.
- Two skills scoring DIFFERENT populations of the same business will report
  DIFFERENT COUNTS, and neither is broken. This skill's N is the OPEN set under
  FLOW, because a plan is a plan for work that is still open. A gap-scoring skill
  scores STAGE ARRIVALS in the window instead, which is a different and also
  correct population, because scoring only the currently open set makes a fast
  period look good. **The two counts are not expected to agree, and this skill
  says so on its front panel wherever it emits a FLOW count.**

**Where the shape comes from, and it is two branches, not one:**

| Run | Where the shape comes from |
|---|---|
| BOUND run | READ from the declared population the run resolved. Never inferred, never guessed. |
| PROVISIONAL run, POPULATION_SHAPE unbound | INFERRED from the columns present at MEDIUM confidence, by 3.2.1, with the inference and its evidence printed in the front panel and the Method section, the tie-break disclosed as a tie-break where test three could not be answered, and every sub-key that could not be inferred treated as UNBOUND. |

That is the whole of the correction: the older wording of this part asserted the
shape was never inferred while 3.2 inferred it on every provisional run, and the
provisional run is not a rare path. Both statements are now true because they are
about different runs, and each says which run it is about.

**Detect the shape by THREE tests, and the THIRD one decides.** SD-POP-24:

| # | Test | Evidence for |
|---|---|---|
| 1 | THE ROSTER TEST. Can a complete list of all of them be produced as of a given date, without reference to what stage each is in? | a roster |
| 2 | THE ENTRY AND EXIT TEST. Does each one have a date it entered and a date it stops being the organization's problem? | a pipeline |
| 3 | THE REPLACEMENT TEST, WHICH DECIDES. When one of them leaves, does it leave a HOLE somebody notices and moves to fill, or does the next one simply take its place in a QUEUE? | a HOLE means the population is a FIXED roster whose members happen to be dated, and the dates are UNIT ATTRIBUTES rather than a pipeline. A QUEUE means FLOW. |

**Tests one and two both passing is the COMMON case, not the ambiguous one.** A
roster of dated standing positions passes both. So does a pipeline held inside a
stable set of containers. The third test separates them and IS NOT OPTIONAL.

**THE TIE-BREAK IS CONSULTED ONLY WHERE TESTS ONE AND TWO DID NOT DISCRIMINATE
AND TEST THREE CANNOT BE ANSWERED.** Not discriminating means both passed or both
failed. Where test one passes and test two FAILS, the shape is FIXED and it is
DECIDED: the tie-break is not run and FLOW is not preferred. Where test two
passes and test one FAILS, the shape is FLOW and it is DECIDED. Only where the
first two tests leave the question open, and the third cannot be answered from
what is in hand, is the tie-break reached.

Where the tie-break IS reached, prefer FLOW and RECORD that the shape was taken
on the TIE-BREAK rather than answered, so the binding owner can see it and
correct it. A tie-break that leaves no trace is a guess, and a shape recorded as
tie-broken when it was decided is a guess in the other direction.

**THE ONLY PROCEDURE.** SD-POP-24 is the single shape detection procedure in this
bundle. Where any shorter formulation appears anywhere, including the phrase "an
entry date plus an exit date plus a stage column means FLOW", it is evidence
toward test two ONLY and never a decision on its own.

Where the roster test passes over CONTAINERS and the entry-exit test passes over
the things moving across them, that is NOT a conflict. **It is two populations.**
Declare both, per SD-POP-23, and let each run name which it scored. Worked
example, neutral: a service centre has a fixed roster of handlers and a flowing
population of cases. That is two declared populations, not one contested one; the
case population's container is a scope level, and the handler population is a
roster in its own right.

**Shape changes the DENOMINATOR, never the DELIVERABLE.** SD-POP-21. A FIXED
roster and a FLOWING pipeline both rank, both exclude, and both produce the same
sections in the same order with the same caps. What changes is what "the
population" MEANS.

A FIXED model applied to a pipeline silently mixes CLOSED and OPEN units into
one denominator, and the reader cannot recover it from the output. A FLOW model
applied to a roster of standing positions cohorts those positions by the year
they opened and produces a comparison nobody asked for, and their end dates are
not null, so the old claim that a flow model over a roster is harmless is FALSE
where the members are dated. Both directions are real, which is why the third
test decides rather than a tie-break.

## 23.1 The two shapes, side by side, stage by stage

| Stage | FIXED | FLOW |
|---|---|---|
| Enumeration | POPULATION_SHAPE.enumeration_source gives the full roster as of census_basis. | POPULATION_SHAPE.enumeration_source is the QUERY that defines the open set, evaluated at run time under FLOW_OPEN_DEFINITION. |
| What N is | Every unit on the roster after scope, qualifiers and exclusions. | Every OPEN unit after scope, qualifiers and exclusions, as of the run moment, with the moment printed. |
| Census disclosure | Print the census date and POPULATION_CENSUS_INTERVAL. | Print the open rule AS APPLIED, the run moment, and POPULATION_CENSUS_INTERVAL. |
| Not-actionable exclusion | UNIT_ACTIONABLE_NOW_CONCEPT and its values, per 11.2. | The SAME concept, and it is SEPARATE from the open-set rule. A unit can be open and still not actionable; both counts are reported separately in the funnel so they never double count. |
| Stage exclusion | not applicable | Units removed because they are closed, withdrawn or outside the open set are reported WITH THEIR COUNTS IN THE FUNNEL exactly as any other exclusion. SD-POP-22. Never silently absent. |
| Aging | Days since the recency concept, if one is bound. | Days from POPULATION_SHAPE.aging_basis, computed, not maintained. Stage-level aging is computed from the stage entry where the source records it. |
| Cohorts | not applicable | FLOW_COHORT_BASIS groups units into comparable cohorts: entry, exit or event. |
| Like-for-like across two periods | FIXED_ROSTER_CHURN_TOLERANCE on roster overlap. | The cohort definition, per divergence 1 below. |
| Peer set | Sibling units at PEER_SET_LEVEL_DEFAULT, anchored by PEER_SET_ANCHOR_PERIOD. | Sibling CONTAINERS at PEER_SET_LEVEL_DEFAULT, with the cohort basis stated alongside. |
| Duplicate identifiers | Merge, per SD-PRS-29. | Merge WITHIN an episode; do not merge ACROSS episodes when reopen_allowed is true. See divergence 2. |
| Breadth section | Usually admissible where a count and a percentage both resolve. | Usually NOT admissible, because a transient unit accumulates no breadth. The section still ships, with the explanatory row naming the missing half of the pair. SD-CTR-12 does not relax. |
| Carryover | The UNIT persists, so carryover attaches to the unit's row. | The unit may have LEFT the population, so carryover attaches to the WORK ITEM. See divergence 4. |
| Zero-measure units | Included at zero, ranked last by the sort key. | Identical. A newly arrived unit with no measure yet ranks last and is VISIBLE there. SD-POP-12. |
| Two-file overlap floor | JOIN_OVERLAP_FLOOR applies, and it is CONDITIONAL on this mode. | JOIN_OVERLAP_FLOOR is NEVER applied. A healthy pipeline replaces most of its rows every period and fails any reasonable overlap floor. See divergence 1. |
| Exception flags | The four generic FIXED flags in 16.2: coverage stale, presence absent, benchmark shortfall, commitment missing. | The four generic FLOW flags in 16.2, computed from the fields FLOW already requires: stage age above the local median stage dwell, past-due exit date with the unit still open, no next action recorded, and exit date moved more than once. The FIXED four resolve to nothing on a pipeline and the section would otherwise be permanently empty. |
| Cold start | Detected by 14.8.2 tests 1 and 3. | Detected by all three, and test 2 is the sharpest because entry dates are always present. |

## 23.2 Scoring under each shape

Every term of the formula in 12.1 is evaluated under both shapes. What differs:

- The MEASURE. Under FIXED it is normally a stock or a rate attached to a
  persistent unit. Under FLOW it is normally a value attached to the item itself,
  and the percentile is computed over the OPEN set. Either way the tier ladder in
  MEASURE_TIERS resolves it, the first tier that resolves and is populated wins,
  and the column, its unit and its time basis are reported.
- The WORKLOAD count. Under FIXED it is the count of work items closing this
  period ON that unit. Under FLOW it is the count of work items closing this
  period on that item, PLUS any stage-mandated step whose due date falls in the
  window. The cap is applied to the COUNT first, then multiplied. SD-SCO-12.
- The ALIGNMENT term is identical. Priorities name units, or name work, or name
  a stage. Where a priority names a STAGE under FLOW, every open unit in that
  stage is treated as matched by that priority, and the narrowness test in
  SD-PRI-24 is computed against the SAME N, so a stage holding most of the
  pipeline does not become a sharper priority than a stage holding a handful.
- The GAP terms are identical in form. Under FLOW a gap term whose source is a
  persistent attribute of the unit is typically resolved-but-empty and is
  therefore NAMED AS NOT EVALUATED, never scored at zero. SD-SCO-11, SD-PRS-18.
- The LOCAL BOOST is identical: the prefix test on raw characters, per 12.6.
- The MANDATORY multiplier is identical, applied once on the finished score.

## 23.3 Exclusions under each shape

The pipeline order in 11.1 is unchanged, and no step may be reordered under
either shape. What each step DOES:

| Step | FIXED | FLOW |
|---|---|---|
| 1 scope and qualifiers | as written | as written; a stage qualifier is an ordinary qualifier routed to the stage column |
| 2 not-actionable | as written | as written, and it is NOT the open-set rule |
| 3 normalize the measure | as written | as written |
| 4 class-escape median with the class INCLUDED | over the roster | over the OPEN set with the class included |
| 5 resolve the mandatory set | as written, BEFORE step 6 | as written, BEFORE step 6, and a directed unit that has since LEFT the open set is still listed, marked as no longer open, and its count is reported. A directive the user cannot see was received is worse than one that arrives with a gap. SD-PRI-14. |
| 6 class exclusion and its three escapes | as written | as written |
| 7 percentiles, medians, peer norms | over the ranked population | over the ranked OPEN population |
| 8 split into mandatory and merit | routing only | routing only |

## 23.4 The four places the two paths CANNOT be reconciled and must diverge

Everywhere else in this file, one rule serves both shapes. These four are stated
as two rules on purpose, because collapsing them would make one of the two
shapes wrong, and the wrongness would be invisible in the output.

**All four were re-checked against the corrected model in SD-POP-23 and
SD-POP-24, and all four SURVIVE.** Making shape a property of the population
rather than of the company does not remove a single one of them, because each is
a divergence between two SHAPES, not between two companies, and a keyed set makes
it MORE likely that a business meets both shapes on the same morning rather than
less. Three of the four are restated below with what the corrected model adds:
divergence 1 gains the overlap-floor conditionality, divergence 2 gains the
provisional-run path, and divergence 3 is unchanged in substance and now names
which declared population it is speaking about. Divergence 4 is unchanged.

### Divergence 1: the like-for-like test across two periods

There is no single test.

- FIXED: like-for-like is a ROSTER OVERLAP test AND A SEPARATE EXIT TEST, and
  overlap alone never establishes it, per SD-CMP-09 and 14.2.1. Compute the
  fraction of the roster that changed between the two periods and compare it
  against FIXED_ROSTER_CHURN_TOLERANCE. Beyond it, the comparison is LABELLED not
  like for like and is still published; it is never suppressed. JOIN_OVERLAP_FLOOR
  applies here and ONLY here: it is CONDITIONAL on the population's mode being
  FIXED, and it is set low even then, because a real roster churns. **Then count
  the units present in the prior file and absent from the current one, before
  computing anything on the pair**, because a survivor-only prior file passes both
  of the tests above at their maximum while being unusable for retention or for
  same-unit growth.
- FLOW: like-for-like is a COHORT DEFINITION test. Compute both periods on the
  same FLOW_COHORT_BASIS and state the basis beside every comparison. Grouping
  by EXIT date makes a slow period look good, because only the easy ones closed;
  grouping by ENTRY date compares intake to intake. The basis is a binding, not
  a judgment, and the run never switches basis mid-comparison.
  **JOIN_OVERLAP_FLOOR is NEVER APPLIED under FLOW, and it is never a gate here.**
  A healthy pipeline shares a fifth of its rows with itself one period later, so
  any reasonable overlap floor declares every real comparison invalid, and the
  stop that results is correct-looking: it reports both rosters and reads as a
  data problem rather than as a method that does not handle pipelines. The join
  under FLOW is on the EPISODE KEY, per divergence 2, never on the identifier
  alone where reopen_allowed is true.

Applying the roster test to a pipeline reports one hundred percent churn on a
healthy pipeline and declares every comparison invalid. Applying the cohort test
to a roster invents cohorts that do not exist. Both fail silently. The two tests
are named separately, both are printed in the audit under their own names, and
the run states WHICH test it applied.

### Divergence 2: duplicate identifiers, when a unit can re-enter

SD-PRS-29 says MERGE the signals on a duplicate identifier, and under FIXED that
is unconditional.

Under FLOW with POPULATION_SHAPE.reopen_allowed true it is WRONG. Two rows
carrying the same unit identifier with non-overlapping entry and exit windows are
two DISTINCT EPISODES of the same unit, not one unit recorded twice. Merging them
fabricates a single long-lived unit, inflates its workload count, sums two
periods of measure into one, and makes its aging meaningless.

The FLOW rule: the merge key is the EPISODE KEY, which is the unit identifier
plus the entry date. Merge duplicates WITHIN an episode exactly as SD-PRS-29
requires. Across episodes, keep them separate, rank them separately, and report
the count of units carrying more than one episode. Where entry dates are absent
and reopen_allowed is true, the run cannot form an episode key: it says so, keeps
the rows separate, marks them as UNRESOLVED DUPLICATES, and excludes them from
the tie-break's uniqueness assumption rather than merging them on a guess.

Where reopen_allowed is false, FLOW uses the FIXED rule unchanged.

**On a PROVISIONAL run, reopen_allowed is ALWAYS unbound**, because it cannot be
inferred from the columns present, per 3.2.1. The run therefore takes the
unresolved-duplicates path above rather than merging on a guess: duplicates are
kept separate, marked UNRESOLVED DUPLICATES, named in the audit with their count,
and excluded from the tie-break's uniqueness assumption. It is not permitted to
infer reopen_allowed from the presence of duplicate identifiers, because a
duplicate identifier is equally evidence of a merge candidate.

### Divergence 3: whether the recency signal may enter the ranking

SD-EXC-12 says a lagging recency field carries weight INSIDE the exception
section and ZERO everywhere else, because weighting it would steer people back to
units they just left.

The reason is that the field LAGS the thing it measures: it is maintained by
hand, it can be days or weeks behind reality, and RECENCY_LAG_DISCLAIMER exists
to say so. That reasoning holds for a maintained last-contact field and it does
NOT hold for an age COMPUTED from a system-recorded entry or stage date, which
does not lag anything.

The general rule, which is the one to implement: **a recency signal may enter
the ranking only when it does not lag the thing it measures, and then only
once.**

- Where the signal is a MAINTAINED contact field, on either shape: exception
  section only, weight zero everywhere else, disclaimer printed, and the section
  says so on its face.
- Where the signal is a COMPUTED age from a system-recorded date, which is the
  normal case under FLOW: it may enter the ranking as a gap term with a NAMED
  SOURCE in GAP_TERM_DEFINITIONS. If it does, it must NOT also carry weight in
  the exception flag, because that would apply the same factor twice, which
  SD-WGT-19 forbids. The run states which of the two placements it used.
- Where it is unclear which kind the field is, take the MAINTAINED reading,
  because that is the reading whose error a reader can detect: an under-weighted
  signal shows up as a unit ranking lower than expected, while a double-counted
  one shows up as nothing at all. SD-STR-10.

The alert instrument is unchanged under both shapes: flat, not scaled, counted
over the whole population. SD-EXC-03, SD-EXC-04.

### Divergence 4: what carryover attaches to

SD-SCO-06 keeps expired prior-period work VISIBLE at the floor weight, labelled
with CARRYOVER_LABEL on the unit's row, contributing zero to the workload count.
"Expired" here means state 8 of 12.3.1 and nothing else: a date that is BEFORE
the run date and BEFORE the current window opened. A date that has not yet passed
is state 6 and a date that passed inside the window now closing is state 7, and
neither takes CARRYOVER_LABEL under either shape.

Under FIXED the unit persists between periods, so the label sits on the unit's
row and the reader sees it next to everything else about that unit.

Under FLOW the unit may have LEFT the population entirely, and a closed unit
cannot appear on a ranked list of open units without re-admitting an excluded
row, which SD-EFF-07 makes a regression failure. So under FLOW the carryover
object is the WORK ITEM, not the unit:

- Expired work on a unit that is STILL OPEN behaves exactly as under FIXED: the
  floor weight, the label on the row, zero toward workload.
- Expired work on a unit that has LEFT the open set is reported in the
  PRIORITIES section as unfinished carried work, with the unit named, its exit
  date, and the item. It scores nothing and it never enters the ranked
  population. Its count is reported in the funnel.
- The run states which of the two it did for each carried item, so a reader can
  see that the work was not lost and was not smuggled back into the ranking.

Attempting one rule for both shapes produces either a ranked list containing
closed units, or a class of unfinished work that disappears from the output with
no trace. Both are failures the reader cannot detect.

## 23.5 What does NOT diverge, and must not be made to

For the avoidance of an implementer inventing a third path:

- The section set, their order, the identity block, the caps, the rank
  continuity, the showing notes, the formatting elements and the two sizes.
  SD-CMP-05 and SD-CTR-06 both say a change of basis never changes the shape.
- The pipeline order in 11.1.
- The percentile definition and the zero bucket.
- The absence of any measure floor.
- The scoring formula, term for term.
- The three escapes from the class exclusion.
- The retrieval gate, the actor test, the carry-forward ordering, and every
  priority rule in PART 8.
- The compliance stage.
- The audit specification.

---

# PART 24: REGRESSION CASES, THE PORTABILITY TEST AND THE VERSION BLOCK

## 24.1 Named regression cases run before any change ships

SD-RUN-10. REGRESSION_CASES holds a small CLOSED set of end-to-end cases, each
with inputs, expected result and the failure it catches. Run ALL of them before
a change ships. The set covers, at minimum:

| Case | What it catches |
|---|---|
| The environment-credit trap | A figure that grew while its benchmark grew faster being labelled a win. SD-CLM-07. |
| The user with no configuration | The provisional run at a company where nothing is bound: does it produce real output, label itself, and ask the user nothing they cannot answer. |
| The altitude ceiling | A narrative line claiming ownership above the role's ceiling, caught by the verb lists. SD-CLM-10. |
| The unconfirmed inference | A proposal whose question never fired shipping as CONFIRMED instead of REMOVED. SD-CNF-04. |
| The span-of-control error | A column set computed on one section and not another, or a check written against fixed column numbers. SD-SPN-03, SD-CTR-08. |
| The low-confidence inference | A thin-evidence sentence shipping as prose instead of becoming a question. SD-CNF-01. |
| The tied superlative | A superlative shipping without its tie count. SD-CLM-11. |
| The rule-inversion trap | A run reporting zero items dated by close-date rule 1 on a period whose publication named several. SD-SCO-01, SD-LNG-04. |
| The neighbouring-column exclusion | An exclusion flag resolved to a forbidden neighbour, which every downstream invariant still passes. SD-POP-05. |
| The ordering trap | The class exclusion running before the mandatory set is resolved. SD-POP-04. |
| The cap-on-the-wrong-axis trap | An over-capped directed section cut by score instead of by measure. SD-RNK-07. |
| The FLOW episode trap | Two episodes of the same identifier merged into one unit. PART 23 divergence 2. |
| The self-built denominator | A share computed against a denominator the writer's own team is building, shipped at achievement strength with a WIN label, on a run where the denominator column resolved and populated. SD-CLM-30, SD-CLM-31, 14.8.4. |
| The cold executive | A comparison requested against a population with no prior period, answered with a request for a file that cannot exist instead of with plan attainment and absolute build. SD-CMP-08, 14.1. |
| The inherited rung | A cold population inheriting the mature business's available rungs instead of having them re-tested. SD-CLM-29, 14.8.3. |
| The leader ranked against subordinates | A peer level resolving at or finer than the requester's own level, or a peer set intersecting the requester's own span. SD-SPN-14, SD-SPN-15, 14.6. |
| The one-unit deliverable | A reader whose scope holds fewer than MIN_POPULATION_FOR_RANKING units receiving a ranked list with a percentile, and the separate case of the unit of business being coarser than the reader's own scope. SD-POP-25, SD-POP-26, 11.7.1, 11.7.2. |
| The inert measure | A measure identical across the whole population, printed as a percentile column of identical values with no statement beside it. SD-POP-27, 11.7.3. |
| The unit-attribute commitment | A source with no work-item block whose ranked list silently reduces to the population sorted by size, because the commitment date lives on the unit. 12.2.1. |
| The empty exception section | A flowing population receiving the fixed-roster flag set, so the section ships one explanatory row on every run forever. 16.2. |
| The shape assertion | A provisional run inferring the shape and an implementer reading Part 23 as if the shape were always read. SD-POP-23, SD-POP-24, 3.2.1, 23.0. |
| The colliding stem | Two concepts matching the same header exactly where one is strict, resolved by column position instead of refused. SD-PRS-47. |
| The invented stop | A run stopping on a condition in no HARD_GATES group: an unreachable published standard, an absent cached reference, or a FLOW overlap floor. SD-SRC-21, SD-SRC-18, 20.1.4. |

## 24.2 The portability test

SD-RUN-12, and reference/field-resolution.md F0.4. Hold TWO REAL EXPORTS of the same
source from DIFFERENT PERIODS, months apart. **A change to the resolution
dictionary that would break either one is wrong.** Run both before shipping any
change.

The two files WILL differ on: the header row position, the container count, the
naming of the same column, the measure basis, the identifier type, the presence
of a work-item block, the presence of a status flag, and the total column count.
That is the normal condition, not a defect, and it is the entire reason fields
resolve by CONCEPT rather than by literal header.

Where a second period's file is available in a run, offer the test, report every
difference, and record it. Nothing is lost if the offer is declined.

## 24.3 The version block

SD-RUN-13. Carry a version block that separates WHAT WAS VERIFIED BY EXECUTION
from WHAT WAS NOT, and names the first-run checks a deployer should watch. A
reader must not trust an unverified path as much as a verified one.

BUNDLE_VERSION and BUNDLE_VERSION_DATE stamp the bound configuration. Where they
are unbound, the artifact says so and states the consequence: two reports built
weeks apart cannot be compared for method changes.

---

# PART 25: GUARDRAILS

The absolute list. Each is in force everywhere in this skill, and each is a
compressed restatement of a rule already stated above with its citation.

1. Never fabricate a unit, a number, a date, a target, a priority or a quote.
   SD-CNF-07.
2. Never emit a rank, a score or a benchmark you could not compute. Leave it
   blank with a stated reason. SD-CNF-07, SD-POP-18.
3. Never confuse two levels of the scope hierarchy; resolve an ambiguous code
   against the DATA. SD-IDN-07.
4. Never analyze a partial source, and count RECORDS, not the reported extent.
   SD-PRS-24.
5. Never trust a write's success response. SD-EFF-13.
6. Never treat an empty read as a failed write until the ladder says so.
   SD-EFF-10.
7. Never mix data writes with structural operations in one call. SD-EFF-20.
8. Never publish an incomplete list, and never publish a partial that could be
   mistaken for finished. SD-EFF-04.
9. Never stop because a stage failed twice. Classify the failure and work the
   graduated ladder. SD-EFF-09.
10. Never stop because the input is large. SD-EFF-01, SD-SCL-01.
11. Correctness outranks speed, always. SD-EFF-01.
12. Never delete anything outside the in-progress scratch artifact, and only one
    damaged unpublished section at that. SD-EFF-26.
13. Never infer change from one snapshot. SD-CMP-01.
14. A comparison never changes the deliverable shape. SD-CMP-05.
15. Confirm every save of a settled answer. SD-IDN-15.
16. Entity weighting never overrides the measure and never reorders the list by
    itself. SD-WGT-05.
17. Undated work is dropped from scoring, never down-weighted, and is dated by
    the published source FIRST. SD-SCO-05, SD-SCO-01.
18. Always read the central source; never stop for its absence. SD-SRC-13.
19. Do not caveat a matching supplied input. SD-PRS-28.
20. Never ask the user to restate a resolvable request. SD-IDN-11.
21. A resolved but empty column is an absent column. SD-PRS-18.
22. Compute all arithmetic with a tool. SD-RUN-14.
23. Quote priorities verbatim, with sender and date. SD-CNF-07.
24. The two action lists never overlap, and ranks never restart. SD-RNK-01.
25. Decline any request to rank or evaluate people. SD-LNG-02.
26. Do not send or share the artifact automatically. SD-CTR-18.
27. Never silently widen a population, a scope or a statement, for any reason,
    including a missing capability. SD-QUA-12.
28. Never default an unknown to the value that maximizes its score; where a
    default is required, take the floor of the relevant scale. G3, SD-WGT-02.
29. An unbound variable never removes a section; the section ships with its
    explanatory row naming the binding that would have filled it. SD-CTR-07.
30. The same degradation is announced at the same prominence on every run until
    it is bound. It is never quietly downgraded because it has appeared before.
31. A frontline user is never asked an organization question, in any phrasing,
    including as a confirmation.

---

# PART 26: FOUR RULES THAT BELONG TO NO SINGLE STAGE

## 26.1 Publish the number you ranked on

SD-CTR-10. SCORE_COLUMN_REQUIRED must be true. The score column is MANDATORY on
every item section, written to SCORE_DECIMAL_PLACES, and it is never omitted,
never rounded away, and never replaced by a band.

> A ranked list that does not publish the number it ranked on cannot be checked
> by the person holding it, and a reviewer comparing two runs has nothing to
> compare.

This is what makes the transparency in 12.1 real rather than rhetorical: the
formula is printed, the constants are named, the worked example is given, and
the score is on the row, so a disagreement can be traced to a specific TERM and
corrected rather than argued. A unit forced last by the zero bucket still
publishes its REAL score, per SD-POP-15.

**AND THE PRECISION IS CHECKED AGAINST THE REACHABLE RANGE OF THE SCORE, BECAUSE A
COLUMN THAT PRINTS THE SAME NUMBER ON TWO ADJACENT ROWS CANNOT DO THE ONE JOB THIS
RULE GIVES IT.** `SCORE_DECIMAL_PLACES` is a standing precision chosen without
seeing the data, and the measure factor of 12.12 raises a percentile to
MEASURE_EXPONENT, which compresses the bottom of the range hard. Measured: on a
ranked population of a couple of hundred, the last few published rows all printed
zero at the standing precision, and two adjacent rows separated by a real score
difference printed the SAME number, so the published column could not be used to
check the ordering of exactly the rows a sceptical reader is most likely to query.
Nothing was wrong: the reason cell named the terms and the tie-break that placed
each row, so the ordering was defensible. The column 26.1 makes mandatory was
simply inert where it mattered most. This is reference/schema/ standing rule S5 in
its ordinary form, a threshold that could be computed from the data in hand and so
must be: the bound value is a FLOOR, never a substitute for the live computation.

- **THE TEST, RUN ONCE OVER THE FULL RANKED POPULATION BEFORE THE COLUMN IS
  WRITTEN:** sort the population by score and compare each adjacent pair AT THE
  PRECISION ABOUT TO BE PUBLISHED. **The precision is adequate when no two rows
  whose real scores DIFFER print the same value.** Two rows whose real scores are
  EQUAL printing the same value is correct and is not a failure; that is what the
  tie-break of 12.13 is for and the reason cell names the key that settled it.
- **WHERE THE TEST FAILS, THE PRECISION IS RAISED**, one place at a time, up to the
  ceiling `SCORE_DECIMAL_PLACES`'s own validation allows. **The precision is never
  LOWERED to tidy the column**, and no score is rounded away, banded or replaced.
- **WHERE THE CEILING IS REACHED AND PAIRS STILL COLLIDE, THE COLUMN STILL SHIPS AT
  THE CEILING AND THE ARTIFACT SAYS SO**, in one line in the Method section naming
  the precision used, how many adjacent pairs still print identically, and that
  those rows are ordered by the terms and the tie-break their reason cells name
  rather than by a difference the printed number can show. **An honest statement
  that the printed number cannot separate two rows is worth more than a reader
  concluding the ordering is arbitrary**, and it is the same shape of disclosure as
  every other bound in this file that can be reached and not cleared.
- **THE SCORE IS NEVER RE-SCALED TO MAKE IT PRINT WELL.** Multiplying the published
  score by a constant to move it away from the floor would break the one thing 26.1
  guarantees, which is that the number on the row is the number the row was ranked
  on. The precision moves; the number does not.

## 26.2 Documents the user supplies are read for EVIDENCE ONLY

SD-PRI-33. A prior period's plan, a spreadsheet someone maintains by hand, a
document a colleague forwarded: read them for CONTENT, and never for FORMAT,
PHRASING or STRUCTURE.

> Prior-period self-written documents are the input problem this method exists
> to fix. Never inherit their shape.

The shape of the deliverable comes from PART 1 and from nowhere else. A
user-supplied document may contribute units, dates, priorities and figures. It
may not contribute a section, a heading, a column order, a cap, or a phrasing
convention. Where such a document contains a heading with no counterpart in
TAB_CONTRACT, that heading does not enter the artifact. This is how a bad house
format stops propagating through an organization because everyone inherited last
period's file.

**AND WHERE THE DOCUMENT'S OWN WORDS CONTRADICT A RESOLVED CELL, THAT IS A THIRD
STATE WITH ITS OWN LABEL, AND NEITHER SIDE WINS.** SD-CNF-10. A person's note
naming a unit, a date or a figure that a column which RESOLVED says something else
about is CONTRADICTED, and contradicted is not the same as either state this run
already had:

- **CONTRADICTED**: a resolved column holds, on the unit the statement names, a
  value the statement cannot be true of. **Where the statement names a UNIT that is
  absent from the source entirely, that is a contradiction of the identity** and
  takes this reading, because the source was read and the unit was not in it.
- **UNSOURCED**: no resolved column addresses the statement at all, and the
  bracketed-placeholder rule of G2 and SD-CNF-08 governs there unchanged.
- **UNVERIFIED**: a column that would address it did not resolve, or resolved and is
  empty within scope, per 3.8 of reference/field-resolution.md. That is a third label again
  and is never reported as a contradiction.

**THREE LABELS, THREE REMEDIES, AND COLLAPSING THEM SENDS THE READER TO THE WRONG
ONE.** A contradiction is settled by somebody saying which source is right; an
absence is settled by finding a source; an unverified statement is settled by
resolving a column. What the run does with a contradiction, and it does all four:

- **NEITHER SOURCE WINS AUTOMATICALLY.** A note is often right and an extract
  stale, late or keyed on a different population; an extract is often right and a
  note written from memory. **A run that picks a winner has decided a question of
  fact it cannot see, and it decides it the same way every time**, which is worse
  than being wrong once because the bias is invisible and repeated.
- **NOTHING CONTRADICTED ENTERS A PERMANENT RECORD.** The item is excluded from
  every claim, count, denominator and ranked figure this artifact publishes, and the
  exclusion is LISTED with its reason rather than being silent. It never contributes
  a unit to a population, a date to a close state or a figure to a term.
- **AND IT IS NEVER DELETED.** Both readings ship: the person's statement in their
  own words, and what the resolved cell says with its column and its unit named,
  **together with the question that would settle which is right**. The run never
  averages the two, never blends them into one sentence and never publishes the
  disputed value. Stripping a contradicted claim out silently deletes the person's
  own record of their work, which SD-CTR-23 names as the most expensive kind of
  loss.
- **IT IS SURFACED TO THE PERSON RATHER THAN RESOLVED BEHIND THEM**, in their own
  language, as a question and not a correction, per SD-CNF-09's preview where the
  run is interactive and in the Method section where it is not.

**AND MANY AT ONCE IS EVIDENCE ABOUT THE EXTRACT RATHER THAN ABOUT THE PERSON.**
Above UNRESOLVED_STOP_COUNT contradicted items the run STOPS, exactly as SD-RUN-09
stops on its own disagreements, and reports that the document and the file appear
to describe different populations rather than working through them one at a time.

## 26.3 Plan for a document built for the eye, not for a parser

SD-PRS-02. The central publication, the compliance reference and most attached
directives are laid out for a human reader, not for a parser. Do not give up on
a table because the first extraction looked like noise.

The ladder:

1. Extract with LAYOUT PRESERVED first.
2. If layout mode is unavailable or the pairing is ambiguous, read the page as an
   IMAGE and treat that as a NORMAL TOOL rather than a last resort.
3. Pair by PROXIMITY, then CONFIRM against a SECOND READING.
4. Report the confidence split: how many pairs were confirmed by two readings,
   how many rest on ONE, and how many could not be paired.

> Two agreeing readings is a confirmed pair; one reading is a candidate.

Where DOCUMENT_EXTRACT is absent entirely, fall to the descending close-weight
ladder in 12.3 for anything whose date could not be read, name every item that
took a fallback weight, and NEVER default an unread date upward.
reference/capability-probe.md 2.12, SD-PRS-03, SD-LNG-05.

---

## 26.4 A closed set must be able to name the ORDINARY case

SD-CTR-29. A CLOSED vocabulary that a run must draw from is only usable if it
carries at least one member for every state this contract can produce, and
coverage is validated IN THAT DIRECTION, from the STATES to the SET, whenever
either changes. A set validated only for internal consistency can be perfectly
well formed and still unable to name the commonest thing that happens.

**THE TEST: for every state the contract can emit, does the closed set contain at
least one member that applies to it?** A state with zero members is a HOLE, and a
hole guarantees an unmapped value on every run in which that state occurs. Where
the holed state is the COMMON case, the set is not merely incomplete, it is
unusable, and it looks complete to anybody who reads it without counting.

The closed sets this skill draws from, and each is validated against the states
beside it, every time either changes:

| Closed set | The states it must cover |
|---|---|
| WORK_TYPES | Every verb class a work item can carry, including the marker-only case at weight zero |
| CLOSE_WEIGHTS with the vocabulary in 12.3.1 | All nine close states, which are exhaustive over the number line by construction |
| EXCEPTION_FLAGS, per shape | Every flag the shape in force can trip |
| PERIOD_TOKEN_MAP | Every token that may appear in a work item name in this organization |
| TAB_CONTRACT at its planning key, with MSG_EMPTY_SECTION | Every section, including each one's empty message |
| The carried-context classes in 1.3d | All seven shape tokens, which the four classes partition |

**A HOLE IS NOT THE SAME THING AS A DELIBERATELY EMPTY ADDITIVE LIST.** A filter
list that starts empty, such as a list of locally banned phrases, is CORRECT when
empty: nothing is filtered yet and nothing is required to produce a value from it.
A VOCABULARY the contract requires a value FROM is a different kind of set, and an
empty family in one is a defect. The test is whether some output cannot be
produced without drawing from the set.

**A member whose implied action is genuinely NONE says so explicitly and names
NOBODY as able to clear it.** An entry that looks actionable and is not sends a
reader to do something about a thing nobody can do anything about, which costs
more than the empty cell it replaced.

Where a state has no member and the set is bound, the run does NOT invent one: it
prints the state, names the set and the state it could not name from it, and
raises the gap with the binding owner as one open request. Inventing a member is
the fabrication SD-CNF-07 forbids.

# PART 27: DOCTRINE COVERAGE INDEX

Every shared doctrine rule whose Applies list includes
PLANNING, with the part of this file where it is in force. A rule with a
location is carried. There are no exceptions and no omissions.

The rules in reference/doctrine/ that do not apply to PLANNING are the REVIEW-only
entries, and they are listed rather than counted, because a count restated
outside the table that derives it drifts the moment a rule is added: SD-CLM-08, SD-CLM-10, SD-CLM-15, SD-CLM-19, SD-CLM-20, SD-CLM-23, SD-CLM-25, SD-CTR-22, SD-CTR-23, SD-IDN-23, SD-IDN-24, SD-LNG-08, SD-LNG-09, SD-LNG-10, SD-LNG-11, SD-SPN-10, SD-SPN-11, SD-SPN-13. SD-CLM-10 is cited in 1.5 anyway, because the altitude ceiling
governs the narrative column here too.


## Group CTR: The output contract and its shape

| ID | Rule | In force at |
|---|---|---|
| SD-CTR-01 | A single declared source of truth for the output | PART 1 |
| SD-CTR-02 | Exactly two deliverable shapes, differing only in three numbers | PART 1 |
| SD-CTR-03 | "Up to" is load bearing on a reference section | PART 1 |
| SD-CTR-04 | Two population figures exist and are published separately | PART 1 |
| SD-CTR-05 | A user-requested size overrides the role default; everything else stays fixed | PART 1 |
| SD-CTR-06 | Three independent request axes compose freely and none changes the shape | PART 1 |
| SD-CTR-07 | Every section ships every run, even with nothing to report | PART 1 |
| SD-CTR-08 | The identity block is structurally identical on every item section | PART 1 |
| SD-CTR-09 | Header strings are byte-identical between runs | PART 1 |
| SD-CTR-10 | Publish the number you ranked on | 26.1 |
| SD-CTR-11 | The rank-within-scope header is the same string at every level | PART 1 |
| SD-CTR-12 | A derived analysis needs BOTH halves of its inputs, and the pair is the admission test | PART 1 |
| SD-CTR-13 | An unresolved column is written blank, never dropped | 1.3b, 1.3c |
| SD-CTR-14 | The items come first; everything explanatory goes after | 19.3 |
| SD-CTR-15 | The audit trail is exhaustive BY DESIGN and sits at the very end | 19.4 |
| SD-CTR-16 | The reply is short and never pastes the list | 19.2 |
| SD-CTR-17 | A one-line heads-up on a large input | 3.5 |
| SD-CTR-18 | Do not send or share the artifact automatically | 19.1 |
| SD-CTR-19 | Every artifact carries the owner's contact line and an invitation to tune | 19.5 |
| SD-CTR-20 | The method is built to be calibrated, and local reality is an INPUT rather than a guess | 19.5 |
| SD-CTR-21 | Transparency exists so a disagreement can be traced rather than argued | 12.1, 22.1 |
| SD-CTR-24 | A bound value outranks a default, and an unbound value never overrides a bound one | 0.2 G6, 14.7, 22 row 54 |
| SD-CTR-26 | A fully answered interview must produce a fully bound run | 3.2 |
| SD-CTR-27 | A derived scope ladder is anchored at BOTH ends, and never on the unit itself | 5.2 |
| SD-CTR-28 | The cost order for a deferred question is computed on this run, never read from a table | PART 1 |
| SD-CTR-29 | A closed set must name the ORDINARY case, and coverage is validated from the states to the set | 26.4 |
| SD-CTR-30 | A default shared by several skills may not carry one skill's content | 1.2, 9.2, 19.1 |
| SD-CTR-25 | Binding authority is ADDITIVE, and answering a question never removes an answerer | 3.4 |

## Group SPN: Span of control

| ID | Rule | In force at |
|---|---|---|
| SD-SPN-01 | Show the levels BELOW the requester, never their own | 1.4 |
| SD-SPN-02 | The inclusion test is mechanical: two conditions plus the unit-level exclusion, and all three must hold | 1.4 |
| SD-SPN-03 | Compute the column set ONCE, over the full ranked population | 1.4 |
| SD-SPN-04 | Compute the distinct-value count from the FILTERED population | 1.4 |
| SD-SPN-05 | When the requester's own level cannot be resolved, include every scope column with more than one value | 1.4 |
| SD-SPN-06 | Scope codes are formatted as text | 1.4 |
| SD-SPN-07 | Filtering a manager's section to one sub-unit does NOT produce that sub-unit's report | 1.4 |
| SD-SPN-08 | The block is for attribution, not delegation | 1.4 |
| SD-SPN-09 | Two claim tiers, and claiming at the wrong grain is fatal in both directions | 1.5 |
| SD-SPN-12 | The self-determined subset is the highest-evidence cut | 6.2 |
| SD-SPN-14 | A peer set is drawn from siblings, never from subordinates | 14.6 |
| SD-SPN-15 | A role at the top of the chain has no internal peer set, and that is a stated result | 14.6 |
| SD-SPN-16 | A peer set that is non-empty and below the anonymity floor is a THIRD state with its own rung, walked outward one level at a time | 14.6 |

## Group FMT: Formatting as a correctness property

| ID | Rule | In force at |
|---|---|---|
| SD-FMT-01 | Formatting is verified, not asserted, and is never traded for speed | 1.10 |
| SD-FMT-02 | Checking a subset and calling it verified is the defect | 1.10 |
| SD-FMT-03 | The freeze point is computed, not fixed; the reason-for-rank column has one position and is never inside the frozen span; and the span is BOUNDED by its summed built width | 1.3 for the position and the bounded walk, 1.10, cited to reference/output-contract.md element 2, 4.1.1 and 4.1.2; verified at 18.1 and 18.2 |
| SD-FMT-04 | Direct cell formatting outranks a style, so the header band must be explicit, and the style's OWN header band must agree in DIRECTION with it rather than oppose it | 1.10, cited to reference/output-contract.md element 5 for the direct band and element 4 for the style's own |
| SD-FMT-05 | The alignment lists are CLOSED at run time, membership is decided by a rule total over the shape tokens, and CENTRE is a third class admitted only on a declared status grid column | 1.10, cited to reference/output-contract.md element 9 and PART 2.5; the shape tokens stay in 1.10, which also declares that this artifact has no status grid column and centres nothing; verified at 18.1 and 18.2 |
| SD-FMT-06 | Read formatting back through the engine, and refuse to publish if you cannot | 1.10, cited to reference/output-contract.md PART 7.1; 18.2 |
| SD-FMT-07 | An empty section is a finished section with nothing in it, its explanatory row sits inside the table range, and a count of rows counts UNITS | 1.2, 1.6, 1.6.1, 1.9, 16.2, 16.4, cited to reference/output-contract.md PART 5.4 |
| SD-FMT-08 | Row height is computed per cell against that cell's own column width, the constant is padding, CHAR_WIDTH_FACTOR runs in one direction with one permitted inversion, and the line count is a WRAP and never a division | 1.10, cited to reference/output-contract.md element 12 and PART 2.2.1, 2.2.3 and 2.3; 17.3, 18.2 |
| SD-FMT-09 | State the check in a falsifiable form | 1.10 |
| SD-FMT-10 | Sampling density must be stated, never assumed | 1.10 |
| SD-FMT-11 | Never put a paragraph in a narrow label column | 1.10 |
| SD-FMT-12 | Verify readability programmatically, not by eye | 1.10 |
| SD-FMT-13 | Title Case every heading, every sheet name and every column header, in one stated convention; the exemption for table column headers is WITHDRAWN and the one that stays is a string the organization BOUND | 1.9 item 8, 1.10, 18.2, cited to the validation of TITLE_CASE_HEADINGS and to reference/output-contract.md PART 7.3 |
| SD-FMT-14 | The character gate tests BOTH bounds | 1.10, cited to reference/output-contract.md element 16; 18.2 |
| SD-FMT-15 | Transliterate, never drop, and never truncate a name | 1.10, 18.2 |
| SD-FMT-16 | Quote the words faithfully and transliterate the characters | 1.10, 18.2 |
| SD-FMT-17 | Source contamination is the main character risk; sweep on the way IN | 1.10, 18.2 |
| SD-FMT-18 | Character verification is mechanical, not visual | 1.10, 18.2 |
| SD-FMT-19 | The character gate applies to authored text, not to binary container bytes | 1.10, 18.2 |
| SD-FMT-20 | Never drop the row and never blank the field to fix a character problem | 1.10, 18.2 |
| SD-FMT-21 | A column the contract makes MANDATORY is never eligible for constant-column removal | 1.3c, 1.3b |
| SD-FMT-22 | The output contract is ONE file, and a rule stated in prose is not enforced | PART 1 opening, 1.10, 18.2, 19.3.1, PART 21 |
| SD-FMT-23 | A header must never be hidden, clipped or half-shown, and the header's character requirement is the narrowest line it can live on inside its budget, floored at its longest single word | 1.10, 17.3, 18.2, cited to reference/output-contract.md elements 10, 12 and 14 and to PART 2.2.1 primitive 3 |
| SD-FMT-24 | Every item section carries a rank and a reason for that rank | 1.3, 1.3b, 1.9, 1.11, 18.1, 18.2, cited to reference/output-contract.md PART 4.1 |
| SD-FMT-25 | A derived last rank is not a row cap, and each capped section is capped independently | 1.6, 1.11, cited to reference/output-contract.md PART 4.2 and PART 5.1 |
| SD-FMT-26 | A note that belongs to a grid has ONE place, the note band below it, the explanatory row of an empty section is not one, and a statement required in two places is RECONCILED rather than repeated | PART 1 opening, 1.6, 1.6.1, 1.9, 16.4, 18.1, 18.2, 19.4, cited to reference/output-contract.md PART 5.3 and PART 5.4 |
| SD-FMT-27 | A verification never scans its own record, and one colour never carries two meanings, so a classification palette is INJECTIVE and disjoint from the alert palette | 1.10, 18.2, and 19.4 item 4m for the declared range; the palettes are element 13's alone here, because 1.10's second declaration adopts no classification column |
| SD-FMT-28 | A grid's TOTAL width is bounded as well as each column's; the bound is declared before the columns are built and never raised to clear a failure; and what gives is a repeated standing qualifier, never a column, a header floor or a meaning | 1.10 for the citation, 17.3 for the declaration and the measurement, 18.2 for the assertion, cited to reference/output-contract.md PART 2.7 and element 10 |
| SD-FMT-29 | Formatting must degrade safely, because the author verifies in the renderer that built the file and the reader opens another: a text-and-band pair is asserted against the intended pairing and against BOTH degraded renderings, every colour carries an explicit opaque alpha, and two layers that can produce one property agree in direction; and the MECHANISM is chosen for the engine the reader opens rather than the one the file was built in, with the check reading the property back from where the reader meets it | 1.10 for the position statement and the citation, 1.2.1 and 1.6.1 for element 7's sheet-wide reach, 18.2 for the assertions, cited to reference/output-contract.md PART 2.8, PART 2.9, elements 4, 5, 7 and 15, and PART 7.2 rows 5, 6, 7, 15 and C1; 17.3 for the filter mechanism |
| SD-FMT-30 | A word is never broken by a cell line: any string wider than its own cell is placed in a MERGED region spanning exactly what it needs and never merely styled across it, every column is floored at the longest unbreakable token it must display, and a token past the column cap is reported rather than broken | 1.10 for the position statement, 17.3 for the merge and the width floor, 18.2 for both assertions, cited to reference/output-contract.md PART 2.10, PART 2.2.1 primitive 4, PART 2.2.2 step 3b, elements 7, 8, 10 and 15, and PART 7.2 rows 7, 10 and C3 |

## Group RNK: Rank continuity, caps and cuts

| ID | Rule | In force at |
|---|---|---|
| SD-RNK-01 | Ranks form one unbroken sequence across the merit sections | 1.6, cited to reference/output-contract.md PART 4.2 |
| SD-RNK-02 | Derived ceilings are consequences, never independent caps | 1.6, cited to reference/output-contract.md PART 4.2 |
| SD-RNK-03 | A check that asserts the wrong number fails a correct artifact and burns the budget | 1.6 |
| SD-RNK-04 | The mandatory section is not a merit section and never consumes a merit slot | 1.6 |
| SD-RNK-05 | The cap counts rows on the SECTION, not positions in the ranked list | 1.6, cited to reference/output-contract.md PART 4.3 and PART 5.1 |
| SD-RNK-06 | Write the shortfall note if and only if n is strictly less than N; the showing note is a different note and is never omitted; and a sheet is bounded by a cap, a tier size or a declared extract size, each giving N its own meaning | 1.6, which reads N from reference/output-contract.md PART 5.1.1 per section and where the SHORTFALL note is this skill's own; 1.3d; verified at 18.2 |
| SD-RNK-07 | Cut an over-capped mandatory list by the honest axis, and name that axis | 11.8 |
| SD-RNK-08 | Do not extend the action lists to absorb overflow | 1.6 |
| SD-RNK-09 | The action list gets shorter RELATIVE TO SPAN as scope widens | 1.1 |
| SD-RNK-10 | A final identifier key on every capped sort is mandatory, not decorative | 1.6 |
| SD-RNK-11 | Sort by the value, never by the classification label | 1.6 |

## Group EFF: Effort, stopping and failing closed

| ID | Rule | In force at |
|---|---|---|
| SD-EFF-01 | There is no time limit, and run length is not a cost the method recognizes | 0.8 |
| SD-EFF-02 | The stop list is closed and enumerated | 20.1 |
| SD-EFF-03 | Fail closed: unknown is not pass | 18.4 |
| SD-EFF-04 | A labelled partial is still a partial | 18.4 |
| SD-EFF-05 | A bannered partial that names what is missing is better than nothing | 18.4 |
| SD-EFF-06 | Two meanings of "empty" that must never be confused | 18.4 |
| SD-EFF-07 | No stage may weaken an earlier stage's guarantee, and every gate RE-CHECKS the previous one | PART 4 |
| SD-EFF-08 | Any unresolved item propagates | PART 4 |
| SD-EFF-09 | Retry is graduated, not counted | 20.2 |
| SD-EFF-10 | An empty or failed read is UNCONFIRMED, never failed, until the ladder says otherwise | 20.2 |
| SD-EFF-11 | One constraint relaxed, and a doctrine rule is never a relaxable constraint | 20.2 |
| SD-EFF-12 | "No forward progress" is the termination condition, and it is measured relatively | 20.2 |
| SD-EFF-13 | Never let a worker's optimism advance the run | 17.3 |
| SD-EFF-14 | A stage that cannot write its checkpoint has failed | 17.1 |
| SD-EFF-15 | A worker failure is isolated to its own partition | 17.5 |
| SD-EFF-16 | Only genuinely independent stages run in parallel, and never across a gate | PART 4 |
| SD-EFF-17 | Partition deterministically, and verify the MERGE rather than the workers | 17.5 |
| SD-EFF-18 | Nothing that needs the whole population may be computed inside a partition | 17.5 |
| SD-EFF-19 | Read back the TAIL of a chunk, never the head | 17.3 |
| SD-EFF-20 | Never mix data writes with structural operations in one call | 17.3 |
| SD-EFF-21 | Data first, structure second, PER unit, never one structural call for the whole artifact | 17.3 |
| SD-EFF-22 | Build order is by ACTUAL size, largest first | 17.2 |
| SD-EFF-23 | Finish each unit completely before starting the next | 17.2 |
| SD-EFF-24 | Last in the order never means finished with less care | 17.2 |
| SD-EFF-25 | A unit is not complete until its data AND its formatting are verified | 17.2 |
| SD-EFF-26 | The only permitted deletion is strictly bounded | 17.4 |
| SD-EFF-27 | Persist the computed result before building, and require reproducibility | 17.1 |
| SD-EFF-28 | Publish only once, at the end | 17.6 |
| SD-EFF-29 | A stale checkpoint is worse than none | 20.3 |
| SD-EFF-30 | Write continuously; never hold more than one stage in memory | 17.1 |
| SD-EFF-31 | The checkpoint holds ledgers only and is never mistakable for a result | 17.1 |
| SD-EFF-32 | Never present incomplete work as finished, in chat or in the file | 19.7 |
| SD-EFF-33 | A checkpoint failure degrades durability, not correctness | 17.1 |
| SD-EFF-34 | Route every failure to a stage that can REMEDIATE it, never to one that only evaluates | PART 4 |
| SD-EFF-35 | Remediation never re-asks a question already answered | PART 4 |
| SD-EFF-36 | Per-gate and global remediation budgets both exist | PART 4 |
| SD-EFF-37 | Not applicable is a passing state | PART 4 |
| SD-EFF-38 | Ask questions to buy time | PART 4 |

## Group RUN: Run architecture and verification design

| ID | Rule | In force at |
|---|---|---|
| SD-RUN-01 | A supervised swarm, not one long script | PART 4 |
| SD-RUN-02 | Every stage has the same six-field contract | PART 4 |
| SD-RUN-03 | Two verifiers are independent only when they answer DIFFERENT questions | 18.3 |
| SD-RUN-04 | Never reconcile against a single ledger | 18.3 |
| SD-RUN-05 | Reconcile only what BOTH verifiers can independently emit | 18.3 |
| SD-RUN-06 | NOT REFUTED is not confirmation | 18.3 |
| SD-RUN-07 | A declared incompatibility outranks any corroboration verdict | 18.3 |
| SD-RUN-08 | A sparse population is not a mispairing | 18.3 |
| SD-RUN-09 | Never average two disagreeing derivations, and never publish a disputed value | 18.3 |
| SD-RUN-10 | Named regression cases run before any change ships | 24.1 |
| SD-RUN-11 | Freeze a ground-truth classification and gate on reproducing it exactly | 12.5 |
| SD-RUN-12 | The portability test is two real files of the same source, months apart | 24.2 |
| SD-RUN-13 | Version stamp, what changed, and what was verified versus not | 24.3 |
| SD-RUN-14 | Compute every figure with a tool, never mentally | 12.14 |
| SD-RUN-15 | A run that cannot be reproduced cannot be trusted | 12.13 |

## Group IDN: Identity, role and scope

| ID | Rule | In force at |
|---|---|---|
| SD-IDN-01 | The manager lookup is mandatory and non-substitutable | 5.1, 5.2 |
| SD-IDN-02 | Only one person in the organization has no supervisor | 5.1, 5.2 |
| SD-IDN-03 | A scope word outranks a role word, and that test runs FIRST | 5.1, 5.2 |
| SD-IDN-04 | Expand abbreviations before matching, and take the most senior token | 5.1, 5.2 |
| SD-IDN-05 | Losing the directory costs the shortcuts, not the deliverable | 5.1, 5.2 |
| SD-IDN-06 | Nothing may be hard-coded from the reference data | 5.3 |
| SD-IDN-07 | An ambiguous identifier is resolved against the DATA, never against its own pattern | 5.3 |
| SD-IDN-08 | One tie-break for ambiguity, used everywhere: the word, then the role | 5.3 |
| SD-IDN-09 | Compare identifiers as TEXT on both sides | 5.3 |
| SD-IDN-10 | If the requested scope is at or above everything the file contains, apply no filter | 5.3 |
| SD-IDN-11 | The user speaks naturally; the skill does the arithmetic | 5.3 |
| SD-IDN-12 | Search every record before asking, and asking is the last resort | 3.3 |
| SD-IDN-13 | When you must ask, ask in the user's language, not the file's | 5.3 |
| SD-IDN-14 | Narrow before asking | 5.3 |
| SD-IDN-15 | Persist a settled answer and verify the save succeeded | 5.3 |
| SD-IDN-16 | Zero rows means the filter is wrong before it means the scope is empty | 5.3 |
| SD-IDN-17 | Batch every question into a single message | 5.3 |
| SD-IDN-18 | Ask only for REQUIRED concepts; never ask for optional ones | 5.3 |
| SD-IDN-19 | Propose, do not prompt | 3.3 |
| SD-IDN-20 | Never ask what the tools can answer, and keep every question under thirty seconds | 5.3 |
| SD-IDN-21 | Blocking and non-blocking questions have different failure semantics | 5.3 |
| SD-IDN-22 | Question batching is arithmetic, not judgment | 5.3 |
| SD-IDN-25 | A question never fires before the stage that supplies its context | 5.3 |

## Group QUA: Qualifiers and population selection

| ID | Rule | In force at |
|---|---|---|
| SD-QUA-01 | Classify the phrase by TYPE before searching any column | PART 6 |
| SD-QUA-02 | Never run a match across the whole sheet | PART 6 |
| SD-QUA-03 | Two axes, because a single label routes flags into arithmetic | PART 6 |
| SD-QUA-04 | Resolve absence phrases by RULE, before any value search | PART 6 |
| SD-QUA-05 | Convert a name to its stored code through a table; substring matching cannot do the conversion | PART 6 |
| SD-QUA-06 | An administrative suffix is a routing cue, not noise | PART 6 |
| SD-QUA-07 | The match cascade, in order, confined to routed columns | PART 6 |
| SD-QUA-08 | A compound phrase splits before classification and applies with AND | PART 6 |
| SD-QUA-09 | Qualifiers are applied in the scope stage, before every exclusion and before the percentile | PART 6 |
| SD-QUA-10 | A miss is reported loudly, with three outcomes that must never be collapsed | PART 6 |
| SD-QUA-11 | Distinguish "the column is absent" from "the value is not in it" | PART 6 |
| SD-QUA-12 | Never silently widen | PART 6 |
| SD-QUA-13 | Downstream guards work unmodified on a qualified population | PART 6 |
| SD-QUA-14 | Record what was routed, resolved and matched, with counts | PART 6 |

## Group PRI: Priorities and direction

| ID | Rule | In force at |
|---|---|---|
| SD-PRI-01 | All sources, every run, with the nearest one first | PART 8 |
| SD-PRI-02 | Sweep everything by SENDER; never filter the sweep by keyword | PART 8 |
| SD-PRI-03 | Classify by CONTENT, not by keyword and not by length; when in doubt, KEEP | PART 8 |
| SD-PRI-04 | Never conclude an absence from the wrong instrument | PART 8 |
| SD-PRI-05 | Reading and acting are two separate decisions | PART 8 |
| SD-PRI-06 | Walk the chain upward, and weight by distance | PART 8 |
| SD-PRI-07 | Record every level, including the ones that published nothing | PART 8 |
| SD-PRI-08 | Carry-forward is evaluated MANAGER BY MANAGER, and the narrower test runs first | PART 8 |
| SD-PRI-09 | Name the rule an implementer will skip, and say so | PART 8 |
| SD-PRI-10 | A mandatory item's weight never decays with the age of the instruction | PART 8 |
| SD-PRI-11 | ANY list from anyone in the chain is a must-cover; no trigger phrase is required | PART 8 |
| SD-PRI-12 | Apply the ACTOR TEST before treating a list as a directive | 8.7, with the recipient resolved rather than assumed at 8.7.1 wherever a direction carries no addressing evidence |
| SD-PRI-13 | When in doubt, treat it as directed | 8.7, scoped at 8.7.1 to doubt about whether to COVER a unit and never to doubt about WHO must act |
| SD-PRI-14 | Match a named item to a row by a stated ladder, and report what will not match | PART 8 |
| SD-PRI-15 | Never infer an item's identity from an aggregate | PART 8 |
| SD-PRI-16 | Unresolvable direction is surfaced and changes nothing about the ranking | PART 8 |
| SD-PRI-17 | A directive from a supervisor never skips the compliance gate | 9.3 |
| SD-PRI-18 | Locally tagged work is the strongest signal in the file, and the test runs on UNPADDED digits | 12.6 |
| SD-PRI-19 | A top-level user has no scope code, so nothing is local to them | 12.6 |
| SD-PRI-20 | A DIRECT local tag overrides a work-type zero; a BROADER one does not | 12.6 |
| SD-PRI-21 | Foreign-unit tags are kept, scored and labelled, never silently dropped | 10.5 |
| SD-PRI-22 | A published external classification is EVIDENCE, not an override | 12.5 |
| SD-PRI-23 | "Requires my action" is a PUBLISHED marker, not a reading of the sentence | 12.7 |
| SD-PRI-24 | A narrow instruction is a sharper priority than a blanket one | 12.7 |
| SD-PRI-25 | Source boost is scaled by the naming level's distance, and the NEAREST namer wins | 12.7 |
| SD-PRI-26 | Two distinctive tokens, or one SPECIFIC name; a family name never matches alone | 12.7 |
| SD-PRI-27 | A family-level mention still counts, just not as a match | 12.7 |
| SD-PRI-28 | Stem before comparing | 12.7 |
| SD-PRI-29 | Show the tokens, or you did not run the test | 12.7 |
| SD-PRI-30 | A run where nothing matched is a real result and must be visible | 12.7 |
| SD-PRI-31 | Priority ranking comes from the organization's published weights, not the writer's opinion | 12.7 |
| SD-PRI-32 | The source hierarchy is a map from QUESTION to artifact, not a ranking of documents | PART 8 |
| SD-PRI-33 | User documents are read for EVIDENCE ONLY | 26.2 |

## Group SRC: Acquiring sources

| ID | Rule | In force at |
|---|---|---|
| SD-SRC-01 | Retrieving an attached list is mandatory work, not best effort | 8.9, 8.10 |
| SD-SRC-02 | THE RETRIEVAL GATE: a zero count is only valid when nothing was sent | 8.9, 8.10 |
| SD-SRC-03 | A partial recovery is treated as partial, but a partial FETCH is not the same as partial DATA | 8.9, 8.10 |
| SD-SRC-04 | Enumerate the plausible-but-wrong approaches and say which one fails silently | 8.9, 8.10 |
| SD-SRC-05 | Do not select a field you were told to read; request the resource and read it out | 8.9, 8.10 |
| SD-SRC-06 | The same address is correct streamed and corrupt decoded as text | 8.9, 8.10 |
| SD-SRC-07 | Never decide from a subject line whether a message carries a file | 8.9, 8.10 |
| SD-SRC-08 | An encoded size is not a file size | 8.9, 8.10 |
| SD-SRC-09 | A spilled response is not an empty response | 8.9, 8.10 |
| SD-SRC-10 | A recent file will not be in search yet | 8.9, 8.10 |
| SD-SRC-11 | Asking the user to fetch it is the last step, and it names everything attempted | 8.9, 8.10 |
| SD-SRC-12 | Never ask the user to fetch something the skill can read | 8.9, 8.10 |
| SD-SRC-13 | The central source is never optional, and it is never a reason to stop | 7.1, 8.11 |
| SD-SRC-14 | Discover the path every run; never hard-code it | 7.1, 8.11 |
| SD-SRC-15 | Resolve the source for the period being PLANNED, not "the latest" | 7.1, 8.11 |
| SD-SRC-16 | Cache what does not vary, fetch live what does | 7.3 |
| SD-SRC-17 | The expiry gate is blocking, per cached block | 7.3 |
| SD-SRC-18 | A stale reference is a disclosed limitation; a halted run is a dead end | 7.3 |
| SD-SRC-19 | A refreshed block is reported back so one file stays authoritative | 7.3 |
| SD-SRC-20 | Attachments on a live source message are part of the source, not an extra | 8.11 |
| SD-SRC-21 | Reading the published standard is mandatory, never assumed, and never a stop | 8.11, 20.1.4 |

## Group PRS: Parsing and resolution

| ID | Rule | In force at |
|---|---|---|
| SD-PRS-01 | The published table is authoritative for dates, types and eligibility; parse it, do not infer | 8.11 |
| SD-PRS-02 | Plan for a document built for the eye, not for a parser | 26.3 |
| SD-PRS-03 | An unreadable date is banded down, never defaulted up | 7.1, 12.3 |
| SD-PRS-04 | Read the date; never assume the window | 7.1, 12.3 |
| SD-PRS-05 | An unreadable window is derived, not fatal | 7.1, 12.3 |
| SD-PRS-06 | Anchor a structural block on the DATA, not on the dictionary | 10.3 |
| SD-PRS-07 | Match a boundary token EXACTLY and take the RIGHTMOST match | 10.3 |
| SD-PRS-08 | Never use an optional metadata prefix as the admission test | 10.3 |
| SD-PRS-09 | A global count row is never used for scoring | 10.4 |
| SD-PRS-10 | Compute per-item counts from the FILTERED scope yourself | 10.4 |
| SD-PRS-11 | Never take the first sheet on faith, and a name match still needs a column check | 10.1, 10.2 |
| SD-PRS-12 | When no single source covers the requested scope, concatenate rather than choose | 10.1, 10.2 |
| SD-PRS-13 | Detect the header row rather than assuming it | 10.1, 10.2 |
| SD-PRS-14 | Three matching passes, each run to completion before the next | 10.1, 10.2 |
| SD-PRS-15 | A short-string guard on fuzzy matching | 10.1, 10.2 |
| SD-PRS-16 | Confirm a resolved column by its VALUES, not only by its name | 10.1, 10.2 |
| SD-PRS-17 | Coerce before comparing; a typed comparison against the wrong type fails silently | 10.1, 10.2 |
| SD-PRS-18 | A resolved but EMPTY column is an absent column | 10.1, 10.2 |
| SD-PRS-19 | Normalize null-like VALUES, not just empty cells | 10.1, 10.2 |
| SD-PRS-20 | Register the STEM, never the full literal | 10.1, 10.2 |
| SD-PRS-21 | Unit and time-basis markers are interchangeable and must be recorded | 10.1, 10.2 |
| SD-PRS-22 | A header that does not resolve is a skill defect, not a user error | 10.1, 10.2 |
| SD-PRS-23 | Record every ambiguous resolution and who decided it | 10.1, 10.2 |
| SD-PRS-24 | Never analyze a partial source, and count RECORDS rather than the reported extent | 10.1, 10.2 |
| SD-PRS-25 | The admission test for an input is column coverage, not its title | 10.1, 10.2 |
| SD-PRS-26 | Escalate up the hierarchy for an input, then filter down | 10.1, 10.2 |
| SD-PRS-27 | Decide which of several inputs is which BEFORE parsing | 10.1, 10.2 |
| SD-PRS-28 | Do not caveat a matching supplied input | 10.1, 10.2 |
| SD-PRS-29 | Duplicate identifiers: MERGE the signals, do not just keep the best row | 10.1, 10.2 |
| SD-PRS-30 | Sanitize text at the boundary, on the way IN, not as a cleanup pass | 10.1, 10.2 |
| SD-PRS-31 | A valid join key is near-unique in both files and produces a one-to-one match | 14.4 |
| SD-PRS-32 | The overlap floor is a hard stop | 14.4 |
| SD-PRS-33 | With three or more files, chain pairwise against one anchor and report what was used | 14.4 |
| SD-PRS-34 | Orient before you test for unit drift | 14.3 |
| SD-PRS-35 | Concentration near the factor is the test, not tightness | 14.3 |
| SD-PRS-36 | Restrict the drift test to columns already typed as measures | 14.3 |
| SD-PRS-37 | A small factor might be a real result; never correct it silently | 14.3 |
| SD-PRS-38 | A header token mismatch is evidence, not an automatic block | 14.3 |
| SD-PRS-39 | Rate, unit and lookback are three separate properties, and conflating them is fatal | 14.2 |
| SD-PRS-40 | On a block, compute nothing for that pair until it resolves | 14.2 |
| SD-PRS-41 | Alias matching is normalized, not literal | 10.2 |
| SD-PRS-42 | An alias that is a common word or carries punctuation needs a sentinel | 10.2 |
| SD-PRS-43 | A sub-entity inherits its parent; an unrecognized alias is flagged, never guessed | 10.2 |
| SD-PRS-44 | Confirm the SCALE of a column by reading its own maximum, every run | 10.2 |
| SD-PRS-45 | Null handling changes the count and must be STATED | 10.2 |
| SD-PRS-46 | Check that two periods match before dividing, and say what you found | 15.6 |
| SD-PRS-47 | No stem belongs to two concepts, and a tie on a strict concept is never broken by position | 10.2 |
| SD-PRS-48 | A second file carrying the evidence is JOINED on a shared identifier, not left unread | 10.1.1, whose admission test has TWO limbs so a file of well-typed columns that match no concept is still reached, and its consequences at 1.3d, 11.1, 12.10 and 16.2 |

## Group POP: Population exclusions and the pipeline order

| ID | Rule | In force at |
|---|---|---|
| SD-POP-01 | Exclude unreachable units before anything else, with no exception | 11.2 |
| SD-POP-02 | THE PIPELINE ORDER, stated once and authoritative | 11.1 |
| SD-POP-03 | The same phrase can mean two different medians, and the difference must be stated | 11.1 |
| SD-POP-04 | Resolve the mandatory set BEFORE the class exclusion; the ordering is mandatory | 11.4 |
| SD-POP-05 | Resolve an exclusion flag by EXACT column name only | 11.3 |
| SD-POP-06 | A missing exclusion flag means NO exclusion, stated plainly | 11.3 |
| SD-POP-07 | Use the source's own flag rather than a maintained name list | 11.3 |
| SD-POP-08 | Three escapes from an exclusion, and only three | 11.3 |
| SD-POP-09 | Keep a rule that costs nothing when it does not fire | 11.3 |
| SD-POP-10 | Report the exclusion every run: counts removed, counts readmitted per escape, and the threshold used | 11.3 |
| SD-POP-11 | There is NO measure floor. Rank the whole population. | 11.5 |
| SD-POP-12 | A unit with no history is RANKED LAST, never dropped | 11.5 |
| SD-POP-13 | USABLE MEASURE, redefined and exact | 11.5 |
| SD-POP-14 | The percentile never reaches zero, which is why the ZERO BUCKET is mandatory | 11.5 |
| SD-POP-15 | The bucket is a sort key, never a score adjustment | 11.5 |
| SD-POP-16 | The percentile definition is mandatory and exact | 11.5 |
| SD-POP-17 | A class served under a different operating model is REMOVED, not down-weighted | 11.3 |
| SD-POP-18 | Guard every divisor before dividing, including a target of zero | 11.7 |
| SD-POP-19 | A median over fewer than the minimum population is not a norm | 11.7 |
| SD-POP-20 | The population funnel publishes TWO numbers per step | 11.6 |
| SD-POP-21 | Detect the population shape and let it change the denominator, never the deliverable | PART 23 |
| SD-POP-22 | In a flowing population, exclusion by stage is an exclusion, not a filter | PART 23 |
| SD-POP-23 | Shape is a property of the POPULATION being scored, not of the company | 23.0, 3.2.1 |
| SD-POP-24 | Shape is detected by three tests, and the third one decides | 23.0, 3.2.1 |
| SD-POP-25 | Below the minimum rankable population, a ranked list is not a deliverable | 11.7.1, 14.6 |
| SD-POP-26 | The unit of business must sit at or below the reader's own scope, and a mismatch is detected | 11.7.2, 14.6 |
| SD-POP-27 | A measure that is uniform across the whole population contributed nothing, and the output says so | 11.7.3, 14.8.2 |
| SD-POP-28 | A status column that resolved is READ, and the default is not "include everything" | PART 23 |
| SD-POP-29 | A character-length threshold is not a matching rule, and a value match is by whole tokens | 11.2.1 |
| SD-POP-30 | The not-workable exclusion is a FORWARD-LOOKING test, and this skill takes the forward-looking reading on every run and names which reading it applied | 11.2 |

## Group WGT: The weighting hierarchy

| ID | Rule | In force at |
|---|---|---|
| SD-WGT-01 | The entity hierarchy table has NO default row | 12.8 |
| SD-WGT-02 | When a default IS correct, tie it to the hierarchy FLOOR, not to a literal | 12.8 |
| SD-WGT-03 | Protect the item while flooring its weight | 12.8 |
| SD-WGT-04 | The mandatory multiplier is applied ONCE, on the finished score | 12.8 |
| SD-WGT-05 | Entity weight scales the alignment term ONLY, and never reorders the list by itself | 12.8 |
| SD-WGT-06 | The user is never expected to know the internal taxonomy | 12.8 |
| SD-WGT-07 | A word naming a whole segment steers to our entry in it, but its measure includes others | 12.8 |
| SD-WGT-08 | A named initiative is a steer and is not an entity | 12.8 |
| SD-WGT-09 | Rank on the OWN measure, never the segment measure, and never let position decide it | 11.5 |
| SD-WGT-10 | Not all work is equally valuable: weight by WORK TYPE on a closed graduated scale | 12.5 |
| SD-WGT-11 | A marker is not an instruction | 12.5 |
| SD-WGT-12 | Work-type weight multiplies the ALIGNMENT term and nothing else | 12.5 |
| SD-WGT-13 | Scan the WHOLE name for every verb, then take the HIGHEST type present | 12.5 |
| SD-WGT-14 | A generic verb sets no type of its own and only promotes upward from below | 12.5 |
| SD-WGT-15 | Verbless names are classified by the NOUN, never defaulted and never dropped | 12.5 |
| SD-WGT-16 | Classify by the VERB, not by the SUBJECT | 12.5 |
| SD-WGT-17 | Never rank on how many work items an entity carries | 12.4 |
| SD-WGT-18 | The measure weighting is universal and any new signal inherits it | 12.12 |
| SD-WGT-19 | Apply the measure exactly ONCE per output | 12.12 |
| SD-WGT-20 | A membership gate belongs only where membership is by flag | 12.12 |

## Group DUP: The de-duplication of effort

| ID | Rule | In force at |
|---|---|---|
| SD-DUP-01 | The coverage-duplication down-weight applies to the direct-action line ONLY | 12.9 |
| SD-DUP-02 | Classification is line-independent; only the WEIGHT is gated | 12.9 |
| SD-DUP-03 | On the senior line the assignment is still identified and reported, just not weighted | 12.9 |
| SD-DUP-04 | Derive the other actor's unit set from the code, do not pattern-match the digits | 12.9 |
| SD-DUP-05 | An absent second actor is a NORMAL result, not a failure | 12.9 |
| SD-DUP-06 | Discount only when the unit's ONLY open work is the other actor's | 12.9 |
| SD-DUP-07 | Scale rather than exclude, so a big opportunity still surfaces | 12.9 |

## Group MND: The mandatory set

| ID | Rule | In force at |
|---|---|---|
| SD-MND-01 | A mandatory set is built from an explicit LIST, never from a per-unit flag column | 11.4 |
| SD-MND-02 | Two doors for the same work is not two mandatory sets | 11.4 |
| SD-MND-03 | Mandatory membership never depends on the score | 11.4 |
| SD-MND-04 | Mandatory units sit in their own section, outside the ranked lists | 11.4 |

## Group SCO: Scoring

| ID | Rule | In force at |
|---|---|---|
| SD-SCO-01 | Close date FIRST, and rule one is primary and sufficient on its own | 12.2 |
| SD-SCO-02 | Admission and weight are separate answers from ONE matcher | 12.2 |
| SD-SCO-03 | The operating cycle is the only authority for when work is due | 7.2, 12.2 |
| SD-SCO-04 | Precedence stated once so nothing has to be re-derived | 7.2, 12.2 |
| SD-SCO-05 | Anything with no derivable date is DROPPED from scoring entirely | 12.3 |
| SD-SCO-06 | Expired prior-period work stays visible at the floor weight and contributes ZERO to workload | 12.3, 12.3.1 |
| SD-SCO-07 | Each close weight has exactly one defined trigger | 12.3, 12.3.1 |
| SD-SCO-08 | A SCORING item requires all three conditions, and one subsumes another | 12.4 |
| SD-SCO-09 | Every gap term has a NAMED SOURCE so two implementers score the same units | 12.10 |
| SD-SCO-10 | A shared source column does not mean a shared test; compute the overlap | 12.10 |
| SD-SCO-11 | A term whose source does not resolve is not scored and NEVER becomes a default | 12.10 |
| SD-SCO-12 | Cap the COUNT first, then multiply; never cap the product | 12.11 |
| SD-SCO-13 | Alignment and workload are different populations on purpose | 12.11 |
| SD-SCO-14 | The scoring formula, written out and implemented exactly | 12.1 |
| SD-SCO-15 | Say what the multiplicative shape actually does, so nobody re-derives it wrongly | 12.1 |
| SD-SCO-16 | A deterministic tie-break is mandatory, and its measure is the run's own basis | 12.13 |
| SD-SCO-17 | A window named for a period covers every day of that period | 7.1 |

## Group STR: The steer

| ID | Rule | In force at |
|---|---|---|
| SD-STR-01 | A lean and a restriction are not the same request | PART 13 |
| SD-STR-02 | The lean transform is exact, deterministic, and its consequence is written out | PART 13 |
| SD-STR-03 | Taking the named entity ABOVE the standing top is what makes a lean mean anything | PART 13 |
| SD-STR-04 | A lean toward a low-ranked entity deliberately inverts the standing hierarchy | PART 13 |
| SD-STR-05 | Verify a lean did not silently become a restriction | PART 13 |
| SD-STR-06 | A restriction changes the population AND the measure basis, and is applied in the scope stage | PART 13 |
| SD-STR-07 | Never refuse an entity request because one column is absent | PART 13 |
| SD-STR-08 | Zero survivors switches to the lean, and the measure basis reverts WITH it | PART 13 |
| SD-STR-09 | Filler words are stripped before reading the mode | PART 13 |
| SD-STR-10 | When genuinely ambiguous, prefer the RECOVERABLE reading and say so in one line | PART 13 |
| SD-STR-11 | A steer re-weights; it never overrides what leadership asked for | PART 13 |
| SD-STR-12 | An entity-level steer never enters the formula as an additive term | PART 13 |

## Group CMP: Comparing two periods

| ID | Rule | In force at |
|---|---|---|
| SD-CMP-01 | Never infer change from one snapshot, and say nothing about trend unless asked | PART 14 |
| SD-CMP-02 | Make two inputs apples to apples before comparing | PART 14 |
| SD-CMP-03 | A zero baseline is a new-entry case, not an infinity | PART 14 |
| SD-CMP-04 | The comparison score carries the full bracket, not just the measure weighting | PART 14 |
| SD-CMP-05 | A comparison changes the ranking basis, never the deliverable shape | PART 14 |
| SD-CMP-06 | The peer set is defined by the period-end file | PART 14 |
| SD-CMP-07 | A two-pass split must NOT change the denominator, and two passes is not sampling | PART 14 |
| SD-CMP-08 | A comparison request against a population with no prior period is answered, not stopped | 14.1, 20.1.3 |
| SD-CMP-09 | Test the EXIT side separately, because a survivor-only prior file scores perfectly on an overlap test | 14.2.1, 23.4 |

## Group EXC: The exception list

| ID | Rule | In force at |
|---|---|---|
| SD-EXC-01 | An exception list answers a different question from a ranked list and never touches the ranking | PART 16 |
| SD-EXC-02 | A recency threshold SCALES with the local cadence | PART 16 |
| SD-EXC-03 | An ALERT is a different instrument from a MEMBERSHIP flag, and it does NOT scale | PART 16 |
| SD-EXC-04 | Count the alert over the whole population, not over displayed rows | PART 16 |
| SD-EXC-05 | A gate must allow a subset relationship it created itself | PART 16 |
| SD-EXC-32 | A band nobody can reach is not a band, and thresholds are relative to what evaluated | 16.3 |
| SD-EXC-06 | Report a zero count, because it is the evidence the check ran | PART 16 |
| SD-EXC-07 | Date arithmetic rules stated explicitly, including the error case | PART 16 |
| SD-EXC-08 | Run only the flags whose columns resolved AND carry data; never treat an absent column as a gap | PART 16 |
| SD-EXC-09 | Weight the flags, do not count them | PART 16 |
| SD-EXC-10 | The measure multiplier has a HALF FLOOR so a real problem at a small unit stays visible | PART 16 |
| SD-EXC-11 | Band AFTER the multiplier, and set the thresholds against the post-multiplier range | PART 16 |
| SD-EXC-12 | A signal that lags reality is disclosed, and weighted only where it is the subject | PART 16 |
| SD-EXC-13 | Report the local benchmark alongside each figure so an outlier is legible as one | PART 16 |
| SD-EXC-14 | A gap the person cannot close is not a gap worth printing, and there are TWO tests | 16.2 |
| SD-EXC-15 | Two flags are needed because one cannot fire where the other applies | PART 16 |
| SD-EXC-16 | Show both sides, never the delta alone | PART 16 |
| SD-EXC-17 | Note when a unit appears on two sections, because that is two independent reads on the same problem | PART 16 |
| SD-EXC-18 | The economics gate, not a geography gate | PART 16 |
| SD-EXC-19 | Do NOT suppress an opportunity because most local peers also lack it | PART 16 |
| SD-EXC-20 | Benchmark ONE LEVEL WIDER than the user's own slice | PART 16 |
| SD-EXC-21 | Report the benchmark once, do not repeat it per row | PART 16 |
| SD-EXC-22 | Some values are SHOWN, never SCORED, and never confer membership | 16.7, 1.3d |
| SD-EXC-23 | State no interpretation of a value whose meaning varies by jurisdiction | PART 16 |
| SD-EXC-24 | Do not build a second version of something that already has a system of record | PART 16 |
| SD-EXC-25 | Check a field's fill rate before building on it | 16.9, 1.3d |
| SD-EXC-26 | Exemptions are kept as belt and braces after the upstream fix | PART 16 |
| SD-EXC-27 | Do not extend a narrow exemption by analogy | PART 16 |
| SD-EXC-28 | Compliance is checked BEFORE weighting, and it is a guardrail rather than an optimization | PART 9 |
| SD-EXC-29 | A compliance gate fails closed on the priorities, not on the run | PART 9 |
| SD-EXC-30 | Never silently drop a priority | PART 9 |
| SD-EXC-31 | A local exception in a reference field is honoured and never guessed at | PART 9 |

## Group BRD: Breadth and derived analysis

| ID | Rule | In force at |
|---|---|---|
| SD-BRD-01 | A derived analysis section never touches the ranking, and says so | PART 15 |
| SD-BRD-02 | Know what your measure actually measures | PART 15 |
| SD-BRD-03 | Where the method breaks its own rule, it says so and gives the reason | PART 15 |
| SD-BRD-04 | A peer norm and a scope median use DIFFERENT populations by design, and both are stated | PART 15 |
| SD-BRD-05 | Evaluate classification rules in order, stop at the first match, and say which overrides which | PART 15 |
| SD-BRD-06 | Show the upside arithmetic so it can be checked | PART 15 |
| SD-BRD-07 | Order carried context columns by CLASS before any count | 1.3d |

## Group CLM: Claims, credit and the counterfactual denominator

| ID | Rule | In force at |
|---|---|---|
| SD-CLM-01 | The permanent record principle | 14.7 |
| SD-CLM-02 | A results list is a set of true, quantified, orphaned facts | 14.7 |
| SD-CLM-03 | Credit attaches only to the units of the business you are accountable for | 14.7 |
| SD-CLM-04 | Every number carries a second number the writer did not choose | 14.7 |
| SD-CLM-05 | Every business must name what its ground is | 14.7 |
| SD-CLM-06 | Two comparative quantities, and never interchange them | 14.7 |
| SD-CLM-07 | Classify by formula, not by direction table | 14.7 |
| SD-CLM-09 | Resolve every claim as high as the evidence defends, and cite the highest level reached | 14.7 |
| SD-CLM-11 | Tie handling is mandatory | 14.7 |
| SD-CLM-12 | No named third parties, including by indirect identification | 14.7 |
| SD-CLM-13 | Work performed by a direct report is team credit, never first-person action | 14.7 |
| SD-CLM-14 | Show the benchmark, never claim it | 14.7 |
| SD-CLM-16 | A rank never substitutes for the counterfactual denominator where an external environment exists | 14.7 |
| SD-CLM-17 | Under-finding wins is the most common failure of a self-written record | 14.7 |
| SD-CLM-18 | Present findings as a working list the person edits, and drop means drop | 14.7 |
| SD-CLM-21 | Never infer a target to manufacture a completion percentage | 14.7 |
| SD-CLM-22 | Activity is not claimable | 14.7 |
| SD-CLM-24 | An illustrative number in a template is never a value | 14.7 |
| SD-CLM-26 | Show every benchmark, keep every loss | 14.7 |
| SD-CLM-27 | THE COLD START. Governing. | 14.8 |
| SD-CLM-28 | A cold start is DETECTED, never declared | 14.8.2 |
| SD-CLM-29 | Rung availability is scoped to the population and is RE-EVALUATED, never inherited | 14.8.3, 14.7 |
| SD-CLM-30 | A denominator the writer is building is not a counterfactual | 14.8.4 |
| SD-CLM-31 | No prior period for the population means no WIN and no MISS | 14.8.5, 14.7 |
| SD-CLM-32 | What a person may honestly claim during a cold start, which is not nothing | 14.8.6 |
| SD-CLM-33 | The rung decides the arithmetic, and a quantity that does not exist is never approximated | 14.7 |
| SD-CLM-34 | The noise band is PER RUNG, and plan attainment carries one that needs no peers | 14.7 |

## Group CNF: Confidence, inference and fabrication

| ID | Rule | In force at |
|---|---|---|
| SD-CNF-01 | Every inference carries a confidence, and confidence decides whether you PROPOSE or ASK | 19.7 |
| SD-CNF-02 | Ask plainly when unsure | 19.7 |
| SD-CNF-03 | Confidence is recorded, not just used | 19.7 |
| SD-CNF-04 | The proposal state machine, and silence defaults to REMOVED | 19.7 |
| SD-CNF-05 | Correlation is weak evidence for causation; present diagnoses as candidates | 19.7 |
| SD-CNF-06 | Never invent an action | 19.7 |
| SD-CNF-07 | Never fabricate; missing data is reported as missing | 19.7 |
| SD-CNF-08 | Every number traces to a cell or a tool result | 19.7 |
| SD-CNF-09 | Show the person the whole thing before it is final | 19.7 |
| SD-CNF-10 | A person's own claim that a resolved cell contradicts is a THIRD state: neither source wins, nothing contradicted enters a permanent record, nothing is deleted, and CONTRADICTED, UNSOURCED and UNVERIFIED are three labels with three remedies | 26.2, with the stop count at 19.7's calibration and the preview at SD-CNF-09 |

## Group LNG: Language, tone and the reader

| ID | Rule | In force at |
|---|---|---|
| SD-LNG-01 | Measure impact; do not judge the remainder | 19.6 |
| SD-LNG-02 | Refuse to rank or evaluate PEOPLE | 0.7, 19.6 |
| SD-LNG-03 | Never open with methodology, caveats or reconciliation | 19.3 |
| SD-LNG-04 | Report the count of items dated by EACH rule separately | 12.2 |
| SD-LNG-05 | Name every item that took a fallback weight and the weight it took | 12.3.1 |
| SD-LNG-06 | Name every item weighted zero, by name and count | 12.3 |
| SD-LNG-07 | Use the organization's exact vocabulary | 19.6 |
| SD-LNG-12 | At the ends of a scale, say the plain thing and print the figure beside it | 11.7.3, 19.3.2 |
| SD-LNG-13 | A templated sentence carrying a count is agreement-safe at zero and at one | 1.6 |

## Group SCL: Scale

| ID | Rule | In force at |
|---|---|---|
| SD-SCL-01 | Nothing about the method changes at scale; only the mechanics of reading and writing do | 20.4 |
| SD-SCL-02 | The output is bounded by the caps, not by the input | 20.4 |
| SD-SCL-03 | Sampling and estimating are prohibited at every scale | 20.4 |
| SD-SCL-04 | "In-scope population" means AFTER scope, after every qualifier and after any restriction | 20.4 |
| SD-SCL-05 | Checkpoint MORE often as the tier rises, not less | 20.4 |

**Every rule whose Applies list names this skill is carried; the index below is the count.**

# CLOSING NOTE

This file states one contract, one pipeline order, one scoring formula and one
audit specification. Where two sections of it appear to disagree about the shape
of the output, PART 1 governs and the other section is the defect. Where this
file appears to disagree with a companion file about something that companion
file owns, the companion file governs.

Nothing in this file names an employer, a system, a product, a place or a
document. Every such value is a variable in reference/schema/, requested at the
moment a decision needs it, defaulted honestly when it is not there, and
disclosed in the artifact either way.

## Live-run remediation, fifth pass

- **1.1 list size.** Rewritten as shorter RELATIVE TO SPAN. The senior pair is the
  larger pair in absolute rows, 20 and 50 against 10 and 25, and that is the
  design. The default table in the schema, SD-RNK-09 and this section now all say
  the same thing. Any reading that hands a senior leader fewer rows than a
  frontline reader off the same file is a misreading.
- **1.3b gains HDR_MEASURE on the item sections.** The table named a percentile of
  a number it never printed, while RIGHT_ALIGN_COLUMNS already named the measure
  as a right-aligned column and HDR_MEASURE existed for the purpose. A ranked list
  that hides the value it ranks on asks the reader to trust an ordering they
  cannot check.
- **1.3b states that HDR_RANK and HDR_SCOPE_RANK both ship where they DIFFER on
  any row.** Neither is ever dropped where the two carry different numbers, and a
  rank column always ships. The coincident case is decided by the test added in
  the ninth pass below.
- **3.2.1 and 23.0 scope the shape tie-break.** It is consulted only where tests
  one and two did not discriminate AND test three cannot be answered. Test one
  passing while test two fails is FIXED, decided, and FLOW is not preferred. Both
  sections now cite SD-POP-24 as the single procedure in the bundle.

## Confirmation-run remediation, sixth pass

- **3.4 C1 states that authority is ADDITIVE.** The named owner and the most
  senior role on ROLE_LADDER both hold ALL, always, and the run names which grant
  authorized any question it fired. Never read the senior-role grant as a fallback
  that lapses once an owner exists. SD-CTR-25.
- **11.2.1 is new, and it is the fix for the prospect at rank one.** Resolving the
  status concept and binding its values are two bindings. Where the concept
  resolved and the values are unbound, the seed set is applied under the stage,
  majority and naming guards, every distinct value is printed as EXCLUDED or KEPT
  with counts, and the user is offered the person-tier correction of F5.1b.
  Silence proceeds on the default. The default is deliberately not neutral,
  because the two errors are not symmetric. SD-POP-28.
- **12.3 names the anchor.** Every close band is measured from the close of the
  window BEING PLANNED, never from the run date, and the anchor date is printed in
  the Method section. CLOSE_HORIZON_DAYS, default 90.
- **19.4 item 2 splits into 2a and 2b.** In full and verbatim: every unbound
  binding that changed a published number, with what it changed. By count, grouped
  by schema group, with the full list on request: everything else. The test is
  mechanical, the undeterminable case goes in 2a, the two counts reconcile to the
  total, and nothing is deleted. Two hundred verbatim notices cost a skeptical
  reader the twelve that mattered.

## Acceptance-run remediation, seventh pass

- **3.4 C3 is computed on the run, not read from PART 22.** Four classes, with a
  membership change jumping the queue and a provably-inert request not firing at
  all. PART 22's order survives as the tie-break only. The two sentences that
  previously disagreed, "moves a published number furthest" and "the cost ordering
  is the order of PART 22", now say one thing. SD-CTR-28.

## Release-acceptance remediation, eighth pass

- **1.3b names HDR_DIRECTIVE_STATUS**, so every column in every family is a named
  HDR_ variable with a byte-identity guarantee. The direction family's fourth
  column was described in prose and had to be invented by a reader.
- **1.3d orders the carried context block by CLASS before any count.** Quantities
  the reader decides with, then groupers, then dates, then labels, with fill rate,
  distinct count and source position applied unchanged within each class. Order
  only: no membership test, no cap and no failsafe changes. SD-BRD-07.

## Producer-readability remediation, ninth pass

- **1.3b gives the commitment date its own named column, HDR_COMMITMENT_DATE**,
  first in the section-specific block on the action and reference sections and
  beside the action column on the directed section, in BOTH the unit-level case
  of rule 1b and the work-item case of rule 1. The date the whole ordering is
  built on existed only inside narrative prose, which asks the reader to trust an
  ordering they cannot check. The header is declared in 1.3b with its documented
  default and its exact notice, because GROUP 24 does not carry it, and it is
  recorded as an open request against the shared schema rather than read as
  though the schema had bound it. 1.3d's membership rule 3 no longer justifies
  itself with a header that did not exist.
- **19.3.1 block 2 is the do-this-week block.** Membership is exactly state 6 of
  12.3.1 and nothing else. It re-ranks nothing, re-weights nothing and changes no
  membership: it is a VIEW of rows already published, each carrying the rank and
  section it holds elsewhere, and the line that stops a reader counting them twice
  is printed every run. The count stays in block 1 as the ask; the rows are the
  answer to it.
- **1.3b collapses Rank and Scope rank when they coincide.** The test is row-by-row
  equality over the full ranked population, computed once and applied identically
  to every item section. Where they differ on any row both ship; where they are
  identical on every row one ships, headed HDR_RANK, never a merged or invented
  string, and the Method section states which way the test went, on what evidence.
  Two identical columns side by side read as a broken export.
- **19.3.2 puts the front panel in the reader's language and keeps the technical
  form where its audience is.** Cold-start detection, tie-broken and bare
  denominator mean nothing to the person holding the plan. Every front-panel line
  now takes the three-part form in plain words, with the variable names, the exact
  A1 and A2 notices, the doctrine IDs and the tests kept verbatim in the Method
  section, which is written for the binding owner. Nothing is dropped, and
  SD-LNG-07 is untouched: the organization's own vocabulary is never paraphrased,
  and what gets translated is this method's own.
- **PART 27 rebuilt against the grown doctrine.** SD-POP-29
  is carried in 11.2.1 as the mechanism by which a cell value matches a listed
  entry, replacing an unstated match with whole-token phrase matching, the
  single-token override and a printed refusal, and stating that no rule in this
  skill admits a match on a character-length threshold. SD-BRD-07 gains its index
  row, having been cited in 1.3d without one.

## Ship-or-no-ship remediation, ninth pass, addendum

- **0.4 no longer states variable counts.** It described the binding files with a
  figure that had drifted three revisions behind. Counts live in the COUNTS block
  of reference/schema/ alone; a file describing another names the invariant, never
  the number.
- **11.7 gains the endpoint wording rule.** The measure percentile is printed
  unchanged at 1.0, and the narrative for the top row says the largest in this
  list, naming any tie, with the figure beside it. SD-LNG-12.

## Ship-acceptance remediation, tenth pass

- **1.3b ships the close state and its weight as columns, and 1.6 ships the
  ordering note.** A correct ranking that puts a later-dated commitment above an
  earlier one is indistinguishable from a broken one when the reason lives in a
  sentence the reader has to go and find. HDR_CLOSE_STATE carries the short label
  of the row's state from 12.3.1 and HDR_CLOSE_WEIGHT carries what that state
  contributed to the score, both immediately after HDR_COMMITMENT_DATE; the
  ordering note states on every ranked section that a larger unit committing later
  can outrank a smaller one committing sooner, and how many rows on that section
  fall outside the planned window. No weight, rank or membership changes, and the
  exact row wording of 12.3.1 still ships.
- **1.3e is the header honesty rule, and every header in the contract carries a
  recorded verdict.** A workload count headed with an imperative was read as an
  instruction and its zero on the largest unit in the plan as do not work this
  account. Five defaults are corrected, the rest are kept as true and terse, a
  BOUND header is never changed, every correction is disclosed with the string it
  replaced and the question it failed, and each is raised as an open request
  against GROUP 24 so the schema and this contract converge deliberately.
- **1.3b puts HDR_ACTION on the action lists and the reference list.** A directive,
  a compliance requirement or a work item supplies it, in that precedence; a
  direction held back by the compliance gate supplies nothing; where no source
  names one the cell says MSG_NO_ACTION_DERIVED and the section says why in the
  reader's words. It is never invented, per SD-CNF-06, never scored, never confers
  membership and never reorders anything.
- **PART 27 rebuilt again.** SD-LNG-12 gains its index row,
  having been carried in 11.7.3 without one, and 19.3.2's reader-language table
  points at 11.7.3 so the ends-of-a-scale rule is stated once and read twice.

## Final-ship remediation, eleventh pass

- **1.3c carries SD-FMT-21 as an ORDERING.** The mandatory set is resolved from the
  contract first and the constant test applies only to what remains, so an
  optimisation can no longer delete a guarantee. The mandatory set is COMPUTED
  from IDENTITY_BLOCK_COLUMNS and the 1.3b family table rather than enumerated,
  because the enumeration going stale is exactly how HDR_ACTION became eligible
  for deletion. A mandatory column carrying one repeated value is a finding about
  the data, reported in one line, and the generalisation covers every removal rule
  in the file rather than the constant test alone.
- **1.10 conforms to the schema's membership rule column for column.** Right align
  COUNT_OR_MEASURE, RATE_OR_PROPORTION and DATE; left align IDENTIFIER_OR_CODE,
  STATUS_OR_CATEGORY, BOOLEAN_LIKE and FREE_TEXT. CLOSED means no column is
  inferred at run time, never that the list is assembled from memory. This file
  now states the shape token of every column it emits and leaves the materialised
  list where it belongs, in the schema, so the two cannot disagree again.
  HDR_CLOSE_WEIGHT ranges right; HDR_CLOSE_STATE ranges left.
- **19.3.1 block 1 gains the commitments-in-window line.** How many of the
  reader's commitments fall inside the window and where each one sits, with every
  row named at its rank in the Method section. The ordering note counts rows on a
  section falling outside the window; this counts the window's own commitments
  falling outside a section, and they are different numbers with different
  consequences.
- **1.6 says what the second action section is FOR, and discloses its coverage.**
  Its note names it as the rest of the population within reach rather than a
  second plan, carries the count of its rows committing inside the window, and
  where the two action sections cover more than half of eligible_count says so and
  puts the question to the binding owner once. The bound sizes are never resized at
  run time.
- **1.3b requires the narrative to vary by construction, and reports a uniform
  mandatory column once.** The narrative names the row's own close-date wording,
  its own measure with the endpoint phrasing of SD-LNG-12, and its own rank and
  the term that moved it. A mandatory column carrying one value on every row ships
  in full and is named once at the top of the front panel, with what would have to
  be bound or supplied for it to fill, instead of being read as a broken export
  forty times.
- **7.1 carries SD-SCO-17, the covering invariant.** A window named for a calendar
  period covers every day of it; the name selects the derivation and the nominal
  length is kept for horizon arithmetic. It is validated before any item is
  banded, never disclosed after the fact.
- **PART 27 rebuilt against the doctrine as it stands**, and the header declarations that this
  file used to carry locally are retired now that GROUP 24 owns them, so one
  variable has one documented default.

## Shared-layer conformance, twelfth pass

- **14.2.1 carries SD-CMP-09, the exit test.** Overlap tests the entry side only,
  so a survivor-only prior file passes it at its maximum while being unusable. The
  exit count runs before anything is computed on the pair, the run decides between
  a survivor-only extract and a genuine no-attrition population and says which and
  why, and the claim cap follows: retention and churn not computable, same-unit
  growth only beside total movement with the gap named, no ranking by survivor
  growth. Divergence 1 and the join-overlap paragraph both point at it.
- **14.7 reads DEADBAND per rung with each band's unit named**, and a bare scalar
  is rejected at validation. Rung 3 is computed from the peer spread and emits no
  label where it cannot be; rung 4 carries a fixed band in percent of target, needs
  no peers and is always computable, so the reader with no peer set still gets
  labelled figures; rung 6 has no band and says so. The band and its unit print
  beside every labelled figure. SD-CLM-34.
- **1.2, 9.2 and 19.1 read the PLANNING key.** TAB_CONTRACT and DELIVERABLE_NAME
  are keyed per skill and a shared default may not carry one skill's content, so
  this file reads its own section list and its own artifact name and never
  inherits another skill's. COMPLIANCE_FAILS_CLOSED_ON names the validated items
  by role rather than by this skill's noun. SD-CTR-30.
- **26.4 carries SD-CTR-29.** Every closed set this skill draws from is coverage
  validated from the STATES to the SET, a hole is distinguished from a
  deliberately empty additive list, a member whose action is none says so, and a
  state with no member is printed and raised rather than invented into the set.
- **1.6 carries SD-LNG-13 and the templated-sentence sweep is done.** The
  singular-plural form, the zero sentence, the count-last rewrite and the
  three-value test now bind every generated line in this file, and every template
  in it was rewritten to agree at zero, at one and at many.
- **The four-class sweep, run over this whole file.** Counts restated outside the
  block that derives them: four, all removed, in 0.2, 0.4, the stage table and the
  audit spec, so the doctrine total, the decision-point total, the guarantee count
  and the close-state count are now stated only where they are derived. Templated
  sentences that broke at zero or one: thirteen, all rewritten, with two zero
  sentences added where the zero case was meaningful. A worked example
  contradicting its rule: one, in 1.3d, where the example ordered the carried
  context block by fill rate and distinct count and the rule orders it by CLASS
  first. Two sections specifying one thing differently: four, being the index row
  for SD-SPN-02 against 1.4, the reference depth in 1.1 against the per-line
  binding, a front-panel line required by 1.3c with no slot in 19.3.1's
  enumeration, and 19.3.1's own stale block numbers left by the five-block
  renumbering.

## Output-contract conformance, thirteenth pass

- **PART 1 states the header-row rule once and positively.** The header row is
  ROW 1 on every item section, per reference/output-contract.md element 1, with no banner,
  title, scope, period, note or spacer row above it on any section on any run.
  The report title, the scope, the period and every caveat moved to the front
  panel, per 19.3.1 block 1, where they now appear in the block's first line. The
  incomplete banner of PART 21 is named explicitly as a DIFFERENT thing that goes
  to the three announcement places and never to a spreadsheet row, and PART 21's
  own prohibition list now says so. SD-FMT-22.
- **1.10 cites the contract instead of restating it.** The freeze point, the
  direct-formatting rule, the row-height arithmetic and the character gate were
  restatements of elements 2, 5, 12 and 16 and are now one-line citations that
  keep SD-FMT-03, SD-FMT-04, SD-FMT-08 and SD-FMT-14 resolving to the standard
  that owns them. What stayed is what the contract does not carry: the shape-token
  table for this skill's own columns, the carried-context rule, the
  column-addition validation, and SD-FMT-09 through SD-FMT-13 and SD-FMT-15
  through SD-FMT-20. SD-FMT-13 stayed because the contract carries no title-case
  rule.
- **17.3 and 18.2 adopt elements 10, 12 and 14.** The build computes widths from
  PART 2.2, body heights from PART 2.3 and the header height from PART 2.4, in
  the section's own structural call and with the widths set before the heights are
  computed from them; the gate recomputes each requirement and compares it to what
  was built. 18.2 is now explicitly the matrix in PART 7.2, one row per section
  per element, with R1 through R5, and a gate that cannot run has FAILED.
  SD-FMT-23.
- **HDR_RANK_REASON ships on every section whose rows are units.** At that pass it
  sat at the END of the identity block, always after IDENTITY_BLOCK_ANCHOR_COLUMN
  so the freeze pane never pins a paragraph to the left edge. **SUPERSEDED BY THE
  SIXTEENTH PASS**, which moves it to the FIRST COLUMN AFTER the identity columns
  and makes it not an identity column at all, per 1.3; the freeze guarantee is
  unchanged and is now enforced by the bounded walk instead. It names the terms of 12.1
  that decided the position, in contribution order, with a worked example built
  from this skill's own terms. It is not the narrative column and does not replace
  it. The directed, breadth and exception sections at that pass headed their
  position column HDR_PRIORITY_BAND because none of the three is ordered on merit,
  **which a later pass retired in favour of HDR_POSITION**, and the reason
  column on each says what actually placed the row. Its header string is a
  GROUP 24 variable read exactly as every other header is read, with SECTION A1
  supplying the documented default and its exact notice where it is unbound, and
  RIGHT_ALIGN_COLUMNS already carries it among the left-aligned free-text
  headers. SD-FMT-24.
- **1.6 cites PART 4.2, PART 4.3, PART 5.1 and PART 5.2.** The derived-ceiling
  arithmetic, the min form and the cap-counts-rows rule are citations now. What
  stayed is this skill's own: the slicing mistake the row-count form prevents,
  SD-RNK-03's wrong-number gate, the two-note table with the CAP note reconciled
  to PART 5.2's exact string and the SHORTFALL note kept as this skill's separate
  and differently worded note, the ordering note in full with SD-LNG-13, the
  second action section's purpose sentence, the covers-most-of-the-population
  disclosure, and SD-RNK-08, SD-RNK-10 and SD-RNK-11. The cap is PER SECTION and
  INDEPENDENT, because the later sections of this artifact hold populations that
  differ by an order of magnitude off one scope. SD-FMT-25.
- **1.11 holds under the new contract.** Elements 10, 12 and 14 record NOT
  APPLICABLE with their reason in markdown, which is a pass; PART 4's two columns
  and PART 5's showing note are information rather than formatting and are not
  excused by degradation. A degraded container is a presentation fallback, never
  an information fallback.

## Demonstration-run remediation, fourteenth pass

A fresh operator ran this skill end to end against a real organization's data,
built two workbooks, read them back through the engine and reported every defect
that changed what shipped. Eighteen were actionable in this file. What changed,
by the defect it closes:

- **A direction naming a CLASS of units could never reach a row, so the action
  column was empty on all 190 rows of one plan.** 8.8's ladder had four rungs and
  all four match a NAMED unit; every priority the organization published named an
  action and a testable rule over a column in the same file and named no unit. The
  new 8.8.1 adds a FIFTH rung producing a PREDICATE match: it carries the action
  and nothing else, confers no mandatory status, no source boost and neither
  multiplier, moves no rank, prints the predicate VERBATIM beside its match count
  and its resolved column on the priorities section, and FAILS LOUDLY with an open
  question where the predicate names a concept no column resolves to. SD-PRI-15 is
  untouched: a stated rule is evidence and a summary figure is not, and this rung
  never reads one.
- **The scope chain.** GROUP 3 and Turn 2 now run to and INCLUDING the level one
  ranked unit sits at, with SCOPE_FINEST_KEY separately the finest OWNED level.
  11.7.2 now reads the bound chain FIRST and detects only as a fallback, and says
  in full why the fallback is correct by construction now and was catastrophic
  before. 5.2's two-ended role anchor says the same thing from the other end, with
  the one-sentence test a binding owner can apply.
- **The top of the house had no priority source by construction.** The new 8.4.1
  reads DOWNWARD exactly one level for a reader at the top of the ladder. 8.7's
  actor test is unchanged and is what separates the two kinds: a direction issued
  TO the reader is a directive; one issued BY a subordinate manager to their own
  people is an ASSIGNMENT under SD-DUP-03, reported on the rows it names, naming
  who assigned what to whom, and never weighted.
- **The note band.** Every per-sheet note now goes where PART 5.3 and SD-FMT-26
  put it. The instruction that a note sat "beside the section heading" is deleted
  rather than reinterpreted, because that placement never existed under elements 1
  and 3. 1.6.1 states which notes this skill emits and in what order.
- **The freeze point.** PART 4.1.1 settled it at this pass: the anchor is the last
  identity column BEFORE the reason column, so the freeze lands ON the reason and
  the reason is not frozen. **EXTENDED BY THE SIXTEENTH PASS**, which adds the
  bound of 4.1.2: the anchor is now DERIVED by a walk over the summed built widths,
  the freeze lands on the reason column only where the whole block fits, and the
  reason is outside the span under both branches.
- **No conversion factor is applied to a width being set.** 17.3 and 18.2 both
  carried that rule at this pass, with CHAR_WIDTH_FACTOR named as belonging to the
  two height computations only. **SUPERSEDED BY THE SIXTEENTH PASS**: banning every
  conversion was the opposite failure and was measured. The rule is now a
  DIRECTION, multiply forbidden and one division permitted at 2.2.2 step 5, per
  PART 2.2.3.
- **Sheet classes and ranked kinds are DECLARED**, in the new 1.2.1, so R1 through
  R5 resolve without a reader working it out. The consequence in 1.2.2 is that the
  priorities section is a REFERENCE TABLE, takes every grid element, and carries
  HDR_POSITION and HDR_RANK_REASON; it is no longer exempt from R1.
- **HDR_POSITION heads every non-merit position column**, and HDR_PRIORITY_BAND
  heads band labels and never a number column. On the exception section both ship.
- **BINDING_OWNER_CONTACT is DEFERRED**, so a run bound faithfully from an
  organization's own documents is no longer provisional forever on the one value
  no document carries. 3.2, 3.4 and 19.5 read it that way.
- **1.3e writes no header string.** The verdict table keeps its verdicts and gains
  a composition rule that builds a corrected default out of what the run already
  resolved; where only question 3 fails and no source word exists, the A1 default
  is kept and glossed. Every correction is raised as an open request against
  GROUP 24, which is where a default string belongs.
- **The uniform-column test runs per rendered SECTION as well as over the full
  ranked population**, because a reader works a section, and the population test
  alone missed the disclosure on exactly the artifact that needed it.
- **The mandatory family row no longer contradicts the trailing order** and no
  longer omits the measure, and the two universal columns now have a stated
  position on any family whose row does not name them.
- **12.1's alignment product names SEVEN factors.** NARROWNESS_MULTIPLIER and
  OWN_ACTION_MULTIPLIER multiply the item's own alignment contribution, once each,
  with a neutral value of one.
- **12.8.1 derives entity weights from a published ORDER** by a printed linear
  ramp to ENTITY_WEIGHT_FLOOR, at medium confidence, never written to config,
  never overwriting a bound weight, and not run at all where the floor is unbound,
  in which case the run says so and names the one value that would activate it.
- **3.1 narrows P3's LABEL** to the case where the priority stage actually reached
  nothing, because printing "no stated priorities" while the directions are quoted
  two sections earlier is a false sentence in the artifact.
- **16.4 states that future-dated, blank and unparseable recency values do not
  enter the local median** that sets the membership threshold, and reports each
  excluded count separately.
- **1.3d closes the gap at exactly six** and excludes population-exclusion sources
  from the carried context block.
- SD-FMT-26 and SD-SPN-16 are cited where they bind and are carried in PART 27.

## Shared-layer convergence, fifteenth pass

Five things this file worked around are now solved in the shared layer, and one
gap it reported now has a rule. Every local workaround is deleted rather than
kept alongside, because two answers to one question is the defect this bundle
spends most of its rules preventing.

- **The P3 narrowing at 3.1 is DELETED.** reference/capability-probe.md P3 is now a
  four-rung priority source ladder, mailbox, document store, supplied files
  discovered by CONTENT wherever FILE_READ is present, then nothing, and "no
  priority source resolved" is available only after every rung returns empty. 3.1
  cites the ladder and adds P3b's consequence for this skill: rung 3 is MANDATORY
  WORK on every run with FILE_READ present, exactly as an attachment is under 8.10
  and the central publication is under 8.11, and a run that skipped it says
  priorities were not looked for rather than that none were stated. PART 8 runs on
  a rung-3 direction end to end, unchanged; only the rung is additionally recorded.
- **The action column's absence text is MSG_NO_ACTION_DERIVED**, a GROUP 24
  variable with its default and its notice in SECTION A1. The literal is gone from
  1.3b, from 19.3.1's column glossary and from the change log.
- **Five header verdicts in 1.3e move to KEPT and their open requests are CLOSED.**
  SECTION A1 now carries corrected defaults for HDR_MUST_CLOSE,
  HDR_MEASURE_PCTILE, HDR_SCORE, HDR_DAYS_SINCE and HDR_ITEM_GAP, with
  HDR_DAYS_SINCE shape dependent there. The composition rule STAYS, because each of
  those A1 rows defers to it wherever a genuine source word resolves and SD-LNG-07
  prefers the reader's own vocabulary to any default; what changed is that a run
  with no word to borrow now ships a good default instead of composing one.
- **The rank-to-weight ramp is DELETED from 12.8.1 and cited instead.** It lives in
  the SECTION A1 row for CREDITABLE_ENTITIES.standing_weight so three skills derive
  one weight matrix from one published order. ENTITY_WEIGHT_FLOOR's default is now
  shape dependent on the entity count and strictly below the ceiling wherever two
  or more entities are in play, with the validation requiring it, so the derivation
  RUNS ON THE DEFAULTS and the refusal branch this file carried is gone. What stays
  in 12.8.1 is only what is this skill's own: which directions count as a published
  order here, that a direction the compliance gate held back publishes none, where
  the derived weight enters the formula, that a bound weight is never overwritten,
  that unmapped still means unmapped, that it is run-local, and where the read-back
  is raised.
- **SD-PRS-48 is wired in at the new 10.1.1.** The join belongs to STAGE 6, runs
  after 10.2 has established which needed concepts did not resolve, and is complete
  before step 1 of 11.1, so a row-count-changing operation is never downstream of
  the funnel that would have to catch it. A joined column is never the identifier,
  never the measure and never a scope column; it may be a gap-term source, an
  exception-flag source, an entity or work-item source, or a carried context
  candidate. **A REFUSED JOIN DEGRADES THROUGH THE EXISTING PATH AND NEVER THROUGH
  A NEW ONE:** the run behaves as though the second file had never existed, which
  is SD-SCO-11 for a gap term, SD-EXC-08 for an exception flag and SD-CTR-13 for a
  column, each unchanged. What a refusal adds is disclosure and nothing else. A
  ranked row that matched nothing on the enriching side is in the same state, blank
  rather than zero, because an absent record is not evidence of a negative.
- **Three shared edits reconciled.** 11.7's SD-POP-18 table gains the TARGET OF
  ZERO row, the one divisor a population guard never sees. 14.7's SD-CLM-34
  passage gains the FIFTH unit, percentage points of the measure's own rate for a
  level compared against a level, with its data-derived band and the rule that a
  level delta and a movement delta are never banded against each other. 1.2.1 now
  reads R1 through R5 from PART 7.2 row by row rather than from PART 2.0's class
  table, so R3 reaches a capped panel and R5 reaches the whole workbook.

## Demonstration-run remediation, sixteenth pass

A fresh agent drove this skill end to end against a real book of business at two
altitudes, built two workbooks, read them back through the engine and reported
thirteen new defects. Three were severe and all three were failures of the same
shape: a rule with no branch for the ordinary case, so the run had to choose, and
the choice was invisible in the artifact. Every item below names what shipped, not
only what the text said.

- **8.7.1 IS NEW AND IT IS THE MOST IMPORTANT CHANGE IN THIS PASS.** The actor test
  had two rows and a directive register with no recipient column fitted neither, so
  a run took the `names no actor at all` clause and read NINE of a subordinate's
  instructions as the head of the house's own mandatory work, at the full
  multiplier, ahead of everything he owned, in the first section of his plan that
  told him to do anything. **The recipient is now RESOLVED and never assumed**
  wherever a direction carries no addressing evidence, which is exactly the case
  for a register and for everything the downward sweep of 8.4.1 returns. The ladder
  is explicit recipient, then the owner of the named unit, then UNIDENTIFIED; the
  reading is DIRECTIVE only where the resolved actor is the reader and ASSIGNMENT
  in every other case, unidentified included. Ownership of a unit is stated NOT to
  be evidence of addressing, MANDATORY_MULTIPLIER is barred from any direction whose
  actor is not the reader, and the directed section is stated to be populated by
  directives alone. SD-PRI-13 is scoped to the doubt it was written for. 8.4.1's
  table gains the third row and 18.1 gains the assertion.
- **10.1.1's admission test has TWO LIMBS, because one limb could not fire in the
  case the section exists for.** Gating the join on the second file resolving a
  concept the parse stage left unresolved can never open for a file whose headers
  resolve to no concept at all, which is every real evidence file. Limb 1 is a
  needed concept resolved BY ANY ROUTE reference/field-resolution.md permits, including the
  first-run provisional adoption of 7.4a with all six of its tests; limb 2 is a
  clean-typed column no container column carries, admitted to the CARRIED CONTEXT
  BLOCK ONLY, with its source file named. 1.3d rule 1 and this test are now stated
  to be the same test read from two ends. A limb-2 column is never scored and never
  trips a flag, and 16.2 says so where the flags run. **CORRECTED IN THE
  SEVENTEENTH PASS, AND THIS BULLET IS LEFT STANDING WITH THE CORRECTION ATTACHED
  RATHER THAN REWRITTEN, BECAUSE READING IT ALONE IS WHAT MISLED THE NEXT RUN:**
  limb 2 restores NO gap term and NO exception flag. It moves where a column
  appears, not whether a term scores. **The route the fix actually depends on is
  reference/field-resolution.md 7.4b, THE SIBLING SET, reached through LIMB 1**, and until
  7.4b existed limb 1 could not fire on a real evidence file at all, because 7.4a
  test 5's uniqueness rule refuses N sibling columns by construction and an evidence
  file's natural shape is one column per requirement.
- **17.3 and 18.2 are rewritten around PART 2.2's three primitives.** The old text
  read the width rule as banning every conversion, which made the width and the
  usable-character count two quantities wearing one number and failed element 14 on
  14 of 29 columns of a workbook built exactly to the rule. The rule is now a
  DIRECTION: multiplying a width is forbidden, dividing a character requirement at
  2.2.2 step 5 is the one permitted inversion, and nothing scales a width
  afterwards. **The workaround that widened columns past 2.2 to clear element 14 is
  deleted**, because 2.2.4's composition makes 14 follow from 10 by construction,
  and raising HEADER_MAX_LINES to clear it is forbidden in both files.
- **The reason-for-rank column moves to the FIRST COLUMN AFTER the identity
  columns**, per reference/output-contract.md 4.1.1, and stops being called an identity
  column. **The frozen span is BOUNDED** by `FROZEN_SPAN_MAX_WIDTH` and the anchor
  is DERIVED by 4.1.2's walk rather than chosen, with the first column always
  frozen, nothing moved, dropped or narrowed, the identity block declared
  MOST-IDENTIFYING FIRST, and the truncation recorded in the Method section. 1.3,
  1.9, 1.10, 18.1, 18.2, 19.4 item 4m and PART 22 decision 49 all read the same
  rule.
- **N is read from PART 5.1.1 per section.** 1.6 carries a table of this skill's
  own sections against the three bounds, states that a TIER SIZE is a bound and its
  note is not vacuous, and states that capped means SUBJECT TO a cap and not CUT BY
  one. The disagreement that had one reader repeat a tier's own row count as its N
  while another gave the eligible population behind it, off one run, is gone.
- **The explanatory row of an empty section is adopted from PART 5.4**: inside the
  table range, not a unit row, n and N both zero. 1.2, 1.6, 1.6.1, 16.2, 16.4 and
  1.9 all say it, and 1.6.1 additionally says what does NOT go in the note band, so
  the exception section's empty-and-alert reconciliation goes in the row rather than
  the band.
- **The recency median reconciliation has ONE PRIMARY LOCATION**, the exception
  section's own note band, and 19.4 item 15 is a RECONCILIATION against it that
  18.1 checks. Two unreconciled copies of one figure are now impossible.
- **The entity column is resolved through `concept_creditable_entity`**, with the
  value test that outranks the name, the coverage fallback bounded by
  `ENTITY_COLUMN_MIN_COVERAGE`, and the stated neutral of 1.0 where nothing
  resolves. The procedure a live run had to invent is deleted in favour of the
  concept, and 19.4 item 4l prints the chosen column, its coverage and the
  runner-up.
- **8.8.1 test 2 states the ROUTE ORDER**, concept first, then header text, then
  7.4a, with the route recorded per predicate, because the two readings differed by
  a third of the priorities on one file and neither was detectably wrong.
- **The direction tie-break chain is TOTAL and is stated once in 8.8.1**, gaining
  position within the source document and the document's own title. It exhausted on
  the commonest input this skill will ever see, a single memo with numbered
  priorities.
- **Band D is named in PART 8** for a direction issued below and swept up, and it
  sorts LAST in 1.2.2, because a row that moves no rank does not lead a section
  that exists to say what the reader must do.
- **An unevaluated direction is announced where the decision lives.** 8.8.1 requires
  its own row on the priorities section with the reason and the closest candidate
  named, 1.6.1 note 10 carries the count in the band, and 1.9 item 16 fails a run
  that discloses it only in the audit. reference/field-resolution.md 6.5 and 7.7 own the
  general rule.
- **The sheet-name constraint is cited, not restated.** 1.2 sends every title
  variable to reference/schema/ GROUP 15 for the four conditions and the
  deterministic truncation rule, and requires the rename to be disclosed and raised.
- **SD-FMT-27 is carried.** 18.2 declares the cell range the formatting matrix
  occupies and excludes it from every STRING-SEARCHING row, R5 included, while
  element 16 still reads every cell of it. **No other range is excluded from any
  check, ever.**
- **1.10 declares that this artifact has NO status grid column and NO classification
  fill**, with the reason per column, rather than adopting PART 2.5's centre class
  or PART 2.6's palette because they exist. 18.2 records it as a positive statement
  and fails a centred column or a second conditional fill.
- **TABLE_STYLE_NAME still needs no local copy here, and the reason has grown.** Its
  prose and its example disagreed in the schema and the schema fixed that; the schema
  then bound the variable to a style whose OWN header band agrees in DIRECTION with
  element 5's band and rejects an opposing style at validation, per element 4 and
  SD-FMT-04. This file names no table style anywhere, which was verified rather than
  assumed, so there was no local copy to correct in either edit; what it carries is
  1.10's citation of SD-FMT-04 and SD-FMT-29, and those now carry the direction.

## Live-run remediation, seventeenth pass

A fresh agent drove this skill end to end against a real book of business at two
altitudes, built two workbooks, read them back through the engine and reported
twelve new defects, with thirty of the previous thirty-three judged fixed. One was
severe and it was the same failure the sixteenth pass believed it had closed,
arriving through a rule nobody had looked at. Every item below names what shipped,
not only what the text said.

- **THE JOIN NOW REACHES THE EVIDENCE FILE AND CAN FINALLY SCORE IT, THROUGH
  reference/field-resolution.md 7.4b AND NOT THROUGH LIMB 2.** 7.4a test 5 refuses a tie, and
  a real evidence file's natural shape is ONE BOOLEAN COLUMN PER NUMBERED
  REQUIREMENT, so eight columns each passing the value check and clearing the fill
  floor tied for one concept and NONE was adopted; four gap terms and three
  exception flags went unevaluated on all 190 rows and most of the population read
  that no action could be derived, two columns away from a file that answered the
  question account by account. **The refusal got more certain the more complete the
  evidence file was.** 7.4b's SIBLING SET separates columns that PARTITION a
  concept from columns that COMPETE for it, on five tests that are additional to
  7.4a's six and never instead of them. 10.1.1's limb 1 now cites it by name;
  10.1.1 states what a gap term and an exception flag do when a sibling set
  resolves, which is per member with the member named beside every figure and no
  rollup invented, and what they do when it does not, which is exactly what a
  missing column already does. 12.10 and 16.2 carry the per-member reading for a
  gap term and for a flag, and their existing not-scored-and-named rules are
  unchanged and are what the refusal path routes to; 8.8.1 gains route d for the
  same shape, recorded as ONE adoption of the set; 19.4 item 4k carries 7.4b's four
  further disclosures including every member that got no column. **The sixteenth
  pass's own note is corrected in place rather than rewritten**, because reading it
  alone is what told the next run the problem was solved.
- **A LIMB-2 COLUMN MAY NOT RESOLVE A PREDICATE ATTRIBUTE, AND THE LIST IS NOW
  CLOSED.** Step 4 says a joined column is ordinary from that point on and 8.8.1
  test 2 route b matches a direction's words against header text, so a limb-2 header
  matching a published requirement would have supplied an action on every row it
  answered. Two careful implementers produced two different action columns off one
  input and neither was detectably wrong. **An action is an output**, so a column
  admitted on a clean type alone with no recorded route may not reach it, nor a
  gap-term source, a flag source, an entity resolution or a work-item source. The
  route into an action is limb 1.
- **THE CLOSE WEIGHT COMES FROM THE DATE AND FROM NOTHING ELSE.** 12.3's weight
  table and 12.2 rule 1 gave a supervisor-named or locally loaded item the full
  close weight while 12.3.1's ladder assigned a state purely from a date and 18.1
  gated on the two AGREEING, so a correct artifact failed its own gate whichever
  text the run believed. **12.3.1 is now the SOURCE and 12.3 is a READING of it**;
  supervisor naming and local loading act on the local boost, the source boost, the
  chain distance and the mandatory multiplier, and never on the close weight. The
  failsafe the old trigger carried is kept where it belongs: such an item counts as
  NAMED for the planned window, so an unreadable date lands it in state 2 rather
  than dropping it under 12.2 rule 3. 12.6's third consequence is rewritten to say
  the same thing once.
- **THE FROZEN-SPAN WALK RUNS ONCE FOR THE ARTIFACT, FROM THE WIDEST CASE.** A
  per-section walk stops in a different place on every section, because a built
  width depends on that section's longest data value: one workbook froze three
  identity columns on its merit sections and five on its empty ones, every section
  individually conformant, and recorded six truncation statements for one identity
  block. reference/output-contract.md 4.1.2 now walks each identity column's MAXIMUM built
  width across the artifact and applies the one anchor BY NAME everywhere; 1.3,
  1.9 item 15, 17.3, 18.1, 18.2, 19.4 item 4m and PART 22 decision 49 all read it,
  the truncation record is ONE line for the workbook, and a genuinely narrower
  section freezes the same columns in fewer width units and may never freeze more.
- **A GRID'S TOTAL WIDTH IS BOUNDED, BY `GRID_MAX_TOTAL_WIDTH`.** The span bound
  says what stays on screen and says nothing about how wide the sheet is. 17.3
  declares the bound before the columns are built, records the value, measures
  every section from the widths read back, and runs reference/output-contract.md 2.7's relief
  ladder where a section is over; 18.2 asserts it under element 10; 19.4 item 4n
  carries the record and PART 22 decision 49b carries the binding. The three things
  that never give are 2.7's and are checked directly: no column dropped, no column
  below its own header floor, no meaning-carrying value shortened. A section over
  the bound WITH the record is a pass; without it, a failure.
- **1.10 NOW MAKES TWO DECLARATIONS, BECAUSE CENTRING AND SHADING ARE DECOUPLED.**
  PART 2.5 governs centring only and PART 2.6 defines a CLASSIFICATION COLUMN that
  reads no length bound. The old single declaration took the absence of a status
  grid column as the absence of a fill, which is no longer a valid inference. This
  artifact declares NO status grid column and, separately, NO classification
  column, the second on 2.6's own conditions per column: the shared
  `CLASSIFICATION_VOCABULARY` binds states no column here is written from and this
  skill's closed sets live in their own taxonomy variables; the flags column fails
  the totality test outright; the play column carries an open set; and a carried
  context column is carried and not scored. 18.1 and 18.2 check the two separately.
- **TITLE CASE GAINS A SECOND EXEMPTION, ON THE FIRST ONE'S REASONING.** A sheet
  name is a heading, and a title variable's value is a bound string or a documented
  default, so shipping one verbatim failed 1.9 item 8 and re-casing it altered a
  documented default. **A heading whose text this skill does not write is exempt**;
  the rule governs the headings this skill authors. Nothing is re-cased and nothing
  is renamed but by GROUP 15's own truncation rule.
- **A TERM IDENTICAL ON EVERY ROW NEVER EXPLAINS A POSITION.** The contribution
  ordering behind HDR_RANK_REASON is computed on the DIFFERENCE FROM THE POPULATION
  MEDIAN of each term rather than on its absolute value, so BASE_TERM is excluded by
  construction and a first-position row no longer leads with the base every unit
  carries. The score does not move and nothing becomes undisclosed; only which
  terms the sentence names changes.
- **THE PUBLISHED SCORE'S PRECISION IS CHECKED AGAINST THE REACHABLE RANGE.** With
  the measure exponent compressing the tail, adjacent rows with different real
  scores printed the same number, so the column 26.1 makes mandatory was inert on
  exactly the rows a sceptical reader queries. The precision is raised until no two
  rows with DIFFERENT real scores print alike, up to the schema's ceiling, and where
  the ceiling is reached the artifact says how many pairs still collide. The score
  is never re-scaled and the precision is never lowered.
- **THE NARRATIVE COLUMN'S BOUND IS READ AS WIDTH UNITS**, per element 11 and 2.2
  step 6, applied directly with no conversion, despite two variables named for
  characters and an appendix default worded in characters. The naming is raised as
  an open request and is never resolved by converting the number.
- **PLAN_AHEAD_RULE IS CONFIRMED AGAINST THE SOURCES.** SD-SRC-15 opens by saying
  match sources on the PERIOD and the ladder read only the calendar, so a run with
  no user-named period would have planned one month against a document titled for
  the next. A period from step 2 is now PROVISIONAL and is corrected at 8.13 where
  an admitted source names one, at most once, with the disagreement reported rather
  than resolved by a third pass; a period the user named stands and the
  disagreement is disclosed. The correction sits at stage 4 because stage 3 has
  swept no source yet, and a rung that could never fire is the defect 10.1.1's own
  limb 1 was written to escape.
- **ONE FILTER PER SECTION, AND IT IS THE ONE THE READER'S ENGINE LOOKS FOR.**
  Element 3 wants a table and element 6 wants a VISIBLE filter, and the earlier
  mechanic here, carrying the filter inside the table object, shipped workbooks with
  no visible filter control on any sheet while a check reading it out of the table
  container recorded a pass. 17.3 states the mechanic and 18.2 asserts it: the
  section's own filter, read back from the section, spanning every column, exactly one
  filter object over the range, and element 3 giving where the engine cannot carry
  both. SD-FMT-29.
- **19.4 ITEM 2b's DENOMINATOR IS DEFINED AND IS READ OFF THE APPENDIX.** "Used
  this run" was undecidable for a variable a planning run never reaches. The
  denominator is every DEFERRED variable in the schema less the ones bound, counted
  from SECTION A1 and A2 row by row at run time rather than restated from memory,
  reconciled against that appendix's own counts block, with the never-reached ones
  counted in 2b and named as such.
- **THE UNIFORM-COLUMN LINE HAS ONE COMPOSED FORM.** 1.3b named the sections per
  column and 19.3.1 named the columns together, so two uniform columns across three
  sections had no stated shape and block 1 is a closed enumeration a line is never
  invented into. 19.3.1 block 1 item 7 now carries the composed form with both
  lists variable, tested at zero, at one and at many on each axis per SD-LNG-13,
  and 1.3b defers to it rather than stating a second shape.
- **THREE SHARED RULES ARE CARRIED THAT THIS FILE DID NOT CITE.** SD-CNF-10 at
  26.2, so a person's own claim that a resolved cell contradicts is a third state
  with its own label, neither source winning, nothing contradicted entering a
  permanent record and nothing deleted. SD-FMT-28 at 1.10, 17.3 and 18.2, for the
  grid width bound. SD-POP-30 at 11.2, so the not-workable exclusion states which
  of its two readings this skill applies and why.
