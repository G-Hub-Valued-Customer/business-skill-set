# GROUP CNF: CONFIDENCE, INFERENCE AND FABRICATION

### SD-CNF-01 Every inference carries a confidence, and confidence decides whether you PROPOSE or ASK
- Rule: HIGH, evidence is unambiguous and points one way: propose it and ask for a
  light confirm. MEDIUM, evidence supports it but a competing reading exists:
  present both readings and ask which is right. LOW, evidence is thin, conflicting
  or absent: do NOT propose prose, ask an open question instead.
- Scope: inferred actions, synthesized learnings, reconstructed objectives, entity
  and benchmark pairings, anomaly explanations, and any claim about causation.
- Rule: "LOW CONFIDENCE NEVER BECOMES A SENTENCE. It becomes a question. An agent
  that writes a confident sentence from thin evidence produces exactly the
  plausible-sounding filler that makes a reviewer distrust the whole document."
- Calibration, all three from the same shape of evidence: one clear reading is
  HIGH; two live readings both supported is MEDIUM; nothing correlating above
  chance is LOW.
- Note: named as the most transferable rule in the corpus. It ports as written.
- Source: R-D8
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CNF-02 Ask plainly when unsure
- Rule: "Did you actually do this? is a better question than a confident wrong
  sentence. Users correct a draft far more readily than they catch a fabrication
  that reads well."
- Source: R-D8
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CNF-03 Confidence is recorded, not just used
- Rule: every candidate carries its confidence into the checkpoint and into the
  verification list, "so a MEDIUM inference that the user confirmed is
  distinguishable later from a HIGH one that never needed confirming."
- Source: R-D8
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CNF-04 The proposal state machine, and silence defaults to REMOVED
- Rule: three states. Inference sets everything to PROPOSED. Drafting accepts any
  of the three, because "confirmation is a postcondition of the confirmation
  stage, never a precondition of the drafting stage." The confirmation stage
  resolves every proposal to CONFIRMED or REMOVED, and "a proposal whose question
  was skipped or never fired is REMOVED, not carried forward." Re-assembly strips
  every REMOVED proposal, deleting the sentence or clause it produced. A removed
  action clause leaves the result standing on its own without an action half; it
  does not leave an unconfirmed action in the text.
- Rule: silence defaults to REMOVED, not to CONFIRMED. That asymmetry is the whole
  point.
- Rule: "Inference is the method's core value and its core risk: a first-person
  claim about what the person did, never confirmed by them, is the single worst
  thing this method can produce."
- Source: R-D30
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CNF-05 Correlation is weak evidence for causation; present diagnoses as candidates
- Rule: "Always present diagnoses as candidates, never as proven cause: here is
  what stands out, does this ring true?"
- Source: R-D27; R-D41 guardrail 7
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CNF-06 Never invent an action
- Rule: where no evidence correlates to an outcome, emit the result without an
  action clause and route it to an open question. Retry once with a widened set,
  then proceed without the clause. Never invent one.
- Source: R Stage 7
- Applies: REVIEW, PLANNING, SCORECARD

### SD-CNF-07 Never fabricate; missing data is reported as missing
- Rule: never invent a unit, a number, a date, a target, a learning, a rating or a
  quote. Quote priorities verbatim with sender and date. "Never emit a rank, score
  or benchmark you could not compute. Leave it blank with a stated reason. A
  visibly missing number is recoverable; a fabricated one is not." An unconfirmed
  inferred action is fabrication even when the underlying number is real.
- Source: P-D294; R-D41 guardrail 1
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CNF-08 Every number traces to a cell or a tool result
- Rule: everything else is a bracketed placeholder naming its source.
- Source: R gate G2
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CNF-09 Show the person the whole thing before it is final
- Rule: "Nobody should discover what their record says by reading it in the
  destination system. The preview is the last cheap moment to change anything."
  Flag inline every claim from a MEDIUM or LOW confidence inference, every
  superlative and its tie count, every reconstructed item and date, and every
  remaining placeholder.
- Companion: offer the out. "Anything here you would remove or soften? That
  question matters. People will not submit something that overstates them, and
  without an easy way to dial back they abandon the whole draft rather than edit
  it."
- Source: R-D38
- Applies: REVIEW, PLANNING, SCORECARD

### SD-CNF-10 A person's own claim that a resolved cell contradicts is UNRESOLVED, never unsourced and never deleted
- Rule: a figure, a name or an event stated in the person's OWN NOTE that a RESOLVED
  COLUMN CONTRADICTS is a THIRD state, and it is neither of the two the run already
  has. It is not UNSOURCED, because it traces to a cell; the cell says something
  else. It is not two of the METHOD'S OWN derivations disagreeing, which is
  SD-RUN-09 and which never reaches a person's statement against the data.
- Rule: **NEITHER SIDE WINS AUTOMATICALLY, AND THAT IS THE POINT OF THE RULE.** A
  person's note is often right and the extract stale, late, filtered to a different
  population, or keyed on a different unit. The data is often right and the note
  written from memory months after the fact. **A run that picks a winner has decided
  a question of fact it cannot see, and it decides it the same way every time**,
  which is worse than getting it wrong once, because the bias is invisible and
  repeated.
- Rule: **NOTHING CONTRADICTED TRAVELS INTO A PERMANENT RECORD UNRESOLVED.** The
  item is excluded from every claim, count, denominator and ranked figure in the
  part of the artifact that goes to the destination system, and the exclusion is
  LISTED with the reason rather than being silent.
- Rule: **AND IT IS NEVER DELETED.** Both readings are printed below the boundary:
  the person's statement in their own words, and what the resolved cell says with
  its column and its unit named, together with THE QUESTION THAT WOULD SETTLE
  WHICH IS RIGHT. On a run with no mail and no chat a person's note is the only
  evidence of what they did, and a seam that strips a contradicted claim out of it
  silently deletes their year, which SD-CTR-23 names as the most expensive kind of
  loss. A run never averages the two, never blends them into one sentence and never
  publishes the disputed value.
- Rule: **IT IS SURFACED TO THE PERSON, NOT RESOLVED BEHIND THEM.** It is one of the
  things the preview of SD-CNF-09 flags inline, in the person's own language, as a
  question rather than as a correction: this is what you wrote, this is what the
  file says, which is right.
- Rule: **THE ARTIFACT DISTINGUISHES "YOUR NOTE AND THE DATA DISAGREE" FROM "WE
  COULD NOT FIND THIS."** Two states, two labels, two remedies. A contradiction is
  settled by somebody saying which source is right; an absence is settled by finding
  a source. Collapsing them sends the person hunting for a file when what was needed
  was one sentence from them, and tells them to doubt their memory when what was
  needed was a better extract.
- Mechanism: the test runs per stated item and is mechanical. CONTRADICTED, where a
  column that RESOLVED holds, on the unit the statement names, a value the statement
  cannot be true of. UNSOURCED, where no resolved column addresses the statement at
  all, and the bracketed-placeholder rule of G2 and SD-CNF-08 governs there
  unchanged. UNVERIFIED, where a column that would address it did not resolve or is
  empty within scope, which is a third label again and is never reported as a
  contradiction. **Where the statement names a UNIT that does not exist in the
  source at all, that is a contradiction of the identity rather than of a measure**,
  and it takes this rule rather than the unsourced one, because the source was read
  and the unit was absent from it. Above UNRESOLVED_STOP_COUNT contradicted items,
  stop, exactly as SD-RUN-09 stops: many contradictions at once are evidence about
  the extract rather than about the person.
- Prevents: two opposite failures with one rule. Publishing the person's words as a
  claim the data refutes, which is fabrication under SD-CNF-07 the moment anybody
  checks it. And silently dropping the person's largest claim because a cell
  disagreed with it, which is the deletion SD-CTR-23 names and which the person
  discovers by reading their own record in the destination system, too late to say
  anything. Measured on one run: a note naming an account that exists nowhere in
  either book file, and a note describing as lost an account that is Active on the
  book with a loss ratio nowhere near the one stated. The run had no rule and
  improvised.
- Source: the demonstration run, review X3; nearest analogy SD-RUN-09, which does
  not reach it
- Applies: PLANNING, REVIEW, SCORECARD

---
