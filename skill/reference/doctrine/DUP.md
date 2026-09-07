# GROUP DUP: THE DE-DUPLICATION OF EFFORT

### SD-DUP-01 The coverage-duplication down-weight applies to the direct-action line ONLY
- Rule: check which report line is being built before discounting anything. It
  applies on the direct line and NEVER on the aggregate tier.
- Mechanism: "A manager deploys that second party. Those units are covered because
  that manager scheduled them to be covered, so showing them discounted
  misrepresents the manager's own resource deployment back to them."
- General form: a de-duplication discount is meaningful to the person choosing
  where to spend a day and misleading to the person who assigned the other
  resource. An account already worked this quarter by a solutions architect or a
  partner should be discounted on the seller's list and shown at full weight on
  the leader's. A patient already enrolled in a care-management programme should
  be discounted on the clinician's outreach list and not on the service-line
  director's.
- Source: P-D181; P-F3
- Applies: PLANNING, SCORECARD

### SD-DUP-02 Classification is line-independent; only the WEIGHT is gated
- Rule: run the actor test on every list at every level, so a directive is never
  mistaken for an assignment on a senior report either. The classification decides
  which section; the line decides whether the multiplier applies.
- Source: P-D182
- Applies: PLANNING, SCORECARD

### SD-DUP-03 On the senior line the assignment is still identified and reported, just not weighted
- Rule: name the list, its sender and date, and note the affected units on their
  rows, "because that is their own deployment showing up in their own report.
  What they must not see is those units pushed down the ranking for it."
- Source: P-D183
- Applies: PLANNING, SCORECARD

### SD-DUP-04 Derive the other actor's unit set from the code, do not pattern-match the digits
- Rule: derive the code from the user's own coarser code by the stated
  construction, and test for equality against that one derived code, not a suffix
  search across the file. "A unit ending in the same suffix in a DIFFERENT parent
  is a different parent's specialist and is irrelevant."
- General form: derive, then test equality. The three-source ladder is: a
  derivable identifier where the scheme supports one, then an explicit assignment
  list, then a per-unit flag naming the other actor.
- Source: P-D184; P-F3
- Applies: PLANNING, SCORECARD

### SD-DUP-05 An absent second actor is a NORMAL result, not a failure
- Rule: when the derived code matches zero rows, say exactly that, fall to the
  next source, and if none resolve apply no discount and record that none was
  identified. Never invent the set, never assume the pattern holds, never treat
  the absence as a reason to stop.
- Source: P-D185
- Applies: PLANNING, SCORECARD

### SD-DUP-06 Discount only when the unit's ONLY open work is the other actor's
- Rule: a unit carrying the other actor's work ALONGSIDE its own actionable work
  is not down-weighted, because the person has their own reason to be there.
  Check the unit's own open work before applying the discount; never discount on
  list membership alone.
- Source: P-D186
- Applies: PLANNING, SCORECARD

### SD-DUP-07 Scale rather than exclude, so a big opportunity still surfaces
- Rule: the unit stays on the list and stays visible, "because a genuinely big
  opportunity should still surface through the discount: that is the point of
  scaling rather than excluding." State on the row why it ranks low so the person
  can override on their own judgment.
- Source: P-D187
- Applies: PLANNING, SCORECARD

---
