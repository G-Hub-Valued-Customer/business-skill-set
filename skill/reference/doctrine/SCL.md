# GROUP SCL: SCALE

### SD-SCL-01 Nothing about the method changes at scale; only the mechanics of reading and writing do
- Rule: tiers by record count, with the method, the sections, the formatting
  elements, the caps and every gate identical in all of them.
- Source: P-D310
- Applies: PLANNING, SCORECARD

### SD-SCL-02 The output is bounded by the caps, not by the input
- Rule: the largest possible artifact is roughly the same in every tier, so the
  build phase is a fixed amount of writing at any scale. "This is exactly why the
  caps exist and why they are never raised to cover more of a big file."
- Source: P-D311
- Applies: PLANNING, SCORECARD

### SD-SCL-03 Sampling and estimating are prohibited at every scale
- Rule: never sample rows, estimate a threshold, extrapolate a percentile from
  part of the file, lower a cap, drop a section, or shorten a list. "A percentile
  taken over a sample is a different number wearing the same name."
- Source: P-D312
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SCL-04 "In-scope population" means AFTER scope, after every qualifier and after any restriction
- Rule: the distribution is built over that set, not over the raw file. "A large
  qualified run and a small one must both compute the percentile over the same
  conceptual population."
- Source: P-D314
- Applies: PLANNING, SCORECARD

### SD-SCL-05 Checkpoint MORE often as the tier rises, not less
- Rule: write a stage checkpoint after every PARTITION_SIZE records read and after
  every scoring block, carrying the distribution "so a resumed run never rebuilds
  it and never risks rebuilding it differently."
- Source: P-D315
- Applies: PLANNING, SCORECARD

---

# COUNTS AND INDEX

| Group | Meaning | Rules |
|---|---|---|
| CTR | The output contract and its shape | 30 |
| SPN | Span of control | 16 |
| FMT | Formatting as a correctness property | 29 |
| RNK | Rank continuity, caps and cuts | 11 |
| EFF | Effort, stopping and failing closed | 38 |
| RUN | Run architecture and verification design | 15 |
| IDN | Identity, role and scope | 25 |
| QUA | Qualifiers and population selection | 14 |
| PRI | Priorities and direction | 33 |
| SRC | Acquiring sources | 21 |
| PRS | Parsing and resolution | 48 |
| POP | Population exclusions and the pipeline order | 30 |
| WGT | The weighting hierarchy | 20 |
| DUP | The de-duplication of effort | 7 |
| MND | The mandatory set | 4 |
| SCO | Scoring | 17 |
| STR | The steer | 12 |
| CMP | Comparing two periods | 9 |
| EXC | The exception list | 32 |
| BRD | Breadth and derived analysis | 7 |
| CLM | Claims, credit and the counterfactual denominator | 34 |
| CNF | Confidence, inference and fabrication | 10 |
| LNG | Language, tone and the reader | 13 |
| SCL | Scale | 5 |

**THE TOTAL IS NOT STATED, HERE OR ANYWHERE.** It is the sum of the column above,
it changes every time a rule is added, and a total row is exactly the kind of
restated figure this file has watched go stale. A reader who needs it adds the
column up in one pass, against the definitions themselves.

## Rules carried from the source inventories

**THIS SECTION STATES NO TOTALS, AND THAT IS DELIBERATE.** A caption here once
carried a rule count that the table above it had long since overtaken, which is
the seventh instance of the same failure in this bundle: a number restated outside
the one table that derives it. The count of rules lives in the group table above
and nowhere else, including here, including in a caption.

What this section records is the INVARIANT, which does not go stale: every rule in
the planning doctrine inventory is carried, every entry in the review doctrine
inventory is carried, and nothing was dropped. That claim is checkable against the
inventories themselves; a number in a caption is checkable against nothing.

Every rule carries a Source line naming where it came from, and the three
populations are:

- Rules carrying a PLANNING source alone.
- Rules carrying a REVIEW source alone.
- Rules carrying BOTH, because the two skills arrived at the same rule
  independently. Independent arrival is the strongest evidence that a rule is
  doctrine rather than a local convention, so those entries name both sources
  rather than picking one.

**The sizes of those three are not stated here either.** They are derivable in one
pass over the Source lines, they change every time a rule is added, and a reader
who needs them should compute them rather than trust a figure last checked several
revisions ago. This is the same discipline the maintainer note in reference/schema/
applies to variable counts, applied here to rule counts, because this file drifted
in exactly the same way and for exactly the same reason.

Where a rule looked employer-specific but was an instance of a general rule, the
general rule is stated here and the specific case survives underneath it as a
worked example or as seed data the skill extends at runtime. The named cases:
the not-actionable exclusion (SD-POP-01), the different-operating-model class
(SD-POP-17), the coverage-duplication discount and the actor test (SD-DUP-01
through SD-DUP-07), the work-type ladder (SD-WGT-10 and SD-WGT-11), the frozen
classification fixture (SD-RUN-11), the breadth section (SD-BRD-01 through
SD-BRD-06), the exception flags (SD-EXC-01 through SD-EXC-31), the
self-determined subset (SD-SPN-12), the absence-resolution concepts
(SD-QUA-04), and the entire concept dictionary (SD-PRS-01 through SD-PRS-46,
with the seed contents in reference/field-resolution.md).

## What was deliberately NOT generalized away

The following stay in their original operative wording because the precision
lives in the phrasing, and a paraphrase loses the thing that makes them work:

- The never-interchange and unit-naming pair, SD-CLM-06.
- The low-confidence rule, SD-CNF-01.
- The silent-widening statement, SD-QUA-12.
- The no-gate-can-catch-this statement, SD-POP-05.
- The default-must-only-help statement, SD-WGT-02.
- The narrowest-test-first ordering, SD-PRI-08.
- The recoverable-error tie-break, SD-STR-10.
- The filter-is-not-a-subordinate's-report statement, SD-SPN-07.
- The cap-on-an-honest-axis statement, SD-RNK-07.
- The alert-versus-membership distinction, SD-EXC-03.
- The gap-the-person-cannot-close statement, SD-EXC-14.
- The ratio-cannot-see-a-zero-denominator statement, SD-EXC-15.

---

# CHANGE LOG: ACCEPTANCE TEST REMEDIATION

Two hostile acceptance tests were run across five invented companies at two
altitudes each. This section records what changed in this file and why, so the
change survives review.

## Rules added: 18

| ID | Answers | Why it was needed |
|---|---|---|
| SD-CTR-24 | Report 1 D4 | An unbound deferred value was overriding a bound ignition value and silently dropping every claim in a business to the floor rung. The precedence rule existed nowhere. |
| SD-SPN-14 | Report 1 D6 | The bundle named the failure of ranking a leader against their own subordinates, as the argument for binding the hierarchy at ignition, and then never wrote the rule that prevents it. |
| SD-SPN-15 | Report 1 D6 and D7 | A role at the top of the chain has no coarser level, so its peer set resolved downward. There was also no way to bind a published external comparison group, which is the most likely real answer at any regulated business. |
| SD-SRC-21 | Report 2 D8, report 1 D17 | Reading the published standard was declared a hard gate with no skip in one place, never a stop in another, and a degradable banner in a third. |
| SD-PRS-47 | Report 2 D9 | The seed dictionary shipped a stem collision between the not-actionable flag and the pipeline stage column, which is the failure no downstream gate can catch. |
| SD-POP-23 | Report 1 D2 and D19, report 2 D12 and D16 | Shape was a single organization-wide binding. Many businesses are genuinely both a roster and a pipeline, and forcing one answer was itself the error. |
| SD-POP-24 | Report 2 D16 | The two-test detection bound a pipeline to a roster of dated standing positions, because both tests passed and the conflict rule preferred flow. |
| SD-POP-25 | Report 1 D3, report 2 D4 | The bundle declared a one or two unit scope needed no special rule. It produced a nine-section artifact holding one row, one score and a percentile of one, with every gate passing. |
| SD-POP-26 | Report 1 D3, report 2 D4 | Nothing related the unit of business to the scope hierarchy, so an interview could accept two individually correct answers that were incompatible. |
| SD-POP-27 | Report 2 D5 | A uniform measure across a whole population makes the measure factor inert, and nothing said so in the output. |
| SD-CMP-08 | Report 2 D5 | A comparison request against a population with no prior period stopped and asked for a file that cannot exist. |
| SD-CLM-27 | Report 2 D5 | There was no cold-start rule anywhere in the bundle. |
| SD-CLM-28 | Report 2 D5 | Detection had to be automatic, because the user living inside a launch does not think of it as an edge case and the executive answers for the mature business. |
| SD-CLM-29 | Report 2 D5 and D1 | Rung availability was organization-wide with no way to scope it, which is the structural cause of the cold-start defect. |
| SD-CLM-30 | Report 2 D5 | The only existing guard fired on a column resolution failure. At a launch the denominator column resolves, populates, and is meaningless. |
| SD-CLM-31 | Report 2 D5 | A first-period figure could carry a WIN label against nothing. |
| SD-CLM-32 | Report 2 D5 | The remedy had to preserve what is claimable during a launch, not only forbid. Absolute build, sequencing against plan and execution against a denominator population are all legitimate. |
| SD-CLM-33 | Report 1 D5 | The rung-by-rung arithmetic table lived in one skill, so two skills produced two different answers off the same configuration and the same data. Promoted here unaltered. |

## Rules amended: 1

| ID | Change | Why |
|---|---|---|
| SD-EXC-14 | Split into two tests, engagement and influence, with only the second suppressing scoring, plus the more-than-half disclosure. | Read as one test it moved most of a regulator-set requirement set to shown-never-scored, leaving a near-empty gap list that reads as "you are fine". The general form also now names the schema field correctly rather than a variable that does not exist. |

## What did NOT change, deliberately

- The five rules the file lists as not generalized away were all confirmed intact
  by both tests and none was touched.
- The floor rung was not weakened. Both reports identify it as what stops a
  marketless business being told it cannot make claims. The defect was always the
  ROUTING into the floor, never the floor.
- The one-input comparison stop survives for a warm population. It is a correct
  gate against a forgotten attachment and only a dead end for a cold one.

## Fourth pass, final regression

- **SD-POP-26 gains the tie-break and the second test, N10.** The detection was
  degenerate at a scope of exactly one record, where every level has one distinct
  value and therefore every level satisfies the test, while the only stated
  fallback covered the case where none matches. The two rows of the reporting
  table then gave opposite answers off the same data: the coarsest reading calls a
  correct configuration a binding error, the finest never surfaces a real one, and
  both artifacts pass every gate. The rule now takes the FINEST matching level,
  and reports a binding error only where the reader's own level is strictly finer
  than every level matching over a population of MORE THAN ONE record.
- **SD-QUA-04 already carried the proper-subset guard from the previous pass.** No
  change was needed here.

## Fifth pass, live end-to-end run against an undescribed file

- **SD-POP-24 is declared the ONLY shape detection procedure in the bundle, and
  its tie-break is scoped.** Three places gave two answers off one file, because
  the interview and a skill each stated a shorter test of their own and the
  tie-break was written as though it applied whenever the third test was
  unanswerable. It now applies ONLY where tests one and two did not discriminate,
  meaning both passed or both failed, AND test three could not be answered. Test
  one passing while test two fails is FIXED, decided, and the tie-break is not run.
  Recording a decided shape as tie-broken is now named as a defect in its own
  right, because it invites an owner to overturn a correct reading.
- **SD-CLM-28's history test is only evaluable where a prior-period column
  resolved.** Where no such column exists the share is UNDEFINED, not zero, the
  test is recorded NOT EVALUABLE, and it neither fires nor passes. Absence of a
  column is a fact about the export, not about the business. The rule also gains
  the CORROBORATION test: a single firing test that another EVALUABLE test flatly
  contradicts yields COLD-CONTESTED rather than COLD, the restrictive claim rules
  still apply, and rung re-evaluation does not strike a rung whose only ground is
  the contested test. The case that found this: no prior-period column at all,
  and an earliest entry date two decades before the window.
- **SD-SPN-02 gains condition three: the unit level is never an attribution
  column.** For the most junior role in a ladder whose finest scope level IS the
  unit, which is the common shape, conditions one and two both passed and the span
  block would have restated the identifier under a second header. An empty span
  block is now stated to be a finished span block, not a degradation.
- **SD-IDN-02 gains the self-reported path.** The two-part test governs what may
  be inferred from a directory that FAILED. Where no directory capability exists
  at all, the person is asked, a statement that they are the top of the house is
  recorded as such with the source named SELF-REPORTED, and recording the head of
  an organization as having an unresolved supervisor when they have just said they
  have none is named as the credibility cost it is.
- **SD-EXC-06 now has THREE states, never two: a count, a zero, and NOT
  EVALUATED.** A check whose column did not resolve prints the line with NOT
  EVALUATED, the reason and the column named. A zero there asserts that nothing is
  overdue when nothing was looked at.
- **SD-RNK-09 retitled and rewritten: shorter RELATIVE TO SPAN.** The absolute row
  counts may rise and in the standing sizes they do. The senior line's pair is the
  larger pair, and that is the original design, not a contradiction.
- **SD-SCO-07 now requires the close-weight ladder to be EXHAUSTIVE over the
  number line.** A closed set of weights is only closed if every derivable date
  falls in exactly one band, and the standing set left a gap between the next
  window and the far horizon.

## Sixth pass, confirmation run at three altitudes

## Rules added: 3

| ID | Answers | Why it was needed |
|---|---|---|
| SD-CTR-25 | Confirmation run 2, new defect 1 | The previous pass's authority fallback REPLACED the senior-role grant rather than adding to it, so naming a configuration owner strictly reduced who could answer a deferred question, and progressive binding became less likely to fire at organizations that had taken the interview seriously. The rule makes authority a union, forbids any authority default written as two branches on whether another variable is bound, and supplies the monotonicity test to run before any such default ships. |
| SD-CTR-26 | Confirmation run 2, blocker 3 | A co-operative director answered all seven ignition turns naturally and still failed ignition validation, because three sub-fields were never elicited and had no derivations. Every artifact was then stamped PROVISIONAL forever off a complete interview, and nothing told the interviewer. The rule makes the interview and the validation one contract, defines ANSWERED, DERIVED and DEFAULTED as three states that all satisfy validation, and requires every derived value to be read back before the interview closes. |
| SD-POP-28 | Confirmation run 2, blocker 2 | Resolving the not-actionable concept and binding its values are two bindings, and the default for the second was "exclude nothing". A prospect ranked at position one of a working plan, four non-active units sat in a senior reader's top twenty, every gate passed and it was disclosed three times. The rule states the asymmetry that decides the default, supplies the seed set, and carries the stage, majority and naming guards. |

## Rules amended: 1

| ID | Change | Why |
|---|---|---|
| SD-SCO-07 | Every close band is anchored on the window BEING PLANNED, never on the run date, and the anchor date is printed. | The near horizon had no named anchor. On one real file the two readings moved 8 percent of the population between the two lowest bands, which reorders the published list, so two competent readers produced two different lists off one file and one configuration. |

## Seventh pass, final acceptance run at three altitudes

## Rules added: 3

| ID | Answers | Why it was needed |
|---|---|---|
| SD-CTR-27 | Acceptance run 3, defect 3 | The positional scope derivation was anchored on the finest level, which is the unit itself, so every role came out one rung too narrow, the top level was left unowned, and a role that leads people who work units resolved as a role that works units, flipping a claim tier in the direction SD-SPN-09 calls fatal. The rule anchors both ends, and records the diagnosis: where a derivation that knows more produces a worse answer than the fallback that knows less, the extra knowledge is applied at the wrong end. |
| SD-CTR-28 | Acceptance run 3, defect 4 | The cost order for deferred questions was a static table, so a run spent its whole budget on a question whose default changed nothing observable while the question deciding whether eleven exiting units sat in a published plan was pushed out of budget. Cost is now computed on the run, in four classes, with membership changes jumping the queue and provably-inert questions not firing at all. |
| SD-EXC-32 | Acceptance run 3, defect 5 | Absolute band thresholds calibrated for a four-flag set became unreachable on a file where one flag evaluated, so the top band silently ceased to exist and the exception section shipped empty three times running. Bands are now shares of what actually evaluated, every flag carries an explicit weight, and an unevaluable flag is removed from the maximum rather than counted as zero. |

## Rules amended: 2

| ID | Change | Why |
|---|---|---|
| SD-EXC-05 | Still forbids a gate demanding two measures agree, and now REQUIRES the artifact to reconcile them where an alert is non-zero and its section is empty. | Permitting a disagreement is not the same as explaining it. An empty section beside an alert reporting thirteen stale units reads as a broken report, and a reader who concludes the report is broken is right to stop trusting the parts that are not. |
| SD-POP-28 | The seed set must cover the DECIDED EXIT NOT YET COMPLETE, and the comparison must be token-wise and bidirectional. | Terminal words plus whole-string prefix matching missed every compound status naming an exit already decided, which is the family that reads as active. The rule also now requires testing any addition against the active statuses of the same family, because the negation carries the meaning. |

## Eighth pass, release acceptance run

## Rules added: 2

| ID | Answers | Why it was needed |
|---|---|---|
| SD-POP-29 | Release acceptance run, N1 and N2 | A four-character token floor failed in both directions at once: too loose, so a live status matched a terminal seed entry and a workable unit would have been silently removed; and too tight, so the three-character negating token in every decided-exit phrase matched nothing and the headline exclusion did not fire. No value of the threshold works, which proves the threshold is the wrong instrument. Matching is now whole-token phrase matching with a single-token override and a printed refusal. The rule also carries the requirement that a notice naming example inputs must RUN them and print the results, because the rule it replaces asserted a verification it failed. |
| SD-BRD-07 | Release acceptance run, N10 | Ordering carried context columns by raw distinct count compared two kinds of usefulness that are not comparable, so a tenure year outranked a line of business. Columns are now sorted by KIND first, quantities then groupers then dates then labels, with the existing keys applied unchanged within each class. Order only; no membership test, cap or failsafe changes. |

## Rules amended: 1

| ID | Change | Why |
|---|---|---|
| SD-EXC-07 | A future-dated value is excluded from every DERIVED STATISTIC computed from its column, not only from the bands, and the excluded count is reported beside the statistic. Where more than half the populated values are impossible, the statistic is not published at all. | The arithmetic half was written and the statistics half was not. On one real file, including future-dated rows in a local median moved the median about fourteen days, the scaled threshold about twenty-seven, and the exception section between thirteen members and zero. Two implementers produced two different sections off one file and no gate could catch it, because both were internally consistent. |

## Ninth pass, ship-or-no-ship run

## Rules added: 1

| ID | Answers | Why it was needed |
|---|---|---|
| SD-LNG-12 | Ship-or-no-ship run, LOW 3 | The top row of a ranked list printed as the hundredth percentile, which is arithmetically exact, fully traceable, and reads to a person as a mistake. Rounding it down is a lie and capping it breaks the reconciliation, so the figure is unchanged and the SENTENCE changes: at the exact endpoints of any scale, say the plain thing, name any tie, and print the number beside it. Stated generally, so a share at exactly 100 percent and a rank of 1 of 1 take the same treatment. |

## Rules amended: 1

| ID | Change | Why |
|---|---|---|
| SD-POP-29 | Gains ONE LIST, ONE PLACE: a value set has exactly one home and every other mention points at it rather than restating any part of it, an EXAMPLE column included. | One variable carried a short list in a definition table and the full list in the defaults appendix, and five of thirty-four verified cases changed verdict depending on which a reader used. A partial restatement is a second default, and a reader who finds the short one never learns the long one exists. |

## Tenth pass, final ship run

## Rules added: 2

| ID | Answers | Why it was needed |
|---|---|---|
| SD-FMT-21 | Final ship run, MEDIUM 3 | The degenerate-constant test could delete a column three separate parts of the output contract declare mandatory, and on a run where no priority source resolved every cell of that column held the same string, so the test fired. An optimisation may never delete a guarantee. The rule also states the positive finding: a mandatory column carrying one repeated value is a fact about the data, reported in one line, and deleting the column hides it. It generalises to every removal rule, not only the constant test, so the next mandatory column cannot hit the same collision. |
| SD-SCO-17 | Final ship run, LOW 4 | A nominal thirty-day period anchored on the first of a calendar month left the thirty-first day outside the window named for that month, so a commitment on the last day of the month being planned was banded into the next window and weighted down. Every date in the artifact was individually correct, so no gate could see it. The period NAME is now the authority and selects the derivation, and the covering invariant is validated rather than disclosed. |

## Rules amended: 1

| ID | Change | Why |
|---|---|---|
| SD-FMT-05 | CLOSED now means no inference AT RUN TIME, and membership is decided by a rule that is total over the seven shape tokens, with the bound list validated as the materialised result of that rule. | Closed was being read as "assembled from memory", which left numeric columns ranged left beside numeric columns ranged right in one table. Closing a list without stating its membership rule is how a list goes stale; stating the rule without closing the list is how a run starts improvising. Both halves are now present. |

## Eleventh pass, review and scorecard acceptance runs

## Rules added: 4

| ID | Answers | Why it was needed |
|---|---|---|
| SD-CMP-09 | Review run, trap 2 | A prior-period file containing only the units that survived scores 100 percent overlap, zero churn out, and passes the join floor at its maximum, so the test that exists to decide whether two files describe the same population certifies the one input that is unusable. Retention from it is 100 percent by construction and same-unit growth is biased upward by exactly the units that left; the weakest performer came out joint best. The exit side is now tested separately, the two states a zero-exit file can be in are distinguished with named evidence, and what may be claimed from a survivor-only pair is capped rather than refused. It was caught in the run only because two sources happened to disagree on a count. |
| SD-CLM-34 | Review run, D4 and D5 | The noise band was one scalar across rungs whose deltas are in four different units, and plan attainment had no band at all, so the most senior reader, who has no peers, received a page of unlabelled numbers including their worst failure. The band is now per rung with its unit named, and rung 4 has a fixed band in percent of target that needs no peer spread. |
| SD-CTR-29 | Scorecard run, defect 1 | A closed reason vocabulary seeded codes for two rare states and none for the state that is the skill's entire subject, so ordinary data produced hundreds of unmapped cells. Coverage is now validated from the states to the set, a hole is distinguished from a deliberately empty additive filter list, and a member with no action states that explicitly. |
| SD-CTR-30 | Scorecard run, defect 2 | Two shared defaults carried one skill's content, so a literal implementer of another skill shipped the wrong document. A default read by more than one skill is now either neutral in wording or keyed by skill, and a default naming a thing whose noun differs by skill names the role instead. |

## Rules added in the release sweep: 1

| ID | Answers | Why it was needed |
|---|---|---|
| SD-LNG-13 | Release sweep, N4 | A generated sentence with a count in it prints "1 rows" the moment the count is one, and one is common: one exception, one unresolved column, one excluded unit. The rule requires the singular and plural forms to be carried with the count, gives zero its own sentence rather than a plural with a nought in it, and requires every template to be tested at zero, one and many before it ships. |

## Twelfth pass, confirmation runs on both remaining skills

## Rules added: 1

| ID | Answers | Why it was needed |
|---|---|---|
| SD-POP-30 | Review confirmation run, SHARED 1 | The not-workable exclusion is a forward-looking test and a retrospective is not forward looking. Applying the planning reading to a year-end review deletes from somebody's own review every unit they worked and then lost, silently, because the unit is simply not there to be missed. Under REVIEW the question becomes whether the unit was workable at ANY point in the period: unworkable throughout is excluded because it was never theirs, unworkable partway is included and marked with the portion of the period it was workable, and an unestablishable transition date is included, disclosed, and reported both ways where it moves a published figure. |

## Thirteenth pass, the universal output contract

## Rules added: 4

| ID | Answers | Why it was needed |
|---|---|---|
| SD-FMT-22 | Originals review, C4 and C6 | The formatting elements existed as prose and were therefore never enforced, so a scorecard shipped with no autofilter, no rank column, no reason column and no cap, and a planning workbook put a banner in row 1 and pushed its headers to row 4. The contract is now one file that skills cite by element number, every element carries a programmatic verification, the verification runs before publication, and a failure blocks it. The output medium is keyed per skill. |
| SD-FMT-23 | Originals review, the reported header failure | Three failures share one cause, a width or height chosen from something other than the thing displayed: a column sized from the data hides a header word behind the filter caret, a fixed or autofit row height clips wrapped content, and a header row sized to one line shows one line of a two-line header. Width is now a header floor plus a caret allowance that the data may raise and never lower, and both heights are computed from wrapped content. |
| SD-FMT-24 | Originals review, the rank and reason decision | Every entity sheet in every skill carries a rank column in first position and a reason-for-rank column saying why the unit sits there. A ranked list whose ordering cannot be explained row by row gets re-sorted by hand, and a census with no rank leaves a reader with data and no answer to what to do first. The reason column is not the narrative column and does not replace it. |
| SD-FMT-25 | Originals review, C5 | Ranks run unbroken across the merit tiers, the derived last merit rank is a derived rank recomputed on any resize and never carried as a literal, reading it as a row cap overruns the cap that every showing-note reconciliation checks against, and every capped sheet is capped independently because later sheets hold populations differing by an order of magnitude off one scope. |

## Sixteenth pass, the three end-to-end skill runs

## Rules added: 1

| ID | Answers | Why it was needed |
|---|---|---|
| SD-FMT-27 | Scorecard run, D5 and D15 | Two failures of the same shape. A string-searching verification whose record must name its search terms found its own record and failed itself, so recording the evidence blocked the gate and hiding it passed; the record is now a declared range excluded from string scans and from nothing else. And a classification palette reusing the two alert colours put an approaching deadline and an unassessable cell in the same colour on one grid, invisibly on the run that authored it, because the alert element scored not applicable there. A colour is a variable with one binding. |

## Rules amended: 9

| ID | Change | Why |
|---|---|---|
| SD-FMT-03 | Gains the single position of the reason-for-rank column, and a BOUND on the total built width of the frozen span with a stated truncation rule and a most-identifying-first ordering of the identity block. | The reason column had two positions across the bundle, and freezing at either of them on a 21-column sheet pinned 17 columns and all 659 character-widths of it, so scrolling right reached nothing. A freeze that costs the reader more than it saves is worse than no freeze, and no element could see that, because each column was individually correct. |
| SD-FMT-05 | Gains a third alignment class, CENTRE, admitted only on a status grid column whose vocabulary is closed, published and short, with the remedy for a status grid of sentences named. | A skill required its status cells centred and the alignment verification required them left, so the instruction could not be obeyed by a workbook that publishes. Centring is the readable choice for a block of short codes read as a pattern and the wrong choice for a cell holding a sentence, so the condition rather than the instruction is what had to be stated. |
| SD-FMT-07 | States where the explanatory row of an empty section sits, that it is not a unit row, and that a row count counts units. | A correct empty section wrote one explanatory row and a showing note of zero of zero, and the reconciliation failed on a workbook with nothing wrong with it. The likely repair, writing one of one, tells the reader a unit exists that does not. |
| SD-FMT-08 | The one-direction rule is restated as a DIRECTION: multiplying a width is still forbidden, dividing a character requirement to obtain the width that holds it is the one permitted inversion, and the line count is a wrap and never a division. | Banning every conversion at the width step produced the opposite failure to the one it fixed: the width and the usable-character count became two quantities wearing one number, and every header needed more lines than its budget on 14 of 29 columns of a workbook built exactly to the rule. Separately, a formula naming two wrapping algorithms in one sentence let two faithful implementations disagree about one workbook. |
| SD-FMT-23 | The header's requirement is defined as the narrowest line the header can live on inside its budget, floored at its longest single word, and converted to a width once. | "Wrap it to the budget and take the longest line" names no width to wrap at, so it can only be read as wrapping against the width it is about to produce. The circle was closed by asking the wrap for the width rather than assuming one. |
| SD-FMT-26 | The explanatory row of an empty section is excluded from the note band, and a statement required in two places is reconciled rather than merely repeated. | One rule put a section's content where the notes go; another had the same sentence required in two places by two rules with nothing reading either, so one workbook carried the same figure twice and a reader could not tell which was current. |
| SD-POP-19 | A delta against a withheld comparator is withheld too, labelled or not, and the withholding is stated beside the figure. | One section said the raw delta ships without its label and this rule said no comparison is drawn, so two artifacts came off one configuration and one data set. Stripping the label off a fragile comparison removes the wording and leaves the claim. |
| SD-SPN-16 | The outward peer walk stops at the first level meeting BOTH floors, the two floors are distinguished by what each is for, and the artifact gains a fourth state for a set large enough to name and too small to band. | The walk stopped at the first level meeting the anonymity floor, which is the smallest set that floor admits and is below the norm floor at the shipped defaults, so a level-delta band was computed and then withheld on every run, on any data. The rule now names the two conditions rather than a number, so it survives either default moving. |
| SD-CLM-34 | The level-delta band names both floors and says which one binds a band. | Naming only the anonymity floor is what let the walk deliver a set that could be named and could not be banded. |

## Eighteenth pass, the unreadable header reported from a delivered workbook

## Rules added: 1

| ID | Answers | Why it was needed |
|---|---|---|
| SD-FMT-29 | The readability report on three delivered workbooks | Formatting must be chosen to degrade safely, because the author verifies in the renderer that built the file and the reader opens another one. Every header cell of three workbooks was written with a `00` alpha byte, which the building engine reads as opaque and many other renderers read as fully transparent; the dark fill vanished and bold white header text landed on a white sheet. The run verified a readable artifact and delivered an unreadable one, and no check it ran could have noticed, because every check ran in the renderer that made the file. The rule makes a text-and-band pair assert three renderings rather than one, requires an explicit opaque alpha on every colour, and states the general form: where two layers can produce a property they must agree in direction, and where a property has two halves either half must be sufficient. |

## Rules amended: 4

| ID | Change | Why |
|---|---|---|
| SD-FMT-02 | Gains the scope rule: a check is scoped to the whole of the rule it enforces, and a check scoped more narrowly than its rule is worse than no check because it certifies the defect. | The full-gridline element requires a border on every populated cell of the sheet; its verification walked the table range. Three workbooks passed it while shipping a populated, merged, entirely unbordered note band beneath a fully bordered table. A defect nobody checked is unnoticed; a defect with a recorded pass beside it is believed. |
| SD-FMT-04 | Gains the requirement that the table style's own header band AGREE IN DIRECTION with the direct header band, and the general form is extended: a lower-precedence layer is not a guarantee and is not free either. | Outranking a style is not being alone on the sheet. The delivered style's own header band was a dark fill under white text, under a direct dark fill under white text, so belt and braces failed together and a renderer honouring either one produced the same unreadable header. |
| SD-FMT-07 | Gains the requirement that the explanatory row CARRY ITS SENTENCE and that the sentence begin in the table's SECOND column, and resolves the contradiction that made the placement a matter of judgment. | The section required the row to begin in the table's first column and, four paragraphs later, to carry no value in the first identity column, which is the same column. Both could not hold. Three empty sections resolved it by putting the sentence in the seventh column of a 23-column sheet, leaving bordered rows 117 and 180.75 points tall whose first six columns are empty at exactly the place a reader looks first. A missing row is visibly missing; a bordered, sized, empty-looking one reads as finished and explains nothing. |
| SD-FMT-12 | Names CONTRAST as part of the arithmetic, measured in the greyscale unit the palette separation rule already uses, with a higher floor for a line than for a letter. | The bundle had one arithmetic for separating two fills and none for separating text from the fill under it, so the second was left to the eye. A gridline at 90 points of separation from a white sheet is a legible letter and an invisible hairline, and it was reported as invisible. |

## Nineteenth pass, the reading report from the delivered workbooks

## Rules added: 1

| ID | Answers | Why it was needed |
|---|---|---|
| SD-FMT-30 | The delivered-workbook reading report, the title band and the word it cut | A word must never be broken by a cell line, and there are exactly two ways it happens. A band styled across a span rather than merged across it leaves its text overflowing into the next cell, whose own border is then drawn through the middle of a word; and a column narrower than the longest unbreakable token it displays forces the wrap to overflow a line. The rule places every over-wide string in a merged region spanning exactly what it needs, floors every column at its longest token, and reports rather than breaks a token past the column cap. Nothing in the bundle could see either case: the width rules governed a grid column and had no opinion about a band, the border rule required exactly the border that did the cutting, and a styled span and a merged span look identical until a border is drawn. |

## Rules amended: 2

| ID | Change | Why |
|---|---|---|
| SD-FMT-13 | The exemption for table column headers is WITHDRAWN. Every heading, every sheet name and every column header is Title Case, in one convention stated precisely enough that two implementations produce one string, and stated in exactly one place. The one exemption that stays is a string the ORGANIZATION BOUND, which ships in the case it was bound in; a documented default is not a bound string and is written in Title Case where it is documented. | The exemption rested on a claim that Title-Casing column headers makes a wide table harder to scan, and the author of the method has overruled it after reading the delivered workbooks: a tab and a column header are the two shortest labels in the artifact and the two most often compared side by side, and mixed casing across them is what a reader meets first. Writing the defaults in Title Case rather than re-casing them at run time also closes the old contradiction between the case rule and the rule that a documented default is never contradicted. |
| SD-FMT-29 | Gains the mechanism rule: where a property can be expressed two ways and only one is read by the renderers the artifact is actually opened in, the widely read one wins over the one that is most correct in the authoring tool, and the check reads the property back from where the READER meets it. A property found only in a container the reader's engine does not open is ABSENT. | The same shape as the alpha-byte failure, one layer out. The filter was required to be the table object's own and a sheet-level filter was forbidden, which is the more correct expression in the engine that built the files and is unread by much of what opens them. Every workbook shipped with no visible filter on any sheet, on the feature the element itself calls the most-used in a delivered workbook, and the verification certified them because it read the filter out of the table container instead of off the sheet. |
