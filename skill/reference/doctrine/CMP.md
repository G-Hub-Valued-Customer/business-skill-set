# GROUP CMP: COMPARING TWO PERIODS

### SD-CMP-01 Never infer change from one snapshot, and say nothing about trend unless asked
- Rule: if the user did not ask, rank the single input and deliver. Do not mention
  trend, do not ask for a second file, do not caveat the absence of one. If they
  did ask, two inputs are required and a single one is a hard gate. "Never
  substitute gap indicators for measured change."
- Source: P-D248
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CMP-02 Make two inputs apples to apples before comparing
- Rule: map each file's columns independently; filter both to the same scope using
  each file's own column; confirm the metric matches on concept AND time basis;
  join on the identifier; note units present in one file only rather than dropping
  them silently. "A mismatched basis is not a comparison: report it and compare
  only on metrics that align."
- Source: P-D249; R-D22
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CMP-09 Test the EXIT side separately, because a survivor-only prior file scores perfectly on an overlap test
- Rule: under FIXED, like-for-like is not established by roster OVERLAP alone.
  Overlap tests the ENTRY side, whether the units in the prior file are still here.
  It cannot see the units that LEFT, because they are absent from both sides of the
  test. Run a separate EXIT TEST before computing anything on the pair.
- **THE PATHOLOGY, AND IT IS THE ONE INPUT THAT SCORES PERFECTLY WHILE BEING
  UNUSABLE.** A prior-period file containing ONLY the units that survived into the
  current period yields 100 percent overlap, zero churn out, and passes the join
  overlap floor at its maximum. The test that exists to decide whether two files
  describe the same population CERTIFIES it as ideally comparable. Every retention
  figure computed on it is 100 percent by construction, and every same-unit growth
  figure is biased upward by exactly the units that left. In the observed case the
  weakest performer by total measure was the joint best by survivor growth, and
  both figures were arithmetically true. Only one was a fact about their year.
- **THE EXIT TEST: count the units present in the PRIOR file and ABSENT from the
  current one. That count is the number of exits the pair can see.** Where it is
  ZERO, the run is in one of exactly two states, and they are not the same state:
  1. A SURVIVOR-ONLY EXTRACT. The prior file is the current roster valued at an
     earlier date, not the roster as it stood at that date.
  2. A POPULATION THAT GENUINELY LOST NOTHING. Real, and rare above a small
     population.
- Rule: the run DECIDES between them, says WHICH it believes and WHY, and does so
  BEFORE it computes anything on the pair. The evidence that separates them:
  population size, since zero attrition over a large population is extraordinary
  and over a handful is unremarkable; whether the prior file's row count equals the
  current count minus the units created since; whether any independent source
  disagrees with the prior file's counts; and whether the prior file's own period
  stamp precedes the units it contains.
- **WHAT MAY BE CLAIMED FROM A SURVIVOR-ONLY PAIR, AND IT IS A CAP NOT A REFUSAL:**
  - RETENTION and CHURN: NOT COMPUTABLE. Not zero, not 100 percent. The file cannot
    answer the question, and a retention figure from it is an artefact of the
    extract. Say so where the figure would have gone.
  - SAME-UNIT GROWTH: computable, SURVIVOR-BIASED, and never published as a bare
    figure. It is published only BESIDE the total movement across the whole
    population, with the gap between them named for what it is: the part of the
    change that left. That pairing is more useful than either number alone and it
    is the form the figure ships in.
- **Rule: THE GAP HAS TWO FORMS AND THE BRANCH IS DECIDED BY WHETHER THE TWO FIGURES
  REST ON ONE MEASURE.** A gap is a NUMBER only when both figures are computed on the
  SAME MEASURE on the SAME BASIS.
  - **SAME MEASURE: name the gap as a figure**, survivor growth less total movement,
    with the measure and the basis named once beside it.
  - **DIFFERENT MEASURES: the gap is a STATEMENT IN WORDS AND NEVER A SUBTRACTION.**
    Print both figures with their bases named and say in words what separates them.
    This is the ORDINARY case rather than the exception, because the total movement
    usually comes from a production system and the survivor figure from a book
    extract: one measured pair differed by a factor of 3.87 on the same population,
    and a difference between them would have been a number with no referent.
  - **G14 GOVERNS THIS BRANCH AND IS NEVER OVERRIDDEN BY IT.** No growth, delta or gap
    is computed across differing units or differing measures; a mismatch is BLOCKED
    with no override, and this rule's requirement that the gap be NAMED is satisfied by
    naming it in words. **A rule that requires a figure never authorizes a forbidden
    subtraction to produce one.** Where the two rules appear to conflict, the block
    governs and the words are the form the gap ships in.
  - TOTAL MOVEMENT across the whole current population: computable and unaffected,
    because it never depended on the join.
  - Any RANKING of units by survivor growth: NOT PUBLISHED, because the bias is not
    uniform across units and the ordering is therefore not recoverable.
- Rule: a genuine no-attrition population is stated as such with its evidence, and
  its retention figure IS published, at 100 percent, with the population size
  beside it so a reader can weigh it.
- **Rule: this is a NAMED test with a NAMED result, not a reconciliation habit.**
  The observed catch happened only because two sources disagreed on a count and a
  general rule against publishing a value whose derivations disagree fired. Had the
  counts agreed, nothing would have caught it. A trap that is caught by luck is not
  caught.
- Prevents: a flattering figure certified as ideally comparable by the very test
  aimed at it.
- Source: review acceptance run, trap 2
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CMP-03 A zero baseline is a new-entry case, not an infinity
- Rule: when the baseline is zero and the current is non-zero, list the unit as a
  new case and leave the change blank rather than infinite.
- Source: P-D250
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CMP-04 The comparison score carries the full bracket, not just the measure weighting
- Rule: multiply the change term by the same bracket the normal score uses,
  computed over the current period. "A unit that declined AND carries open
  directed work outranks one that merely declined, which is the intent."
- Source: P-D251
- Applies: PLANNING, SCORECARD

### SD-CMP-05 A comparison changes the ranking basis, never the deliverable shape
- Rule: same sections, same sizes, same caps. Nothing about a comparison suspends
  the other rules.
- Source: P-D252
- Applies: PLANNING, SCORECARD

### SD-CMP-06 The peer set is defined by the period-end file
- Rule: group by the peer level column, compute every metric for every peer, rank
  the user and count how many peers share the user's value. Every comparison runs
  on the same-unit intersection used for the user's own metrics. "Rosters change
  between periods. Ranking a user against a roster that includes peers absent from
  one file produces a rank that cannot be reproduced. State the peer count and the
  unit basis alongside every rank."
- Source: R-D25
- Applies: REVIEW, PLANNING, SCORECARD

### SD-CMP-07 A two-pass split must NOT change the denominator, and two passes is not sampling
- Rule: the first pass retains the full sorted distribution or an exact rank index
  and carries it into the second pass as part of the checkpoint. The second pass
  looks percentiles up rather than recomputing them. Both passes read every row.
- Mechanism: "If the second pass were to rank the survivors among themselves,
  every percentile would shift upward, and a large-tier run would rank the same
  units differently from a small-tier run on the same data. A unit's percentile
  must be identical whichever tier processed it." Verified directly by re-reading
  a sample of units.
- Source: P-D313
- Applies: PLANNING, SCORECARD

### SD-CMP-08 A comparison request against a population with no prior period is answered, not stopped
- Rule: a request to compare, made against a population where no unit predates the
  current window, is not a missing-file problem and must not be answered by asking
  for a file that does not exist and never will.
- Mechanism: before the one-input stop fires, test the population's own entry
  dates. Where no unit predates the current window, or where fewer than
  COLD_START_MIN_PRIOR_SHARE of units do, the population is COLD and the stop is
  replaced by an answer:
  1. Say that no prior period exists for this population, and name the earliest
     entry date found as the evidence.
  2. Offer the second numbers that DO exist: attainment against a plan set before
     the period, and the bare denominator population.
  3. Emit the current state, ranked by the terms that are computable, and the
     absolute build to date.
- Rule: the one-input stop survives unchanged for a WARM population. It is a
  correct gate against a user who forgot to attach the second file. It is a dead
  end for a user whose second file cannot exist.
- Prevents: the executive altitude of a launch, which is the altitude that most
  needs an answer, receiving a request it cannot satisfy.
- Source: report 2 D5
- Applies: PLANNING, REVIEW, SCORECARD

---
