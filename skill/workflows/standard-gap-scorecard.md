---
name: standard-gap-scorecard
description: |
  Scores any population against any published standard and reports every gap with a
  reason code. Delivers a colour-coded workbook, or structured markdown carrying the
  same information where no spreadsheet tool exists, in which green means the
  requirement was met, red means a real actionable gap, yellow means the entity could
  not be assessed, and grey means nothing was required of it, with the code written
  into every cell and a plain-language reason in the row margin. Use when someone asks
  what is missing, where they stand against a checklist, standard, protocol, policy,
  baseline or service level, who is out of compliance, which sites, accounts, files,
  cases, assets, staff, shipments or tickets fail a requirement, or asks for a gap
  report, a conformance scorecard, an audit-readiness view or a completion report.
  Fits safety checklists, clinical protocols, service level agreements, brand and
  merchandising standards, licensing and certification, onboarding completion,
  configuration baselines, quality specifications and audit controls. Scope defaults to
  the requester's own unit and widens with their role. Do not use to reformat an
  existing spreadsheet, to rank a population by opportunity rather than by conformance,
  or to evaluate people.
---

# Standard Gap Scorecard

Score a population against a published standard. Report where the standard is met,
where there is a real gap somebody can go and close, and where nothing could be
determined, and never let those three become two.

This skill is one of three that share one configuration. It reads:

- reference/schema/ for every variable name used below. No employer literal appears
  in this file; every literal lives behind a bound name.
- reference/binding-interview.md for how an unbound value behaves. IGNITION is TEN
  organization variables. Everything else is DEFERRED and is requested only at the
  moment a decision needs it, from a person who would know the answer, once.
  `BINDING_OWNER_CONTACT` was the eleventh member and is now DEFERRED, for the reason
  its own schema row states: it is the one ignition candidate no document can supply,
  so it stamped every faithfully documents-bound run PROVISIONAL forever and the
  provisional label stopped distinguishing a recoverable gap from an unrecoverable one.
  Where it is unbound the run is NOT provisional on that account, and the artifact still
  carries that variable's own standing disclosure on every run until it is bound.
- reference/doctrine/ for the shared rules. Rules are cited by ID and never restated.
- reference/output-contract.md for **THE UNIVERSAL OUTPUT CONTRACT**: the output medium
  keyed per skill, the formatting elements with their standards and their
  programmatic verifications, the caret allowance and the computed column widths,
  row heights and header row height, the mandatory rank and reason-for-rank columns,
  rank continuity and the derived last rank, the per-sheet cap and the exact
  showing-note wording, and the unit noun. **Elements are cited by number and their
  standards are never restated here**, because a restated contract is how they
  degraded to passing mentions and stopped being enforced: this skill previously
  shipped with no autofilter on any sheet, no rank column on its main sheet, no
  consolidated reason column and no cap. It also carries the SHEET CLASSES that decide
  which elements bind which sheet, the THREE KINDS of ranked sheet and the rank arithmetic
  of each, the NOTE BAND that is the one place a per-sheet note may sit, and the
  verification matrix that runs before publication. **It governs Step 5 and this file
  cites it rather than restating it.** Where this file and the contract appear to
  disagree, the contract governs and this file is stale.
  **There is exactly ONE output contract, and this is the only bullet in this file that
  names it.** An earlier revision carried two consecutive bullets for it, saying the same
  thing in different words, and a reader of that revision spent a check establishing that
  there was not a second contract somewhere.
- reference/capability-probe.md for what the environment can actually do and what to produce
  when it cannot do everything. Invoked, not duplicated.
- reference/field-resolution.md for finding a concept inside a file this skill has never seen.
  Invoked, not duplicated.

## How to read this file

**What is here, in order.**

| Part | What it settles |
|---|---|
| A | The contract. The five cell states, the three rates, the second number, retired requirements, what varies by role, cold populations, and person-bearing scope levels |
| B | Evidence provenance: the four classes, the ordered procedure that assigns one, the tripwire on a scope-wide unassessable result, and which classifications each class permits |
| C | The workflow. Nine steps, 0 to 6, in an order declared authoritative. Step 5 builds the six tabs against reference/output-contract.md |
| D | Population shape. Which population is being scored and what shape it has |
| E | Degraded runs and what still ships |
| F | Bindings requested at the point of need, keyed by the decision that needs them |
| G | Hard gates. The convention, this skill's group, and what is deliberately not a gate |
| H | Guardrails, restated for checking |
| I | What this skill declares: its bindings, its doctrine, its regression cases |

**Which statement governs when a rule appears more than once.** Several rules are stated
in three or four places, deliberately, because the redundancy is what makes them survive a
partial read. It also means a search returns several hits. The precedence is fixed:

1. **Part A governs everything.** It is the declared contract in the sense of SD-CTR-01,
   and any later instruction that disagrees with it is the defect, not an exception.
2. **The numbered workflow step is normative** for how something is done. Where Part A
   states a principle and a step states a procedure, both hold and the step implements the
   principle.
3. **Part H and Part I are restatements for checking, never sources.** A guardrail and a
   regression case exist so a reader can verify a run; neither creates a rule, and where
   one appears to differ from Part A or from a step, the guardrail is the defect.
4. **A cited doctrine ID governs over this file's paraphrase of it.** This file cites and
   does not restate; where it does restate for readability, the doctrine is authoritative.

**The decision index.** One decision usually needs rules from several places. These are the
ones that cost the most lookups, with everything each needs:

| To decide | Read |
|---|---|
| What one cell is | A1 and A2 for the states; A3 for what the cell carries, including the closed bound pair of pass qualifiers and the codes that stand for them; 4.1 for the ladder in order; B for what the provenance permits; 4.2 for the code; SD-QUA-04 and the resolver's null and absence rules |
| Which provenance class a requirement carries | B1.1 for the ordered procedure and the one case where a tie-break applies; B1.2 for the tripwire that runs before Step 5; B2 for the attestation asymmetry; B4 for naming the layer actually read |
| Whether a requirement is scored at all | 2.2b for authorship; 4.4 for the two tests; 4.4b for the granularity; SD-EXC-14 and SD-EXC-22 |
| What the headline number is | A4 for the three rates and which one leads; A5 for the rung, the level arithmetic and the band; SD-CLM-33 |
| Whether a figure may be compared to other people | A5.1 for the mix test; A4 for the attributable rate; A9 where the comparison level is people |
| What order a reader works the list in | 5.0 for the severity basis and why it is not opportunity; 5.5 for the urgency columns and the filter |
| What the artifact looks like | reference/output-contract.md for every element and the verification; 5.1 for the six tabs and for each sheet's declared class and kind; 5.3 for the column order, its header variables, the artifact-wide frozen span and the grid width bound; 4.6 for the classification column, its fills and the alignment test, which are two separate decisions; 5.4 for the narrative string; 5.10 for where a per-sheet note goes and which sheets ship a showing note |
| Whether a comparison may be drawn | A5 for the rung and the peer rules; A8 for a cold population; A9 for a person-bearing level; 1.6 for a small scope |
| Which population is being scored | D0 and D0.1 for the shape; 3.5 for the window and the evidence's own period stamp; 3.5.1 for the period state; 4.1 step 1 for the exclusions |
| Whether the run is complete | 3b.1 for the manifest; 3b.6 for the six conditions; 3b.8 for the post-build check |
| What stops the run | Part G, and nothing else |

---

# PART A: THE CLASSIFICATION CONTRACT

This part is the declared contract for this skill, in the sense of SD-CTR-01. Every
later instruction is subordinate to it, and any later instruction that disagrees with
it is the defect.

## A1. Five states, and the separation between them is the product

Every requirement, evaluated against every entity in the population, resolves to
exactly one of five states. Not four. Not three. The states, their labels, their symbols
and their fills are `CLASSIFICATION_LABELS`, whose five standing keys are the ones below
and whose taxonomy shape carries, per state, `is_scored`, `is_pass`, `fill_variable` and
`requires_reason_code`. Only PASS and GAP are scored; the other three are shown, counted
separately and excluded from every denominator, which is the mechanism that stops an
unassessable requirement being reported as a failure.

`CLASSIFICATION_LABELS` is never bound to `STATUS_VALUES`. `STATUS_VALUES` holds
per-objective progress on a review form and means on track or behind. These are cell
states in a scored grid and mean met, missed, could not be judged, out of scope and
withdrawn. The two vocabularies look similar and are not, and conflating them makes a
not-required cell count as a behind objective and an unassessable cell count as a gap,
which is the exact inversion this contract exists to prevent.

| State | Meaning | The question it answers |
|---|---|---|
| PASS | The requirement applied, evidence was assessable, and the requirement was met. | Yes. |
| GAP | The requirement applied, evidence was assessable, and the requirement was not met. | No, and somebody can go and fix it. |
| UNASSESSABLE | The requirement applied and should have been evaluated, and the evidence would not support a verdict either way. | Cannot tell. |
| NOT REQUIRED | The requirement did not apply to this entity. Nothing was expected of it and nothing counts against it. | The question does not arise. |
| RETIRED | The requirement is not part of the current standard at all. The column is not built. | The question is no longer asked of anyone. |

The load-bearing separation is GAP against UNASSESSABLE. Most compliance reporting
collapses "we checked and it is missing" together with "we could not check", and that
single conflation is what makes a compliance report untrustworthy and unactionable. A
person sent to an entity because the camera was pointed at the wrong wall, the extract
was empty or the record had not synced yet stops trusting the report, and the report
stops getting used.

The second separation is UNASSESSABLE against NOT REQUIRED. Yellow says somebody needs
to go and look again. Grey says nobody needs to do anything. Collapsing those two sends
people to chase entities that were never on the hook, which is the same loss of trust
arriving by a different road.

RETIRED is separate from all four because a requirement the current standard no longer
carries must be dropped from the scorecard entirely and must never be reported as
failing. See A6.

## A2. The general form of G2 for a cell

SD-EFF-03 says a gate that cannot be evaluated has failed: unknown is not pass. That
governs gates. The cell-level form of the same principle is stronger and is stated
here because an implementer will otherwise apply the gate rule to a cell and produce
red where the honest answer is yellow:

**At a gate, unknown is not pass. At a cell, unknown is neither pass nor gap. It is its
own state, and it carries a reason code saying which kind of unknown it is.**

Both statements are the same rule: never let an absence of evidence resolve to the
answer that is convenient. For a gate the convenient answer is pass. For a cell the
convenient answer is a red mark that makes the report look decisive. Both are
forbidden, for the reason in G3 and SD-WGT-02.

## A3. Every cell carries its code as visible text

A colour is not a classification. Every status cell carries, as characters in the cell:

- the code (`PASS`, `GAP`, `UNASS`, `N/R`), and
- a symbol from the permitted character range: `+` for PASS, `x` for GAP, `?` for
  UNASSESSABLE, `-` for NOT REQUIRED, and
- for anything other than PASS, the reason code.

So a cell reads `x GAP: absent at inspection`, or `? UNASS: no evidence captured this
period`, or `- N/R: not lawful in this jurisdiction`.

**A PASS THAT RESTS ON WEAKER EVIDENCE SAYS SO IN THE CELL, AND THE QUALIFIER SET IS
CLOSED AND BOUND.** Not every pass is a pass of the same kind, and the difference belongs
where the reader is looking rather than in a note somewhere else. A pass tested in full
against the requirement's own met-condition carries the code alone. A pass resting on
weaker evidence carries a QUALIFIER MARK after the code, in parentheses, so that a filter,
a sort and a paste all keep it.

**THE VOCABULARY IS `PASS_QUALIFIER_VOCABULARY`, AND THIS FILE WRITES NEITHER OF ITS
STRINGS.** It is a closed keyed set of exactly TWO entries, looked up BY KEY, each entry
carrying the `label` that states the qualifier in full. The two keys are below; the wording
is that key's bound `label` and nothing else, exactly as 5.5 names the five state keys of
`URGENCY_VOCABULARY` and writes none of its labels. An earlier revision of this section
wrote both strings out in Part A on the ground that no bound variable carried them, and
that request has been granted: the strings now live in the schema, this file names only the
keys, and an organization can state them in its own language without editing this file.

| Key | When it is written | Where the rule that produces it lives |
|---|---|---|
| `attested` | The published standard itself states that attestation satisfies the requirement, and the evidence is the attestation | B2 |
| `presence_only_recency_untested` | The per-row evidence date is missing, so the staleness test could not run and the cell was classified on presence alone | 3.5.2, and 4.1 step 8 is the rung that could not run |

**THE QUALIFIER IS A STANDING QUALIFIER, SO ITS FULL WORDING LIVES IN THE LEGEND AND WHAT
THE CELL CARRIES IS ITS CODE.** reference/output-contract.md 2.7 defines a STANDING QUALIFIER
mechanically, defines where one belongs, and runs a relief ladder over a grid whose summed
built width exceeds `GRID_MAX_TOTAL_WIDTH`; SD-FMT-28 is the doctrine. This qualifier is
one by every part of that definition: it QUALIFIES the cell's own answer rather than
stating it, it is drawn from a CLOSED DECLARED set, and it is written in the SAME WORDS
every time its key appears, so it costs its full length on every row while carrying exactly
one piece of information, WHICH KEY IT IS. That is the definition, and 2.7's first rung
therefore governs it: the wording moves to the Legend, the cell keeps its own answer and a
short declared code, and the Legend entry is MANDATORY and is verified. This file does not
restate the ladder and does not decide where a qualifier belongs; 2.7 decides it once and
this is a lookup.

**THE CODE, DEFINED SO NO RUN AUTHORS A STRING AND TWO RUNS WRITE THE SAME CELL.** The code
for a qualifier is its entry's ORDINAL POSITION in `PASS_QUALIFIER_VOCABULARY`, written as
a number. The set is closed at exactly two entries, its keys are fixed and are never
renamed, and S10's totality validation is what keeps it so, therefore the ordinal is stable
between runs and between organizations, and no string this file authored is ever written
into a cell. So a cell reads `+ PASS`, or `+ PASS (1)`, or `+ PASS (2)`, and where both
hold it carries both inside one pair of parentheses, in the vocabulary's own order,
separated by a comma. **I1 records the schema request that would replace the ordinal with a
bound mnemonic code per entry**, and the moment it lands nothing in this file changes,
because the build reads the vocabulary rather than naming a code.

**THE LEGEND ENTRY IS NOT OPTIONAL AND IS WHAT MAKES THE MOVE LOSSLESS.** The Legend
carries, per key, in one row: the code, the key, that key's bound `label` in the words the
cell used to hold, and what a reader should conclude from a pass carrying it. A code with
no Legend row is an abbreviation the reader has to decode, which costs more than the width
it saved, and it is the one way 2.7's first rung can be done wrongly.

**THE SET IS CLOSED AND ITS TOTALITY IS THE VALIDATION**, per standing rule S10 in
reference/schema/, which runs from the STATES a rule can emit to the SET and never the
other way. There are exactly two ways this file can produce a pass that rests on weaker
evidence than a full test of the met-condition, and the two rows above are those two. A run
may not invent a third and may not reuse the nearer of the two: where some other clause of
a met-condition could not be tested, that is a HOLE in this set and it is reported as one,
routed to `BINDING_OWNER_NAME` exactly as an unmapped reason code is.

**WHERE THE HOLE IS REPORTED, AND IT IS NOT IN THE CELL.** The untested clause is named on
the front panel and in the Legend, per requirement, with the met-condition's own wording for
that clause quoted, and with the evidence that was read in its place named. It is NOT
written into the status cell. Three reasons converge and no reason of any weight opposes
them: 4.1 step 9 keeps the standard's own wording out of the status cell and puts it in the
trailing narrative column; reference/output-contract.md 2.6 requires every populated cell of a
classification column to resolve to exactly one state by a total mechanical rule, which a
free sentence defeats; and a per-requirement fact repeated into every one of hundreds of
cells is the shape 2.7's ladder exists to remove. It is a fact about the REQUIREMENT and
not about the unit, so it belongs where facts about requirements live. An earlier revision
of this paragraph required the cell to say which clause went untested, which the same file
forbade in three other places, and no conforming run could obey both.

**WHY THE MARK IS IN THE CELL AND THE WORDING IS IN THE LEGEND, WHICH IS THIS SECTION'S OWN
ARGUMENT APPLIED TO ITSELF.** The thing that must survive a filter, a sort and a paste is
the FACT that this pass is qualified and WHICH qualifier it carries, and the code carries
both, in the cell, on every such cell. What moves to the Legend is the wording and nothing
else. It was measured on a run whose evidence source carried no capture date on any column:
247 passes on the two requirements whose own met-conditions read "dated within 90 days" and
"dated within the policy term" shipped as ordinary passes, so a reader filtering the census
for green on either got the rows and no signal that the dating half of the stated condition
had never been checked, while the analogous attested pass one column over carried its
label. That failure was a cell carrying NO MARK AT ALL, and a coded mark closes it exactly
as the spelled-out wording did. **The distinction is the whole of SD-FMT-28:** a phrase
unique to its own row is never touched, and a phrase identical on every row that carries it
is representable by a code without losing anything, because the reader reads the sentence
once instead of on every row. A pass that rests on weaker evidence must still say so where
the reader is standing, and half a met-condition untested is the same shape of weaker
evidence as an attestation.

**A QUALIFIER IS NOT A REASON CODE AND IS NOT DRAWN FROM `REASON_CODE_SET`.** That set is
closed at four families, one per NON-PASS state, and its content is the schema's own
documented default, which this file reproduces at 4.2 and does not author. A qualified pass
is a pass and has no home in a set of non-pass families, which is why it has its own closed
pair.

Two independent reasons, both of which have burned real reports:

1. A colour-only sheet is unreadable for a colourblind reader, unreadable when printed
   in monochrome, and unreadable when filtered or pasted elsewhere.
2. A bare code with no reason tells nobody anything. A gap without a reason is not
   actionable, and a reason code is also how a yellow later becomes a green or a red:
   somebody reads `no evidence captured this period`, captures evidence, and the cell
   resolves next run.

Colours are applied in addition, never instead. SD-FMT-14 governs the character range
on both bounds; every symbol above is inside `ALLOWED_CHARACTER_RANGE`.

## A4. The rates, and never one of them alone

The single number most likely to be computed wrongly in this whole skill is the
compliance percentage. Compute and publish two:

- **Pass rate = PASS divided by (PASS + GAP).** The denominator is what was actually
  assessed. This is the answer to "of the entities we could judge, how many met the
  standard".
- **Assessability rate = (PASS + GAP) divided by the eligible count.** This is the
  answer to "how much of what we were supposed to judge could we judge at all".

Never publish `PASS divided by eligible` as the compliance figure. That single division
silently converts every unassessable entity into a failure and destroys the separation
this whole skill exists to protect. The conformance rate and the assessability rate travel
together: wherever one is written, in the artifact or in the reply, the other is written
beside it. Neither ships alone.

**The third rate, and it exists because the first one answers a different question from
the one a peer comparison asks.**

- **Attributable conformance rate = PASS divided by (PASS + GAP), computed over the
  ATTRIBUTABLE cells only.** A cell is attributable when the reader's own action can move
  it. It is not attributable when its reason code names a clearer other than the reader:
  `BLOCKED_EXTERNAL`, and `AWAITING_APPROVAL` where the approver is somebody else. The test
  is the influence test from 4.4 applied at cell granularity, decided by the bound
  `resolvable_by` on the code rather than by a judgment made per cell, so it cannot be
  used to launder a gap into somebody else's column.

The conformance rate and the attributable rate are TWO RATES and they are never
interchanged. The conformance rate is the compliance figure: it counts every scored cell,
including the blocked ones, because the entity genuinely does not conform and an auditor,
a regulator or a customer counts it. The attributable rate is the execution figure: it
counts only what this reader could have changed, and it is the one a peer comparison uses,
per A5.

Three rules hold them together:

1. **Neither ships alone.** Publishing only the conformance rate imports factors the reader
   did not choose into a figure presented as being about them. Publishing only the
   attributable rate hides real non-conformance. Both, always, side by side, each named.
2. **The difference between them is printed as a number**, with the count and share of
   non-attributable cells that produced it, and every excluded cell is still visible in the
   census in its own state with its own code.
3. **The conformance rate is the headline.** It leads, it is what "the pass rate" means
   without a qualifier anywhere in this file, and the attributable rate is introduced by
   name wherever it appears.

**The three names are fixed, with exactly one stated exception, and Part A grants it here
so nothing later has to contradict Part A to take it.** Under the NOT YET STARTED period
state of 3.5.1, the window has not opened, nothing below can be a conformance figure FOR
THAT WINDOW, and 3.5.1 gives the labels all three figures carry instead. That is a
RELABELLING and nothing else: the arithmetic, the denominators, the guard on a zero
divisor, the rule that neither ships alone, the printed difference between the first two,
and which of them leads are every one unchanged. 3.5.1 states the three names once and this
section, 5.2 and 5.6 read them from there rather than each carrying a copy.

Guard the divisor before dividing, per SD-POP-18. Where `PASS + GAP` is zero, the pass
rate is not computed: the cell says `not assessed`, never `0 percent`. The same guard
applies independently to the attributable rate, whose denominator can be zero while the
conformance denominator is not. Never emit a number you could not compute.

Publish the counts as well as the rates: eligible, assessed, pass, gap, unassessable,
not required, per requirement and across the scope. SD-CTR-04 requires both population
figures; SD-POP-20 requires two numbers per funnel step.

## A5. Every rate carries a second number

G4 and SD-CLM-04 apply to a pass rate exactly as they apply to any other figure. A pass
rate of 71 percent is an orphaned fact. It carries the rung named in
`COUNTERFACTUAL_BY_METRIC`, or `COUNTERFACTUAL_DEFAULT_RUNG` where that metric has no
assignment, drawn from `COUNTERFACTUAL_AVAILABLE_RUNGS`:

- share of a bounded addressable population, where the standard defines one;
- a matched control, such as sibling units the standard has not yet reached;
- the peer distribution across sibling units at `PEER_SET_LEVEL_DEFAULT`, which is the
  usual rung for a scorecard;
- attainment against a target set before the period by somebody other than the reader;
- the reader's own prior-period rate, carrying the warning in SD-CLM-04 rung 5;
- the bare denominator, which is the floor and is always available.

**The rung decides the arithmetic, and a quantity that does not exist is never
approximated by a neighbouring one.** SD-CLM-33 carries the rung table and it governs
this skill: which comparative quantity exists, what the classifier does, and what claim
strength is permitted, per rung. Read it there rather than re-deriving it. Three
consequences that bite hardest on a scorecard:

- UNPAIRED is reached only at rung 6, where no comparative quantity is defined. A missing
  benchmark POPULATION is not by itself the floor: a peer set, a control group or a plan
  each supply a comparative quantity without one.
- At rung 4 the quantity is attainment against a target, not a growth rate, and the flat
  state is ON PLAN. A pass rate against a rollout plan lives here and it is a strong,
  ordinary claim.
- A label is computed against `DEADBAND` only where the rung supports one. `DEADBAND` is a
  MAPPING PER RUNG **AND, on the rungs that compare two quantities of different kinds, PER
  QUANTITY FORM**, each band carrying its own named unit, because the unit of the delta
  differs by rung and, on those rungs, by whether the quantity compared is a MOVEMENT or a
  LEVEL. A bare scalar is rejected at validation. Print the band and its unit beside every
  labelled figure. Inside the band, print the delta with its unit and no label.
- **The LEVEL DELTA band is the one this skill lives on** (SD-CLM-34). A scorecard's
  headline is a conformance LEVEL, and a level compared against a comparator level is a
  fourth unit: percentage points of the measure's own rate, not share points, not growth
  points and not percent of target. Rungs 3 and 5 carry a movement band and a level delta
  band, and this skill reads the level delta band. A level delta and a movement delta are
  never banded against each other's band and are never emitted as though they were one
  finding: a rate flat in movement and below the comparator level is two facts.
- The level delta band is derived from the comparator set's OWN spread and takes every rule
  that governs a comparator set: no band where the set is below `ANONYMITY_FLOOR`
  (SD-SPN-16), and none where the set was built by the reader (SD-CLM-30). Rung 6 has no
  band at all, which is a stated absence and not a missing entry.
- The rung-4 band is a fixed percent of target and needs no peer spread, so plan attainment
  carries a label even for a reader who has no peers at all. That matters here: it is the
  one labelled figure available to a top-of-chain reader with no internal peer set. **Which
  is exactly why a documented default may not delete it while the run is holding a target,
  and A5.2 says what happens instead.** Where the target itself is ZERO the rung is still
  available and the finding is still paired; what it loses is the label, and A5.2 says that
  too, because a percent of zero is undefined while a count against zero is not.

**A pass rate is a LEVEL, not a rate of change, and the rung table has no row for a
level.** SD-CLM-33 gives the arithmetic for a rate delta and a proportion delta. A
scorecard's headline figure is neither: it is a conformance level at a point in time, and
with no prior period there is no growth for anybody, so the rung-3 quantity is undefined
while a perfectly good level comparison exists. This skill therefore states the level
arithmetic, per rung, as an extension of SD-CLM-33 rather than as a departure from it. It
adds a quantity the table does not carry; it changes nothing the table does carry.

| Rung | The LEVEL comparison | Label |
|---|---|---|
| 1 share of addressable | Own conformance level minus the addressable set's conformance level, in percentage points of conformance | Against the rung-1 band |
| 2 matched control | Treated level minus control level, in percentage points of conformance | Against the rung-2 band |
| 3 peer distribution | Own level minus the peer median level, in percentage points of conformance, carrying the member count and the tie count | Against the rung-3 LEVEL DELTA band, derived from the absolute pairwise differences between the peer set's own levels. It needs no prior period. Its MOVEMENT band is a different band, is not read here, and a run that reached for it and found no prior period used to emit no label at all |
| 4 plan attainment | Own level divided by the target level, in percent of target | Against the fixed rung-4 band. Always computable |
| 5 own prior run rate | Own level now minus own level at the prior census, in percentage points of conformance, with the uncontrolled-movement warning | Against the rung-5 LEVEL DELTA band, and blocked entirely under a cold population by SD-CLM-31 |
| 6 bare denominator | Undefined. The count with its denominator population | UNPAIRED. The classifier does not fire |

### A5.1 The mix test: a comparison runs on the ATTRIBUTABLE rate, and says how much of the gap was mix

A peer comparison asserts something about the reader's work. Any component of the rate that
the reader did not choose and cannot move is a factor imported into that assertion, and it
contaminates the comparison whenever it is UNEVENLY distributed across the comparison
population. It usually is: a blocked share depends on which counterparties, jurisdictions,
classes or parents a reader happens to hold, and no two readers hold the same mix.

This is the counterfactual denominator failing at its own job. SD-CLM-03 forbids claiming
the movement of a population whose composition the reader did not choose, and the same
prohibition runs in the debit direction: a reader may not be DEBITED for the composition of
a population they did not choose either. SD-CLM-07's environment-credit trap arrives here
as an environment-debit trap, and it is harder to see, because a figure that makes somebody
look worse attracts less scrutiny than one that flatters them.

**The test, and it is arithmetic rather than a threshold, so nothing has to be tuned.**
Before any peer comparison ships:

1. Compute the non-attributable share of the scored cells for the reader, and for every
   member of the comparison population.
2. Publish three numbers: the reader's share, the comparison set's median share, and the
   spread across the set from lowest to highest. Always, whether or not it turns out to
   matter, because a spread of nearly nothing is the evidence the check ran (SD-EXC-06).
3. Compute the comparison BOTH WAYS: the delta on the conformance rate, and the delta on
   the attributable rate.
4. **Publish the attributable delta as the comparison.** Print the conformance delta beside
   it, and print the difference between the two, named for what it is: the part of the
   published gap that is mix rather than work.
5. Where that difference is larger than the rung's own `DEADBAND`, say so in words above
   the figure, naming the share of the gap it accounts for. A reader whose published gap is
   mostly the counterparties they happen to hold needs that sentence, not a footnote.

Computing it both ways costs one extra division and removes the need for any threshold,
any tuning and any judgment about when the contamination is material: the number itself
says how material it was.

**Generalize it, because blocked cells are only the case that was found.** Any component of
a compared figure that satisfies all three of the following contaminates the comparison and
takes this treatment: it affects a cell's classification; the reader did not choose it; and
it is distributed unevenly across the comparison population. Name every such component in
the Legend beside the requirement it affects, so the next one is visible before somebody
has to measure it by hand.

Nothing here changes the conformance rate, the census, the counts or which cells are red.
It changes one thing: which rate is placed on a rung and compared to other people.

**A level delta and a rate delta are different quantities with different units and are
never interchanged.** This is SD-CLM-06's never-interchange rule applied to a third
quantity, and it carries the same requirement: every emitted figure names its unit. Points
of conformance, points of growth and percent of target are three units, and a reader who
reads one as another sees a claim of a different size.

Word the finding at the strength `CLAIM_STRENGTH_BY_RUNG` permits for the rung used, and
name the rung where `RUNG_DISCLOSURE_REQUIRED` is true.

**Precedence: an unbound value never overrides a bound one.** SD-CTR-24. Where a deferred
binding that supplies ONE rung is unbound, it removes that rung and nothing else. The run
then falls to the highest remaining BOUND rung, never past it to the floor, and the
notice names the narrowing rather than a substitution. The floor is reached only when no
bound rung resolves. A business that bound the peer distribution at ignition as its
primary control keeps it when an unrelated deferred map is never bound, and it will
usually never be bound, correctly.

**The peer set is drawn from siblings, never from subordinates.** SD-SPN-14. The resolved
peer level must be strictly COARSER than the requester's own resolved level, and the peer
set is the sibling units at the requester's own altitude inside that coarser level. Test
the resolution: a peer level at or finer than the requester's own is wrong and is
discarded, never used, and no member of the peer set may sit inside the requester's own
scope. Ranking a leader against the entities they manage is internally consistent,
meaningless, and reads to that leader as an accusation.

**A role at the top of the chain has no internal peer set, and that is a stated result.**
SD-SPN-15. Where the requester's own level is the coarsest in the chain there is no
coarser level, therefore no sibling set, therefore no internal peer set. Say so plainly
and do not manufacture one. In order: use an EXTERNAL peer set where
`PEER_SET_IS_EXTERNAL` is true, naming `EXTERNAL_PEER_SET_SOURCE` and its refresh cadence
and stating how stale the release is relative to the run; otherwise drop the peer rung
for that run, fall to the highest remaining bound rung, and name the drop beside every
affected figure. A published outside comparison group is a legitimate and common answer
for a regulated or benchmarked business, and it is bound as a publication and a cadence,
never forced into the organization's own containment chain, which holds only units the
organization owns.

**A peer set that EXISTS and is too small to publish is a THIRD state, and it is not the
one above.** SD-SPN-16. A sibling set of zero is SD-SPN-15's case. A sibling set that is
non-empty and smaller than `ANONYMITY_FLOOR` is a different state with a different
procedure: WALK OUTWARD one level at a time, still strictly coarser than the requester's
own level and still holding no member inside the requester's own scope per SD-SPN-14,
counting again at each level, and STOP at the first level whose set meets the floor. The
walk may not continue past it, because a walk that keeps going is a search for a flattering
comparison rather than for a lawful one. Where the chain is exhausted with no level at the
floor, take SD-SPN-15's mechanism from its first step. A set below the floor is never
published in any form: not a rank, not a position, not a median, not a spread, not as one
of two, and not in generalized wording a reader can invert. **The artifact distinguishes
the three states in three different sentences and never prints one for another:** no peer
set at all; peers exist and were not compared, naming the level, the count, the floor and
that the reason is anonymity rather than absence; and compared, at a named level over a
named count, with the result. A comparison drawn at a coarser level names that level and
the count it yielded beside every figure that reads it, and never inherits the claim
strength a same-level comparison would have carried.

Name `MOVING_GROUND_NAME` beside any period-over-period comparison. Where it is unbound,
its specific consequence is the one stated in its own ignition row and nowhere else: claim
strength is capped, no figure ships at achievement strength, every figure is printed with
its denominator, and the artifact states that no ground has been named. **The run is not
stopped and no number is withheld.** Read the consequence from that row rather than from
the generic line in the binding-states table, which describes what an ignition variable does
in general and not what this one does here. For a scorecard the
ground moves in ways that look exactly like performance: the standard itself changed,
the eligible population churned, an evidence source changed its capture rate, a
jurisdiction changed a rule. A pass rate that rose because a hard requirement was
retired is not an improvement, and SD-CLM-07's environment-credit trap arrives here
wearing that costume.

### A5.2 A target the run is already holding is READ EVIDENCE, not an invented rung

**The failure this section closes, because it is a default deleting the last rung a
particular reader can have.** `COUNTERFACTUAL_AVAILABLE_RUNGS` is an ignition variable and
its documented consequence when unbound is that only the floor rung is available. For most
readers that is a narrowing, and a narrowing is what a default is allowed to do. For the
reader at the TOP OF THE CHAIN it is a deletion, and the deletion is total: rung 3 is
already gone under SD-SPN-15, because there is no coarser level and therefore no sibling
set; rung 5 is gone by definition on a cold population; rung 4 is the rung A5 has just
named as the ONE labelled figure such a reader can have, and the unbound default strikes
it. What is left is rung 6, a bare denominator with no label. Of A8's three mandatory
cold-run findings, the second is then blocked outright by a default rather than by an
absence of evidence, on a run that had a target in its hand and had already read it.

**THE RULE. Where every one of the following holds, rung 4 is AVAILABLE for that figure,
at MEDIUM confidence, as a DERIVED rung:**

1. **`COUNTERFACTUAL_AVAILABLE_RUNGS` IS UNBOUND.** A bound value outranks a derived one,
   and an organization that deliberately omitted plan attainment from its available rungs
   keeps its omission (S9 in reference/schema/, SD-CTR-24). This rule never overrides a
   binding. It fills an absence and nothing else.
2. **A TARGET WAS READ, not sought.** The target came from a document this run ALREADY
   HOLDS under Step 2's source ladder. Never from a fetch made to go looking for a target,
   never from a number this run computed, and never from a figure in a prior artifact this
   skill produced.
3. **THE TARGET IS A QUANTITY**: a number, a proportion, a ceiling or a floor that a
   conformance level can be compared against. A statement of intent carrying no quantity is
   not a target and does not qualify.
4. **ITS AUTHOR IS NOT THE READER.** That is SD-CLM-04's own rung-4 condition, that the
   target was set by somebody other than the reader, and this condition is that condition
   and nothing more. **AN EARLIER REVISION ADDED "AND DOES NOT SIT INSIDE THE READER'S OWN
   SCOPE", AND IT IS DELETED, because it was unsatisfiable for exactly the reader this
   section is written to protect.** A reader at the TOP OF THE CHAIN has every person in
   the organization inside their scope by definition, so every internally authored document
   failed the second half, and the clause struck rung 4 for the one reader whose only
   labelled figure it is, through this section's own condition instead of through the
   default this section overrides. It also attributed a scope test to SD-CLM-04, which
   carries none. Where two clauses of Part A conflict, the one whose stated intent the
   other defeats is the defect.
   **AND THE READER DID NOT SET THE TARGET THROUGH SOMEBODY ELSE**, which is the real
   failure the deleted clause was reaching for and which is stated here as its own test
   rather than as a scope bound. Where the document itself records that the reader SET,
   APPROVED, COMMISSIONED or DIRECTED the target, it is the reader's own target and the rung
   is not derived from it, however junior its author. Where the document ADDRESSES the
   target TO the reader, naming them as the party it binds, the author is somebody other
   than the reader in exactly SD-CLM-04's sense and the condition HOLDS, however far inside
   the reader's scope that author sits: a target somebody sets FOR you is not a target you
   set. Where the document is silent on both, the condition holds on the authorship test
   alone, and the run says in one line that authorship was read from the document's own
   attribution and that the document records no commissioning either way. **The test is
   read from the document and is never inferred from the reporting line**, because the
   reporting line is what made the deleted clause unsatisfiable.
5. **ITS DATE PRECEDES THE OPENING** of the operating window being scored, which is the
   other half of the same rung-4 condition.
6. **THERE IS NO SIXTH CONDITION, AND A TARGET OF ZERO IS NOT ONE.** The commissioning
   test above is the second half of condition 4 and not a condition of its own: both halves
   are one question, WHO SET THIS TARGET, asked of the document rather than of the
   organization chart. A target of zero
   qualifies exactly as any other quantity does. What it changes is the ARITHMETIC of the
   finding and never the AVAILABILITY of the rung, and the paragraph below says what it
   yields.

**A TARGET OF ZERO QUALIFIES, AND HERE IS WHAT IT YIELDS, STATED POSITIVELY.** A target of
zero is a legitimate and common target and it is the one divisor a population guard never
sees, because it does not come from the population at all (SD-POP-18). On a conformance or
servicing standard it is the ORDINARY target rather than an edge case: clear the backlog,
no open request older than the stated age, no unit carrying an open service item into its
renewal conversation. Where conditions 1 to 5 hold and the qualifying target is zero, rung
4 is AVAILABLE and DERIVED exactly as it is for any other target, and the finding it
produces is a COUNT AGAINST THE TARGET:

- **The measured COUNT, its denominator population and the target of zero are printed
  together as ONE PAIRED FINDING**, with the document's title, date and author beside it
  per this section's own disclosure rule: so many units carrying the thing the target says
  should not exist, out of so many in scope, against a target of zero.
- **NO RATIO IS EMITTED AND NONE IS APPROXIMATED. THE CLASSIFIER DOES NOT FIRE AND NO BAND
  LABEL IS PRINTED**, because the rung-4 band is a fixed percent OF TARGET and a percent of
  zero is undefined. SD-POP-18 governs this and this file adds nothing to it: never
  substitute a small number for the zero, never invert the measure to make it divide, and
  never band the count against some other rung's band to recover a label the arithmetic does
  not support. The absence of the label is PRINTED as one line beside the figure, so it
  reads as a stated absence rather than as a figure somebody forgot to classify.
- **IT IS PAIRED, NOT UNPAIRED.** A comparative quantity exists, was read from a named
  document, and is printed beside the figure. Rung 6 is where NO comparative quantity is
  defined, which is not this case, and a run reporting a zero-target finding as UNPAIRED
  would be reporting the absence of the thing it is holding in its hand.
- **A8'S SECOND MANDATORY COLD FINDING IS SATISFIED BY IT**, and the run says so rather than
  recording that finding as blocked. Sequencing against plan is answered by a count against
  a target of zero exactly as it is answered by a percent of a target of forty. What is
  missing is the label and nothing else.

**Why this is a fix and not a licence to invent a band.** The version this replaces struck
the rung outright on a zero target. Every other condition held on a run where the reader
was at the coarsest level of the chain, the population was cold, and the only qualifying
target in hand was a compliance objective written as zero: rung 3 was already gone under
SD-SPN-15, rung 5 by definition, and the guard then took rung 4, so the most senior reader
in the organization received rung 6, a bare denominator with no labelled figure at all,
which is word for word the failure this section opens by describing. **A default that
narrows what a run attempts is doing its job; a guard that deletes evidence the run is
holding is not**, and a guard against a division is not a reason to delete the two numbers
that do not need one. The remedy is to ship the second number without the label, never to
manufacture a label: a band computed on the count rather than on the ratio would be a band
this bundle nowhere defines, in a unit nothing names, and SD-POP-18 says in terms that the
classifier does not fire. **A paired, unlabelled, honestly stated count is a stronger
finding than a bare denominator and a weaker one than a banded ratio, and it is exactly
what the evidence supports.**

**Why this is an application of precedence rather than an exception to it.** S9 orders
precedence downhill from evidence to convention: a value bound at ignition, a value bound
later, **a value derived from the data this run**, then a documented default. A target read
from a named document, carrying its author and its date, IS a value derived from the data
this run, and it therefore sits ABOVE the documented default in that order rather than
below it. The distinction that matters, and the one an implementer should carry away: a
default that narrows what a run ATTEMPTS is doing its job; a default that deletes evidence
the run is HOLDING is not. The two are told apart by exactly one test, which is whether
there is a value in hand.

**What ships with it, every time it fires.** The document's title, its date, its author and
the requirement or scope the target applies to, printed beside every figure that reads the
rung; the rung named as DERIVED rather than as bound, so nobody mistakes it for a
configured control; the claim strength from `CLAIM_STRENGTH_BY_RUNG` for rung 4 and never
higher; the label computed against the rung-4 band, which is a fixed percent of target and
needs no peer spread, EXCEPT where the target is zero, in which case the count against the
target ships with the stated absence of a label per the zero-target paragraph above; and
the derivation written to the provisional record with its evidence per F1, so whoever eventually runs ignition starts from a proposal rather than a
blank page.

**What it may never do.** It never revives rung 3, which SD-SPN-15 struck for a structural
reason no document can repair. It never revives rung 5, which a cold population struck by
definition under SD-CLM-31. It never promotes a figure above rung 4's own strength. It
never assembles a target out of a trend, a prior period's figure, a neighbouring
organization's number or a sentence that merely sounds ambitious. And where no document in
hand carries a qualifying target, **the documented default stands unchanged**, the figure
ships at the floor rung with its denominator population, and the front panel names what one
binding would have changed, per the standing invitation in `TUNING_INVITATION`.

## A6. RETIRED is a rebuild, not a blank column

SD-CTR-13 says a column whose source did not resolve is written blank with its header
present, never dropped. That rule is about a column the contract carries whose evidence
failed to resolve. It does not apply to a retired requirement, because the contract
itself is rebuilt from the standard every run:

- A requirement in the current standard whose evidence column did not resolve is
  written, header present, every cell `? UNASS: no evidence source mapped`, and named
  in the audit. SD-CTR-13 applies.
- A requirement absent from the current standard is not in this run's contract at all.
  No column is built. It is named once in the audit as retired, with the standard and
  date that dropped it. SD-CTR-13 does not apply, because there is no column to blank.

Reporting a retired requirement as failing is the single most common way a scorecard
manufactures a scope-wide crisis out of nothing. It is also the signature of a run that
skipped Part C.

## A7. What the contract fixes and what it does not

Fixed, and identical for every requester at every level: the five states, the reason
codes, the rates and which of them leads, the sections in `TAB_CONTRACT` and their order, the identity
block, the header strings, and every gate. SD-CTR-02, SD-CTR-08, SD-CTR-09.

Varies by role, and only in count: the length of the priority-fixes tab, per
`DELIVERABLE_LINES`. The action list gets shorter RELATIVE TO SPAN as scope
widens, per SD-RNK-09, because a more senior person has less time, not more. It
is never proportional to span. Read that as a share and not as rows: the senior
line's pair is the LARGER pair in absolute rows, and a first tier of twenty over
several thousand units is a far shorter list, for the person holding it, than a
first tier of ten over a hundred.

**THERE IS NO CENSUS EXEMPTION. It is gone, and this paragraph exists so nobody
reinstates it.** An earlier version of this file exempted the census sheet from
`REFERENCE_CAP` on the ground that a capped census could not reconcile against the
manifest. That reasoning was wrong, and it would have shipped a five thousand row sheet
to a five thousand account organization. **Every capped sheet is capped at
`REFERENCE_CAP` independently, per reference/output-contract.md PART 5.1, and the census sheet is capped
like everything else.** Nobody works more than that in a period, and a reader who needs
a narrower view re-runs at a narrower scope, which is the answer the cap exists to force.

The reconciliation objection is answered rather than accommodated: **the manifest
reconciles the RETRIEVED population, not the WRITTEN rows.** Step 3b verifies that every
entity in scope was retrieved and classified; Step 5 then writes the top
`REFERENCE_CAP` of them and states the showing note. The two counts are different
numbers answering different questions, both are published, and the front panel says so
in one line. Completeness is a property of the run; the cap is a property of the sheet.

What varies by role is the size of the action tiers, per `DELIVERABLE_LINES`, and
nothing else. The cap does not vary by role.

## A8. A population with no history of its own

A COLD POPULATION is one where no entity, or almost no entity, has a prior period of its
own. A new site estate, a newly certified fleet, a standard that took effect this period,
a programme rolling out from zero, a reader who took the scope over last month. SD-CLM-27
governs and it is a first-class operating condition, not an arithmetic edge case.

**Two kinds, never conflated.** A COLD ENTITY inside a warm population is already handled
by the classification contract: it has never been assessed, so its cells are
`? UNASS: no evidence captured this period`, it is counted in the assessability rate, and
it is excluded from the pass-rate denominator. Nothing in this section changes that, and
the distinction it rests on is the same one A1 is built around: **never assessed is not
the same answer as assessed and failed.** A COLD POPULATION is where almost every entity
is in that state at once, and where the comparisons the Summary would normally draw are
either undefined or drawn against something the reader's own team is currently building.

**Detected, never declared.** SD-CLM-28. The run detects a cold population from the data,
scoped to the population being scored per SD-POP-23. It does not ask, does not wait to be
told, and does not rely on a binding, because a reader living inside a rollout does not
think of themselves as an edge case. Three tests, any one of which marks the population
cold, all run before scoring:

1. **The history test.** The share of in-scope entities carrying a usable prior-period
   assessment is at or below `COLD_START_MIN_PRIOR_SHARE`.
2. **The entry test.** No in-scope entity has an entry or commissioning date before the
   current window opened.
3. **The uniformity test.** Every assessable cell for a requirement carries the same
   state across the whole in-scope population, which is what no history looks like when
   there is no date to read either.

Record which test fired and the figure that fired it, in the audit and on the front
panel. A detection nobody can see is a guess with better manners.

**What changes when a population is cold:**

- **No WIN, no MISS, no FLAT on any rate.** SD-CLM-31. The classifier does not fire,
  because the label asserts movement and there is nothing to have moved from. The state
  emitted instead is NO BASELINE, it is printed, and it is distinguishable from UNPAIRED
  and from FLAT. A reader must be able to tell "this did not move" from "this cannot be
  compared" from "this has nothing to be compared to yet". Attainment against a plan is
  exempt and keeps its own three states, because it compares against a target rather
  than against a prior period, and a rollout normally has a target.
- **Rung availability is re-evaluated for that population, never inherited.** SD-CLM-29.
  A cold population does not borrow the mature business's rungs. Peers are available only
  where the peers are also cold, because ranking a cold entity against warm peers measures
  age rather than conformance. Own prior rate is struck by definition. Plan attainment is
  normally available and is usually the strongest rung a cold population has. The bare
  denominator is never struck. Name every rung struck and why, beside the figures it
  would have carried.
- **A denominator the reader is building is not a counterfactual.** SD-CLM-30. Where the
  eligible population itself is being created by the same work being scored, a
  share-of-addressable pass rate is the numerator wearing a second name and it arrives
  near 100 percent by construction. Run the independence test per metric, every run, not
  only on a resolution failure: a denominator that resolves and populates is not thereby
  independent. Where the numerator exceeds `ADDRESSABLE_SELF_SHARE_CEILING` of the
  denominator, or where the denominator moves with the numerator across the population
  inside the deadband, the set is self-built. Strike the rung, say so, and name the figure
  that fired the test. Every figure computed against a self-built denominator is capped at
  bounded claim strength whatever rung the organization bound.

**What a cold scorecard may still say, which is not nothing.** SD-CLM-32. Surface all
three without being asked:

1. **Absolute build.** What is in place now that was not in place at the start of the
   period, as a count with its unit and its period: requirements newly met, entities
   brought into conformance, evidence sources newly reaching entities that had none. It
   carries no comparison and needs none.
2. **Sequencing against plan.** Attainment against a rollout target set before the period
   by somebody other than the reader, in percent of target, with the attainment
   classifier. Exceeding a rollout plan is a real result. **Where that target is ZERO, this
   finding is a COUNT AGAINST THE TARGET rather than a percent of it**, with no ratio and no
   classifier, per A5.2's zero-target paragraph and SD-POP-18. That form SATISFIES this
   finding and the run reports it as answered; recording it as blocked, on a run holding a
   target it has already read, is the defect A5.2 exists to prevent.
3. **Execution against a denominator population.** The floor rung, and a legitimate,
   gate-passing claim: so many of so many assessed, with the eligible set named and
   bounded.

A cold run that produces none of these three has not done its job. Absence of a
comparison is not absence of a finding. **Before concluding that the second of the three
is unavailable, apply A5.2**: where the block on it is an unbound rung default rather than
an absent target, and a qualifying target sits in a document this run already read, the
rung is derived rather than struck. The front panel says, in plain words, that this
population has no prior period, that no movement labels were computed for that reason,
and which of the three kinds each figure below is.

## A9. A scope level whose members are PEOPLE

A containment chain may hold a level whose members are individuals: a producer, an
adjuster, a technician, a nurse, a caseworker, a rep. That level is legitimate and common,
and it collides head-on with the rule that this skill never evaluates people. Followed
literally and without this section, the peer-set rule wants siblings at the reader's own
altitude, the summary wants a rollup per scope unit, and the two together produce a table
of named individuals ranked by conformance rate. That is a different artifact with
different consequences from a per-entity gap list, and nobody chose it. It reads as an HR
file, it will be used as one, and it will be produced by accident.

**The decision, and it is contract-level so that everything below is subordinate to it: a
person-bearing level is a legitimate SCOPE and is never a published COMPARISON or
REPORTING axis.**

### A9.1 Detecting a person-bearing level

Detect, never assume, and never wait to be told. A level is PERSON-BEARING when any of:

- its values resolve through the people family of the concept dictionary: assigned to,
  owner, handler, adviser, technician, rep, submitter, clinician, case owner;
- `ROLE_LADDER` binds a role whose `scope_level` is that level, and the members of that
  level are the individuals holding that role rather than units they own;
- its values are free text shaped like personal names, and its cardinality is far below the
  entity count while each value maps to many entities.

**Where it cannot be determined, treat the level as person-bearing.** That default
suppresses a comparison rather than creating one, which is the direction G3 requires: an
unknown never resolves to the reading that manufactures a finding about a person.

### A9.2 What a person-bearing level may do

- **Select a population.** This is the ordinary case and the reason the level exists. "My
  accounts", "this adviser's book", "the cases assigned to me" all resolve through it, and
  nothing here restricts that.
- **Attribute a row.** The level may appear as an identity column naming who owns each
  entity, so a manager can route a conversation and brief by name (SD-SPN-08). A row
  reading "this account, owner named, four open gaps" is a work list. Naming the owner of a
  unit of work is not a judgment of them.

### A9.3 What a person-bearing level may never do

None of the following ships, in any section, at any altitude:

- a rollup, subtotal, rate or count grouped by that level;
- a rank, an ordering or a sort key on that level;
- a named peer comparison, or any figure attributed to an individual by name;
- a span-of-control column used to compare rather than to attribute;
- a section, sheet or heading whose subject is a person.

### A9.4 What replaces each, so the run is not merely blocked

- **The rollup** rolls to the nearest level above it that is not person-bearing. Where
  none exists, publish the scope total alone and say why in one line. Never fabricate an
  intermediate.
- **The peer set** may still be COMPUTED, because the organization may legitimately have
  bound the peer distribution as its second number and A5 needs a value. It is published
  only as an ANONYMOUS DISTRIBUTION: the median, the spread and the count of members, with
  no name, no rank, no position and no ordering. Below `ANONYMITY_FLOOR` members, not even
  that: a positional statement in a small set names somebody by elimination (SD-CLM-12), so
  generalize instead and say the set was too small to describe.
- **The reader's own figure** against that distribution is published as a level delta
  against the median with the count named, never as a place in a list.
- **The span block** keeps the attribution column and drops any grouped figure computed
  from it, and the Legend says in plain words that the census is not a comparison between
  people and must not be used as one (SD-LNG-02).

### A9.5 The interlock, so the accidental version is impossible

An exhortation is not a mechanism. Before any section is written, test every published
GROUPING key, SORT key and COMPARISON axis against A9.1. Any that resolves person-bearing
is not published in that shape, and the substitution in A9.4 is applied and named. This is
condition 6 of the reconciliation gate in 3b.6, it is checked against the built artifact
rather than against the intention, and it blocks the build in the same way the other five
conditions do.

The distinction to hold on to: **this skill scores the conformance of entities. A person
may own an entity, and may therefore appear beside it. A person is never the subject of a
figure.** Where a request asks for the second thing, decline it outright and say why
(SD-LNG-02); where a configuration would produce it by accident, A9.5 catches it.

---

# PART B: EVIDENCE PROVENANCE

## B1. Provenance decides which classifications are permitted

The source of an observation changes what may be concluded from it. Four classes. Every
requirement in the run is tagged with exactly one, by the ordered procedure in B1.1, and
the tag is recorded per requirement in the Legend per B5.

**NOTHING HERE IS LEFT TO THE WORD "FITS".** An earlier version of this section said that
where neither the standard nor `SOURCE_AUTHORITY_MAP` states an evidence rule, the run
should "take the weakest class that fits". The load-bearing word was never defined
anywhere in this file. Read as a severity dial rather than as a description, that sentence
is an instruction to descend the table, and the bottom of the table permits no PASS at
all. On a real standard that states what counts as MET for every requirement and never
states what counts as EVIDENCE, with the authority map unbound on a first run and no
interactive channel to ask, a literal reading tagged every requirement at the weakest
class and published a conformance rate of ZERO PERCENT for an organization whose real
figure was nothing like zero. Every cell was internally consistent, every formatting
element passed, and the reconciliation gate saw nothing, because that gate watches for a
wall of red and this was a wall of amber. B1.1 replaces the sentence with a procedure that
does not depend on an undefined word, and B1.2 is the tripwire that would have caught it.

**The rule that sentence existed to enforce is not weakened, and B1.1 keeps it:** an
unknown is never defaulted to the class that maximizes the score. G3 and SD-WGT-02 govern
here exactly as before.

Where the requirement's author is external and the external standard specifies its own
evidence rule, its own sampling method or its own acceptable provenance, **that rule
governs over the internal one**, and the Legend names which rule was applied to which
requirement. An external standard that requires observed evidence is not satisfied by an
internal decision to accept attestation, and applying the internal rule silently produces
greens the standard's own author would not accept. Where the external standard is silent,
the internal rule applies and the Legend says so.

| Class | What it is | PASS permitted | GAP permitted |
|---|---|---|---|
| DIRECT OBSERVATION | Somebody or something examined the entity and recorded what was there: an inspection, a photograph, a meter reading, a machine recognition result, a physical count. | Yes | Yes |
| SYSTEM EXTRACT | A field in a system of record that structurally cannot hold the value unless the thing happened: a completed training record, a signed document on file, a configuration read back from the device. | Yes | Yes |
| ATTESTATION | The party being scored asserted it: a self-report, a checkbox the entity's own operator ticked, a survey return, a verbal confirmation logged by the person accountable for the result. | Only where the standard itself states that attestation satisfies the requirement, and only labelled as attested | Yes |
| INFERENCE | Derived from a proxy rather than observed: the requirement is assumed met because a related field is populated, because a correlated event occurred, or because a model predicts it. | No | No |

### B1.1 The provenance procedure, in order, stopping at the first step that answers

Run the steps in order. Stop at the first one that resolves. Record, per requirement,
WHICH step decided it and WHAT it read, in the Legend per B5 and in Method, so a reader
can see the judgment rather than inferring it from the colour of the grid.

1. **THE BOUND EVIDENCE RULE.** Where `SOURCE_AUTHORITY_MAP` carries an entry for this
   requirement that answers "what counts as evidence", take the class that entry
   describes. A bound value outranks everything below it, per SD-CTR-24 and standing rule
   S9 in reference/schema/.
2. **THE STANDARD'S OWN EVIDENCE RULE.** Where the published standard states what evidence
   it will accept for this requirement, take the class that rule describes. Where the
   requirement's author is external and the external rule differs from the internal one,
   the external rule governs, per the paragraph above, and the Legend says which rule was
   applied to which requirement.
3. **THE MET-CONDITION, READ AS A DESCRIPTION AND NOT AS A DIAL.** Where neither of the
   above says anything, classify from what the requirement's own MET-CONDITION describes.
   A class is chosen because it says what the evidence IS, never because of where it sits
   on a strength ordering:
   - a met-condition naming a RECORD, a filed document, a signed artifact on file, or a
     system state that structurally cannot exist unless the thing happened, is
     **SYSTEM EXTRACT**;
   - a met-condition naming an ASSERTION BY THE PARTY BEING SCORED, their signature, their
     confirmation, their tick, their survey return, is **ATTESTATION**;
   - a met-condition satisfied only by somebody EXAMINING the entity, an inspection, a
     photograph, a meter reading, a physical count, a recognition result, is
     **DIRECT OBSERVATION**;
   - **INFERENCE IS NEVER REACHED BY THIS STEP AND IS NEVER A DEFAULT.** It has exactly
     one use, and B3 states it: the run itself derived the value from a proxy rather than
     reading it. A requirement is never tagged INFERENCE because nothing else was stated.
4. **WHERE THE MET-CONDITION DESCRIBES MORE THAN ONE CLASS, TAKE THE WEAKEST OF THE
   CLASSES IT DESCRIBES, AND NEVER A CLASS IT DOES NOT DESCRIBE.** The candidate set is
   exactly the classes step 3's bullets matched on this requirement's own wording, so this
   step chooses INSIDE a set the description supplies and never descends the table looking
   for something weaker still. It therefore cannot reach INFERENCE, which step 3 forbids it
   to reach, and it cannot reach a class the met-condition says nothing about.

   **THE LAYER THE RUN ACTUALLY READ CAN LOWER THE RESULT AND CAN NEVER RAISE IT.** Where
   the evidence layer this run reached, per B4, is WEAKER than the weakest class the
   met-condition describes, the class is that layer's, because a description of what the
   evidence WOULD be is not evidence about what was actually read. Where the layer read is
   STRONGER, it is disclosed under B4 and it changes no class. Stated as one line: **the
   class is the weaker of the weakest class the met-condition describes and the class of
   the layer actually read.**

   **BOTH DIRECTIONS HAVE NOW FAILED ON A REAL RUN, AND THE RULE IS STATED SO THAT NEITHER
   CAN RETURN.** An earlier version of this step said to take the class of the evidence
   layer the run ACTUALLY READ. 3.2.1 says this skill joins an evidence extract onto a
   population on essentially every run, so the layer actually read is a system extract on
   essentially every run, and that sentence therefore resolved EVERY ambiguous requirement
   to SYSTEM EXTRACT: the STRONGER class, which the guarantee below forbids in terms, and
   the reading that makes B2's attestation asymmetry unreachable. At an organization whose
   standard requires observation, `? UNASS: attested only, standard requires observation`
   could then never be assigned to a requirement whose evidence arrives through an extract,
   and the artifact is a wall of greens where the honest answer is amber. It was measured on
   one requirement whose met-condition is a signature by the party being scored, which step
   3's bullets put on BOTH SYSTEM EXTRACT and ATTESTATION: 134 cells resolved to the
   stronger class and shipped as unqualified passes. The failure in the OTHER direction is
   the one B1 opens with, where "the weakest class that fits" descended the whole table and
   published a conformance rate of zero percent for an organization whose real figure was
   nothing like zero. **This step descends nothing and defaults nothing.** It chooses among
   the classes the description itself supplies, and the layer actually read can only lower
   that choice.
5. **WHERE THE MET-CONDITION CANNOT BE READ AT ALL**, the provenance is UNRESOLVED and is
   not defaulted to anything. Every cell for that requirement is
   `? UNASS: provenance unresolved, evidence rule not stated`, the requirement is named on
   the front panel and in the Legend with what would resolve it, and B1.2 is tested before
   anything is published.

**THE GUARANTEE THIS PROCEDURE MUST KEEP, STATED SO A LATER EDITOR CANNOT LOSE IT.** A
class is never chosen because it produces more passes. Step 3 reads a description, and a
description is not adjustable to taste. Step 4's tie-break moves toward the WEAKER class
and never toward the stronger one, and the layer B4 names can lower a class and can never
raise one. Step 5 refuses to choose at all rather than choosing conveniently. **The
guarantee and step 4 now say one thing in two places rather than two things in one
section**: an earlier revision stated the guarantee here and a procedure eleven lines above
that resolved every requirement to the stronger class, and a reader following the procedure
literally could not have kept the guarantee at all. Where the two ever appear to differ
again, the guarantee is the statement of intent and the step is the defect, per the
precedence rule in How to read this file. And B2 is untouched: a class that PERMITS a pass does not thereby produce
one, attestation becomes a pass only where the standard itself says attestation suffices,
and every such cell carries the `attested` qualifier code from A3.

**A class decided at step 3 is a MEDIUM-confidence reading and is recorded as one**
(SD-CNF-03). It is written to the provisional record with its evidence per F1, never to
the organization config, so a binding owner confirms or corrects it once for everybody
rather than the run re-deciding it every period. Where `INTERACTIVE` is present and the
run still has budget under Part F, the step-3 decision worth spending it on is the one
that moves a published number furthest, which is how Part F measures cost and how
SD-CTR-28 requires it to be computed on this run rather than read from a table.

### B1.2 The provenance tripwire, because a classification decision can produce a scope-wide result

**WHERE A PROVENANCE DECISION WOULD MAKE MORE THAN HALF THE SCORED CELLS ACROSS THE WHOLE
SCORECARD UNASSESSABLE, STOP AND SAY SO BEFORE PUBLISHING ANYTHING.** Compute it once,
after B1.1 has run over every requirement and before Step 5 builds anything: the count of
cells that would be UNASSESSABLE BECAUSE OF THE PROVENANCE CLASS ASSIGNED, over the count
of cells that would otherwise have been scored. Publish the two numbers whatever the
result, because a count that did not fire is the evidence the test ran (SD-EXC-06).

**Why this exists, and why nothing already in the file covers it.** 3b.6 condition 4 and
the `universal_gap_unconfirmed` gate protect the reader from a scope-wide GAP, on the
reasoning that a requirement failing across a whole eligible population is far more often
a broken mapping, a retired requirement or a wrong eligibility test than a real collapse.
The mirror case had no protection at all. One provenance decision, taken once, over a
standard that never states its evidence rule, turns the entire grid amber: there is no red
wall for condition 4 to see, no all-null column for condition 3 to see, a conformance rate
that is arithmetically correct over a denominator of almost nothing, and an artifact that
verifies clean end to end. **A wall of amber is as scope-wide a result as a wall of red,
and it is harder to notice, because amber reads as honesty.**

**The majority is definitional, not a tunable.** It is the same majority the two disclosure
tests in 4.4 and 4.4b use, stated the same way for the same reason: a figure computed over
a minority of the work is not the figure its own name claims to be. No threshold is bound
for it and none should be.

**What fires.** The gate `provenance_unassessable_unconfirmed` in G2. Where `INTERACTIVE`
is present it asks one question and stops, naming each requirement, the class B1.1 assigned
it, which step of B1.1 assigned it, the count of cells that decision made unassessable, and
the three likelier causes: an evidence rule nobody has bound, a met-condition naming a
record that was read as an assertion, and an evidence source the run could not reach. Where
`INTERACTIVE` is absent the question cannot be asked, so the bannered incomplete path in
reference/capability-probe.md 2.14 rung 2 applies and the artifact ships with the question named at
the top of the front panel ABOVE every rate, per SD-EFF-05.

**What the tripwire may never do.** It never resolves itself by promoting a class. A
tripwire that repaired its own trigger by moving requirements up the table would be exactly
the defaulting-to-the-flattering-answer failure G3 forbids, arriving dressed as a fix.

## B2. The asymmetry on attestation, and why it is not squeamishness

**Self-reported evidence must never silently become green.**

A self-reported positive is the party being scored marking their own work. It is
admissible as a PASS only where the published standard says attestation is sufficient,
and even then the cell carries the `attested` qualifier code from A3, and the Legend
publishes that code against its full wording and says what it means.
Where the standard requires observation and only attestation exists, the cell is
`? UNASS: attested only, standard requires observation`.

A self-reported negative is admissible as a GAP without qualification. Somebody
declaring their own shortfall is strong evidence of a shortfall, and treating it as
unassessable would mean the honest reporter is scored better than the silent one.

That asymmetry is the same rule as SD-WGT-02: position the default so that doing the
work can only help. Under this rule, replacing attestation with observation can turn a
yellow into a green and can never turn a green into a yellow.

**AND WHERE AN ATTESTATION CONTRADICTS A COLUMN THAT RESOLVED, THAT IS A THIRD STATE AND
NEITHER SIDE WINS AUTOMATICALLY.** SD-CNF-10 governs it and this file cites it rather than
improvising. The two states this section already knows about are an attestation with nothing
to check it against, which the ladder above handles, and an attestation the evidence
confirms. A person's own statement that a RESOLVED column contradicts is neither: it is not
unsourced, because it traces to a cell, and the cell says something else. **A run that picks
a winner has decided a question of fact it cannot see, and it decides it the same way every
time**, which is worse than getting it wrong once. So: the cell is `? UNASS` with the
matching reason, it is excluded from both conformance denominators and named in the exclusion
list rather than dropped silently, **both readings are printed** in the row's narrative entry
and in the Legend, the person's statement in their own words and what the resolved column
says with its column and its unit named, together with the question that would settle which
is right, and the run never averages the two and never publishes the disputed value.
**CONTRADICTED, UNSOURCED and UNVERIFIED are three labels with three remedies** and this
skill keeps them apart exactly as it keeps GAP, UNASSESSABLE and NOT REQUIRED apart, for the
same reason: collapsing them sends somebody hunting for a file when what was needed was one
sentence from a person. Above `UNRESOLVED_STOP_COUNT` contradicted items the run stops, because
many contradictions at once are evidence about the extract rather than about the people.

## B3. Inference produces a lead, never a verdict

An inferred result is at best a MEDIUM-confidence reading, and SD-CNF-01 is explicit
that a low or medium confidence inference never becomes a sentence. In this skill it
never becomes a cell colour either. An inferred result yields
`? UNASS: inferred only, not observed`, and the inference itself is written into the
row margin as a lead worth checking, with its confidence named per SD-CNF-03.

An implementer will be tempted to score an inference green when it is confident. Do not.
A confidently wrong green is the exact failure the whole classification contract exists
to prevent, and unlike a yellow it is not recoverable, per SD-CNF-07.

## B4. Name the evidence layer you actually read

Where the evidence is a derived result rather than the underlying observation, say so
plainly and never describe the derived result as if it were the observation.

Worked example. A recognition service photographs each site and publishes a structured
result saying which of a set of required elements it detected. The photographs
themselves sit behind authenticated, encrypted links that this environment cannot
retrieve, and that is the design, not a failure: the recognition results are available
precisely because reading the images is not required. A run built on those results says
"recognition result" everywhere and never says "we looked at the photo". If asked to
look at a photograph, say plainly that the images are not reachable from here, name why,
and deliver the scorecard from the recognition results instead.

The general rule: state which layer of evidence each finding traces to, and never claim
to have inspected a primary artifact you read only a derivative of. This is SD-CNF-08
applied to provenance rather than to arithmetic.

**THIS SECTION IS A DISCLOSURE RULE, AND IT IS ASYMMETRIC WHERE IT REACHES INTO
CLASSIFICATION.** What it governs is how a finding is WORDED: the layer is named, every
run, on every requirement, in the Legend and in Method. It is not a way of choosing a
provenance class upward. B1.1 step 4 states the one direction in which the layer read
touches the class at all: where the layer actually read is WEAKER than the weakest class
the met-condition describes, the class drops to it; where the layer read is stronger, the
class does not rise. Reusing this section as a general classification rule inverted the
direction B1.1's guarantee promises and resolved a whole grid to the stronger class, which
is why the asymmetry is written into both places rather than left to be inferred from one.

## B5. Provenance is recorded per requirement, in the Legend

Every requirement's provenance class appears in the Legend section beside its name. A
reader must be able to see, without asking, which greens were observed, which were
attested, and which requirements could produce no verdict at all.

---

# PART C: THE WORKFLOW

Nine steps: 0, 1, 2, 3, 3b, 4, 4b, 5, 6. The order is authoritative in the manner of
SD-POP-02: several steps below claim to run first, and this ordering is the one that
satisfies all of them.

Step 2 is MANDATORY and is never skipped for convenience. **It is not a stop.** Reading
the published standard belongs to no HARD_GATES group, per SD-SRC-21. Where the standard
cannot be reached after the full ladder in 2.1, the run continues on the fallback ladder
in that section, banners itself as standard unconfirmed per 2.9 and Part E, names the
exact release it scored against with its date, and never presents the result as
authoritative. A missing standard is a disclosure, not a stop, per SD-SRC-13 and
SD-EFF-02.

## Step 0. Probe the environment

Run the probe in reference/capability-probe.md Part 1, in full, before anything else. Do not
restate it here and do not skip it to save time: SD-EFF-01 says run length is not a cost
this method recognizes, and a run that discovers at the build stage that it cannot write
a workbook has already spent the budget the fallback needed.

The probe record decides:

- whether the deliverable is a workbook, a workbook labelled formatting-unverified, or
  structured markdown carrying identical information (reference/capability-probe.md 2.1 and 2.2);
- whether the standard in Step 2 can be reached and parsed (DOC_STORE, DOCUMENT_EXTRACT,
  WEB);
- whether the evidence in Step 3 can be reached (SYSTEM_OF_RECORD, FILE_READ);
- whether the completeness architecture in Step 3b can checkpoint and fan out
  (FILE_WRITE, CODE_EXECUTION);
- whether a deferred binding may be requested at all this run (INTERACTIVE).

The probe halts the run only on `shared.source_unreadable`, which is the gate declared
in Part G that reference/capability-probe.md 1.6 describes. Everything else degrades and
announces its degradation in the artifact, per C1 of that file and Part E below.

## Step 1. Resolve who is asking, and over what population

Work the ladder in SD-IDN-12 and stop at the first hit. Never ask for something the
records already hold.

1. **Identity and role.** Resolve the requester's own record in full, not only the
   title, then the manager relationship as a separate call (SD-IDN-01: a profile record
   carrying no manager field can never answer who somebody reports to, and using it for
   that returns a confident wrong answer rather than an error). Expand
   `ROLE_TITLE_ABBREVIATIONS` before matching, run the `WIDE_SCOPE_TOKENS` test first
   and record the token that decided it, then match against `ROLE_LADDER.titles`
   (SD-IDN-03, SD-IDN-04). Where nothing resolves, use `ROLE_FALLBACK_KEY`, which is
   bound to the narrowest role so an unknown never inflates a claim or a list size.

2. **Default scope from the role.** The default population is every entity at and below
   the requester's own `scope_level` in `SCOPE_LEVELS`, filtered to their
   `PERSON_SCOPE_CODE`. That is the general rule the source case is an instance of: a
   front-line role defaults to its own finest owned unit; the role one step up defaults
   to the unit that contains it; a role at rank 0 applies no filter at all (SD-IDN-10,
   which is a normal path and not a degraded one).

3. **An explicit scope in the request always wins.** Accept a short code or a plain
   phrase, identify the level from the code width in `SCOPE_LEVEL_ID_WIDTHS` or from the
   word used, and pad it yourself (SD-IDN-11). Never ask the user to pad and never reject
   a short code. Resolve an ambiguous code against the data, not against its own pattern
   (SD-IDN-07), and tie-break word first then role (SD-IDN-08). Zero rows on the first
   filter means the filter is wrong before it means the scope is empty (SD-IDN-16):
   re-test the comparison as text on both sides (SD-IDN-09) and re-test the level reading
   before concluding anything.

4. **Resolve the requirement subset from the phrasing.** A broad request ("what are we
   missing", "where do we stand") takes every requirement the standard scores this
   period. A narrow request naming one requirement, one family of requirements or one
   programme takes that subset plus its trend. Route the phrase to a column family before
   searching any column, per SD-QUA-01, and never run a match across the whole sheet, per
   SD-QUA-02. A phrase that routed to a family but matched no value stops before scoring
   and asks, offering the `MISS_SUGGESTION_COUNT` nearest values present (SD-QUA-10). A
   phrase that routed nowhere runs the request without that term and labels the output
   unqualified. Never silently widen (SD-QUA-12).

5. **Do not add a person filter where the source already restricts by viewer.** Where the
   evidence source enforces row-level access, the returned population is already the
   requester's. Adding a second filter on the person silently narrows it again. Record in
   the audit which restriction was relied on.

Batch every ambiguity into one message (SD-IDN-17). Offer distinct values with a
recognizable label and a count beside each, and accept a name or a list position, not
only a code (SD-IDN-13). Narrow before asking (SD-IDN-14). Persist a settled answer and
verify the save succeeded (SD-IDN-15).

### 1.6 Two degenerate scopes, and they are different failures

Run both tests before scoring. They look alike in the output and they have opposite
fixes, and collapsing them is the same class of error as collapsing a gap with an
unassessable entity.

**Test one, the binding error: is the unit of business COARSER than the reader's own
scope?** Detect it rather than assert it (SD-POP-26). The scope level whose distinct
value count over the in-scope population equals that population's record count is the
level at which one entity sits; that is `UNIT_LEVEL_KEY`, and where it is unbound it is
read from the data this way and the reading is named. Where MORE THAN ONE level satisfies
the test, which is always so when the reader's in-scope population holds exactly one
record, take the FINEST matching level. Compare it against the reader's own resolved
level, and report a binding error ONLY where the reader's own level is strictly finer than
EVERY level that satisfies the test over a population of MORE THAN ONE RECORD. Over a
population of one record the detection is uninformative: say the scope holds one entity
and do not assert a configuration mismatch that cannot be distinguished. SD-POP-26. Where the entity level is coarser, this reader owns a PART of an entity
rather than a set of them and cannot receive an entity-level scorecard at all. Say so
before the content, name both levels, and name the level that would produce a scorable
population for them. This is a binding error, not a small population, and it is reported
as one.

**Test two, the honest small population: does the reader's own scope contain fewer than
`MIN_POPULATION_FOR_RANKING` entities?** This is common and correct. A single-site
manager, a single-crew supervisor, a single-vehicle operator and a single-book adviser
all live here, and a compliance scorecard has more readers in this state than any other
kind of report has.

What changes, and it is only the comparative half (SD-POP-25):

- No cross-entity ranking, no percentile, no median, no distribution and no peer
  language, however well the arithmetic behaves. Never print a rank of one out of one.
- Say it on the front panel BEFORE the content, in plain words: this scope holds n
  entities, so nothing here is ranked and no cross-entity comparison is drawn.
- Name every suppressed comparison by name, so the reader sees what was not attempted
  rather than assuming it was attempted and came back empty.
- Name the scope level that would produce a rankable population for this reader.
- Peer language is suppressed for a second and independent reason at the top of a chain,
  per SD-SPN-15 in A5. The two suppressions are reported separately.

What does NOT change, and this is the point: **the scoring unit of this skill is the
requirement, not the entity.** A reader who owns one site scored against forty
requirements receives forty classified cells, forty reason codes, a real pass rate, a
real assessability rate, a real priority-fixes tab and a real legend. Every one of those
numbers is computed over requirement-cells rather than over entities, so none of them is
degenerate at a population of one. Deliver all of it, and do not route the reader
elsewhere.

That is the difference between this skill and a ranking skill, and it must read
correctly. A reader who owns exactly one entity is the commonest reader a compliance
scorecard has, and telling them their scope is too small to report on would be both
wrong and the fastest way to lose them.

## Step 2. Read what is actually being scored. MANDATORY, never assumed

**Do not run a scorecard from a requirement list held in this file, in a previous run,
in memory, or in the requester's head. Read the published standard, every run, before
querying any evidence.**

This is the step that gets skipped, and skipping it is the failure mode this skill exists
to prevent. Scoring against an assumed standard rather than the real published one
produces an artifact that is internally consistent, confident and wrong, which is the
shape SD-QUA-12 names as the failure that destroys trust. It gets worse at a new company,
not better: at a company the implementer knows, a stale requirement list is merely out of
date; at a new one it is fiction.

**Mandatory means never assumed. It does not mean the run stops.** SD-SRC-21 settles
this, and the heading is worded the way it is on purpose: the real requirement is that
the requirement set comes from the document rather than from memory or inference, and a
heading reading "never skipped" reads as a stop and will be implemented as one. Reading
the standard is in no HARD_GATES group. Where it cannot be reached, 2.9 governs.

Worked example, neutral. A chain publishes next period's brief on the twenty-fifth for a
period beginning on the first. Somebody running the scorecard on the twenty-second cannot
reach it, because it does not exist yet. The correct behaviour is to score against the
current release, name it and its date, banner the run, and continue. The incorrect
behaviour is to return nothing.

### 2.1 Find the authoritative copy, and only that copy

`SOURCE_AUTHORITY_MAP` answers, by question, which artifact settles what (SD-PRI-32).
Three of its seven questions matter here: who defines the quality bar, what counts as
evidence, and who defines local targets. Resolve the artifact for each.

- Discover the path every run. Read the actual folder list and select by name content,
  ignoring leading numerals, punctuation and spacing (SD-SRC-14,
  `DOC_STORE_PATH_DISCOVERY_REQUIRED`). Reference values in the config are a starting
  point for discovery, never a hard-coded path. Two consecutive periods' folders in one
  library commonly differ by a single space after a numeral, and a literal path breaks
  the first period somebody types it differently, silently.
- **One authoritative location. Never a staging copy, never a mirror.** A standard
  library commonly holds three kinds of copy: the live released set, a staging area for
  the next period that is not yet in force, and mirrors elsewhere that were correct once.
  Read the live released set only. If a search surfaces a copy outside it, discard the
  copy and go back to the authoritative location.

  Worked example. A published guide set holds one document per jurisdiction, refreshed
  each cycle, in a folder whose name says it is the live space, beside a sibling folder
  whose name says it is the preparation space for the next cycle. A months-old copy of
  one jurisdiction's guide also sits in an unrelated communications library. Only the
  live space is read. The preparation space is unreleased and scoring against it scores
  requirements nobody has been told about yet; the communications mirror scores last
  year's.

- Apply the expiry gate per cached block, per SD-SRC-17, against
  `REFERENCE_VALIDITY_PERIODS`. Within validity, use the block and do not re-crawl. Past
  validity the block is stale and may not be used until refreshed. If the refresh fails
  after the retry ladder, use the stale block, record that it is past validity and could
  not be refreshed, and continue (SD-SRC-18): a stale reference is a disclosed limitation
  and a halted run is a dead end. Report any refreshed content back in the closing
  summary so one file stays authoritative (SD-SRC-19).
- A missing central source is never a stop (`CENTRAL_BRIEF_REQUIRED` is false, SD-EFF-02,
  SD-SRC-13). A search that comes back empty means the folder was not matched, not that
  nothing was published. Walk the fallback ladder: the target period's release, then the
  current period's, then the most recently published one, dated honestly.

### 2.2 Read the scored block, not the promoted block

A standard document almost always separates **what is measured** from **what is being
pushed this period**. They are different lists, the second is usually narrower or wider
than the first, and they sit on the same page. Build the requirement set from the scored
block. Never infer scoring from the promotion block.

Worked example. A period guide carries a block headed with the scored focus and a second
block headed with the current initiative focus. The scored block says a site must carry
either of two acceptable age-verification notices. The initiative block is narrower: one
notice in sites with an automated verification terminal, the other in sites without.
Scoring the initiative rule creates a false gap at every site that displays the
acceptable alternative. The scored block is a single combined requirement satisfied by
either notice, and it is scored as one requirement, never as two.

Also read, where the standard carries them:

- **Entity categorization.** Which class of entity a requirement applies to, including
  variants that read almost identically. A requirement written for a category "with a
  named attachment" and a requirement written for the same category "without" it are two
  different eligibility tests, and reading one for the other silently mis-scores an
  entire class.
- **Exclusion tests published inside the standard.** Physical, contractual or size
  thresholds that remove an entity from scoring. Worked example: a standard excludes a
  site from one requirement when the fixture is under a stated width and under a stated
  shelf count, where the width is held in one system and the shelf count is only visible
  in the observation itself. Both must be checked; checking one gives the wrong exclusion
  set.
- **Effective dates.** Requirements that begin measurement in a future period, and
  requirements paused mid-period.
- **Prioritization order** where the standard states one, so the worklist in Step 5 can
  order by the organization's published weights rather than by the writer's opinion
  (SD-PRI-31, `METRIC_SET` weights where an incentive or scorecard plan is bound).
- **Measurement level** per requirement (`METRIC_SET.measurement_scope_level`). A
  requirement whose official score is computed at a level above the entity cannot produce
  an entity-level verdict. See Step 4b.

### 2.2b Resolve who AUTHORED each requirement, and never assume it was this organization

Every requirement in the set is tagged with its author before anything else is decided
about it: INTERNAL, published by this organization, or EXTERNAL, published by a regulator,
an accrediting body, a standards organization, a licensing authority, a payer, a customer
or any other party outside it.

The tag is not decoration. Six decisions in this skill read it, and each of them was
written by somebody who assumed the author was internal. That assumption is wrong at every
regulated, accredited, licensed, certified or contractually governed business, which is
most of the businesses that need a compliance scorecard at all.

| Decision | What changes when the author is EXTERNAL |
|---|---|
| Scored or shown, 4.4 | Nothing. External authorship never routes a requirement out of the scored block on its own. Only a separate finding that compliance is determined above the reader does |
| Edition verification, 2.3 | The edition is verified against the standard's own effective-from and superseded-by dates, not against this organization's operating window |
| Precedence, 2.6 | An internal document cannot amend what an external standard requires. It can only govern this organization's own scoring of it |
| Retirement, 2.8 | A requirement is retired by its own author. An internal document cannot retire an external requirement |
| Pausing, 4.1 step 3 | An internal pause suspends this organization's scoring, not the requirement. The requirement stays in force and the cell stays scored |
| Evidence rules, B1 | Where the external standard specifies its own evidence rule, sampling method or acceptable provenance, that rule governs over the internal one, and the Legend names which was used |

Where the author cannot be determined, record it as unresolved and treat the requirement
as EXTERNAL for every decision above, because every one of those defaults is the one that
keeps a requirement scored, in force and visible. G3 requires that direction: never
default an unknown to the value that suppresses a finding.

### 2.3 Verify the edition

Every published standard carries an edition marker: a cover date, a version, a period
name, an effective-from line. Confirm the edition read is the one in force for the period
being scored. Where it is not, do not trust it silently: warn on the front panel, name the
edition actually read and the period actually scored, and continue. SD-SRC-15 is the
reason: a run that quietly scores the wrong period is indistinguishable from a correct one
until somebody is standing in front of the work.

**An external standard keeps its own calendar and it will not match yours.** Verify an
externally authored edition against its own effective-from and superseded-by dates, never
against this organization's operating window. A standard refreshed annually in a fixed
month is the current edition for eleven months in which no internal release matches it,
and treating that mismatch as staleness produces a warning on every run until the warning
stops being read. State the standard's own effective dates and the period scored, both,
and warn only where the edition read has actually been superseded or has not yet taken
effect.

### 2.4 Multi-jurisdiction scopes read every jurisdiction in scope

A scope wider than one jurisdiction commonly spans several sets of rules. Resolve the
distinct values of `JURISDICTION_CONCEPT` present in the population, read every
jurisdiction's standard, and score each entity against its own jurisdiction's rules.
Never apply one jurisdiction's requirement set to another's entities.

Convert a place name to its stored code through `JURISDICTION_NAME_TO_CODE` and then
match exactly (SD-QUA-05). Coincidental substring containment is never evidence. Strip an
administrative suffix before matching and route the phrase to that one column
(SD-QUA-06). Where no jurisdiction-specific document exists, fall to
`COMPLIANCE_GUIDE_MASTER` and record which entities were scored against the fallback.

### 2.5 Parsing a document built for the eye

Standards are written for readers, not parsers. Apply SD-PRS-02: extract with layout
preserved first; if layout mode is unavailable or a pairing is ambiguous, read the page
as an image and treat that as a normal tool rather than a last resort; pair by proximity
and confirm against a second reading. Report how many pairings were confirmed by two
readings, how many rest on one, and how many could not be paired.

**Two extractors fail differently on the same document. Try a second before concluding a
document is unreadable, and record which one worked.** Worked example: a set of
linearized documents on which one extraction library reports a missing root object and
refuses, while a second library reads them without difficulty. A run that stops at the
first library reports the standard as unavailable and falls back to an assumed
requirement list, which is the worst outcome available at this step.

### 2.6 Precedence when sources disagree

Precedence is by question, not by document rank (SD-PRI-32). Within one question, the
most recent and most specific artifact governs, and the disagreement is named in the
audit rather than resolved silently.

The usual ordering, generalized: the current period's release outranks the standing
guide; the standing jurisdiction guide outranks a national or default guide; a dated
amendment or bulletin outranks the guide it amends for the topic it names; and the
programme definition document settles definitions, weights and exclusions but not
period-specific pauses. Where two artifacts disagree on the same question, follow the
nearer and more recent and say so.

**That ordering runs inside one authorship, never across two.** An internally published
release is the nearer and more recent document, and on an externally authored requirement
it still cannot amend what the standard requires. Split the question: the external
standard settles WHAT is required and WHO it applies to; the internal document settles
WHETHER and HOW this organization scores it this period, and what it wants pushed. Where
the two appear to disagree about the requirement itself, that is not a precedence question
and it is not resolved by recency. It is a discrepancy: score the external requirement,
name both documents and their dates on the front panel, and say plainly that an internal
document states something different. An internal restatement that has drifted from the
standard it restates is a common and quiet failure, and this is the only place the run can
catch it.

Worked example. A monthly internal release states that scoring of one internally authored
requirement is paused for this period. The standing internal guide still lists it. It is
paused, marked `- N/R: paused this period`, and the release is named as the authority.

Worked example, the same shape with an external author. A monthly internal release states
that the organization will not score one externally published requirement this period. The
requirement is still in force and the entity is still exposed to it. It is NOT marked
`N/R` and the cell is NOT greyed. It stays scored, and the internal decision not to score
it is disclosed on the front panel as a scoring pause with the release named. Writing an
internal scheduling decision into a cell as though the obligation had lapsed is the same
class of error as reporting an unassessable entity as compliant.

Worked example. A dated bulletin says one requirement launched in a first wave of
jurisdictions; a later bulletin says a second wave was postponed in a different set. The
first wave is unaffected by the second bulletin. Read both, apply per jurisdiction, and
name both in the Legend.

### 2.7 State the requirement set before querying anything

Before touching the evidence, state to the requester: which requirements are in scope for
this period and this jurisdiction, which evidence field backs each one, which provenance
class each carries and which step of B1.1 assigned it, and which requirements were retired,
paused or not yet effective.
This is cheap, it is the last moment a wrong requirement set can be caught for free, and
SD-EFF-38 says stopping to ask costs no correctness.

### 2.8 Retire what the standard no longer carries

Any requirement absent from the current standard is dropped, per A6. Where an evidence
field exists with no counterpart in the current standard, label it `RETIRED`, exclude it,
and never report it as a gap.

**A requirement is retired by its own author.** An internal document cannot retire an
externally authored requirement, and its absence from an internal restatement is not
evidence that the external standard dropped it: it is more often evidence that the
restatement is incomplete or out of date. Retire an external requirement only on the
external standard's own withdrawal, supersession or effective-until date, and name the
external edition that retired it. Where an internal document omits a requirement the
external standard still carries, score the requirement and name the omission on the front
panel.

Worked example. An evidence source still carries a column for a discontinued programme.
The current standard scores its replacement, which is satisfied by either of two pricing
notices. A run that reports the discontinued programme as missing across the scope is
reading a stale list and has skipped this step. That signature is worth watching for:
a requirement failing at or near 100 percent of the population is far more often a
retired requirement, a broken evidence mapping or a wrong eligibility test than a real
scope-wide collapse.

### 2.9 When the standard cannot be read at all

Say so plainly. Name the requirement list actually used and where it came from. Flag the
whole run on the front panel and in the first line of the reply as **standard
unconfirmed**, using `MSG_DEGRADED_RUN` with both slots filled: the source that could not
be read, and the effect on the output. Never silently proceed on an assumed list. This is
a degraded run, not a failed one, and Part E governs it.

## Step 3. Resolve the evidence and map every requirement to it

### 3.1 Find the evidence source

Search `SOURCE_WORKBOOK_LOCATIONS` in order for `SOURCE_WORKBOOK_NAME`, or reach the
bound system of record. Where a discovery interface does not index the source, use the
search interface that does, and record which route worked. Where an identifier resolution
call fails but the identifier itself is usable directly, use it directly and record the
working path in the audit so the next run does not repeat the failure.

Worked example, generalized from a real case: a catalogue call does not list the analytic
model at all, so the model is found through a general search; the returned address then
fails the call that converts an address into an internal identifier, while the identifier
embedded in that same address works when passed straight to the metadata, schema and
query calls. Both facts belong in the audit, and neither is a reason to stop.

### 3.2 Resolve columns by concept, never by literal header

Apply reference/field-resolution.md in full. Do not restate it here. The parts that bite hardest
in this skill:

- Score containers by resolvable required concepts, never take the first on faith, and
  break ties by record count rather than by the reported extent (F1.2, F1.4, SD-PRS-11).
- Detect the header row rather than assuming it, and confirm the choice by resolving the
  required concepts (F2, SD-PRS-13).
- Run exact, then prefix, then substring, each pass to completion (F3.3, SD-PRS-14), with
  the short-string guard in F3.4.
- Confirm every resolved column by its values, not only by its name (F3.6, SD-PRS-16).
- **A resolved but empty column is an absent column** (F3.8, SD-PRS-18). This is the
  single most damaging false positive available to a scorecard: a wholly empty evidence
  column reports every eligible entity as failing that requirement. Check the non-null
  count within scope before using any evidence column, and where it is zero, mark the
  requirement `? UNASS: evidence column present but empty` and name it in the audit.
- Resolve any strict concept by exact name only, never by a neighbouring column in the
  same synonym group (F3.7, SD-POP-05). This is the failure no gate can catch: because
  the intended class is usually a subset of the neighbouring class, removing on the
  neighbour removes all of them too and every downstream invariant still passes.

  Worked example: two scope columns whose names differ by a suffix and whose row counts
  differ slightly. Filtering on the wrong one returns a population that is nearly right,
  reconciles against itself, and is not the requester's.
- **No stem belongs to two concepts, and a tie on a strict concept is never broken by
  position** (SD-PRS-47). Where two concepts both produce an exact match on the same
  header and either is strict, NEITHER resolves: the header is reported as ambiguous,
  both candidates are named, and every feature both feed is skipped and named. Never
  break such a tie by column position, by dictionary order, or by which pass reached it
  first. The live case for this skill is in 4.1 step 1.
- **On a FIRST RUN, a strong candidate the dictionary does not carry has a route** (7.4a).
  Every other route in that section is keyed on who decided, and two of the four decide
  nothing at an organization that has bound nothing and has no interactive channel, so a
  run could see a column that plainly answers a concept, find no route that permits using
  it, and publish a zero. A zero from an unresolved concept looks exactly like a zero from
  a genuine absence, which is the conflation this whole skill exists to prevent, arriving
  one layer below the classification ladder. Take that route on its own terms: provisional
  adoption for this run only, at the confidence it states, disclosed where it states, and
  never written to the organization config.

#### 3.2.1 Where the evidence sits in a SECOND file, JOIN it on the identifier

**SD-PRS-48 governs, and this skill performs that join on essentially every run.** The
population and the evidence are routinely two different files: a roster keyed on the unit
identifier, and an evidence extract keyed on the same identifier with one column per
requirement. Leaving the second file unread is not the conservative choice. It is a
decision to score every requirement it carries as unevaluated when the evidence to score
them truthfully was in the same input set.

**A JOIN IS NOT A CONCATENATION**, and the run states which it did. Concatenation adds ROWS
from files of the same shape and de-duplicates (SD-PRS-12). A join adds COLUMNS from a file
of a different shape and adds no row to the population.

**The four preconditions, every one of which must hold before any join is performed:**

1. **THE SAME IDENTIFIER CONCEPT RESOLVES ON BOTH SIDES**, by 3.2's ordinary rules on the
   STRICT reading, through `UNIT_ID_CONCEPT`. A key matched by position, by row order, by
   name similarity or by any fuzzy comparison is not a join key. A compound key is
   permitted where every part of it resolves on both sides.
2. **THE KEY IS UNIQUE ON THE ENRICHING SIDE.** Count the distinct key values against the
   row count of the evidence file. Where it holds more than one row per key the join is
   REFUSED, unless a stated rule collapses the duplicates, and that rule and its collapse
   count are printed. A one-to-many join silently multiplies rows, which is how a join
   corrupts a scored population.
3. **THE KEY IS COMPARED AS TEXT**, trimmed, with the identifier's own formatting
   preserved and leading zeros intact (`UNIT_ID_IS_TEXT`, SD-SPN-06). A numeric read of an
   identifier is not a key.
4. **THE JOIN IS LEFT, FROM THE POPULATION BEING SCORED.** The eligible population is
   fixed by Step 1 and Step 3.4 before the join and is not changed by it.

**THE ROW COUNT BEFORE THE JOIN EQUALS THE ROW COUNT AFTER IT. Assert it, and a change in
either direction blocks** rather than being explained away. It is asserted again in 3b.6
against the manifest, which is a second reading of the same fact from a different place.

**Both non-matching sides are reported, not one:**

- **A SCORED UNIT WITH NO MATCH IN THE EVIDENCE FILE KEEPS ITS PLACE IN THE POPULATION.**
  The enriched columns are UNRESOLVED for that row and are written blank per SD-CTR-13,
  **never zero, never a default and never a negative**.
- **AN EVIDENCE ROW WITH NO MATCH is counted and named, never silently discarded.** A large
  unmatched remainder on the evidence side is the evidence that the two files key
  differently or cover different scopes, and it is the ONLY warning this run gets before it
  trusts a bad key. Report it as a count even when it is zero, because a zero is the
  evidence the check ran (SD-EXC-06).

**THE INTERACTION WITH THE CLASSIFICATION LADDER, AND IT IS THE WHOLE REASON PART A
EXISTS.** A unit that did not match the evidence file is NOT a unit whose evidence says the
requirement was not met. Those are the two things A1 was written to keep apart, and a join
is the commonest way they get collapsed, because an unmatched row and a failing row look
identical once a blank has been read as a zero. **Every cell of an unmatched unit resolves
UNASSESSABLE, at step 8 of the ladder in 4.1, reading
`? UNASS: no evidence captured this period`.** It is counted in the assessability rate, it
is excluded from both conformance denominators, and it is never GAP, never red and never
folded into a gap count. A term computed over an unresolved column is NOT SCORED for that
row and says so, because an absent record is not evidence of a negative.

**A JOIN THAT LANDS AND CANNOT BE SCORED HAS NOT ANSWERED THE FAILURE THIS SECTION EXISTS
FOR, AND THE JOIN IS ONLY HALF THE FIX.** SD-PRS-48 now says so in terms. The joined columns
must then RESOLVE to the concepts the requirements need, by 3.2's ordinary routes, and the
commonest shape a real evidence file has is the one that defeats the ordinary uniqueness
test: **ONE COLUMN PER MEMBER of the published requirement set**, which means those columns
TIE WITH EACH OTHER for the same concept by construction, and a uniqueness rule written to
refuse an ambiguous PAIR refuses the whole SET. Measured twice on real books: eight boolean
columns each clearing the value check and the fill floor, none adopted, and the requirements
they carried unevaluated on all 190 rows with the file joined and sitting open beside the
population. **The route for exactly that shape is the DECLARED SIBLING SET in
reference/field-resolution.md 7.4b**, which separates a set of siblings from an ambiguity by its own
tests and adopts the set as one entry naming every member. Run it. A run that performs the
join, reports a match rate of a hundred percent and then scores nothing from it has moved
the failure rather than closed it, and the artifact cannot tell that apart from a file that
was never opened.

**SO THE DISCLOSURE SAYS, PER JOINED COLUMN, WHETHER IT RESOLVED TO A CONCEPT OR WAS CARRIED
UNREAD.** A joined column nothing reads is indistinguishable in the artifact from a column
that never arrived, and the count of each is what tells a reader which of the two happened.
Where a joined column was carried unread, name it and name the requirement that goes
unevaluated as a consequence, exactly as the READ AND NOT JOINED path below does.

**THE DISCLOSURE, wherever a joined term is used and once in full in Method and the
Legend:** the file joined, the key used, the columns it added, **whether each added column
resolved to a concept or was carried unread**, the MATCH RATE as matched of
scored, and the unmatched count on EACH side. A requirement whose evidence arrived by join
is readable as such, so a reader who distrusts the key can see exactly how much of the
answer depends on it.

**WHERE ANY PRECONDITION FAILS, THE FILE IS READ AND NOT JOINED.** Record it in exactly
those words, name the condition that failed, and name every requirement that goes
unevaluated as a consequence, each of which is `? UNASS: no evidence source mapped` under
3.3. The cost is made visible rather than left invisible. Never join on a weaker key to
avoid the disclosure, and never treat a refused join as a reason to stop the run.

### 3.3 Never invent a requirement-to-evidence mapping

Every requirement in the run is mapped to exactly one evidence field, and the mapping is
recorded in the Legend. A requirement with no confirmed evidence field is
`? UNASS: no evidence source mapped`, is stated as such in the report, and is raised with
the requester. **Never substitute a nearby field.** A mis-mapped field silently scores the
wrong thing, produces a full column of confident results, and passes every reconciliation.

Worked example. A standard scores a requirement that the evidence source physically
cannot see, because the observation method cannot distinguish it from an adjacent variant.
The cell is `? UNASS: not detectable by this evidence source; verify in the operational
system`, not a gap and not a pass. Naming the system where a human can check it is what
makes the yellow actionable.

### 3.4 Eligibility is resolved before the verdict

For every requirement, resolve its eligibility test before evaluating any entity:

- the entity class the standard names;
- any published eligibility or targeting field in the evidence;
- any election, enrolment, contract or programme participation the standard requires;
- any jurisdictional permission;
- any exclusion test published inside the standard;
- the effective-from period.

An entity failing the eligibility test is `N/R` with the specific reason. An entity whose
eligibility cannot be determined is `? UNASS: eligibility could not be determined`, never
`N/R` and never `GAP`. Guessing eligibility in either direction is forbidden: guessing it
open manufactures gaps, and guessing it closed hides them.

**The proper-subset guard, applied to eligibility.** Where an eligibility or targeting
rule is resolved from an ABSENCE, as most of them are, apply the guard in
reference/field-resolution.md 3.12 and SD-QUA-04: an absence rule yields a usable subset only
where the complement is a PROPER, NON-EMPTY subset. Where the field is blank on every row
in scope, or populated on every row in scope, the distinction does not exist in this
population. Record the eligibility rule as NOT PRESENT, do not apply it, classify every
entity `? UNASS: eligibility could not be determined`, and name it in the audit.

The reason this guard belongs here and not only in the resolver is that both readings of a
resolved-but-full absence manufacture a scope-wide result and neither trips any other
check. Read as all-eligible, the requirement produces a wall of red or amber over
entities it was never meant to touch. Read as none-eligible, it produces a wall of grey
that reads as an all-clear, which is the same failure as 4.4 arriving from a different
direction. A subset equal to the whole population is not an eligibility rule; it is the
population under a second name.

### 3.5 Take the current period by default, and record the evidence age

Resolve the period being scored through the operating window
(`PLANNING_PERIOD_NAME`, `PLANNING_PERIOD_LENGTH_DAYS`, `OPERATING_WINDOW_SOURCE`, or
`OPERATING_WINDOW_DERIVATION_RULE` where the published window cannot be read, disclosed as
derived per SD-PRS-05). A relative phrase such as "this period" is not a named period
(SD-SRC-15) and falls through to the calendar rules. The reporting calendar is never the
authority (SD-SCO-03): a fiscal or calendar quarter end is only ever an input the
operating window converts.

**WHERE THE EVIDENCE'S OWN PERIOD STAMP NAMES A DIFFERENT WINDOW FROM THE ONE THE CALENDAR
RULES RESOLVE, THE RUN DOES NOT SILENTLY PICK ONE.** Two period resolutions are in play on
almost every run and until now neither section mentioned the other: this section resolves
the window the run is SCORING, and 3.5.2 rung 2 reads a period stamp inside the evidence
SOURCE, a banner row, a column of extract dates, a period token in the filename. They
usually agree. Where they do not, the choice is not cosmetic: it decides whether the three
headline figures carry A4's names or 3.5.1's readiness names, and it moves the anchor the
urgency column bands against, which moves rows in and out of the `overdue` state wholesale.
On a measured run the two readings were a month apart and 62 of 190 rows changed state
between them, and nothing in this file required either reading to be disclosed. A run that
quietly scores the wrong window is indistinguishable from a correct one until somebody is
standing in front of the work, which is SD-SRC-15's own statement of the harm.

**THE RULE, AND IT IS S9's PRECEDENCE APPLIED RATHER THAN A NEW ONE.** Compare the resolved
window against the evidence source's own period stamp, every run, before any cell is
classified:

1. **Where they name the same window**, say so in one line and continue. A match stated is
   the evidence the comparison ran (SD-EXC-06).
2. **Where they differ AND the resolved window was DERIVED** rather than read from a
   published source, that is, `OPERATING_WINDOW_SOURCE` did not resolve and
   `OPERATING_WINDOW_DERIVATION_RULE` produced the dates under SD-PRS-05, **THE STAMPED
   WINDOW GOVERNS.** S9 orders precedence downhill from evidence to convention, and a value
   derived from the data this run sits ABOVE a value produced by a documented rule. The
   evidence is the thing being scored, and it carries its own statement of which window it
   describes.
3. **Where they differ AND the resolved window was READ from a published source or bound**,
   the BOUND value governs, per S9 and SD-CTR-24. A value derived from the data never
   overrides one the organization actually bound, and the disagreement is then a finding
   about the evidence rather than about the window: the source may be a period behind, or
   the wrong extract may have been supplied.

**BOTH WINDOWS ARE NAMED ON THE FRONT PANEL WHATEVER THE OUTCOME, AND THE DIFFERENCE IS
PRINTED AS A COUNT.** Name the resolved window and its origin, the stamped window and where
the stamp was read, which of the two governed and under which of the three cases above, and
**the number of rows whose urgency state differs between the two readings**. Where the
period STATE also differs between the two, say that too, because one reading may be IN
PROGRESS and the other NOT YET STARTED, and 3.5.1 renames all three rates under the second.
A reader who cannot see that the choice existed cannot judge the report.

#### 3.5.1 Check that the period has STARTED, and say which of three states it is in

Resolving a window is not the same as checking it has begun. Compare the run date against
the resolved window and record one of three states, on the front panel, in the reply and in
the audit. A run that does not make this comparison will happily score a window that opens
weeks after the run date, and nothing else in the method objects.

| State | Test | What the artifact publishes |
|---|---|---|
| NOT YET STARTED | the window opens after the run date | A READINESS view, defined below. No conformance rate for that window |
| IN PROGRESS | the window has opened and has not closed | Both rates, labelled partial-period, with the elapsed share of the window named beside them |
| CLOSED | the window closed on or before the run date | Both rates, unqualified |

**NOT YET STARTED is not a refusal and not an error.** Asking where we stand against next
period's standard is a reasonable and common question, and the honest answer is a readiness
view rather than a conformance rate:

- Publish the requirement set that takes effect on the window's start date, the eligible
  population, and every cell classified against evidence held NOW.
- Publish the figure as a **READINESS rate**, defined in the Legend as conformance measured
  today against a requirement set that takes effect on a stated future date. It is
  explicitly not a conformance rate for that window and it is never compared against a
  closed period's conformance rate. Naming it correctly is the whole fix: the arithmetic is
  useful and only the label was wrong.
- **THE RENAMING COVERS ALL THREE OF A4'S RATES, AND THIS IS THE ONE PLACE IT IS STATED.**
  A4 fixes the three names, 5.2 and 5.6 both mandate them BY NAME on sheets that must ship
  under this period state, and a rule that renamed one of the three and said nothing about
  the other two left the front panel and the Summary required to publish two figures under
  names this section had just forbidden. The three labels are:

| A4's name for it | Its label under NOT YET STARTED | Why |
|---|---|---|
| The conformance rate | **Readiness rate, conformance basis** | It is a conformance computation over a window that has not opened, so the word conformance survives only as the basis and never as the claim |
| The attributable conformance rate | **Readiness rate, attributable basis** | The same computation over the attributable cells only. It is renamed for the same reason and it is still published beside the first, because neither ships alone |
| The assessability rate | **Assessability rate**, unchanged | It is a COVERAGE figure and not a conformance one. It answers how much of what was to be judged could be judged, which is as true before a window opens as after it, so renaming it would say something false about it |

  All three are defined under their new labels in the Legend AND on the front panel, in
  plain words, on the same run they are renamed. **A reader must never meet a relabelled
  figure without its definition beside it**, because a renamed number with no definition is
  indistinguishable from a different number.
- Emit no movement label of any kind, for the same reason SD-CLM-31 blocks one on a cold
  population: there is nothing yet to have moved.
- State it on the front panel BEFORE any figure, in plain words, naming both dates: this
  period opens on a stated date, which is a stated number of days after this report was
  produced, so nothing below is a conformance rate for it.
- Where INTERACTIVE is present, ask once whether the current window was meant. This is a
  scope question about the request, not a binding request, so it does not spend a Part F
  budget. Where it is absent, run the readiness view and say the question was not asked.

**IN PROGRESS** carries its own risk and its own line: a rate over a window that is one
third elapsed is not comparable to a rate over a closed one, and a reader will compare them
anyway unless told. Name the elapsed share beside every rate, and never compare a
partial-period rate to a closed-period rate without stating both windows and their elapsed
shares.

#### 3.5.2 Evidence age when nothing carries a timestamp

Two different dates are involved and conflating them is the error. The SOURCE age is a
disclosure printed for the reader; the PER-ROW evidence date is what classifies a cell as
stale at 4.1 step 8. Neither is ever invented and neither line is ever omitted.

**The source age ladder.** Take the first that resolves, name which rung was used, and
never present a lower rung as a higher one:

1. The source's own last-refresh timestamp.
2. A period stamp inside the source: a banner row, a column of extract dates, a period
   token in the filename. Name it as derived from the source's own stamp.
3. The maximum per-row evidence date across the retrieved rows. The source cannot be older
   than its newest record, so this is a FLOOR, and it is named as a floor.
4. The file's own modification time. A floor, and one that is external to the data rather
   than a fact about it. Name both of those things.
5. None of the above: the age is UNKNOWN. **Print the line saying so.** An omitted line
   reads as a fresh source; the word unknown reads as what it is.

**Where the per-row evidence date is missing**, the staleness test at 4.1 step 8 cannot
run. Do not default it in either direction: defaulting to in-period maximizes the pass
count and defaulting to stale maximizes amber, and G3 forbids the first while the second
would bury real evidence. Instead, classify those cells on PRESENCE alone, mark the
requirement in the Legend and the audit as recency-untested, and say in one line that the
evidence exists and its age could not be established. A present value of unknown age is
still evidence of presence; it is simply not evidence of currency, and the artifact says
which of the two it is.

**THE ARTIFACT SAYS IT IN THE CELL, AND THE CELL IS THE PLACE THAT SENTENCE MEANS.** Every
pass classified on presence alone under this rule carries the code for A3's
`presence_only_recency_untested` qualifier, on every such cell of every such requirement.
**THE MARK IS IN THE CELL AND ITS WORDING IS IN THE LEGEND**, per A3 and
reference/output-contract.md 2.7, and that division is not the failure this paragraph was written
against: the failure was a qualified pass carrying NO MARK AT ALL, so a filter for green
returned it with nothing to distinguish it, and a coded mark closes that exactly as the
spelled-out wording did. What a Legend line may never do is carry the mark itself. The
Legend and the audit still carry the requirement-level statement as well; that is in
addition to the per-cell code and never instead of it.

**AND THE REQUIREMENTS WHERE IT BITES HARDEST ARE NAMED, ONE BY ONE, ON THE FRONT PANEL.**
Where a requirement's OWN MET-CONDITION carries a recency clause, a dated-within, an
in-force-on, a current-as-of, the untested half is half of the stated condition rather than
a general caveat about currency, and the reader is told so in those terms: a pass on this
requirement is evidence that something is on file and is NOT evidence that it is current.
Name each such requirement, with its met-condition's own recency wording quoted, on the
front panel and in the Legend. The distinction is not decorative: on a requirement with no
recency clause, presence IS the whole met-condition and the qualifier discloses only that
the period-capture rung could not run; on one with a recency clause, the qualifier
discloses that the standard's own test was half-run.

**THIS NEVER BECOMES A REASON TO WITHHOLD THE PASS.** A qualified pass is a pass: it is
scored, it is in both conformance denominators, it is green, and it is counted in every
rate exactly as an unqualified pass is. The qualifier changes what the cell SAYS and
changes no arithmetic anywhere, which is the same relationship the `attested` qualifier has
to the rates under B2.

## Step 3b. The completeness architecture

**A person must be able to start this, walk away, and come back to a report that is
whole. It does not need to be fast. It needs to be complete.**

The same steps, the same checks and the same report at every level of scope. A run over
one small unit and a run over a scope containing dozens of them differ in duration and in
nothing else. Never shorten, sample or simplify the wider path (SD-SCL-01, SD-SCL-03,
SD-EFF-01).

### 3b.1 Build the manifest first, and treat it as the run's contract

Before retrieving any scored row, count the expected entities per unit at the finest
scope level inside the requested scope, and persist that map to
`CHECKPOINT_PATH_PATTERN` under `SCRATCH_DIR`. Under FLOW, count the expected stage
arrivals in the window rather than the open set: see Part D.

Every later check reconciles against this manifest. **A run that cannot state its expected
total before it starts cannot verify itself afterwards.** Where the manifest itself cannot
be computed, say so, and treat every count in the artifact as unreconciled: that is a
degraded run and Part E governs it.

### 3b.2 One scope unit is one unit of work

Never retrieve a wide scope in a single call. Every query interface has a result ceiling,
and some truncate at it silently, returning a well-formed short result with no error and
no indication that anything is missing. That failure looks exactly like a genuinely small
population.

- Discover the ceiling by probe rather than assuming there is none: request a count, then
  request rows, and compare. Where a ceiling is found, record it in the probe record and
  partition below it.
- Partition deterministically by scope unit, then by `PARTITION_SIZE` inside a unit that
  is larger than the ceiling, ordered by identifier ascending (SD-EFF-17).
- Dispatch at most `MAX_CONCURRENT_WORKERS` in flight. Each worker is stateless and
  receives: its scope unit, the resolved requirement set from Step 2, the evidence source
  identifier, the period, and its own output path. Each writes its own checkpoint and
  returns a row count (SD-RUN-01).
- Nothing that needs the whole population is computed inside a partition (SD-EFF-18).
  Workers return raw values. Pass rates, medians, peer norms and any percentile are
  computed once by the supervisor over the merged set. A rate computed per partition is a
  different number wearing the same name.
- Only genuinely independent stages run in parallel, and never across a gate (SD-EFF-16).
  Reading the standard is not independent of resolving the jurisdictions in scope, and
  neither is independent of parsing the population.

### 3b.3 The empty-result rule: wait before you react

An empty or short result is far more often a cold source, a throttle, a replication lag or
a slow render than a true zero (SD-EFF-10: an empty read is UNCONFIRMED, never failed).

- On any empty or below-expected result, wait the first interval in
  `RETRY_BACKOFF_SCHEDULE` and re-run the identical query.
- If the second attempt matches the first, wait again and try once more. Three consistent
  attempts, at minimum, before a unit may be recorded as `verified empty`, and that label
  travels into the final report.
- **Never treat a first empty response as fact, and never rewrite a query that has not
  been retried.** Rewriting a query against a throttle produces a different query that
  then returns different data, confidently. That is the specific harm; it is worth
  stating in these words to whoever implements this.
- A transient failure has no attempt limit (SD-EFF-09). A failure scoped to one unit
  narrows, retries, rebuilds, then degrades that unit alone (SD-EFF-15). Only a named
  gate in `HARD_GATES` stops the run (SD-EFF-02).

### 3b.4 Per-unit acceptance gate

A unit is `complete` only when its returned entity count equals its manifest count. On a
shortfall: retry the unit under 3b.3, then split it into halves by identifier and retry
each half, up to `SCOPED_RETRY_LIMIT` (SD-EFF-09, SD-EFF-15). Record exactly one terminal
status per unit: `complete`, `partial (n of m)`, or `verified empty`. Never an unqualified
success.

### 3b.5 Checkpoint after every unit

Results land on disk as each unit finishes (SD-EFF-30). An interrupted run resumes by
reading the checkpoint directory and skipping units already marked complete (SD-EFF-29:
a stale checkpoint is worse than none, so if the evidence source or the standard changed,
discard downstream checkpoints and rebuild from the parse stage). Never hold a wide
scope's results only in context. The checkpoint holds ledgers only and nothing that looks
finished (SD-EFF-31), lives under `SCRATCH_DIR`, never under `OUTPUT_DIR`, and is deleted
when the real artifact publishes.

Where FILE_WRITE is degraded or absent, retry once, then continue without checkpointing
and warn that an interruption will require restarting. A checkpoint failure degrades
durability, not correctness (SD-EFF-33).

### 3b.6 The reconciliation gate: the build gate, and it is not a stop

Do not build the artifact until all of the following hold:

1. Every unit in the manifest carries a terminal status.
2. The sum of retrieved entities equals the manifest total.
3. Every requirement column carries at least one non-null evidence value across the
   scope. An all-null column is a broken mapping or an empty source column, not a
   scope-wide failure (SD-PRS-18, SD-EXC-08). Stop and re-resolve rather than shipping a
   wall of yellow or, far worse, a wall of red.
4. No requirement is classified GAP for the entire eligible population unless Step 2 was
   re-read and confirmed it is genuinely universal. See 2.8.
   **The amber twin of this condition is not here, and that is deliberate rather than an
   omission.** This condition tests for a wall of RED. A provenance decision that turns
   most of the grid AMBER is the same shape of scope-wide result and this gate cannot see
   it, because there is no all-null column for condition 3 and no universal GAP for this
   condition. It is tested earlier instead, at B1.2, before Step 5 builds anything, because
   the decision that causes it is taken before the build and the cheapest place to catch it
   is where it is made.
5. The regression invariants in `REGRESSION_INVARIANTS` hold against the current
   artifact, not against an earlier checkpoint's claim about it (SD-EFF-07).
6. **No published grouping key, sort key or comparison axis resolves person-bearing**
   under A9.1. Test every one against the built artifact rather than against the
   intention. Any that does is not published in that shape: apply the substitution in
   A9.4, name it, and re-run this condition. This is the interlock that makes the
   accidental per-person ranking impossible rather than merely discouraged.

This is a BUILD gate, not a run stop. It is in no `HARD_GATES` group, because its
terminal state after the retries is a bannered artifact rather than a stop, and neither
permitted gate behaviour describes that. See Part G3, and 3b.7 for what it does instead.
The one condition inside it that IS a gate is check 4 when it survives a re-read of Step
2: that is `scorecard.universal_gap_unconfirmed`.

Advance on evidence read from the artifact, never on a worker's report (SD-EFF-13).
"Wrote 250 rows" is a claim; a read showing 250 populated rows is evidence.

### 3b.7 If reconciliation fails after the retries, still produce the artifact, bannered

Build it, and stamp `INCOMPLETE_BANNER_TEXT` on the front panel and on the summary
section, naming the exact units and counts missing, and preserve the checkpoint.

This is the SD-EFF-05 path and it is reconciled with SD-EFF-04 by the test SD-EFF-05
itself states: a silent partial that reads as finished is forbidden; a partial that is
unmistakably bannered and enumerates its own gaps is the correct terminal state after a
long run. The distinguishing question is whether a reader could mistake it for complete.
For a scorecard the answer must be no, because a silently short conformance report is the
one failure mode this skill must never have: every missing entity reads as a compliant
one.

### 3b.8 Post-build verification

After saving, reopen the artifact and confirm from the file itself that the data row
count equals the manifest total and that the section carries the expected column count.
Re-read `SPOT_CHECK_SAMPLE_SIZE` entities from the source and compare their cells to the
artifact. Report both numbers to the requester. Only then is the run finished.

### 3b.9 Time is not a cost this method recognizes

Never abandon a unit because it is slow; retry it under 3b.3. Never reduce the entity
set, drop a requirement, shorten the period or lower the evidence depth to make a run
finish sooner. Slow and right is a complete success. Fast and short is a failure
regardless of how quickly it returned. Announce a long run before starting it, per
SD-CTR-17, so the requester knows the silence is work.

## Step 4. Classify every cell

One state per entity per requirement, resolved by the ordered procedure below. Stop at
the first test that fires. The ordering is authoritative and is the local form of
SD-POP-02: several of these tests claim to run first, and this is the order that
satisfies all of them.

### 4.1 The classification ladder

Run these in order, per entity, per requirement.

1. **Is the entity in the population at all?** Entities whose status column carries a
   not-workable value are excluded from every section before anything else, and the count
   is reported in the funnel (SD-POP-01). They are not `N/R` cells; they are not rows. A
   closed, suspended, withdrawn or held entity that stays in the population reads as a gap
   somebody is expected to drive to, and sending a person to a locked door on the strength
   of this report destroys its credibility on the spot. Where `OUT_OF_MODEL_CLASS_CONCEPT`
   is bound, that class is removed as well, per SD-POP-17, with its count reported.

   **The test is whether a COLUMN RESOLVED, never whether a BINDING EXISTS, and the whole
   rule is settled in the `UNIT_ACTIONABLE_NOW_VALUES` row of the schema.** The distinction
   that gets lost: the concept being unbound is not the same as no column resolving. A run
   resolves this concept from the seed dictionary whether or not the organization ever bound
   it, so an unbound binding routinely coexists with a perfectly good resolved column. Where
   a column resolves by ANY path, bound or seeded, the exclusion RUNS, and where the value
   list was never bound it runs against `UNIT_NOT_ACTIONABLE_SEED_VALUES` under
   `UNIT_NOT_ACTIONABLE_MATCH_RULE`, which is whole-token phrase matching with no prefix
   matching and no character-length threshold anywhere (SD-POP-29). Only where NO column
   resolves at all is there nothing to read, and then no exclusion is applied because there
   is no evidence, not because the exclusion was switched off. Say that in the funnel and on
   the front panel, and never assume every entity is available (SD-POP-06).

   **Three guards on a default-driven exclusion, all mandatory.** GUARD 1, the stage guard:
   under FLOW, a value that is also a stage name in `POPULATION_SHAPE.stages` is never
   excluded from an unbound default, because that would let the exclusion delete a stage.
   GUARD 2, the majority guard: where the seed set would exclude more than
   `EXCLUSION_SANITY_CEILING` of the in-scope population, nothing is excluded, the run says
   the column was read and looked wrong, and the values are listed. An exclusion the
   organization actually bound is never refused on volume, because the organization is
   entitled to know its own business. GUARD 3, the naming guard: every distinct value in the
   column is listed in the artifact under EXCLUDED or KEPT with its count, so the reader sees
   the whole decision rather than its result.

   **Say which reading of the exclusion was applied, in one line on the front panel**
   (SD-POP-30). This skill scores conformance in a period, so it takes the forward-looking
   reading: the question is whether the entity can be worked in the period being scored. The
   retrospective reading, whether it was workable at any point in the period, belongs to a
   review and produces a different population; the mode is a property of the running skill
   and is never inferred from the data. Where this run is scoring a CLOSED period and a
   reader will use it retrospectively, name the reading used and the count of entities that
   changed state during the window, so the difference between the two populations is visible
   rather than silent.

   **The collision to watch, and it is the failure no gate can catch.** The
   not-actionable concept and the stage concept share vocabulary: a generic status stem
   sits near both, and a stage list commonly contains a value that also reads as
   unavailable. A file carrying one column of stage values can resolve to the exclusion
   concept, the exclusion then removes a whole stage, the funnel reconciles, and every
   downstream invariant passes. SD-PRS-47 is the defence and it is refusal, not
   arbitration: where both concepts match the same header exactly and the exclusion
   concept is strict, neither resolves, the header is reported as ambiguous with both
   candidates named, and both the exclusion and the stage cuts are skipped and named.
   Under FLOW, check this before anything else, because the stage concept is where the
   scoring population comes from.

   **RECONCILE THIS EXCLUSION AGAINST THE STANDARD'S OWN ENTITY-CLASS SCOPE, AND PUBLISH
   THE DIFFERENCE EVEN WHERE IT IS ZERO.** Most published standards open by naming the class
   of entity they apply to. That sentence is an ELIGIBILITY SCOPE and Step 3.4 resolves it
   at step 5 of this ladder, where a failing entity is `N/R` with a reason. This step's
   exclusion is a different rung of the same ladder producing a different outcome: a step-1
   exclusion vanishes into the funnel and is not a row, while a step-5 failure is a row
   carrying a grey cell. **Two independent tests selecting the same population is worth more
   than either alone, and a disagreement between them is invisible unless somebody looks.**
   Where the standard states an entity-class scope of its own, resolve it, compare the
   population it selects against the population this step's exclusion leaves, and report the
   comparison as three numbers on the front panel and in Method: the count each test
   selects, and the count of entities the two tests disagree about, **printed even when it
   is zero, because a zero is the evidence the check ran** (SD-EXC-06). Name the entities in
   the disagreement in Method, with which test kept each and which dropped it.

   **WHY A SILENT DISAGREEMENT IS THE DANGEROUS CASE.** Where the seed value set excludes a
   value the standard still counts as in-class, this step deletes rows the standard says
   should have been scored: the funnel reports a clean exclusion, the eligibility test at
   step 5 finds nothing left to mark, and no number anywhere moves. Where the standard
   excludes a class this step keeps, the opposite happens and the entities arrive as grey
   cells rather than as an exclusion, which is visible but is counted in a different place.
   Neither test is promoted over the other here and neither is adjusted to match: **the
   comparison is REPORTED, not resolved**, because which of the two is right is a question
   about this organization's own vocabulary that only the binding owner can answer, and it
   is routed to `BINDING_OWNER_NAME` where the disagreement is not zero. The exclusion this
   step applies is unchanged by the comparison.

   **The second guard on the same column: a flag set on every row, or on none.** The
   not-actionable exclusion is a presence rule and takes the proper-subset guard in
   reference/field-resolution.md 3.12 exactly as an absence rule does. Where the resolved flag
   carries a not-actionable value on EVERY row in scope, the exclusion removes the whole
   population and the run reaches `shared.record_count_zero` looking like an empty scope
   rather than a mis-resolved column. Where it carries one on NO row, the exclusion is
   inert and the run reports an exclusion it never made. In both cases the distinction
   does not exist in this population: record the exclusion as NOT PRESENT, apply none,
   report the count as zero with that reason in the funnel, and name it in the audit.
   Neither state is evidence about the entities; both are evidence about the column.
2. **Is the requirement in the current standard?** No: `RETIRED`, no column built (A6).
3. **Has the requirement taken effect for this period?** No: `- N/R: effective from
   <period>`, read from the requirement's own effective-from date rather than from this
   organization's operating window where the author is external. Paused this period:
   `- N/R: paused this period`, and this code applies ONLY where the pause was issued by
   the requirement's own author. An internal decision not to score an externally authored
   requirement is a scoring pause, not a lapsed obligation: the cell stays scored and the
   pause is disclosed on the front panel, per 2.6.
4. **Is the requirement permitted for this entity's jurisdiction?** No: `- N/R: not
   permitted in this jurisdiction`, which is permanent until the rule changes and is
   never a gap and never a data problem. Where the compliance reference was unreachable,
   hold back the requirements it would have validated, name them, and rank without them:
   the gate fails closed on the requirements and never on the artifact
   (`COMPLIANCE_FAILS_CLOSED_ON`, SD-EXC-29).
5. **Is the entity eligible?** No: `- N/R` with the specific reason from 4.2. Cannot be
   determined: `? UNASS: eligibility could not be determined` (Step 3.4).
6. **Is there an evidence field, and does it carry data?** No field mapped, field empty
   across the scope, or the evidence source could not see this requirement:
   `? UNASS` with the matching reason.
7. **Does the provenance permit a verdict?** Attested where the standard requires
   observation, or inferred: `? UNASS` with the matching reason (Part B). **The class this
   test reads was assigned by B1.1 and by nothing else**, and B1.2's tripwire is computed
   over the result of this step across every requirement, before Step 5 builds anything: a
   provenance decision that lands most of the grid on this rung is a scope-wide result and
   is not published without being questioned first.
8. **Was evidence captured for this entity in this period?** No capture:
   `? UNASS: no evidence captured this period`. **A unit that did not MATCH the evidence
   file at the join in 3.2.1 has no capture and lands here**, on this rung and never on
   step 9's: an absent record is not evidence of a negative, and a blank read as a failure
   is the exact conflation A1 exists to prevent. Captured but older than the period:
   `? UNASS: evidence predates this period`. Captured but unusable:
   `? UNASS: evidence quality insufficient`, naming the defect.
9. **Does the evidence satisfy the requirement's test?** Yes: `+ PASS`. No: `x GAP`,
   carrying a code from the GAP family of `REASON_CODE_SET` and a reason **phrased as the
   absence**.

   **The reason states the FINDING, never the requirement's met-condition on its own.**
   This is the wording trap in this skill and it inverts silently. A standard states its
   requirement as the condition that satisfies it, so an implementer forbidden to invent
   text reaches for that sentence and drops it into the cell, where it reads as an
   assertion that the condition holds. The cell then says the opposite of the finding, and
   nothing downstream can catch it because the text is quoted accurately from the standard.

   Wrong: a cell reading `x GAP: no open request older than five business days`. Quoted
   correctly from the standard, and to the reader it says there is no such request, which
   is the good state. Right: the cell reads `x GAP: NOT_DONE`, and the row's narrative
   entry for that requirement reads
   `Open requests: GAP NOT_DONE. Recorded as not met. The standard requires: no open
   request older than five business days.` Three parts, in that order, wherever the
   standard's own wording appears: the code, the finding as an absence, then the
   requirement clearly framed as the requirement.

   **THE STANDARD'S OWN WORDING GOES IN THE NARRATIVE COLUMN AND NEVER IN THE STATUS
   CELL.** The status cell carries the symbol, the state code and the reason code, and
   stops there. The wording is carried in the trailing narrative column of element 11, per
   5.4, which is last, widest and never truncated. Three separate reasons converge on that
   placement and no reason of any weight opposes it. **One:** a requirement column's width
   is the character count of its longest value, capped, per reference/output-contract.md 2.2 step 3,
   so a sentence in a status cell makes every requirement column as wide as its longest
   sentence, and a measured build came out 21 columns and 659 character-widths across, about
   ten screens, on which a reader scrolling right to the eighth requirement had lost the
   unit's name. **That width is now BOUNDED and not merely regretted:**
   reference/output-contract.md 2.7 bounds a grid's summed built width by `GRID_MAX_TOTAL_WIDTH`
   and runs a relief ladder before publication where it is exceeded, verification row 10
   asserts it, and SD-FMT-28 is the doctrine. What a status cell carries is therefore a
   question with a measured cost attached, and this step is the first place that cost is
   paid. **Two:** a status column carrying a sentence can never qualify for CENTRING under
   reference/output-contract.md 2.5, so the grid cannot be read across the row as a straight-edged
   pattern. That is an alignment loss and nothing more: 2.5's character bound governs
   CENTRING only, it is not a condition on shading, and the classification fill of 4.6 is
   unaffected by it either way. **Three:** the wording repeated
   in every one of hundreds of cells is one sentence about the REQUIREMENT, not about the
   unit, and the place a fact about the requirement belongs is the Legend, which already
   carries it per 5.6, with the narrative saying what is wrong with THIS unit. It is also
   the shape 2.7 names as a standing qualifier's cousin: a phrase identical on every row
   costs its full width on every row and says one thing.

   Test every cell template and every narrative entry by reading it aloud as the reader: if
   the sentence could be read as describing a pass, it is wrong however accurately it quotes
   the source. **The wording trap moves with the wording**: it is now a narrative-column
   trap, it inverts exactly as silently there, and the three-part ordering above is what
   defuses it in either column.

### 4.2 The reason code vocabulary

`REASON_CODE_SET` is the bound vocabulary. Its taxonomy shape is in the schema and each
entry carries `code`, `applies_to`, `meaning`, `implied_action` and `resolvable_by`. A
code with no implied action is a label rather than a reason and does not belong in the
set, and a code whose `resolvable_by` is nobody is visible as unresolvable, which is
itself worth knowing.

Two rules govern it. **It is CLOSED.** A run may not invent a reason. A cell whose reason
fits no code is marked unmapped, named in the audit, and routed to `BINDING_OWNER_NAME`
who extends the set. Free text here defeats the purpose, because free text cannot be
counted, compared between periods, or acted on in bulk. **The code is written as CELL
TEXT**, per A3; colour is a second channel and never the only one.

**COVERAGE VALIDATION, and it is not optional.** SD-CTR-29. A closed vocabulary a run
must draw from is usable only if it carries at least one member for every state the
contract can produce. Validate in that direction, from the STATES in `CLASSIFICATION_LABELS`
to the SET, whenever either changes. A state with zero members is a HOLE, and a hole
guarantees an unmapped cell on every run in which that state occurs. The named case is this
skill's own: the set once seeded eleven codes for one rare state and eight for another and
NONE for GAP, which is this skill's entire subject, so an ordinary run produced hundreds of
unmapped cells while the set looked complete to anybody who read it without counting.

The seeded set therefore has FOUR families, one per non-pass state. Its authority is the
schema's own documented default for `REASON_CODE_SET`; the tables below set that default
out in the order the classifier meets it. Where this file and the schema's default ever
differ, the schema governs and the difference is a defect to report, not a choice to make.
Codes are byte-identical between runs (SD-CTR-09).

GAP reasons, seeded. This is the commonest state and every code here is cleared by
somebody:

| Code | Meaning | Cleared by |
|---|---|---|
| NOT_DONE | The requirement applies and no evidence of it exists | the unit owner |
| PARTIAL | Some of the requirement is met and some is not | the unit owner |
| EXPIRED | It was met and the evidence has lapsed | the unit owner |
| SUPERSEDED | It was met to an earlier version of the standard | the unit owner |
| NOT_STARTED | It is in scope and no work has begun | the unit owner |
| IN_PROGRESS | Work has begun and is incomplete at the census date | the unit owner |
| BLOCKED_EXTERNAL | Work cannot proceed because something outside the reader's control is outstanding | the named external party, and NOT the reader |
| AWAITING_APPROVAL | Complete and pending a decision by somebody else | the approver |
| EVIDENCE_MISSING | The work may be done and the evidence cannot be produced | the unit owner, and distinct from NOT_DONE because the remedy differs |

RETIRED reasons, seeded. Every one has an implied action of NONE and is cleared by NOBODY,
stated explicitly, because a retired cell that looks actionable sends somebody to do work
that no longer exists:

| Code | Meaning |
|---|---|
| WITHDRAWN_BY_ISSUER | The requirement was removed from the standard by its author. Shown for continuity only |
| REPLACED_BY | Superseded by a named successor requirement, whose identifier the cell carries |
| OUT_OF_SCOPE_NOW | The entity left the scope the requirement applies to |

Unassessable reasons, seeded:

| Code | Meaning | Action it implies |
|---|---|---|
| no evidence captured this period | Nothing was recorded for this entity in the window | Capture evidence |
| evidence predates this period | The most recent record is older than the window | Re-capture |
| evidence quality insufficient | Recorded but unusable: obscured, out of frame, too distant, illegible, below the source's own confidence floor, suspected duplicate, nothing to assess | Re-capture |
| evidence source unreachable | The source could not be read this run | Retry, or check access |
| evidence column present but empty | The field resolved and holds no values across the scope | Fix the mapping or the feed |
| no evidence source mapped | The standard scores it and no field was confirmed | Map it, or check manually |
| not detectable by this evidence source | The source structurally cannot see this requirement | Verify in the named system |
| attested only, standard requires observation | Only a self-report exists | Observe it |
| inferred only, not observed | Derived from a proxy | Observe it |
| eligibility could not be determined | The eligibility test could not be resolved | Resolve eligibility |
| conflicting evidence | Two sources disagree | Reconcile the two sources |

Not-required reasons, seeded:

| Code | Meaning |
|---|---|
| not targeted | The requirement applies to an assigned subset and this entity is not in it |
| no programme, election or contract on file | The entity is not enrolled, elected or contracted for it |
| not permitted in this jurisdiction | A rule where this entity sits forbids it. Permanent |
| below the standard's own exclusion threshold | The standard excludes entities under a stated size, class or capability |
| entity class out of scope for this requirement | The standard scopes it to a class this entity is not in |
| paused this period | A dated release suspended measurement |
| effective from <period> | Measurement has not started |
| served under a different operating model | Removed by the class exclusion, where that class is shown rather than dropped |

**A bare state with no reason is not a deliverable.** `N/R` on its own tells a reader
nothing, and the seven or eight things it can mean have completely different consequences:
one of them is permanent, one resolves next period, one is a mapping defect, one is a
contract the person could go and sell. The reason is the product.

### 4.3 Targeting is not failure

Many requirements apply only to a named subset. When a requirement's eligible count is a
small share of the scope, that is targeting, and it must never present as a scope-wide
collapse.

- Resolve targeting from the standard's own scoping pages and from any published
  eligibility field. Never infer it from the shape of the results.
- Apply the proper-subset guard from 3.4 before applying any targeting rule. A targeting
  field that is blank on every row or populated on every row defines no target set, and
  the requirement is unassessable rather than universally targeted or universally
  exempt.
- `HQ_FLAG_BREADTH_LIMIT` is the tripwire: where a requirement's eligible population is
  below that share of the scope, treat the result as presumptively targeted and re-read
  the eligibility test before publishing. The tripwire prompts a re-read; it never
  reclassifies anything on its own.
- Entities outside the target set are `N/R: not targeted`, never `GAP`.
- State the applicable entity count for every targeted requirement, on the Summary and
  in the Legend: "applies to 17 of 214 entities in scope".

Worked example. A requirement covering a specialist product line applies to fewer than
twenty sites per front-line unit and is a local choice between two alternatives inside one
site category. Scored against every site it produces a red wall; scored against its real
eligible set it produces a short, true, actionable list.

### 4.4 A gap the reader cannot close is not worth printing, and there are TWO tests

**Two tests, and only the second suppresses scoring.** SD-EXC-14. The tests separate the
AUTHORITY to set a requirement from the ABILITY to affect the measured value, and reading
them as one test is what produces the failure in the second direction below.

1. **THE ENGAGEMENT TEST.** Does the reader engage this entity at all? If not, the
   requirement is not theirs: it is shown rather than scored.
2. **THE INFLUENCE TEST.** Can the reader's own actions MOVE the measured value, whoever
   set the requirement? If yes it is **SCORED**, however far above them the requirement
   was set. A requirement set by a regulator, an accrediting body, a parent organization
   or a central function is shown rather than scored ONLY where compliance with it is
   also determined above the reader, such as a contract term, a purchased configuration,
   a formulary or scheduling decision, or a decision taken at a level the reader cannot
   reach.

`EXCEPTION_FLAGS.requires_decision_authority_at_unit` is the shape of the second test and
is read as the influence test, not the authority test.

**An externally authored standard routes to the SCORED block by default.** A requirement
published by a regulator, an accrediting body, a standards organization, a licensing
authority, a payer or a customer is not thereby out of the reader's hands. It is the
ordinary case for a compliance scorecard, and it is usually the whole reason the reader
opened one. Authorship above the reader tells you who wrote the requirement; it tells you
nothing about who can meet it. Only a second, separate finding that compliance itself is
determined above the reader moves it to shown-never-scored, and that finding is recorded
with its evidence rather than inferred from the author's name.

**Why this direction matters as much as the other.** Read as a single test, the rule moves
most of an externally published requirement set to shown-never-scored because a regulator
set it, leaves a pass rate computed over a handful of items, and produces a near-empty
worklist that reads as "you are fine". The one number the reader would act on, the count
of things to go and fix, is then suppressed by a rule written to protect them. That is the
same conflation the whole classification contract exists to prevent, arriving through a
routing decision instead of through the ladder, and it is worse than the ladder version
because nothing in the artifact looks wrong.

**The disclosure, and it is mandatory.** Where more than half the requirement set falls to
shown-never-scored, stop and say so on the front panel BEFORE the pass rate: this
scorecard scores n of m requirements and the rate covers only those. Name the suppressed
requirements and, for each, the finding that put it there. A pass rate over a minority of
a standard is not a compliance figure, and a reader must be told that before they read it.

A requirement that does route to shown-never-scored appears in its own column with its
status and benchmark, takes no part in either rate, and confers no membership on the
worklist (SD-EXC-22, `SHOWN_NEVER_SCORED_CONCEPTS`). Counting a requirement the reader
genuinely cannot move is the most damaging false positive available to this skill after
the empty-column case; suppressing one they can move is the most damaging false negative.

### 4.4b The influence finding is scoped to the population it actually holds for

4.4 decides WHETHER a requirement is in the reader's hands. This decides WHERE, and it is
the half that was missing. **A requirement is not uniformly in or out of a reader's hands
just because the standard states it once.** Real requirements are mixed: a counterparty
refuses a class for some entities and grants it routinely for others; a jurisdiction
forbids it in two places and permits it in nine; a parent sets the term for the entities it
owns and not for the rest.

**Route at the granularity the finding actually holds at.**

1. **An influence finding is a triple**, recorded and published as one: the requirement,
   the SUBSET of the eligible population the finding holds for, and the evidence for it.
   A finding with no stated subset covers the whole eligible population ONLY where its
   evidence covers the whole eligible population. Where the evidence is drawn from part of
   the population, the subset is that part and no more, and widening it is the silent
   widening SD-QUA-12 forbids.
2. **The subset resolves to a testable attribute already in the data**: the counterparty,
   the jurisdiction, the class, the parent, the contract, the programme. A finding whose
   subset cannot be resolved to such an attribute is not scoped, routes whole, and says so.
   Never define the subset by listing entity identifiers: a maintained list rots and does
   not travel (SD-POP-07).
3. **The proper-subset guard applies here as it does everywhere else** (3.4, SD-QUA-04). A
   subset equal to the whole eligible population is not a subset, it is the whole
   requirement, and it routes whole. A subset equal to none of it is not a finding.
4. **Where the subset is proper, only that subset is ROUTED DIFFERENTLY and the complement
   is scored normally.** Both counts are published together, in the Summary, in the Legend
   and on the front panel, in one sentence. Never publish one count without the other.
   **THE SENTENCE IS COMPOSED AFTER STEP 5 HAS RUN, AND ITS TEMPLATE IS BRANCH-DEPENDENT,
   because step 5 decides which of two sentences is TRUE and only one of them contains the
   word suppressed.** An earlier version of this step mandated the suppressed wording
   unconditionally. Under step 5's first branch that sentence is false in three ways at
   once: it tells the reader that k entities were not scored on a requirement all m were
   scored on, it contradicts the conformance rate printed beside it, which is computed over
   all m, and it invites the reader to reconcile two numbers that were never in conflict.
   A sentence that contradicts the number next to it destroys the number.
   - **Under step 5's FIRST branch**, where the cells are scored and carry
     `x GAP: BLOCKED_EXTERNAL`: **this requirement is scored on all m eligible entities; on
     n the gap is the reader's to close, and on the other k it is cleared by the named
     parties, and those k are IN the conformance rate, OUT of the attributable rate, and
     OUT of the worklist.**
   - **Under step 5's SECOND branch**, where the cells are shown, never scored: **this
     requirement is scored on n of m eligible entities and shown, never scored, on the
     other k, whose conformance belongs to the named parties' own report and is out of
     every rate.**
   - **Where one requirement's subsets split across BOTH branches**, both sentences ship,
     each with its own k and its own named parties, and the counts sum to m. Never collapse
     them into one sentence with one k, because the two k's are in different denominators.
   - **The word suppressed is reserved for a cell that is out of the rate printed beside
     it.** It is accurate under the second branch and under 4.4's shown-never-scored
     routing, and it is inaccurate under the first, where the cell is scored, is red, is in
     the census and is in the conformance figure.
5. **The suppressed cells are classified, not left blank and not greyed by reflex.** Ask
   one further question: does the entity's conformance still matter to the organization,
   because a regulator, an auditor, a customer or a contract will look at it?
   - **Yes:** `x GAP` carrying the reason code `BLOCKED_EXTERNAL`, whose `resolvable_by`
     names the party who can clear it and explicitly NOT the reader. The cell stays in the
     census and in the conformance rate, because the entity genuinely does not conform and
     somebody needs to know. It is excluded from the ATTRIBUTABLE rate by A4, which is what
     keeps it out of a peer comparison while keeping it in the compliance figure. **It is excluded from this reader's worklist**, because the worklist is
     the list of things this reader can go and do. The Legend says both halves in plain
     words: these are real shortfalls, and they are not yours to clear.
   - **No, the conformance of those entities is somebody else's report entirely:**
     shown-never-scored for that subset only, in the shown column, out of every rate.
   - **Cannot be determined:** take the first. A visible shortfall with a named owner is
     recoverable by the reader; a hidden one is not.
6. **The disclosure fires on two independent tests, and either one is enough.** The first
   is SD-EXC-14's and counts REQUIREMENTS: where more than half the requirement set falls
   to shown-never-scored, stop and say so on the front panel before the pass rate. The
   second counts CELLS: where more than half the scored cells across the whole scorecard
   are suppressed by influence findings, the same statement fires. The second exists
   because one mixed requirement over a large population can suppress most of the work
   while being one requirement of eight, and the requirement-count test cannot see it.

**Worked example, neutral.** A servicing standard requires a written confirmation from the
counterparty on every account. Two counterparties have closed the class outright and no
request from the reader can obtain one; four grant it on request. The evidence is the
standard's own note that the counterparty issues the confirmation, plus a distribution
showing two counterparties at zero confirmations with no blanks while the rest run between
seventy and eighty percent.

Routed whole to shown, the reader loses a genuine to-do on every account with an open
counterparty, and an honest reader is told not to do work they could do while a passive one
gets cover. Routed whole to scored, the accounts with closed counterparties each carry a
red cell nobody can ever close. Routed at the granularity the finding holds at, the
accounts with open counterparties are scored and appear on the worklist with "request the
confirmation" against them, the accounts with closed counterparties carry
`x GAP: BLOCKED_EXTERNAL` naming the counterparty and appear on no worklist, and both
counts are on the Summary. That is the only routing that is true about both halves.

### 4.5 Red means go and fix this

Never colour an unassessable cell, a not-required cell or an excluded entity red, in the
artifact or in the chat, and never fold their counts into a gap count. Report gaps and
"could not assess" as two separate numbers everywhere either appears. This distinction is
the entire point of the scorecard.

### 4.6 Colour, and colour is never alone

Every status cell carries a symbol and a code as text, per A3, and a fill in addition. The
fill is the second channel and never the first: the words in the cell are read one at a
time, and the colour is what a reader takes in across the whole grid at once, which is how
they find the failures before they have read anything.

**THE REQUIREMENT COLUMNS ARE DECLARED CLASSIFICATION COLUMNS UNDER reference/output-contract.md
2.6, AND THAT IS WHAT CARRIES THE FILL. THEY ARE NOT DECLARED STATUS GRID COLUMNS AND THE
FILL NEVER DEPENDED ON THEIR BEING ONE.** 2.6 states four conditions, none of which is a
length bound, and 2.5's `CENTRE_ALIGN_MAX_CHARS` decides CENTRING and is read nowhere else.
This file cites both and restates neither. **An earlier revision of this section hung the
fill on a STATUS GRID COLUMN declaration under 2.5, and that is the sentence this one
replaces**, for the reason 2.6's own opening paragraph now gives: A3 and 4.2 fix the
vocabulary a requirement cell carries, its shortest gap cell is fifteen characters and its
shortest unassessable cell longer still, against a centring bound of twelve, so **no
standard, no organization and no binding could ever have produced a lawful fill on this
skill's own grid**. Measured on one build: 1520 status cells shipped with no colour at all,
correctly under the text as it stood, and contrary to the artifact this file's own
description promises. A cell can be far too long to centre and still be exactly the cell
that most needs a fill.

**THE FOUR CONDITIONS OF 2.6, AND WHAT THIS FILE SUPPLIES FOR EACH.**

1. **THE COLUMN IS DECLARED, AND THE DECLARATION IS ON THE METHOD SHEET**, per 5.7. Its
   shape token is STATUS_OR_CATEGORY, which a requirement column's is. Its states are the
   members of `CLASSIFICATION_VOCABULARY`, published in the Legend with the meaning of each
   per 5.6, and a run never invents a state. **THE RESOLUTION RULE FROM CELL TO STATE IS
   PUBLISHED WITH THEM AND IT IS TOTAL AND MECHANICAL, AND THIS IS THE CONDITION THIS SKILL
   HAS TO WORK FOR**, because its cell values are not its states. It is stated in the next
   paragraph.
2. **`CLASSIFICATION_FILLS` IS INJECTIVE.** One fill per state, every state carrying one,
   and NO TWO STATES SHARING ONE, however alike they read. The table below is built to it.
3. **THE FILLS COME FROM `CLASSIFICATION_FILLS`**, published in the Legend with the state
   each colour carries. Where a state's fill is one of the contract's own status colours the
   map CITES that variable, so no colour has two setting sites, and this file writes no hex
   value and names no colour of its own. **EVERY ONE OF THEM IS WRITTEN WITH AN EXPLICIT
   OPAQUE ALPHA, PER reference/output-contract.md 2.9**, and verification row C1 reads the alpha back
   off the BUILT artifact rather than off the map: a fill written with a transparent alpha is
   opaque to the engine that wrote it and gone in the next renderer, so a grid whose whole
   second channel is colour can lose all of it with a recorded pass standing behind it. The
   form is the schema's, the check is the contract's, and this file supplies neither.
   SD-FMT-29.
4. **THE PALETTE IS DISJOINT FROM THE ALERT PALETTE**, which the next paragraph but one is
   about.

**THE RESOLUTION RULE, DECLARED HERE, TOTAL OVER EVERY POPULATED CELL THIS SKILL CAN
EMIT.** `CLASSIFICATION_VOCABULARY` binds STATES and never distinct cell values, which is
exactly the distinction that makes the fill reachable on this grid: A3 writes a state
crossed with a reason code, and on a pass with a qualifier code, so the distinct values run
to hundreds while the state set stays at five. The rule is one lookup and it reads only the
front of the cell:

- **A populated requirement cell begins with the SYMBOL of exactly one state**, taken from
  that state's own `symbol` in `CLASSIFICATION_LABELS`, followed by that state's own code
  from the same taxonomy. The cell resolves to that state. Everything after those two
  tokens is a reason code, a qualifier code or a finding, and the resolution does not read
  it.
- **The symbols are one per state and no symbol is shared**, which is what makes the first
  token sufficient and the rule mechanical rather than a judgment. A3 puts them in the cell
  and this rule reads them back.
- **The rule is TOTAL because A3 is total.** Every populated cell this skill emits is
  written state first, by A3, on every rung of the 4.1 ladder without exception, so no
  populated cell resolves to two states and none resolves to none.
- **A cell the rule cannot place is not filed under the nearest state.** The cell is
  reported unmapped and routed to `BINDING_OWNER_NAME`, the column is NOT a classification
  column for that build, and **it then carries no fill at all rather than a guessed one**,
  per 2.6's own statement that a rule leaving one populated cell unresolved is not total.
  That is a stated outcome and not a build failure, and the Legend says it happened.
- **RETIRED is a member of the vocabulary and never appears in a cell**, because A6 does not
  build the column at all. A state that cannot occur still has an entry in the map, and a
  state with no occurrences is not a state without a fill.

| State | Fill |
|---|---|
| PASS | `COLOR_STATUS_PASS`, cited by `CLASSIFICATION_FILLS` |
| GAP | `COLOR_STATUS_GAP`, cited by `CLASSIFICATION_FILLS` |
| UNASSESSABLE | `COLOR_STATUS_UNASSESSABLE`, cited by `CLASSIFICATION_FILLS` |
| NOT REQUIRED | `COLOR_STATUS_NOT_SCORED`, cited by `CLASSIFICATION_FILLS` |
| RETIRED | Its own entry in `CLASSIFICATION_FILLS`, which is the one standing state with no palette variable of its own, so that map supplies the value and this file names no colour |

**NO TWO STATES SHARE A FILL, AND NOT REQUIRED AND RETIRED ARE THE PAIR THIS SKILL WAS
GETTING WRONG.** An earlier revision of the table above gave those two one fill, on the
reasoning that both are shown rather than scored and both read as grey. `CLASSIFICATION_FILLS`
is INJECTIVE, verification row 13 asserts it, and a map that is not injective BLOCKS
publication. **The discriminator is not how alike two states read; it is whether they are
counted differently, excluded differently, or cleared by different people**, and any one of
the three is enough. These two differ on all three: NOT REQUIRED says the requirement did
not apply to this entity and nobody has anything to do, RETIRED says the requirement's own
issuer withdrew it and the column exists on no sheet this period, they enter different
lines of the funnel, and a reader who cannot tell them apart cannot tell a cell that is out
of scope from a requirement that is out of the standard. **Four answers that read as three
colours are three answers**, and the fourth is not recoverable by any reader. Where the
bound vocabulary holds more states than the bound palette has separable colours, the excess
states carry NO FILL and the Legend names which; that is 2.6's own remedy and it is never
resolved by giving two answers one colour.

**BOTH PALETTE VARIABLES FOR THE TWO NON-PASS SCORED STATES EXIST AND ARE BOUND.**
`COLOR_STATUS_GAP` and `COLOR_STATUS_UNASSESSABLE` are defined in reference/schema/ with
documented defaults and with the greyscale separation arithmetic that proves the whole
palette apart. **An earlier revision of this table said no palette variable existed outside
the alert pair for either state and withheld their fills until one was bound**, while the
schema three thousand lines below the same delivered file handed the build two values: two
readers of one file built two different workbooks, and the file's own precedence rule
already settled it, because where this file and the schema differ the schema governs and
the difference is a defect to report rather than a choice to make. The claim is deleted and
both states take their variables above.

**A STATE THAT CARRIES NO FILL IS STILL A STATED OUTCOME AND NOT A BUILD FAILURE.** It is
now the rare case rather than the standing one, and 2.6's condition 2 is where it comes
from: where the bound vocabulary has more members than the bound palette has distinguishable
colours, some members carry no fill and the LEGEND SAYS WHICH. It is never resolved by
giving two answers one colour and never by borrowing a colour that already means something
else. The Legend therefore names, every run, which states carry a fill, which do not, and
why. **Nothing is lost from the classification itself**: A3 puts the symbol, the code and
the reason code in the cell as characters, so an unfilled GAP cell still reads as a gap and
still filters, sorts, prints and pastes as one. That is the same guarantee that makes the
markdown fallback in E2 lose nothing, and it is why the fill was always the second channel
and never the first.

**THE DISJOINTNESS IS A HARD CONSTRAINT ON THE BINDING AND IT DECIDES WHAT MAY BE
ASSIGNED.** `COLOR_ALERT_WARN` and `COLOR_ALERT_OVERDUE` belong to element 13's bands and
are never a value in `CLASSIFICATION_FILLS`, on any sheet, whether or not that sheet carries
an elapsed-time column (SD-FMT-27). An earlier revision of this section assigned GAP the
overdue fill and UNASSESSABLE the warn fill, and it collided with nothing on the run that
authored it, because no sheet in that workbook carried an elapsed-time column and element
13 scored NOT APPLICABLE everywhere. The same assignment at an organization that DOES track
one paints two colours with two meanings on one grid: an approaching deadline in one column
and an unassessable cell in the next, with nothing in the artifact to tell a reader which
meaning a colour carries. **A colour is a variable with one binding, exactly as a header
string is**, and a defect invisible on the run that authored it is the kind this file is
built to refuse.

Each bound value is required to be distinct from every other in greyscale as well as in
colour, because a not-scored cell that reads as a pass inverts the contract, and the fills
are answers that must never share a value pairwise. The arithmetic is the schema's and this
file runs it rather than restating it. **SEPARATION IS ONE PROPERTY OF A BOUND FILL AND
OPACITY IS THE OTHER**: two fills perfectly separated in greyscale are indistinguishable the
moment neither of them renders, which is exactly what a transparent alpha does to both, so
2.9's form is asserted on every entry of the map ALONGSIDE the separation arithmetic and
never instead of it. **A cell carries at most one fill**: where a status
cell also falls inside an alert band, the alert fill governs and the classification fill is
not applied, per 2.6, and the Legend states that precedence once.

**WHERE THE TWO TAXONOMIES MEET, SO THERE IS NEVER A SECOND SETTING SITE FOR ONE COLOUR.**
`CLASSIFICATION_LABELS` names a `fill_variable` per state and `CLASSIFICATION_FILLS` maps
each state of `CLASSIFICATION_VOCABULARY` to the fill it carries, citing those same
variables. The two agree by construction, because the vocabulary's members are that
taxonomy's keys. **The BUILD reads `CLASSIFICATION_FILLS`**, which is what 2.6 condition 3
names and what verification row 13 reads back. Where the two ever disagree at an
organization, that is a BINDING defect: report it, route it to `BINDING_OWNER_NAME`, and
build nothing from the disagreement rather than picking a winner.

**ALIGNMENT AND FILL ARE SET INDEPENDENTLY AND NEITHER IMPLIES THE OTHER.**
reference/output-contract.md element 9 has three alignment classes and 2.5 decides membership by
rule (SD-FMT-05). A requirement column is CENTRED only where all three of 2.5's conditions
hold on this run's own bound values, and the skill declares it a STATUS GRID COLUMN on the
Method sheet when they do:

1. Its shape token is STATUS_OR_CATEGORY, which a requirement column's is.
2. Every populated value comes from a closed, declared vocabulary published in the Legend.
   After 4.1 step 9 moved the standard's own wording to the narrative column, and after A3
   moved the pass qualifier's wording to the Legend against its code, a requirement cell
   holds a symbol from `CLASSIFICATION_LABELS`, a state code from the same taxonomy, a
   reason code from `REASON_CODE_SET` and, on a qualified pass, a code from
   `PASS_QUALIFIER_VOCABULARY`. All four are closed sets and all four are published, so this
   condition holds.
3. The LONGEST member of that vocabulary is at most `CENTRE_ALIGN_MAX_CHARS`. **This is the
   condition that decides it, it is arithmetic, and it is computed at build time from the
   values actually written.** Under the standing bindings the longest cell value on a
   requirement column exceeds the bound, so **the columns are LEFT ALIGNED, which is the
   ordinary case and is not a defect, and they carry their classification fill exactly as
   they would if they were centred.** Where an organization's bound reason vocabulary and
   its bound value of `CENTRE_ALIGN_MAX_CHARS` are such that it does not, the columns are
   centred and are declared as status grid columns as well, which 2.6 says is automatically
   a classification column too.

**THREE PROHIBITIONS FOLLOW AND ALL THREE HAVE BEEN VIOLATED AT LEAST ONCE.** **The
centring is never bought by shortening the cell**: A3's reason code is contract-level, it
is what makes a yellow actionable and a red clearable, and dropping it to win an alignment
class would trade the product for a tidier edge. **The fill is never made conditional on
the centring test**, which reference/output-contract.md PART 8 now forbids in terms and which is
the defect that emptied 1520 cells of colour. **And the alignment is never asserted here as
a fact about the built sheet**: this file states the test, element 9 verifies the result
over every populated cell of the table block, and a build that centred a column failing the
test is blocked at the gate. **THAT SCOPE IS ELEMENT 9's ALONE AND IS NOT THE GATE'S**:
element 7's border walk covers every populated cell of the SHEET'S USED RANGE, the note band
of 5.3, the explanatory row of 5.4 and every populated row of a panel included, per PART 7.2
row 7, so a scope read off this paragraph and applied to the borders is exactly the check
scoped more narrowly than the rule it enforces that SD-FMT-02 forbids. An earlier revision of this section said, flatly, to centre
every status cell, which element 9 rejects for a column of sentences and which therefore
could not be obeyed by a workbook that publishes.

## Step 4b. Requirements that are not binary, and requirements scored above the entity

Not every requirement is present-or-absent, and a scorecard that silently drops the rest
under-reports what the population is actually measured on. Include them, clearly labelled
as their own section, and do not force them into the five states.

### 4b.1 Continuous and threshold requirements

Where the standard expresses a requirement as a percentage, a count, a rate or a time:

- Print the value in the cell and shade it against the standard's own threshold.
- Assert a per-entity verdict only where the standard states a per-entity threshold. Where
  it does not, the value is a prioritization signal, not a verdict, and the Legend says so.
- Read the scale from the column's own maximum every run (SD-PRS-44, F3.11). A threshold
  written for a fraction matches zero rows against a points column, silently.
- Where no value was captured for the entity in the period, the cell is
  `- N/R` or `? UNASS` by the ladder in 4.1, never zero. A missing percentage is not a
  percentage of zero.

### 4b.2 Requirements measured above the entity

Where the level at which a requirement is officially measured is above the entity, the
official score is not an entity-level fact. Show the entity-level value as a prioritization
signal, roll it to the level the standard measures at, and say on the Legend which level
the official figure is computed at. Do not publish an entity-level pass or fail for it.

Read that level from the requirement's own author. For an internally authored requirement
it is `METRIC_SET.measurement_scope_level`. For an externally authored one it is whatever
level the external standard measures at, which is frequently a level this organization's
own chain does not contain and which no internal binding will describe. Where the external
level does not map onto `SCOPE_LEVELS`, say so, roll to the nearest level that does, and
name both. Never substitute the internal measurement level for the external one: the two
answer different questions and only one of them is the score the entity is actually held
to.

### 4b.3 A binary flag and a degree flag are siblings

Where a requirement has both a presence test and a completeness test, both are needed and
neither replaces the other: an entity failing the presence test cannot fail the degree
test, because it has no figure at all (SD-EXC-15). Score both, and do not let the ratio
metric's blindness to a zero denominator hide the entities that have nothing.

## Step 5. Build the deliverable

**reference/output-contract.md, the universal output contract, GOVERNS this step. It is cited here and
never restated.** A restated contract is how this skill drifted the first time: the
formatting rules survived as prose, nothing ran them, and a workbook shipped with no
autofilter on any sheet, no rank column on its main sheet, no consolidated reason column
and no cap. Prose is not a contract. Where this file appears to say something
reference/output-contract.md says differently, that file governs and this file is stale.

`OUTPUT_MEDIUM` for this skill is xlsx, so reference/output-contract.md PART 2 applies in full and PART 3
does not. Every element is verified programmatically against the BUILT artifact before
publication, per PART 7, and a failure blocks publication.

### 5.0 The ranking basis is SEVERITY, and it is never harmonized with opportunity

**This skill ranks by what is most broken. The planning skill ranks by where the
opportunity is. Those are different orders over the same entities and the difference is
deliberate.**

- **The severity basis:** the count of attributable GAP cells on the row, weighted by the
  published priority weight of each failing requirement where one is bound (`METRIC_SET`
  weights, SD-PRI-31), then the tie-break ending in the identifier ascending (SD-RNK-10).
- **The entity's size, value, revenue or measure DOES NOT ENTER IT.** Not as a factor, not
  as a multiplier, not as a tie-break. A small entity with six gaps outranks a large one
  with one, and that is the whole point.
- **Blocked gaps do not drive the rank.** The rank runs on ATTRIBUTABLE gaps, per A4,
  because a list ordered by things the reader cannot close puts unactionable rows at the
  top. The full gap count is still published on the row; only the ordering excludes them.

**Why this must be stated rather than assumed.** Both skills now share one output format,
and a later reader will reasonably wonder why two ranked lists over the same accounts
disagree and will be tempted to reconcile them. They must not be reconciled. The shared
format is what lets a reader move between the two documents; the different bases are what
stop the second document being a copy of the first. A scorecard ranked by opportunity is a
second work plan, and this skill would have no reason to exist.

### 5.1 The six tabs

Six, in this order, every run. A tab with nothing to report still ships, carrying its
header and exactly one row saying why in plain language (SD-CTR-07), and that row is
written as a zero sentence rather than a plural with a nought in it (SD-LNG-13).

| # | Tab | Declared sheet CLASS, and KIND where it is ranked | What it holds |
|---|---|---|---|
| 1 | **Front Panel** | PANEL SHEET. Not a ranked sheet | Where the reader stands, what is broken, what is blocked, the period state, and every disclosure that changed a published number |
| 2 | **Priority Fixes** | ENTITY SHEET. Ranked kind: EXTRACT, of tab 3 | The worst entities extracted from the census, ranked worst-first, carrying the census's own rank numbers |
| 3 | **Scorecard** | ENTITY SHEET. Ranked kind: CENSUS | Every entity in scope, one row each, one column per requirement, ranked worst-first, with the `HDR_FAILS` count and the narrative string |
| 4 | **Summary** | REFERENCE TABLE. Not a ranked sheet; ordered by pass rate ascending | Pass rate per requirement across the scope |
| 5 | **Legend** | REFERENCE TABLE. Not a ranked sheet; ordered | Every code in plain English with the action it implies |
| 6 | **Method** | PANEL SHEET. Not a ranked sheet | The audit trail, exhaustive by design and last |

**THE CLASS AND KIND COLUMN IS A DECLARATION, NOT A DESCRIPTION, AND IT IS WHAT MAKES THE
VERIFICATION RESOLVE.** reference/output-contract.md 2.0 requires a skill to declare each sheet's
CLASS and PART 4.2 requires a ranked sheet to declare its KIND, and PART 8 lists both among
the things a skill may do with that file. **2.0's class table and PART 7.2's matrix now
agree, and where a scope is given more loosely in the table than in the matrix row, the
matrix row governs**, because it is written per row and the table column is written per
class. That is the file's own statement and this step is built to it. Both declarations are recorded on the Method
sheet per 5.7, so a reader can see which elements were expected to run where rather than
inferring it from what the verification happened to check. Each row of the verification
matrix is then run on the sheets ITS OWN class column names and is NOT APPLICABLE
elsewhere, with the sheet class as the stated reason. What the declarations settle for this
workbook, without a reader having to work any of it out:

- **Elements 1 to 14 and 16 bind tabs 2, 3, 4 and 5**, because a reference table is a grid
  in every respect those elements care about. Element 15 is NOT APPLICABLE on those four,
  with the sheet class as the reason.
- **Elements 15 and 16 bind tabs 1 and 6.** Elements 1 to 14 are NOT APPLICABLE there, with
  the sheet class as the reason, which is why cell A1 of a panel holds a title and does not
  fail row 1 of the matrix. **R3 and R5 still reach both panels**: R3 wherever a panel is
  itself capped, and R5 because it scans the whole workbook. Neither becomes inapplicable
  because a sheet is a panel, and neither is scoped by sheet class at all.
- **R1 runs on all four grids**, in its RANK form on tabs 2 and 3, whose order is a merit
  order, and in its POSITION form on tabs 4 and 5, whose order is not. See 5.3 and 5.6 for
  which header variable each takes.
- **R2 does not run on this workbook's ranked sheets at all.** It is scoped to MERIT TIER
  SETS, and this workbook emits a census and an extract of it, which share identifiers by
  construction. R2 is recorded NOT APPLICABLE with that scope as the reason, per 5.8.
- **R3 runs on every BOUNDED sheet whatever its class**, which is its own scope in the
  matrix, and reference/output-contract.md 5.1.1 gives the three bounds a sheet's row count can
  have and what `N` means under each. On this workbook that is tab 3, bounded by
  `REFERENCE_CAP`; tab 2, bounded by its own DECLARED SIZE, with `N` the census's row count;
  and tabs 4 and 5, which are capped sheets like every other capped sheet. **CAPPED MEANS
  SUBJECT TO A CAP, NOT CUT BY ONE**, so a reference table holding thirteen rows under a cap
  of five hundred is a bounded sheet that lost nothing and ships its note with `n` equal to
  `N`. R3 reconciles the built unit row count against that sheet's note band and against
  Method on every one of them.
- **R4 runs in its CENSUS form**: tab 3's row count equals the census form
  `min( REFERENCE_CAP , eligible_count )`, and tab 2 holds its declared size. The merit-tier
  quantities `tier_1_size`, `last_visit_rank` and the derived last merit rank do not exist
  on this workbook, and a check that reads them here is testing a number this skill never
  produced.
- **R5 runs over the whole workbook** and is not scoped by sheet class either, so no
  hard-coded unit noun may disagree with `UNIT_NOUN_SINGULAR` or `UNIT_NOUN_PLURAL` on any
  sheet of any class, panels included.
- **R1 and R2 are the only two R rows that turn on the entity-versus-reference
  distinction**, and 7.2 says how each of them does.
- **The Legend is declared a REFERENCE TABLE and not a panel**, which 2.0 expressly permits
  a skill to choose, provided it chooses. It is emitted as a grid with one row per code, so
  it takes every grid element. Declaring neither is the one thing that is not allowed, and
  it is how one sheet came to be scored against two families of element in one bundle.

**The report title lives on the front panel and nowhere else**, because element 1 puts the
header row of every entity sheet in row 1 with no banner, no title and no note above it.
That element is first in the contract because every other element depends on it. Element 1
governs what sits ABOVE the header row and nothing else; a note BELOW the grid has its own
place and 5.10 gives it.

**The section names come from `TAB_CONTRACT`, keyed to this skill, and the schema's
documented default for that key is the six sections above in the order above.** Because the
medium is a workbook, each section's title BECOMES A SHEET NAME, so every one of those
values satisfies the SHEET-NAME CONSTRAINT the schema states once in its Group 15: at most
31 characters after any prefix or suffix the run composes on, none of the six forbidden
characters, unique within the workbook compared case-insensitively, and stable between
runs. A bound value that violates it is repaired by the schema's own truncation rule, which
is stated there so that two runs truncate identically, and never by this file choosing for
itself. **AND EVERY ONE OF THOSE SECTION NAMES IS TITLE CASE, in the one convention
`TITLE_CASE_HEADINGS` states, because a sheet name is a heading (SD-FMT-13). SO IS EVERY
COLUMN HEADER ON EVERY SHEET: the exemption that used to hold table column headers in
sentence case is WITHDRAWN.** The single exemption that stays is a string the ORGANIZATION
BOUND, which ships in the case it was bound in, since those are the organization's own
words; a DOCUMENTED DEFAULT is not a bound string and is already written in Title Case
where it is documented, so this file re-cases nothing at run time and SD-CTR-24 is
untouched. The two
now agree, on the count and on the order, and the agreement is deliberate: a run that
resolves the variable and a run that reads this step must build the same workbook. An
earlier default named seven sections, restored an exceptions section this file had removed,
and put the census before the worklist, so a literal implementer of the schema and a
literal implementer of this step shipped different artifacts off one configuration. Where
an organization binds `TAB_CONTRACT` for this skill, the bound list governs the names and
the order, per SD-CTR-24; where it does not, the default and this step say the same thing.

**The exception content is not lost with the seventh tab.** What an exceptions sheet
carried now sits in two places, both of which a reader reaches sooner: the material items
on the FRONT PANEL under what is broken and what is blocked, and the full enumeration in
METHOD. Nothing is dropped, and the front panel names each item, its count and what would
clear it: requirements whose evidence column resolved and is empty; requirements with no
evidence field mapped; requirements whose eligibility could not be determined; entities
excluded as not workable with the distinct values that excluded them; entities with no
evidence at all this period; evidence sources unreachable; scope levels suppressed as
person-bearing under A9; and every subset suppressed by an influence finding under 4.4b.

### 5.2 Tab 1, Front Panel

A panel sheet. **IT OPENS BY SAYING WHAT THE READER IS HOLDING, AND THE QUALIFICATIONS THAT
CHANGE HOW A RATE IS READ STILL SIT ABOVE THE RATES.** Those are two different orderings and
an earlier revision had them fighting: it put up to a dozen lines of per-requirement caveat
above the report's own title, so on one measured run a reader met nineteen rows of
qualification before the panel said what report they were holding or whose scope it covered.
Every one of those lines was right. The ORDER was defended nowhere, and the finding-first
principle this section itself cites cuts the other way (SD-LNG-03, SD-CTR-14). The order
below separates the two questions and settles it once.

**FIRST, AND BEFORE ANYTHING ELSE: the report title, the scope and the period.** A reader
who cannot tell in one line what they are holding cannot read a caveat about it either.
Element 15 also puts the title in cell A1 of this panel, and the two agree.

**THEN, AND STILL BEFORE ANY RATE, the things that change how a rate is READ.** Each of the
following is a statement about the whole figure, not about one requirement, and a reader who
meets the rate first will read it wrongly:

1. **The period state and its dates**, per 3.5.1, **and, where the evidence source's own
   period stamp names a different window from the one the calendar rules resolved, both
   windows, which governed and why, and the count of rows whose urgency state differs
   between the two readings**, per 3.5.
2. **The mandatory disclosure** from 4.4 and 4.4b wherever it fires, with both counts.
3. **The statement that unassessable cells are excluded from the pass-rate denominator.**
4. **ONE LINE, and one line only, saying how many requirements are marked recency-untested
   per 3.5.2, how many of those carry a recency clause in their own met-condition, and that
   each is named below the rates.** A count changes how the rates are read and belongs here.
   The enumeration does not, because it is a fact about individual requirements and a reader
   cannot use it until they have the figure it qualifies.

**THEN THE RATES:** the conformance rate, the attributable conformance rate and the
assessability rate, all three, under the labels 3.5.1 gives them where the period state is
NOT YET STARTED and under A4's names otherwise, with the difference between the first two as
a number; the second number from A5 with its rung, its unit and its strength; the mix
numbers from A5.1 wherever a peer comparison ships.

**THEN, IMMEDIATELY BELOW THE RATES, THE PER-REQUIREMENT ENUMERATION ITEM 4 PROMISED**, and
it is mandatory and is not shortened: **every requirement marked recency-untested**, per
3.5.2, and among them, NAMED ONE BY ONE with their own met-condition's recency wording
quoted, every requirement whose met-condition itself carries a recency clause. A pass on one
of those is evidence that something is on file and is not evidence that it is current, and
every such pass cell says so in the cell as well, per A3, through its qualifier code. **The
enumeration MOVED and nothing was dropped**: the count is above the rates, the names are
below them, both are on this panel, and a reader who wants the list reaches it without
scrolling past the answer to get to the question.

**THEN EVERYTHING ELSE, in this order:** every clause of a met-condition reported as a HOLE
under A3, per requirement, with the clause quoted and the evidence read in its place named;
the edition of the standard read and its date; the evidence source and its age with the
ladder rung that produced it, per 3.5.2; the population funnel with two numbers per step
(SD-POP-20), naming which reading of the not-workable exclusion was applied (SD-POP-30),
every distinct status value under EXCLUDED or KEPT with its count, and the three numbers
reconciling that exclusion against the standard's own entity-class scope per 4.1 step 1;
**the completeness statement and the cap statement as two separate lines**, per A7; **the
grid-width line where any grid shipped over `GRID_MAX_TOTAL_WIDTH`**, per
reference/output-contract.md 2.7, telling the reader that the sheet is wider than the bound and that
the freeze and the filter are how it is meant to be read; what is broken and what is
blocked, per 5.1; a line naming any scope level suppressed as person-bearing and what was
published instead (A9.4); every degradation on its own line with what it changed (Part E);
`METHOD_OWNER_STATEMENT`, `MSG_AUTHOR_LINE` and `TUNING_INVITATION`.

The finding leads and the methodology follows (SD-LNG-03, SD-CTR-14). **That principle is
what put the title first and what put the enumeration below the rates**, and the three
statements that still sit above them are there because each is a property of the rate itself
rather than a caveat about the run.

### 5.3 Tabs 2 and 3, the entity sheets

Both are declared ENTITY SHEETS per 5.1 and both take the full contract: every element in
reference/output-contract.md PART 2 that binds an entity sheet, plus R1, R4 and R5 of the
verification matrix, and R3 on BOTH of them, because R3 binds every BOUNDED sheet per
reference/output-contract.md 5.1.1 and both are bounded: tab 3 by `REFERENCE_CAP` and tab 2 by its
own declared size. **R2 is NOT APPLICABLE on this pair**, with its own scope as the stated reason: it is scoped to merit
tier sets, and tab 2 is an EXTRACT of tab 3's census, which shares every identifier it
carries by construction. Their identity blocks are
structurally identical to each other (SD-CTR-08), verified by header name and relative
order rather than by column number.

**EVERY HEADER BELOW IS WRITTEN AS A VARIABLE AND NEVER AS A LITERAL.** The variable is
what the sheet is built from and what the verification reads back; a header string typed
into this file is a second source of truth that nothing updates, and PART 4.1 and PART 8
both forbid it. An organization that wants to call the count of failing requirements
something else in its own language binds one value and every sheet follows.

**Column order, left to right, on both:**

1. **The position column**, `HDR_RANK`, a fixed identity column in first position, per
   PART 4.1. Both sheets are ordered on the severity basis in 5.0, which IS a merit order,
   so the rank form of the header is the correct one here and `HDR_POSITION` is not used on
   these two sheets.
2. The identity block from `IDENTITY_BLOCK_COLUMNS`: the entity identifier and name, then
   the span-of-control columns showing the levels below the requester and never their own
   (SD-SPN-01, SD-SPN-02, SD-SPN-03, SD-SPN-05), formatted as text so leading zeros
   survive (SD-SPN-06). Where a level is person-bearing it appears as an attribution
   column only and never as a grouping (A9). **The block is declared MOST-IDENTIFYING
   FIRST**, per PART 4.1.2: the position column, then the entity identifier, then the
   entity name, then every other identity column, so that a span the width bound truncates
   keeps the columns that answer "which entity is this row".
3. **The reason-for-rank column, `HDR_RANK_REASON`**, per PART 4.1 and PART 4.1.1: **the
   FIRST COLUMN AFTER THE IDENTITY COLUMNS, closing the identity block, and never inside
   the frozen span.** It says why this entity sits where it does, naming the terms that
   decided it in the order they contributed. For example: four attributable gaps, two of
   them on high-weight requirements, ahead of the next entity on gap count.
   `HDR_RANK_REASON` is the ONLY variable for this column. A second name for it was defined
   in the schema with an identical default, was cited by nothing, and is retired; do not
   reintroduce it, and do not write the column's header as a literal, because the literal
   and the variable's default were different words and a run that wrote the literal produced
   a header no binding described.

   **THIS POSITION IS THE CONTRACT'S AND IT IS THE ONLY ONE.** An earlier revision of this
   step put the column second from last, between the count columns and the narrative
   column, while PART 4.1.1 and verification row 2 both put it at the head of the sheet and
   tied the freeze point to it. The two could not both hold, and a literal build of either
   failed: freezing at a column eighteen places along a twenty-one column sheet pinned
   seventeen columns and every character-width of the sheet, so scrolling right reached
   nothing, and freezing after the identity block instead failed verification row 2 and
   blocked publication. PART 4.1.1 governs, this file is built to it, and PART 8 forbids
   any skill to put the column anywhere else. SD-FMT-24 is the doctrine and it carries the
   same statement of position.
4. **The commitment-date column, `HDR_COMMITMENT_DATE`, and the urgency column,
   `HDR_URGENCY`**, per 5.5. `HDR_COMMITMENT_DATE` is the variable for this column and
   there is no second name for it: the header a reader sees is whatever that one variable
   is bound to, and this file writes no alternative word for it anywhere.
5. One column per requirement scored this period, each cell carrying its symbol, its state
   code, its reason code and, on a qualified pass, the qualifier's CODE, as text, per A3.
   **The standard's own wording is NOT in these cells**; it is in the narrative column, per
   4.1 step 9 and 5.4. **The pass qualifier's own wording is not in these cells either**; it
   is in the Legend against its code, per A3 and reference/output-contract.md 2.7. **Every one of
   these columns is a DECLARED CLASSIFICATION COLUMN under reference/output-contract.md 2.6**,
   declared on Method per 5.7, carrying the fills of `CLASSIFICATION_FILLS` keyed on the
   states of `CLASSIFICATION_VOCABULARY` by the total resolution rule 4.6 publishes. Under
   the standing bindings they are LEFT ALIGNED, because they fail 2.5's centring bound, and
   a left-aligned classification column is the ordinary case and carries its fill exactly as
   a centred one would.
6. **`HDR_FAILS`**, the count of GAP cells on the row. **`HDR_BLOCKED`**, the count of
   those that are `BLOCKED_EXTERNAL`, shown wherever any exist. **`HDR_UNASSESSED`**, the
   count of UNASSESSABLE cells, which is a coverage figure and is never added to the gap
   count. All three are numeric and land in `RIGHT_ALIGN_COLUMNS` by that variable's own
   membership rule rather than by anybody remembering to put them there.
7. **The trailing narrative column, `HDR_NARRATIVE`**, per 5.4 and element 11. Last and
   widest.

**THE FROZEN SPAN IS BOUNDED, IT IS COMPUTED ONCE FOR THE WHOLE ARTIFACT, AND THIS FILE
ADOPTS THE BOUND RATHER THAN RESTATING IT.** reference/output-contract.md PART 4.1.2 states it
once: `FROZEN_SPAN_MAX_WIDTH` bounds the SUMMED BUILT WIDTH of the frozen span; **the walk
runs ONCE FOR THE ARTIFACT, from the WIDEST CASE**, taking each identity column's maximum
BUILT width across every entity sheet and reference table that carries the full identity
block; the identity columns are then walked left to right; the span ends at the last column
whose inclusion keeps the running sum at or under the bound, and that column is
`IDENTITY_BLOCK_ANCHOR_COLUMN`, **which is the anchor for EVERY sheet of this workbook**;
the first column is always frozen even where it alone exceeds the bound; and the freeze is
then set at row 2 and at the first column after the anchor, **located BY HEADER NAME on each
sheet**, per element 2.

**A GENUINELY NARROWER SHEET FREEZES THE SAME COLUMNS IN FEWER WIDTH UNITS, AND MAY NEVER
FREEZE MORE.** The anchor is a COLUMN and not a width. A sheet whose name column holds no
value falls back to its own header floor, so its span is narrower in units and holds exactly
the same columns; that is the intended outcome and it costs the reader nothing. **What no
sheet ever does is freeze MORE columns than the widest case allows.** This is not a
refinement of the bound but the thing that makes SD-CTR-08 true of a workbook rather than of
each sheet separately: identical columns in identical order with the pin in a different
place per tab is not a structurally identical identity block, because what the reader
experiences moving between tabs IS the pin. A per-sheet walk was measured stopping in a
different place on the merit sheets and on the empty ones of one workbook, every sheet
individually conformant and the workbook not.

**Nothing is moved, nothing is dropped and nothing is narrowed to make the span fit**, and
in particular no column is narrowed below its own 2.2 header floor, which would trade a
readable freeze for an unreadable header. **The record is ONE LINE FOR THE ARTIFACT AND
NEVER ONE LINE PER SHEET**, on Method per 5.7: the bound, the summed WIDEST-CASE built width
of the span, which sheet supplied the widest case for each identity column walked, and every
identity column left outside the span by header name; where the bound does not truncate, the
same one line states the summed widest-case width and that the whole identity block is
frozen on every sheet. Verification row 2 reads it, and asserts as well that the anchor's
header NAME is identical on every sheet carrying the full identity block, so a workbook
whose tabs freeze different numbers of columns FAILS that row even where each tab is
individually inside the bound. Six records of one identity block are worse than none, and a
silently shortened freeze is indistinguishable from a broken one, which is why the one
record is not optional.

**THE GRID'S TOTAL WIDTH IS A SECOND BOUND AND NEITHER SUBSTITUTES FOR THE OTHER.**
reference/output-contract.md 2.7 bounds the SUMMED BUILT WIDTH of every column of one entity sheet
or reference table by `GRID_MAX_TOTAL_WIDTH`, in the same width unit the span bound uses;
SD-FMT-28 is the doctrine and verification row 10 asserts it. The span bound says what stays
on screen and this one says how much there is, and a sheet can honour the first perfectly
and still be ten screens wide: measured on one build, three columns stayed correctly pinned
and the census was still 21 columns and 749.12 width units across, so the reader read the
sheet through the filter, one column at a time, rather than by moving across it.

**WHAT THIS FILE DOES ABOUT IT, IN ORDER, AND IT DOES NOT RESTATE THE LADDER.** The value of
`GRID_MAX_TOTAL_WIDTH` is READ BEFORE THE COLUMNS ARE BUILT and recorded on Method, and **a
run never raises it to clear a grid that failed it**. The build then runs 2.7's relief
ladder in the order 2.7 gives, and this skill's one standing qualifier is already out of the
cell before the ladder starts, because A3 puts it in the Legend against its code as a
standing decision rather than as a width remedy. **The three things that never give are 2.7's
and they bind here without exception:** no column is dropped, no column goes below its own
2.2 header floor, and no value that carries meaning is shortened, which on this workbook
means no entity name, no identifier, no date, no reason code and no per-row finding is ever
abbreviated to save width. Where the grid is still over the bound after the ladder has run
to exhaustion, **it ships over the bound and says so**: Method records the bound, the
measured total, the overage and the columns that account for it in descending order of built
width, and the front panel carries 5.2's one line. **An honest overage is the correct last
outcome**, because every other way out is one of the three things that never give.

**MEASURE IT, EVERY RUN, AND RECORD THE MEASUREMENT WHETHER OR NOT IT FAILS.** The summed
built width of every grid in this workbook is computed from the built widths after 2.2 has
run, printed on Method per sheet against the bound, and read back by verification row 10
before publication. A bound that is only measured when somebody suspects a problem is not a
bound, and a passing measurement is the evidence the check ran (SD-EXC-06).

**WIDTHS AND HEIGHTS ARE THE CONTRACT'S ARITHMETIC AND THIS FILE CARRIES NO SECOND VERSION
OF IT.** reference/output-contract.md 2.2 defines three primitives and 2.2.4 states the one
direction the composition runs in; 2.3 computes every row height from the greedy wrap of
primitive 1 against the BUILT widths, and 2.4 does the same for the header row. This file
states no formula, no factor, no line count and no padding, and it carries no reconciliation
between two of them (SD-FMT-23): a build that computed a row height two ways and took the larger was
working around a contradiction that no longer exists in the contract, and reintroducing
such a workaround here would put a second algorithm back into a place that now has one.

**The reason-for-rank column and the narrative column are different columns and neither
replaces the other.** The reason says why the row is HERE; the narrative says what is WRONG
with it and what to do about it. A sheet carrying one and calling it the other has failed
R1. They are also the two columns most often collapsed into one by an implementer who reads
them as duplicates, which is why PART 4.1 says the same thing and why both headers are
bound separately.

**Tab 2, Priority Fixes. Declared an EXTRACT of tab 3's census**, per reference/output-contract.md
PART 4.2.3, and the declaration is made on the sheet itself, in its note band per 5.10, and
in Method: which sheet it is an extract OF, and how many rows it takes. **Its size is this
skill's own declaration, and the declared size is the sum of the two tier sizes in
`DELIVERABLE_LINES` for the resolved role.** Those sizes are the length of the list a
person of that role receives; they are not merit-tier boundaries, because this workbook has
no merit tier set. `tier_1_size`, `last_visit_rank` and the derived last merit rank are
merit-tier quantities, they mean nothing on a census workbook, and this file names none of
them as the size of anything.

**The decision on those sizes, and the reason, because the standing defaults were
questioned and keeping them is a choice rather than an omission.** They stay. The case
against them is that a top ten of worst offenders is too few when one requirement fails
across sixty entities, and that case is real but it is not an argument about this tab. One
requirement failing across sixty entities is a REQUIREMENT-shaped problem, and this skill
already answers it twice, better and elsewhere: tab 4 orders requirements worst-first by
pass rate and puts that requirement at the top with its count, and tab 3's autofilter
returns all sixty rows in one click, bounded by `REFERENCE_CAP` rather than by a tier size.
Lengthening an entity list to answer a requirement question would give the reader sixty
rows that all say the same thing, and a long ranked list is a roster rather than a plan
(SD-RNK-08).

The sizes remain bindable, and the signal to raise them is different from the one that
prompted the question: where a reader's own scope routinely produces more entities with
attributable gaps than the tiers hold, across several periods, that organization binds
larger tiers once. It is never overridden per run to absorb an overflow.

**What the EXTRACT declaration settles, and this file no longer argues any of it for
itself.** reference/output-contract.md PART 4.2.3 now carries the whole of it, and the three things
that used to be defended here are the three that file states:

- **It carries the census's OWN rank numbers for the rows it holds and never re-ranks from
  1.** A row at census rank 34 is at rank 34 here, so a reader who finds an entity on both
  sheets sees one number, which is the whole point of a rank.
- **It duplicates every identifier it carries, by construction, and that is not a defect.**
  It is a view of the top of the census, not a separate population, and R2's
  no-duplicate-identifier assertion does not run between a census and an extract of it.
- **It declares what it is an extract of and how many rows it takes**, on its own sheet and
  in Method, because without that a reader cannot tell an extract from a tier and neither
  can a verification.

**IT IS A BOUNDED SHEET AND IT SHIPS THE SHOWING NOTE**, per reference/output-contract.md PART
5.1.1, whose table gives the third bound: an extract's DECLARED SIZE, with `n` the unit rows
written to the extract and **`N` the unit row count of the CENSUS it extracts from**. So a
seventy-row extract of a hundred and ninety row census states `showing 70 of 190`, in the
exact wording PART 5.2 gives, in its note band. This is the note a reader most needs and the
one that was missing: the extract is the first grid a reader opens and the sheet whose row
count is least self-explanatory, and without it the sheet shows seventy rows and says
nowhere that a hundred and twenty more exist, so a reader who takes it for the whole
population acts on a fifth of their book. R3 reconciles it against the sheet and against
Method like any other bounded sheet.

**THE SHOWING NOTE AND THE SHORTFALL NOTE ARE TWO DIFFERENT NOTES AND ONE IS
UNCONDITIONAL.** The showing note ships every run whatever the counts. The SHORTFALL note,
which says the sheet holds fewer rows than its own declared size allows, ships if and only
if that is true (SD-RNK-06). It is also bounded by PART 5.1's cap like any other sheet.

**Tab 3, Scorecard. Declared a CENSUS**, per reference/output-contract.md PART 4.2.2: every entity
in scope, ranked worst-first, holding ranks 1 through `min( REFERENCE_CAP , eligible_count )`
and holding that many rows. A census starts at 1 and does not resume after anything,
because there is no tier before it to resume from; a census that started at a merit tier's
last rank would omit its own worst entities from its own census, which is not a census.
**It is capped like every other capped sheet and it states the showing note in the exact
form reference/output-contract.md PART 5.2 gives, in the note band 5.10 gives it.** The
filter across every column is what turns this grid into a tool: one click isolates
every entity failing one requirement, every overdue row, every blocked cell. That is
element 6, it is the single most-used feature of a delivered workbook, and a sheet
shipping without it has failed. **AND IT IS THE SHEET'S OWN FILTER, DECLARED ON THE
SHEET, WITH EXACTLY ONE FILTER OBJECT OVER THE RANGE**, which is element 6's mechanism
and not this file's choice: a filter carried only inside the table object is the form
much of what opens these workbooks does not read, and the delivered files shipped with
no visible filter control on any sheet while a check that read it out of the table
container recorded a pass. **THE MECHANISM IS CHOSEN FOR THE ENGINE THE READER OPENS
AND NOT FOR THE ONE THE FILE WAS BUILT IN. SD-FMT-29.** Where the engine cannot carry
both a table object and a visible filter over one range, element 3 gives and the visible
filter stays, per elements 3 and 6, and the conflict is named in Method.

Sort both worst-first on the severity basis in 5.0. Never sort by a classification label
(SD-RNK-11) and never by the column `HDR_COMMITMENT_DATE` heads (5.5). That column is named
by its variable here as it is everywhere else in this file: an earlier revision wrote a
retired literal word for it in this one sentence, inside the step whose own opening
sentence says every header is a variable and never a literal, and a second source of truth
is a second source of truth however small the sentence carrying it is.

### 5.4 The Why string, and its exact form

**"The Why string" is this file's short name for the CONTENT of the trailing narrative
column, whose header is `HDR_NARRATIVE` and is never written as a literal.** The name is
used below because it is what the string does, and it is not a header. The same applies to
the two other short names this file uses in prose: the "Fails count" is the content of the
`HDR_FAILS` column and the "Reason for rank" is the content of the `HDR_RANK_REASON`
column.

A single readable string in the right margin consolidating the row's reasons, so a reader
gets the story without scanning nineteen columns. It is **in addition to** the per-cell
codes, never instead of them.

**The form:** a semicolon-joined list, each entry `requirement name: STATE CODE` with any
qualifying detail in parentheses, joined by a semicolon and a space.

**THIS COLUMN IS WHERE THE STANDARD'S OWN WORDING LIVES**, per 4.1 step 9, which moved it
out of the status cell. Where the reader needs the requirement's own words to know what to
do, the entry carries them AFTER the finding and introduced as the requirement, in the
three-part order 4.1 step 9 fixes: the code, the finding stated as an absence, then the
requirement clearly framed as the requirement. The inversion trap moves here with the
wording and is defused here by the same ordering. Element 11 makes this column last and
widest and it is never truncated, which is exactly why it is the column that can carry a
sentence and a requirement column is not.

**THIS COLUMN IS ALSO WHERE reference/output-contract.md 2.7'S SECOND RUNG SENDS EVERY REMAINING
PER-ROW PROSE FRAGMENT, AND THAT IS WHY THE GRID'S TOTAL WIDTH IS THIS SECTION'S BUSINESS
AS WELL AS 5.3'S.** 2.7 bounds a grid's summed built width by `GRID_MAX_TOTAL_WIDTH`, and
the ladder it runs decides WHAT A CELL CARRIES, which is exactly what this section decides:
a sentence belongs in ONE wide column read once, not spread across eight columns and read
eight times. So a per-row fragment that is not a status cell's own answer comes here, and a
STANDING QUALIFIER, which is the same words on every row that carries it, goes to the Legend
against its code instead and never here, per 2.7's own three-way placement rule and per A3.
**Element 11's own bound on this column's width is unchanged and is never raised to absorb
what the ladder moved**, which is the one way rung 2 can be done wrongly: this column is
already the widest on the sheet and widening it further to hold what eight columns used to
hold would spend the whole saving in one place. Where the material genuinely will not fit
inside element 11's range, it is a Legend or a Method fact and not a per-row one, and 5.6
and 5.7 are where it goes.

> `Loss runs on file: GAP NOT_DONE; Certificate backlog: GAP EXPIRED; Appetite
> confirmation: GAP BLOCKED_EXTERNAL (counterparty); Flood determination: UNASS (no
> evidence captured this period)`

**The ordering inside the string:** GAP entries first, then UNASSESSABLE, and within each
group the sheet's own column order so the string reads left to right like the grid.
NOT REQUIRED entries are omitted entirely: they ask for nothing, and including them
dilutes the one column a hurried reader actually reads.

**Where the row has no non-pass cell**, the string reads `no open items`. That is the zero
sentence, and it ships rather than an empty cell (SD-LNG-13).

**It is never truncated.** A truncated Why hides a gap, which is the failure this whole
skill exists to prevent. The Fails count is the at-a-glance number; the Why carries all of
them; element 11 makes the column widest and element 12 computes the row height from the
wrapped content, so nothing clips at any length.

### 5.5 The urgency dimension, which is two columns and an autofilter

A reader works a list in the order the calendar demands, and a severity-ranked list puts an
entity renewing in eight days below one renewing in four months. Give them both, without
letting the calendar decide who is on the list.

- **The commitment-date column, headed `HDR_COMMITMENT_DATE`,** carries the entity's own
  commitment date, resolved through `concept_unit_commitment_date`: a renewal, an expiry, a
  term end, a next review, a certification or licence expiry. It resolves by exact name
  only and declares its forbidden neighbours, so a last-contact date is never read as a
  commitment. Its header is that one variable and this file writes no other word for it.
- **The urgency column, headed `HDR_URGENCY`,** carries one value per row, and **THE
  VALUES ARE LOOKED UP FROM `URGENCY_VOCABULARY` BY STATE KEY AND ARE NEVER WRITTEN FROM
  THIS FILE'S OWN PROSE.** That taxonomy is a closed set of exactly FIVE state keys, one
  per state, and an organization binds what each state is CALLED without adding, removing
  or reordering the keys. The five keys and the condition this skill computes each from are
  below; the STRING written into the cell is that key's bound `label` and nothing else. The
  horizon is the operating window itself, so no new threshold is bound and it moves
  correctly with the business.

| State key | The condition this skill computes it from |
|---|---|
| `no_date_on_file` | No commitment date resolved for the row |
| `due_this_window` | The date falls inside the operating window |
| `later` | The date falls after the operating window closes |
| `overdue` | The date falls before the window OPENS and the row carries at least one ATTRIBUTABLE gap cell |
| `passed_nothing_outstanding` | The date falls before the window opens and the row carries NO attributable gap cell |

- **THE FIVE KEYS ARE TOTAL OVER THE ROWS AND THE TOTALITY IS THE VALIDATION**, per standing
  rule S10 in reference/schema/, which this file cites rather than restating: validate from
  the STATES the rule above can emit to the SET, never from the set to the states, whenever
  either changes. A row either has a date this run resolved or it does not; where it does,
  the date falls inside the window, after it, or before it, which is three cases and no
  fourth; and the before-it case splits on whether anything is outstanding, which is two and
  no third. **A run never invents a value and never takes the nearest available one.** Where
  a row reaches a state this set cannot name, the run reports the row, names the state it
  could not write, and the set is extended by the binding owner. An earlier revision listed
  four values in prose and had no member for a row whose date had passed with nothing
  outstanding on it: `overdue` was forbidden by the rule below, the two window-relative
  values were false statements about the date, and the not-on-file value was false because a
  date was on file, so on one measured run five rows out of a hundred and ninety had nothing
  correct to write and had to be named in the Legend by hand.
- **THE ANCHOR FOR THE `overdue` STATE IS THE WINDOW'S OPENING DATE, NEVER THE RUN DATE**,
  and the anchor date itself is printed in the Legend and in Method. A date has PASSED when it
  falls before the operating window OPENS. The two readings are usually the same date and
  are not always: a report built weeks before a window opens separates them by exactly that
  many days, and on a measured run nine entities sat between the two readings with nothing
  in the file to decide them. Anchoring on the window rather than on the run date is the
  same discipline the schema states for `CLOSE_HORIZON_DAYS`, for the same reason: a report
  built early must band identically to the same report built on the window's first morning,
  or the published order moves with the hour somebody pressed go.
- **THE TEST IS PER ROW, ON ANY UNMET REQUIREMENT THE READER CAN CLOSE, because there is
  ONE urgency column and a row has one value.** A row takes the `overdue` state when its
  commitment date falls before the window opens AND the row carries at least one
  ATTRIBUTABLE gap cell. It is not per requirement: a per-requirement urgency cannot exist
  in one column, and inventing one column per requirement to carry it would double the width
  of the grid to express a calendar fact that belongs to the entity and not to the
  requirement. A row whose every cell is PASS, NOT REQUIRED or UNASSESSABLE takes
  `passed_nothing_outstanding` and never `overdue`, whatever its date, because there is
  nothing outstanding on it to be late.
- **OUTSTANDING MEANS OUTSTANDING FOR THIS READER, AND THE DEFINITION IS PUBLISHED.** A gap
  cell counts toward the `overdue` test only where it is ATTRIBUTABLE in the sense A4 fixes:
  its reason code's bound `resolvable_by` names this reader rather than somebody else. That
  is not a new test and it is not a judgment made per cell; it is the same test 5.0 uses as
  the ranking basis and the same one 4.4b step 5 uses to keep a `BLOCKED_EXTERNAL` cell off
  this reader's worklist. **All three now say the same thing about the same cells**, which
  they did not: the rank excluded blocked cells and the worklist excluded them, while the
  one filter the reader actually clicks did not, so on a measured run 7 of 70 `overdue` rows
  carried no attributable gap at all and their only gap was a confirmation a counterparty
  had closed. A reader who does what this section tells them to do, click the urgency filter
  to reach the near-term work, was handed seven rows with nothing this organization could
  act on. The Legend states the definition in one line: a row is late when something the
  reader can close is late, and a blocked shortfall is carried by the `HDR_BLOCKED` count
  and not by this column.
- **THE TWO WINDOW-RELATIVE STATES ARE STATEMENTS ABOUT THE DATE AND NOTHING ELSE**, and
  this file says so rather than letting a reader infer otherwise. `due_this_window` and
  `later` do not split on outstanding work, because the vocabulary's own totality argument
  splits only the before-the-window case; a row due this window with nothing attributable
  outstanding is correctly `due_this_window`. So that a reader combining the filter with the
  count columns is not surprised, **the Legend prints, per state, the count of rows in it
  that carry no attributable gap**, every run, including where that count is zero, because a
  zero is the evidence the check ran (SD-EXC-06).
- **The autofilter is the near-term view.** An earlier version of this file put a
  near-term BLOCK at the head of the worklist. A block above a table breaks element 1, so
  it is a column instead, and element 6 gives the reader the same view in one click and a
  better one, because they can combine it with any requirement column.
- **Membership and rank are untouched.** Urgency never adds a row and never removes one.
  Sorting the sheet by date would make the cap cut on the date axis and delete exactly the
  high-severity entities the sheet exists to surface, which is SD-RNK-07's named failure
  arriving through a convenience.
- **The `no_date_on_file` state is visible, not sorted quietly to the bottom.** A missing
  renewal date on a live entity is itself worth somebody's attention.
- **Where no commitment-date column resolves at all**, both columns ship, every row takes
  the `no_date_on_file` state and carries that key's bound label, and one line in Method
  says no commitment date resolved and names what column would supply it. Both headers are still written from their variables:
  an unresolved column is written blank with its header PRESENT, never dropped and never
  headed by a placeholder. The columns are not dropped: an unresolved column is
  written blank with its header present (SD-CTR-13).

### 5.6 Tabs 4 and 5, the reference tables

**Both are declared REFERENCE TABLES** per 5.1, and a reference table is not an entity
sheet only because its rows are requirements and codes rather than units of business. It is
a grid in every respect the formatting elements care about, so it takes every element that
binds a grid and records every one that cannot apply with its reason, per 5.8.

**R1 DOES RUN ON BOTH, in its POSITION form.** An earlier version of this step said R1 was
asserted of entity sheets and did not apply here. It does apply: the verification matrix
scopes R1 to ENTITY SHEET and REFERENCE TABLE alike, and the only difference is which
header variable the first column takes.

- **The position column is headed `HDR_POSITION`, whose documented default names it for
  what it is: a position.** Neither of these sheets is ordered by merit, so `HDR_RANK` is
  wrong here, and it carries a claim about severity that the order does not make.
- **`HDR_PRIORITY_BAND` IS NEVER USED AS A POSITION HEADER, on these sheets or anywhere
  else.** It heads a column of BAND LABELS, whose values are the members of
  `PRIORITY_BAND_LABELS`, and heading a column of integers with it makes every reader who
  has seen a band label elsewhere in the bundle read 1, 2, 3 as the three band names. That
  was measured on a real build: two reference sheets shipped with a first column headed
  with the band variable holding the integers 1 upward. The two variables name two
  different things and neither substitutes for the other.
- **The reason-for-rank column, `HDR_RANK_REASON`, is required on both**, because PART 4.1
  requires it on a non-merit order too, where it says why the row sits at that POSITION
  rather than why it scored where it did. On the Summary that sentence names the pass rate
  and the count that put the requirement at that position; on the Legend it names why the
  code sits in that family and in that order. A position column with no explanation is the
  thing a reader re-sorts by hand.

**Tab 4, Summary. IT HOLDS TWO KINDS OF ROW AND THE SHEET SAYS WHICH IS WHICH.** A
requirement row and a scope-unit rollup row are not the same kind of thing, they do not
share a meaningful ordering, and R1 requires ONE position column running down the sheet, so
the sheet cannot simply interleave them by rate and cannot leave a reader to guess. The
structure is fixed here so that two runs build the same sheet:

- **EACH ROW SAYS WHICH KIND IT IS, IN ITS `HDR_RANK_REASON` CELL, AS THAT CELL'S FIRST
  CLAUSE.** No new column is added for it: PART 4.1 requires the reason-for-rank column on
  a non-merit order precisely to say why the row sits at that POSITION, and on this sheet
  the first half of that answer is which block the row is in. A requirement row's reason
  opens by naming it a requirement row; a rollup row's opens by naming it a scope-unit
  rollup. The kind is carried by a column the contract already mandates rather than by a
  column this file would have to invent a header for. I1 records the schema request for a
  dedicated row-kind header, which would let a reader filter the two blocks apart in one
  click where free text does not.
- **The requirement rows come FIRST, as one block**, at positions 1 upward, ordered
  worst-first by conformance rate ascending, which is where a reader looks when one
  requirement fails across sixty entities.
- **The scope-unit rollup rows come SECOND, as one block**, resuming at the next position
  and ordered worst-first by conformance rate ascending within their own block.
- **The position column is ONE unbroken sequence down the sheet**, 1 to the last row, which
  is what R1 requires of it. It is a POSITION and not a rank: the sheet's order is not a
  merit order, the header is `HDR_POSITION` per the bullets above, and the reason-for-rank
  column on each row says which block the row is in and what put it at that position inside
  that block.
- **The ordering note in the note band states all of it in one sentence**, per 5.10: the two
  kinds, which block comes first, and that each block is ordered by conformance rate
  ascending.

**Why blocks and not interleaving, and why not a second sheet.** Interleaving by rate ranks
a requirement against a branch, which is a comparison neither number supports and which no
reader asked for. A second sheet would put the rollup a click away from the requirement
figures it must be read beside, and would add a seventh tab to a six-tab contract that
`TAB_CONTRACT` fixes. Two labelled blocks on one sheet keep both readings available, keep
the position column continuous, and add no column at all.

**WHERE THIS SHEET'S OWN HEADERS COME FROM, AND THE RULE IS reference/output-contract.md PART 8'S
AND IS SCOPED AS PART 8 SCOPES IT.** The prohibition is on writing a header string as a
literal **WHERE THAT FILE OR THE SCHEMA NAMES A VARIABLE FOR IT**. Every header this sheet
carries for which a variable exists reads that variable and is never typed: `HDR_POSITION`
and `HDR_RANK_REASON` above, and every other name the schema supplies. **Where NO variable
exists for a column this sheet is required to carry, the column is still built, its header
is defaulted in plain language, and the default is DISCLOSED**, which is the outcome PART 8
provides for and which SD-CTR-13 requires, because the alternative is to drop a column the
contract mandates and a dropped column is a fact the reader cannot recover.

**AN EARLIER REVISION OF THIS SECTION SAID FLATLY THAT NO HEADER ON THIS SHEET IS WRITTEN AS
A LITERAL, AND UNDER THAT SENTENCE THE SHEET COULD NOT BE BUILT AT ALL.** This sheet is
required below to carry about fifteen columns of its own, and the schema names a variable
for three of them. A literal reader of the deleted sentence had two moves and both are
forbidden: write the literals, which the sentence banned, or drop the columns, which this
section mandates and SD-CTR-13 forbids. The contract governed, the literals shipped, and the
two statements disagreed with nothing reconciling them. The scoped form above is PART 8's own
wording and it makes the buildable case the lawful one.

**THE DISCLOSURE, WHICH IS WHAT KEEPS A DEFAULTED HEADER FROM BECOMING A SILENT ONE.**
Method records, per sheet, the COUNT of headers written from a variable, the COUNT written as
a defaulted literal because no variable names them, and the defaulted headers ONE BY ONE with
the column each heads and the figure it carries. The front panel's binding disclosure per
Part F counts them, and the count is routed to `BINDING_OWNER_NAME` as a schema request
rather than left as a run-time choice: I1 carries it. **A defaulted header is a disclosed
gap in the schema and never a licence**, and the moment the variables exist this sheet reads
them and this paragraph's count goes to zero. Nothing here weakens the entity sheets' rule,
which is absolute for a different reason: every header those sheets carry HAS a variable, so
a literal there is always a second source of truth for something already bound.

Per requirement: eligible, assessed, pass, gap, unassessable, not required; the conformance
rate, the attributable conformance rate and the assessability rate, all three, per A4 and
under the labels 3.5.1 gives them where the period state is NOT YET STARTED, with the
difference between the first two printed as a number and the count and share of
non-attributable cells that produced it; the applicable entity count for every targeted
requirement; both counts from 4.4b for every requirement an influence finding scoped, with
the blocking parties named; the second number from A5 with its rung, its unit and its
strength; the mix numbers from A5.1 wherever a peer comparison ships.

**The second block carries the same figures rolled up per SCOPE UNIT**, and it ships where
the requester's scope contains more than one AND that level is not person-bearing under A9,
in which case the rollup goes to the nearest level above that is not, or to the scope total
alone with one line saying why. Where the scope contains one unit, the second block is
absent and the note band says so, which is the zero sentence and not an empty block
(SD-LNG-13).

Below `MIN_POPULATION_FOR_NORM`,
print the figure with its count beside it and draw no comparison (SD-POP-19). Benchmark one
level wider than the requester's own slice (SD-EXC-20), which is the direction SD-SPN-14
requires of a peer set: outward, never down into the requester's own span. Report a zero
count rather than omitting it, because a zero is the evidence the check ran (SD-EXC-06).

Precedence on this sheet is SD-CTR-24: a documented default applied to an unbound variable
may narrow what it attempts, and may never contradict, replace or silently supersede a
value the organization actually bound. Test that before applying any default here; where
the default would change a decision a bound value already decided, the bound value stands
and the notice names the narrowing rather than a substitution.

**Tab 5, Legend.** Every code in every family in plain English, with the action it implies
and who can clear it, including the codes whose action is explicitly none and whose clearer
is explicitly nobody. Then, per requirement: its evidence field, its provenance class and
which evidence rule governed it, its authorship tag, its eligibility rule, its applicable
count, and the two counts from 4.4b where an influence finding scoped it. Then the
standard's edition and date and every source document the requirement set came from, by
name and date; every requirement retired, paused or not yet effective, and why; and the
indicator caveat in 5.9 where it applies. For a multi-jurisdiction scope, name every
jurisdiction's standard that was read. A reader must be able to see which document drove
the scoring, and which cells are theirs to clear, without asking.

**THIS SHEET ALSO CARRIES THE THREE THINGS THE CONTRACT REQUIRES A CLASSIFICATION COLUMN TO
PUBLISH, AND ALL THREE ARE MANDATORY AND VERIFIED.** reference/output-contract.md 2.6 makes the
Legend the place a classification column's answers are readable, so a reader can see the
whole set of answers a column can give without opening the method sheet:

1. **THE STATE VOCABULARY.** Every member of `CLASSIFICATION_VOCABULARY`, with what each
   state means and how it is counted, per A1: which two are scored, which three are shown
   and excluded from every denominator, and that RETIRED never appears in a cell because A6
   does not build the column. **And the RESOLUTION RULE 4.6 declares, stated for the
   reader**: a cell resolves to the state its leading symbol and state code name, and
   everything after them is a reason code, a qualifier code or a finding.
2. **THE FILL PER STATE**, from `CLASSIFICATION_FILLS`, with the state each colour carries,
   the statement that no two states share a fill, the statement that every one of them was
   written with an EXPLICIT OPAQUE ALPHA per reference/output-contract.md 2.9 and read back as one at
   verification row C1, and the NAMES of any states carrying no fill and why, per 4.6. Then, in one line, the precedence 2.6 fixes: where a status cell
   also falls inside an alert band the alert fill governs and the classification fill is not
   applied, so a cell never carries two.
3. **THE PASS QUALIFIER CODES**, one row per key of `PASS_QUALIFIER_VOCABULARY`: the code,
   the key, that key's bound `label` in full, and what a reader should conclude from a pass
   carrying it. **This row is what makes A3's move of the qualifier out of the cell
   lossless**, per reference/output-contract.md 2.7's first rung, and a code shipped with no row here
   is the one way that rung can be done wrongly. The Legend also prints the count of passes
   carrying each code, so a reader can see how much of the pass rate was never dated.

**AND EVERY HOLE A3 REPORTS**, per requirement: the clause of a met-condition that could not
be tested, quoted in the standard's own words, with the evidence read in its place named and
the routing to `BINDING_OWNER_NAME` stated. It sits here as well as on the front panel
because it is a fact about the REQUIREMENT and this is the sheet a reader opens to ask what a
requirement means.

### 5.7 Tab 6, Method

Exhaustive by design and placed last, where it costs a hurried reader nothing and lets a
sceptical one reconstruct every cell (SD-CTR-15). A panel sheet, element 15.

**THIS SHEET DECLARES THE CELL RANGE ITS VERIFICATION MATRIX OCCUPIES, AND THAT
DECLARATION IS WHAT LETS A STRING-SEARCHING VERIFICATION RECORD ITS OWN EVIDENCE.**
reference/output-contract.md 7.1 states the mechanism once and this file supplies the one thing it
requires of a skill: the matrix sits in a declared, stated range on this sheet, every
STRING-SEARCHING verification excludes that range from its own scan and says in its own
record that it did so, and element 16, the character gate, still scans it like every other
cell, because a character outside the permitted set is a defect wherever it sits and a
character scan cannot be tripped by a record of itself (SD-FMT-27).

**WHY THE DECLARATION IS LOAD-BEARING AND NOT HOUSEKEEPING.** R5 scans the whole workbook
for a hard-coded unit noun, and 5.8 requires every matrix entry to state its reason, so
R5's own row has to say WHAT IT SEARCHED FOR or it has no stated reason and is recorded NOT
IMPLEMENTED, which fails. Written into an unexcluded matrix, those terms are then found by
the row that wrote them: it was measured, the raw occurrence count over the workbook went
from 22 to 44 the moment the row was written, and the gate turned a passing run into a
failing one. **A run that recorded its evidence failed while a run that hid its evidence
passed**, which is the exact inversion an audit trail exists to prevent, and the workbook
was not the thing at fault. With the range declared and excluded, R5's record holds what it
must hold: the terms searched, the count found, the result, and the fact that the exclusion
was applied. **No range is ever excluded from a verification in order to pass**; the only
permitted exclusion is a row's own record of its own search, and PART 8 forbids any other.

It carries: the probe record in full; the container, header row and runner-up chosen; every
header that did not resolve, by literal text; every column resolved by value check after
failing the name match; every column resolved and empty; every ambiguous resolution with
both candidates and the reason one won; every stem proposed for promotion
(reference/field-resolution.md 7.7); the manifest against the retrieved counts, per unit, and
against the written rows, as two separate reconciliations per A7; the terminal status of
every unit; **every capped sheet's showing note, agreeing with the note in that sheet's
note band per 5.10**; the full exception enumeration from 5.1; every retry and what it
resolved; the regression invariant results; **the sheet declarations from 5.1, one row per
sheet giving its CLASS and, where it is ranked, its KIND, with the extract naming which
sheet it extracts from and how many rows it takes**, which reference/output-contract.md 2.0 and
PART 4.2 both require to be recorded here; the verification matrix from
reference/output-contract.md PART 7.2 with a row per sheet per element, every NOT APPLICABLE
carrying one of the five reasons in 5.8, and the counts of the three formatting states per
sheet; **the DECLARED CELL RANGE that matrix occupies, stated on this sheet, per 7.1**;
**the frozen-span record from PART 4.1.2, which is ONE LINE FOR THE ARTIFACT and never one
line per sheet**, naming the bound, the summed WIDEST-CASE built width of the span, which
sheet supplied the widest case for each identity column walked, and any identity column left
outside the span by header name; **the grid-width record from PART 2.7, per grid**, naming
the value of `GRID_MAX_TOTAL_WIDTH` that was read BEFORE the columns were built, the measured
summed built width of that sheet, and, where the measurement is over the bound, the overage
and the columns that account for it in DESCENDING order of built width, together with the
statement that the relief ladder was run and that no column was dropped, no column was
narrowed below its own header floor and no value carrying meaning was shortened; **which
columns were declared CLASSIFICATION COLUMNS under PART 2.6**, with the vocabulary each was
declared against, the resolution rule from cell to state, the count of populated cells the
rule placed and the count it could not, and the fill each state carries or the statement that
it carries none; **which columns, if any, were ALSO declared STATUS GRID COLUMNS under PART
2.5, with the closed vocabulary each was declared against and the longest member's character
count against `CENTRE_ALIGN_MAX_CHARS`**, so a reader can check the CENTRING against the same
three conditions the verification does, **and the statement that the centring test decided
alignment only and was read by nothing else**; **the header record per sheet from 5.6**, the
count read from a variable, the count defaulted because no variable names them, and each
defaulted header with the column it heads; **the provenance decision per requirement, naming
which step of B1.1 decided it and
what it read, and the two counts from B1.2 whether or not the tripwire fired**; **the three
numbers reconciling the not-workable exclusion against the standard's own entity-class scope,
per 4.1 step 1, with the disagreeing entities named**; the
spot-check comparison; and one worked cell taken end to end so a reader can reproduce it by
hand (SD-CTR-21).

### 5.8 The three-state formatting record

**The pass matrix has THREE states, not two, because an element that never occurs and an
element nobody implemented are indistinguishable in a two-state record and the second is a
defect hiding inside a pass.**

| State | Meaning | Is it a pass |
|---|---|---|
| PASS | The element applies to this sheet, was applied, and was read back and verified | Yes |
| NOT APPLICABLE | The element CANNOT apply to this sheet, **and the record names why** | Yes (SD-EFF-37) |
| NOT IMPLEMENTED | The element applies and was not attempted, or was attempted and could not be verified | **No** |

**A NOT APPLICABLE entry with no stated reason is recorded NOT IMPLEMENTED instead.** That
is the whole mechanism, and it works because it makes the failing state the default for an
unexplained entry, which is what G2 and SD-EFF-03 require of anything that cannot be
evaluated.

**AND A PASS IS ONLY EVER A PASS IN THE RENDERER THAT READ IT BACK, WHICH IS WHY EVERY BAND
IS SCORED AGAINST ITS DEGRADED RENDERINGS AND NOT ONLY AGAINST THE ONE IT WAS BUILT IN.**
SD-FMT-29. Every text-and-band pair on every sheet of this workbook goes through all three of
reference/output-contract.md 2.8's assertions, the intended pairing and the two renderings in which
one half of the formatting fails to arrive, and every colour the build writes anywhere
carries an explicit OPAQUE alpha per 2.9, read back at verification row C1. A pair that
clears the intended assertion and fails either degraded one is recorded NOT IMPLEMENTED and
blocks publication however good it looks here. **A THREE-STATE RECORD DOES NOT PROTECT
AGAINST THIS ON ITS OWN**: the failure it answers passed a two-state and a three-state record
alike, because the check and the defect were both inside the one engine. The arithmetic, the
floors and the colour values live in 2.8, 2.9 and reference/schema/; this file states none
of them.

**The reason is drawn from the closed set below.** It has FIVE members, and the fifth is
what makes the set TOTAL over the elements and verification rows the contract can emit,
rather than total over the ones somebody happened to think of:

1. **THE SHEET HAS NO ROWS** to which the element could apply.
2. **THE CONTAINER CANNOT EXPRESS IT**, as a row-height rule cannot exist in a markdown
   rendering.
3. **THE ELEMENT OR THE VERIFICATION ROW IS SCOPED, BY THE CONTRACT ITSELF, TO A SHEET
   CLASS, A SHEET KIND OR A SHEET PROPERTY THIS SHEET DOES NOT HAVE, and the scope is
   named.** Elements 1 to 6 and 8 to 14 bind a grid and not a panel; **ELEMENT 7 IS THE ONE
   EXCEPTION AND BINDS BOTH**, because its scope is every populated cell of the SHEET'S USED
   RANGE and a panel row is a populated cell, so element 7 is never recorded NOT APPLICABLE
   on a panel under this member and a record that does so is NOT IMPLEMENTED; element 15
   binds a panel and not a grid; R2 binds a merit tier set and this workbook emits a census
   and an extract; R3
   binds a capped sheet; R4 reads one form on a merit tier set and another on a census.
   Each of those is this member, and each names the scope it failed rather than saying
   "different family", which was too narrow a word for what the contract actually scopes by.
4. **THE INPUT THE ELEMENT READS IS NOT PRESENT ON THIS SHEET, NAMED.** Element 13 reads an
   elapsed-time column and a sheet may have none; element 11 reads a trailing narrative
   column and a reference table may carry none. Without this member a correct workbook
   failed at the final gate: the earlier set offered "no rows", which was false, "container
   cannot express it", which was false, and "different sheet family", which was false, so
   the honest not-applicable had no qualifying reason, became NOT IMPLEMENTED, and blocked
   publication of a workbook with nothing wrong with it.
5. **THE ELEMENT'S OWN TEXT NAMES THE CONDITION UNDER WHICH IT DOES NOT APPLY, AND THAT
   CONDITION HOLDS.** Quote the element's own words as the reason. reference/output-contract.md
   PART 2 states this directly and states it as always qualifying: a closed list kept
   anywhere else that cannot express an element's own stated exemption is an INCOMPLETE
   LIST, and the workbook it rejects is not the thing at fault. **This member is why the
   set stays total when the contract changes**: an element added later whose exemption fits
   none of members 1 to 4 is covered by member 5 the moment its own text states the
   exemption.

Anything outside those five is not a reason and does not qualify. **Validate the set in the
direction SD-CTR-29 requires, from the ELEMENTS to the LIST and never the other way**, and
re-run that validation whenever the contract changes: for every element and every
verification row the contract can emit, is there at least one member of this set that can
express the way it fails to apply. A member with nothing to express is harmless; an element
with no expressible reason is a correct workbook that cannot publish.

Publish the counts of all three states per sheet in Method. A sheet reporting many
not-applicable entries is either genuinely simple or quietly unbuilt, and only the counts
beside their reasons let a reader tell which.

Where the elements cannot be read back at all, the element gate cannot run and an element
gate that cannot run has failed (reference/output-contract.md PART 7.1). The resolution is the shared gate
`formatting_unverifiable` in Part G, conditional on `DELIVERABLE_CONTAINER_REQUIRED`: true
stops the run outright rather than publishing an unverified container; false, its documented
default, resolves the gate NOT APPLICABLE with its reason and falls back to structured
markdown carrying identical information per E2. Never publish silently either way.

Filename from `OUTPUT_FILENAME_PATTERN` with the scorecard entry in `DELIVERABLE_NAME`,
carrying the scope label, its code, the period and any qualifier so two runs never collide.
Write to `OUTPUT_DIR`. Use `UNIT_NOUN_SINGULAR` and `UNIT_NOUN_PLURAL` wherever a unit noun
appears, and hard-code none (reference/output-contract.md PART 6).

### 5.9 The indicator caveat

Where the evidence source is not the system of record for the official score, print that
on the Summary: this view is an indicator and will not match the official result exactly;
use it for themes, trends and prioritization, not to dispute an official score. Do not
build a second version of something that already has a system of record (SD-EXC-24).

### 5.10 The note band, which is where every per-sheet note goes

**A note that belongs to a grid has ONE permitted location and reference/output-contract.md
PART 5.3 defines it exactly.** SD-FMT-26 is the doctrine. This file routes its notes there
by citation and states no placement of its own, because the placement question is exactly
the one that produced four different answers on four builds.

**AND THE BAND IS BORDERED LIKE EVERY OTHER POPULATED CELL ON THE SHEET.** Each note row
carries ELEMENT 7's BORDER ON ALL FOUR OUTER EDGES OF ITS MERGED REGION, per PART 5.3 and
PART 7.2 row 7, because element 7's scope is the SHEET'S USED RANGE and never the table
range, and **SITTING OUTSIDE THE TABLE RANGE EXEMPTS THE BAND FROM NOTHING IN IT.** This is
the one property of the band worth naming here, because it is the one a reading scoped to
the table block silently drops: a band that is populated, merged across the sheet width and
unbordered on every side sits directly under a table bordered on all four sides of every
cell, and a border walk that stops at the table range certifies it as a pass. SD-FMT-02,
SD-FMT-29.

**AND THE BAND IS MERGED ACROSS THE TABLE'S FULL COLUMN SPAN, NOT MERELY STYLED ACROSS
IT.** PART 2.10 and SD-FMT-30. The two look identical until element 7 draws its border,
and only then does the difference show: a styled span leaves the note text in the first
cell, overflowing into the cells beside it, so the border this file just required on the
second cell is drawn straight through whatever word is crossing it. **THAT IS THE SAME
DEFECT THIS PARAGRAPH ALREADY DESCRIBES, ONE STEP EARLIER**, and it binds every other
band this skill writes as well: the front panel's and Method's title rows, every panel
section header band, the explanatory row of an empty sheet and any banner. A string that
needs more width than its own cell goes in a MERGED region spanning exactly what it
needs, and no string is ever permitted to overflow a cell boundary.

**Why it has to be stated at all.** Three elements between them forbid every obvious
placement while a fourth makes the note mandatory and verified. Above the header row breaks
element 1 and everything that depends on row 1 being the header row. Inside the table range
breaks element 3 and, worse, puts a row that is not a unit into something that sorts,
filters and counts as though it were. Below the table in the FIRST column collides with
element 9, which right-aligns the position column, and that collision was measured on a
real build as exactly one violation on exactly one cell, found only because the audit
checked alignment over every populated cell rather than sampling. Below the table in the
TRAILING narrative column breaks nothing and is invisible, twenty columns right of where a
reader is looking. The note band is the fifth placement and it is the one that survives all
four objections, and elements 1, 3 and 9 now say so in their own text, so a reader of any
one of them learns the note band is permitted without coming here.

**What this skill routes into the note band, per sheet, in this order where a sheet carries
more than one:**

| Sheet | Notes in its band |
|---|---|
| Tab 2, the extract | Its declaration of which sheet it is an extract of and how many rows it takes, per 5.3; then its showing note, with `n` its own unit rows and `N` the census's unit row count per PART 5.1.1; then its shortfall note where it holds fewer rows than its declared size allows |
| Tab 3, the census | Its showing note, in the exact wording reference/output-contract.md PART 5.2 gives |
| Tab 4 and tab 5, the reference tables | Their ordering note, saying what the sheet is sorted by, since neither order is a merit order; then their showing notes, which ship on both, every run |

**EVERY SHEET IN THAT TABLE IS BOUNDED AND EVERY ONE OF THEM SHIPS A SHOWING NOTE, WHATEVER
ITS COUNTS.** reference/output-contract.md 5.1.1 names the THREE bounds a sheet's row count can
have, `REFERENCE_CAP`, a merit tier's size and an extract's declared size, and gives `n` and
`N` for each; 5.2 says the note ships where nothing was cut, with `n` equal to `N`, because
the note is the evidence the bound was EVALUATED exactly as a zero count is the evidence a
check ran. **"CAPPED" MEANS SUBJECT TO A CAP AND NEVER CUT BY ONE.** An earlier revision of
this table said the showing note went on "either sheet that was capped", which reads as
conditional on an actual cut; under that reading a Summary of thirteen rows and a Legend of
fifty-nine, both far under the cap, shipped no note at all, and R3 then had nothing to
reconcile on either sheet. The two readings shipped different workbooks off one
configuration, which is the whole failure a single stated form exists to prevent.

**WHAT `n` AND `N` COUNT ON A SHEET WHOSE ROWS ARE NOT UNITS OF BUSINESS, BECAUSE TWO OF
THESE FOUR SHEETS ARE REFERENCE TABLES.** reference/output-contract.md 5.2 states the counting rule
as UNIT ROWS, which is the right words for the two entity sheets and is written in the case
those sheets are in. A REFERENCE TABLE is defined by that same file as a grid whose rows are
NOT units of business, so a literal reading of the words gives `n` equal to zero and `N`
equal to zero on the Summary and on the Legend, and R3 then reconciles zero against zero and
passes on two sheets that visibly hold rows. **This skill counts THE SHEET'S OWN DATA ROWS on
a reference table: requirement rows and rollup rows on the Summary, code rows and reference
rows on the Legend**, which is what the bound would actually have cut and is what the
contract's own worked regression case expects, a Summary and a Legend both far under the cap
shipping `showing n of N` with `n` equal to `N`. On the two entity sheets the two readings
are the same number, because there every data row IS a unit row.

**AND THE EMPTY-SHEET TEST NOW READS THE SAME COLUMN ON BOTH CLASSES, BECAUSE 5.4 SAYS SO
IN ITS OWN WORDS.** 5.4's mechanical test tells an explanatory row from a data row by its
blank value in the sheet's FIRST IDENTITY COLUMN, which is the POSITION column R1 puts in
first position on every grid of either class, and it reads that column rather than an
IDENTIFIER column precisely because a REFERENCE TABLE carries no unit identifier to read.
An earlier wording of 5.4 named the identity block's IDENTIFIER column and therefore gave
the Summary and the Legend no test at all; that wording is gone and this paragraph no longer
has a local reading to supply. The two conditions 5.4 requires to hold together, a blank
there and being the only data row on the sheet, hold together on all four sheets in exactly
the same way.

**AND THE ROW CARRIES ITS SENTENCE, WHICH IS THE HALF A BORDERED EMPTY BOX PASSES WITHOUT.**
Per 5.4 and PART 7.2 row C2, the sentence saying why the sheet qualified nothing begins in
the TABLE'S SECOND COLUMN, the first column after the position column, with the position
column left empty so the counter's test above still reads it. A row that exists, is
bordered, is sized to a computed height and holds no string at all is a FAILURE and blocks
publication, and so is a sentence placed further right than the second column behind a run
of empty cells. This file states no placement of its own for it and cites 5.4 for all of it.

**WHAT REMAINS A DISAGREEMENT WITH THE SHARED FILE'S WORDING IS THE COUNTING READING ALONE,
AND IT IS REPORTED AS ONE RATHER THAN RESOLVED HERE.** The empty-sheet test above is no
longer one of them: 5.4 now states the first-identity-column test itself. The contract
governs and this file is stale wherever the two still differ; what is written above is the
reading that builds the sheet the contract's own regression case describes, and the wording
is raised as a shared-layer item rather than fixed locally.
**Whichever reading a future contract fixes, the three-way reconciliation is unchanged**:
the built count, the sheet's own note and Method's note are computed from ONE number, so
they agree by construction and R3 has something real to read on every one of these four
sheets.

**Every one of those is repeated in Method per 5.7 and reconciled against the sheet**, and
R3 verifies the built row count, the sheet's own note and the method note against each
other. A disagreement blocks publication.

**The note band is not a substitute for the front panel or for Method.** The report title,
the scope, the period and every caveat still live on the front panel per element 1 and 5.2.
What the band carries is the note that has to sit BESIDE THE GRID IT IS ABOUT, which is
where a reader's eye lands at the moment the count of rows they just read becomes a
question.

## Step 6. Reply

At most `CHAT_REPLY_MAX_LINES`, and never paste the list (SD-CTR-16). Six things:

1. Scope, period, and the edition of the standard scored against.
2. **Completeness, explicitly.** "214 of 214 entities across 1 unit", or "1,612 of 1,650
   across 11 units; unit 7 partial, 98 of 136." A person who walked away needs to know in
   one line whether the report is whole. Never imply a completeness you did not verify in
   3b.8.
3. **All three rates from A4**, under 3.5.1's labels where the period state requires them,
   with the difference between the first two as a number, and with the second number from A5.
   **Two of the three is not a permitted reply.** A4 says twice that neither the conformance
   rate nor the attributable rate ships alone, and H1 forbids a compliance figure that is not
   accompanied by both others; an earlier revision of this item named exactly two, so a run
   following it literally published in the reply the one thing Part A says must never happen.
   The reply is the place it matters most, because it is what a reader quotes.
4. The two or three requirements carrying the most gaps.
5. How many entities could not be assessed, and the leading reason.
6. The filename.

Where the run degraded, the first line names the count of degradations and the single most
consequential effect, per reference/capability-probe.md 4.1.

---

# PART D: POPULATION SHAPE

## D0. Shape is a property of the POPULATION, not of the company

FIXED and FLOW are not a fact about an organization. They are a fact about the population
a given run is scoring, and many real businesses are genuinely both: a stable roster of
sites with work orders flowing across them, a stable roster of advisers with cases flowing
across them, a stable roster of machines with maintenance events flowing across them.
Forcing one answer for a whole company is itself the error (SD-POP-23).

`POPULATION_SHAPE` is a KEYED SET of declared populations, each carrying its own key, its
own mode, its own unit noun and its own fields. Every run resolves WHICH declared
population it is scoring, from the request and from the source in hand, and then reads
that population's shape. A business may declare one; it may declare three. Where only one
is declared it is the default for every run and nothing else changes.

This skill therefore never asks whether the company is FIXED or FLOW. It asks which
population it is scoring and what shape THAT population has, and it names the population
it scored on the front panel of every artifact.

**Two skills scoring different populations of the same business will report different
counts, and neither is broken.** A planning run counts every OPEN unit as of the run
moment, because a plan is a plan for work that is still open. This skill counts stage
arrivals in the window under FLOW, or the roster as of the census date under FIXED. The
two counts are not expected to agree. Each artifact names the population it scored and
says so, so a reader holding both on the same morning does not conclude that one of them
is faulty.

## D0.1 Detecting the shape: three tests, and the third one decides

Per SD-POP-24, in order, and never on the strength of the first two alone:

1. **The roster test.** Can a complete list of all of them be produced as of a given
   date, without reference to what stage each is in? A confident yes is evidence of a
   roster.
2. **The entry and exit test.** Does each one have a date it entered and a date it stops
   being the organization's problem? Yes to both is evidence of a pipeline.
3. **The replacement test, which decides.** When one of them leaves, does it leave a HOLE
   somebody notices and moves to fill, or does the next one simply take its place in a
   QUEUE? A hole means the unit is a standing position in the business: the population is
   a FIXED roster whose members happen to be dated, and the dates are unit attributes
   rather than a pipeline. A queue means FLOW.

Tests one and two both passing is the COMMON case, not the ambiguous one. A roster of
dated standing positions passes both; so does a pipeline held inside a stable set of
containers. The third test separates them and is not optional. A site estate whose members
carry an opening date and an agreement end date passes tests one and two and is
unambiguously a roster, because a site that closes leaves a hole somebody moves to fill.

Where the roster test passes over CONTAINERS and the entry-exit test passes over the
things moving across them, that is not a conflict. It is two populations. Both are
declared, and each run names which one it scored.

Where the third test is also ambiguous, take FLOW and record in the config that the shape
was taken on the tie-break rather than answered, so the binding owner can see it and
correct it. A tie-break that leaves no trace is a guess.

## D0.2 What the shape changes, and what it does not

The shape changes what "the population" means and therefore what the denominator is. It
changes nothing else: the same sections, the same five states, the same reason codes, the
same rates, the same gates (SD-POP-21).

## D1. FIXED: an enumerable set of standing entities

The population is a roster taken as of `POPULATION_SHAPE.census_basis`. Sites, accounts,
vehicles, machines, routes, facilities, licence holders, servers, contracts.

- The manifest is the roster count per scope unit.
- A requirement attaches to the entity. One row per entity, one cell per requirement.
- Evidence recency is measured against the operating window: evidence older than the
  window opening is `? UNASS: evidence predates this period`. Where the standard states no
  window, fall back to the larger of `RECENCY_FLOOR_DAYS` and `RECENCY_MEDIAN_FACTOR`
  times the local median capture interval (SD-EXC-02), and say which rule was used.
- A period-over-period comparison is like for like only within
  `FIXED_ROSTER_CHURN_TOLERANCE`. Beyond it, label the comparison not like for like rather
  than suppressing it, and name the entities present in one period only rather than
  dropping them silently (SD-CMP-02).
- **Test the EXIT side separately, because a survivor-only prior file scores perfectly**
  (SD-CMP-09). Overlap tests the entry side only: it asks whether the entities in the prior
  file are still here and it cannot see the ones that left, because they are absent from
  both sides of the test. Before computing anything on a pair, count the entities present
  in the PRIOR file and absent from the current one. Where that count is zero, the run is in
  one of two states and they are not the same: a survivor-only extract, which is the current
  roster valued at an earlier date rather than the roster as it stood then, or a population
  that genuinely lost nothing, which is real and rare above a small population. Decide
  between them on the evidence, say which and why, and do it before any figure is computed.
  From a survivor-only pair: retention and churn are NOT COMPUTABLE, not zero and not one
  hundred percent; a same-entity conformance movement is computable, survivor-biased, and
  published only beside the movement across the whole current population with the gap
  between them named as the part that left; and no ranking of entities by that movement is
  published at all, because the bias is not uniform across entities.
- An entity with no history is ranked last on the worklist, never dropped (SD-POP-12).

## D2. FLOW: items moving through stages, where the requirement attaches to a stage

The population is items in motion. Claims, cases, tickets, orders, files, encounters,
shipments, applications, work orders, candidates, releases.

The requirement is not "this entity carries this element" but "this item satisfied this
requirement at this stage". Six things change:

1. **The scoring population is stage arrivals in the window, not the open set.** Every
   item that reached the stage the requirement attaches to, during the period being
   scored, whether or not it is still open. Grouping by
   `FLOW_COHORT_BASIS` decides which window an item belongs to. Scoring only the currently
   open set makes a fast period look good, because the easy items have already left, which
   is the same distortion SD-CMP-01 and Q-D4 warn about.
2. **The manifest counts expected stage arrivals**, from the stage history or the stage
   timestamps, not the open count.
3. **An item that has not reached the stage is `N/R: has not reached this stage`.** It is
   not a gap, and it is not unassessable. It is not yet due.
4. **An item that passed the stage before the requirement took effect is `N/R: effective
   from <period>`**, per 4.1 step 3, evaluated against the item's own stage date rather
   than against the run date.
5. **An item whose stage history is missing or ambiguous is `? UNASS: stage history
   incomplete`.** Never infer that an item passed a stage from the fact that it reached a
   later one, unless the process makes that structurally impossible to skip and the
   standard says so. That inference is Part B's INFERENCE class and it produces a lead,
   not a verdict.
6. **Reopens.** Where `POPULATION_SHAPE.reopen_allowed` is true, an item can pass a stage
   more than once. Score each pass, report the count of items with multiple passes, and
   say in the Legend which pass the headline figure uses. Silently keeping the last pass
   hides a rework problem; silently keeping the first hides a fix.

Exclusion by stage is an exclusion, not a filter: items removed because they are closed,
withdrawn or outside the open set are reported with their counts in the funnel exactly as
any other exclusion is (SD-POP-22). They are never silently absent.

The open-set rule is `FLOW_OPEN_DEFINITION`. Where it is unbound and no exit field
resolves, every item is treated as open and the report says so, which overstates the
workload rather than hiding it.

Worked example. A lending operation moves files through intake, verification, decision and
completion. The standard requires that a signed income document is on file when a file
leaves verification. The scored population is every file that left verification during the
period. A file still at intake is `N/R: has not reached this stage`. A file that left
verification last period is out of this period's population entirely and is counted in the
funnel as such. A file that left verification with the document field blank and a
verification record present is a `GAP`. A file that left verification with no verification
record at all is `? UNASS: stage history incomplete`, and it is the yellow that most needs
chasing, because it is where a real gap most often hides.

## D3. The shape is read, never guessed, and a provisional run says which

On a bound run the shape of the declared population being scored is READ. It is never
inferred at scoring time.

On a PROVISIONAL run, where nothing is bound, the shape is inferred from the columns
present at MEDIUM confidence, and three things follow, all mandatory. The inference and
its evidence are printed on the front panel and in the audit. The three tests in D0.1 are
applied to whatever the requester can answer, and where only the column evidence is
available the replacement test cannot be run and that is said. And every sub-key of the
population that could not be inferred is treated as unbound, so `reopen_allowed` in
particular, which cannot be inferred from columns at all, stays unbound and D2 item 6
takes its unresolved path rather than merging on a guess.

Where the tie-break in D0.1 decides, FLOW is taken. A flow model over a roster degrades to
a single open cohort with a null exit date, which is recoverable. A fixed model over a
pipeline mixes closed and open items into one denominator, which the reader cannot recover
from the output. That is SD-STR-10 applied to the population shape: prefer the error a
reader can detect.

---

# PART E: DEGRADED RUNS

Assume no tooling. The probe in Step 0 decides what is available; reference/capability-probe.md
Part 2 decides what to do with each gap. This part says only what is specific to a
scorecard, and nothing here overrides that file.

## E1. The deliverable ladder

| Rung | Environment | What ships |
|---|---|---|
| 1 | Spreadsheet write and inspect both present | The colour-coded workbook: every section in `TAB_CONTRACT`, the identity block, the fills, the filter, the caps, the verified formatting matrix |
| 2 | Write present, structure or inspection degraded | Every section with correct data, columns, headers, ranks, counts and caps. Every formatting element that could not be applied or read is recorded as not applied or not verified, by name, not as failed |
| 3 | No spreadsheet capability, or formatting unverifiable with `DELIVERABLE_CONTAINER_REQUIRED` false | **Structured markdown carrying identical information.** Not a summary |
| 4 | Markdown cannot be written to a file | The same structured markdown inline in the reply, with the caps still applied, saying plainly it could not be written to a file |
| 5 | Nothing can be emitted | Report the failure, name every path attempted, preserve the checkpoint |

Rung 3 is where formatting-unverifiable resolves when the organization has not required a
specific container, which is the documented default. Where
`DELIVERABLE_CONTAINER_REQUIRED` is true instead, the shared gate
`formatting_unverifiable` in Part G stops the run rather than substituting a container the
organization said it will not accept. That choice is a binding, not a judgment, and it is
now bound rather than described.

## E2. What "identical information" means at rung 3

The markdown fallback carries, without exception:

- Every section in `TAB_CONTRACT`, in the same order, under the same title strings,
  including any section with nothing to report and its `MSG_EMPTY_SECTION` row.
- Every column in the same order with byte-identical headers.
- **Every cell's state, symbol, code and reason as text.** This is why A3 requires the code
  in the cell: the classification survives the loss of colour completely, because the
  colour was never carrying it.
- **The `HDR_RANK` column, the `HDR_RANK_REASON` column, the `HDR_FAILS` count and the
  narrative string**, in the same column order as 5.3, each under the header its variable
  is bound to. These are content rather than formatting and none of them is a spreadsheet
  feature, so none of them relaxes. What is lost at this rung is the autofilter, and that
  loss is named: say in the front panel that the reader cannot isolate rows in one click
  and that the narrative column carries the same information row by row.
- Both rates, both denominators and every count from A4.
- Every reason code and the Legend that explains each one.
- The manifest reconciliation, the funnel, the audit and every degradation line.
- Identifiers and codes rendered so leading zeros survive, with the convention named in
  the front panel.
- A wide requirement set split into two pipe tables joined on the identifier, in the same
  column order, saying so. Never drop a column (SD-CTR-13).
- Row-height and fill elements recorded as not applicable rather than failed (SD-FMT-01).

Presentation changes. The sections, their order, the columns, the headers, the five
states, the reason codes, the counts, the rates, the disclosures and the audit do not.

## E3. Scorecard-specific degradations

- **No computation available.** Do not estimate a rate, do not rank by impression, do not
  eyeball a pass count. Emit the population, the resolved requirement set, the evidence
  mapping and the qualitative sections, and state plainly that no rates could be computed
  (reference/capability-probe.md 2.5 rung 3, SD-SCL-03, SD-CNF-07).
- **The standard could not be read.** Step 2.9. Banner the run as standard unconfirmed,
  name the list used, and never present it as authoritative.
- **The evidence source is reachable but stale, partial or narrower than the request.**
  Use it, date it honestly, and say on the front panel and in the reply that the scorecard
  was built on evidence of that age or that coverage. Never present it as current. A
  record count of zero is `shared.record_count_zero` (SD-PRS-24).
- **No jurisdiction reference.** No permission check runs. Say that if a requirement in
  this report cannot lawfully or contractually be met somewhere, this report does not know
  it.
- **No prior period for the population.** Not a degradation and not an error: it is a cold
  population, detected per A8, and the run says so, drops the movement labels, re-evaluates
  the rungs for that population, and reports absolute build, sequencing against plan and
  execution against a denominator. A cold run that emits nothing has failed; a cold run
  that emits a WIN label has failed worse.
- **No lawful fill for a cell state.** Where the `fill_variable` a state names is unbound,
  or would resolve to either alert colour, that state carries NO FILL, the Legend names
  which states carry one and which do not, and the classification is unaffected because A3
  puts the code, the symbol and the reason in the cell as characters. It is a stated
  outcome under reference/output-contract.md 2.6 condition 2 and never a build failure, and it is
  never resolved by giving two states one colour.
- **No interactive channel.** No deferred binding is requested and no clarifying question
  is asked. Apply every documented default, print every notice, take the bannered path for
  anything blocking, and list every question that would have been asked and what each
  would have resolved (reference/capability-probe.md 2.14 rung 2). Silence is never confirmation
  (SD-CNF-04).

## E4. Announce it, three places, every run

Front panel, audit section, and the first line of the reply (reference/capability-probe.md 4.1).
Each line names what was unavailable, what it changed, and what the reader should do. Never
only the first. Two capabilities missing never compound into one line saying some things
were unavailable (P7). A degradation announced last run and still present is announced
again at the same prominence; it is never quietly downgraded because it has appeared
before.

The self-check before publication: could a reader opening this artifact six months from
now, with no memory of the conversation, tell from the artifact alone which parts were
produced with less than the full method and what that cost them? If not, the announcement
is not finished.

---

# PART F: BINDINGS REQUESTED AT THE POINT OF NEED

TEN organization variables are bound at ignition. Everything else this skill uses is
DEFERRED and is requested only when a decision needs it, once, and only from somebody who
would know. `BINDING_OWNER_CONTACT` was the eleventh and is now DEFERRED: it is the one
ignition candidate no policy document can supply, and leaving it in the set stamped every
faithfully documents-bound run PROVISIONAL on a binding no amount of care could clear.
Where it is unbound the run is not provisional on that account, binding authority is
unaffected, and the artifact carries that variable's own standing disclosure instead. The rules are in reference/binding-interview.md Parts 2 and 5 and are not restated
here. Four of them govern every request below:

- **The right answerer only.** A person-tier user is never asked an organization question,
  in any phrasing, including as a confirmation. Where the person in front of the run is not
  the answerer, apply the documented default, print the notice, and queue the request to
  `BINDING_OWNER_NAME`.
- **At most two requests per run, and never more than one before the first output.**
- **Highest-cost gap first**, measured by how far the default moves a published number.
- **Once, then never.** A bound or declined variable does not fire again.

When a request does fire, it says four things in order before asking: the decision it is
facing, why the value is needed for that decision, what it will do if the answerer
declines quoting the documented default and its degradation notice in plain words, and
then the question.

| Decision this skill is facing | Binding | Catalogue entry | If declined |
|---|---|---|---|
| Which entities cannot be worked right now, so they are excluded before anything else | `UNIT_ACTIONABLE_NOW_CONCEPT`, `UNIT_ACTIONABLE_NOW_VALUES` | Q-D6 | No exclusion; the report says some entities may be closed, suspended or on hold |
| Which declared population this run is scoring, and what shape it has | `POPULATION_SHAPE` as a keyed set | Turn 4, then Q-D3 | The single declared population is used; where none is declared the shape is inferred at MEDIUM confidence and D3 governs |
| At what level one entity sits, so a coarse-unit binding error is caught | `UNIT_LEVEL_KEY` | Q-D7 adjacent, at first scope resolution | Detected from the data by the distinct-value test in 1.6, and the detection is named |
| Below what population nothing may be ranked | `MIN_POPULATION_FOR_RANKING` | Q-N1 adjacent, at first sizing | The standing minimum, never below `MIN_POPULATION_FOR_NORM`; the suppression is stated before the content |
| Whether the peer set is internal siblings or a published outside group | `PEER_SET_IS_EXTERNAL`, `EXTERNAL_PEER_SET_SOURCE` | Q-E6, at the first peer comparison | An internal sibling set is assumed and the group used is named; where an external group was declared without a publication, the peer rung is dropped and the drop is named |
| When a population counts as having history | `COLD_START_MIN_PRIOR_SHARE` | Q-E5 adjacent, at the first movement label | The standing share; the report states which cold test fired and the figure that fired it |
| How much of a denominator the reader's own result may occupy before it is self-built | `ADDRESSABLE_SELF_SHARE_CEILING` | Q-E6, at the first share figure | The standing ceiling; where it fires, the share rung is struck and the figure named |
| Whether an unverifiable container is published labelled or replaced by markdown | `DELIVERABLE_CONTAINER_REQUIRED` | Q-FORMAT-REMAINDER | False: structured markdown carrying identical information, and nothing is dropped |
| What the cell states are called and how they are filled | `CLASSIFICATION_LABELS`, `COLOR_STATUS_PASS`, `COLOR_STATUS_NOT_SCORED` | Q-EXCEPTION-REMAINDER | The five standing states with their standing symbols and fills; every cell carries its state as text so the grid reads with no colour at all |
| What the reason vocabulary is | `REASON_CODE_SET` | Q-EXCEPTION-REMAINDER | The seeded set in 4.2; a reason fitting no code is marked unmapped and named rather than written as free text |
| Where the standard lives and which artifact settles what | `SOURCE_AUTHORITY_MAP`, `PRIORITY_SOURCES` | Q-J1 | Only the nearest source is read; the report says nothing reflects an organization-wide standard |
| Whether a periodic release publishes this period's requirements and pauses | `CENTRAL_BRIEF_NAME`, `CENTRAL_BRIEF_TABLE_COLUMNS` | Q-J2 | No release is read and the report says so; a missing central source is never a stop |
| Where reference documents live, and whether folder names may be hard-coded | `DOC_STORE_NAME`, `DOC_STORE_SITE_VARIABLE`, `DOC_STORE_LIBRARY_VARIABLE` | Q-P1 | Discovery runs against whatever container resolves; a failure to find a reference is reported by name. The answer to the hard-coding half is always no |
| Whether a requirement may be forbidden somewhere | `COMPLIANCE_CHECK_ENABLED`, `JURISDICTION_CONCEPT` | Q-M1 | No permission check runs, and the report says it does not know |
| Where the per-jurisdiction rules are written | `COMPLIANCE_GUIDE_SET`, `COMPLIANCE_GUIDE_MASTER`, `COMPLIANCE_GUIDE_SUPPLEMENTS` | Q-M2 | The check cannot run; every requirement it would have validated is held back and named, never silently permitted |
| A place name in a request did not match the stored codes | `JURISDICTION_NAME_TO_CODE`, `SUBREGION_SUFFIXES` | Q-M3 | Place names resolve only on exact match; a miss returns the nearest values present |
| Whether an unreachable rules reference holds back the requirements or the report | `COMPLIANCE_FAILS_CLOSED_ON` | Q-M4 | The requirements are held back and named. That is the only permitted setting |
| Which stages exist and what makes an item open, under FLOW | `POPULATION_SHAPE.stages`, `FLOW_OPEN_DEFINITION` | Q-D3 | Open is a blank exit date; with no exit column, every item is open and the report says so |
| How two periods of a flowing population are grouped | `FLOW_COHORT_BASIS` | Q-D4 | Entry date, named beside every comparison |
| When two periods of a fixed roster stop being like for like | `FIXED_ROSTER_CHURN_TOLERANCE` | Q-D5 | Ten percent; beyond it the comparison is labelled not like for like rather than suppressed |
| How long a worklist each role should receive | `DELIVERABLE_LINES` | Q-N1 | Standing sizes, named in the front panel. Push back once if the senior number is proportional to span |
| How deep the reference sections go | `REFERENCE_CAP` | Q-N2 | Standing depth; the showing note discloses the cut |
| What sections the artifact has and what an empty one says | `TAB_CONTRACT`, `MSG_EMPTY_SECTION` | Q-N3 | Standing sections and generated empty messages, each naming the binding or column that would have filled it |
| What identifies an entity, in what order, called what | `IDENTITY_BLOCK_COLUMNS`, the `HDR_` strings | Q-N4 | Plain English defaults, stable between runs, with the count of defaulted headers named once |
| What the file is called so two runs never collide | `OUTPUT_FILENAME_PATTERN`, `DELIVERABLE_NAME` | Q-N6 | Standing pattern and a generic report name |
| How strongly a pass rate may be worded on each comparison basis | `CLAIM_STRENGTH_BY_RUNG` | Q-E4 | The standing defaults, printed beside each figure |
| How much movement is noise before a rate is called a win or a miss | `DEADBAND` | Q-E5 | Computed from the data; where it cannot be computed, the raw delta ships with no label |
| Which column holds the identifier and whether it carries leading zeros | `UNIT_ID_CONCEPT`, `UNIT_ID_IS_TEXT` | Q-H3 | The seed concept, handled as text, with the column named |
| Which columns hold the scope levels | the scope concepts in `COLUMN_CONCEPT_DICTIONARY` | Q-H4 | Whichever single scope column resolves, with finer levels read by prefix and the level used stated |
| A short scope code must be padded | `SCOPE_CODE_SCHEME` and the width, direction and pad character | Q-B2 | The scheme is detected from the data; undetectable means codes are matched exactly and the values present are offered |
| A title did not resolve to a role | `ROLE_LADDER.titles`, `ROLE_TITLE_ABBREVIATIONS` | Q-C4 | The generic abbreviation set; an unresolved title asks the user once to pick from a list |
| Who we assume somebody is when we cannot tell | `ROLE_FALLBACK_KEY` | Q-C5 | The narrowest role, which shortens the worklist rather than inflating it |
| Which quiet problems are real here, and which nobody can fix themselves | `EXCEPTION_FLAGS` and the threshold set | Q-EXCEPTION-REMAINDER | The generic flags; every flag whose column did not resolve or carried no data is named as not evaluated, and no absent column is treated as a gap |
| The formatting contract | `FORMATTING_ELEMENTS`, the palette, the fonts, the row heights | Q-FORMAT-REMAINDER | Never asked in a run. The standing set is applied and verified; a volunteered colour or font is recorded immediately |
| Reliability mechanics on a large population | the write, partition, concurrency and checkpoint variables | Q-RUNCTL-REMAINDER | Never asked in a run. Standing values apply |

## F1. The first run at a company where nothing is bound

reference/binding-interview.md Part 6 governs, in full. The frontline user is asked the four
person questions and nothing else, ever, including the ignition questions. The run is
PROVISIONAL: it produces real output, it is labelled provisional in the artifact at the
same prominence every time, and it neither refuses to run nor pretends to be a bound run.

**WHERE `INTERACTIVE` IS ABSENT, NO QUESTION IN THAT PART FIRES AT ALL, AND THIS IS THE
CROSS-REFERENCE A READER OF PART 6 ALONE NEEDS.** Every step of the first-run sequence
assumes somebody can be asked, so on a scheduled run, an unattended batch or a pipeline
with nobody on the other end, none of it can run and the file's silence used to read as an
instruction to try. reference/binding-interview.md rule I11 states the consequence in the
interview's own language and reference/capability-probe.md 2.14 rung 2 carries the matching
paragraph, which is the authority where the two ever appear to differ. Both are cited here
and neither is restated: read them for what happens instead, which is in outline that no
question is asked and no answer is invented, every unbound variable takes its documented
default and prints that variable's exact degradation notice, the run lists every question
it WOULD have asked with the variable each would have bound and what that binding would
have changed about this artifact, and nothing is written to the organization config because
no authorized answerer looked at anything. Silence is never read as confirmation and never
as a decline, per SD-CNF-04.

For this skill specifically, a provisional run can still do most of the job. It can read a
standard the requester points it at; it can resolve a population and a scope from the file;
it can classify into all five states, because the classification contract needs no
organization binding at all; and it can publish every rate in A4. What it cannot do, and says on
its face: it excludes nothing, because no not-actionable field is bound; it applies no
jurisdictional permission test; it carries only the floor rung as its second number, so no
figure is worded as an achievement; and it uses generic reason codes rather than the
organization's own words.

Everything the run inferred is written to a provisional record with its evidence, never to
the config, so that whoever eventually runs the ignition interview starts from proposals
rather than from a blank page.

---

# PART G: HARD GATES

## G1. The convention, adopted as written

`HARD_GATES` is ONE organization variable and it is a TAXONOMY of FOUR KEYED GROUPS:
`shared`, `planning`, `review`, `scorecard`. It is never a flat list. The convention is
owned and defined once, by the planning skill, and this skill conforms to it as written
rather than restating or renegotiating it. What follows is this skill's conformance, not
a second definition.

**The gate record.** Every gate, in every group, carries exactly six fields, and a gate
missing any of them is not a gate: `key`, stable lower snake case and unique across all
four groups; `group`; `fires_at`, the named stage or probe step with any condition;
`behaviour`, exactly one of `stop_outright` or `ask_one_question_then_stop`, with no third
value; `reads`, the schema variable the gate tests or the literal `none`, never a
threshold written as a literal in skill text; and `doctrine`, an ID whose Applies list
covers every skill in whose group the gate sits.

**The effective set.** This skill enforces `shared` plus `scorecard`, and nothing else. It
never enforces or reads another skill's group.

**No skill may remove a shared gate.** Where a shared gate cannot apply to a run mode it
resolves NOT APPLICABLE per SD-EFF-37, which is a passing state, recorded with its reason.
It is never silently dropped and never redefined locally.

**Counts live in the taxonomy and nowhere else.** This file states no count of gates, in a
table, in prose, in a heading or in a parenthesis, and refers to the set only by group
name.

**Additions are bound, never invented.** A stop condition this skill needs and does not
have is requested through the deferred-binding mechanism in Part F, naming the decision.
Until it is bound, the condition degrades and is disclosed rather than stopping. An
implementer inventing a stop condition is the exact failure SD-EFF-02 exists to prevent.

## G2. The scorecard group

| key | fires_at | behaviour | reads | doctrine |
|---|---|---|---|---|
| `no_scorable_requirement` | Step 3, after the requirement set from Step 2 has been mapped to evidence and every mapped column has had its non-null count checked within scope | `stop_outright`: name the requirement set that was resolved, name every evidence field tested and why each failed, and say plainly that no cell could be classified and no rate computed | `COLUMN_CONCEPT_DICTIONARY` | SD-PRS-25 |
| `scorecard_qualifier_matched_no_value` | Step 1 item 4, where the phrase ROUTED to a column family and no value in that family matched | `ask_one_question_then_stop`: report the phrase, the column tested, and the `MISS_SUGGESTION_COUNT` nearest values present | `MISS_SUGGESTION_COUNT` | SD-QUA-10 |
| `universal_gap_unconfirmed` | Step 3b.6 reconciliation, and ONLY where the requirement's eligible population is at or above `MIN_POPULATION_FOR_RANKING`, after Step 2 has been re-read once automatically and still reports the requirement as current | `ask_one_question_then_stop`: name the requirement, the eligible count, and the three likelier causes, then ask whether it is genuinely failing everywhere | `MIN_POPULATION_FOR_RANKING` | SD-EXC-08 |
| `provenance_unassessable_unconfirmed` | Step 4, after B1.1 has assigned a provenance class to every requirement and BEFORE Step 5 builds anything, and ONLY where the scored population is at or above `MIN_POPULATION_FOR_RANKING` | `ask_one_question_then_stop`: name each requirement, the class B1.1 assigned it and which step of B1.1 assigned it, the count of cells that decision made unassessable against the count that would otherwise have been scored, and the three likelier causes, then ask whether the evidence rule is genuinely absent | `MIN_POPULATION_FOR_RANKING` | SD-EXC-08 |

`no_scorable_requirement` is this skill's twin of the planning skill's
`no_measure_column`, and it carries a different key because keys are unique across all
four groups, and the twins fire at different stages on different evidence. Its
justification is the same: a source is usable when it resolves an identifier, a scope
column and the thing the method rests on, and for this skill the thing the method rests on
is evidence for at least one current requirement.

`scorecard_qualifier_matched_no_value` is the twin of the planning gate of nearly the same
name, distinguished because SD-QUA-10 does not carry REVIEW and the gate therefore cannot
be promoted to `shared`.

`provenance_unassessable_unconfirmed` is DECLARED HERE, in this skill's own group, with the
full six-field record G1 requires, rather than invented at run time by an implementer who
needed a stop and did not have one. That distinction is what G1's additions rule is about:
a run may never invent a stop condition, and the skill's own declared group is where a
needed one is written down so every run enforces the same one. It is the twin of the gate
below, on the other colour,
and B1.2 states the whole reasoning. The two gates answer the same shape of failure from
opposite ends: a scope-wide result produced by a RESOLUTION DECISION rather than by the
data. `universal_gap_unconfirmed` catches it when the result is red; this one catches it
when the result is amber, which nothing else in the file could see. It shares the
population floor for the same reason its twin has one: over two or three entities a
majority-unassessable scorecard is ordinary and the gate does not fire. It shares
SD-EXC-08 because it is the same doctrine read in the other direction, that a column or a
class which resolved to nothing is a defect to repair rather than a finding to publish.

`universal_gap_unconfirmed` is the gate that protects the thing this skill exists for. A
requirement classified GAP for one hundred percent of a non-trivial eligible population is
far more often a retired requirement, a broken evidence mapping or a wrong eligibility test
than a real collapse, and shipping it manufactures a scope-wide crisis out of a defect. The
population floor matters: at one or two entities a universal gap is ordinary and the gate
does not fire. Under a non-interactive run the question cannot be asked, so the bannered
incomplete path in reference/capability-probe.md 2.14 applies and the requirement ships with the
question named, per SD-EFF-05.

## G3. What is deliberately NOT a gate in any group

Stated so nobody re-adds them, because each has been implemented as a stop at least once.

| Condition | Why it is not a gate | What happens instead |
|---|---|---|
| Reading the published standard | SD-SRC-21. Mandatory means never assumed, not never skipped. Reading the standard belongs to no group | The fallback ladder in 2.1, the banner in 2.9, the exact release and date named |
| A required reference has no cached equivalent | SD-SRC-13 and SD-SRC-18. A stale or absent reference is a disclosed limitation; a halted run is a dead end | The sections it feeds ship with their explanatory rows naming the reference, and affected figures drop a rung |
| The manifest reconciliation in 3b.6 | Its terminal state is a bannered partial, so it satisfies neither permitted `behaviour` value. Making it a gate would contradict 3b.7 and recreate the defect this Part exists to close | The retries in 3b.3 and 3b.4, then the bannered artifact in 3b.7 naming the exact units and counts missing |
| An all-null evidence column | It is a LOGICAL failure repaired in place per SD-EFF-09, and its unrepaired terminal state is a classification, not a stop | Re-resolve up to `REPAIR_CYCLE_LIMIT`, then the requirement is `? UNASS: evidence column present but empty` and is named in the audit |
| A cold population, or no prior period | A first-class operating condition per SD-CLM-27, not a failure | A8: labels dropped, rungs re-evaluated, the three surviving claim kinds reported |
| A population below `MIN_POPULATION_FOR_RANKING` | An honest small scope, and the commonest reader this skill has | 1.6: the comparative half is suppressed and named; every cell, rate and reason still ships |

---

# PART H: GUARDRAILS

## H0. When not to use this skill, and where to send it instead

- Editing, reformatting or charting a workbook that already exists: the spreadsheet skill.
- Ranking a population by opportunity, revenue or where somebody should spend a day
  rather than by conformance: the planning skill in this bundle.
- Writing or grading objectives and performance narrative: the review skill in this bundle.
- Anything `SYSTEM_OF_RECORD_EXCLUSIONS` names as owned by another system. Do not build a
  second version of something that already has a system of record (SD-EXC-24), and route
  per `SIBLING_SKILLS`.
- Judging whether a standard is a good standard. This skill scores against the published
  standard; it does not rewrite it.

## H1. The classification guardrails

- **Never let an unassessable condition be reported as a gap**, in the artifact or in the
  chat. Report gap counts and could-not-assess counts as two separate numbers everywhere
  either appears.
- **Never let a not-required condition be reported as either.** Grey, amber and red are
  three answers, never two.
- **Never publish pass divided by eligible as the compliance figure.** All three rates,
  always, per A4, **in the artifact AND in the reply**. Two of the three is not a permitted
  publication anywhere, and Step 6 item 3 is the place a run is most likely to ship two.
- **Never publish a pass that rests on weaker evidence as a plain pass.** Each such pass
  carries its qualifier CODE in the cell, from the closed bound pair A3 names, and a Legend
  line is never a substitute for the MARK. The Legend carries the WORDING against that code,
  which is where reference/output-contract.md 2.7 puts a standing qualifier and is not the same
  thing as carrying the mark (A3, B2, 3.5.2, SD-FMT-28).
- **Never resolve a person's statement against a column that resolved by picking a winner.**
  It is a third state with its own remedy: the cell is unassessable, both readings are
  printed with the question that would settle them, and nothing disputed is published as a
  figure (B2, SD-CNF-10).
- **Never resolve an ambiguous provenance to the stronger class.** B1.1 step 4 takes the
  weaker of the classes the met-condition describes, and the layer actually read can lower
  that and never raise it (B1.1, B4).
- **Never compare a reader to peers on a rate carrying cells they cannot move.** The
  comparison runs on the attributable rate, both deltas are computed, and the difference
  between them is published as the part of the gap that is mix rather than work (A5.1).
  A figure that makes somebody look worse gets less scrutiny than one that flatters them,
  which is why this direction needs the rule more, not less.
- **Never let self-reported evidence become green silently**, per B2.
- **Never let an inference produce a colour**, per B3.
- **Never assign a provenance class because of where it sits on the table.** B1.1 assigns
  it from what the evidence IS, in a stated order, and INFERENCE is never a default. The
  one place a strength ordering enters is B1.1 step 4's tie-break between two classes the
  met-condition genuinely describes, and it moves toward the weaker one.
- **Never publish a scorecard that one provenance decision made mostly unassessable
  without questioning the decision first.** B1.2 computes it before Step 5 builds anything.
  A wall of amber is as scope-wide a result as a wall of red, and nothing else in the file
  can see it.
- **Never score a requirement the current standard does not carry.** The standard read in
  Step 2 is the authority on what counts this period; the evidence source's column list is
  not. A column that has outlived its requirement is a trap, not a requirement.
- **Never score a requirement that has not started, or one the jurisdiction does not
  permit.** Both are grey.
- **Never turn a targeted requirement into a wall of red.** Where a requirement applies to
  a handful of assigned entities, everything outside that set is grey, and the applicable
  count is stated.
- **Never let an empty evidence column become a wall of red.** A resolved but empty column
  is an absent column (SD-PRS-18), and treating it as a universal failure is the single
  most damaging false positive this skill can produce.
- **Never let a full column become a rule.** A field blank on every row, or populated on
  every row, defines no distinction. Record it as NOT PRESENT and apply nothing
  (SD-QUA-04, reference/field-resolution.md 3.12). Read one way it manufactures a wall of red;
  read the other it manufactures a wall of grey that reads as an all-clear.
- **Never route a requirement out of scoring because somebody above the reader wrote it.**
  Authorship is not ability. Only a separate finding that compliance is determined above
  the reader suppresses scoring, and where more than half the set is suppressed, say so
  before the pass rate (SD-EXC-14, 4.4).
- **Never suppress a whole requirement on a finding that holds for part of it.** Route at
  the granularity the finding holds at, publish both counts, and give the suppressed subset
  a state with an owner who is not the reader (4.4b).
- **Never phrase a gap reason as the requirement's met-condition.** It reads in the cell as
  an assertion that the condition holds, which is the opposite of the finding, and it
  passes every check because it quotes the standard accurately (4.1 step 9).
- **Never publish a conformance rate for a period that has not started.** Publish a
  readiness rate, name it as one, and state the period's dates before any figure (3.5.1).
- **Never drop a scored category because it is not the headline kind.** Continuous,
  threshold and above-entity requirements are part of the same standard; omitting them
  under-reports what the population is measured on. Report them, labelled as their own
  section, never folded into the binary counts.
- **Never invent a requirement-to-evidence mapping.** An unmapped requirement is amber with
  a reason, and it is raised.
- **Never let a rate imply a comparison that does not exist.** A cold population carries no
  WIN, MISS or FLAT anywhere, and NO BASELINE is printed instead, distinguishable from
  UNPAIRED and from FLAT.
- **Never let a denominator the reader is building pass as a comparison.** Run the
  independence test every run, not only when a column fails to resolve.

## H2. The source guardrails

- **Never read the standard from outside its authoritative location**, and never from a
  staging area holding the next period's unreleased content. Stale mirrors exist and will
  silently score the wrong period.
- **Never apply one jurisdiction's requirement set to another's entities.** A
  multi-jurisdiction scope reads every jurisdiction's standard in scope.
- **Never conclude a document is unreadable from one extractor.** Try a second, and record
  which worked.
- **Never state an interpretation of a value whose meaning varies by jurisdiction**
  (SD-EXC-23). Print the status and the benchmark, attribute it, and leave the judgment to
  the person who knows their jurisdiction.
- **Never let an internal document amend an external standard.** It governs whether and
  how this organization scores a requirement; it cannot change what the requirement is,
  retire it, pause the obligation, reset its edition or relax its evidence rule (2.2b).
  Where the two disagree about the requirement itself, score the external one and name
  both.
- **Never claim to have inspected evidence you did not read.** Name the layer you actually
  read, per B4.
- **Never treat reading the standard as a stop.** SD-SRC-21. Mandatory means never assumed.
- **Never break a strict-concept tie by column position.** Where two concepts match one
  header exactly and either is strict, neither resolves and both are named (SD-PRS-47).
- **Never leave a second file carrying the evidence unread**, and never join it on a key
  that failed a precondition. Join on the identifier under SD-PRS-48 and 3.2.1, or record
  the file READ AND NOT JOINED with the failed condition and the unevaluated requirements
  named. Leaving it unread is not the conservative choice.
- **Never let an unmatched unit become a gap.** A unit with no row in the evidence file has
  no capture, lands unassessable at step 8 of the ladder, and is never scored as a failure
  (3.2.1, A1). A blank is not a zero and an absent record is not evidence of a negative.
- **Never let a join change the row count of the scored population.** Before equals after,
  asserted and blocking, in either direction (SD-PRS-48).

## H3. The completeness guardrails

- **Never accept a first empty result.** Three consistent attempts on the backoff schedule
  before anything is called empty, and never rewrite a query that has not been retried.
- **Never ship a short report silently.** If the reconciliation gate fails, deliver the
  artifact bannered, with the exact units and counts missing named.
- **Never report a scope you did not fully retrieve.** If the unit batching came up short
  of the manifest, state the gap in the artifact and in the first line of the reply.
- **Never shorten the wider-scope path.** The same steps, the same checks, the same
  requirements. Only longer.
- **Never sample, estimate or extrapolate** a rate, a threshold or a count at any scale
  (SD-SCL-03).
- **Never present the degraded output as complete**, and never quietly downgrade a
  degradation notice because it has appeared before.
- **Never invent a stop condition.** The effective stop list is `shared` plus `scorecard`
  in Part G and nothing else. A condition this skill needs and does not have is requested
  as a binding and degrades until it is bound.
- **Never state a count of gates** anywhere in this file, per the convention in G1.

## H4. The honesty guardrails

- **Never fabricate an entity, a state, a reason, a count or a rate.** If a query returns
  nothing, say so. A visibly missing number is recoverable; a fabricated one is not
  (SD-CNF-07). Every number traces to a cell or a tool result (SD-CNF-08), and every
  arithmetic result is computed by code, never mentally (SD-RUN-14).
- **State the period, the standard's edition and the evidence refresh date** on the
  Summary, in the Legend and in the reply. An undated scorecard gets argued about.
- **Print the indicator caveat** where the evidence source is not the system of record for
  the official score.
- **Do not evaluate, rank or compare people.** This skill scores the condition of entities,
  never the person who serviced them, even where the evidence carries a person field.
  Never group results by person, and decline outright if asked (SD-LNG-02). Where the
  population is people, as in a certification or onboarding scorecard, the same rule holds
  in its exact form: score the requirement against the record, publish no ranking of
  individuals, and apply `ANONYMITY_FLOOR` to any comparative figure.
- **Measure impact, do not judge the remainder.** Write toward the fix, never toward shame
  (SD-LNG-01). Every entity matters to the person who owns it.
- **Do not send, post or share the artifact** unless explicitly asked (SD-CTR-18). Produce
  it, name it, hand it over.
- **A filter on somebody else's section is not that person's report** (SD-SPN-07). Filtering
  a wide scorecard to one sub-unit answers which of my entities are in that sub-unit; it
  never answers what that sub-unit's own scorecard says, because the caps, the ranking and
  the peer set were all computed over a different population. The remedy is to run the
  skill at that scope.
- **Never publish a figure whose subject is a person.** A scope level whose members are
  individuals selects a population and attributes a row; it is never a grouping, a rank, a
  sort or a comparison axis, and where it cannot be determined whether a level is
  person-bearing it is treated as one (A9). The interlock is condition 6 of 3b.6, tested
  against the built artifact.
- **Never interchange a level, a rate and an attainment.** Three quantities, three units,
  and every emitted figure names its own (A5, SD-CLM-06).
- **Never let a documented default delete evidence the run is holding.** A default may
  narrow what a run attempts and may not strike a rung whose defining quantity was read
  from a document already in hand, named, dated and authored by somebody other than the
  reader (A5.2, S9, SD-CTR-24).
- **Never write that a cell was suppressed when it sits in the rate printed beside it.**
  The word belongs to a cell that is out of that rate; under 4.4b step 5's first branch the
  cell is scored, red, in the census and in the conformance figure, and the sentence for
  that branch is the one 4.4b step 4 gives.
- **Never publish a conformance rate under a name 3.5.1 has renamed.** Where the window has
  not opened, all three of A4's rates carry 3.5.1's labels and each is defined beside its
  first appearance.
- **Never certify a closed vocabulary without validating it against the states it serves.**
  From the states to the set, not the reverse (SD-CTR-29, 4.2).
- **Never inherit another skill's section list or artifact name.** Both are keyed by skill
  (SD-CTR-30, Step 5).
- **Never ship a templated sentence tested only at many.** Zero, one and many, every time
  (SD-LNG-13).
- **Never rank a reader against their own subordinates**, and never manufacture a peer set
  for a reader at the top of the chain. Say there is none, use the bound external group if
  there is one, otherwise drop the rung and name the drop (SD-SPN-14, SD-SPN-15).
- **Never let the calendar decide who is on the sheet.** Urgency is two columns and a
  filter, not an ordering; sorting by date makes the cap cut on the date axis and deletes
  exactly the entities the sheet exists to surface (SD-RNK-07, 5.5).
- **Never send the reader to work they cannot do through the one filter they click.** The
  urgency column's `overdue` state, the ranking basis and the worklist all run on
  ATTRIBUTABLE gaps and all three say the same thing about the same cells (5.5, 5.0,
  4.4b).
- **Never write an urgency value from prose.** The five states are keys and the strings are
  their bound labels in `URGENCY_VOCABULARY` (5.5, S10).
- **Never ship an entity sheet without a filter on every column, a rank column in
  first position and a reason-for-rank column.** Element 6 and R1. A sheet without them has
  failed and does not publish.
- **Never carry the filter only inside the table object, and never set two filter objects
  over one range.** It is the SHEET'S own filter, read back from the sheet, and a filter
  found only inside the table container is scored ABSENT. Where the engine cannot carry
  both, element 3 gives and the visible filter stays (elements 3 and 6, SD-FMT-29).
- **Never style a band across a span without MERGING it across that span, and never let a
  string overflow its own cell.** The next cell's border is then drawn through a word.
  Every title band, section header band, note band, explanatory row and banner is merged
  across exactly the span it needs (PART 2.10, SD-FMT-30).
- **Never narrow a column below the longest unbreakable token it displays, and never break,
  hyphenate, truncate or shrink a token to fit one.** A token past the column cap is
  reported in Method, naming the column, the token, its length and the width it forced
  (PART 2.2.2 step 3b, PART 2.10, SD-FMT-30).
- **Never write a heading, a tab name or a column header in anything but Title Case.** One
  convention, stated by `TITLE_CASE_HEADINGS`, with the single exemption of a string the
  organization BOUND, which ships in the case it was bound in (SD-FMT-13).
- **Never put a title, a banner or a note above the header row.** Element 1. The title
  lives on the front panel, and everything else in the contract depends on this one. A note
  that belongs to a grid goes in that sheet's NOTE BAND and nowhere else (5.10, SD-FMT-26),
  which is below the populated block and does not engage element 1 at all.
- **Never head a position column with a band label.** `HDR_POSITION` on a non-merit order,
  `HDR_RANK` on a merit order, and `HDR_PRIORITY_BAND` on neither (5.6, PART 4.1).
- **Never write a column header as a literal WHERE A VARIABLE NAMES IT**, which is PART 8's
  own scope. Every header for which a variable exists reads that variable, and a header
  typed into this file is a second source of truth nothing updates. Where a column the
  contract mandates has NO variable, the column is still built, its header is defaulted in
  plain language, and the default is counted and named in Method and raised as a schema
  request; dropping the column instead is forbidden by SD-CTR-13 (I1, PART 8, 5.6).
- **Never make a classification fill conditional on the centring test.** 2.5's character
  bound decides ALIGNMENT and is read nowhere else; 2.6's four conditions decide the FILL
  and none of them is a length bound. Coupling them made the fill unreachable on this
  skill's own grid and shipped 1520 status cells with no colour (4.6, PART 8, SD-FMT-27).
- **Never give two states of the classification vocabulary one fill.** Four answers that
  read as three colours are three answers, the map is INJECTIVE, and two states counted
  differently, excluded differently or cleared by different people are never merged however
  alike they read. Where the palette runs out, a state carries NO fill and the Legend names
  it (4.6, verification row 13).
- **Never let a grid's total width go unmeasured.** `GRID_MAX_TOTAL_WIDTH` is read before
  the columns are built, never raised to clear a failing grid, and the measurement is
  recorded whether or not it fails. Where a grid is over after the ladder has run, it ships
  over and says so, and no column is dropped, narrowed below its own header floor or
  shortened in a value that carries meaning to get there (5.3, PART 2.7, SD-FMT-28).
- **Never walk the frozen span once per sheet.** It is walked ONCE for the artifact from the
  widest case and applied by header name everywhere, one truncation record for the workbook
  and never one per sheet, so the pin lands in the same place on every tab (5.3, PART 4.1.2,
  SD-CTR-08).
- **Never leave a joined evidence file unscored.** A join that lands and resolves nothing has
  moved the failure, not closed it; the one-column-per-requirement shape resolves through the
  declared sibling set, and every joined column is disclosed as resolved or carried unread
  (3.2.1, SD-PRS-48).
- **Never exempt a sheet from `REFERENCE_CAP`.** The census is capped like everything else,
  every capped sheet states its showing note, and completeness is reconciled on the
  RETRIEVED population rather than on the written rows (A7, 5.3).
- **Never rank this skill's output by opportunity, size or value.** Severity only, and the
  entity's measure does not enter it. Harmonizing the two rankings makes this a second work
  plan (5.0).
- **Never truncate the Why string.** A truncated Why hides a gap (5.4).
- **Never record an unexplained not-applicable as a pass.** Three states, and an entry with
  no stated reason is NOT IMPLEMENTED, which is a failure (Step 5, SD-EFF-03).
- **Never decide the not-workable exclusion on whether a binding exists.** The test is
  whether a column resolved, by any path, and the three guards are mandatory on a
  default-driven exclusion (4.1 step 1).
- **Never let an unbound value override a bound one.** A default may narrow what a run
  attempts; it may never replace a decision the organization already made (SD-CTR-24).
- **Never refuse a reader because their scope is small.** Suppress the comparative half,
  name what was suppressed, and deliver every cell, every rate and the full worklist. The
  scoring unit is the requirement, not the entity (SD-POP-25, 1.6).
- **A run must be reproducible.** The same inputs must produce the same artifact. Where they
  do not, find the non-determinism before the report is used (SD-RUN-15).

---

# PART I: WHAT THIS SKILL DECLARES

## I1. The bindings that carry the classification vocabulary

**This file introduces no variable name.** Every name it uses is defined in
reference/schema/, including every one this skill originally asked for, all of which are
now in the schema and are read from there:

| Name | Schema location | What this file contributes |
|---|---|---|
| `CLASSIFICATION_LABELS` | Group 18, taxonomy, DEFERRED | Part A is the contract those five states implement, and 4.1 is the ladder that assigns one |
| `REASON_CODE_SET` | Group 18, taxonomy, DEFERRED | 4.2 holds the seeded content that the schema's documented default refers to, so the seed lives in exactly one place |
| `PASS_QUALIFIER_VOCABULARY` | Group 18, taxonomy, DEFERRED | A3 names the two keys, states which rule of this file produces each, and defines the code that stands for the key in a cell |
| `CLASSIFICATION_VOCABULARY` | Group 16, taxonomy, DEFERRED | 4.6 declares the requirement columns against it and publishes the TOTAL resolution rule from a cell of this skill's own shape to exactly one state |
| `CLASSIFICATION_FILLS` | Group 16, mapping, DEFERRED | 4.6 states which state takes which entry, injectively, and 5.6 publishes the map in the Legend |
| `COLOR_STATUS_PASS` | Group 16, DEFERRED | 4.6 assigns it to the PASS state, cited by `CLASSIFICATION_FILLS` |
| `COLOR_STATUS_GAP` | Group 16, DEFERRED | 4.6 assigns it to the GAP state, cited by `CLASSIFICATION_FILLS` |
| `COLOR_STATUS_UNASSESSABLE` | Group 16, DEFERRED | 4.6 assigns it to the UNASSESSABLE state, cited by `CLASSIFICATION_FILLS` |
| `COLOR_STATUS_NOT_SCORED` | Group 16, DEFERRED | 4.6 assigns it to NOT REQUIRED, and to NOT REQUIRED alone |
| `GRID_MAX_TOTAL_WIDTH` | Group 15, DEFERRED | 5.3 reads it before the columns are built, measures every grid against it, and records the measurement whether or not it fails |

**THREE SCHEMA REQUESTS THIS FILE MADE HAVE BEEN GRANTED, AND THE PARAGRAPHS THAT MADE THEM
ARE DELETED RATHER THAN LEFT STANDING.** Each one was a sentence saying a variable did not
exist, in a file whose schema defined it, and each shipped two readers building two different
workbooks off one configuration:

- **`COLOR_STATUS_GAP` AND `COLOR_STATUS_UNASSESSABLE` EXIST, WITH DOCUMENTED DEFAULTS AND
  WITH THE GREYSCALE SEPARATION ARITHMETIC THAT PROVES THE PALETTE APART.** 4.6's table used
  to say no palette variable existed outside the alert pair for either state and to withhold
  the fill until one was bound. That claim is deleted from 4.6 and from here, and both states
  take their variables. **The old claim was wrong twice**: the variables existed, and they
  were never what blocked the fill.
- **`PASS_QUALIFIER_VOCABULARY` EXISTS.** A3 used to write both qualifier strings out in Part
  A on the ground that no bound variable carried them. It names the two keys now and writes
  neither string.
- **`GRID_MAX_TOTAL_WIDTH` EXISTS**, so a grid's total width is bounded rather than merely
  regretted, and 5.3 measures and records it.

**WHAT ACTUALLY BLOCKED THE FILL, RECORDED HERE AS A RETIRED DIAGNOSIS SO NOBODY RESTORES
IT.** The fill was blocked by a CONDITION, not by a missing colour: 4.6 declared the
requirement columns STATUS GRID COLUMNS in order to earn the fill, and a status grid column
is bounded at `CENTRE_ALIGN_MAX_CHARS` characters. This skill's shortest possible gap cell is
fifteen characters and its shortest unassessable cell is longer, against a bound whose
default is twelve, so no standard, no organization and no binding could ever have produced a
lawful fill on this grid. Measured: 1520 status cells shipped monochrome, correctly under the
text as it stood and contrary to the artifact this file's own description promises.
reference/output-contract.md 2.6 now carries four conditions of its own, none of them a length bound,
2.5's bound governs CENTRING and is read nowhere else, and 4.6 declares a CLASSIFICATION
COLUMN and leaves the columns left aligned. **A cell can be far too long to centre and still
be exactly the cell that most needs a fill**, and the earlier sentence naming two palette
variables as THE ONLY THING BLOCKING THE FILL was wrong about the cause as well as about the
variables.

**GAP AND UNASSESSABLE NO LONGER REUSE THE ALERT PALETTE, AND THAT REUSE IS RECORDED HERE
AS A RETIRED DECISION SO NOBODY RESTORES IT.** An earlier revision gave GAP
`COLOR_ALERT_OVERDUE` and UNASSESSABLE `COLOR_ALERT_WARN`, on the reasoning that the alert
semantics already matched and two palette variables were saved. reference/output-contract.md 2.6
and SD-FMT-27 forbid it: those two colours are element 13's bands, a classification
palette is DISJOINT from them, and a workbook that carries an elapsed-time column would
otherwise paint one colour with two meanings on one grid.

**NOT REQUIRED AND RETIRED NO LONGER SHARE A FILL EITHER**, and that sharing is recorded
alongside it for the same reason. `CLASSIFICATION_FILLS` is INJECTIVE and verification row
13 blocks publication on it. Two states counted differently, excluded differently or cleared
by different people are never given one colour however alike they read, and these two differ
on all three.

**THE SCHEMA REQUESTS THIS FILE STILL MAKES, AND NONE OF THEM BLOCKS AN ARTIFACT.** Each
names the decision that needs it, per Part F, and each ships a stated default until it lands:

1. **A SHORT BOUND CODE PER ENTRY OF `PASS_QUALIFIER_VOCABULARY`**, so an organization can
   give the qualifier a mnemonic in its own language rather than an ordinal. Until it exists,
   A3 uses the entry's ORDINAL POSITION in that closed two-entry set, which is stable between
   runs because the keys are fixed and never renamed, and the Legend publishes the ordinal
   against the entry's bound `label` in full. The moment a bound code exists nothing in this
   file changes, because A3 reads the vocabulary rather than naming a code.
2. **HEADER VARIABLES FOR THE SUMMARY'S OWN COLUMNS**, which the schema names for three of
   about fifteen. The sheet carries eligible, assessed and the four state counts, the three
   rates, the difference between two of them, the applicable count, both influence counts and
   the second number with its rung, and no variable names any of those. Until they exist,
   5.6 defaults those headers in plain language under reference/output-contract.md PART 8's scoped
   rule and Method counts and names every one, which is the same sweep that gave the entity
   sheets `HDR_COMMITMENT_DATE`, `HDR_URGENCY`, `HDR_FAILS`, `HDR_BLOCKED` and
   `HDR_UNASSESSED` and which did not reach the reference tables.
3. **A HEADER VARIABLE FOR THE SUMMARY'S ROW-KIND COLUMN**, per 5.6, which would let a reader
   filter the requirement block apart from the scope-unit block in one click; until it exists
   the kind is the first clause of each row's `HDR_RANK_REASON` cell.

**EVERY COLUMN HEADER THIS SKILL EMITS FOR WHICH A VARIABLE EXISTS IS THAT VARIABLE, AND THE
SWEEP THAT MADE IT TRUE IS RECORDED HERE SO NOBODY UNDOES IT.** Five headers on each entity
sheet were once written as literals with no binding behind them, which contradicted the
sentence this section opens with, meant an organization could not rename them in its own
language, and meant the count of defaulted headers Part F promises to disclose could not
count them, because a literal is not a default. They are now `HDR_COMMITMENT_DATE`,
`HDR_URGENCY`, `HDR_FAILS`, `HDR_BLOCKED` and `HDR_UNASSESSED`, read from the schema like
every other header. Three further corrections belong with them: the reason-for-rank column is
`HDR_RANK_REASON` and there is no second variable for it, the earlier duplicate having been
retired; the position column of a sheet whose order is NOT a merit order is `HDR_POSITION`
and never `HDR_PRIORITY_BAND`, which heads BAND LABELS and never a column of numbers; and the
commitment-date column has exactly one variable, so this file writes no alternative word
for it and asks for no second name. **On the entity sheets the rule is absolute**, because
every header they carry has a variable; on the reference tables it is PART 8's scoped form
plus the disclosure in 5.6, because three of about fifteen do. No hex value and no colour
name appears anywhere in this file.

## I2. Doctrine cited

Contract and shape: SD-CTR-01, SD-CTR-02, SD-CTR-04, SD-CTR-07, SD-CTR-08, SD-CTR-09,
SD-CTR-10, SD-CTR-13, SD-CTR-14, SD-CTR-15, SD-CTR-16, SD-CTR-17, SD-CTR-18, SD-CTR-21,
SD-CTR-24, SD-CTR-28, SD-CTR-29, SD-CTR-30.

Span of control: SD-SPN-01, SD-SPN-02, SD-SPN-03, SD-SPN-05, SD-SPN-06, SD-SPN-07,
SD-SPN-08, SD-SPN-14, SD-SPN-15, SD-SPN-16.

Formatting: SD-FMT-01, SD-FMT-02, SD-FMT-03, SD-FMT-05, SD-FMT-06, SD-FMT-08, SD-FMT-14,
SD-FMT-23, SD-FMT-24, SD-FMT-26, SD-FMT-27, SD-FMT-28, SD-FMT-29.

**SD-FMT-29 IS NEW HERE AND IT IS WHY A FORMATTING PASS IS NOT SELF-CERTIFYING.** Formatting
is chosen to degrade safely, because the author verifies in the renderer that built the file
and the reader opens another one: a text-and-band pair is asserted against the intended
pairing and against both degraded renderings, every colour carries an explicit opaque alpha,
and where two layers can produce one property they agree in direction rather than merely both
being present. 5.8 carries the position, 5.10 carries element 7's sheet-wide border walk that
reaches the note band, and 4.6 and 5.6 carry the opacity form on every classification fill.

**SD-FMT-28 IS NEW HERE AND IT BOUNDS A GRID'S TOTAL WIDTH**, which nothing did: the frozen
span bound was in force and correctly honoured, three columns stayed pinned, and a census
sheet was still 21 columns and 749.12 width units across because a mandatory cell qualifier
fifty characters long repeated on every row of fourteen columns. 5.3 reads the bound before
the columns are built and measures every grid against it; A3 has the standing qualifier out
of the cell before the ladder starts.

**FOUR RULES THIS FILE ALREADY CITED WERE AMENDED, AND THIS FILE AGREES WITH ALL FOUR AS
AMENDED.** SD-CTR-08 now says the freeze lands in the SAME PLACE on every entity sheet, which
5.3 adopts by walking the span once for the artifact. SD-FMT-27 now says a classification
fill is never conditional on the centring test, which 4.6 adopts by declaring a
classification column rather than a status grid column. SD-FMT-03 gains the single position
of the reason-for-rank column and the bound on the span, both of which 5.3 already carried.
SD-PRS-48 now says a join that lands and cannot be scored has not answered the failure it
exists to prevent, which 3.2.1 adopts through the declared sibling set.

Rank and caps: SD-RNK-01, SD-RNK-06, SD-RNK-07, SD-RNK-08, SD-RNK-09, SD-RNK-10, SD-RNK-11.

Effort and failing closed: SD-EFF-01, SD-EFF-02, SD-EFF-03, SD-EFF-04, SD-EFF-05,
SD-EFF-07, SD-EFF-09, SD-EFF-10, SD-EFF-13, SD-EFF-15, SD-EFF-16, SD-EFF-17, SD-EFF-18,
SD-EFF-22, SD-EFF-23, SD-EFF-25, SD-EFF-28, SD-EFF-29, SD-EFF-30, SD-EFF-31, SD-EFF-33,
SD-EFF-37, SD-EFF-38.

Run architecture: SD-RUN-01, SD-RUN-10, SD-RUN-14, SD-RUN-15.

Identity and scope: SD-IDN-01, SD-IDN-03, SD-IDN-04, SD-IDN-07, SD-IDN-08, SD-IDN-09,
SD-IDN-10, SD-IDN-11, SD-IDN-12, SD-IDN-13, SD-IDN-14, SD-IDN-15, SD-IDN-16, SD-IDN-17.

Qualifiers: SD-QUA-01, SD-QUA-02, SD-QUA-04, SD-QUA-05, SD-QUA-06, SD-QUA-10, SD-QUA-12.

Priorities and authority: SD-PRI-31, SD-PRI-32.

Sources: SD-SRC-13, SD-SRC-14, SD-SRC-15, SD-SRC-17, SD-SRC-18, SD-SRC-19, SD-SRC-21.

Parsing: SD-PRS-02, SD-PRS-05, SD-PRS-11, SD-PRS-12, SD-PRS-13, SD-PRS-14, SD-PRS-16,
SD-PRS-18, SD-PRS-24, SD-PRS-25, SD-PRS-44, SD-PRS-47, SD-PRS-48.

Population: SD-POP-01, SD-POP-02, SD-POP-05, SD-POP-06, SD-POP-07, SD-POP-12, SD-POP-17,
SD-POP-18, SD-POP-19, SD-POP-20, SD-POP-21, SD-POP-22, SD-POP-23, SD-POP-24, SD-POP-25,
SD-POP-26, SD-POP-27, SD-POP-29, SD-POP-30.

Weighting: SD-WGT-02.

Exceptions: SD-EXC-02, SD-EXC-06, SD-EXC-08, SD-EXC-14, SD-EXC-15, SD-EXC-20, SD-EXC-22,
SD-EXC-23, SD-EXC-24, SD-EXC-29.

Comparison: SD-CMP-01, SD-CMP-02, SD-CMP-09.

Breadth: SD-BRD-03, cited as the precedent for the declared departure in A7.

Claims: SD-CLM-03, SD-CLM-04, SD-CLM-06, SD-CLM-07, SD-CLM-12, SD-CLM-27, SD-CLM-28,
SD-CLM-29, SD-CLM-30, SD-CLM-31, SD-CLM-32, SD-CLM-33, SD-CLM-34.

Confidence: SD-CNF-01, SD-CNF-03, SD-CNF-04, SD-CNF-07, SD-CNF-08, SD-CNF-10.

**SD-CNF-10 IS NEW HERE.** A person's own claim that a resolved cell contradicts is a THIRD
state, neither unsourced nor a disagreement between two of the method's own derivations, and
neither side wins automatically. B2 routes it, because on this skill the person's claim
arrives as an attestation and the resolved cell is the evidence column beside it.

Language: SD-LNG-01, SD-LNG-02, SD-LNG-03, SD-LNG-13.

Scale: SD-SCL-01, SD-SCL-03.

Scope and structure: SD-SCO-03, SD-STR-10.

Governing rules: G2, G3, G4, G5.

The gate records in Part G carry their own doctrine IDs in the `doctrine` column and are
not repeated here.

## I3. The regression cases this skill must pass before a change ships

Per SD-RUN-10, a small closed set of end-to-end cases, each with inputs, expected result
and the failure it catches. At minimum:

1. **The retired requirement.** An evidence column exists for a requirement the current
   standard does not carry. Expected: no column, one line in the audit. Failure: a
   scope-wide red wall.
2. **The empty evidence column.** A requirement's column resolves and holds no values.
   Expected: amber for every eligible entity with the mapping reason, and the
   reconciliation gate stops the build. Failure: a scope-wide red wall.
3. **The unassessable entity.** An entity with no evidence captured in the period.
   Expected: amber, excluded from the pass-rate denominator, counted in the assessability
   rate. Failure: red, or silent inclusion as a pass.
4. **The self-report.** A requirement whose only evidence is an attestation and whose
   standard requires observation. Expected: amber, labelled. Failure: green.
5. **The targeted requirement.** A requirement eligible for a small fraction of the scope.
   Expected: grey outside the target set, with the applicable count stated. Failure: red
   outside the target set.
6. **The jurisdictional exclusion.** A requirement forbidden where some entities sit.
   Expected: grey, permanent, named. Failure: red, or silent omission.
7. **The silent truncation.** A scope larger than the query interface's result ceiling.
   Expected: partitioned retrieval, manifest reconciled, complete. Failure: a short report
   that looks whole.
8. **The cold source.** The first query for a unit returns empty and the third returns
   rows. Expected: the unit is complete. Failure: `verified empty` recorded on the first
   response.
9. **The wrong scope column.** Two similarly named scope columns with slightly different
   row counts. Expected: exact-name resolution, the right population. Failure: a
   near-right population that reconciles against itself.
10. **The stage that has not been reached.** Under FLOW, an item that has not yet arrived
    at the requirement's stage. Expected: grey, not yet due. Failure: red.
11. **The span-of-control error.** A wide-scope run filtered to one sub-unit, presented as
    that sub-unit's report. Expected: refused, with the remedy named. Failure: a
    plausible, wrong report.
12. **The no-binding company.** Every organization variable unbound, a frontline
    requester, one file. Expected: a real provisional artifact with all five states, both
    rates at the floor rung, and the provisional block at the top. Failure: a refusal, or
    an artifact that reads as authoritative.
13. **The unpublished standard.** The next period's release is published after the run
    date. Expected: score against the current release, name it and its date, banner the
    run as standard unconfirmed, continue. Failure: a stop, or a silent score against an
    assumed list.
14. **The single-entity reader.** A reader whose scope holds one entity, scored against
    a full requirement set. Expected: every cell, every rate, the full reason vocabulary,
    the worklist, and one front-panel line saying nothing is ranked and no cross-entity
    comparison is drawn. Failure: a refusal, a one-row ranked list, a percentile, or a
    rank of one out of one.
15. **The coarse unit.** A reader whose own scope sits finer than the level at which one
    entity sits. Expected: named as a binding error before the content, both levels named,
    the scorable level named. Failure: a one-row artifact in which every gate passes.
16. **The top-of-house reader.** A reader at the coarsest level in the chain. Expected:
    no internal peer set, said plainly, the external group used if one is bound, otherwise
    the peer rung dropped and the drop named. Failure: ranked against their own
    subordinate units.
17. **The unbound map that should not move a bound rung.** A deferred binding that
    supplies one rung is unbound at a business that bound a different rung at ignition.
    Expected: that rung removed, the bound rung retained, the narrowing named. Failure:
    every figure dropping to the floor.
18. **The cold population.** No entity has a prior assessment. Expected: cold detected and
    the firing test named, no WIN, MISS or FLAT anywhere, NO BASELINE printed, rungs
    re-evaluated, and absolute build, plan attainment and execution-against-denominator all
    reported. Failure: a WIN label, or an empty report.
19. **The self-built denominator.** The eligible population is being created by the same
    work being scored. Expected: the share rung struck, the firing figure named, claim
    strength capped at bounded. Failure: a share near one hundred percent shipped at
    achievement strength.
20. **The status collision.** Under FLOW, one column headed with a generic status stem
    carrying stage values. Expected: neither concept resolves, the header is reported as
    ambiguous with both candidates named, and both the exclusion and the stage cuts are
    skipped and named. Failure: the exclusion silently removing a stage while the funnel
    reconciles.
21. **The universal gap.** A requirement classified GAP for the whole eligible population
    at a population above the ranking floor. Expected: Step 2 re-read once, then the gate
    asks. Failure: a scope-wide crisis published without a question.
22. **The externally authored requirement the entity affects.** A requirement published by
    a regulator or accrediting body whose compliance the reader's own actions move.
    Expected: SCORED, and appearing on the worklist when it fails. Failure: shown, a pass
    rate over a minority of the set, and a near-empty worklist that reads as an all-clear.
23. **The mostly suppressed set.** More than half a requirement set routes to
    shown-never-scored. Expected: the run stops and says so on the front panel before the
    pass rate, naming n of m and each suppressed requirement with its finding. Failure: a
    pass rate published as though it covered the standard.
24. **The internal restatement that drifted.** An internal document omits, pauses or
    contradicts an externally authored requirement still in force. Expected: the external
    requirement scored, both documents named with their dates, the discrepancy on the
    front panel. Failure: the requirement greyed, retired or silently amended.
25. **The full column.** A targeting, eligibility or not-actionable field blank on every
    row or populated on every row. Expected: NOT PRESENT, the rule not applied, every
    affected cell unassessable, and the column named in the audit. Failure: a wall of red,
    a wall of grey, or a whole population excluded and reported as an empty scope.
26. **The person-bearing level.** A scope chain whose level below the reader is individual
    people, with the peer distribution bound at ignition to that level. Expected: the level
    selects and attributes; the peer figure ships as an anonymous distribution with its
    count; no rollup, rank, sort or named comparison by person anywhere; condition 6 of
    3b.6 passes. Failure: a table of named individuals ordered by conformance rate.
27. **The mixed requirement.** An influence finding true for a proper subset of the eligible
    population. Expected: the subset suppressed with `BLOCKED_EXTERNAL` and an owner who is
    not the reader, the complement scored and appearing on the worklist, both counts
    published. Failure: the whole requirement routed either way, and one half of the
    population either given a red it cannot close or losing a real to-do.
28. **The inverted gap reason.** A standard whose met-condition is phrased as an absence.
    Expected: the cell reads as the finding, with the code first and the requirement
    introduced as the requirement. Failure: a cell that reads as a pass while quoting the
    standard accurately.
29. **The period that has not started.** A window opening after the run date. Expected: the
    period state named before any figure, a readiness rate rather than a conformance rate,
    no movement label, and the question asked once where INTERACTIVE is present. Failure: a
    conformance rate published for a period nobody has lived through yet.
30. **The undated evidence.** A source with no refresh timestamp and rows with no evidence
    dates. Expected: the age ladder walked, the rung used named, the age printed as unknown
    where it is, cells classified on presence with the requirement marked recency-untested.
    Failure: an omitted age line, an invented date, or every cell defaulted stale or fresh.
31. **The survivor-only prior file.** A prior-period extract containing only entities still
    present. Expected: the exit test run first, zero exits diagnosed and explained, retention
    reported as not computable, same-entity movement published only beside whole-population
    movement, no ranking on it. Failure: one hundred percent retention reported as a result.
32. **The level with no rate.** A peer comparison on a conformance level with no prior
    period. Expected: the level delta in points of conformance with the member count, no
    label because the rung-3 band cannot be computed, and the unit named. Failure: a growth
    delta reported where no growth exists, or the figure suppressed entirely.
33. **The uneven blocked share.** A peer comparison where the non-attributable share varies
    widely across the comparison population. Expected: three shares published, the delta
    computed both ways, the attributable delta published as the comparison, and the
    difference named as the part of the gap that is mix. Failure: one delta, published as
    though it measured the reader's work.
34. **The near renewal below the severe account.** A worklist whose rank-6 entity is due in
    days and whose rank-4 entity is due in months. Expected: both keep their severity rank
    and their place on the list, and the reader reaches the imminent one in one click by
    filtering the urgency column, per 5.5. Failure: the list reordered by date; the imminent
    entity cut by the cap because the cap now runs on the date axis; or a near-term BLOCK
    written above the table, which breaks element 1 and is why 5.5 makes it a column.
35. **The element nobody built.** A formatting element that applies to a section and was
    never attempted. Expected: NOT IMPLEMENTED, which fails. Failure: recorded not
    applicable with no reason, and counted as a pass.
36. **The unbound value list with a resolved column.** A status column resolves from the
    seed dictionary and the organization never bound the value list. Expected: the exclusion
    RUNS against the seed values under whole-token matching, with all three guards applied
    and every distinct value named as excluded or kept. Failure: no exclusion, on the
    grounds that the binding was absent.
37. **The five thousand entity scope.** A scope far larger than `REFERENCE_CAP`. Expected:
    every entity retrieved and classified, the census sheet written to the cap, the showing
    note on the sheet and in Method agreeing, and two separate reconciliations on the front
    panel, one for retrieval and one for rows written. Failure: five thousand rows, or a
    silent cut with no note.
38. **The workbook with no filter.** Any entity sheet built without an autofilter spanning
    every column, or without a rank column in first position, or without a reason-for-rank
    column. Expected: the verification fails and publication is blocked. Failure: a
    workbook a reader must re-sort by hand.
39. **The title in row 1.** A build that writes the report title, the scope or a caveat
    above the header row of an entity sheet. Expected: element 1 fails, publication blocks,
    and the title is moved to the front panel. Failure: a broken freeze pane, a broken table
    range, a dead autofilter and a header lookup that returns a caption.
40. **The two rankings compared.** The same entities ranked by this skill and by the
    planning skill. Expected: different orders, and both artifacts saying what their basis
    is. Failure: an attempt to reconcile them, which turns this skill into a second work
    plan.
41. **The row with nothing wrong.** An entity with no non-pass cell. Expected: the
    `HDR_FAILS` count zero, the `HDR_NARRATIVE` cell reading `no open items`, and the row
    still present in the census. Failure: an empty narrative cell, or the row dropped.
42. **The standard that never says what counts as evidence.** A published standard stating
    a met-condition for every requirement and an evidence rule for none, with
    `SOURCE_AUTHORITY_MAP` unbound and `INTERACTIVE` absent. Expected: B1.1 step 3 classifies
    each requirement from what its own met-condition describes, the classes are recorded with
    the step that decided them, and the conformance rate is computed over the cells that
    class permits. Failure: every requirement tagged at the weakest class, every cell
    UNASSESSABLE, and a conformance rate of zero percent published for an organization whose
    figure is not zero, with every gate passing.
43. **The wall of amber.** A provenance decision that would make more than half the scored
    cells UNASSESSABLE. Expected: `provenance_unassessable_unconfirmed` fires before Step 5
    builds anything, with both counts named; under a non-interactive run the artifact ships
    bannered with the question at the top of the front panel above every rate. Failure: an
    internally consistent, fully verified artifact reporting a scope-wide result nothing
    tested, because the reconciliation gate watches for red and this is amber.
44. **The top-of-chain reader holding a target.** A requester at the coarsest level of the
    chain, a cold population, `COUNTERFACTUAL_AVAILABLE_RUNGS` unbound, and a document
    already read this run stating a numeric target for a scored requirement, authored before
    the window by somebody other than the reader. Expected: rung 4 available as DERIVED at
    medium confidence, the label computed, the document's title, date and author printed
    beside the figure, and the derivation written to the provisional record. Failure: the
    most senior reader in the organization receiving no second number at all while the run
    holds the target in its hand.
45. **The blocked subset sentence.** A requirement with a proper subset routed to
    `BLOCKED_EXTERNAL` under 4.4b step 5's first branch. Expected: the published sentence
    says the requirement is scored on ALL eligible entities and says which of them the
    reader can close and which the named parties can, and it agrees with the conformance rate
    printed beside it. Failure: a sentence saying the subset was suppressed, contradicting a
    rate computed over the whole eligible population.
46. **The sheet with no elapsed-time column.** An entity sheet carrying no elapsed-time
    column, so element 13 cannot apply. Expected: NOT APPLICABLE with element 13's own stated
    reason, which is a qualifying reason under 5.8 member 4 and member 5, and the workbook
    publishes. Failure: NOT IMPLEMENTED, which blocks publication of a workbook with nothing
    wrong with it.
47. **The census and its extract.** A workbook whose tab 2 repeats seventy identifiers from
    tab 3 at the same rank numbers. Expected: R2 recorded NOT APPLICABLE with its scope as
    the reason, because it is scoped to merit tier sets, and R4 read in its census form.
    Failure: a duplicate-identifier assertion run between a census and an extract of it,
    failing a correct workbook, or the extract re-ranked from 1 so one entity carries two
    different ranks in one bundle.
48. **The window that has not opened.** A run whose operating window opens after the run
    date. Expected: the period state NOT YET STARTED published before any figure, all three
    rates carrying the labels 3.5.1 gives them, each defined on the front panel and in the
    Legend, no movement label of any kind, and the `overdue` state computed against the
    window's opening date and not against the run date. Failure: a conformance rate published for a
    window that has not opened, two of the three figures published under names 3.5.1 forbids,
    or an urgency column that moves with the hour the report was produced.
49. **The unmatched unit.** A unit in the scored population with no row in the evidence
    file joined under 3.2.1. Expected: the unit keeps its place and its rank eligibility,
    every joined column is blank for it, every cell of its row is
    `? UNASS: no evidence captured this period`, it is counted in the assessability rate
    and excluded from both conformance denominators, and the match rate and both unmatched
    counts are disclosed. Failure: the blank read as a zero, the row scored GAP across the
    board, and a compliant unit published as the worst entity in the scope.
50. **The refused join.** An evidence file whose identifier resolves but is not unique on
    its own side, or resolves only by name similarity. Expected: no join, the file recorded
    READ AND NOT JOINED in those words, the failed precondition named, and every requirement
    that file would have scored named as unevaluated with `? UNASS: no evidence source
    mapped`. Failure: a one-to-many join that multiplies rows of the scored population, or a
    fuzzy key that matches the wrong units and reconciles perfectly against itself.

51. **The presence-only pass on a recency condition.** An evidence source with no per-row
    capture date, scored against a standard two of whose met-conditions carry a recency
    clause of their own. Expected: every pass on every recency-untested requirement reads
    `+ PASS (presence only, recency untested)` in the cell, the two requirements with a
    recency clause are named one by one on the front panel and in the Legend with their own
    wording quoted, and no rate moves. Failure: 247 cells published as an ordinary pass
    while the disclosure sits in a Legend that a filter, a sort and a paste all discard.
52. **The met-condition that describes two classes.** A requirement whose met-condition is a
    signature by the party being scored, so step 3's bullets match both SYSTEM EXTRACT and
    ATTESTATION, on a run whose evidence arrives through a joined system extract. Expected:
    B1.1 step 4 takes ATTESTATION, the weaker of the two the description supplies; the layer
    actually read is disclosed under B4 and raises nothing; every pass reads
    `+ PASS (attested)`; and where the standard requires observation the cells are
    `? UNASS: attested only, standard requires observation`. Failure: every ambiguous
    requirement resolved to SYSTEM EXTRACT because that is the layer the run read, which
    makes B2's asymmetry unreachable on every run this skill performs.
53. **The compliance target written as zero.** A top-of-chain reader, a cold population,
    `COUNTERFACTUAL_AVAILABLE_RUNGS` unbound, and a qualifying target already read this run
    that reads "no unit should carry an open service item". Expected: rung 4 available and
    DERIVED, the finding shipped as a COUNT AGAINST THE TARGET with its denominator
    population and the document's title, date and author, no ratio, no band label, the
    absence of the label printed as a stated absence, the finding recorded as PAIRED, and
    A8's second cold finding reported as answered. Failure: the guard striking the rung, the
    most senior reader receiving rung 6 with a bare denominator, and a mandatory finding
    reported as blocked on a run holding the target in its hand.
54. **The overdue row nobody can act on.** A row whose commitment date fell before the window
    opened and whose only gap is `BLOCKED_EXTERNAL`. Expected: the row takes
    `passed_nothing_outstanding`, its blocked shortfall is carried by the `HDR_BLOCKED`
    count, and the urgency filter returns only rows carrying work this reader can do.
    Failure: the row published as overdue, so the one filter the reader clicks disagrees
    with the ranking basis and the worklist rule, which both exclude the same cell.
55. **The two windows.** A run whose calendar-resolved operating window and whose evidence
    source's own period stamp name different windows. Expected: the comparison run and
    stated whatever the result; where the resolved window was derived, the stamped window
    governs; where it was read from a published or bound source, the bound value governs;
    both windows named on the front panel with which governed and why; and the count of rows
    whose urgency state differs between the two readings printed. Failure: either window
    taken silently, which is indistinguishable from a correct run.
56. **The verification that read its own record.** A workbook whose method sheet carries
    R5's record naming the unit nouns R5 searched for. Expected: the matrix range declared
    and stated on the method sheet, R5 excluding that range and saying so in its own record,
    element 16 still scanning it, and the gate passing with the searched terms visible.
    Failure: a run that recorded its evidence blocked while a run that hid its evidence
    published.
57. **The uncapped reference table.** A Summary of thirteen rows and a Legend of fifty-nine
    under a cap of five hundred. Expected: both ship `showing n of N` with `n` equal to `N`,
    both reconcile in Method, and R3 has something to read on each. Failure: no note on
    either, on a reading of "capped" that means cut rather than subject to a cap.
58. **The extract that says nothing about the census.** A seventy-row extract of a hundred
    and ninety row census, holding its full declared size so no shortfall note fires.
    Expected: `showing 70 of 190` in the extract's note band, with `N` the census's own unit
    row count per PART 5.1.1, reconciled in Method. Failure: a reader opening the first grid
    in the workbook, seeing seventy rows, and acting on a fifth of their book.
59. **The frozen span that fills the window.** An entity sheet whose identity block's summed
    built width exceeds `FROZEN_SPAN_MAX_WIDTH`. Expected: the walk stops at the last
    identity column that fits, the first column is frozen regardless, nothing is moved,
    narrowed or dropped, the reason column still follows every identity column and is
    outside the span, and the truncation is recorded on Method. Failure: seventeen of
    twenty-one columns pinned, so scrolling right reaches nothing, or a column narrowed
    below its own header floor to make the span fit.
60. **The status grid that carries a sentence.** A build that centres the requirement columns
    while their cells hold the standard's own wording. Expected: 2.5's three conditions
    tested, condition 3 failing on the longest value, the columns left aligned, the wording
    carried in the narrative column, and element 9 verifying clean. Failure: 1520 centred
    cells failing element 9 and blocking publication of a workbook whose only defect was an
    instruction it obeyed.
61. **The colour with two meanings.** A workbook carrying an elapsed-time column and a status
    grid. Expected: the classification palette disjoint from `COLOR_ALERT_WARN` and
    `COLOR_ALERT_OVERDUE`, any state with no lawful fill carrying none and named in the
    Legend, and at most one fill per cell with the alert fill governing a collision.
    Failure: an approaching deadline and an unassessable cell painted the same colour on one
    grid, with nothing in the artifact to tell a reader which meaning is which.
62. **The grid that could never be coloured.** A run under the standing bindings, whose
    shortest gap cell is fifteen characters against a centring bound of twelve. Expected: the
    requirement columns declared CLASSIFICATION COLUMNS under 2.6, left aligned under 2.5,
    every state carrying its fill from `CLASSIFICATION_FILLS`, and the Method sheet recording
    that the centring test decided alignment only. Failure: 1520 status cells shipped
    monochrome, correctly under a rule that hung the fill on the centring bound, on a run
    that could not have coloured a single cell under any binding of any organization.
63. **The two states that read alike.** A build assigning NOT REQUIRED and RETIRED one fill,
    or any two states of `CLASSIFICATION_VOCABULARY` one fill. Expected: verification row 13
    fails on injectivity and publication is blocked, and the repair is a distinct fill or a
    state carrying none and named in the Legend. Failure: four answers shipped as three
    colours, with the fourth unrecoverable by any reader.
64. **The cell the resolution rule cannot place.** A populated requirement cell that does not
    begin with a state's own symbol and code. Expected: the cell reported unmapped and routed
    to `BINDING_OWNER_NAME`, the column NOT declared a classification column for that build,
    and the whole column shipping with no fill and the Legend saying so. Failure: the cell
    filed under the nearest state, which asserts something nobody checked, or a fill applied
    from a rule that is not total.
65. **The top-of-chain reader holding a target.** A Principal at the coarsest level of the
    chain, a cold population, `COUNTERFACTUAL_AVAILABLE_RUNGS` unbound, and one qualifying
    target read from an internal document authored by a subordinate and addressed to that
    reader. Expected: A5.2's condition 4 satisfied on the authorship test, the commissioning
    half tested against the document and not against the reporting line, rung 4 DERIVED, and
    A8's second cold finding satisfied. Failure: the rung struck a second time by the clause
    written to save it, and the most senior reader in the organization handed a bare
    denominator.
66. **The grid ten screens wide.** A census whose summed built width exceeds
    `GRID_MAX_TOTAL_WIDTH`. Expected: the bound read before the columns were built and
    recorded, 2.7's ladder run in order with the standing qualifier already in the Legend
    against its code, every width recomputed from 2.2, and either a grid inside the bound or
    an honest overage recorded with the columns that account for it. Failure: a column
    dropped, a header narrowed below its floor, a meaning-carrying value shortened, or the
    bound raised after the measurement to clear the row.
67. **The two tabs that freeze differently.** A workbook whose entity sheets and reference
    tables carry the same identity block, one of them holding no value in its name column.
    Expected: the span walked ONCE from the widest case, the same identity columns frozen on
    every tab, the narrower sheet freezing them in fewer width units, and ONE truncation
    record for the artifact. Failure: three columns pinned on one tab and five on the next,
    every sheet individually conformant, six records of one identity block, and a reader who
    cannot say where the pin is.
68. **The Summary that could not be built.** A Summary required to carry about fifteen
    columns for which the schema names three header variables. Expected: every header with a
    variable read from it, the rest defaulted in plain language under PART 8's scoped rule,
    the count and the list of defaulted headers recorded in Method and raised as a schema
    request, and no column dropped. Failure: the sheet unbuildable, or the columns dropped,
    or literals shipped with nothing disclosing them.
69. **The reference table asked for its unit rows.** A Summary of eleven rows and a Legend of
    sixty-four, on sheets whose rows are requirements and codes rather than units of
    business. Expected: both ship `showing n of N` counting the sheet's own DATA rows, both
    reconcile three ways, and the reading is stated. Failure: `showing 0 of 0` on two sheets
    that visibly hold rows, reconciling zero against zero and passing.
70. **The reply that published two rates.** A reply naming the conformance rate and the
    assessability rate. Expected: all three of A4's rates in the reply with the difference
    between the first two printed. Failure: a compliance figure quoted onward with no
    attributable figure beside it, understating what the reader can actually move; measured
    at 3.7 percentage points on one run, produced entirely by two counterparties.
71. **The front panel that buried its own title.** A run where every requirement is
    recency-untested and several carry a recency clause. Expected: the report title, the
    scope and the period first; the period state, both mandatory disclosures, the denominator
    statement and ONE counting line above the rates; the rates; then the per-requirement
    enumeration in full below them. Failure: nineteen rows of qualification before the panel
    says what report the reader is holding.
72. **The exclusion nobody reconciled.** A standard opening with an entity-class scope of its
    own, and a status column the not-workable exclusion also reads. Expected: both
    populations resolved, the three numbers published on the front panel and in Method
    including a disagreement count of zero, and any disagreeing entities named. Failure: a
    seed value set that excludes a class the standard still counts, a clean funnel, an
    eligibility test with nothing left to mark, and no number anywhere moving.
73. **The clause that could not be tested.** A met-condition carrying a clause neither pass
    qualifier describes, such as a date the evidence is a bare flag for. Expected: the hole
    reported on the front panel and in the Legend with the clause quoted and the evidence read
    in its place named, routed to `BINDING_OWNER_NAME`, no third qualifier invented and
    neither existing one stretched, and nothing written into the status cell. Failure: a
    sentence in a status column, which 4.1 step 9 and 2.6's total resolution rule both
    forbid, on a route the same file mandated.

## Live-run remediation, fifth pass

- **The tier-size statement is rewritten as shorter RELATIVE TO SPAN**, with the
  senior line's pair named as the larger pair in absolute rows, matching SD-RNK-09
  and the schema default.

## Live-run remediation, sixth pass

Every item below came out of one end-to-end run against a real standard and a real book,
and each is recorded so nobody reintroduces the sentence that caused it.

- **The provenance procedure replaced "the weakest class that fits".** B1.1 is an ordered
  procedure and the undefined word is gone; B1.2 is the tripwire that catches a
  classification decision producing a scope-wide unassessable result, and
  `provenance_unassessable_unconfirmed` in G2 is what fires. The rule the old sentence
  existed to enforce is stated in its own words in B1.1 and is not weakened.
- **A5.2 stops a documented default deleting a rung the run has evidence for**, which
  matters most for the reader at the top of the chain, who has no other labelled figure.
- **4.4b step 4's mandated sentence is branch-dependent**, because the unconditional
  version was false under step 5's first branch and contradicted the rate printed beside it.
- **Every column header is a variable.** `HDR_COMMITMENT_DATE`, `HDR_URGENCY`, `HDR_FAILS`,
  `HDR_BLOCKED`, `HDR_UNASSESSED`, `HDR_RANK_REASON` and `HDR_POSITION`, with
  `HDR_PRIORITY_BAND` removed from the position column it was never meant to head.
- **Each sheet declares its class and, where ranked, its kind**, in 5.1, which is what makes
  R1 through R5 resolve without a reader working it out, and the local defence of the
  extract is deleted because the contract now carries it.
- **5.8's closed set of not-applicable reasons has five members**, the fifth being the
  element's own stated exemption, which is what keeps the set total as the contract changes.
- **5.10 routes every per-sheet note to the note band** the contract defines, and this file
  states no placement of its own.
- **3.5.1 renames all three rates under a window that has not opened**, and A4 grants the
  exception explicitly so Part A is not contradicted by a later step.
- **5.5 anchors the `overdue` state on the window's opening date, never the run date**, and
  states that the test is per row on any unmet requirement.
- **The ignition set is ten organization variables.** `BINDING_OWNER_CONTACT` is DEFERRED.
- **F1 cites the two rules that govern a first run with no interactive channel** rather
  than leaving a reader to attempt an interview that cannot run.
- **One output-contract bullet, not two**, and every citation of that file is by filename.
- **3.2.1 wires SD-PRS-48 into evidence resolution.** The join of an evidence file onto the
  population on the unit identifier had no rule behind it and this skill does it every run.
  Four preconditions, both unmatched sides reported, the row count asserted before and
  after, the enrichment disclosed, and the READ AND NOT JOINED path where a precondition
  fails. The ladder interaction is made explicit at 4.1 step 8: an unmatched unit has no
  capture and is UNASSESSABLE, never a gap, which is the blank-versus-fail conflation
  Part A exists to prevent.
- **A5 reads the LEVEL DELTA band.** `DEADBAND` is keyed per rung and per quantity form,
  and a conformance level compared against a comparator level is a fourth unit, so rungs 3
  and 5 no longer emit an unlabelled figure for want of a prior period (SD-CLM-34).
- **A5.2 guards a target of zero**, which is the one divisor no population guard sees
  (SD-POP-18).

## Live-run remediation, seventh pass

Every item below came out of a second end-to-end run against a real standard and a real
book, and each is recorded so nobody reintroduces the sentence that caused it.

- **A pass that rests on weaker evidence says so in the cell.** A3 carries a CLOSED pair of
  pass qualifiers, the attested one from B2 and the presence-only one from 3.5.2, and a
  Legend line is never a substitute for either.
- **B1.1 step 4 takes the WEAKER of the classes the met-condition describes**, and the layer
  B4 names can lower a class and never raise one. The guarantee eleven lines below it and
  the step now say one thing, and the step descends nothing.
- **A5.2's zero target yields a COUNT AGAINST THE TARGET**, paired, unlabelled and honest,
  and it SATISFIES A8's second cold finding rather than blocking it. The guard against a
  division is no longer a reason to delete the two numbers that need none (SD-POP-18).
- **The reason-for-rank column is the first column after the identity columns**, which is
  the contract's one position for it, and the frozen span is bounded by
  `FROZEN_SPAN_MAX_WIDTH` with the truncation recorded on Method.
- **The standard's own wording moved from the status cell to the narrative column**, which
  bounds the grid's width, keeps the requirement columns eligible for a status-grid
  declaration, and puts a fact about the requirement where facts about requirements live.
- **The classification fills are disjoint from the alert palette**, and a state with no
  lawful fill carries none and is named in the Legend rather than borrowing a colour that
  already means something else (SD-FMT-27).
- **Status columns are centred if and only if they qualify under 2.5**, tested at build
  time on the values actually written, and never bought by shortening a cell (SD-FMT-05).
- **The urgency column reads `URGENCY_VOCABULARY` by state key**, five keys and no prose
  list, and its `overdue` state runs on ATTRIBUTABLE gaps, so the filter, the rank and the
  worklist say the same thing about the same cells.
- **3.5 compares the resolved window against the evidence's own period stamp**, states which
  governed under S9's precedence, and prints the count of rows the choice moved.
- **The method sheet declares the cell range its verification matrix occupies**, so a
  string-searching row can record what it searched for without failing itself.
- **Every bounded sheet ships its showing note**, the extract included, with `N` read from
  PART 5.1.1's table for that sheet's own bound; capped means subject to a cap, never cut
  by one.
- **The Summary's two kinds of row are two labelled blocks under one position sequence**,
  each ordered by conformance rate ascending, with the kind carried in the reason-for-rank
  cell and the structure stated in the ordering note.
- **5.3 names the commitment-date column by its variable in every sentence**, the last
  retired literal having been deleted from the one place it survived.

## Live-run remediation, eighth pass

Every item below came out of a third end-to-end run against a real standard and a real book,
and each is recorded so nobody reintroduces the sentence that caused it.

- **The classification fill no longer hangs on the centring test, and this is the change that
  makes the workbook the description promises reachable at all.** 4.6 declares the
  requirement columns CLASSIFICATION COLUMNS under reference/output-contract.md 2.6, publishes
  `CLASSIFICATION_VOCABULARY` and a TOTAL mechanical rule from a cell to exactly one state,
  and leaves the columns LEFT ALIGNED, which they are and which is now expressly fine. Under
  the old text no organization and no binding could ever have produced a lawful fill on this
  grid, because A3 and 4.2 fix the vocabulary and its shortest member already exceeds the
  centring bound. 1520 status cells shipped monochrome, correctly, on a workbook sold as
  colour-coded (SD-FMT-27).
- **`CLASSIFICATION_FILLS` is injective and NOT REQUIRED no longer shares a fill with
  RETIRED.** Two states counted differently, excluded differently or cleared by different
  people are never given one colour however alike they read.
- **`COLOR_STATUS_GAP` and `COLOR_STATUS_UNASSESSABLE` exist and are bound**, and both the
  4.6 table row and the I1 sentence saying otherwise are deleted, along with the claim that
  they were the only thing blocking the fill, which was wrong twice.
- **A5.2's condition 4 is SD-CLM-04's condition and nothing more.** The scope clause was
  unsatisfiable for the top-of-chain reader the section is written to protect, because every
  internal author sits inside that reader's scope by definition. The real concern is stated
  as its own test, read from the document rather than from the reporting line: a target the
  reader commissioned is theirs, and a target ADDRESSED to them is somebody else's (13-D7).
- **A3's pass qualifier is a bound lookup, not two strings in Part A.**
  `PASS_QUALIFIER_VOCABULARY` exists; this file names the two keys and writes neither label.
- **A3's qualifier WORDING moved to the Legend against its code, which is 2.7's first rung.**
  The mark stays in every cell, so a filter, a sort and a paste keep it; the fifty-character
  sentence stops being repeated across fourteen columns of every row. The Legend row is
  mandatory and verified (14-D9, SD-FMT-28).
- **The grid's total width is bounded, measured and recorded.** 5.3 reads
  `GRID_MAX_TOTAL_WIDTH` before the columns are built, never raises it, runs 2.7's ladder, and
  ships an honest overage with the columns that account for it where the grid is still over.
- **The frozen span is walked ONCE for the artifact from the widest case**, applied by header
  name everywhere, with ONE truncation record for the workbook, so the pin lands in the same
  place on every tab (SD-CTR-08).
- **A3 no longer requires an untested met-condition clause to be written into the cell**,
  which 4.1 step 9 and 2.6's total resolution rule both forbid. The hole is named on the front
  panel and in the Legend, per requirement, with the clause quoted.
- **5.6 takes PART 8's SCOPED header rule**, so the Summary can be built: a literal is lawful
  only where no variable names the column, every one is counted and named in Method, and the
  variables are requested in I1. Under the flat prohibition the sheet could not be built at
  all.
- **5.10 says what `n` and `N` count on a sheet whose rows are not units of business**, which
  is the Summary and the Legend, and raises the contract's wording as a shared item rather
  than resolving it locally.
- **Step 6 publishes all three rates**, which A4 and H1 both required and which item 3 named
  two of.
- **5.2 puts the report title, the scope and the period FIRST**, keeps the three statements
  that change how a rate is read above the rates, and moves the per-requirement recency
  enumeration below them with a counting line above.
- **4.1 step 1 reconciles the not-workable exclusion against the standard's own entity-class
  scope** and publishes the three numbers even when the disagreement is zero.
- **3.2.1 carries the second half of SD-PRS-48**: a join that lands and resolves nothing has
  moved the failure, and the one-column-per-requirement shape resolves through the declared
  sibling set in reference/field-resolution.md 7.4b.
- **B2 routes an attestation that a resolved column contradicts to SD-CNF-10**, which is a
  third state with its own remedy and where neither side wins automatically.
