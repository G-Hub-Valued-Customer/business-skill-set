# GROUP SPN: SPAN OF CONTROL

### SD-SPN-01 Show the levels BELOW the requester, never their own
- Rule: "A reader already knows their own level; what they need is the level
  beneath it, so they know whose work each unit is." Omit the requester's own
  level and everything coarser as redundant.
- Mechanism: a per-level table derived from SCOPE_LEVELS.
- Prevents: a column repeating one value on every row, and a manager unable to
  tell whose units they are looking at.
- General form: unchanged. Literal example: a market-level requester gets the
  territory column; a territory-level requester gets none.
- Source: P-D14
- Applies: PLANNING, SCORECARD

### SD-SPN-02 The inclusion test is mechanical: two conditions, both must hold
- Rule: include a scope column when it is strictly finer than the requester's own
  resolved level AND it carries more than one distinct value in the report
  population AND it is not the unit level itself.
- Mechanism: condition two "is the empirical backstop and it settles every
  awkward case without a special rule."
- **CONDITION THREE, AND IT IS NOT OPTIONAL: THE UNIT LEVEL IS NEVER AN
  ATTRIBUTION COLUMN.** A span block exists to say WHICH FINER THINGS INSIDE this
  row the reader owns. The unit itself is the row, and its identifier is already
  in the identity block by SD-CTR-08. Where the only level strictly finer than the
  requester's own is the unit level, conditions one and two both pass and the
  block would restate the identifier under a second header, which reads as a
  second, disagreeing identity column.
- Rule: where condition three strikes the only surviving candidate, the span block
  is EMPTY, and an empty span block is a finished span block. It is not a failure,
  it is not a degradation, and it carries no notice beyond one line in the Method
  section naming the level that was struck and why. This is the normal case for
  the most junior role in any ladder whose finest scope level IS the unit, which
  is the common shape, not an exotic one.
- Prevents: special-case rules for a coarse unit that happens to hold only one
  finer unit.
- Source: P-D15
- Applies: PLANNING, SCORECARD

### SD-SPN-03 Compute the column set ONCE, over the full ranked population
- Rule: compute condition two over the same population N that supplies the
  percentile, once, and apply the resulting column set identically to every item
  section. "One computation, one column set, matching sections."
- Prevents: a level carrying several values on one section and one on another,
  giving the two sections different column counts and breaking the guarantee that
  the identity block is structurally identical everywhere.
- Source: P-D16
- Applies: PLANNING, SCORECARD

### SD-SPN-04 Compute the distinct-value count from the FILTERED population
- Rule: use the filtered population, not the whole file, because a qualifier or a
  restriction can collapse a level to one value.
- Source: P-D17
- Applies: PLANNING, SCORECARD

### SD-SPN-05 When the requester's own level cannot be resolved, include every scope column with more than one value
- Rule: err toward more columns, never toward omitting the block. "An extra
  column costs a little width, while a missing one costs a manager the ability to
  tell whose units they are looking at. Never resolve the ambiguity by omitting
  the block."
- Source: P-D18
- Applies: PLANNING, SCORECARD

### SD-SPN-06 Scope codes are formatted as text
- Rule: format every scope column as text. Codes carry leading zeros in some
  units and a spreadsheet strips them silently.
- Source: P-D19
- Applies: PLANNING, SCORECARD

### SD-SPN-07 Filtering a manager's section to one sub-unit does NOT produce that sub-unit's report
- Rule: absolute. No part of any skill may imply that it does. Two independent
  reasons: the sections hold only the rows that were published, and rank is
  relative to the population it was computed over, and filtering does not
  recompute it. The remedy is to run the skill at that subordinate's scope.
- Mechanism: "It answers which of MY units are in that sub-unit, never what are
  that sub-unit's top units." The caps make it structural, and widening scope
  makes it sharper: on a very large file the published rows are well under one
  percent of the eligible set.
- Prevents: "A manager who believes a filter equals a subordinate's report will
  under-serve every unit that happens not to appear in their published rows."
- Source: P-D20
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SPN-08 The block is for attribution, not delegation
- Rule: it tells a manager whose units are on their list so they can route a
  conversation, brief by name, and see distribution across the units beneath them.
- Source: P-D21
- Applies: PLANNING, SCORECARD

### SD-SPN-09 Two claim tiers, and claiming at the wrong grain is fatal in both directions
- Rule: a DIRECT tier person personally changed the unit and claims unit-level
  results by name. An AGGREGATE tier person did not; someone on their team did,
  and they claim aggregates, team outcomes and systems. "Getting it wrong in
  either direction is fatal: a front-line person who hides behind aggregates
  looks passive, and a leader who claims a single unit looks like they do not
  understand their own job."
- Mechanism: ROLE_LADDER.claim_tier. Enforced by a gate that tests every claim
  against the tier.
- General form: bind the ATOM, the smallest unit a person can personally change,
  and the AGGREGATE, the population a leader is accountable for the shape of.
  The atom is a store here and is a ticket, an account, a case, a shift, a
  machine, a line item, a patient or a code change elsewhere.
- Source: R-D6
- Applies: REVIEW, PLANNING, SCORECARD

### SD-SPN-10 A named unit may appear only as an illustration inside an aggregate claim
- Rule: at the aggregate tier a named unit appears only as an illustration, and
  the credit stays with the team. Never emit an individual-unit claim at that
  tier.
- Source: R-D6
- Applies: REVIEW

### SD-SPN-11 Mixed scope claims at two grains and never blends them in one sentence
- Rule: a person holding both a direct book and aggregate responsibilities claims
  unit-level wins in the book and aggregate wins in the rest. Never blend the two
  in one sentence.
- Mechanism: PERSON_SECONDARY_SCOPES.
- Source: R-D6
- Applies: REVIEW

### SD-SPN-12 The self-determined subset is the highest-evidence cut
- Rule: the subset of the population whose outcome was determined locally rather
  than by a decision taken above the writer is the strongest available evidence
  of individual skill, because it isolates skill from inherited advantage.
  Surface it first and say so explicitly.
- Mechanism: resolved as the complement of a populated grouping field, never by
  searching for a word. Compare it three ways: against the same person's managed
  units, against the same subset elsewhere at the peer level, and against the
  scope total. Beating any of the three is a top-tier win.
- General form: any business that can distinguish self-determined outcomes from
  centrally determined ones can compute this cut. An inbound lead against a
  self-sourced one; an unmandated renewal against a corporate contract; a
  discretionary purchase against a required one.
- Source: R-D6; R-D9
- Applies: REVIEW, PLANNING

### SD-SPN-13 Influence inside a managed group is still a legitimate claim
- Rule: a direct-tier person influences a centrally managed group inside their own
  scope through the local decision maker even where terms are set above them.
  A claim about that group inside their scope is legitimate and strong.
- Source: R-D6
- Applies: REVIEW

### SD-SPN-14 A peer set is drawn from siblings, never from subordinates
- Rule: the resolved peer level must be strictly COARSER than the requester's own
  resolved level, and the peer set is the sibling units at the requester's own
  altitude inside that coarser level. Walking outward is the only permitted
  direction. Walking downward into the requester's own span is forbidden.
- Mechanism: resolve the peer level, then test it. If the resolved level is at or
  finer than the requester's own level, the resolution is wrong and is discarded,
  never used. Test the resolved peer set for a second property: no member of the
  peer set may sit inside the requester's own scope. A peer set that intersects
  the requester's own span is not a peer set.
- Prevents: ranking a leader against the units they manage, which is internally
  consistent, meaningless, and reads to the leader as an accusation. This is the
  exact failure named in the argument for binding the scope hierarchy at ignition,
  and until now the argument existed without the rule.
- Worked case, neutral: a system-level executive owns nine facilities. Her peer
  level resolves to the facility, because that is the only level the default
  names, and the run ranks her among her own nine facilities.
- Source: report 1 D6
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SPN-15 A role at the top of the chain has no internal peer set, and that is a stated result
- Rule: where the requester's own level is the coarsest in the chain, there is no
  coarser level, therefore no sibling set, therefore NO INTERNAL PEER SET. Say so
  plainly. Do not manufacture one.
- Mechanism, in order:
  1. If an EXTERNAL peer set is bound, a published comparison group maintained
     outside this organization, use it, name the publication and its refresh
     cadence, and state how stale the release is relative to the run.
  2. Otherwise drop the peer rung for that run, fall to the highest remaining
     bound rung, and name the drop beside every affected figure, per SD-CTR-24.
  3. Where no rung remains but the floor, the figures ship with a denominator
     population and no achievement wording.
- Rule: an external peer set is a legitimate answer to "the spread across peers
  doing the same job" and is the most likely real answer at any regulated or
  benchmarked business. It is bound as a publication and a cadence, never forced
  into the organization's own containment chain, because the chain holds only
  units the organization owns.
- Rule: this rule answers a peer set of ZERO. A peer set that EXISTS but is too
  small to compare anonymously is a different state with a different answer, and
  SD-SPN-16 holds it. Neither state is read as the other.
- Prevents: a top-of-house role being silently ranked against its own
  subordinates, and a published external comparison group being quietly recorded
  as an internal level it is not.
- Source: report 1 D6 and D7
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SPN-16 A peer set that is non-empty and below the anonymity floor is a THIRD state, and it has its own rung
- **Rule: TWO FLOORS GOVERN A PEER SET, THEY ANSWER DIFFERENT QUESTIONS, AND A SET CAN
  MEET EITHER WITHOUT THE OTHER.** `ANONYMITY_FLOOR` asks whether an INDIVIDUAL can be
  identified from the aggregate: it is a disclosure limit, and below it nothing about
  the set may be published at all. `MIN_POPULATION_FOR_NORM` asks whether the
  DISTRIBUTION is large enough to derive a band or a norm from: it is a statistical
  limit, and below it the set may be named and counted but no comparison may be drawn
  from it, per SD-POP-19. **Neither implies the other, and this rule NAMES THE TWO
  CONDITIONS rather than a number**, so it stays correct whichever way a binding owner
  moves either default and however far apart they sit.
- Rule: where the resolved peer level yields a sibling set that is NON-EMPTY and below
  EITHER floor, the run WALKS OUTWARD one level at a time until the set meets BOTH
  floors or the chain is exhausted. **The peer rung is available only at a level whose
  set MEETS BOTH.** A set below ANONYMITY_FLOOR is never published: not as a rank, not
  as a position, not as a median, not as a spread, not as "one of two", and not in
  generalized wording that a reader can invert. A set that meets ANONYMITY_FLOOR and
  not MIN_POPULATION_FOR_NORM may be named and counted, and no comparison is drawn
  from it.
- **THE FAILURE THIS RULE ANSWERS.** The rules covered a peer set of zero and they
  covered a scope too small to rank. Nothing covered a peer set of ONE, which the
  documented fallback produces routinely: one level coarser than a reader's own level
  is a small container, and a container holding two of them yields a peer set of one
  against any floor either variable can carry. A literal run then gives that reader no peer comparison
  EVER, while the same file holds several directly comparable siblings one level
  further out.
- Mechanism, in order, and every step is recorded:
  1. Resolve the peer level as bound or derived. Count the sibling set.
     **THE SIBLING SET EXCLUDES THE REQUESTER'S OWN UNIT. A container holding N units
     at the requester's altitude yields a peer set of N MINUS 1, and BOTH FLOORS ARE
     TESTED AGAINST THAT NUMBER.** A set containing the person being compared is not a
     peer set: the reader would be ranked against themselves, they would move their own
     median, and the anonymity floor would be counting one member who is not anonymous
     to the reader at all. This was stated only inside a worked example, and the two
     readings produce two different permanent records off one file: an organization with
     exactly five units at the reader's altitude yields four excluding the reader, below
     both floors at their documented defaults, so the chain is walked and nothing about
     peers is published; and five including the reader, meeting both exactly, so a
     median, a position and a labelled delta ship. The exclusion is applied at every
     step of the walk below, not only at the first.
  2. Where the count is at or above BOTH ANONYMITY_FLOOR and MIN_POPULATION_FOR_NORM,
     use it. Nothing further applies.
  3. Where the count is zero, this is SD-SPN-15, not this rule.
  4. Where the count is one or more and below EITHER floor, step to the NEXT COARSER
     level and count again. Every step is still subject to SD-SPN-14: the level stays
     strictly coarser than the reader's own, and no member of the set may sit inside
     the reader's own scope.
  5. **STOP AT THE FIRST LEVEL WHOSE COUNT MEETS BOTH FLOORS.** The walk is not
     permitted to continue past that level, because a walk that keeps going is a search
     for a flattering comparison rather than a search for a lawful one. **It is equally
     not permitted to stop SHORT of it on the strength of one floor alone.** A stop
     condition naming only the anonymity floor lands the walk on the smallest set that
     floor admits, which is below the norm floor whenever the norm floor is the larger
     of the two, and the run then holds a peer set it may name and may draw nothing
     from: the band it just computed can never fire, on any data, at either default.
     That is arithmetic on the two values and not a property of one file's population.
  6. Where the chain is exhausted and no level meets both floors, there is no usable
     internal peer set for this run. Take SD-SPN-15's mechanism from its step 1: an
     external peer set if one is bound, otherwise DROP the peer rung, fall to the
     highest remaining bound rung, and name the drop beside every affected figure.
- **Rule: FALLING OFF THE PEER RUNG MEANS DROPPING TO A WEAKER RUNG, NEVER BUILDING A
  STRONGER ONE.** A comparison drawn at a superseded level is a comparison against a
  DIFFERENT peer group, and it is published as such: the level actually used and the
  count it yielded are printed beside every figure that reads it, and the derived
  level is named as superseded. It is never presented as though the reader's own
  derived level had produced it, and a figure drawn at a coarser level never inherits
  the claim strength a same-level comparison would have carried.
- **Rule: NEITHER FLOOR IS EVER LOWERED TO FIT THE SET, and neither is substituted for
  the other.** Not for a single figure, not because the walk failed, not because the
  omission is awkward to explain. ANONYMITY_FLOOR exists so that an individual cannot
  be identified from an aggregate, and a set published because it was inconvenient not
  to publish it is the exact harm. MIN_POPULATION_FOR_NORM exists so that a band is
  derived from a distribution rather than from three numbers, and a comparison drawn
  below it is a fragile figure wearing a label. Where a binding sets either value, that
  value governs; where nothing is bound, the documented default governs; a run never
  chooses either, and a run never reads one where the other is meant.
- **Rule: THE ARTIFACT DISTINGUISHES FOUR STATES IN FOUR DIFFERENT SENTENCES, and
  never prints one of them for another. Each names WHICH floor it is about, because two
  of them are silences for two different reasons:**

| State | What the reader is told |
|---|---|
| NO PEER SET | There is no sibling set at all, because the reader is at the coarsest level of the chain. Per SD-SPN-15. |
| TOO FEW PEERS TO NAME SAFELY | Peers EXIST and nothing about them was published: name the level, the count it yielded, ANONYMITY_FLOOR by name, and that the reason is anonymity rather than absence. Where the walk succeeded, name the level used instead; where it failed, say the chain was exhausted. |
| ENOUGH PEERS TO NAME, TOO FEW TO DERIVE A BAND FROM | The set was named and counted and NO comparison was drawn from it: give the level, the count, the reader's own figure, and MIN_POPULATION_FOR_NORM by name, and say that the withheld thing is the comparison and not the peer group. This is a real state, it is neither of the two either side of it, and printing one of those for it tells the reader either that their peers do not exist or that they were compared. |
| COMPARED, AND THE RESULT IS FLAT | The comparison RAN, at a named level over a named count meeting both floors, and the reader sits where the figure says. FLAT is a result, not a silence. |

- Rule: the suppressed comparison is named rather than omitted, per SD-POP-25's
  discipline: a reader who is told nothing assumes the comparison was attempted and
  came back unremarkable, which is the one reading that is false in all four states.
- Prevents: a reader in a small container receiving no peer comparison for the life
  of the deployment while comparable siblings sit one level away, unlooked at; the
  opposite failure, a three-person distribution published as a peer distribution, from
  which any reader can name the other two; and a walk that halts in the gap between the
  two floors, which produces a peer set that satisfies the disclosure limit, fails the
  statistical one, and makes every band computed on it unfirable on any data.
- Source: the demonstration run, review D3; extended by the demonstration run, review N2
- Applies: PLANNING, REVIEW, SCORECARD

---
