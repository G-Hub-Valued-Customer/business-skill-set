# APPENDIX B: WHAT AN UNBOUND VARIABLE MAY NEVER DO

This appendix exists so the staged-binding contract cannot be read as permission
to guess.

- An unbound variable never produces a wrong answer. It produces a documented
  default that is named in the output, or a degradation notice that says what
  could not be determined and what was therefore not attempted.
- An unbound variable never takes the value that maximizes a score, a weight, a
  rank, a list size or a claim. Where a default is genuinely required, it takes
  the floor of the relevant scale, so that binding it later can only raise a
  result and never lower it.
- An unbound variable never silently widens a population, a scope or a claim.
- An unbound variable never removes a section. The section ships with its
  explanatory row naming the binding that would have filled it.
- An unbound variable never causes a frontline user to be asked an organization
  question. The default is applied, the notice is printed, and the request is
  routed to the binding owner.
- An unbound counterfactual binding never lets a claim ship at achievement
  strength. Every affected claim drops to bounded phrasing.
- The same degradation is announced at the same prominence on every run until it
  is bound. A notice is never quietly downgraded because it has appeared before.

---

# CHANGE LOG: ACCEPTANCE TEST REMEDIATION

What changed in this file after two hostile acceptance tests across five invented
companies, and why.

## Standing rules

- **S9 added.** Precedence runs downhill from evidence to convention, and an
  unbound value never overrides a bound one. An unbound deferred entity-to-
  benchmark map was routing every figure in a business to the floor rung,
  overriding a rung the organization had bound at ignition as its primary
  control. The rule that forbids this existed nowhere.

## Variables added: 11

| Variable | State | Answers | Why |
|---|---|---|---|
| UNIT_LEVEL_KEY | DEFERRED | R1 D3, R2 D4 | Nothing related the unit of business to the scope hierarchy, so an interview could accept a containment chain and a unit noun that were incompatible, and produce a one-row artifact in which every gate passed. Deferred rather than ignition because it is detectable from the data. |
| MIN_POPULATION_FOR_RANKING | DEFERRED | R1 D3, R2 D4 | The bundle declared a one or two unit scope needed no special rule. |
| COUNTERFACTUAL_RUNG_SCOPES | DEFERRED | R2 D5 | Rung availability was a single organization-wide list with no way to say a part of the business cannot produce one of them. This is the structural cause of the cold-start defect. |
| COLD_START_MIN_PRIOR_SHARE | DEFERRED | R2 D5 | The threshold that separates a cold unit inside a warm population from a cold population. |
| ADDRESSABLE_SELF_SHARE_CEILING | DEFERRED | R2 D5 | The independence test needs a threshold at which a denominator is judged to be one the writer is building. |
| JOIN_UNIQUENESS_FLOOR | DEFERRED | R1 D9, R2 D3 | Named by doctrine, defined nowhere. |
| UNRESOLVED_STOP_COUNT | DEFERRED | R1 D9, R2 D3 | Named by doctrine, defined nowhere, and it gates a stop. |
| JOIN_OVERLAP_FLOOR | CONDITIONAL | R1 D1 and D9, R2 D3 | Named by doctrine, defined nowhere, and it gates a hard stop. Now conditional on a FIXED population and explicitly never applied under FLOW, because a healthy pipeline fails any reasonable overlap floor. |
| PEER_SET_IS_EXTERNAL | CONDITIONAL | R1 D7 | A published external comparison group is the most likely real answer at any regulated or benchmarked business and could not be bound at all. |
| EXTERNAL_PEER_SET_SOURCE | CONDITIONAL | R1 D7 | The publication and cadence for that group. A group refreshed annually and read quarterly is stale for three quarters of the year. |
| DELIVERABLE_CONTAINER_REQUIRED | DEFERRED | R1 D18 | The capability probe resolved the workbook-versus-markdown choice by appealing to a binding that had no name, which is what standing rule S1 exists to prevent. |

## Variables amended: 4

| Variable | Change | Why |
|---|---|---|
| POPULATION_SHAPE | Now a KEYED SET of declared populations, each with its own mode and unit. Its ignition validation now requires only a key, a mode and a unit noun, with every other field conditional on mode and bound at first need. | The old validation demanded three fields the ignition interview explicitly refuses to collect, so the one state that blocks could never be satisfied. And many businesses are genuinely both a roster and a pipeline; forcing one answer was itself the error. |
| COUNTERFACTUAL_AVAILABLE_RUNGS | Now explicitly the organization-wide DEFAULT, overridden by any population-scoped entry, and a rung named here whose own definition is unbound is not available. | Rung availability was inherited organization-wide by a population that could not produce it. |
| PEER_SET_LEVEL_DEFAULT | Validation now requires the level to be STRICTLY COARSER than the requester's own at run time, or the literal EXTERNAL. A resolved level at or finer than the requester's own is discarded, never used. | An executive's peer set resolved to her own subordinate facilities, so she was benchmarked against herself. |
| ENTITY_BENCHMARK_MAP, SECTION A1 | Its absence now removes rungs 1 and 2 only, and figures fall to the highest remaining BOUND rung rather than to the floor. | The old default silently overrode an ignition binding. |

## Appendix restructured

- SECTION A1 or A2 is now **A1, deferred**, and a new **A2, conditional** carries the
  trigger, the documented default once triggered, and the exact notice for all 41
  conditional variables, including the five POPULATION_SHAPE sub-keys. Until A2
  existed, forty-one variables could trigger with no default and no notice, which
  is the governing rule failing at the place it matters most. Coverage is now
  exact in both directions, with no orphans either way. The row counts themselves
  live in the COUNTS block and are stated nowhere else, including here.

## What did NOT change, deliberately

- The ignition set stays at 11 ORG variables. Two candidates were considered and
  deferred instead: UNIT_LEVEL_KEY, because it is detectable from the data, and
  the rung-definition variables, because a rung named but undefined is now struck
  rather than guessed, which is a safe default rather than a blocking one.
- SECTION B was not weakened. Every fix above is a place where the file failed to
  live up to that page, not a place where the page was wrong.

## Second remediation pass: shape dependence and the gate convention

Raised by the planning skill agent. Once shape became a property of the
population being scored rather than of the company (SD-POP-23), every documented
default and notice that silently assumed a fixed roster became a place where the
notice and the behaviour disagree.

### Rows rewritten for shape dependence: 13

Twelve in SECTION A1: EXCEPTION_FLAGS, GAP_TERM_DEFINITIONS,
POPULATION_CENSUS_INTERVAL, RECENCY_FLOOR_DAYS, RECENCY_MEDIAN_FACTOR,
ALERT_WARN_DAYS, ALERT_OVERDUE_DAYS, RECENCY_LAG_DISCLAIMER,
UNIT_ACTIONABLE_NOW_CONCEPT, UNIT_ACTIONABLE_NOW_VALUES, MSG_ALERT_LINE,
HDR_LAST_ENGAGEMENT. One in SECTION A2: PEER_SET_ANCHOR_PERIOD.

Each now states its default and its notice per shape, and each notice names the
shape the run actually used, so a reader can never be told the run evaluated one
set of flags when it evaluated another.

The main-table rows for EXCEPTION_FLAGS and GAP_TERM_DEFINITIONS were also
rewritten: both are now keyed by shape, and both carry the flow seeds alongside
the inherited fixed ones.

Deliberately NOT rewritten: ALERT_SCALES and ALERT_COUNT_POPULATION. Both state a
relationship rather than a measurement, that the alert is flat while the
membership flag scales, and that counts are taken over the whole population. Both
statements are true in either shape and adding a branch would imply a difference
that does not exist.

### HARD_GATES now describes exactly the six-field, four-group shape

The schema entry names four keyed groups and no others, requires every gate
record to carry key, group, fires_at, behaviour, reads and doctrine, permits
exactly two behaviour values, requires every `reads` name to exist in this
schema, and states that the count per group lives in the taxonomy and nowhere
else in the bundle. The SECTION A1 default now supplies the standing set in that
form.

**AND THIS PARAGRAPH NO LONGER STATES A COUNT, BECAUSE IT IS NOT ALLOWED TO.** An
earlier version of this sentence gave a per-group tally and a total. That broke
the convention it was written to describe, in the file that owns the convention:
C5 forbids a skill file from stating the count of any group's members, and C8
forbids this schema from stating membership or a count. It was also WRONG against
the bodies it described, and because this change log is reproduced byte-identically
into every collapsed skill file, the wrong count shipped once per skill rather than
once. A count restated outside its taxonomy is a second source of truth that
nothing updates, which is precisely why the convention exists. **The number of
gates in any group is read from HARD_GATES at run time and is stated nowhere else,
including here, including in prose, including in a change log.**

Two conditions are explicitly declared NOT to be gates, because both had drifted
toward being treated as ones: reading the published standard, per SD-SRC-21, and
a population below MIN_POPULATION_FOR_RANKING, per SD-POP-25. The second is worth
naming because MIN_POPULATION_FOR_RANKING is read by the skills: it changes what
the output is, and it never ends the run. A gate record reading it would be a
category error, not a threshold disagreement.

## Third remediation pass: round 2 regression

### N1, BLOCKER. The schema no longer authors a gate set.

The previous pass put a twelve-gate enumeration into the SECTION A1 default for
HARD_GATES. It disagreed with all three skills in membership, in group placement
and in five of twelve key spellings, and one difference was behavioural rather
than cosmetic: it placed `no_measure_column` in the SHARED group, which stops a
review run at an unbound company. The review skill's no-data path is that skill's
product and must not be blocked by a gate inspecting an artifact it does not
produce, per SD-EFF-37, and the doctrine that justifies the gate does not carry
REVIEW. That is the defect the whole convention was written to close, moved from
three skill files into this one.

The entry now owns the record shape, the four group names, the two permitted
behaviour values and the rule that every `reads` name must exist in this schema,
and owns nothing else. Membership is declared by the skills. The default names
only the shared core keys, verified character by character against
period-planning 20.1.2: source_unreadable, record_count_zero, scope_unresolvable,
formatting_unverifiable, character_gate_unrunnable.

### N4, MAJOR. The POPULATION_SHAPE shape block is now a keyed set.

The row said keyed set and validated a key; the shape block above it, which the
file's own reading convention makes the authority an implementer builds from,
described one object with no key. Every entry now carries a key, its own mode,
its own unit nouns and its own unit_level_key, and every mode-conditional field
is conditional on THAT population's mode. UNIT_LEVEL_KEY, FLOW_OPEN_DEFINITION,
FLOW_COHORT_BASIS and FIXED_ROSTER_CHURN_TOLERANCE were reworded to match.

### Report 1 D8, MAJOR, previously not attempted. Binding authority is now computable.

ROLE_LADDER gains `binding_authority`, defaulting to NONE for every role and ALL
for the binding owner, with an SECTION A1 row. Interview 2.2 C1 now tests it.
Without it the right-answerer constraint could not be evaluated at all, and a
constraint that cannot be evaluated has failed, so no deferred question could ever
fire for anybody. See the interview change log for the matching correction to the
claim that the config fills itself in through everyone's use.

### N7 and N9, MINOR. Counts and cross-references.

- An appendix row count disagreed with the number of variables it covered,
  because the appendices also carry rows for taxonomy SUB-KEYS. Corrected, and the
  variable count and the appendix row count are now stated separately in the COUNTS
  block so the next reader can see why they differ. **The figures themselves are
  not repeated here**, per the maintainer note: this entry records what was wrong
  and why, and the COUNTS block holds the numbers.
- The POPULATION_SHAPE validation cited Q-H1, which binds the source file's name
  and locations and no population sub-key. Deleted; Q-D3 is the binding path.

**A standing note for maintainers, because this class of error has now recurred
in three consecutive passes.** Three numbers move whenever a variable or a rule is
added: the COUNTS table here, the A1 and A2 row counts here, and any count of
these stated in a skill file. Re-derive them mechanically after every change
rather than editing the one you happened to touch.

## Appendix C: Intentional non-variables

Two classes of name in this bundle are written in upper case but are NOT schema
variables. Both will trip any automated sweep looking for a variable that is read
as bound configuration but defined nowhere, which is a defect class that has
recurred three times in this bundle and is worth checking for. Neither of these is
that defect. Both are recorded here so the distinction is documented rather than
rediscovered.

### C.1 The counterfactual rung names

SHARE_OF_ADDRESSABLE, MATCHED_CONTROL, PEER_DISTRIBUTION, PLAN_ATTAINMENT,
OWN_PRIOR_RUN_RATE, BARE_DENOMINATOR.

These are the six fixed rungs of COUNTERFACTUAL_LADDER, specified in Group 6. The
ladder itself is not configurable: an organization binds WHICH rungs are available
to it and WHICH is its default, through COUNTERFACTUAL_AVAILABLE_RUNGS and
COUNTERFACTUAL_DEFAULT_RUNG, but it cannot add a rung, rename one, or reorder them.
The names are therefore constants of the method, not values of the binding.

Owning file: reference/schema/ Group 6.

### C.2 The capability names

**THE ROSTER IS NOT RESTATED HERE. THE ONE COPY IN THIS FILE IS APPENDIX A3.2**,
which is itself a copy of reference/capability-probe.md 1.3. This change-log entry carried a
six-name subset of it, which was a second list that nothing updated, and it was
already stale by two capabilities when it was found.

These are probe capabilities, not organization bindings. They describe what the
running agent can do, which is discovered at run start and varies by environment
rather than by employer. Nothing about them is bound during the interview.

Owning file: reference/capability-probe.md section 1.3.

### C.3 The rule

A name belongs in this appendix only when it is a constant of the method or a
property of the runtime. Anything that varies by employer is a variable and belongs
in the main table with a tier, a default and a degradation notice. When in doubt it
is a variable: the cost of an unnecessary binding is one interview question, and the
cost of a missing one is a value read as configuration and defined nowhere.

## Fourth pass, final regression

- **The HARD_GATES cell no longer asserts a rule and breaks it in the same
  breath.** It said the schema states no membership and no count, then stated the
  count. The clause now reads that the shared core keys are REPRODUCED FROM the
  planning skill and are authoritative there, so the pointer survives and the
  skill is the single authority on membership. No key changed: all five were
  verified character by character against period-planning 20.1.2.
- **UNIT_LEVEL_KEY's SECTION A1 default carries the tie-break, N10.** Finest
  matching level where more than one matches, and no binding error asserted over a
  population of one record.
- **SECTION A3 records the intentional non-variables.** The six counterfactual
  rung names, owned by Group 6, and the fifteen capability names, owned by
  reference/capability-probe.md 1.3, are upper-case tokens that are not variables and have
  no default and no notice by design. A3.3 states the test a sweep should apply so
  they are not rediscovered as defects on every pass.

## Fifth pass, live end-to-end run against an undescribed file

A first run of the planning skill was done by an agent that had never seen the
bundle, against a real file of a couple of hundred rows that nobody had
described, at two altitudes. Twelve findings. This file answers ten of them.

- **IGNITION IS NOW STATED AS A QUALITY STATE, NOT A GATE.** The state table read
  as though a run could not be produced before the ignition set was bound, while
  two other files in the bundle describe a provisional run in detail. A reader
  spent twenty minutes deciding whether a run may start at all. The table now says
  the run does not stop, it degrades to a PROVISIONAL RUN, and that no state in
  this schema stops a run: the only things that stop a run are the members of
  HARD_GATES, and no binding state is one of them.
- **ROLE_LADDER.binding_authority gains a fallback, which closes the
  binding-owner trap.** Where BINDING_OWNER_NAME is unbound, authority had
  resolved to NONE for every role, which made the deferred-request constraint C1
  unsatisfiable and switched the entire progressive-binding mechanism off for the
  life of the deployment. The fallback is that the MOST SENIOR ROLE in
  ROLE_LADDER holds `ALL` until an owner is named, with the A1 row saying so and
  saying what it costs.
- **ROLE_LADDER.claim_tier and ROLE_LADDER.altitude_ceiling gain A1 rows.** Both
  were named as required and neither had a documented default or a degradation
  notice, so a run that could not read them had nothing to print. claim_tier now
  derives from UNIT_LEVEL_KEY plus ladder order.
- **DELIVERABLE_LINES validation and its A1 default were rewritten.** The senior
  pair is the LARGER pair in rows and the list is never proportional to span. See
  the note on which principle governs, below.
- **CLOSE_WEIGHTS gains a fifth band and the ladder is now exhaustive.** A date
  after the next window but inside the near horizon, CLOSE_HORIZON_DAYS, default 90,
  fell in no band at all, so an implementation either dropped those items or
  banded them to the floor on its own judgment. The new band is 0.35.
- **SOURCE_BOOST_NONE is added, at 1.0.** The multiplier for an item that no
  source named was defined nowhere, which on a run with no reachable message store
  and no document store is EVERY item.
- **Seven variables moved from OPTIONAL to DEFERRED with A1 rows.**
  HDR_ITEM_COUNT, HDR_PEER_NORM, HDR_ITEM_GAP, HDR_EST_UPSIDE and HDR_PLAY were
  named as required headers by a skill and appeared in no group here.
  CHAR_WIDTH_FACTOR, now 0.88, and LINE_HEIGHT_PADDING_PT, now 15, were used
  inside an arithmetic formula with no value anywhere.
- **MSG_ALERT_LINE gains a third form.** A check whose column did not resolve
  prints NOT EVALUATED with the reason and the column named, never a zero. A zero
  asserts that nothing is overdue when nothing was looked at.
- **SPAN_BLOCK_POSITION now agrees with IDENTITY_BLOCK_COLUMNS.** The two
  variables described one column order and gave two answers. The default is now
  the position IDENTITY_BLOCK_COLUMNS places the scope columns in, and where they
  ever disagree, IDENTITY_BLOCK_COLUMNS governs. The empty-span case is stated.
- **COLD_START_MIN_PRIOR_SHARE now says the share is UNDEFINED, not zero, where
  no prior-period column resolved.** A single-snapshot export, which is what
  almost every first run is handed, was marking nearly every population COLD.
- **Group 5 names ONE shape-inference procedure, SD-POP-24, and no other.**
- **forbidden_neighbours is typed: it holds concept keys and nothing else.**

**Which principle governs the list sizes, stated plainly.** The ORIGINAL design
wins: the senior line keeps the LARGER pair. "Shorter as scope widens" was always
about the list as a SHARE of span, never as absolute rows. Ten items over a
hundred units is a tenth of a reader's span; twenty over several thousand is a
fraction of one percent, and the second is by far the shorter list to the person
holding it. The alternative reading would hand a senior leader fewer rows than a
frontline reader off the same file, which no version of this method has ever
done, and it would contradict the standing sizes in the same table row that states
them. SD-RNK-09, the DELIVERABLE_LINES validation and its degradation notice were
all rewritten to say the same thing.

## Sixth pass, confirmation run at three altitudes

- **REGRESSION FIXED FIRST: binding authority is now ADDITIVE, not a
  replacement.** The previous pass granted the most senior role `ALL` only where
  the owner name was UNBOUND. That ran backwards. At any organization whose
  configuration owner sits in operations, IT, enablement or any function that is
  not an entry on the operating role ladder, which is most of them, naming an
  owner moved the senior role from `ALL` to `NONE`, so doing the right thing at
  ignition made progressive binding STRICTLY LESS LIKELY to fire than skipping it.
  The default is now a UNION of two standing grants: the named owner holds `ALL`
  whenever a name is recorded, AND the most senior role holds `ALL` whether or not
  an owner is named. Only an explicit per-role binding may narrow either, and no
  run may narrow either. SD-CTR-25 states the invariant and carries the
  MONOTONICITY TEST to be run before any change to an authority default ships:
  binding one more fact must never shrink the set of questions a person can
  answer.
- **The status-column exclusion has a real default.** A resolved column supplies a
  CONCEPT; the VALUES are a separate binding, and the gap between them put a
  prospect at rank one of a working plan, disclosed three times and still not fit
  to hand anybody. UNIT_ACTIONABLE_NOW_VALUES now defaults, where the concept
  RESOLVED, to matching UNIT_NOT_ACTIONABLE_SEED_VALUES, a new seed list of
  generic non-workable statuses, under three mandatory guards: the STAGE guard, so
  an exclusion can never delete a stage under FLOW; the MAJORITY guard, bounded by
  the new EXCLUSION_SANITY_CEILING at 0.50, so a default that would remove most of
  a population is refused; and the NAMING guard, so every distinct value is
  printed as EXCLUDED or KEPT with counts. Where the concept did NOT resolve there
  is still no exclusion, because there is no column to read. SD-POP-28 carries the
  asymmetry argument: the two errors are not symmetric, so the default is not
  neutral.
- **IGNITION COMPLETENESS is now defined, and a fully answered interview produces
  a non-provisional run.** A sub-field is satisfied when it is ANSWERED, DERIVED or
  DEFAULTED, and a DERIVED sub-field is NOT an unbound sub-field. Nine ROLE_LADDER
  sub-keys gained A1 rows with derivations, including claim_tier, which is derived
  from UNIT_LEVEL_KEY and the ladder order exactly as the first tester proposed:
  the role at or immediately coarser than the unit level is DIRECT, every coarser
  role is AGGREGATE. POPULATION_SHAPE.mode gained an A2 row deriving it from
  SD-POP-24. Every derived value is read back to the answerer before the interview
  closes, which is the only circumstance in which a medium-confidence value may be
  written to an org config. SD-CTR-26 states the invariant.
- **CLOSE_HORIZON_DAYS is added at 90 and every close band is anchored on the
  PLANNED window, never the run date.** The two anchors moved 8 percent of a real
  population between the two lowest bands, which reorders the published list.
- **YEAR_PLAUSIBLE_RANGE is added.** A column of bare four-digit years classified
  as an identifier before the date rung was reached, which silently disabled the
  cold-start entry test.

**COUNTS ARE DERIVED MECHANICALLY AND VERIFIED IN BOTH DIRECTIONS.** The figures
themselves live in the COUNTS block and are not repeated in this change log, which
is the rule this entry exists to record. A1 holds one row per DEFERRED variable
plus one per sub-key of the two ignition taxonomies; A2 holds one per CONDITIONAL
variable;
being the 41 CONDITIONAL variables plus 8 POPULATION_SHAPE sub-keys. No DEFERRED variable lacks an A1 row and no CONDITIONAL variable lacks
an A2 row. The previously stated counts had drifted and are corrected; do not
adjust these by hand.

## Seventh pass, final acceptance run at three altitudes

- **UNIT_NOT_ACTIONABLE_SEED_VALUES now covers THREE families, and the match rule
  changed with it.** The old set held terminal states and never-started states and
  missed every DECIDED EXIT NOT YET COMPLETE, which is the family that reads as
  active to a naive matcher. Whole-string prefix matching could not reach it from
  either direction: a status meaning a pending non-renewal starts with none of the
  seed entries and none of them starts with it. Eleven such units ranked at full
  weight and two sat inside a published top twenty. The seed set now names the
  decided-exit family explicitly, and new UNIT_NOT_ACTIONABLE_MATCH_RULE makes the
  comparison TOKEN-WISE and BIDIRECTIONAL. Verified against the false-positive
  traps that matter: a status meaning a renewal is in progress and workable matches
  nothing, because the negating token is what the seed entry requires. Bare single
  tokens that would prefix an ordinary word were removed from the set.
- **ROLE_LADDER.scope_level is anchored at BOTH ends, and the junior anchor is the
  finest OWNABLE level, not the finest level.** Nobody owns one unit of business as
  their scope: the unit is the row. The old single anchor put the most junior role
  on the unit level and shifted every role one rung narrow, leaving the top level
  unowned, the top of the house owning a mid level, and a role that leads people
  who work units resolving as a role that works units. The tell was that the
  derivation's own fallback was right where the derivation was wrong. SD-CTR-27
  carries the rule and the diagnosis.
- **ROLE_LADDER.claim_tier follows the corrected anchor.** EXACTLY ONE level is
  DIRECT, the finest ownable level, and every coarser level is AGGREGATE without
  exception. The derivation and the fallback are now required to agree, and where
  they differ the fallback stands and the disagreement is recorded.
- **IDENTIFIER_MIN_WIDTH is added**, so a column of digits is separated from a code
  by distinctness or width rather than by length alone. Without it a count of two
  or three items classified as an identifier.
- **EXCEPTION_FLAGS defaults now carry explicit per-flag weights**, and
  PRIORITY_BAND_THRESHOLDS defaults are expressed as SHARES OF THE ATTAINABLE
  MAXIMUM rather than as absolute scores. Absolute thresholds calibrated for a
  four-flag set were unreachable on a file where one flag evaluated, so the top
  band silently ceased to exist and the exception section shipped empty in three
  consecutive runs. An absolute binding is still legal and is now REJECTED AT
  VALIDATION where its top band exceeds the attainable maximum. A flag that could
  not be evaluated is removed from the attainable maximum, never counted as zero.
- **EXCEPTION_ALERT_RECONCILIATION is added.** Where the alert line is non-zero and
  the exception section is empty, the empty section carries one row naming both
  counts, both thresholds and why two correct measures disagree. This does not
  force them to agree, which SD-EXC-05 forbids; it forces the workbook to explain
  itself rather than stating two contradictory things on one page.

Counts re-derived mechanically. The figures themselves live in the COUNTS block
and are not restated here. What this pass verified is the INVARIANT: no DEFERRED
variable without an A1 row, and no CONDITIONAL variable without an A2 row.

## Eighth pass, release acceptance run

- **The not-workable match rule is rebuilt on WHOLE-TOKEN PHRASES with no prefix
  matching and no character-length threshold anywhere.** The four-character floor
  failed in both directions at once, which is what proves the threshold was the
  wrong instrument rather than the wrong number. Too loose: a four-letter word
  sitting inside a longer seed entry matched an ordinary word in a live status, so
  a status meaning an active renewal was due would have been EXCLUDED and a
  workable account silently removed. Too tight: the negating token in every
  decided-exit phrase is three characters, so a literal reading matched nothing and
  the headline exclusion did not fire at all. Raising the floor worsens the second
  and lowering it worsens the first. The rule now normalizes, tests for a
  CONTIGUOUS RUN of exactly equal tokens, refuses a one-token match where the cell
  carries a live-relationship marker from the new UNIT_ACTIONABLE_ACTIVE_MARKERS,
  and PRINTS every refusal. Morphological variants are listed rather than derived.
- **The seed set lost the entries that caused the over-fire**, each with its reason
  recorded in a DELIBERATELY ABSENT note: the bare word for a quote, because a
  quoted renewal is a live renewal; the bare word for an application, for the same
  reason; the bare word for a hold, because the qualified forms cover it; and any
  bare word naming a target, because a target account is one somebody wants worked.
- **APPENDIX A4 prints the verification instead of claiming it.** The previous
  notice asserted three traps had been verified and failed one of them. The rule is
  now run against 34 status strings parsed out of this file's own rows, and the
  results are printed. Zero failures.
- **GAP_TERM_DEFINITIONS names a SOURCE CONCEPT and a TEST for every term**, in both
  shapes. A term that names neither is a word rather than a wiring. Coverage absent
  additionally carries a PROHIBITION: it is never sourced from a recency date,
  because that field already feeds the staleness flag and SD-WGT-19 forbids
  counting one signal twice. Where its concept does not resolve it is NOT EVALUATED
  and says so, rather than falling back.
- **HDR_DIRECTIVE_STATUS is added.** The direction family's fourth column was
  described in prose, so it had no byte-identity guarantee under SD-CTR-09 and a
  reader had to invent its header string.
- **CONTEXT_GROUPER_MAX_DISTINCT and FILE_QUESTION_BATCH_CAP are added**, supporting
  the context ordering rule and the file-question batch respectively.

Counts re-derived mechanically. The figures themselves live in the COUNTS block
and are not restated here. What this pass verified is the INVARIANT: no DEFERRED
variable without an A1 row, and no CONDITIONAL variable without an A2 row.

## Ninth pass, ship-or-no-ship run

- **UNIT_NOT_ACTIONABLE_SEED_VALUES now has ONE list in ONE place.** Its GROUP 5
  EXAMPLE cell held a short illustrative list while SECTION A1 held the full one,
  and five of the thirty-four verified cases changed verdict depending on which a
  reader used. The example cell now names where the list lives and shows none of
  it, and APPENDIX A4 says explicitly that it parses the SECTION A1 rows. An EXAMPLE
  column that partially restates a documented default is a second default.
- **The HARD_GATES change-log sentence no longer states a count.** It gave a
  per-group tally and a total, which broke C5 and C8 in the very file that owns
  them, was wrong against the bodies it described, and shipped once per skill
  because this change log is reproduced byte-identically into every collapsed
  file. Fixing it here fixes all three, since no skill source carries the sentence.
  The number of gates in any group is read from HARD_GATES and stated nowhere else,
  including in prose and including in a change log.
- **Every count restated outside the COUNTS block is gone, and the maintainer note
  now forbids restating them at all.** Two change logs carried stale row counts and
  a sibling skill described this file with a stale variable count. Every drift
  found in six passes has been a RESTATEMENT rather than the block itself, so the
  rule is now that this block is the only place any of these figures appears:
  change logs record what changed and why and state no totals, and another file
  describing this one names the invariant rather than the number. The note also
  carries the three-line sweep to run after any table change.
- **RIGHT_ALIGN_COLUMNS covers every numeric column the contract can emit**,
  including the measure percentile, the must-close count, the four derived-family
  numerics and every carried context column whose SHAPE TOKEN is numeric. Closed
  means nothing is inferred into it AT RUN TIME; it never meant leaving the list
  short, and a number left aligned beside a right-aligned one reads to a person as
  a broken export. A carried context column qualifies on its shape token, which the
  parse stage already established, not on a guess about its header.
- **PERCENTILE_DEFINITION carries the endpoint wording.** The top of a ranked list
  is at exactly 1.0 and is printed unchanged, because rounding it down is a lie and
  capping it breaks the reconciliation. The sentence beside it says the plain thing
  instead. SD-LNG-12.

## Tenth pass, final ship run

- **The malformed SECTION A1 row is fixed, and every table in the bundle is now
  checked.** EXCEPTION_ALERT_RECONCILIATION carried FOUR cells in a THREE-column
  table, an A2-shaped trigger cell inside an A1 table, so a run reading by column
  position printed the trigger where the default belongs, a rule where the notice
  belongs, and dropped the real notice entirely. That is the row this run had to
  print, because the exceptions section shipped empty beside a non-zero alert on
  both artifacts. The trigger is now folded into the documented-default cell, where
  an "applies when" condition belongs in a three-column appendix.
- **CELL-COUNT VALIDATION is added to the standing validator and is run over the
  whole bundle, not only A1 and A2.** A malformed row in a table read by position
  is SILENT, which is why this one survived several rounds of review: nothing looks
  wrong until a run reads the wrong cell. The check compares every row against the
  header of the table it is in, restarting at each header rather than assuming one
  table per section.
- **RIGHT_ALIGN_COLUMNS gains a MEMBERSHIP RULE that is total over the shape
  tokens.** Right align COUNT_OR_MEASURE, RATE_OR_PROPORTION and DATE; left align
  IDENTIFIER_OR_CODE, STATUS_OR_CATEGORY, BOOLEAN_LIKE and FREE_TEXT. The seven
  tokens are exhaustive, so a numeric column added later joins the list by
  construction rather than by someone remembering. CLOSED now explicitly means no
  inference AT RUN TIME, which is a different claim from the list being assembled
  by memory, and the two were being conflated.
- **Five HDR_ variables the contract uses were defined nowhere and are added:**
  HDR_CLOSE_WEIGHT, HDR_CLOSE_STATE, HDR_COMMITMENT_DATE, and HDR_SPAN_PREFIX with
  HDR_SPAN_SUFFIX for the span columns. The span headers are DERIVED from
  SCOPE_LEVELS rather than enumerated, which is why they are two variables and not
  one per level, so a six-level hierarchy needs no new bindings. Verified: every
  HDR_ variable the planning skill references now exists in this schema, and every
  HDR_ variable named in the right-align row exists.
- **The COUNTS block is re-derived, and the by-type line now carries its own
  reconciliation.** It summed to 407 against a total of 419 in the same block. It
  now states that the four types sum to the total and that a by-type line failing
  to reconcile is a defect in the block rather than a rounding.
- **The remaining count restatements are gone**, including one in an older change
  log entry, which now records what was wrong and why while the COUNTS block holds
  the numbers.
- **OPERATING_WINDOW_DERIVATION_RULE gains the COVERING INVARIANT.** A thirty-day
  nominal length anchored on the first of a calendar month left the thirty-first
  outside the window named for that month, so a commitment on the last day of the
  month being planned banded as the NEXT window. The period NAME now selects the
  derivation: a name denoting a calendar unit makes the window that whole unit,
  first day to last, and the nominal length is used for horizon arithmetic only. A
  derivation that cannot satisfy the invariant is a binding error, never resolved by
  shortening the month. SD-SCO-17.

## Eleventh pass, review and scorecard acceptance runs

- **PEER_SET_LEVEL_DEFAULT now says that A STATED PEER COUNT OUTRANKS THE
  ONE-STEP-COARSER DERIVATION.** The interview collected a peer COUNT and never a
  peer LEVEL, and the derivation then contradicted the count the interview had just
  taken. That is not cosmetic: it decides whether a peer comparison happens at all,
  and at a real organization it was the difference between a five-way comparison and
  none. Where only a count was given, the level is derived FROM the count, recorded
  as such, and read back.
- **DEADBAND is now a MAPPING PER RUNG with each band's UNIT NAMED.** A single
  scalar defined as being "in the unit of that delta" named four different
  quantities depending on which rung read it: percentage points of share, of the
  treated-minus-control gap, of growth, and percent of target. A band read in the
  wrong unit either labels noise as a result or silences a real one. Rung 6 has no
  band, stated as an absence rather than left blank.
- **Rung 4, plan attainment, gains its own band in PERCENT OF TARGET, and it never
  depends on a peer spread.** Its absence produced the wrong silence at the top of
  the organization: the most senior reader has no peers, so no band was computable,
  so NOTHING they were shown carried a label, including a headline attainment and
  their single worst failure. The target is the comparison; no peer is needed to
  say that a figure well short of it is short.
- **REASON_CODE_SET gains a GAP family and a RETIRED family, and the variable now
  carries a COVERAGE VALIDATION.** The set seeded codes for two rare states and
  none for the state that is the scorecard's entire subject, so every gap cell on
  an ordinary run came back unmapped, hundreds of times. The validation runs from
  the STATES to the SET: every non-pass state in CLASSIFICATION_LABELS must have at
  least one code that applies to it. Verified: all four non-pass states are now
  covered. The retired codes state their implied action as explicitly NONE and
  their resolver as NOBODY, because a retired cell that looks actionable sends
  somebody to do work that no longer exists.
- **TAB_CONTRACT and DELIVERABLE_NAME are now PER SKILL.** Both carried the planning
  skill's content as a shared default, so a literal implementer running the
  scorecard shipped a document titled and shaped like a work plan. TAB_CONTRACT is
  a keyed set with an ordered list per skill; DELIVERABLE_NAME is a mapping and a
  bare string is now rejected at validation.
- **COMPLIANCE_FAILS_CLOSED_ON now names the ROLE rather than one skill's noun.**
  Its default was "priorities", which is the planning skill's word, in a variable
  the scorecard also reads, where it read as an instruction to hold back something
  that document does not have. It now says THE VALIDATED ITEMS, named by the
  running skill.

Counts re-derived mechanically. The figures live in the COUNTS block and are not
restated here; what this pass verified is the invariant, that no DEFERRED variable
lacks an A1 row and no CONDITIONAL variable lacks an A2 row.

## Twelfth pass, confirmation runs on both remaining skills

- **The not-workable exclusion is settled in ONE row, and the test is whether a
  COLUMN RESOLVED, never whether a BINDING EXISTS.** Two SECTION A1 rows disagreed,
  and the resolution lived only in reference/field-resolution.md F5.1b by implication, in a
  third file. That is intolerable for a rule deciding POPULATION MEMBERSHIP: two
  readings produce two populations and every number differs. The distinction being
  lost was that an unbound CONCEPT is not the same as NO COLUMN RESOLVING, since a
  run resolves the column from the seed dictionary whether or not the organization
  ever bound it. The UNIT_ACTIONABLE_NOW_VALUES row now holds the whole rule; the
  UNIT_ACTIONABLE_NOW_CONCEPT row states what it governs and cites it; and F5.1b
  says explicitly that it does not settle the question.
- **REVIEW mode gets its own reading of the exclusion, which it did not have.** See
  SD-POP-30 and the decision recorded below.
- **Every ignition variable now carries its SPECIFIC unbound consequence, in a
  third column of the ignition table, and that column is the only statement of it.**
  The binding-states table gives the GENERIC consequence, the provisional label. Each
  variable's specific consequence had no home in this schema, so it was written into
  the interview instead, where it contradicted the generic one: one file said stamp
  the run provisional and the other said cap claim strength, and two readers produced
  two different artifacts off one binding state. **Both consequences apply and they
  are not alternatives:** the generic one is what the artifact SAYS, the specific one
  is what the run DOES. All eleven are now stated here and cited elsewhere.

## Thirteenth pass, the universal output contract

- **reference/output-contract.md is new and is the ONE statement of the output contract.** The
  formatting elements had survived here and in the skills only as passing mentions,
  so nothing enforced them: a scorecard shipped with no autofilter on any sheet, no
  rank column on its main sheet, no consolidated reason column and no cap, and a
  planning workbook put a title banner in row 1 and pushed its headers to rows 4
  through 6. Every one of those violated a rule the bundle already contained in
  prose. Prose is not a contract.
- **FORMATTING_ELEMENTS no longer lists its members here.** The members and their
  standards live in the contract and nowhere else, and this entry says so. An element
  list restated outside the contract is how the elements drifted the first time.
- **Twelve variables added**, all named by the contract and none of which existed:
  OUTPUT_MEDIUM, keyed per skill so a review is a document and a worklist is a
  spreadsheet; CARET_ALLOWANCE_CHARS, COLUMN_WIDTH_MAX_CHARS, HEADER_MAX_LINES and
  LINE_HEIGHT_PT for the computed widths and heights; NARRATIVE_WIDTH_MIN_UNITS and
  NARRATIVE_WIDTH_MAX_UNITS; ALERT_BAND_THRESHOLDS; UNIT_NOUN_SINGULAR and
  UNIT_NOUN_PLURAL, defaulting to Account and Accounts; and HDR_RANK_REASON.
  Verified: every variable the contract names now resolves in this schema.

## Fifteenth pass, seven requests from the three skill agents

- **HDR_DIRECTIVE_STATUS gains `applied as an assignment`, a fifth value.** The
  planning skill now resolves the actor of a direction, and a direction applied to
  a row the reader only oversees was being written as `recorded, not applied`,
  which is false: it was applied, as an assignment. The states-to-set validation
  under S10 is written out with it.
- **MOVING_GROUND_SHORT_FORM and MOVING_GROUND_STATEMENT are new.** The review
  skill names the ground in full in two places and carries a short form inside
  every claim, so no claim can travel into a destination system without its ground.
  Both were composed fresh per run, which is the class of thing this schema binds.
  The short form's derivation is stated once, in its A1 row, and fails honestly
  rather than producing a word that names nothing.
- **FIELD_BUDGET_SPLIT's A2 row now carries the zero allocation and the release as
  arithmetic**, including the rounding and where the remainder goes, so two
  implementations split a released budget identically. A component with no source
  is allocated zero and a description is never written to fill a budget.
- **COLOR_STATUS_GAP and COLOR_STATUS_UNASSESSABLE are new, and the PALETTE
  SEPARATION RULE is stated once in Group 16 with an arithmetic test.** Until they
  existed those two states carried no fill at all. The rule requires eight points of
  greyscale separation between all six fills because these workbooks are printed and
  photocopied, and its first run caught a live collision in this file's own
  defaults: the approaching band and the not-scored fill were four tenths of a point
  apart and identical on paper. COLOR_STATUS_NOT_SCORED's default moved for that
  reason.
- **PASS_QUALIFIER_VOCABULARY is new.** A pass qualified only by a legend is an
  unqualified pass in the cell, and the two qualifiers could not live in
  REASON_CODE_SET, which is closed at four non-pass families.
- **The alignment rule now has THREE classes wherever it is stated**, the third
  being a declared status grid column bounded by CENTRE_ALIGN_MAX_CHARS, and every
  HDR_ row whose alignment sentence assumed two has been corrected with the actual
  outcome for that column rather than a generality.

## Fourteenth pass, the ignition set and the closed vocabularies

- **COUNTERFACTUAL_DEFAULT_RUNG is DERIVED before it is floored, and the whole
  ignition set was swept by the same test.** It is an ignition value that no
  organization document can answer, because it is a question about this method's
  configuration rather than about the business. A run that bound three rungs from
  the documents, all of which computed, then shipped every claim at floor wording
  because the one unanswerable value was unbound: an unbound ignition value
  deleting the effect of bound ones, which is regression case 15 with the tiers
  swapped and is forbidden by S9. It now derives as the highest available rung
  whose own definition is bound, recorded as DERIVED and read back for correction.
  COUNTERFACTUAL_AVAILABLE_RUNGS gains the matching derivation. Membership of the
  ignition set now turns on three tests rather than one, the second and third being
  answerability from an organization's own documents and proportionality of the
  unbound consequence, and the sweep over all ten members is recorded in the file
  so it can be re-run rather than re-argued.
- **ANONYMITY_FLOOR and MIN_POPULATION_FOR_NORM are no longer one apart with a rule
  that stops in the gap.** An outward walk stops at the first level meeting the
  anonymity floor; the smallest set meeting a floor of four is four; four is below
  a norm floor of five. So the shipped defaults sent every walk to a set that could
  be ranked and could not be compared, and the level-delta band could never fire.
  The defaults are now equal, the validation forbids setting one below the other,
  and the relationship is stated at both variables.
- **URGENCY_VOCABULARY is new, and closes a hole in a closed set.** The urgency
  column was four values with a rule that a passed date carries the overdue value
  only where something is outstanding, so a passed date with nothing outstanding
  had no value it could lawfully take and five units on one run had to be named by
  hand in a legend. The fifth member states that row's truth.
- **CLOSE_WEIGHTS now writes out the map from the nine close states onto its five
  weights**, which was inferable and therefore two implementers' guess, and
  STATUS_VALUES gains a third member for an objective with nothing to judge it
  against, with the rule that a set with no applicable member is reported as one
  rather than resolved by picking the closest value.
- **The SHEET-NAME CONSTRAINT is stated once, in Group 15, with its truncation
  rule**, and MANDATORY_SECTION_LABEL's default is legal as written. The old
  default carried a colon and ran past thirty-one characters, so a literal build
  raised an exception in the workbook engine and produced a file that would not
  open.
- **INCOMPLETE_BANNER_TEXT has two defaults, chosen by a check that already runs.**
  One literal served a draft with a placeholder in it and a complete draft nobody
  had read, so an artifact opened with DO NOT SUBMIT in the title band and then
  said, in the next paragraph the same rule mandates, that everything was real and
  should be read and submitted.
- **TABLE_STYLE_NAME's prose no longer names a different style than its example**,
  and the rule that the example governs a literal string is stated with it.
- **S10 is new, and it is the closed-vocabulary validation generalized.** It was
  run once, on one set, and found a hole; it is now a standing rule naming every
  closed set in this schema and requiring the check to run from the STATES a rule
  can emit to the SET, never the other way round. HDR_DIRECTIVE_STATUS's values
  were the second hole it found: three were named in prose and there was nothing to
  write for a direction that was admitted and could not be evaluated. The values
  are now a closed set of four, stated in one row.
- **Two variables added for procedures that had none:**
  ENTITY_COLUMN_MIN_COVERAGE for finding the column that carries the creditable
  entity, and PROVISIONAL_ADOPTION_MIN_FILL for the first-run adoption route. Two
  more were added by the sweep in the other direction, CENTRE_ALIGN_MAX_CHARS and
  FROZEN_SPAN_MAX_WIDTH: the output contract reads both, a mandatory element gate
  fails where either is missing, and nothing defined them here.

## Sixteenth pass, the grid width bound and the classification fill

- **GRID_MAX_TOTAL_WIDTH is new, and it is the second of two width bounds.**
  FROZEN_SPAN_MAX_WIDTH already bounded the frozen span, and honouring it perfectly
  still left a measured census sheet 749.12 units across, read through the filter one
  column at a time because nobody could traverse it. One bound says what stays on
  screen; this one says how much there is. Its documented default carries the
  measurements it was derived from, in its own row, so that the next person to move
  it has to argue with the arithmetic rather than with a number: 486.43 for a
  well-built grid after the relief ladder, 813.71 for the same grid before it, and
  659 and 749.12 for two workbooks that failed a reader outright. A bound set so high
  that nothing ever trips it is not a bound. The ladder that runs when a sheet
  exceeds it, and the three things that never give while it runs, are stated in
  reference/output-contract.md PART 2.7 and are cited rather than restated.
- **CLASSIFICATION_VOCABULARY is new, and it binds STATES rather than cell values.**
  The output contract permits a fill per state of a declared classification column,
  and nothing here defined the set those fills are keyed on. The distinction that
  makes it usable on a real grid is that a cell value is routinely a state crossed
  with a reason code or a qualifier, so the distinct values run to hundreds while the
  state set stays at five. It is under S10, and S10's roster now names it: the check
  runs from every state a skill can emit to the member that carries it.
- **CLASSIFICATION_FILLS is new, and its default is stated as the arithmetic that
  proves it.** One fill per state, no two states sharing one, disjoint from both
  alert colours, and every pair separated under the palette separation rule, whose
  domain is now the union of the six named fills and every value of this map. The
  greyscale values, their six adjacent separations and the minimum are printed in the
  default itself, so the check is re-runnable by hand and a later edit that breaks it
  is visible without a script.
- **COLOR_STATUS_GAP and COLOR_STATUS_UNASSESSABLE are NOT subsumed, and both rows
  now say so.** They stay the one binding site for their two states and the map cites
  them rather than restating a hex, so a colour is still set in exactly one place.
  RETIRED is the one standing state with no palette variable of its own, so the map
  supplies its value rather than giving it the not-scored grey, which the one-fill-
  per-state rule forbids.

## Seventeenth pass, nine findings from the three skill agents

- **NARRATIVE_WIDTH_MIN_CHARS and NARRATIVE_WIDTH_MAX_CHARS are renamed to
  NARRATIVE_WIDTH_MIN_UNITS and NARRATIVE_WIDTH_MAX_UNITS.** The output contract
  applies this range to the width DIRECTLY with no conversion of any kind, which
  makes it the one pair in the whole width arithmetic that takes no conversion, and
  it was the one pair named as though it took one. A width unit and a character are
  not the same quantity, and a name that says otherwise invites the conversion the
  contract forbids.
- **TITLE_CASE_HEADINGS gains a second exemption: a BOUND string, and the documented
  default standing in for one, ships in the case it was bound in.** A case rule that
  rewrites an organization's own words is a rename nobody asked for, and it is the
  same defect as translating a header. MANDATORY_SECTION_LABEL's sentence-case
  default was illegal against the old wording while being correct in every other
  respect. The exemption bites hardest where the string becomes a sheet name, since
  sheet names are compared between runs and a case change breaks that comparison.
  **SUPERSEDED IN PART, AND THE VARIABLE'S OWN VALIDATION GOVERNS.** The exemption for
  table column headers is WITHDRAWN under SD-FMT-13, and the half of the second
  exemption covering a DOCUMENTED DEFAULT is withdrawn with it: a default is this
  bundle's own words, so every default is now WRITTEN in Title Case rather than
  exempted from it, which is why MANDATORY_SECTION_LABEL's default is Title Case above
  and why no run re-cases anything. What survives is the half that was always the
  point, that a string the ORGANIZATION BOUND ships in the case it was bound in.
- **SCORE_DECIMAL_PLACES is a FLOOR that the run computes upward from.** The correct
  precision is data-dependent and a constant cannot be it: the run raises precision
  until no two rows with different real scores print alike, because a printed tie
  that is not a tie makes the rank beside it look arbitrary. Per S5, the bound value
  is the floor and the live computation governs above it.
- **DEADBAND's rung-5 level band no longer reads MIN_POPULATION_FOR_NORM, and
  MIN_PRIOR_PERIODS_FOR_BAND is new.** That variable floors a PEER COUNT; the rung-5
  level band needs a count of the unit's own PRIOR PERIODS, and reading the peer
  floor there demanded five periods of history and made the band structurally
  unreachable for every annual reviewer. The band was defined, never once computable
  for them, and nothing said so. **Rung 5 is deliberately NOT given a fixed band the
  way rung 4 is:** rung 4's unit is a percent of target, which is self-normalising,
  while a level delta in points of a rate has no anchor, so a fixed number there
  would be calibrated to nobody's volatility and applied to everybody's.
- **CLAIM_STRENGTH_BY_RUNG's A1 row now carries the three WORDINGS and not only the
  assignment.** Strong, qualified and bounded were defined in one skill's own body
  because nothing here defined them, while all three skills word claims. An
  assignment to a word nobody defined is not a default.
- **FORM_SECTIONS gains `field_kind`, a key into FIELD_LIMITS**, and the standing
  default assigns one to each drafted section. A skill had written a four-step total
  rule inferring the kind from what a section DOES, which is correct and is still a
  derivation standing in for a binding: at the documented defaults two candidate keys
  carry the same number, so the hole is invisible, and at an organization that binds
  them differently two implementers cap the same box two ways.
- **PASS_QUALIFIER_VOCABULARY gains a bound `code` per entry, and it is never an
  ordinal.** A skill was using each entry's position in the set as its legend code,
  which works exactly until a member is added, at which point every legend code in
  every prior workbook silently means a different qualifier.
- **COLOR_STATUS_RETIRED is new, and it reconciles the contradiction in the direction
  that keeps a colour a variable with one binding.** CLASSIFICATION_LABELS requires
  every key to name a fill variable; RETIRED had none, which forced either a shared
  fill, which the one-fill-per-state rule forbids, or a raw hex inside
  CLASSIFICATION_FILLS, which would have been the one colour in the palette with
  nothing behind it. The separation rule's domain is now seven named fills plus the
  map, and the arithmetic still passes with a minimum separation of 8.6.
- **The GROUP 24 header sweep now covers the REFERENCE TABLES, which it had never
  reached.** It was run over the entity sheets, where it holds absolutely, and not
  over the grids whose rows are requirements and codes rather than units of business,
  so a summary sheet shipped about a dozen columns whose headers were plain-language
  literals with nothing behind them. They were disclosed, correctly, as defaulted
  headers, which is the contract's provision and not a licence: such a header cannot
  be renamed into an organization's own language and drifts between implementers.
  Twenty-two header variables and ROW_KIND_LABELS are added for the summary and the
  legend. **The per-state count columns are a PREFIX AND SUFFIX PAIR rather than one
  variable per state**, on the HDR_SPAN_PREFIX precedent, because that family is
  generated from CLASSIFICATION_VOCABULARY: fixed variables would have been correct
  only until the vocabulary gained a member. The planning skill's own reference table
  was checked and has no such gap; the review skill emits no grid at all.

## Eighteenth pass, the unreadable header reported from a delivered workbook

- **COLOR_TITLE_BAND and COLOR_HEADER_TEXT swap direction, in one edit, because they
  are one decision.** The band's default was a very dark blue at greyscale 53.5 under
  white text at 255.0. That pairing is handsome while both halves render and is gone
  the instant either does not: with the fill absent it is white text on a white sheet,
  a separation of 0.0. The band is now LIGHT, B9CFE7 at 203.2, and the ink is the dark
  blue the band used to be, 1F3864 at 53.5. The three separations are 149.6 intended,
  201.5 with the fill gone, and 203.2 with the ink gone, against a floor of 90. The
  palette is the same family and only the direction moved.
- **COLOR_SUBTITLE_BAND and COLOR_SECTION_HEADER move with it**, for the identical
  reason, and COLOR_LABEL_FILL did not have to: it was already light and already
  carried dark text. The four structural bands are held 8 apart from each other and
  from the sheet ground so the panel hierarchy survives a photocopy, and they are
  stated NOT to be members of the palette separation rule's union, because they encode
  no state and no reader compares a header band to a scored cell to learn what a cell
  means.
- **COLOR_GRIDLINE moves from 9BA7B5 to 4A5A6A**, from greyscale 165.0 to 87.0. The
  old value separated from a white sheet by 90.0, which is a legible letter and an
  invisible hairline, and the author's report of a grid he could not see was the
  measurement. A LINE holds a higher floor than a letter for the physical reason that a
  hairline lays down a fraction of the ink a glyph does. The new value is 168.0 clear
  of the sheet ground and 116.1 clear of the darkest band it is drawn over.
- **THE OPACITY RULE IS NEW AND IT BINDS EVERY COLOUR VARIABLE IN GROUP 16.** Three
  delivered workbooks wrote every header fill as `001F3864` and every header font colour
  as `00FFFFFF`. The leading byte is the alpha byte, the common spreadsheet engine reads
  `00RRGGBB` as opaque, and many other renderers read it as fully transparent. The file
  was therefore correct in the tool that built it and unreadable in the tool the reader
  opened it in, which is the worst shape a defect can take: the run that made it
  verified a readable artifact. Every colour is now written with an explicit `FF` alpha
  where the container's field carries one, and never padded to eight digits with a `00`.
- **TABLE_STYLE_NAME's default moves from the medium-weight family's default member to
  the light-weight family's accent-1 member, and the prose moves with the example.** The
  old default's own header band is a dark fill under white text, which agreed in
  direction with the old direct formatting, so a renderer honouring the style and a
  renderer honouring the direct formatting produced the same unreadable header from two
  different places. The style's header band now agrees with the direct band in the
  readable direction instead. Row stripes stay on, and a style whose own header band
  opposes the contract's element 5 is rejected at validation.
- **COLOR_STATUS_NOT_SCORED's EXAMPLE cell is corrected from F2F2F2 to E0E0E0.** Its A1
  default had already moved to E0E0E0 and had recorded why, while the example beside the
  variable still carried the value the separation rule rejected. That is precisely the
  prose-and-example disagreement TABLE_STYLE_NAME's row was written about, sitting three
  rows below it.
