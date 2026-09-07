# GROUP WGT: THE WEIGHTING HIERARCHY

### SD-WGT-01 The entity hierarchy table has NO default row
- Rule: an originator or entity that resolves to none of the listed entries is
  not assigned the top weight and is not assigned anything else either. It is
  reported as unmapped and takes no entity weight.
- Mechanism: "Defaulting an unknown to the top weight silently promotes it above
  every real entry at once. That is exactly what happened in a real build", where
  the unmapped item "became the single largest per-unit contributor in a scope
  where it should have been the smallest."
- Source: P-D173
- Applies: PLANNING, REVIEW, SCORECARD

### SD-WGT-02 When a default IS correct, tie it to the hierarchy FLOOR, not to a literal
- Rule: for an item whose entity cannot be resolved, apply ENTITY_WEIGHT_FLOOR and
  record that the floor was applied. Tie the default to the floor so it moves if
  the table's lowest weight changes; never hard-code a number that is also a real
  entry's weight.
- Mechanism: "What the floor guarantees is that resolving the entity can only
  raise the score, never lower it, because every real weight is at or above the
  floor. Defaulting to the top does the opposite, which rewards giving up."
- General form: a default must be positioned so that doing the work can only
  help.
- Source: P-D174
- Applies: PLANNING, REVIEW, SCORECARD

### SD-WGT-03 Protect the item while flooring its weight
- Rule: an item admitted on a local or supervisor test is still admitted
  automatically, still takes full close weight, still takes the source boost and
  still keeps the local boost, so the floor can never zero it or drop it from
  scoring. "Never let an unresolved entity remove a local item from scoring."
- Source: P-D175
- Applies: PLANNING, SCORECARD

### SD-WGT-04 The mandatory multiplier is applied ONCE, on the finished score
- Rule: never also inside a term. Applying it in both places squares it. It is
  listed alongside the entity weights for comparison only and is not one of them.
- Mechanism: because every mandatory unit receives the same multiplier it does not
  reorder its own section either. It is applied "so the score a reader sees
  matches the formula."
- Source: P-D176
- Applies: PLANNING, SCORECARD

### SD-WGT-05 Entity weight scales the alignment term ONLY, and never reorders the list by itself
- Rule: the final order is the combined score. "This is why a high-measure unit in
  a lower-ranked entity can and should outrank a small unit in the top entity.
  Never let entity rank alone reorder the list."
- Source: P-D177
- Applies: PLANNING, SCORECARD

### SD-WGT-06 The user is never expected to know the internal taxonomy
- Rule: map any brand, product, program or category word in the request to its
  parent entity before applying a steer, matching case-insensitively and
  tolerating the punctuation people actually type. "Nobody in the field says the
  internal entity code; they say the product name."
- Source: P-D178
- Applies: PLANNING, REVIEW, SCORECARD

### SD-WGT-07 A word naming a whole segment steers to our entry in it, but its measure includes others
- Rule: rank on our own measure, use the segment measure only to size the
  opportunity, and say which was which.
- Source: P-D179
- Applies: PLANNING, SCORECARD

### SD-WGT-08 A named initiative is a steer and is not an entity
- Rule: match against resolved column names and published initiative titles, on
  the distinctive words rather than the whole title, and treat a match as a lean
  toward the units carrying it. If it matches nothing, say so in one line and run
  without it. Never stop.
- Source: P-D180
- Applies: PLANNING, SCORECARD

### SD-WGT-09 Rank on the OWN measure, never the segment measure, and never let position decide it
- Rule: every entity has an own measure and a segment measure and they are not
  interchangeable. Test the own-measure stems to exhaustion before considering a
  segment stem. If only a segment measure exists, say so plainly and never
  present it as the entity's own figure.
- Mechanism: the documented trap. In one real file the segment column sat
  IMMEDIATELY LEFT of the entity's own column for every entity, "and the
  matcher's tie-break prefers the leftmost column, so a naive resolve picks the
  segment column every single time, for every entity." The user then receives a
  ranking on a competitor-inclusive measure while the front panel faithfully
  prints the wrong column's name.
- General form: a live trap where a generic tie-break rule systematically
  produces the wrong answer.
- Source: P-D191
- Applies: PLANNING, REVIEW, SCORECARD

### SD-WGT-10 Not all work is equally valuable: weight by WORK TYPE on a closed graduated scale
- Rule: exactly one type per work item, no extra type and no "other". The scale
  orders work by how much the state of the world changes because the person
  showed up.
- General form of the ladder: change a decision, above change a state, above
  change what someone knows, above confirm an existing state, above produce a
  record, above a label that asks for nothing. Persuading a counterparty to
  commit; configuring, migrating or physically altering something; training and
  enablement; audit and verification; logging and record hygiene; a segmentation
  marker naming the unit's standing.
- Prevents: "The old binary, business-building or weightless, collapsed all of
  that into two buckets and mis-typed the single highest-value item in the file."
- Source: P-D204; P-F4
- Applies: PLANNING, SCORECARD

### SD-WGT-11 A marker is not an instruction
- Rule: the bottom rung "admits the unit to the population and appears on its row,
  but it asks for nothing, so it scores nothing."
- General form: named as one of the sharpest distinctions in the corpus and
  entirely universal.
- Source: P-D204; P-F4
- Applies: PLANNING, REVIEW, SCORECARD

### SD-WGT-12 Work-type weight multiplies the ALIGNMENT term and nothing else
- Rule: a zero-weighted marker still counts toward the workload count if it
  carries a close date, still appears in the inventory, and still shows on the
  row. "It is considered; it is not scored."
- Source: P-D205
- Applies: PLANNING, SCORECARD

### SD-WGT-13 Scan the WHOLE name for every verb, then take the HIGHEST type present
- Rule: deliberate, because "when a header asks for two things, the person has to
  do the harder one, so the harder one sets the weight."
- Source: P-D206
- Applies: PLANNING, SCORECARD

### SD-WGT-14 A generic verb sets no type of its own and only promotes upward from below
- Rule: a generic completion verb promotes a low type one step, resolves to the
  baseline type when no specific verb is present, and never promotes a type
  already at or above that level.
- Mechanism: one generic verb appeared in sixteen headers of a real file and
  would otherwise have stamped all sixteen with one type.
- General form: a pattern for handling a semantically empty token.
- Source: P-D207
- Applies: PLANNING, REVIEW, SCORECARD

### SD-WGT-15 Verbless names are classified by the NOUN, never defaulted and never dropped
- Rule: a gap or opportunity noun paired with a physical-object noun is
  state-changing work; otherwise it is persuasion work. A noun naming only the
  unit's standing is a marker. Nothing matched is reported by name and weighted at
  the baseline.
- Mechanism: "Roughly half the work-item columns in a real file carry no verb."
  And: "A gap is something a person closes by persuading someone."
- Prevents: silently discounting a large unrecognized item. "Never silently
  discount an item the rules did not recognize; surface it so the dictionary can
  be extended."
- Source: P-D208
- Applies: PLANNING, SCORECARD

### SD-WGT-16 Classify by the VERB, not by the SUBJECT
- Rule: the most expensive single classification error in the corpus came from
  typing an item by its subject rather than its verb. "Selling the price, hanging
  the sign and checking the sign are three different jobs."
- Prevents: zeroing the highest-leverage conversation in the period.
- Source: P-D209; WORK_TYPE_CLASSIFY_BY
- Applies: PLANNING, REVIEW, SCORECARD

### SD-WGT-17 Never rank on how many work items an entity carries
- Rule: rank on the measure, the alignment and the number that must close this
  period. "A high-measure unit with two closing-now items outranks a mid-measure
  unit with nine undated ones."
- Source: P-D212
- Applies: PLANNING, SCORECARD

### SD-WGT-18 The measure weighting is universal and any new signal inherits it
- Rule: it applies to every opportunity the method surfaces, on every section,
  without exception, with a stated form per output.
- Source: P-D213
- Applies: PLANNING, SCORECARD

### SD-WGT-19 Apply the measure exactly ONCE per output
- Rule: score a cost-gated term flat and let the measure enter once through that
  section's own multiplier. "Never scale the commitment term by percentile
  separately; doing so applies the measure twice and buries the very units the
  section publishes."
- General form: double-counting the same factor in two places is named three
  separate times in the corpus. It is a defect class, not an occasional slip.
- Source: P-D214
- Applies: PLANNING, REVIEW, SCORECARD

### SD-WGT-20 A membership gate belongs only where membership is by flag
- Rule: an "only flag is X" test is meaningful on an exception list and undefined
  on a ranked list, where a unit appears because of its measure, alignment and
  workload rather than because of a flag. "One weight everywhere; one membership
  gate, on one section."
- Source: P-D215
- Applies: PLANNING, SCORECARD

---
