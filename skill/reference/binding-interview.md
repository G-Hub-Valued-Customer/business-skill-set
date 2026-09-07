# BINDING INTERVIEW

Binding is STAGED. Nobody sits through an eighty-five question interview before
their first monthly plan.

There are three stages and one governing rule.

- **Stage 1, the IGNITION SET.** Eleven organization bindings, gathered in eight
  conversational turns, in under ten minutes. This is everything without which
  the first run would be WRONG rather than merely thinner.
- **Stage 2, PROGRESSIVE BINDING.** Every other organization variable is
  requested at the moment a run first hits a decision that actually needs it,
  never before. The config fills itself in through the BINDING OWNER's own use
  and through the queued request list that everybody else's runs feed, not
  through everybody's runs: a user without ROLE_LADDER.binding_authority for a
  variable is never asked for it, per C1. Where the binding owner grants
  authority to other roles in the Stage 3 audit, those roles start answering too.
- **Stage 3, the FULL AUDIT.** An on-demand pass that walks every unbound
  variable at once, for someone who wants to finish the binding deliberately.
  Same questions, different entry point.

**THE GOVERNING RULE. An unbound variable must never produce a wrong answer. It
produces exactly one of two things: a documented default that is named in the
output, or an honest degradation notice that says what could not be determined
and what was therefore not attempted.**

That is the completeness gate from the doctrine turned on the configuration
itself. Every default and every notice is written out, per variable, in
reference/schema/ SECTION A1 or A2. Nothing in this file may contradict it.

The interview WRITES the config. Nothing here is a hand-edited file. Every
answer is captured, normalized, validated against the rule in reference/schema/,
and written back with the question that produced it, so the next maintainer can
see why a value is what it is.

---

# PART 0: THE RULES THAT GOVERN ALL THREE STAGES

## I1. Two tiers, one wall between them

ORG questions are answered by a person with organizational authority. PERSON
questions are answered by every user. The wall is absolute:

**A PERSON-tier run never asks an ORG-tier question.** Not as a fallback, not as
a quick check, not phrased as a confirmation. A frontline employee does not know
the standing entity hierarchy, the incentive weights, the compliance publisher,
or which rung of the counterfactual ladder the business has bound, and asking
them produces an answer that looks like a binding and is not one.

This rule is what makes Stage 2 safe. A deferred question fires at first need
only when the person in front of it is the right answerer. When it is not, the
default is applied, the notice is printed, and the request is routed to the
binding owner. See Part 5.

The one exception is a value that is genuinely personal even though it looks
organizational: the character limit the user can read off their own open form in
five seconds. That is bound as PERSON_CONFIRMED_FIELD_LIMITS and it overrides
the ORG default for that user's run only. It never writes back to the ORG tier.

## I2. Ask nothing the records already hold

Before any question fires, work the ladder and stop at the first hit:

1. The request itself.
2. The user's own directory record, read in FULL, not only the title.
3. Their manager's record.
4. Stored memory from a previous run.
5. The source file itself, including its distinct values.
6. The filename, or the message that carried the file.
7. Only then, ask.

A user who has just been told the skill knows who they are and what they own
will not accept being asked for their own unit code.

## I3. Batch, never interrogate

If three things are ambiguous, ask about all three in one message. Never ask,
work, then ask again. Never present more than QUESTION_BATCH_MAX questions at
one time. When more than that are outstanding, ask in weight order, highest
first, in successive batches.

In Stage 2 this rule has teeth: at most two deferred bindings may be requested
in any one run, and never more than one before the first output is produced. A
run that stops four times to bind configuration is an interview wearing a
report's clothes.

## I4. Ask in the answerer's language, not the file's

When a question needs the answerer to choose among values present in the data,
offer the distinct values, each labelled with something a person recognizes, and
a count beside each. Accept a name or a list position as the answer, not only a
code.

## I5. Narrow before asking

If a coarser level resolves but a finer one does not, use the coarser level to
narrow the question. A question about eleven options becomes a question about
three.

## I6. Persist the answer and verify the save

Save immediately. Confirm the write returned success. Retry once on failure. If
it still will not stick, tell the answerer plainly, because a failed save means
they get asked again every run.

## I7. Confidence gates every inferred binding

Where the interview proposes a value it inferred rather than one the answerer
supplied:

- HIGH confidence, one clear reading: propose it and ask for a light confirm.
- MEDIUM, a competing reading exists: present both readings and ask which.
- LOW, thin or conflicting: do not propose a value. Ask the open question.

A low-confidence inference never becomes a bound value.

## I8. A vague answer is never rounded up into a binding

Every question carries a VAGUE handling line. The three permitted responses to a
vague answer are: narrow the question with data the skill already has; offer a
small closed set of readings and let the answerer pick; or record the variable as
UNBOUND with the reason. Never take the most convenient reading and write it in.

## I9. Nothing employer-specific is written into skill text

The interview writes values into the config. Skill text references variable names
only. A live host name, a path, an endpoint, a document number or an internal
code that arrives in an answer is stored as the value of a named variable and
never quoted back into a rule.

## I10. A declined question is a recorded state, not a gap

When an answerer declines, or says they do not know, the variable is written as
DECLINED with the date and the reason. A declined variable behaves exactly as an
unbound one: default applied, notice printed. It is not re-asked at every
opportunity. It surfaces again only in the Stage 3 audit, or when a run reaches a
decision where the default is materially worse than an answer would be, and then
at most once more.

## I11. Where INTERACTIVE is absent, no turn and no question in this file fires

The capability probe runs before anything else and it can report INTERACTIVE
ABSENT: a scheduled run, an unattended batch, a pipeline with nobody on the other
end. **Every Stage 1 turn, every Stage 2 catalogue entry, every Stage 3 audit
prompt, every question in the person script and every read-back in this file needs
a person to answer it, so on such a run NONE of them fires.** That is stated here
once rather than repeated at each of them, and it is the same rung
reference/capability-probe.md 2.14 gives for INTERACTIVE ABSENT, expressed in the language of
this file. Where the two ever appear to differ, 2.14 governs, because the ladder is
the authority on what a missing capability does.

Until this rule was written, a reader of PART 6 alone would set out to run an
ignition interview that could not be run, and the file's silence read as an
instruction to try.

What happens instead, in order:

1. **No question is asked and no answer is invented.** Silence is never read as
   confirmation and never as a decline, per SD-CNF-04. A question that cannot be
   asked is not a question that was answered no.
2. **Every unbound variable takes its documented default** from
   reference/schema/ SECTION A1 or A2, and prints that variable's exact degradation
   notice, exactly as it would have done had the question fired and been deferred.
3. **The run lists EVERY question it would have asked**, in the order it would have
   asked them, naming for each one the variable it would have bound and what that
   binding would have changed about this artifact. A bare list of question
   identifiers is not compliant: the list is the thing that makes the run
   recoverable by somebody who was not there.
4. **Nothing is written to the ORG config.** An inference made to get this run out
   is used for this run, disclosed, and never persisted, because I7 holds and no
   authorized answerer looked at it. This is the same wall PART 6 puts around a
   frontline user's provisional run, for the same reason.
5. **The run is PROVISIONAL where any ignition variable is unbound**, at the
   standing prominence, and the forwardable block that PART 6 step 5 would have
   spoken is WRITTEN INTO THE ARTIFACT instead, so somebody can still send it on.

**A RUN THAT CANNOT ASK IS NOT A RUN THAT MAY GUESS.** The only difference between
this path and an interactive first run is that the questions are printed rather
than asked, and the answers are defaults rather than answers. Nothing else about
the output changes: the same sections ship, the same gates run, the same notices
print.

---

# PART 1: STAGE 1, THE IGNITION INTERVIEW

Ten ignition bindings, plus the owner's address, which is asked in the same
breath and is deferred rather than required. Seven questions and a close. Under
ten minutes with someone who knows the business.

It is written as prose because that is how a competent person actually asks
these things. There are no question numbers, no blocks, and no form. The
interviewer holds those targets in mind and converses toward them.

## What Stage 1 must come away with

| Binding | Why it cannot wait |
|---|---|
| ORG_NAME | Every notice and header names the organization. |
| BINDING_OWNER_NAME | A degradation notice must say who can fix it. |
| SCOPE_LEVELS | Without the containment chain a filter can silently return the wrong population and a peer set can compare someone to their own subordinates. Turn 2 elicits the chain DOWN TO AND INCLUDING one unit of business; a chain that stops one level short, at the finest OWNED level, silently suppresses the ranked list of every frontline reader. |
| ROLE_LADDER | Claim tier decides what a person may claim; guessing it is fatal in both directions. Turn 3 elicits the ORDER; every sub-field it does not elicit is DERIVED and read back, per SD-CTR-26, so a bare ordered list of role names completes this binding. |
| POPULATION_SHAPE | Decides what the denominator is; the wrong model mixes closed and open work into one figure and the reader cannot recover it. Turn 4 elicits the unit noun and runs the three tests; where the tests cannot be run conversationally, `mode` is DERIVED by SD-POP-24 from the data and read back in the close. |
| COUNTERFACTUAL_AVAILABLE_RUNGS | Decides what second number every figure carries. |
| COUNTERFACTUAL_DEFAULT_RUNG | Decides how strongly every claim may be worded. |
| MOVING_GROUND_NAME | A claim may not ship at achievement strength until the business has named what moves underneath it. |
| PLANNING_PERIOD_NAME | Half of the operating window. |
| PLANNING_PERIOD_LENGTH_DAYS | The other half. A run that plans the wrong period is indistinguishable from a correct one until someone is standing in front of the work. |

## How to open

> I need about ten minutes to point this at your business, and then it works. I
> am going to ask you seven things, and then ask whether you have a real file I
> could look at. Everything else it needs, it will ask for
> later, once, at the moment it actually needs it, and only from someone who
> would know the answer. Where you are not sure, say so and I will write down
> that it is unset. It will then say plainly what it could not do rather than
> making something up.

## Turn 1: who you are and who owns this

> First, the easy one. What is the organization called, and who should people
> contact when this thing gets something wrong or needs tuning? A shared mailbox
> is better than a person, because whoever answers it in two years is the one who
> matters.

BINDS: ORG_NAME, BINDING_OWNER_NAME, BINDING_OWNER_CONTACT.
GOOD: a name, a role or team, and a reachable address.
VAGUE: a personal name with no address. Ask for an address and say why. Every
report carries the same invitation and the same address, and an unreachable one
turns the invitation into decoration.

**THE ADDRESS IS ASKED FOR HERE AND IS NOT AN IGNITION BINDING.** ORG_NAME and
BINDING_OWNER_NAME are ignition; BINDING_OWNER_CONTACT is DEFERRED, with a
documented default and a standing disclosure in reference/schema/ SECTION A1. This
is the right turn to ask for it, because the person answering knows it and will
never be cheaper to ask, and it is not an ignition binding because it is the ONE
value that a binding built from an organization's own documents can never supply:
no internal policy document carries a mailbox, and inventing one is forbidden. As
an ignition variable it stamped every documents-bound run PROVISIONAL forever on
the one thing no amount of care could clear. Ask for it, take a no gracefully,
and move on: an unbound address costs a posted notice, not a sound binding.

**BINDING_OWNER_NAME IS THE ONE ANSWER THIS TURN MAY NOT LEAVE WITHOUT.**
It is not unskippable because a name is precious. It is unskippable because two
separate machines stop working without it, and both of them are invisible to the
person declining.

Machine one: every degradation notice this toolkit ever prints ends with an
addressee. With no owner named, the notice ends with nothing, and a gap that
nobody is told to fix is a gap that stays open for the life of the deployment.

Machine two, and this is the one nobody sees coming: progressive binding itself
is gated on binding authority, and authority is ADDITIVE. Two standing grants run
at all times, per SD-CTR-25: the named owner holds `ALL`, and the most senior role
on ROLE_LADDER also holds `ALL`, whether or not an owner is named. Naming an owner
never removes an answerer; it ADDS one, and usually adds the only one who is not
also the busiest person in the building. With no owner named, every Stage 2
question waits for whoever sits at the top of the ladder to happen to run the tool
personally. In a company where that person never does, Stage 2 never fires at all,
and the toolkit stays at its ignition set forever while appearing to work.

So this turn does not accept silence, and it does not accept a shrug. If the
answerer will not name an owner, say this to them, in these words or close to
them:

> I can carry on without it, but I want you to know what you are choosing. If
> nobody owns this, then every time it hits something it does not know it will
> print a gap with nobody to send it to, and the questions it saves up for later
> will only ever be answerable by whoever is most senior on your role list, in
> person, at the moment they happen to run it themselves. If that person does not
> personally run this thing, it will never learn anything after today. Naming
> somebody does not take that away from them; it adds a second door. A shared
> mailbox and a team name is enough. It does not have to be a person and it does
> not have to be permanent, because it can be changed in Stage 3 in about a
> minute.

Then ask once more.

DECLINED, after that: record BINDING_OWNER_NAME as DECLINED, not as UNBOUND. The
standing senior-role grant in reference/schema/ SECTION A1 for
ROLE_LADDER.binding_authority still stands, because it always stands. Print the
consequence at the top of the first report produced under the declined state, not
only in the gap list:

> No owner is set for this toolkit. Gaps it finds will be reported to nobody, and
> its deferred questions can only be answered by {most senior role in
> ROLE_LADDER} at the moment they run it themselves. Setting an owner adds a
> second answerer without taking anything away from the first. It takes one line
> and is the single highest value minute anyone will spend on this.

A DECLINED owner is a recorded state under I10 and it is re-offered at the top of
every Stage 3 audit until it is set. It is never silently re-asked of a frontline
user, because naming an organization's binding owner is an ORG-tier act and I1's
wall holds.

## Turn 2: the shape of the organization

> Walk me from the whole company down to ONE of the things this will put on a
> list: one account, one claim, one site, whatever your version of that is.
> Include every level in between, and finish on that smallest thing itself. Use
> the words your people actually use, not the ones on the org chart.

BINDS: SCOPE_LEVELS, and by derivation SCOPE_TOP_KEY, SCOPE_FINEST_KEY and
UNIT_LEVEL_KEY.
GOOD: an ordered chain of two to seven names WHOSE LAST ENTRY IS ONE UNIT OF
BUSINESS, not a person's patch of them.

**ASK FOR THE LAST LEVEL EXPLICITLY, BECAUSE NOBODY VOLUNTEERS IT AND THE OLD
WORDING ASKED FOR THE WRONG ONE.** This turn used to say "down to the smallest
piece one person owns". Answered honestly at an organization whose smallest owned
thing is one person's book, that produces a chain that stops at the book, one
level short of the account. The consequence is not a thin report, it is a
suppressed one: the unit-level detection finds no level whose distinct value count
matches the record count, falls back to the finest level in the chain, concludes
the reader owns exactly ONE unit, and removes the ranked list, the percentile and
every comparative sentence from the artifact of a person with dozens of live
units. Every gate passes while it happens. The full statement of the mechanism is
in reference/schema/ GROUP 3, and it is the reason the wording of this turn
changed.

**THE TWO LEVELS AND THEIR TWO NAMES.** The LAST level of the chain is the thing
on the row and it becomes UNIT_LEVEL_KEY. The smallest thing anybody OWNS is one
level above it and it becomes SCOPE_FINEST_KEY. Nobody's scope is one row, so no
role is ever recorded as owning the last level. Both are derived from this one
answer, which is why this turn asks for a chain and not for two separate things.

VAGUE, the chain stops at a person's book, patch, territory, panel or portfolio:
that is the finest OWNED level, and one level is missing. Ask the follow-up in
their own words:

> And inside one of those, what is the thing itself, one at a time, that ends up
> as a single line on a report?

Add that answer as the last level. If they say the two are genuinely the same
thing, that is a two-level organization and it is legal; record it and say that
the smallest owned thing and the ranked thing are the same, so no peer comparison
below the top exists.

CHECK BEFORE MOVING ON, in one sentence: read the last level back and ask whether
one person can own several of them. If yes, the chain is one level short.

VAGUE, mixed geography and function: split it. Ask which of those levels a
person is measured against, and which is a cross-cut. Only the containment chain
goes in; the cross-cut becomes a qualifier dimension and is bound later.
VAGUE, a matrix: ask directly whether every unit belongs to exactly one owner at
each level, yes or no. If no, note it and bind SCOPE_ATTRIBUTION_IS_TREE at the
first attribution decision rather than now.
DECLINED: cannot be declined. If the answerer genuinely does not know the
hierarchy, they are the wrong answerer, and say so plainly and courteously.

## Turn 3: who uses it and what they may claim

> Now the roles, junior first, and for each one tell me which of those levels
> they own. Then one more thing about each: when something goes right at the
> smallest level, is that their own hands, or did someone on their team do it?

BINDS: ROLE_LADDER, with keys, display names, scope level and claim tier.
GOOD: an ordered list of roles mapped to levels, with a clean split between the
people who do the work themselves and the people whose team does.
VAGUE, "both": that is a real answer and it has a name. Record the role as direct
for the units they personally work and aggregate for the rest, and note that the
two are never blended in one sentence.
VAGUE, no levels given: ask level by level. Who owns one of these, who owns a
group of those, and so on.
DEFER FROM THIS TURN: titles and abbreviations, seniority variants, specialist
roles, the fallback role, and the people-leader requirement. All are Stage 2.

**THE NATURAL ANSWER TO THIS TURN IS A BARE ORDERED LIST OF ROLE NAMES, AND THAT
MUST BE ENOUGH.** SD-CTR-26. A co-operative person hears "the roles, junior
first" and gives you five job titles in order. That is a good answer to the
question as asked, and it is the answer this turn will get most of the time. It
does not name a scope level per role and it does not name a claim tier, and an
earlier revision therefore left ROLE_LADDER failing its own ignition validation
off a fully co-operative answer and stamped every artifact PROVISIONAL forever
without telling anyone.

**DO NOT SOLVE THAT BY ASKING MORE QUESTIONS. DERIVE, THEN READ BACK.**

**THE DERIVATIONS ARE NOT RESTATED HERE. THERE IS ONE STATEMENT OF EACH AND IT IS
THE SECTION A1 ROW FOR THAT SUB-FIELD IN reference/schema/.** Run the derivation
as that row states it, and read the result back.

An earlier revision of this turn carried its own summary of the scope-level and
claim-tier derivations, and the summary and the A1 row had drifted apart into two
INCOMPATIBLE procedures. The summary anchored the junior end on the FINEST level
outright; the A1 row anchors at BOTH ends with the junior anchor one level ABOVE
the unit. On an ordinary five-level chain the summary produces an unowned top
level, a head of the organization demoted a rung, and a most-junior role sitting
AT the unit level, which the bundle itself then reports as a binding error under
SD-POP-26. The invariant that a fully answered interview produces a NON-PROVISIONAL
run holds only on the A1 reading, and this file is what an implementer reads FIRST.
A second statement of a procedure is a second procedure, however carefully it was
copied on the day it was written.

The sub-fields this turn leaves to derivation, each with its one home:

| Sub-field | Where its single derivation is stated |
|---|---|
| `scope_level` | its SECTION A1 row |
| `claim_tier` | its SECTION A1 row |
| `altitude_ceiling`, `report_line`, `peer_level`, `titles`, `is_specialist`, `has_reports_default` | their SECTION A1 rows |

What this turn owns, and states once, is the SHAPE of the outcome rather than the
procedure that reaches it: the most junior role ends up owning the smallest thing
anybody actually owns, the most senior role ends up owning the whole organization,
exactly one level is DIRECT, and every level above it is AGGREGATE. If a derivation
you have just run does not produce that shape, you have run it wrong, or the answers
are inconsistent, and either way it is read back and corrected rather than written.

Then say what you derived, in the same breath, in their words, and let them
correct it in one line:

> So: {junior role} owns one {finest OWNED level, per SCOPE_FINEST_KEY} and does that work themselves;
> {next role} owns a {next level} and their team does it; {and so on}. Correct
> me on any line that is wrong.

A correction makes that line ANSWERED. Silence leaves it DERIVED, which SATISFIES
ignition and is recorded with its derivation named, not as a gap. This read-back
is the ONLY place in the bundle where a medium-confidence value may be written to
the ORG config, and it is legitimate because a person with authority is looking at
it. I7 is untouched: a RUN may still never do this.

## Turn 4: what is being ranked, and whether the list of them holds still

> What does this thing rank, one at a time? And think about a list of every one
> of them: six months from now, is it broadly the same list, or is it a different
> list because things came in and went out?

BINDS: POPULATION_SHAPE. A KEYED SET, not a single answer. Most businesses
declare one population. Some honestly have two, and the interview must be able to
record that rather than forcing a choice.

This turn does not stop at the answer. The words people use do not reliably
distinguish the two shapes, and two of the three tests below pass at almost every
business. Run all three, conversationally.

**Test 1, the roster test.**

> Could you hand me a complete list of all of them as of today, without caring
> what stage each one is in?

A confident yes is evidence of a roster. It is not a conclusion.

**Test 2, the entry and exit test.**

> Does each one have a date it started being yours and a date it stops being your
> problem?

Yes to both is evidence of a pipeline. It is not a conclusion either. A roster of
standing positions passes this test whenever its members carry an opening date
and a term.

**Test 3, the replacement test. This is the one that decides.**

> When one of them leaves, does it leave a hole somebody notices and moves to
> fill, or does the next one just take its place in the queue?

A HOLE means the unit is a standing position in the business. The population is a
FIXED roster whose members happen to be dated, and those dates are unit
attributes rather than a pipeline.

A QUEUE means FLOW.

**RESOLUTION: RUN SD-POP-24. THIS TURN DOES NOT RESTATE IT.**

What this turn owns is the WORDING OF THE THREE QUESTIONS above, which is
conversational and belongs here. What it does NOT own is what to do with the
answers. SD-POP-24 is the single shape detection procedure in this bundle: it
states which tests decide, in what order, when the tie-break may be consulted, and
what is recorded. Read the answers into it and take its result.

That separation is deliberate and it is the same lesson Turn 3 learned the hard
way. A second statement of a procedure is a second procedure, however carefully it
was copied on the day it was written, and the two then drift into giving different
answers off one set of answers.

One case does belong here, because it changes what this TURN does rather than what
the procedure concludes: where the roster test passes over CONTAINERS and the
entry-exit test passes over the things moving across them, that is not one
population answered badly. It is TWO populations. Declare both, give each its own
key, mode and unit noun, and say so:

> It sounds like you have two of these: a list of {containers} that mostly holds
> still, and a stream of {items} moving across them. Those get scored differently
> and I would rather record both than make you pick. Is that right?

**IF THE ANSWERER GIVES YOU A NOUN AND NOTHING ELSE, THAT IS STILL ENOUGH.**
SD-CTR-26. Asked what this thing ranks, a co-operative person says one word, the
name of the thing, and stops. That is a complete answer to the question as asked
and it binds the population's unit noun. It does not bind `mode`, and an earlier
revision therefore failed ignition validation off a fully answered interview.
Where the three tests above cannot be run conversationally, because the answerer
has moved on or does not think in these terms, `mode` is DETECTED from the data by
SD-POP-24 and recorded as DERIVED with the tests that fired and their evidence.
DERIVED satisfies ignition. Read it back in the Turn 8 close with the other
derived values, in their words:

> One more thing I worked out rather than asked: your {unit noun} look to me like
> {a list that mostly holds still / a stream of work moving through}, because
> {the evidence}. Tell me if that is wrong, because it changes what every number
> in these reports is a share of.

**WHY THE OLD RULE WAS WRONG.** The previous version treated tests 1 and 2 both
passing as a conflict and preferred FLOW, on the grounds that a flow model over a
roster is harmless. It is not harmless where the dates are real: it cohorts
standing positions by the year they opened and produces a comparison nobody asked
for. See SD-POP-23 and SD-POP-24.

DEFER FROM THIS TURN: the stage list, the open rule, the cohort basis, the reopen
rule, the enumeration source, the churn tolerance, the not-actionable flag and the
different-model class. All Stage 2, all conditional on mode, and all of them carry
a documented default and a notice in reference/schema/ SECTION A2.

## Turn 5: the second number

> Every number this thing prints will carry a second number that the person
> writing it did not choose. Without one, a true figure is an orphan: it does not
> say whether anything was beaten or whether the ground just moved. So: which of
> these can you actually produce?
>
> A share of a set you could have reached. A comparison against a group inside
> your own business that did not get the treatment. The spread across peers doing
> the same job. Attainment of a plan somebody else set before the period started.
> Your own run rate last period. Or, at the very least, a plain count that bounds
> the size of the claim, forty-seven of sixty-one.

BINDS: COUNTERFACTUAL_AVAILABLE_RUNGS, and the definition of every rung named.

GOOD: a subset. The last one is always available and is the floor.

**THE FOLLOW-UP IS UNCONDITIONAL, NOT A BRANCH.** For every rung they name, ask
its test immediately, in the same breath. This is not something to do only when
somebody says "all of them"; a crisp subset answer needs it just as much, and a
crisp answer is what most people give.

> - You said you can do share of a set you could have reached. What exactly is
>   that set, and which column counts it?
> - You said you compare against an untreated group. What is that group, and what
>   makes it comparable?
> - You said you rank peers. Are those peers inside this organization, or in a
>   published comparison group somebody else maintains? WHAT KIND OF THING is a
>   peer: is it another {each level in the chain, offered by name}? And roughly how
>   many are there?
> - You said attainment against a plan. Where does the plan live, and who sets
>   it?
> - You said your own run rate. Against what exactly: the same window last year,
>   or the window just gone?

**A RUNG NAMED BUT NOT DEFINED IS NOT AN AVAILABLE RUNG. Strike it and say so.**

BINDS, per rung answered: ADDRESSABLE_POPULATION_DEFINITION and
ADDRESSABLE_POPULATION_CONCEPT; CONTROL_GROUP_DEFINITION; PEER_SET_LEVEL_DEFAULT,
PEER_SET_IS_EXTERNAL, EXTERNAL_PEER_SET_SOURCE and PEER_SET_ANCHOR_PERIOD;
PLAN_SOURCE_NAME and PLAN_SET_BY_ROLE; PRIOR_PERIOD_BASIS.

**BIND THE PEER LEVEL HERE, IN THE SAME ANSWER THAT GIVES THE COUNT. DO NOT
COLLECT ONLY THE COUNT.** This turn previously asked how many peers there were and
never what kind of thing a peer IS, so PEER_SET_LEVEL_DEFAULT went unbound and fell
to its documented default, the level one step coarser than the requester. At an
organization whose peers are the several people at the requester's OWN level, that
default contradicts the count the interview had just collected, and the
contradiction is not cosmetic: it decides whether a peer comparison happens at all.
A count of five with a derived level that yields no peer set produces NO comparison
where the answerer plainly described one.

**WHERE THE ANSWERER NAMES A LEVEL, BIND IT.** That is the whole of the ordinary
case. Where they give only a COUNT, derive the level from the count and say you
did: take the level in SCOPE_LEVELS whose sibling count at the requester's position
is CLOSEST to the number they gave, and read it back for correction with the other
derived values in Turn 8. A stated count is evidence about the level; treat it as
such rather than discarding it.

**THE PRECEDENCE, STATED ONCE AND CARRIED IN THE A1 ROW: A STATED PEER COUNT
OUTRANKS THE ONE-STEP-COARSER DERIVATION WHERE THE TWO DISAGREE.** The derivation
is a fallback for when nobody said anything. It is not evidence, and it does not
override somebody who told you the answer.

NOTES ON THE PEER ANSWER, because it is the one most often mis-recorded:
- Fewer than four peers means a positional claim identifies a person by
  elimination, and the rung is kept but the run generalizes rather than ranks.
- An EXTERNAL peer group is a legitimate and very common answer, and it is bound
  differently: it names a publication and a refresh cadence, and it is never
  forced into the organization's own containment chain, which holds only units
  the organization owns. A group refreshed annually and read quarterly is stale
  for three quarters of the year, and that is stated beside every figure.

VAGUE, "we have nothing like that": then the floor is the answer, and move on.

Then, in the same breath:

> And of those, which one should be the default when nothing else applies?

BINDS: COUNTERFACTUAL_DEFAULT_RUNG.

**THEN THE SCOPING QUESTION, and it is not optional.**

> Is there any part of the business where one of those is not true? A new line, a
> new market, a new category, a site that opened this year, an acquisition still
> on its own systems. If so, name it, because that part gets a different second
> number and I will not let it borrow yours.

BINDS: COUNTERFACTUAL_RUNG_SCOPES.
WHY: rung availability is a property of a population, not of a company. A mature
business answers this turn honestly for itself and the answer is false for the
launch inside it. Without this question the launch inherits comparisons it cannot
produce, and the run computes a share against a denominator the writer's own team
is currently building.
IF THEY NAME NOTHING: that is a fine answer. Cold populations are also DETECTED
at run time from the data, per SD-CLM-28, so this question improves the answer
rather than being the only defence.

## Turn 6: what moves underneath

This turn is required and it has no skip.

> Last year somebody here had a number that went up and it still was not good,
> because something moved underneath it. What moved?

BINDS: MOVING_GROUND_NAME.
GOOD: a named external or systemic force.
VAGUE, "nothing moves, we are not in a market": reframe once, and do not accept a
no.

> Then answer it differently. If every one of your people did exactly the same
> work next year as this year, would the numbers come out the same? What would
> make them different?

Volume, seasonality, mix, staffing, an upstream policy change, a rate change made
above them, a weather year, a regulatory deadline. Every business has one. Record
whatever comes back, however unquantified.
STILL UNANSWERED: record it as unbound and say what will happen. **THE
CONSEQUENCE IS STATED IN ONE PLACE, the third column of the ignition table in
reference/schema/, and this turn quotes it rather than inventing its own version.**
An earlier revision of this turn stated the consequence in its own words while the
binding-states table stated a different one, and two readers produced two different
artifacts off the same binding state. Say it to the answerer in these terms:

> Every claim will then be printed with its denominator and none of them will be
> worded as an achievement, and the report will carry a provisional label until
> somebody names this. That is the honest outcome and it is not a threat, it is
> the contract.

Both halves are true and they are not alternatives: the capped claim strength is
what the run DOES differently, and the provisional label is what the artifact SAYS.
Never state one as though it were the whole consequence.

## Turn 7: the period

> What do you call the window a plan covers, and how long is it?

BINDS: PLANNING_PERIOD_NAME, PLANNING_PERIOD_LENGTH_DAYS.
GOOD: a name and a length.
VAGUE, "it depends": ask how many of them there are in a year. Twelve, thirteen,
four, or fifty-two answers it.
WHY IT CANNOT WAIT: a plan built against the wrong window mis-weights every due
date in it, and nothing in the output looks wrong until somebody is standing in
front of the work.
DEFER FROM THIS TURN: where the real dates are published, the derivation rule,
the plan-ahead rule and the review points. All Stage 2, all defaulted and
disclosed.

## Turn 8: the close, and the offer of a file

> That is everything I need to start. Two last things. Do you have one real data
> file I could look at now? Five minutes on a real file is worth more than
> another hour of questions.

If yes, run the field resolution pass live, report which concepts resolved, which
did not, and which columns had no home, and add the resolved stems as seed data.
This is the single highest-value five minutes available and it converts a dozen
Stage 2 questions into answers nobody had to give.

If a second file from a different period is available, run the portability test
and report every difference between the two.

**BEFORE ANYTHING IS WRITTEN, RUN THE IGNITION COMPLETENESS CHECK AND SHOW ITS
RESULT.** SD-CTR-26. Walk the ten ignition variables and, for the three that
are taxonomies, every sub-field each of them requires. Put each in exactly one of
three states: ANSWERED, DERIVED, or DEFAULTED. Then read back EVERY DERIVED line
in one table, in the answerer's own words, and invite a correction:

> Two of these I worked out from what you told me rather than asking you
> outright, because you had already given me enough. Here they are. Correct any
> line and I will take yours.
>
> | What | What I have | How I got it |
> |---|---|---|
> | {sub-field in plain words} | {value in their words} | {the derivation in one clause} |

A correction promotes that line to ANSWERED. Silence leaves it DERIVED, and
DERIVED satisfies ignition.

**THEN STATE THE COMPLETENESS RESULT IN PLAIN WORDS, AND IT IS NOT OPTIONAL.**
The answerer must never leave believing they finished when they did not:

> That completes the setup. Nothing in the core set is missing, so your reports
> will be normal reports, not provisional ones.

or, where something genuinely could not be settled:

> One thing is still open: {the variable in plain words}. Until it is set, every
> report will be marked provisional and will say why. It takes about a minute
> whenever you want to close it.

**IF THE CHECK FAILS OFF A FULLY ANSWERED INTERVIEW, THAT IS A DEFECT IN THIS
BUNDLE, NOT IN THE ANSWERER.** Record it as such: name the variable, name the turn
that should have elicited it or the derivation that should have computed it, and
say so in the report rather than blaming the interview on the person who sat
through it.

Then close:

> Here is what I have bound, here is what I could not, and here is what each gap
> will cost. Everything else it needs, it will ask for once, when it hits the
> decision that needs it, and only from someone who would know. You can also tell
> it to finish the whole configuration in one sitting whenever you want, and it
> will walk the rest.

Write the config. Report four counts, never three: ANSWERED, DERIVED, DEFAULTED
and DECLINED. Every derived value is written with its derivation named beside it,
so a later audit can see what was computed rather than stated.

## What Stage 1 explicitly does NOT do

It does not lock the org tier. BINDING_LOCKED stays false, because Stage 2
depends on the tier being open. It is set true only at the end of a Stage 3
audit, or when the binding owner says so.

It does not ask about entities, measures, work types, priorities, lineage,
compliance, the deliverable, the review form, systems, language, run control or
seed vocabulary. Those are the sixteen blocks that used to sit in front of the
first run, and every one of them now waits for a decision that needs it.

---

# PART 2: STAGE 2, PROGRESSIVE BINDING

## 2.1 How a deferred question fires

A deferred question fires when, and only when, a run reaches a decision that
needs its value. It never fires on a schedule, never fires because the config
looks incomplete, and never fires ahead of the decision.

When it fires, the skill says four things in this order, and then asks:

1. **The decision it is facing.** Not the variable name. What it is about to do.
2. **Why the value is needed for that decision.**
3. **What it will do if the answerer declines**, quoting the documented default
   and the degradation notice from reference/schema/ SECTION A1 or A2, in plain words.
4. **The question.**

Then it records the answer to the config, confirms the save, and never asks
again.

The shape, worded generically:

> Before I rank these I have to decide {decision}. I do not have {plain-language
> name of the value} for {ORG_NAME}. If you would rather not answer now, I will
> {documented default}, and the report will say: {degradation notice}. That is a
> real answer and it is safe. But if you know it, one line saves it forever:
> {question}.

## 2.2 The four constraints on firing

- **C1. Right answerer only, and it is a LOOKUP, not a judgment.** A deferred ORG
  question fires only to the binding owner, or to a user whose
  ROLE_LADDER.binding_authority names the schema GROUP that variable sits in.
  **AUTHORITY IS ADDITIVE, AND ITS DEFAULT IS A UNION OF TWO STANDING GRANTS**,
  per SD-CTR-25: the named binding owner holds ALL whenever a name is recorded,
  AND the most senior role on ROLE_LADDER holds ALL whether or not an owner is
  named. Naming an owner NEVER removes an answerer. An earlier revision of this
  bullet said that where binding_authority is unbound only the binding owner is
  ever asked; that is the replacement reading, it is wrong, and it is the exact
  regression SD-CTR-25 exists to forbid. To anyone holding neither grant the
  default is applied, the notice is printed, and the request is queued to the
  binding owner. The run names WHICH grant authorized any question it fired. See
  Part 5.

  This test used to be unevaluable. Nothing in the bundle said which roles carry
  which authority, so the constraint could not be tested, and a constraint that
  cannot be evaluated has failed, per SD-EFF-03. The safe reading was that no
  deferred question ever fires for anybody but the binding owner, which is what
  the field now says explicitly rather than by accident. The unsafe reading, which
  an implementer wanting the mechanism to work would have reached for, is to infer
  authority from seniority, and that hands a senior operator a question about
  entity weights, which is the wall this rule exists to be.
- **C2. At most two per run, and never more than one before the first output.**
  A run that stops four times to bind configuration is an interview wearing a
  report's clothes.

  **THE BUDGET COUNTS ORG-TIER QUESTIONS. IT DOES NOT COUNT FILE QUESTIONS, AND
  THAT IS WHAT RESOLVES THE COLLISION WITH I3.** I3 says batch everything into one
  message; C2 says at most one before the first output. Read as one budget over one
  kind of question, the two collide the moment two questions are outstanding at
  once, and an implementer must either break the batch or drop a question. They do
  not collide, because they govern different things:

  | Kind | What it asks | Counts against C2 | Answerable by |
  |---|---|---|---|
  | ORG-TIER BINDING QUESTION | what the organization's configuration should be: a threshold, a weight, a level, a policy | YES | only a holder of a standing authority grant |
  | PERSON-TIER FILE QUESTION | what something in the file the user just supplied MEANS: which column, which values, which of these candidates | NO | anyone running the tool, including a frontline user on a fully unbound first run |

  **EVERY QUESTION UNDER FIELD RESOLUTION IS A FILE QUESTION.** That includes
  F5.1's own step 5, the required-concept question, which was previously the one
  the tier of was never stated. It asks which column in the user's file holds a
  thing; it does not ask what the organization is. It therefore sits outside the
  ORG budget exactly as F5.1a and F5.1b do, needs no binding authority, and never
  crosses I1's wall. An earlier reading that made it ORG-tier would have meant a
  frontline user could not be asked which column held the identifier in their own
  spreadsheet, which is absurd on its face.

  **FILE QUESTIONS HAVE THEIR OWN BUDGET, AND IT IS ONE MESSAGE, NOT ONE
  QUESTION.** All outstanding file questions are batched into a SINGLE message per
  run, per I3, however many there are, because they are answered by the person
  already sitting there looking at their own file and answering three at once costs
  them one interruption rather than three. Where two class-1 questions are both
  outstanding, both are asked, in one message, and neither consumes the ORG budget.
  Cap the batch at FILE_QUESTION_BATCH_CAP items and report any beyond it as
  unasked, so a pathological file cannot turn one message into a form.
- **C3. Highest-cost gap first, AND COST IS MEASURED ON THIS RUN, NOT READ FROM A
  TABLE.** Where several are outstanding, fire the one whose default is materially
  worse than an answer would be. Cost is how far the default moved a published
  number on THIS file, not how interesting the variable is.

  **THE ORDER IS COMPUTED, NOT STATIC.** A cost order fixed at authoring time
  cannot know which questions matter on a file it has never seen, and the failure
  is not hypothetical: a run spent its whole budget on a question whose default
  changed nothing observable, while the question deciding whether eleven units
  that had already given notice of exit sat inside a published plan was pushed out
  of budget entirely. The static table ranked the decorative question above the
  one that moved two rows into a top ten.

  **COMPUTE THE COST OF EVERY OUTSTANDING REQUEST BEFORE FIRING ANY OF THEM.** The
  run has already applied every default by the time it can publish anything, so
  the counterfactual is cheap: for each outstanding request, count what the default
  changed in the artifact this run is about to produce.

  | Rank | Class | The test |
  |---|---|---|
  | 1 | CHANGES MEMBERSHIP OF A RANKED LIST | the default added or removed at least one row from a published action, reference or exception list. Any question in this class JUMPS THE QUEUE, ahead of every class below, whatever the static table says. |
  | 2 | CHANGES A PUBLISHED ORDER OR FIGURE | the default changed a rank, a score, a percentile, a weight, a count or any printed number, without changing membership. Order within the class by the number of published rows affected, descending. |
  | 3 | CHANGES SOMETHING NOT PUBLISHED | the default changed a value nobody sees this run: a section with no members, a feature not reached, a label not printed. |
  | 4 | PROVABLY CHANGED NOTHING | the artifact is byte-identical either way. **A request in this class does not fire at all this run.** It stays queued. Spending a scarce question on a difference nobody could observe is the cost that pushed the class-1 question out of budget. |

  **TIES, AND ONLY TIES, FALL BACK TO THE SKILL'S STATIC COST ORDER.** Where two
  requests land in the same class with the same measured effect, break the tie by
  the skill's documented decision-point order, and then by variable name, so the
  same file always spends its budget the same way and two runs of the same data
  are comparable.

  **RECORD THE COMPUTATION, NOT ONLY ITS RESULT.** The audit names every
  outstanding request, its computed class, the number of published rows its default
  affected, and whether it fired. A reader can then see that the question they were
  asked was the expensive one, and a binding owner can see which questions are
  being suppressed as class 4 run after run, which is exactly the list worth
  clearing in one sitting.

  **THIS DOES NOT RAISE THE BUDGET.** C2 still allows at most two per run and at
  most one before the first output. C3 decides only WHICH two.
- **C4. Once, then never.** A bound or declined variable does not fire again.
  A declined one may fire once more only if a later run reaches a decision where
  the default is materially worse than at the first firing, and then never again
  outside Stage 3.

## 2.3 What Stage 2 never does

- It never blocks a run. Every deferred question has a default and the run
  proceeds on it.
- It never asks a PERSON-tier user an ORG question.
- It never asks for something the file, the directory or a previous run already
  answered.
- It never re-asks a declined question at the next opportunity.
- It never presents the default as a failure. A defaulted run is a correct run
  with a named limitation.

## 2.4 THE CATALOGUE

Eighty-six entries: the seventy-six relocated original questions, eight
composite entries, and two entries added after acceptance testing. The original
identifiers are preserved so nothing is lost: the ignition interview absorbed nine of the original eighty-five (Q-A2,
Q-B1, Q-C1, Q-C2, Q-D1, Q-D2, Q-E1, Q-E2, Q-E3), and Q-A1 and Q-L1 were split,
with their ignition halves in Stage 1 and their remainders here.

Each entry names the DECISION that triggers it. Entries are grouped by the run
event that produces that decision, because that is the order a real deployment
meets them in.

---

### GROUP 2A: TRIGGERED BY THE FIRST RANKED LIST

### Q-D6 | TRIGGER: the run is about to exclude nothing, because no not-actionable field is bound
BINDS: UNIT_ACTIONABLE_NOW_CONCEPT, UNIT_ACTIONABLE_NOW_VALUES.
ASK: "Which field tells you that one of these cannot be worked right now, and
what values does it carry?"
WHY: a lagging measure survives the thing it measures, so a unit that cannot be
touched still reads as a strong performer and ranks high.
GOOD: a column name and a value list.
VAGUE, "we would just know": push once for the column name. There is no name-list
substitute; a maintained list of exceptions rots and does not travel.
IF DECLINED: **the consequence depends on whether a COLUMN resolved, and it is
stated in one place, the UNIT_ACTIONABLE_NOW_VALUES row in reference/schema/
SECTION A1.** Do not paraphrase it here. In short, so the answerer can decide
knowingly: where no column resolves at all, nothing is excluded and the report says
some units on the list may be closed, suspended or on hold with their history still
ranking them high; where a column DOES resolve, the standing seed set is applied
under its three guards and every distinct value is printed as EXCLUDED or KEPT, so
declining costs you the local vocabulary rather than the exclusion itself. Under
REVIEW the test is different again, per SD-POP-30, because a unit that became
unworkable during the period was workable for the rest of it.

### Q-G1 | TRIGGER: more than one measure column resolved, or the resolved one failed its value check
BINDS: MEASURE_TIERS.
ASK: "If you could rank these by one number, what would it be? And if that number
is missing from a file, what would you fall back to, and then to?"
GOOD: an ordered ladder with the header stems as they appear.
VAGUE: offer the candidate columns with a sample of their values and their
maxima, and let the answerer pick.
IF DECLINED: the first seed stem that resolves and is populated is used, and the
column, its unit and its time basis are named in the audit for checking.

### Q-H3 | TRIGGER: identifier resolution was ambiguous, or values lost leading zeros
BINDS: UNIT_ID_CONCEPT, UNIT_ID_IS_TEXT.
ASK: "Which column is the identifier, and can it carry leading zeros?"
GOOD: a column name and a yes or no.
VAGUE: show the candidates with uniqueness and null counts beside each.
IF DECLINED: the seed dictionary's identifier concept is used and identifiers are
handled as text, which is the safe direction; the column used is named.

### Q-H4 | TRIGGER: no scope column resolved, or two did and they disagree
BINDS: the scope concepts in COLUMN_CONCEPT_DICTIONARY.
ASK: "Which columns hold the levels we talked about, and what are they called in
the file?"
GOOD: a column per level.
VAGUE: offer the candidate columns with their distinct value counts, which almost
always makes the level obvious.
IF DECLINED: whichever single scope column resolves is used, finer levels read
off it by prefix and coarser by truncation, and the level used is stated.

### Q-B2 | TRIGGER: a user gave a short scope code, or a plain-language scope phrase must be padded
BINDS: SCOPE_CODE_SCHEME, SCOPE_CODE_WIDTH, SCOPE_CODE_PAD_DIRECTION,
SCOPE_CODE_PAD_CHARACTER, SCOPE_LEVEL_ID_WIDTHS, and by derivation
SCOPE_CODE_AMBIGUITY_THRESHOLD.
ASK: "Do your levels have codes, and does a wider level's code sit inside a
narrower one? If so, how many digits at each level?"
GOOD: yes with an example, or no, or "they are unrelated ids".
VAGUE, "I think so": ask for two real codes at different levels, test the prefix
relationship yourself, and show the answerer what you concluded.
IF DECLINED: the scheme is detected from the data; if it cannot be detected,
codes are treated as opaque and matched exactly, so a short code will not be
padded and the user is offered the values present instead.

### Q-B3 | TRIGGER: a scope phrase did not resolve against the values in the file
BINDS: SCOPE_PLAIN_LANGUAGE_MAP.
ASK: "When someone here asks for a report, what do they actually say? Give me
five or six real phrasings."
GOOD: real phrases. This is seed data and the skill extends it at runtime.
VAGUE: accept whatever comes, mark the map as thin, and note that unmatched
phrases are logged for extension rather than refused.
IF DECLINED: scope phrases resolve only against the distinct values in the file,
and a failed phrase produces the list of values present rather than a refusal.

### Q-B4 | TRIGGER: a title resolved ambiguously between a junior role and a wider one
BINDS: WIDE_SCOPE_TOKENS.
ASK: "Which words in a job title tell you someone covers something wider than a
single front-line unit?"
WHY: a title carrying any of these outranks a junior role word, and that test runs
before the title table, so a senior title is never demoted below what the data
supports.
IF DECLINED: the generic token list is used and the token that decided a role is
named in the audit.

### Q-C4 | TRIGGER: a directory title failed to resolve to a role
BINDS: ROLE_LADDER.titles, ROLE_TITLE_ABBREVIATIONS.
ASK: "What titles and abbreviations do your directory records actually carry?"
WHY: real records are written in shorthand, and a lookup that misses the
abbreviation falls through to inference on a record that was unambiguous.
IF DECLINED: the generic abbreviation set is used and an unresolved title causes
the user to be asked once to pick their role from a list.

### Q-C5 | TRIGGER: the directory was unreachable and the user did not answer
BINDS: ROLE_FALLBACK_KEY.
ASK: "If we cannot tell who someone is, which role should we assume?"
GOOD: the narrowest role.
VAGUE or senior: push back once. An unknown that defaults upward inflates every
claim and every list size.
IF DECLINED: the narrowest role in the ladder is assumed, which produces a shorter
list and narrower claims, and that is stated.

### Q-D7 | TRIGGER: the population contains a visibly distinct subgroup, or a user asks why certain units appear
BINDS: OUT_OF_MODEL_CLASS_CONCEPT, OUT_OF_MODEL_CLASS_LABEL,
OUT_OF_MODEL_ESCAPES_ENABLED.
ASK: "Is there a group of these that is served by a completely different
operating model, so it should not compete for the same person's time at all?"
FOLLOW UP: confirm the exact column name and record that it resolves by exact
name only, because a neighbouring type column will remove a different population
and every downstream check will still pass.
VAGUE, a description with no column: do not accept a name list as a substitute.
IF DECLINED: no class exclusion is applied and the whole population is ranked,
which is stated in the funnel.

### Q-N1 | TRIGGER: the first deliverable is about to be sized
BINDS: DELIVERABLE_LINES.
ASK: "A front-line person and a senior leader both get a list. How many items
should each act on?"
PUSH BACK ONCE if the senior number is proportional to their span: a more senior
person has less time, not more. The action list gets shorter as scope widens
while the reference depth stays constant.
IF DECLINED: the standing sizes are used and named in the front panel.

### Q-N2 | TRIGGER: the eligible count exceeded the default reference cap
BINDS: REFERENCE_CAP.
ASK: "How deep should the reference list behind the action lists go?"
NOTE: state that the cap counts rows on the section, never positions in the
ranked list, and that no instruction may assert the section holds exactly that
number.
IF DECLINED: the standing depth is used and the showing note discloses the cut.

### Q-Q1 | TRIGGER: the first narrative column is about to be written
BINDS: IMPACT_LANGUAGE_RULE, BANNED_PHRASES.
ASK: "When a report says which items carry the most business impact, is there
anything we should never say about the rest?"
WHY: every unit matters to the person who owns it. The tools measure impact, and
that is a measurement, not a judgment about the rest.
IF DECLINED: the standing phrasing is used and no comparative editorializing is
written.

---

### GROUP 2B: TRIGGERED BY THE FIRST FLOWING-POPULATION DECISION

### Q-D3 | TRIGGER: the run must decide which units are open right now
BINDS: POPULATION_SHAPE.stages, POPULATION_SHAPE.entry_field,
POPULATION_SHAPE.stage_field, POPULATION_SHAPE.reopen_allowed,
POPULATION_SHAPE.enumeration_source, FLOW_OPEN_DEFINITION.
NOTE: reopen_allowed cannot be inferred from columns alone. Where it is unbound,
duplicate identifiers are REPORTED rather than merged, because merging them sums
two separate episodes of the same item into one and a reader cannot recover it.
ASK: "What are the stages, in order, and what makes one of these open right now
rather than finished?"
VAGUE, stages with no open rule: offer the two common readings, an exit date that
is blank, or a stage that is not terminal, and test both against the file.
IF DECLINED: open is taken as a blank exit date; where no exit column resolves,
every unit is treated as open and the report says so, which overstates the
workload rather than hiding it.

### Q-D4 | TRIGGER: the first period-over-period comparison on a flowing population
BINDS: FLOW_COHORT_BASIS.
ASK: "When you compare this month to last, do you group these by when they came
in, when they closed, or when something happened to them?"
WHY: grouping by exit date makes a slow month look good, because only the easy
ones closed.
IF DECLINED: entry date is used as the cohort basis and the basis is named beside
every comparison.

### Q-D5 | TRIGGER: the first period-over-period comparison on a fixed roster
BINDS: FIXED_ROSTER_CHURN_TOLERANCE.
ASK: "Between two periods, roughly what fraction of the list changes, and at what
point would you say the two lists are no longer the same thing?"
IF DECLINED: a ten percent tolerance is assumed, and any comparison beyond it is
labelled as not like for like rather than suppressed.

---

### GROUP 2C: TRIGGERED BY THE FIRST CLAIM OR THE FIRST COMPARISON

### Q-E4 | TRIGGER: the first claim is about to be worded
BINDS: CLAIM_STRENGTH_BY_RUNG.
ASK: "How strongly may a claim be worded when it rests on each of those second
numbers?"
OFFER: strong for a share of an addressable set and for a matched control,
qualified for a peer spread and for plan attainment, qualified with a warning for
your own prior run rate, bounded for a plain count.
WHY THE WARNING: growth against your own trend controls for nothing external, and
it is exactly the claim the ground-moved failure punishes.
IF DECLINED: the offered defaults are used and printed beside each claim.

### Q-E5 | TRIGGER: the first win or miss label is about to be emitted
BINDS: DEADBAND.
ASK: "How much movement is noise? At what point do you say a number genuinely
moved?"
VAGUE: offer to compute it from a real file, propose a band at the lower decile
of absolute movement across peers, and ask for a confirm.
IF DECLINED: the band is computed from the data; where it cannot be computed, no
win or miss label is emitted and only the raw delta with its unit is printed.

### Q-E6 | TRIGGER: a metric is about to be compared on a rung above the floor, and that rung's own definition is unbound
BINDS, one per available rung: ADDRESSABLE_POPULATION_DEFINITION,
ADDRESSABLE_POPULATION_CONCEPT, CONTROL_GROUP_DEFINITION, PEER_SET_LEVEL_DEFAULT,
PEER_SET_IS_EXTERNAL, EXTERNAL_PEER_SET_SOURCE, PEER_SET_ANCHOR_PERIOD,
PLAN_SOURCE_NAME, PLAN_SET_BY_ROLE, PRIOR_PERIOD_BASIS.
ASK, only for rungs already named available, and only the one the run needs now:
"You told me this organization can compare on {rung name}. What exactly is the
set, and which column counts it?"
WHY: a rung named at ignition and never defined is a rung the run cannot compute.
Until this entry existed there was no question that bound these, no default when
they were unbound, and no notice when a default was applied, while three skills
read them by name as if they were bound.
GOOD: a definition and a column, or a source and an owner.
VAGUE: offer the candidate columns with their totals beside them and let the
answerer pick, per I4.
IF DECLINED: that rung is UNAVAILABLE for this run. Every metric assigned to it
drops to the highest rung whose own definition IS bound, never past it to the
floor, the drop is stated beside the figure, and the claim strength drops with
the rung. The exact notice per variable is in reference/schema/ SECTION A2.

### Q-E7 | TRIGGER: a population was detected as COLD, and no scoped rung availability exists for it
BINDS: COUNTERFACTUAL_RUNG_SCOPES for that population,
COLD_START_MIN_PRIOR_SHARE, ADDRESSABLE_SELF_SHARE_CEILING.
ASK: "Almost nothing in {population} has a prior period, so it cannot borrow the
comparisons the rest of the business uses. Which of them can {population} produce
on its own? And is there a plan for it that somebody else set before the period
started?"
WHY: the mature business around a launch can produce comparisons the launch
cannot, and rung availability was inherited organization-wide with no way to say
so. See SD-CLM-29.
GOOD: a shorter list of rungs, usually attainment against a launch plan plus the
bare denominator.
IF DECLINED: the rungs are re-tested against the cold population automatically
and struck where they fail, per SD-CLM-29. Nothing is inherited. Every rung
struck is named beside the figures it would have carried, no win or miss label is
computed for that population per SD-CLM-31, and the run reports the absolute
build, the sequencing against plan where a plan exists, and the execution against
a denominator population, per SD-CLM-32.

### Q-G2 | TRIGGER: a comparison was blocked on a rate or a unit mismatch
BINDS: MEASURE_UNIT_TOKENS, MEASURE_RATE_TOKENS.
ASK: "What units do your numbers come in, and do your headers say whether a
number is a total or a per-period rate?"
WHY: a per-period value compared against a period total is meaningless and is
blocked with no override.
IF DECLINED: the generic tokens are used, and a comparison whose basis cannot be
confirmed is blocked and reported rather than computed.

### Q-G3 | TRIGGER: two files differ in how much history they cover
BINDS: MEASURE_LOOKBACK_TOKENS.
ASK: "Do your headers carry a marker for how much history a number covers?"
NOTE: a differing lookback is permitted, recorded as a run-rate comparison, and
never used to open a report.
IF DECLINED: the generic tokens are used and an undetected difference is not
labelled, which is stated as a limitation.

### Q-G4 | TRIGGER: a unit-drift factor of two or five was detected between two files
BINDS: UNIT_DRIFT_CANDIDATE_FACTORS, UNIT_DRIFT_AUTONORM_FACTORS.
ASK: "Have you ever had two files where the same column was in different units?
And if one of your numbers genuinely doubled in a period, would that be a real
result worth celebrating?"
WHY THE SECOND HALF: if yes, a factor of two must be excluded from silent
correction, because correcting it would erase the best result of the year and
never say so.
IF DECLINED: small factors are never corrected silently and the user is asked at
the moment one is detected.

---

### GROUP 2D: TRIGGERED BY THE FIRST PRIORITY SWEEP

### Q-J1 | TRIGGER: the run is about to read priorities for the first time
BINDS: PRIORITY_SOURCES, SOURCE_AUTHORITY_MAP, PRIORITY_SOURCE_COUNT.
ASK: "Where does a person here learn what matters this period? Name every
source."
NOTE: confirm that the nearest source, the person's own supervisor, is read first
and outranks the rest, and that a central source is the cross-check and the
fallback, never the starting point.
IF DECLINED: only the supervisor chain is read, and the report says nothing in it
reflects an organization-wide priority.

### Q-P2 | TRIGGER: the first mailbox sweep
BINDS: MAIL_SWEEP_FOLDERS.
ASK: "Which mail folders should a sweep of a manager's messages cover?"
NOTE: it must include the deleted-items equivalent.
IF DECLINED: every folder the mailbox exposes is swept, and the folders covered
are named with the message counts.

### Q-J3 | TRIGGER: a manager's message contains a list of units
BINDS: DIRECTIVE_RELEASE_PHRASES, and confirms ACTOR_TEST_ENABLED.
ASK: "When a manager sends a list of units to their team, is that an instruction
to cover them? And what phrases would your managers use to say do not work
these?"
NOTE: any list from anyone in the chain is a must-cover, no trigger phrase is
required, and the only thing that releases an item is an explicit instruction not
to cover it.
IF DECLINED: the generic release phrases are used, and an instruction to stand
down in different wording will not be recognized, which is stated.

### Q-J4 | TRIGGER: the chain resolved more than one level and two levels disagree
BINDS: CHAIN_WALK_DEPTH, CHAIN_DISTANCE_WEIGHTS.
ASK: "How far up the chain should we read, and does a priority from three levels
up count as much as one from the person's own manager?"
PUSH ONCE if they say it counts the same: where levels disagree, which one does
the person follow. The nearer manager knows the units.
IF DECLINED: the standing depth and distance weights are used and every level
resolved is named, including levels that published nothing.

### Q-J2 | TRIGGER: a message references a published periodic priority document
BINDS: CENTRAL_BRIEF_NAME, CENTRAL_BRIEF_TABLE_COLUMNS, and confirms
CENTRAL_BRIEF_REQUIRED false.
ASK: "Does a central function publish a periodic document naming the period's
priorities, their due dates and who they apply to? What are its columns called?"
NOTE: a document one period old is worth far more than no plan, and stopping a
run over a folder-name mismatch is the worse failure.
IF DECLINED: no central brief is read and the report says so.

### Q-J5 | TRIGGER: headers carry a marker that looks like an action flag
BINDS: OWN_ACTION_MARKER_CONCEPT, OWN_ACTION_MULTIPLIER.
ASK: "Is there a published marker in the file that says an item needs this
person's action specifically?"
NOTE: the marker is tested for, never inferred from words in the item name.
IF DECLINED: no item takes the marker multiplier and that is recorded rather than
approximated from verbs.

### Q-H5 | TRIGGER: a block of work-item columns is suspected and its boundary is ambiguous
BINDS: the work-item block concepts, ACTIVITY_BLOCK_TERMINATOR_CONCEPT.
ASK: "Are there columns in there that record what somebody did, as opposed to
what the result was? And is there a marker in the file that separates that block
from the rest, such as a total row or a boundary column?"
NOTE: the boundary is matched exactly and the rightmost match wins.
IF DECLINED: the block is resolved by the ordered fallbacks in
reference/field-resolution.md, and no block is a valid outcome that is stated.

### Q-H6 | TRIGGER: work-item headers carry prefixes
BINDS: ORIGINATOR_PREFIX_MAP.
ASK: "Do any of those columns carry a prefix saying who created the work?"
STATE THE RULE IMMEDIATELY: that prefix is optional metadata for weighting only
and is never an admission test, because typically most work-item columns carry no
prefix at all and they hold most of the signal.
IF DECLINED: prefixes are ignored entirely, which costs weighting nuance and
costs nothing else.

---

### GROUP 2E: TRIGGERED BY THE FIRST WORK-TYPE WEIGHTING

### Q-I1 | TRIGGER: the alignment term is being computed and work items must be typed
BINDS: WORK_TYPES.
ASK: "Not all work changes the same amount. Rank these from most to least
valuable here: persuading someone to decide something new; physically or
systemically changing something; teaching someone; confirming something is
already true; producing a record; and a label that just tells you what something
is and asks for nothing."
VAGUE, "it depends": anchor it. Which of those two would you rather someone did
with the last hour of the day. Repeat pairwise until the order settles.
IF DECLINED: the generic ladder and its standing weights are used, and every item
whose type could not be recognized is named at the baseline rather than
discounted.

### Q-I2 | TRIGGER: more than a fifth of work items fell to the baseline type
BINDS: WORK_TYPES.trigger_verbs, WORK_TYPES.trigger_nouns.
ASK: "What verbs appear in your work item names for each of those?"
IF DECLINED: the generic verbs are used and every unrecognized item is surfaced
by name so the vocabulary can be extended once for everybody.

### Q-I3 | TRIGGER: one verb appears across an unusually large share of headers
BINDS: GENERIC_COMPLETION_VERBS.
ASK: "Are there verbs in your names that mean nothing on their own, words like
complete or process?"
WHY: such a word promotes a low type by one step and never promotes a type
already at or above the baseline, otherwise it stamps every item it touches with
one type.
IF DECLINED: the generic list is used and a local completion verb may type an
item one rung too high, which is visible in the audit.

---

### GROUP 2F: TRIGGERED BY THE FIRST ENTITY-SPECIFIC REQUEST

These fire the first time a request names a product, service, line or programme,
or the first time more than one entity-specific measure column resolves.

### Q-F1 | TRIGGER: a heading or a request needs a word for the class credit attaches to
BINDS: CREDITABLE_ENTITY_CLASS_NAME.
ASK: "What do you call the thing a person gets credit for the performance of? A
product line, a service line, a programme, a portfolio?"
IF DECLINED: a generic phrase is used in headings and nothing else changes.

### Q-F2 | TRIGGER: more than one entity resolved and they must be ordered
BINDS: CREDITABLE_ENTITIES ranks.
ASK: "List them, best first, and tell me why that order is the order."
VAGUE, an unordered list: ask which one a person should work first when they can
only work one, and build the order from repeated application of that question.
IF DECLINED: nothing is weighted up or down by line of business, and ranking
rests on the measure, the alignment and the workload alone.

### Q-F3 | TRIGGER: an entity weight is needed for the alignment term
BINDS: CREDITABLE_ENTITIES standing weights, ENTITY_WEIGHT_FLOOR.
ASK: "What weight should each carry relative to the top one?"
STATE THE RULE: there is no default row. Anything that resolves to none of these
is reported as unmapped and takes no weight, and where a default is genuinely
correct it is tied to the floor of this list, so resolving an entity can only
raise a score and never lower it.
IF DECLINED: a single implicit entity at weight one is used.

### Q-F4 | TRIGGER: an entity name in a file or a request failed to match
BINDS: CREDITABLE_ENTITIES.aliases.
ASK: "For each one, what spellings show up in your data files? Include the wrong
ones you keep seeing."
NOTE: ask specifically for misspellings. A real recurring typo in a header is a
live literal that must be matched.
IF DECLINED: unmatched names are flagged and asked about rather than guessed.

### Q-F5 | TRIGGER: an alias matched far more rows than expected
BINDS: SENTINEL_TOKENS.
ASK: "Are any of those spellings a common short word on their own, or do any
carry punctuation?"
WHY: such an alias is protected by a sentinel before punctuation is stripped,
because the bare remainder matches text that has nothing to do with it.
Coincidental substring containment is never evidence.
IF DECLINED: no aliases are protected, and every matched value set with its row
count is listed in the audit so an over-match is visible.

### Q-F6 | TRIGGER: a growth or share comparison needs a benchmark population
BINDS: ENTITY_BENCHMARK_MAP, BENCHMARK_POPULATIONS.
ASK: "For each one, what is the wider population it should be compared against,
and what is that population called in your headers?"
VAGUE, "there is no wider population for that one": good. That entity is
unbenchmarked and routes to execution claiming with a denominator population.
Record it explicitly rather than leaving it unmapped by accident.
IF DECLINED: every entity is treated as unbenchmarked and every figure routes to
execution claiming.

### Q-F7 | TRIGGER: a figure is about to be claimed whose subject may not be claimable
BINDS: NON_CLAIMABLE_ENTITIES.
ASK: "What appears in your data that must never be claimed as an achievement,
even when it is going well?"
PROMPT with the general form: anything whose composition the person did not
choose. A whole-market total, an agreement they inherited, a price change made
above them, a macro effect.
IF DECLINED: nothing is marked unclaimable and the report cannot warn when a
figure describes a population the person did not compose, which is stated.

### Q-F2-INIT | TRIGGER: a priority matched nothing because it is a single distinctive word
BINDS: SPECIFIC_INITIATIVE_NAMES.
ASK: "Are there initiative names distinctive enough that one word is enough to
recognize them?"
NOTE: this list grows each period from the priority document itself.
IF DECLINED: two distinctive shared words are required for every match, and every
unmatched priority is reported by name.

### Q-F2-STOP | TRIGGER: a priority matched too loosely on a common domain word
BINDS: MATCH_STOPWORDS.
ASK: "Which words are so common in your headers that they should not count as
distinctive?"
IF DECLINED: the generic stopword set plus the generic completion verbs is used
and every match shows its shared tokens.

---

### GROUP 2G: TRIGGERED BY THE FIRST PERIOD OR CALENDAR DECISION

### Q-L1 | TRIGGER: the derived window and the file's own period stamp disagree
BINDS: OPERATING_WINDOW_SOURCE.
ASK: "Where are the real start and end dates of your window published?"
IF DECLINED: the window is derived and the dates used are printed above the list,
with a note that every due-date weighting shifts with them.

### Q-L2 | TRIGGER: the published window could not be read
BINDS: OPERATING_WINDOW_DERIVATION_RULE.
ASK: "If we cannot read the published window, what rule gives us the right
dates?"
NOTE: a derived window is always disclosed as derived.
IF DECLINED: the standing derivation is used and the exact dates are printed.

### Q-L3 | TRIGGER: a work item name carries a quarter or half token
BINDS: PERIOD_TOKEN_MAP, and confirms REPORTING_CALENDAR_IS_NOT_AUTHORITY.
ASK: "Does your operating window line up with the calendar quarter?"
ALMOST ALWAYS NO. Explain: a reporting quarter ends on a month boundary because
that is how finance divides the year, and the days between that boundary and the
operating window's close carry no work.
IF DECLINED: the generic tokens are used and any token that cannot be resolved
through the window is dropped from scoring and named, never guessed at.

### Q-L4 | TRIGGER: the run falls near a window boundary
BINDS: PLAN_AHEAD_RULE.
ASK: "When someone plans, are they planning the window they are in or the next
one?"
WHY: a run that quietly plans the wrong window is indistinguishable from a correct
one until somebody is standing in front of the work.
IF DECLINED: the standing rule is used and the period covered is named at the top
of the report.

### Q-L5 | TRIGGER: the first review-mode run
BINDS: CYCLE_POSITIONS, CYCLE_POSITION_NAMES, GOAL_REVIEW_CADENCE.
ASK: "What are your review points through the year, and what do you call them?
How often is the goal set reviewed with the manager?"
IF DECLINED: the generic four positions and a quarterly cadence are assumed and
stated wherever cadence affects a date.

### Q-S2 | TRIGGER: a second period's file arrives
BINDS: nothing directly; it runs the portability test.
ASK: "Can I look at this alongside the earlier one?"
ACTION: resolve both and report every difference in header row, container count,
column naming, measure basis and column count. A change to the dictionary that
would break either file is wrong.
IF DECLINED: nothing is lost this run; the test is offered again at Stage 3.

---

### GROUP 2H: TRIGGERED BY THE FIRST COMPLIANCE-SENSITIVE ITEM

### Q-M1 | TRIGGER: a jurisdiction column resolved and a priority names something that might be restricted
BINDS: COMPLIANCE_CHECK_ENABLED, JURISDICTION_CONCEPT.
ASK: "Is there anything a person might be told to do that they are not permitted
to do in some places?"
VAGUE, "not really": ask the general form. Is there any rule that differs by
state, province, licence, contract or site.
IF DECLINED: no compliance check runs and the report says that if something in it
cannot lawfully or contractually be done somewhere, the report does not know it.

### Q-M2 | TRIGGER: the compliance check is enabled and a reference must be found
BINDS: COMPLIANCE_GUIDE_SET, COMPLIANCE_GUIDE_MASTER,
COMPLIANCE_GUIDE_SUPPLEMENTS.
ASK: "Where is that written down, and is it one document per place?"
IF DECLINED: the check cannot run and every priority it would have validated is
held back and named, rather than silently permitted.

### Q-M3 | TRIGGER: a place name in a request did not match the codes in the data
BINDS: JURISDICTION_NAME_TO_CODE, SUBREGION_SUFFIXES.
ASK: "When your people say a place name, is it the same string your data stores?"
STATE THE RULE: conversion is by table, then exact match, never by checking
whether one string sits inside another.
IF DECLINED: place names resolve only where they match the stored value exactly,
and a miss returns the nearest values present rather than widening.

### Q-M4 | TRIGGER: the compliance reference was unreachable on a run
BINDS: COMPLIANCE_FAILS_CLOSED_ON.
ASK: "If we cannot reach that reference on a given day, should we hold back the
priorities we could not check, or hold back the whole report?"
THE CORRECT ANSWER IS THE PRIORITIES. Confirm it. An unreachable reference must
not silently permit everything, and must not kill the deliverable either.
IF DECLINED: the priorities are held back and named, which is the only permitted
setting.

---

### GROUP 2I: TRIGGERED BY THE FIRST DELIVERABLE BUILD

### Q-N3 | TRIGGER: the first artifact is about to be assembled, or a user asks for a section that does not exist
BINDS: TAB_CONTRACT, MSG_EMPTY_SECTION.
ASK: "What sections should the deliverable have, in what order? And for each one,
what should the single row say when there is nothing to report?"
STATE THE RULE: every section ships every run, even with nothing to report,
carrying its header and exactly one row saying why in plain language.
IF DECLINED: the standing sections and generated empty messages are used, and
each generated message names the binding or column that would have filled it.

### Q-N4 | TRIGGER: the first artifact is built and column headers were defaulted
BINDS: IDENTITY_BLOCK_COLUMNS and the HDR_ strings.
ASK: "What columns identify an item, in what order, and what should each be
called?"
STATE THE RULE: these strings are byte-identical between runs and are never
improved for readability.
IF DECLINED: plain English defaults are used, they are stable between runs, and
the count of defaulted headers is named once rather than a line per column.

### Q-N5 | TRIGGER: the identity block is wider than the default and the freeze point matters
BINDS: IDENTITY_BLOCK_ANCHOR_COLUMN, SPAN_BLOCK_POSITION.
ASK: "Which column should stay on screen when someone scrolls right?"
NOTE: the freeze point is computed as the column after the anchor, never
hard-coded, because the attribution block changes the position by role.
NOTE: **the anchor is DERIVED rather than chosen where this question is not
answered.** reference/output-contract.md states the walk: the identity columns are summed
left to right against FROZEN_SPAN_MAX_WIDTH, ONCE FOR THE WHOLE ARTIFACT rather
than once per sheet, and the anchor is the last column whose inclusion keeps the
sum at or under the bound. This entry states which variable the answer binds; that
file states the derivation, and where this appears to disagree with it, it governs.
IF DECLINED: the derived anchor is used, the derivation is recorded, and no
identity column is dropped or narrowed to make it fit.

### Q-N6 | TRIGGER: two runs would collide on a filename
BINDS: OUTPUT_FILENAME_PATTERN, DELIVERABLE_NAME.
ASK: "What should the file be called so two runs never collide?"
NOTE: it must carry a scope label, its identifying code, the period and any
qualifier.
IF DECLINED: the standing pattern and a generic report name are used.

### Q-A3 | TRIGGER: the first artifact is published
BINDS: METHOD_OWNER_STATEMENT, TUNING_INVITATION.
ASK: "In two plain sentences with no jargon: what does this compute from a user's
own data, and what does it take from you as an input rather than assuming?"
VAGUE, a mission statement: redirect. I am not asking what it is for. I am asking
what a user should be told is calculated from their own numbers, and what was set
by you.
IF DECLINED: a generic statement is printed.

### Q-A1 | TRIGGER: a second division starts using the bundle, or the first Stage 3 audit
BINDS: OPERATING_UNIT_NAME, OPERATING_UNIT_LONG_NAME, ORG_SHORT_NAME.
ASK: "What is the division or business these reports cover, as distinct from the
company?"
IF DECLINED: reports are headed with the organization name and cannot distinguish
two divisions using this toolkit.

---

### GROUP 2J: TRIGGERED BY THE FIRST REVIEW OR OBJECTIVE-SETTING RUN

### Q-O1 | TRIGGER: a write-up is about to be drafted
BINDS: DESTINATION_SYSTEM_NAME, FORM_SPEC_SOURCE.
ASK: "What system does a completed write-up get pasted into, and what document
defines the form?"
IF DECLINED: a generic structure is drafted and the user is told to check it
against the live form before pasting.

### Q-O2 | TRIGGER: the draft needs a section structure
BINDS: FORM_SECTIONS, FORM_SECTIONS_BY_CYCLE_POSITION.
ASK: "What are the sections of that form, in order, and which ones does the
employee fill in?"
IF DECLINED: the generic section set is drafted, and sections the form carries and
this set does not are not drafted at all, which is stated.

### Q-O3 | TRIGGER: a field is about to be written and its limit is unknown
BINDS: FIELD_LIMITS, OBJECTIVE_FIELD_IS_SINGLE, FIELD_BUDGET_SPLIT.
ASK: "Are there character limits on any of those fields? And is the goal box one
field holding the title, the description and the measures together, or separate
fields?"
STATE: these are defaults, not facts. They differ by field, by form version and by
tenant, and are confirmed per run by the person who has the form open.
IF DECLINED: the common defaults are used, every emitted field carries its exact
character count, and the user is asked once to confirm from the counter next to
the field.

### Q-O4 | TRIGGER: a heading is about to be emitted that may not exist on the live form
BINDS: BANNED_HEADINGS.
ASK: "Are there headings your people put in their own prior write-ups that are
not on the live form?"
STATE THE RULE: a heading with no counterpart on the live form must never travel
into the record.
IF DECLINED: no warning can be given and the user is told to check the section
names against the form before submitting.

### Q-O5 | TRIGGER: a behaviour or rating section must be drafted
BINDS: BEHAVIOUR_FRAMEWORK_NAME, BEHAVIOUR_FRAMEWORK_ITEMS,
BEHAVIOUR_SCALE_VALUES, RATING_SCALE, RATING_AXES, SELF_ASSESSMENT_PROMPTS,
STATUS_VALUES, ACTIVITY_STATUS_VALUES.
ASK: "What behaviours or values are rated, on what scale? And what is the rating
scale for performance, with its distribution guidance? What is the operative
difference between the top band and the one below it?"
WHY THE LAST PART: that one sentence is what a write-up is actually aimed at.
IF DECLINED: those sections are not drafted at all and are named as not drafted,
rather than being invented.

### Q-O6 | TRIGGER: a rating rubric is cited and its version is unknown
BINDS: RATING_AXES volatility note, REFERENCE_VALIDITY_PERIODS.
ASK: "Has that rubric changed recently?"
WHY: a stale rubric is the quiet way a write-up gets built against last year's
standard.
IF DECLINED: every cached reference expires at year end and a block past that date
is refetched, or used and marked stale.

### Q-K1 | TRIGGER: a claim must be laddered to something above the person's own objective
BINDS: LINEAGE_LADDER, ENTERPRISE_STRATEGY_PILLARS.
ASK: "If someone wants to say their work mattered, what is the highest thing they
can point at? And then what is the next thing down, and the next?"
IF DECLINED: no claim is connected to a company priority, and claims are worded at
the level they can actually be defended.

### Q-K2 | TRIGGER: a claim would cite a level above the person's own scope
BINDS: ROLE_LADDER.altitude_ceiling, CONTRIBUTION_VERBS, OWNERSHIP_VERBS.
ASK: "For each role, how high may they claim ownership before it reads as
inflation?"
STATE THE ENFORCEMENT so it is not a matter of taste: above the ceiling the claim
must use a contribution verb and must not use an ownership verb, and the check
tests the verb list.
IF DECLINED: contribution phrasing is used for anything above the person's own
scope, which is the safe direction.

### Q-K3 | TRIGGER: more than three candidate wins must be ranked for the headline
BINDS: INCENTIVE_PLAN_NAME, METRIC_SET, METRIC_MULTIPLIERS.
ASK: "Is there a published set of metric weights that says what the organization
thinks matters most? And which of those can a person at each level actually
influence?"
WHY: priority ranking comes from the organization's own published weights, not
from the writer's opinion about which of their wins is biggest.
IF DECLINED: candidates are ranked by altitude, then peer rank, then magnitude,
and the user is asked which should lead.

### Q-C6 | TRIGGER: the first review-mode run by a user with direct reports
BINDS: PEOPLE_LEADER_OBJECTIVE_REQUIRED, PEOPLE_LEADER_OBJECTIVE_SOURCE.
ASK: "Do people who lead others have to carry a leadership goal, and where is that
requirement written down?"
IF DECLINED: none is required or drafted, which is stated.

---

### GROUP 2K: TRIGGERED BY A SPECIFIC RUN EVENT

### Q-C3 | TRIGGER: a unit shows open work assigned to a party other than the requester, or an assignment list appears in the mailbox
BINDS: ROLE_LADDER.is_specialist, SECOND_ACTOR_RESOLUTION_LADDER,
SECOND_ACTOR_UNIT_SUFFIX, COVERAGE_DUPLICATION_FACTOR,
COVERAGE_DUPLICATION_APPLIES_TO.
ASK: "Is there a role that covers a subset of someone else's units under that
person's direction? A specialist, a shared resource, a support technician?"
EXPLAIN THE CONSEQUENCE: a unit already being worked by that party is discounted
for the person choosing where to spend a day, and NOT discounted for the manager
who deployed that party, because that is their own resource showing up in their
own report.
VAGUE, "sort of": ask the deciding question. Does the person receiving the report
choose whether that other party goes there. If yes, no discount.
IF DECLINED: no duplication discount is applied and that is recorded as a normal
result, not a failure.

### Q-H1 | TRIGGER: the run had to search more than one location, or found more than one candidate file
BINDS: SOURCE_WORKBOOK_NAME, SOURCE_WORKBOOK_LOCATIONS.
ASK: "What is the file this reads, what is it called, and where does it come from
each period?"
IF DECLINED: the standing locations are searched in order and the file used, its
record count and the container within it are named.

### Q-H2 | TRIGGER: the second period's file differs in shape from the first
BINDS: nothing directly. It sets expectations and seeds the dictionary.
ASK: "Does it come out the same shape every time?"
VAGUE, "mostly": that is the expected answer and it is the reason resolution works
by concept and never by literal header. Say so.
IF DECLINED: nothing is lost. Every unresolved header is logged either way.

### Q-P1 | TRIGGER: a reference document must be found in a document store
BINDS: DOC_STORE_NAME, DOC_STORE_SITE_VARIABLE, DOC_STORE_LIBRARY_VARIABLE, and
confirms DOC_STORE_PATH_DISCOVERY_REQUIRED true.
ASK: "Where do reference documents live, and are the folder names stable enough to
hard-code?"
THE ANSWER IS ALWAYS NO. Record the reference values as a starting point for
discovery only. Two folders for consecutive periods will differ by a space or a
punctuation mark, and a literal path breaks the first period somebody types it
differently, silently.
IF DECLINED: discovery runs against whatever container resolves, and a failure to
find a reference is reported by name.

### Q-P3 | TRIGGER: the skill is about to produce something that resembles routing, scheduling or dispatch
BINDS: SYSTEM_OF_RECORD_EXCLUSIONS, SIBLING_SKILLS.
ASK: "Is there a system that already owns a job this might be tempted to do?
Routing, scheduling, dispatch, forecasting?"
WHY: do not build a second version of something that already has a system of
record.
IF DECLINED: nothing is withheld on that ground, and the user is invited to say if
something duplicates a system they already run.

### Q-P4 | TRIGGER: the first evidence crawl
BINDS: EVIDENCE_SOURCES, CHAT_PLATFORM_NAME.
ASK: "Where should a user's evidence be looked for, in what order?"
IF DECLINED: the standing crawl is used and the tiers actually reached are named
with their counts.

### Q-Q2 | TRIGGER: a term of art is about to be paraphrased in output prose
BINDS: CONTROLLED_VOCABULARY.
ASK: "Are there words your business uses in an exact way that we must not
paraphrase?"
IF DECLINED: no term is protected and paraphrase is possible, which is stated once.

### Q-R1 | TRIGGER: the first transient failure of a run
BINDS: RETRY_BACKOFF_SCHEDULE, SCOPED_RETRY_LIMIT, REPAIR_CYCLE_LIMIT.
ASK: "When something goes wrong mid-run, how long should we keep trying before we
tell the user?"
PRESENT THE LADDER: a transient failure waits and retries with no attempt limit; a
failure scoped to one unit narrows, retries, rebuilds, then degrades that unit
only; a logical failure repairs in place and re-verifies a fixed number of times;
and only a named hard gate stops the run.
IF DECLINED: the standing ladder is used.

### Q-R2 | TRIGGER: the first hard gate fires
BINDS: HARD_GATES.
ASK: "What should stop a run outright?"
STATE EXPLICITLY what is not on the list and never will be: fatigue, run length,
retry count, and output size. Count the gates and record the count in one place
only.
IF DECLINED: the standing closed set is used and named.

### Q-R3 | TRIGGER: the first bannered partial emit
BINDS: INCOMPLETE_BANNER_TEXT, INCOMPLETE_PLACEHOLDER_TEXT.
ASK: "Is it ever acceptable to publish a partial report?"
THE ANSWER: no for a silent partial, yes for a bannered one. A labelled partial
that looks finished is still a partial; one that is clearly bannered and names
what is outstanding is worth more than nothing after a long run.
IF DECLINED: the standing banner and placeholder are used.

### Q-S1 | TRIGGER: any run where a real file is available and the dictionary is still thin
BINDS: COLUMN_CONCEPT_DICTIONARY additions, NULL_LIKE_VALUES, MIN_STEM_LENGTH,
HEADER_SCAN_DEPTH, CONCEPT_LEARNING_ENABLED.
ASK: nothing. This is not a question; it is an offer to look.
ACTION: run the field resolution pass, report which concepts resolved, which did
not, and which columns had no home. Propose the resolved stems for the shared
dictionary in the closing summary.
IF DECLINED: the seed dictionary is used unchanged and every unresolved header is
still logged.

### Q-N-REMAINDER | TRIGGER: a run needs a deliverable-contract constant not covered above
BINDS: USER_SIZE_TIER_1_FRACTION, USER_SIZE_OVERRIDE_ALLOWED, SCOPE_RANK_HEADER,
SCORE_COLUMN_REQUIRED, SCORE_DECIMAL_PLACES, UNRESOLVED_COLUMN_TREATMENT,
CHAT_REPLY_MAX_LINES, SUBMISSION_BOUNDARY_BANNER, OUTPUT_DIR, UPLOAD_DIR,
SCRATCH_DIR, DOWNLOAD_DIR.
ASK: these are never asked in a run. Each has a standing value that is also the
only permitted value or a safe convention, and each is confirmed only in the
Stage 3 audit.
IF DECLINED: the standing values apply and are listed in the method section.

### Q-SCORING-REMAINDER | TRIGGER: the first score is computed
BINDS: SCORE_FORMULA_SHAPE, BASE_TERM, MEASURE_EXPONENT, GAP_TERM_WEIGHT,
GAP_TERM_CAP, GAP_TERM_DEFINITIONS, WORKLOAD_COUNT_CAP, WORKLOAD_MULTIPLIER,
SOURCE_BOOST_ONE, SOURCE_BOOST_BOTH, MANDATORY_MULTIPLIER, LOCAL_BOOST,
LOCAL_OVERRIDE_DEPTH, NARROWNESS_THRESHOLD, NARROWNESS_MULTIPLIER,
HQ_FLAG_BREADTH_LIMIT, STEER_TILT_TARGET_WEIGHT, STEER_TILT_OTHERS_FACTOR,
INITIATIVE_STEER_TERM, TIE_BREAK_KEYS, ZERO_MEASURE_SORT_KEY,
PERCENTILE_DEFINITION, ZERO_MEASURE_TREATMENT, MIN_POPULATION_FOR_NORM,
CLOSE_WEIGHTS, UNDATED_ITEM_TREATMENT, CARRYOVER_LABEL.
ASK: none of these is asked in a run. Every one has a standing value, the formula
is printed in full with a worked example in every artifact, and the whole set is
reviewed in the Stage 3 audit or when a user disputes a specific number.
WHY THIS IS SAFE: the artifact publishes the formula and the score, so a
disagreement can be traced to a specific term and corrected rather than argued.
IF DECLINED: the standing constants apply and are visible in every report.

### Q-EXCEPTION-REMAINDER | TRIGGER: the first exception section is built
BINDS: EXCEPTION_FLAGS, FLAG_MEASURE_MULTIPLIER_FLOOR, PRIORITY_BAND_THRESHOLDS,
PRIORITY_BAND_LABELS, RECENCY_FLOOR_DAYS, RECENCY_MEDIAN_FACTOR, ALERT_WARN_DAYS,
ALERT_OVERDUE_DAYS, ALERT_SCALES, ALERT_COUNT_POPULATION,
BENCHMARK_GAP_THRESHOLD, SIZE_GATED_PROGRAM_TEST, RECENCY_LAG_DISCLAIMER,
FLAG_EXEMPTIONS.
ASK, once, at the first exception section: "This section lists quiet problems no
other report surfaces. Which of these are real problems in your business, and is
there anything on it that a person cannot actually fix themselves?"
WHY THE SECOND HALF: a gap the person cannot close is not a gap worth printing.
Before keeping a flag, confirm the person both engages the unit and controls the
thing being measured.
IF DECLINED: the generic flags are used, every flag whose column did not resolve
or carried no data is named as not evaluated, and no absent column is treated as a
gap.

### Q-FORMAT-REMAINDER | TRIGGER: the first workbook is styled
BINDS: FORMATTING_ELEMENTS, TABLE_STYLE_NAME, the palette variables, the font
variables, the row-height variables, NARRATIVE_COLUMN_WIDTH_RANGE,
CHAR_WIDTH_FACTOR, LINE_HEIGHT_PADDING_PT, RIGHT_ALIGN_COLUMNS,
TITLE_CASE_HEADINGS, ALLOWED_CHARACTER_RANGE, FULL_WALK_ROW_LIMIT,
SAMPLING_DENSITY.
ASK: none of these is asked in a run. The standing set is applied and verified.
Colour and font are the only ones a user is likely to volunteer, and a volunteered
value is recorded immediately.
IF DECLINED: the standing formatting contract applies and every element is
verified or recorded as not applicable.

### Q-RUNCTL-REMAINDER | TRIGGER: a large file, or a fan-out
BINDS: WRITE_CHUNK_SIZE, WRITE_VERIFY_TAIL_ROWS, WRITE_CONFIRM_WAIT_SECONDS,
PARTITION_SIZE, MAX_CONCURRENT_WORKERS, SCALE_TIER_BOUNDARIES,
CHECKPOINT_PATH_PATTERN, PARTITION_CHECKPOINT_PATH_PATTERN,
CHECKPOINT_DELETE_ON_PUBLISH, REGRESSION_INVARIANTS, SPOT_CHECK_SAMPLE_SIZE,
REGRESSION_CASES, GLOBAL_REMEDIATION_BUDGET, PER_GATE_FAILURE_LIMIT,
FORBIDDEN_RETRIEVAL_PATHS, INLINE_FETCH_CEILING, MIME_ENCODING_FACTOR.
ASK: none of these is asked in a run. They are reliability mechanics with safe
standing values, reviewed in the Stage 3 audit.
IF DECLINED: the standing values apply.

### Q-QUESTIONS-REMAINDER | TRIGGER: the question machinery itself needs tuning
BINDS: QUESTION_BANK, QUESTION_BATCH_MAX, NON_BLOCKING_BUDGET_FORMULA,
COMPOSITE_QUESTION_IDS, FORM_REQUIRED_EXEMPT_QUESTIONS, ANOMALY_QUESTION_CAP,
HEADLINE_CANDIDATE_THRESHOLD, MISS_SUGGESTION_COUNT, EVIDENCE_SUFFICIENCY_FLOOR,
SYNTHESIS_MIN_EVIDENCE, SYNTHESIS_MAX_OBJECTIVES, RUN_ESTIMATE_BANDS,
ASK_LANGUAGE_RULE.
ASK: only in the Stage 3 audit, or when a user says they were asked too much or
too little.
IF DECLINED: the standing values apply.

---

# PART 3: STAGE 3, THE FULL AUDIT

## 3.1 What it is

The same questions, entered deliberately rather than by trigger. It exists for
the person who wants to finish the binding in one sitting, usually the binding
owner, usually after two or three real runs have shown them what the gaps cost.

It is never launched automatically, never suggested more than once per run, and
never suggested to a user who is not an authorized answerer.

## 3.2 How it is entered

Any of:

- The user asks for it in plain words: finish the setup, complete the
  configuration, what else do you need, what is still unset.
- The binding owner opens it directly.
- A run offers it, at most once, in one line at the end of a report, and only
  when the number of outstanding bindings that materially changed that report is
  three or more:

> Three settings that would have changed this report are still unset. Ten minutes
> would close them. Say finish the setup whenever you want.

## 3.3 How it runs

1. **Report the state first.** Bound, unbound, declined and inferred, with counts,
   and for each unbound one, the single line from reference/schema/ SECTION A1 or A2 saying what its
   default costs.
2. **Order by cost, not by group.** Walk the outstanding bindings in descending
   order of how far their default moves a published number. A colour palette
   never comes before an exclusion flag.
3. **Batch by conversation, not by block.** Group questions that a person would
   naturally answer together, four at a time, per I3.
4. **Skip what has been declined**, unless the answerer asks to revisit
   declined items.
5. **Offer the file pass.** If a real file is available, run the field resolution
   pass and the portability test and convert a dozen questions into answers
   nobody had to give.
6. **Close by reporting what is still open** and what each remaining gap costs,
   then offer to set BINDING_LOCKED.

## 3.4 What the audit may set that Stage 1 and Stage 2 may not

BINDING_LOCKED. Locking the org tier stops deferred questions from firing at
users. It is set only here, only by an authorized answerer, and only after the
audit has reported what remains unbound, so nobody locks a configuration without
seeing its holes.

A locked configuration still degrades honestly: every remaining unbound value
uses its default and prints its notice. Locking suppresses the asking, never the
disclosure.

## 3.5 The audit is also the change entry point

An answer given in the audit that contradicts an earlier one is recorded as a
change, with both values and the date. Where the change affects the role ladder
or the scope hierarchy, every stored PERSON answer is marked for re-confirmation,
because PERSON_BINDING_VERSION no longer matches.

---

# PART 4: THE PERSON SCRIPT

Runs on a user's first run. Everything it can resolve from their own record it
resolves silently and presents as a confirmation, never as an open prompt.

Four questions, asked in one message. Two of them are usually pre-answered from
the directory and reduce to a yes.

Open with, verbatim:

> Before I start: four quick things about you, and then I will not ask again.

## Q-PERSON-1: ROLE
> Your title is recorded as {resolved title}. That puts you in {role display
> name}, which means the reports come sized for {tier phrasing}. Is that right?

If the directory is unreachable:
> What is your job title?

GOOD: a title. Resolve it through the abbreviation map, then the wide-scope token
test, then the title table. Bind PERSON_ROLE_TITLE.
VAGUE or unresolvable: offer the ladder's display names as a numbered list with
one line each describing what that role owns, and accept a number.
NEVER: ask which report line they should get, how many items they should receive,
or what tier they belong to. Those are ORG bindings the role resolves.

## Q-PERSON-2: SCOPE
> Which {finest OWNED level display name, per SCOPE_FINEST_KEY} is yours? You can give me the code or just the
> name.

Where the code is already known:
> I have you on {scope label} ({code}). Still right?

GOOD: a code or a name. Pad it yourself. Never ask the user to pad, never reject a
short code, and never ask them to restate it in the file's format.
VAGUE: offer the distinct values present at that level, each labelled with
something recognizable and a count beside it, and accept a name or a list
position.
ZERO ROWS on the first filter: that means the filter is wrong before it means the
scope is empty. Re-test the comparison as text on both sides and re-test the level
reading, and only then come back with the distinct values present at every level.
NEVER: ask what the levels of the organization are, how codes are padded, or what
width a code is. Those are ORG bindings.

## Q-PERSON-3: SUPERVISOR
> You report to {resolved manager name}. I will read their messages for the
> priorities they have set. Correct?

Where no manager lookup exists:
> Who do you report to? I use it to find the priorities they have set for this
> period.

GOOD: a name, ideally with an address. Bind PERSON_SUPERVISOR_NAME and
PERSON_SUPERVISOR_CONTACT.
VAGUE, "a few people": ask which one sets their priorities for the period. Record
the others as additional senders in the sweep.
EMPTY: record no supervisor only when both hold: a manager lookup was actually
made and returned empty, AND the person's own title names the top of the house. An
error is a failed lookup, not an absent manager. A profile record that carries no
manager field can never answer this question.

## Q-PERSON-4: DIRECT REPORTS
> Do you have people reporting to you?

Bind PERSON_HAS_DIRECT_REPORTS. Explain in half a line why it is asked: it decides
whether work done by someone else is written as team credit rather than as the
user's own action.

## OPTIONAL FOLLOW UPS

These fire only when the run needs them, never in the first message.

- PERSON_SECONDARY_SCOPES: fires only when the role's claim tier is mixed.
  > You hold both {a} and {b}. I will treat {a} as your own direct work and {b} as
  > aggregate. Is that the right split?
- PERSON_PREFERRED_LIST_SIZE: never asked. Bound only when the user states a size
  in a request, and then remembered.
- PERSON_ROLE_START_DATE: fires only when a run compares two periods and the
  earlier one may predate the user in this scope.
  > This compares {earlier period} to {later period}. Were you in this
  > {level name} for both?
- PERSON_CONFIRMED_FIELD_LIMITS: fires once, before drafting, in the REVIEW skill
  only.
  > Before I write these: what is the character limit on the objective box, and on
  > each measure? If you have the form open the counter is usually right next to
  > the field. If you are not sure I will target {FIELD_LIMITS default}, which is
  > the common default.

## WHAT THE PERSON SCRIPT NEVER ASKS

None of the following may be asked of a PERSON-tier user, in any phrasing,
including as a confirmation:

- What the levels of the organization are, or what they are called.
- How scope codes are constructed, padded or widthed.
- Which entities, product lines or programmes credit may attach to, or how they
  rank.
- What the counterfactual denominator is, which rung applies, or what the moving
  ground is.
- Which metrics carry which weights.
- What the deliverable sections are, how many items a role should receive, or what
  the caps are.
- Which document is authoritative for anything.
- Where reference material lives.
- What the compliance reference is or which jurisdictions restrict what.
- What the work types are or what they weigh.
- Any threshold, factor, cap or weight from the schema.

---

# PART 5: WHEN AN UNBOUND ORG VALUE IS FOUND MID-RUN

A run will regularly reach a point where it needs an ORG value that has not been
bound. That is the normal operating condition of a staged binding, not an error.

## 5.1 The two paths

**Path A, the answerer is authorized.** The deferred question fires, subject to
the four constraints in 2.2. Ask, record, confirm the save, continue.

**Path B, the answerer is not authorized.** This is the common case, because most
users are not the binding owner.

**The run proceeds in a degraded but honest mode. It applies the documented
default, names what is unbound, states what that changed, does not guess, and
queues the request to the binding owner.**

## 5.2 The procedure for Path B

1. **Do not ask the user.** They are not the answerer for this value, and an
   answer from them would be recorded as a binding it is not.
2. **Apply the documented default from reference/schema/ SECTION A1 or A2.** Never the value that
   maximizes a score, a weight, a rank, a list size or a claim. Where a default is
   genuinely required, take the floor of the relevant scale, so that binding it
   later can only raise a result and never lower it.
3. **Skip exactly what the value feeds, and nothing else.** The schema records a
   feeds list against each concept and each binding. Suppress only those flags,
   gates, weights, benchmarks and sections. A missing breadth column costs one
   section, not the report.
4. **Print the notice in the artifact, not only in the chat.** The artifact is
   what survives. Emit the exact degradation notice from reference/schema/ SECTION A1 or A2 in the front
   panel and in the audit section.
5. **Mark the affected numbers.** Any figure that would have used the unbound
   value is either omitted with a stated reason or published with its weakened
   basis named. A visibly missing number is recoverable; a fabricated one is not.
6. **Downgrade the claim strength BY ONE STEP, TO THE NEXT RUNG THAT IS ACTUALLY
   BOUND, AND NEVER STRAIGHT TO THE FLOOR.** Where the unbound value is a
   counterfactual binding, every affected claim drops to the HIGHEST rung whose own
   definition IS bound, the drop is stated beside the figure, and the claim strength
   drops with the rung. It reaches bounded phrasing, a number with a denominator
   population and no achievement wording, ONLY where no rung's own definition is
   bound at all. **An unbound value never deletes the effect of a rung the
   organization did bind**, per SD-CTR-24 and the ignition rows for
   COUNTERFACTUAL_AVAILABLE_RUNGS and COUNTERFACTUAL_DEFAULT_RUNG, both of which
   DERIVE before they floor. This step states the procedure; those rows state the
   derivation, and where this appears to disagree with them, they govern.
7. **Queue it to the binding owner.** Append the variable, the run that needed it,
   the decision it was facing, and what the default cost, to the unbound-value
   queue. This is how the ORG tier learns what it is missing without any user
   being interrogated.
8. **Do not treat it as a hard gate.** Unbound is not a stop unless the value is
   one of the three that make a source unusable at all: the unit identifier, a
   ranking measure, and any one scope column.

## 5.3 What the user sees

In the artifact, in plain business language:

> {VARIABLE_DISPLAY_NAME} has not been set for {ORG_NAME}, so {named effect}.
> Everything else in this report is unaffected. {BINDING_OWNER_NAME} can set it.

In the chat, one line:

> Note: {n} organization settings were not available, so {short effect}. The
> report names them, and I have flagged them for {BINDING_OWNER_NAME}.

## 5.4 What degraded mode never does

- It never invents a value.
- It never asks a frontline user an organizational question.
- It never silently widens a population, a scope or a claim.
- It never publishes a number whose basis it could not name.
- It never suppresses a whole section that a single missing value only partly
  affects.
- It never presents the degraded output as a complete one.
- It never quietly stops mentioning a degradation because it has mentioned it
  before.

---

# PART 6: THE FIRST RUN AT A COMPANY WHERE NOTHING IS BOUND

This is the worst case and the most likely one: a frontline employee opens the
toolkit at a company where no ignition interview has been run, nobody has bound
anything, and there is no binding owner recorded. It is also the moment the
bundle will be judged, so it is specified end to end.

## 6.1 The state at the start

- Every ORG variable is unbound, including all ten ignition variables.
- Every PERSON variable is unbound.
- The user is a frontline employee. They are not an authorized answerer for any
  ORG binding.
- They have, at most, one file and a question like "what should I work on this
  month".

## 6.2 The rule that governs the whole sequence

**The frontline user is never asked an ORG question, including an ignition one.**
Ignition is a blocking state for the ORG tier, and the correct response to a
blocking state the user cannot clear is not to hand them the block. It is to
produce the most useful honest thing available and route the block to somebody
who can clear it.

That means the first run at an unbound company is a PROVISIONAL RUN. It produces
real output. It is labelled provisional in the artifact. It does not pretend to
be a bound run and it does not refuse to be a run.

## 6.3 The sequence, step by step

**Step 1. Capability probe.** Runs first, as always. Establishes what can be read
and written. If nothing can be read and no file was supplied, this is the one
hard stop, and it asks for a file rather than for a binding.

**Step 2. Infer what can be inferred, silently.** Before anything is asked:

- Resolve the user's identity, title and manager from the directory if it is
  reachable.
- Resolve the file: container selection, header detection, and the three required
  concepts, using the seed dictionary.
- Detect the scope columns present and their distinct value counts. A column whose
  values nest inside another column's values is a hierarchy, and the chain can be
  read straight out of the data.
- Detect the population shape by running SD-POP-24, which is the only shape
  detection procedure in this bundle. This step states no test of its own: the
  three tests, their order, and the conditions under which the tie-break may be
  consulted all live in SD-POP-24, and where anything here appears to disagree
  with it, SD-POP-24 governs.
- Detect the period the file covers from its own stamps.

Most of the ignition set has now been inferred at MEDIUM confidence from the data
alone. None of it is written to the ORG config, because a frontline user is not
the answerer and I7 forbids binding a medium-confidence inference.

**WHERE INTERACTIVE IS ABSENT, STEPS 3 AND 5 BELOW ASK NOTHING.** Per I11 and
reference/capability-probe.md 2.14 rung 2, no question can be put to anybody on such a run.
Step 3's four person questions are not asked: each one's documented default is
applied, each is listed as a question that would have been asked with the value it
would have bound, and the reader is told plainly that the answers could not be
collected and will be asked next time somebody is present. Step 5's forwardable
block is written into the artifact rather than spoken. Every other step of this
sequence runs unchanged, because none of the others needs a person.

**Step 3. Ask the four PERSON questions.** These the user can answer, and they
are the only questions asked. Where the role ladder is unbound, Q-PERSON-1 becomes:

> What is your job title? I do not have this organization's role list yet, so I
> will treat you as working your own {finest OWNED level detected from the data} unless
> you tell me otherwise.

Where the hierarchy was detected from the data rather than bound, Q-PERSON-2 offers the
detected values with counts, in the user's language, per I4.

**Step 4. Produce the run.** With the inferred shape and the four person answers,
the run can do most of its job:

- It can rank, because the identifier and a measure resolved.
- It can filter to the user's own scope, because a scope column resolved.
- It can read the user's supervisor's messages for priorities, because the
  supervisor is a PERSON binding.
- It can exclude nothing, because no not-actionable flag is bound, and it says so.
- **It can carry a second number on every figure, at whatever rung the ignition
  rows for COUNTERFACTUAL_AVAILABLE_RUNGS and COUNTERFACTUAL_DEFAULT_RUNG derive
  from the documents actually bound, which on a documents-bound first run is
  usually NOT the floor.** Both of those rows DERIVE BEFORE THEY FLOOR: the
  available set is derived as every rung whose own definition variables are bound
  plus the floor rung, and the default is derived as the highest rung in that set
  whose own definition is bound. Both are recorded DERIVED at MEDIUM confidence,
  named beside the claims they govern, and read back for correction. Read the rung
  and the strength it supports from those two rows in reference/schema/, never from
  here. **THE FLOOR APPLIES ONLY WHERE NO AVAILABLE RUNG'S OWN DEFINITION IS
  BOUND**, and only then is every figure printed with a bare denominator
  population and none of them worded as an achievement.
- **A PROVISIONAL RUN IS NOT A FLOOR-WORDED RUN, and the two were confused once, in
  this very section.** A first run that binds the peer, plan or prior-run-rate rungs
  out of the organization's own published documents words its claims at the strength
  those rungs support, names the derivation beside them, and still carries the
  provisional label of step 5 for everything the interview has not answered. The
  label is about what was ASKED; the rung is about what was BOUND; a run can be
  fully provisional and still carry a rung above the floor. An unbound value here
  never deletes the effect of a rung the organization did bind, which is SD-CTR-24
  and the third column of the ignition table.
- It cannot weight by entity, by work type or by published priority, and it says
  which of those it could not do.

**Step 5. Label it provisionally, in the artifact.** The front panel opens with a
block that is not buried and not apologetic:

> This report was produced before anyone configured this toolkit for {ORG_NAME as
> the user named it, or "your organization"}. It is real and the numbers in it
> trace to your file. Here is what it could not do:
>
> - Nothing was excluded as unworkable, because no status field is set. Some items
>   below may be closed or on hold.
> - Every figure carries {the rung the derivation reached} as its comparison, and
>   the line says which. Where that derivation reached only the floor rung, this
>   line reads instead: every figure carries a plain count as its comparison,
>   because no benchmark is set, and no figure in this report is worded as an
>   achievement.
> - No organization priorities were applied, because none are set. Priorities from
>   {supervisor name} were read and are shown.
> - {and so on, one line per material gap, from reference/schema/ SECTION A1 or A2}
>
> Ten minutes with someone who knows the business closes all of this. Ask them to
> say: set up this toolkit.

**Step 6. Do not ask the user to fetch an answerer.** Offer the sentence they can
forward, and stop. Chasing a binding owner is not the frontline user's job and
pressing them for one is the friction that gets a tool abandoned.

**Step 7. Record everything the run inferred, for the eventual ignition
interview.** Every medium-confidence inference is written to a provisional file,
not to the config, with its evidence. When somebody does run Stage 1, the
interview opens with those inferences as proposals:

> Before I ask: from the files people have already run, it looks like your
> hierarchy is {detected chain}, your work arrives as {detected shape}, and your
> period is about {detected length} {day or days, selected on the number}. Tell me
> where I have that wrong and we
> will be finished in five minutes rather than ten.

That is the payoff of the provisional run: the first real interview is faster
because the tool has been paying attention.

## 6.4 What the frontline user experiences, in full

1. They ask for their monthly plan.
2. They are asked four questions about themselves.
3. They wait, are told roughly how long, and are told the silence is work.
4. They get a real ranked list of their own work, in their own scope, reflecting
   their own manager's priorities.
5. The top of it tells them plainly what it could not do and who can fix it, in
   one short block they can forward.
6. They are asked nothing they could not answer.

## 6.5 What must never happen in this sequence

- The user is never asked what the organization's levels are, what its entities
  are, what its period is called, what benchmark it uses, or who owns the
  configuration.
- The run never refuses because the configuration is empty.
- The run never produces a list that reads as authoritative when it was produced
  with the floor rung and no exclusions.
- **The run never words its claims at the floor because it is provisional.** The
  floor is a consequence of no available rung's definition being bound, and of
  nothing else. Applying it to a run that bound rungs from the organization's own
  documents deletes work the organization did, and it is the inversion SD-CTR-24
  forbids.
- The run never invents a hierarchy, a benchmark, an exclusion or a priority in
  order to look complete.
- The provisional labelling is never softened on later provisional runs. It
  appears at the same prominence every time until the ignition interview happens.

## 6.6 The second frontline user, and the tenth

Nothing changes for them either. Each answers the same four questions about
themselves. Each gets the same provisional label. The inferred-shape file
accumulates evidence across all of them, so the eventual ignition interview gets
better the longer it is delayed, which is the correct incentive: waiting costs
disclosure, not correctness.

---

# APPENDIX: QUESTION ACCOUNTING

The original interview carried eighty-five organization questions. All
eighty-five survive.

| Where it lives now | Count |
|---|---|
| Absorbed into the Stage 1 ignition prose (Q-A2, Q-B1, Q-C1, Q-C2, Q-D1, Q-D2, Q-E1, Q-E2, Q-E3) | 9 |
| Relocated into the Stage 2 catalogue, each tagged with its triggering decision | 76 |
| Total | 85 |
| Composite catalogue entries added, covering schema variables that were never separate questions | 8 |
| Entries added after acceptance testing (Q-E6, Q-E7) | 2 |
| Entries in the Stage 2 catalogue | 86 |

The four person-script questions are numbered Q-PERSON-1 to Q-PERSON-4 so they
cannot be confused with the Stage 2 entries Q-P1 to Q-P4, which are the systems
and sources questions.

Q-A1 and Q-L1 were split: their ignition halves are in Stage 1 turns 1 and 7, and
their remainders are catalogue entries.

Eight further catalogue entries carry composite identifiers (Q-F2-INIT,
Q-F2-STOP, Q-N-REMAINDER, Q-SCORING-REMAINDER, Q-EXCEPTION-REMAINDER,
Q-FORMAT-REMAINDER, Q-RUNCTL-REMAINDER, Q-QUESTIONS-REMAINDER). They cover the schema variables that
were never separate questions in the original interview and that no run should
ever stop to ask about, because each has a standing value that is safe, published
in the artifact, and reviewable in the Stage 3 audit.

Stage 3 walks every one of the eighty-five, plus the composite entries, in
descending order of what their absence costs.

---

# CHANGE LOG: ACCEPTANCE TEST REMEDIATION

What changed in this file after two hostile acceptance tests across five invented
companies, and why.

## Turn 4, population shape, rewritten

The old detection ran two tests and treated both passing as a CONFLICT, resolved
by preferring FLOW on the grounds that a flow model over a roster is harmless.
Acceptance testing found three separate failures of that logic at three different
companies: it could not produce a schema-valid value at all at two of them, and at
a third it bound a pipeline to a roster of 207 standing locations because both
tests passed and the members carried opening dates and agreement terms.

Three changes:

1. **A third test decides.** When one of them leaves, does it leave a hole
   somebody notices, or does the next one take its place in a queue. A hole is a
   standing position and therefore a FIXED roster whose members happen to be
   dated. A queue is FLOW.
2. **Both of the first two tests passing is the COMMON case, not a conflict.**
   The turn now says so, so an interviewer does not reach for a tie-break that
   was never appropriate.
3. **Shape is a property of the population, not of the company.**
   POPULATION_SHAPE is now a keyed set. Where a business has a roster of
   containers AND a stream moving across them, both are declared and each run
   names which it scored. Forcing a single answer was itself the error. See
   SD-POP-23 and SD-POP-24.

The turn also no longer promises to bind fields it then defers. Its ignition
target is a key, a mode and a unit noun; everything else is conditional on mode
and carries a default and a notice in reference/schema/ SECTION A2.

## Turn 5, the second number, rewritten

The follow-up questions that DEFINE each rung existed only inside a branch that
fired when somebody answered "all of them". Every test binding owner gave a crisp
subset answer, so the branch never fired and five of the six rungs were named as
available and never defined, while three skills read their definitions by name as
if they were bound.

Three changes:

1. **The follow-up is unconditional.** For every rung named, its test is asked
   immediately, in the same breath. A rung named but not defined is not an
   available rung: it is struck and the striking is said out loud.
2. **The peer answer is disambiguated.** Internal siblings and a published
   external comparison group are different bindings, and the external one is the
   most likely real answer at any regulated or benchmarked business. It names a
   publication and a cadence and is never forced into the organization's own
   containment chain.
3. **A scoping question was added.** Is there any part of the business where one
   of these is not true. This is the question that stops a launch inheriting the
   comparisons of the mature business around it.

## Catalogue entries added: 2

| Entry | Trigger | Answers |
|---|---|---|
| Q-E6 | A metric is about to be compared on a rung whose own definition is unbound | Report 2 D1. Eight variables defining five of the six rungs had no question, no default and no notice anywhere. |
| Q-E7 | A population was detected as cold and has no scoped rung availability | Report 2 D5. The cold-start case had no binding path at all. |

Q-D3 was also extended to bind the remaining POPULATION_SHAPE sub-keys, including
the reopen rule, with an explicit statement that the reopen rule cannot be
inferred from columns and that unbound means duplicates are reported rather than
merged.

## Corrections

- **A cross-reference that would have broken the wall.** Part 6, the first run at
  an unbound company, pointed a frontline user at Q-P2, which is the mail-folder
  sweep question, an ORG question. The intended reference was Q-PERSON-2, the
  scope question. The file makes the exact confusion its own accounting appendix
  declares impossible, in the one sequence every new company runs first. Fixed.
- **The catalogue count.** The section header said seventy-six where the file's
  own accounting appendix said eighty-four. Both now say eighty-six, which is what
  is there.
- **Seven questions, not eight.** The opening promised eight things and the eighth
  turn binds nothing. It is now described as seven questions and a close.

## What did NOT change, deliberately

- The ignition set is still an ORG binding set that fits in under ten
  minutes. Turn 5 grew, but its follow-ups are one line each and they replace a
  branch that was never reached.
- Part 6, the first run at an unbound company, is unchanged apart from the
  cross-reference. Both reports identified it as correct architecture, and Step 7,
  writing inferences to a provisional record rather than to the config, was
  specifically praised. It is now also the mechanism that detects a cold
  population before anyone has bound anything.

## Third pass, round 2 regression

- **The right-answerer constraint is now computable, report 1 D8.** C1 tested a
  property that existed nowhere in the bundle: no role carried an authority
  field, no mapping existed, and no default existed because there was no variable
  to default. A constraint that cannot be evaluated has failed, per SD-EFF-03, so
  the honest reading was that no deferred question could ever fire for anybody but
  the binding owner, while this file promised the opposite. C1 now tests
  ROLE_LADDER.binding_authority, which defaults to NONE for every role and ALL for
  the binding owner, and it says in the open that the default means only the
  binding owner is ever asked.
- **The Stage 2 preamble no longer overclaims.** It said the config fills itself
  in through use across the first several runs. It fills itself in through the
  binding owner's own use and through the queued request list that everybody
  else's runs feed, and it now says so. Where the owner grants authority to other
  roles in the Stage 3 audit, those roles start answering too.

## Fourth pass, live end-to-end run against an undescribed file

- **BINDING_OWNER_NAME is now genuinely unskippable in Turn 1, and the CONSEQUENCE
  is stated to the answerer rather than to the file.** The trap the run found: with
  no owner recorded, ROLE_LADDER.binding_authority resolved to NONE for every
  role, the deferred-request constraint C1 became unsatisfiable, and the entire
  progressive-binding mechanism was switched off silently while the toolkit
  appeared to work. Turn 1 now names both machines that stop, gives the answerer
  the words that describe what they are choosing, asks once more, and on a second
  refusal records the value as DECLINED rather than UNBOUND, prints the
  consequence at the TOP of the first report produced under that state, and
  re-offers it at the top of every Stage 3 audit. It is never re-asked of a
  frontline user, because naming an organization's binding owner is an ORG-tier
  act and I1's wall holds. The schema carries the matching fallback so the
  mechanism degrades rather than dying.
- **PART 6 step 2 no longer states a second shape-detection procedure.** It had
  said an entry date plus an exit date plus a stage column is a flowing pipeline,
  which is evidence toward test two only and never a decision. It now runs
  SD-POP-24 and states that SD-POP-24 governs wherever anything appears to
  disagree with it.

## Fifth pass, confirmation run at three altitudes

- **Turn 1 now describes authority as ADDITIVE, because it is.** The previous
  pass's wording called the senior-role grant a fallback, which is what the
  regression looked like from inside the file. Naming an owner ADDS a door; it
  never closes one. The declined path says the same thing to the answerer.
- **Turn 3 now expects a bare ordered list of role names and treats that as
  enough.** SD-CTR-26. Every sub-field the turn does not elicit is DERIVED by the
  derivations in reference/schema/ SECTION A1 and read back in the answerer's own
  words for correction. The fix is not more questions; it is derivation plus a
  read-back.
- **Turn 4 now says that a noun and nothing else is still enough.** Where the
  three shape tests cannot be run conversationally, `mode` is DERIVED from the
  data by SD-POP-24 and read back in the close. The tie-break wording is also
  scoped here to match SD-POP-24.
- **Turn 8 gains the IGNITION COMPLETENESS CHECK, and it is not optional.** The
  close walks all ten ignition variables and every sub-field of the three
  taxonomies, puts each in exactly one of ANSWERED, DERIVED or DEFAULTED, reads
  back every DERIVED line in one table, and then STATES THE RESULT IN PLAIN WORDS
  so the answerer never leaves believing they finished when they did not. Where
  the check fails off a fully answered interview, that is recorded as a defect in
  this bundle rather than as a gap in the organization's knowledge. The close now
  reports four counts, not three: ANSWERED, DERIVED, DEFAULTED and DECLINED.

## Sixth pass, final acceptance run at three altitudes

- **C1 no longer carries the replacement reading of binding authority.** This
  bullet still said that where binding_authority is unbound only the binding owner
  is ever asked, which is the same regression SD-CTR-25 was written to forbid,
  surviving in a second place. Authority is a UNION of two standing grants and
  naming an owner never removes an answerer.
- **C3 is now computed on the run rather than read from a table.** Four classes:
  a question whose default changed MEMBERSHIP of a ranked list jumps the queue; one
  that changed a published order or figure comes next, ordered by rows affected;
  one that changed something unpublished comes third; and one that provably changed
  nothing DOES NOT FIRE AT ALL and stays queued. Ties, and only ties, fall back to
  the skill's static decision-point order, so two runs over one file spend the
  budget identically. The audit records every request's class and row count, not
  only which one fired. The budget itself is unchanged: C3 decides which two, never
  how many.

## Seventh pass, release acceptance run

- **C2 now says what it counts, which is what resolves its collision with I3.**
  The budget counts ORG-TIER BINDING questions, which ask what the organization's
  configuration should be. It does NOT count PERSON-TIER FILE questions, which ask
  what something in the file the user just supplied means. Every question under
  field resolution is a file question, including F5.1's own step 5, whose tier was
  previously never stated; reading it as ORG-tier would have meant a frontline user
  could not be asked which column held the identifier in their own spreadsheet. All
  outstanding file questions are batched into ONE message however many there are,
  capped by FILE_QUESTION_BATCH_CAP, so two class-1 questions outstanding at once
  are both asked and neither consumes the ORG budget.

## Eighth pass, review and scorecard acceptance runs

- **Turn 3 no longer restates the role-to-level derivation, it cites it.** This
  file carried its own summary of the scope-level and claim-tier derivations, and
  the summary and the SECTION A1 row had drifted into two INCOMPATIBLE procedures.
  The summary anchored the junior end on the finest level outright, producing an
  unowned top level, a head of the organization demoted a rung, and a most junior
  role sitting AT the unit level, which the bundle then reports as a binding error.
  The non-provisional invariant holds only on the A1 reading, and this file is what
  an implementer reads FIRST. There is now one statement of each derivation and this
  turn points at it. What the turn still owns is the SHAPE of the outcome, which is
  a check on the derivation rather than a second copy of it.
- **Turn 5 binds the peer LEVEL in the same answer that gives the count.** It
  previously asked only how many peers there were, so the level fell to a default
  that contradicted the count just collected, which decides whether a peer
  comparison happens at all. The question now asks what KIND of thing a peer is,
  offering the levels by name; where only a count is given the level is derived from
  it and read back; and a stated count outranks the derivation where they disagree.

## Ninth pass, confirmation runs on both remaining skills

- **Turn 6 no longer states the consequence of an unbound MOVING_GROUND_NAME in
  its own words.** It quoted a capped claim strength while the binding-states table
  in the schema said the run is stamped provisional, so two readers produced two
  different artifacts off one binding state. Both are true and they are not
  alternatives: the capped claim strength is what the run DOES, the provisional
  label is what the artifact SAYS. The consequence now has one home, the third
  column of the ignition table in reference/schema/, and this turn quotes it.
- **Q-D6's DECLINED consequence now cites the exclusion rule rather than
  paraphrasing it.** Its paraphrase still said no exclusion is applied, which stopped
  being true when a resolved column with an unbound value list began applying the
  seed set. Declining now costs the local vocabulary rather than the exclusion.

## Tenth pass, the first run that bound its rungs and worded them at the floor anyway

- **PART 6 step 4 no longer floors the second number, which is the whole of the fix
  that landed everywhere else and never landed here.** The change that made
  COUNTERFACTUAL_AVAILABLE_RUNGS and COUNTERFACTUAL_DEFAULT_RUNG DERIVE BEFORE THEY
  FLOOR reached the schema's ignition rows and the skills that read them, and did
  not reach the one section a first-run implementer actually opens, which still said
  a first run can carry a second number only at the floor rung. A measured run bound
  three rungs out of the organization's own published documents and would, followed
  literally, have worded a year with an above-target retention result and 121 percent
  attainment at the weakest strength the bundle can emit. Step 4 now reads the rung
  from those two rows, states that the floor applies only where no available rung's
  own definition is bound, and says in terms that a PROVISIONAL RUN IS NOT A
  FLOOR-WORDED RUN: the label is about what was asked and the rung is about what was
  bound.
- **Step 5's front-panel block no longer asserts the floor either.** Its comparison
  line now names the rung the derivation reached, and carries the floor wording only
  as the case where the derivation reached the floor.
- **6.5 gains the prohibition the section needed**: a run never words its claims at
  the floor because it is provisional, because that deletes rungs the organization
  did bind, which is the inversion SD-CTR-24 forbids.
- **PART 5.2 step 6 was stale in the same way and is reconciled.** Degraded mode
  drops an affected claim to the highest rung whose own definition IS bound, never
  straight to the floor, and reaches bounded phrasing only where no rung's
  definition is bound at all. Q-E6's own DECLINED consequence already said this; the
  procedure that governs every unbound ORG value did not.
- **Q-N5 no longer paraphrases how the freeze point is found.** It said the last
  identity column before the section-specific block is used, which stopped being
  true when the anchor became a DERIVED walk of the identity columns against
  FROZEN_SPAN_MAX_WIDTH. It now names the variable it binds, points at the file that
  states the derivation, and records that the walk is run ONCE FOR THE ARTIFACT.
