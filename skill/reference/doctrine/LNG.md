# GROUP LNG: LANGUAGE, TONE AND THE READER

### SD-LNG-01 Measure impact; do not judge the remainder
- Rule: say business impact, never a phrase that ranks the rest as unimportant.
  "Every unit matters to the person who owns it. This method measures which units
  carry the most business impact: that is a measurement, not a judgment about the
  rest."
- Rule: "The ranking already communicates priority; commentary that ranks the
  units against each other in words is editorializing. Write toward impact, never
  toward shame."
- Source: P-D292
- Applies: PLANNING, REVIEW, SCORECARD

### SD-LNG-02 Refuse to rank or evaluate PEOPLE
- Rule: these skills rank units of business. A request to rank or evaluate named
  people is declined outright.
- Source: P-D293
- Applies: PLANNING, REVIEW, SCORECARD

### SD-LNG-03 Never open with methodology, caveats or reconciliation
- Rule: those are internal. The finding leads.
- Source: R-D41 guardrail 6
- Applies: PLANNING, REVIEW, SCORECARD

### SD-LNG-04 Report the count of items dated by EACH rule separately
- Rule: "Naming the split is what makes the rule-inversion bug visible: a run
  reporting zero items dated by the first rule, on a period whose brief named
  several, has inverted the ladder."
- General form: instrument the audit trail specifically so the known failure mode
  has an observable signature.
- Source: P-D298
- Applies: PLANNING, REVIEW, SCORECARD

### SD-LNG-05 Name every item that took a fallback weight and the weight it took
- Rule: so a reader can see which work was scored as probable rather than
  confirmed.
- Source: P-D299
- Applies: PLANNING, REVIEW, SCORECARD

### SD-LNG-06 Name every item weighted zero, by name and count
- Rule: "A large item that scored nothing must be visible here", so a person can
  see that it was deliberately scored low rather than wonder why their biggest
  number moved nothing.
- Source: P-D300
- Applies: PLANNING, REVIEW, SCORECARD

### SD-LNG-07 Use the organization's exact vocabulary
- Rule: use CONTROLLED_VOCABULARY terms exactly as the business writes them. Do
  not paraphrase a term of art.
- Source: R 10.2
- Applies: PLANNING, REVIEW, SCORECARD

### SD-LNG-08 Write short by default
- Rule: do not write long and trim afterward. Target TARGET_FILL_RATIO of the
  confirmed limit so a user edit does not push the field over. Count the exact
  string that will be pasted, not the word count and not the visible length:
  spaces, punctuation and line breaks all count.
- Source: R-D15
- Applies: REVIEW

### SD-LNG-13 A templated sentence carrying a count is agreement-safe at zero and at one
- Rule: any sentence generated with a number in it is written so it reads
  correctly when that number is ZERO and when it is ONE, not only when it is many.
  A template reading "{n} rows" prints "1 rows" the moment n is one, and n is one
  far more often than a template author expects: one exception, one unresolved
  column, one excluded unit, one peer.
- **THE CONSTRUCTION, and it is mandatory for every generated sentence:** carry the
  singular and plural forms of the noun with the count and select on the value, so
  "1 row" and "2 rows" are both correct. Where a sentence would otherwise need a
  verb to agree as well, choose a phrasing whose verb does not change: "rows
  excluded: 1" agrees at every value, and so does "excluded 1 row" against
  "excluded 2 rows" when the noun is selected.
- Rule: ZERO gets its own reading, and it is usually a different SENTENCE rather
  than the plural form with a nought in it. "0 rows were excluded" is correct and
  reads as a machine; "nothing was excluded" is the same fact in the reader's
  language. Where a zero case is meaningful, and in this bundle it usually is
  because a zero is the evidence a check ran, write the zero sentence explicitly.
- Rule: this reaches every place a number meets a noun: front panel lines, empty
  section messages, degradation notices, audit lines, showing notes and any
  degradation text carrying a count of what was affected.
- **Rule: TEST EVERY TEMPLATE AT THREE VALUES, zero, one and many, before it
  ships.** That is the whole check and it takes seconds. A template only ever
  exercised at many will read as broken on the first quiet run, which is exactly
  the run where a reader is most inclined to doubt the tool.
- Prevents: a document that reads as machine output at precisely the moment its
  numbers are small enough for a person to check by hand.
- Source: release sweep, N4
- Applies: PLANNING, REVIEW, SCORECARD

### SD-LNG-12 At the ends of a scale, say the plain thing rather than the arithmetic thing
- Rule: where a computed figure lands at the exact top or bottom of its scale, the
  reader-facing sentence says WHAT THAT MEANS in ordinary words, and the figure
  itself is printed unchanged beside it. Do not round it, do not cap it, and do not
  suppress it.
- The named case: the percentile is average rank over N, so the largest unit in a
  list sits at exactly 1.0 and the narrative read that the measure "sits at the
  100th percentile". That is arithmetically correct and fully traceable, and to a
  person holding the list it reads as a mistake, because in ordinary use a
  percentile is a position among others and being at the hundredth of them is not a
  position anybody recognizes. Rounding it down would be a lie and capping it would
  break the reconciliation, so neither is available. The wording is what changes.
- Mechanism: at the TOP of a ranked population say it is the LARGEST IN THIS LIST,
  naming the list. At the BOTTOM say it is the SMALLEST IN THIS LIST. In both cases
  print the figure itself in the same sentence or the adjacent cell, so nothing is
  hidden and the audit still reconciles against the number rather than the phrase.
- Rule: the substitution fires ONLY at the exact endpoints of the scale, and only
  in reader-facing narrative. The column, the audit and every gate keep the raw
  figure. A value one place inside the endpoint is described normally, because
  "the 99th percentile" is a sentence people understand.
- Rule: where the endpoint is SHARED by tied units, say so: the largest in this
  list, tied with a stated number of others. A superlative asserted over a tie is
  the one way this rewrite could introduce a falsehood, and naming the tie is what
  stops it.
- Rule: this is a general rule about ends of scales, not a special case for one
  figure. A share that lands at exactly 100 percent of a population, a rank of 1 of
  1, and a band at the top of its ladder all take the same treatment: state the
  plain fact, print the number beside it.
- Prevents: a correct number that reads as a broken one, which costs the artifact
  the reader's confidence in every other number on the page.
- Source: ship-or-no-ship run, LOW 3
- Applies: PLANNING, REVIEW, SCORECARD

### SD-LNG-09 The system truncates silently, so every emitted field is counted and must fit
- Rule: "It does not warn, it does not wrap, and it does not tell the user what
  was lost. A field written past the limit arrives in the permanent record cut off
  mid-sentence."
- Mechanism: emit the exact character count beside every field, and gate on it.
- Note: the limits are DEFAULTS, NOT FACTS. They differ by field, by form version
  and by tenant, and are confirmed per run by the person who has the form open.
- Source: R-D15
- Applies: REVIEW

### SD-LNG-10 The compression order is fixed, and there is a never-cut list
- Rule: cut in order and stop as soon as it fits. Filler and hedging; then
  restatement; then lineage and rationale; then scope qualifiers that repeat
  across every measure. NEVER cut a number, a population, a deadline, or the name
  of an entity being claimed. If it still does not fit, the objective is doing too
  much: split it. "Never drop a deadline to save characters, and never let a
  truncation reach the system."
- Source: R-D15
- Applies: REVIEW

### SD-LNG-11 What compression removes from the field is still reported to the person
- Rule: the lineage line is the first thing to go from a pasted field and is
  emitted as commentary instead, "because it is what they say out loud in the
  review conversation."
- Source: R-D15
- Applies: REVIEW

---
