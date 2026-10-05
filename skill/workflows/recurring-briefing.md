---
name: recurring-briefing
description: |
  Delivers a short, act-on-it briefing on a schedule, to one person, without being
  asked. Two loops at different cadences: a cheap delivery loop that assembles the
  next period's briefing from content prepared in advance, and an expensive rebuild
  loop that refreshes that content from source. Every line states which source it
  came from and how fresh that source is, and content carried forward from a previous
  rebuild is labelled as carried rather than presented as current. Use when someone
  asks for a daily or weekly brief, a morning rundown, a route or call-day guide, a
  standing digest, a shift handover, a watch list that arrives on its own, or says
  they want something emailed to them every morning instead of having to go and ask.
  Fits field visit schedules, service and installation routes, case and caseload
  queues, shift and ward handovers, account coverage days, dispatch boards and
  standing operational digests. Scope is always the recipient's own work. Do not use
  to build a ranked plan for a period (period planning), to score a population
  against a standard (standard gap scorecard), to write a review (objectives and
  review), or to deliver anything to anybody other than the person who set it up.
---

# Recurring Briefing

Deliver the next period's work to one person, on a schedule, in a form they can act on
from a phone before they start. Say what each line came from. Never let content that
was carried forward read as content that was just rebuilt.

This skill is one of the workflows that share one configuration. It reads:

- reference/schema/ for every variable name used below. No employer literal appears in
  this file; every literal lives behind a bound name.
- reference/binding-interview.md for how an unbound value behaves. IGNITION is the ten
  organization variables. Everything else is DEFERRED and is requested at the moment a
  decision needs it, from a person who would know, once.
- reference/doctrine/ for the shared rules. Rules are cited by ID and never restated.
- reference/output-contract.md for the universal output contract. **This workflow
  introduces a fourth output medium, the scheduled message, which the contract does not
  yet key.** Part J states what the medium requires and what must be added to the
  contract before this workflow ships. Until that is added, this file is the interim
  authority for the medium ONLY, and the contract governs everything else.
- reference/capability-probe.md for what the environment can do, and it settles more of
  this workflow than a first reading suggests. **`INTERACTIVE` is already defined there as
  ABSENT for a scheduled or unattended run, and ladder 2.14 rung 2 is already declared the
  correct behaviour for one.** Part A3.1 states what that means for the two loops. Two
  capabilities genuinely do not exist in that file and are added by
  work/capability-probe-patch.md: `SEND` and `SCHEDULER`. **`MAIL` PRESENT does not imply
  a send channel**; MAIL's probe lists folders and reads messages, and its whole ladder is
  about reading.
- reference/field-resolution.md for finding a concept inside a file this skill has
  never seen. Invoked, not duplicated.

## Why this workflow is shaped differently from the other three

The other three workflows are asked for. Somebody types a request, waits, and is present
when the artifact arrives. They can see a refusal, read a degradation notice, and decide
whether to act.

This one arrives unasked, at a fixed hour, to somebody who is holding a phone in a parking
lot and has ninety seconds. **The burden of proof inverts.** A requested artifact may say
"I could not determine this" and rely on the reader to absorb it. A scheduled artifact is
acted on without being audited, so it must either be current or must say so loudly enough
that a person skimming on a phone cannot miss it.

That single asymmetry generates most of what follows: the four freshness states, the rule
that the delivery loop never computes, the rule that a failed rebuild sends a short notice
instead of partial content, and the rule that nothing is ever sent to anyone but the
person who set it up.

## How to read this file

| Part | What it settles |
|---|---|
| A | The contract. The five source states including the one only this workflow can see, the two loops and their INTERACTIVE split, the one recipient, and what a briefing is allowed to assert |
| B | Source provenance: the ladder, the drift comparison that runs before it, why a failed identifier never widens, and what this workflow owes the shared dictionary |
| C | The workflow. Five stages, 0 to 4, in an order declared authoritative |
| D | Cadence and shape: delivery period, rebuild period, and what varies by role |
| E | Degraded runs. The rungs this medium reads, the two capabilities the probe does not have, and the one place the three-place announcement rule does not fit |
| F | Bindings requested at the point of need, keyed by the decision that needs them |
| G | Hard gates. What stops a send |
| H | Guardrails, restated for checking |
| I | What this workflow declares: its bindings, its doctrine, its regression cases |
| J | The scheduled message medium, pending its addition to the output contract |

**Precedence when a rule appears more than once.** Same convention as the other workflows:

1. **Part A governs everything.** It is the declared contract in the sense of SD-CTR-01,
   and any later instruction that disagrees with it is the defect.
2. **The numbered stage is normative** for how something is done.
3. **Parts H and I are restatements for checking, never sources.**
4. **A cited doctrine ID governs over this file's paraphrase of it.**

**The decision index.**

| To decide | Read |
|---|---|
| What freshness state one source carries | B1 for the ladder in order; B2 for what each state permits a line to assert; A2 for the five states |
| Whether a briefing may be sent at all | Part G, and nothing else. G0 for the convention and the six-field record, G1 for the records, G2 for what each one is for |
| What the delivery loop is allowed to do | A3; 3.1 for the assembly rule; the delivery loop never computes and never reads a source |
| What happens when a rebuild fails | A4; 2.7 for the atomic swap; E3 for the notice and its two-line form |
| Who may receive a briefing | A5; G2; the recipient is the person who set it up and the binding is never widened |
| What one stop or item carries | 3.2 and the item content standard; A6 for what may not appear |
| Whether to rebuild now or carry | 2.1 for the trigger test; D2 for the rebuild period |
| What the reader sees when a source is absent | B2; the named-absence string, never a blank and never a guess |
| Whether a scheduled run has the permissions it needs | 1.5; E1; 2.16 rung 2; permissions are granted while a person is present or the schedule is not created |
| Whether a source has drifted, and what that permits | A2.0 for the state; B1 rung 0 for the comparison; B2 for what it permits; G-RB-9 |
| What this workflow owes the dictionary | B6; field-resolution 7.5 criterion 5; it proposes and never promotes |
| Why an unresolved identifier is not merely inconvenient | B4; F5.6; G-RB-10 |
| Whether a carried value is legal at all | A2.1 for the carve-out from capability-probe 4.4; G-RB-6 for the gate that keeps it legal; SD-SRC-18 |
| Whether a banner may be softened after several periods | A2.2; G-RB-7; capability-probe 4.4. It may not |
| Which capability ladder this workflow reads | E6; P1c; 2.15 and 2.16 only |
| Where a degradation is announced | E7; capability-probe 4.1 with this medium's adaptation |
| How a date is written, and at what precision | M13 and J2; DATE_FORMAT_DAY, DATE_FORMAT_MONTH, DATE_FORMAT_WEEKDAY; G-RB-11 for the one half of it that stops a send |
| Whether a person may appear in a briefing, and in what shape | A5.2; A5.2.1 for the detection; A5.2.2 for attribution; A5.2.3 for the four prohibitions; A5.2.4 for what replaces each; G-RB-14 for the interlock |
| Why this workflow draws no comparison between people | A5.2.4; A1.1 leaves it no second number, and both anonymity floors are unreachable in a span small enough to brief |
| Whether an action belongs in this reader's list at all | A5.3 and the claim tier; G-RB-15. Atoms for a direct-tier reader, shapes for an aggregate-tier one |
| What a second number means in this medium | A1.1. The workflow computes no performance figure, and a quoted one travels with the second number its source carried |
| Whether a filter on somebody's briefing is somebody else's briefing | A5.2.6. It is not, and the reason here is the banner, the tripwire denominator and the action cap, all computed over the whole span |
| Why a long briefing says a thing once rather than on every item | A5.2.4b; `MESSAGE_MAX_REPEATED_SHARE`; the split is per-item fact against standing explanation, and only the second moves |
| Whether a state is safely expressed | M15 and J2; G-RB-13; the state is in the characters and the styling is a second channel |
| Whether a verification result means anything | I5b; three states, and an unexplained not-applicable is a failure |
| Why a section is empty, and whether it should have been | A2.0b rule one; G-RB-12; a section resolves against its own source and against no other |
| Whether a source is really unresolved | A2.0b rule two; a second reading is attempted first, and a file that disclaims one of its own blocks resolves per block |
| Whether a count may be written into a sentence | M14 and J2; COUNT_NOUN_FORMS; SD-LNG-13; the three-value test gates the rebuild and not the send |

---

# PART A: THE BRIEFING CONTRACT

This part is the declared contract for this workflow in the sense of SD-CTR-01. Every
later instruction is subordinate to it.

## A1. The five governing rules apply unchanged

Carried from the doctrine because a scheduled artifact is where they are most often lost:

- **G1.** One declared contract per deliverable, superior to every other section.
- **G2.** Fail closed. Unknown is not pass.
- **G3.** Never default an unknown to the value that maximizes its score.
- **G4.** Every number carries a second number the writer did not choose.
- **G5.** A rule that costs nothing when it does not fire and keeps the method portable
  is worth carrying.

G2 bites hardest here. An unattended run that cannot determine something has no reader to
ask, so the failure mode is to print a confident sentence from stale data. The freshness
states in A2 exist to make that structurally impossible.

## A1.1. G4's form for this medium, which is a RESTRICTION rather than an apparatus

**A1 claims the five rules apply unchanged, and a claim with no mechanism behind it is the
shape this method exists to catch.** So G4 gets its form stated here, as the other three
have theirs: G1 in this Part's precedence, G2 in A2's states, G3 in the never-default rules
of B2 and M13.

The scorecard spends A4 and A5, roughly three hundred and twenty lines, working G4 out for
a grid: two rates that never ship alone, a third for comparison, the difference between
them printed, a rung that decides the arithmetic, a band per rung and per quantity form, a
mix test computed both ways. **None of that belongs here, and saying why is more useful
than importing it.**

**Most of what a briefing carries is a FACT rather than a FIGURE, and G4 binds a figure
presented as performance.** Five units on site is a count of things that are there. A work
order opened on a stated date is that date. Neither is a claim about anybody's work and
neither has a second number that would mean anything; demanding one would produce a
briefing full of denominators nobody reads, which is G5 failing in the opposite direction.

**A briefing CAN carry a performance figure, and there are three ways in.** The rule is one
restriction that closes all three:

> **This workflow computes no performance figure.** Where one arrives from a source, it
> travels with the second number that source carried. Where the source carried none, the
> figure is not quoted and the fact underneath it is.

1. **A planned-against-actual count.** Two visits planned against a period half gone is a
   figure about whether somebody is keeping up. The briefing prints the plan as the plan,
   per the wording rule in B2, and computes no attainment from it.
2. **A figure read from a source that is itself a plan or a scorecard.** This is the real
   case and the one a briefing meets first. The figure arrives already carrying G4's
   obligation, and **a briefing that strips a figure's second number in the act of quoting
   it has broken G4 on somebody else's behalf**, which is worse than never carrying the
   figure, because the original artifact was honest and the quotation is not.
3. **Any comparison to a previous period**, which A7's cold-start rule already handles by
   omission.

**Why a restriction is the right answer and not an exemption.** A briefing has no audit
section, no method sheet and no legend; it is ninety seconds on a phone. A rung, a band and
a mix test published into that medium would be a second number nobody can check, which
satisfies G4's letter and defeats it. **Declining to compute the figure at all is strictly
stronger than computing it badly**, and it costs the reader nothing they could have used,
because the artifact that is allowed to carry a performance figure properly is the one the
PLANNING and SCORECARD workflows already produce.

**What this buys elsewhere, stated because it does real work twice.** A5.2.4 rests on it:
with no second number there is no peer distribution to compute, so the hardest part of the
scorecard's person-bearing section has nothing to operate on here. And A7's cold start gets
simpler for the same reason, because a missing baseline costs a comparison this workflow
was never going to draw.

## A2. Five source states, and keeping them apart is the product

Every source feeding a briefing resolves to exactly one of five states. Not two, and not
the four this file carried before field-resolution.md was read. `SOURCE_FRESHNESS_STATES`
carries, per state, `is_current`, `permits_assertion`, `label_in_artifact` and
`requires_named_source`.

| State | Meaning | What the reader is entitled to conclude |
|---|---|---|
| CURRENT | The source was read during the most recent successful rebuild. | This reflects the world as of the last rebuild. |
| CARRIED | The source could not be read this rebuild; the last good copy is being used, and its own date is stated. | This was true as of a stated earlier date and may have moved. |
| ABSENT | The source has never arrived, or does not cover this item. | Nothing is known. The question is open, not answered no. |
| UNRESOLVED | The source arrived but could not be parsed or reconciled. | Something is there and could not be read. Somebody should look. |
| DRIFTED | The source read normally, and a concept that resolved last rebuild does not resolve now, or resolves to a different column. | The file is healthy and something upstream changed shape. The data below may be thinner than last period without being wrong. |

The load-bearing separation is CURRENT against CARRIED. Every scheduled briefing system
that loses trust loses it the same way: it keeps sending confident content after its
inputs went stale, the reader acts on a number that was true three weeks ago, and from
then on the reader checks everything manually, which is the whole value gone.

The second separation is ABSENT against UNRESOLVED, and it is SD-EFF-06 applied to whole
  sources rather than to cells. It decides who does what. ABSENT
is a gap in the world and usually means waiting. UNRESOLVED is a gap in the reading and
means somebody should open the file. Collapsing them turns a parser defect into a
shrug.

## A2.0. DRIFTED, and why only this workflow can see it

field-resolution.md F0.1 warns that the source is never the same shape twice: two exports of
the same file months apart differ on header row position, sheet count, the naming of the
same column, the measure basis, the identifier type. F0.4 turns it into a development
discipline, the portability test, run before shipping a dictionary change.

**For the other three workflows that is a discipline. For this one it is Tuesday.** A
briefing reads the same sources every period for years, so it runs the portability test
continuously whether anyone intended it to or not. And it holds something none of the others
hold: **it knows how each concept resolved last period.**

That makes a state visible that the four-state model could not express. A schedule feed
whose planned-start column was renamed upstream is not CURRENT, because the concept did not
resolve. It is not ABSENT, because the file arrived in full and on time and most of it
resolved fine. It is not UNRESOLVED, because the file parsed perfectly. It is certainly not
CARRIED. **The file is healthy and the concept moved underneath it**, and every one of the
four older states would have said something reassuring.

F5.5 already draws the neighbouring distinction and stops one short of this one: the column
is absent, against the value is not in it, which read identically and have different fixes.
DRIFTED is the third member of that family, reads identically again, and has a third fix
that is upstream and is usually somebody's export template.

**This is the most expensive failure available to a recurring artifact, and the expense is
entirely in how quiet it is.** The briefing keeps arriving. It keeps looking complete. One
section loses a dimension or the ordering reverts to feed order, and because it degrades by
one notch rather than breaking, nobody reports it. The deployment this workflow was
generalized from carries the lived version in its troubleshooting notes: a brief that said
it was running from the previously saved schedule every single day, for weeks, because an
upstream subscription had changed layout and the daily line saying so had become wallpaper.

**So DRIFTED is announced at banner prominence on first occurrence**, not as a per-line
label, because the entire failure mode is that it is easy to miss. It names both
resolutions, the one that held last period and the one in force now, which is the pair an
upstream owner needs and neither of which is recoverable later.

**Container drift counts.** F1.6 says a container named after a person is somebody's filtered
working extract. A source that was the real export for forty periods and is now a working
extract with a name on it is a drift event, not merely a lower-scoring container. The
briefing would otherwise run on one person's slice looking exactly as complete as last week.

## A2.0b Resolution is PER SOURCE for a state and PER SECTION for content, and a source resolves PER BLOCK where its own author disclaims one

Two rules, and both were written after the worked example broke them. They are here rather
than in a stage because each one is the collapse A1 and A2 exist to prevent, arriving one
level away from the cell.

**ONE. A SECTION RESOLVES AGAINST ITS OWN SOURCE AND AGAINST NO OTHER.** An item missing
from one source loses the content of the sections that source feeds, and loses nothing
else. Every other section is built from its own source and is withheld by nothing.

The failure this closes was measured on the worked example. A stop was on the schedule feed
and not in the period plan, and the build suppressed every section of it behind one note
reading that no content was prepared and that "everything below is omitted rather than
guessed". Nothing needed guessing: that site had a contract record and **three open work
orders**, one of them a condensate overflow in a data room, seventeen days old, every one
of them sitting in its own file and readable. The period plan governs the plan section. It
governs the contract section not at all. **Absence in one source read as absence in all is
the same error as a blank read as a zero, one level up**, and it is harder to see, because
the briefing was telling the truth about the source it had checked.

**And it is a structural property as well as a correctness one.** What a reader experiences
moving between items IS the section set. A briefing in which item four carries five
sections and item six carries one is a briefing whose items are each individually honest
and whose shape tells the reader nothing, and a section quietly missing is
indistinguishable from a section that does not exist. So every item carries every bound
section, every run, and a section with nothing in it says why in its own words, per
SD-CTR-07. This is G-RB-12.

**TWO. A SOURCE RESOLVES PER BLOCK WHERE ITS OWN AUTHOR DISCLAIMS ONE, AND A SECOND
READING IS ATTEMPTED BEFORE ANY SOURCE IS CALLED UNRESOLVED.** Two readers fail differently
on the same file. UNRESOLVED is the state for a source no disciplined reading recovers, and
it is reached after a second reading and not before.

Where a file carries an authoritative block and a block its own exporter has marked
unconfirmed, the authoritative block is CURRENT and is used, and the disclaimed block is
never used as a value. **The disclaimed block is still READ**, to establish which items it
mentions, because "the readable block names nothing for this item" and "a row for this item
sits in a block its own author disclaimed" are two different facts and only one of them is
an absence. Those are three distinct per-item sentences out of one source, and a run that
can say only one thing about a whole source cannot write any of them.

The failure this closes was also measured on the worked example. A hand-made parts export
carried three clean rows above its own disclaimer and three disclaimed rows below it. The
build called the whole file unreadable and **discarded all three good rows**, every one of
them for a site on that day's schedule, including the part for the first stop of the
morning. The file said what it could be trusted on and the briefing did not read that far.

---

## A2.1. The carve-out from capability-probe 4.4, stated rather than assumed

**reference/capability-probe.md 4.4 says a degraded run may never fill a gap with "an
estimate, an average, a plausible value or a value carried over from a previous run."**
The CARRIED state carries a value over from a previous rebuild. That reads as a direct
contradiction and it is carved out here, explicitly, for the same reason A5.1 exists.

The prohibition is against carrying a value over to FILL a gap, which is the silent
substitution that makes a degraded artifact look complete. CARRIED does not fill the gap.
It keeps the gap visible: the value appears, labelled as carried, dated to when it was
last current, and past the tripwire the whole briefing is bannered. SD-SRC-18 is the rule
that governs the disclosed version, and it is explicit: a stale reference is a disclosed
limitation, a halted run is a dead end.

**The condition on which that reading holds is a gate, not a convention.** A carried value
that loses its label, its date or its banner is no longer a disclosed limitation; it is
4.4's forbidden substitution, and the artifact has become the thing both rules exist to
prevent. So M5 and M6 of the message contract are not formatting elements. **They are what
keeps the CARRIED state legal**, and that is why they sit in Part G rather than in a style
note.

## A2.2. A standing degradation is announced at full prominence every period

capability-probe 4.4: "It may never downgrade its own announcement between runs. A
degradation announced last run and still present is announced again, at the same
prominence."

That rule was written for artifacts produced on request, where it rarely bites. **A daily
briefing is the case it was waiting for.** On day one a stale source is alarming and the
banner is obvious. By day five there is pressure, from the reader and from anyone tuning
the thing, to soften it to a footnote because it has been said already.

**The softening is the failure.** The source is exactly as stale on day five, and the
reader is five days further from remembering why. A banner is never reduced, moved below
the first item, or replaced by a per-line label because it has run before. It comes off
when the source comes back, and not one period earlier.

## A3. Two loops, and the delivery loop never computes

`DELIVERY_PERIOD` and `REBUILD_PERIOD` are separate bindings and the second is always the
longer.

- **The delivery loop** runs every delivery period. It reads the schedule of what is
  planned, assembles the briefing from content prepared by the last rebuild, adds anything
  that is genuinely only knowable now, and sends. It does not query a source of record, does
  not recompute a ranking, and does not rebuild content. Target: a small number of calls and
  about a minute.
- **The rebuild loop** runs every rebuild period. It discovers the current inputs,
  re-reads the sources of record, rebuilds the per-item content, validates it, and swaps
  it in. Target: minutes, and it may be expensive.

This is not an optimization. It is a correctness property. A delivery loop that computes
is a delivery loop that can fail halfway at 5 AM and send half a briefing. A delivery loop
that only assembles either finds its content or does not, and the second case is a notice,
not a partial.

## A3.1. The loops differ in INTERACTIVE state, not only in cadence

This is the more consequential split and it is inherited rather than invented.
reference/capability-probe.md 1.4 defines a scheduled or unattended run as NON-INTERACTIVE,
and ladder 2.14 rung 2 declares that rung the correct behaviour for one.

| Stage | INTERACTIVE | What follows |
|---|---|---|
| 1, enable and activate | PRESENT | Questions may be asked. Config may be written. |
| 2, rebuild | ABSENT | 2.14 rung 2. No question fires, and **nothing is written to the organization config.** |
| 3, deliver | ABSENT | Same. |

**The clause that constrains the whole design is 2.14's own: on rung 2 nothing is written
to the organization config, because no authorized answerer looked at anything.** A
scheduled rebuild therefore may not bind anything. A value still unbound when the scheduler
first fires stays unbound until a person comes back. Stage 1 is not a convenience; it is
the only window in which binding happens, which is why 1.5 insists every grant and every
binding is settled there rather than deferred into the loops.

The corresponding gain is worth claiming. P4 says INTERACTIVE absent together with
DIRECTORY absent drops role and scope to `ROLE_FALLBACK_KEY`, the narrowest role. A
briefing never falls there, because `BRIEFING_SCOPE` was bound in Stage 1 with a person
present. The setup turn is what buys every later unattended run its correct scope.

**And a scheduled run's non-interactivity is not itself announced.** It is the permanent
shape of the medium, not a degradation, and announcing it every morning would train the
reader to skip the banner that matters. What IS announced is anything that went unbound
because nobody could be asked. See P10 in the probe patch.

## A3.2. What a run that cannot ask still owes, and where it owes it

reference/binding-interview.md I11 states the duty in full, and three of its five points
land on every scheduled firing of this workflow, permanently:

- **Point 3.** The run lists EVERY question it would have asked, in order, naming the
  variable each would have bound and what that binding would have changed. **A bare list of
  identifiers is explicitly non-compliant.**
- **Point 4.** Nothing is written to the organization config. Already stated in A3.1.
- **Point 5.** The run is PROVISIONAL wherever an ignition variable is unbound, at the
  standing prominence.

**A daily artifact cannot carry point 3 inside itself.** A one-off report prints its unbound
list once; a briefing would print the same list 250 times a year and the reader would stop
seeing it inside a fortnight. The split is the one capability-probe 4.1 already draws:

1. The **message** carries the count and the single most consequential effect.
2. The **durable record** carries the full list in I11 point 3's form.
3. The **unbound-value queue** gets the append required by binding-interview 5.2 step 7:
   the variable, the run that needed it, the decision it was facing, and what the default
   cost. That queue already exists and is how the ORG tier learns what it is missing
   without anybody being interrogated.

E7 proposed a durable record from scratch before the queue was read. The queue is the
better mechanism for unbound values and the durable record holds the probe detail; both
exist, and neither lives in the message.

## A3.3. PROVISIONAL, and why it joins the banner rule

I11 point 5 and binding-interview 6.2 make a run with any unbound ignition variable
PROVISIONAL. 6.5 fixes its prominence: **"The provisional labelling is never softened on
later provisional runs. It appears at the same prominence every time until the ignition
interview happens."**

A briefing at an unbound organization is provisional every morning, indefinitely. That is
the same shape as a carried source that has been stale for a fortnight, and it meets the
same pressure: a label that has appeared sixty times feels like noise to everyone except
the person who will act on it wrongly.

**So A2.2 governs both.** One rule, two triggers: a standing degradation and a standing
provisional label are each carried at full prominence every period until their condition
ends, and neither is ever reduced, moved below the first item, or replaced by something
quieter because it has run before. G-RB-7 enforces it for both.

## A4. A failed rebuild never produces a partial briefing

If any rebuild stage fails, the previous content stays in place untouched and the run
sends the short notice described in E3. It never swaps in partial content and never emails
a half-rebuilt briefing. See SD-EFF-32 (never present incomplete work as finished) and
SD-EFF-04 (a labelled partial is still a partial). The atomic swap in 2.7 is what makes this enforceable rather than
aspirational.

## A5. One recipient, and the binding is never widened

`BRIEFING_RECIPIENT` is the person who set the briefing up. A briefing is never sent to a
supervisor, a teammate, a distribution list or an address supplied later in a request. The
send permission granted at setup is scoped to that one address, and a request to widen it
is refused with the reason, not negotiated. See G2, SD-IDN-03 and SD-CTR-18 as carved out in A5.1.

The reason is not privacy theatre. A briefing is built from one person's scope and reads
as a judgment of their work. Sent to anybody else it becomes a performance report nobody
agreed to, and that is a different artifact with different rules.

## A5.1. The carve-out from SD-CTR-18, stated rather than assumed

**SD-CTR-18 says do not send or share the artifact automatically.** This workflow sends
automatically. That is a direct conflict with standing doctrine and it is carved out here,
explicitly, rather than left for a reader to notice and wonder about.

The rule exists because an artifact that leaves on its own reaches someone who did not ask
for it, in a state the author could not inspect. Both halves of that harm are addressed, and
the carve-out holds only while both conditions hold:

1. **The recipient is the person who asked for it, and only ever them.** Nobody receives a
   briefing they did not set up for themselves. The send permission is scoped to one address
   at setup and never widened. There is no onward share, no copy, no supervisor view. So the
   first half of the harm, reaching somebody who did not ask, cannot occur.
2. **The artifact cannot leave in a state the method did not validate.** Content is validated
   before it is swapped in and the swap is atomic, so a briefing is assembled only from
   content that passed. A failed rebuild sends a short notice instead. So the second half,
   leaving in an uninspected state, cannot occur either.

**Where either condition fails, SD-CTR-18 governs again and nothing is sent.** That is what
the gates in Part G enforce: G-RB-2 and G-RB-3 defend the first condition, G-RB-1 defends the
second. The carve-out is not a general permission for this workflow to send; it is a
permission conditioned on exactly those gates, re-checked at every send per SD-EFF-07.

## A5.2. A scope level whose members are PEOPLE

A6 forbids a briefing that reads as a judgment of its reader. This section is the other
half: **a briefing must not read as a judgment of the people inside its reader's scope
either.**

A span may hold a level whose members are individuals: a technician, an adviser, a
caseworker, a rep, a driver, a nurse. That level is legitimate and it is the ordinary shape
of a manager's scope. **The decision is contract-level and everything below is subordinate
to it: a person-bearing level is a legitimate SCOPE and is never an ordering, a grouping or
a reporting axis.** SD-LNG-02 and SD-CLM-12 are the doctrine.

### A5.2.0. The pressure that produces the forbidden artifact here, which is not the one a grid faces

The scorecard's A9 names its own collision: a peer-set rule wanting siblings and a summary
wanting a rollup, which together produce a table of named people ranked by a rate. **This
workflow has neither mechanism.** It computes no peer set, because A1.1 leaves it no
second number to compute, and it has no summary.

**Its collision is the length of the artifact.** A frontline briefing is one person's day.
A manager's briefing is that content multiplied by the number of people in the span,
delivered to a phone, before the day starts, under an action cap. And every natural way to
make a long briefing readable groups or ranks by person:

| The pressure | What it reaches for | What it breaks |
|---|---|---|
| Items from several people interleaved by time | A block per person, each headed by their name | A5.2.3's ordering rule and its subject rule at once |
| A subject line useful unopened | A count per person in the subject | A5.2.3's grouped count |
| A banner that says how stale the briefing is | "Two of your three technicians have stale work orders" | A5.2.3's grouped rollup |
| An action cap spread over several people's work | Spend the slots on whoever has most wrong | A5.2.3's ordering rule |

**Every one of those four arrives as a usability improvement rather than as a judgment, and
that is what makes this the likeliest defect in the file.** Nobody decides to rank their
own people. Somebody decides a twenty-four item briefing is hard to read on a phone, which
it is, and the first fix to hand is the forbidden artifact.

### A5.2.1. Detecting a person-bearing level

Detect, never assume, never wait to be told. A level is PERSON-BEARING when ANY of:

- its values resolve through the people family of the concept dictionary: assigned to,
  owner, handler, technician, adviser, rep, submitter, clinician, case owner, driver;
- `ROLE_LADDER` binds a role whose `scope_level` is that level, and the members of that
  level are the individuals holding the role rather than units they own;
- its values are free text shaped like personal names, and its cardinality is far below the
  item count while each value maps to many items.

**Where it cannot be determined, the level IS person-bearing.** That default suppresses a
grouping rather than creating one, which is the direction G3 requires: an unknown never
resolves to the reading that manufactures a finding about a person.

**This test is stated in two places in this bundle and that is a disclosed defect rather
than a convention.** It is A9.1 of the scorecard word for word, and finding C's rule, which
is SD-FMT-13's own, is that a definition lives in exactly one place. It cannot be cited
across workflows, because the router has a run read one workflow and nothing else until
something cites it by name, so citing A9.1 would mean loading the whole scorecard to
resolve one test. **The promotion of this test to a doctrine rule is recorded as a request
in I1**, in the form the scorecard used for its qualifier strings: the duplicate ships, the
request is named, and when the rule exists both workflows cite it and both copies come out.

### A5.2.2. What a person-bearing level MAY do

- **Select a population.** The ordinary case and the reason the level exists.
  `BRIEFING_SCOPE` already resolves through it.
- **Attribute an item.** The level may name who owns each item so the reader can route a
  conversation and brief by name, per SD-SPN-08. **Naming the owner of a unit of work is
  not a judgment of them.**

**At the finest altitude there is nothing to attribute, and that is a finished state rather
than a missing one.** SD-SPN-02's third condition: the unit level is never an attribution
column, because the unit is the item and its identifier is already in the item's own
header. A frontline reader whose finest scope level IS the item therefore carries no
attribution at all, which SD-SPN-02 calls the normal case for the most junior role in any
ladder and not an exotic one. The site identifier and town on a technician's briefing are
the identity of the stop, not a span block.

**The attribution set is computed ONCE over the delivery period's own items and applied
identically to every item**, per SD-SPN-03 and SD-SPN-04. An item whose owner is the only
one of their kind in that town still carries the same attribution shape as every other
item. That is G-RB-12's structural rule arriving from the span side, and it has the same
reason: what a reader experiences moving between items is the shape.

### A5.2.3. What it may NEVER do

None of these ships, in any section, at any altitude:

- **a rollup, subtotal, rate or count grouped by that level**, in the subject line, the
  banner, the provenance line, the footer or any item section;
- **an ordering, a grouping or a sort key on that level, and no heading whose subject is a
  person.** These are ONE failure in this medium rather than two, because a message has no
  sheets and no columns: grouping it by person produces per-person blocks headed by names,
  which is both at once. **It is stated as one named failure because the pressure toward it
  is constant and a prohibition has to be rememberable to survive that.**
- **any figure attributed to an individual by name**, and no comparison between the people
  in a span;
- **an attribution used to compare rather than to attribute.**

### A5.2.4. What replaces each, so the run is not merely blocked

- **The rollup** rolls to the nearest level above that is not person-bearing: the span
  total, or a geographic level where one resolves. Where none exists, the span total alone
  with one line saying why. **Never fabricate an intermediate.**
- **The ordering** is the one this workflow already has and it turns out to be what makes
  the manager altitude lawful: **items are ordered by when the work happens, never by rank
  and never by person.** B2 and A6 already said so for a different reason, which is that a
  ranked list is the PLANNING skill's artifact. It is worth stating that the two reasons
  converge rather than leaving it a happy accident.
- **The attribution** stays, and the footer says in plain words that the briefing is not a
  comparison between the people in it and must not be used as one, per SD-LNG-02.
- **The peer set does NOT apply here, and the reason is not squeamishness.** A9.4 keeps a
  computed anonymous distribution because its own A5 needs a second number. This workflow
  computes no performance figure at all, so there is no distribution to publish and no
  reader figure to place against one. **And the arithmetic makes the rule absolute here
  where it is conditional there**: `ANONYMITY_FLOOR` and `MIN_POPULATION_FOR_NORM` both
  default to 5, SD-SPN-16 requires BOTH to be met, and the sibling set excludes the reader,
  so a span of three yields two. **A manager's span is a handful of people by definition, so
  no aggregate over it could ever clear either floor.** **SD-SPN-16 is therefore NOT ADOPTED
  by this workflow**, with its own two-floor arithmetic as the reason: its outward walk,
  its four states and its two-floor test all presuppose a span large enough for some level
  to clear both floors, and this medium has none. What replaces it is one sentence:
  at a person-bearing level this medium publishes no aggregate, because a span small enough
  to brief is small enough that every count over it names people by elimination, which is
  SD-CLM-12 exactly.

### A5.2.4b. The repeated-explanation relief, which the second altitude produced and the first did not need

**Running the manager altitude found a defect the technician altitude could not have
shown.** A per-item explanatory line that is identical on every item carrying it costs its
full length on every item while carrying one piece of information, and a span multiplies
the number of items. Measured on the worked dataset, from one build: **twenty per cent of
the reader-facing text at the finest altitude over eight items, and fifty-one per cent over
twenty-three.** One sentence, the parts absence, accounted for two thousand nine hundred
and forty-one characters across eighteen items.

**This workflow ADOPTS SD-FMT-28, and the word is deliberate.** The first draft called it
"SD-FMT-28's shape in a medium with no columns", which reads as borrowing an argument, and
the conformance checker was right to refuse that: a rule whose mechanism a workflow actually
runs has to name that workflow on its Applies line or one of the two is the defect. Every
part of the mechanism is here. The bound is declared before the artifact is built and is
never raised to clear a build that failed it. What gives is a standing qualifier drawn from
a closed declared set and written in the same words every time, which is
`STANDING_EXPLANATIONS`. The standing place's entry is mandatory, because a short form with
nothing explaining it is an abbreviation the reader has to decode. The three things that
never give map one for one: no column dropped is no item dropped, no header floor breached
is no state losing its characters, and no meaning shortened is no per-item fact shortened.
The last rung is the same rung: ship over and say so.

**What differs is the unit and the rungs this medium does not have**, and SD-FMT-28's
general form now says that a medium lacking a rung declares it absent rather than skipping
the ladder. What a grid bounds is summed width; what a message bounds is **the share of its
reader-facing text spent on repeated explanation**, against `MESSAGE_MAX_REPEATED_SHARE`.
A grid moves a qualifier to its legend or to a trailing narrative column; a message has
neither, so **those two rungs are declared absent here** and the standing place is the one
block described below. The width recompute is absent for the same reason there are no
columns to recompute.

**THE SPLIT THAT MAKES THE RELIEF LOSSLESS.** Each such line is two facts welded together:
one about THIS ITEM, which differs, and one about the SOURCE or the METHOD, which is
identical every time. Only the second repeats, so only the second moves.

**AND IT MOVES ABOVE THE FIRST ITEM, NOT BELOW THE LAST.** A grid puts a standing
qualifier's wording in its Legend, which a reader opens deliberately. A message has no
legend, and its footer is twenty-three items away from the first thing it explains, so the
only place a reader certainly passes through is the provenance block at the top. The moved
wording sits in its own block immediately above the first item, as a key to reading them
and never among the findings: an explanation of what a line MEANS is not a finding, and an
earlier build put it inside the action list where it read as four more things to do.

**THE THREE THINGS THAT NEVER GIVE.** No item is dropped. No per-item FACT is dropped. No
state loses its characters, per M15. What moves is wording and nothing else, which is why
the two states a relieved line distinguishes still read differently: none open as of a date
is not the same string as not in the export, and the key says which is which.

**THE MEASURE COUNTS ONLY DECLARED STANDING EXPLANATIONS, AND THAT IS THE WHOLE
CORRECTNESS OF IT.** The first version counted any paragraph identical to another, which on
the manager's run swept in a plan line nine times. That is not a repeated explanation, it is
nine items whose planned visits and PM status happen to carry the same two values, and it is
exactly the per-item fact the relief is forbidden to touch. **A bound that counts a
coincidence of values as waste is a bound that pressures a run to drop data**, which inverts
what the bound is for. SD-FMT-28 draws the same line: a phrase unique to its own row is
never touched.

**THE DECLARED SET TAKES SD-CTR-29'S COVERAGE VALIDATION, IN SD-CTR-29'S OWN DIRECTION.**
Validate from the explanations the run can EMIT to the declared set, never the other way.
The first declared set held four and the build emitted six of the same shape, so the absent
contract string and the disclaimed parts string were invisible to the bound and the relief
could never have reached them however often they repeated. **An undeclared repeated
explanation is a hole, and a hole guarantees the bound understates on every run in which
that line occurs.**

**THE KEY SAYS WHICH IS WHICH AND NEVER CARRIES THE DISTINCTION, AND THIS ONE WAS PROVED
RATHER THAN REASONED.** M15 strips every style and class from the built message and asserts
each state is still legible in the characters. Collapse two different parts states into one
item line and run it: **it passes.** The phrases it looks for, a measured zero and a
disclaimed block, survive inside the moved block, so the state is gone from the lines while
the key goes on naming it. That was verified by mutating the built artifact and watching M15
pass and nothing else notice. **A relief that leans on its own legend is lossy, and M15
cannot see it**, so the losslessness test reads the item lines with the moved block gone,
which is a second-channel test against a channel M15 does not consider: a reader may lose
the styling, and a reader may also simply not read the legend.

**Measure it every run and record the measurement whether or not it fires.** A bound only
measured when somebody suspects a problem is not a bound, and a passing measurement is the
evidence the check ran.

**The bound and the declared set are `MESSAGE_MAX_REPEATED_SHARE` and
`STANDING_EXPLANATIONS`, and the element is M16.** The measure belongs to the bound's own
validation and is stated there rather than here, because a different measure makes a
different bound. M16's losslessness clause gates the send; **M16's bound does not.** A
briefing that cannot be relieved without dropping an item, dropping a fact or losing a
state ships over the bound and says so, per G-RB-16. Long and complete beats short and
quietly thinner.

### A5.2.5. The interlock, because an exhortation is not a mechanism

**Before the message is sent, every ordering key, every grouping key and every count in it
is tested against A5.2.1, against the BUILT message rather than against the intention.** Any
that resolves person-bearing is not sent in that shape: A5.2.4's substitution is applied and
named. This is G-RB-14, it blocks the send, and `verify-briefing.py` runs it by reading the
rendered message back.

**The distinction to hold on to: this workflow reports the state of work. A person may own
an item and may therefore be named beside it. A person is never the subject of a figure.**

### A5.2.6. A filter on somebody else's briefing is not that person's briefing

SD-SPN-07, and it is absolute: no part of this workflow may imply otherwise. Its two stated
reasons are about published rows and about rank, and neither fully reaches a briefing, which
drops no item and computes no rank. **A third reason does, and it is specific to this
medium: the banner, the tripwire denominator and the action cap are every one of them
computed over the reader's WHOLE span.**

A frontline worker handed their own slice of a manager's briefing receives a staleness
banner computed over sources that may not feed their items at all, an action list capped
across several people's work, and a freshness aggregate struck at the wrong altitude.
**"Half your sources are not current today" over a manager's four sources is a different
sentence from the same words over one person's day.** The remedy is the one SD-SPN-07 gives:
run the workflow at that person's own scope, which is one more briefing and not a filter.

## A5.3. An action is written at the reader's own claim tier

SD-SPN-09 binds two tiers at `ROLE_LADDER.claim_tier`. A DIRECT tier reader personally
changes the thing. An AGGREGATE tier reader does not; somebody in their span does.
**Getting it wrong is fatal in both directions, and the action list is where this workflow
gets it wrong.**

- **A DIRECT tier reader's actions are atoms**: confirm this work order before quoting,
  chase the date on this part, ask this site who holds their agreement.
- **An AGGREGATE tier reader's actions are shapes**: three of your sites have no contract
  record at all, so the renewals file needs looking at; the work order export has not
  refreshed in eight days, so service operations needs chasing.

**A manager's briefing whose action list is twenty-four atom-level items is a briefing that
tells a manager to do the jobs of the people in her span**, and `BRIEFING_ACTION_CAP` makes
it worse rather than better, because a capped list then chooses WHICH of her people's jobs
she should do today, which is an ordering on a person-bearing level reached by a different
road.

The test is the one SD-SPN-09 states and it is lexical rather than judgment: an action at
the aggregate tier names a population or a source and not a single item, and an action at
the direct tier names the item it is about. An action list at the wrong tier fails G-RB-15.

## A6. What a briefing may never contain

**A5.2 is the other half of this section and the two are read together.** A6 protects the
reader from a briefing that reads as a judgment of them. A5.2 protects the people inside
the reader's scope from the same thing. Neither covers the other.

- A number with no traceable source. Every figure resolves to a named input. See SD-CNF-08.
- A value inferred to fill a gap. ABSENT prints its named-absence string. See SD-CNF-07
  and SD-CNF-06.
- Content from a source in CARRIED state without the carried label and the source's own date.
- An item outside `BRIEFING_SCOPE`, which is the recipient's own work and nobody else's.
- A judgment about a named person other than the recipient.
- More than one send per delivery period. A second send in the same period is a defect,
  not a correction; a correction is the next period's briefing. See SD-EFF-28.

## A7. Cold starts

A first run has no previous content, no previous schedule, **and no previous resolution**,
so B1 rung 0 cannot fire and no source can be DRIFTED on a first rebuild. It is not the same
as a rebuild that failed. On a cold start the briefing states that it is the first
one, omits every change-versus-last-period line rather than computing against zero, and
says what will appear once a second period exists. See SD-CLM-28 (a cold start is DETECTED, never declared) and SD-CLM-31 (no prior period means no WIN and no MISS).

---

# PART B: SOURCE PROVENANCE AND THE FRESHNESS LADDER

## B1. The ladder, in order

For each configured source, at each rebuild, in this order. The first rung that resolves
sets the state.

**Rung 0 runs first and is a comparison rather than a read.** Resolve the source's concepts,
then compare that resolution against the one recorded at the previous rebuild. Where a
concept resolved then and does not now, or resolves to a different column now, the source is
DRIFTED and the ladder still continues: drift is a statement about the resolution, not about
whether the file was read, so a DRIFTED source also carries CURRENT or CARRIED for the
concepts that did resolve. **This is the one rung where two states coexist**, and it is why
drift is announced by banner rather than by the per-line label that assumes one state per
source. On a first rebuild there is nothing to compare against and rung 0 cannot fire; see
A7 on cold starts.

1. **Read it from its source of record.** Resolves to CURRENT. Record the read timestamp
   and the source's own period stamp, which are two different facts and both are kept.
2. **Find it among this period's discovered inputs**, recognized by content rather than
   by filename. Resolves to CURRENT, with the file's own modified date recorded.
3. **Parse failure.** The source was located and could not be read. Resolves to
   UNRESOLVED. Record what was tried and what the parser saw. See SD-EFF-10 and SD-PRS-18.
4. **Fall back to the last good copy.** Resolves to CARRIED. Record the date that copy
   was itself current. See SD-SRC-18: a stale reference is a disclosed limitation, a halted
   run is a dead end.
5. **Nothing at any rung.** Resolves to ABSENT.

Recognition by content and never by filename is the same rule the other workflows use for
columns, applied to whole files: a source is identified by the concepts its columns carry.
See reference/field-resolution.md, SD-SRC-14 and SD-PRS-25.

## B2. What each state permits a line to assert

| State | The line may say | The line may not say |
|---|---|---|
| CURRENT | The value, plainly. | Anything, without its source named somewhere in the artifact. |
| CARRIED | The value, with the carried label and the date it was current. | The value as though it were just read. |
| ABSENT | The named-absence string for that source. | A zero, a blank, an average, or a default. |
| UNRESOLVED | That the source was present and unreadable. | Any value from it. |
| DRIFTED | Every value from the concepts that still resolve, plainly. | Anything from the concept that moved, and nothing that implies this period is comparable to the last on that dimension. |

An ABSENT source printing a zero is the single most expensive defect available to this
workflow, because zero is a legitimate value and the reader cannot tell. The named-absence
string is mandatory and its wording is a binding, not a sentence this file chooses.

## B3. The carried tripwire

If more than `CARRIED_SOURCE_TRIPWIRE` of the configured sources resolve to CARRIED in one
rebuild, the rebuild is not treated as successful. The briefing still goes out, because a
briefing built from last good content is better than silence, but it carries the degraded
banner from E2 at the top rather than per-line labels alone, and the next rebuild's notice
names every carried source. A reader skimming on a phone will not assemble five per-line
labels into the conclusion that the whole thing is stale. One banner does that for them. See SD-EFF-05.

## B4. A failed identifier never widens

field-resolution.md F5.6: "If a concept cannot be resolved and the feature it feeds would
otherwise cover a broader population than the user asked for, the output says so on its
face. A report that quietly covers the user's whole span when they asked for one slice is
wrong in the way that destroys trust, because every number in it is internally consistent."

`ITEM_IDENTIFIER` is the join between the schedule feed and every per-item source. Where it
fails to resolve in one source, the tempting repairs are to match on name, to match on
location, or to attach that source's content to every item. **Each of those silently
widens**, and the briefing stays perfectly self-consistent while attaching one site's open
work to another site's name, under a technician's own heading, at five in the morning.

The feeds list says an unresolved identifier costs every section that joins on it. It costs
them for this reason, and the reason is worth carrying next to the rule, because "costs
those sections" reads as housekeeping and what it prevents is not.

## B5. Name the layer actually read

Where a source can be read at more than one layer, the artifact names the layer that was
actually read, not the system it ultimately came from. A figure read from a cached extract
says the extract, not the warehouse behind it.

## B6. What this workflow owes the dictionary, and may never do to it

field-resolution.md 7.5 promotes a learned stem into the standing dictionary on five
criteria, the fifth of which is that it "has been seen in at least two distinct source
periods, OR it was named directly by a user."

**No other workflow in this bundle accumulates distinct source periods.** They run on
request. This one reads the same sources on a fixed cadence and crosses that threshold by
continuing to exist, which makes it structurally the best evidence generator the dictionary
has.

**And it may never act on it.** 7.5 opens: promotion is an ORG-tier act, never a PERSON-tier
one; a run proposes and the binding owner accepts. A3.1 is harder still, because a scheduled
rebuild is INTERACTIVE ABSENT and writes nothing to the organization config.

So a rebuild observes the second period, records that criterion 5 is now met, and appends
the proposal to the unbound-value queue **in the exact form 7.5 specifies**, which is the
form the binding owner pastes into the config. Over a year of operation the briefing becomes
the quiet source of most of the dictionary's real evidence, and every bit of it arrives as a
proposal that somebody with authority accepted or did not.

---

# PART C: THE WORKFLOW

Five stages. The order is authoritative.

## Stage 0: Probe and resolve

**0.1** Run reference/capability-probe.md. This workflow additionally requires a scheduler
and a send channel. Record both as present or absent; Part E governs each absence.

**0.2** Resolve who is asking and their role per the shared identity rules. **`BRIEFING_SCOPE`
is DERIVED from the person-tier scope already bound at Q-PERSON-2 and is never asked again**,
per I2 and because PART 4 opens by promising four questions and no more. Where no person
scope exists, the PERSON SCRIPT runs; this workflow does not substitute a question of its
own. A role that owns other people's work does not receive their briefings; it receives its
own, at its own altitude. See SD-SPN-01, SD-IDN-03.

**0.3** Resolve `DELIVERY_PERIOD`, `REBUILD_PERIOD`, `DELIVERY_TIME` and the derived
wait-until and expected-delivery times. Each has a documented default and prints its
degradation notice when unbound.

**0.4** Read the configuration if one exists. Absence of a configuration means this is a
first run; go to Stage 1. Presence means go to Stage 2 or Stage 3 depending on the trigger.

## Stage 1: Enable, then activate

Two conversational turns, deliberately separated, because the first one ends with a task
only the person can do.

**Stage 1's status against binding-interview's three stages, stated because I3 has teeth.**
I3 limits a RUN to two deferred bindings, and at most one before the first output. Stage 1
asks for more than that. It is legal because **Stage 1 is not a run**: it is a setup
conversation the person opened by asking for a briefing, closer in kind to the person script
or the ignition interview than to a report. It produces no artifact and ranks nothing.
**If that reading is wrong, the activation flow needs restructuring rather than excusing**,
and this paragraph exists so the claim is visible enough to be challenged.

**1.1 Enable.** The assistant explains, in its own words and as a numbered list the person
follows, how to create the standing schedule feed: what fields it must carry, what filters
it must apply, what cadence it must run at, and where its output must land. It stops and
waits. Nothing is installed, built or scheduled.

**1.2** If the feed already exists, say so, skip the walkthrough and ask only what time it
is set for.

**1.3 Activate.** On the person's return, resolve `DELIVERY_TIME` from their own sentence,
derive the run time, the wait-until and the expected delivery, and state all three back.

**1.4** Install the build and delivery steps, create the configuration from the template
with this person's scope and period window, and write the operator notes with their times
filled in.

**1.5 Grants before the schedule, and this ordering is load-bearing.** A scheduled run can
only use what the task was already permitted. So every permission the loops will need is
raised now, while the person is present, by running a real rebuild and a real dry run
before the schedule is created. The send permission is scoped to `BRIEFING_RECIPIENT`
alone. The schedule is created last and confirmed immediately, because an unapproved
schedule card saves nothing and fails silently at the first firing. See SD-RUN-13, and SD-EFF-14 on a stage that cannot write its checkpoint.

**1.6** Run Stage 2 along its first-run path.

**1.7** Dry-run Stage 3 for the next delivery period, render the preview, send nothing.

**1.8** Tell the person what arrives, when, which period is the quiet rebuild, and the
small number of conditions that can need their attention.

## Stage 2: Rebuild

Triggered by the rebuild schedule, or by the person saying the inputs have changed.

**2.1 Trigger test.** See SD-SRC-15: resolve the source for the period being PLANNED,
never "the latest". Determine whether the period's defining input is new. A new one
means a full rebuild including anything derived from the period's shape; an unchanged one
means refresh the data and the per-item content only.

**2.2 Discover.** Scan the configured locations for inputs modified since the last rebuild,
recognize each by its column signature (SD-PRS-25, SD-SRC-14), keep the newest of each
kind, and stage them. Any
additional file keyed by the item identifier is staged as an extra input and its row for
each item appears in that item's content under a general heading, with its own columns and
values, identities dropped and values shown as found and never interpreted. This is what
lets a new input appear in the briefing with no change to this workflow.

**2.3** Apply the freshness ladder from B1 to every configured source. Record each state.

**2.4 Fold in direction.** Open each document discovered as direction for this period and
fold anything that directs the work into the period notes: a deadline into deadlines,
published wording into quotes, a supervisor's direction into the focus list. Quote, never
paraphrase. A document with no item-level direction is skipped and the skip is logged.

**2.5** Re-read the sources of record for the period's window.

**2.6 Build** the per-item content for every item in scope, not only the ones currently
scheduled, so an item added mid-period already has content.

**2.7 Validate, then swap atomically.** See SD-EFF-27, SD-EFF-14 and SD-EFF-29. Validate structure, item count, required fields and
character set. Only on a clean validation, swap the new content in and keep the previous as
the rollback copy. A failed validation leaves the previous content in place and the stage
fails. This is the mechanism A4 depends on.

**2.8 Publish** the configuration, the content and the captured schedule to durable storage
so a fresh workspace can restore.

**2.9** On any stage failure, go to E3.

## Stage 3: Deliver

Triggered by the delivery schedule.

**3.1 Assemble only.** See SD-SRC-16: cache what does not vary, fetch live what does. Restore from durable storage if the workspace is fresh. Find this
period's schedule feed, polling until the wait-until time. Read every planned item, save
the remaining schedule, keep the items for this period in planned order, and note items
added or dropped against the previous saved schedule. **No source of record is read and
nothing is recomputed.**

**3.2** Build the message from the prepared per-item content plus the period's own calendar
or equivalent. An item with no prepared content gets its header and a short note saying so,
never invented lines.

**3.3 Schedule fallback,** in order: this period's feed, then the schedule saved from the
previous period, then the schedule captured at period start. Whichever was used is stated
in the first lines of the message, not buried.

**3.4** Apply the medium rules in Part J. Send to `BRIEFING_RECIPIENT` only.

**3.5** A period with no planned items gets a two-line message saying so. See SD-CTR-07. Silence is never
the same as nothing scheduled, because silence is indistinguishable from a broken job.

**3.6 Dry run.** Given a period and the dry-run switch, write the preview and send nothing.
Required after any content change.

## Stage 4: Standing operation

**4.1** The briefing runs without further instruction until stopped.

**4.2** A stop request stops the schedule, says so plainly, and leaves content and
configuration in place so it can be resumed without rebinding.

**4.3** A change to period, time or recipient re-enters Stage 1 at 1.3, because every one
of those changes invalidates a permission grant or a derived time.

---

# PART D: CADENCE AND SHAPE

**D1.** `DELIVERY_PERIOD` is the unit the briefing covers: a working day in a field or
service organization, a shift in a continuous operation, a week in a lower-tempo one.

**D2.** `REBUILD_PERIOD` is always longer and is placed on a non-delivery boundary where
one exists, so a rebuild never competes with a send.

**D3.** Non-delivery periods get no send. A rebuild that happens on one sends nothing
unless it needs attention.

**D4.** What varies by role is altitude and volume, not structure. A frontline recipient
gets their own items in planned order. A recipient who owns a wider scope gets a shorter
briefing covering a wider population, because the span rules make a wide scope produce a
smaller share of what it owns, not a longer list. See SD-SPN-01.

**D5.** Everything in a briefing is ordered by when it will be acted on, never by rank.
A briefing is a sequence, not a list. The ranked list is period planning's artifact and
this workflow cites it rather than reproducing it.

---

# PART E: DEGRADED RUNS

**This part does not define ladders.** reference/capability-probe.md defines them and this
workflow reads the rungs that match its own capabilities, per P1c. What is here is the
handful of resolutions that file does not settle because no workflow before this one sent
anything or ran on a clock.

## E1. No scheduler

`SCHEDULER` ABSENT is rung 3 of 2.16 in the probe patch. The workflow does not pretend to
be scheduled. It produces the briefing on demand with identical content and names the one
request that produces it. What is lost is the unattended property, announced under the
probe's PART 4 like any other degradation.

**`SCHEDULER` DEGRADED is the ordinary first-run state** and it is rung 2: raise every
grant the loops will need now, in the foreground, with a person present, and only then
register. A schedule registered before its grants are held appears to succeed and then
produces nothing at an hour nobody is watching. See 1.5.

## E2. No send channel

`SEND` ABSENT is rung 3 of 2.15: write the briefing to the output location and name it. A
briefing that cannot be sent is still a briefing.

**`SEND` DEGRADED is the one rung in the bundle that refuses to deliver a successful
artifact**, and it is rung 2: a grant that is unscoped or wider than one address does not
resolve by sending to a narrower list as a matter of convention. The briefing is written,
the person is told what the grant allows and what it must be narrowed to, and nothing
leaves. Every other capability failure costs the reader information; this one would cost
somebody else their privacy. See A5, A5.1 and G-RB-3.

## E3. A rebuild stage failed

Previous content stays in place, per SD-EFF-29 and the atomic swap in 2.7. The run sends a
short notice naming the stage that failed and what the next delivery will be built from.
It never attaches partial content, per SD-EFF-32 and SD-EFF-04, and it never explains at
length: the notice exists to make somebody open something, not to be read closely at five
in the morning.

## E4. Too many carried sources

B3 and A2.2 apply. The banner ships above the first item, at full prominence, every period
the condition holds.

## E5. No schedule feed this period

Fall back per 3.3 and say which rung was used in the first lines. The briefing still goes
out, because the previous schedule is usually right and silence is worse than slightly
wrong. The polling in 3.1 is the graduated retry of SD-EFF-09, not a bespoke loop, and an
empty read is UNCONFIRMED rather than failed until that ladder is exhausted, per SD-EFF-10
and P6.

## E6. No spreadsheet or document tooling

Irrelevant here and must not block anything. P1c is explicit that a run reads the ladder
matching its own medium, and a run reading the wrong pair "reports the wrong capability as
blocking and degrades a deliverable that was never at risk." This workflow's medium is a
message. It reads 2.15 and 2.16 and ignores 2.1, 2.2, 2.2a and 2.2b.

## E7. Where a degradation is announced, and the one adaptation this medium forces

The probe's 4.1 requires three places, all of them, every time: the artifact's front panel,
the artifact's audit section, and the first line of the reply. **A message has no audit
section and cannot grow one**; a full probe record inside a briefing makes the briefing
unreadable, which is the same worry 4.1 has when it refuses to let the panel expand into
paragraphs.

The three places become:

1. **The banner above the first item**, carrying a count line and then one line per
   degraded capability, each naming all three things 4.2 requires: what was unavailable,
   what it changed, and what the reader should do.
2. **The first lines**, naming the count and the single most consequential effect.
3. **A durable audit record written to the briefing's own storage**, holding the probe
   record in full, which the message NAMES and does not contain. **For unbound values
   specifically the mechanism already exists and is better**: binding-interview 5.2 step 7's
   unbound-value queue, appended with the variable, the run that needed it, the decision it
   was facing and what the default cost. See A3.2. The durable record holds the probe
   detail; the queue holds the bindings; neither lives in the message.

**This is a real departure and it is flagged rather than absorbed.** 4.1 says "the artifact
is the copy that survives," and for this medium that stops being true: a briefing is read
once on a phone and deleted, and the durable record is what survives. The audit still
exists and is still complete. It is simply not in the thing the reader holds.

## E8. The self-check, sharpened for this medium

The probe's 4.5 asks one question before publication:

> If a reader opened this artifact six months from now with no memory of the conversation,
> could they tell from the artifact alone which parts of it were produced with less than
> the full method, and what that cost them?

**For a briefing the horizon is not six months. It is tomorrow morning**, and the reader is
the same person, who will not remember which day the work order export stopped refreshing.
The question is harder here than where it was written, not easier, and a briefing that
cannot answer it is not finished.

## E9. The resolution report, which fires on healthy runs

field-resolution.md 7.7 requires every run to report eleven classes of resolution event in
its audit section: every unresolved header by literal text, every concept resolved through
an ask and who decided it, every value-check resolution, every resolved-but-empty column,
every ambiguous resolution with both candidates, every provisional adoption, every sibling
set, every unresolved concept with the decision it cost, and every stem proposed for
promotion.

A message has no audit section, and on a daily artifact that list is longer than the
briefing. It goes to the durable record per E7, and the message names it.

**The distinction that matters, and it is not the one E7 draws.** The probe record and the
unbound-value list are degradation reports. **This one fires on a perfectly healthy run.**
If it were routed through the banner machinery every briefing would carry a banner forever
and the banner would stop meaning anything, which is the same erosion A2.2 defends against
from the other direction. The resolution report is written, named and not announced. Only
DRIFTED, which is a resolution event that is also a degradation, crosses into the banner.
---

# PART F: BINDINGS AT THE POINT OF NEED

Requested at the moment a decision needs them, once, from a person who would know.
Everything here is DEFERRED; none of it is ignition.

| Binding | The decision that needs it |
|---|---|
| `DELIVERY_PERIOD`, `DELIVERY_PERIOD_DAYS` | Stage 0.3, before any schedule is derived |
| `REBUILD_PERIOD` | Stage 0.3 |
| `DELIVERY_TIME` | Stage 1.3, from the recipient's own sentence. Never defaulted |
| `DELIVERY_FEED_WAIT_MINUTES` | Stage 1.3, derived from `DELIVERY_TIME` |
| `BRIEFING_RECIPIENT` | Stage 1.5, before the send permission is scoped. Never defaulted |
| `BRIEFING_SCOPE` | Stage 0.2, from role resolution |
| `SCHEDULE_FEED_SHAPE` | Stage 1.1, to write the walkthrough |
| `ITEM_IDENTIFIER` | Stage 2.2, to recognize an extra input as item-keyed |
| `BRIEFING_SOURCES` | Stage 2.2 and 2.3 |
| `SOURCE_FRESHNESS_STATES` | Stage 2.3 |
| `NAMED_ABSENCE_STRINGS` | Stage 2.3, one per configured source |
| `CARRIED_SOURCE_TRIPWIRE` | Stage 2.3 |
| `BRIEFING_ITEM_SECTIONS`, `BRIEFING_ACTION_CAP` | Stage 2.6 |
| `MESSAGE_MAX_WIDTH`, `MESSAGE_BODY_SIZE`, `BRIEFING_SUBJECT_SHAPE` | Part J |

**Every variable this workflow cites is written, and the conformance checker enforces
that rather than this sentence claiming it.** They live in reference/schema/recurring-delivery.md,
each carrying its definition, its documented default and its exact degradation notice in the
same file, per the standing rule that a run holding a definition without its default has
nothing to print at the moment the value turns out to be unbound.

**Two are deliberately not defaultable.** `DELIVERY_TIME` and `BRIEFING_RECIPIENT` fail the
wrongness test in the opposite direction from the usual: their absence does not make the
output thinner, it makes it arrive at the wrong hour or at the wrong person forever. Both
are asked while a person is present and neither has a default column value.

**Three are PERSON tier.** `DELIVERY_TIME`, `BRIEFING_RECIPIENT` and `BRIEFING_SCOPE` are
answered by each recipient on their own first run and are never asked of one person on
behalf of another, per S3. That is what makes a per-person briefing per-person rather than
a broadcast with names in it.

**None is IGNITION.** An organization that never uses this workflow is never asked any of
them. The remaining gap is the group number: the file needs one assigned and its row added
to reference/schema/README.md, and until that is done no name above resolves.

---

# PART G: HARD GATES

These stop a send. Nothing else does.

## G0. The gate convention, adopted as written

`HARD_GATES` is ONE organization variable and it is a TAXONOMY OF KEYED GROUPS, never a
flat list. **The convention is owned and defined once, by the planning skill, and this
workflow conforms to it as written rather than restating or renegotiating it.** What
follows is this workflow's conformance and not a second definition.

**The gate record. Every gate carries exactly six fields, and a gate missing any of them is
not a gate**: `key`, stable lower snake case and unique across every group; `group`;
`fires_at`, the named stage with any condition; `behaviour`, exactly one of
`stop_outright` or `ask_one_question_then_stop`, with no third value; `reads`, the schema
variable the gate tests or the literal `none`, never a threshold written as a literal in
workflow text; and `doctrine`, an ID whose Applies list covers every skill in whose group
the gate sits.

**THE SIXTH FIELD WAS WHY THE DECLARATION WAS A BLOCKING ITEM AND NOT A TIDYING ONE, AND
IT IS WORTH KEEPING THE RECORD OF IT.** Before the bundle was extended to four workflows,
no doctrine rule's `Applies:` list named BRIEFING, so **not one gate below satisfied its
sixth field and by the convention's own definition this workflow declared no gates at
all** while reading, to anybody who did not check, like a workflow with thirteen of them.
The declaration landed and every record below now resolves: each `doctrine` entry names a
rule whose Applies line covers BRIEFING, verified by reading the rule rather than by
asserting it. **Writing the records out is also what caught two of them pointing at the
wrong rule**, which is the next paragraph but one.

**Counts live in the taxonomy and nowhere else.** This file states no count of gates, in a
table, in prose, in a heading or in a parenthesis, and refers to the set only by group
name. The reason is not tidiness: the three audits in work/ had already recorded this
workflow as carrying eleven gates, twelve and thirteen, each correct when it was written.

**This workflow enforces `shared` plus `briefing` and nothing else**, and it never
enforces or reads another skill's group. **No skill may remove a shared gate.** Where a
shared gate cannot apply to a scheduled run it resolves NOT APPLICABLE per SD-EFF-37,
which is a passing state, **recorded with its reason**, exactly as I5b requires of any
check that could not be evaluated. It is never silently dropped and never redefined here.

**The shared group's five keys, and what each one means for this medium, because a gate
inherited without being read is a gate nobody enforces.** `HARD_GATES` names them and the
planning skill is authoritative for them; this is this workflow's conformance and not a
second definition.

| Shared key | How it reads here |
|---|---|
| `source_unreadable` | Applies unchanged. A required source that cannot be read at the probe stops the rebuild. |
| `record_count_zero` | **Applies, and its condition needs stating rather than assuming, which is the one place this workflow came close to removing a shared gate.** A period with no items is a legitimate state of the business and A4 ships the two-line message for it, so the gate must not fire on every quiet day. It fires where the zero is UNCONFIRMED, and resolves NOT APPLICABLE where the zero is VERIFIED EMPTY after the retry ladder has run and the filter has been shown to work. That is not a narrowing of the gate, it is the gate reading the right condition: a measured zero and a broken filter are two different facts and only one of them is a run that failed. SD-IDN-16 is the reason, in its own words, that zero rows means the filter is wrong before it means the scope is empty. |
| `scope_unresolvable` | Applies unchanged, and it is the one condition in this workflow that stops a RUN rather than a send or a schedule. |
| `formatting_unverifiable` | Applies, conditional on `DELIVERABLE_CONTAINER_REQUIRED` exactly as elsewhere. For this medium the elements are M1 to M15 and unverifiable means the assembled message could not be read back. |
| `character_gate_unrunnable` | Applies unchanged. It is the cannot-run twin of `briefing_character_set`, which is the fires-on-a-violation form. |

**None of the five resolves NOT APPLICABLE on an ordinary run**, which is a cleaner result
than it might have been and is worth recording: this medium does not escape any of the
shared stop conditions, it only reads one of them against a condition the other media
never have to distinguish.

**Additions are bound, never invented.** A stop condition this workflow needs and does not
have is requested through Part F, naming the decision. Until it is bound the condition
degrades and is disclosed rather than stopping, because an implementer inventing a stop
condition is the failure SD-EFF-02 exists to prevent.

## G1. The briefing group

The six-field record per gate. The `doctrine` column is the field G0 says cannot yet be
satisfied, and each entry names the rule the gate is built on so the field is one edit away
rather than one decision away.

| key | fires_at | behaviour | reads | doctrine |
|---|---|---|---|---|
| `briefing_no_validated_content` | Stage 2.7, after content assembly | `stop_outright` | `BRIEFING_SOURCES` | SD-EFF-04 |
| `briefing_recipient_unresolved` | Stage 1, and again before every send | `stop_outright` | `BRIEFING_RECIPIENT` | SD-CTR-18, via A5.1 |
| `briefing_send_permission_wider_than_one` | Stage 0 probe, and again before every send | `stop_outright` | `BRIEFING_RECIPIENT` | SD-CTR-18, via A5.1 |
| `briefing_second_send_in_period` | Before every send | `stop_outright` | `DELIVERY_PERIOD` | SD-EFF-28 |
| `briefing_character_set` | After assembly, before the send | `stop_outright` | `ALLOWED_CHARACTER_RANGE` | SD-FMT-14 |
| `briefing_carried_unlabelled` | After assembly, before the send | `stop_outright` | `SOURCE_FRESHNESS_STATES` | SD-SRC-18 |
| `briefing_banner_absent_or_softened` | After assembly, before the send | `stop_outright` | `CARRIED_SOURCE_TRIPWIRE` | SD-EFF-05 |
| `briefing_send_degraded_unscoped_grant` | Stage 0 probe | `stop_outright` | `none` | SD-CTR-18, via A5.1 |
| `briefing_drift_unbannered` | After assembly, before the send | `stop_outright` | `DRIFT_ANNOUNCE_SCOPE` | SD-EFF-29 |
| `briefing_section_joined_on_substitute_key` | Stage 2, at every join | `stop_outright` | `ITEM_IDENTIFIER` | SD-PRS-48 |
| `briefing_date_precision_widened` | After assembly, before the send | `stop_outright` | `DATE_FORMAT_MONTH` | SD-CNF-07 |
| `briefing_section_suppressed_by_other_source` | After assembly, before the send | `stop_outright` | `BRIEFING_ITEM_SECTIONS` | SD-CTR-07 |
| `briefing_state_legible_only_by_styling` | After assembly, before the send | `stop_outright` | `CLASSIFICATION_FILLS` | SD-FMT-29 |
| `briefing_person_bearing_axis_published` | After assembly, before the send, over every ordering key, grouping key and count in the built message | `stop_outright` | `ROLE_LADDER` | SD-LNG-02 |
| `briefing_action_at_wrong_claim_tier` | After the action lists are composed, before the send | `stop_outright` | `ROLE_LADDER` | SD-SPN-09 |

Every one of them is `stop_outright` and not one is `ask_one_question_then_stop`, which is
not an accident and is worth stating: **a scheduled run has nobody to ask**, per A3.1, so
the second behaviour is unreachable in the delivery loop by construction. The prose below
gives each gate's reasoning; the records above are the declaration.

**Three rows read "SD-CTR-18, via A5.1" and the qualifier is load-bearing.** SD-CTR-18 says
produce the artifact, name it, hand it over, and never mail it. **This workflow mails it**,
which is the one declared departure in A5.1, and A5.1 is legal only because of its two
conditions: the recipient is the person who set the briefing up, and the grant is one
address. So those three gates do not cite a rule this workflow obeys. **They enforce the
conditions that make departing from it lawful**, which is a different relationship and is
written out so no reader concludes the file cites a rule it breaks.

**And writing these records out caught two of them wrong, which is the whole argument for
the six-field format.** The degraded-send gate had been given SD-EFF-06, which is the
two-meanings-of-empty rule and has nothing to do with a send grant. The drift gate had been
given SD-PRS-47, which is about two concepts tying on one header, not about a concept
resolving somewhere new; SD-EFF-29 is the rule, and it says in its own words that a source
changing shape discards every downstream checkpoint, which is what a drifted rebuild is.
Both were invisible while the gates were prose paragraphs and both were obvious the moment
the field existed.

## G2. What each gate is for

**G-RB-1.** No validated content. A send with no content that passed 2.7 is never made.

**G-RB-2.** Recipient not resolved, or resolved to anyone other than the person who set it
up. See A5.

**G-RB-3.** Send permission absent or wider than one address.

**G-RB-4.** A second send attempted in one delivery period. See A6.

**G-RB-5.** Character set violation in the assembled message.

**G-RB-6.** A source in CARRIED state rendered without its label or without the date it
was last current. Per A2.1 this is not a formatting lapse: an unlabelled carry is
capability-probe 4.4's forbidden substitution, and the artifact has become the thing both
rules exist to prevent.

**G-RB-7.** The carried tripwire has fired and no banner sits above the first item, or a
banner has been reduced, moved or replaced because it ran in a previous period. See A2.2.

**G-RB-8.** `SEND` DEGRADED with a grant that is unscoped or wider than one address. The
briefing is written and not delivered. See E2 and 2.15 rung 2.

**G-RB-9.** A source in DRIFTED state on its first occurrence, rendered without a banner
naming both resolutions. A per-line label is not sufficient here and is the specific failure
A2.0 exists to prevent: drift is quiet by nature, and a label scaled to a line is a label
scaled to be missed.

**G-RB-10.** A section built from a source whose `ITEM_IDENTIFIER` did not resolve, joined
on anything else. See B4 and F5.6. The section is omitted with its named-absence string;
it is never matched on a substitute key.

**G-RB-16.** A repeated explanation relieved in a way that drops an item, drops a per-item
fact, or leaves a state legible only through its moved wording. See A5.2.4b. The relief
moves wording and nothing else, and a run that cannot relieve without losing one of the
three ships over the bound and says so, which is the honest last outcome.

**G-RB-14.** An ordering key, a grouping key or a count in the built message that
resolves person-bearing under A5.2.1. See A5.2.5. The substitution in A5.2.4 is applied and
named, and the test runs over the BUILT message rather than over the intention, because
A5.2.0's whole finding is that this shape arrives as a usability improvement rather than as
a decision anybody would defend.

**G-RB-15.** An action list written at an altitude other than the reader's own bound claim
tier. See A5.3. An aggregate-tier reader handed a list of atoms is being told to do the
work of the people in their span, and the action cap makes it worse by choosing which of
them.

**G-RB-13.** A state legible only through styling, or two states sharing one style. See
M15. A message is verified with its stylesheet and every class attribute stripped, because
a pass is only ever a pass in the renderer that read it back, and the renderer this one is
read in is not the one it was built in.

**G-RB-12.** An item carrying fewer than the bound sections, or a section suppressed for
a reason belonging to a different source. See A2.0b. The section ships with its own
explanatory line; it is never dropped because another source had no row for this item.

**G-RB-11.** A date rendered at a finer precision than its source carries. A source
holding `2027-04` holds a month; a line reading 1 April 2027 has asserted a day that is in
no file. See M13. This is a gate and the two other halves of M13 are not, and the division
is the point: a format inconsistency is ugly and a precision widening is a fabricated
value, and only one of those is the thing this workflow exists to stop.

Deliberately NOT gates, because a briefing that stops is worse than a briefing that is
honest about itself: sources in CARRIED state, sources ABSENT, the carried tripwire firing,
a missing schedule feed, a period with no items, and a failed rebuild. Every one of those
ships, labelled.

**Two more belong on that list and are worth naming, because they were nearly made gates.**
Two renderings of the same date precision in one message, and a count that disagrees with
its noun, are both caught at rebuild and neither stops a send. A reader who gets `1 stops`
has still been told the truth about his day; a reader who gets nothing has not, and has no
way to tell a blocked send from a dead job. Both are defects, both are fixed at the
rebuild that produced them, and neither is worth a silent morning. What does gate is the
rebuild itself: **a count template that has not been exercised at zero, at one and at more
than one is not promoted into the bound section standard**, which is where the cost of
catching it is a minute rather than a reader's confidence.

---

# PART H: GUARDRAILS

Restatements for checking. Not sources.

- One send per delivery period, to one person, who is the person who set it up.
- The delivery loop assembles and never computes.
- A failed rebuild leaves previous content in place and sends a short notice.
- Every figure traces to a named source; an absent source prints its named-absence string.
- Content from a carried source is labelled carried and dated.
- Scope is the recipient's own work; no other person's items are read.
- No step of the setup is ever placed on anyone but the recipient.
- Discovery opens only what it needs to classify and keeps nothing else.
- Logs carry counts and names, never message bodies or payloads.
- Nothing is uploaded anywhere the person did not put it.

---

# PART I: WHAT THIS WORKFLOW DECLARES

## I1. Status

**Structurally complete and demonstrated.** Deliberately shorter than the three shipped
workflows, because it binds a medium with no grid. It ships with a worked dataset in a
fourth industry and a built sample output, on the same terms as the other three.

## I2. What is done

1. **Schema.** Group 26, reference/schema/recurring-delivery.md, both tables, every
   variable carrying its definition, documented default and exact degradation notice in the
   one file. The group file is the count.
2. **Doctrine bound.** Every rule ID this file cites was read out of
   reference/doctrine/ and its title verified. None invented. **No rule needed to be added
   to the doctrine**, which is evidence the doctrine generalized past the three workflows
   it was extracted from.
3. **The SD-CTR-18 conflict resolved in writing.** A5.1 carves the exception, names its two
   conditions, and ties each to the gate that defends it.
4. **Worked dataset.** sample-data/facilities-services, a commercial HVAC and building
   services region, 48 sites, six planted traps documented in its DATASET.md so the claim
   is checkable.
5. **Sample output.** Two built briefings from one build at two altitudes, verified
   against the rendered artifacts rather than against the builder, in three states. Every
   applicable check passes at both altitudes and both rebuild byte-identical. Each run
   prints its own tally, which is where the number of checks is stated.

## I2b. Schema and doctrine requests this file makes, and none of them blocks an artifact

The pattern is the scorecard's: each request names the decision that needs it and ships a
stated interim until it lands, and the moment it lands nothing in this file changes because
the file reads the binding rather than naming the value. **A request recorded is a disclosed
gap. A duplicate nobody recorded is a second convention.**

1. **A DOCTRINE RULE FOR THE PERSON-BEARING TEST.** A5.2.1 is A9.1 of the scorecard word for
   word, because two workflows now need one definition and the router gives a run no way to
   cite across workflows: it reads the router and one workflow and nothing else until
   something cites it by name, so citing A9.1 would mean loading 380KB of the scorecard to
   resolve one three-part test. SD-LNG-02 and SD-CLM-12 carry the prohibition and neither
   carries the DETECTION. **Until the rule exists, the test ships in both files and this
   entry is the disclosure.** When it exists, both copies come out and both workflows cite
   it, and nothing else in either file moves.
2. **`BRIEFING_CLAIM_TIER_ACTION_SHAPES`, or a reuse of what the review skill already
   binds.** A5.3 requires an action list at the reader's own claim tier and the test is
   lexical: an aggregate-tier action names a population or a source, a direct-tier action
   names its item. `ROLE_LADDER.claim_tier` supplies the tier and nothing supplies the
   SHAPES. Until it exists the two shapes are the ones A5.3 states, and a run records which
   it used.

## I3. What the reference audits changed

Two reference files were read in full after the first draft, and each produced findings the
draft could not have reached by matching conventions. Both audits are in work/.

**capability-probe.md, seven findings, two serious.**

1. **The probe already contemplates scheduled runs.** `INTERACTIVE` is defined ABSENT for an
   unattended run and 2.14 rung 2 is declared correct for one. A3.1 now states the loops'
   INTERACTIVE split and its constraint: **a scheduled rebuild may not bind anything**, so
   Stage 1 is the only binding window that will ever exist.
2. **4.4 forbids filling a gap with a value carried over from a previous run**, which reads
   as a flat contradiction of CARRIED. A2.1 carves it, and **G-RB-6 and G-RB-7 are what hold
   the carve-out**, which is why they are gates rather than style notes.

Also: the three-place announcement rule does not fit a medium with no audit section (E7); a
standing degradation keeps full prominence every period and a daily artifact is where that
bites (A2.2); `MAIL` is probed for reading only so `SEND` and `SCHEDULER` are missing
coverage rather than adaptations; and 4.5's self-check is harder here than where it was
written (E8).

**field-resolution.md, six findings, one that changed the model.**

1. **DRIFTED is a fifth state and the four could not express it.** F0.1 warns the source is
   never the same shape twice and F0.4 makes it a development-time portability test. This is
   the only workflow that runs that test continuously, because it reads the same sources
   every period for years, and the only one that knows how a concept resolved last period. A
   source whose column was renamed upstream is healthy, parsed, on time, and wrong, and all
   four older states said something reassuring about it. A2.0 adds the state, B1 rung 0 adds
   the comparison that detects it, G-RB-9 requires a banner rather than a line.
2. **This workflow is the bundle's natural dictionary-promotion engine and may never
   promote.** 7.5's fifth criterion is two distinct source periods, which no other workflow
   accumulates and this one crosses by continuing to exist. 7.5 and A3.1 both forbid it
   acting: it proposes into the queue, in the form the binding owner pastes. B6.
3. **F5.6 applies to the identifier and the reason is worth carrying.** An unresolved
   `ITEM_IDENTIFIER` tempts a match on name or location, and each silently widens while the
   briefing stays perfectly self-consistent, attaching one site's open work to another site's
   name. B4 and G-RB-10.

Also: container selection runs every rebuild and F1.6's working-extract rule is itself a
drift signal; 7.7's eleven-class resolution report has nowhere to go in a message and goes to
the durable record, and is deliberately NOT routed through the banner because it fires on
healthy runs (E9); and 3.8 confirmed the FEEDS column from a second file.

**binding-interview.md, ten findings, three that changed the work.**

1. **`BRIEFING_SCOPE` duplicated Q-PERSON-2.** The person script already binds scope and I2
   forbids asking what the records hold. It is now DERIVED, never asked. PART 4 opens by
   promising four questions and no more, and a fifth about the same subject would have made
   that sentence false on every first run.
2. **The schema group had no FEEDS list and 5.2 step 3 requires one.** A group of
   variables with a default and a notice and no declared blast radius leaves an implementer guessing
   which sections an unbound value should cost. The column is now written, and reading it
   as a whole surfaced a property worth stating: an unbound value in this workflow changes
   how the briefing reaches you or what it may assert, and almost never whether it arrives.
3. **"Not defaultable" is not a thing in this model.** 5.2 step 8 says unbound is not a stop
   outside three named values. An unbound delivery time does not stop a run, it stops a
   schedule; an unbound recipient stops a send, not a briefing. Both are now stated that way,
   which is more accurate and removes the only place this workflow claimed a stop the
   doctrine does not grant it.

Also: I11 point 3's duty to list every unasked question lands on every scheduled firing
forever, and the unbound-value queue in 5.2 step 7 is the right home for it rather than the
message (A3.2); PROVISIONAL is a standing label the draft did not carry and it shares A2.2's
rule (A3.3); I10's DECLINED state was missing from the schema; and Stage 1 now states its
own status against the three-stage model, because I3's limit of two deferred bindings per
run would otherwise read as broken.

**the router, the doctrine declaration and the schema index, seven findings, one that
outranks everything else in I4.**

1. **The bundle declared THREE workflows, in five places, and not one of the doctrine
   rules this file cites listed BRIEFING in its `Applies:` line.** Every one read PLANNING,
   REVIEW, SCORECARD, and four read narrower than that. `doctrine/README.md` defined the
   field as "which of the three skills the rule binds", so a fourth value was not legal in
   it, and a reader following any citation out of this file landed on a rule whose own
   scope line excluded the workflow that cited it, which is G1 broken at the level of the
   bundle rather than the deliverable. **It was also silent**, which is why it outranked
   the unassigned group number: an unresolvable variable stops a run loudly at the moment
   it is reached, and a scope line nobody checks stops nothing at all. **The bundle is now
   extended to four and every definition that could have hardcoded how many skills there
   are states none**, so the next workflow costs its Applies lines and nothing else. The
   four narrow rules were SD-BRD-03, SD-EFF-06, SD-EFF-28 and SD-SPN-01, and all four are
   yes for one shared reason: each omits REVIEW because a review is drafted with a present
   person about that one person, and a briefing is the opposite on both counts.
2. **A convention written twice is two conventions**, and SD-FMT-13 says so about its own.
   The date and agreement rules had been written in full in three places in a single
   session. They are now stated once, in the schema group, and cited everywhere else. See
   J4's second paragraph.
3. **`COUNT_NOUN_FORMS` nearly became a second source for a string the bundle already
   binds.** Two singular and plural pairs exist, `UNIT_NOUN_*` in Group 16 and
   `UNIT_OF_BUSINESS_*` in Group 5. Those name a singleton, which is why they are scalars;
   this is an open set, which is why it is a mapping. The validation now says a noun bound
   as a pair elsewhere is never redeclared here.
4. **SD-FMT-13's mechanism says the right fix for the lowercased month is no caser at
   all**, not a careful one, because a run never re-cases anything at build time. The
   helper is gone from the sample build and a comment says why, so nobody adds it back.

Also: the doctrine's own completeness claim reads as an indictment rather than a
reassurance here: this file cites fifty rules of the 481 in the tree, so the other 431 are
not absent but **unread**, which is the state that sentence names as the failure. That ratio
is a measurement of one workflow at one moment and not a target, and it moves every time a
rule is cited; the router's
reference tree names `reference/schema/group-*.md`, a pattern no file in the shipped bundle
matches, which is a defect in the bundle rather than in this work; and the router's claim
that ten values are asked on a first run **survives this group intact**, because all
twenty-five of its variables are DEFERRED or DERIVED and none is ignition tier. That last
one is a property rather than a coincidence and belongs stated: this workflow is a delivery
mechanism over bindings that already exist, and the day it needs an eleventh ignition value
is the day it has stopped being that.

## I4. What remains

1. **Decide what this bundle is, and then declare it.** The bundle declares three
   workflows in five places and every doctrine rule this file cites says on its face that
   it does not govern a briefing. Three options, and they are genuinely different
   artifacts: extend the bundle to four workflows, which means the Skills line, the
   `Applies` field definition, thirty-four `Applies:` lines across thirteen doctrine files,
   the router frontmatter, the router's workflow table, and a fifth key in the
   `HARD_GATES` taxonomy; declare the briefing a variant of PLANNING, which is cheapest and
   buries the distinction Part A is entirely built on; or ship it as a separate bundle that
   cites this one, which keeps the three-workflow declaration true and leaves two trees to
   keep in step and breaks the bundle's own nothing-is-subsetted guarantee.

   **DONE. The bundle is extended to four.** It was the only one of the three that keeps
   both of the bundle's load-bearing properties, and the properties are what make one
   install enough for a user: nothing is subsetted, so a cited rule is never missing, and
   one declared contract per deliverable, so no workflow carries two. What changed is in
   work/declaration-patch.md: the doctrine's Skills line and its `Applies` field
   definition, the router's frontmatter and workflow table and the planning-versus-briefing
   test, the schema index's own opening claim, `HARD_GATES` gaining a fifth group, the
   count-of-three sweep across six files, and the `Applies:` lines of every rule any
   workflow relies on, which the conformance checker now verifies in both directions rather
   than leaving to a number written down here. **Every definition that could have hardcoded how many skills there are
   now states none**, so a fifth workflow costs its Applies lines and nothing else.

   **The three rules scoped narrower than the standard three are answered, and all three
   are yes for one shared reason.** SD-EFF-06 is the two-meanings-of-empty rule, SD-EFF-28
   is publish-once-at-the-end, and SD-SPN-01 is show-the-levels-below-the-requester. Every
   one of them lists PLANNING and SCORECARD and omits REVIEW, and the omission is the same
   omission each time: **a review is drafted with a present person about that one person**,
   so it has no sections that fail to build, no reason to publish whole, and no levels
   beneath its subject. A briefing is the opposite of a review on both counts and the most
   unattended artifact in the bundle, so each rule reaches it a fortiori rather than by
   argument. SD-SPN-01 is the interesting one and it lands exactly where A9 does: at the
   manager altitude it supplies the technician column as attribution, which is the thing
   A9.3 forbids being used as a grouping.
   **And G0 is the sharpest form of it**: the gate convention requires a `doctrine` field
   whose Applies list covers every skill in whose group the gate sits, so until the
   declaration is settled **not one gate in Part G satisfies its sixth field, and by the
   convention's own definition this workflow declares no gates at all.** Everything else in
   this file is subordinate to Part G, and Part G is subordinate to a decision nobody has
   taken.
2. **DONE. The schema group is 26**, `reference/schema/recurring-delivery.md`, subject
   Recurring Delivery. Its row is in the group table and every one of its variables is in
   the index, which is sorted, has no duplicates, and resolves every name this file cites.
   **That is now checked from the group files to the index rather than asserted here**, and
   the first run of that check found two variables defined and unindexed, which is a name a
   run cannot resolve, plus two entries in the index that are not variables at all.
3. **Sweep the doctrine for rules that govern a scheduled unattended artifact and were
   never cited here.** 34 of 481 are cited. The bundle's own words are that the other 447
   are not missing but unread, and three reference reads have produced twenty-seven
   findings between them. The base rate says this finds something.
4. **Apply three patches**, in work/: capability-probe-patch.md for `SEND` and `SCHEDULER`,
   output-contract-patch.md for the message medium, skillmd-patch.md for the router. Each
   names what it assumes and what should be checked before it is applied.
   output-contract-patch.md now carries M13 and M14 as well, so applying it is what moves
   the date and agreement rules out of this file's Part J and into the contract proper.
5. **DONE. A shipped workflow has been read end to end**, standard-gap-scorecard.md, all
   5,255 lines, in order. It produced fourteen major findings and about forty smaller ones,
   written up in work/shipped-workflow-read-notes.md. Six were correctness defects in this
   workflow's own sample or build rather than in its design, and all six are fixed. Three
   structural rules came out of it and are folded in: I5b's three-state verification record,
   M15 and G-RB-13, and G0's gate convention. **The findings recorded below are not yet
   folded in**, and they are the next work. A9 and the second altitude led this list and
   are now done, which is where A5.2 and A5.2.4b came from. What remains, in rough order of
   weight: the carried tripwire counting one state where the wall-of-amber case needs
   every non-current one; G4 having no form for this medium while A1 claims the five rules
   apply unchanged; the empty-period message collapsing a measured zero with a broken
   filter; the schedule feed's rung-2 fallback making a renamed feed permanent and honest;
   source states with no line-qualifier dimension; the four join preconditions; and the
   delivery-deadline departure from SD-EFF-01, which is declared nowhere and which needs a
   cited precedent in the way A7 of the scorecard cites SD-BRD-03.
6. **Write the live-run remediation register**, append-only and pass-numbered, on the model
   the other three workflows carry. The header is the same every time and the last clause is
   the whole point: each item is recorded so nobody reintroduces the sentence that caused
   it. The defects I5 already records are its first pass, and I5 is currently carrying them
   as prose, which is the form that does not survive being added to.
7. **Rewrite Part I6 in the three-field form.** Inputs, expected result, and the failure the
   case catches, with a measured number where the case came from a real defect. The shipped
   workflow carries seventy-three cases in that form, written once and added to since; the
   cases in I6 below are one-liners that name neither the expectation nor the failure.
8. **Run the second altitude. DONE, and it is the single most productive thing in this
   list.** The dataset describes the same date run as the regional manager rather than as
   the technician, and the span rules surviving a move to a new medium was a claim until it
   was a result. Four of the five person-bearing parts transferred unchanged. The fifth,
   SD-SPN-16's peer set, is NOT ADOPTED here on its own arithmetic, which A5.2.3 states.
   What the run actually produced was a defect the narrow altitude could not express at all,
   and the rule that came out of it is A5.2.4b with contract element M16 behind it. **The
   remaining altitudes in the dataset are not optional for the same reason: a rule tested at
   one width is a rule tested at one width.**
9. **Drive it end to end with a hostile agent** on the terms the other three were driven.
   One build is not seventeen rounds, and item 6 is the register those rounds write into.

## I5. What building the sample already caught

**One.** The first render printed a contract tier whose literal value is the word None as
"None - renews 2026-04", which reads as an absent record rather than as a site on file with
no tier. That is the exact collapse this workflow exists to prevent, reproduced by the
renderer rather than the method, and it was invisible in the specification.

**Two.** The reader of the second render caught a lowercased month, `28 september`. The
cause was one call: Python's `str.capitalize()` raises the first character of a string and
lowercases every character after it, so a sentence assembled from fragments and then
sentence-cased loses the capital on any proper noun inside it. By itself that is a typo.
Looking for its siblings found two things that are not.

The message was showing a reader **four renderings of the same kind of date** in one
screen: `2026-09-28` in a label, `28 Sep` in one sentence, `28 September` in another, and
`Tuesday 2026-10-06` in the title. Each was defensible alone and the set was not. A
briefing's entire job is to tell a reader which facts are current, and that is a comparison
between dates; a reader cannot make it quickly across four formats. M13 now binds one
format per precision, and the precision half of it matters on its own: a renewals file
carrying `2027-04` knows the month and does not know the day, so rendering it with a day is
G3, defaulting an unknown to a value the writer chose.

And **five templated counts would have printed `1 stops`, `1 visits`, `1 units on site`,
`1 days old` and `1 units covered`** the first time a technician had a single call. Every
one had been exercised only at many, because the sample data happened to carry many. One
had already been written as `visit(s)`, the parenthetical that SD-LNG-13 names and forbids.
M14 now binds the forms and the three-value test.

**Four, and it is the worst of them.** The build suppressed every section of one stop
because ONE source had no row for it, and that stop had a contract record and three open
work orders in their own files, one a condensate overflow in a data room seventeen days
old. The briefing printed "everything below is omitted rather than guessed" over facts that
needed no guessing. **That is absence in one source read as absence in all, which is the
collapse this entire workflow exists to prevent, committed by the artifact offered as
evidence that it does.** A2.0b rule one and G-RB-12.

**Five.** The build called a hand-made parts export unreadable as a whole. It had three
clean authoritative rows above its own disclaimer, all three for sites on that day's
schedule, including the part for the first stop of the morning, and the build threw all
three away. A2.0b rule two.

**Six, seven and eight came out of running the second altitude**, which is the only place
they could have come from.

**Six.** The subject line said "23 stops. Bellhaven to Cutler Ridge." At the finest
altitude first-to-last is a real route: it is where one person starts and ends. Over a whole
region the same two words are the first and last town in TIME order across three separate
routes, **which is not a journey anybody makes and reads as though it were.** A manager's
day has no first and last town, it has a footprint, so it now says how many towns.

**Seven.** The per-item action line at the aggregate tier said the items "are listed in
R. Alvarez's own briefing, not here." **Nothing in the run establishes that R. Alvarez has
a briefing.** It is the same class of defect as the others: a confident sentence about a
thing nobody checked, and this one invents another artifact.

**Eight.** The same line printed "Nothing here, all the owner's." on an item with no
outstanding actions. A bare pluralising conditional had been written beside `n_of`, which IS
tested at zero, one and many, and was itself never tested at all. **The three-value rule
failed in the file written to honour it, for the third time, and the lesson is narrower than
the rule: a helper that is tested does not protect the conditional written next to it.**
Every pluralising ternary now goes through the same self-test.

**Both seven and eight were found by reading a shipped workflow end to end and applying its
rules back to this one**, which is I4 item 5 doing exactly what its own sentence said it
would. Neither was reachable from this file: the first is caught by the structural-identity
argument a workbook makes about its frozen span, and the second by a parsing rule written
about documents built for the eye. The three reference reads before it changed the design.
This one changed the artifact, and the artifact was wrong in a way the design was not.


**Nine, ten and eleven came out of writing the schema rows for the relief**, which meant
reading the code that implements it closely enough to say what it binds. All three are the
same defect underneath, and it is one this bundle names: a value with two homes.

**Nine.** Each of five standing explanatory sentences was written TWICE in the build: once
at the emit site inside the item loop and once in the declared set, where the declared copy
existed for no purpose but to be matched against the emitted one by string equality.
**SD-FMT-13 is exact about this, and the mechanism it prescribes is deletion rather than
synchronisation.** The obvious failure is benign: edit one copy and the coverage check
reports the emitted line as undeclared and stops the build, which is fail-closed and
correct. **The narrow failure is not benign, and it is the one that would actually have
happened.** The coverage check normalises whitespace before comparing; the share measure and
the relief do not, because they count and replace raw substrings. So a reflowed line, a
rewrapped sentence or a changed double space, which is the kind of edit nobody records
making, passes the coverage check and silently matches nothing in the measure, and that explanation
drops out of the bound and out of the relief while every check reports green. The emit sites
now read their text from the declared set, so identity is a property of the code rather than
a thing a future editor has to maintain. Both artifacts rebuilt byte-identical after the
change, which is what a behaviour-preserving fix is supposed to look like and the reason to
hash them before and after.

**Ten.** A sixth standing explanation was held outside the declared set entirely and
special-cased in four places: the share measure, the coverage check, the relief and the key
block each knew about it separately. **A closed set with a member kept outside it is not a
closed set.** This is the same finding SD-CTR-29 produced when the set declared four while
the run emitted six, arriving by the other road: there the set was short, here the set was
bypassed. A seventh such sentence added later would have been special-cased in four places
too, or forgotten in one of them, and a hole in the relief is invisible by construction
because the symptom is a briefing that is merely longer. It is now an ordinary member with
an empty short form, and **an empty short form is itself a declaration**: it says the
sentence is appended to a varying per-item line and goes away rather than shortening.

**Eleven, and it has more instances than anything else in this list.** Counts stated in
prose had gone stale across every file in this workflow's own folder.

The verification script's docstring opened "Sixteen checks" when it carried thirty. The
build script's comment claimed fifty-eight per cent at the manager altitude, which was the
figure before the correction that narrowed the measure and moved it to fifty-one; the
comment was written in the same pass as the correction that invalidated it. This file said
"the six defects" in I4 and "what the five have in common" in I5, above the same list of
eight. I5b stated the worked example's verification tally in words, and both altitudes had
moved past it. The sample's own README was the worst of them: "Three files" beside a table
of four, "Twenty-three checks" in one sentence, "Twenty checks run" in another, "Two of the
twenty-three" in a third, "All twenty-two applicable checks pass" in a fourth, and "Five
defects this sample caught" heading a list that had outgrown it.

**Every one was written by somebody who had the correct number in front of them at the time,
which is the whole point.** The rule against it is one this bundle already states twice
over: counts live in the taxonomy and nowhere else, and a convention written twice is two
conventions. **The lesson is not to be more careful with numbers.** It is that a number in
prose beside the thing it counts has two homes and the prose copy is the one nobody comes
back to.

Each is now either deleted or replaced by the structural claim it was standing in for, and
in two places that claim is the stronger sentence: the comparison between the two altitudes'
not-applicable counts says more than either count, and "the list is the count" says more
than a corrected eight. **The first draft of this entry opened with a count of its own
instances**, which is either funny or the clearest evidence available that the habit is not
carelessness.

**It is also the second time the same investigative move paid.** M13 and M14 exist because
somebody looked for the siblings of a lowercased month and found two defects that were not
typos. Nine, ten and eleven exist because somebody looked for the siblings of one stale
percentage. The move costs an hour and it has now found five defects in two attempts.

**What they have in common is the argument for shipping a sample at all.** A specification
can be right while its artifact is wrong, and every defect above was invisible in the
specification: nothing in Parts A through H was incorrect, and the message a reader would
have received was. Several were caught by a person reading the output rather than by any
check written against the method, which is why item 5 above is not optional and why the
verification script now ships beside the sample rather than being described in it.

**A note on how those sentences used to read.** This paragraph said "what the five have in
common" while the list beneath it held eight, and the paragraph before it said "the six
defects" while I5 held the same eight. Defect eleven below is that habit, named, and the
fix here is not a corrected number: it is no number, because the list IS the count and a
count stated beside its own list has two homes.

**The quiet day is the one that matters here.** A count template exercised only at many
reads as broken on the first light day, and the first light day is exactly the day a reader
has the time to notice that the tool is wrong. A briefing earns its standing on the days it
has little to say.

## I5b. The verification record has THREE states, and the third one needs a stated reason

Taken from the shipped scorecard's own 5.8, because the argument is not about spreadsheets:
**an assertion that never fired and an assertion nobody wrote are indistinguishable in a
two-state record, and the second is a defect hiding inside a pass.**

So a check whose precondition this run does not contain is recorded NOT APPLICABLE with a
reason drawn from a closed set, and **a not-applicable entry with no qualifying reason is
recorded NOT IMPLEMENTED, which fails.** That is the whole mechanism, and it works because
it makes the failing state the default for anything that could not be evaluated, which is
what G2 requires of a check exactly as it requires it of a cell.

The closed set has five members and the fifth is what keeps it total as the contract grows:
the run binds no source in the state the check reads; no item in the run is in that state;
the medium cannot express what the check reads; the check is scoped to a state or a shape
this run does not have; or the rule the check enforces states its own exemption and it
holds. Anything outside the five is not a reason.

Publish the counts of all three states. **A run reporting many not-applicable entries is
either genuinely simple or quietly untested, and only the counts beside their reasons let a
reader tell which.** The numbers themselves are not restated here, for the reason defect
eleven gives: the tally each run prints is their one home.

**What IS worth stating is the shape, because the two altitudes make the case better than
either number could.** The same checks run against both artifacts. The technician altitude
records several not-applicable entries and the manager altitude records one, from identical
code, because a run over eight items owned by one person genuinely cannot exercise a check
about ordering across owners. **In a two-state record both runs would have read as all
pass, and the narrow one would have been the more reassuring of the two.** The one entry
both altitudes record is DRIFTED: no previous resolution record exists on a first rebuild,
so the sample exercises four of the five source states and says so rather than passing the
fifth vacuously.

---

## I6. Regression cases to write

- A standing explanation written both at its emit site and in the declared set fails
  SD-FMT-13. The emit site reads the declared set, and the two copies are not reconciled.
- An explanation the run emits more than once and does not declare stops the build before
  the send. Found by validating from the emitted explanations TO the set, which is
  SD-CTR-29's direction; validated the other way the same set reports complete.
- A declared set with no entries reports the bound UNENFORCEABLE and never reports it met.
  Zero out of an empty set is a green light that means nothing, which is G2.
- Two states whose relieved wording is identical fail G-RB-16 **even where the key block
  names both**, and the test reads the item lines with the moved block gone. Verified by
  mutation: M15 passes this artifact, which is why the case exists.
- A relief that shortens a per-item FACT rather than a standing explanation fails G-RB-16.
- A relief that drops an item to meet the bound fails G-RB-16. The bound yields instead and
  the briefing says it shipped over it.
- A moved block placed inside an action list fails M16's placement clause, where it reads as
  further things to do rather than as a key to reading the items.
- The repeated share is measured and recorded on every run, **including every run on which
  the relief does not fire**, because a passing measurement is the evidence the check ran.
- A count stated in prose beside the list, set or tally it counts fails SD-FMT-13 on the
  first addition to that list. The list is the count.
- The same checks run at two altitudes and report different not-applicable counts, and both
  runs publish all three states. A narrow run that reports all-pass is the reassuring half
  of a defect.
- An ABSENT source prints its named-absence string and never a zero.
- A CARRIED source is labelled and dated everywhere it appears.
- A measured zero is stated as measured and never collapsed into absence.
- A bound value whose literal is a negation word is not rendered as a missing record.
- The carried tripwire fires and the banner appears above the first item.
- A failed rebuild leaves previous content byte-identical and sends the short notice.
- A delivery run reads no source of record. Verified by observation, not assertion.
- A send to a second address is refused at the gate.
- A cold start omits every change-versus-last-period line rather than computing against zero.
- A period with no items sends the two-line message rather than nothing.
- An extra item-keyed input appears in the briefing with no change to this file.
- A subject line byte-identical to the previous period's fails M4.
- A carried source rendered without its label or date fails G-RB-6.
- A banner softened, moved or dropped while its condition still holds fails G-RB-7.
- A scheduled rebuild that writes to the organization config fails A3.1.
- `SEND` degraded to an unscoped grant produces a written artifact and no delivery.
- A run that reads the xlsx or docx ladders rather than 2.15 and 2.16 fails E6.
- A setup that asks for scope when a person-tier scope is already bound fails A3.1 and I2.
- A scheduled run that does not append an unbound value to the queue fails A3.2.
- A PROVISIONAL label softened on a later provisional run fails A3.3 and G-RB-7.
- A declined binding re-asked at the next setup attempt fails I10.
- An unbound delivery time that stops the briefing rather than the schedule fails the
  feeds list and 5.2 step 8.
- A concept that resolved last rebuild and resolves to a different column now sets DRIFTED
  and raises a banner naming both resolutions.
- A DRIFTED source announced only by a per-line label fails G-RB-9.
- A first rebuild sets no source DRIFTED, because rung 0 has nothing to compare against.
- A source that becomes a person-named working extract raises drift, not a quiet re-score.
- An unresolved identifier omits its sections and never joins on name or location.
- A stem meeting 7.5 criterion 5 is proposed to the queue and never written to the config.
- The resolution report never raises a banner on an otherwise healthy run.
- A resolved-but-full absence rule records the subset as NOT PRESENT rather than as the
  whole population under a second name, per 3.12's proper-subset guard.
- Every day-precision date in a rendered message matches DATE_FORMAT_DAY. An ISO date, an
  abbreviated month, a slashed date, or a day and month with the year dropped fails M13.
- A month-precision source value rendered with a day fails M13, and fails it as a G3
  violation rather than as a formatting preference.
- DATE_FORMAT_WEEKDAY appearing anywhere below the subject and title fails M13.
- **Every templated count is exercised at zero, at one and at more than one before the
  send.** A template that reads correctly at many and prints `1 stops` at one fails M14,
  and it fails on the quietest run rather than the busiest, which is the run a reader has
  time to doubt.
- A parenthetical plural, `visit(s)`, fails M14 outright. It is not a shortcut, it is the
  shortcut SD-LNG-13 names.
- A count whose noun forms are neither bound nor derivable is shown as a labelled figure
  and never written into a sentence.
- No sentence-casing helper is applied to a string that can contain a proper noun. A
  helper that lowercases past the first character fails M14, and this case exists because
  that is what shipped.
- **An item missing from one source carries every other section in full.** A section
  suppressed because a different source had no row for that item fails G-RB-12, and it
  fails it as the one-level-up form of a blank read as a zero rather than as a layout
  defect.
- Every item carries every bound section on every run, and a section with nothing in it
  says why in its own words rather than being dropped.
- **A source whose own author disclaims one of its blocks resolves per block.** Calling the
  whole file UNRESOLVED fails A2.0b rule two, and so does using a value out of the
  disclaimed block.
- A source is called UNRESOLVED only after a second reading has been attempted and
  recorded, and the reading that worked is named.
- An item named only inside a disclaimed block gets a sentence that is neither a value nor
  an absence.
- A bound string ships in the case it was bound in. A run that lower-cases or sentence-cases
  a part name, a site name or any other bound string at build time fails M14, and this case
  exists because it shipped twice.
- **A repeated explanation is relieved without dropping an item, a per-item fact, or a
  state's characters.** A relief that shortens a per-item FACT fails G-RB-16, and so does
  one that leaves two states indistinguishable once their shared wording has moved.
- **The repeated-share measure counts only declared standing explanations.** A measure that
  counts a coincidence of per-item values as waste fails A5.2.4b, and it fails in the
  dangerous direction, because it pressures a run to drop data.
- **Every explanatory line the run can emit is declared in the standing set**, validated
  from the emitted lines to the set. An undeclared repeated line is a hole and the bound
  understates on every run that emits it.
- The moved wording sits above the first item, in its own block, and never among the
  findings. A key placed inside the action list reads as more actions.
- The repeated share is measured and recorded every run, whether or not the relief fires.
- **Every pluralising conditional is exercised at zero, at one and at more than one, not
  only the helper.** A tested helper beside an untested ternary is how "Nothing here, all
  the owner's" shipped.
- **A check tests a distinction and the reachability of its explanation, never a
  placement.** A check that required the words "measured zero" inside an item's own block
  passed only until the relief moved that explanation, and a verification that holds only
  in the unrelieved case is not a verification.
- **A briefing run at an altitude whose span holds people publishes no ordering, grouping
  or count on that level.** A per-person block headed by a name fails G-RB-14, and it fails
  it as the artifact A5.2.0 says arrives disguised as a usability improvement.
- Every item carries the same attribution shape, computed once over the period's own items,
  including an item whose owner is the only one of their kind in that town.
- **A briefing at the finest altitude carries no attribution at all and that is a finished
  state**, not a missing one, per SD-SPN-02's third condition.
- A subject line carrying a count per person fails G-RB-14. So does a banner saying how many
  of the reader's people have a stale source.
- The footer says in plain words that the briefing is not a comparison between the people in
  it, on every run at an altitude where it holds any.
- **No aggregate over a person-bearing level ships at all**, with or without names, because
  both anonymity floors are unreachable in a span small enough to brief. A run that computes
  one and anonymises it has still computed it.
- **An aggregate-tier reader's action list contains no atoms**, and a direct-tier reader's
  contains no shapes. Either fails G-RB-15.
- A filter of one person's slice out of another person's briefing is refused, with the
  remedy named: run the workflow at that person's scope. Fails A5.2.6.
- **This workflow computes no performance figure.** One quoted from a source without the
  second number that source carried fails A1.1, and it fails as G4 broken on the source's
  behalf rather than on this file's.
- **Every state is legible with the stylesheet and every class attribute stripped.** A
  state carried only by colour or weight fails G-RB-13, and it fails on exactly the readers
  least able to recover it.
- No two states share one style, even where their words differ.
- **A verification record carries three states, and a not-applicable entry with no reason
  from the closed set is recorded NOT IMPLEMENTED.** A two-state record that passes a check
  whose condition never arose fails I5b.
- **Every gate carries all six fields of the gate record.** A gate missing any of them is
  not a gate, and a `doctrine` field whose Applies list does not cover this workflow is the
  field that is currently missing on every one of them.
- **No count of gates appears anywhere in this file**, in a table, in prose, in a heading or
  in a parenthesis. Three audits in work/ recorded eleven, twelve and thirteen, each correct
  when written, which is the whole argument.
- A shared gate that cannot apply to a scheduled run resolves NOT APPLICABLE with its
  reason. Silently dropping it fails G0, and so does redefining it here.
- The sample's own verification script passes before any sample is called evidence. A
  worked example whose checks have not been re-run after an edit is a claim, not a result.

---

# PART J: THE SCHEDULED MESSAGE MEDIUM

Interim authority for this medium only, pending its addition to the output contract.

**J1.** The medium is a message, not a built file. The elements of the contract that govern
spreadsheets and documents do not bind it, and the contract must say so explicitly rather
than leave it inferred.

**J2.** The medium's own standards:

- Single column. `MESSAGE_MAX_WIDTH` maximum, `MESSAGE_BODY_SIZE` body, legible on a phone held
  in one hand.
- Character set enforced before send.
- A subject line that is useful unopened: the period, the item count, and the first and last
  location or equivalent anchor.
- Freshness labels inline at the line they qualify, plus the degraded banner at the top when
  B3 fires.
- Which schedule source was used, stated in the first few lines.
- Per item: a header carrying its identifier and its position in the period, then the
  sections bound in `BRIEFING_ITEM_SECTIONS`, then a short numbered list of what to do,
  every entry tied to a line above it.
- Short declarative lines. Numbers before adjectives. No padding, because every line costs
  the reader a scroll in a parking lot.
- **Dates are written in the one convention stated at `DATE_FORMAT_DAY`.** It is stated
  there and cited here, never restated, following the precedent SD-FMT-13 sets for its own
  convention: a convention written twice is two conventions.
- **Every state is carried in CHARACTERS and no two states share one style.** A message
  loses its styling routinely, and on exactly the readers least able to recover it, so the
  words carry the state and the styling is a second channel applied in addition. The
  message is verified against the rendering in which its styling does not arrive, not only
  against the one it was built in.
- **Counts are written in the one convention stated at `COUNT_NOUN_FORMS`.** Same rule,
  same reason. Per SD-FMT-13's mechanism no string is re-cased at build time, so a run
  composes what it writes in the case it ships in and carries no sentence-caser at all.

**J3.** Verification before send: character set, single-send check for the period, recipient
scope, content validated, every figure carrying a resolvable source, and no date rendered
at a finer precision than its source carries. A failure at any of these is a gate in Part
G, not a warning.

Verification at **rebuild**, which is a different moment and a different cost: one date
format per precision across the whole message, and every templated count exercised at zero,
at one and at more than one before its template is promoted into the bound section
standard. These are rebuild gates rather than send gates on purpose. See the second half of
Part G for why a disagreeing count ships rather than stopping a morning.

**J4.** J2's last two bullets and their clauses in J3 are the only part of this file
written after a reader found the defect rather than before. They are kept in the order a
reader would hit them rather than at the end, because an appendix of lessons is a list
nobody reads twice. What they cost is four lines. What their absence cost was a message
that told a technician his work orders were from `28 september`, in the fourth date format
on the screen, above a line that would have read `1 stops` on the first light day of the
month.

They are also both citations rather than statements, and that was the second lesson. The
first draft of them stated each convention in full, here and in the output contract and in
the schema, three identical copies of a rule written in one session. SD-FMT-13 had already
said why that is wrong, about its own convention, in the file this workflow had not yet
read: a convention written twice is two conventions, and the moment of agreement is the
only moment they will ever be identical.
