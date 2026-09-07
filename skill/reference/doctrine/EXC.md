# GROUP EXC: THE EXCEPTION LIST

### SD-EXC-01 An exception list answers a different question from a ranked list and never touches the ranking
- Rule: not "where is the opportunity" but "where is something quietly wrong that
  no other report will surface". Membership is tripping at least one SCORED flag.
  It is an exception list, never the full roster.
- Source: P-D253
- Applies: PLANNING, SCORECARD

### SD-EXC-02 A recency threshold SCALES with the local cadence
- Rule: flag above max(RECENCY_FLOOR_DAYS, RECENCY_MEDIAN_FACTOR times the local
  median interval).
- Mechanism: "cadences differ sharply by unit, so a flat line means very different
  things in each. A flat line floods a fast unit and hides real gaps in a slow
  one."
- General form: applies wherever cadence varies by unit.
- Source: P-D254
- Applies: PLANNING, SCORECARD

### SD-EXC-03 An ALERT is a different instrument from a MEMBERSHIP flag, and it does NOT scale
- Rule: the membership flag scales with the local cadence. The alert answers "has
  this been left too long by any reasonable standard" and uses a flat threshold.
- Mechanism: "A scaled alert in a fast unit would fire at eight weeks and stop
  meaning anything."
- Source: P-D255
- Applies: PLANNING, SCORECARD

### SD-EXC-04 Count the alert over the whole population, not over displayed rows
- Rule: a unit can trip the alert and still be absent from the section, because
  the membership flag scales and because the cap can push it off. State that the
  counts are population-wide and may exceed the shaded rows visible. "Counting
  only displayed rows would under-report the exact units the alert exists to
  catch."
- Source: P-D256
- Applies: PLANNING, SCORECARD

### SD-EXC-05 A gate must allow a subset relationship it created itself
- Rule: "Do NOT require the shaded cell count to equal the reported figures.
  Shaded cells are a SUBSET of the reported counts and the gate must allow that."
  What the gate does check: every displayed row in a band carries the right fill,
  and no row outside a band carries any.
- Prevents: a self-contradictory gate that blocks every run.
- **BUT A SUBSET THE GATE PERMITS IS STILL A CONTRADICTION THE READER SEES, AND IT
  MUST BE RECONCILED IN THE ARTIFACT.** Permitting two measures to disagree is not
  the same as leaving a reader to discover the disagreement. The observed case: an
  exception section EMPTY in every run while the alert line two inches above it
  reported thirteen stale units. Both were correct and both followed the rules,
  because the flag SCALES with the population's own cadence while the alert uses
  FLAT day bands, and no item in the file reached the scaled threshold. The gate
  was right to allow it and the workbook still said two contradictory things on
  one page.
- Rule: wherever an alert count is NON-ZERO and the section it appears to
  summarize is EMPTY, the empty section carries ONE row reconciling them, naming
  both counts, both thresholds, and the reason they differ, in the reader's own
  terms. This does NOT force the two to agree, and no gate may require that; it
  forces the artifact to explain itself. An unexplained empty section beside a
  non-zero alert reads as a broken report, and a reader who concludes the report
  is broken is right to stop trusting the parts that are not.
- Source: P-D257; extended by acceptance run 3, defect 5
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EXC-32 A band nobody can reach is not a band, and thresholds are relative to what evaluated
- Rule: a scoring band is only real if the score that reaches it is ATTAINABLE
  given the flags that actually evaluated on this run. Where fewer flags resolve
  than the thresholds were calibrated against, an absolute threshold set for the
  full set becomes unreachable by construction and the top band silently ceases to
  exist.
- The named case: four flags with weights, thresholds calibrated for all four, and
  a real file on which exactly one flag could be evaluated. The maximum attainable
  score was then below the top threshold, so no unit could be banded high however
  bad it was, and the exception section shipped empty in three consecutive runs.
  Nothing failed. Nothing was reported as failing. The band was simply gone.
- Mechanism: express default bands as SHARES OF THE ATTAINABLE MAXIMUM, where the
  attainable maximum is the sum of the weights of the flags that EVALUATED, times
  the largest multiplier in play. Recompute it every run, because which flags
  evaluate is a property of the file and not of the configuration. Print the
  attainable maximum and the resulting absolute thresholds in the audit, so a
  reader can see what the bands meant on this file.
- Rule: an ABSOLUTE threshold binding is legal and, where an organization binds
  one, it is used as given. It is REJECTED AT VALIDATION where the top band exceeds
  the attainable maximum of the flag set it is bound alongside. A configuration
  that cannot reach its own top band is a configuration error, and it is caught at
  binding time rather than discovered three runs later in an empty section.
- Rule: **every flag carries an explicit weight.** A taxonomy that says each flag
  carries its own weight and then ships a default naming no weights forces every
  implementer to invent one, and two implementers invent differently off one
  configuration. A weight is not an optional refinement of a flag; it is half of
  what a flag is.
- Rule: a flag that could not be evaluated is REMOVED FROM THE ATTAINABLE MAXIMUM,
  never counted as a zero contribution. Counting it as zero is what makes the
  denominator lie: it says the population was measured against four tests when it
  was measured against one.
- Prevents: a top band that quietly does not exist, and an exception section that
  is empty for a reason no reader can see.
- Source: acceptance run 3, defect 5
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EXC-06 Report a zero count, because it is the evidence the check ran
- Rule: report both counts every run including when they are zero. "A zero-count
  line is not noise: it is the evidence the check ran."
- **A CHECK THAT COULD NOT RUN IS NOT A ZERO, AND MUST NOT BE PRINTED AS ONE.**
  Where the column a check reads did not resolve, or resolved and carries no data,
  the line still prints, and it prints NOT EVALUATED in place of the counts, with
  the reason and the column named. A zero there asserts that nothing is overdue
  when nothing was looked at, which is the one thing a reader of an alert line
  cannot recover from. THREE states, never two: a count, a zero, and not
  evaluated.
- Source: P-D258
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EXC-07 Date arithmetic rules stated explicitly, including the error case
- Rule: whole days from the recorded date to the run date. A blank, null or
  unparseable date is NOT counted in either band and is reported separately. A
  future-dated value is a data error: report it, do not shade it, and do not treat
  it as zero.
- **AND IT IS EXCLUDED FROM EVERY DERIVED STATISTIC COMPUTED FROM THAT COLUMN, NOT
  ONLY FROM THE BANDS.** This was the unwritten half, and a published number turned
  on it. A future-dated recency value yields a NEGATIVE interval, and a negative
  interval is not an interval. It therefore does not enter the MEDIAN, the mean,
  any percentile, any local cadence, or any threshold scaled from one. The
  arithmetic rule and the statistics rule are the same rule and neither may be read
  without the other.
- The measured cost of leaving it unwritten: on one real file, including the
  future-dated rows in the local median moved the median by about fourteen days,
  moved the scaled threshold by about twenty-seven days, and moved the exception
  section between THIRTEEN members and ZERO. Two competent implementers produced
  two different sections off one file, and no gate could catch it because both were
  internally consistent.
- Rule: the count of excluded future-dated values is REPORTED beside the statistic
  it was excluded from, not only in the error list, so a reader can see how much of
  the column the statistic actually rests on. Where more than half the populated
  values are future-dated, the statistic is NOT PUBLISHED at all and the column is
  reported as unusable, because a median of the minority is a number with a
  misleading amount of authority.
- Rule: the same exclusion applies to every other impossible value in a derived
  statistic: a negative duration, a negative count, an exit before an entry. A
  value that cannot exist does not get a vote on what is typical.
- Source: P-D259; extended by release acceptance run, N6
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EXC-08 Run only the flags whose columns resolved AND carry data; never treat an absent column as a gap
- Rule: skip the flag entirely, name it as not evaluated and why, and score the
  remaining flags normally. If no flag can be evaluated at all, ship the section
  with one row saying so.
- Mechanism: "an unpopulated commitment column would otherwise put every eligible
  unit on this section flagged for missing every commitment, which is the single
  most damaging false positive this method can produce."
- Source: P-D260
- Applies: PLANNING, SCORECARD

### SD-EXC-09 Weight the flags, do not count them
- Rule: "A raw count treats a long-standing pricing note as equal to an empty
  shelf."
- Source: P-D261
- Applies: PLANNING, SCORECARD

### SD-EXC-10 The measure multiplier has a HALF FLOOR so a real problem at a small unit stays visible
- Rule: multiply the summed flag weight by FLAG_MEASURE_MULTIPLIER_FLOOR plus
  (1 minus that floor) times the percentile.
- Mechanism: "Without this a bottom-percentile unit lands in the top band on two
  flat flags, which contradicts the whole premise. The half floor keeps a genuine
  problem at a smaller unit visible rather than erasing it."
- General form: a precise statement of how to weight by size without erasing the
  small.
- Source: P-D262
- Applies: PLANNING, SCORECARD

### SD-EXC-11 Band AFTER the multiplier, and set the thresholds against the post-multiplier range
- Rule: thresholds set at the raw flag weights are wrong, because every score is
  multiplied by a factor that never exceeds one.
- Mechanism: "A single top-weight flag lands at its full value only for the
  highest-measure unit in scope, at three quarters for a median unit and at half
  at the bottom, so under the old threshold the top band silently required two
  flags and the column the reader sorts on was deflated across the board."
- General form: a threshold calibrated against the pre-transform scale is a very
  common real bug.
- Source: P-D263
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EXC-12 A signal that lags reality is disclosed, and weighted only where it is the subject
- Rule: a lagging recency field carries weight inside the exception section and
  zero everywhere else. "It never touches the action lists, and the section must
  say so on its face", with the disclaimer printed as a visible note.
- Mechanism: "Weighting it would steer people back to units they just left."
- Source: P-D264
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EXC-13 Report the local benchmark alongside each figure so an outlier is legible as one
- Rule: print the benchmark once beside the figure.
- Source: P-D265
- Applies: PLANNING, SCORECARD

### SD-EXC-14 A gap the person cannot close is not a gap worth printing, and there are TWO tests
- Rule: "Before adding a flag, confirm the person both engages the unit and
  controls the thing being measured."
- Mechanism: applied concretely, a commitment set at a parent level "is a matter
  no front-line person can close: counting it is the single most damaging false
  positive this method can produce."
- REFINEMENT, and it is load bearing. The rule has been read as one test and it is
  two, and only the second suppresses scoring. Separate the AUTHORITY to set a
  requirement from the ABILITY to affect the measured value.
  1. THE ENGAGEMENT TEST. Does the reader engage this unit at all? If not, the
     item is not theirs: it is shown rather than scored.
  2. THE INFLUENCE TEST. Can the reader's own actions MOVE the measured value,
     whoever set the requirement? If yes, it is SCORED, however far above them the
     requirement was set. A requirement set by a regulator, a parent organization
     or a central function is shown rather than scored ONLY where compliance with
     it is also determined above the reader, such as a contract term, a purchased
     configuration or a decision taken at a level the reader cannot reach.
- Prevents, in the first direction: counting a gap the reader cannot close.
- Prevents, in the second direction, which the single-test reading caused: moving
  most of a requirement set to shown-never-scored because a regulator set it,
  leaving a pass rate computed over a handful of items and a near-empty worklist
  that reads as "you are fine". The one number the reader would act on, the count
  of things to go and fix, is then suppressed by a rule written to protect them.
- Rule: where more than half a requirement set falls to shown-never-scored, stop
  and say so on the front panel BEFORE the pass rate: this scores n of m
  requirements, and the rate covers only those.
- General form: the flag carries EXCEPTION_FLAGS.requires_decision_authority_at_unit,
  which is now read as the influence test rather than the authority test.
- Source: P-D266; P-F7; refined by report 1 D12
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EXC-15 Two flags are needed because one cannot fire where the other applies
- Rule: a binary presence flag and a degree-of-completeness flag are siblings. "A
  unit failing the presence flag cannot fail the degree flag, because it has no
  figure at all, which is exactly why both flags are needed."
- General form: a ratio metric cannot see a zero denominator.
- Source: P-D267
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EXC-16 Show both sides, never the delta alone
- Rule: "the pair is the conversation." Include the sizing figure so the reader
  can size it.
- Source: P-D270
- Applies: PLANNING, SCORECARD

### SD-EXC-17 Note when a unit appears on two sections, because that is two independent reads on the same problem
- Rule: where one unit qualifies for two sections, say so on both. Two sections
  reaching the same unit by two different tests is corroboration, and a reader who
  sees it once sees a coincidence rather than the second read.
- Prevents: the strongest signal in the artifact being invisible because it is split
  across two places that never mention each other.
- Source: P-D271; P-D291
- Applies: PLANNING, SCORECARD

### SD-EXC-18 The economics gate, not a geography gate
- Rule: adoption of a cost-bearing programme tracks size, not location, so the
  qualifying rule is a size test and not a location test. "A small unit declining
  is a rational business decision, not an execution gap." Recompute the size
  figures from the user's own file every run and never quote reference figures.
- Source: P-D272
- Applies: PLANNING, SCORECARD

### SD-EXC-19 Do NOT suppress an opportunity because most local peers also lack it
- Rule: "Low penetration is exactly what an opportunity looks like." The measure
  weighting already handles genuine regional differences. "Do not build a
  hard-coded regional table: it cannot be validated from a single-region file, and
  it rots silently."
- Source: P-D273
- Applies: PLANNING, SCORECARD

### SD-EXC-20 Benchmark ONE LEVEL WIDER than the user's own slice
- Rule: a unit against its parent, a parent against its parent. When the file
  holds nothing wider, benchmark against the whole file and say so, "because a
  slice compared only to itself cannot see that it is the weakest one."
- Source: P-D274
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EXC-21 Report the benchmark once, do not repeat it per row
- Rule: a benchmark that is the same for every row is stated ONCE, beside the section,
  and never repeated in a column of identical cells.
- Prevents: a full-width column of one repeated value spending the reader's attention
  and the sheet's width on a single fact.
- Source: P-D275
- Applies: PLANNING, SCORECARD

### SD-EXC-22 Some values are SHOWN, never SCORED, and never confer membership
- Rule: display the status in its own column for every row, give it zero weight,
  and report the population share as a single figure.
- Source: P-D276
- Applies: PLANNING, SCORECARD

### SD-EXC-23 State no interpretation of a value whose meaning varies by jurisdiction
- Rule: print the status and the benchmark; do not tell the reader what it
  implies, because the rules that give it meaning differ by place and the method
  runs in all of them.
- Quote: "report what the data says, attribute it, and leave the judgment to the
  person who knows their jurisdiction."
- Source: P-D277
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EXC-24 Do not build a second version of something that already has a system of record
- Rule: even where the inputs are present, do not duplicate a capability another
  system owns, "because a second version competes with the system of record."
- Source: P-D278
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EXC-25 Check a field's fill rate before building on it
- Rule: a field populated for a small fraction of units is too thin to be useful.
  Check the rate rather than assuming, and say so if a future file is materially
  better populated.
- Source: P-D279
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EXC-26 Exemptions are kept as belt and braces after the upstream fix
- Rule: once a class is removed upstream, per-flag exemptions never fire, but they
  remain as a second line of defence in case a future change re-admits the class.
  A unit of that class appearing on the section is treated as evidence the
  upstream exclusion failed, and the artifact should not be published.
- General form: a defence-in-depth pattern with an explicit tripwire reading.
- Source: P-D280
- Applies: PLANNING, SCORECARD

### SD-EXC-27 Do not extend a narrow exemption by analogy
- Rule: "If someone says another group behaves the same way in their area, that is
  a change to request, not one to infer from the data."
- Source: P-D281
- Applies: PLANNING, SCORECARD

### SD-EXC-28 Compliance is checked BEFORE weighting, and it is a guardrail rather than an optimization
- Rule: an item that cannot lawfully or contractually be executed in the user's
  jurisdiction is not an opportunity and must never be weighted as one. Check each
  distinct jurisdiction once, cache the reading, apply per unit.
- Mechanism: a five-row finding table. Restricted means weight zero and removal
  from the ranking, with the rule named.
- Prevents: recommending work that cannot be done, which is worse than
  recommending nothing.
- Source: P-D121
- Applies: PLANNING, SCORECARD

### SD-EXC-29 A compliance gate fails closed on the priorities, not on the run
- Rule: if the compliance source is unreachable, hold back every priority that
  could not be validated, rank without them, and report which were held back.
  "Everything else fails closed, and a compliance gate must not be the one
  exception, but an unreachable reference is not a reason to withhold the
  artifact."
- Source: P-D122
- Applies: PLANNING, SCORECARD

### SD-EXC-30 Never silently drop a priority
- Rule: list every dropped priority with the reason. "A person whose top
  initiative does not appear needs to know it was excluded for a local rule rather
  than assume the method missed it."
- Source: P-D123
- Applies: PLANNING, SCORECARD

### SD-EXC-31 A local exception in a reference field is honoured and never guessed at
- Rule: a scope caveat in a supporting-resources field is read and honoured. An
  item restricted to a jurisdiction the user does not operate in is dropped
  entirely and the drop is named. "Never guess at an abbreviation in a title when
  the resources field spells it out."
- Source: P-D124
- Applies: PLANNING, SCORECARD

---
