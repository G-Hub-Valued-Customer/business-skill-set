# THE BINDING SCHEMA, AND HOW A VARIABLE RESOLVES

# BINDING SCHEMA

The complete variable dictionary for the three-skill bundle: PLANNING (periodic
account or population planning), REVIEW (objective setting and performance
write-up), SCORECARD (compliance and execution gap scoring).

One config, three skills. Nothing in this file is skill-specific. Every skill
reads the same bound config and fails honestly on anything unbound.

## How to read this file

Each row carries:

- NAME: the config key, UPPER_SNAKE_CASE.
- DEFINITION: one line.
- TIER: ORG (bound by someone who knows the answers) or PERSON (answered by each
  user on their own first run).
- STATE: one of the four binding states below.
- TYPE: scalar, list, taxonomy, or mapping.
  - scalar: one value.
  - list: an ordered or unordered set of values of one kind.
  - mapping: a set of key to value pairs, flat.
  - taxonomy: a structured object whose shape is specified under the group
    heading. A taxonomy is never a bare list of names.
- VALIDATION: a rule the binding interview or a later run can test.
- EXAMPLE: a worked value from a business that is not consumer goods.

## Standing rules that govern the whole schema

- S1. No employer literal is ever written into skill text. Every literal lives
  here, behind a name.
- S2. A variable that is unbound is named as unbound in the output. It is never
  guessed, never defaulted to the value that maximizes a score, and never
  silently skipped.
- S3. A variable marked ORG is never asked of a PERSON-tier user. If a run needs
  an unbound ORG value, the run degrades and says so. See reference/binding-interview.md.
- S4. Seed data marked SEED is a starting dictionary, not a closed list. The
  skill extends it at runtime and records what it added. See reference/field-resolution.md.
- S5. Every threshold that could be computed from the data in hand is computed
  from the data in hand. A bound threshold is a floor or a fallback, never a
  substitute for a live computation.
- S6. Every derived value carries the inputs it was derived from. A derived
  ceiling is never stored as a literal.
- S9. PRECEDENCE RUNS DOWNHILL FROM EVIDENCE TO CONVENTION. In order: a value
  bound at IGNITION; a value bound later; a value derived from the data this run;
  a documented default. A documented default applied to an unbound variable may
  NARROW what a run attempts. It may never contradict, replace or silently
  supersede a value the organization actually bound. Before applying a default,
  test whether it would change a decision a bound value already decided; if it
  would, the default is not applied to that decision, the bound value stands, and
  the notice names the narrowing rather than the substitution. An unbound value
  that supplies one rung, one flag or one section removes only that rung, flag or
  section: the run falls to the best remaining BOUND option, never past it to the
  floor. See SD-CTR-24.
- S8. A LOCATION may be bound. A STANDARD may not. The schema binds where an
  authoritative document lives, what it is called, and when a cached copy of it
  expires. It never binds the content of a requirement set, a rule set or a
  scored standard as the authority for a run. A standard is read from its
  published source on every run. Where a reference block is cached, it is a copy
  behind a validity date, subordinate to the live source, refreshed or marked
  stale, and never the thing a run scores against. Nothing in this schema is a
  place to put the requirements themselves.
- S10. EVERY CLOSED VALUE SET CARRIES A TOTALITY ARGUMENT, AND THE VALIDATION RUNS
  FROM THE STATES TO THE SET AND NOT FROM THE SET TO THE STATES. A closed
  vocabulary is a promise that a run will never have to invent a value, and it
  keeps that promise only where every state a skill can actually emit has a member
  that applies to it. The check is: enumerate the states the emitting rule can
  produce, including the ones its own guards create; then, for each, name the
  member that carries it. A set that cannot describe a real row is worse than an
  open one, because the run is forbidden from inventing and is left with nothing
  correct to write. Where a hole is found, the set gains the missing member; a run
  never resolves it by taking the closest available value, which asserts something
  nobody checked. The sets under this rule are CLASSIFICATION_LABELS,
  CLASSIFICATION_VOCABULARY, REASON_CODE_SET, CLOSE_STATE_VOCABULARY,
  URGENCY_VOCABULARY,
  PASS_QUALIFIER_VOCABULARY, the values of HDR_DIRECTIVE_STATUS, CLOSE_WEIGHTS,
  PRIORITY_BAND_LABELS, ROW_KIND_LABELS, STATUS_VALUES, ACTIVITY_STATUS_VALUES,
  UNIT_ACTIONABLE_NOW_VALUES and RIGHT_ALIGN_COLUMNS, plus the seven shape tokens
  and the four capability states, which are total by construction and are named
  here so a later sweep does not have to rediscover that.
- S7. Binding is STAGED, not up front. An unbound variable must never produce a
  wrong answer. It produces exactly one of two things: a documented default that
  is named in the output, or an honest degradation notice that says what could
  not be determined and what was therefore not attempted. This is the
  completeness gate turned on the configuration itself.

## The four binding states

| State | Meaning | When it is asked | What happens if it is unbound |
|---|---|---|---|
| IGNITION | Required before a BOUND run can be produced. | In the ignition interview, before the first bound run. | The run does NOT stop. It degrades to a PROVISIONAL RUN: the value is inferred from the data where it can be, at MEDIUM confidence and never written to the config, the run produces real output, and the artifact is labelled provisional at the same prominence on every run until the value is bound. See reference/binding-interview.md Part 6, which specifies that sequence end to end. NO STATE IN THIS SCHEMA STOPS A RUN. The only conditions that stop a run are the members of HARD_GATES, and no binding state is one of them. |
| DEFERRED | Required eventually, but requested at the moment a run first hits a decision that needs it. | At first need, once, then recorded so it is never asked again. | The documented default in SECTION A1 or A2 is applied and the degradation notice in SECTION A1 or A2 is printed in the artifact. |
| OPTIONAL | Improves the output. Nothing degrades without it. | Only in the full audit, or when the user volunteers it. | Nothing. The feature it enriches is simply not enriched, and the run says nothing about it. |
| CONDITIONAL | Required only when another binding takes a particular value. The trigger condition is stated in the VALIDATION cell. | At first need, once the trigger condition is met. | If the trigger is not met, nothing. If the trigger is met, it behaves exactly as DEFERRED. |

The ceiling on IGNITION is 15 ORG variables, and the set below holds 10. The
test for membership is not "is this important" but "would its absence make the
output WRONG rather than merely thinner". A value whose absence can be honestly
disclosed and correctly defaulted is DEFERRED, however important it is.

**IGNITION IS A QUALITY STATE, NOT A GATE.** An earlier revision of this table
said the first run cannot start and that IGNITION was the only state that blocks.
That was wrong and it contradicted two other files that specify the provisional
run in full. A frontline user cannot clear an organization binding, and the
correct response to a blocking state the user cannot clear is not to hand them
the block. An unbound IGNITION value degrades exactly as any other unbound value
does: inferred where the data supports it, defaulted where it does not, disclosed
either way, and never written to the config from a run.

### The 10 ORG ignition variables, and why each one fails the disclosure test

**THE THIRD COLUMN IS THE FIX FOR A DEFECT THAT APPEARED TWICE.** The binding
states table above gives the GENERIC consequence of an unbound ignition value, that
the run degrades to a provisional one. That is true and it is not the whole
consequence, and because each variable's SPECIFIC consequence had no home in this
schema, it ended up written in the interview instead, in another file, where it
could and did contradict the generic statement. A reader taking the states table
and a reader taking the interview produced two different artifacts off one binding
state.

**BOTH CONSEQUENCES APPLY, ALWAYS, AND THEY ARE NOT ALTERNATIVES.** The generic one
is about the ARTIFACT'S LABEL: the run is provisional and says so at the same
prominence every time. The specific one is about WHAT THE RUN ACTUALLY DOES
DIFFERENTLY, and it is stated in the third column below and nowhere else. Every
other file names the variable and points here.

| Variable | Why it cannot be deferred | WHAT SPECIFICALLY HAPPENS IF IT IS UNBOUND, and this column is the ONLY statement of it |
|---|---|---|
| SCOPE_LEVELS | Without the containment chain the skill cannot tell whether a code sits above or below the user. A filter can then return the wrong population and a peer comparison can compare a person against their own subordinates, with every number internally consistent. That is the failure SD-QUA-12 says destroys trust, and no label repairs it. | The hierarchy is DETECTED from the file where the data supports it, at medium confidence, and named. Scope filters resolve only against values present in the file, no peer comparison is attempted at any level, and the artifact says both. |
| ROLE_LADDER | Claim tier decides what a person may claim. Guessing it makes a frontline person hide behind aggregates they did not produce, or a leader claim a subordinate's individual work. SD-SPN-09 calls both fatal, in both directions. | The reader is treated as the NARROWEST role, per ROLE_FALLBACK_KEY: the shorter list and the narrower claims. No claim is worded at aggregate strength for anybody. |
| POPULATION_SHAPE | Decides what the denominator is. A fixed-roster model applied to a flowing pipeline mixes closed and open units into one denominator, and SD-POP-21 records that the reader cannot recover it from the output. | Mode is DETECTED by SD-POP-24, at medium confidence, with the tests that fired printed and the answer marked DECIDED or TIE-BROKEN. Every sub-key that cannot be inferred is treated as unbound and takes its A2 default. |
| COUNTERFACTUAL_AVAILABLE_RUNGS | Every number the bundle emits carries a second number the writer did not choose. Without knowing which second numbers exist, the skill either ships bare numbers or invents a comparison. | **DERIVED FIRST, FLOORED SECOND.** The available set is DERIVED as every rung whose own definition variables are bound, plus rung 6, which is always present; the derivation is recorded at MEDIUM confidence, every rung it struck is named with the definition that was missing, and it is read back for correction. Only where that derivation yields rung 6 alone does the floor consequence stand: every figure is printed with a denominator population and NONE is worded as an achievement. |
| COUNTERFACTUAL_DEFAULT_RUNG | Decides how strongly every claim may be worded. An unbound default means claims are worded at a strength nobody authorized. | **DERIVED BEFORE IT IS FLOORED, BECAUSE NO ORGANIZATION DOCUMENT ANSWERS THIS ONE.** It is a question about the method's own configuration rather than about the business, so a run bound faithfully from an organization's own published documents will reach it unanswered, exactly as BINDING_OWNER_CONTACT once did. THE DERIVATION: where COUNTERFACTUAL_AVAILABLE_RUNGS is bound or derived, the default rung is the HIGHEST rung present in the available set whose own definition is bound. It is recorded as DERIVED at MEDIUM confidence, the derivation is named beside the claims it governs, and it is read back for correction in the interview close, which is the same DERIVED-satisfies-ignition mechanism the ROLE_LADDER and POPULATION_SHAPE sub-fields use. THE FLOOR APPLIES ONLY where no rung is available at all, or where no available rung's own definition is bound: then claims fall to the floor rung's wording, nothing is worded above the strength the floor supports, and the artifact says which rung each figure used. **AN UNBOUND VALUE HERE NEVER DELETES THE EFFECT OF A RUNG THE ORGANIZATION DID BIND.** That inversion is forbidden by S9 and by SD-CTR-24 and it is regression case 15 with the tiers swapped: a bound ignition value being overridden by an unbound one, on the same axis, is the same defect as a deferred default deleting an ignition binding. |
| MOVING_GROUND_NAME | The named requirement in SD-CLM-05: a business must name what its ground is, and a claim may not ship at achievement strength until it has. A default here would be an invented benchmark. | **CLAIM STRENGTH IS CAPPED. No figure ships at ACHIEVEMENT strength, every figure is printed with its denominator, and the artifact states that no ground has been named.** The run is NOT stopped and the numbers are NOT withheld. This is the specific consequence, and it is stated HERE so it is not stated differently anywhere else. |
| PLANNING_PERIOD_NAME | Half of the operating window. See below. | The period is DETECTED from the file's own stamps and named as detected. Where nothing can be read, the run says which window it planned and that the window was assumed. |
| PLANNING_PERIOD_LENGTH_DAYS | The other half. SD-SRC-15 records that a run which quietly plans the wrong period is indistinguishable from a correct one until the person is standing in front of the work. That is precisely the failure a disclosure notice does not repair, because the reader has no way to notice the notice mattered. | Derived from the detected period, and the derived window's exact dates are printed above the list so a reader can see instantly whether the wrong window was planned. |
| ORG_NAME | Every degradation notice, every unbound-value notice and every artifact header names the organization. Without it the notices that carry the whole staged-binding contract are unaddressed text. | Notices address the organization generically. Every other consequence is unaffected. |
| BINDING_OWNER_NAME | A degradation notice must say who can fix it, or the progressive binding loop never closes and the same gap is disclosed forever. | The standing senior-role authority grant still stands, per SD-CTR-25, so progressive binding still fires. Notices carry no addressee and say so at the top of the first report, per reference/binding-interview.md Turn 1. |
The last two are the weakest members of the set by the wrongness test, and they
are included on a different ground, stated openly: they are what makes the
DEFERRED state work at all. Without an identifiable owner, a deferred variable is
not deferred, it is abandoned.

**BINDING_OWNER_CONTACT WAS THE ELEVENTH MEMBER AND IS NOW DEFERRED. THE REASON IS
WORTH KEEPING, BECAUSE THE ARGUMENT FOR PUTTING IT HERE IS STILL A GOOD ONE AND
SOMEBODY WILL MAKE IT AGAIN.** It failed a test no other member of the set fails:
IT IS THE ONE VALUE A DOCUMENT CAN NEVER SUPPLY. A first run bound faithfully from
an organization's own published documents can read the organization's name, its
hierarchy, its roles, its unit, its period, its ground and the NAME of the person
who owns the servicing standard. It cannot read a mailbox, because internal policy
documents do not carry one, and inventing one is forbidden by SD-CNF-07. So every
documents-bound run was stamped PROVISIONAL at full prominence, forever, on the
one binding that no amount of care could clear, and the provisional label stopped
distinguishing a run that was missing something recoverable from one that was not.

**WHAT THE PROVISIONAL STATE EXISTS TO SIGNAL IS NOT LOST, IT IS MOVED TO ITS OWN
LINE.** Where BINDING_OWNER_CONTACT is unbound the run is NOT provisional on that
account alone, and the artifact still carries, at the standing prominence and on
every run until it is bound, the sentence in this variable's SECTION A1 row: the
invitation in this report names no address, so a reader who finds something wrong
has nowhere to send it. That is the honest disclosure. What it is not is a claim
that the whole binding is unsound.

**AND THE RECOVERABILITY ARGUMENT SURVIVES THROUGH THE NAME RATHER THAN THE
ADDRESS.** Progressive binding is gated on binding AUTHORITY, and authority is
computed from BINDING_OWNER_NAME and from the standing senior-role grant, neither
of which reads an address. A deferred question still fires, still finds an
authorized answerer, and is still recorded. The address decides whether a NOTICE
can be posted, not whether a QUESTION can be asked.

### THE ANSWERABILITY TEST, APPLIED TO THE WHOLE IGNITION SET

**MEMBERSHIP OF THIS SET NOW TURNS ON THREE TESTS AND NOT ONE, AND THE SECOND AND
THIRD WERE ADDED AFTER TWO MEMBERS FAILED THEM IN SUCCESSIVE LIVE RUNS.** The first
test is the original one and it is not weakened. Before anything is added here, or
kept here, all three are answered in writing:

1. **THE WRONGNESS TEST.** Would its absence make the output WRONG rather than
   merely thinner? A value whose absence can be honestly disclosed and correctly
   defaulted is DEFERRED, however important it is.
2. **THE ANSWERABILITY TEST.** Can a person answering the ignition interview FROM
   THEIR OWN ORGANIZATION'S DOCUMENTS actually answer it? A value that no document
   at any organization supplies is not a binding, it is a permanent stamp: it makes
   every honest first run degrade on a gap no amount of care can close, and the
   degradation label then stops distinguishing a run missing something recoverable
   from one that is not. BINDING_OWNER_CONTACT failed this test and was moved to
   DEFERRED. COUNTERFACTUAL_DEFAULT_RUNG failed it in the same way one round later
   and was given a DERIVATION rather than moved, because unlike an address it can be
   computed from another ignition answer.
3. **THE PROPORTIONALITY TEST.** Is the unbound consequence in the third column
   PROPORTIONATE to what is actually missing? A consequence that discards work the
   run ALREADY DID, or that overrides a value the organization DID bind, fails this
   test whatever its wording, because it converts one missing answer into the loss
   of every answer beside it. Where a value can be derived from another binding, the
   derivation is stated in the third column and the floor applies only past it.

**THE SWEEP, RUN OVER ALL TEN ORG MEMBERS AND RECORDED SO IT CAN BE RE-RUN.** The
route column is the answer to test 2: what an unanswered value falls back to before
any floor is reached.

| Variable | Answerable from an organization's own documents | Route when the interview does not answer it | Proportionate |
|---|---|---|---|
| SCOPE_LEVELS | Yes: an organization chart, a unit list or the file's own codes. | DETECTED from the file at medium confidence. | Yes. |
| ROLE_LADDER | Yes: role definitions, titles, a delegation table. | ROLE_FALLBACK_KEY, the narrowest role. | Yes: narrowing is the safe direction. |
| POPULATION_SHAPE | Partly. `mode` is a question about the data rather than about policy, and few businesses have written it down. | DETECTED by SD-POP-24 with the tests that fired printed, then per-sub-key A2 defaults. | Yes, because the detection is published and correctable. |
| COUNTERFACTUAL_AVAILABLE_RUNGS | Yes, one rung at a time: each rung's own definition is a business fact and the run strikes the rungs no document defines. | DERIVED from which rung definitions are bound, floored at rung 6. | Yes, as of the derivation above. |
| COUNTERFACTUAL_DEFAULT_RUNG | **NO. No document at any organization answers it, because it is a question about this method's configuration.** | DERIVED as the highest available rung whose definition is bound. | Yes, as of the derivation above. It was NOT before: the floor deleted every rung the run had just bound. |
| MOVING_GROUND_NAME | Yes: published objectives, a market or operating commentary, a plan's own preamble. | None. Claim strength is capped and the absence is stated. | Yes: this is the SD-CLM-05 requirement itself, and a default here would be an invented benchmark. |
| PLANNING_PERIOD_NAME | Yes: a calendar, a plan, the file's own stamps. | DETECTED from the file's stamps. | Yes. |
| PLANNING_PERIOD_LENGTH_DAYS | Yes, as above. | DERIVED from the detected period, with the window's exact dates printed. | Yes. |
| ORG_NAME | Yes, trivially. | Notices address the organization generically. | Yes. |
| BINDING_OWNER_NAME | Yes: the owner of a standard, a policy or a plan is named in it. | The senior-role authority grant under SD-CTR-25; notices carry no addressee and say so. | Yes. |

**THE FOUR PERSON IGNITION VARIABLES PASS TEST 2 BY CONSTRUCTION** and are recorded
here so a later sweep does not have to rediscover it: they are asked of the person
about themselves, not of a document, so there is no document that can fail to
supply them. Their unbound routes are in Group 25 and SECTION A1.

**WHAT THE SWEEP FOUND, STATED PLAINLY:** one member failed test 2 outright and
test 3 with it, and is fixed above; one member passed test 2 but had no derivation
where one was computable, and now has one; the other eight pass all three. The
count of ORG ignition variables is unchanged at 10, because the fix for the failing
member was a derivation rather than a move, and the ceiling of 15 is untouched.

### IGNITION COMPLETENESS: what counts as bound, and why a full interview must finish

**AN IGNITION VARIABLE IS SATISFIED WHEN EVERY SUB-FIELD IT REQUIRES IS ANSWERED,
DERIVED OR DEFAULTED. A DERIVED SUB-FIELD IS NOT AN UNBOUND SUB-FIELD.** Three of
the eleven are TAXONOMIES with sub-fields, and an earlier revision validated them
sub-field by sub-field against answers only. The result was that a co-operative
director who answered every one of the seven interview questions naturally, in
the way a competent person actually answers them, left ROLE_LADDER.claim_tier,
ROLE_LADDER.scope_level and POPULATION_SHAPE.mode without explicit values, failed
ignition validation, and got an artifact stamped PROVISIONAL forever. Nothing
warned the interviewer, because from their side the interview was complete. That
is worse than a missing binding: it is a working interview that produces a
permanently degraded product and tells nobody.

**THE RULE, AND IT IS AN INVARIANT: A FULLY ANSWERED IGNITION INTERVIEW PRODUCES
A NON-PROVISIONAL RUN.** If it does not, either the interview is not asking for
something it needs, or a sub-field is missing a derivation. Both are defects in
this bundle, never in the answerer. See SD-CTR-26.

Each sub-field of an ignition taxonomy therefore sits in exactly one of three
states, and every one of them satisfies ignition:

| State | Meaning | Confidence | Recorded as |
|---|---|---|---|
| ANSWERED | the interviewer stated it | HIGH | the value, with source ANSWERED |
| DERIVED | computed from other answers by the derivation in its SECTION A1 row | MEDIUM | the value, with source DERIVED and the derivation named |
| DEFAULTED | no derivation applies, so the documented default stands | LOW | the value, with source DEFAULTED and the notice carried |

**A DERIVED SUB-FIELD IS READ BACK BEFORE THE INTERVIEW CLOSES, NEVER AFTER.**
Every derived value is shown to the answerer in the close, in one table, in their
own words, with the invitation to correct any line. A correction promotes that
line to ANSWERED. Declining to review promotes nothing and is recorded as such.
This is the only place a MEDIUM-confidence value may be written to the ORG config,
and it is legitimate precisely because a person with authority looked at it and
said yes. A run may still never do this: I7 is untouched.

### The completeness trace, verified mechanically

Checked by walking the tables rather than by reading them, in three passes:

1. **Every one of the 10 ORG ignition variables is named in a BINDS line of a
   Stage 1 turn.** None is left to a turn that does not exist. Count of ignition
   variables not elicited by any turn: ZERO.
2. **Every sub-field of the three ignition taxonomies is elicited, derived or
   defaulted.** SCOPE_LEVELS has 7 sub-fields: 2 elicited by Turn 2, 5 derived
   with A1 rows. ROLE_LADDER has 11: 2 elicited by Turn 3, 9 derived with A1 rows.
   POPULATION_SHAPE has 9: 4 elicited by Turn 4, 5 derived or conditional with A2
   rows, `mode` among them. Count of sub-fields with no derivation and no default:
   ZERO.
3. **Coverage runs in both directions.** No DEFERRED variable lacks an A1 row, no
   CONDITIONAL variable lacks an A2 row, and the only appendix rows that are not
   variables are the A1 and A2 SUB-KEY rows, whose counts live in the COUNTS block
   and nowhere else.

**THE CONCLUSION, STATED AS A CLAIM SOMEBODY CAN CHECK: an interview in which the
answerer answers all seven turns leaves NO ignition variable and NO ignition
sub-field unbound, so the completeness check in Turn 8 passes and the runs that
follow are NOT provisional.** Where any future change breaks that, it breaks one
of the three passes above, and re-running them names which.

**WHAT REMAINS GENUINELY UNBINDABLE STILL BLOCKS NOTHING.** Where a sub-field is
neither answered nor derivable, the documented default applies, the notice is
carried, and the run proceeds. Ignition completeness is about not stamping a run
PROVISIONAL on a technicality; it is not a new gate. No binding state stops a run.

### The 4 PERSON ignition variables

PERSON_ROLE_TITLE, PERSON_SCOPE_CODE, PERSON_SUPERVISOR_NAME and
PERSON_HAS_DIRECT_REPORTS. These are the four questions of the person script.
They are asked of the user, not of the binding owner, and the ORG ceiling does
not apply to them.

---


---

## THE RESOLUTION RULE

Every configuration value is a NAMED VARIABLE. To resolve one, find it in the
index below and read that one group file. **The group file carries the
variable's definition, its tier, its state, its validation, its documented
DEFAULT and its exact DEGRADATION NOTICE together.** In the single-file build
those last two live in a separate appendix; they are moved here so that a run
holding a definition can never be holding it without the default it needs when
the value turns out to be unbound. That separation was the one real hazard in
splitting this file and it is closed by construction rather than by discipline.

## THE GROUPS

| Group | File | Subject |
|---|---|---|
| 1 | `reference/schema/bundle-identity-and-attribution.md` | Bundle Identity And Attribution |
| 2 | `reference/schema/organization-identity.md` | Organization Identity |
| 3 | `reference/schema/scope-hierarchy.md` | The Scope Hierarchy |
| 4 | `reference/schema/role-ladder.md` | The Role Ladder |
| 5 | `reference/schema/population-shape.md` | Population Shape |
| 6 | `reference/schema/counterfactual-denominator.md` | The Counterfactual Denominator |
| 7 | `reference/schema/creditable-entities.md` | Creditable Entities |
| 8 | `reference/schema/measures-and-units.md` | Measures And Units |
| 9 | `reference/schema/column-concept-dictionary.md` | The Column Concept Dictionary |
| 10 | `reference/schema/work-items-and-work-types.md` | Work Items And Work Types |
| 11 | `reference/schema/priority-sources-and-authority.md` | Priority Sources And Authority |
| 12 | `reference/schema/lineage-and-claims.md` | Lineage And Claims |
| 13 | `reference/schema/periods-and-the-operating-calendar.md` | Periods And The Operating Calendar |
| 14 | `reference/schema/compliance-and-jurisdiction.md` | Compliance And Jurisdiction |
| 15 | `reference/schema/deliverable-contract.md` | The Deliverable Contract |
| 16 | `reference/schema/formatting.md` | Formatting |
| 17 | `reference/schema/scoring-constants.md` | Scoring Constants |
| 18 | `reference/schema/exception-flags-and-thresholds.md` | Exception Flags And Thresholds |
| 19 | `reference/schema/breadth-section.md` | The Breadth Section |
| 20 | `reference/schema/review-form-and-field-limits.md` | The Review Form And Field Limits |
| 21 | `reference/schema/questions-and-interaction.md` | Questions And Interaction |
| 22 | `reference/schema/run-control-and-reliability.md` | Run Control And Reliability |
| 23 | `reference/schema/systems-of-record-and-capability-bindings.md` | Systems Of Record And Capability Bindings |
| 24 | `reference/schema/language-labels-and-messages.md` | Language, Labels And Messages |
| 25 | `reference/schema/person-tier.md` | Person Tier |

## EVERY VARIABLE, AND THE ONE FILE IT LIVES IN

| Variable | File |
|---|---|
| `ACTIVITY_BLOCK_TERMINATOR_CONCEPT` | `reference/schema/column-concept-dictionary.md` |
| `ACTIVITY_STATUS_VALUES` | `reference/schema/review-form-and-field-limits.md` |
| `ACTOR_TEST_ENABLED` | `reference/schema/priority-sources-and-authority.md` |
| `ADDRESSABLE_POPULATION_CONCEPT` | `reference/schema/counterfactual-denominator.md` |
| `ADDRESSABLE_POPULATION_DEFINITION` | `reference/schema/counterfactual-denominator.md` |
| `ADDRESSABLE_SELF_SHARE_CEILING` | `reference/schema/counterfactual-denominator.md` |
| `ALERT_BAND_THRESHOLDS` | `reference/schema/formatting.md` |
| `ALERT_COUNT_POPULATION` | `reference/schema/exception-flags-and-thresholds.md` |
| `ALERT_OVERDUE_DAYS` | `reference/schema/exception-flags-and-thresholds.md` |
| `ALERT_SCALES` | `reference/schema/exception-flags-and-thresholds.md` |
| `ALERT_WARN_DAYS` | `reference/schema/exception-flags-and-thresholds.md` |
| `ALLOWED_CHARACTER_RANGE` | `reference/schema/formatting.md` |
| `ANOMALY_QUESTION_CAP` | `reference/schema/questions-and-interaction.md` |
| `ANONYMITY_FLOOR` | `reference/schema/lineage-and-claims.md` |
| `ASK_LANGUAGE_RULE` | `reference/schema/questions-and-interaction.md` |
| `ATTRIBUTION_TEAM_PHRASES` | `reference/schema/lineage-and-claims.md` |
| `BANNED_HEADINGS` | `reference/schema/deliverable-contract.md` |
| `BANNED_PHRASES` | `reference/schema/language-labels-and-messages.md` |
| `BARE_DENOMINATOR_CONCEPT` | `reference/schema/counterfactual-denominator.md` |
| `BASE_TERM` | `reference/schema/scoring-constants.md` |
| `BEHAVIOUR_FRAMEWORK_ITEMS` | `reference/schema/review-form-and-field-limits.md` |
| `BEHAVIOUR_FRAMEWORK_NAME` | `reference/schema/review-form-and-field-limits.md` |
| `BEHAVIOUR_SCALE_VALUES` | `reference/schema/review-form-and-field-limits.md` |
| `BENCHMARK_GAP_THRESHOLD` | `reference/schema/exception-flags-and-thresholds.md` |
| `BENCHMARK_POPULATIONS` | `reference/schema/creditable-entities.md` |
| `BINDING_LOCKED` | `reference/schema/bundle-identity-and-attribution.md` |
| `BINDING_OWNER_CONTACT` | `reference/schema/bundle-identity-and-attribution.md` |
| `BINDING_OWNER_NAME` | `reference/schema/bundle-identity-and-attribution.md` |
| `BODY_FONT` | `reference/schema/formatting.md` |
| `BODY_FONT_SIZE` | `reference/schema/formatting.md` |
| `BREADTH_ADMISSION_IS_THE_PAIR` | `reference/schema/breadth-section.md` |
| `BREADTH_COUNT_CONCEPT` | `reference/schema/breadth-section.md` |
| `BREADTH_FLOOR_DEPARTURE_STATEMENT` | `reference/schema/breadth-section.md` |
| `BREADTH_FLOOR_FRACTION` | `reference/schema/breadth-section.md` |
| `BREADTH_SATISFACTION_CONCEPT` | `reference/schema/breadth-section.md` |
| `BREADTH_SORT_KEYS` | `reference/schema/breadth-section.md` |
| `BUNDLE_VERSION` | `reference/schema/bundle-identity-and-attribution.md` |
| `BUNDLE_VERSION_DATE` | `reference/schema/bundle-identity-and-attribution.md` |
| `CARET_ALLOWANCE_CHARS` | `reference/schema/formatting.md` |
| `CARRYOVER_LABEL` | `reference/schema/periods-and-the-operating-calendar.md` |
| `CENTRAL_BRIEF_NAME` | `reference/schema/priority-sources-and-authority.md` |
| `CENTRAL_BRIEF_REQUIRED` | `reference/schema/priority-sources-and-authority.md` |
| `CENTRAL_BRIEF_TABLE_COLUMNS` | `reference/schema/priority-sources-and-authority.md` |
| `CENTRE_ALIGN_MAX_CHARS` | `reference/schema/formatting.md` |
| `CHAIN_DISTANCE_WEIGHTS` | `reference/schema/priority-sources-and-authority.md` |
| `CHAIN_WALK_DEPTH` | `reference/schema/priority-sources-and-authority.md` |
| `CHAR_WIDTH_FACTOR` | `reference/schema/formatting.md` |
| `CHAT_PLATFORM_NAME` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `CHAT_REPLY_MAX_LINES` | `reference/schema/deliverable-contract.md` |
| `CHECKPOINT_DELETE_ON_PUBLISH` | `reference/schema/run-control-and-reliability.md` |
| `CHECKPOINT_PATH_PATTERN` | `reference/schema/run-control-and-reliability.md` |
| `CLAIM_PART_ORDER` | `reference/schema/lineage-and-claims.md` |
| `CLAIM_STRENGTH_BY_RUNG` | `reference/schema/counterfactual-denominator.md` |
| `CLASSIFICATION_FILLS` | `reference/schema/formatting.md` |
| `CLASSIFICATION_LABELS` | `reference/schema/exception-flags-and-thresholds.md` |
| `CLASSIFICATION_VOCABULARY` | `reference/schema/formatting.md` |
| `CLOSE_HORIZON_DAYS` | `reference/schema/periods-and-the-operating-calendar.md` |
| `CLOSE_STATE_VOCABULARY` | `reference/schema/language-labels-and-messages.md` |
| `CLOSE_WEIGHTS` | `reference/schema/periods-and-the-operating-calendar.md` |
| `COLD_START_MIN_PRIOR_SHARE` | `reference/schema/counterfactual-denominator.md` |
| `COLOR_ALERT_OVERDUE` | `reference/schema/formatting.md` |
| `COLOR_ALERT_WARN` | `reference/schema/formatting.md` |
| `COLOR_GRIDLINE` | `reference/schema/formatting.md` |
| `COLOR_HEADER_TEXT` | `reference/schema/formatting.md` |
| `COLOR_LABEL_FILL` | `reference/schema/formatting.md` |
| `COLOR_SECTION_HEADER` | `reference/schema/formatting.md` |
| `COLOR_STATUS_GAP` | `reference/schema/formatting.md` |
| `COLOR_STATUS_NOT_SCORED` | `reference/schema/formatting.md` |
| `COLOR_STATUS_PASS` | `reference/schema/formatting.md` |
| `COLOR_STATUS_RETIRED` | `reference/schema/formatting.md` |
| `COLOR_STATUS_UNASSESSABLE` | `reference/schema/formatting.md` |
| `COLOR_SUBTITLE_BAND` | `reference/schema/formatting.md` |
| `COLOR_TITLE_BAND` | `reference/schema/formatting.md` |
| `COLUMN_CONCEPT_DICTIONARY` | `reference/schema/column-concept-dictionary.md` |
| `COLUMN_WIDTH_MAX_CHARS` | `reference/schema/formatting.md` |
| `COMPLETION_ABOVE_100_ALLOWED` | `reference/schema/review-form-and-field-limits.md` |
| `COMPLIANCE_CHECK_ENABLED` | `reference/schema/compliance-and-jurisdiction.md` |
| `COMPLIANCE_FAILS_CLOSED_ON` | `reference/schema/compliance-and-jurisdiction.md` |
| `COMPLIANCE_FINDINGS` | `reference/schema/compliance-and-jurisdiction.md` |
| `COMPLIANCE_GUIDE_MASTER` | `reference/schema/compliance-and-jurisdiction.md` |
| `COMPLIANCE_GUIDE_SET` | `reference/schema/compliance-and-jurisdiction.md` |
| `COMPLIANCE_GUIDE_SUPPLEMENTS` | `reference/schema/compliance-and-jurisdiction.md` |
| `COMPOSITE_QUESTION_IDS` | `reference/schema/questions-and-interaction.md` |
| `COMPRESSION_ORDER` | `reference/schema/review-form-and-field-limits.md` |
| `CONCEPT_LEARNING_ENABLED` | `reference/schema/column-concept-dictionary.md` |
| `CONCEPT_LEARNING_LOG_PATH` | `reference/schema/column-concept-dictionary.md` |
| `CONTEXT_GROUPER_MAX_DISTINCT` | `reference/schema/column-concept-dictionary.md` |
| `CONTRIBUTION_VERBS` | `reference/schema/lineage-and-claims.md` |
| `CONTROLLED_VOCABULARY` | `reference/schema/language-labels-and-messages.md` |
| `CONTROL_GROUP_DEFINITION` | `reference/schema/counterfactual-denominator.md` |
| `COUNTERFACTUAL_AVAILABLE_RUNGS` | `reference/schema/counterfactual-denominator.md` |
| `COUNTERFACTUAL_BY_METRIC` | `reference/schema/counterfactual-denominator.md` |
| `COUNTERFACTUAL_DEFAULT_RUNG` | `reference/schema/counterfactual-denominator.md` |
| `COUNTERFACTUAL_RUNG_SCOPES` | `reference/schema/counterfactual-denominator.md` |
| `COVERAGE_DUPLICATION_APPLIES_TO` | `reference/schema/scoring-constants.md` |
| `COVERAGE_DUPLICATION_FACTOR` | `reference/schema/scoring-constants.md` |
| `CREDITABLE_ENTITIES` | `reference/schema/creditable-entities.md` |
| `CREDITABLE_ENTITY_CLASS_NAME` | `reference/schema/creditable-entities.md` |
| `CYCLE_POSITIONS` | `reference/schema/periods-and-the-operating-calendar.md` |
| `CYCLE_POSITION_NAMES` | `reference/schema/periods-and-the-operating-calendar.md` |
| `DEADBAND` | `reference/schema/counterfactual-denominator.md` |
| `DELIVERABLE_CONTAINER_REQUIRED` | `reference/schema/deliverable-contract.md` |
| `DELIVERABLE_LINES` | `reference/schema/deliverable-contract.md` |
| `DELIVERABLE_NAME` | `reference/schema/deliverable-contract.md` |
| `DESTINATION_SYSTEM_NAME` | `reference/schema/review-form-and-field-limits.md` |
| `DIRECTIVE_RELEASE_PHRASES` | `reference/schema/priority-sources-and-authority.md` |
| `DIRECTORY_MANAGER_LOOKUP` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `DIRECTORY_SELF_LOOKUP` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `DOC_STORE_LIBRARY_VARIABLE` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `DOC_STORE_NAME` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `DOC_STORE_PATH_DISCOVERY_REQUIRED` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `DOC_STORE_SITE_VARIABLE` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `DOWNLOAD_DIR` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `ENTERPRISE_FINANCIAL_TARGETS` | `reference/schema/organization-identity.md` |
| `ENTERPRISE_LONG_TERM_GOALS` | `reference/schema/organization-identity.md` |
| `ENTERPRISE_STRATEGY_PILLARS` | `reference/schema/organization-identity.md` |
| `ENTITY_ALIAS_UNRECOGNIZED_ACTION` | `reference/schema/creditable-entities.md` |
| `ENTITY_BENCHMARK_MAP` | `reference/schema/creditable-entities.md` |
| `ENTITY_COLUMN_MIN_COVERAGE` | `reference/schema/creditable-entities.md` |
| `ENTITY_WEIGHT_FLOOR` | `reference/schema/creditable-entities.md` |
| `EVIDENCE_SOURCES` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `EVIDENCE_SUFFICIENCY_FLOOR` | `reference/schema/questions-and-interaction.md` |
| `EXCEPTION_ALERT_RECONCILIATION` | `reference/schema/exception-flags-and-thresholds.md` |
| `EXCEPTION_FLAGS` | `reference/schema/exception-flags-and-thresholds.md` |
| `EXCLUSION_SANITY_CEILING` | `reference/schema/population-shape.md` |
| `EXTERNAL_PEER_SET_SOURCE` | `reference/schema/counterfactual-denominator.md` |
| `EXTERNAL_WORK_TYPE_IS_EVIDENCE_ONLY` | `reference/schema/work-items-and-work-types.md` |
| `FAMILY_NAMES` | `reference/schema/creditable-entities.md` |
| `FIELD_BUDGET_SPLIT` | `reference/schema/review-form-and-field-limits.md` |
| `FIELD_LIMITS` | `reference/schema/review-form-and-field-limits.md` |
| `FILE_QUESTION_BATCH_CAP` | `reference/schema/column-concept-dictionary.md` |
| `FIXED_ROSTER_CHURN_TOLERANCE` | `reference/schema/population-shape.md` |
| `FLAG_EXEMPTIONS` | `reference/schema/exception-flags-and-thresholds.md` |
| `FLAG_MEASURE_MULTIPLIER_FLOOR` | `reference/schema/exception-flags-and-thresholds.md` |
| `FLOW_COHORT_BASIS` | `reference/schema/population-shape.md` |
| `FLOW_OPEN_DEFINITION` | `reference/schema/population-shape.md` |
| `FORBIDDEN_RETRIEVAL_PATHS` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `FORMATTING_ELEMENTS` | `reference/schema/formatting.md` |
| `FORM_FIELDS` | `reference/schema/review-form-and-field-limits.md` |
| `FORM_REQUIRED_EXEMPT_QUESTIONS` | `reference/schema/questions-and-interaction.md` |
| `FORM_SECTIONS` | `reference/schema/review-form-and-field-limits.md` |
| `FORM_SECTIONS_BY_CYCLE_POSITION` | `reference/schema/review-form-and-field-limits.md` |
| `FORM_SPEC_SOURCE` | `reference/schema/review-form-and-field-limits.md` |
| `FROZEN_SPAN_MAX_WIDTH` | `reference/schema/deliverable-contract.md` |
| `FULL_WALK_ROW_LIMIT` | `reference/schema/formatting.md` |
| `GAP_TERM_CAP` | `reference/schema/scoring-constants.md` |
| `GAP_TERM_DEFINITIONS` | `reference/schema/scoring-constants.md` |
| `GAP_TERM_WEIGHT` | `reference/schema/scoring-constants.md` |
| `GENERIC_COMPLETION_VERBS` | `reference/schema/work-items-and-work-types.md` |
| `GLOBAL_REMEDIATION_BUDGET` | `reference/schema/run-control-and-reliability.md` |
| `GOAL_FAILURE_PATTERNS` | `reference/schema/review-form-and-field-limits.md` |
| `GOAL_FRAMEWORK_NAME` | `reference/schema/review-form-and-field-limits.md` |
| `GOAL_PATTERN` | `reference/schema/review-form-and-field-limits.md` |
| `GOAL_REVIEW_CADENCE` | `reference/schema/periods-and-the-operating-calendar.md` |
| `GOAL_TERM` | `reference/schema/review-form-and-field-limits.md` |
| `GRADUATED_BUCKET` | `reference/schema/scoring-constants.md` |
| `GRID_MAX_TOTAL_WIDTH` | `reference/schema/deliverable-contract.md` |
| `HARD_GATES` | `reference/schema/run-control-and-reliability.md` |
| `HDR_ACTION` | `reference/schema/language-labels-and-messages.md` |
| `HDR_ADDRESS` | `reference/schema/language-labels-and-messages.md` |
| `HDR_APPLICABLE_COUNT` | `reference/schema/language-labels-and-messages.md` |
| `HDR_ASSESSABILITY_RATE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_ASSESSED` | `reference/schema/language-labels-and-messages.md` |
| `HDR_ATTRIBUTABLE_RATE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_AUTHORSHIP_TAG` | `reference/schema/language-labels-and-messages.md` |
| `HDR_BLOCKED` | `reference/schema/language-labels-and-messages.md` |
| `HDR_CITY` | `reference/schema/language-labels-and-messages.md` |
| `HDR_CLEARED_BY` | `reference/schema/language-labels-and-messages.md` |
| `HDR_CLOSE_STATE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_CLOSE_WEIGHT` | `reference/schema/language-labels-and-messages.md` |
| `HDR_CODE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_CODE_MEANING` | `reference/schema/language-labels-and-messages.md` |
| `HDR_COMMITMENT_DATE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_CONFORMANCE_RATE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_DAYS_SINCE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_DIRECTED_BY` | `reference/schema/language-labels-and-messages.md` |
| `HDR_DIRECTED_DATE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_DIRECTIVE_STATUS` | `reference/schema/language-labels-and-messages.md` |
| `HDR_ELIGIBILITY_RULE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_ELIGIBLE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_ENTITY_FOCUS` | `reference/schema/language-labels-and-messages.md` |
| `HDR_EST_UPSIDE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_EVIDENCE_FIELD` | `reference/schema/language-labels-and-messages.md` |
| `HDR_EVIDENCE_RULE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_FAILS` | `reference/schema/language-labels-and-messages.md` |
| `HDR_FLAGS` | `reference/schema/language-labels-and-messages.md` |
| `HDR_IMPLIED_ACTION` | `reference/schema/language-labels-and-messages.md` |
| `HDR_INFLUENCE_OTHER_COUNT` | `reference/schema/language-labels-and-messages.md` |
| `HDR_INFLUENCE_READER_COUNT` | `reference/schema/language-labels-and-messages.md` |
| `HDR_INSTRUCTION` | `reference/schema/language-labels-and-messages.md` |
| `HDR_ITEM_COUNT` | `reference/schema/language-labels-and-messages.md` |
| `HDR_ITEM_GAP` | `reference/schema/language-labels-and-messages.md` |
| `HDR_JURISDICTION` | `reference/schema/language-labels-and-messages.md` |
| `HDR_LAST_ENGAGEMENT` | `reference/schema/language-labels-and-messages.md` |
| `HDR_MEASURE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_MEASURE_PCTILE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_MUST_CLOSE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_NARRATIVE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_NON_ATTRIBUTABLE_CELLS` | `reference/schema/language-labels-and-messages.md` |
| `HDR_PARENT_GROUP` | `reference/schema/language-labels-and-messages.md` |
| `HDR_PEER_NORM` | `reference/schema/language-labels-and-messages.md` |
| `HDR_PLAY` | `reference/schema/language-labels-and-messages.md` |
| `HDR_POSITION` | `reference/schema/language-labels-and-messages.md` |
| `HDR_POSTAL` | `reference/schema/language-labels-and-messages.md` |
| `HDR_PRIORITY_BAND` | `reference/schema/language-labels-and-messages.md` |
| `HDR_PROVENANCE_CLASS` | `reference/schema/language-labels-and-messages.md` |
| `HDR_RANK` | `reference/schema/language-labels-and-messages.md` |
| `HDR_RANK_REASON` | `reference/schema/language-labels-and-messages.md` |
| `HDR_RATE_DIFFERENCE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_ROW_KIND` | `reference/schema/language-labels-and-messages.md` |
| `HDR_SCOPE_RANK` | `reference/schema/language-labels-and-messages.md` |
| `HDR_SCORE` | `reference/schema/language-labels-and-messages.md` |
| `HDR_SPAN_PREFIX` | `reference/schema/language-labels-and-messages.md` |
| `HDR_SPAN_SUFFIX` | `reference/schema/language-labels-and-messages.md` |
| `HDR_STATE_COUNT_PREFIX` | `reference/schema/language-labels-and-messages.md` |
| `HDR_STATE_COUNT_SUFFIX` | `reference/schema/language-labels-and-messages.md` |
| `HDR_UNASSESSED` | `reference/schema/language-labels-and-messages.md` |
| `HDR_UNIT_ID` | `reference/schema/language-labels-and-messages.md` |
| `HDR_UNIT_NAME` | `reference/schema/language-labels-and-messages.md` |
| `HDR_URGENCY` | `reference/schema/language-labels-and-messages.md` |
| `HEADER_MAX_LINES` | `reference/schema/formatting.md` |
| `HEADER_SCAN_DEPTH` | `reference/schema/column-concept-dictionary.md` |
| `HEADLINE_CANDIDATE_THRESHOLD` | `reference/schema/questions-and-interaction.md` |
| `HQ_FLAG_BREADTH_LIMIT` | `reference/schema/priority-sources-and-authority.md` |
| `IDENTIFIER_MIN_WIDTH` | `reference/schema/column-concept-dictionary.md` |
| `IDENTITY_BLOCK_ANCHOR_COLUMN` | `reference/schema/deliverable-contract.md` |
| `IDENTITY_BLOCK_COLUMNS` | `reference/schema/deliverable-contract.md` |
| `ILLUSTRATION_RULE_ENABLED` | `reference/schema/lineage-and-claims.md` |
| `IMPACT_LANGUAGE_RULE` | `reference/schema/language-labels-and-messages.md` |
| `INCENTIVE_PLAN_NAME` | `reference/schema/review-form-and-field-limits.md` |
| `INCOMPLETE_BANNER_TEXT` | `reference/schema/review-form-and-field-limits.md` |
| `INCOMPLETE_PLACEHOLDER_TEXT` | `reference/schema/review-form-and-field-limits.md` |
| `INITIATIVE_STEER_TERM` | `reference/schema/scoring-constants.md` |
| `INLINE_FETCH_CEILING` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `INTENSITY_PER_ITEM_CONCEPT` | `reference/schema/breadth-section.md` |
| `JOIN_OVERLAP_FLOOR` | `reference/schema/measures-and-units.md` |
| `JOIN_UNIQUENESS_FLOOR` | `reference/schema/measures-and-units.md` |
| `JURISDICTION_CONCEPT` | `reference/schema/compliance-and-jurisdiction.md` |
| `JURISDICTION_NAME_TO_CODE` | `reference/schema/compliance-and-jurisdiction.md` |
| `LABEL_NO_PARENT_GROUP` | `reference/schema/language-labels-and-messages.md` |
| `LINEAGE_LADDER` | `reference/schema/lineage-and-claims.md` |
| `LINEAGE_LINE_PLACEMENT` | `reference/schema/review-form-and-field-limits.md` |
| `LINE_HEIGHT_PADDING_PT` | `reference/schema/formatting.md` |
| `LINE_HEIGHT_PT` | `reference/schema/formatting.md` |
| `LINE_SEPARATION_MIN` | `reference/schema/formatting.md` |
| `LOCAL_BOOST` | `reference/schema/priority-sources-and-authority.md` |
| `LOCAL_OVERRIDE_DEPTH` | `reference/schema/priority-sources-and-authority.md` |
| `LOOKBACK_MAY_DIFFER` | `reference/schema/measures-and-units.md` |
| `MAIL_SWEEP_FOLDERS` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `MAIL_SYSTEM_NAME` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `MANDATORY_MULTIPLIER` | `reference/schema/priority-sources-and-authority.md` |
| `MANDATORY_SECTION_LABEL` | `reference/schema/language-labels-and-messages.md` |
| `MATCH_STOPWORDS` | `reference/schema/creditable-entities.md` |
| `MAX_CONCURRENT_WORKERS` | `reference/schema/run-control-and-reliability.md` |
| `MEASURE_EXPONENT` | `reference/schema/measures-and-units.md` |
| `MEASURE_LOOKBACK_TOKENS` | `reference/schema/measures-and-units.md` |
| `MEASURE_RATE_TOKENS` | `reference/schema/measures-and-units.md` |
| `MEASURE_TERM` | `reference/schema/review-form-and-field-limits.md` |
| `MEASURE_TIERS` | `reference/schema/measures-and-units.md` |
| `MEASURE_UNIT_TOKENS` | `reference/schema/measures-and-units.md` |
| `METHOD_OWNER_STATEMENT` | `reference/schema/bundle-identity-and-attribution.md` |
| `METRIC_MULTIPLIERS` | `reference/schema/review-form-and-field-limits.md` |
| `METRIC_SET` | `reference/schema/review-form-and-field-limits.md` |
| `MIME_ENCODING_FACTOR` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `MIN_BREADTH_GAP` | `reference/schema/breadth-section.md` |
| `MIN_POPULATION_FOR_NORM` | `reference/schema/measures-and-units.md` |
| `MIN_POPULATION_FOR_RANKING` | `reference/schema/measures-and-units.md` |
| `MIN_PRIOR_PERIODS_FOR_BAND` | `reference/schema/counterfactual-denominator.md` |
| `MIN_STEM_LENGTH` | `reference/schema/column-concept-dictionary.md` |
| `MISS_SUGGESTION_COUNT` | `reference/schema/questions-and-interaction.md` |
| `MOVING_GROUND_NAME` | `reference/schema/counterfactual-denominator.md` |
| `MOVING_GROUND_SHORT_FORM` | `reference/schema/counterfactual-denominator.md` |
| `MOVING_GROUND_SOURCE` | `reference/schema/counterfactual-denominator.md` |
| `MOVING_GROUND_STATEMENT` | `reference/schema/counterfactual-denominator.md` |
| `MSG_ALERT_LINE` | `reference/schema/language-labels-and-messages.md` |
| `MSG_AUTHOR_LINE` | `reference/schema/language-labels-and-messages.md` |
| `MSG_DEGRADED_RUN` | `reference/schema/language-labels-and-messages.md` |
| `MSG_EMPTY_SECTION` | `reference/schema/language-labels-and-messages.md` |
| `MSG_NO_ACTION_DERIVED` | `reference/schema/language-labels-and-messages.md` |
| `MSG_REFERENCE_SECTION_EMPTY` | `reference/schema/language-labels-and-messages.md` |
| `MSG_SHOWING_N_OF_N` | `reference/schema/language-labels-and-messages.md` |
| `MSG_UNBOUND_VALUE` | `reference/schema/language-labels-and-messages.md` |
| `MSG_UNMATCHED_MANDATORY` | `reference/schema/language-labels-and-messages.md` |
| `NAME` | `reference/schema/bundle-identity-and-attribution.md` |
| `NAMED_THIRD_PARTIES_ALLOWED` | `reference/schema/lineage-and-claims.md` |
| `NARRATIVE_COLUMN_WIDTH_RANGE` | `reference/schema/formatting.md` |
| `NARRATIVE_WIDTH_MAX_UNITS` | `reference/schema/formatting.md` |
| `NARRATIVE_WIDTH_MIN_UNITS` | `reference/schema/formatting.md` |
| `NARROWNESS_MULTIPLIER` | `reference/schema/priority-sources-and-authority.md` |
| `NARROWNESS_THRESHOLD` | `reference/schema/priority-sources-and-authority.md` |
| `NEVER_CUT_LIST` | `reference/schema/review-form-and-field-limits.md` |
| `NON_BLOCKING_BUDGET_FORMULA` | `reference/schema/questions-and-interaction.md` |
| `NON_CLAIMABLE_ENTITIES` | `reference/schema/creditable-entities.md` |
| `NULL_LIKE_VALUES` | `reference/schema/column-concept-dictionary.md` |
| `OBJECTIVE_FIELD_IS_SINGLE` | `reference/schema/review-form-and-field-limits.md` |
| `OPERATING_UNIT_LONG_NAME` | `reference/schema/organization-identity.md` |
| `OPERATING_UNIT_NAME` | `reference/schema/organization-identity.md` |
| `OPERATING_WINDOW_DERIVATION_RULE` | `reference/schema/periods-and-the-operating-calendar.md` |
| `OPERATING_WINDOW_SOURCE` | `reference/schema/periods-and-the-operating-calendar.md` |
| `ORG_AI_USE_POLICY_REFERENCE` | `reference/schema/organization-identity.md` |
| `ORG_NAME` | `reference/schema/organization-identity.md` |
| `ORG_PURPOSE_STATEMENT` | `reference/schema/organization-identity.md` |
| `ORG_SHORT_NAME` | `reference/schema/organization-identity.md` |
| `ORG_VISION_STATEMENT` | `reference/schema/organization-identity.md` |
| `ORIGINATOR_PREFIX_MAP` | `reference/schema/column-concept-dictionary.md` |
| `OUTPUT_DIR` | `reference/schema/deliverable-contract.md` |
| `OUTPUT_FILENAME_PATTERN` | `reference/schema/deliverable-contract.md` |
| `OUTPUT_MEDIUM` | `reference/schema/formatting.md` |
| `OUT_OF_MODEL_CLASS_CONCEPT` | `reference/schema/population-shape.md` |
| `OUT_OF_MODEL_CLASS_LABEL` | `reference/schema/population-shape.md` |
| `OUT_OF_MODEL_ESCAPES_ENABLED` | `reference/schema/population-shape.md` |
| `OVER_LIMIT_REMEDY` | `reference/schema/review-form-and-field-limits.md` |
| `OWNERSHIP_VERBS` | `reference/schema/lineage-and-claims.md` |
| `OWN_ACTION_MARKER_CONCEPT` | `reference/schema/priority-sources-and-authority.md` |
| `OWN_ACTION_MULTIPLIER` | `reference/schema/priority-sources-and-authority.md` |
| `PANEL_SECTION_HEADINGS` | `reference/schema/language-labels-and-messages.md` |
| `PARTITION_CHECKPOINT_PATH_PATTERN` | `reference/schema/run-control-and-reliability.md` |
| `PARTITION_SIZE` | `reference/schema/run-control-and-reliability.md` |
| `PASS_QUALIFIER_VOCABULARY` | `reference/schema/exception-flags-and-thresholds.md` |
| `PEER_SET_ANCHOR_PERIOD` | `reference/schema/counterfactual-denominator.md` |
| `PEER_SET_IS_EXTERNAL` | `reference/schema/counterfactual-denominator.md` |
| `PEER_SET_LEVEL_DEFAULT` | `reference/schema/counterfactual-denominator.md` |
| `PEOPLE_LEADER_OBJECTIVE_REQUIRED` | `reference/schema/role-ladder.md` |
| `PEOPLE_LEADER_OBJECTIVE_SOURCE` | `reference/schema/role-ladder.md` |
| `PERCENTILE_DEFINITION` | `reference/schema/measures-and-units.md` |
| `PERIOD_TOKEN_MAP` | `reference/schema/periods-and-the-operating-calendar.md` |
| `PERSON` | `reference/schema/person-tier.md` |
| `PERSON_BINDING_VERSION` | `reference/schema/person-tier.md` |
| `PERSON_CONFIRMED_FIELD_LIMITS` | `reference/schema/person-tier.md` |
| `PERSON_CONTACT` | `reference/schema/person-tier.md` |
| `PERSON_DISPLAY_NAME` | `reference/schema/person-tier.md` |
| `PERSON_HAS_DIRECT_REPORTS` | `reference/schema/person-tier.md` |
| `PERSON_PREFERRED_LIST_SIZE` | `reference/schema/person-tier.md` |
| `PERSON_ROLE_START_DATE` | `reference/schema/person-tier.md` |
| `PERSON_ROLE_TITLE` | `reference/schema/person-tier.md` |
| `PERSON_SCOPE_CODE` | `reference/schema/person-tier.md` |
| `PERSON_SCOPE_LEVEL` | `reference/schema/person-tier.md` |
| `PERSON_SECONDARY_SCOPES` | `reference/schema/person-tier.md` |
| `PERSON_SUPERVISOR_CONTACT` | `reference/schema/person-tier.md` |
| `PERSON_SUPERVISOR_NAME` | `reference/schema/person-tier.md` |
| `PERSON_UPLINE_CHAIN` | `reference/schema/person-tier.md` |
| `PER_GATE_FAILURE_LIMIT` | `reference/schema/run-control-and-reliability.md` |
| `PLANNING_PERIOD_LENGTH_DAYS` | `reference/schema/periods-and-the-operating-calendar.md` |
| `PLANNING_PERIOD_NAME` | `reference/schema/periods-and-the-operating-calendar.md` |
| `PLAN_AHEAD_RULE` | `reference/schema/periods-and-the-operating-calendar.md` |
| `PLAN_SET_BY_ROLE` | `reference/schema/counterfactual-denominator.md` |
| `PLAN_SOURCE_NAME` | `reference/schema/counterfactual-denominator.md` |
| `PLAY_LABELS` | `reference/schema/breadth-section.md` |
| `PLAY_RULES` | `reference/schema/breadth-section.md` |
| `POPULATION_CENSUS_INTERVAL` | `reference/schema/population-shape.md` |
| `POPULATION_SHAPE` | `reference/schema/population-shape.md` |
| `PRIORITY_BAND_LABELS` | `reference/schema/exception-flags-and-thresholds.md` |
| `PRIORITY_BAND_THRESHOLDS` | `reference/schema/exception-flags-and-thresholds.md` |
| `PRIORITY_SOURCES` | `reference/schema/priority-sources-and-authority.md` |
| `PRIORITY_SOURCE_COUNT` | `reference/schema/priority-sources-and-authority.md` |
| `PRIOR_PERIOD_BASIS` | `reference/schema/counterfactual-denominator.md` |
| `PROCESS_CALENDAR` | `reference/schema/periods-and-the-operating-calendar.md` |
| `PROOF_ACCEPTED_FORMS` | `reference/schema/lineage-and-claims.md` |
| `PROVISIONAL_ADOPTION_MIN_FILL` | `reference/schema/column-concept-dictionary.md` |
| `QUESTION_BANK` | `reference/schema/questions-and-interaction.md` |
| `QUESTION_BATCH_MAX` | `reference/schema/questions-and-interaction.md` |
| `RATE_DENOMINATOR_MUST_MATCH` | `reference/schema/measures-and-units.md` |
| `RATING_AXES` | `reference/schema/review-form-and-field-limits.md` |
| `RATING_SCALE` | `reference/schema/review-form-and-field-limits.md` |
| `REASON_CODE_SET` | `reference/schema/exception-flags-and-thresholds.md` |
| `RECENCY_FLOOR_DAYS` | `reference/schema/exception-flags-and-thresholds.md` |
| `RECENCY_LAG_DISCLAIMER` | `reference/schema/exception-flags-and-thresholds.md` |
| `RECENCY_MEDIAN_FACTOR` | `reference/schema/exception-flags-and-thresholds.md` |
| `REFERENCE_CAP` | `reference/schema/deliverable-contract.md` |
| `REFERENCE_CLASSIFICATION_FIXTURE` | `reference/schema/work-items-and-work-types.md` |
| `REFERENCE_FIXTURE_MATCH_REQUIRED` | `reference/schema/work-items-and-work-types.md` |
| `REFERENCE_VALIDITY_PERIODS` | `reference/schema/periods-and-the-operating-calendar.md` |
| `REGRESSION_CASES` | `reference/schema/run-control-and-reliability.md` |
| `REGRESSION_INVARIANTS` | `reference/schema/run-control-and-reliability.md` |
| `REPAIR_CYCLE_LIMIT` | `reference/schema/run-control-and-reliability.md` |
| `REPORTING_CALENDAR_IS_NOT_AUTHORITY` | `reference/schema/periods-and-the-operating-calendar.md` |
| `REPORT_LINE_JUNIOR_KEY` | `reference/schema/role-ladder.md` |
| `REPORT_LINE_SENIOR_KEY` | `reference/schema/role-ladder.md` |
| `RETRY_BACKOFF_SCHEDULE` | `reference/schema/run-control-and-reliability.md` |
| `RIGHT_ALIGN_COLUMNS` | `reference/schema/formatting.md` |
| `ROLE_FALLBACK_KEY` | `reference/schema/role-ladder.md` |
| `ROLE_LADDER` | `reference/schema/role-ladder.md` |
| `ROLE_TITLE_ABBREVIATIONS` | `reference/schema/role-ladder.md` |
| `ROW_HEIGHT_HEADER` | `reference/schema/formatting.md` |
| `ROW_HEIGHT_SECTION_MIN` | `reference/schema/formatting.md` |
| `ROW_HEIGHT_SPACER` | `reference/schema/formatting.md` |
| `ROW_HEIGHT_TITLE_MIN` | `reference/schema/formatting.md` |
| `ROW_KIND_LABELS` | `reference/schema/language-labels-and-messages.md` |
| `RUNG_DISCLOSURE_REQUIRED` | `reference/schema/counterfactual-denominator.md` |
| `RUN_ESTIMATE_BANDS` | `reference/schema/questions-and-interaction.md` |
| `SAMPLING_DENSITY` | `reference/schema/formatting.md` |
| `SCALE_TIER_BOUNDARIES` | `reference/schema/run-control-and-reliability.md` |
| `SCOPED_RETRY_LIMIT` | `reference/schema/run-control-and-reliability.md` |
| `SCOPE_ATTRIBUTION_IS_TREE` | `reference/schema/scope-hierarchy.md` |
| `SCOPE_CODE_AMBIGUITY_THRESHOLD` | `reference/schema/scope-hierarchy.md` |
| `SCOPE_CODE_PAD_CHARACTER` | `reference/schema/scope-hierarchy.md` |
| `SCOPE_CODE_PAD_DIRECTION` | `reference/schema/scope-hierarchy.md` |
| `SCOPE_CODE_SCHEME` | `reference/schema/scope-hierarchy.md` |
| `SCOPE_CODE_WIDTH` | `reference/schema/scope-hierarchy.md` |
| `SCOPE_FINEST_KEY` | `reference/schema/scope-hierarchy.md` |
| `SCOPE_LEVELS` | `reference/schema/scope-hierarchy.md` |
| `SCOPE_LEVEL_ID_WIDTHS` | `reference/schema/scope-hierarchy.md` |
| `SCOPE_PLAIN_LANGUAGE_MAP` | `reference/schema/scope-hierarchy.md` |
| `SCOPE_RANK_HEADER` | `reference/schema/deliverable-contract.md` |
| `SCOPE_TOP_KEY` | `reference/schema/scope-hierarchy.md` |
| `SCORE_COLUMN_REQUIRED` | `reference/schema/deliverable-contract.md` |
| `SCORE_DECIMAL_PLACES` | `reference/schema/deliverable-contract.md` |
| `SCORE_FORMULA_SHAPE` | `reference/schema/scoring-constants.md` |
| `SCRATCH_DIR` | `reference/schema/deliverable-contract.md` |
| `SECONDARY_UNIT_ID_CONCEPT` | `reference/schema/population-shape.md` |
| `SECOND_ACTOR_RESOLUTION_LADDER` | `reference/schema/scoring-constants.md` |
| `SECOND_ACTOR_UNIT_SUFFIX` | `reference/schema/scoring-constants.md` |
| `SECTION_FONT_SIZE` | `reference/schema/formatting.md` |
| `SELF_ASSESSMENT_PROMPTS` | `reference/schema/review-form-and-field-limits.md` |
| `SENIOR_TIER_PREDICATE` | `reference/schema/role-ladder.md` |
| `SENTINEL_TOKENS` | `reference/schema/creditable-entities.md` |
| `SHOWN_NEVER_SCORED_CONCEPTS` | `reference/schema/compliance-and-jurisdiction.md` |
| `SIBLING_SKILLS` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `SIZE_GATED_PROGRAM_TEST` | `reference/schema/exception-flags-and-thresholds.md` |
| `SOURCE_AUTHORITY_MAP` | `reference/schema/priority-sources-and-authority.md` |
| `SOURCE_BOOST_BOTH` | `reference/schema/priority-sources-and-authority.md` |
| `SOURCE_BOOST_NONE` | `reference/schema/priority-sources-and-authority.md` |
| `SOURCE_BOOST_ONE` | `reference/schema/priority-sources-and-authority.md` |
| `SOURCE_WORKBOOK_LOCATIONS` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `SOURCE_WORKBOOK_NAME` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `SPAN_BLOCK_MAX_COLUMNS` | `reference/schema/scope-hierarchy.md` |
| `SPAN_BLOCK_POSITION` | `reference/schema/deliverable-contract.md` |
| `SPECIFIC_INITIATIVE_NAMES` | `reference/schema/creditable-entities.md` |
| `SPOT_CHECK_SAMPLE_SIZE` | `reference/schema/run-control-and-reliability.md` |
| `STATUS_VALUES` | `reference/schema/review-form-and-field-limits.md` |
| `STEER_TILT_OTHERS_FACTOR` | `reference/schema/scoring-constants.md` |
| `STEER_TILT_TARGET_WEIGHT` | `reference/schema/scoring-constants.md` |
| `SUBMISSION_BOUNDARY_BANNER` | `reference/schema/deliverable-contract.md` |
| `SUBREGION_SUFFIXES` | `reference/schema/compliance-and-jurisdiction.md` |
| `SUPERLATIVE_REQUIRES_TIE_COUNT` | `reference/schema/lineage-and-claims.md` |
| `SUPERVISOR_SWEEP_WINDOW_CURRENT` | `reference/schema/priority-sources-and-authority.md` |
| `SUPERVISOR_SWEEP_WINDOW_PRIOR` | `reference/schema/priority-sources-and-authority.md` |
| `SYNTHESIS_MAX_OBJECTIVES` | `reference/schema/questions-and-interaction.md` |
| `SYNTHESIS_MIN_EVIDENCE` | `reference/schema/questions-and-interaction.md` |
| `SYSTEM_OF_RECORD_EXCLUSIONS` | `reference/schema/systems-of-record-and-capability-bindings.md` |
| `TABLE_STYLE_NAME` | `reference/schema/formatting.md` |
| `TAB_CONTRACT` | `reference/schema/deliverable-contract.md` |
| `TARGET_FILL_RATIO` | `reference/schema/review-form-and-field-limits.md` |
| `TEXT_SEPARATION_MIN` | `reference/schema/formatting.md` |
| `TIE_BREAK_KEYS` | `reference/schema/scoring-constants.md` |
| `TITLE_CASE_HEADINGS` | `reference/schema/formatting.md` |
| `TITLE_FONT_SIZE` | `reference/schema/formatting.md` |
| `TUNING_INVITATION` | `reference/schema/bundle-identity-and-attribution.md` |
| `UNDATED_ITEM_TREATMENT` | `reference/schema/periods-and-the-operating-calendar.md` |
| `UNIT_ACTIONABLE_ACTIVE_MARKERS` | `reference/schema/population-shape.md` |
| `UNIT_ACTIONABLE_NOW_CONCEPT` | `reference/schema/population-shape.md` |
| `UNIT_ACTIONABLE_NOW_VALUES` | `reference/schema/population-shape.md` |
| `UNIT_DRIFT_AUTONORM_FACTORS` | `reference/schema/measures-and-units.md` |
| `UNIT_DRIFT_BAND` | `reference/schema/measures-and-units.md` |
| `UNIT_DRIFT_CANDIDATE_FACTORS` | `reference/schema/measures-and-units.md` |
| `UNIT_DRIFT_CONCENTRATION` | `reference/schema/measures-and-units.md` |
| `UNIT_DRIFT_MIN_PAIRS` | `reference/schema/measures-and-units.md` |
| `UNIT_DRIFT_TOLERANCE` | `reference/schema/measures-and-units.md` |
| `UNIT_ID_CONCEPT` | `reference/schema/population-shape.md` |
| `UNIT_ID_IS_TEXT` | `reference/schema/population-shape.md` |
| `UNIT_LEVEL_KEY` | `reference/schema/population-shape.md` |
| `UNIT_NOT_ACTIONABLE_MATCH_RULE` | `reference/schema/population-shape.md` |
| `UNIT_NOT_ACTIONABLE_SEED_VALUES` | `reference/schema/population-shape.md` |
| `UNIT_NOUN_PLURAL` | `reference/schema/formatting.md` |
| `UNIT_NOUN_SINGULAR` | `reference/schema/formatting.md` |
| `UNIT_OF_BUSINESS_PLURAL` | `reference/schema/population-shape.md` |
| `UNIT_OF_BUSINESS_SINGULAR` | `reference/schema/population-shape.md` |
| `UNRESOLVED_COLUMN_TREATMENT` | `reference/schema/deliverable-contract.md` |
| `UNRESOLVED_STOP_COUNT` | `reference/schema/measures-and-units.md` |
| `UPLOAD_DIR` | `reference/schema/deliverable-contract.md` |
| `URGENCY_VOCABULARY` | `reference/schema/language-labels-and-messages.md` |
| `USER_SIZE_OVERRIDE_ALLOWED` | `reference/schema/deliverable-contract.md` |
| `USER_SIZE_TIER_1_FRACTION` | `reference/schema/deliverable-contract.md` |
| `WIDE_SCOPE_TOKENS` | `reference/schema/scope-hierarchy.md` |
| `WORKLOAD_COUNT_CAP` | `reference/schema/work-items-and-work-types.md` |
| `WORKLOAD_MULTIPLIER` | `reference/schema/work-items-and-work-types.md` |
| `WORK_TYPES` | `reference/schema/work-items-and-work-types.md` |
| `WORK_TYPE_BASELINE_KEY` | `reference/schema/work-items-and-work-types.md` |
| `WORK_TYPE_CLASSIFY_BY` | `reference/schema/work-items-and-work-types.md` |
| `WRITE_CHUNK_SIZE` | `reference/schema/run-control-and-reliability.md` |
| `WRITE_CONFIRM_WAIT_SECONDS` | `reference/schema/run-control-and-reliability.md` |
| `WRITE_VERIFY_TAIL_ROWS` | `reference/schema/run-control-and-reliability.md` |
| `YEAR_PLAUSIBLE_RANGE` | `reference/schema/column-concept-dictionary.md` |
| `ZERO_MEASURE_SORT_KEY` | `reference/schema/scoring-constants.md` |
| `ZERO_MEASURE_TREATMENT` | `reference/schema/measures-and-units.md` |

A variable that is not in this index does not exist. A run that wants one
that is not here has invented it, which standing rule S-NO-LITERALS forbids;
it raises the gap rather than defaulting it.

