# GROUP POP: POPULATION EXCLUSIONS AND THE PIPELINE ORDER

### SD-POP-01 Exclude unreachable units before anything else, with no exception
- Rule: drop every unit flagged not actionable from every list including the
  mandatory section. Report the count so the omission is visible rather than
  silent. If the column is missing, say so; do not assume every unit is
  available.
- Mechanism: "A closed unit's measure is historical, so it reads as a strong
  performer and ranks high. Sending someone to a locked door on the strength of
  this report destroys its credibility on the spot."
- General form: EXCLUDE UNITS THAT CANNOT BE ACTED ON RIGHT NOW, BEFORE ANY OTHER
  STEP, AND REPORT THE COUNT. The universal core is that a lagging measure
  survives the thing it measures. An account in a contractual freeze still shows
  last quarter's revenue and would rank top of a renewal list. A discharged
  patient still carries the utilization history that would put them on an
  outreach list. A client on a legal hold is unreachable and reads as strong.
- Source: P-D158; P-F1
- Applies: PLANNING, SCORECARD

### SD-POP-02 THE PIPELINE ORDER, stated once and authoritative
- Rule: one ordering that satisfies every rule that claims to run first. No stage
  may be reordered.
  1. Scope and qualifiers.
  2. Not-actionable exclusion.
  3. Normalize the measure.
  4. Compute the class-escape median with the excluded class INCLUDED.
  5. Resolve the mandatory set.
  6. Apply the class exclusion and its escapes, producing the RANKED POPULATION.
  7. Compute percentiles, every other median and every peer norm over the ranked
     population, with mandatory units INCLUDED.
  8. Split the ranked population into the mandatory section and the merit tiers.
     This is a routing step and not a population change.
- Prevents: several rules each claiming primacy and an implementer resolving the
  conflict differently each time.
- General form: the technique of writing one authoritative ordering that
  satisfies every "first" claim is the transferable part.
- Source: P-D159
- Applies: PLANNING, SCORECARD

### SD-POP-03 The same phrase can mean two different medians, and the difference must be stated
- Rule: "scope median" means the step-7 median everywhere EXCEPT in the class
  escape, which uses the step-4 median.
- Mechanism: on one real scope the two differed by more than fifty percent, "so a
  run that uses the wrong one either admits units that should not be admitted or
  excludes ones that should."
- General form: an overloaded term silently changing a threshold is a defect
  class in its own right. Name both, once.
- Source: P-D160
- Applies: PLANNING, SCORECARD

### SD-POP-04 Resolve the mandatory set BEFORE the class exclusion; the ordering is mandatory
- Rule: resolve directed units from the priority sources first, then apply the
  class exclusion to everything that is not directed.
- Mechanism: "Reversing those two steps silently deletes a unit the user's own
  manager told them to cover, which is the most damaging failure this method can
  produce and it produces no error when it happens." State in the audit that the
  ordering held, and carry it as a regression invariant.
- Source: P-D161; P-F2 escape 1
- Applies: PLANNING, SCORECARD

### SD-POP-05 Resolve an exclusion flag by EXACT column name only
- Rule: the class flag resolves by exact name, then by named alternates, and
  nothing else. Never fall back to a neighbouring column in the same synonym
  group.
- Mechanism: matching the wrong one removed roughly three times the intended
  population in a real run. Critically: "A gate cannot catch this error: every
  unit of the intended class also carries the neighbouring flag, so removing on
  the neighbour removes all of them too and the invariant still passes. The only
  defence is resolving the right column in the first place."
- General form: the sharpest statement in the corpus of a failure no gate can
  catch. Any concept whose mis-resolution is invisible downstream is marked
  strict_exact_only with named forbidden neighbours.
- Source: P-D162
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-06 A missing exclusion flag means NO exclusion, stated plainly
- Rule: if no class column resolves, apply no exclusion, say so in the audit and
  the opener, and rank the whole population. Same when the column resolves but is
  empty for every row. "A missing flag is a reason to report, never a reason to
  guess."
- Source: P-D163
- Applies: PLANNING, SCORECARD

### SD-POP-07 Use the source's own flag rather than a maintained name list
- Rule: "Use the source's own flag rather than matching names, so the rule travels
  to any unit without a name list to maintain."
- Prevents: a hard-coded list that rots and does not port.
- Source: P-D164
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-08 Three escapes from an exclusion, and only three
- Rule: the unit was named by a supervisor; the unit reaches the upper half of
  its scope by the ranking measure computed with the class INCLUDED; or the
  request named the class by name. All are evaluated per run against live data.
- Mechanism: escape two computes the median before the exclusion over the full
  population, "so the test means half the units in this scope rather than half the
  excluded class, which would readmit roughly half of them and defeat the rule."
- Source: P-D165; P-F2
- Applies: PLANNING, SCORECARD

### SD-POP-09 Keep a rule that costs nothing when it does not fire
- Rule: escape two admitted nothing anywhere in the reference data and is kept
  anyway, because a denser population will fire it. The best candidate fell four
  percent short of the threshold.
- Prevents: over-fitting the method to one dataset.
- Quote: "A rule that costs nothing when it does not trigger and keeps the method
  portable is worth carrying."
- Source: P-D166
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-10 Report the exclusion every run: counts removed, counts readmitted per escape, and the threshold used
- Rule: "Someone who wonders where a third of their units went must find the
  answer in the artifact rather than assume the file is broken."
- Source: P-D167
- Applies: PLANNING, SCORECARD

### SD-POP-11 There is NO measure floor. Rank the whole population.
- Rule: no fraction cut, no median cut, no minimum to be ranked. The section sizes
  decide what appears, and a unit that does not appear ranked below the cut rather
  than being removed by a threshold.
- Mechanism: the documented harm. A two-thirds floor dropped several genuine
  mid-size units while the unit one place above the line survived on a trivial
  difference. "The floor had been calibrated when a third of the population was a
  low-value class dragging the distribution down. Remove them and the same rule
  starts amputating real business."
- Prevents: a threshold that was calibrated against a population that has since
  changed.
- Quote: "A floor answers the wrong question. The measure tells you what a unit is
  worth per visit; it does not tell you whether the unit needs one." And:
  "Capacity is already the constraint and it is the honest one."
- Source: P-D168
- Applies: PLANNING, SCORECARD

### SD-POP-12 A unit with no history is RANKED LAST, never dropped
- Rule: a newly created unit has no measure yet, so it should rank at the bottom
  and be visible there, not vanish until it accumulates history.
- Source: P-D169
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-13 USABLE MEASURE, redefined and exact
- Rule: a blank, null, non-numeric, zero or negative measure is INCLUDED in the
  population and treated as zero. It is counted in N, receives the lowest
  percentile, and ranks last in the zero bucket. Only the not-actionable gate and
  the class exclusion remove anything.
- Source: P-D170
- Applies: PLANNING, SCORECARD

### SD-POP-14 The percentile never reaches zero, which is why the ZERO BUCKET is mandatory
- Rule: with k units tied at the minimum, each receives (k + 1) divided by (2N),
  so no unit is annihilated to a hard zero score and ordering among the smallest
  is still decided by the other terms. The bucket is a sort key applied after
  scoring, and it is what makes "ranks last" true rather than approximate.
- Prevents: "Someone sent to a unit with no activity ahead of a unit with real
  activity would rightly stop trusting the list."
- General form: a multiplicative term with a positive floor does not enforce a
  last-place guarantee; a sort key does.
- Source: P-D171; P-D234
- Applies: PLANNING, SCORECARD

### SD-POP-15 The bucket is a sort key, never a score adjustment
- Rule: do not zero the score, do not add a penalty term, and publish the unit's
  real score.
- Source: P-D172
- Applies: PLANNING, SCORECARD

### SD-POP-16 The percentile definition is mandatory and exact
- Rule: rank the in-scope population ascending by the ranking measure, average the
  ranks of tied values, divide by N. Tied values receive an identical percentile,
  "which is what makes a rerun reproduce the same list." Never compute over a
  subset, never over a sample.
- Source: P-D216
- Applies: PLANNING, SCORECARD

### SD-POP-17 A class served under a different operating model is REMOVED, not down-weighted
- Rule: where a subset of the population is covered by a completely different
  operating model, it is removed from the population entirely rather than
  discounted, because it should not compete for the person's time at all.
- General form: the class named by OUT_OF_MODEL_CLASS_CONCEPT. Accounts on a self-serve or partner-led motion
  that a named seller neither owns nor should be measured against; patients
  attributed to another care team; clients on a managed-service retainer rather
  than a project engagement.
- Source: P-F2
- Applies: PLANNING, SCORECARD

### SD-POP-18 Guard every divisor before dividing
- Rule: a closed table of degenerate conditions and their behaviours: zero rows
  after filtering; a qualifier matching no rows; a qualifier resolving to no
  column; blank, zero or negative measures; phantom trailing rows; a one or two
  unit scope; an entirely uniform measure; fewer eligible units than the list
  size; and A TARGET OF ZERO, which is a divisor of zero arriving from the plan
  rather than from the population.
- Mechanism: N equal to one or two needs no special rule because the average-rank
  percentile is well defined there, and an entirely uniform measure gives every
  unit the same percentile with nothing dividing by zero. "Deliver every eligible
  unit and say so, and never pad the list."
- Mechanism, the zero target: a target of zero is a LEGITIMATE and common target,
  and it is the one divisor a population guard never sees because it is not drawn
  from the population at all. Attainment against it is UNDEFINED, no ratio is
  emitted and none is approximated, the classifier does not fire, and the measure
  ships with its count and its denominator population. Never substitute a small
  number for the zero, and never invert the measure to make it divide.
- Quote: "Never emit a number you could not compute."
- Source: P-D316
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-19 A median over fewer than the minimum population is not a norm
- Rule: below MIN_POPULATION_FOR_NORM, print the figure with the count beside it
  and skip the comparison rather than presenting a fragile number as a benchmark.
- **Rule: A DELTA AGAINST A WITHHELD COMPARATOR IS A COMPARISON, AND IT IS WITHHELD
  TOO.** Where the comparator set is below the NORM floor, no delta against it ships:
  not a labelled one, and not an unlabelled raw one either. The entity's own figure
  ships, the comparator's count ships beside it, and the arithmetic between them is
  not performed. A delta against a fragile median is the fragile number wearing a
  minus sign, and stripping the WIN, MISS or FLAT label off it removes the wording
  while leaving the claim.
- **Rule: THE WITHHOLDING IS STATED, because silence reads as "no difference".** The
  artifact says, in one line beside the figure, that the comparison was withheld
  because the comparator set is below MIN_POPULATION_FOR_NORM, and it gives the count.
  A reader who is told nothing concludes there was nothing to tell.
- Mechanism: this rule and any skill section describing the same case state ONE
  instruction. Where a skill's own wording says the raw delta ships unlabelled, that
  wording is stale and this rule governs: the label and the delta stand or fall
  together, and the disclosure ships either way.
- Prevents: two artifacts off one configuration and one data set, which is what a run
  produced when one section said print four unlabelled deltas and another said draw no
  comparison from the median at all; and a fragile benchmark surviving into a
  permanent record with only its label removed.
- Source: P-D317; extended by the demonstration run, review N5
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-20 The population funnel publishes TWO numbers per step
- Rule: each step publishes the count remaining after it and the count dropped by
  it, both measured inside the scope as it stood. A file-wide figure never
  appears in the funnel, because reporting units that were never in scope makes
  the funnel fail to reconcile.
- Source: P-D297
- Applies: PLANNING, SCORECARD

### SD-POP-21 Detect the population shape and let it change the denominator, never the deliverable
- Rule: a FIXED roster and a FLOWING pipeline both rank, both exclude, both
  produce the same sections. What changes is what "the population" means: a
  roster as of a census date, or the open set under FLOW_OPEN_DEFINITION grouped
  by FLOW_COHORT_BASIS.
- Mechanism: where both the roster test and the entry-exit test pass, the
  population is FLOW with a stable roster of containers, and the container is a
  scope level rather than the unit.
- Prevents: a FIXED model applied to a pipeline silently mixing closed and open
  units into one denominator, which the reader cannot recover.
- Source: derived from P-D159, P-D216 and the population-shape binding
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-22 In a flowing population, exclusion by stage is an exclusion, not a filter
- Rule: units removed because they are closed, withdrawn or out of the open set
  are reported with their counts in the funnel exactly as any other exclusion is.
  They are never silently absent.
- Source: derived from P-D158 and P-D167 under FLOW
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-23 Shape is a property of the POPULATION being scored, not of the company
- Rule: FIXED and FLOW are not a fact about an organization. They are a fact about
  the population a given run is scoring. Many real businesses are genuinely both:
  a stable roster of units with work items flowing across them. Forcing one answer
  for the whole company is itself the error, and it is the error that produced
  three separate misbindings in acceptance testing.
- Mechanism: POPULATION_SHAPE holds a KEYED SET of declared populations, each with
  its own mode, its own unit noun, and its own fields. Every run resolves which
  declared population it is scoring, from the request and from the source in hand,
  and reads that population's shape. A business may declare one; it may declare
  three. Where only one is declared it is the default for every run and nothing
  else changes.
- Consequence: a skill never asks "is this company FIXED or FLOW". It asks "which
  population am I scoring, and what shape is that population". Two skills running
  the same morning on the same business may legitimately be in different shapes,
  and each names the population it scored in its own front panel.
- Consequence: two skills scoring DIFFERENT populations of the same business will
  report different counts, and neither is broken. Each states which population it
  scored and that the counts are not expected to agree.
- Prevents: a roster of standing positions being bound as a pipeline because its
  members happen to carry dates; a pipeline being bound as a roster because a
  roster of containers exists; and a business that is honestly both being forced
  to pick one and then quietly getting the wrong answer for half its work.
- Source: report 1 D2 and D19; report 2 D16 and D12
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-24 Shape is detected by three tests, and the third one decides
- Rule: detect the shape of each declared population with three tests, in this
  order, and never on the strength of the first two alone.
  1. THE ROSTER TEST. Can a complete list of all of them be produced as of a given
     date, without reference to what stage each is in? A confident yes is evidence
     of a roster.
  2. THE ENTRY AND EXIT TEST. Does each one have a date it entered and a date it
     stops being the organization's problem? Yes to both is evidence of a
     pipeline.
  3. THE REPLACEMENT TEST, which decides. When one of them leaves, does it leave a
     HOLE somebody notices and moves to fill, or does the next one simply take its
     place in a QUEUE? A hole means the unit is a standing position in the
     business: the population is a FIXED roster whose members happen to be dated,
     and the dates are unit attributes rather than a pipeline. A queue means FLOW.
- Rule: tests one and two both passing is the COMMON case, not the ambiguous one.
  A roster of dated standing positions passes both. So does a pipeline held inside
  a stable set of containers. The third test separates them and is not optional.
- **THIS IS THE ONLY SHAPE DETECTION PROCEDURE IN THE BUNDLE.** No skill, no
  interview turn and no provisional-run section states a second one. Where another
  file appears to give a shorter test, it is citing this rule and this rule
  governs. In particular, "an entry date plus an exit date plus a stage column
  means FLOW" is NOT a procedure; it is evidence toward test two only, and test
  two never decides on its own.
- Rule, and this is where the tie-break belongs: the tie-break is consulted ONLY
  where tests one and two DO NOT DISCRIMINATE, which means both passed or both
  failed, AND test three could not be answered. Read the three cases:
  - Test one passes and test two FAILS: FIXED, decided, by test two's absence of
    evidence for a pipeline. Do not run the tie-break, and do not prefer FLOW.
  - Test two passes and test one FAILS: FLOW, decided. The tie-break is not
    reached, and the record says decided rather than tie-broken.
  - Both pass, or both fail: tests one and two have not discriminated. Test three
    decides. Only where test three ALSO cannot be answered is the tie-break
    consulted.
- Resolution where the tie-break is reached: prefer FLOW, and record in the config
  that the shape was taken on the tie-break rather than answered, so the binding
  owner can see it and correct it. A tie-break that leaves no trace is a guess.
  Recording it as tie-broken where it was in fact decided by test one or test two
  is equally a defect, because it invites an owner to overturn a correct reading.
- Rule: where the roster test passes over CONTAINERS and the entry-exit test
  passes over the things moving across them, that is not a conflict. It is two
  populations. Declare both, per SD-POP-23, and let each run name which it scored.
- Prevents: the documented misbindings, in both directions, at three of five test
  companies.
- Source: report 2 D16; report 1 D2
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-25 Below the minimum rankable population, a ranked list is not a deliverable
- Rule: ranking, percentile, median, distribution and peer language are
  meaningless below a stated minimum. Define MIN_POPULATION_FOR_RANKING. Below it,
  the run does not emit a ranked list, does not print a percentile, and does not
  use comparative language, however well the arithmetic behaves.
- Mechanism: the arithmetic argument that a small population needs no special rule
  is true and irrelevant. An average-rank percentile over one unit is well defined
  and equals a constant; a rank of one out of one is well defined and says
  nothing. The test is not whether the number computes. It is whether the number
  carries information.
- What the output becomes instead, and it is not nothing:
  1. Say it on the front panel BEFORE the content, in plain words: this scope
     contains n units, so nothing here is ranked, no percentile is printed, and no
     comparison is drawn.
  2. Deliver the rows. Everything that describes a unit rather than ordering it
     survives: the identity block, the open work, the directed items, the
     exceptions, the narrative column.
  3. Name every suppressed comparison by name, so the reader can see what was not
     attempted rather than assuming it was attempted and came back empty.
  4. Name the scope level, or the finer thing, that WOULD produce a rankable
     population for this reader, so the answer is actionable rather than a refusal.
  5. Where another skill in the bundle scores a unit the reader genuinely chooses
     between, say which one and why: a scorecard whose scoring unit is the
     requirement rather than the entity produces a real deliverable for a reader
     who owns exactly one entity.
- Rule: this is not the same as fewer eligible units than the list size, which is
  a normal short list. It is a population too small to order at all.
- Rule: never pad, never present a one-row or two-row list as a plan, and never
  print a percentile of a population of one.
- Source: report 1 D3; report 2 D4
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-26 The unit of business must sit at or below the reader's own scope, and a mismatch is detected
- Rule: the level at which one unit of business sits must be at or finer than the
  requester's own scope level. Where the unit of business is COARSER than the
  reader's own scope, that reader owns a PART of a unit and cannot receive a
  ranked list of units at all. This is a binding error, not a small population,
  and it is reported as one.
- Mechanism, detection rather than assertion: resolve the unit level from the
  data. The scope level whose distinct value count over the in-scope population
  equals the record count of that population is the level at which a unit sits.
  Compare it against the reader's own resolved level. Where the unit level is
  coarser, say so before the content, name both levels, and route per SD-POP-25.
- Mechanism, THE TIE-BREAK: where MORE THAN ONE level satisfies the test, take the
  FINEST matching level. More than one level always satisfies it when the in-scope
  population holds exactly one record, because every level then has exactly one
  distinct value, and the no-level-matches fallback does not apply because they all
  match. The finest is correct because a finer level can never be the wrong answer
  for a reader who owns it.
- Mechanism, THE SECOND TEST: a binding error is reported ONLY where the reader's
  own level is strictly FINER than EVERY level that satisfies the test over a
  population of MORE THAN ONE RECORD. Where the population holds one record the
  detection is uninformative: say the scope holds one unit and do not assert a
  configuration mismatch the data cannot distinguish. Without this, the coarsest
  reading calls a correct configuration a binding error and the finest reading
  never surfaces a real one, and both artifacts pass every gate.
- Prevents: a binding interview accepting two individually correct answers, a
  containment chain and a unit noun, that are incompatible with each other, and
  producing a one-row artifact in which every gate passes and every count
  reconciles.
- Source: report 1 D3; report 2 D4
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-27 A measure that is uniform across the whole population contributed nothing, and the output says so
- Rule: where the ranking measure takes the same value for every unit in the
  population, every unit receives the same percentile, the measure factor becomes
  a constant, and the ordering is decided entirely by the other terms. That is
  often the correct behaviour. It is never an acceptable silence.
- Mechanism: state it on the front panel in those words, name the terms that
  actually decided the order, and never print a measure percentile column of
  identical values without that statement beside it.
- Prevents: a reader treating a composite score as a normal composite when one of
  its two factors is inert. The specific case is a launch, where no unit has
  measure history and the ranking is the bracket alone.
- Source: report 2 D5
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-28 A status column that resolved is READ, and the default is not "include everything"
- Rule: resolving a concept and binding its VALUES are two different bindings, and
  the gap between them is where the most damaging kind of error lives. Where the
  not-actionable concept RESOLVES and the value list is unbound, the run does NOT
  default to excluding nothing. It applies the seed value set, discloses the whole
  decision, and asks first where it can.
- The named case, and it is the reason this rule exists: a status column resolved
  cleanly, its values were visible in the artifact, the value list was a separate
  unbound variable whose default was "no exclusion", and the run therefore ranked
  a PROSPECT at rank one of a working plan and put four non-active units in a
  senior reader's top twenty. It was disclosed on the front panel, in the funnel
  and twice in the audit, every gate passed, and the artifact was still not fit to
  hand to anybody. Correct disclosure does not redeem a wrong instruction.
- **THE ASYMMETRY THAT DECIDES THE DEFAULT.** Including a unit nobody can work
  this period sends a person to do impossible work and costs them the trust they
  had in the list. Excluding a unit that was in fact workable costs one row on one
  list, is visible in the KEPT-and-EXCLUDED listing the same run prints, and is
  recoverable in a sentence. The errors are not symmetric, so the default is not
  neutral, and pretending it is neutral is itself a choice with a cost.
- Mechanism, and all three guards are mandatory:
  1. THE STAGE GUARD. Under FLOW, a value that is also a stage name is NEVER
     excluded from an unbound default. A terminal stage is handled by the open-set
     rule, and letting an exclusion delete a stage is the failure SD-PRS-47 and
     SD-POP-05 both name.
  2. THE MAJORITY GUARD. Where the seed set would remove more than
     EXCLUSION_SANITY_CEILING of the in-scope population, nothing is excluded and
     the run says the column was read and looked wrong. A default that removes
     most of a population has almost certainly read the wrong column. This guard
     applies ONLY to a default; an exclusion the organization BOUND is never
     refused on volume, because an organization is entitled to know its own
     business.
  3. THE NAMING GUARD. Every distinct value in the column is printed under one of
     exactly two headings, EXCLUDED or KEPT, each with its count.
- **THE SEED SET MUST COVER THE DECIDED EXIT THAT HAS NOT COMPLETED, AND THE MATCH
  MUST BE TOKEN-WISE.** This is where the first version of the rule failed in the
  field. A seed set of terminal words plus a whole-string prefix comparison
  excluded the never-started states correctly and missed every DECIDED EXIT IN
  PROGRESS, because those statuses are compound and read as active: a pending
  non-renewal, a cancellation pending, a notice served, a book in run-off. Neither
  side of a whole-string prefix test reaches the other, so nothing matched, and
  eleven units that had already given notice of exit ranked at full weight with
  two of them inside a published top twenty. An account that has given notice
  cannot be sold this period, and putting it near the top of a selling plan is
  precisely the failure this rule exists to prevent.
  Two changes together, and neither works without the other:
  - The seed set covers THREE families, not one: terminal states, DECIDED EXITS
    NOT YET COMPLETE, and never-started states, plus the temporarily unreachable.
  - The comparison is TOKEN-WISE and BIDIRECTIONAL: every token of a seed entry
    must appear in the cell value, in any order, where either token may be a
    prefix of the other and the shorter is at least four characters.
- **AND THE MATCH MUST NOT REACH AN ACTIVE STATUS THAT MERELY MENTIONS THE SAME
  NOUN.** A status meaning a renewal is in progress and workable shares the word
  renewal with a status meaning a renewal has been refused. The negation carries
  the meaning, so the seed entries in the decided-exit family carry their negating
  token and are matched as a whole entry, never token by token in isolation. Bare
  single-word seed entries that would prefix an ordinary word are excluded from
  the set for the same reason. Test any addition to this set against the active
  statuses of the same family before adding it.
 The reader sees
     the whole decision, not its result. A local status word meaning the same
     thing as a seed value will not be in the generic set and will appear under
     KEPT, which is precisely where a reader spots it in one glance.
- Rule: where the run can ask, it asks first, ONCE, as a PERSON-tier question
  about the user's own file, per reference/field-resolution.md F5.1b. No binding authority
  is required, because the question is about what values in a file mean and never
  about what the organization's policy is. **Silence on that question proceeds on
  the default and says it was unconfirmed. It never reverts to excluding nothing.**
- Rule: this does not weaken SD-CTR-24 or the no-silent-widening rule. A
  documented default may narrow what a run attempts and must never contradict a
  value the organization bound. Where UNIT_ACTIONABLE_NOW_VALUES IS bound, the
  bound list governs completely and the seed set is not consulted at all.
- Prevents: a technically flawless artifact that sends a person to renew an
  account that is not a client.
- Source: confirmation run 2, blocker 2; extends report 2 D9
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-30 The not-workable exclusion asks a different question in a retrospective than in a plan
- Rule: the exclusion of units that cannot be worked is a FORWARD-LOOKING test, and
  a retrospective is not forward looking. Under PLANNING and SCORECARD the question
  is "can this be worked in the period being planned", and a unit that cannot is
  removed. Under REVIEW the question is **"was this workable at ANY point in the
  period being reviewed"**, and the answers differ for exactly the units that
  changed state during it.
- **THE REASON, STATED SO IT IS NOT READ AS A TECHNICALITY.** A retrospective
  population is what a person was RESPONSIBLE FOR DURING the period, not what
  survives at the end of it. A unit that became unworkable in month nine was
  workable for eight months, and the work done on it was real work. Applying the
  planning exclusion to a year-end review deletes eight months of somebody's year
  from their own review, and it does so silently, because the unit simply is not
  there to be missed. That is the same class of error as a survivor-only prior
  file, arriving from the opposite direction: one hides what left, the other hides
  what was there.
- Mechanism, three cases and each has one answer:
  1. NOT WORKABLE FOR THE WHOLE PERIOD: EXCLUDE. It was never theirs to work. It is
     excluded because it was never in the population, not because it left one.
  2. BECAME UNWORKABLE DURING THE PERIOD: INCLUDE AND MARK. Name the date it
     changed and, where derivable, the portion of the period it was workable.
     Every rate computed over the population says whether it pro-rated.
  3. TRANSITION DATE NOT ESTABLISHABLE: INCLUDE AND DISCLOSE. Where the count of
     such units is material to a published figure, report the figure BOTH WAYS with
     the difference named, per the pairing discipline in SD-CMP-09. Do not choose
     silently between two populations when the choice moves a number.
- Rule: FORWARD-LOOKING statements INSIDE a review, such as next-period
  commitments or a plan for the coming window, take the PLANNING reading and
  exclude on current workability. One document can legitimately hold both readings;
  what it may not do is apply one of them without saying which.
- Rule: the mode is a property of the RUNNING SKILL and is never inferred from the
  data. A run states which reading it applied, in the front panel, in one line.
- Prevents: a year-end review scored on a population that omits everything the
  person worked and then lost, which flatters and penalises different people
  unpredictably and is invisible in the output.
- Source: review acceptance run, SHARED 1
- Applies: PLANNING, REVIEW, SCORECARD

### SD-POP-29 A character-length threshold is not a matching rule, and a value match is by whole tokens
- Rule: never decide whether one token matches another by how LONG it is. A
  character count cannot tell a meaningful short token from a fragment of a longer
  word, so any rule of the form "these match if either is a prefix of the other and
  the shorter is at least N characters" is forbidden as a matching device anywhere
  in this bundle.
- **THE FAILURE IS IN BOTH DIRECTIONS AT ONCE, WHICH IS WHY THE THRESHOLD CANNOT BE
  TUNED OUT.** One real rule with a four-character floor was simultaneously:
  - TOO LOOSE. A four-letter word sitting inside a longer seed entry matched a
    perfectly ordinary word in a live status, so a status meaning an active renewal
    was due matched a terminal seed entry and a workable unit would have been
    silently removed from the plan. Removing workable units is the same class of
    harm as keeping unworkable ones, in the other direction, and it is harder to
    notice because the evidence leaves with the row.
  - TOO TIGHT. The negating token in every decided-exit phrase is three characters,
    below the floor, so a literal reading matched nothing at all and the entire
    exclusion the rule existed for did not fire. The headline behaviour was one
    literal reading from being absent.
  Raising the floor breaks the second case further; lowering it breaks the first.
  There is no value of N that works, which is the proof that N is the wrong
  instrument.
- Mechanism, four steps, and this is the whole rule:
  1. NORMALIZE both sides: lowercase, every non-alphanumeric character becomes a
     space, collapse runs of spaces, split into tokens.
  2. PHRASE TEST: an entry matches when its token sequence appears as a CONTIGUOUS
     RUN inside the cell's token sequence, comparing tokens by EXACT EQUALITY. A
     one-token entry matches only an identical token. Word boundaries therefore come
     free: a token cannot match inside another token because tokens are compared
     whole.
  3. THE SINGLE-TOKEN OVERRIDE: where the cell carries a token marking a live
     relationship, a match by a ONE-TOKEN entry is REFUSED and only a multi-token
     entry may fire. A compound status that names a live relationship needs the exit
     stated as a phrase, not implied by one word.
  4. REPORT THE REFUSAL, on its own line, naming the cell, the entry and the marker
     that refused it. A near miss the reader cannot see is the same as no rule.
- **Rule: ONE LIST, ONE PLACE. A value set has exactly one home and every other
  mention of it POINTS at that home rather than restating any part of it.** A
  partial restatement is a second default, and a reader who finds the short one
  never learns the long one exists. The observed cost: one variable carried a short
  illustrative list in a definition table and the full list in the defaults
  appendix, and five of thirty-four verified cases changed verdict depending on
  which a reader used. This applies to an EXAMPLE column as much as to prose:
  where a variable's members ARE its documented default, its example cell names
  where the list lives and shows none of it.
- Rule: **morphological variants are LISTED, never derived.** Dropping prefix
  matching means a stem no longer reaches its own plural or participle, so every
  form that must match is an entry in its own right. That is more lines and it is
  the correct trade: a list is auditable and a derivation is not.
- **Rule: a claim that a rule was verified against named traps is itself testable,
  and it is TESTED, not asserted.** The rule this replaces carried a notice naming
  three traps it had been verified against, and it failed one of them. A document
  that asserts a test it does not pass is worse than one that claims nothing,
  because it spends the reader's trust to hide the defect. Where a rule's notice
  names example inputs, those exact inputs are run and their results printed.
- Prevents: silently removing workable units, silently removing nothing at all, and
  a document asserting a test it fails.
- Source: release acceptance run, N1 and N2
- Applies: PLANNING, REVIEW, SCORECARD

---
