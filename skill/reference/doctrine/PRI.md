# GROUP PRI: PRIORITIES AND DIRECTION

### SD-PRI-01 All sources, every run, with the nearest one first
- Rule: read every bound priority source on every run. The user's own supervisor
  is looked at FIRST and outranks every other source. A central source is the
  cross-check and the fallback, never the starting point. The prior period is a
  separate evaluated source.
- Source: P-D96
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-02 Sweep everything by SENDER; never filter the sweep by keyword
- Rule: retrieve every message from every manager in the chain, from every folder
  including the deleted-items equivalent, over both bound windows, every run,
  with no keyword filter. Filter by sender only. Read the subjects yourself. A
  keyword search runs afterward only as a supplement, to catch other senders
  quoting a manager.
- Mechanism: the documented failure. A keyword search returned one message; a
  sender search on the same mailbox and window returned twenty-two, and "the
  keyword search missed roughly 95 percent of the supervisor's direction, and
  every missed message was more on point than the one it found."
- Quote: "RETRIEVE EVERY MESSAGE FROM EVERY MANAGER IN THE CHAIN, FROM EVERY
  FOLDER, EVERY RUN. NO KEYWORD FILTER. NO EXCEPTIONS."
- General form: "real managers do not write in planning vocabulary. A keyword
  list built from how a specification talks will never match how a manager talks."
- Source: P-D97
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-03 Classify by CONTENT, not by keyword and not by length; when in doubt, KEEP
- Rule: a message is direction when it does any one of a named set of things. It
  is discarded only when it does none of them and is purely conversational or
  administrative. Never discard on the subject line alone. Report the count swept,
  the count read as direction, and the count discarded with a one-word reason
  each.
- Prevents: "Reading one extra logistics message costs nothing; discarding a
  one-line list of twelve units that need attention costs the plan."
- Source: P-D98
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-04 Never conclude an absence from the wrong instrument
- Rule: "no supervisor communication" requires the SENDER search to have returned
  zero messages. If it returned messages and none read as direction, say that
  instead, naming the count retrieved and the window covered.
- Source: P-D99
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-05 Reading and acting are two separate decisions
- Rule: sweep everything; direct selectively. The longer window is always read
  into the inventory; its lists become directives only under the carry-forward
  rule.
- Source: P-D100
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-06 Walk the chain upward, and weight by distance
- Rule: resolve up to CHAIN_WALK_DEPTH levels or until the chain returns empty,
  search each level, and weight by CHAIN_DISTANCE_WEIGHTS. Where levels disagree,
  follow the immediate supervisor and name the disagreement, "because the nearer
  manager knows the units."
- Mechanism: "These weights are not decoration: they scale the source boost
  inside the scoring formula."
- Prevents: a distant directional statement outscoring a near, specific
  instruction.
- Source: P-D101
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-07 Record every level, including the ones that published nothing
- Rule: a level that published nothing is a normal result and is not a missing
  supervisor. Record "resolved, no communication found this period" against that
  person by name. "A reader must be able to see that the chain was walked, not
  assume it."
- Source: P-D102
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-08 Carry-forward is evaluated MANAGER BY MANAGER, and the narrower test runs first
- Rule: three ordered rules, stop at the first that fires. Rule 1: published this
  period AND signalled continuation, so the lookback runs and the recovered list
  is directed at full weight. Rule 2: published this period with no continuation
  signal, so nothing older carries forward. Rule 3: published nothing this
  period, so the prior period carries forward in full.
- Mechanism: "The continuation test is rule 1 and that ordering is load-bearing:
  a manager who published this period AND said the priorities continue satisfies
  the conditions of BOTH rules, so the narrower test must run first."
- Prevents: "Putting the plain current-direction test first would swallow every
  carry-forward case and the continuation rule would never fire at all." Rule 2
  prevents reaching past a current instruction to revive an older one.
- General form: order overlapping tests narrowest first.
- Source: P-D103
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-09 Name the rule an implementer will skip, and say so
- Rule: where one rule in a ladder is the one most likely to be dropped, say so
  explicitly in the text, with the evidence.
- Mechanism: the documented case: two independent runs split precisely on the
  middle rule and produced different top tens off identical data.
- General form: a documentation practice, not a computation.
- Source: P-D104
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-10 A mandatory item's weight never decays with the age of the instruction
- Rule: carry-forward is a yes-or-no admission test, not a discount. Once
  admitted, the items carry full weight. "Do not invent a partial weight for
  older direction; either the list is live or it is not."
- Source: P-D105
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-11 ANY list from anyone in the chain is a must-cover; no trigger phrase is required
- Rule: a manager who sends a list of units is telling the person to cover those
  units. That is the default reading and it needs no keyword to activate it. The
  only thing that releases an item is an explicit instruction not to cover it,
  from DIRECTIVE_RELEASE_PHRASES.
- Prevents: requiring vocabulary the sender never uses.
- Source: P-D106
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-12 Apply the ACTOR TEST before treating a list as a directive
- Rule: the test is WHO the message names as the actor, and it is the only test.
  A list naming another person or role as the one who will work the items is an
  ASSIGNMENT and routes to the de-duplication weight. Everything else is a
  directive, including a bare list with no framing at all.
- Mechanism: "Two independent runs against the same mailbox split on exactly this
  message, and the one that directed it inverted the weighting on those units by
  a factor of four."
- General form: fully universal, and belongs in any skill that reads instructions
  out of prose.
- Source: P-D107
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-13 When in doubt, treat it as directed
- Rule: "The cost of covering a unit the manager mentioned in passing is one
  visit; the cost of missing a unit they expected covered is the person's
  credibility with their boss."
- General form: an asymmetric-cost tie-break.
- Source: P-D108
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-14 Match a named item to a row by a stated ladder, and report what will not match
- Rule: identifier if present; then name plus locality; then name plus address;
  then name alone when unique in scope. Compare as normalized text. Any named
  item that cannot be matched is listed with a blank rank and a note, and the
  count is repeated in the opener. "A directive the user cannot see was received
  is worse than one that arrives with a gap in it."
- Source: P-D109
- Applies: PLANNING, SCORECARD

### SD-PRI-15 Never infer an item's identity from an aggregate
- Rule: a message reporting a count, a percentage or a summary figure without
  naming an item has not named one. Do not reverse-engineer which row it must
  have meant, however uniquely it appears to resolve. "Two runs against the same
  mailbox will infer two different units and both will look confident."
- Prevents: confident non-determinism.
- Source: P-D110
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-16 Unresolvable direction is surfaced and changes nothing about the ranking
- Rule: record it with a blank identifier and the quoted wording, report it in the
  opener, and leave the merit ranking untouched.
- Source: P-D111
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-17 A directive from a supervisor never skips the compliance gate
- Rule: automatic admission means an item does not need a published match. It
  does not mean it skips the compliance gate. "A supervisor cannot authorize what
  the local rules do not permit."
- Source: P-D201
- Applies: PLANNING, SCORECARD

### SD-PRI-18 Locally tagged work is the strongest signal in the file, and the test runs on UNPADDED digits
- Rule: extract any scope token from the work item name, normalize, and test
  whether the RAW digits are a left-anchored prefix of the user's own code. "Do
  NOT run the prefix test on the padded value." Padding is for comparing a tag
  against a scope COLUMN; the prefix test uses raw digits. "Different purposes,
  and swapping them breaks the rule silently."
- General form: applies wherever one normalization serves two purposes.
- Source: P-D199
- Applies: PLANNING, SCORECARD

### SD-PRI-19 A top-level user has no scope code, so nothing is local to them
- Rule: set the local boost to neutral throughout, admit items on the published
  and supervisor tests alone, and say so. "An empty code prefixes everything and
  would hand the boost plus automatic admission to every tagged item in the file."
- Source: P-D200
- Applies: PLANNING, SCORECARD

### SD-PRI-20 A DIRECT local tag overrides a work-type zero; a BROADER one does not
- Rule: a tag at the user's own finest LOCAL_OVERRIDE_DEPTH levels overrides the
  work-type weight. A tag at a coarser level gives the boost but not the
  override.
- Mechanism: "when your own boss loads a low-weight task against your own unit, it
  is a cannot-miss and it scores. When it arrives tagged to a whole coarse unit,
  it does not", because many peers load work at coarser levels, so a coarse tag
  "is closer to a central instruction than to a personal one."
- Source: P-D202
- Applies: PLANNING, SCORECARD

### SD-PRI-21 Foreign-unit tags are kept, scored and labelled, never silently dropped
- Rule: an item flagged on a record in scope is work on that record regardless of
  which unit authored it. It gets no local boost and no automatic admission, and
  scores only if it matches a stated priority on its own merits. Record the
  authoring tag and report the count.
- Source: P-D135; P-D203
- Applies: PLANNING, SCORECARD

### SD-PRI-22 A published external classification is EVIDENCE, not an override
- Rule: record an externally published type and use it to break a genuine tie, but
  follow the local ladder where they disagree, and note the disagreement.
- Mechanism: "a central source types an initiative once while the operating file
  may carry that initiative as two or three separate columns asking for different
  work. A single central type cannot be right for both."
- Source: P-D210
- Applies: PLANNING, SCORECARD

### SD-PRI-23 "Requires my action" is a PUBLISHED marker, not a reading of the sentence
- Rule: test for the published marker and nothing else. "Do not infer it from
  words like sell, execute or complete: the tag is a published originator marker,
  not a reading of the sentence." When no column carries the marker, no item
  takes the multiplier; record that rather than approximating it from verbs.
- Source: P-D219
- Applies: PLANNING, SCORECARD

### SD-PRI-24 A narrow instruction is a sharper priority than a blanket one
- Rule: apply NARROWNESS_MULTIPLIER when the item is flagged at less than
  NARROWNESS_THRESHOLD of the ranked in-scope population, using the same N that
  supplies the percentile denominator.
- Source: P-D220
- Applies: PLANNING, SCORECARD

### SD-PRI-25 Source boost is scaled by the naming level's distance, and the NEAREST namer wins
- Rule: SOURCE_BOOST_ONE when one source named it, SOURCE_BOOST_BOTH when two
  did, then scaled by the naming level's distance weight when a supervisor named
  it. A central naming is not distance-scaled because it is organization-wide by
  construction. Where several levels named the same item, use the nearest one's
  weight.
- Source: P-D218
- Applies: PLANNING, SCORECARD

### SD-PRI-26 Two distinctive tokens, or one SPECIFIC name; a family name never matches alone
- Rule: normalize, drop stopwords and short tokens, and require at least two
  shared distinctive tokens, or one shared token that is a specific initiative
  name. A family or category name is never a specific name and requires a second
  token.
- Mechanism: the documented harm. A single message about a family, read as a
  one-token match, "links that message to EVERY item in that family, so every one
  of them becomes supervisor-named AND centrally named and jumps from one source
  boost to both at once." One of three runs read the family token as a match and
  scored every top-ten unit measurably higher, which reordered the list. "A
  manager mentioning a family has named a family, not an initiative."
- Source: P-D229
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-27 A family-level mention still counts, just not as a match
- Rule: it enters the audit as a family-level priority, it steers the weighting,
  and it can admit an item when combined with a second token. What it does not do
  is manufacture a match against every item in that family. Record family-level
  and specific-level mentions separately with counts.
- Source: P-D230
- Applies: PLANNING, SCORECARD

### SD-PRI-28 Stem before comparing
- Rule: compare on a normalized stem of at least MIN_STEM_LENGTH characters, the
  same rule the column dictionary uses. "A match that depends on plural agreement
  is not a rule, it is a coin flip."
- Source: P-D231
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-29 Show the tokens, or you did not run the test
- Rule: record one line per matched item naming the priority it matched, the
  shared tokens, whether each is a family or a specific name, and the resulting
  boost. "An implementer who cannot show the tokens did not run the test."
- Source: P-D232
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-30 A run where nothing matched is a real result and must be visible
- Rule: report items examined, matched to each source, matched to both, and
  flagged but matching nothing. "Not a silent zero across the priority term."
- Source: P-D233
- Applies: PLANNING, SCORECARD

### SD-PRI-31 Priority ranking comes from the organization's published weights, not the writer's opinion
- Rule: where the organization publishes a weighted metric set, that ordering is
  the priority ranking for which win leads. Always name the weight alongside the
  claim.
- Source: R-D7; R-D5 rung L2
- Applies: REVIEW, PLANNING, SCORECARD

### SD-PRI-32 The source hierarchy is a map from QUESTION to artifact, not a ranking of documents
- Rule: each question has exactly one artifact that settles it: who defines the
  form; who defines the methodology; who defines the quality bar; who defines
  strategy; who defines priority ranking; who defines local targets; and what
  counts as evidence.
- Source: R-D7
- Applies: PLANNING, REVIEW, SCORECARD

### SD-PRI-33 User documents are read for EVIDENCE ONLY
- Rule: never for format, phrasing or structure. "Prior-period self-written
  documents are the input problem this method exists to fix. Never inherit their
  shape."
- Source: R-D7; R-D41 guardrail 4
- Applies: REVIEW, PLANNING, SCORECARD

---
