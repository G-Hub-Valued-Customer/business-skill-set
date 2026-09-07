# GROUP 18: EXCEPTION FLAGS AND THRESHOLDS

TAXONOMY SHAPE, EXCEPTION_FLAGS. Each flag carries `key`, `display_name`,
`weight`, `source_concepts`, `test`, `requires_decision_authority_at_unit`
(boolean), `membership_conferring` (boolean; a shown-never-scored value is
false), `scales_with_local_cadence` (boolean), and `exemptions`.

TAXONOMY SHAPE, CLASSIFICATION_LABELS. The closed set of states a scored cell may
hold. Each entry carries:
- `key`: stable id, never renamed, because a scored grid is compared across
  periods.
- `display_label`: the word written into the cell.
- `symbol`: a single permitted character written alongside the label, so the
  state survives in a plain text rendering with no fill.
- `is_scored`: whether the cell contributes to any denominator.
- `is_pass`: whether the cell counts as met, for the scored subset only.
- `fill_variable`: the palette variable that fills the cell.
- `requires_reason_code`: whether a cell in this state must carry a code from
  REASON_CODE_SET.

The five standing states are PASS, GAP, UNASSESSABLE, NOT REQUIRED and RETIRED.
Only PASS and GAP are scored; the other three are shown, counted separately, and
excluded from the denominator, which is what stops an unassessable requirement
being reported as a failure.

DO NOT REUSE STATUS_VALUES FOR THIS. STATUS_VALUES holds per-objective progress
on a review form and means on track or behind. These are cell states in a scored
grid and mean met, missed, could not be judged, out of scope, and withdrawn. The
two vocabularies look similar and are not: conflating them makes a not-required
cell count as a behind objective, and an unassessable cell count as a gap, which
is the specific inversion this separation exists to prevent.

TAXONOMY SHAPE, REASON_CODE_SET. The closed vocabulary written into the row
margin explaining every cell that is not a plain pass. Each entry carries:
- `code`: short stable token, written as CELL TEXT, never only as a colour.
- `applies_to`: which CLASSIFICATION_LABELS keys may carry it.
- `meaning`: one line, in the business's own words.
- `implied_action`: what the reader is supposed to do about it. A code with no
  implied action is a label, not a reason, and does not belong in the set.
- `resolvable_by`: the role or function that can clear it, so an unresolvable
  code is visible as such.

Two rules govern the set. First, it is CLOSED: a run may not invent a reason, and
a reason that does not fit is reported as unmapped and routed to the binding
owner, who extends the set. Free text in this position defeats the whole purpose,
because it cannot be counted, compared between periods or acted on in bulk.
Second, the code is written as CELL TEXT. Colour is a second channel and never
the only one, so the classification survives printing, copying into another
format, a colour-blind reader, and the complete loss of the palette.

TAXONOMY SHAPE, PASS_QUALIFIER_VOCABULARY. A KEYED SET with exactly TWO entries,
looked up BY KEY, written into a PASS cell beside the pass itself. Each entry
carries:
- `key`: from the fixed pair below. Never renamed.
- `label`: the string written in the cell after the pass. Short: it shares a cell
  with the state it qualifies.
- `code`: the SHORT BOUND TOKEN the cell carries when the label itself has moved to
  the legend under the first rung of the output contract's relief ladder, published
  in the legend against this entry's full `label`. **IT IS BOUND AND IT IS NEVER AN
  ORDINAL.** A skill was using each entry's POSITION in the set as its legend code,
  which works exactly until a member is added, at which point every legend code in
  every prior period's workbook means a different qualifier and nothing in either
  file says so. A code is an identity and an ordinal is an accident of order.

**WHY A PASS NEEDS A QUALIFIER AT ALL, AND WHY IT CANNOT LIVE IN REASON_CODE_SET.**
REASON_CODE_SET explains every cell that is NOT a plain pass, and it is closed at
four families, all of them non-pass. A pass whose met-condition is half PRESENCE and
half RECENCY, tested where the evidence carries a date and untestable where it does
not, is still a pass; it is not a gap, not unassessable, not out of scope and not
retired, so it has no home in that set and it cannot be given one without breaking
that set's own coverage validation. It gets its own closed pair instead.

**THE TWO KEYS ARE FIXED VOCABULARY:** `attested`, where the evidence was found AND
its age was tested against the window; and `presence_only_recency_untested`, where
the evidence was found and no date could be read, so presence alone carried the
cell.

**THE STATES-TO-SET VALIDATION UNDER S10.** A cell is a pass only where the evidence
was found. Given that, its date either could be read and tested or could not, which
is two cases and no third: a date that WAS read and failed the window is not a pass
at all, it is a gap, which is exactly why the pair is total rather than merely
convenient. A run meeting a pass it can place in neither member does NOT take the
nearer one: it reports the cell, names the state it could not qualify, and the hole
goes to the binding owner, per S10.


| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| EXCEPTION_FLAGS | The scored flags whose members form the exception section, PER POPULATION SHAPE. | ORG | DEFERRED | taxonomy | Keyed by shape: a fixed set and a flow set, each with at least 1 flag. Every flag carries the shape it applies to. Every flag with requires_decision_authority_at_unit true names the influence test. Flags whose columns do not resolve or carry no data are skipped and named, never treated as gaps. Per SD-POP-23 the shape is read from the population being scored, not from the company. | FIXED: coverage stale 2.0; presence absent 2.0; benchmark shortfall 3.0; commitment missing 2.0. FLOW: stage age above local dwell 2.0; past due and still open 3.0; no next action 2.0; exit date moved repeatedly 2.0 |
| FLAG_MEASURE_MULTIPLIER_FLOOR | The floor of the size multiplier applied to the summed flag weight, so a real problem at a small unit stays visible. | ORG | DEFERRED | scalar | Between 0 and 1, strictly above 0. | 0.5 |
| PRIORITY_BAND_THRESHOLDS | The bands applied AFTER the size multiplier. May be bound as SHARES of the attainable maximum or as ABSOLUTE scores; the default is shares. | ORG | DEFERRED | mapping | Where bound as shares, each is strictly between 0 and 1 and the bands are ordered. Where bound as absolute scores, the binding is REJECTED AT VALIDATION if the top band exceeds the attainable maximum for the flag set it is bound alongside, because a band nobody can reach is a band that does not exist. Never set against the raw flag weights without the multiplier. | high at or above 0.50 of attainable; medium at or above 0.25 of attainable |
| EXCEPTION_ALERT_RECONCILIATION | The single row an empty exception section carries when the alert line is non-zero, explaining why two correct measures disagree. | ORG | DEFERRED | scalar | Required whenever the alert count is non-zero and the section has no members. Names both counts, both thresholds and the reason. | see SECTION A1 |
| PRIORITY_BAND_LABELS | Display labels for those bands. | ORG | DEFERRED | list | One per threshold plus the residual. | High; Medium; Low |
| RECENCY_FLOOR_DAYS | Absolute floor of the membership recency threshold. | ORG | DEFERRED | scalar | Positive integer. | 60 |
| RECENCY_MEDIAN_FACTOR | Multiplier on the local median cadence; the membership threshold is the larger of the floor and this product. | ORG | DEFERRED | scalar | Greater than 1. | 2 |
| ALERT_WARN_DAYS | Start of the approaching band on the flat alert. | ORG | DEFERRED | scalar | Positive integer, less than ALERT_OVERDUE_DAYS. | 150 |
| ALERT_OVERDUE_DAYS | Start of the overdue band on the flat alert. This alert does NOT scale with local cadence. | ORG | DEFERRED | scalar | Positive integer. | 180 |
| ALERT_SCALES | Whether the alert scales with local cadence. | ORG | DEFERRED | scalar | Boolean. Must be false. The membership flag scales; the alert does not. | false |
| ALERT_COUNT_POPULATION | Whether alert counts are taken over the whole ranked population or over displayed rows. | ORG | DEFERRED | scalar | Must be whole_population. Shaded cells are a SUBSET of reported counts and the gate must allow that. | whole_population |
| BENCHMARK_GAP_THRESHOLD | The shortfall at which a benchmark flag fires, on the column's own scale. | ORG | DEFERRED | scalar | Scale read from the column's own maximum each run. | 0.25 fractional, or 25 points |
| SIZE_GATED_PROGRAM_TEST | The size test that qualifies a unit for a cost-bearing program flag, replacing any geography test. | ORG | DEFERRED | scalar | Must be a size test computed from the user's own file each run. | at or above the scope median measure |
| RECENCY_LAG_DISCLAIMER | The visible note stating how far the recency field lags reality and that it is not used in ranking. | ORG | DEFERRED | scalar | Non-empty when a recency flag is bound. | Last contact date can lag actual contact by up to two weeks. Treat as a prompt to confirm. Not used in ranking. |
| FLAG_EXEMPTIONS | Per flag, the classes exempt from it, kept as belt and braces after an upstream class exclusion. | ORG | OPTIONAL | mapping | An exempt-class row appearing on the exception section is evidence the upstream exclusion failed and blocks publication. Never extended by analogy. | coverage stale exempts third-party administered |
| CLASSIFICATION_LABELS | The closed set of states a scored cell may hold, with the label, the symbol and the fill for each. | ORG | DEFERRED | taxonomy | Exactly the five standing keys unless the binding owner adds one deliberately. Exactly two are scored. Every key names a fill variable and a symbol, **and every one of the five now HAS a fill variable to name: COLOR_STATUS_PASS, COLOR_STATUS_GAP, COLOR_STATUS_UNASSESSABLE, COLOR_STATUS_NOT_SCORED and COLOR_STATUS_RETIRED.** A key added by the binding owner brings its own fill variable with it, or it carries no fill and the legend names it; it never borrows another key's, which the one-fill-per-state rule forbids. Never bound to STATUS_VALUES. | PASS; GAP; UNASSESSABLE; NOT REQUIRED; RETIRED |
| PASS_QUALIFIER_VOCABULARY | The two qualifiers written into a PASS cell beside the pass, saying whether the pass was attested or rested on presence alone because no date could be read. Looked up by key. | ORG | DEFERRED | taxonomy | **TOTAL OVER THE TWO KEYS, AND THE TOTALITY IS THE VALIDATION: exactly two entries, one per key, no key absent, no key repeated, no third key.** Every entry carries a non-empty `label` with no placeholder and a non-empty `code`. **THE CODE IS SHORT, STABLE, UNIQUE WITHIN THE SET, AND NEVER THE ENTRY'S ORDINAL POSITION**, which renumbers the moment a member is added and silently re-reads every legend already printed. Written as CELL TEXT beside the state, never as colour and never only in a legend, because a pass that is qualified only in a legend is an unqualified pass everywhere the cell is read; where the relief ladder has moved the full label to the legend the CODE is what stays in the cell, and a code with no legend row is the one way that step can be done wrongly. A pass that fits neither key is REPORTED as a hole rather than assigned the nearer key. | see the SECTION A1 default, which is the standing pair |
| REASON_CODE_SET | The closed reason vocabulary written into the row margin explaining every cell that is not a plain pass. | ORG | DEFERRED | taxonomy | Closed, extended only by the binding owner. Every code names its implied action and who can clear it. Written as cell text, never as colour alone. **COVERAGE VALIDATION, and it is not optional: the set must carry at least one code for EVERY non-pass state in CLASSIFICATION_LABELS. A closed set that cannot name a state the contract can produce guarantees an unmapped cell on every run in which that state occurs, which is the commonest state on most runs.** | see the SECTION A1 default, which is the seeded set in four families |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 18: Exception flags and thresholds

| Variable | Documented default | Degradation notice |
|---|---|---|
| EXCEPTION_FLAGS | SHAPE DEPENDENT, read from the population being scored, **AND EVERY FLAG CARRIES AN EXPLICIT WEIGHT, because the banding cannot be computed without one.** Under FIXED: coverage stale 2.0; presence absent 2.0; benchmark shortfall 3.0; commitment missing 2.0. Under FLOW: stage age above the local median dwell for that stage 2.0; a past-due exit date with the item still open 3.0; no next action recorded 2.0; an exit date moved more than once 2.0. The heavier weight in each set is the flag that names a broken commitment rather than a stale one, because a missed promise outranks a quiet gap. A flag whose column does not resolve or carries no data is skipped, named, and REMOVED FROM THE ATTAINABLE MAXIMUM, per PRIORITY_BAND_THRESHOLDS. | The exception flags have not been defined for your organization, so the generic set for this population's shape was used, with the standing weights. This population is {shape}, so the flags evaluated were {the flags that evaluated, with their weights}, and {the flags that could not be evaluated} could not be evaluated and were excluded from the scoring range rather than counted as zero. No absent column was treated as a gap. |
| FLAG_MEASURE_MULTIPLIER_FLOOR | 0.5. | The standing half floor was used, which is what keeps a genuine problem at a small unit visible rather than erasing it. |
| PRIORITY_BAND_THRESHOLDS | **EXPRESSED AS SHARES OF THE ATTAINABLE MAXIMUM, NOT AS ABSOLUTE SCORES: high at or above 0.50, medium at or above 0.25, low below.** The ATTAINABLE MAXIMUM is the sum of the weights of the flags that ACTUALLY EVALUATED on this run, times the largest size multiplier in play. Absolute thresholds remain a legal bound form, and where they are bound they are used as given; the shares are what the DEFAULT uses, because a default cannot know how many flags a given file will support. | The exception bands were not set for your organization, so the standing shares were used against what was actually reachable on this file: {the flags that evaluated and their weights}, giving an attainable maximum of {value}, so the high band starts at {value} and the medium band at {value}. Absolute thresholds are not used by default because they cannot be reached when fewer flags resolve than the thresholds were calibrated against. |
| EXCEPTION_ALERT_RECONCILIATION | APPLIES whenever the alert line reports a non-zero count and the exception section is EMPTY; where either condition fails this variable is not read at all. THE DEFAULT: both statements stand, because they measure different things, and the empty section carries ONE row saying so in the reader's own terms, naming both counts, both thresholds and the reason they differ. | The alert line and the exception section disagree on this file and both are correct. The alert uses FLAT day bands, the same everywhere. The exception flag SCALES with this population's own cadence, whose median interval here is {value} {day or days}, so its threshold is {value} {day or days} and the oldest item in the file is {value} {day or days}. Nothing is being hidden and nothing is broken: one measure is absolute and the other is relative to how this book actually behaves. |
| PRIORITY_BAND_LABELS | High, Medium, Low. | The standing band labels were used. |
| RECENCY_FLOOR_DAYS | 60. The interval it floors is shape dependent: under FIXED it is the interval since last meaningful contact with the unit, and under FLOW it is the age of the item in its current stage. | The standing recency floor was used, and the actual threshold is the larger of that floor and the local median interval times the bound factor. This population is {shape}, so the interval measured was {time since last contact, or age in current stage}. |
| RECENCY_MEDIAN_FACTOR | 2. It multiplies the local median CADENCE under FIXED and the local median STAGE DWELL under FLOW. | The standing multiplier was used, applied to the local median for this population's shape: your own contact cadence under a fixed roster, or the median dwell in the same stage under a flowing population. |
| ALERT_WARN_DAYS | 150 days without contact under FIXED. Under FLOW the flat alert measures days past the item's own due or exit date while it is still open, and the standing band is 0 days, meaning the day it goes past due. | The standing approaching-threshold band was used, and it is flat rather than scaled, per SD-EXC-03. This population is {shape}, so the alert counted {days since last contact, or days past due while still open}. |
| ALERT_OVERDUE_DAYS | 180 days without contact under FIXED. Under FLOW, 30 days past the item's own due or exit date while it is still open. | The standing overdue band was used, and it is flat rather than scaled. This population is {shape}, so the band counted {days since last contact, or days past due while still open}. |
| ALERT_SCALES | false. | The alert is flat while the membership flag scales with your local cadence, which is the only permitted setting. |
| ALERT_COUNT_POPULATION | whole_population. | Alert counts are taken over the whole ranked population and may exceed the shaded rows you can see, which is stated beside the counts. |
| BENCHMARK_GAP_THRESHOLD | A quarter of the column's own scale, read from the column's own maximum each run. | No benchmark shortfall threshold has been set, so a quarter of the column's own range was used and the scale detected is named. |
| SIZE_GATED_PROGRAM_TEST | At or above the scope median measure, recomputed from your own file each run. | No size test has been set for cost-bearing programs, so the median of your own scope was used and the figure is printed. |
| RECENCY_LAG_DISCLAIMER | SHAPE DEPENDENT. Under FIXED, the standing note that a last-contact field can lag actual contact and is not used in ranking. Under FLOW, the standing note that a stage or activity timestamp records when the record was updated rather than when the work happened, and is not used in ranking. | The standing lag disclaimer for this population's shape was printed. If your field does not lag, the note is harmless; if it lags further than the note says, tell the binding owner. |
| CLASSIFICATION_LABELS | The five standing states: PASS, GAP, UNASSESSABLE, NOT REQUIRED, RETIRED, with PASS and GAP scored and the other three shown, counted separately and excluded from the denominator. | The cell states have not been named for your organization, so the standing five were used. Each cell carries its state as text as well as a fill, so the grid reads correctly in print, in greyscale and with no colour at all. |
| PASS_QUALIFIER_VOCABULARY | **THE STANDING PAIR, TOTAL OVER THE TWO KEYS, AND THIS ROW IS THE ONLY STATEMENT OF THEM.** `attested`, label "attested", for a pass whose evidence was found and whose age was tested against the window. `presence_only_recency_untested`, label "presence only, recency untested", for a pass whose evidence was found and whose date could not be read, so presence alone carried the cell. **THE TWO CODES ARE `AT` AND `PO`**, bound here rather than derived from position, each published in the legend against its own full label. They are two characters because the cell they share is a scored cell in a wide grid, and they are letters rather than numbers because a number beside a state reads as a count. | The qualifiers on a passing cell were not bound, so the standing pair was used. They exist because half of what a requirement asks is usually WHEN, and a pass that rests on presence alone is a weaker statement than one whose date was checked. Both are written in the cell itself, so the distinction survives a copy into another format and the loss of the palette, and the count of each is reported so you can see how much of your pass rate was never dated. |
| REASON_CODE_SET | The seeded set, in FOUR families, because a set that cannot name the ORDINARY case is not a set. The count is four and not three: an earlier revision said three and then listed four, in the row whose entire subject is a coverage validation that counts members per family. **FAMILY 1, GAP, which is the commonest state and had no codes at all:** NOT_DONE, the requirement applies and no evidence of it exists, cleared by the unit owner; PARTIAL, some of the requirement is met and some is not, cleared by the unit owner; EXPIRED, it was met and the evidence has lapsed, cleared by the unit owner; SUPERSEDED, it was met to an earlier version of the standard, cleared by the unit owner; NOT_STARTED, it is in scope and no work has begun, cleared by the unit owner; IN_PROGRESS, work has begun and is incomplete at the census date, cleared by the unit owner; BLOCKED_EXTERNAL, work cannot proceed because something outside the reader's control is outstanding, cleared by the named external party and NOT by the reader; AWAITING_APPROVAL, complete and pending a decision by somebody else, cleared by the approver; EVIDENCE_MISSING, the work may be done and the evidence cannot be produced, cleared by the unit owner and distinct from NOT_DONE because the remedy differs. **FAMILY 2, UNASSESSABLE:** the eleven seeded reasons a requirement could not be assessed. **FAMILY 3, NOT_REQUIRED:** the eight seeded reasons it did not apply. **FAMILY 4, RETIRED, which the coverage validation below also found empty when it was written:** WITHDRAWN_BY_ISSUER, the requirement was removed from the standard, cleared by nobody and shown for continuity only; REPLACED_BY, superseded by a named successor requirement, cleared by nobody and carrying the successor's identifier; OUT_OF_SCOPE_NOW, the unit left the scope the requirement applies to, cleared by nobody. Every code in every family carries its implied action and who can clear it, INCLUDING the retired codes, whose implied action is explicitly NONE and whose resolvable_by is explicitly NOBODY, because a retired cell that looks actionable sends somebody to do work that no longer exists. | No reason codes have been bound for your organization, so the seeded set was used, and every non-pass cell carries a code from it. A cell whose reason does not fit any code is marked unmapped and named in the audit rather than given free text, and the binding owner can add the missing code once for everybody. |
