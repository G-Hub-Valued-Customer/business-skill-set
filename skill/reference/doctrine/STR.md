# GROUP STR: THE STEER

### SD-STR-01 A lean and a restriction are not the same request
- Rule: four modes: LEAN, RESTRICT, INITIATIVE, NONE. Decided from the grammar of
  the request and named in the output so the reader can tell at a glance which
  list they are holding.
- Mechanism: a possessive or "for" construction naming the entity is a
  restriction; an explicit lean phrase is a lean.
- Source: P-D236
- Applies: PLANNING, SCORECARD

### SD-STR-02 The lean transform is exact, deterministic, and its consequence is written out
- Rule: set the named entity's weight to STEER_TILT_TARGET_WEIGHT and multiply
  every other entity's weight by STEER_TILT_OTHERS_FACTOR. Print the resulting
  weight matrix in full "so nobody has to derive them, and so the consequence is
  visible."
- Source: P-D237
- Applies: PLANNING, SCORECARD

### SD-STR-03 Taking the named entity ABOVE the standing top is what makes a lean mean anything
- Rule: if the named entity already sits at the standing top, leaving it there
  "would otherwise change nothing at all and return the unsteered list under a
  steered label."
- Prevents: a no-op that is labelled as an action.
- Source: P-D238
- Applies: PLANNING, SCORECARD

### SD-STR-04 A lean toward a low-ranked entity deliberately inverts the standing hierarchy
- Rule: "The standing hierarchy is the default ordering when nobody has said
  otherwise; a user naming an entity has said otherwise, and the lean is how the
  method honours it." Print the row of the table that was used so a reader who
  expects the default to lead can see why it did not.
- Source: P-D239
- Applies: PLANNING, SCORECARD

### SD-STR-05 Verify a lean did not silently become a restriction
- Rule: "if every unit in the result carries the named entity, you ran the wrong
  mode." A large unit with strong opportunity in another entity must still
  surface; that is the entire point of a lean.
- Source: P-D240
- Applies: PLANNING, SCORECARD

### SD-STR-06 A restriction changes the population AND the measure basis, and is applied in the scope stage
- Rule: it is a population operation exactly as a qualifier is, and must be folded
  into the same step, before every exclusion and before the percentile, because
  the median and percentile must be computed over the set the report is actually
  about.
- Mechanism: applied later, "a unit with strong standing in the named entity but
  modest total measure would be cut before its standing was ever considered, which
  is precisely backwards for a request asking for the biggest units in that
  entity." The other three modes do not restrict the population and stay where
  they are.
- Source: P-D241
- Applies: PLANNING, SCORECARD

### SD-STR-07 Never refuse an entity request because one column is absent
- Rule: fall back in order to another measure for that entity, then to membership
  by flags alone ranked on the scope measure. Name the basis used and say plainly
  when membership came from work flags rather than from that entity's own
  measure.
- Source: P-D242
- Applies: PLANNING, SCORECARD

### SD-STR-08 Zero survivors switches to the lean, and the measure basis reverts WITH it
- Rule: flip both together and name the reverted column. "If the mode flips and
  the basis does not, the ranking runs on a column that just proved to be empty
  across the population, every percentile collapses toward zero, and the list is
  meaningless." Fewer survivors than the list size is fine: deliver every one and
  say how many cleared. Zero survivors is not.
- Quote: "An empty artifact is never an acceptable answer to a reasonable
  question."
- Source: P-D243
- Applies: PLANNING, SCORECARD

### SD-STR-09 Filler words are stripped before reading the mode
- Rule: strip the filler nouns first, then decide on the grammar that remains.
  "Do not let a filler noun trigger the ambiguity rule."
- Source: P-D244
- Applies: PLANNING, SCORECARD

### SD-STR-10 When genuinely ambiguous, prefer the RECOVERABLE reading and say so in one line
- Rule: prefer the lean. "A lean still surfaces the entity's best units near the
  top, so an over-broad list is recoverable by the reader; a restriction that
  should have been a lean silently hides opportunity they will never know
  existed. Do not stop to ask: deliver the lean and note the reading."
- General form: when in doubt, choose the error the reader can detect and
  correct.
- Source: P-D245
- Applies: PLANNING, REVIEW, SCORECARD

### SD-STR-11 A steer re-weights; it never overrides what leadership asked for
- Rule: every mode still honours supervisor and central priorities and never
  releases a mandatory unit.
- Source: P-D246
- Applies: PLANNING, SCORECARD

### SD-STR-12 An entity-level steer never enters the formula as an additive term
- Rule: a lean acts by changing the entity weight inside the alignment term; a
  restriction acts by changing the population and the measure basis. The additive
  steer term exists only for a named initiative, "which is a membership fact about
  the unit rather than a re-weighting of a whole entity. Adding an entity steer as
  a separate additive term as well would apply the same preference twice."
- Source: P-D247
- Applies: PLANNING, SCORECARD

---
