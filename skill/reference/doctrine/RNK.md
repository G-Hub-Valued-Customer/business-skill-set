# GROUP RNK: RANK CONTINUITY, CAPS AND CUTS

### SD-RNK-01 Ranks form one unbroken sequence across the merit sections
- Rule: the first action section starts at rank 1, the second resumes at the next
  rank, the reference section resumes after that. No gaps, no duplicates, no
  restart at 1. "A unit's rank is its position in the whole scope and has to mean
  the same thing on every section."
- **Rule: this describes a MERIT TIER SET.** A census starts at 1 and resumes from
  nothing, and an extract of a census repeats the census's own numbers. The
  underlying principle is the one that does not change: a unit's rank means its
  position in the whole scope on every sheet that shows it. See SD-FMT-25.
- Source: P-D32
- Applies: PLANNING, SCORECARD

### SD-RNK-02 Derived ceilings are consequences, never independent caps
- Rule: the last merit rank is derived as last_action_rank plus REFERENCE_CAP and
  must be recomputed whenever a resize changes last_action_rank. Never carry the
  literal.
- Mechanism: reading a derived ceiling as a row cap overruns the cap that every
  "showing n of N" reconciliation checks against and fails a correct-looking
  artifact at the final gate.
- Source: P-D33
- Applies: PLANNING, SCORECARD

### SD-RNK-03 A check that asserts the wrong number fails a correct artifact and burns the budget
- Rule: a gate must assert the number the contract actually produces. A gate
  asserting the tier size where the contract produces the derived ceiling is
  testing the wrong number.
- Mechanism: "This exact error shipped an unstyled artifact", because the failing
  gate sent a healthy build into a retry loop that consumed the budget the
  formatting pass needed.
- Prevents: a false-negative gate cascading into a real defect elsewhere.
- Source: P-D34
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RNK-04 The mandatory section is not a merit section and never consumes a merit slot
- Rule: mandatory units are ranked among themselves, are excluded from the merit
  sections, and never consume a merit rank or enter eligible_count. "A second
  action section holds its full count of merit-ranked units whether the directive
  named none or named thirty."
- Prevents: "a directive covering thirty units would otherwise consume a
  manager's entire first tier and push out genuine opportunity."
- Source: P-D35
- Applies: PLANNING, SCORECARD

### SD-RNK-05 The cap counts rows on the SECTION, not positions in the ranked list
- Rule: take ranked[last_tier : last_tier + REFERENCE_CAP], then confirm the
  section holds min(REFERENCE_CAP, eligible_count minus last_tier) rows before
  writing.
- Mechanism: "Slicing the ranked list at the cap and then removing the first tier
  yields a short section and silently drops that tier's worth of units; that is
  the error, and a real build made it."
- Source: P-D36
- Applies: PLANNING, SCORECARD

### SD-RNK-06 Write the shortfall note if and only if n is strictly less than N
- Rule: when the section holds everything it was supposed to hold there is no
  shortfall and the SHORTFALL note is omitted entirely. Two cases with different
  meanings of N: shortfall, where n is rows written and N is the section's own named
  size; and cap, where n is rows written and N is the count that qualified for that
  section. N is never the eligible pool and never the scope population.
- **Rule: THE SHOWING NOTE IS A DIFFERENT NOTE AND IS NEVER OMITTED.** It ships on
  every sheet whose row count is BOUNDED by anything, whether or not the bound cut
  anything, because it is the evidence the bound was evaluated, exactly as a zero count
  is the evidence a check ran. This rule governs the SHORTFALL note and is never read
  as licence to drop the showing note from a sheet that came in under its cap.
- **Rule: A SHEET IS BOUNDED BY MORE THAN ONE KIND OF THING, and each kind gives N its
  own meaning.** A cap bounds a reference or auxiliary sheet, a TIER SIZE bounds an
  action tier, and a DECLARED SIZE bounds an extract of a census. All three cut a real
  population down to a stated number of rows, which is what the showing note discloses,
  so all three ship it. "Carries no separate cap" said of a tier means it is not capped
  a SECOND time on top of its size; read as "not bounded at all" it leaves N undefined
  and two readers print different notes off one run.
- Prevents: "announcing a shortfall that did not occur tells the reader to go
  looking for missing units that do not exist."
- Rule: where a note of any kind is written, it goes in the sheet's NOTE BAND per
  SD-FMT-26, which is the one place a note about a grid may sit.
- Prevents: a reader taking the top of a census for the whole population, which is what
  an extract with no showing note invites; and a gate with nothing to reconcile on a
  sheet that came in under its cap.
- Source: P-D37; extended by the demonstration run, planning N10 and scorecard D12, D13
- Applies: PLANNING, SCORECARD

### SD-RNK-07 Cut an over-capped mandatory list by the honest axis, and name that axis
- Rule: cut the mandatory set by MEASURE rank, never by score. Publish the top
  REFERENCE_CAP by measure, order the displayed rows by score, and say MEASURE in
  the disclosure.
- Mechanism: score multiplies by the measure percentile and the zero bucket
  forces every no-measure unit to the bottom, "so a score-ranked cut therefore
  deletes the mandatory units the guarantee protects, silently, and the showing
  note discloses a count without disclosing the bias."
- Prevents: a cap silently deleting exactly the population an earlier guarantee
  protected. "Writing highest-scoring there is both false and dangerous."
- General form: a cap must be applied on an axis that does not interact with a
  protection elsewhere in the method.
- Source: P-D38
- Applies: PLANNING, SCORECARD

### SD-RNK-08 Do not extend the action lists to absorb overflow
- Rule: "Do not extend the action lists to absorb the overflow: a long ranked
  list is a roster, not a plan."
- Source: P-D39
- Applies: PLANNING, SCORECARD

### SD-RNK-09 The action list gets shorter RELATIVE TO SPAN as scope widens
- Rule: the tier shape is deliberate and scales to any span of control, because a
  more senior person has less time, not more. The action list is NEVER
  proportional to span: it grows far more slowly than the span it covers, so as a
  SHARE of what a reader owns it shrinks sharply as scope widens, while the
  reference depth stays constant.
- **THE ABSOLUTE ROW COUNTS MAY RISE, AND IN THE STANDING SIZES THEY DO.** The
  senior line's pair is the LARGER pair in rows. That is not a contradiction of
  this rule; it is the original design. A direct-tier reader owning a hundred
  units receives a first tier of ten, a tenth of their span. An aggregate-tier
  reader owning several thousand receives a first tier of twenty, a fraction of
  one percent. The second is by far the shorter list in the only sense that
  matters to the person holding it. Read as absolute rows, this rule would hand a
  senior leader fewer items than a frontline reader off the same file, which no
  version of this method has ever done, and it would contradict the standing sizes
  in the same table row that states them.
- Prevents: an action list that scales with span, which is a roster rather than a
  plan.
- Source: P-D40
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RNK-10 A final identifier key on every capped sort is mandatory, not decorative
- Rule: every sort that feeds a capped section ends with the unit identifier
  ascending, "because without a total order a tie straddling the cap makes the
  surviving set differ between runs, which breaks the repeatability guarantee."
- Source: P-D290; P-D228
- Applies: PLANNING, SCORECARD

### SD-RNK-11 Sort by the value, never by the classification label
- Rule: a classification label tells the reader what to do. It is an attribute,
  not a priority, and sorting on it inverts the value order.
- Mechanism: the named harm: sorting by label buried a high-value unit beneath a
  low-value one in the first build of a derived section.
- Source: P-D289
- Applies: PLANNING, SCORECARD

---
