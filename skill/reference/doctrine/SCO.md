# GROUP SCO: SCORING

### SD-SCO-01 Close date FIRST, and rule one is primary and sufficient on its own
- Rule: work three rules in order and stop at the first that fires. Rule 1 reads
  the published due date, or takes full weight for supervisor-named or locally
  loaded work. Rule 2 reads a period token in the item's own name, resolved
  through the operating window. Rule 3 drops anything with no derivable date.
- Mechanism: named as the most damaging way to implement the section wrongly, and
  why: "Rule 2 is the one with concrete mechanics, a token to search for, so an
  implementer naturally reaches for it and treats rule 1 as commentary. That
  inverts the ladder."
- Prevents: "The absence of a date token in a column header is NOT evidence that
  the item has no close date; it is the normal case, because sources name work by
  what to do rather than by when." The documented harm: the two largest live items
  carried no token, "so a rule-2-first implementation scored them at zero, and
  nothing in the output looked wrong."
- Source: P-D192
- Applies: PLANNING, SCORECARD

### SD-SCO-02 Admission and weight are separate answers from ONE matcher
- Rule: matching the published source decides ADMISSION; the published date then
  decides the CLOSE WEIGHT independently. "Use one matcher, read two things from
  it: membership, and the date. Never assume the date from the membership."
- Source: P-D193
- Applies: PLANNING, SCORECARD

### SD-SCO-03 The operating cycle is the only authority for when work is due
- Rule: resolve every period token against the operating window, never against
  the calendar or fiscal quarter. A calendar or fiscal quarter end is never an
  authority at any level; it is only ever an input the window converts.
- Mechanism: "A calendar quarter ends on a month boundary because that is how
  financial reporting divides the year. The operation does not stop on that
  boundary. The days between are a reporting artifact and carry no work." A token
  whose calendar end falls on or before the current window's close, or in the gap
  before the next window opens, bands to full weight.
- Prevents: the documented harm, where banding a token down on the strength of a
  quarter end "moved a unit from rank 4 to rank 1 between two real runs."
- General form: the operational calendar, not the reporting calendar, governs
  when work is due.
- Source: P-D194
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SCO-04 Precedence stated once so nothing has to be re-derived
- Rule: the published due date always wins; then the operating window; then a
  period token in the name, resolved THROUGH the window.
- Source: P-D195
- Applies: PLANNING, SCORECARD

### SD-SCO-05 Anything with no derivable date is DROPPED from scoring entirely
- Rule: it contributes nothing, and it is not down-weighted. "A unit is not more
  important because it carries five undated flags."
- Source: P-D196
- Applies: PLANNING, SCORECARD

### SD-SCO-06 Expired prior-period work stays visible at the floor weight and contributes ZERO to workload
- Rule: a token resolving to a window that closed strictly before the current
  window opened bands to the floor weight and zero toward the workload count,
  labelled as carryover on the row, "so a person who still owes the work can see
  it, but it can never outrank current-period work and never inflates the
  workload count. Only current-period work is ever at full weight."
- Source: P-D197
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SCO-07 Each close weight has exactly one defined trigger
- Rule: the permitted close weights are the values in CLOSE_WEIGHTS and no
  others. "Never produce an intermediate weight from a date you successfully
  read, and never default an unreadable date to full weight."
- **THE LADDER MUST BE EXHAUSTIVE OVER THE NUMBER LINE.** A closed set of weights
  is only closed if every derivable date falls in exactly one band. The standing
  set left a gap between the next window and the far horizon: a date after the
  next window but still inside the near horizon fell in no band, so an
  implementation either dropped those items or banded them to the floor on its own
  judgment, and two implementations differed. The set now carries a band for that
  range. When a band is added or a boundary moved, the ladder is re-checked for
  gaps before the change ships.
- **EVERY BAND IS ANCHORED ON THE WINDOW BEING PLANNED, NEVER ON THE RUN DATE.**
  "This window" in the top band means the window the plan is FOR, so every other
  band inherits the same anchor and the ladder cannot contradict itself. A near
  horizon counted from the run date instead of from the planned window's close
  moves items between the two lowest bands purely according to how early the plan
  was built: on one real file of a couple of hundred records it moved 8 percent of
  the population, which reorders the published list. Two competent readers then
  produce two different lists off one file and one configuration. Print the anchor
  date itself, as a date, so the banding is reproducible without inferring it.
- The
  probable-this-period weight contributes ZERO to the workload count, because
  that count requires certainty, and the weight exists precisely to record that
  this period is probable rather than confirmed.
- Source: P-D198
- Applies: PLANNING, SCORECARD

### SD-SCO-08 A SCORING item requires all three conditions, and one subsumes another
- Rule: the item is flagged at this unit; it has a derivable close date; and it
  matches a stated priority or carries the user's own scope code. The third
  automatically satisfies the second, "so the second never independently rejects
  an item the third accepted."
- Mechanism: "An item the unit carries that matches no stated priority contributes
  NOTHING to this term, however many of them there are. That is what stops the
  term becoming a weighted item count, which is forbidden."
- Source: P-D217
- Applies: PLANNING, SCORECARD

### SD-SCO-09 Every gap term has a NAMED SOURCE so two implementers score the same units
- Rule: a closed set of flat terms at GAP_TERM_WEIGHT each with explicit source
  definitions, plus one graduated bucket, summing to GAP_TERM_CAP.
- Mechanism: "The flat set is complete: there is no additional term. Do not cap
  below the reachable maximum, and do not add a term without raising the cap to
  match: a cap set under the reachable maximum silently clips the highest-signal
  units, which are the units this method exists to surface."
- Source: P-D221
- Applies: PLANNING, SCORECARD

### SD-SCO-10 A shared source column does not mean a shared test; compute the overlap
- Rule: two terms may read the same column and still have different tests. Any
  double count is bounded and must be COMPUTED from both columns, never assumed.
- Mechanism: in one real file the two tests disagreed on 133 of 354 units, "so
  reading the identifier alone would grant the second term to all 354 and
  over-count 133 of them." One intended double count is declared explicitly and no
  other term may be double-counted.
- Source: P-D222
- Applies: PLANNING, SCORECARD

### SD-SCO-11 A term whose source does not resolve is not scored and NEVER becomes a default
- Rule: it is named as not evaluated.
- Source: P-D223
- Applies: PLANNING, SCORECARD

### SD-SCO-12 Cap the COUNT first, then multiply; never cap the product
- Rule: the workload term contributes min(count, WORKLOAD_COUNT_CAP) times
  WORKLOAD_MULTIPLIER.
- Prevents: a unit climbing on volume of work alone.
- Source: P-D224
- Applies: PLANNING, SCORECARD

### SD-SCO-13 Alignment and workload are different populations on purpose
- Rule: the workload count counts every item closing this period whatever its type
  and whether or not it matched a stated priority. The alignment term counts only
  the ones that matched and scales each by work type. Neither is a subset of the
  other.
- Mechanism: "Alignment asks how much of what leadership asked for is open here.
  Workload asks how much work is open here at all. A unit carrying four items that
  close this period is a busy unit even if nobody named them, and the person still
  has to do them." An item dated by the second rule with no priority match
  contributes to workload and nothing to alignment: "that is correct, not a leak."
- Source: P-D225
- Applies: PLANNING, SCORECARD

### SD-SCO-14 The scoring formula, written out and implemented exactly
- Rule: score equals (BASE_TERM plus alignment plus gap plus min(workload_count,
  WORKLOAD_COUNT_CAP) times WORKLOAD_MULTIPLIER plus steer) times (measure_pct
  raised to MEASURE_EXPONENT), where alignment is the sum over scoring items of
  entity_weight times close_weight times source_boost times work_weight times
  local_boost, followed by the zero bucket applied after the score and before the
  rank.
- Note: the shape is portable as written; every constant is a bound value.
- Source: P-D226
- Applies: PLANNING, SCORECARD

### SD-SCO-15 Say what the multiplicative shape actually does, so nobody re-derives it wrongly
- Rule: the bracket ranges from its base to roughly an order of magnitude, and the
  measure factor ranges from zero to one and can only scale it down. Among the
  units competing for the top, the measure varies only slightly while the bracket
  can vary several-fold. "The measure is therefore the tie-shaper rather than the
  sole rank driver. Do not describe it as the dominant term in the ordering,
  because it is not."
- General form: describe the model's actual behaviour, not its intended emphasis.
- Source: P-D227
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SCO-16 A deterministic tie-break is mandatory, and its measure is the run's own basis
- Rule: score descending, then the measure descending, then the identifier
  ascending. "The measure here means whichever column supplied the percentile for
  this run. One key, defined by the run's own basis, so the tie-break never
  silently switches measures."
- Mechanism: "Without it a rerun on the same file can return a different list,
  which breaks the repeatability guarantee. Ties are real rather than
  hypothetical: several units share the exact measure value at the section cut
  line."
- Source: P-D228
- Applies: PLANNING, SCORECARD

### SD-SCO-17 A window named for a period covers every day of that period
- Rule: THE COVERING INVARIANT. Where an operating window is NAMED for a calendar
  period, every day inside that period falls inside the window that names it. A
  derivation that leaves a day of the named month outside the month's own window is
  a BINDING ERROR, rejected at validation, not a disclosure.
- The named case: a nominal period length of thirty days, anchored on the first day
  of a calendar month, left the thirty-first day of a thirty-one day month outside
  the window. A commitment falling on the last day of the month being planned was
  therefore banded as belonging to the NEXT window and weighted down accordingly, on
  a plan whose own title named that month. A person handed their plan for a named
  month is entitled to have every day of that month in it, and no amount of
  correct arithmetic underneath repairs that.
- **THE NAME IS THE AUTHORITY, AND IT SELECTS THE DERIVATION.** Where the period
  name denotes a CALENDAR unit, a month, a quarter, a half or a year, the window IS
  that unit entirely, first day to last, and the nominal length is used only for
  horizon arithmetic such as a near horizon or a lookahead. Where the name denotes a
  ROLLING or fiscal window that is not a calendar unit, a four-week cycle or a
  thirteen-period year, the nominal length sets the boundaries and the invariant is
  satisfied trivially because no calendar unit is being named.
- Rule: a nominal length that disagrees with the calendar unit it is bound
  alongside is not an error in the binding and is not corrected. It is retained,
  because it is what the business calls the length of its period, and it is simply
  not used to cut the window. Where the two differ by more than a few days, say so
  once: the business may have meant a rolling window and named it loosely.
- Rule: never resolve a covering failure by shortening the period, by moving the
  anchor, or by silently extending the window past the unit it names. The window is
  the unit; the arithmetic bends to it.
- Prevents: a day of the month being planned falling outside the plan for that
  month, which is invisible to every gate because every date in the artifact is
  individually correct.
- Source: final ship run, LOW 4
- Applies: PLANNING, REVIEW, SCORECARD

---
