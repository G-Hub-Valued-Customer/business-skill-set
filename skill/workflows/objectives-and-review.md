---
name: objectives-and-review
description: End-to-end concierge for the objective-setting and performance-review cycle at any organization in any industry. Sets objectives at period start against headquarters and supervisor priorities, tracks progress mid-period, and writes the completed mid-period and end-of-period sections. Reads any data file carrying entity identifiers and performance measures, verifies the data actually covers the period being written about, computes performance against a counterfactual denominator, ranks against peers, infers the actions behind each result, and proposes learnings from losses that ladder to organization objectives. Picks the user up from any starting point: complete documentation, raw files, one sentence such as "I did x, y and z this year", or nothing at all. Use when someone asks to set goals or objectives, update objective progress, write a mid-year, half-year or year-end review, draft a self-assessment, work out what their wins were this period, grade or rewrite their objectives and measures, or prepare any text that will become part of a performance record.
---

# OBJECTIVES AND REVIEW

## Mission

People write results lists. A results list is a set of true, quantified, orphaned
facts. A true number does not say what action produced it, whether it beat
anyone, or why the organization should care. The reader supplies the context, and
in a calibration room nobody does.

People are already doing the work. They cannot phrase it.

This skill does four things that a person writing about their own year cannot
easily do for themselves. It finds every defensible win the data supports rather
than the one or two the person remembers. It attaches a second number to every
first number, so a figure stops being an orphan. It infers the action behind each
result and then asks the person to confirm it, because the action half is what
people omit. And it refuses to let any of that ship at a strength the evidence
does not carry.

See SD-CLM-02.

**And it produces ONE THING, in one shape, for one purpose.** The deliverable is a
document that WRAPS the character-limited fields of a submission form rather than
replacing them: readable end to end, and copyable field by field, because the last
thing that happens to this text is that somebody pastes it into a box that truncates
without saying so. The medium is settled in PART 8 and the contract it answers to is
reference/output-contract.md PART 3.

## The governing premise

**THIS OUTPUT BECOMES A PERMANENT RECORD.** Every rule below that constrains a
claim exists because an overclaim, a misattributed peer result, or an invented
figure can damage a career. When a rule and convenience conflict, the rule wins.
See SD-CLM-01.

Five rules govern every other rule in this file, and they are stated in
reference/doctrine/ as G1 through G5:

- G1. One declared contract per deliverable, superior to every other section. Any
  later instruction that disagrees with the contract is the defect.
- G2. Fail closed. Unknown is not pass.
- G3. Never default an unknown to the value that maximizes its score.
- G4. Every number carries a second number the writer did not choose.
- G5. A rule that costs nothing when it does not fire and keeps the method
  portable is worth carrying.

## How to read this file

- **Doctrine is cited, never restated.** A rule with an ID of the form SD-XXX-nn
  lives in reference/doctrine/. Read the ID as an instruction to go and obey that rule in
  full. Where this file restates a rule it is because the mechanism has to be
  executed here, not because the ID is optional.
- **Every employer-specific value is a variable.** Variables are written in
  UPPER_SNAKE_CASE and are defined in reference/schema/. No literal company,
  system, brand, product, division, form, document number, location code,
  identifier, path or address ever appears in this file. See standing rule S1 and
  interview rule I9.
- **Binding is staged.** Ten organization variables are bound before the first
  run can produce anything (the IGNITION set). Everything else is DEFERRED and is
  requested at the moment a decision needs it, from someone who would know the
  answer, once. See reference/binding-interview.md.
- **An unbound variable never produces a wrong answer.** It produces exactly one
  of two things: the documented default from reference/schema/ SECTION A1 or A2, named
  in the output, or the degradation notice from that same appendix, printed in the
  output. See standing rule S7 and reference/schema/ SECTION B.
- **Companion files are invoked, not duplicated.** This file never restates their
  contents.

| File | What it settles | When this skill invokes it |
|---|---|---|
| reference/doctrine/ | The shared rules, by stable ID. Every rule whose Applies list carries REVIEW governs this skill. **The size of that set is a property of that file and is never restated here**, because a count copied into a second file is wrong the first time a rule is added. This skill also cites rules outside that set wherever one explains another it does enforce. | Continuously. Every SD- citation. |
| reference/schema/ | Every variable, its tier, state, validation, documented default and degradation notice. | Whenever a variable is read, and whenever one is found unbound. |
| reference/binding-interview.md | How a binding is asked for, by whom, and what happens when it is declined. | Stage 0, and at every point-of-need request. |
| reference/capability-probe.md | What the environment can actually do, and the degradation ladder for each capability. | Once, before Stage 0, every run. |
| reference/field-resolution.md | How a column is found inside a file the skill has never seen. | Stage 4, and anywhere a concept must be resolved against a header. |
| reference/output-contract.md | **THE UNIVERSAL OUTPUT CONTRACT.** The output medium keyed per skill; the formatting elements with their standards and their programmatic verifications, for the skills whose medium is a spreadsheet; the docx requirements D1 through D6, for the one whose medium is a document; the rank and reason-for-rank columns; rank continuity and the derived last rank; the per-sheet cap and the exact showing-note wording; the unit noun. | Invoked before publication, on every run. **`OUTPUT_MEDIUM` for this skill is docx per PART 1 of that file, so PART 3 governs this artifact IN FULL and PART 2 does not apply to it and is not scored against it.** **This skill CITES a requirement by number and never restates its standard**, because a restated contract is how the elements degraded to passing mentions and stopped being enforced. Where this file and the contract appear to disagree, the contract governs and this file is stale. |

## What this skill does not do

- It does not rank or evaluate named people. It writes about one person's own
  work, and it compares that work to positions in an anonymous distribution. A
  request to rank or evaluate colleagues is declined outright. See SD-LNG-02.
- It does not duplicate a capability that a downstream system owns. See
  SD-EXC-24 and SYSTEM_OF_RECORD_EXCLUSIONS.
- It routes requests that belong elsewhere through SIBLING_SKILLS. Where
  SIBLING_SKILLS is empty, an out-of-scope request is declined plainly rather
  than attempted.

## The character set rule, and why it is a standing rule

Every character this skill authors is keyboard ASCII in the set defined by
ALLOWED_CHARACTER_RANGE, which is a printable RANGE tested on BOTH bounds PLUS an
explicit list of permitted code points outside it. **The list is not empty and must
never be read as empty: the LINE FEED, code point 10, is permitted where a line
break is meaningful in the container, and is forbidden everywhere a value is one
line by construction.** A set expressed as a bare range cannot permit the line feed
and cannot be read as permitting it by implication, which is why the exception is
stated here and enforced in Part 10.1. This is not a style preference.
Output from this skill is programmatically scanned, pasted into systems with
narrower character handling than the drafting environment, and stored in records
that outlive the session. The full rule set is SD-FMT-14 through SD-FMT-20 and is
executed in Part 10 of this file. It applies to authored text, never to the raw
bytes of a binary container.

---

# PART 1: RUN DOCTRINE

Read this before anything else. It governs every decision below.

## 1.1 There is no time limit on this task

You are under zero time pressure. A run that takes twenty-five minutes and is
right is a complete success. A run that returns in four minutes with an
unverified number, a fabricated action, or a missing section is a failure no
matter how fast it returned. See SD-EFF-01.

NEVER shorten a sweep, skip a verification, drop a section, or summarize instead
of building because the work is taking a while. Length of run is not a cost this
method recognizes.

NEVER stop at a partial result and describe what you would have done. Finish it.

The only acceptable early stops are the hard gates in HARD_GATES, listed in Part
7.4 of this file. Fatigue, run length, retry count and output size are not on
that list and never will be. See SD-EFF-02.

## 1.2 Durability: write continuously, never hold work in memory

**THE RULE: after EVERY stage that produces a finding, a number or a paragraph,
APPEND it to the checkpoint before starting the next stage. Never carry more than
one stage of work in memory.** See SD-EFF-30.

Named append points in this pipeline:

| Stage | What is appended |
|---|---|
| Stage 2 | The goal ledger, block by block, as each source resolves. |
| Stage 3 | The evidence ledger, tier by tier, before the next tier starts. |
| Stage 4 | Parsed measures, per entity and per benchmark pairing, as each resolves. |
| Stage 6.4 | Each candidate win as its cut completes. |
| Stage 7 | Each proposal, with its confidence, as it is formed. |
| Stage 9 | The draft, section by section. |
| Any stage | Every question answer, on receipt. |

Two ordering rules travel with this one:

- **BUILD THE HEAVIEST THING FIRST**, while the run is freshest. Spending the
  early run on small pieces and reaching the largest one with nothing left is how
  a write-up ships with three polished objectives and a bare fourth. See
  SD-EFF-22.
- **FINISH EACH UNIT COMPLETELY BEFORE STARTING THE NEXT.** One objective fully
  drafted, verified and checkpointed, then the next. Never draft every objective
  shallowly and return to deepen them. See SD-EFF-23 and SD-EFF-25.

Checkpoint rules, all of them binding:

1. The checkpoint is written under SCRATCH_DIR, following CHECKPOINT_PATH_PATTERN.
   It is NEVER written to OUTPUT_DIR. SCRATCH_DIR must never equal OUTPUT_DIR.
2. It opens with a stop banner making clear it is not a deliverable.
3. It holds LEDGERS ONLY: raw findings, computed deltas, peer ranks, tie counts,
   lineage matches, the parse log, the probe record, and the proposal ledger with
   its confidences. It holds no assembled objectives, no narrative, and no block
   intended for pasting. If it contains nothing that looks finished, it cannot be
   mistaken for finished. See SD-EFF-31.
4. It records resume state.
5. It is deleted when the real artifact publishes, per CHECKPOINT_DELETE_ON_PUBLISH.
   It is NOT deleted on a bannered partial emit.
6. A stage that cannot write its checkpoint retries once, then continues with a
   warning that an interruption will require restarting the crawl. A checkpoint
   failure degrades durability, not correctness. See SD-EFF-33 and SD-EFF-14.
7. A stale checkpoint is worse than none. See SD-EFF-29.

In chat, never say the findings are ready. Say the crawl is done, then ask the
questions. See SD-EFF-32.

## 1.3 The retry ladder

An empty or failed read is UNCONFIRMED, never failed, until the ladder says
otherwise. Two failure modes look identical: a call that returns success and
lands nothing, and a service that lags its own write. Treat both as unconfirmed
and work the ladder. See SD-EFF-10.

| Attempt | Action |
|---|---|
| 1 fails | Wait per RETRY_BACKOFF_SCHEDULE, re-read, retry with one constraint relaxed. |
| 2 fails | Retry with the fallback method named in that stage. |
| 3 fails | Record the gap, use the documented fallback value, and CONTINUE. |

**One constraint relaxed**, in order of preference: widen a date window; lower a
match threshold; drop an optional filter; fall back from exact to fuzzy matching.
**Never relax a doctrine rule as a retry step.** See SD-EFF-11.

Retry is graduated, not counted: a transient failure has no attempt limit and
waits on RETRY_BACKOFF_SCHEDULE; a failure scoped to one unit narrows, retries to
SCOPED_RETRY_LIMIT, rebuilds, then degrades that unit only; a logical failure
repairs in place and re-verifies up to REPAIR_CYCLE_LIMIT; and only a named hard
gate stops the run. See SD-EFF-09.

A missing central or published source is NOT a hard gate. Neither is an
unreachable chat platform, an unreachable document store, or a message search
that returns nothing. See SD-SRC-13.

## 1.4 Ask questions to buy time

Stopping to ask the user a question is FREE. It costs no correctness and it
converts dead waiting time into useful input. When a stage will take a while, ask
the questions that stage needs while it runs, rather than saving them for a batch
afterward. See SD-EFF-38.

This is subject to QUESTION_BATCH_MAX and to the sequencing rule: a question never
fires before the stage that supplies its context. See SD-IDN-25.

## 1.5 Field character limits, a hard constraint verified per run

**THE SYSTEM TRUNCATES.** It does not warn, it does not wrap, and it does not tell
the user what was lost. A field written past the limit arrives in the permanent
record cut off mid-sentence. Every field this skill emits must be counted and must
fit. See SD-LNG-09.

**THE LIMITS ARE DEFAULTS, NOT FACTS.** They differ by field, by form version and
by tenant. FIELD_LIMITS supplies the standing defaults. They are confirmed per run
by the person who has the form open, and that answer is bound to
PERSON_CONFIRMED_FIELD_LIMITS for that user's run only. It never writes back to
the organization tier. A user with the form open can read the counter next to the
box in five seconds, and that answer is worth more than any assumption in this
file.

**THE SINGLE-FIELD QUESTION IS LOAD BEARING.** OBJECTIVE_FIELD_IS_SINGLE decides
the entire character budget. Where it is true, the objective box holds the title,
the description AND every measure as ONE capped field. It is not one limit for the
objective plus one limit per measure. Budget by FIELD_BUDGET_SPLIT.

**A COMPONENT WITH NO SOURCE IS ALLOCATED ZERO, AND ITS BUDGET IS RELEASED.** The
split names components the objective field can hold; it does not assert that the
source objective HAS all of them. The objectives a manager actually sets are very
often a title, a measure and a target and nothing else, and no evidence item is a
description of an objective as opposed to evidence of work against it. **Writing a
description to fill a budget is fabrication and is forbidden by 2.12 and SD-CNF-07;
leaving the budget unspent is not permitted either, because it silently shrinks the
field the person's own figures had to fit into.** So: where a component has NO SOURCE
in the objective or in the evidence, it is allocated ZERO and its share is released to
the remaining components IN PROPORTION to their own shares, the field holds the
components that do exist, and **the release is recorded in METHOD, naming the
component, the share released and where it went.** A description is never written to
fill a budget, and a budget is never left unspent to honour a split. This is the run
rule; the split itself remains FIELD_BUDGET_SPLIT's and is read from there.

Worked example of a budget split, **worked in PROPORTIONS and not in characters**,
because an example carrying a literal limit and a literal targeted fill restates two
schema defaults in the body of this file and was found restating one of them wrongly,
which is the defect class the whole no-literals rule exists to stop. The procedure, and
**the parts must sum to at or under the TARGETED FILL, never to the raw limit**: take
the confirmed limit for the objective field; multiply it by TARGET_FILL_RATIO to get
the targeted fill; split that fill by FIELD_BUDGET_SPLIT's own shares for the title,
the description and all measures combined; divide the measure share by the number of
measures the objective actually carries; and release the share of any component the
source does not have, per the rule above. Every alternative split is checked the same
way: add the parts and compare the total against the targeted fill, not against the
limit. **A split summing to the raw limit is over by exactly the margin
TARGET_FILL_RATIO exists to reserve**, and that margin is what absorbs an edit of the
person's own. The style consequence, which is why this example is here at all, is that
measures are written as bare imperatives: with several measures sharing one share of
one field, a measure carrying its metric, its population and its deadline in the
shortest true sentence is worth more than the same statement written half again as
long, because the extra characters buy nothing and eat more than half of another
measure.

**WRITE SHORT BY DEFAULT.** Do not write long and trim afterward. Target
TARGET_FILL_RATIO of the confirmed limit so that an edit of the user's own does
not push the field over. See SD-LNG-08.

**COUNT WHAT THE SYSTEM COUNTS.** Spaces, punctuation and line breaks all count.
Count the exact string that will be pasted, not the word count and not the visible
length. Emit the exact character count for every field.

**A LINE BREAK IS A CHARACTER THIS SKILL MAY WRITE, AND IT COUNTS AS ONE.** The
permitted set is ALLOWED_CHARACTER_RANGE, which is the printable range PLUS code
point 10. **Inside the text of a capped free-text field a line break is permitted**,
counts as exactly one character toward that field's limit, and passes the character
sweep in 10.1. **In a sheet name, a filename, a heading, a column header, an
identifier, a code or any single-line label it is forbidden**, because those are one
line by construction and an embedded break corrupts a lookup by name. **This
resolves what used to be a contradiction inside this file**: the counting rule here
required line breaks to be counted while the character gate forbade the character,
so a multi-paragraph free-text field, which a four-thousand-character limit plainly
anticipates, could not be written at all. Neither rule bends now, because the
permitted set carries the exception explicitly.

**A LINE BREAK INSIDE A FIELD IS PERMITTED, NOT ENCOURAGED.** Where the destination
field is single-line, or where the destination system's own handling of a break is
unknown, write the field as ONE paragraph. Where a break is written, it is written
because the field's content genuinely has paragraphs, and it never separates the
field's text from anything that is not that field's text.

**WHERE the count is SHOWN is settled by reference/output-contract.md PART 3.3, realized in
8.3, and WHEN it is RECOUNTED is settled in 7.6.** This section settles WHAT is
counted and what happens when a field is over, and those two rules are not restated
anywhere else in this file. **The count is NOT in the heading line and NOT above the
field text**: it is the block's own last line, below the text and above the next
heading, per that contract, which is cited and not re-argued here.

**COMPRESSION ORDER, WHEN A FIELD IS OVER.** Cut in COMPRESSION_ORDER and stop as
soon as it fits. The standing order, and the reasoning for each step:

1. Filler and hedging. Phrases that add length and no content.
2. Restatement. If the objective title already names the entity, the description
   does not need to name it again.
3. Lineage and rationale. The organization initiative and the metric weight belong
   in the conversation and in the verification list, not inside a capped box.
4. Scope qualifiers that repeat across every measure. State the scope once in the
   objective, not in all six measures.

**NEVER CUT**, per NEVER_CUT_LIST: a number, a population, a deadline, or the name
of an entity the writer is claiming credit for. **AND, PER 2.3, THE GROUND'S SHORT
FORM AND ITS MOVEMENT STATEMENT**, which no step of the order above reaches: they are
not filler, not restatement, not a lineage line or a rationale, and not a scope
qualifier repeated across measures. The ground's FULL name is not in the field at all,
so there is nothing there to cut; what is in the field is the short form 2.3 derives,
and dropping a named entity from that short form cuts nothing NEVER_CUT_LIST protects,
because that list protects entities the writer is claiming credit FOR and the ground is
by construction not one. **THE PROVISIONAL-PERIOD STATEMENT REQUIRED BY STAGE 4 PERIOD
VALIDATION ITEM 6 IS PROTECTED ON THE SAME TERMS AND FOR A STRONGER REASON**: it is not
filler, not restatement, not a lineage line and not a scope qualifier repeated across
measures, so no step of the order reaches it, and a field made to fit by dropping it
puts a figure from an unfinished period into a permanent record with nothing saying so. If the field still does not fit
after the last permitted cut, the objective is doing too much. OVER_LIMIT_REMEDY
is split_the_objective: split it into two objectives, or move a measure out. Never
drop a deadline to save characters, and never let a truncation reach the system.
See SD-LNG-10.

**WHERE COMPRESSION CHANGES THE SHAPE.** The lineage line is the first thing to go
from a pasted field, and it is still REPORTED to the person, because it is what
they say out loud in the review conversation. LINEAGE_LINE_PLACEMENT is
commentary_outside_the_field. See SD-LNG-11.

## 1.6 Acquiring sources, and the retrieval gate

The highest-value input this skill uses, a supervisor's stated direction, a target
list, a results summary, very often arrives as an attachment on a message rather
than as a document in a store. A run that cannot open attachments cannot see the
thing it most needs. This protocol is not optional and its forbidden list is not
advisory. See SD-SRC-01.

**A list from the user's own manager outranks every other input this method
reads.**

The ladder, stated generally because the specific calls belong to whatever mail
and document stack is bound. Every rung is doctrine; the tool names are not.

1. **List messages by SENDER**, never by keyword, across MAIL_SWEEP_FOLDERS and
   SUPERVISOR_SWEEP_WINDOW_CURRENT. Where the tool writes a large result to a file
   rather than returning it, READ THE FILE. A run that treats a spilled response as
   empty will report no mail from a manager who wrote twenty messages. See
   SD-PRI-02 and SD-SRC-09.
2. **Enumerate attachments on every candidate message.** Never decide from a
   subject line whether a message carries a file. The attachment filename is often
   the real content even when the subject says nothing. See SD-SRC-07.
3. **Never use a reported size to decide a file is too big.** A reported attachment
   size is the encoded size, roughly MIME_ENCODING_FACTOR times the real file. See
   SD-SRC-08.
4. **Fetch the bytes by the streaming path.** Request the resource and read the
   bytes out of what comes back. Do not send field-selection parameters on a byte
   fetch. Reading the field name and then asking for it by name is the single most
   common way this step fails, and the resulting error text points at a call that
   returns metadata only, so a reader who follows it loops and concludes the
   attachment is unreachable. See SD-SRC-05.
5. **The same address is correct streamed and corrupt decoded as text.** The
   difference is whether the bytes are streamed to a file or decoded through a text
   response. See SD-SRC-06.
6. **Fall back to an inline encoded fetch**, one attachment at a time, subject to
   INLINE_FETCH_CEILING.
7. **If truncated, recover what you can, and report WHICH parts were recovered**,
   not merely that the file was truncated. Reconcile the recovered record count
   against any count the message body itself prints; where they agree exactly, the
   list is complete for scope and is reported as complete with a note on how the
   recovery was confirmed. A partial FETCH is not the same as partial DATA. See
   SD-SRC-03.
8. **If the message references a file rather than attaching it**, resolve it by
   filename in DOC_STORE_NAME. A file sent hours ago will NOT be in search yet; do
   not conclude from a search miss that it does not exist. See SD-SRC-10.
9. **Only after all of the above**, ask the user to supply the file, naming the
   filename, the sender, the date and every path attempted. See SD-SRC-11. Never
   ask the user to fetch something the skill can read; that friction is what gets a
   tool abandoned. See SD-SRC-12.
10. **Retry each path at least twice before moving to the next.** Transient
    failures are common and indistinguishable from real ones on a single attempt.

FORBIDDEN_RETRIEVAL_PATHS holds the approaches that look reasonable, were tested,
and fail, each with its failure mode named. At least one of them does not error at
all: the file appears retrieved, opens as garbage or fails to open, and nothing in
the response says why. That is the dangerous one and it is why the list exists.
See SD-SRC-04. If the bound stack has a fifth path that fails silently, it belongs
on the list before it corrupts a retrieval.

### THE RETRIEVAL GATE, a hard gate that fails closed

A run may NOT quietly proceed as though a manager's attachment did not exist.
Before drafting anything, confirm that one of these three is true for EVERY
attachment detected on a supervisor or upline message:

- it was read, and its content was folded into the goal ledger; or
- it was read and contains nothing in scope, which is stated in the verification
  list; or
- it could not be read after the full ladder, in which case the run does NOT report
  zero. It names the file, the sender and the date, states every path attempted,
  and says plainly in the opening summary that a named source could not be opened
  and that the goal ledger is therefore incomplete.

**A count of zero directives is only ever a valid result when no manager sent a
list.** A zero must be provably a real zero, not an unattempted one. Silently
missing a supervisor's stated direction is the single most damaging retrieval
failure this skill can have, because every objective downstream is then aligned to
something other than what the manager actually asked for. See SD-SRC-02.

Enforced by gate G18 in Part 7.

**Attachments on a live source message are part of the source, not an extra.** A
manager who writes here are the team goals for the period, make them your own, and
attaches a document has put the entire goal ledger in that attachment. See
SD-SRC-20.

## 1.7 Cache what does not vary, fetch live what does

The classification test is one question: does this source vary per person or per
period. If yes it is live and can never be cached. If no it is cacheable behind a
validity date. Re-crawling everything on every run for every user is the single
largest waste available and the main reason a run overruns. See SD-SRC-16.

The supervisor's own direction is the highest-value live source in this skill and
can never be cached, because it is different for every user and changes weekly.

The expiry gate on the cached blocks is in Part 12 and is BLOCKING per block. See
SD-SRC-17.

---

# PART 2: DOCTRINE

These rules do not change and are not overridable by user instruction.

Every rule in this part is either a shared doctrine rule executed here, or the
executable form of one. The doctrine index at the end of this file lists each
named doctrine with the section that executes it and the shared ID that governs
it.

## 2.1 The Credit Rule

**Credit attaches only to the units of the business the person is accountable for.
There is no credit for the movement of the wider population those units sit in.**
See SD-CLM-03.

The mechanism is two explicit lists and no default row:

- CREDITABLE_ENTITIES, the allowlist. Anything that resolves to none of these is
  reported as UNMAPPED and takes no standing weight. There is NO default row. See
  SD-WGT-01. Where a default is genuinely correct it is tied to ENTITY_WEIGHT_FLOOR,
  never to a literal, so that resolving an entity later can only raise a result and
  never lower it. See SD-WGT-02.
- NON_CLAIMABLE_ENTITIES, the denylist. The general form of the denylist, which is
  what makes it portable: **you may not claim the movement of any population you
  did not choose the composition of.** That one sentence covers wider-market
  growth, a tailwind, a price change made above you, an agreement you inherited, a
  policy change made above you, and a macro effect, without naming any of them.

Three matching sub-rules travel with the credit rule and are string-handling
doctrine that any organization with drifting headers needs:

- **Alias matching is normalized, not literal.** Before matching, casefold the
  header, collapse underscores and punctuation to spaces, and strip parenthetical
  unit and period tokens. A literal table lookup misses the single most important
  column in a real file. See SD-PRS-41.
- **An alias that is a common short word, or that carries punctuation, needs a
  sentinel.** Replace such an alias with a sentinel token BEFORE stripping
  punctuation, then match the sentinel. NEVER register the bare remainder as an
  alias. The general rule is that coincidental substring containment is never
  evidence: convert through an explicit table, then match exactly. The documented
  harm from getting this wrong: a bare two-character remainder falsely attributed
  more than two hundred rows of unrelated flags to one entity. The same class of
  error appears wherever a short code happens to sit inside a longer word.
  SENTINEL_TOKENS holds the protected set. See SD-PRS-42 and SD-QUA-05.
- **A sub-entity inherits its parent entity and its parent's benchmark.** If an
  alias is unrecognized, do not guess the parent. Flag it and ask, per
  ENTITY_ALIAS_UNRECOGNIZED_ACTION, whose permitted values are flag_and_ask and
  flag_and_floor and never guess_parent. See SD-PRS-43.

Enforced downstream by gate G1 on the MEASURED ENTITY of each number, and by 8.4
on the grammatical subject of each sentence.

## 2.2 THE COUNTERFACTUAL DENOMINATOR

This is the load-bearing generalization of the whole credit doctrine, and it is
the reason this skill works at a business with no competitive category.

**Every number carries a second number the writer did not choose.** The general
name for that slot is the COUNTERFACTUAL DENOMINATOR: the figure that answers
"compared to what, and how much of that was you". A competitive category is one
instance of that second number. It is not the requirement. See SD-CLM-04 and
governing rule G4.

The ladder is fixed and is not configurable. What IS configurable is which rungs a
business can supply (COUNTERFACTUAL_AVAILABLE_RUNGS), which rung each metric uses
(COUNTERFACTUAL_BY_METRIC), which rung applies when a metric has no assignment
(COUNTERFACTUAL_DEFAULT_RUNG), and how strongly a claim on each rung may be worded
(CLAIM_STRENGTH_BY_RUNG).

| Rung | Key | What it is | Why it sits here |
|---|---|---|---|
| 1 | share_of_addressable | Share of a bounded addressable population. | Best. Any business with a bounded addressable set has this even with no outside competitor. |
| 2 | matched_control | An untouched, unassigned or later-treated segment inside the same business. | The same environment, minus the writer. Strongest available where there is no external market. |
| 3 | peer_distribution | The distribution of sibling units at the peer level. | Controls for anything that moved under everybody, provided the movement was shared. |
| 4 | plan_attainment | Percent of a target set before the period by someone other than the writer. | Negotiable, so weaker; but attainment above target is still one of the strongest claims a person can make. |
| 5 | own_prior_run_rate | The writer's own prior-period run rate. | Weakest numeric benchmark. It controls for nothing external and it is exactly the claim the ground-moved failure punishes. |
| 6 | bare_denominator | A population count that bounds the magnitude, of the form n of N. | Not a comparison. The floor. No number ever ships alone. |

### 2.2.1 The rung decides the arithmetic, and the arithmetic degrades honestly

The two comparative quantities in 2.4 are defined against a benchmark. Which
quantities exist depends on the rung, and a quantity that does not exist at a rung
is NOT approximated by a neighbouring one. It is reported as not available for that
metric, with the rung named.

**The rung-by-rung table is SD-CLM-33 and it governs all three skills in this
bundle.** Read it there and apply it as written. It was promoted out of this file
unaltered, so that two skills can no longer produce two different answers off the
same configuration and the same data. This section does not restate it; what
follows is what this skill does with it.

**Degrading honestly means saying which rung was used, not pretending a stronger
one was available.** RUNG_DISCLOSURE_REQUIRED should be true, and its documented
default is true. Every figure names what it was compared against.

**A weaker rung is never silently substituted for a stronger one that failed.** If
a metric is assigned to a rung and that rung's own inputs do not resolve, the
metric drops to the highest rung that DOES resolve and is bound, the drop is stated
beside the figure, and the claim strength drops with it. It does not keep the
wording the stronger rung would have authorized. See SD-PRS-40.

**PRECEDENCE. An unbound value never overrides a bound one.** SD-CTR-24 and
standing rule S9. Precedence runs downhill from evidence to convention: a value
bound at ignition; a value bound later; a value derived from the data this run; a
documented default. A documented default applied to an unbound variable may NARROW
what the run attempts. It may never contradict, replace or silently supersede a
value the organization actually bound.

Before applying any documented default, test whether it would change a decision a
bound value already decided. If it would, the default is not applied to that
decision: the bound value stands, the run does only the part the unbound variable
was needed for, and the notice names the NARROWING rather than the substitution.

**The named case, because it is the one that inverted precedence in acceptance
testing.** ENTITY_BENCHMARK_MAP maps each creditable entity to exactly one
benchmark population, and it is DEFERRED. At a business with no wider population
it will never be bound, correctly, and the interview blesses that answer. Its
absence therefore removes **rungs 1 and 2 only**, because those are the only two
rungs that need a benchmark POPULATION. Every affected figure falls to the highest
rung that COUNTERFACTUAL_AVAILABLE_RUNGS still supplies and whose own definition is
bound, and the claim strength falls with it. **A figure reaches the bare
denominator ONLY where no other bound rung resolves.**

An entity absent from the map is UNBENCHMARKED for rungs 1 and 2, laddering through
its own parent entity. Record it explicitly rather than leaving it unmapped by
accident. See SD-CLM-14.

**THE SECOND NAMED CASE, WHICH INVERTED PRECEDENCE THE OTHER WAY AND DELETED THREE
BOUND RUNGS WITH ONE UNANSWERED QUESTION.** COUNTERFACTUAL_DEFAULT_RUNG is an
IGNITION value that NO ORGANIZATION DOCUMENT ANSWERS, because it asks about this
method's own configuration rather than about the business, exactly as
BINDING_OWNER_CONTACT did. A run bound faithfully from an organization's own
published objectives, its production file and its plan documents reaches it
unanswered every time and will keep doing so. **It is therefore DERIVED BEFORE IT IS
FLOORED, and the derivation is its IGNITION ROW in reference/schema/, which is the
only statement of it.** Read that row and execute it: where
COUNTERFACTUAL_AVAILABLE_RUNGS is bound or derived, the default rung is the HIGHEST
rung present in the available set whose own definition is bound; it is recorded
DERIVED at MEDIUM confidence, the derivation is named beside the claims it governs,
and it is read back for correction at the interview close. **DERIVED satisfies
ignition; counting it ANSWERED does not**, exactly as for PLANNING_PERIOD_LENGTH_DAYS
in 3.2. COUNTERFACTUAL_AVAILABLE_RUNGS carries a derivation of its own in the same
row, from which rung definitions are bound, floored at the bare-denominator rung, and
it runs first because the default is derived from its result.

**THE FLOOR CONSEQUENCE APPLIES ONLY WHERE NO AVAILABLE RUNG'S OWN DEFINITION IS
BOUND.** A run that struck rungs 1 and 2 for want of a benchmark population, bound
the peer, plan and prior-run-rate rungs from the organization's own documents,
computed all three and produced labels from them, and then worded every claim at the
floor because one configuration question went unanswered has DELETED THE EFFECT OF
THREE BINDINGS THE ORGANIZATION ACTUALLY MADE. **That is the precedence rule running
backwards.** It is forbidden by standing rule S9 and SD-CTR-24, and it is regression
case 15 with the tiers swapped: an unbound IGNITION value overriding bound ones is
the same defect as a deferred default deleting an ignition binding, on the same axis
and for the same reason. Regression invariant 10 in 7.5 tests it at every gate and
regression case 26 fixes it as a case.

**THE SAME TEST IS RUN ON EVERY IGNITION MEMBER BEFORE ITS FLOOR IS APPLIED, AND IT
IS ONE QUESTION: could a documents-only binding answer this at all?** Where it could
not, the floor is not an honest consequence of an incomplete binding, it is a
permanent cap on a run that did everything asked of it. The run then derives what the
documents DID answer, records the derivation with its evidence, names the value as
one no document can supply, and queues that finding to BINDING_OWNER_NAME. **A floor
never stands in for an answer no organization can give.**

**The general form, which applies to every unbound value in this skill and not
only to that one:** an unbound value that supplies ONE rung, ONE flag or ONE
section removes only that rung, that flag or that section. The run then falls to
the best remaining BOUND option, never past it to the floor.

**WHAT EACH OF THE THREE CLAIM STRENGTHS ACTUALLY READS LIKE, BECAUSE A SCALE WHOSE
MIDDLE VALUE IS UNDEFINED IS A SCALE TWO IMPLEMENTERS WILL WRITE DIFFERENTLY.**
CLAIM_STRENGTH_BY_RUNG takes one of three values per rung and **the MAPPING of rung to
strength is that variable's and is read from its row in reference/schema/, never from
here.** What belongs here is what this skill's prose does with each value, because the
prose is this skill's own work:

| Strength | What a sentence at this strength does | What it may never do |
|---|---|---|
| strong | States the result as an ACHIEVEMENT, against a comparison the writer did not choose and did not build. | Nothing beyond the ordinary rules; this is the top of the scale and it is reached only where the rung earns it. |
| qualified | States the same figure WITH what it was measured against, named, and WITH the ground and what is known about its movement, per 2.3 and gate G19. It is a claim, not a hedge: the figure and its comparison both stand. | **No word asserting that the writer CAUSED the result**, and no achievement wording that would survive the comparison being removed. |
| bounded | States a number with its DENOMINATOR POPULATION and its scope, per 2.2.3. | **No achievement wording of any kind**, and no comparison, because there is none to name. It is not eligible for a WIN label. |

**THE DIFFERENCE BETWEEN STRONG AND QUALIFIED IS NOT VOLUME, IT IS ATTACHMENT.** A
qualified sentence carries its comparison and its uncontrolled ground INSIDE the claim,
in the person's own register per 10.2.1, so a reader who deletes the attachment is left
with a sentence that no longer says anything. A strong sentence can stand without them
because the rung already supplies them. **A run that writes a qualified claim as though
it were strong, and puts the attachment in a following sentence, has written a strong
claim with a footnote**, and gate G19 fails it. Every one of the three is written in the
person's own words, and none of the three may carry a rung key, a band name or a
classifier token inside a block, per 10.2.1 and gate G13.

**Rung 6 is a floor, not a failure.** An execution claim with a denominator
population is a legitimate, gate-passing claim. Worked example, neutral: a
maintenance planner writes "completed 47 of the 61 inspections flagged for the
period". That number has a bound, a population and a scope. It does not have a
comparison, so it may not be worded as an achievement relative to anyone, and it
is not eligible for a WIN label. The floor is what stops a business with no market
being told it cannot make claims. The defect is always the ROUTING into the floor,
never the floor.

### 2.2.2 When rank is primary and when it is supplemental

**Where the environment can move underneath everyone, a peer rank is supplemental
and NEVER a substitute for the counterfactual denominator**, because an entity can
rank first among peers while lagging its benchmark, which is a MISS. **Where there
is no such shared environment, the peer distribution IS the primary control.**

Which case applies is a binding, not a judgment. The test:

- If rung 1 or rung 2 is available AND MOVING_GROUND_SOURCE can be read this run,
  the shared environment is measurable. Rank is supplemental.
- If neither is available, or MOVING_GROUND_SOURCE cannot be read, the shared
  environment is not measurable. Rank is primary, subject to the tie-count rule
  (2.13) and ANONYMITY_FLOOR, and the output states that the environment could not
  be measured and that rank is therefore the strongest available control.

**A peer set is drawn from siblings, never from subordinates**, and a role at the
top of the chain has no internal peer set at all. SD-SPN-14 and SD-SPN-15, executed
at Stage 4 item 7. Where no peer set exists, rung 3 is dropped for that run and the
drop is named, per SD-CTR-24: the run falls to the highest remaining BOUND rung and
never past it to the floor.

**And a peer set that EXISTS but is below EITHER of the two peer floors is neither of
those two states.** SD-SPN-16, executed as Test 3 at Stage 4 item 7: the run walks
outward one level at a time until a set meets BOTH ANONYMITY_FLOOR and
MIN_POPULATION_FOR_NORM, stops at the first level that does, publishes nothing at all
from any level below ANONYMITY_FLOOR, draws no comparison at all from a level below
MIN_POPULATION_FOR_NORM, and prints the level actually used and its count beside every
figure that reads it. **Rung 3 survives the
walk at a DIFFERENT group, which is stated, and never at a stronger claim strength
than a same-level comparison would have carried.** Where the chain is exhausted the
rung is dropped exactly as it is for an empty set.

See SD-CLM-16.

### 2.2.3 THE COLD START

A COLD START is a run in which the population being scored has no prior period of
its own. **It is a first-class operating condition, not an arithmetic edge case.**
SD-CLM-27 governs, and where this section and any other instruction in this file
disagree about a cold population, SD-CLM-27 through SD-CLM-33 govern.

A cold population is a normal thing for a business to have: a launch, a new line, a
new market, a new site, an acquisition still on its own systems, a person who took
over a book last quarter. **The method's job is to say true things about it, not to
refuse.**

**Two kinds, never conflated.**

| Kind | What it is | How it is handled |
|---|---|---|
| A COLD UNIT inside a WARM population | One unit is new; the population around it has history. | The existing rules already handle it: include the unit at the floor of the measure, rank it last, keep it visible there rather than dropping it, and leave its period-over-period change blank rather than infinite. SD-POP-12, SD-CMP-03. Nothing in this section changes that. |
| A COLD POPULATION | No unit, or almost no unit, has a prior period. | This section. Every comparison the method would normally draw is either undefined or is drawn against something the writer's own team is currently building. |

The test that separates them is the share of the in-scope population carrying a
usable prior-period value, against COLD_START_MIN_PRIOR_SHARE. Above it the
population is WARM and any unit below it is a cold unit. At or below it the
POPULATION is cold.

**A cold start is DETECTED, never declared.** SD-CLM-28. The run detects it from
the data. It does not wait for the person to say so, does not ask, and does not
rely on a binding. A person living inside a launch does not think of themselves as
an edge case and will not volunteer it, and an executive answering a binding
interview answers for the mature business, because that is the business they run.

Three tests, all of which run on every run before scoring, and any one of which
marks the population COLD:

**SD-CLM-28 OWNS THESE THREE TESTS AND GOVERNS WHERE THIS RESTATEMENT DIFFERS**,
including the corroboration rule and what counts as NOT EVALUABLE.

1. **THE HISTORY TEST, AND IT IS ONLY EVALUABLE WHERE A PRIOR-PERIOD COLUMN
   RESOLVED.** The share of in-scope units carrying a usable prior-period value is
   at or below COLD_START_MIN_PRIOR_SHARE. Where NO prior-period column resolved
   at all, the share is UNDEFINED, not zero, and this test DOES NOT FIRE and DOES
   NOT PASS: it is recorded NOT EVALUABLE with the reason. A single-snapshot
   export carries no history column and is not thereby a young population.
2. **THE ENTRY TEST.** No in-scope unit has an entry date before the current
   window opened, or the earliest entry date found sits inside the current or the
   immediately preceding window. Under FLOW this is the sharpest of the three,
   because entry dates are always present. See Part 13.
3. **THE UNIFORMITY TEST.** The ranking measure is zero, blank or identical across
   the whole in-scope population, which is what a population with no history looks
   like when it has no entry date to read either.

**Record which test fired, and the figure that fired it, in the audit and in the
front panel. A detection nobody can see is a guess with better manners.**

**THE CORROBORATION RULE. A SINGLE FIRING TEST THAT ANOTHER EVALUABLE TEST FLATLY
CONTRADICTS DOES NOT MARK THE POPULATION COLD ON ITS OWN.** Where exactly one
test fires and a DIFFERENT test that WAS evaluable points the other way, record
the population COLD-CONTESTED rather than COLD. Name the contradiction on the
front panel with both figures. The claim restrictions still apply, because the
safe reading is the restrictive one, but rung re-evaluation does NOT strike a
rung whose only ground for striking is the contested test. The worked
contradiction, neutral: a file with no prior-period column at all and an earliest
entry date two decades before the current window. The entry test is answerable
from the data and is evidence of a long-established population; nothing about the
missing column outranks it.

Where TWO OR MORE tests fire, or where the only firing test is uncontradicted by
any evaluable test, the population is COLD, full stop, and no corroboration is
required.

**Record every test that was NOT EVALUABLE, and why.** A reader cannot weigh a
detection without knowing how many of the three tests could actually speak.

Detection is scoped to the population being scored, per SD-POP-23 and Part 13. A
business may be warm in one population and cold in another on the same morning,
and usually is.

**RUNG AVAILABILITY IS RE-EVALUATED, NEVER INHERITED.** SD-CLM-29. A cold
population does not inherit the rung availability of the mature business around it.
Where COUNTERFACTUAL_RUNG_SCOPES carries an entry for this population, that entry
governs. Where none exists and the population is detected COLD, the
organization-wide list is NOT inherited: each rung is tested against the cold
population on its own terms and struck where it fails.

| Rung | Under a cold population |
|---|---|
| 1 share of addressable | STRUCK unless the addressable set is bounded by something outside the writer's own action. See the independence test below. |
| 2 matched control | Available only where a genuine untreated segment exists inside the COLD population itself. A control drawn from the mature business is not a control for the launch. |
| 3 peer distribution | Available only where the peers are also cold. Ranking a cold unit against warm peers measures age, not performance. |
| 4 plan attainment | Normally AVAILABLE, and usually the strongest rung a cold population has, provided the plan was set before the period by somebody other than the writer. |
| 5 own prior run rate | STRUCK by definition. There is no prior run rate. |
| 6 bare denominator | Always available. It is the floor and it is never struck. |

**Name every rung struck, and why, beside the figures it would have carried.**

**THE INDEPENDENCE TEST.** SD-CLM-30. A comparison is only a comparison when the
second number was not chosen, and is not being created, by the person making the
claim. Where the denominator of a share is itself under construction by the work
being claimed, that share is not a counterfactual. It is the numerator wearing a
second name.

Run it per metric, on every run, **not only on a resolution failure**:

1. Does the denominator column resolve and populate? **A denominator that resolves
   and populates is NOT thereby independent.** The old guard fired only on a
   resolution failure, and that is exactly why it missed.
2. Is the denominator a sum that includes the numerator? If so, compute the
   numerator's share of it.
3. Where that share exceeds ADDRESSABLE_SELF_SHARE_CEILING, or where the
   denominator's own period-over-period movement tracks the numerator's within
   the DEADBAND band **for the rung being tested, read in that band's own named
   unit** per 2.5, across the population, the set is SELF-BUILT. **Strike the rung,
   say so, and name the figure that fired the test.**

**A denominator whose value is being created by the writer's own team caps claim
strength at BOUNDED for every figure computed against it, whatever rung the
organization bound.** Bounded means a number with its denominator population and no
achievement wording.

The failure this prevents, stated so it is recognizable: a launch computes share of
a population that is the sum of the authorizations the writer's own team has just
won, arrives at a share near one hundred percent by construction, and ships it at
achievement strength with a WIN label. Every gate passes. Regression case 10 tests
it.

**NO BASELINE, a distinct state.** SD-CLM-31. Where the population is COLD, the
win, miss and flat classifier **does not fire**. No figure in that population
carries a WIN, a MISS or a FLAT label. This is an independent block, not the floor
rung turning the classifier off, and it applies even where a rung that normally
supports a label is in force, because a label asserts movement and there is nothing
to have moved from.

The state emitted instead is **NO BASELINE**. It is a real state, it is printed,
and it is distinguishable from UNPAIRED, from FLAT and from a suppressed label. A
reader must be able to tell the difference between "this did not move", "this
cannot be compared" and "this has nothing to be compared to yet".

**A plan attainment figure is EXEMPT from this block** and keeps its own three
states, because attainment compares against a target rather than against a prior
period, and a launch normally has a target. That is the point of the exemption.

**WHAT A PERSON MAY HONESTLY CLAIM DURING A COLD START, WHICH IS NOT NOTHING.**
SD-CLM-32. The cold-start rules forbid a specific class of claim. They do not
forbid claiming. A launch is often the hardest work a person does all year and this
method must be able to say so. Three kinds of claim survive a cold start intact,
and the run surfaces **all three** rather than waiting to be asked:

1. **ABSOLUTE BUILD.** What exists now that did not exist at the start of the
   period, stated as a count with its unit and its period. Doors opened, accounts
   activated, sites certified, programmes live, requirements implemented. It
   carries no comparison and needs none, because it is a statement of construction
   rather than of relative performance.
2. **SEQUENCING AGAINST PLAN.** Attainment against a target set before the period
   by somebody other than the writer, in percent of target, with the three-state
   classifier that belongs to attainment. This is normally the strongest claim a
   cold population supports and it is a genuinely strong one: exceeding a launch
   plan is a real result.
3. **EXECUTION AGAINST A DENOMINATOR POPULATION.** The floor rung, and a
   legitimate gate-passing claim: so many of so many eligible, with the eligible
   set named and bounded.

**A cold-start run that produces none of these three has not done its job. Absence
of a comparison is not absence of a finding.** This is the over-correction to
refuse: a cold run that returns nothing has failed exactly as surely as a cold run
that ships a fabricated share.

State the sequencing claim at the writer's own altitude and with a contribution verb
where it ladders above their scope, exactly as any other claim. **Nothing about a
cold start relaxes the altitude ceiling.**

**The front panel says, in plain words, that this population has no prior period,
that no win or miss labels were computed for that reason, which detection test
fired and with what figure, and which of the three claim kinds each figure below
is.**

**A COMPARISON REQUEST AGAINST A COLD POPULATION IS ANSWERED, NOT STOPPED.**
SD-CMP-08. A request to compare two periods, made against a population where no
unit predates the current window, is not a missing-file problem and must not be
answered by asking for a file that does not exist and never will. Before any
one-input stop fires, test the population's own entry dates. Where the population
is COLD:

1. Say that no prior period exists for this population, and name the earliest entry
   date found as the evidence.
2. Offer the second numbers that DO exist: attainment against a plan set before the
   period, and the bare denominator population.
3. Emit the current state and the absolute build to date.

The one-input stop survives unchanged for a WARM population. It is a correct guard
against a person who forgot to attach the second file, and a dead end only for a
person whose second file cannot exist.

**A UNIFORM MEASURE IS NEVER A SILENCE.** SD-POP-27. Where the ranking measure
takes the same value for every unit in the population, which is what a cold
population usually looks like, every unit receives the same percentile, the measure
factor becomes a constant, and the ordering is decided entirely by the other terms.
That is often the correct behaviour and it is never an acceptable silence. State it
on the front panel in those words, name the terms that actually decided the order,
and never print a measure percentile column of identical values without that
statement beside it.

### 2.2.4 THE SHAPE OF A TARGET DECIDES THE ATTAINMENT ARITHMETIC

**THE PRINCIPLE IS SD-CLM-33 AND IS CITED, NEVER RESTATED: attainment is not one
formula, the SHAPE OF THE TARGET decides the arithmetic, and the shape is DECLARED
BEFORE THE DIVISION IS DONE.** That rule also settles what happens when the division
cannot be done: **where attainment is undefined for the target as stated, rung 4 emits
NO LABEL, the figure drops to the highest remaining rung with the drop NAMED beside
it, and the target is NEVER REWRITTEN to make the division work.** SD-POP-18's
degenerate table carries the zero TARGET as a guarded divisor. Obey all of that as
written.

**What the doctrine deliberately leaves to the skill is the SET OF SHAPES and the
arithmetic of each, and that is what this subsection supplies.** It adds no rung and
changes no band: it says which numerator and which denominator go into the division,
per shape, and what the result means, so that two implementers cannot compute two
different attainments off one objective.

**FIRST, CLASSIFY THE TARGET. The shape is read from how the target was WRITTEN, by
whoever set it, and is never chosen to make the arithmetic convenient.** Record the
shape beside the figure. The four shapes, and every target this skill receives is
one of them:

| Target shape | How it was written | Attainment | What the figure MEANS |
|---|---|---|---|
| LEVEL | A value the measure is to reach: a rate, a count, a currency amount, a share. | actual level divided by target level, in percent of target. | How much of the destination was reached. 100 percent is arrival. |
| CHANGE | A movement the measure is to make: grow by n percent, add n units, cut n points. | ACHIEVED CHANGE divided by TARGETED CHANGE, in percent of target, where the achieved change is measured from the same baseline the target was set from. | How much of the movement was made. 100 percent is the whole movement. |
| ZERO | A target of zero: no open items, no lapses, no reportable events. | UNDEFINED. There is no division to perform. | Nothing. The classifier does not fire. See below. |
| CEILING | A value the measure must stay AT OR UNDER, where the target names a maximum rather than a destination. | target divided by actual, in percent of target, so that beating a ceiling reads above 100 exactly as beating a floor does. | How far inside the ceiling the measure stayed. Under 100 is an overrun. |

**THE CHANGE CASE IS THE ONE THAT PRODUCES OPPOSITE LABELS, AND IT IS NOT RARE. It
is what an objective of the form "grow the measure by 6 percent" is.** The two
readings are both arithmetically valid and they disagree: read as a change, an
achieved 2.7 points against a targeted 6.0 points is 45 percent of target and a wide
MISS; read as a level, the same year is the achieved value against the value 6
percent growth implies, which lands inside a five-percent band and reads ON PLAN.
**Same two numbers, opposite labels, in a permanent record.** The rule is that **the
shape of the target as WRITTEN decides**: a target that names a CHANGE is attained
by change over change, and the band is read against that quantity. **The reading
actually used is printed beside the figure, naming the shape**, so a reader can see
which question was answered.

**AND WHERE THE TWO READINGS CROSS THE BAND IN OPPOSITE DIRECTIONS, BOTH ARE
PRINTED.** That is not hedging and it is not two labels: ONE label is emitted, from
the shape as written, and the other reading is printed beside it as a figure with
its own basis named and no label of its own, so that a reader who was thinking in
levels is not silently told they missed. Where the two readings agree on the label,
only the governing one is printed.

**THE ZERO TARGET, WHICH IS A DIVISION BY ZERO AND IS NOT A LABEL.** A target of
zero open items is an ordinary, well-written objective and it has no attainment
percentage, because every attainment form above puts the target in a denominator.
SD-POP-18 requires every divisor to be guarded before dividing and its degenerate
table carries the zero TARGET as one of those conditions. This is how this skill
executes it:

1. **Attainment is UNDEFINED and no percentage is computed.** Not 0, not 100, not
   infinity, and never the numerator printed as though it were a percentage.
2. **The rung-4 classifier does NOT fire on that measure.** No WIN, no MISS, no ON
   PLAN. A label computed from an undefined quantity is not a weaker label, it is a
   fabricated one.
3. **The measure ships at rung 6, with its denominator population**, per 2.2.1 and
   SD-CLM-33's floor row: the count achieved, the population it was counted over,
   and the target stated as the zero it is. "Closed the period with 2 open items
   against a target of none, across the 46 accounts in scope" is a complete,
   gate-passing statement and is what this case produces.
4. **The drop from rung 4 to rung 6 is NAMED beside the figure**, per
   RUNG_DISCLOSURE_REQUIRED and SD-CTR-24, with the reason stated as the zero target
   rather than as a missing input, because a reader who is told an input was missing
   will go looking for it.
5. **The target is never rewritten to make it divisible.** Not to "at most 2", not
   to "a 90 percent reduction", not to any restatement that manufactures a
   denominator. That is inventing a target, which 2.12 and SD-CLM-21 forbid outright.

**A NEGATIVE OR ABSENT TARGET TAKES THE SAME PATH AS ZERO.** Guard the divisor, do
not divide, drop to rung 6 with the denominator population, and name the drop. **The
guard runs BEFORE the division on every rung-4 figure, without exception**, because
a division by zero that reaches an artifact does not fail loudly: it prints as an
error string, an infinity or a plausible-looking number, and the third one is the
one that gets pasted.

**WHAT IS NOT CHANGED HERE.** The rung-4 band is still the fixed percent-of-target
band, still needs no peer spread, and still labels plan attainment for a reader with
no peers at all, per 2.5 and SD-CLM-34. What this subsection changes is only WHICH
QUANTITY the band is read against, and it names that quantity per target shape so
that two implementers cannot compute two different attainments off one objective.

## 2.3 Every business must name what its ground is

A business with no external market is not a business without a benchmark. It is a
business whose benchmark is internal. But the specific failure that the
ground-moved warning exists to deliver, **that a large positive number can still be
a miss because the ground moved underneath it**, arrives in such a business as a
rising baseline rather than as a rising market. It does not go away. It only
becomes harder to see.

MOVING_GROUND_NAME is an IGNITION binding for exactly this reason. It is the answer
to the question: last period somebody here had a number that went up and it still
was not good, because something moved underneath it; what moved? Volume,
seasonality, mix, staffing, an upstream policy change, a rate change made above
them, a weather year, a regulatory deadline. Every business has one. See SD-CLM-05.

**ENFORCEMENT. A claim does not ship at achievement strength until the ground it
moved against is named.** Three consequences, all of them mechanical:

1. Every claim carrying a number names the ground and states what is known about
   its movement this period: a figure where MOVING_GROUND_SOURCE could be read, and
   the words "movement not measured this period" where it could not. **WHICH FORM of
   the name a claim carries is settled in the placement rule below, and the movement
   statement is carried in every case.**
2. Where MOVING_GROUND_NAME is UNBOUND, this run executes the specific consequence
   stated in that variable's IGNITION ROW in reference/schema/, which is the only
   statement of it: claim strength is capped, no figure ships at achievement
   strength, every figure prints with its denominator, and the artifact states that
   no ground has been named. **The run is not stopped and the numbers are not
   withheld.** The generic consequence applies as well and is not an alternative to
   it: the run is provisional and says so at the same prominence every time. The
   degradation notice prints in the artifact every run until it is bound. **Read
   both consequences from those two places and do not restate either here or
   anywhere else**, because a specific consequence written twice is how one binding
   state produced two different artifacts.
3. Where the claim rests on rung 5, the uncontrolled-movement warning is attached
   to the claim itself and not only to the audit: growth against your own trend
   controls for nothing external, and this is the claim the ground-moved failure
   punishes.

**WHERE THE GROUND IS NAMED, HOW MANY TIMES, AND WHAT A CLAIM CARRIES WHEN THE FULL
NAME IS SOMEWHERE ELSE.** This is settled here, once, because the requirement above
and the field budget in 1.5 cannot both be met by naming the ground in full inside
every field. A real bound ground is a clause rather than a word: "carrier rate
increases filed by three named carriers, effective through the period" is the kind of
answer an organization's own published objectives actually give, and at that length
it is around a quarter of an objective field's whole budget, spent once per field, on
one disclosure, before a single figure is stated. **The remedy is NOT to cut the
disclosure and it is NOT to let a claim travel without one.** It is to say where the
full name lives and what a claim carries instead.

- **THE FULL BOUND VALUE OF MOVING_GROUND_NAME IS NAMED IN FULL IN EXACTLY TWO
  PLACES, BOTH MANDATORY, NEITHER INSIDE A FIELD BLOCK.** First, in the GROUND
  STATEMENT that sits immediately above the FIRST field block of the copy region,
  beside the selection sentence D2 requires there, in the panel label styling and
  never as a copyable block: it says what the ground is, what is known about its
  movement this period, and that every figure below was measured against it. It is
  the last thing a reader passes before the first thing they paste. Second, in METHOD
  below the boundary, with MOVING_GROUND_SOURCE, the figure or the words saying the
  movement was not measured, and the date the source was read.
- **EVERY CLAIM CARRYING A NUMBER STILL NAMES THE GROUND, IN ITS SHORT FORM, AND
  STILL CARRIES THE MOVEMENT STATEMENT.** A field that travels into the destination
  system without its ground is exactly what G19 exists to prevent, and it stays
  impossible: the box a person pastes says what moved underneath the number, in the
  same words every time.
- **THE SHORT FORM IS DERIVED ONCE PER RUN AND IS USED IDENTICALLY IN EVERY FIELD.**
  It is the bound name with its qualifying list removed and nothing else changed, and
  it must still say TWO things: what moved, and that it was not set by the writer.
  Where the bound name carries no removable qualifier, the short form IS the full
  name and nothing is saved. **It is never paraphrased per field**, because six
  paraphrases of one ground read as six grounds, and it is printed beside the full
  form in the GROUND STATEMENT and in METHOD so a reader can match them without
  guessing.
- **DROPPING A THIRD PARTY'S NAME FROM THE SHORT FORM IS NOT A NEVER_CUT_LIST
  VIOLATION, AND THIS IS STATED BECAUSE A RUN READ IT AS ONE.** NEVER_CUT_LIST
  protects the name of an entity the writer is CLAIMING CREDIT FOR. The ground is by
  construction the opposite: it is what moved underneath the writer, and the writer
  claims no credit for it. The named entities behind a ground therefore live in the
  GROUND STATEMENT and in METHOD, where they are checkable, and their absence from a
  short form inside a capped box cuts nothing the list protects.
- **THE GROUND STATEMENT AND THE MOVEMENT WORDS ARE NOT CUT BY COMPRESSION_ORDER.**
  The in-field short form and the movement statement are not filler, not restatement,
  not a lineage line, not a rationale and not a scope qualifier repeated across
  measures, so no step of that order reaches them. Where a field will not fit WITH
  them, the field is over and OVER_LIMIT_REMEDY applies: split the objective or move
  a measure out. **A field is never made to fit by dropping its ground.**

Gate G19 in Part 7 tests this.

## 2.4 The two comparative quantities, and never interchange them

Two POINT-BASED comparative quantities exist and they are NOT the same. Confusing
them produces overclaims of several multiples.

    RATE DELTA          rate_delta = entity growth minus benchmark growth
                        UNIT: percentage points of growth
                        MEANING: how much faster or slower the entity moved than
                        the benchmark it was measured against.

    PROPORTION DELTA    proportion_delta = end share minus start share
                        where share = entity value divided by benchmark value
                        UNIT: share points
                        MEANING: how much of the benchmark population the entity
                        captured or lost.

**EVERY EMITTED CLAIM MUST NAME ITS UNIT.** Write "grew share of the addressable
set by 1.55 share points" and "outperformed the benchmark by 6.4 percentage points
of growth". **Never write a bare word points.**

A reviewer who reads share points as growth points sees a claim several times
larger than the truth. See SD-CLM-06. The never-interchange rule and the mandatory
unit naming survive any rebinding verbatim and are the single most valuable pair in
this file to preserve exactly.

Enforced by gate G13, which fails on a bare "points".

Raw entity growth percentages and raw execution counts remain reportable in their
own right, provided each carries the counterfactual denominator that gate G1
requires.

Which of the two quantities is computable is decided by the rung, per the rung table
in SD-CLM-33. A quantity that is UNDEFINED at the rung in force is not emitted, is
not approximated by the other, and is named as unavailable in the audit.

### 2.4.1 The LEVEL DELTA, which compares two rates and is not one of the two above

**The pair above compares MOVEMENT. The commonest comparison in a service business
compares LEVELS: one rate against another rate, at a point in time.** A retention
rate of 90.9 percent against a peer median of 87.65 percent; a completion rate of
70.5 against 71.6; a confirmation rate of 53.6 against 75.0. **None of those is a
rate delta and none is a proportion delta**, because neither side of any of them is
a growth rate and neither is a share of the other. Under the pair alone the
classifier has no unit to band, so no label can be emitted for the three figures a
manager is most likely to ask about, while the movement of the same measure, which
nobody asked about, gets one.

    LEVEL DELTA         level_delta = entity level minus comparator level
                        UNIT: percentage points of the measure's own rate
                        MEANING: how far above or below the comparator the entity
                        SITS, at the point both were measured. Not how fast either
                        one moved.

**IT IS A THIRD QUANTITY AND IT IS NEVER SUBSTITUTED FOR EITHER OF THE OTHER TWO.**
SD-CLM-06 governs the two that compare movement and its never-interchange rule is
untouched: a level delta is not a rate delta, is not a proportion delta, is not
converted into either, and is not printed in either one's unit. **The unit is named
in full, as percentage points of the named measure**, and it says WHICH measure:
"3.25 percentage points of retention above the peer median", never "3.25 points" and
never "3.25 percentage points of growth". G13 fails a bare "points" here exactly as
it does everywhere else.

**IT IS ONLY DEFINED WHERE BOTH SIDES ARE THE SAME KIND OF RATE**, over the same
population definition, the same denominator and the same window, per Stage 4 item 4
and gate G14. Two rates that are not commensurable do not produce a level delta;
they produce two figures, each printed with its own basis.

**IT IS BOUND, NOT ESTABLISHED HERE.** SD-CLM-34 names the level delta as the fourth
unit and states that a level delta and a movement delta are NEVER banded against each
other's band; DEADBAND carries the band itself, PER RUNG AND PER QUANTITY FORM, with a
MOVEMENT band and a LEVEL DELTA band on each of rungs 3 and 5. **This subsection
defines the quantity and its unit; the band that classifies it is 2.5's and the
binding's.**

**A LEVEL DELTA AND A MOVEMENT DELTA ARE TWO FACTS, NOT ONE, AND ARE NEVER EMITTED AS
THOUGH THEY WERE.** A rate that is FLAT in movement and BELOW the comparator level is
both of those things at once, and each is labelled against its own band or not at all.
Neither is presented as confirming the other, neither is dropped because the other was
printed, and neither is banded against the other's band. SD-CLM-34.

**IT ATTACHES TO A RUNG, IT DOES NOT CREATE ONE.** A level comparison against a peer
median is a rung-3 comparison and carries rung 3's peer count, its tie count and its
anonymity constraints, including SD-SPN-16 where the peer set is below either of the
two peer floors. A
level comparison against a plan level is a rung-4 comparison and is the LEVEL row of
2.2.4. A level comparison against a control group's level is rung 2. **The rung
decides the claim strength and the disclosure; this quantity decides only what is
subtracted from what and in which unit the answer is printed.**

**WHERE THE COMPARATOR IS A MEDIAN, IT CARRIES ITS COUNT.** Below
MIN_POPULATION_FOR_NORM the median prints with its count and no comparison is drawn
from it, per SD-POP-19 and Stage 4 item 7, and that rule is not relaxed because the
quantity changed. **A LEVEL DELTA AGAINST SUCH A MEDIAN IS A COMPARISON DRAWN FROM
IT**, so it is not computed and not printed, with or without a label, and the
withholding is stated beside the figure per 2.5. **The reason the walk in Test 3 stops
at a level meeting BOTH peer floors is precisely so that this band, once computed, can
actually fire**: a walk stopping one short of the norm floor produces a set this
quantity is defined on and forbidden to speak about.

## 2.5 WIN / MISS / FLAT

**Do not classify by direction table. Classify by formula**, which covers every
case including entity up with benchmark down, entity down with benchmark up, a flat
benchmark, and exact zeros.

    band = DEADBAND[the rung in force], read in that band's own named unit

    label = WIN       if rate_delta is greater than plus band
    label = MISS      if rate_delta is less than minus band
    label = FLAT      if the absolute value of rate_delta is at or under band
    label = UNPAIRED  if the benchmark denominator is zero, negative or absent

**The band is looked up by rung on every comparison. There is no single band and no
band is borrowed from a neighbouring rung**, because the quantity on the left of
each test is in the unit of the rung that produced it.

An UNPAIRED entity routes to execution claiming with a denominator population, at
rung 6. **UNPAIRED is reached only where no comparative quantity is defined at the
rung in force. A missing benchmark POPULATION is not by itself UNPAIRED**: a peer
set, a control group or a plan each supply a comparative quantity without one. See
SD-CLM-33 and SD-CTR-24.

**DEADBAND IS A MAPPING PER RUNG AND PER QUANTITY FORM, NEVER ONE SCALAR, AND EVERY
BAND NAMES ITS OWN UNIT.** The unit of the delta differs by rung: percentage points of
share at rung 1, percentage points of the treated-minus-control gap at rung 2,
percentage points of growth at rungs 3 and 5, percent of target at rung 4, and nothing
at all at rung 6, which carries no delta to band. **And on the two rungs that are
asked two different questions, rungs 3 and 5, the band is keyed by the FORM of the
quantity as well as by the rung**: a MOVEMENT band, and a required LEVEL DELTA band in
percentage points of the measure's own rate, per 2.4.1 and SD-CLM-34. **One scalar
cannot be in percentage points of growth and in percent of target at once, so a bare
scalar is REJECTED AT VALIDATION** rather than read in whichever unit the reader
assumes, and one band under a rung cannot serve both a movement and a level. A band
read in the wrong unit, or in the right unit and the wrong form, either labels noise
as a result or silences a real one. The bands, their units and their defaults are the
DEADBAND rows in reference/schema/ SECTION A1 and A2; this file does not restate them.
See SD-CLM-07 and SD-CLM-34.

Each band is bound and is calibrated to the volatility of that rung's own ground.
It is NOT copied from another business and NOT copied between rungs.

**THE BAND FOR A LEVEL DELTA, WHICH IS THE FOURTH UNIT AND IS ALWAYS DATA-DERIVED.**
The mapping above names a band in share points, in points of growth and in percent
of target. A LEVEL DELTA per 2.4.1 is in none of those, so without this paragraph no
band exists for it, no label may be emitted, and the classifier is silent on exactly
the comparisons a reader most wants labelled. The rule:

- **THE BAND IS READ FROM DEADBAND, WHICH IS KEYED PER RUNG AND PER QUANTITY FORM.**
  Rungs 3 and 5 each carry TWO bands, a MOVEMENT band and a required LEVEL DELTA band,
  and the run reads the one matching the form of the quantity it just computed. **A
  rung entry carrying only a movement band is incomplete rather than a licence to
  reuse it**, per SD-CLM-34 and the DEADBAND row: the spread of LEVELS across a
  comparator set is a different quantity from the spread of their MOVEMENTS and is
  routinely several times wider, so borrowing the movement band labels ordinary
  variation as a result. The bands, their units and their defaults are the DEADBAND
  rows in reference/schema/ SECTION A1 and A2; this file does not restate them.
- **The unit is PERCENTAGE POINTS OF THE MEASURE'S OWN RATE**, and the band names the
  measure: a retention band is in points of retention and is not the band for a
  completion rate.
- **WHERE THE BAND IS UNBOUND IT IS DERIVED, AND THIS IS THE DERIVATION THIS SKILL
  PERFORMS**, which is the part SD-CLM-34 leaves to the skill that computes it: the
  lower decile of the ABSOLUTE PAIRWISE DIFFERENCES BETWEEN THE COMPARATOR SET'S OWN
  LEVELS at rung 3, and the lower decile of the absolute differences between the
  unit's OWN SUCCESSIVE PERIOD LEVELS at rung 5. A bound value is never overridden by
  one derived at run time, per standing rule S9 and SD-CTR-24.
- **MIN_POPULATION_FOR_NORM GUARDS BOTH BANDS ON BOTH RUNGS, AND THE TWO WITHHOLDINGS
  IT SITS BESIDE ARE NOT THE SAME WITHHOLDING.** In all four cases below no WIN, MISS
  or FLAT label is emitted for that form on that rung; **what differs is whether the
  DELTA ITSELF may ship**, and this file used to give one answer where SD-POP-19 gave
  another, which is two artifacts off one configuration and one data set.
  **SD-POP-19 GOVERNS AND IS CITED RATHER THAN RESTATED DIFFERENTLY HERE.**
  - **The comparator set is below MIN_POPULATION_FOR_NORM, or below ANONYMITY_FLOOR
    per SD-SPN-16, or was built by the writer per SD-CLM-30.** The comparator itself
    may not be published as a benchmark, so **NO DELTA AGAINST IT SHIPS: not a
    labelled one and not an unlabelled raw one either, and the arithmetic between the
    two figures is not performed.** A delta against a fragile median is the fragile
    number wearing a minus sign, and stripping the label off it removes the wording
    while leaving the claim. The entity's own figure ships, the comparator's count
    ships beside it, and **the artifact states in one line beside the figure that the
    comparison was withheld, which variable withheld it and what the count was**,
    because a silence reads as "no difference". Per SD-POP-19 and Stage 4 item 7.
  - **The comparator set MEETS both floors and the SPREAD alone cannot be computed.**
    The comparator may be published, so the raw delta ships with its unit, its
    comparator named and the count behind the comparator, and the artifact says the
    LABEL was withheld because no band could be computed. This is the only case in
    which an unlabelled delta ships, and it is a statement about the band rather than
    about the comparator.

**Three of the bands behave differently when unbound, and the difference is the whole
point.**

- **The rung 3 MOVEMENT band is DATA-DERIVED.** Where it is unbound it is computed
  from the data as the lower decile of absolute period-over-period movement across
  peers. Where even that cannot be computed, **no WIN or MISS label is emitted for
  that form on that rung**, and the raw delta with its named unit is printed ONLY
  where the comparator itself may be published, per SD-POP-19 and the two cases
  above. A reader who has no peer set at all has no comparator to publish and no delta
  to print: that reader is in Test 2's state, rung 3 is dropped and the drop is named.
- **The rung 3 and rung 5 LEVEL DELTA bands are DATA-DERIVED in the same way**, from
  the spread of LEVELS rather than of movements, per the paragraph above. They are
  separate entries under their own rungs and neither is ever read as the other.
- **The rung 4 band is FIXED IN PERCENT OF TARGET and needs no peer spread, so it is
  ALWAYS COMPUTABLE.** Plan attainment therefore carries a labelled figure for a
  reader with no peers at all, including a reader at the top of the chain whose
  rung 3 was dropped per Stage 4 item 7. **A missing peer set must never silence the
  classifier on a plan-attainment figure**: attainment short of target is short of
  target whether or not anybody else was measured, and the silence that used to
  follow from a peer-derived band was the wrong silence in the one place the reader
  is most senior.

**THE RUNG-5 LEVEL-DELTA BAND IS UNCOMPUTABLE ON AN ANNUAL RUN BY CONSTRUCTION, AND
THAT IS DISCLOSED AS A STRUCTURAL SILENCE RATHER THAN PRINTED AS AN ORDINARY ONE.**
The band is derived from the spread of the unit's OWN SUCCESSIVE PERIOD LEVELS and it
needs at least MIN_POPULATION_FOR_NORM of them. **A year-end review compares one year
against the prior one and therefore has ONE prior period, for every annual reviewer at
every organization, whatever their data is like.** So on an annual run the rung-5
route to a level-delta label is shut before any file is read. Where the peer walk in
Stage 4 item 7 also exhausts the chain, the rung-3 route is shut as well, and **both
routes to a labelled level delta are closed at once**, which is the ordinary state of a
small organization's annual reviewer rather than an exotic one.

**WHAT THE RUN DOES ABOUT IT, BECAUSE THE SILENCE ITSELF IS NOT NEGOTIABLE HERE.** The
raw level delta still ships with its unit named in full, per 2.4.1 and the second case
above, wherever the comparator itself may be published. **The withholding of the LABEL
is stated beside the figure and says WHICH of the two routes was shut and WHY**, and on
an annual run it says that the rung-5 band could not be derived because the run has one
prior period rather than because this person's data is thin. **A reader must be able to
tell a band that could not be computed from a comparison that came out FLAT**, and on
this run the difference is the whole of it. Where BOTH routes are shut, both are named,
in one line each, rather than one standing in for the other.

**THIS IS A DISCLOSURE AND NOT A REPAIR, AND THE REPAIR IS NOT THIS FILE'S TO MAKE.**
The band is DEADBAND's, its floor is MIN_POPULATION_FOR_NORM's, and both are bound in
reference/schema/. **A run NEVER lowers either to obtain a label**, and it never
borrows the movement band for a level delta, which SD-CLM-34 forbids and which would
label ordinary variation as a result. The rung-4 precedent, a FIXED band in the
measure's own unit that needs no spread and is therefore always computable, is what a
rung-5 level-delta band would have to look like to reach an annual reviewer at all;
until it exists, the silence is disclosed in the terms above and is never quietly
filled.

**Benchmark growth is never itself a label.** An entity that grew 27 percent while
its benchmark grew 32 percent is a MISS at minus 5.0 percentage points of growth,
regardless of how large 27 percent looks. This is the environment-credit trap, the
most seductive error in this kind of data. It reads as a triumph and it is a miss.
Regression case 1 tests it.

At rung 4 the classifier runs on attainment rather than on a rate delta, per the
rung table in SD-CLM-33, against the fixed percent-of-target band above, and the
FLAT state is named ON PLAN. At rung 6 the classifier does not fire at all.
**The classifier never disappears because a
business has no market. It changes what it is measured against, and it keeps its
warning.**

**And where the POPULATION is cold, the classifier does not fire at any rung.**
SD-CLM-31. That is an independent block, not the floor rung turning the classifier
off, and the state emitted is NO BASELINE, which a reader can tell apart from
UNPAIRED and from FLAT. Plan attainment is exempt and keeps its three states. See
2.2.3.

## 2.6 The Marriage Model

Every claim carries four parts, in CLAIM_PART_ORDER, which is: action, result,
proof, consequence.

    ACTION       What the person did. Inferred from evidence in Stage 7 and
                 confirmed by the person in a question round.
    RESULT       The claimable number, with its unit named per 2.4.
    PROOF        The counterfactual denominator from 2.2, or a peer rank with its
                 tie count. PROOF_ACCEPTED_FORMS is the bound list and must
                 include the counterfactual denominator.
    CONSEQUENCE  The named organizational mechanism the result advances, resolved
                 through the lineage ladder in 2.7.

**The ACTION half is what people omit. It is inferable, and it is the reason this
method exists.** See SD-CLM-08.

An unmarried claim is a result with no action, no proof and no consequence: a
quantity, a scope code and a period, and nothing that tells a reader what to do
with it. That is the orphaned fact the mission names.

A married claim, neutral illustration, at the direct tier: "Rebuilt the standing
order pattern at the twelve accounts flagged for stockouts, which lifted fill rate
9.4 percentage points of growth against the untreated accounts in the same
district, the strongest of the eleven books in that district with no ties, which
advances the on-shelf availability initiative."

**Read the proof clause of that example against Stage 4 item 7 before copying its
shape.** The rank is drawn across the sibling books at the writer's OWN altitude
inside the next coarser level, which is the only peer set a direct-tier writer has.
A rank across the districts themselves would be a claim at a level above the
writer, and the same sentence would then fail gate G3 and gate G22 while looking
identical to a reader.

## 2.7 The Lineage Ladder

**Resolve every claim as high as the evidence defends, and cite the highest level
reached.** See SD-CLM-09.

LINEAGE_LADDER is a bound taxonomy of between three and seven rungs, highest
altitude first. The depth is configuration and is never fixed at a number by this
file. Rung 1 is enterprise strategy; the last rung is the individual's own
objective. A generic five-rung instance, offered as a shape and not as a value:

| Rung | Generic content | Bound from |
|---|---|---|
| L1 | The enterprise goal or current initiative. | ENTERPRISE_STRATEGY_PILLARS, ENTERPRISE_LONG_TERM_GOALS |
| L2 | The compensated or scorecard metric, always named with its weight. | METRIC_SET, INCENTIVE_PLAN_NAME |
| L3 | The intermediate organizational unit's objective. | The scope level above the person |
| L4 | The direct supervisor's dated, stated priority. | PRIORITY_SOURCES, the live sweep |
| L5 | The person's own objective. | The goal ledger |

**Ranking function: altitude reached, then peer rank, then magnitude. A top-rung
claim leads. A bottom-rung claim is a footnote. Never lead with a footnote.**

### The altitude ceiling, and why enforcement is lexical

**A claim may ladder no higher than the level at which the person can credibly
influence the outcome. Citing above the ceiling reads as inflation.** The ceiling
per role is ROLE_LADDER.altitude_ceiling. See SD-CLM-10.

**ENFORCEMENT IS LEXICAL, NOT JUDGMENT.** When a claim cites a level ABOVE the
role's own scope, the consequence clause MUST use a verb from CONTRIBUTION_VERBS
and MUST NOT use a verb from OWNERSHIP_VERBS. The two lists are disjoint by
validation. Contributing to a goal is legitimate for a front-line person;
delivering it is not. Gate G3 tests the verb lists, which makes the ceiling
mechanically checkable rather than a matter of taste.

The standing lists, which port verbatim across businesses:

    CONTRIBUTION_VERBS   advances, supports, contributes to
    OWNERSHIP_VERBS      achieved, delivered, drove, led, owned

## 2.8 Span of Control: what each role may claim

This decides WHAT COUNTS AS A WIN, and it is the difference between a credible
write-up and one a reviewer dismisses in a sentence.

**Getting it wrong in either direction is fatal: a front-line person who hides
behind aggregates looks passive, and a leader who claims a single unit looks like
they do not understand their own job.** See SD-SPN-09.

This is also the doctrine that makes one skill serve a frontline worker and a chief
executive without a second version, and it is an honesty mechanism as much as a
sizing mechanism. Span of control decides not only how much output a person gets;
it decides **which claims a person is permitted to make**. It is what stops someone
taking credit for an outcome above their own altitude.

### The two claim tiers

ROLE_LADDER.claim_tier carries one of two values for every role.

**DIRECT tier.** The person personally changed the unit. They called on it, fixed
it, wrote it, reviewed it, resolved it, installed it. A unit-level result IS their
direct action. Attribute unit wins to them by default and name the units.

**AGGREGATE tier.** A unit-level result is NOT their action. Someone on their team
did that work. They may NEVER write a sentence of the form "unit 123456, which I
fixed this year". That sentence tells the reader they do not understand their own
role. They win on aggregates: the whole scope, a whole grouping, a whole entity
across their scope. They may claim team and system outcomes: coverage across the
scope, adoption of a programme, breadth across a grouping, capability built, a
practice they installed that the team then ran.

**The illustration rule.** At the aggregate tier a named unit may appear ONLY as an
illustration inside an aggregate claim, and the credit stays with the team.
Neutral form: "including a rebuild at our highest-volume site that the regional
team executed". Governed by ILLUSTRATION_RULE_ENABLED. See SD-SPN-10.

**Mixed scope.** A person who holds both a direct book and aggregate
responsibilities claims unit-level wins in the book and aggregate wins in the rest.
**Never blend the two in one sentence.** PERSON_SECONDARY_SCOPES carries the split.
See SD-SPN-11.

The general binding underneath both tiers is a pair: the ATOM, the smallest unit a
person can personally change; and the AGGREGATE, the population a leader is
accountable for the shape of. The atom is a store in one business and is a ticket,
an account, a case, a shift, a machine, a line item, a patient, a claim or a code
change in another. POPULATION_SHAPE binds it, and it binds it PER DECLARED
POPULATION rather than per company, per SD-POP-23 and Part 13.

**Under FLOW the atom is the EPISODE, not the identifier.** Where
POPULATION_SHAPE.reopen_allowed is true, two passes of the same identifier through
the pipeline are two distinct atoms, and a claim that merges them is a claim about
a result that never happened as described. See Part 13 divergence 2.

**The atom must sit at or below the reader's own scope.** SD-POP-26. Where it sits
COARSER than the reader's own level, the reader owns a PART of an atom and cannot be
given a ranked list of atoms at all. That is a binding error, it is detected rather
than assumed, and it is reported as one. See 4.5.

**Below MIN_POPULATION_FOR_RANKING atoms in the reader's scope, no cut in this
section is ranked and no comparative language is used.** SD-POP-25. The cuts still
run and the content still ships; what is suppressed is the ordering language, and
every suppression is named. See 4.5.

### The self-determined subset, the highest-evidence cut

**The subset of the population whose outcome was determined locally, rather than by
a decision taken above the writer, is the strongest available evidence of
individual skill, because it isolates skill from inherited advantage. Surface it
first and say so explicitly.** See SD-SPN-12.

It is resolved as the COMPLEMENT of a populated grouping field, never by searching
for a word. See reference/field-resolution.md Part 3.12 and SD-QUA-04.

Compare it three ways: against the same person's own managed units; against the
same subset elsewhere at the peer level; and against the scope total. **Beating any
of the three is a top-tier win** and ranks above an equivalent total-measure win.

Any business that can distinguish self-determined outcomes from centrally
determined ones can compute this cut. Neutral worked cases: an inbound lead against
a self-sourced one; an unmandated renewal against a corporate contract; a
discretionary purchase against a required one; a site whose layout the local
manager sets against a site whose layout is set centrally.

### Influence inside a managed group is still a legitimate claim

A direct-tier person influences a centrally managed grouping inside their own scope
through the local decision maker, even where the terms are set above them. A claim
about that grouping inside their own scope is legitimate and strong. Neutral form:
"the national account's sites in my district grew 52 percent". See SD-SPN-13.

### What the tier does to the output size

DELIVERABLE_LINES carries exactly two shapes, differing only in three numbers, and
SENIOR_TIER_PREDICATE decides which shape a role receives. **The action list gets
SHORTER RELATIVE TO SPAN as scope widens.** A more senior person has less time,
not more, so the list is never proportional to span: it grows far more slowly
than the span it covers, and as a SHARE of what the reader owns it shrinks
sharply. The reference depth stays constant.

**THE SENIOR PAIR IS THE LARGER PAIR IN ROWS, AND THAT IS THE DESIGN.** Ten items
over a hundred units is a tenth of a span; twenty over several thousand is a
fraction of one percent, and the second is the shorter list in the only sense
that matters to the reader holding it. Any reading of SD-RNK-09 that hands a
senior leader fewer rows than a frontline reader off the same file is a
misreading. See SD-RNK-09 and SD-CTR-02.

Enforced by gate G16.

## 2.9 The Source Hierarchy

Authority is a map from QUESTION to the one artifact that settles it. It is never a
ranking of documents. SOURCE_AUTHORITY_MAP binds all seven questions:

| Question | Bound to |
|---|---|
| Who defines the deliverable form | FORM_SPEC_SOURCE |
| Who defines the goal methodology | GOAL_FRAMEWORK_NAME and its source |
| Who defines the quality bar | RATING_SCALE and RATING_AXES, current version |
| Who defines strategy | ENTERPRISE_STRATEGY_PILLARS, ENTERPRISE_LONG_TERM_GOALS |
| Who defines priority ranking | METRIC_SET weights, per INCENTIVE_PLAN_NAME |
| Who defines local targets | The supervisor chain, per PRIORITY_SOURCES |
| What counts as evidence | EVIDENCE_SOURCES |

See SD-PRI-32.

**Priority ranking comes from the organization's own published weights, not from
the writer's opinion about which of their wins is biggest.** See SD-PRI-31.

**USER DOCUMENTS ARE READ FOR EVIDENCE ONLY. Never for format, phrasing or
structure.** Prior self-written documents are the input problem this skill exists
to fix. Never inherit their shape. In particular, a heading that appears in a
person's own prior write-up and has no counterpart on the live form must not be
reproduced; BANNED_HEADINGS holds the ones already known, and the list is extended
whenever a prior document introduces another. See SD-PRI-33 and SD-CTR-22.

**All sources, every run, with the nearest one first.** The person's own supervisor
is read first and outranks the rest; a central or published source is the
cross-check and the fallback, never the starting point. See SD-PRI-01.

## 2.10 Confidence gating, the anti-slop rule

Every inference this skill makes carries a confidence. **Confidence decides whether
the agent PROPOSES or ASKS.** This is separate from whether a form field is
required, and it is the mechanism that keeps invented-sounding content out of a
permanent record. See SD-CNF-01.

    HIGH    evidence is unambiguous and points one way
            propose it, and ask for a light confirm
    MEDIUM  evidence supports it but a competing reading exists
            present both readings and ask which is right
    LOW     evidence is thin, conflicting or absent
            do NOT propose prose. Ask an open question instead.

**WHAT THIS APPLIES TO:** inferred actions, synthesized learnings, reconstructed
objectives, entity-to-benchmark pairings, anomaly explanations, and any claim about
causation.

**THE RULE: LOW CONFIDENCE NEVER BECOMES A SENTENCE. It becomes a question.** An
agent that writes a confident sentence from thin evidence produces exactly the
plausible-sounding filler that makes a reviewer distrust the whole document.

The calibration, worked from one shape of evidence, in neutral terms. A measure
moved at 23 units in the person's scope:

    HIGH    21 of the 23 carry the same activity marker and a logged interaction.
            One clear reading.
            Proposal: "You closed the coverage gap at 21 units. Confirm or edit."

    MEDIUM  12 carry one activity marker, 11 carry a different one, and both
            programmes ran in the period.
            Question: "Was this the first kind of work, the second, or both?
            Which drove it?"

    LOW     No activity marker correlates above chance.
            Question: "The measure moved at 23 units and I cannot tell from the
            data what drove it. What did you do there?"

**ASK PLAINLY WHEN UNSURE.** "Did you actually do this?" is a better question than
a confident wrong sentence. Users correct a draft far more readily than they catch
a fabrication that reads well. See SD-CNF-02.

**CONFIDENCE IS RECORDED, not just used.** Every candidate carries its confidence
into the checkpoint and into the verification list, so a MEDIUM inference the user
confirmed is distinguishable later from a HIGH one that never needed confirming.
See SD-CNF-03.

**Correlation is weak evidence for causation.** Always present diagnoses as
candidates, never as proven cause: here is what stands out, does this ring true?
See SD-CNF-05.

Routing: HIGH and MEDIUM route to the composite action question. LOW routes to the
open cause question, which is never accompanied by a guess.

## 2.11 The Proposal State Machine

Three states, and the asymmetry between them is the whole point.

    PROPOSED   Set by Stage 7 on every inferred action and synthesized learning.
    CONFIRMED  Set by the confirmation round when the person confirms it.
    REMOVED    Set by the confirmation round when the person rejects it, AND set
               by default when the question was skipped or never fired.

**REMOVED CARRIES ITS REASON, and the reason is recorded on the proposal:**

    REJECTED    the person saw it and said no.
    UNANSWERED  the question was skipped, never fired, or could not be asked
                because no channel existed to ask it.

**The reason changes exactly one thing and changes nothing else: whether the
proposal may be OFFERED below the submission boundary.** Both reasons strip the
proposal from the copy region identically, and neither is ever treated as
confirmation. See 2.20.

- **Drafting accepts all three states.** Confirmation is a postcondition of the
  confirmation stage, never a precondition of the drafting stage. Blocking drafting
  on confirmation deadlocks the run.
- **The confirmation round resolves every proposal to CONFIRMED or REMOVED.**
- **A proposal whose question was skipped or never fired is REMOVED, not carried
  forward.**
- **Re-assembly strips every REMOVED proposal FROM THE COPY REGION**, deleting the
  sentence or clause it produced. A removed action clause leaves the result standing
  on its own without an action half. It does not leave an unconfirmed action in the
  text.
- **Silence defaults to REMOVED, not to CONFIRMED.**
- **A proposal REMOVED as UNANSWERED may be offered below the submission boundary**,
  once, as a clearly labelled proposal attached to the question that would confirm
  it, per 2.20. A proposal REMOVED as REJECTED is deleted from the artifact
  entirely, above the boundary and below it, because the person has already
  answered.

**Inference is this method's core value and its core risk: a first-person claim
about what the person did, never confirmed by them, is the single worst thing this
method can produce.** See SD-CNF-04. Enforced by gate G15, **which is scoped to the
copy region, because that is where the harm is**: an unconfirmed sentence that
cannot travel into the destination system and is labelled as an unanswered proposal
is a question with its content attached, which is the cheapest thing this method
can hand a person. Regression cases 4 and 5 test it.

## 2.12 Never invent an action, and never infer a target

**Never invent an action.** Where no evidence correlates to an outcome, emit the
result without an action clause and route it to an open question. Retry once with a
widened evidence set, then proceed without the clause. See SD-CNF-06.

**Never infer a target to manufacture a completion percentage.** A measure with no
stated target cannot produce a completion percentage. Mark it UNGRADABLE, ask, and
route the phrasing for rewrite. NEVER invent a retrospective target to manufacture
completion math on an objective that never carried one. Choosing "no target was set
for this" is honest and acceptable, and it routes the measure to grading for a
rewrite that will be gradable next period. See SD-CLM-21.

**Attainment above 100 percent is legitimate and is stated as achieved-over-target,
never clipped.** COMPLETION_ABOVE_100_ALLOWED must be true. An attainment of 103.4
percent against a target is one of the strongest claims a person can make and must
survive to the output intact.

**Never fabricate.** Never invent a unit, a number, a date, a target, a learning, a
rating or a quote. Quote priorities verbatim with sender and date. Never emit a
rank, score or benchmark you could not compute: leave it blank with a stated
reason. **A visibly missing number is recoverable; a fabricated one is not.** An
unconfirmed inferred action is fabrication even when the underlying number is real.
See SD-CNF-07 and SD-CNF-08.

**An illustrative number in a template is never a value.** Every figure, population
and date in a rewrite the person accepts must trace to the ledger, to an answer, or
to the data. Anything unsourced is emitted as a bracketed placeholder naming its
source, **and the placeholder's home is below the submission boundary and never
inside a field block**, per gate G2, 8.3 D5 and reference/output-contract.md PART 3.4: the
claim ships in the copy region without the number, the number goes below the boundary
with its source and the question that would settle it, and the two are linked by the
field's own heading. A rewrite seeded with an invented target becomes the standard the
person is graded against next period. See SD-CLM-24.

### 2.12.1 A CLAIM IN THE PERSON'S OWN NOTE THAT A RESOLVED CELL CONTRADICTS

**SD-CNF-10 GOVERNS THIS AND IS EXECUTED HERE. IT IS A THIRD STATE AND IT IS NEITHER
OF THE TWO THIS SKILL ALREADY HAD.** 2.12 above and gate G2 answer a figure that
traces to NO cell: it is UNSOURCED, the claim ships above the boundary without the
number and the number goes below it as a bracketed placeholder. 3.4 and SD-RUN-09
answer TWO OF THIS METHOD'S OWN DERIVATIONS disagreeing with each other. **Neither
reaches a figure, a name or an event that the person stated and that a RESOLVED COLUMN
SAYS SOMETHING ELSE ABOUT**, and until this subsection existed there was no named rule
for it, so a run reached for the nearest analogy and decided by itself.

**THE TWO OBVIOUS READINGS ARE OPPOSITE AND BOTH ARE DEFENSIBLE, WHICH IS EXACTLY WHY
A RUN MUST NOT CHOOSE BETWEEN THEM.** Publish the person's words, and the review
fabricates the moment anybody checks the data, which 2.12 and SD-CNF-07 forbid. Delete
them, and on a run with no mail and no chat the person's own note is the only evidence
of what they did, so the seam silently deletes their year, which SD-CTR-23 names as the
most expensive loss this skill can produce and which the person discovers by reading
their own record in the destination system, too late to say anything.

**NEITHER SOURCE WINS AUTOMATICALLY.** A note written months after the fact is often
wrong about a name. An extract is often stale, filtered to a different population,
keyed on a different unit, or cut at a different date. **A run that picks a winner has
decided a question of fact it cannot see, and it decides it the same way every time**,
which is worse than being wrong once, because the bias is invisible and repeated.

**THREE LABELS, THREE REMEDIES, AND THEY ARE NEVER COLLAPSED INTO EACH OTHER.** The
test is per stated item and it is mechanical:

| Label | The test | What settles it |
|---|---|---|
| CONTRADICTED | A column that RESOLVED holds, on the unit the statement names, a value the statement cannot be true of. **A unit the statement NAMES and that is ABSENT from the source entirely is CONTRADICTED**, of the identity rather than of a measure, because the source was read and the unit was not in it. | Somebody saying which source is right. |
| UNSOURCED | No resolved column addresses the statement at all. | Finding a source. G2, SD-CNF-08 and reference/output-contract.md PART 3.4 govern this one unchanged, and this subsection changes nothing about it. |
| UNVERIFIED | A column that WOULD address it did not resolve, or resolved and is empty within scope. | Resolving or populating the column. It is never reported as a contradiction. |

**COLLAPSING THEM COSTS THE PERSON THE WRONG ACTION.** Reporting a contradiction as an
absence sends them hunting for a file when what was needed was one sentence from them.
Reporting an absence as a contradiction tells them to doubt their own memory when what
was needed was a better extract.

**WHAT HAPPENS TO A CONTRADICTED ITEM, AND NOTHING IN THIS LIST IS OPTIONAL:**

1. **NOTHING CONTRADICTED TRAVELS INTO THE PERMANENT RECORD UNRESOLVED.** The item is
   excluded from every claim, every count, every denominator and every ranked figure in
   the copy region, and **the exclusion is LISTED with its reason** rather than being
   silent, per 4.4 and the exclusion discipline this skill already runs.
2. **AND IT IS NEVER DELETED.** BOTH READINGS are printed below SUBMISSION_BOUNDARY_BANNER:
   the person's statement in their own words, and what the resolved cell says with its
   COLUMN AND ITS UNIT NAMED, together with **THE QUESTION THAT WOULD SETTLE WHICH IS
   RIGHT**. The two sit under one heading so they are read as one item rather than as
   two unrelated notes.
3. **THE RUN NEVER AVERAGES THEM, NEVER BLENDS THEM INTO ONE SENTENCE AND NEVER
   PUBLISHES THE DISPUTED VALUE**, in any wording, above the boundary or below it.
4. **IT IS SURFACED TO THE PERSON, NOT RESOLVED BEHIND THEM.** It is one of the things
   the preview in Stage 11.5 flags inline, per SD-CNF-09, in the person's own language
   and as a QUESTION rather than as a correction: this is what you wrote, this is what
   the file says, which is right.
5. **ABOVE UNRESOLVED_STOP_COUNT CONTRADICTED ITEMS, STOP**, exactly as SD-RUN-09
   stops and reading the same variable. **Many contradictions at once are evidence
   about the extract rather than about the person**, and continuing past that point
   produces a document that reads as an accusation. The gate record is
   `review.contradicted_items` in 7.4.2. The count is performed once, immediately after
   the contradiction sweep in Stage 6, and it is counted separately from
   `unresolved_items`, because a run whose readers agreed perfectly and whose person
   disagreed with the book seven times is not the same run as its opposite.

**WHERE THE CONTRADICTED ITEM IS THE PERSON'S LARGEST CLAIM, NOTHING ABOUT THIS RULE
CHANGES.** That is the case the rule was written from and it is the case a run is most
tempted to resolve quietly in either direction. Enforced by gate G24.

## 2.13 Tie handling, superlatives and anonymity

**TIE HANDLING IS MANDATORY.** When the person's rank is shared, the claim must say
so. "Tied best in scope" is honest. "Led the scope" is an overclaim when six peers
matched the result. **Compute the count of peers at the same value before writing
any superlative.** A superlative a reviewer can disprove in one query destroys the
credibility of every other claim in the document. SUPERLATIVE_REQUIRES_TIE_COUNT
must be true. See SD-CLM-11. Regression case 7 tests it.

**A THIRD PARTY IS A NATURAL PERSON OTHER THAN THE WRITER. IT IS NOT AN
ORGANIZATION.** This is stated first because the rule is unreadable without it and
the two readings produce different documents. Under the narrow reading an outside
company named in the organization's own published objectives may be named in a claim
about work done against it; under the broad reading it must be stripped, and the
claim loses the one specific that made it checkable. **The narrow reading governs,
with two limits:**

- **A PERSON is never named** in a claim, a proof clause, a narrative section, an
  example, a comment or the verification list, whoever they are and however
  favourably: not a peer, not a report, not a colleague, not a customer contact, not
  a counterparty's staff. Use the ROLE.
- **AN ORGANIZATION is named freely where the organization's OWN published sources
  name it**, and where naming it is what makes the claim checkable: an outside party
  named in the employer's published objectives, in a directive the run read, or in
  the person's own supplied evidence. It is not invented, not inferred from a code,
  and not named where the run's only source for it is a guess. **NEVER_CUT_LIST
  protects the name of an entity the writer is claiming credit for**, and this is the
  reading under which that protection and this gate agree rather than contradict.
- **An organization is still subject to every other rule.** NON_CLAIMABLE_ENTITIES
  governs whether the person may claim CREDIT for its movement; this rule governs
  only whether the name may appear. The two are different questions and a name that
  may appear does not become claimable by appearing.
- **The binding owner named in the contact line is not a third party**, and neither
  is the person the review is about. The contact line is a fact about who owns the
  configuration, required by SD-CTR-19 and carried by MSG_AUTHOR_LINE, and it is
  exempt on the same ground as the identity field below: it is a property of the
  record rather than an assertion about anybody's performance. Where the artifact can
  carry the ROLE alongside or instead of the personal name, it does, because a role
  outlives a person; where MSG_AUTHOR_LINE's bound form requires the name, the name
  ships and the gate passes.

**No named third parties in a CLAIM, in narrative, in an example or in a comment,
and that is everywhere this skill AUTHORS text.** Peer comparison is anonymous and
positional. NAMED_THIRD_PARTIES_ALLOWED must be false. The rule also covers
INDIRECT identification: in a small peer set a positional claim can name someone by
elimination, and a compound identifier resolves to one person. **Below
ANONYMITY_FLOOR peers, generalize rather than rank**, and take the procedure in
SD-SPN-16, executed as Test 3 at Stage 4 item 7: walk outward to a level that meets
BOTH ANONYMITY_FLOOR and MIN_POPULATION_FOR_NORM, publish NOTHING from any level below
the anonymity floor, draw no comparison from a level below the norm floor, and say
which of the four states in that test the reader is in. **Generalizing is not a licence to publish the
comparison in vaguer words**: in a set of two, "the stronger of the two" and "above
the average" both identify the other member exactly. Behavioural examples describe
behaviour without naming the colleague or report involved, because those examples
often touch a third party's personal circumstances and travel into a record that
person cannot see. See SD-CLM-12.

**THE ONE EXEMPTION, STATED EXPLICITLY BECAUSE TWO READINGS OF THIS RULE DIVERGE ON
IT.** The schema defines the variable as whether a third party may be named IN A
CLAIM, while the gate and the degradation notice read as "anywhere", and the bound
form very often carries a supervisor, reviewer or approver field. **An IDENTITY
FIELD of the bound form is not a claim and is not authored text: it is a field the
form itself requires, and the value in it is a fact about the record rather than an
assertion about anybody's performance.** So:

- **Fill an identity field from the record**, exactly as the form requires, and name
  the person there. Suppressing it produces a form the destination system rejects,
  which is not a privacy protection.
- **Everywhere else, use the ROLE and never the name.** Not in a claim, not in a
  proof clause, not in an example, not in a comment, not in the verification list.
- **The exemption is limited to the identity section**, which is the section
  FORM_SECTIONS carries as pre-filled rather than drafted by the person. It never
  widens to a drafted section that happens to mention who somebody reports to, and
  it never licenses naming a peer, a report or a colleague anywhere.

Where no identity field exists on the bound form, nothing is exempt and no third
party is named at all.

**The peer set is defined by the period-end file**, per PEER_SET_ANCHOR_PERIOD, and
every comparison runs on the same-unit intersection used for the person's own
figures. Rosters change between periods. Ranking someone against a roster that
includes peers absent from one file produces a rank that cannot be reproduced.
**State the peer count and the unit basis alongside every rank.** See SD-CMP-06.

## 2.14 Show the benchmark, never claim it

**Every benchmark present in the data appears in the output**, either as the
comparison attached to a claim or as the denominator of a proportion, and **never
as the subject of an achievement sentence.**

**THE SUBJECT DECIDES.** If the subject of the sentence is not something the writer
is accountable for, the sentence does not belong in the body.

    ALLOWED    The entity's own result stated with its benchmark delta:
               "Grew the service line 27.4 percent against an addressable set that
               grew 32.1 percent, a shortfall of 4.7 percentage points of growth."
    ALLOWED    A benchmark figure as the denominator of a share statement.
    FORBIDDEN  A standalone sentence whose subject is the benchmark or its growth,
               however well benchmarked.

A benchmark whose metric is UNRESOLVED or UNPAIRED appears ONLY in the verification
list and never in the body, because its number is not trustworthy. Both placements
satisfy the visibility requirement. **Nothing is dropped for being unflattering.**
See SD-CLM-14 and SD-CLM-26.

**Test the entity the number describes, not the grammatical subject, and test per
number.** A sentence carrying two numbers with two different measured entities is
tested twice and fails if either fails. Action-first phrasing is house style and
must not be penalized. See SD-CLM-15. Enforced by gates G1 and G7.

## 2.15 Activity is not claimable

Four failure patterns are flagged automatically during grading, and
GOAL_FAILURE_PATTERNS holds at least these four:

| Pattern | Neutral example of the failure |
|---|---|
| no metric | "Improve visibility of the new line" |
| no deadline | "Grow coverage in the district" |
| no population | "Increase share" |
| activity rather than outcome | "Visit my top accounts monthly" |

**The last is the most common and the most damaging. Activity is not claimable.**
See SD-CLM-22.

The enforced shape is GOAL_PATTERN: **verb plus metric plus population plus
deadline.**

**Visible coaching, not silent correction.** Show the original, the rewrite, and a
one-line reason. **Never suppress an item because it failed grading**: emit it
unscored and note that it could not be graded. See SD-CLM-23.

## 2.16 Learning is synthesized from losses, and it names the mechanism

For every MISS, diagnose from the data, then propose a transferable learning that
ladders to a stated goal. **A learning is not "I need to do better". It names the
mechanism.** See SD-CLM-25.

The diagnostic method, which is the general form and ports across businesses:
**compare the person's rank across related process measures to isolate which lever
failed.** Neutral worked example: coverage complete and at the top of the
distribution, while the outcome measure falls, points away from frequency and
toward depth, breadth or the quality of each interaction. That is a mechanism a
person can act on. "Try harder" is not.

**TWO TESTS decide whether a MISS is worth diagnosing at all, and only the second
suppresses the diagnosis.** SD-EXC-14, as amended. Separate the AUTHORITY to set a
requirement or a target from the ABILITY to move the measured value.

1. **THE ENGAGEMENT TEST.** Does the person engage this unit or this measure at all?
   If not, it is not theirs: it is SHOWN, with its figure and its benchmark, and it
   is not diagnosed and not claimed.
2. **THE INFLUENCE TEST.** Can the person's own actions MOVE the measured value,
   whoever set the requirement? **If yes, it is diagnosed and it is claimable,
   however far above them the requirement was set.** A measure set by a regulator, a
   parent organization or a central function is shown rather than diagnosed ONLY
   where compliance with it is also determined above the reader, such as a contract
   term, a purchased configuration or a decision taken at a level the reader cannot
   reach.

Read as ONE test, this rule moves most of a centrally set measure set out of scope
and leaves a near-empty findings list that reads as "you are fine". The one thing
the person would act on is then suppressed by a rule written to protect them.

**Where more than half of a measure set falls to shown-rather-than-diagnosed, say so
on the front panel BEFORE the findings**, in a sentence that reads correctly at
every count per SD-LNG-13: "this write-up diagnoses 1 of 7 measures" and "this
write-up diagnoses 4 of 7 measures" both agree, and where the diagnosed count is
zero the sentence is written as its own plain statement, "no measure in this set
could be diagnosed", followed by the reason. Never print a plural noun with a count
of one beside it.

Every proposed learning is a PROPOSED inference under 2.10 and 2.11. **It must be
CONFIRMED before it can be emitted inside the copy region.** Where the confirming
question was never answered, the learning is REMOVED as UNANSWERED and may still be
offered below the submission boundary as a labelled proposal with its question
attached, per 2.20. **What is forbidden is an unconfirmed learning in the submitted
body, not an unconfirmed learning offered to the person for an answer.**

## 2.17 Work performed by a direct report is team credit

Where the evidence identifies WHO performed the work, tag it. Work performed by a
direct report is written with ATTRIBUTION_TEAM_PHRASES, never as the leader's own
first-person action. **A leader whose record claims personal execution of a
subordinate's work has an integrity problem if it is ever checked against the
logs.** See SD-CLM-13. This is the credit doctrine applied to the vertical axis
rather than to the market axis. PERSON_HAS_DIRECT_REPORTS turns the check on.

## 2.18 Reconstruct rather than halt

Where the person supplied no objectives and chooses reconstruction, the method
rebuilds them from evidence. **Most people cannot fill a blank field but can
correct a draft containing their real work. This path is the product and must not
be blocked by any data gate.** See SD-CLM-19. Regression case 2 tests it.

The mechanism is in Stage 6.5.

**Never silently backdate, and never characterize a reconstruction as
contemporaneous.** An objective derived after the fact has no true start or due
date. Emit both as explicitly reconstructed and awaiting confirmation, flag the
objective as a reconstruction, and tell the person plainly before emit. A dated
comment states the date the WORK occurred; it does not assert when the entry was
written. Where the host system timestamps entry creation, that timestamp is the
truth about authorship, and this method does not attempt to shape the impression it
gives. See SD-CLM-20.

## 2.19 Under-finding wins is the most common failure

**One total number is not a performance review.** The objective is to isolate every
defensible win the data supports across the person's whole span of control, and
then let them choose. See SD-CLM-17. The mechanism is the cut lattice in Stage 6.4.

**Present findings as a working list the person edits, not as a finding they
receive.** They may add, modify or drop. This is the cheapest possible moment to
correct the analysis. A person who drops two wins here is exercising judgment the
method does not have. **Dropped items leave the candidate list entirely and are
never carried into a closing section as consolation.** See SD-CLM-18.

## 2.20 The submission boundary

Content that must not travel into the destination system sits BELOW
SUBMISSION_BOUNDARY_BANNER, never inside a copy block. Two things always sit below
it: the forward-looking focus section, and the verification list. Neither is a
section of the bound form.

**A heading with no counterpart on the live destination form must never enter the
submitted body.** That is the same rule that bans an inherited heading from a prior
self-written document. See SD-CTR-22 and SD-CTR-23.

### What the boundary is FOR, and what it therefore permits

The boundary exists to hold content that must not travel into the destination
system. **A rule that strips such content from below the boundary as well is
enforcing the boundary against itself**, and the observed cost of that is a review
whose learning section is a placeholder while the person's own note contained two
usable learnings.

**An UNCONFIRMED proposal may appear BELOW the boundary, and only there, subject to
all five of these:**

1. **Never inside a copy block, and never under a heading the bound form carries.**
   It is not a section of the form and it is not draft text for one.
2. **Labelled as a proposal, in the label itself**, never as first-person text. The
   person did not say it and the artifact never implies they did.
3. **Attached to the question that would confirm it**, printed with it, so the
   person can answer rather than guess what is being asked.
4. **Carrying its confidence**, per 2.10, so a MEDIUM proposal is distinguishable
   from a HIGH one. **A LOW-confidence inference never became a proposal in the
   first place** and nothing here revives it: it was an open question with no guess
   attached, above the boundary and below it, and it stays one.
5. **Only where the proposal is REMOVED as UNANSWERED.** A proposal the person
   REJECTED is deleted from the artifact entirely. Offering a rejected proposal back
   to the person is worse than never offering it.

**Nothing about this relaxes the copy region.** Above the boundary, a sentence
derived from a proposal outside CONFIRMED is the failure gate G15 exists to catch,
and it is caught there unchanged.

**What the boundary looks like in the emitted artifact is settled in 8.3 D5**, and it
is not restated here: headings below the boundary are visually distinct from field
headings, nothing below it is formatted as a copyable field, and the assertion that
holds it is V5 in 7.6.

## 2.21 The expiry gate on cached references

For EVERY cached reference block, compare today against its validity date from
REFERENCE_VALIDITY_PERIODS.

    within validity   use the block. Do not crawl. Do not verify.
    past validity     the block is STALE and MAY NOT be used until refreshed.
                      Re-fetch from the source named in that block's own header
                      and use the fresh content for this run.

**Running on expired doctrine is how a write-up gets built against last year's
strategy or the prior period's weights. The gate is not advisory.** See SD-SRC-17.

If a re-fetch fails after the retry ladder, use the stale block, record that it is
past its validity date and could not be refreshed, and CONTINUE. **A stale
reference is a disclosed limitation; a halted run is a dead end.** See SD-SRC-18.

**When a block is refreshed, report the new content in the closing summary** so the
shared configuration can be updated once, rather than every user re-crawling the
same documents forever. See SD-SRC-19.

Enforced by gate G17.

---

# PART 3: RUN ARCHITECTURE

## 3.1 The capability probe runs first, every run

**Assume no tooling.** Before Stage 0, invoke reference/capability-probe.md and run the probe
in full. It is not a stage, it has no gate, and it is never skipped to save time,
because run length is not a cost this method recognizes and because a run that
discovers halfway through that it cannot write a file has already spent the budget
it needed for the fallback.

Two rules from that file govern everything here:

- **C0. Probe, never assume.** A capability is present only when a probe returned
  evidence. A capability named in the environment description but not probed is
  UNKNOWN, and unknown is treated as absent.
- **C1. A degraded run announces its degradation in the output**, not only in the
  chat, which scrolls away.

The probe record is written to SCRATCH_DIR before anything else runs, and every
later stage reads it rather than re-probing. A stage that finds a capability
behaving differently from its probed state updates the record, marks the capability
DEGRADED, and appends to the degradation list. It does not silently adapt.

**The one probe-time member of HARD_GATES** is `shared.source_unreadable`, per
7.4.1: if no source can be read at all and none was supplied inline, the run cannot
begin. Name every location attempted and ask for the file. **Everything else
degrades**, and nothing in the capability probe may add a stop condition of its own:
an absent or stale cached reference is a disclosed limitation, never a stop, per
SD-SRC-13, SD-SRC-18 and 7.4.3.

**What this skill does with the common degradations**, over and above the ladders
in reference/capability-probe.md Part 2:

| Capability absent | Effect on this skill |
|---|---|
| MAIL | No supervisor priorities are read. The lineage ladder resolves no higher than the person's own objective unless a cached organization source supplies a rung. Every claim's consequence clause drops to the highest rung actually resolved. The retrieval gate is satisfied vacuously and the artifact says so. |
| DIRECTORY | Role, scope and supervisor come from the person script instead of being confirmed. ROLE_FALLBACK_KEY applies if the person does not answer, which produces narrower claims and a shorter list, and that is the safe direction. |
| DOC_STORE | Cached reference blocks cannot be refreshed. Stale blocks are used and disclosed per 2.21. No block is silently treated as current. |
| CODE_EXECUTION | Every figure is still computed with a tool per SD-RUN-14, by whatever rung the ladder reaches. Where no arithmetic can be verified, no computed comparison is emitted and the run says which comparisons were therefore not attempted. Never compute a comparison mentally and ship it. |
| INTERACTIVE | No question can be asked, so no blocking question can be answered and the run routes to the incomplete emit path per reference/capability-probe.md 2.14 rung 2. **Which fields that empties is decided by 6.3's CLASS TEST, applied to every blocking question and not to the bank's column alone**, and a placeholder goes only into a field whose blocking input is genuinely a CONTENT input that is missing. Every CONSTRAINT question takes its documented default shape and empties nothing: the limits, the window, the scale, the preview and the win list are all constraints. The banner names which question resolves each gap, and the empty-document check in 6.3 runs before anything is emitted. No proposal reaches CONFIRMED, so no inferred action ships, and nothing is invented to fill a field nobody could be asked about. |
| MEMORY | Person-tier answers do not survive to the next run. The person script runs again, and the artifact says why. |
| DOCUMENT_WRITE | No document can be built. The run takes rung 3 of reference/capability-probe.md 2.2a and emits structured markdown carrying identical information, per 8.6. Every field block, every heading, every limit and every count survives; the styling does not. |
| DOCUMENT_INSPECT | The docx gate in 7.6 cannot read a structural attribute back, so the styling half cannot be verified and resolves per reference/capability-probe.md 2.2b. **It does not touch the counts.** A count is read from TEXT, so every block is still recounted and the over-limit check still runs and still blocks. See 7.6. |

**THIS SKILL'S CONTAINER CAPABILITIES ARE DOCUMENT_WRITE AND DOCUMENT_INSPECT**,
probed at positions 6 and 7 per reference/capability-probe.md 1.3 and 1.4. DOCUMENT_WRITE
decides whether the artifact can be built at all; DOCUMENT_INSPECT decides whether
the docx gate in 7.6 can run. They are probed separately for the same reason the
spreadsheet pair is, and an environment routinely has one without the other.

**AND THIS SKILL READS 2.2a AND 2.2b, NEVER 2.1 AND 2.2.** reference/capability-probe.md rule
P1c: a run reads the ladder that matches ITS OWN medium, because OUTPUT_MEDIUM is
keyed per skill. **A run that reads the spreadsheet pair reports the wrong capability
as blocking and degrades a deliverable that was never at risk** -- an absent
SPREADSHEET_WRITE costs this skill nothing, because this skill does not emit a
workbook. The ladder this skill takes is 2.2a, carried into 8.6.

**The announcement rule.** Every degradation appears in three places, every time:
the front panel of the artifact, before the content; the audit section, with the
probe record in full; and the first line of the reply, naming the count and the
single most consequential effect. Each line names what was unavailable, what it
changed, and what the reader should do about it. A line naming only the first of
those three is not compliant. MSG_DEGRADED_RUN carries two slots and both are
filled.

**A degraded run may never let a number ship at full claim strength.** Where the
missing capability was the counterfactual denominator's source, every affected
claim drops to bounded phrasing.

## 3.2 Binding: what is required before the first run, and what is not

Invoke reference/binding-interview.md. The staged model is not optional and it is not a
convenience: it is the completeness gate turned on the configuration itself.

**The ten IGNITION organization bindings.** Without these the first run would be
WRONG rather than merely thinner. Four of them are used by this skill on every
single run and are named here because a reader needs to know which ones carry the
claims: COUNTERFACTUAL_AVAILABLE_RUNGS, COUNTERFACTUAL_DEFAULT_RUNG,
MOVING_GROUND_NAME and ROLE_LADDER. The other six are SCOPE_LEVELS,
POPULATION_SHAPE, PLANNING_PERIOD_NAME, PLANNING_PERIOD_LENGTH_DAYS, ORG_NAME and
BINDING_OWNER_NAME.

**TWO OF THOSE FOUR ARE SATISFIED BY DERIVATION AND NEVER BY A FLOOR.**
COUNTERFACTUAL_AVAILABLE_RUNGS and COUNTERFACTUAL_DEFAULT_RUNG each carry a
DERIVATION in their ignition rows that runs BEFORE the floor consequence, because the
second of them asks about this method's configuration and no organization document
answers it. Execute the derivation, record it DERIVED at MEDIUM confidence with the
rungs it kept and the rungs it struck with the definition each was missing, name it
beside the claims it governs, read it back for correction at the interview close, and
apply the floor ONLY where no available rung's own definition is bound. This skill's
half of it is stated in 2.2.1 and is not restated here.

**BINDING_OWNER_CONTACT IS NOT ONE OF THEM AND WAS.** It is DEFERRED, and the
reason is stated in its own ignition discussion in reference/schema/ rather than
here: it is the one candidate a documents-only binding can never satisfy, because
no internal policy document carries a mailbox and SD-CNF-07 forbids inventing one.
**A run with no bound address is therefore NOT provisional on that account alone.**
It still prints, at the standing prominence and on every run until an address is
bound, the sentence in that variable's own SECTION A1 row: the invitation in this
artifact names no address, so a reader who finds something wrong has nowhere to
send it. Binding AUTHORITY is unaffected, because it is computed from
BINDING_OWNER_NAME and the standing senior-role grant, so every deferred question
still fires and still finds an authorized answerer. **Counting it as ignition
stamped every documents-bound run PROVISIONAL forever on a binding no amount of
care could clear**, and a provisional label that never comes off stops
distinguishing a run that is missing something recoverable from one that is not.

**A LENGTH READ OFF A PERIOD NAME IS DERIVED, NEVER ANSWERED.**
PLANNING_PERIOD_LENGTH_DAYS is an ignition member, and a period NAME is not an
answer to it. Where the interview collected a name and no length, the length is
computed from the name and the operating window, and it is recorded as **DERIVED,
with the name it was derived from and the derivation stated**, exactly as any other
derived sub-field. DERIVED satisfies ignition; **counting it ANSWERED does not, and
is a hole in the completeness trace rather than a shortcut through it.** Where the
name does not yield a length unambiguously, which is any name that does not fix
both a start and an end, the value is UNBOUND and is asked. The same rule governs
every ignition member a reader might be tempted to infer from a neighbouring
answer: state which of ANSWERED, DERIVED, DEFAULTED and DECLINED it is, and never
promote a derivation to an answer.

**The four PERSON ignition bindings**, asked of every user on their first run, in
one message, with two of them usually pre-answered from the directory and reduced
to a yes: PERSON_ROLE_TITLE, PERSON_SCOPE_CODE, PERSON_SUPERVISOR_NAME,
PERSON_HAS_DIRECT_REPORTS.

**Everything else is DEFERRED and is requested at the point of need.** When a
deferred binding fires, the skill says four things in this order and then asks:

1. The decision it is facing. Not the variable name. What it is about to do.
2. Why the value is needed for that decision.
3. What it will do if the answerer declines, quoting the documented default and the
   degradation notice from reference/schema/ SECTION A1 or A2 in plain words.
4. The question.

Then it records the answer, confirms the save, and never asks again.

**Constraints on firing, all four binding:** the answerer must be authorized for
that binding; at most two deferred bindings may be requested in any one run, and
never more than one before the first output; where several are outstanding, fire
the one whose default is materially worse than an answer would be; once bound or
declined, never again.

**Where the answerer is not authorized, which is the common case**, the run
proceeds in a degraded but honest mode: apply the documented default, name what is
unbound, state what that changed, do not guess, and queue the request to
BINDING_OWNER_NAME. **A PERSON-tier user is never asked an ORG-tier question**, not
as a fallback, not as a quick check, and not phrased as a confirmation.

The one exception is a value that is genuinely personal even though it looks
organizational: the character limit the user can read off their own open form in
five seconds. PERSON_CONFIRMED_FIELD_LIMITS overrides FIELD_LIMITS for that user's
run only and never writes back to the ORG tier.

**Deferred bindings this skill most often reaches, and the decision that fires
each.** This is a routing table, not a request list; none of these is asked up
front.

| Decision the run is facing | Bindings requested | If declined |
|---|---|---|
| A write-up is about to be drafted | DESTINATION_SYSTEM_NAME, FORM_SPEC_SOURCE | A generic structure is drafted and the user is told to check it against the live form before pasting. |
| The draft needs a section structure | FORM_SECTIONS, FORM_SECTIONS_BY_CYCLE_POSITION | The generic section set is drafted; sections the live form carries and this set does not are not drafted at all, which is stated. |
| A one-block-per-field assertion needs a set of FIELDS to test against | FORM_FIELDS | The field set is derived per its SECTION A1 row from the sections the cycle position draws, dropping the ones nobody drafts and expanding the objectives section to one field per objective, and the derived set is printed in the field index so the set the assertion ran against is visible. |
| A field is about to be written and its limit is unknown | FIELD_LIMITS, OBJECTIVE_FIELD_IS_SINGLE, FIELD_BUDGET_SPLIT | Common defaults are used, every emitted field carries its exact count, and the user is asked once to confirm from the counter next to the field. |
| A heading may not exist on the live form | BANNED_HEADINGS | No warning can be given and the user is told to check the section names against the form before submitting. |
| A behaviour or rating section must be drafted | BEHAVIOUR_FRAMEWORK_NAME, BEHAVIOUR_FRAMEWORK_ITEMS, BEHAVIOUR_SCALE_VALUES, RATING_SCALE, RATING_AXES, SELF_ASSESSMENT_PROMPTS, STATUS_VALUES, ACTIVITY_STATUS_VALUES | Those sections are not drafted at all and are named as not drafted, rather than invented. |
| A claim must ladder above the person's own objective | LINEAGE_LADDER, ENTERPRISE_STRATEGY_PILLARS | No claim is connected to an organization priority; claims are worded at the level they can actually be defended. |
| A claim would cite above the person's own scope | ROLE_LADDER.altitude_ceiling, CONTRIBUTION_VERBS, OWNERSHIP_VERBS | Contribution phrasing is used for anything above the person's own scope, which is the safe direction. |
| More than HEADLINE_CANDIDATE_THRESHOLD wins must be ranked for the headline | INCENTIVE_PLAN_NAME, METRIC_SET, METRIC_MULTIPLIERS | Candidates are ranked by altitude, then peer rank, then magnitude, and the user is asked which should lead. |
| The first review-mode run by a user with direct reports | PEOPLE_LEADER_OBJECTIVE_REQUIRED, PEOPLE_LEADER_OBJECTIVE_SOURCE | None is required or drafted, which is stated. |
| The first claim is about to be worded | CLAIM_STRENGTH_BY_RUNG | The standing strengths are used and printed beside each claim. |
| The first WIN or MISS label is about to be emitted | DEADBAND, as a mapping per rung AND per quantity form, never as a scalar | The standing band for the rung each figure used, and for the form of the quantity it computed, is applied and printed with its unit beside every labelled figure. Rungs 3 and 5 each carry two: a movement band and a level delta band, both computed from the spread in the data. Where the band alone cannot be computed those figures print as deltas with no label; where the COMPARATOR is below MIN_POPULATION_FOR_NORM no delta is computed against it at all, labelled or raw, and the withholding is stated beside the figure, per SD-POP-19. The rung-4 band is fixed in percent of target, needs no peer spread, and labels plan attainment even for a reader with no peers. |
| The first review-mode run | CYCLE_POSITIONS, CYCLE_POSITION_NAMES, GOAL_REVIEW_CADENCE | The generic four positions and a quarterly cadence are assumed and stated wherever cadence affects a date. |
| The first evidence crawl | EVIDENCE_SOURCES, CHAT_PLATFORM_NAME | The standing crawl is used and the tiers actually reached are named with their counts. |
| A rating rubric is cited and its version is unknown | RATING_AXES volatility note, REFERENCE_VALIDITY_PERIODS | Every cached reference expires at year end and a block past that date is refetched, or used and marked stale. |
| Two period files are about to be compared and the population's mode decides which test runs | POPULATION_SHAPE sub-keys for that population: FLOW_COHORT_BASIS, FLOW_OPEN_DEFINITION, reopen_allowed under FLOW; FIXED_ROSTER_CHURN_TOLERANCE and JOIN_OVERLAP_FLOOR under FIXED | The documented defaults in reference/schema/ SECTION A2 apply, the mode is inferred at MEDIUM confidence with its evidence printed, duplicates are kept separate rather than merged on a guess, and the test actually applied is named. |
| A cold population is detected and its rungs must be re-evaluated | COUNTERFACTUAL_RUNG_SCOPES, COLD_START_MIN_PRIOR_SHARE, ADDRESSABLE_SELF_SHARE_CEILING | The standing thresholds are used, the test that fired is named with its figure, every struck rung is named, and the three claimable kinds are surfaced anyway. |
| A rank is about to be drawn and the peer set must be resolved | PEER_SET_LEVEL_DEFAULT, PEER_SET_IS_EXTERNAL, EXTERNAL_PEER_SET_SOURCE | A stated peer COUNT outranks the one-step-coarser derivation and selects the level whose sibling count matches it, recorded as derived from the count. Where nobody stated a count either, an internal sibling set is assumed. Where the requester sits at the coarsest level, no peer set is manufactured, rung 3 is dropped, and the drop is named. |
| The scope may be too small to rank, or the unit may be coarser than the reader | MIN_POPULATION_FOR_RANKING, UNIT_LEVEL_KEY | The standing floor is used, the unit level is detected from the data, and both outcomes in 4.5 are stated before the content rather than discovered by the reader. |

## 3.3 The first run at an organization where nothing is bound

This is the worst case and the most likely one: a frontline employee opens this
skill at a company where no ignition interview has been run and there is no binding
owner recorded.

**The frontline user is never handed the block.** Ignition is a blocking state for
the ORG tier, and the correct response to a blocking state the user cannot clear is
to produce the most useful honest thing available and route the block to somebody
who can clear it. The first run at an unbound organization is a PROVISIONAL RUN. It
produces real output, it is labelled provisional in the artifact, and it neither
pretends to be a bound run nor refuses to be a run.

The sequence is specified end to end in reference/binding-interview.md PART 6 and is followed
exactly. **PART 6 STEP 4 IS THE STEP A FIRST-RUN IMPLEMENTER ACTUALLY OPENS, AND IT
NOW DERIVES BEFORE IT FLOORS**, in the same terms this section and 2.2.1 use: it
carries a second number at whatever rung the two ignition rows derive from the
documents actually bound, it says that a documents-bound first run is usually not at
the floor, and it says that a PROVISIONAL run is not a FLOOR-WORDED run. That step was
stale once while this file three screens away said the opposite, so a careful
implementer read two files and got two documents off one configuration and one data
set. **Where that step and this section are ever read as disagreeing again, neither is
patched locally.** The ignition rows for COUNTERFACTUAL_AVAILABLE_RUNGS and
COUNTERFACTUAL_DEFAULT_RUNG in reference/schema/ are the single statement of the
derivation, both files cite them rather than restating them, and the restatement that
has drifted from those rows is the one that is wrong.

**WHAT EACH UNBOUND IGNITION VARIABLE SPECIFICALLY DOES TO A RUN IS READ FROM ITS
OWN ROW IN THE IGNITION TABLE IN reference/schema/, WHICH IS THE ONLY STATEMENT OF
IT.** The binding-states table carries the GENERIC consequence, that the run is
provisional and is labelled so at the same prominence every time, and **both apply
always and are not alternatives**: the generic one is about the artifact's label,
the specific one is about what the run actually does differently. Work the ignition
row for every variable found unbound, before writing anything, and do not carry a
second copy of any of those consequences in this file. The list below is what this
skill can still DO on such a run, which is a different question and is why it is
stated here.

- It can crawl evidence, because the evidence sources are reachable or they are not,
  and either way the tiers reached are named.
- It can read the supervisor's priorities, because the supervisor is a PERSON
  binding.
- It can rank and compare, because the identifier and a measure resolve.
- **It can still carry a second number on every figure**, at whatever rung the
  ignition rows for COUNTERFACTUAL_AVAILABLE_RUNGS and COUNTERFACTUAL_DEFAULT_RUNG
  leave available when unbound. **BOTH OF THOSE ROWS DERIVE BEFORE THEY FLOOR, and on
  a provisional run the derivation is the operative half**: the available set is
  derived from which rung definitions the documents bound, and the default is derived
  as the highest rung in that set whose own definition is bound. Both are recorded
  DERIVED at MEDIUM confidence and read back for correction. What that rung is and how
  strongly a claim on it may be worded is stated in those rows and is read from them,
  not from here.
- **A PROVISIONAL RUN IS NOT A FLOOR-WORDED RUN**, and the two were confused once. A
  first run that binds the peer, plan and prior-run-rate rungs from the organization's
  own published documents words its claims at the strength those rungs support, names
  the derivation beside them, and still carries the provisional label for everything
  the interview has not answered. Only a run where NO available rung's own definition
  is bound falls to the floor's wording. See 2.2.1, and reference/binding-interview.md PART 6
  step 4, which now states the same rule in the same words for the same run.
- It cannot ladder above the supervisor's stated priority, and it says so.
- Every medium-confidence inference about the organization's shape is written to a
  provisional file with its evidence, never to the config, so that the eventual
  ignition interview opens with those inferences as proposals and takes five
  minutes instead of ten.
- **The provisional labelling is never softened on later provisional runs.** It
  appears at the same prominence every time until the ignition interview happens.

## 3.4 Two independent readers, and one arithmetic

Where the run parses a data file, the parse is verified by two readers with
genuinely different methods, and the arithmetic is then done once.

**WHY THE SPLIT.** If both readers emit computed figures, each must do the same
arithmetic on the same cells, and their agreement proves only that they picked the
same columns. **Independence is real only when the two methods answer DIFFERENT
questions.** One answers "what does this column mean", from header names, known
vocabulary and the alias tables. The other answers "what does this column's data
look like", from value distribution, cardinality, range, null pattern and cross-file
ratio behaviour. Agreement between name-reasoning and value-reasoning is genuine
evidence that a column was identified correctly. The arithmetic is then done once,
deterministically, and is not a matter of opinion. See SD-RUN-01 and SD-RUN-03.

    SEMANTIC READER    emits column MEANING only. No arithmetic.
                       Fields: container selected and why; header row; identity
                       columns; entity columns; benchmark columns; action-evidence
                       columns; period basis; join key candidate.

    EMPIRICAL READER   emits candidate mappings from VALUES only. No header-name
                       reasoning.
                       Fields: container selected and why; header row; column
                       profiles; join key candidate; overlap row count; uniqueness;
                       ratio probes; pairing corroboration; unit normalizations;
                       suspected scale columns.

**Never reconcile against a single ledger and never promote single-method output.**
A single reader produces an UNVERIFIED result, which does not meet the standard for
a permanent record. See SD-RUN-04.

**Reconcile only what BOTH readers can independently emit.** Demanding that two
differently-instructed readers produce identical semantic output is unsatisfiable
and would hard-stop every data-bearing run. See SD-RUN-05.

| Item | Treatment |
|---|---|
| Header row | MUST MATCH EXACTLY. Any mismatch is blocking. |
| Container selected | MUST MATCH EXACTLY. |
| Join key candidate | MUST MATCH EXACTLY. |
| Entity-to-benchmark pairing | CORROBORATED, NOT MATCHED. The semantic reader is authoritative; the empirical reader runs a rejection test only. |
| Period basis | CORROBORATED. The semantic reader is authoritative, reading it from header tokens. The empirical reader does not emit it and is not asked to infer it. |
| Unit normalization factor | CORROBORATED. The empirical reader is authoritative. The semantic reader does not emit arithmetic and is not asked to. |

**NOT REFUTED IS NOT CONFIRMATION.** NOT REFUTED, REFUTED and INCONCLUSIVE are
verdict STATES of a rejection test, not bound variables, and nothing reads them from
the configuration. A rejection test is a necessary condition,
never a sufficient one. The documented evidence: tested exhaustively on real data, a
containment test failed to refute 18 of 20 deliberately WRONG entity-to-benchmark
pairings, because almost any entity is smaller than almost any population it sits
in. It can only catch a gross error. The semantic pairing plus the deterministic
alias table remain the authority. See SD-RUN-06.

- REFUTED when the median ratio exceeds 1 AFTER any unit normalization has been
  applied. An entity cannot exceed the population that contains it. **Normalization
  runs first: a pairing must never be refuted on a units artifact.**
- A median of exactly zero means the entity is thinly distributed, not mispaired.
  Report the zero share and mark the verdict INCONCLUSIVE, never REFUTED. See
  SD-RUN-08.
- **A declared rate or unit incompatibility outranks any NOT REFUTED verdict.**
  Corroboration never overrides a declared block. See SD-RUN-07.

**On disagreement or refutation:**

1. The authoritative reader re-derives that item once, showing its work.
2. Still refuted: mark UNRESOLVED. Exclude that item's figures from every claim and
   list it in the verification section. **Never average two disagreeing values and
   never publish a disputed derivation.** See SD-RUN-09.
3. UNRESOLVED items at or above UNRESOLVED_STOP_COUNT: STOP and return to root.
   The count is performed once, immediately after reconciliation. An item is one
   entry in the MUST MATCH list or one refuted corroboration. **Count UNRESOLVED
   only for items both readers actually emit or corroborate.** An item only one
   reader produces by design is never counted as a disagreement. **The threshold is
   read from the variable and is never written as a number in this file**, so a
   binding owner who sets it gets the run they configured. The gate record is
   `review.unresolved_items` in 7.4.2 and it reads the same variable.

**SD-RUN-09 REACHES TWO OF THIS METHOD'S OWN DERIVATIONS AND NOTHING ELSE, AND IT IS
THE WRONG ANALOGY FOR THE CASE NEXT DOOR.** A statement in the PERSON'S OWN NOTE that a
RESOLVED COLUMN contradicts is not two readers disagreeing about one parse: one side of
it is not a derivation at all. It is SD-CNF-10, executed in 2.12.1 and gated by G24,
and it has its own count, its own stop record and its own place below the boundary. A
run that resolves it by the nearest analogy here is deciding a question of fact that no
rule authorized it to decide, which is what happened once before 2.12.1 existed. **The
two counts are kept apart**: `unresolved_items` counts disagreeing derivations,
`contradicted_items` counts the person against the data, and one being clean says
nothing about the other.

**Where the environment cannot run two independent readers**, say so in the
artifact, run the single available reading, and mark every mapping it produced as
UNVERIFIED in the verification list. An unverified mapping does not stop the run and
it does not silently pass as confirmed.

## 3.5 The stage contract

Every stage in Part 5, and the two-reader step inside Stage 4, carries the same six
fields. See SD-RUN-02.

    PRECONDITION   what must be true before the stage may run
    ACTION         what it does
    POSTCONDITION  what must be true when it finishes
    ON FAIL        where it goes when the postcondition is not met
    WAIT           whether it blocks on a person
    STOP           the named condition, if any, on which it halts

**RETURN TO ROOT** means: halt forward progress, write the checkpoint, report in
plain language what happened, and offer paths forward. It never means silent
continuation.

**Every figure is computed with a tool, never mentally.** See SD-RUN-14. **A run
that cannot be reproduced cannot be trusted:** the checkpoint holds enough to
reproduce every published figure. See SD-RUN-15.

---

# PART 4: DETECTION

Everything in this part is detected before the pipeline proper begins: the cycle
position, the evidence state, the role and claim tier, the population being scored
with its shape, and the two degenerate-scope conditions. They are independent of
each other and every one of them is needed. **No count of them is stated here**,
because the set is the numbered sections below and a count in the heading is a
second declaration that goes stale the moment one is added.

## 4.1 Cycle position

CYCLE_POSITIONS holds exactly four run modes, whose names are configurable through
CYCLE_POSITION_NAMES. The generic four:

| Position | Meaning |
|---|---|
| SET | Objectives are being set for a period that has not run yet. |
| TRACK | Progress is being updated mid-period. |
| MIDPOINT | The mid-period section is being written. |
| CLOSE | The end-of-period section is being written. |

Detected from four inputs, in this order: the period the user names; the current
date against the operating window; the period the supplied data covers; and whether
results exist at all. If it remains ambiguous, ask the period question, which is
blocking.

**Resolve the period being PLANNED or WRITTEN ABOUT, not "the latest".** A relative
phrase is not a named period: phrases such as this period, this cycle and now fall
through to the calendar rules rather than being read as the period the run happens
to start in. **A run that quietly plans or writes about the wrong period is
indistinguishable from a correct one until the person is standing in front of the
work.** See SD-SRC-15. PLAN_AHEAD_RULE decides at a window boundary.

**The reporting calendar is not authority.** A fiscal or calendar quarter end is an
input the operating window converts, never a due date.
REPORTING_CALENDAR_IS_NOT_AUTHORITY must be true. See SD-SCO-03.

Cycle position decides which sections are drafted, through
FORM_SECTIONS_BY_CYCLE_POSITION.

## 4.2 Evidence state

Four states, independent of cycle position. This drives crawl depth and decides
whether reconstruction runs.

| State | Meaning | Consequence |
|---|---|---|
| FULL | Objectives and data and a documented record all present. | Full crawl, full parse, full sweep. |
| REPORTS | Data files present, objectives thin or absent. | Full parse; objectives may need reconstruction. |
| FRAGMENT | A sentence or two and nothing else. | Skip the data stage. Reconstruct. |
| EMPTY | Nothing at all. | Skip the data stage. Reconstruct from the crawl and from the person's own answers. |

**THE NO-DATA BRANCH.** FRAGMENT and EMPTY trigger reconstruction: crawl the period,
derive the objectives the work actually laddered to, and present them for the person
to edit rather than to author. **This path is the product and MUST NOT be blocked by
any data gate.** The gates that inspect parsed data are NOT APPLICABLE on this
branch, per the matrix in Part 7.1, and NOT APPLICABLE is a passing state. See
SD-EFF-37.

## 4.3 Role tier and claim tier

Resolved from the person's own record wherever the directory is reachable, and
confirmed rather than prompted.

1. Expand abbreviations through ROLE_TITLE_ABBREVIATIONS before matching, and take
   the most senior token. See SD-IDN-04.
2. **A scope word outranks a role word, and that test runs FIRST.** A title carrying
   any token from WIDE_SCOPE_TOKENS outranks a junior role word, so a senior title
   is never demoted below what the data supports. See SD-IDN-03.
3. Then match against ROLE_LADDER.titles.
4. If it resolves to nothing, ask once, offering the ladder's display names as a
   numbered list with one line each describing what that role owns, and accept a
   number.
5. If the person does not answer and the directory is unreachable, use
   ROLE_FALLBACK_KEY, which is the narrowest role. **An unknown that defaults upward
   inflates every claim and every list size**, so the fallback is always downward.

The resolved role supplies four things: the scope level owned, the claim tier
(DIRECT or AGGREGATE), the altitude ceiling, and the peer level whose siblings form
the peer set.

**HOW A ROLE MAPS ONTO A SCOPE LEVEL IS DERIVED IN EXACTLY ONE PLACE**, the
ROLE_LADDER.scope_level row in reference/schema/ SECTION A1, and this file cites it
rather than restating it. The same is true of claim_tier and peer_level, which are
derived by their own A1 rows. **Do not write a shorter formulation of that
derivation here, or anywhere else in this file.** The rule that a shorter
formulation must yield to the bound definition is the last rule in this file, and
the way a second formulation does damage is not that a reader cannot find the
first: it is that the reader stops at whichever they reach first and ships a
different artifact off the same configuration.

**The manager lookup is mandatory and non-substitutable.** A profile record that
carries no manager field can never answer the question of who someone reports to.
Record no supervisor ONLY when both hold: a manager lookup was actually made and
returned empty, AND the person's own title names the top of the house. **An error is
a failed lookup, not an absent manager.** See SD-IDN-01 and SD-IDN-02.

**A role with direct reports carries a people-leadership objective** where
PEOPLE_LEADER_OBJECTIVE_REQUIRED is true, sourced from
PEOPLE_LEADER_OBJECTIVE_SOURCE. PERSON_HAS_DIRECT_REPORTS also turns on the
attribution check in 2.17.

## 4.4 Which population is being scored, and what shape it has

Resolved at Stage 0, before the crawl, and named in the front panel of whatever the
run emits. **A run never asks whether this company is a roster or a pipeline. It
asks which population it is scoring and what shape that population has.** The full
rule set is Part 13, which carries SD-POP-21 through SD-POP-24 into this skill.

Three outputs from this resolution feed the rest of the pipeline:

1. **The population key**, from POPULATION_SHAPE, resolved from the request and
   from the source in hand. Where only one population is declared it is the default
   and nothing else changes.
2. **The mode**, FIXED or FLOW, read from that population on a bound run and
   inferred at MEDIUM confidence with its evidence printed on a provisional run.
3. **Which of the three detection tests decided it**, and whether it was decided or
   taken on a tie-break. A tie-break that leaves no trace is a guess.

## 4.5 Degenerate scope, which is two different failures

Both are detected before the content and neither is silent. **They are kept
separate, because one is honest and one is a binding error.**

**A. A genuinely small population.** SD-POP-25. Ranking, percentile, median,
distribution and peer language are meaningless below MIN_POPULATION_FOR_RANKING.
The arithmetic argument that a small population needs no special rule is true and
irrelevant: an average-rank percentile over one unit is well defined and equals a
constant, and a rank of one out of one is well defined and says nothing. **The test
is not whether the number computes. It is whether the number carries
information.**

Below the floor, this skill does not print a percentile, does not draw a peer
comparison, and does not use comparative language, however well the arithmetic
behaves. What it does instead, and it is not nothing:

1. Say it on the front panel BEFORE the content, in plain words, in a sentence that
   agrees at every count per SD-LNG-13: "this scope contains 1 account, so nothing
   here is ranked, no percentile is printed and no comparison is drawn", and the
   same sentence with "3 accounts" where three is the count. Carry the singular and
   the plural of the bound unit noun with the count and select on the value, and
   name the unit from POPULATION_SHAPE rather than writing "units". **A scope of one
   is the commonest case this sentence ever prints in**, which is exactly why it
   must not read "1 accounts".
2. Deliver the content. Everything that describes rather than orders survives: the
   objectives, the measures, the absolute build, the execution claims with their
   denominator populations, the evidence, the learnings, the narrative.
3. **Name every suppressed comparison by name**, so the reader can see what was not
   attempted rather than assuming it was attempted and came back empty.
4. Name the scope level, or the finer thing, that WOULD produce a comparable
   population for this reader, so the answer is actionable rather than a refusal.
5. Where the claim would have rested on rung 3, drop that rung, fall to the highest
   remaining bound rung per SD-CTR-24, and name the drop.

This is not the same as having fewer eligible items than a list size, which is a
normal short list. It is a population too small to order at all. **Never pad, and
never present a one-row comparison as a distribution.**

**B. A unit of business coarser than the reader's own scope.** SD-POP-26. This is a
BINDING ERROR, not a small population, and it is reported as one. Where the unit of
business sits at a level COARSER than the reader's own scope level, that reader
owns a PART of a unit and cannot receive a ranked list of units at all.

Detected rather than asserted: resolve the unit level from the data, as the scope
level whose distinct value count over the in-scope population equals that
population's record count, and compare it against the reader's own resolved level.
Where MORE THAN ONE level satisfies the test, which is always so when the in-scope
population holds exactly one record, take the FINEST matching level, and report a
binding error ONLY where the reader's own level is strictly finer than EVERY level
that satisfies the test over a population of MORE THAN ONE RECORD. Over a population
of one record the detection is uninformative: say the scope holds one unit and do not
assert a configuration mismatch that cannot be distinguished. SD-POP-26.
Where UNIT_LEVEL_KEY is bound, it is the declaration and the detection is the check
on it. Where the unit level is coarser than the reader's level, **say so before the
content, name both levels, say plainly that this is a configuration mismatch rather
than a property of their scope, route the output per A above, and queue the request
to BINDING_OWNER_NAME.**

The failure this prevents: an interview accepting two individually correct answers,
a containment chain and a unit noun, that are incompatible with each other, and a
run then producing an artifact in which every gate passes and every count
reconciles at one.

---

# PART 5: THE PIPELINE, AS A STATE MACHINE

Thirteen numbered stages, Stage 0 through Stage 12, plus five sub-stages: 6.4, 6.5,
10.5, 11.5 and 12.1. Linear order with two skip branches and one loop. Three
question rounds exist in the design and two of them are full rounds that block; the
third is the preview, which also blocks.

Nothing in this pipeline may be reordered to save time. See SD-EFF-07: no stage may
weaken an earlier stage's guarantee, and every gate re-checks the previous one.

## 5.0 The state machine

    PROBE     Capability probe (reference/capability-probe.md)
      advance: probe record written to SCRATCH_DIR
      stop:    shared.source_unreadable only: no source readable and none supplied
               inline. Name every location attempted, then ask for the file.
               Nothing else in the probe stops a run.

    Stage 0   Scope Lock
      advance: single role, single scope, single period, known objective source;
               cycle position, evidence state, the declared population being
               scored and that population's shape all determined
      block:   scope not inferable, ask the scope question (blocking)
      fail:    work the re-tests in SD-IDN-16, then the shared gate fires with its
               own behaviour, ask_one_question_then_stop
      stop:    shared.scope_unresolvable: scope cannot be resolved to a single role
               and a single scope

    Stage 1   Expectation Gate
      advance: automatic. This stage informs; it does not block.
      fail:    estimate not computable, state the work without a duration, continue

    Stage 2   Goal Ledger (cache first)
      advance: every reference within validity or explicitly recorded as stale;
               live sources fetched; all of it checkpointed
      block:   the expiry gate is BLOCKING per block (2.21)
      gate:    the RETRIEVAL GATE (1.6) fails closed on any unopened supervisor or
               upline attachment
      fail:    work the retry ladder, then use the stale or most recent block and
               CONTINUE. This stage does not hard stop.

    Stage 3   Evidence Ledger
      advance: ledger populated, or evidence state confirmed EMPTY
      fail:    reduce the window, retry, proceed with what was found, note the gap
      route:   an empty ledger routes to reconstruction and to the undocumented
               work question
      stop:    none. An empty evidence ledger is a valid state.

    Stage 4   Data Ingestion and Period Validation
      skip:    evaluated in order, first match wins. Cycle position SET skips the
               whole stage. Evidence state FRAGMENT or EMPTY skips the whole stage.
               Otherwise, at least one data file present, so parse.
      advance: period validated or explicitly confirmed by the person; mappings
               reconciled per 3.4
      block:   period uncertain, ask the data question (blocking); a small unit
               drift factor detected, ask the unit question (blocking); a rate
               denominator mismatch is blocked with no override; a unit mismatch is
               blocked until normalized
      fail:    parse retry per the contract, then RETURN TO ROOT
      stop:    only the review-group gates that fire at this stage:
               data_period_mismatch; join_overlap_below_floor, which fires under
               FIXED mode ONLY and is never applied under FLOW; and
               unresolved_items, at UNRESOLVED_STOP_COUNT

    Stage 5   Checkpoint (runs alongside Stages 2 through 4)
      advance: checkpoint written with resume state current
      fail:    retry once, then continue with a warning
      stop:    never. A checkpoint failure degrades durability, not correctness.

    Stage 6   Marriage and Scoring
      advance: every claimable figure labelled and ranked; every superlative
               carrying a tie count; every claim carrying its unit and its rung
      fail:    RETURN TO ROOT
      stop:    evidence state FULL or REPORTS AND no claimable figure from any
               entity-benchmark pairing AND no claimable execution outcome from any
               unbenchmarked entity. Does NOT apply on the no-data branch.

    Stage 6.4 Win Discovery Sweep
      advance: a ranked candidate win list
      fail:    an impossible cut is recorded as unavailable and the sweep continues
      stop:    none. Zero candidates proceeds to the questions.

    Stage 6.5 Reconstruction (conditional)
      enter:   no objectives from any source AND the person chose reconstruction
      advance: between 1 and SYNTHESIS_MAX_OBJECTIVES candidate objectives, every
               one flagged RECONSTRUCTED
      fail:    no cluster reaches SYNTHESIS_MIN_EVIDENCE, so emit a single objective
               from the person's own answer, flagged RECONSTRUCTED
      stop:    none. This stage never blocks the run.

    Stage 7   Action Inference and Learning Synthesis
      advance: every WIN has proposed action language, every MISS has a proposed
               learning, all in state PROPOSED
      fail:    no activity evidence correlates, so emit the result without an action
               clause and route it to the open question; retry once with a widened
               evidence set; then proceed without the clause. NEVER invent an action.
      stop:    none

    Stage 8   Question Round 1, grounded          [WAIT POINT]
      advance: every blocking question for this stage answered
      fail:    no response, so write the checkpoint and route to Stage 12.1
      stop:    the person cancels

    Stage 9   Draft Assembly
      advance: the cycle-specific postcondition met
      fail:    repair and re-verify up to REPAIR_CYCLE_LIMIT cycles, then
               RETURN TO ROOT
      stop:    review.review_mode_no_objectives: no objectives available from any
               source, including reconstruction

    Stage 10  Question Round 2, field level        [WAIT POINT]
      advance: every blocking question answered; EVERY proposal resolved to
               CONFIRMED or REMOVED
      fail:    no response, so checkpoint and route to Stage 12.1
      stop:    the person cancels

    Stage 10.5 Re-Assembly
      advance: no reserved placeholder remains for an answered question; no
               sentence in the copy region derives from a proposal outside
               CONFIRMED; every proposal below the boundary satisfies 2.20
      fail:    repair and re-verify up to REPAIR_CYCLE_LIMIT cycles, then
               RETURN TO ROOT

    Stage 11  Grading
      advance: every measure scored; every UNGRADABLE one carrying a proposed
               rewrite and a one-line reason
      fail:    emit the measure unscored and note that it could not be graded.
               Never suppress a measure because it failed grading.
      stop:    none

    Stage 11.5 Preview                             [WAIT POINT]
      advance: the person has seen the complete draft and responded, or has
               explicitly declined to review
      fail:    no response, so checkpoint and route to Stage 12.1
      stop:    the person cancels

    Stage 12  Greenlight and Emit                  [WAIT POINT]
      advance: every gate in Part 7 returns PASS or NOT APPLICABLE
      fail:    route per 7.3 to a stage that can REMEDIATE it
      stop:    PER_GATE_FAILURE_LIMIT failed returns on one gate, which routes to
               Stage 12.1 and does NOT return to root
      budget:  GLOBAL_REMEDIATION_BUDGET cycles across all gates, then Stage 12.1
               regardless of which gate is failing

    Stage 12.1 Incomplete Emit Path (terminal, and never empty)
      entered from: Stage 8 ON FAIL, Stage 10 ON FAIL, Stage 11.5 ON FAIL, a
               per-gate triple failure, or the global remediation budget exhausted
      output:  cycle-appropriate blocks, with every unanswered blocking question
               resolved by its CLASS per 6.3: a CONSTRAINT question takes its
               documented default shape and the content ships with the departure
               named; a CONTENT question puts INCOMPLETE_PLACEHOLDER_TEXT in the
               fields it feeds and in no others. All of it under
               INCOMPLETE_BANNER_TEXT, naming what is outstanding and which
               question resolves each, with constraint departures and content
               placeholders listed separately. The checkpoint is RETAINED.

    WAIT POINTS: after scope lock and before the crawl; after Question Round 1 and
    before drafting; after Question Round 2 and before emitting; and before
    emitting, for the greenlight.

    FAILURE DESTINATIONS
      RETURN TO ROOT   halt forward progress, checkpoint, report plainly, offer
                       paths forward. Reached from: Stage 4 parse failure, Stage 6
                       ON FAIL, Stage 9 double assembly failure, Stage 10.5 double
                       failure, retry-ladder exhaustion, and a reader failing twice
                       on the same file.
      Stage 12.1       reached from unanswered blocking questions and from gate
                       exhaustion. Always produces something.
      HARD GATE        the closed set in Part 7.4.

**On the contradiction this pipeline inherited, resolved here once.** The source
skill said in one place that a gate failing three times escalates to RETURN TO ROOT
and in another that it routes to the incomplete emit path and explicitly does not
return to root. **The incomplete emit path wins.** A person who has waited through a
long crawl and two question rounds must never receive nothing, and a bannered
partial draft they can finish is always worth more than an empty result. See
SD-EFF-05. RETURN TO ROOT remains the destination for the failures listed above,
none of which has produced a draft yet.

## Stage 0: Scope Lock

    PRECONDITION   the skill is invoked; the probe record exists
    ACTION         resolve identity, role, scope, manager and the upline chain to
                   CHAIN_WALK_DEPTH from the directory. Propose scope, period and
                   objective source as confirmations, never as open prompts.
                   Determine cycle position (4.1), evidence state (4.2), the
                   population and its shape (4.4 and Part 13), and run the
                   degenerate-scope tests (4.5).
    POSTCONDITION  a single role, a single scope, a single period, a known
                   objective source, the declared population being scored and its
                   shape, and every detected property in Part 4 settled
    ON FAIL        re-test the comparison as text on both sides and re-test the
                   level reading, per SD-IDN-16, then offer the distinct values
                   present at every level. The gate's own behaviour then governs:
                   ask_one_question_then_stop, per 7.4.1. No attempt count is
                   written here, because the gate record carries the behaviour.
    WAIT           the person's confirmation
    STOP           shared.scope_unresolvable: scope cannot be resolved to a single
                   role and a single scope

Everything downstream depends on this. **A write-up built on the wrong scope is
worthless.**

Rules that govern the asking here, all of them from the shared doctrine:

- **Ask nothing the records already hold.** Work the ladder and stop at the first
  hit: the request itself; the person's own directory record read in FULL, not only
  the title; their manager's record; stored memory from a previous run; the source
  file itself including its distinct values; the filename or the message that
  carried the file; and only then, ask. See SD-IDN-12 and SD-IDN-20.
- **Propose, do not prompt.** See SD-IDN-19.
- **The person speaks naturally; the skill does the arithmetic.** Accept a short
  scope code and pad it. Never ask the person to pad, never reject a short code, and
  never ask them to restate it in the file's format. See SD-IDN-11.
- **Compare identifiers as TEXT on both sides**, after padding. See SD-IDN-09.
- **Zero rows means the filter is wrong before it means the scope is empty.**
  Re-test the comparison as text on both sides, re-test the level reading, and only
  then come back with the distinct values present at every level. See SD-IDN-16.
- **When you must ask, ask in the person's language, not the file's**: offer the
  distinct values present, each labelled with something recognizable, with a count
  beside each, and accept a name or a list position. See SD-IDN-13 and
  ASK_LANGUAGE_RULE.
- **Narrow before asking.** If a coarser level resolves and a finer one does not,
  use the coarser one to narrow the question. See SD-IDN-14.
- **Batch every question into a single message.** See SD-IDN-17.
- **Persist a settled answer and verify the save succeeded.** See SD-IDN-15.

## Stage 1: Expectation Gate

    PRECONDITION   scope locked
    ACTION         state the work, estimate the time from RUN_ESTIMATE_BANDS by
                   evidence state, and set the return expectation
    POSTCONDITION  the person knows roughly how long this will take and what they
                   will come back to
    ON FAIL        if the estimate cannot be computed, state the work without a
                   duration
    WAIT           none. This stage informs; it does not block.
    STOP           none

This stage exists because Part 1.1 removes run length as a cost, and a person who
has not been told that will read a long silence as a failure. Say what is being
read, in the person's terms, and say that the silence is work.

Where the estimate is generic rather than measured, say so. The bands are a bound
default, not a measurement of this run.

## Stage 2: Goal Ledger, cache first

    PRECONDITION   scope locked
    ACTION         read the cached reference blocks first; run the expiry gate on
                   EVERY block; refresh what is stale; then fetch the always-live
                   sources
    POSTCONDITION  every reference present and within validity, or explicitly
                   recorded as stale; live sources fetched; all of it in the
                   checkpoint
    ON FAIL        work the retry ladder, then fall back to the stale or most
                   recent block and CONTINUE
    WAIT           none. Runs during the expectation gate. Ask this stage's
                   questions while it runs, per 1.4.
    STOP           none. This stage does not hard stop.

**2a. The cached reference library.** Part 12 of this file defines its structure.
Each block opens with a validity date, a source name and a fetch date.

**2b. The expiry gate, BLOCKING per block.** Specified in 2.21.

**2c. Always live, never cached.** Two classes of source are per-person or
per-period and are fetched on EVERY run:

1. **The supervisor chain's stated priorities.** Sweep by SENDER across
   MAIL_SWEEP_FOLDERS, which must include the deleted-items equivalent, over
   SUPERVISOR_SWEEP_WINDOW_CURRENT for the current period and
   SUPERVISOR_SWEEP_WINDOW_PRIOR for carry-forward. **Never filter the sweep by
   keyword.** See SD-PRI-02. **Classify by CONTENT, not by keyword and not by
   length; when in doubt, KEEP.** See SD-PRI-03.
2. **Anything the person supplied in this request**, read for EVIDENCE ONLY per 2.9.

**AND THE INPUT SET IS ITSELF A PRIORITY SOURCE, PER reference/capability-probe.md P3 RUNG 3,
WHICH IS WALKED AND NOT SKIPPED.** Where FILE_READ is present, every readable
non-source file the person supplied is a CANDIDATE priority document, discovered by
what it SAYS and never by its filename. That rung's three admission tests are obeyed
there in full and are not restated here. **What this skill states, because a review
runs over a window that a real directive very often sits INSIDE, is how the PERIOD test
is read.**

**THE PERIOD TEST IS AN OVERLAP TEST, NOT A COVERAGE TEST, AND THE RUN RECORDS THE
OVERLAP.** A candidate is admitted where the period it carries or implies OVERLAPS the
window being run. **A source covering PART of the window is admitted FOR THAT PART, and
its scope is stated beside anything drawn from it.** Read as a coverage test it rejects
exactly the sources a review most needs: a dated statement of what the organization
asked for during one month of the year being reviewed does not COVER that year, it sits
inside it, and a literal implementer records it READ AND NOT ADMITTED and loses a
genuine, dated, attributable directive that was one read away. **The same wording bites
the other way at the other end**: a source covering a whole year fails a run over one
month of it, and the item lost there is the annual objective every monthly claim is
supposed to ladder to. **A source whose period does not overlap the window at all is
still NOT ADMITTED**, with the test it failed named, because that is a statement about a
different period and admitting it would date the run's own directives wrongly.

**WHAT IS RECORDED FOR AN ADMITTED PARTIAL SOURCE:** its title, its issuing person or
role, its date, the rung it came in on, **and the overlap itself, as the part of the
window it speaks to**. Anything drawn from it carries that scope where it is used, so a
priority stated for one month is never read as a priority stated for the year. Authority
is unchanged by the rung and unchanged by the overlap: a directive is weighted by WHO
issued it under PRIORITY_SOURCES, never by how much of the window it covers.

**Walk the chain upward and weight by distance**, using CHAIN_DISTANCE_WEIGHTS. The
nearer manager knows the units, so where two levels disagree the nearer one wins,
and the disagreement is named rather than averaged. **Record every level, including
the ones that published nothing.** See SD-PRI-06 and SD-PRI-07.

**Never conclude an absence from the wrong instrument.** A search that returns
nothing proves the search ran, not that nothing was published. See SD-PRI-04.

**Reading and acting are two separate decisions.** Read everything, then decide what
it means. See SD-PRI-05.

**ANY list from anyone in the chain is a must-cover; no trigger phrase is
required.** The only thing that releases an item is an explicit instruction not to
cover it, from DIRECTIVE_RELEASE_PHRASES. See SD-PRI-11.

**Apply the ACTOR TEST before treating a list as a directive.** A list that names
another party as the actor is an assignment to that party, not a directive to the
reader. ACTOR_TEST_ENABLED must be true and the actor test is the only test. See
SD-PRI-12. **When in doubt, treat it as directed.** See SD-PRI-13.

**A mandatory item's weight never decays with the age of the instruction.** See
SD-PRI-10.

**Unresolvable direction is surfaced and changes nothing about the ranking.** See
SD-PRI-16.

The retrieval gate in 1.6 fires here and blocks drafting.

**2d. Refresh, and the write-back.** Discover the path every run; never hard-code
it. Read the actual folder list and select by name content, ignoring leading
numerals, punctuation and spacing. Reference values are a starting point for
discovery only. The documented case: two consecutive periods' folders in the same
library differed only by a space after a numeral, and a literal path breaks the
first period somebody types it differently, silently. See SD-SRC-14.

## Stage 3: Evidence Ledger

    PRECONDITION   scope locked
    ACTION         crawl EVIDENCE_SOURCES in tiers, appending each tier to the
                   checkpoint before starting the next; stop widening as soon as
                   the ledger is sufficient for the cycle position
    POSTCONDITION  the evidence ledger is populated, or the evidence state is
                   confirmed EMPTY
    ON FAIL        reduce the window, retry, then proceed with what was found and
                   note the gap
    WAIT           none. Runs during the expectation gate.
    STOP           none. An empty evidence ledger is a valid state and routes to
                   reconstruction and to the undocumented-work question.

The standing crawl, used where EVIDENCE_SOURCES is unbound:

| Tier | Source | Condition |
|---|---|---|
| 1 | The person's own sent messages across the period. | Always. |
| 2 | Received messages naming the person. | Always. |
| 3 | Chat posts, calendar events organized or led, files authored. | Positions that write about a completed period. |
| 4 | Anything wider. | Only on a stated trigger: the person says something is missing, or tiers 1 through 3 produced fewer than EVIDENCE_SUFFICIENCY_FLOOR items. |

**Widening happens only on a stated trigger**, never because the ledger looks thin
to the agent.

Per item, record: what happened; when; the quantified outcome where one is present;
the source; and a classification as a business result or as an organization
contribution. Unmatched items go to the organization-contribution holding list for
the free-text sections rather than being discarded.

## Stage 4: Data Ingestion and Period Validation

    PRECONDITION   evaluated in order, first match wins:
                   cycle position SET, so SKIP the whole stage;
                   evidence state FRAGMENT or EMPTY, so SKIP the whole stage;
                   at least one data file present, so parse.
    ACTION         resolve the file per reference/field-resolution.md, run the two readers
                   per 3.4, reconcile, then compute every figure once
    POSTCONDITION  the period is validated or explicitly confirmed by the person,
                   and the mappings are reconciled
    ON FAIL        parse retry per the contract, then RETURN TO ROOT
    WAIT           on an uncertain period or a mismatch, wait for the data question
    STOP           only the review-group gates that fire here: data_period_mismatch;
                   join_overlap_below_floor, under FIXED mode ONLY; and
                   unresolved_items at UNRESOLVED_STOP_COUNT. Under FLOW no
                   overlap gate exists at all, per Part 13 divergence 1.

### Period validation, which runs before any figure is claimed

Establish what period the data covers, by authority order: an explicit statement in
the file; a period stamp in the file's own metadata; the filename; the message that
carried it. **A bare month name is not evidence of a period**, because it does not
say which year or which window. Where coverage cannot be established, ask; where the
answer does not cover the period being written about, STOP. See SD-PRS-24 and
SD-SRC-15.

**COVERAGE IS NOT THE ONLY TEST. A PERIOD THAT HAS NOT HAPPENED YET IS IMPOSSIBLE,
NOT MERELY UNUSUAL.** The coverage test asks whether the resolved period contains the
period being written about, and a source stamped for a window that ends AFTER the run
date passes it comfortably: a fourth-quarter file covers the year it sits in, whatever
today's date is. **So the run compares the resolved period's END to the run date,
every run, as a separate test:**

1. **Where the resolved period's end is at or before the run date**, nothing further
   applies.
2. **Where it POSTDATES the run date**, record it as an IMPOSSIBLE PERIOD. **Name BOTH
   dates on the front panel, at full prominence**: the run date and the period end the
   source claims, in the same sentence, so a reader can see the contradiction without
   computing it.
3. **Treat every figure drawn from that source as PROVISIONAL on the discrepancy being
   resolved**, and say so beside the figures rather than only once at the top. The
   figures are not withheld and the run is not stopped: the file is real, somebody
   produced it, and the most likely explanations are a mislabelled export, a fiscal
   calendar that does not match the run clock, or a run clock that is wrong.
4. **Ask, where a channel exists**, naming both dates and offering the likely
   readings. Where no channel exists, the disclosure stands in place of the answer.
5. **The same test applies to a person's own supplied evidence note**, and to any
   dated statement the run takes a figure from, not only to the data files.
6. **AND THE FACT TRAVELS INTO THE COPY REGION, NOT ONLY ONTO THE FRONT PANEL.** The
   panel is above the submission boundary and **the panel is not what gets pasted**:
   only the field blocks travel into the destination system, so a disclosure that lives
   only on the panel is a disclosure the permanent record does not carry. Where the
   period end postdates the run date, **every claim whose figure is drawn from that
   source states inside its own block, in the person's own register per 10.2.1, that
   the period is not yet complete and what the figure is as at the run date**. It is
   said in the person's words and not as a method note, it is protected from
   COMPRESSION_ORDER exactly as the ground's short form is, and it is not dropped to
   make a field fit; where it will not fit, OVER_LIMIT_REMEDY applies and the objective
   is split. **A PERMANENT RECORD BUILT ON AN UNFINISHED PERIOD IS THE PRECISE THING
   THIS SKILL EXISTS TO STOP**, and a run that disclosed it only where the reader could
   see it and the record could not has disclosed it to the wrong reader. The panel line
   at item 3 of 8.3 and the full form below the boundary are both unchanged and neither
   is a substitute for this.

**This is SD-EXC-07's instinct applied to the period stamp itself.** That rule says a
future-dated VALUE inside a column is a data error, is reported rather than shaded,
and is excluded from every statistic derived from that column. **The period stamp is
the same kind of value and was the one place the instinct was never applied**, so a
run could proceed, correctly by every gate, on data that could not exist yet. It is a
disclosure and a provisional label, not a stop, because stopping on it would throw
away a real file over a calendar mismatch the reader can very often explain in one
sentence.

**Never analyze a partial source, and count RECORDS rather than a reported extent.**

### The parsing contract, seven items in order

**Item 1. Container and header detection.** Invoke reference/field-resolution.md Parts 1 and
2. Never take the first container on faith; score by resolvable REQUIRED concepts,
not by name; break ties by record count, never by a reported extent; detect the
header row rather than assuming it, within HEADER_SCAN_DEPTH; record the choice and
the runner-up.

**Item 2. Join key resolution, and the like-for-like test, which is
SHAPE-DEPENDENT.** A valid join key is near-unique in BOTH files, at or above
JOIN_UNIQUENESS_FLOOR, and produces a one-to-one match. Reject many-to-many
candidates. Prefer a column whose name or profile suggests a unit identifier over a
geographic or personnel code, because those overlap heavily and are not unit keys.
Normalize before joining: trim whitespace, strip leading zeros, casefold, remove
non-alphanumeric separators. A code stored as text with a leading zero must still
match its integer twin. See SD-PRS-31.

**Which key is joined on is decided by the population's shape**, per Part 13
divergence 2. Under FIXED it is the unit identifier. Under FLOW with
POPULATION_SHAPE.reopen_allowed true it is the EPISODE KEY, the unit identifier plus
the entry date, and duplicates are merged WITHIN an episode and never ACROSS
episodes. Where entry dates are absent and reopen_allowed is true, or on a
provisional run where reopen_allowed is always unbound, the rows are kept separate,
marked UNRESOLVED DUPLICATES and named with their count, never merged on a guess.

**Which like-for-like test runs is also decided by the shape**, per Part 13
divergence 1, and the run STATES WHICH TEST IT APPLIED.

- **Under FIXED, the overlap floor applies and it is a stop.** Matched rows must be
  at least JOIN_OVERLAP_FLOOR of the row count of the smaller file. Below that,
  stop and report both rosters. **Without this floor, a near-empty intersection
  produces figures that both readers derive identically from the same empty set,
  agree on perfectly, and promote to CONFIRMED. A fabricated rank would ship
  carrying two-method validation.** See SD-PRS-32. Roster churn beyond
  FIXED_ROSTER_CHURN_TOLERANCE labels the comparison as not like for like and is
  still published; it is never suppressed.
- **Under FIXED, THE EXIT TEST RUNS SEPARATELY, and it runs BEFORE anything is
  computed on the pair.** SD-CMP-09. Overlap tests the ENTRY side only: whether the
  units in the prior file are still here. **It cannot see the units that LEFT,
  because they are absent from both sides of the test.** So count the units present
  in the PRIOR file and ABSENT from the current one. That count is the number of
  exits the pair can see, it is printed, and it is a named result rather than an
  observation somebody happened to make. The full rule, including what may be
  claimed afterwards, is SD-CMP-09 and it is obeyed there in full.

  **A ZERO EXIT COUNT IS THE PATHOLOGICAL CASE AND IT SCORES PERFECTLY.** A
  prior-period file containing only the units that survived yields one hundred
  percent overlap, zero churn out, and passes JOIN_OVERLAP_FLOOR at its maximum:
  **the test that exists to decide whether two files describe the same population
  certifies the one input that cannot answer the question it is being used for.**
  Where the exit count is zero the run is in one of exactly two states, they are not
  the same state, and **the run says WHICH it believes and WHY before it computes
  anything**: a SURVIVOR-ONLY EXTRACT, which is the current roster valued at an
  earlier date; or a POPULATION THAT GENUINELY LOST NOTHING, which is real and rare
  above a small population. The evidence that separates them is named in SD-CMP-09
  and every piece of it is available here: the population size; whether the prior
  row count equals the current count minus the units created since; whether any
  independent source disagrees with the prior file's counts; and whether the prior
  file's own period stamp precedes the units it contains.

  **On a survivor-only pair the claims are CAPPED, not refused.** Retention and
  churn are NOT COMPUTABLE, which is neither zero nor one hundred percent, and the
  artifact says so where the figure would have gone. Same-unit growth is computable,
  survivor-biased, and **never published as a bare figure**: it ships only beside the
  total movement across the whole current population, **with the gap between the two
  NAMED for what it is, the part of the change that left.** Total movement is
  computable and unaffected.

  **AND "NAMED" IS NOT ALWAYS "SUBTRACTED", BECAUSE THE TWO FIGURES ARE NOT ALWAYS
  COMMENSURABLE.** Test the two before naming the gap, exactly as item 4 tests any
  other pair:

  - **WHERE BOTH REST ON THE SAME MEASURE, THE SAME BASIS AND THE SAME POPULATION
    DEFINITION, NAME THE GAP AS A FIGURE**, with its unit, beside the two it came
    from. That is the ordinary case when both come out of the same extract.
  - **WHERE THEY REST ON DIFFERENT MEASURES, PRINT BOTH WITH THEIR BASES NAMED AND
    STATE IN WORDS WHAT SEPARATES THEM, AND COMPUTE NO DIFFERENCE.** This is the
    ordinary case when the survivor figure comes from a book extract and the only
    total movement that counts what LEFT comes from a production system: measured on
    one run, a survivor figure on the book's annual-premium basis against a total
    movement on written premium, two bases differing by a factor near four.
    **Subtracting one from the other to manufacture a gap is precisely the comparison
    item 4 and gate G14 BLOCK, with no override**, and G14 governs here. This rule
    never overrides it and never buys a required disclosure with a forbidden
    subtraction.

  **THE REQUIREMENT IS THAT THE READER LEARNS WHAT THE SURVIVOR FIGURE LEAVES OUT.** A
  figure names that; a sentence names it too. What is never permitted is publishing the
  survivor figure alone, and what is never permitted to fix that is a subtraction across
  two measures. Where the two are not commensurable the artifact says so in the same
  place the gap would have been, so a reader cannot mistake the absence of a number for
  an absence of attrition. **No ranking by survivor growth is published at all**,
  because the bias is not uniform across units and the ordering is not recoverable.
  A genuine no-attrition population is stated as such with its evidence and its
  retention figure IS published, at one hundred percent, with the population size
  beside it. Enforced by gate G23.
- **Under FLOW, JOIN_OVERLAP_FLOOR is NEVER applied and is never a gate.**
  Like-for-like is a COHORT DEFINITION test instead: compute both periods on the
  same FLOW_COHORT_BASIS and state the basis beside every comparison. **A healthy
  pipeline shares perhaps a fifth of its rows with itself one period later, so any
  reasonable overlap floor would declare every real comparison invalid**, and the
  stop that results reads as a data problem at the company rather than as a method
  that does not handle pipelines. The gate carries its condition in its own
  fires_at, per Part 7.4.

With three or more files, chain pairwise against one anchor, which is the period-end
file, and report which files were used and which were not. **Never silently discard
a file the person supplied.** See SD-PRS-33.

**Item 3. Unit drift detection.** Run this ONLY on pairs both classified as a rate
or volume measure in item 5. Running it across all numeric columns produces false
positives on identity columns: on real files an account number against a scope code
fires at factor 2. See SD-PRS-36.

    ratio     = start value divided by end value, per matched unit
    oriented  = ratio if the median ratio is at or above 1, otherwise 1 / ratio
    magnitude = the median of the oriented ratios

**ORIENTATION IS MANDATORY AND MUST PRECEDE THE CONCENTRATION TEST.** Without it the
result depends on which file was divided by which. See SD-PRS-34.

Three conditions are co-required before a factor may be declared: at least
UNIT_DRIFT_MIN_PAIRS positive pairs; the magnitude within UNIT_DRIFT_TOLERANCE of a
candidate factor from UNIT_DRIFT_CANDIDATE_FACTORS; and at least
UNIT_DRIFT_CONCENTRATION of oriented ratios within UNIT_DRIFT_BAND of that factor.

**DO NOT test dispersion with a tight interquartile band.** Unit-level business
metrics are naturally dispersed. On real data a genuine conversion showed an
interquartile range of 18 to 24 percent of the median while being an unambiguous
factor of ten. A 5 percent dispersion ceiling is unsatisfiable by construction for
any unit-level metric and would miss every real unit change. **Concentration near
the factor is the correct test, not tightness.** See SD-PRS-35.

**A header token mismatch is evidence, not an automatic block.** The header mismatch
says a conversion is likely; the test says what it is. A letter inside a rate marker
is often a category hint rather than a unit conversion, and treating it as one
blocks most real pairs and produces no output at all. See SD-PRS-38.

**AUTO-NORMALIZE only the factors in UNIT_DRIFT_AUTONORM_FACTORS.** For a small
validated factor, do NOT normalize automatically: ask. **A genuine doubling produces
a magnitude near two, and silently correcting it would erase the person's best
result of the year and never tell them.** See SD-PRS-37.

Record the factor and the evidence in the checkpoint and in the verification list.
Never surface the arithmetic in the person-facing prose.

**Item 4. Rate, unit and lookback compatibility. A BLOCKING PRECONDITION TO ANY
MATH.** Three properties must be separated. Conflating them either blocks every
legitimate comparison or permits a catastrophic one.

    RATE DENOMINATOR   the time base the value is expressed per. A raw period total
                       has no rate denominator. Bound as MEASURE_RATE_TOKENS.
    UNIT               what is being counted. Bound as MEASURE_UNIT_TOKENS.
    LOOKBACK LENGTH    how much history the average covers. Bound as
                       MEASURE_LOOKBACK_TOKENS.

Rules, in order:

- a. **The rate denominator MUST match**, and RATE_DENOMINATOR_MUST_MATCH is true
  with no override. A per-period value compared against a period total is
  meaningless and is BLOCKED.
- b. **The unit MUST match**, or a validated normalization from item 3 must have
  been applied and recorded. This is the rule that prevents a phantom collapse of
  an order of magnitude.
- c. **The lookback MAY differ.** LOOKBACK_MAY_DIFFER is true. When a and b hold, a
  differing lookback is a RUN-RATE COMPARISON: permitted, recorded in the
  verification list as a run-rate comparison naming both bases, stated in any
  narrative that leans on the figure, and **never used to open the write-up.**

**Why c is permitted:** both a year-to-date weekly average and a thirteen-week
weekly average express the same quantity, units per week. The lookback changes how
much history is smoothed, not what the number measures. Blocking on lookback alone
would reject every real pair of files. On two real files, all four
entity-to-benchmark pairs differed in lookback and none differed in rate
denominator; a lookback-blocking rule would have produced no output at all. See
SD-PRS-39.

**On a block: mark the pair UNPAIRED, fire the relevant question, and compute
nothing for that pair until it resolves. Do not substitute a nearby column.** See
SD-PRS-40. Enforced by gate G14.

**Item 5. Column resolution by routing.** Invoke reference/field-resolution.md Part 3.

**ROUTE BEFORE YOU MATCH.** Classify and route a column BEFORE matching any alias
against it. **Never run an alias search across the whole sheet.** Whole-sheet
substring matching is how an action-evidence flag reading "verification prompt on
every terminal" gets attributed to an entity as a volume result, and how a county
name lands in a city column. Confine every match to the columns the routing step
selected. See SD-QUA-02 and SD-QUA-07.

**Two axes, because a single label routes flags into arithmetic.** See SD-QUA-03.

    entity        a creditable entity | a benchmark population | a non-claimable
                  aggregate | none
    measure_type  rate_volume | share | count | flag | identity | date | text

**ONLY measure_type rate_volume may enter the arithmetic in items 3, 4 and 5.** A
column named for an entity but holding a marker is a flag; it is never a volume
metric.

**Resolve absences by RULE, before any value search.** Some qualifiers are
represented by an empty cell, and a value search cannot find an absence. **A
population defined by the absence of an attribute is resolved as the COMPLEMENT of a
populated field, never by searching for a word.** See SD-QUA-04.

| Concept | Resolves to |
|---|---|
| The self-determined subset | the grouping field is BLANK after null normalization |
| The managed subset | the grouping field is POPULATED, which is the complement |
| An unbenchmarked entity | no benchmark column exists for that entity |

**Searching for the word finds nothing**, because the concept is represented by an
empty cell rather than by the word, and a resolver that value-searches it falls
through and silently widens to every unit in scope. This is the most consequential
absence in this method, because the self-determined subset is the top-tier win
signal at the direct tier per 2.8.

**THE PROPER-SUBSET GUARD, which is the mirror of the resolved-but-empty rule.** An
absence rule yields a usable subset only where the complement is a PROPER,
NON-EMPTY subset. Where the grouping field is blank on EVERY row in scope, or
populated on EVERY row in scope, the distinction does not exist in this population.
Record the subset as NOT PRESENT, **skip every cut, every filter and every gate that
depends on it**, and name it in the audit. **A subset equal to the whole population
is not a cut; it is the population under a second name**, and comparing it against
itself produces a number against itself that a reader cannot detect as vacuous. The
method is careful that a resolved-but-EMPTY column is treated as absent, per
reference/field-resolution.md 3.8 and SD-PRS-18, and this is the same care applied to a
resolved-but-FULL absence rule.

**PLACEMENT NOTE, so that nobody moves this the wrong way.** This guard is GENERAL,
not specific to how this skill cuts a population. It governs any concept resolved by
absence, in any skill, at qualifier time exactly as much as at cut time: a filter
that resolves to the whole population is as wrong as a cut that does. **Its proper
home is reference/field-resolution.md 3.12, directly under the absence map it guards, with a
mechanism bullet on SD-QUA-04 so the rule and the resolver agree.** It is written out
in full here only because the shared resolver does not yet carry it, and a guard that
exists in one skill and not in the resolver produces two skills disagreeing off the
same file on the same morning. **When the shared resolver carries it, this paragraph
becomes a citation and nothing else in this section changes.** Until then, do not
delete it as local colour, and do not treat its presence here as evidence that the
guard is skill-specific.

**THE ENTITY BREADTH AND THE ITEM COUNT ARE TWO NUMBERS AND THE SEED DICTIONARY NOW
SEPARATES THEM.** Wherever this skill needs how many distinct ENTITIES a unit carries,
which is cut 4 of the direct-tier lattice in Stage 6.4, any objective phrased as
carrying more of something, and any breadth figure in a claim, **the concept is
`concept_distinct_entity_count`, which is STRICT, and its reciprocal forbidden
neighbour is `concept_item_count`.** reference/field-resolution.md carries both entries and the
reasoning; read them there. **A unit can carry three of the countable things and ONE
creditable entity**, so a column of item counts read as an entity breadth overstates
the figure on every row by a factor nobody can see in the output, and scores an
objective asking for more ENTITIES as already met. **Run the value check before either
column is used for a breadth figure**, both halves of it: against any stated average
in a supplied document, and against the other candidate's ordering. Where the two
orderings differ the header cannot settle it, and the correct outcome is to take
NEITHER, name both columns with their means, and raise it as a question. **A refusal
here is a resolved question and is reported as one, never as a failure**: publishing
the wrong one costs the reader's trust in every breadth number on the artifact, and
saying so costs one line.

**NO STEM BELONGS TO TWO CONCEPTS, AND A TIE ON A STRICT CONCEPT IS NEVER BROKEN BY
POSITION.** SD-PRS-47. Where two concepts both produce an exact match on the same
header, and either is marked strict_exact_only, **NEITHER resolves.** The header is
reported as ambiguous, both candidates are named, and every feature both feed is
skipped and named. A tie on a strict concept is never broken by column position, by
dictionary order, or by which pass happened to reach it first. The named case,
because it is the failure no downstream gate can catch: a generic status stem sits
in both the not-actionable exclusion concept and the pipeline stage concept; a file
with one column of stage values resolves to the exclusion concept, the exclusion
removes a stage, the funnel reconciles, and every invariant passes. **The only
defence is resolving the right column in the first place, and the only way to
guarantee that is to refuse to guess.**

The match cascade, confined to the routed columns: exact, then normalized-exact,
then prefix, then bidirectional substring, each pass run to completion before the
next. See SD-PRS-14. A short-string guard applies below MIN_STEM_LENGTH: only an
exact match counts. See SD-PRS-15.

**Confirm a resolved column by its VALUES, not only by its name.** See SD-PRS-16.
**A resolved but EMPTY column is an absent column.** See SD-PRS-18. **Normalize
null-like VALUES, not just empty cells**, per NULL_LIKE_VALUES. See SD-PRS-19.
**Coerce before comparing**, because a typed comparison against the wrong type fails
silently. See SD-PRS-17. **Read the scale from the column's own maximum, every
run**: at or below one it is fractional, above one it is in points. Against a
fractional column a literal threshold of 25 matches zero rows, silently. See
SD-PRS-44.

**Never silently widen.** A qualifier that matched nothing is reported, with three
outcomes that must never be collapsed: the column is absent; the column is present
and the value is not in it; the column is present and the value matched zero rows.
See SD-QUA-10, SD-QUA-11 and SD-QUA-12.

For every routed column record: the phrase, its resolved entity and measure type,
the column, the operator, and the matched value set with row counts. **This is what
makes a disputed number traceable.** See SD-QUA-14.

**Item 6. Action-evidence columns.** Any column that records a discretionary act
rather than an outcome is ACTION EVIDENCE, and four questions are mined from it.
These four generalize to a sales call, a code review, a customer check-in, a safety
inspection, a chart audit or a maintenance visit:

| Question | What it yields |
|---|---|
| COUNTS | how many were done |
| COVERAGE | what share of the eligible population was reached |
| STALENESS | how long since the last touch |
| DEPTH | how thoroughly each one was done |

Coverage is a rung 6 claim at minimum, because it carries a denominator population.
Where the eligible population resolves through BARE_DENOMINATOR_CONCEPT, use it;
where it does not, use the in-scope count after every exclusion and say so, because
that is a wider denominator and it understates the share achieved.

**A signal that lags reality is disclosed**, per RECENCY_LAG_DISCLAIMER, and is
weighted only where it is the subject. See SD-EXC-12.

**WHERE THE ACTION EVIDENCE IS IN A SECOND FILE, IT IS JOINED, NOT LEFT UNREAD.**
SD-PRS-48, and it is obeyed there in full. A file keyed on the same unit identifier
that carries the columns this stage needs is ENRICHMENT: the run joins its columns
onto the source, on that identifier, and computes the four questions above from them.
**Leaving it unread is not the conservative choice.** It is a decision to compute
coverage, staleness and depth as zero for every unit while the evidence sat in the
same input set, and nothing in the run reports that it happened, because a term that
contributed nothing looks exactly like a term that had nothing to contribute.

**A JOIN IS NOT A CONCATENATION AND THE RUN STATES WHICH IT DID.** Item 2 above joins
two files of the SAME SHAPE on a unit key to compare two periods, and adds no column.
This joins a file of a DIFFERENT SHAPE and adds no ROW. The two are never substituted
for each other. **Every one of SD-PRS-48's preconditions holds before a join is
performed, and where any of them fails the run does NOT join**: it records the file as
READ AND NOT JOINED, names the condition that failed, and names the terms that go
unevaluated as a consequence, so the cost is visible rather than invisible. The four,
in short, with the full statement in the rule: both sides resolve the same identifier
concept on the strict reading, never by position, row order or name similarity; the
key is UNIQUE on the enriching side, counted and printed, because a one-to-many join
silently multiplies rows; the key is compared as TEXT, trimmed, leading zeros intact,
per SD-SPN-06; and the join is LEFT, from the source that carries the population, so
the population is fixed before the join and is not changed by it.

**BOTH NON-MATCHING SIDES ARE REPORTED, NOT ONE.** A row in the population with no
match KEEPS ITS PLACE and the enriched columns are UNRESOLVED for it, **written blank
per SD-CTR-13, never zero and never a default**: an absent record is not evidence that
nothing was done, and a term computed over those columns is NOT SCORED for that row
and says so. An enriching row with no match is COUNTED AND NAMED, never silently
discarded, because a large unmatched remainder is the only warning the run gets that
the two files key differently or cover different scopes before it trusts a bad key.

**THE ROW COUNT BEFORE THE JOIN EQUALS THE ROW COUNT AFTER IT. ASSERT IT.** A change
in either direction is a defect and BLOCKS; it is never a result to be explained. It
is carried as a regression invariant in 7.5 so that it is re-checked at every gate
downstream and not only at the moment of the join.

**A JOIN THAT LANDS AND CANNOT BE SCORED HAS NOT ANSWERED THE FAILURE THE RULE EXISTS
FOR**, per the amended SD-PRS-48, and this is the half a run is most likely to stop
short of. The joined columns must then RESOLVE to the concepts the terms need, by the
ordinary resolution routes in reference/field-resolution.md. **Where the enriching file carries
ONE COLUMN PER MEMBER of a published set, which is the commonest shape a real evidence
file has, those columns TIE WITH EACH OTHER for the same concept by construction**, and
a uniqueness test written to refuse an ambiguous PAIR refuses the whole SET: measured,
eight columns each clearing the value check and the fill floor, none adopted, and every
term that needed them unevaluated on every row with the file joined and sitting beside
the source. The resolution rules carry a SIBLING SET route for exactly that shape and
it is taken. **The join is half the fix and the resolution is the other half, and a run
that stops at the join has MOVED the failure rather than closed it**, into a place
where the artifact looks enriched and every term still contributes nothing.

**THE ENRICHMENT IS DISCLOSED WHEREVER AN ENRICHED TERM IS USED**: the file joined,
the key used, the columns added, the MATCH RATE as matched of the population, the
unmatched count on EACH side, **and whether each joined column RESOLVED to a concept or
was carried unread**, because a joined column nothing reads is indistinguishable in the
artifact from a file that was never opened. A term whose evidence arrived by join is readable as
such, so a reader who distrusts the key can see exactly how much of the answer depends
on it. **This is the same disclosure discipline as a rung**: a figure that does not
say what it rests on cannot be checked by the person it is about.

**Item 7. Peer comparison, and the two tests that must run before it.** Resolve the
peer level from ROLE_LADDER.peer_level or PEER_SET_LEVEL_DEFAULT, then TEST the
resolution before using it.

**A STATED PEER COUNT OUTRANKS THE DERIVATION, and the run records which of the two
produced the level it used.** The interview elicits how many peers a person has far
more readily than it elicits what kind of thing a peer IS, so the common case is a
bound COUNT and an unbound LEVEL. Where that happens, take the SCOPE_LEVELS level
whose sibling count at the requester's position is closest to the stated number and
**record the level as DERIVED FROM THE COUNT**, per the PEER_SET_LEVEL_DEFAULT row
in reference/schema/ SECTION A1. The one-step-coarser derivation is the FALLBACK for
when nobody described the peer set at all; **it never overrides somebody who did.**
Precedence here is the general rule in 2.2.1 and SD-CTR-24: a documented default may
narrow what the run attempts and may never contradict a value the organization
actually bound. **Where the two disagree, the artifact names both readings and says
which it used**, because the difference between them is often the difference between
a real peer comparison and none at all. Test 1 below then applies to whichever level
was produced, by either path.

**TEST 1. Siblings, never subordinates.** SD-SPN-14. The resolved peer level must be
strictly COARSER than the requester's own resolved level, and the peer set is the
sibling units at the requester's own altitude inside that coarser level. **Walking
outward is the only permitted direction. Walking downward into the requester's own
span is forbidden.** If the resolved level is at or finer than the requester's own
level, the resolution is WRONG and is DISCARDED, never used. Then test the resolved
set for a second property: **no member of the peer set may sit inside the
requester's own scope.** A peer set that intersects the requester's own span is not
a peer set. The failure this prevents is ranking a leader against the units they
manage, which is internally consistent, meaningless, and reads to the leader as an
accusation.

**TEST 2. A role at the top of the chain has no internal peer set, and that is a
stated result.** SD-SPN-15. Where the requester's own level is the coarsest in the
chain, there is no coarser level, therefore no sibling set, therefore NO INTERNAL
PEER SET. Say so plainly. **Do not manufacture one.** Then, in order:

1. If PEER_SET_IS_EXTERNAL is true, use the published comparison group from
   EXTERNAL_PEER_SET_SOURCE, name the publication and its refresh cadence, and
   **state how stale the release is relative to this run.** A group refreshed
   annually and read quarterly is stale for three quarters of the year. An external
   peer set is a legitimate answer to "the spread across peers doing the same job"
   and is the most likely real answer at any regulated or benchmarked business. It
   is bound as a publication and a cadence and is never forced into the
   organization's own containment chain, because the chain holds only units the
   organization owns.
2. Otherwise drop rung 3 for this run, fall to the highest remaining BOUND rung per
   SD-CTR-24, and name the drop beside every affected figure. **Dropping rung 3 does
   NOT silence the classifier on a plan-attainment figure**: the rung-4 band is
   fixed in percent of target and needs no peer spread, so attainment still carries
   its label and its ON PLAN state, per 2.5. A reader at the top of the house is the
   most senior reader this skill has and is the last one who should receive an
   unlabelled headline.
3. Where no rung remains but the floor, the figures ship with a denominator
   population and no achievement wording.

**TEST 3. A peer set that EXISTS and is below EITHER floor is a THIRD state, and it
has its own procedure.** SD-SPN-16. Test 2 answers a peer set of ZERO. This test
answers a NON-EMPTY set that is below ANONYMITY_FLOOR or below
MIN_POPULATION_FOR_NORM, **which the documented fallback produces routinely and not
exceptionally**: one level coarser than a reader's own level is often a small
container, and a container holding two of them yields a peer set of one against any
floor either variable can carry. Without this test that reader gets no peer
comparison EVER, while the same file holds several directly comparable siblings one
level further out. Run it after Test 1 has passed and Test 2 has found the set
non-empty.

**TWO FLOORS GOVERN A PEER SET, THEY ANSWER DIFFERENT QUESTIONS, AND A SET CAN MEET
EITHER WITHOUT THE OTHER.** SD-SPN-16 states this and it is executed here.
ANONYMITY_FLOOR asks whether an INDIVIDUAL can be identified from the aggregate: it
is a disclosure limit, and below it nothing about the set is published at all.
MIN_POPULATION_FOR_NORM asks whether the DISTRIBUTION is large enough to derive a
band or a norm from: it is a statistical limit, and below it the set may be named and
counted but no comparison is drawn from it, per SD-POP-19 and 2.5. **Neither implies
the other, this test NAMES THE TWO CONDITIONS rather than a number, and the walk is
required to satisfy BOTH.** A stop condition naming only the anonymity floor lands
the walk on the smallest set that floor admits, the run then holds a peer set it may
name and may draw nothing from, and the LEVEL DELTA band of 2.4.1 computes and can
never fire, on any data. That is arithmetic on the two values rather than a property
of one file's population, and it is why the stop condition below names both.

The procedure:

1. **Count the sibling set at the resolved level.** Record the level and the count.
   **THE SIBLING SET EXCLUDES THE REQUESTER'S OWN UNIT, AND BOTH FLOORS ARE TESTED
   AGAINST THAT NUMBER.** A container holding N units at the requester's own altitude
   yields a peer set of N MINUS 1. **This is stated here because it decides whole
   documents and was previously stated only inside a worked example.** Measured: an
   organization with exactly five units at the reader's altitude, with both floors at
   their documented defaults. Excluding the reader the set is four, below both floors,
   the chain is exhausted and nothing about peers is published in any form; including
   the reader it is five, meets both floors exactly, and the document publishes a peer
   median, a position and a labelled level delta. **Those are two materially different
   permanent records off one file**, and the excluding reading is the one that holds:
   ANONYMITY_FLOOR asks whether an individual OTHER THAN THE READER can be identified
   from the aggregate, and a reader cannot be protected from themselves by being counted
   among the people they are being compared against. **The count printed beside every
   figure that reads the set is the excluding count**, and the artifact says so, so that
   a reader who knows how many units their organization has can reconcile it.
2. **At or above BOTH ANONYMITY_FLOOR and MIN_POPULATION_FOR_NORM, use it.** Nothing
   further in this test applies.
3. **At zero, this is Test 2 and not this test.** The two states are never read as
   each other.
4. **At one or more and below EITHER floor, STEP OUTWARD ONE LEVEL and count
   again**, and repeat. Every step stays subject to Test 1: the level stays strictly
   coarser than the reader's own, and no member of the set may sit inside the
   reader's own scope. Record every level tried and the count it yielded, not only
   the one that worked.
5. **STOP AT THE FIRST LEVEL WHOSE COUNT MEETS BOTH FLOORS.** The walk may not
   continue past it. **A walk that keeps going is a search for a flattering
   comparison rather than a lawful one**, and the stop rule is what makes the
   difference visible. **It is equally not permitted to stop SHORT of it on the
   strength of one floor alone**, which is the failure that produced a peer set the
   run could rank and could not compare, on every run and any data. Where the two
   floors are set apart, the larger of the two is what the walk is measured against;
   where they are equal, which is how they are documented, one test satisfies both
   and the walk stops in the same place.
6. **Where the chain is exhausted and no level meets both floors**, there is no
   usable internal peer set this run. Take Test 2's step 1 and step 2: the external
   comparison group if one is bound, otherwise DROP rung 3, fall to the highest
   remaining BOUND rung per SD-CTR-24, and name the drop beside every affected
   figure. A dropped rung 3 still never silences a rung-4 label, per 2.5.

**NOTHING BELOW ANONYMITY_FLOOR IS EVER PUBLISHED, IN ANY FORM.** Not a rank, not a
position, not a median, not a spread, not "one of two", and not in generalized
wording a reader can invert. In a two-member container, "the stronger of the two" and
"above the branch average" both name the other member exactly, and the fact that no
name appears in the sentence does not make it anonymous.

**AND A SET THAT MEETS ANONYMITY_FLOOR AND NOT MIN_POPULATION_FOR_NORM IS NAMED AND
COUNTED AND COMPARED AGAINST NOTHING.** The level and the count are published, the
reader's own figure is published, and no delta against that set is computed at all:
not a labelled one, and not an unlabelled raw one either, per SD-POP-19. The
withholding is stated beside the figure and names MIN_POPULATION_FOR_NORM as the
reason, because a silence there reads as "no difference". The two withholdings are
different withholdings and are never printed for each other.

**FALLING OFF THE PEER RUNG MEANS DROPPING TO A WEAKER RUNG, NEVER BUILDING A
STRONGER ONE.** A comparison drawn at a superseded level is a comparison against a
DIFFERENT peer group and is published as such: **the level actually used and the
count it yielded print beside every figure that reads it, and the derived level is
named as superseded.** It is never presented as though the reader's own derived level
produced it, and it never inherits the claim strength a same-level comparison would
have carried. The rung is still rung 3 and the claim strength is still rung 3's,
qualified; what changed is the group, and the group is stated.

**THE ARTIFACT SAYS ONE OF FOUR THINGS AND NEVER PRINTS ONE FOR ANOTHER.** These are
four different states of the world, a reader acts on each differently, and two of
them are silences for two different reasons, so each names WHICH floor it is about:

| State | What the artifact says |
|---|---|
| NO PEER SET | There is no sibling set at all, because the reader is at the coarsest level of the chain. Test 2, SD-SPN-15. |
| TOO FEW PEERS TO NAME SAFELY | Peers EXIST and nothing about them was published. Name the level, the count it yielded, ANONYMITY_FLOOR by name, and that the reason is anonymity rather than absence. Where the outward walk succeeded, name the level used instead and its count. Where it failed, say the chain was exhausted. |
| ENOUGH PEERS TO NAME, TOO FEW TO DERIVE A BAND FROM | The set was named and counted and NO comparison was drawn from it. Give the level, the count, the reader's own figure, and MIN_POPULATION_FOR_NORM by name, and say that the withheld thing is the COMPARISON and not the peer group. This is a real state, it is neither of the two either side of it, and printing one of those for it tells the reader either that their peers do not exist or that they were compared. |
| COMPARED, AND THE RESULT IS FLAT | The comparison RAN, at a named level over a named count meeting BOTH floors, and the reader sits where the figure says. **FLAT is a result, not a silence**, and it is never printed for any state above. |

**NEITHER FLOOR IS EVER LOWERED TO FIT THE SET, AND NEITHER IS SUBSTITUTED FOR THE
OTHER.** Not for one figure, not because the walk failed, not because the omission is
awkward to explain in front of the reader. Where either value is bound, that value
governs; where nothing is bound, the documented default governs; **a run never
chooses either, and a run never reads one where the other is meant.**

Only then: compute every figure for every peer, rank the person AND count how many
peers share the person's value. **The tie count is mandatory.**

**Under FLOW the peer set is sibling CONTAINERS at the resolved peer level**, with
the cohort basis stated alongside, and both tests above apply unchanged to
containers. See Part 13.

**The peer set is defined by the period-end file**, per PEER_SET_ANCHOR_PERIOD, and
every comparison runs on the same-unit intersection used for the person's own
figures. **State the peer count and the unit basis alongside every rank.** See
SD-CMP-06 and 2.13.

Below MIN_POPULATION_FOR_NORM the median is printed with its count beside it, no
comparison is drawn from it and NO DELTA AGAINST IT IS COMPUTED, labelled or not, and
the withholding is stated beside the figure. See SD-POP-19, which governs, and 2.5.
Below ANONYMITY_FLOOR peers, generalize rather than rank, and publish nothing at all.
Below MIN_POPULATION_FOR_RANKING, 4.5 applies and no ranking is emitted at all.

### The not-workable exclusion, which asks a DIFFERENT QUESTION in a review

**THE TEST IS WHETHER A COLUMN RESOLVED, NEVER WHETHER A BINDING EXISTS.** The
whole rule is settled in the UNIT_ACTIONABLE_NOW_VALUES row of reference/schema/
and nowhere else; this section executes it and does not restate it. The distinction
that decides the population is this: **an unbound binding is not the same as no
column.** A run resolves the status concept from the seed dictionary whether or not
the organization ever bound anything, so an unbound binding routinely coexists with
a perfectly good resolved column. Where a column resolves BY ANY PATH, bound or
seeded, the exclusion RUNS. Only where NO column resolves at all is there nothing
to read, and then nothing is excluded because there is no evidence, not because the
exclusion was switched off. The three guards on an unbound value list, the stage
guard, the majority guard and the naming guard, are all mandatory and are read from
that row.

**AND UNDER REVIEW THE QUESTION CHANGES, WHICH IS THIS SKILL'S CASE SPECIFICALLY.**
SD-POP-30. The exclusion is a FORWARD-LOOKING test and a retrospective is not
forward looking. The planning question is "can this be worked in the period being
planned". **The review question is "was this workable at ANY point in the period
being reviewed".**

**Why that is not a technicality.** A retrospective population is what the person
was RESPONSIBLE FOR DURING the period, not what survives at the end of it. A unit
that became unworkable in month nine was workable for eight months and the work
done on it was real work. **Applying the planning exclusion to a year-end review
deletes from somebody's own review everything they worked and then lost, and it
does so invisibly, because the unit is simply not there to be missed.** That is the
survivorship failure of a survivor-only prior file arriving from the opposite
direction: one hides what left, the other hides what was there. This skill is the
one it lands on, and the exit test in item 2 will not catch it, because the unit was
never in the population to be counted out of it.

Three cases, and each has exactly one answer:

1. **NOT WORKABLE FOR THE WHOLE PERIOD: EXCLUDE.** It was never theirs to work, and
   it is excluded because it was never in the population rather than because it left
   one. Counted and named with the rest of the exclusions.
2. **BECAME UNWORKABLE DURING THE PERIOD: INCLUDE AND MARK.** Name the transition
   date and, where it is derivable, the portion of the period the unit was workable.
   **Every rate computed over the population states whether it pro-rated**, because
   a rate over a unit that was present for part of the period is a different
   quantity from a rate over one present throughout, and a reader cannot tell which
   they are holding unless it is said.
3. **TRANSITION DATE NOT ESTABLISHABLE: INCLUDE AND DISCLOSE.** Where the count of
   such units is material to a published figure, **report that figure BOTH WAYS with
   the difference named**, per the pairing discipline in SD-CMP-09. Never choose
   silently between two populations when the choice moves a number.

**A FORWARD-LOOKING STATEMENT INSIDE A REVIEW TAKES THE PLANNING READING.** The
focus section below the submission boundary, a next-period commitment and any
objective being set for the coming window exclude on CURRENT workability, because
they are plans. **One document may legitimately hold both readings; what it may
never do is apply one of them without saying which.** The reading applied is a
property of what is being written, not of the data, and **the front panel states in
one line which reading each part used.** Enforced by gate G21.

### Comparing two periods

Where the run compares two periods, the shared rules apply in full: never infer
change from one snapshot and say nothing about trend unless asked (SD-CMP-01); make
two inputs comparable before comparing, filtering both to the same scope using each
file's own column (SD-CMP-02); a zero baseline is a new-entry case, not an infinity
(SD-CMP-03); and PERSON_ROLE_START_DATE is checked so that a prior period that
predates the person in this scope is not attributed to them.

**Which like-for-like test applies is decided by the shape**, per item 2 above and
Part 13 divergence 1.

**And under FIXED the EXIT TEST runs beside it, every time two periods are
compared.** SD-CMP-09. Overlap answers whether the prior file's units are still
here; only the exit count answers whether the prior file ever held the ones that
left. **Run it before computing retention, churn or same-unit growth**, state which
of the two zero-exit states the run believes and why, and carry the caps in item 2:
retention NOT COMPUTABLE on a survivor-only pair, survivor growth published only
beside total movement with the gap NAMED -- as a figure where both rest on the same
measure and the same basis, and in words with both bases named where they do not, per
item 2 and gate G14, which is never overridden to produce a gap -- and no ranking by
survivor growth at all.
**A pair that passes every overlap test and fails this one is the most flattering
input this skill can receive**, which is why the test is named, printed and gated
rather than left to a reconciliation habit.

**Before any one-input stop fires, test whether the population is COLD.** SD-CMP-08.
Where no in-scope unit predates the current window, or fewer than
COLD_START_MIN_PRIOR_SHARE of them do, the population is cold and the stop is
replaced by an answer, per 2.2.3: name the earliest entry date found as the
evidence, offer plan attainment and the bare denominator as the second numbers that
do exist, and emit the current state and the absolute build to date. **The one-input
stop survives unchanged for a WARM population.**

## Stage 5: Checkpoint

    PRECONDITION   any of Stages 2 through 4 producing output
    ACTION         write the incremental checkpoint per 1.2
    POSTCONDITION  the checkpoint is written with resume state current
    ON FAIL        retry once, then continue and warn that an interruption will
                   require restarting the crawl
    WAIT           none. Runs alongside Stages 2 through 4.
    STOP           never

## Stage 6: Marriage and Scoring

    PRECONDITION   reconciled mappings and computed figures, the goal ledger, and
                   the evidence ledger. On the no-data branch it operates on the
                   evidence ledger alone.
    ACTION         match each evidence item to the highest-altitude goal it
                   discharges, subject to the altitude ceiling; record the lineage
                   path; run the CONTRADICTION SWEEP of 2.12.1 over every item the
                   person themselves stated; label every paired figure per 2.5;
                   attach the counterfactual rung per 2.2; compute peer rank and
                   tie count; rank by altitude, then peer rank, then magnitude
    POSTCONDITION  every claimable figure labelled and ranked; every superlative
                   carrying a tie count; every claim carrying its unit and its
                   rung; every stated item carrying one of the three labels in
                   2.12.1 and no item carrying two of them
    ON FAIL        RETURN TO ROOT
    WAIT           none
    STOP           evidence state FULL or REPORTS AND no claimable figure from any
                   entity-benchmark pairing AND no claimable execution outcome from
                   any unbenchmarked entity. Does NOT apply on the no-data branch.

Unmatched evidence goes to the organization-contribution holding list for the
free-text sections. It is not discarded.

**THE CONTRADICTION SWEEP RUNS HERE, AND HERE IS THE EARLIEST PLACE IT CAN RUN.** It
needs the resolved columns from Stage 4 and the person's own stated items from Stage 3,
and it has to finish before Stage 7 infers an action from a statement, before Stage 8
asks a question about one, and long before Stage 9 writes one into a box. **Walk every
item the person stated in their own words** -- an account or unit named, an event
described, a figure quoted -- and label each CONTRADICTED, UNSOURCED or UNVERIFIED by
the mechanical test in 2.12.1. Record the label, the column that decided it, that
column's unit, and the question that would settle it. **A unit the person NAMES that
does not exist anywhere in the source is CONTRADICTED, not UNSOURCED**, because the
source was read and the unit was absent from it. Count the CONTRADICTED items once,
immediately after the sweep, against UNRESOLVED_STOP_COUNT per
`review.contradicted_items`. **An item this sweep did not reach is not thereby
confirmed**: an item nothing addressed is UNVERIFIED and says so.

## Stage 6.4: Win Discovery Sweep

    PRECONDITION   scored figures from Stage 6; the claim tier and span from 2.8
    ACTION         run EVERY cut the role and the data permit
    POSTCONDITION  a ranked candidate win list
    ON FAIL        record an impossible cut as unavailable and continue. Never halt.
    WAIT           none
    STOP           none. Zero candidates proceeds to the questions.

**One total number is not a performance review.** See 2.19 and SD-CLM-17.

Each candidate records six things: the cut; the creditable entity; the claimable
number with its unit named; the comparison that proves it, with its rung; the peer
rank with its tie count; and a confidence per 2.10.

### The cut lattice

The dimensions below are the general form. Bind the nouns; the cuts themselves port.

**At the DIRECT claim tier, seven cuts:**

1. **The self-determined subset as a bloc.** Resolved as the complement of a
   populated grouping field, never by a word search. Compared three ways per 2.8.
   Beating any of the three is a top-tier win and outranks an equivalent
   total-measure win.
2. **Each managed grouping as a bloc**, compared against the same grouping outside
   the person's own scope.
3. **Individual units**, ranked by contribution to each entity's movement.
4. **Breadth and depth of what was delivered.** Items carried, depth of range, gaps
   closed, target-list completion. These are direct actions and are often the cause
   behind a measure win. **Where the breadth is a count of distinct ENTITIES per unit,
   the concept is `concept_distinct_entity_count` and never `concept_item_count`**,
   which is its forbidden neighbour and holds a different number: three items of one
   entity is a breadth of one, per Stage 4 item 5 and reference/field-resolution.md. Where the
   two cannot be separated, the cut is skipped and named, not scored on the nearer
   column.
5. **Upgrades to terms, tiers or programme participation.** Elections gained,
   validation rates.
6. **Process discipline against the eligible population.** Coverage, staleness
   eliminated, completion against the population flagged.
7. **Discretionary engagement.** Events, participation, anything the person chose to
   do that nobody required.

**At the AGGREGATE claim tier, five cuts:**

1. **Whole-scope performance against the next level up.**
2. **Each top-tier account or grouping rolled**, compared to that grouping's
   performance outside the person's scope. **This is the core aggregate-tier win and
   it is usually under-claimed.**
3. **Each creditable entity rolled across the whole scope.**
4. **Team and system outcomes.** Coverage across the scope, programme adoption rate,
   breadth across a grouping, capability built, a practice installed that the team
   then ran.
5. **The distribution of performance inside the scope.** How many units improved,
   how the spread tightened. **A leader who lifted the bottom of the distribution
   has a real win that no single-unit number shows.** This cut belongs only to
   leaders and is preserved verbatim for that reason.

**NEVER emit an individual-unit claim at the aggregate tier.** See SD-SPN-10.

**Ranking:** altitude, then span-of-control strength (the self-determined subset
first at the direct tier; the account aggregate first at the aggregate tier), then
peer rank, then magnitude.

Enforced by gate G16.

## Stage 6.5: Reconstruction

    ENTER          no objectives were available from any source AND the person
                   chose reconstruction when asked
    PRECONDITION   the goal ledger and the evidence ledger both populated
    ACTION         the five steps below
    POSTCONDITION  between 1 and SYNTHESIS_MAX_OBJECTIVES candidate objectives,
                   every one flagged RECONSTRUCTED, carrying evidence citations and
                   a lineage path
    ON FAIL        if no cluster reaches SYNTHESIS_MIN_EVIDENCE, emit a single
                   objective from the person's own answer, flagged RECONSTRUCTED.
                   Never halt for lack of clusters.
    WAIT           none. The objectives are presented for edit at Question Round 1.
    STOP           none. This stage never blocks the run.

1. Cluster the evidence ledger by the goal each item discharges, using the lineage
   ladder.
2. Each cluster with at least SYNTHESIS_MIN_EVIDENCE supporting items becomes a
   candidate objective. Cap at SYNTHESIS_MAX_OBJECTIVES, and **merge the weakest
   clusters into the nearest neighbour rather than emitting one more.**
3. Write each objective in the organization's own language, at the person's
   altitude ceiling.
4. Derive measures from the quantified outcomes inside that cluster. A cluster with
   no quantified outcome yields a measure with no target, which routes to the target
   question and is marked UNGRADABLE rather than given an invented target.
5. Attach the supporting evidence citations to every objective for review.

**Most people cannot fill a blank field but can correct a draft containing their
real work.** See SD-CLM-19. Date handling is in 2.18: never silently backdate.

## Stage 7: Action Inference and Learning Synthesis

    PRECONDITION   scored figures or the evidence ledger, and action-evidence
                   columns where present
    ACTION         ACTION A, infer the winning actions; ACTION B, synthesize a
                   learning from every MISS
    POSTCONDITION  every WIN has proposed action language; every MISS has a
                   proposed learning; all of it in state PROPOSED; every
                   superlative carries a tie count
    ON FAIL        if no activity evidence correlates to a WIN, emit the result
                   without an action clause and route that win to the open
                   question; retry once with a widened evidence set; then proceed
                   without the clause. NEVER invent an action.
    WAIT           none
    STOP           none

**This stage is why the skill exists.** It runs BEFORE Question Round 1 so that its
proposals can be confirmed there.

**ACTION A, inferring the action.** Correlate the units where the measure moved
against the units carrying the relevant action-evidence marker and a logged
interaction. The general method is: correlate outcome movement against the
discretionary acts recorded in the data. The confidence attached to the result is
decided by the calibration in 2.10 and nothing else.

**ACTION B, synthesizing the learning.** For every MISS, diagnose from the data,
then propose a transferable learning that names the mechanism. See 2.16.

**The attribution check** in 2.17 runs here, where PERSON_HAS_DIRECT_REPORTS is true.

**Tie handling** in 2.13 runs here, before any superlative is written.

**The honesty constraint** in 2.10 runs here: diagnoses are candidates, never proven
cause.

## Stage 8: Question Round 1, grounded

    PRECONDITION   the crawl is complete, Stage 7 proposals are available, and
                   either the checkpoint is written or a checkpoint-unavailable
                   warning is recorded
    ACTION         open with the findings, then ask; run the interactive win review
    POSTCONDITION  every blocking question for this stage is answered, or the run
                   routes per the skip semantics in Part 6
    ON FAIL        the person does not respond, so write the checkpoint and route
                   to Stage 12.1
    WAIT           blocks on answers
    STOP           the person cancels

**Open with the finding, never with methodology, caveats or reconciliation.** Those
are internal. See SD-LNG-03.

**THE INTERACTIVE WIN REVIEW.** The Stage 6.4 candidate list is presented as a
working list the person edits, not as a finding they receive. They may ADD, MODIFY
or DROP. **Dropped wins leave the candidate list entirely and are never carried into
the closing forward-looking section as consolation.** See 2.19 and SD-CLM-18.

## Stage 9: Draft Assembly

    PRECONDITION   the proposal ledger from Stage 7 exists. IT MAY BE EMPTY.
                   Proposals in state PROPOSED, CONFIRMED or REMOVED are all valid
                   inputs. Confirmation is a Stage 10 postcondition, never a Stage
                   9 precondition.
    ACTION         assemble per the cycle-appropriate template in Part 8; compute
                   completion percentages against stated targets only; date
                   comments to the dates the work occurred
    POSTCONDITION  the cycle-specific postcondition in Part 8.2 is met
    ON FAIL        repair in place and re-verify, up to REPAIR_CYCLE_LIMIT cycles,
                   then RETURN TO ROOT
    WAIT           none
    STOP           review.review_mode_no_objectives: no objectives are available
                   from any source, including reconstruction

Assembly order follows 1.2: heaviest first, each unit finished completely before the
next, checkpointed section by section.

**ASSEMBLY PRODUCES THE FIELD BLOCKS. IT DOES NOT PRODUCE THE CONTAINER.** Each
drafted field is assembled as ONE CONTIGUOUS STRING with nothing interleaved, in the
shape 8.3 D2 requires, and carries its exact character count taken per 1.5. The
document itself is built at Stage 12. **Assembling a field as prose with its
commentary mixed through it and separating the two later is how commentary reaches a
paste**, so the separation is made at the moment the text is written and never
afterwards. Anything that is not the field's own text, the lineage line included, is
written to the region below the submission boundary at the same moment, per 1.5 and
2.20.

**Completion percentages** come only from stated targets. A measure with no target is
marked UNGRADABLE and routed. Never infer a target. See 2.12.

**Reserved placeholders.** Any field whose input is pending carries a reserved
placeholder naming what it is waiting for, so that re-assembly can replace it
deterministically.

**Reconstructed dates** are emitted as explicitly reconstructed and awaiting
confirmation. See 2.18.

## Stage 10: Question Round 2, field level

    PRECONDITION   the draft is assembled
    ACTION         ask the field-level questions from Part 6
    POSTCONDITION  every blocking question answered or routed to Stage 12.1; EVERY
                   proposal resolved to CONFIRMED or REMOVED
    ON FAIL        write the checkpoint and route to Stage 12.1. Never fabricate a
                   free-text answer, a behaviour rating, a learning or a target.
    WAIT           blocks on answers
    STOP           the person cancels

**A proposal whose question was skipped or never fired is REMOVED, not carried
forward.** See 2.11.

## Stage 10.5: Re-Assembly

    PRECONDITION   Stage 10 complete; every proposal resolved
    ACTION         fold every answer into the draft, replacing reserved
                   placeholders; STRIP every proposal in state REMOVED from the
                   COPY REGION, deleting the sentence or clause it produced;
                   delete every proposal REMOVED as REJECTED from the artifact
                   entirely; move every proposal REMOVED as UNANSWERED below the
                   submission boundary as a labelled proposal with its confidence
                   and its confirming question, per 2.20; apply any accepted
                   rewrite by re-running assembly for those measures only
    POSTCONDITION  no reserved placeholder remains for an answered question; no
                   sentence in the copy region derives from a proposal outside
                   CONFIRMED; every proposal below the boundary satisfies all
                   five conditions in 2.20
    ON FAIL        repair in place and re-verify, up to REPAIR_CYCLE_LIMIT cycles,
                   then RETURN TO ROOT
    WAIT           none
    STOP           none

A REMOVED action clause leaves the result standing on its own without an action
half. It does not leave an unconfirmed action in the copy region. Where it was
removed for want of an answer rather than by a refusal, the proposal itself survives
below the boundary as a question with its content attached, which is what the person
needs in order to answer it.

## Stage 11: Grading

    PRECONDITION   the draft is complete
    ACTION         score every measure against the bound methodology axes; flag the
                   four failure patterns automatically; propose a rewrite for every
                   failure
    POSTCONDITION  every measure scored; every UNGRADABLE one carrying a proposed
                   rewrite and a one-line reason
    ON FAIL        emit the measure unscored and note that it could not be graded.
                   Never suppress a measure because it failed grading.
    WAIT           none. Rewrites are presented with the draft at the preview;
                   accepted rewrites are applied by re-running assembly for the
                   affected measures only, then re-gating.
    STOP           none

The four failure patterns and the enforced shape are in 2.15. **Show the original,
the rewrite, and a one-line reason. Visible coaching, not silent correction.**

**An illustrative number in a rewrite is never a value.** See 2.12.

## Stage 11.5: Preview

    PRECONDITION   the draft is assembled and re-assembled; grading complete
    ACTION         show the person the full draft BEFORE the final formatted emit,
                   structured as the write-up will appear, plus a summary of what
                   changed since the win review
    POSTCONDITION  the person has seen the complete draft and responded, or has
                   explicitly declined to review
    ON FAIL        the person does not respond, so checkpoint and route to Stage
                   12.1
    WAIT           blocks on the response
    STOP           the person cancels

**Nobody should discover what their record says by reading it in the destination
system. The preview is the last cheap moment to change anything.** See SD-CNF-09.

Flag inline, for the person's attention: every claim that came from a MEDIUM or LOW
confidence inference; every superlative and its tie count; every reconstructed
objective and date; every remaining placeholder; and every figure whose
counterfactual rung is weaker than the default rung, with the rung named.

**THE PREVIEW SHOWS THE COPY REGION IN ITS FINAL BLOCK SHAPE**, per 8.3: the field
index first, then every field of FORM_FIELDS under its own heading, in that set's
order, each block showing its heading, then its text, then its count caption
carrying the count and the limit, which is the order the built document uses. It is shown as TEXT rather than as the built
document, because the document is built at Stage 12 after the greenlight and nobody
should be asked to approve a container instead of the words inside it. **The counts
shown here are the counts of the previewed strings.** They are RECOUNTED from the
built document at Stage 12 per 7.6, and a count that moves between the two is itself
the change and is reported rather than quietly overwritten.

## Stage 12: Greenlight and Emit

    PRECONDITION   every gate in Part 7 returns PASS or NOT APPLICABLE
    ACTION         BUILD the artifact in the medium PART 8 declares; VERIFY it by
                   reading the BUILT artifact back, per 7.6; emit the
                   cycle-appropriate blocks with their character counts and their
                   limits; then offer the out
    POSTCONDITION  blocks emitted, character sweep passed, the document
                   verification in 7.6 returned PASS on every assertion or the run
                   took a named rung of 8.6 and said which, checkpoint deleted
    ON FAIL        route per 7.3 to a stage that can REMEDIATE the failure
    WAIT           the greenlight
    STOP           PER_GATE_FAILURE_LIMIT failed returns on one gate, which routes
                   to Stage 12.1

**Offer the out.** "Anything here you would remove or soften?" That question matters.
People will not submit something that overstates them, and without an easy way to
dial back they abandon the whole draft rather than edit it. See SD-CNF-09.

**Do not send or share the artifact automatically.** See SD-CTR-18.

**Nothing is published on the strength of the build intention.** The counts, the
blocks, the index and the boundary are asserted against the document that actually
exists, per 7.6 and reference/output-contract.md PART 7.1. A verification that cannot run has
FAILED, and the run falls to the rung 8.6 names rather than publishing a document
nobody checked.

**The reply is short and never pastes the list**, per CHAT_REPLY_MAX_LINES. See
SD-CTR-16.

## Stage 12.1: Incomplete Emit Path

    ENTERED FROM   Stage 8 ON FAIL, Stage 10 ON FAIL, Stage 11.5 ON FAIL, a
                   per-gate triple failure, or the global remediation budget
                   exhausted
    ACTION         emit the cycle-appropriate blocks, resolving every unanswered
                   blocking question BY ITS CLASS, per 6.3:
                   CONSTRAINT, so write the field to its documented default shape,
                   ship the content, and name the departure and the question that
                   resolves it;
                   CONTENT, so put INCOMPLETE_PLACEHOLDER_TEXT in the fields that
                   question feeds, and in no others.
                   Then carry every proposal REMOVED as UNANSWERED below the
                   submission boundary as a labelled proposal with its confidence
                   and its question, per 2.20
    POSTCONDITION  the output carries INCOMPLETE_BANNER_TEXT, in the form its own
                   row selects for what is actually missing, with a named list of
                   what is outstanding and which question resolves each, with the
                   constraint departures and the content placeholders listed
                   separately, because they are two different kinds of gap and a
                   reader acts on them differently
    EXEMPTIONS     fields carrying the placeholder are exempt from the gates that
                   inspect field content: G5, G6 and G13
    CHECKPOINT     RETAINED, not deleted

**Never present an incomplete draft as finished.** A bannered partial that names what
is outstanding is worth far more than nothing after a long crawl. A labelled partial
that looks finished is still a partial. See SD-EFF-04 and SD-EFF-05.

**WHICH BANNER, AND THE CHECK THAT DECIDES IT ALREADY RUNS.** INCOMPLETE_BANNER_TEXT
carries TWO documented defaults rather than one, and they are selected by the
EMPTY-DOCUMENT CHECK below, which runs on this path before anything is emitted.
**Where ANY drafted field carries INCOMPLETE_PLACEHOLDER_TEXT, the banner is the form
that says the document must not be submitted.** Where NO drafted field carries it,
which is the ordinary case when the banner fires because a preview could not run or a
win list was never reviewed, **the banner is the form that says the document must be
READ before it is submitted.** Read the wording of each from that variable's own row
in reference/schema/, which is the only statement of it; where the binding owner bound
a single string, that string is used for both cases and the run says so.

**WHY THE SELECTION IS PART OF THE RULE AND NOT A REFINEMENT OF IT.** One literal
served both cases, so a run whose only fault was an unrunnable preview opened with a
DO NOT SUBMIT banner in the title band and then, in the very next paragraph the same
rule mandates, told the reader that every field carried real content, that nothing was
a placeholder, and that they should read it, correct it and submit it. **The banner
and the paragraph beneath it said opposite things and the banner was the one at title
size.** Both forms are equally unmissable, in the same band at the same prominence,
both still say the document is not finished, and each is removed only by the reader
doing the thing it names. **Neither form is softened, and neither is chosen by
judgment**: the check decides it.

**AND THE ORDER AGAINST THE TITLE BAND IS DECIDED HERE, ONCE, BECAUSE TWO RULES WANTED
THE SAME LINE.** This stage requires the banner at the very top and 8.3 requires the
title band to carry the REVIEW entry of DELIVERABLE_NAME, and only one of them can be
the first paragraph. **THE TITLE BAND IS FIRST AND THE BANNER IS SECOND, IMMEDIATELY
BELOW IT, SO THE DOCUMENT IS NAMED BEFORE IT IS QUALIFIED.** A document whose first
line is a warning and whose second is its own name reads as a warning about nothing,
and a permanent-record artifact that does not say what it is in its first line is
harder to file, harder to search and harder to hand to somebody. **Nothing about the
banner's prominence changes**: it is in the title band's own styling, at the same size,
immediately under the name, above the front panel, above the field index and above
every disclosure, and it is still REPEATED once immediately above
SUBMISSION_BOUNDARY_BANNER. **Two paragraphs is not scrolling**, and no reader who
opens the file can reach any content without passing it. Item 1 of the panel order in
8.3 is read with this paragraph: the banner is still not one of the panel's lines, and
it still keeps its full form where it sits.

**WHERE THE INCOMPLETE BANNER GOES IN THE DOCUMENT, AND WHY IT IS UNMISSABLE.**
The selected form of INCOMPLETE_BANNER_TEXT sits **IMMEDIATELY BELOW THE TITLE BAND
AND ABOVE EVERY OTHER CONTENT IN THE ARTIFACT**, above the front panel and above the
field index, carrying the title-band styling D6 names rather than body
text, and it is REPEATED ONCE immediately above SUBMISSION_BOUNDARY_BANNER so that a
reader who scrolled straight to the copy region meets it before the first block they
would paste. It is never a footnote, never a trailing note and never only in the
reply. **It is not inside any field block**, so it is not selectable as part of a
block's text and cannot travel into the destination system with a paste, per 8.3 D2
and D5. Every field carrying INCOMPLETE_PLACEHOLDER_TEXT is named in the banner's
list, and its block still carries a count, which is the count of the PLACEHOLDER
rather than of the missing content and says so on the block.

**The banner survives every rung of 8.6.** Where the run fell to structured markdown
it is the first line of the document and is repeated above the boundary banner in the
same way. The container is never the reason a reader could not tell a partial from a
finished one.

**NO CONSTRAINT QUESTION EVER EMPTIES A FIELD ON THIS PATH.** SD-EFF-04 says never
present an incomplete draft as finished; it does not say make the draft incomplete.
An unanswered field limit, an unconfirmed window, an unresolved scale factor, an
unrun preview and an unreviewed win list are all constraints: each has a documented
default shape, each is written to it, each departure is named, and **every field that
had content still carries it.** The placeholder belongs only where a CONTENT question
went unanswered and the document genuinely cannot state the thing. A run that empties
a review over a formatting question has converted a recoverable gap into a lost one,
which is the inversion this whole path exists to prevent.

**AND THE GUARD IS NOT ONLY ON THE CONSTRAINT SIDE.** The same inversion arrives
through the CONTENT door whenever a question is classed CONTENT that the test in 6.3
calls CONSTRAINT, and every sentence of the paragraph above is scoped to constraint
questions, so none of them fires. **Two things run on this path, in this order,
before anything is emitted:**

1. **RE-APPLY THE 6.3 TEST to every blocking question that went unanswered**, whatever
   class the bank gave it, and resolve by the test's answer where the two disagree,
   recording the departure. The bank's column is a convenience; the test is the rule.
2. **RUN THE EMPTY-DOCUMENT CHECK in 6.3.** Where every drafted field would carry the
   placeholder and the evidence ledger is not empty, that is a classification defect
   until proved otherwise, and it is proved otherwise only by working every emptying
   question through the test again. Where it survives that, the banner says in plain
   words that the evidence ledger held content and names every question that could
   not be asked to place it.

**A REVIEW WITH A PLACEHOLDER IN EVERY BLOCK IS NOT AN INCOMPLETE DELIVERABLE, IT IS
A FAILED RUN, AND IT IS REPORTED AS ONE** in the banner, in METHOD and in the first
line of the reply. The person who receives it must not have to open eight blocks to
discover there is nothing in any of them.

**A run that could not ask its questions at all is the run the proposal permission in
2.20 exists for.** Every field in the copy region still carries its placeholder and
nothing invented reaches it. Below the boundary, the proposals the run formed are
printed as proposals beside the questions that would confirm them, so the person
sees what the method found and answers it, rather than receiving a placeholder where
their own words would have gone.

---

# PART 6: THE QUESTION BANK AND GATING

QUESTION_BANK is a bound taxonomy. The standing bank is below and is used wherever
the bank is unbound. **Row order is load bearing: it is the tie-break when weights
are equal.** Batch composition is never left to judgment.

## 6.1 The bank

| ID | Trigger | Weight | Blocking | Stage | Class |
|---|---|---|---|---|---|
| Q-LIMITS | always, before drafting | 10 | YES | 8 | CONSTRAINT |
| Q-SCOPE | scope not inferable | 10 | YES | 0 | CONTENT |
| Q-DATA | period uncertain or mismatched | 10 | YES | 4 | CONTENT |
| Q-OBJ | review mode and no objectives from any source | 10 | YES | 0 | CONTENT |
| Q-PERIOD | period ambiguous | 9 | YES | 0 | CONSTRAINT |
| Q-UNIT | a small unit drift factor detected | 10 | YES | 4 | CONSTRAINT |
| Q-STATUS | review mode, per objective set, and only where the assembled template contains a section it feeds | 9 | YES | 10 | CONTENT |
| Q-LEARN | a closing position, and only where the assembled template contains a section it feeds | 9 | YES | 10 | CONTENT |
| Q-BEHAVIOUR | a closing position, where a behaviour framework is bound, and only where the assembled template contains a section it feeds | 9 | YES | 10 | CONTENT |
| Q-TARGET | any measure with no stated target | 9 | YES | 8 at SET, 10 in review | CONTENT |
| Q-UNDOC | always, after the crawl | 8 | no | 8 | CONTENT |
| Q-DEV | SET or a closing position | 8 | no | 10 | CONTENT |
| Q-ACTION | any WIN with an inferred action at HIGH or MEDIUM confidence | 9 | YES | 8 | CONTENT |
| Q-CAUSE | any WIN with LOW confidence on the action | 9 | YES | 8 | CONTENT |
| Q-ANOM | a material anomaly, capped at ANOMALY_QUESTION_CAP | 7 | no | 8 | CONTENT |
| Q-CHALLENGE | a closing position | 7 | no | 10 | CONTENT |
| Q-PRIORITY | more than HEADLINE_CANDIDATE_THRESHOLD headline candidates | 6 | no | 8 | CONSTRAINT |
| Q-INCLUSION | a closing position, all roles, and only where the assembled template contains a section it feeds | 9 | YES for people leaders, no otherwise | 10 | CONTENT |
| Q-WINS | always, after win discovery | 9 | YES | 8 | CONSTRAINT |
| Q-PREVIEW | always, before emit | 9 | YES | 11.5 | CONSTRAINT |
| Q-SOFTEN | always, final | 5 | no | 12 | CONSTRAINT |

**Whether a question blocks is read from the Blocking column of the bank in force,
and no count of the bank is stated here**, because QUESTION_BANK is bindable and a
count in prose goes stale the moment an organization adds a row. Q-INCLUSION is the
one conditional entry: blocking for a person with direct reports, non-blocking
otherwise. Weights run from 5 to 10 and the arithmetic in 6.2 reads them from the
bank rather than from this paragraph.

**A QUESTION WHOSE ANSWER HAS NO HOME DOES NOT FIRE.** Four rows carry the clause
"only where the assembled template contains a section it feeds", and the clause is
the same rule in all four: Q-STATUS, Q-BEHAVIOUR, Q-INCLUSION and Q-LEARN. **A
blocking question that feeds no section of the assembled template can neither be
answered into anything nor empty anything**, so a run that fires it puts a person in
front of a question with no destination, and a run that routes to Stage 12.1 over it
has stopped a complete document on a gap that does not exist. **The test is run
against the ASSEMBLED template**, which is FORM_SECTIONS filtered by
FORM_SECTIONS_BY_CYCLE_POSITION for the position in force, not against the bank and
not against what the destination form might carry. Where the section is present, the
question fires and blocks exactly as written. Where it is absent, the question is
recorded as NOT FIRED with the reason, in METHOD, so that a reader can tell a
question that was skipped from one that was never applicable.

**Q-WINS IS CLASSED CONSTRAINT, AND THE CLASSIFICATION IS LOAD BEARING.** It is the
one row a reader is most likely to think is misfiled, so the reasoning is stated
here rather than left to the test in 6.3. Q-WINS presents the discovered candidate
win list and lets the person ADD to it, MODIFY an entry or DROP one. **It supplies no
fact the document cannot state**: every candidate on that list was discovered from
the person's own data at Stage 6.4, already carries its own evidence, its rung and
its confidence, and is already subject to every gate. What the question governs is
which of those findings are kept and in what order they run, which is SHAPE. **Its
non-answer therefore takes the documented default shape and never empties a field.**
Classing it CONTENT emptied all eight blocks of a review that had everything it
needed to say, on any run with no channel to ask, which is the failure regression
case 18 exists to prevent arriving through the other door.

Review mode means the cycle position is any of TRACK, MIDPOINT or CLOSE. A closing
position means MIDPOINT or CLOSE.

## 6.2 Budget and precedence

Blocking questions are requirements, not preferences.

    Step 1  Fire every BLOCKING question whose trigger is met AND whose stage is
            the current stage.
    Step 2  Count them. Call that B.
    Step 3  The non-blocking budget for the round is
            max(0, QUESTION_BATCH_MAX minus B), filled by weight.

**Never present more than QUESTION_BATCH_MAX questions at one time.** When more than
that are outstanding, ask in weight order, highest first, in successive batches
within the same stage. **A wall of questions is abandonment.** See SD-IDN-22.

**A composite question is ONE question.** The questions in COMPOSITE_QUESTION_IDS are
each presented as a single grid covering every objective, every behaviour or every
ungradable measure. Each counts as 1 toward B, not as N. The standing composite set
is Q-STATUS, Q-BEHAVIOUR, Q-TARGET, Q-INCLUSION, Q-ACTION and Q-LEARN. See
SD-IDN-23.

**A question that is the sole input to a required section is EXEMPT from the
non-blocking budget and always fires.** FORM_REQUIRED_EXEMPT_QUESTIONS holds them,
and each entry names the section it feeds. In the standing bank at a closing
position, Q-CHALLENGE and Q-DEV are exempt, because each is the sole input to a
section of the bound form and neither may be dropped by arithmetic. See SD-IDN-24.

**Tie-breaking.** Where several questions share a weight, order them by their
position in the table above, top first.

**Sequencing.** A question never fires before the stage that supplies its context.
The stage column is authoritative. See SD-IDN-25.

## 6.3 Skip semantics

**NON-BLOCKING questions are freely skippable. An empty answer means skip, never
cancel.**

**BLOCKING questions are NOT skippable in the sense of being ignorable.** If the
person declines or does not answer, the run terminates through the incomplete emit
path in Stage 12.1. The skill never fabricates the missing value and never silently
proceeds as if the question had been answered.

**This distinction is the difference between a person choosing to leave a field
blank and the skill inventing content for a permanent record.** See SD-IDN-21.

### CONSTRAINT and CONTENT, and why a blocking question is not one kind of thing

**Every question in the bank carries a CLASS, and the class decides what its
non-answer does.** The two are not interchangeable and treating them alike is how a
single unanswered formatting question empties a document that had everything it
needed to say.

    CONSTRAINT   The question governs the SHAPE of an answer: how long a field may
                 be, which window it covers, what scale a figure is in, what order
                 the findings run in, whether the person wants anything softened.
                 It never supplies a fact about the period.
    CONTENT      The question supplies something the document CANNOT STATE without
                 it: what the person did, what their status was, what they learned,
                 which candidate wins they keep, what the scope is, what the data
                 covers.

**Where a bound QUESTION_BANK carries no class for a question, classify it by the
test above before the question fires, and record the classification with the
answer.** The test is one question: does a non-answer leave the document unable to
STATE something, or only unable to SHAPE something? Unknown is not CONSTRAINT: a
question that cannot be classified is treated as CONTENT, because that is the
fail-closed direction, per governing rule G2.

**AND WHERE A BOUND BANK'S CLASS CONTRADICTS THE TEST, THE TEST GOVERNS AND THE
BINDING IS A DEFECT.** Apply the test to every blocking question before the round
fires, not only to the unclassified ones. Where the answer disagrees with the bank's
own column, **use the test's answer, record the departure with both classifications
and the reasoning, name it in METHOD, and queue the correction to
BINDING_OWNER_NAME.** A class column is a convenience; the test is the rule that
makes the class mean anything, and a mislabelled row is exactly how a document with
everything it needed to say gets emptied by a question about how to arrange it.

**FAIL-CLOSED IS NOT SYMMETRIC HERE, AND THE ASYMMETRY IS DELIBERATE.** Treating an
unclassifiable question as CONTENT is fail-closed because the risk it guards is
FABRICATION. Treating a question the test calls CONSTRAINT as CONTENT because a
column says so is not fail-closed at all: it destroys a true document to protect
against a risk that is not present. **Fail closed against inventing; never fail
closed against stating what the data already says.**

**The rule, and it is the whole of the fix:**

- **An unanswered CONSTRAINT question is written to its DOCUMENTED DEFAULT SHAPE,
  and the departure is NAMED.** The content still ships. The default shape comes
  from the variable's own row in reference/schema/, never from a guess, and the
  artifact says which default was used, what it would have used instead, and which
  question resolves it. **A constraint question may NEVER empty a field that has
  content.** A question about how long a field may be is not a question about what
  happened, and a run that answers the first with a placeholder in the second has
  destroyed a document to protect a margin.
- **An unanswered CONTENT question leaves its field as a placeholder, and that
  field genuinely cannot ship.** This is the failsafe in 2.12 and it is untouched:
  the skill never invents a status, a learning, a rating, a target or an action.
- **A CONTENT question empties ONLY the fields it feeds.** It never propagates. A
  missing status on objective three does not blank objective three's measures, its
  figures, its lineage or any other objective, and a missing completion percentage
  leaves the measure standing and marked UNGRADABLE with its rewrite, per 2.12.
- **Where a blocking question's non-answer is governed by a named hard gate in
  7.4**, the gate's own behaviour governs and the run stops there rather than
  reaching Stage 12.1. Scope and data coverage are the two: a document about the
  wrong scope or the wrong period is not a partial document, it is a wrong one.
- **A question that feeds no section of the assembled template does not fire at
  all**, per 6.1, and therefore has nothing to default and nothing to empty. It is
  recorded as NOT FIRED with its reason rather than routed to Stage 12.1.

**THE DOCUMENTED DEFAULT SHAPE OF AN UNANSWERED Q-WINS, STATED EXPLICITLY BECAUSE IT
IS THE ONE CONSTRAINT DEFAULT THAT COULD BE MISREAD AS PERMISSION TO WRITE.** Where
the win review cannot be run, the candidate list ships **EXACTLY AS WIN DISCOVERY
PRODUCED IT** and in the order the discovery sweep produced it:

1. **Nothing is added.** Not a win the data did not yield, not an inferred
   achievement, not a rounded-up version of one that was yielded. **Q-WINS going
   unanswered is not a licence to invent the person's year**, and the whole of 2.12,
   SD-CNF-06, SD-CNF-07 and SD-CNF-08 is untouched by this default.
2. **Nothing is promoted.** No candidate is moved up the order to make a better
   opening, because the ORDER is the part the person was going to decide and a run
   that decides it has answered the question on their behalf.
3. **Nothing is dropped**, per SD-CLM-18: dropping is the person's act, and a run
   that quietly prunes a finding has edited their record for them.
4. **Every action clause on every candidate is still governed by the proposal state
   machine.** An inferred action that never reached CONFIRMED is still stripped from
   the copy region and still appears below the boundary as a labelled proposal with
   its confidence and its question, per 2.11, 2.20 and gate G15. **The result stands
   without its action half rather than the finding disappearing.**
5. **The departure is NAMED**: the artifact says once that the win list was not
   reviewed by the person, that it is the discovered list unedited, and which
   question resolves it. The list is content the data already supports; the review of
   it is shape.

**THE EMPTY-DOCUMENT CHECK, WHICH RUNS BEFORE ANY INCOMPLETE EMIT.** After resolving
every unanswered blocking question by its class, and before Stage 12.1 emits
anything: **count the drafted fields that would carry INCOMPLETE_PLACEHOLDER_TEXT.
Where that count is EVERY drafted field, and the evidence ledger is not empty, STOP
AND RE-APPLY THE TEST IN THIS SECTION to every question that emptied a field.** A run
holding a full evidence ledger that can state nothing has almost certainly
misclassified a question, and the classification is the cheap thing to fix. Where the
re-application changes nothing and every field is still empty, the run says so in the
banner in those words: that the evidence ledger held content and the questions that
would have placed it could not be asked, and it names each one. **A review with a
placeholder in every block is a failure state to be reported as one, never a
deliverable to be emitted quietly**, and this check is what makes the difference
visible to the run itself rather than only to the person reading it.

**The worked case, because it is the one that produced this rule.** The field limit
question is CONSTRAINT. Where it goes unanswered, FIELD_LIMITS supplies the standing
defaults, every field is written to TARGET_FILL_RATIO of that default and carries
its exact character count, and the artifact says once that the limits were not
confirmed and where the person can read the real ones in five seconds. **Every
objective, every measure and every free-text section that had content still ships.**
Reading the blocking rule literally in the other direction puts the placeholder into
every capped field and emits an empty review, which is the one outcome worse than
asking again.

## 6.4 How every question is asked

- **Never ask what the tools can answer.** See SD-IDN-20 and SD-IDN-12.
- **Every question is answerable in under thirty seconds.**
- **Every question carries its findings.** A question with no context attached is a
  demand; a question with the finding attached is a review.
- **Ask only for REQUIRED concepts; never ask for optional ones.** See SD-IDN-18.
- **Offer the distinct values present**, each labelled with something a person
  recognizes and a count beside it, and accept a name or a list position rather than
  only a code. ASK_LANGUAGE_RULE must be true. See SD-IDN-13.
- **When a term matched no value, offer the nearest MISS_SUGGESTION_COUNT values**,
  ranked by ascending normalized edit distance with an alphabetical tie-break, so
  the same miss always returns the same list.
- Use structured question presentation rather than loose prose wherever the
  environment supports it.

## 6.5 The questions that carry the doctrine

The questions below are not ordinary questions and their wording is specified,
because each is the sole guard on a failure the rest of the method cannot catch.
**No count of them is stated here**, for the reason every other count in this file is
left to derive itself.

**Q-LIMITS**, before drafting: ask what the character limit is on the objective box
and on each measure; say that the counter is usually right next to the field on the
open form; and say what will be targeted if the person is not sure. Blocking,
because a wrong limit means truncated text in a permanent record. Cheap to answer,
and it removes the largest formatting risk in the run. **It is a CONSTRAINT
question, and its non-answer never empties a field**: the standing defaults are
used, every field carries its exact count, and the artifact says once that the
limits were not confirmed. See 6.3.

**Q-TARGET**, per ungradable measure: every row offers the option "no target was set
for this". **Choosing it keeps the measure UNGRADABLE, which is honest and
acceptable**, and routes it to grading for a rewrite that will be gradable next
period. NEVER invent a retrospective target to manufacture completion math on an
objective that never carried one.

**Q-CAUSE**, on a LOW-confidence action: an open question, **never accompanied by a
guess.** State the result, state plainly that the data does not say what drove it,
and ask what the person did.

**Q-WINS**, after win discovery: present the discovered candidate list in full, each
candidate with its evidence, its rung and its confidence, and ask the person to add
anything the data could not see, modify anything stated wrongly, and drop anything
they do not want in their record. **Drop means drop**, per SD-CLM-18: a dropped
candidate is gone, is not argued with, and does not reappear below the boundary.
**It is a CONSTRAINT question and its non-answer never empties a field**: the
discovered list ships unedited under the default in 6.3, nothing is added, promoted
or pruned, and the departure is named once. **The question exists because
under-finding wins is the most common failure of this method** (2.19, SD-CLM-17) and
the person is the only source for a win that left no trace in any file; it does not
exist to license the run to supply one.

---

# PART 7: VERIFICATION GATES

## 7.1 Gate states

**Every gate resolves to PASS, FAIL or NOT APPLICABLE. NOT APPLICABLE is a passing
state and never blocks emit.** See SD-EFF-37.

    NO-DATA BRANCH active (4.2)   G4, G7, G9, G10, G12 and G14 are NOT APPLICABLE
    Cycle position SET            G5 is NOT APPLICABLE, because no results exist
                                  yet. Validate targets and dates instead.
    Cycle position TRACK          G6 applies only to comment text
    No superlative in the output  G12 is NOT APPLICABLE
    No behaviour framework bound  the behaviour section is not drafted at all,
                                  and is named as not drafted
    Population is COLD (2.2.3)    G19 is satisfied by the cold-start disclosure
                                  rather than by a ground movement figure, and
                                  G20 replaces it as the operative test
    Population mode is FLOW       the join-overlap member of HARD_GATES is NOT
                                  APPLICABLE and is recorded with that reason,
                                  per Part 13 divergence 1 and 7.4 C4, and G23 is
                                  NOT APPLICABLE for the same reason, because the
                                  cohort test already measures the exit side
    One period only, no pair      G23 is NOT APPLICABLE and is recorded with that
                                  reason. It is never satisfied by a comparison
                                  that was drawn without running it.
    Population below              G21 suppresses rank rather than failing, and
    MIN_POPULATION_FOR_RANKING    the suppression itself is what G21 tests
    Self-determined subset        G16's subset half is NOT APPLICABLE where the
    NOT PRESENT                   subset resolved to the whole population or to
                                  none of it, per Stage 4 item 5

**Why the matrix exists.** Without it, the no-data path and the objective-setting
path can never emit: they skip the stages whose output those gates inspect, then
fail gates that route back to the skipped stages, then exhaust the budget and die.
**That path is the product and must never be blocked by a gate inspecting an
artifact it does not produce.**

**Unknown is never PASS.** A gate that cannot be evaluated at all, as distinct from
one that does not apply, is a FAIL. See governing rule G2 and SD-EFF-03.

## 7.2 The gates

| Gate | Name | What it tests |
|---|---|---|
| G1 | CLAIM SUBJECT AND BASIS | Applies to every QUANTITATIVE claim, and has two halves. (a) The MEASURED ENTITY of the result clause is either a creditable entity from CREDITABLE_ENTITIES, or a named execution population inside the person's scope explicitly attached to a creditable entity or a named initiative. **Test the entity the number describes, not the grammatical subject. APPLY THIS TEST PER NUMBER, not per sentence:** a sentence carrying two numbers with two different measured entities is tested twice and fails if either fails. Action-first phrasing is house style and must not be penalized. (b) **Every quantitative claim carries a counterfactual denominator from the ladder in 2.2, and names which rung it used.** A rank satisfies (b) only in the case defined in 2.2.2. An execution claim satisfies (b) by carrying a denominator population. A narrative claim on the no-data branch carrying no number is exempt from G1 entirely and is listed in the verification section. **A sentence whose measured entity is a benchmark, however well benchmarked, FAILS this gate.** |
| G2 | TRACEABILITY | Every number traces to a cell or a tool result. **A number that traces to neither does not become a bracketed placeholder inside the field block, because D2 forbids a bracketed aside there and there is no compliant place for one.** It resolves per reference/output-contract.md PART 3.4, which is the placeholder's only home: the CLAIM ships in the copy region WITHOUT the number, in the person's own words; the NUMBER goes below SUBMISSION_BOUNDARY_BANNER as a bracketed placeholder carrying the figure as stated, who or what stated it, and the question that would source it; and the two are linked by the field's own heading so a reader who sources it knows which box to put it back into. **Fails where an untraceable number appears in the copy region in any form, and fails where such a number was silently dropped instead of being carried below the boundary.** |
| G3 | ALTITUDE | No claim exceeds the person's scope or their altitude ceiling. Tests the CONTRIBUTION_VERBS and OWNERSHIP_VERBS lists per 2.7. |
| G4 | UNIT DRIFT | The unit drift test ran, with its dispersion evidence, before any comparison was computed. |
| G5 | GRADABILITY | Every measure carries either a completion percentage of 0 or greater naming its target, OR an explicit UNGRADABLE flag with a proposed rewrite. **Values above 100 are legitimate and are stated as achieved-over-target, never clipped.** |
| G6 | FIELD LIMITS | Every emitted field carries its exact character count, and every count is at or under the confirmed limit for that field. No field was written long on the assumption that the person will trim it. Where a field exceeded its limit, COMPRESSION_ORDER was applied and the field either fits or the objective was split. **A truncated field reaching the destination system is the failure this gate exists to prevent.** This gate runs on the DRAFT. Its built-artifact twin is V3 in 7.6, which recounts every block from the published document and stops on `review.field_block_over_limit`, because compression, an accepted rewrite and a folded answer all change the string after this gate has seen it. |
| G7 | BENCHMARK VISIBILITY | Every benchmark present in the data appears somewhere in the output. A benchmark with a CONFIRMED figure appears in the body. A benchmark whose figure is UNRESOLVED or UNPAIRED appears ONLY in the verification section and never in the body. Both placements satisfy this gate. **Nothing is dropped for being unflattering.** |
| G8 | THIRD PARTIES | **A third party is a NATURAL PERSON other than the writer, per 2.13.** No named third party in any text this skill authors: not in a claim, a proof clause, a narrative section, an example, a comment or the verification list, and not only peers. Positional language only. **An ORGANIZATION is not a third party for this gate** and passes wherever the organization's own published sources name it and the name is what makes the claim checkable; it is still bound by NON_CLAIMABLE_ENTITIES for CREDIT, which is a different test. **The contact line required by SD-CTR-19 and carried by MSG_AUTHOR_LINE passes**, naming the binding owner's role, or their name where the bound line requires it. Also fails on INDIRECT identification. Below ANONYMITY_FLOOR peers, generalize rather than rank. **The single exemption is an IDENTITY FIELD of the bound form**, which is a value the form requires rather than a claim: a supervisor, reviewer or approver named there PASSES, and the same person named anywhere else FAILS. The exemption never widens beyond the section FORM_SECTIONS carries as pre-filled rather than drafted. See 2.13. |
| G9 | MAPPING | Mapping reconciliation is complete; UNRESOLVED items are excluded from every claim and are listed in the verification section. |
| G10 | PERIOD | Period validation passed, or was explicitly confirmed by the person. **And the impossible-period test in Stage 4 ran**: where the resolved period's end postdates the run date, fails unless both dates are named together on the front panel, every figure drawn from that source is marked provisional on the discrepancy, **and every claim in the COPY REGION whose figure comes from that source says inside its own block, in the person's own register, that the period is not yet complete and what the figure is as at the run date**. The panel does not travel into the destination system and a disclosure only the panel carries is a disclosure the permanent record does not carry. See Stage 4 period validation item 6. A resolved period that merely covers the period being written about does not satisfy this gate on its own. |
| G11 | CHARACTER SET | The character sweep passed on all authored text, tested on BOTH bounds of ALLOWED_CHARACTER_RANGE **and against its exception list, which carries code point 10**. A line feed inside the text of a capped free-text field PASSES and is counted as one character toward that field's limit, per 1.5. A line feed in a heading, a filename, a column header, an identifier, a code or any single-line label FAILS. A carriage return is normalised before the sweep rather than failed by it, per 10.1. **A sweep that reads the range and not the list fails a document the field-limit rule required**, and that is the defect this row names. |
| G12 | TIE COUNT | Every superlative carries a verified tie count. |
| G13 | UNIT NAMING | Every emitted numeric claim names its unit per 2.4 and 2.4.1: share points, percentage points of growth, **percentage points of the named measure's own rate**, percent of target, percent, a count, or a currency. **A bare word points fails**, and so does "percentage points" with no measure named where the quantity is a level delta. **And every labelled figure names the band it was classified against and that band's unit**, read from DEADBAND by RUNG and by QUANTITY FORM: a figure labelled against a movement band while carrying a level delta, or the reverse, FAILS. **PLACEMENT IS PART OF THIS GATE, per 8.3 D5 and 10.2.1: the UNIT is inside the block in the person's own words, and the BAND, its unit and the quantity form are below the boundary.** Fails a field block carrying a classifier token, a band name, a deadband, a quantity-form name or a rung key, because all of those are the method's vocabulary and none of them is what a person writes in a self-assessment box; and fails a run in which the band and its unit appear nowhere at all, because moving them below the boundary is not dropping them. Read back from the BUILT artifact at Stage 12, so a rewrite folded in at Stage 10.5 cannot put them back. |
| G14 | RATE AND UNIT COMPATIBILITY | No growth, share or delta was computed across differing rate denominators, or across differing units without a validated recorded normalization. A differing lookback is permitted and is recorded as a run-rate comparison. |
| G15 | PROPOSAL CONFIRMATION | **Scoped to the COPY REGION.** No sentence inside the copy region, above SUBMISSION_BOUNDARY_BANNER, derives from an inferred action or a synthesized learning outside state CONFIRMED. Also fails if any reserved placeholder survives for a question the person answered. **Below the boundary the gate tests the five conditions in 2.20 instead**, and fails on any of them: a proposal inside a copy block or under a form heading; a proposal not labelled as a proposal; a proposal printed without the question that would confirm it; a proposal printed without its confidence; or any proposal REMOVED as REJECTED appearing anywhere at all. |
| G16 | SPAN OF CONTROL | Every claim matches the person's claim tier per 2.8. Also fails if a direct-tier person's write-up contains no analysis of the self-determined subset when that subset EXISTS AS A PROPER, NON-EMPTY SUBSET in their data, because it is their strongest available signal. NOT APPLICABLE where the subset resolved to the whole population or to none of it, per the proper-subset guard in Stage 4 item 5: a subset equal to the population is not a cut. |
| G17 | REFERENCE VALIDITY | Every cached reference is within its validity date, or was refreshed, or is recorded as stale-and-unrefreshable. Also fails if the metric weights used do not match the period being written about. |
| G18 | RETRIEVAL | Every attachment on a supervisor or upline message was read, or was read and found out of scope, or is named as unreadable with every path attempted. Also fails if any attachment was fetched by a path on FORBIDDEN_RETRIEVAL_PATHS. |
| G19 | MOVING GROUND | Every claim carrying a number names the ground and states what is known about its movement this period. **Tested against the placement rule in 2.3, which is the only statement of it: the SHORT FORM and the movement statement INSIDE the claim, the full bound MOVING_GROUND_NAME in the GROUND STATEMENT immediately above the first field block and again in METHOD.** Fails where any claim carrying a number has no ground in it; fails where the GROUND STATEMENT is missing, is inside a field block, or names a different ground from the one the fields carry; fails where the short form differs between two fields of one run; and fails where a field was made to fit by dropping the ground. Where MOVING_GROUND_NAME is unbound, fails any claim worded at achievement strength. Where the claim rests on rung 5, fails unless the uncontrolled-movement warning is attached to the claim itself. See 2.3. |
| G20 | COLD START | Applies where any cold-start test in 2.2.3 fired. Fails unless ALL of the following hold: the front panel names the population as having no prior period, names which detection test fired and the figure that fired it; no figure in that population carries a WIN, MISS or FLAT label, NO BASELINE being printed instead and being distinguishable from UNPAIRED and from FLAT; every struck rung is named with its reason; every figure computed against a denominator that failed the independence test is capped at bounded phrasing with the firing figure named; and at least one of the three claimable kinds in SD-CLM-32 is present. **A cold run that produces none of the three has failed this gate.** A plan attainment figure is exempt from the label block. |
| G21 | POPULATION AND SCOPE INTEGRITY | The front panel names the declared population scored, its mode, and which of the three detection tests decided it, or discloses the tie-break. Where the scope holds fewer than MIN_POPULATION_FOR_RANKING units, no rank, percentile, median or comparative language appears anywhere, every suppressed comparison is named, and the level that would produce a comparable population is named. Where the unit of business is coarser than the reader's own scope, that is stated before the content as a configuration mismatch with both levels named. Where the ranking measure is uniform across the population, that is stated with the terms that actually decided the order. **And the front panel states which reading of the not-workable exclusion each part of the document used, the retrospective reading for what is being reviewed and the planning reading for anything forward looking, with every unit that became unworkable during the period included and marked, and every rate saying whether it pro-rated.** See 4.4, 4.5, Stage 4, SD-POP-25, SD-POP-26, SD-POP-27, SD-POP-30. |
| G22 | PEER SET INTEGRITY | The resolved peer level is strictly coarser than the requester's own, and no member of the peer set sits inside the requester's own scope. **The output names which path produced the level: a bound level, a level derived from a stated peer count, or the one-step-coarser fallback; and where a stated count and the fallback disagree, both readings are named and the count wins.** Where the requester sits at the coarsest level, the output says there is no internal peer set rather than manufacturing one, and either names the external comparison group with its publication and staleness or names rung 3 as dropped with the rung it fell to. **Where the resolved set is NON-EMPTY and below EITHER ANONYMITY_FLOOR or MIN_POPULATION_FOR_NORM, fails unless Test 3 at Stage 4 item 7 ran: every level tried is recorded with the count it yielded, the walk stopped at the FIRST level meeting BOTH floors and neither short of it nor past it, NOTHING from any level below ANONYMITY_FLOOR is published in any form including generalized wording, NO delta labelled or raw is computed against a comparator below MIN_POPULATION_FOR_NORM per SD-POP-19, the level actually used and its count print beside every figure that reads it, and the derived level is named as superseded.** Fails on any of the four states in that test being printed for another: an artifact that says FLAT where the truth is too few peers to compare fails this gate, and so does one that says there is no peer set where the truth is a set too small to derive a band from. **A dropped rung 3 never suppresses a rung 4 label**, per 2.5. See Stage 4 item 7, SD-SPN-14, SD-SPN-15, SD-SPN-16, SD-CTR-24. |
| G23 | PRIOR PERIOD POPULATION | Applies wherever two periods are compared under FIXED. The exit test in Stage 4 item 2 ran, its count is printed, and where that count is zero the artifact states which of the two zero-exit states the run believes and the evidence for it, BEFORE any figure computed on the pair. On a survivor-only pair: no retention or churn figure is published as a number, the state printed is NOT COMPUTABLE; no same-unit growth figure appears without the total movement beside it and the gap named; and no ranking by survivor growth appears anywhere. **The gap is named as a FIGURE only where the survivor figure and the total-movement figure rest on the SAME MEASURE, the same basis and the same population definition; where they do not, both print with their bases named and what separates them is stated in WORDS, and no difference is computed.** G14 governs that pair as it governs any other and is never overridden to satisfy this row: a run that subtracts across two measures to produce a gap fails G14 and fails this gate as well. On a genuine no-attrition population: the retention figure IS published with the population size beside it and the evidence named. **A pair certified like-for-like by overlap alone, with no exit test recorded, FAILS.** See SD-CMP-09. |
| G24 | CONTRADICTED CLAIM INTEGRITY | Applies to every item the person stated in their own words that the contradiction sweep in Stage 6 labelled CONTRADICTED, per 2.12.1 and SD-CNF-10. Fails unless ALL of the following hold: the item contributes to NO claim, count, denominator or ranked figure in the copy region; the exclusion is LISTED with its reason rather than being silent; BOTH readings are printed below SUBMISSION_BOUNDARY_BANNER, the person's statement in their own words and what the resolved cell says with its COLUMN AND UNIT NAMED, under one heading, with the question that would settle which is right; and the preview flagged it inline to the person as a question rather than as a correction, per SD-CNF-09. **Fails where the disputed value appears in any wording above the boundary**, which is fabrication under 2.12 the moment the data is checked. **Fails equally where the item was silently deleted**, which is the loss SD-CTR-23 names. **Fails where the two readings were averaged, blended into one sentence, or reconciled by the run choosing one of them.** And fails where a CONTRADICTED item was labelled UNSOURCED or UNVERIFIED, or either of those was labelled CONTRADICTED, because the three carry three different remedies. |

## 7.3 Gate failure routing

**Route every failure to a stage that can REMEDIATE it, never to one that only
evaluates.** See SD-EFF-34.

    G1, G3, G7, G12, G19  Stage 6, then Stage 9, then Stage 12
    G20                   Stage 6, then Stage 6.4, then Stage 9, then Stage 12
    G21                   Stage 0 for the population and scope resolution, then
                          Stage 6, then Stage 9, then Stage 12
    G22                   Stage 4 item 7, then Stage 6, then Stage 9, then
                          Stage 12
    G23                   Stage 4 item 2 to run the exit test and decide between
                          the two zero-exit states, then Stage 6, then Stage 9,
                          then Stage 12
    G24                   Stage 6 to re-run the contradiction sweep and re-label,
                          then Stage 9 to rewrite the claim without the item, then
                          Stage 11.5 so the person sees the pair before it is
                          final, then Stage 12
    G2, G6, G8, G13       Stage 9, then Stage 12
    G4, G10, G14          Stage 4, then Stage 6, then Stage 9, then Stage 12
    G5                    Stage 10 firing Q-TARGET, then Stage 9, then Stage 11,
                          then Stage 12
    G9                    the two-reader step, re-reconciled, then Stage 6, then
                          Stage 9, then Stage 12
    G15                   Stage 10.5, then Stage 12
    G16                   Stage 6.4, then Stage 9, then Stage 12
    G17                   Stage 2 to refresh the stale block, then Stage 6, then
                          Stage 9, then Stage 12
    G18                   Stage 2 to work the retrieval ladder again, then Stage 6,
                          then Stage 9, then Stage 12
    G11                   apply the substitution rule in Part 10, then re-gate in
                          place

**Why the first chain runs through drafting.** Stage 6 fixes labels, lineage, ranks,
rungs and tie counts. Stage 9 rewrites the prose that carried the defect. Stage 6
alone cannot fix a sentence, so routing must continue through the drafting stage, or
the re-gate inspects unchanged text and fails identically.

**Remediation scope.** A gate failure re-runs only the stages named in its chain. A
chain may fire ONLY the specific question named in that chain, and only for items
that question has never been asked about. **Answers already given are never
re-asked. A person must never be asked the same question twice because a downstream
gate failed.** See SD-EFF-35.

**Triple failure.** PER_GATE_FAILURE_LIMIT failed returns on the same gate routes to
Stage 12.1, which emits the draft with the offending claim replaced by a placeholder
and the gate named in the banner. **It does NOT return to root.**

**Global budget.** GLOBAL_REMEDIATION_BUDGET remediation cycles across all gates for
one run. Beyond that, route to Stage 12.1 regardless of which gate is failing.
**Without a global cap, alternating failures between two gates can cycle far longer
than any person will wait.** See SD-EFF-36.

## 7.4 HARD_GATES

**HARD_GATES is ONE organization variable and it is a TAXONOMY of FOUR KEYED
GROUPS. It is never a flat list.** SD-EFF-02. The convention below is owned by the
period-planning skill and this skill conforms to it as written, without
renegotiation, so that a binding owner who binds HARD_GATES once satisfies all three
skills in the bundle.

    HARD_GATES:
      shared:    enforced by ALL THREE skills
      planning:  enforced by the planning skill only
      review:    enforced by this skill only
      scorecard: enforced by the scorecard skill only

**C1. The gate record.** Every gate, in every group, carries exactly these six
fields, and **a gate missing any of them is not a gate**: `key`, stable lower snake
case and unique across all four groups, never renamed and never reused; `group`;
`fires_at`, the named stage or probe step at which it is evaluated, with any
condition; `behaviour`, exactly one of `stop_outright` or
`ask_one_question_then_stop`, with no third value; `reads`, the schema VARIABLE
whose value the gate tests or the literal `none`, **never a threshold written as a
literal in skill text**; and `doctrine`, the doctrine ID that justifies it, whose
Applies list must cover every skill in whose group the gate sits.

**C2. The effective set.** This skill's stop list is `shared` PLUS `review`. Nothing
else. It never enforces another skill's group and never reads it.

**C3. Promotion, and the single-declaration rule.** A gate enforced by more than one
skill is promoted to `shared` and declared there, once. The same gate appearing in
two skill groups is a defect in the binding, not a duplicate.

**C4. No skill may remove a shared gate.** Where a shared gate cannot apply to a run
mode, it resolves NOT APPLICABLE per SD-EFF-37, which is a PASSING state, and it is
**recorded as not applicable with its reason.** It is never silently dropped and
never redefined locally.

**C5. Counts live in the taxonomy and nowhere else.** No count of gates is stated in
this file, in a table, in prose, in a heading or in a parenthesis. The set is
referred to by group name.

**C6. Additions are BOUND, never invented.** A stop condition not in this skill's
effective set is requested through the deferred-binding mechanism, naming the
decision, and until it is bound the condition DEGRADES and is DISCLOSED rather than
stopping. **An implementer inventing a stop condition is the exact failure
SD-EFF-02 exists to prevent, and a companion file inventing one is the same failure
wearing a different hat.**

**C7. Conditional gates name their condition in `fires_at`, and the condition names
a bound value.** A gate conditional on population shape names the mode.

**C8. The unbound default.** Where HARD_GATES is unbound, the standing sets below
apply, both are printed in the method section, and the artifact names them as
standing rather than bound.

### 7.4.1 The shared core, enforced by all three skills

| key | fires_at | behaviour | reads | doctrine |
|---|---|---|---|---|
| `source_unreadable` | probe step 1, and again at acquire | `ask_one_question_then_stop`: name every location attempted, then ask for the file | `SOURCE_WORKBOOK_LOCATIONS` | SD-PRS-25, reference/capability-probe.md 1.6 |
| `record_count_zero` | Stage 4 parse, after counting rows by non-blank identifier | `stop_outright` | `none` | SD-PRS-24 |
| `scope_unresolvable` | Stage 0, after the text re-test and the level re-test in SD-IDN-16 | `ask_one_question_then_stop`: offer the distinct values present at every level | `none` | SD-IDN-16, SD-IDN-13 |
| `formatting_unverifiable` | Stage 12 verify, and ONLY where `DELIVERABLE_CONTAINER_REQUIRED` is true | `stop_outright`: do not publish as verified | `DELIVERABLE_CONTAINER_REQUIRED` | SD-FMT-06, reference/capability-probe.md 2.2 |
| `character_gate_unrunnable` | Stage 12 verify | `stop_outright`: unknown is not pass | `ALLOWED_CHARACTER_RANGE` | SD-FMT-14, SD-FMT-18, SD-EFF-03 |

`formatting_unverifiable` is the one shared gate with a condition, and the condition
matters: where DELIVERABLE_CONTAINER_REQUIRED is FALSE, which is its documented
default, **the run does not stop.** It falls back to structured output carrying
identical information and the gate resolves NOT APPLICABLE.

**The shared row is written as the planning skill owns it and is not renegotiated
here.** Where THIS skill evaluates it, the ladder it reads is reference/capability-probe.md
2.2b rather than 2.2, per rule P1c and 3.1, because this skill's OUTPUT_MEDIUM is
docx. The gate itself, its key, its behaviour and its binding are identical across
the three skills; only the ladder each one reads differs, which is what keeping
OUTPUT_MEDIUM keyed per skill means in practice. **And this gate governs STYLING
only.** The character counts are never inside it: see 7.6.

### 7.4.2 The review extension, this skill only

| key | fires_at | behaviour | reads | doctrine |
|---|---|---|---|---|
| `data_period_mismatch` | Stage 4 period validation, after the authority order has been worked and the person has been asked. **Fires on COVERAGE only.** An IMPOSSIBLE PERIOD, whose end postdates the run date, is a disclosure and a provisional label under Stage 4 and gate G10, never this stop: a real file with a calendar mismatch is not a file about the wrong period | `ask_one_question_then_stop`: name what the data covers and what was asked for | `none` | SD-SRC-15, SD-PRS-24 |
| `join_overlap_below_floor` | Stage 4 item 2, and ONLY where the scored population's mode is FIXED. **Never evaluated under FLOW.** | `stop_outright`: report both rosters | `JOIN_OVERLAP_FLOOR` | SD-PRS-32 |
| `unresolved_items` | Stage 4, once, immediately after reconciliation | `stop_outright`: name every unresolved item | `UNRESOLVED_STOP_COUNT` | SD-RUN-09 |
| `contradicted_items` | Stage 6, once, immediately after the contradiction sweep of 2.12.1. **Counted separately from `unresolved_items` and never added to it**: one counts this method's own derivations disagreeing, the other counts the person's own statements against a resolved column, and a clean count on either says nothing about the other | `stop_outright`: name every contradicted item with BOTH readings and the question that would settle each. **Many contradictions at once are evidence about the extract rather than about the person**, so the stop names the source that produced them and does not word itself as a finding about the writer | `UNRESOLVED_STOP_COUNT` | SD-CNF-10 |
| `review_mode_no_objectives` | Stage 9, in review mode | `ask_one_question_then_stop`: offer reconstruction | `none` | SD-CLM-19 |
| `field_block_set_mismatch` | Stage 12 verify, on the BUILT artifact, against `FORM_FIELDS` | `stop_outright`: name each field, and say whether it is a block with no entry in FORM_FIELDS or an entry in FORM_FIELDS with no block. **Print the field set as well as the disagreement**, because a mismatch is as often a wrongly derived set as a wrong block | `FORM_FIELDS` | SD-CTR-22, SD-CTR-23 |
| `field_block_over_limit` | Stage 12 verify, on the BUILT artifact, after G6 has run on the draft | `stop_outright`: name every over-limit block and by how many characters | `PERSON_CONFIRMED_FIELD_LIMITS` | SD-LNG-09, SD-LNG-10 |
| `field_count_unverifiable` | Stage 12 verify, wherever a block's own TEXT cannot be recounted from the built artifact. **Never fired by DOCUMENT_INSPECT alone**: a count is read from text rather than from structure, so an absent DOCUMENT_INSPECT resolves per reference/capability-probe.md 2.2b and leaves this gate untouched. | `stop_outright`: unknown is not pass | `none` | SD-LNG-09, SD-EFF-03, reference/capability-probe.md 2.2b |
| `field_index_disagreement` | Stage 12 verify, on the BUILT artifact | `stop_outright`: print both readings and publish neither | `none` | SD-RUN-09 |
| `boundary_heading_leak` | Stage 12 verify, on the BUILT artifact | `stop_outright`: name every offending heading and what it sits under | `SUBMISSION_BOUNDARY_BANNER` | SD-CTR-22, SD-CTR-23 |

**The five document gates are members of the STANDING review set under C8, not
inventions made at run time.** C6 forbids an implementer conjuring a stop condition
mid-run; it does not forbid this file from declaring its own group's standing set,
which is exactly what C8 provides for and what the four gates above them already are.
Where HARD_GATES IS bound and the binding's review group omits them, C6 governs and
each omitted condition DEGRADES and is DISCLOSED rather than stopping, and the
artifact names which document assertion was therefore not enforced.

**They sit in `review` rather than in `shared` because no other skill in the bundle
emits a document.** Under C3 a gate enforced by more than one skill is promoted and
declared once; the day a second skill emits a document, these are promoted rather
than copied. **And they are not the shared `formatting_unverifiable` gate wearing a
document hat.** That gate is conditional on DELIVERABLE_CONTAINER_REQUIRED and
governs PRESENTATION, which degrades. These govern the COPY CONTRACT, which is
information and does not. A run may publish with its palette unapplied; it may never
publish with a count it did not verify.

`join_overlap_below_floor` carries its condition in `fires_at` on purpose. Under
FLOW it is not applied at all, per Part 13 divergence 1 and JOIN_OVERLAP_FLOOR's own
validation, because a healthy pipeline fails any reasonable overlap floor and the
resulting stop reads as a data problem at the company rather than as a method that
does not handle pipelines. Under FLOW the gate resolves NOT APPLICABLE and is
recorded with that reason, per C4.

`review_mode_no_objectives` is reachable **only where the person declined
reconstruction when it was offered**, because reconstruction itself never blocks the
run and always emits at least one objective. Where reconstruction ran, this gate
cannot fire.

### 7.4.3 What is NOT a gate in any group, and why

| Condition | Placement | Why |
|---|---|---|
| No measure column resolved | `planning`, and a scorecard twin. **Not this skill's.** | SD-PRS-25 governs this skill and is obeyed here; what does NOT follow from it is a STOP. This skill's no-data path is its product, and a gate inspecting an artifact that path does not produce must not block it, per SD-EFF-37. The absence is reported loudly and the run continues. |
| A qualifier matched no value | `planning`, and a scorecard twin. **Not this skill's.** | SD-QUA-10 governs this skill and is obeyed here; it requires the miss to be reported, not the run to be stopped. The miss is reported loudly and the run continues. |
| A comparison was asked for and only one input exists | `planning`, warm populations only. | And on a cold population it does not fire at all: SD-CMP-08 answers instead, per 2.2.3. |
| Reading the published form specification, standard or brief | **NOT A GATE IN ANY GROUP.** | SD-SRC-21: mandatory, never assumed, never a stop. It degrades under a banner naming the exact release scored against and its date. |
| A required reference has no cached equivalent, or the cached one is stale | **NOT A GATE IN ANY GROUP.** | SD-SRC-13 and SD-SRC-18: a stale or absent reference is a disclosed limitation; a halted run is a dead end. Nothing in the capability probe or in Part 12 adds to the stop list. |
| Fatigue, run length, retry count, output size | **NEVER MEMBERS AND NEVER WILL BE.** | SD-EFF-01, SD-EFF-02. |

Everything not in this skill's effective set degrades, discloses and continues.

## 7.5 Regression invariants re-checked at every gate

REGRESSION_INVARIANTS are re-checked at every gate from the parse stage onward,
**against the CURRENT artifact, never against an earlier claim about it.** See
SD-EFF-07. The standing set for this skill:

1. The record count reconciles between the source and the parse log.
2. Scope purity holds: no row outside the person's resolved scope contributed to any
   figure.
3. Every declared exclusion still holds downstream.
4. **No unit inside the reader's resolved scope was dropped from a published count
   without appearing in the exclusion list with its reason.** Every denominator, every
   population count and every ranked figure reconciles against the in-scope roster plus
   the named exclusions, and an exclusion carries the rule that made it. **This
   replaces an invariant that could not fail in this skill**: the set carried over "no
   measure floor was applied; the whole in-scope population was ranked", which is a
   planning-skill invariant, and a review is not a worklist and produces no ranked list
   to apply a floor to, so it was re-checked at every gate from the parse stage onward
   and passed by construction. **An invariant that cannot fail is noise inside a set
   whose whole value is that each member can**, and it teaches a reader that the set is
   ceremonial. The replacement can fail, and it is the one that catches the ordinary
   failure here: a unit quietly leaving a denominator between two stages, which is
   invisible in the artifact and changes every rate computed on it.
5. Qualifier membership holds: every row in a qualified population still satisfies
   the qualifier.
6. Sampled percentiles are stable between the first computation and the current one.
7. Every claim still names its unit and its counterfactual rung.
8. Every proposal inside the copy region is still in state CONFIRMED, and every
   proposal below the submission boundary still satisfies all five conditions in
   2.20.
9. **The row count of the scored population is unchanged by every enrichment join
   performed**, per SD-PRS-48 and Stage 4 item 6: the count before each join equals
   the count after it, and a change in either direction blocks rather than being
   explained. The match rate and both unmatched counts still reconcile with the
   figures the enriched terms produced.
10. **No figure is worded at a rung weaker than the strongest rung available to it.**
    Every figure's rung is at or above the highest rung that COUNTERFACTUAL_AVAILABLE_RUNGS
    supplies and whose own definition is bound, unless that rung's own inputs failed to
    resolve for that metric and the drop is stated beside the figure with its reason.
    **A run in which at least one available rung's definition is bound and every claim
    is nonetheless worded at the floor rung FAILS this invariant**, whatever the state
    of COUNTERFACTUAL_DEFAULT_RUNG, because an unbound value has then overridden a
    bound one. See 2.2.1, SD-CTR-24 and standing rule S9.

**Sampling and estimating are prohibited at every scale.** Never sample rows,
estimate a threshold, extrapolate a percentile from part of the file, lower a cap,
drop a section or shorten a list. **A percentile taken over a sample is a different
number wearing the same name.** See SD-SCL-03.

Before publication, re-read SPOT_CHECK_SAMPLE_SIZE units from the source and compare
them against the artifact.

## 7.6 The document verification, which runs on the BUILT artifact

**READ BACK THROUGH THE ENGINE, NEVER FROM THE BUILD INTENTION.** reference/output-contract.md
PART 7.1 governs how this runs and is cited rather than restated. Open the artifact
that was actually built and read its structure: the headings that exist, the style
each heading carries, the text between one heading and the next, and the strings in
the field index. **Asserting what the assembly code intended to write is not
verification**, and a broken copy contract is precisely the defect that is invisible
in a draft and fatal in the destination system. **A gate that cannot run has FAILED**
and the artifact is not published.

**The matrix is reference/output-contract.md PART 7.2, rows D1 through D6**, cited by number
and never restated here. The rows of that matrix defined for a grid are recorded NOT
APPLICABLE for this artifact, **with the stated reason that they are defined for a
grid and this artifact has none**, which is a passing state per SD-EFF-37. A not
applicable recorded WITHOUT its reason is recorded NOT IMPLEMENTED instead, which is
not a passing state. Publish the record with its reasons in METHOD, so a reader can
tell a simple artifact from a quietly unbuilt one.

**WHICH ELEMENTS OF THAT CONTRACT DO NOT REACH A DOCUMENT, NAMED ONE BY ONE, SO
NOBODY SCORES THIS SKILL AGAINST THEM LATER.** PART 3 of that file states that the
docx carries no formatting elements from PART 2, and PART 1 keys the medium per skill.
The elements below are the ones a reader is most likely to look for, and each is
recorded NOT APPLICABLE with the stated reason that it is defined for a GRID and this
artifact has none:

| Element of the contract | Why it cannot reach this artifact |
|---|---|
| PART 2.2 and its subsections, the caret allowance and column width | A width in characters against a column with a filter caret. A document has no columns and no autofilter. |
| PART 2.3 and 2.4, row and header-row height | Computed against a cell's own column width. There are no cells. |
| PART 2.5 AS REWRITTEN, the total membership rule over shape tokens deciding right, centred and left, and the three-condition STATUS GRID COLUMN | An alignment rule over COLUMN SHAPE TOKENS. **This skill emits no column, so no string it writes carries a shape token and the membership rule has nothing to be total over.** A status a review reports is prose inside a capped field, not a cell in a grid, and a field block has no alignment to decide. `CENTRE_ALIGN_MAX_CHARS` is read by that section and by nothing else in the contract, so it is not read here either. |
| PART 2.6 AS REWRITTEN, the classification fill per state of a declared vocabulary, and its separation from both the alert shading and the centring test | A PER-CELL FILL drawn from a declared state vocabulary. A field block carries no fill, this skill paints no cell, and it publishes no scored state vocabulary to key one on. **The rewrite's substance is that a fill is never conditional on the centring bound, which is a relation between two grid rules and reaches nothing here.** Recorded NOT APPLICABLE on the same ground as the whole of PART 2 and NOT as a rule this skill declines. |
| PART 2.7, the bound on a grid's TOTAL summed built width and the relief ladder that answers it | A bound on the SUMMED BUILT WIDTH OF EVERY COLUMN OF ONE SHEET, in the width unit PART 2.2 sets columns in. **There is no sheet, no column and no width unit here, so the bound has no quantity to measure and the ladder has no column to relieve.** Its three untouchables and its relief ladder are grid mechanics throughout: a legend, a trailing narrative column and a recomputation from PART 2.2, none of which this artifact has. **The PRINCIPLE has a counterpart here and it is met elsewhere, and it is named so nobody reads this row as a gap**: what bounds this artifact is FIELD_LIMITS in CHARACTERS, per 1.5, the targeted fill under TARGET_FILL_RATIO, warned as V3b, and the caps disclosed per field in the field index. That bound is never raised to clear a field that failed it either. |
| PART 4 and 4.1, rank and the reason-for-rank columns, and 4.1.2's bounded frozen span | Freeze panes, an identity block and a column order. There is no sheet to freeze and no identity block to bound. |
| PART 4.2 and 4.3, the three kinds of ranked sheet and the reference tier's size | Sheet classes. This skill emits no sheet. |
| PART 5.1, 5.1.1 and 5.2, the cap, the three bounds a row count can have and the showing note | All three bounds count ROWS. A review's copy region is bounded by FIELD_LIMITS in characters, which 1.5 governs and which the field index and the count captions already disclose. |
| PART 5.3, the note band | The one permitted location for a note ABOUT A GRID, merged across the table's column span and BORDERED by element 7 on all four outer edges of that merged region like every other populated cell of the sheet. Both halves are grid mechanics and neither reaches a document. **What DOES reach it is what the band carries**: this artifact's equivalents are the front panel line and the full form below the boundary, per 8.3, and each of those carries its note as a SENTENCE a reader can read, never as a bordered box with nothing in it. |
| PART 5.4, the explanatory row of an empty sheet | The mechanism is a data row inside a table range. **The PRINCIPLE still binds and is met elsewhere**: an empty drafted SECTION here ships its heading and exactly one line saying why, per 8.2, SD-CTR-07 and SD-FMT-07, and it is never silently omitted. **THE SENTENCE IS THE HALF THAT BINDS EVERYWHERE, AND IT IS NOT OPTIONAL.** 5.4 requires the row to hold a NON-EMPTY string saying in plain words WHY the section qualified nothing, beginning in the table's SECOND column, and it fails a row that is bordered, sized and empty more loudly than it fails a missing one, because a missing row is visibly missing and a blank one looks finished. Here that string is the LINE, and a heading shipped over a blank, a dash or a single space standing in for a sentence fails 8.2 in exactly the same way. What does not reach this artifact is the row, the table range, the second-column position and the FIRST-IDENTITY-COLUMN test that tells a grid's counter the two apart. |

**AND THE THREE VARIABLES THOSE SECTIONS INTRODUCED ARE NOT READ BY THIS SKILL, WHICH
IS RECORDED HERE SO A LATER COMPLETENESS SWEEP DOES NOT READ THEIR ABSENCE AS A HOLE.**
Each is a spreadsheet concept, each is bound in reference/schema/ for the skills that
emit a grid, and a run of THIS skill reads none of them, binds none of them and reports
none of them as unbound:

| Variable | Why this skill does not read it |
|---|---|
| `GRID_MAX_TOTAL_WIDTH` | The maximum summed built width of every column of one entity sheet or reference table, in the width unit PART 2.2 sets columns in. This skill emits no sheet and no column, so the quantity it bounds does not exist in this artifact. Reading it here would produce a bound with nothing to measure and a method-sheet record of a build that never happened. |
| `CLASSIFICATION_VOCABULARY` | The closed declared set of states a classification fill is keyed on. This skill paints no cell and publishes no scored state set to key one on; the closed sets it does carry, per 8.2 and SD-CTR-29, are validated as vocabularies and are never rendered as colour. |
| `CLASSIFICATION_FILLS` | The map from those states to fills. A field block carries no fill. The one palette this skill does read arrives as D6 and it names the variables the grid skills name, so a binding owner binds one palette and gets both artifacts. |

**A variable recorded here is recorded NOT READ with its reason, which is the same
discipline as a NOT APPLICABLE with its reason**: an unexplained absence is
indistinguishable from an omission, and the whole purpose of this subsection is that
nobody scores this skill against a grid it does not emit.

**PART 3 governs this skill, PART 6's unit noun governs every string it writes, and
PART 7 governs how the verification runs. Nothing else in that file does.** A NOT
APPLICABLE recorded without its reason is recorded NOT IMPLEMENTED instead, which is
not a passing state, so each row above carries its reason into METHOD.

**WHICH OF THE FORMATTING DOCTRINES THIS SKILL ADOPTS, AND WHICH IT DOES NOT, READ
FROM EACH RULE'S OWN APPLIES LINE RATHER THAN FROM A JUDGMENT MADE HERE.** reference/doctrine/
states per rule which skills it binds, and that line is the answer:

| Rule | Adopted here? |
|---|---|
| SD-FMT-27, a verification never scans its own record, and one colour never carries two meanings | **ADOPTED, in the half that reaches this artifact.** Its APPLIES line names this skill. The own-record exclusion is executed below and it is the reason this subsection has a declared excluded span. **Its palette half is not adopted and is not declined**: a colour bound twice is a property of a grid carrying a classification fill beside an alert band, and this artifact carries neither, so the collision it prevents cannot occur here. Its rewritten statement that a fill is never conditional on the centring test is a relation between two grid rules and reaches nothing this skill emits. |
| SD-FMT-28, a grid's TOTAL width is bounded and what gives is a repeated qualifier | **NOT ADOPTED, and its own APPLIES line says so.** It binds the two grid skills and not this one. It bounds a SUMMED BUILT COLUMN WIDTH, which this artifact has no quantity for, and its relief ladder moves qualifiers into a legend and a trailing narrative column, neither of which exists here. **It is named rather than silently ignored**, because a new rule nobody records reads as a rule somebody missed. The counterpart bound that does govern this artifact is FIELD_LIMITS in characters, per 1.5 and V3b. |
| SD-FMT-29, formatting must degrade safely, so a band and its ink are asserted against BOTH degraded renderings, every colour carries an explicit opaque alpha, and the MECHANISM is chosen for the engine the READER opens rather than the one the file was built in | **ADOPTED IN FULL**, and its APPLIES line names this skill. **Its newest half, that a mechanism is chosen for the reader's engine and that a check reads a property back from where the READER meets it, is adopted as a principle and has no filter to apply it to here**, since the measured case was a spreadsheet filter and this artifact has no grid; what it governs here is the palette and the container, both of which are already read back from the built document. **It is not a grid rule and nothing about it is spreadsheet-shaped**: this artifact carries a styled panel drawn from the same palette per D6, and a document is opened in a viewer, a converter, a preview pane, a browser and a printer exactly as a workbook is, so the failure it answers reaches here unchanged. The bands are LIGHT, their ink is DARK, both degraded renderings are asserted before the document is built, and every colour is written opaque. What does not reach this artifact is the CELL the rule was measured on, never the rule. |
| SD-FMT-30, no word is ever broken by a cell line, so an over-wide string goes in a MERGED region and every column is floored at its longest unbreakable token | **NOT ADOPTED IN ITS MECHANICS, ADOPTED IN ITS PRINCIPLE, AND NAMED HERE RATHER THAN SILENTLY IGNORED.** Both halves are CELL mechanics: a merged region spanning columns, and a column width floored in characters. **This skill emits no cell and no column**, so there is no boundary for a string to overflow and no width to floor, and both are recorded NOT APPLICABLE on the same ground as the whole of PART 2. **The principle does reach this artifact and is met by rules it already carries**: no field is ever solved by breaking a word, and FIELD_LIMITS bounds a block in CHARACTERS with the compression order of 1.5 deciding what goes, which never cuts a word in half to fit. |
| SD-FMT-03, the computed freeze point and the bounded frozen span | **NOT ADOPTED**, per its APPLIES line. There is no freeze, no identity block and no anchor column in a document. |
| SD-CTR-08, the identity block is structurally identical on every item section, and the freeze lands in the same place on all of them | **NOT ADOPTED**, per its APPLIES line, for the same reason. Its amendment fixes where a pin lands across sections of a workbook. |
| SD-PRS-48, a second file carrying the evidence is JOINED, and a join that lands and cannot be scored has not answered the failure | **ADOPTED IN FULL**, per its APPLIES line, and executed at Stage 4 item 6 with regression invariant 9. The amendment is the second half: the joined columns must RESOLVE to the concepts the terms need, by the sibling-set route where the enriching file carries one column per member of a set. |

**AND PART 7.1'S OWN-RECORD RULE IS ADOPTED HERE, BECAUSE THIS ARTIFACT CARRIES ITS
OWN VERIFICATION RECORD INSIDE ITSELF.** SD-FMT-27. The record from this section is
printed in METHOD, inside the document it describes, and a record that is auditable has
to name WHAT IT SEARCHED FOR. **Every assertion in this skill that SEARCHES FOR STRINGS
excludes the verification record from its own scan and says in its own record that it
did so**, naming the heading the record sits under as the excluded span. Without that,
an assertion that scans the document for a banned heading, a banned phrase, a sentinel
token or a hard-coded unit noun finds the terms it wrote into its own record and fails
itself, so a run that recorded its evidence fails and a run that hid its evidence
passes, which is the exact inversion an audit trail exists to prevent. **THAT
EXCLUSION IS THE ONLY ONE PERMITTED and no assertion may exclude anything in order to
pass.** **IT IS FOR STRING SEARCHES AND FOR NOTHING ELSE: V6, the character sweep,
still reads every string in the artifact INCLUDING the record**, because a character
outside the permitted set is a defect wherever it sits and cannot be planted by a
record of itself; and an assertion reading a structural attribute is unaffected.

**The assertions this skill adds on top of D1 through D6**, every one of them read
back from the built artifact:

| # | What is asserted | What blocks publication |
|---|---|---|
| V1 | **Run against FORM_FIELDS, never against FORM_SECTIONS, which is a list of SECTIONS.** Every entry in FORM_FIELDS has EXACTLY ONE block, in FORM_FIELDS order, and no block exists for a field FORM_FIELDS does not carry. **A test of one block per FORM_SECTIONS ENTRY fails a correct document wherever one section holds two fields, and that is the ordinary case.** Where FORM_FIELDS is unbound it is derived per its reference/schema/ SECTION A1 row, and the derived set is printed beside the result so a failure names which of the two was wrong. | `review.field_block_set_mismatch` |
| V2 | Every block's PUBLISHED count equals the length of the text actually written into that block, recounted from the built artifact and never carried forward from the draft. | `review.field_count_unverifiable` |
| V3 | No block is over its limit. ONE over-limit block blocks publication. | G6 on the draft, then `review.field_block_over_limit` on the built artifact |
| V3b | **No block exceeds TARGET_FILL_RATIO of its own confirmed limit.** Recounted from the built artifact exactly as V3 is. **UNLIKE V3 THIS IS A WARNING AND NOT A PUBLICATION BLOCK**, and every block over the target is NAMED with its overage in characters, in METHOD, so the person can see which boxes have no room left in them. | Nothing. It warns and names, and V3 is the only over-limit stop |
| V4 | The field index agrees with the blocks, field for field and count for count, **and both agree with FORM_FIELDS**. | `review.field_index_disagreement` |
| V5 | Nothing below SUBMISSION_BOUNDARY_BANNER carries a field-block heading style, and no text below it is formatted as a copyable field. | `review.boundary_heading_leak` |
| V6 | The character sweep ran over every string this skill authored, on BOTH bounds of ALLOWED_CHARACTER_RANGE **and against its exception list**, per 10.1. A permitted line feed inside a field's text is not a failure and is counted as one character; a line feed in any heading, label or identifier is. | G11, then `shared.character_gate_unrunnable` |
| V7 | **The copy region's opening span**, read as break structure per 8.3: a page break sits immediately before the copy region; every paragraph between that break and the first field block is a member of the CLOSED PERMITTED OPENING SET in 8.3, in that set's order; and no second page break sits among them. **The section heading of a one-to-many first section IS a member of that set**, per 8.1.1, and a run that fails a document for carrying it has failed a correct document. | `review.boundary_heading_leak` where a below-boundary heading appears in the span; otherwise it names the offending paragraph and routes to Stage 9 |

**V2 is the assertion that makes the other five worth running.** A count computed at
Stage 9 and printed at Stage 12 describes the Stage 9 string. Compression under
COMPRESSION_ORDER, an accepted rewrite from Stage 11, an answer folded in at Stage
10.5 and a placeholder substituted at Stage 12.1 all change the string after the
count was taken, and every one of those is routine rather than exceptional. **The
number in the block's count caption must be recounted from the characters that are
actually in the built block**, or it is a true statement about a document that no
longer exists.

**V3b EXISTS BECAUSE EVERY GATE IN THIS FILE READS THE LIMIT AND, UNTIL IT DID,
NOTHING READ THE TARGET.** 1.5 requires the run to target TARGET_FILL_RATIO of the
confirmed limit and says why: **that margin is what absorbs an edit of the person's
own.** The budget arithmetic in 1.5 sums the parts against the TARGETED FILL rather
than against the raw limit for the same reason. But G6 tests the LIMIT, V3 tests the
LIMIT, and `review.field_block_over_limit` reads the LIMIT, so a run could ship every
field one character under its cap, pass every gate in the bundle, and hand the person a
document in which any word they add truncates their own record silently. **The margin
the ratio exists to reserve was protected by nothing.** V3b is the read-back that
protects it.

**AND IT IS DELIBERATELY NOT A BLOCK.** The targeted fill is a writing discipline, not
a property of the destination system: a field at the limit is still a field that pastes
correctly, and stopping publication over a margin would trade a real document for a
style rule. **What a warning buys is that the spend is VISIBLE.** A block over the
target is named with its overage, so the person can see before they paste which boxes
have room for their own sentence and which do not, and so a maintainer can see whether
COMPRESSION_ORDER is being reached for late rather than written short from the start.
**A run that spends that margin has spent something that belongs to the person**, and
the least it can do is say so.

**V3 names G6 first on purpose, and adds no counting rule of its own.** G6 in 7.2
already tests that every emitted field carries its exact count and that every count
is at or under the confirmed limit for that field. 1.5 already settles what is
counted, what TARGET_FILL_RATIO targets, what COMPRESSION_ORDER cuts and in what
order, what NEVER_CUT_LIST protects and what OVER_LIMIT_REMEDY does when the field
still does not fit. **This section adds the READ-BACK and nothing else**: the stop
that fires when the built artifact holds an overrun the draft did not, because the
draft is not what gets pasted.

**V1 and V5 are the two halves of one idea.** A field that has no block cannot be
pasted, and a block that is not a field must not be. **V1's set is FORM_FIELDS and
never the section list**, and the set is printed beside the result so a failure names
which of the two was wrong. Below the boundary the same test
runs in reverse, because the failure there is a reader mistaking working notes for
draft text and pasting them into the permanent record. See 2.20 and SD-CTR-22.

**WHERE DOCUMENT_INSPECT IS ABSENT, THE STYLING HALF CANNOT BE VERIFIED AND THE
COUNTS STILL CAN.** This is the one distinction an implementer will get wrong, so it
is stated flatly. **A character count is read from TEXT, not from a structural
attribute.** A run that can open the built document and read the words in it can
recount every block, whatever it can or cannot learn about a heading style. **So
DOCUMENT_INSPECT being ABSENT NEVER EXCUSES V3, the over-limit check**, and it never
excuses V1, V2, V4 or V6 either, all of which are read from text. It reaches only the
part of D6 and V5 that needs a style attribute, and that part resolves per
reference/capability-probe.md 2.2b and rule P1b. **An implementation that skips the over-limit
check because the docx gate could not run has confused a presentation failure with a
correctness one, and the field it let through arrives truncated in a permanent
record.** That is the whole reason the two capabilities are probed as two tokens.

**Where the TEXT of the built artifact cannot be read back at all**, which is
DOCUMENT_WRITE degraded or absent rather than DOCUMENT_INSPECT absent, the copy
contract cannot be verified and it is NOT published as a document. The resolution is
the ladder in 8.6, which is reference/capability-probe.md 2.2a: emit the same content as
structured markdown, which carries no unverifiable container contract, and say so in
all three announcement places. This is not a judgment call and it is not
DELIVERABLE_CONTAINER_REQUIRED's decision: that binding chooses between a
labelled-unverified container and a fallback for PRESENTATION, and presentation
degrades. **A count nobody verified is not presentation.**

---

# PART 8: OUTPUT FORMAT

**`OUTPUT_MEDIUM` FOR THIS SKILL IS DOCX, per reference/output-contract.md PART 1.** The medium
is keyed per skill in that file and a run reads only its own entry. **PART 3 of that
contract therefore governs this skill's artifact IN FULL**, requirements D1 through
D6, and it is CITED here by number and never restated. A restated contract is how a
formatting rule degrades into a passing mention that nothing enforces.

**PART 2's SPREADSHEET FORMATTING ELEMENTS DO NOT APPLY TO THIS SKILL AND ARE NOT
SCORED AGAINST IT.** The contract says so itself, in PART 3: freeze panes,
autofilters, table objects and computed column widths are grid concepts, and a review
has no grid to apply them to. **That sentence is cited here rather than paraphrased
so that nobody scores this artifact against elements it cannot carry and reports a
column of phantom failures.** The one element-shaped rule this skill does carry
arrives as D6, the palette, and it names the same variables the spreadsheet skills
name so that the bundle reads as one system.

**Where this file and the contract appear to disagree, THE CONTRACT GOVERNS and this
file is stale.** That is the same precedence the file header sets for every companion
file, and it is repeated here because PART 8 is where a drafting implementer actually
looks.

**WHAT THE DOCUMENT IS FOR, in one sentence, because every rule below follows from
it.** The document WRAPS the character-limited form-field blocks. **It does not
replace them.** The review exists to be pasted, field by field, into a submission form
whose fields truncate silently and without warning, per 1.5 and SD-LNG-09. The
document makes those fields READABLE; it never makes them less COPYABLE. **A change
that improves the reading at the cost of the pasting is the wrong trade every time**,
and 8.3 is written to make that trade hard to make by accident.

## 8.1 The form

**Mirror the bound form structure, and READ IT LIVE EVERY RUN where the capability
permits.** FORM_SPEC_SOURCE is the authority for what the sections are;
FORM_SECTIONS is the bound list, in order, each marked drafted or manager-only.

**MANDATORY, NEVER ASSUMED. Not mandatory, never skipped.** SD-SRC-21. The form
specification, and any published standard or brief this skill scores or drafts
against, is READ every run. It is never assumed, never remembered from a previous
run as authoritative, and never replaced by this method's own idea of what the
sections are. **And it is NOT a stop.** A specification that cannot be reached after
the full retrieval ladder DEGRADES: the run continues, banners itself as
specification unconfirmed, names the exact release it drafted against with its date,
and never presents the result as authoritative. Reading the standard is not a member
of HARD_GATES, per 7.4.3. The correct heading for such a step is MANDATORY, NEVER
ASSUMED, because MANDATORY, NEVER SKIPPED reads as a stop and will be implemented as
one.

Where FORM_SPEC_SOURCE is unbound, a generic structure is drafted and the person is
told to check it against the live form before pasting, because **a heading with no
counterpart on the live form must never travel into the record.** Sections the live
form carries and the bound list does not are not drafted at all, and that is stated
rather than papered over.

**A DEFAULT SHARED WITH ANOTHER SKILL IN THE BUNDLE IS KEYED BY SKILL, NEVER
SINGLE.** SD-CTR-30. The generic section set below is this skill's own, for this
skill's destination form, and it is correct here because FORM_SECTIONS describes a
form only this skill drafts. **Where a variable IS read by more than one skill, its
documented default is either neutral in wording or a keyed set with one entry per
skill, and this skill reads only its own entry.** HARD_GATES in 7.4 is the worked
instance of that. A single shared default carrying one skill's sections or one
skill's artifact name is that skill's contract wearing a shared name, and a literal
implementer of any other skill ships the wrong document. Where a default must name a
THING whose noun differs by skill, it names the ROLE instead.

**THE GENERIC SECTION SET IS NOT STATED HERE. It is the FORM_SECTIONS row of
reference/schema/ SECTION A1, which is its only home**, exactly as HARD_GATES and
the formatting elements are cited rather than copied. That row carries the order, the
titles and the `drafted` flag on every entry, including the manager's own section,
which is present and not drafted. **This file used to carry a second table calling
itself the same default, with different contents**, so one configuration produced two
different documents and a set test stopped one of them. There is one statement now
and it is not here.

**THE `drafted` FLAG IS READ, NEVER INFERRED, AND THE SET IS NEVER TRIMMED TO THE
DRAFTED ONES.** A section this person does not write is still a section of their
form. A run that does not know it exists cannot warn them that a heading it produced
has no counterpart, cannot order the blocks correctly around it, and will report the
manager's own section as an unexpected block. **Every set test that asserts one block
per entry runs over the DRAFTED SUBSET, never over the whole set**, per that row and
per V1 in 7.6.

**Header strings are byte-identical between runs** and are never improved for
readability, so that two write-ups remain comparable. See SD-CTR-09.

### 8.1.1 A form SECTION and a submission FIELD are different things, and the field set is DERIVED and PRINTED

**reference/output-contract.md PART 3.1 settles this and is cited rather than restated.** A
SECTION is a part of the destination form. A FIELD is ONE CHARACTER-CAPPED BOX inside
it. One section can hold one field or many, and the two are counted separately.
**FORM_SECTIONS is a list of SECTIONS and is never read as a list of fields.**

**THE FIELD SET IS FORM_FIELDS, AND ITS DERIVATION IS NOT WRITTEN HERE.** FORM_FIELDS
is a variable, it is DERIVED rather than hand-maintained, and **its single derivation
is its reference/schema/ SECTION A1 row**, which takes the sections, keeps the ones
the cycle position draws, drops the ones whose `drafted` flag is false, and expands
what remains one field per section except one field per objective where
OBJECTIVE_FIELD_IS_SINGLE is true. Read it there. **This file used to carry that
derivation in prose, and a set that is derived in prose in each place that needs it is
derived differently in each place**, which is the same defect as a restated default.
Each entry carries its key, the section key it belongs to, the title as the
destination system names it, its order and the FIELD_LIMITS key that caps it.

**What this subsection adds is what is genuinely this skill's own**: where the set is
printed, what the heading of a field inside a one-to-many section looks like, what
decides which FIELD_LIMITS key caps a drafted section, and what reads the set.

**WHICH FIELD_LIMITS KEY CAPS A SECTION IS RESOLVED BY A STATED TOTAL RULE AND IS
PRINTED, BECAUSE THE DERIVATION SAYS "ITS KIND" AND NOTHING SAYS WHAT A SECTION'S KIND
IS.** FORM_FIELDS' derivation takes each field's cap from the FIELD_LIMITS entry for
its kind. FIELD_LIMITS is keyed by kind. **FORM_SECTIONS carries no kind.** So on the
standing generic set exactly one section names a kind at all, and it does so only
because its own title happens to contain the words that name one; every other drafted
section leaves the key to be guessed. At the documented defaults two of the candidate
keys carry the same number, so nothing moves and the hole is invisible -- **and at any
organization that binds two of those keys to different numbers, two implementers cap
the same box differently, and one of them either truncates a permanent record or blocks
publication of a correct one.**

**THE RULE, WHICH IS TOTAL OVER THE SECTIONS AND DECIDES BY THE SECTION'S FUNCTION AND
NEVER BY WORDS IN ITS TITLE**, applied in this order, first match winning:

1. **Where FORM_SECTIONS carries a declared kind for the section, that kind governs and
   nothing below is consulted.** It is the binding owner's answer and it outranks every
   derivation, per standing rule S9.
2. **A section that yields ONE FIELD PER OBJECTIVE** -- which is the objectives section
   under OBJECTIVE_FIELD_IS_SINGLE, and any section FORM_SECTIONS marks the same way --
   takes the OBJECTIVE key.
3. **A section whose one field is a continuous narrative the person writes about
   themselves** takes the FREE TEXT key.
4. **Every remaining drafted section** takes the COMMENT key.

**THE RESOLVED KIND IS PRINTED BESIDE THE CAP IN THE FIELD INDEX AND IN METHOD**,
naming which of the four steps decided it. That is the whole point: a person with the
form open can see in five seconds that a box the run capped as a comment is a free-text
box on their form, and correct it into PERSON_CONFIRMED_FIELD_LIMITS per 1.5, which
outranks all four steps. **A guessed cap that nothing prints is a guess nobody can
catch.** The durable repair is a declared kind per section rather than a rule that
infers one, and that is a schema request rather than something this file may invent;
until it lands, step 1 is where a bound answer enters and the other three steps are
deterministic so that two implementers reach the same cap.

**THE BLOCK, THE COUNT AND THE LIMIT ATTACH TO THE FIELD.** The section supplies the
ORDER of the blocks and the name they are grouped under, and nothing else. **A
verification that counts blocks against the SECTION list fails a correct document the
moment one section holds two fields**, which is the ordinary case rather than an
exotic one: it reads one section named for objectives, sees four blocks, declares a
mismatch and stops publication on an artifact that is right. That defect is the
reason V1 in 7.6 is written against FORM_FIELDS and not against FORM_SECTIONS.

**FORM_FIELDS IS PRINTED IN THE DOCUMENT.** It is the field index in 8.3, and it is
printed for three reasons, all of them load bearing: a reader can see how
many boxes they are about to fill and in what order; the block count has something to
reconcile against that is not the section count; and the derivation itself is visible,
so a reader who has five boxes on their form and six lines in the index can see the
disagreement before they paste rather than after.

**THE HEADING OF A FIELD IN A ONE-TO-MANY SECTION CARRIES THE FORM'S OWN INDEX.**
Where a section yields several fields of the same kind, the heading is the destination
system's own name for the field followed by the index the form itself uses to tell the
boxes apart. That is not a friendlier name and not an improved one; **it is the
destination's name plus the only thing that says WHICH BOX**, and without it a reader
with four identically headed blocks cannot match any of them to the form. Per
reference/output-contract.md PART 3 D1.

**AND A ONE-TO-MANY SECTION IS STILL NAMED.** The blocks of a section that yields
SEVERAL fields are grouped under the section's own heading, so the document's
structure still mirrors the form's structure and the navigation pane still shows the
person the shape of what they are filling in. The section heading is not a field
heading, carries no count caption, and is never selected as part of a block, per
8.3 D2.

**AND WHERE A SECTION YIELDS EXACTLY ONE FIELD, THE SECTION HEADING IS SUPPRESSED AND
THE FIELD HEADING STANDS ALONE.** A section heading exists to GROUP several blocks,
and where there is nothing to group it groups nothing while costing a heading. **The
cost is not cosmetic and it was measured.** FORM_FIELDS' own derivation gives a
single derived field the section's title, so keeping both produces two adjacent
headings carrying THE SAME WORDS, one of which is a copy block and one of which is
not, distinguishable only by heading level and by which one has a count caption under
it. That is exactly the careful reading of a heading that 8.3 D5 says a reader must
never have to do, and on the standing section set it happens on more than one section
of every ordinary run. **What survives the suppression:** the field keeps the
section's order and its place in FORM_FIELDS, the field index still prints it under
that name, the navigation pane still shows one entry for it rather than two, and V1
still reconciles blocks against FORM_FIELDS rather than against the section list, so
nothing that reads either set changes. **What is never done instead:** the section
heading is not kept and reworded to tell the two apart, because a reader matching the
document to their form is matching the destination system's own names and an invented
distinction between them is a second name for one box.

## 8.2 Cycle-specific templates

FORM_SECTIONS_BY_CYCLE_POSITION decides which sections each position draws. The
standing map:

| Position | Sections drawn | Postcondition of assembly |
|---|---|---|
| SET | Objectives and measures; development objectives | Every objective carries a title, a description, measures in GOAL_PATTERN shape, a start and a due date, and a lineage line outside the field. No completion percentage exists yet. |
| TRACK | Objectives and measures; progress comments | Every objective carries a status from STATUS_VALUES and at least one dated comment. Completion is computed only where a target exists. **An objective with no target, no measure or no reading to judge it against takes the member of STATUS_VALUES that exists for exactly that state, and is never given the nearest member of a two-value set**, which asserts a judgment nobody made in the direction the reader acts on. Where the bound set carries no such member, the status is left to the standing absence statement and the objective is named in the audit, per that variable's own row and the closed-vocabulary rule below. This is the same state G5 flags as ungradable inside the block, said in the field the form asks for. |
| MIDPOINT | All drafted sections | Every objective carries a completion percentage or an UNGRADABLE flag; the mid-period free text is drafted; every claim carries its rung. |
| CLOSE | All drafted sections | As MIDPOINT, plus behaviours where bound, plus the closing free-text sections, plus the learning from every MISS. |

**Every drafted section ships every run, even with nothing to report**, carrying its
heading and exactly one line saying why in plain language. See SD-CTR-07 and
SD-FMT-07. A section is never silently omitted because a binding or a capability was
missing.

### A closed vocabulary is validated from the STATES to the SET

SD-CTR-29. Several sections draw a value from a CLOSED set the contract requires a
value from: a status per objective from STATUS_VALUES, an activity status from
ACTIVITY_STATUS_VALUES, a rating from RATING_SCALE, a behaviour level from
BEHAVIOUR_SCALE_VALUES, a failure pattern from GOAL_FAILURE_PATTERNS. **Validate
coverage in that direction, from the states to the set, whenever either changes:
for every state this skill can emit, does the set contain at least one member that
applies to it?** A state with zero members is a HOLE, it guarantees an unmapped
value on every run in which that state occurs, and **a holed set looks complete to
anybody who reads it without counting.** The state most likely to be holed is the
ordinary one, because the rare states are the ones somebody thought to seed. Where a
hole is found, name it, emit the state unmapped with the reason, and queue the
request to BINDING_OWNER_NAME rather than forcing the nearest member.

**A VALUE IS NEVER CHOSEN BECAUSE IT IS THE CLOSEST AVAILABLE, AND A SET WITH NO
APPLICABLE MEMBER IS REPORTED AS A SET WITH NO APPLICABLE MEMBER.** The named case is
the ungradable objective: the standing STATUS_VALUES now carries a member for an
objective with nothing to judge it against, so that state is COVERED and the covering
member is the one used. Where a bound set omits it, the hole is real, it is named, and
the field is left to the standing absence statement. **Neither the standing member nor
the absence statement is ever replaced by the nearer of the two ordinary states**,
because both of those say something about performance and the truth is that nothing
was measured. The same discipline governs every other closed set this section lists.

**Distinguish a HOLE from a DELIBERATELY EMPTY ADDITIVE LIST.** BANNED_HEADINGS,
BANNED_PHRASES, SENTINEL_TOKENS, FORBIDDEN_RETRIEVAL_PATHS, NON_CLAIMABLE_ENTITIES
and SIBLING_SKILLS are all correct when empty: nothing has been added yet and no
output has to be produced FROM them. **The test is whether some output cannot be
produced without drawing from the set.** An empty additive list is not a defect and
is never reported as one; an empty family in a vocabulary the contract draws from
always is. A member whose implied action is genuinely NONE says so explicitly and
names nobody as able to clear it.

## 8.3 Emission shape

**The shape below is the CONTENT and the ORDER, and neither changes with the
container.** What changes with the container is how each part is REALIZED. The
content and the order are settled here; the docx realization is settled in the
subsections that follow; and where no document can be built, this same content in
this same order survives into structured markdown per 8.6.

    <the incomplete banner, where Stage 12.1 produced this artifact; FIRST,
     above everything, per Stage 12.1>

    <the front panel: the period and scope header naming ORG_NAME and the
     operating window; the population scored, its mode and which detection test
     decided it; and, where two periods are compared, the exit test result from
     Stage 4 item 2 with the state the run believes and its evidence; and the
     container actually produced, wherever it was not the document>

    <degradation block, where the run was degraded; first, not buried>

    <a PAGE BREAK, so that the copy region begins on its own page>

    <the FIELD INDEX: one line per entry of FORM_FIELDS, in that set's order, naming the field as the destination system names
     it, its limit, its count, and OVER by n characters where it is over>

    <the SELECTION SENTENCE required by D2, and the GROUND STATEMENT required by
     2.3 carrying the full MOVING_GROUND_NAME, its short form and what is known
     about its movement; both immediately above the first block, neither inside
     one>

    <the copy region: the drafted form sections in FORM_SECTIONS order, and inside
     each section every FIELD of FORM_FIELDS belonging to it as its OWN BLOCK; and each
     block is exactly three parts in exactly this order, the HEADING, the FIELD
     TEXT, and the COUNT CAPTION carrying that field's count and limit; and
     nothing sits between the heading and the text, between the text and that
     field's own caption, or between that caption and the next heading>

    ----- the value of SUBMISSION_BOUNDARY_BANNER -----

    FOCUS               forward-looking commentary. NOT a section of the form.
    ITEMS TO VERIFY     every unconfirmed proposal removed for want of an answer,
                        labelled as a proposal, carrying its confidence and the
                        question that would confirm it, per 2.20 and never in a
                        copy block; every placeholder; every MEDIUM or LOW
                        confidence claim;
                        every superlative with its tie count; every reconstructed
                        objective and date; every run-rate comparison with both
                        bases; every rung weaker than the default, named; every
                        unbound value with its degradation notice; every stale
                        reference; every unopened attachment with the paths tried;
                        every learned stem proposed for the shared dictionary
    METHOD              what was computed from the person's own data and what was
                        supplied as a binding, per METHOD_OWNER_STATEMENT; the
                        container actually produced and which rung of 8.6 it came
                        from; the probe record in full; and the verification
                        record from 7.6, every assertion with its result and every
                        not-applicable with its reason
    CONTACT             MSG_AUTHOR_LINE, naming BINDING_OWNER_NAME and
                        BINDING_OWNER_CONTACT, with TUNING_INVITATION

**The items come first; everything explanatory goes after.** See SD-CTR-14. **The
audit trail is exhaustive by design and sits at the very end.** See SD-CTR-15.

**Nothing below the banner is ever inside a copy block**, so that it cannot travel
into the destination system by accident. See 2.20.

**Every artifact carries the owner's contact line and an invitation to tune.** See
SD-CTR-19. **The method is built to be calibrated, and local reality is an INPUT
rather than a guess.** See SD-CTR-20. **Transparency exists so a disagreement can be
traced rather than argued.** See SD-CTR-21.

### THE FRONT PANEL IS ONE LINE PER DISCLOSURE, AND THE COPY REGION STARTS ON THE FIRST PAGE

**Nothing is dropped from the front panel and nothing is softened. What is capped is
its LENGTH ON THE PAGE.** This exists because two rules that are both right pull
against each other: every disclosure above is required to appear before the content,
at full prominence, and SD-CTR-14 says the items come first with everything
explanatory after, while SD-LNG-03 and guardrail 6 say never to open with methodology
or caveats. A run that satisfies the first literally puts nineteen hundred words in
front of the first thing a person has to paste, and the person scrolls past all of it.

**THE RULE. EACH DISCLOSURE GETS ONE LINE ON THE FRONT PANEL, AND ITS FULL FORM SITS
BELOW THE BOUNDARY IN THE VERIFICATION LIST.** The line is a statement, not a
heading and not a summary of a heading: it says the thing, in the reader's language,
in one line, and it names where the full form is. **A disclosure that cannot be said
in one line is still said in one line, and the line says which part is the whole
story**, because a reader who reads nothing else must not be misled by what they read.

**THE ORDER IS FIXED, so two runs are comparable and so a reader learns where to
look.** Any disclosure that does not apply on a given run is simply absent, and no
placeholder line stands in for it:

1. The incomplete banner, where Stage 12.1 produced this artifact. It is not one of
   these lines: it is the first content in the artifact, above the panel, per Stage
   12.1, and it keeps its full form there.
2. The period and scope, with ORG_NAME and the operating window.
3. The IMPOSSIBLE PERIOD line, where the resolved period's end postdates the run date,
   naming both dates.
4. The population scored, its mode, and which detection test decided it.
5. The exit test result, where two periods were compared, with the state believed and
   its evidence named in one clause.
6. The cold-start line, where a cold-start test fired, with the figure that fired it.
7. The not-workable reading used by each part of the document, with the both-ways
   figures where one exists.
8. The degenerate-scope line, where the scope is below the ranking floor or the unit
   of business is coarser than the reader.
9. The peer-path line: which path produced the peer level, the level and count
   actually used, and where a level was superseded per SD-SPN-16.
10. The container actually produced, wherever it was not the document, with its rung.
11. The provisional label, with what it is provisional on.
12. The degradation block: **a LEADING COUNT LINE, and then ONE LINE PER DEGRADED
    CAPABILITY, each of those lines naming all three things reference/capability-probe.md 4.2
    requires, which are what was unavailable, what it changed, and what the reader
    should do about it.** The count line does NOT replace the per-capability lines and
    is never printed instead of them: a panel carrying only a count and the single
    most consequential effect drops the "what to do" statement for every degradation
    but one, which 4.2 calls non-compliant. The per-capability detail IN FULL, with
    the probe evidence, the rung taken and the alternatives tried before it, sits
    below the boundary in METHOD. **reference/capability-probe.md 4.1 governs this line's form,
    and where any panel ordering in this file disagrees with it, that file governs and
    the ordering here is stale.** This is the one panel entry that is a block of lines
    rather than a single line, and the one-line cap in this subsection applies to each
    of its lines rather than to the block.
13. The sentence saying where a selection starts and stops, per D2, which sits
    immediately above the first block rather than in this list.
14. The GROUND STATEMENT required by 2.3: the full bound MOVING_GROUND_NAME, its
    short form, what is known about its movement this period, and that every figure
    below was measured against it. Like item 13 it sits immediately above the first
    block rather than in this list, in the panel label styling and never as a
    copyable block, so that the last thing a reader passes before the first thing
    they paste is what moved underneath the numbers.

**THE TEST: THE COPY REGION BEGINS ON ITS OWN PAGE, AND THE ASSERTION IS RUN OVER THE
BREAK STRUCTURE, BECAUSE THAT IS THE PART A DOCUMENT ENGINE CAN ACTUALLY READ.** A
page break sits immediately before the copy region opens. **WHAT THE RULE IS FOR IS
THAT NO FRONT-PANEL DISCLOSURE, AND NOTHING FROM BELOW THE BOUNDARY, SITS BETWEEN THAT
BREAK AND THE FIRST FIELD BLOCK**, so a reader reaches the first thing they have to
paste without scrolling back through the audit. Everything else in this test serves
that one statement.

**WHY IT IS NO LONGER WORDED AS A PAGE TEST.** A document container computes
pagination at RENDER time and not at save time, so "on the same page" is not an
attribute any document library can read back from a saved file. **A test that calls
itself mechanical and names an unreadable attribute is a test with no mechanism**, and
the run that meets it can only assert its own intention, which 7.6 forbids in terms.
What IS readable from the built artifact is the ordered sequence of paragraphs and the
breaks between them. So the assertion is three readable things: the break EXISTS
immediately before the copy region; every paragraph between that break and the first
field block is a member of the PERMITTED OPENING SET below; and there is NO FURTHER
page break among them. That is checkable, it is checkable from text and paragraph
order without DOCUMENT_INSPECT, and it is true of exactly the documents the old page
wording was reaching for.

**THE PERMITTED OPENING SET IS CLOSED, AND IT IS A SET RATHER THAN A COUNT:**

| # | What may sit between the break and the first field block | When it is present |
|---|---|---|
| 1 | The FIELD INDEX | Always. |
| 2 | The selection sentence of item 13 | Always, per D2. |
| 3 | The GROUND STATEMENT of item 14 | Always, per 2.3 and gate G19. |
| 4 | The SECTION HEADING of the first drafted section | Where 8.1.1 requires one, which is where that section yields SEVERAL fields. Suppressed where it yields exactly one, per 8.1.1. |
| 5 | The FIRST FIELD BLOCK, with its own heading and its count caption | Always. The caption is part of the block, per D3. |

**ITEM 4 IS WHY THIS IS A SET AND NOT A LIST OF FOUR THINGS, AND IT IS THE DEFECT THIS
WORDING REPAIRS.** The enumeration used to name four items and mean five. 8.1.1
requires the blocks of a ONE-TO-MANY section to be grouped under that section's own
heading, the objectives section is a one-to-many section on the ordinary run, and that
heading sits immediately above the first field block, which is inside the span this
test governs. **The two rules could not both be satisfied by any arrangement, and the
test therefore FAILED A CORRECT DOCUMENT.** Measured on a real run: four objective
fields under one objectives section, the section heading present and required by
8.1.1, and the first verification pass failing on this enumeration while the document
was right under every rule that produced it. **A TEST THAT FAILS A CORRECT DOCUMENT IS
WORSE THAN NO TEST**, because the only remedies available to the run are to disable it
or to record it as passing on something other than what it says, and both of those
teach the next implementer that this assertion may be ignored. The section heading is
what gives way to nothing: dropping it leaves several identically shaped boxes with
nothing saying which part of the form they belong to, and moving it above the break
separates a heading from the only blocks it exists to group.

**WHAT IS STILL FORBIDDEN IN THAT SPAN, WHICH IS THE WHOLE CONTENT OF THE RULE:** any
front-panel disclosure line, any part of the verification list, any METHOD content,
any proposal, any bracketed placeholder, any second field block's heading before the
first block's text, and any second page break. **A paragraph in that span that is not a
member of the permitted set FAILS, whatever it says**, and a member of the set that
appears out of the set's order fails as well, because the order is what makes the
ground statement the last thing a reader passes. Read back from the built artifact as
V7 in 7.6.

**WHY THIS TEST AND NOT THE ONE IT REPLACES.** The rule used to say the first field
block begins on the FIRST PAGE of the document, and that test cannot be met on the run
3.3 calls the worst case and the most likely one. Measured, on a real first run at an
unbound organization: twelve applicable panel disclosures, a degradation block of
eight capability lines that item 12 and reference/capability-probe.md 4.2 both require, and the
Stage 12.1 banner above all of it put the first field block on page three of thirteen,
with every line already one line and nothing droppable. The old test's only remaining
remedy was to report its own failure in one line, which told the reader the
configuration was unbound, which the provisional label two lines above had already
told them, and did nothing about the two pages between them and the first thing they
have to paste. **A page break costs nothing, drops no disclosure, compresses nothing
into a line it does not fit, and delivers what the rule was actually for**, which is
that a reader reaches the first block without scrolling through the audit.

**THE PANEL IS STILL CAPPED AT ONE LINE PER DISCLOSURE and every full form still sits
below the boundary**, because the reason for that cap was never only the page count:
a panel a reader scrolls past is a panel a reader does not read, whichever page it
ends on. **Where the panel itself runs to more than one page**, that is reported in
one line, since a run carrying that many live disclosures is telling the reader
something about the state of the configuration; it is not a licence to drop one.

**THE FULL FORM IS NOT OPTIONAL AND IS NOT SHORTER.** Everything the panel used to
carry in full is carried in full in the verification list, under a heading naming the
same thing the panel line named, so a reader who wants the whole of one disclosure
finds it in one place. **Cap the panel, never the disclosure.** A disclosure trimmed
to fit a panel is the failure this rule exists to prevent, and it is worse than the
long panel it replaced.

### The docx realization, requirement by requirement

**Each subsection below says how ONE requirement of reference/output-contract.md PART 3 is
realized in a document. The requirement's STANDARD lives in that file and is not
restated here.** What lives here is the mechanics: the thing an implementer has to do
with headings, paragraphs and styles to make the standard true.

### D1: one block per field

**Every entry of FORM_FIELDS is its OWN BLOCK**, in that set's order, grouped under its section's heading, **under a heading that names the
field EXACTLY as the destination system names it**, taken from the bound form spec
through FORM_SPEC_SOURCE. Not a friendlier name, not a shortened one, not a name
improved for readability. The person is going to match the heading against a label on
a screen, one at a time, twelve times, and a heading that has been improved costs them
the match. Header strings are byte-identical between runs, per SD-CTR-09.

**THE UNIT IS THE FIELD AND NOT THE SECTION.** A section holding four objective boxes
produces FOUR blocks, not one, and a run that produces one block for that section has
produced a document nobody can paste from. **Where a section yields several fields of
the same kind, each heading is the destination system's own name for the field
followed by the index the form itself uses**, so that four blocks are four
distinguishable boxes rather than four identical headings. The section's own heading
sits above them, carries no count caption, and is not a field heading.

**Where FORM_SPEC_SOURCE is UNBOUND**, the generic section set in 8.1 supplies the
names, **and the document says so ON ITS FACE**: on the front panel, above the field
index, and once in METHOD. The wording tells the person to check every heading against
the live form before pasting anything, because **a heading with no counterpart on the
live form must never travel into the record** (SD-CTR-22, SD-CTR-23). A section the
live form carries and the bound list does not is not drafted at all and is named as
not drafted, per 8.1.

**One field, one block, and no more.** A field split across two blocks cannot be
selected in one drag, which defeats the whole shape. An objective that will not fit
one field is not two blocks: it is two objectives, or a measure moved out, per
OVER_LIMIT_REMEDY in 1.5.

### D2: the block is copyable as a unit, which is the whole reason the document exists

**THE BLOCK HAS EXACTLY THREE PARTS IN EXACTLY THIS ORDER: THE HEADING, THE FIELD
TEXT, AND THE COUNT CAPTION.** reference/output-contract.md PART 3.3 settles that shape and the
reasoning for it, including the three placements it forbids; this subsection is the
mechanics.

**WHAT A READER SELECTS FROM THE END OF THE HEADING TO THE START OF THE COUNT CAPTION
IS EXACTLY WHAT GETS PASTED.** That sentence is the requirement, and the caption is
what makes the end of the selection VISIBLE rather than something the reader has to
guess at. Everything below is the mechanics of making it true.

- **The field's text is ONE CONTIGUOUS RUN**: one paragraph, or a run of paragraphs
  that are all the field's own text. **Nothing is interleaved.** No commentary, no
  rationale, no lineage line, no coaching note, no proposal, no bracketed aside, no
  bullet the destination form will not accept, and no character outside the set
  ALLOWED_CHARACTER_RANGE permits.
- **The count caption is the block's LAST line**: below the field text, above the next
  heading, in the caption style, reading `n of N characters`, and it may name the
  field it belongs to. **It is never in the heading line and never above the field
  text.** A count in the heading destroys the one thing the heading is for, which is
  matching the destination system's own label; a caption above the text is picked up
  by every drag that starts at the heading, which is how every reader starts, and that
  was built and measured before the shape was settled.
- **The caption is a VISIBLE STOP LINE, and that is why it works below the text where
  it does not work above it.** A reader drags downward from under the heading and
  stops AT a line in a different style; the same line above the text is one they have
  already crossed before they notice it. The trailing-metadata worry is answered by
  position: the caption is not adjacent to the start of the paste target, it is
  adjacent to its end, where the reader is looking.
- **Nothing sits between the heading and the field text, nothing sits between the
  field text and that field's own count caption, and nothing sits between the count
  caption and the next heading.** No separator, no rule, no note, no spacer paragraph
  carrying text. The only thing that may sit between one field's text and the next
  field's heading is that field's OWN count caption, which belongs to the block above
  it and to no other.
- **The lineage line is not in the block.** LINEAGE_LINE_PLACEMENT is
  commentary_outside_the_field, per 1.5 and SD-LNG-11. It is still reported, because
  it is what the person says out loud in the review conversation; it is reported
  BELOW the boundary.
- **Where the destination field is plain text, the block is plain text.** No
  formatting inside a block that the form will strip or mangle: no bold inside the
  field text, no bullet glyphs, no smart punctuation, no tab characters. The
  formatting this document carries lives in the headings, the captions and the panel,
  which are the parts nobody pastes.

**THE DOCUMENT SAYS ON ITS FACE WHERE A SELECTION STARTS AND STOPS.** One sentence,
once, immediately above the first block of the copy region, in plain words and not as
a caption on any block: **select from the end of a heading down to the count line
under it, and paste that.** It names the caption as the stop line and says that the
caption itself is never pasted. **A copy contract nobody was told about is a
convention, not a contract**, and the person doing the pasting is the one person who
has to know it. The sentence is not inside any block, carries no field heading style,
and is repeated once immediately below SUBMISSION_BOUNDARY_BANNER only to say that
nothing below that line is ever selected at all.

**This is the requirement everything else in 8.3 defers to.** If a presentation
choice would make a block prettier and less copyable, it is not made.

### D3: the limit and the count are shown

**Every block states its character limit and its CURRENT COUNT in its COUNT CAPTION,
which is the block's LAST line, below the field text and above the next heading, in
the form `n of N characters`.** A block over its limit is marked **OVER by that many
characters** and is a **PUBLICATION-BLOCKING FAILURE, not a warning**.

**The gates that block it are named rather than implied.** G6 FIELD LIMITS in 7.2 is
the draft-side gate: every emitted field carries its exact count and every count is
at or under the confirmed limit. `review.field_block_over_limit` in 7.4.2 is the
built-artifact gate, asserted as V3 in 7.6. **One over-limit block stops the
publication**, and the run does not resolve it by trimming silently: it applies
COMPRESSION_ORDER, and where the field still does not fit it applies
OVER_LIMIT_REMEDY.

**The counting rule is 1.5's and is not restated here.** Count the exact string that
will be pasted; spaces, punctuation and permitted line breaks all count, at one
character each. 1.5 also owns TARGET_FILL_RATIO, COMPRESSION_ORDER and
NEVER_CUT_LIST. **This subsection owns only WHERE the number is shown**, and that is
settled by reference/output-contract.md PART 3.3 and realized in D2 above: **the count caption
is the last line of the block, below the field text.** Not in the heading, not above
the text, not above the heading, and not omitted in favour of the index.

**THE COUNT IS NOT MOVED INTO THE FIELD INDEX INSTEAD.** The index carries every count
as well and the two reconcile under V4, but **a reader pasting field six is looking at
field six and not at an index four pages up**, and a limit that lives only in an index
is a limit nobody reads at the moment it matters. Both statements exist, both are
generated from the built blocks, and a disagreement between them stops publication
rather than being resolved by preferring one.

**The count is written to read correctly at every value**, per SD-LNG-13. A block at
zero characters says so as its own sentence rather than as a plural with a nought in
it, and an empty drafted section still ships its heading and its one explanatory line,
per 8.2, SD-CTR-07 and SD-FMT-07.

### D4: the limits come from the binding, never from a guess

**The limit shown against a block comes from FIELD_LIMITS, or from
PERSON_CONFIRMED_FIELD_LIMITS where the person confirmed it for that run.** Never from
a guess, never from this file's illustrations, and **never read live from the
destination system**, which this skill does not query.

**The precedence, stated explicitly because two variables can supply one number.**
Standing rule S9 governs: precedence runs downhill from evidence to convention.
**PERSON_CONFIRMED_FIELD_LIMITS for that run OUTRANKS the bound FIELD_LIMITS default,
which outranks the documented default in the schema.** The person has the form open
and can read the counter beside the box in five seconds; that answer is worth more
than any assumption in this file, and 1.5 already requires it to be asked once per
run. **It never writes back to the organization tier.** Where a documented default
would change a decision a bound value already decided, the bound value stands and the
notice names the narrowing rather than a substitution, per S9 and SD-CTR-24.

**Where a field's limit is not bound at all**, the block says the limit is UNKNOWN and
shows the count alone. It does not invent a plausible limit, and it does not omit the
count because the limit is missing: **the count is still the only number that tells
the person whether they are close to a boundary they can see on their own screen.**
The unknown limit is named in the field index and once in METHOD, and G6 records the
field as uncheckable rather than as passed, per G2 and SD-EFF-03.

### D5: nothing below the submission boundary is inside a field block

**This is already doctrine in 2.20 and is cited rather than re-argued.** Content that
must not travel into the destination system sits BELOW SUBMISSION_BOUNDARY_BANNER,
never inside a copy block: the forward-looking focus section, the verification list,
every unconfirmed proposal permitted there under the five conditions in 2.20, the
lineage lines, **every bracketed placeholder**, and the method and contact sections.

**THE BRACKETED PLACEHOLDER HAS EXACTLY ONE HOME AND IT IS HERE.** reference/output-contract.md
PART 3.4 settles it and this is the mechanics. G2 requires a number that traces to no
cell and no tool result to become a bracketed placeholder naming its source; D2
forbids a bracketed aside inside a field block. **Neither bends. The claim and the
number separate:**

1. **The CLAIM ships in the copy region WITHOUT the number**, in the person's own
   words. A non-numeric action clause the person themselves wrote is their evidence
   and is not an inference by this skill, so it stays; what does not travel into a
   permanent record is an unsourced quantity dressed as a fact.
2. **The NUMBER goes below the boundary as a bracketed placeholder**, carrying the
   figure exactly as it was stated, WHO or WHAT stated it, and THE QUESTION THAT WOULD
   SOURCE IT. It is listed in ITEMS TO VERIFY beside the other unsourced material.
3. **The block and the placeholder are linked by the field's own heading**, so a
   reader who sources the number knows which box it goes back into and does not have
   to re-read the whole review to find out.

**WHY THE NUMBER IS NOT SIMPLY DROPPED.** On a run with no mail, no chat and no
action-evidence column, **a person's own note is the only evidence of what they did**,
and a seam that strips every figure out of it silently deletes their year. Below the
boundary it is preserved, visible, and clearly marked as not yet sourced. **A number
deleted because it had nowhere to go is the most expensive kind of silence this skill
can produce**, because nobody can see that it happened.

**The docx consequence, which is what this subsection adds:**

- **Headings below the boundary are VISUALLY DISTINCT from field headings.** A
  different heading style, at a different level, and they never carry the count and
  limit caption that marks a copy block. **A reader must never have to read a heading
  carefully to tell whether it is a thing they are supposed to paste.**
- **No text below the boundary is formatted as a copyable field.** Nothing down there
  is one contiguous run under its own heading with nothing between it and the next
  heading, because that shape is the signal that says paste me.
- **The boundary itself is stated once, in the document, in plain words**, and it is
  not a decorative rule. It says what is above it and what is below it and what
  happens to each.
- **A proposal below the boundary is labelled as a proposal, in the label itself**,
  carries its confidence and carries the question that would confirm it, per 2.20. It
  is never first-person text, because first-person text below a boundary is the thing
  most likely to be pasted by a person in a hurry.

**EVERY GATE THAT REQUIRES TEXT SAYS WHICH SIDE OF THE BOUNDARY ITS TEXT GOES, AND
THEY ARE COLLECTED HERE SO NO GATE HAS TO BE READ TWICE.** A gate that demands
something be stated and does not say where produces exactly the seam G2 used to
produce: a required string with no compliant home.

| Gate | What it requires be stated | Which side it goes |
|---|---|---|
| G1 | The counterfactual rung each figure used, and the comparison itself | INSIDE the block, as part of the claim, because the comparison is the claim, and written as a thing rather than as a rung key per 10.2.1. The rung NAME is inside where the claim's own words carry it, and its full disclosure, with the rung key and the claim strength it authorized, sits below the boundary |
| G2 | An unsourced number, its source and the question that would settle it | BELOW, always, as a bracketed placeholder. The claim ships above without the number |
| G5 | An UNGRADABLE flag and its proposed rewrite | The FLAG is inside the block, in words, because the person's record has to say the measure could not be graded. The proposed REWRITE is below, as a proposal, with the question that would settle it |
| G7 | A benchmark whose figure is UNRESOLVED or UNPAIRED | BELOW, in the verification list only, never in the body |
| G12 | The tie count behind a superlative | INSIDE, with the superlative, because a superlative without its tie count is the overclaim |
| G13 | The unit of the figure, and the band it was classified against with that band's unit | The UNIT is INSIDE, named in the person's own words per 10.2.1, because a figure with no unit is not a figure. The BAND, its unit and the quantity form are BELOW, with the rung disclosure, because a band is the method checking itself and a reader verifying the arithmetic is already below the boundary |
| G15 | Any proposal not in state CONFIRMED | BELOW, labelled as a proposal, with its confidence and its question. Stripped from the copy region entirely |
| G19 | The named ground and what is known about its movement | The SHORT FORM of the ground and the movement statement are INSIDE, with the claim, and where nothing is known the words saying so are inside too. The FULL bound MOVING_GROUND_NAME is named in full ABOVE the copy region in the GROUND STATEMENT that sits immediately above the first block, and again BELOW the boundary in METHOD with its source and read date. Per 2.3, which settles the placement once |
| G22 | The peer level, its count, and any superseded level per SD-SPN-16 | The count and the level are INSIDE where a figure reads them, per 2.13. The path that produced the level, and every level tried, are BELOW |
| G24 | A CONTRADICTED item: the person's own statement, what the resolved cell says with its column and unit, and the question that would settle it | BELOW, always, both readings together under one heading. **Nothing of the item goes above**, not the disputed value, not a softened version of it and not a blended sentence; and the item's exclusion from the counts above is LISTED below with its reason. The claim the item would have carried either ships above without it or does not ship |

**Nothing in the INSIDE column is a bracketed aside, a lineage line, a rationale or a
note.** Each one is part of the sentence a person is going to paste, in their own
register, and if it cannot be written that way it belongs below the boundary instead.
**WHAT "IN THEIR OWN REGISTER" MEANS IS SETTLED IN 10.2.1 AND IS NOT A MATTER OF
TASTE**: that subsection carries the plain form of every mandatory in-block
disclosure, and a block written in the method's vocabulary fails the gate that
required the disclosure, not merely the style rule. **A disclosure is never dropped to
satisfy the register**; where it cannot be said plainly it moves below the boundary in
full and the claim above is worded so that it does not need it.

Asserted as V5 in 7.6 and stopped by `review.boundary_heading_leak`. Gate G15 tests
the same boundary from the other side.

### D6: the panel styling matches the spreadsheet palette

**Same palette, same variables, no restated values.** The title band takes
COLOR_TITLE_BAND; section headers take COLOR_SECTION_HEADER; label fills take
COLOR_LABEL_FILL; the ink on every one of those bands takes COLOR_HEADER_TEXT; body
text takes BODY_FONT at BODY_FONT_SIZE; the panel title takes TITLE_FONT_SIZE. **The
colour values are NOT restated in this file**, in prose, in a table or in an example:
the variables are named and the values live in the schema.

**AND THE DIRECTION OF EACH PAIR IS PART OF THE PALETTE RATHER THAN PART OF THE
SPREADSHEET.** SD-FMT-29. Every band named above is a LIGHT band and COLOR_HEADER_TEXT
is the DARK ink carried on it, per reference/output-contract.md element 15 and PART 2.8, and
every colour this skill writes anywhere is written with an EXPLICIT OPAQUE ALPHA, in
the `FFRRGGBB` form PART 2.9 states, never a transparent one. **THE RENDERING RISK IS
NOT A SPREADSHEET RISK AND THIS DOCUMENT INHERITS ALL OF IT**: a review is opened in a
viewer, a converter, a preview pane, a browser and a printer exactly as a workbook is,
so a band that reads only while BOTH its fill and its font colour arrive fails here in
the way it was measured failing there. A light band under dark ink stays readable when
the FILL does not render, because the dark ink still sits on the page, and it stays
readable when the FONT COLOUR does not render, because the container's default dark
ink still sits on the light band. The arithmetic, the two floors and the values are
2.8's, 2.9's and the schema's, and this file states none of the three.

**Why it matters enough to be a requirement.** Someone holding this review and a work
plan from the planning skill in the same week must see ONE SYSTEM rather than two
tools that happened to run. The palette is the cheapest possible carrier of that, and
it costs nothing when it does not fire, per governing rule G5.

**Where the palette cannot be applied or cannot be read back, it is recorded as NOT
APPLIED rather than as failed**, and the run continues at rung 2 of 8.6. **Styling is
presentation and presentation degrades.** The copy contract does not, and the two are
never traded for each other.

### The FIELD INDEX, because a document has no sheets

**A workbook lets a reader see every field at once by putting them in a grid. A
document cannot, so it states the same thing as a list.**

**The field index sits at the TOP of the document, immediately after the front panel
and the degradation block, and BEFORE the copy region.** One line per submission
entry of FORM_FIELDS, in that set's order: **the field's name as
the destination system names it, its limit, its count, and OVER by n characters where
it is over.** A field whose limit is unbound shows its count and says the limit is
unknown, per D4.

**THE INDEX IS THE PLACE FORM_FIELDS IS PRINTED**, per 8.1.1. It lists
FIELDS and not SECTIONS, it says how many boxes there are, and where a section yielded
several fields it shows them individually with the form's own index on each. **A
reader whose form has five boxes and whose index has six lines can see the
disagreement before they paste**, which is the whole reason the derivation is printed
rather than merely performed.

**What it is FOR.** A reader checks the WHOLE submission in one glance before pasting
anything, rather than discovering the eleventh field is over after pasting ten. That
one glance is the difference between a two-minute submission and a re-draft, and it is
why the index leads rather than trails.

**The index and the blocks MUST AGREE**, field for field and count for count, **and
the reconciliation is VERIFIED** as V4 in 7.6 and stopped by
`review.field_index_disagreement`. **Two statements of one number that disagree are
not a formatting problem**: the run publishes neither reading as fact, prints both,
and stops, per SD-RUN-09. The index is generated FROM the built blocks rather than
from the draft, which is the only construction in which agreement means anything.

**The index is not inside a field block and is never itself pasted.** It carries the
same visual treatment as the panel, per D6.

### Headings are real heading styles, and page breaks are not separators

**Every heading in this document is a REAL DOCUMENT HEADING STYLE, not a bold
paragraph pretending to be one.** A bold paragraph looks identical and navigates
nothing. **A reviewer working twelve fields uses the navigation pane to move between
them**, and a document whose headings are bold body text gives them an empty outline
and a scroll bar. The heading levels are consistent: field headings at one level,
below-boundary section headings at a different and visually distinct level, per D5.

**PAGE BREAKS ARE NOT USED TO SEPARATE FIELDS.** Two reasons, and both are practical:

- **A field split across a page boundary is still ONE CONTIGUOUS SELECTION.** A drag
  from under the heading to above the next heading crosses the page break without
  noticing it, and nothing about the paste changes. The page boundary is a rendering
  artifact, not a structural one.
- **A page break between every field makes a twelve-page document out of two pages of
  text.** That is worse to read, worse to scroll and worse to print, and it buys
  nothing at all.

A page break is used where a page break is genuinely meant, and there are exactly
two places:

- **BEFORE THE COPY REGION**, always, so that the field index, the selection
  sentence, the GROUND STATEMENT and the first field block open a page of their own
  with no panel disclosure on it. This is the mechanical test in 8.3 and it is not
  conditional on the panel's length: a break that is only inserted when the panel runs
  long makes two runs at one organization look like two different documents.
- **BEFORE THE SUBMISSION BOUNDARY**, wherever the copy region ran long enough that
  the boundary would otherwise land mid-page and be missed.

Neither of those separates one FIELD from another, which is what the ban above is
about.

### The document's name, its file name and its own sections

**The title band carries the REVIEW entry of DELIVERABLE_NAME**, which is a mapping
keyed by skill and never a single shared string, per SD-CTR-30: one artifact name
across three different documents titles two of them wrongly. **THE TITLE BAND IS THE
FIRST CONTENT IN THE ARTIFACT.** Where Stage 12.1 produced this document, the selected
form of INCOMPLETE_BANNER_TEXT sits IMMEDIATELY BELOW IT, in the same band's styling,
above the front panel and above everything else, per Stage 12.1, which settles the
order once and which this sentence agrees with rather than re-deciding. **Two rules
wanted the first line and the silence between them made one of them wrong on every
run**; the document is named first and qualified second. **The file name follows
OUTPUT_FILENAME_PATTERN**, carrying the scope label, its code, the period and any
qualifier so that two runs never collide, and the file is written to OUTPUT_DIR and
never to SCRATCH_DIR, per 1.2.

**Where TAB_CONTRACT's REVIEW entry is bound, it names the DOCUMENT'S OWN SECTIONS**,
and the copy region is the section of it that carries the FIELD blocks, one per
entry of FORM_FIELDS.
**FORM_SECTIONS never becomes TAB_CONTRACT and TAB_CONTRACT never reorders the copy
region**: one is the destination form's own list of fields and the other is this
document's list of sections, they answer to different owners, and a run that conflates
them ships a document whose headings match nothing on the form.

**Every unit noun in the document reads its variable and none is hard-coded**, per
reference/output-contract.md PART 6.

## 8.4 Benchmark visibility without benchmark credit

Specified as doctrine in 2.14. In the output it resolves to three forms:

    ALLOWED    The entity's own result stated with its benchmark delta and the unit
               named.
    ALLOWED    A benchmark figure as the denominator of a share statement.
    FORBIDDEN  A standalone sentence whose subject is the benchmark or its
               movement, however well benchmarked.

**The subject of the sentence decides.** Gate G1 enforces it and gate G7 enforces
the visibility half.

## 8.5 What the reply says

The conversational reply that accompanies the artifact is at most
CHAT_REPLY_MAX_LINES lines. It never pastes the write-up. Its first line names the
count of degradations and the single most consequential effect, where the run was
degraded. It leads with the finding, never with methodology. See SD-CTR-16 and
SD-LNG-03.

**That first line is a templated sentence carrying a count and it is written to
agree at every value**, per SD-LNG-13: "1 thing was degraded" and "3 things were
degraded" both read correctly, and where nothing was degraded the line is not a
plural with a nought in it but its own sentence saying the run was not degraded.
**Test it at zero, at one and at many before it ships.** Zero is the quiet run, and
the quiet run is where a reader is most inclined to doubt the tool.

**The first line also names the CONTAINER actually produced wherever it was not the
document**, per 8.6 and 3.1: which rung was taken, and what it changed. **A person
who asked for a review and received structured markdown must learn that from the
first line, not from the file extension.** The reply still never pastes the write-up,
per CHAT_REPLY_MAX_LINES and SD-CTR-16, and it still leads with the finding rather
than with the container, per SD-LNG-03: the container is named in the same line as
the degradation count, not given a line of its own.

## 8.6 Where no document can be built

**THE LADDER IS reference/capability-probe.md 2.2a, AND ITS RUNGS ARE NOT RESTATED HERE.**
DOCUMENT_WRITE is the capability, probed at position 6, and 2.2a gives its five rungs
from the full document down to naming every path attempted. **Rung 3 is where the
work is**, and its markdown equivalent, with what identical information means for a
copy contract, is 2.2a.1. **The styling half resolves separately, per 2.2b**, which
is DOCUMENT_INSPECT, and 7.6 owns what that does and does not excuse.

**This skill reads 2.2a and 2.2b and NEVER 2.1 or 2.2**, per rule P1c and 3.1,
because OUTPUT_MEDIUM is keyed per skill. An absent SPREADSHEET_WRITE costs this
skill nothing at all, and a run that reports it as blocking has degraded a
deliverable that was never at risk.

**What this section adds, and what is genuinely this skill's own**, is which of THIS
artifact's parts sit on which side of the information-versus-presentation line, and
where the rung gets announced.

**WHAT SURVIVES EVERY RUNG, AND WHAT DOES NOT.** This is the whole distinction and it
is stated once, here.

- **The COPY CONTRACT is INFORMATION.** One block per entry of FORM_FIELDS; the section order of FORM_SECTIONS; a heading naming the field as the
  destination system names it, with the form's own index where a section yields
  several; the block individually selectable with nothing interleaved; **the count and
  the limit in a caption that is the block's LAST line, below the field text**; the
  sentence saying where a selection starts and stops; **the GROUND STATEMENT required
  by 2.3, which is what stops a reader taking a number as the writer's own
  achievement**; nothing below the boundary inside a block. **It survives intact to rung 4 and is never traded for anything.**
  In structured markdown the caption is the line immediately under the field's text
  and before the next heading, which is the same shape in a container that has no
  caption style.
- **The STYLING is PRESENTATION.** The palette, the heading styles, the caption
  placement, the navigable outline, the page-break discipline. **It degrades, and
  every degradation of it is named.** The PAGE BREAK before the copy region is
  presentation and a container with no pages cannot carry it; **what it was for is
  information and survives**, so in structured markdown the field index, the selection
  sentence, the GROUND STATEMENT and the first block still follow the panel with
  nothing of the panel interleaved, and the mechanical test in 8.3 is recorded NOT
  APPLICABLE with that reason rather than failed.

**A run that drops a count to save a container has traded the thing the artifact is
FOR against the thing it is WEARING.** That is the inversion this section exists to
prevent, and it is the same inversion Stage 12.1 prevents on the question axis.

**Rung 3 is not a summary, and the word identical is meant literally**, per 2.2a.1.
Three consequences that are specific to THIS artifact and are therefore stated here:
**the FIELD INDEX ships**, because a reader still needs to check the whole submission
in one glance and markdown can hold a list; **the incomplete banner still leads and
still repeats above the boundary**, per Stage 12.1; and **no heading is renamed to
read better in plain text**, because the heading is the destination system's own word
for the field and D1 does not relax for a container change. What markdown cannot
express, the palette and the real heading styles, is recorded as NOT APPLICABLE with
its reason rather than as failed, per SD-FMT-01 and SD-EFF-37.

**THE ANNOUNCEMENT, IN THREE PLACES, EVERY TIME**, per 3.1 and reference/capability-probe.md
PART 4:

1. **The FRONT PANEL**, before the content, naming the container produced, the rung
   it came from, and what that changed.
2. **The METHOD block**, with the probe record in full and the 7.6 verification
   record beside it.
3. **The FIRST LINE OF THE REPLY**, per 8.5, naming the count of degradations and the
   single most consequential effect.

**A run that emits markdown and says so only in the chat has announced nothing**,
because the chat scrolls away and the artifact is what gets read next March.

---

# PART 9: GUARDRAILS

Each one is a NEVER, and each traces to the permanent record principle in 2. **The
list is the numbered items below and no count of them is stated here**, because the
list has already grown twice and a count in the opening line contradicts the list
under it the first time it does.

1. **NEVER fabricate an action, a number, a date, a target, a learning or a rating.**
   An unconfirmed inferred action is fabrication even when the underlying number is
   real. Missing values become bracketed placeholders naming their source, and land
   in the verification section BELOW the submission boundary, never inside a field
   block, per gate G2, 8.3 D5 and reference/output-contract.md PART 3.4: **the claim ships
   without the number and the number is carried below the boundary with its source
   and the question that would settle it.** See SD-CNF-07 and SD-CLM-24.
2. **NEVER claim the movement of a population whose composition the person did not
   choose.** See SD-CLM-03 and 2.1.
3. **NEVER attribute an aggregate above the person's scope, or above their altitude
   ceiling, to the person.** See SD-CLM-10 and 2.7.
4. **NEVER copy a prior document's structure or phrasing.** User documents are
   evidence only. See SD-PRI-33 and 2.9.
5. **NEVER evaluate or rank other named people.** Peer comparison is anonymous and
   positional. See SD-CLM-12 and SD-LNG-02.
6. **NEVER open with methodology, caveats or reconciliation.** Those are internal.
   See SD-LNG-03.
7. **NEVER assert causation from correlation.** Diagnoses are candidates for
   confirmation. See SD-CNF-05.
8. **NEVER characterize a reconstructed entry as contemporaneous logging.** See
   SD-CLM-20.
9. **NEVER backdate a reconstructed objective without flagging it as
   reconstructed.** See SD-CLM-20.
10. **NEVER write a checkpoint to the output directory.** See 1.2.
11. **NEVER publish a value whose two derivations disagreed.** Mark it UNRESOLVED,
    exclude it, and list it. See SD-RUN-09.

Further guardrails belong to the generalization and are stated with the rest so
that nothing depends on a reader inferring them:

12. **NEVER let a claim ship at achievement strength before the ground it moved
    against is named.** See 2.3 and gate G19.
13. **NEVER substitute a weaker counterfactual rung for a stronger one that failed
    without saying so and lowering the claim strength with it.** See 2.2.1.

---

# PART 10: PROSE RULES

## 10.1 Character set enforcement

**SCOPE.** This gate applies to every character of TEXT THIS SKILL AUTHORS: chat
responses, copy blocks, checkpoint contents, and every text string written into a
file, including strings placed inside binary containers. **IT DOES NOT APPLY to the
raw bytes of a binary container.** See SD-FMT-19.

**THE PERMITTED SET IS A RANGE PLUS AN EXPLICIT EXCEPTION LIST, AND BOTH HALVES ARE
READ.** ALLOWED_CHARACTER_RANGE states a printable lower and upper bound, both
tested, AND an exception list of permitted code points outside it. **The list is
non-empty: it carries code point 10, the LINE FEED.** A gate that reads the range
and ignores the list rejects a character the field-limit rule in 1.5 requires it to
count, which is the contradiction this paragraph exists to close. A one-sided upper
bound is not a range check, and a range read without its exception list is not the
permitted set.

**WHERE THE LINE FEED IS PERMITTED, AND WHERE IT IS NOT.** Permitted: inside the
text of a capped free-text field, and inside any wrapped value. Forbidden: a sheet
name, a filename, a heading, a column header, an identifier, a code, and any
single-line label. A break in one of those corrupts a lookup by name, and the sweep
rejects it there exactly as it rejects any other disallowed code point. **Code point
13, the carriage return, is NOT permitted and is NORMALISED rather than dropped**: a
carriage-return-and-line-feed pair collapses to one line feed, and a lone carriage
return becomes one line feed. It carries no meaning of its own and renders as
nothing on some engines and as a paragraph break on others, so the same string
otherwise produces two different documents. **Code point 9, the tab, is forbidden
outright**: inside a cell or a form field it is an alignment instruction rather than
content, and in any delimited export it splits one value into two.

**THE DEFAULT RULE.** Any code point that is outside ALLOWED_CHARACTER_RANGE's
printable range AND not on its exception list is transliterated to its closest
equivalent inside the range. If no reasonable equivalent exists, it is dropped and
the substitution is logged to the verification section. **This rule is exhaustive by
construction, so no character class can slip through.** Test BOTH bounds of the
range, and test the exception list, on every sweep. See SD-FMT-14.

**THE SUBSTITUTION SET**, stated as classes rather than as a closed table, because a
closed table is not exhaustive:

| Class | Treatment |
|---|---|
| Typographic dashes of any width | a plain hyphen |
| Curly or directional quotation marks, single and double | the plain keyboard equivalents |
| Ellipsis and other composed punctuation | the spelled-out keyboard equivalent |
| Non-breaking, thin, zero-width and other exotic spaces | a plain space |
| Byte order marks and other invisible marks | dropped, and logged |
| Carriage return, alone or paired with a line feed | normalised to ONE line feed where a line feed is permitted in that container, and dropped where it is not |
| Tab, vertical tab, form feed and every other control character | dropped, and logged; only the line feed is permitted, and only where 1.5 permits it |
| Arrows, bullets, middle dots and other symbol characters | the word or the plain punctuation that carries the same meaning |
| Currency, superscript and fraction characters | spelled out, or the plain equivalent |
| Accented letters in a name | transliterated to base letters |

**NAMES.** A name carrying an accent is transliterated to its base letters, **never
dropped and never truncated. Losing a name is worse than losing an accent.** See
SD-FMT-15.

**QUOTED SOURCE TEXT.** Quote the WORDS faithfully and transliterate the CHARACTERS.
**Character fidelity never outranks system compatibility.** See SD-FMT-16.

**SOURCE CONTAMINATION IS THE MAIN RISK.** Sweep any text taken from a source BEFORE
it enters a draft, not after. Spreadsheet exports write negative numbers with a
typographic minus, and an unswept minus is a sign error waiting to happen. See
SD-FMT-17.

**VERIFICATION IS MECHANICAL, NOT VISUAL.** Never approve output by reading it. Scan
every authored string programmatically and reject on any code point outside the
range. **A visual pass will not catch a non-breaking space, a zero-width space or a
byte order mark.** See SD-FMT-18.

**NEVER drop the row and never blank the field to fix a character problem.** Fix the
character. See SD-FMT-20.

Enforced by gate G11, which is the only gate that re-gates in place rather than
routing to a stage.

## 10.2 Style

- Punctuation is keyboard only: hyphens, commas, colons, semicolons, pipes,
  full stops, question marks, parentheses and quotation marks.
- Headings are Title Case where TITLE_CASE_HEADINGS is true, in the one convention that
  variable states and validates. **THE EXEMPTION FOR TABLE COLUMN HEADERS IS
  WITHDRAWN**, so a column header anywhere this skill writes one is Title Case with
  every other heading, and so is any name written to a tab by a skill that writes to
  one. **ONE EXEMPTION REMAINS: a string the ORGANIZATION BOUND ships in the case it
  was bound in**, because those are the organization's own words. A DOCUMENTED DEFAULT
  is not a bound string; it is already written in Title Case where it is documented, so
  this skill re-cases nothing at run time and SD-CTR-24 is untouched. See SD-FMT-13.
- **Measure impact; do not judge the remainder.** Use IMPACT_LANGUAGE_RULE phrasing.
  Never use a phrase from BANNED_PHRASES. Every unit matters to the person who owns
  it; this method measures which units carry the most business impact, and that is a
  measurement, not a judgment about the rest. **Write toward impact, never toward
  shame.** See SD-LNG-01.
- **Use the organization's exact vocabulary.** Terms in CONTROLLED_VOCABULARY are
  used exactly as the business writes them and are never paraphrased. See SD-LNG-07.
- Results are declarative. A result is stated, not sold.
- **Write short by default.** See 1.5 and SD-LNG-08.
- **EVERY SENTENCE CARRYING A COUNT AGREES AT ZERO, AT ONE AND AT MANY.** SD-LNG-13.
  Carry the singular and the plural of the noun with the count and select on the
  value, so "1 measure" and "2 measures" are both correct; or choose a phrasing
  whose verb does not change, such as "measures excluded: 1". **Zero gets its own
  sentence**, in the reader's language rather than the machine's: "nothing was
  excluded", not "0 items were excluded". This reaches front panel lines, empty
  section messages, degradation notices, audit lines, question preambles and any
  text carrying a count of what was affected. **Test every template at all three
  values before it ships**, which takes seconds; a template only ever exercised at
  many reads as broken on the first quiet run, which is exactly the run where the
  numbers are small enough for a person to check by hand.
- **Report the count of items dated by EACH rule separately.** Naming the split is
  what makes a rule-inversion bug visible. See SD-LNG-04.
- **Name every item that took a fallback weight and the weight it took**, so a reader
  can see which work was scored as probable rather than confirmed. See SD-LNG-05.
- **Name every item weighted zero, by name and count**, so a person can see that a
  large item was deliberately scored low rather than wonder why their biggest number
  moved nothing. See SD-LNG-06.

### 10.2.1 THE COPY REGION IS WRITTEN IN THE PERSON'S REGISTER, NOT THE METHOD'S

**This is a rule about the field blocks and about nothing else.** Everything below
SUBMISSION_BOUNDARY_BANNER is the method talking to a checker and stays in the
method's own vocabulary, exactly as it is. What a person pastes into a permanent
record is written as that person would write it.

**THE FAILURE THIS RULE ANSWERS, MEASURED.** A run that obeyed every content rule in
this file produced an objective box reading, in part, that a figure was so many
percent of target, MISS on the percent-of-target band, and as a level so many percent
of target with no label. Every clause of that was required: G1 puts the comparison
inside, G13 names the band and its unit, 2.2.4 prints both readings where they cross
in opposite directions. It came to a fifth of the box, and it is vocabulary no
producer writes and no reviewer expects in a self-assessment field. **The skill spent
all of its care on making sure nothing unconfirmed reached the box and none at all on
making sure what did reach it sounded like the person.**

**THE RULE. NO DISCLOSURE IS DROPPED; WHAT CHANGES IS ITS WORDING AND, FOR TWO OF
THEM, ITS SIDE OF THE BOUNDARY.** Inside a field block, every mandatory disclosure is
written in the ordinary words of the person's own trade. The method's own tokens, the
classifier LABEL, the BAND NAME and the band's UNIT, and the rung KEY, sit below the
boundary with the rest of the rung disclosure, which is where a reader checking the
arithmetic is already looking. **A disclosure that cannot be written in the person's
register is not thereby exempt: it moves below the boundary in full and the claim
above it is worded so that it does not need it.**

| What a rule requires be disclosed | The method's register, which never appears inside a block | The person's register, which is what is written |
|---|---|---|
| The comparison and its rung, per G1 | The rung key and the rung's number | What the figure was measured against, said as a thing: the target that was set, the typical branch, the same measure last year |
| The classification, per 2.5 | WIN, MISS, FLAT, ON PLAN, UNPAIRED, NO BASELINE as tokens | The plain consequence: short of what was asked for, ahead of it, level with it, nothing to compare it against yet. **The token itself goes below the boundary with its band** |
| The band and its unit, per G13 | The band, the deadband, the quantity form | Nothing inside the block. **The band and its unit go below the boundary in full**, and the figure inside still names its own unit in plain words, which is the half of G13 that stays |
| An UNGRADABLE measure, per G5 | UNGRADABLE as a flag word | There was no target to score this against. The flag is still inside the block, in words, and the proposed rewrite is still below |
| A target's shape and a two-way reading, per 2.2.4 | As written, as a level, the shape name | The two readings said as two readings: so much of the increase that was asked for, and so much of the level that was asked for |
| A zero target, per 2.2.4 | UNDEFINED attainment, degenerate denominator | There was no number to grow from, so this is reported as what was done rather than as a percentage |
| A superlative's tie count, per G12 | The tie count as a field | The count said as a count: the highest of the group, with the number who share it |
| The peer level and its count, per G22 | The level key and the resolved level | The group said as a group, with how many are in it |
| The ground and its movement, per G19 and 2.3 | The variable name | The short form 2.3 derives, in the trade's own words, and what is known about its movement |
| A withheld comparison, per SD-POP-19 | The variable that withheld it | Plain words saying the group was too small to compare against and how many were in it. The variable's name goes below the boundary |

**THE THREE THINGS THIS RULE DOES NOT LICENSE.** It is not permission to soften a
result, and 10.2's "a result is stated, not sold" governs both registers. It is not
permission to drop a number, a unit, a population or a count from a block. And it is
not permission to write a sentence the person did not earn: everything in the copy
region is still bound by G15, by 2.12 and by the confidence gate, and a plainer word
for a disclosure is still a disclosure. **Where the plain wording and the exact one
disagree about what happened, the exact one is right and the block is rewritten until
the plain wording is also true.**

**HOW IT IS ENFORCED, AND IT IS ENFORCED WHERE G13 IS.** The gates that require text
inside a block, G1, G5, G12, G13, G19 and G22, each test the disclosure's PRESENCE and
its SIDE OF THE BOUNDARY per 8.3 D5, and G13 additionally fails a block carrying a
classifier token, a band name or a rung key, because all three belong below. Read back
from the built artifact at Stage 12, so that a rewrite folded in at Stage 10.5 cannot
put the method's vocabulary back into a box after the draft was checked.

---

# PART 11: REGRESSION CASES

REGRESSION_CASES is a bound taxonomy of named end-to-end cases. **Run every case
before any change to this skill ships.** See SD-RUN-10. The standing set, each case
with its inputs, its expected result and the failure it catches:

**CASE 1. The environment-credit trap.**
INPUTS: an entity that grew strongly while the benchmark it sits in grew more.
EXPECTED: the label is MISS, the rate delta is negative and carries the unit
"percentage points of growth", and the claim is not worded as an achievement.
FAILURE: any output that presents the entity's raw growth as a win, or that presents
the benchmark's movement as the person's result.

**CASE 2. The person with no documentation.**
INPUTS: a person who says one sentence about their period and supplies nothing else.
EXPECTED: the evidence state resolves to FRAGMENT, the data stage is skipped,
reconstruction runs, and a real draft is produced with every objective flagged as
reconstructed and every date flagged as awaiting confirmation.
FAILURE: any halt that asks the person for a file; any silently backdated objective;
any gate that blocks the emit because it inspected an artifact this path does not
produce.

**CASE 3. The altitude ceiling.**
INPUTS: a direct-tier person whose result contributes to an enterprise goal.
EXPECTED: the consequence clause uses a verb from CONTRIBUTION_VERBS and no verb
from OWNERSHIP_VERBS.
FAILURE: an ownership verb attached to a rung above the person's ceiling.

**CASE 4. The unconfirmed action.**
INPUTS: an inferred action whose confirmation question never fires.
EXPECTED: the proposal is REMOVED as UNANSWERED, the action clause is stripped from
the copy region, and the result stands on its own without an action half. Below the
submission boundary the proposal appears once, labelled as a proposal, carrying its
confidence and the question that would confirm it, outside any copy block. Where the
person REJECTED it instead, it appears nowhere at all.
FAILURE: an unconfirmed first-person action reaching the copy region; a rejected
proposal offered back below the boundary; or an unanswered proposal stripped from
below the boundary as well, which is the gate enforcing the boundary against itself
and which costs the person the one thing they could have answered.

**CASE 5. The span-of-control error.**
INPUTS: an aggregate-tier person whose data contains a standout individual unit.
EXPECTED: the unit appears only as an illustration inside an aggregate claim, with
credit to the team.
FAILURE: an individual-unit claim at the aggregate tier; or, at the direct tier, a
write-up that hides behind aggregates and contains no analysis of the
self-determined subset when that subset exists in the data.

**CASE 6. The low-confidence inference.**
INPUTS: a measure that moved with no activity evidence correlating above chance.
EXPECTED: no proposed sentence. An open question, unaccompanied by a guess.
FAILURE: a confident action sentence written from thin evidence.

**CASE 7. The tied superlative.**
INPUTS: a person whose value is matched by several peers.
EXPECTED: the claim says tied, and names the count.
FAILURE: any superlative shipped without a verified tie count.

The cases below belong to the generalization and to the acceptance-test
remediation, and are run with the rest. **No count of them is stated, because the
set grows with every acceptance run and a count in this line would be wrong before
the next one finishes:**

**CASE 8. The business with no market.**
INPUTS: a bound configuration whose only available rung is bare_denominator, with
MOVING_GROUND_NAME bound.
EXPECTED: every figure ships with a denominator population, every claim is worded at
bounded strength, the WIN and MISS classifier does not fire, the moving ground is
named beside every claim, and the artifact states which rung was used and why no
stronger one was available.
FAILURE: a claim worded as an achievement; a WIN label emitted at rung 6; a rate
delta or a proportion delta computed where the rung does not define one.

**CASE 9. The unbound ground.**
INPUTS: a run where MOVING_GROUND_NAME is unbound.
EXPECTED: no claim ships at achievement strength; every claim drops to bounded
phrasing; the degradation notice prints in the artifact at full prominence; and the
request is queued to BINDING_OWNER_NAME.
FAILURE: any achievement-strength claim; a notice printed only in chat; a notice
quietly downgraded because it appeared on a previous run.

**CASE 10. The self-built denominator.**
INPUTS: a cold population whose benchmark column resolves, populates, and is the sum
of the authorizations the writer's own team has just won.
EXPECTED: the independence test fires on the resolved and populated column, not only
on a resolution failure; rung 1 is struck and named; the figure that fired the test
is printed; every figure computed against that denominator is capped at bounded
phrasing; and NO BASELINE appears rather than a WIN.
FAILURE: a share near one hundred percent shipped at achievement strength with a WIN
label, with every other gate passing.

**CASE 11. The cold executive.**
INPUTS: a comparison requested at executive altitude against a population where no
unit predates the current window.
EXPECTED: no request for a second file; the earliest entry date named as evidence;
plan attainment and the bare denominator offered as the second numbers that exist;
the current state and the absolute build emitted; and at least one of the three
claimable kinds present.
FAILURE: a stop asking for a file that cannot exist; or a run that refuses to make
any claim at all, which fails the same case in the opposite direction.

**CASE 12. The pipeline write-up.**
INPUTS: two period extracts of a flowing population sharing roughly a fifth of their
rows, with reopened units present.
EXPECTED: the population and its mode are named in the front panel with the test
that decided them; the join overlap gate resolves NOT APPLICABLE and is recorded
with that reason; like-for-like is computed as a cohort-definition test on a stated
FLOW_COHORT_BASIS; the join runs on the episode key; and a write-up is produced.
FAILURE: any stop on overlap; two episodes of one identifier merged into one unit;
a comparison whose cohort basis is not stated; a run that produces nothing.

**CASE 13. The executive with no peers.**
INPUTS: a requester at the coarsest level of the chain, with PEER_SET_LEVEL_DEFAULT
naming a level below them.
EXPECTED: the resolved peer level is discarded as at-or-finer; the output says there
is no internal peer set; either the external comparison group is used and its
staleness stated, or rung 3 is dropped and the fall named.
FAILURE: the requester ranked among their own subordinate units, with every number
internally consistent.

**CASE 14. The reader who owns part of a unit.**
INPUTS: a reader whose own scope level is finer than the level at which one unit of
business sits.
EXPECTED: the mismatch is detected from the data, stated before the content, both
levels named, called a configuration mismatch rather than a property of their scope,
and queued to BINDING_OWNER_NAME; no ranked list of units is emitted.
FAILURE: a one-row artifact in which every gate passes and every count reconciles at
one.

**CASE 15. The unbound value that outranked a bound one.**
INPUTS: an ignition-bound rung of peer_distribution, with ENTITY_BENCHMARK_MAP
unbound.
EXPECTED: the absent map removes rungs 1 and 2 only; figures are computed at the
bound rung; the claim strength is the bound rung's strength; the floor is not
reached.
FAILURE: every figure routed to the bare denominator, which is a deferred default
deleting an ignition binding.

**CASE 16. The survivor-only prior file.**
INPUTS: a FIXED population and a prior-period file from which no row is absent in
the current file, so overlap is one hundred percent, churn out is zero, and the join
overlap floor passes at its maximum. The weakest performer by total movement is the
joint best by same-unit growth, and both figures are arithmetically true.
EXPECTED: the exit test runs before anything is computed on the pair and its count
is printed; the artifact states which of the two zero-exit states it believes and
the evidence for it; retention and churn print as NOT COMPUTABLE rather than as one
hundred percent; same-unit growth appears only beside total movement with the gap
between them named as the part of the change that left, as a figure where both rest
on one measure and in words with both bases named where they do not; no ranking by survivor
growth appears anywhere; and the finding is on the front panel before the content.
FAILURE: a retention figure of one hundred percent; a survivor growth figure
published alone or ranked; a pair certified ideally like for like on overlap with no
exit test recorded; or the trap caught only because two sources happened to disagree
on a count, which is not catching it.

**CASE 17. The reader with no peers and a plan.**
INPUTS: a requester at the coarsest level of the chain, rung 3 dropped for want of
any sibling set, and a plan attainment figure well above target and another well
below it.
EXPECTED: both attainment figures carry a label against the fixed rung-4 band in
percent of target, with ON PLAN as the flat state; the band and its unit print
beside each; and no figure borrows a band computed at another rung.
FAILURE: an unlabelled headline attainment because no peer spread was computable,
which silences the classifier exactly where the reader is most senior.

**CASE 18. The unanswered formatting question.**
INPUTS: a complete crawl, a full evidence ledger, every content question answered,
and Q-LIMITS unanswered.
EXPECTED: the standing field limits are used, every field carries its exact
character count, the departure is named once in the banner and once in the
verification list with the question that resolves it, and **every objective, every
measure and every free-text section that had content ships.**
FAILURE: a placeholder in any capped field; an empty or near-empty review emitted
because one constraint question went unanswered; a constraint departure listed in
the same block as a content placeholder, which tells a reader the two need the same
kind of action.

**CASE 19. The unit that became unworkable mid-period.**
INPUTS: a review over a closing period, a status column that resolved from the seed
dictionary with no value list bound, and three units: one not workable for the whole
period, one that became unworkable in the ninth month with a readable transition
date, and one that became unworkable on a date that cannot be established.
EXPECTED: the first is excluded and named among the exclusions; the second is
INCLUDED and marked with its transition date and the portion of the period it was
workable, with every rate over the population saying whether it pro-rated; the third
is INCLUDED and disclosed, and where it moves a published figure that figure is
reported both ways with the difference named; and the front panel states which
reading was applied to which part of the document.
FAILURE: the planning exclusion applied to the retrospective, which deletes the work
done on the second and third units from the person's own review and leaves nothing
in the output to notice; a rate over a partially present unit published without
saying whether it pro-rated; or a forward-looking commitment inside the same
document taking the retrospective reading without saying so.

**CASE 20. The run with no channel to ask anything, and a full evidence ledger.**
INPUTS: INTERACTIVE absent; a complete crawl; a full evidence ledger; every blocking
question in the bank unanswered because none can be asked, Q-WINS among them.
EXPECTED: every unanswered blocking question is resolved by the test in 6.3 and not
by the bank's column alone; Q-WINS resolves CONSTRAINT and the discovered candidate
list ships unedited, with nothing added, promoted or dropped; every field that had
content still carries it; the empty-document check runs and passes because the fields
are not empty; the artifact carries INCOMPLETE_BANNER_TEXT in the form its row
selects where NO drafted field carries INCOMPLETE_PLACEHOLDER_TEXT, which is the form
telling the reader to READ the document before submitting it rather than not to submit
it, naming the preview that never ran and the win list that was never reviewed; and
its first paragraph says every field carries real content and nothing is a
placeholder, which now agrees with the banner above it instead of contradicting it.
FAILURE: a placeholder in all eight blocks and a review with nothing in it, which is
regression case 18's failure arriving through the CONTENT door; any win, action or
figure INVENTED to fill a field the person could not be asked about; a run that emits
a wholly empty review without reporting it as a failed run; **and a banner that says
the document must not be submitted sitting directly above a paragraph saying every
field carries real content and the reader should submit it**, which is one literal
serving two documents.

**CASE 21. The peer set of one.**
INPUTS: a reader whose own level is the finest in the chain; a peer level resolved by
the one-step-coarser fallback to a container holding exactly two of them, so the
sibling set is ONE; both peer floors at their documented defaults; a level further out
holding a count that meets ANONYMITY_FLOOR and not MIN_POPULATION_FOR_NORM; and a
level beyond that whose count meets both.
EXPECTED: Test 3 fires; the below-floor level is recorded with its count and nothing
whatever is published from it, in ranked, positional, median, spread or generalized
form; the walk steps outward, does NOT stop at the level meeting only the anonymity
floor, and STOPS at the first level meeting BOTH floors; the level actually used and
its count print beside every figure that reads them; the derived level is named as
superseded; the claim strength is not raised by the coarser group; the LEVEL DELTA
band of 2.4.1 is computed on the set the walk stopped at and its labels are EMITTED;
and the artifact says TOO FEW PEERS TO NAME SAFELY for the below-anonymity level
rather than saying there is no peer set or printing FLAT.
FAILURE: a comparison drawn at the below-floor level in any wording, including "the
stronger of the two" and "above the branch average"; a reader given no peer comparison
at all while comparable siblings sit one level out; a walk that stops at a level
meeting one floor and not the other, which hands the run a peer set it may name and
may draw nothing from and makes every band computed on it unfirable; a walk that
continues past the first level meeting both; a coarser-level figure presented as
though the reader's own derived level produced it.

**CASE 22. The growth target and the zero target in one objective set.**
INPUTS: four objectives, one whose target is written as a CHANGE ("grow the measure
by 6 percent"), one whose target is a LEVEL, one whose target is a CEILING, and one
whose target is ZERO.
EXPECTED: the change target is attained as achieved change over targeted change, the
band is read against that quantity, the shape is named beside the figure, and where
the level reading crosses the band the other way both readings print with one label
from the shape as written; the level target divides level by level; the ceiling target
divides target by actual so that beating it reads above 100; and the zero target
produces NO attainment percentage, NO rung-4 label, ships at rung 6 with its
denominator population, and names the drop with the zero target as its reason.
FAILURE: a division by zero reaching the artifact in any form, including an error
string, an infinity, or a plausible number; a zero target rewritten to make it
divisible; two readings of a growth target producing opposite labels with neither
named; a growth objective silently labelled ON PLAN by the level reading against a
band calibrated for it.

**CASE 23. The level comparison with no band.**
INPUTS: four comparisons of one rate against another rate, in points of the measure's
own rate, at a rung whose band is defined in points of growth; the third against a
comparator set that MEETS both peer floors and whose spread nonetheless cannot be
computed; and the fourth against a comparator set BELOW MIN_POPULATION_FOR_NORM.
EXPECTED: the first two carry the LEVEL DELTA of 2.4.1 with its unit naming the
measure and a WIN, MISS or FLAT label against a band derived from the spread of the
comparator set itself; the third carries the raw delta, its comparator and the
comparator's count with NO label, and the artifact says the LABEL was withheld because
no band could be computed; **the fourth carries NO DELTA AT ALL, labelled or raw**,
ships the entity's own figure with the comparator's count beside it, and says the
COMPARISON was withheld and names MIN_POPULATION_FOR_NORM as the reason, per SD-POP-19
and 2.5; and no level delta is printed in points of growth or in share points.
FAILURE: no label on the first two, which is the silence this case exists to remove; a
level delta banded against the rung's movement band; a level delta labelled where the
spread could not be computed; **an unlabelled raw delta against the below-floor
comparator, which is the fragile number wearing a minus sign**; the third and fourth
cases given the same treatment, which is two different withholdings printed as one; a
bare "points" anywhere.

**CASE 24. The section that holds four fields.**
INPUTS: OBJECTIVE_FIELD_IS_SINGLE true, a person with four business objectives, and a
FORM_SECTIONS set whose objectives entry is one section.
EXPECTED: FORM_FIELDS is derived per its SECTION A1 row over the drafted subset the cycle
position draws and expands the objectives section to FOUR fields; the field index
prints all four with the form's own index on each heading; four blocks are built; V1
runs against the derived set and PASSES; and the document publishes.
FAILURE: V1 run against FORM_SECTIONS, seeing one section and four blocks, declaring a
mismatch and stopping publication on a correct artifact; one block holding all four
objectives, which no reader can paste into four boxes; four blocks under four
identical headings.

**CASE 25. The unsourced number in the person's own note.**
INPUTS: a run with no mail, no chat and no action-evidence column, and a person's own
evidence note carrying five figures that trace to no cell.
EXPECTED: the non-numeric action clauses from the note survive in the copy region in
the person's own words; each unsourced FIGURE appears BELOW the submission boundary as
a bracketed placeholder carrying the figure as stated, who stated it, and the question
that would source it; each placeholder names the field's heading so a reader knows
which box it goes back into; no bracketed aside appears inside any field block; and
gate G2 passes.
FAILURE: a bracketed placeholder inside a field block; an unsourced number shipping in
the copy region as though sourced; every figure in the note silently deleted, which
strips the only evidence of the person's year out of their review with nothing in the
document to notice.

**CASE 26. The default rung that no document answers.**
INPUTS: an organization whose published documents define the peer distribution, the
plan and the writer's own prior run rate, and define no addressable set and no matched
control; a faithful documents-only binding that therefore binds
COUNTERFACTUAL_AVAILABLE_RUNGS to those three plus the floor rung; and no answer
anywhere to which of them is the default, because the question is about this method's
configuration rather than about the business.
EXPECTED: COUNTERFACTUAL_DEFAULT_RUNG is DERIVED as the highest rung in the available
set whose own definition is bound, recorded DERIVED at MEDIUM confidence, named beside
the claims it governs and read back for correction; the struck rungs are named with the
definition each was missing; every figure is worded at the strength its own rung
supports; the run may still be provisional for other reasons and says so; and
regression invariant 10 passes.
FAILURE: **every claim in the document worded at the floor rung's strength on a year
the bound rungs support claims for**, which is an unbound ignition value deleting the
effect of three bindings the organization made; the derivation recorded as ANSWERED
rather than DERIVED, which is a hole in the completeness trace; the derivation
performed and not named beside the claims; a floor applied while any available rung's
own definition is bound.

**CASE 27. The ground that will not fit the box.**
INPUTS: a bound MOVING_GROUND_NAME that is a clause naming several outside entities;
an objective field whose budget is a fraction of what the full clause costs; and four
objective fields, each carrying at least one number.
EXPECTED: the full bound name appears in the GROUND STATEMENT immediately above the
first field block and again in METHOD with its source and read date, and nowhere
inside a block; every claim carrying a number carries the SHORT FORM derived once for
the run, identical in all four fields, plus the movement statement or the words saying
the movement was not measured; the short form still says what moved and that it was
not set by the writer; the outside entity names live in the GROUND STATEMENT and in
METHOD; no field is over its limit; and G19 passes.
FAILURE: the full clause repeated inside every field, spending a quarter of each box on
one disclosure before a figure is stated; a field paraphrasing the ground differently
from its neighbour, so that one ground reads as several; a field shipping with no
ground in it at all, which is a claim travelling into the destination system without
the thing that stops a reader taking it as the writer's own achievement; a field made
to fit by dropping the ground rather than by OVER_LIMIT_REMEDY; the GROUND STATEMENT
built as a copyable block.

**CASE 28. The block written in the method's voice.**
INPUTS: an objective whose attainment is short of target, computed at the plan rung
against that rung's fixed band, with a change-shaped target that reads the other way as
a level; and a second objective with no target at all.
EXPECTED: the first block says, in the words the person's own trade uses, how much of
what was asked for was achieved and that it fell short, carries both readings where
they cross in opposite directions, and names its unit; the classifier token, the band,
the band's unit, the quantity form and the rung key are BELOW the boundary with the
rung disclosure; the second block says in words that there was no target to score
against and the proposed rewrite sits below; and G13 passes on the built artifact.
FAILURE: a field block carrying a classifier token, a band name, a deadband, a
quantity-form name or a rung key, which is a method's audit output pasted into a
person's self-assessment; any disclosure DROPPED rather than moved or reworded; a
plainer wording that is not also exactly true; a block that reads well and no longer
says what the figure was measured against.

**CASE 29. The section that yields exactly one field.**
INPUTS: a FORM_SECTIONS set in which two drafted sections yield one field each and one
yields four, with OBJECTIVE_FIELD_IS_SINGLE true.
EXPECTED: the two single-field sections have their section heading suppressed and their
field heading standing alone; the four-field section keeps its section heading and
groups four blocks under it; the field index prints six entries; V1 reconciles six
blocks against FORM_FIELDS and passes; and no two adjacent headings in the document
carry the same words.
FAILURE: a Heading at one level and a Heading at the next level carrying identical
words, one a copy block and one not, distinguishable only by which has a count caption
under it; a section heading kept and reworded to tell the two apart, which gives one
box two names; the field heading suppressed instead of the section heading, which
leaves a block whose heading is not the destination system's name for it.

**CASE 30. The objective with no description.**
INPUTS: OBJECTIVE_FIELD_IS_SINGLE true; four objectives that carry a title, a measure
and a target and no description anywhere in the source; and no evidence item that is a
description of an objective as opposed to evidence of work against it.
EXPECTED: the description component is allocated ZERO, its share is released in
proportion to the components that do exist, the field holds the title and the measures,
the release is recorded in METHOD naming the component, the share and where it went;
and every field carries its exact count.
FAILURE: a description INVENTED to fill its share of the budget, which is fabrication
under 2.12 and SD-CNF-07; the share left unspent, which shrinks the field the person's
own figures had to fit into and tells nobody it happened; the reallocation performed
and not recorded, which is a decision no rule authorized.

**CASE 31. The account in the note that the book contradicts.**
INPUTS: a person's own note carrying seven stated items; one of them naming an account
that exists NOWHERE in either source file and calling it their largest; one of them
describing an account as lost that the current file carries as active with a figure
nowhere near the one stated; and every other item either traceable or unsourced.
EXPECTED: both items are labelled CONTRADICTED and not UNSOURCED, the second on the
measure and the first on the IDENTITY, because the source was read and the unit was
absent from it; both are excluded from every claim, count and denominator in the copy
region and the exclusions are listed with their reasons; BOTH READINGS of each are
printed below the boundary under one heading, the person's own words and what the
resolved column says with its column and unit named, with the question that would
settle each; the preview flags both to the person as questions; the contradicted count
is taken once against UNRESOLVED_STOP_COUNT and kept separate from the unresolved
count; and gate G24 passes.
FAILURE: either item published in the copy region in any wording, which is fabrication
the moment the data is checked; either item silently dropped, which deletes the
person's own account of their year where nobody can see it happened; the two readings
averaged or blended into one sentence; the absent account labelled UNSOURCED, which
sends the person hunting for a file when what was needed was one sentence from them;
or the run choosing a winner between the note and the book.

**CASE 32. The section heading on the first page of the copy region.**
INPUTS: a drafted objectives section yielding FOUR fields, so 8.1.1 requires the
section's own heading above the first block; a page break immediately before the copy
region; and the field index, the selection sentence and the ground statement between
them.
EXPECTED: the opening span is read back from the built artifact as break structure,
every paragraph in it is a member of the closed permitted opening set in 8.3 including
the section heading, no second page break sits among them, no panel disclosure and
nothing from below the boundary appears in the span, and V7 PASSES on a correct
document.
FAILURE: V7 failing a document that 8.1.1 required; the section heading dropped to
satisfy an enumeration, leaving four identically shaped boxes with nothing saying which
part of the form they belong to; the heading moved above the page break, separating it
from the blocks it groups; or the assertion recorded as passing on the rule's purpose
rather than run against what the rule says, which is what a run does when a test fails
a correct document.

**CASE 33. The annual reviewer with one prior period.**
INPUTS: a year-end review comparing this year against the prior one, so one prior
period exists by construction; a peer walk that exhausts the chain; and a level delta
of the reader's own rate against their own prior rate.
EXPECTED: the rung-5 level-delta band is recorded as UNCOMPUTABLE with the reason that
the run has one prior period and MIN_POPULATION_FOR_NORM needs more, the rung-3 route
recorded as shut by the exhausted walk, the raw delta shipped with its unit named in
full, and the withholding of the LABEL stated beside the figure naming BOTH shut routes
in one line each.
FAILURE: the movement band borrowed to label a level delta, which SD-CLM-34 forbids and
which labels ordinary variation as a result; either floor lowered to obtain a label; the
figure printed with no statement of why it carries no label, which a reader reads as
FLAT; or one shut route named and the other left silent.

**CASE 34. The gap that cannot be subtracted.**
INPUTS: a survivor-only prior file; a same-unit growth figure computed on the book's
own basis over the surviving units; and the only available total movement across the
whole population computed on a DIFFERENT measure from a production system, the two
bases differing by a large factor.
EXPECTED: the exit test runs and its count is printed; the survivor figure never ships
alone; both figures ship with their bases named; what separates them is stated in
WORDS; NO difference is computed; and gates G14 and G23 both pass.
FAILURE: one figure subtracted from the other to manufacture a gap, which G14 blocks
with no override; the survivor figure published alone because no lawful gap could be
computed, which is the flattering half shipping without the correction; or the absence
of a gap figure left unexplained where the gap would have gone, which a reader takes
for an absence of attrition.

**Version stamp, what changed, and what was verified versus not**, on every change.
See SD-RUN-13. **Freeze a ground-truth classification and gate on reproducing it
exactly**, where REFERENCE_CLASSIFICATION_FIXTURE is populated. See SD-RUN-11. **The
portability test is two real files of the same source, months apart**, and a change
that would break either one is wrong. See SD-RUN-12 and reference/field-resolution.md F0.4.

---

# PART 12: THE REFERENCE LIBRARY

The source of this skill carried an embedded appendix of the employer's own strategy
documents, form definitions and metric weights. That appendix is not portable and
nothing like it appears here. **What is portable is the mechanism**: a small set of
cached blocks, each carrying its own validity header, read instead of crawling, and
governed by a blocking staleness check with a disclosed-stale fallback and a
write-back loop.

## 12.1 The structure of a block

Every block, whatever it holds, opens with a three-field header and nothing else may
substitute for it:

    validity date   a date, or a rule that yields one, taken from
                    REFERENCE_VALIDITY_PERIODS. This is a FIELD LABEL on a stored
                    block, not a schema variable, and nothing reads it by that name
                    from the configuration.
    source name     the NAME of the artifact this content came from. A name, never
                    a path, never an address, never a document number.
    fetch date      the date this content was last read from that source

Blocks are stored as configuration, alongside the bound variables. **No block
content is ever written into this file.**

## 12.2 The six block types

Each type is defined by the QUESTION it answers, per the source hierarchy in 2.9,
and is populated from the named variables. The illustrations are neutral inventions,
offered to show the shape a bound value takes and never as a value.

| Block | Answers | Populated from | Typical validity | Neutral illustration of the shape |
|---|---|---|---|---|
| A. Current initiatives | What is the organization pushing this period? | ENTERPRISE_STRATEGY_PILLARS | Published annually, so through the early part of the following year | Four named pillars, each with a stable id, a name and one line of description. For a facilities-services business: response-time reduction; first-visit resolution; technician capability; digital work orders. |
| B. Multi-year goals | Where is the organization trying to be? | ENTERPRISE_LONG_TERM_GOALS, ENTERPRISE_FINANCIAL_TARGETS, ORG_PURPOSE_STATEMENT, ORG_VISION_STATEMENT | Through the horizon year of the goal set | A goal set with a horizon year, each entry naming a metric and a target, plus the purpose and vision lines cited as the top rung of the lineage ladder. |
| C. Metric weights | What does the organization think matters most? | INCENTIVE_PLAN_NAME, METRIC_SET, METRIC_MULTIPLIERS | Through the end of the current measurement half or year | A weighted metric table where the ordering IS the priority ranking, each row naming the metric, its weight, the scope level it is measured at, and whether a person at each level can actually influence it. Multipliers are listed separately, because a payout multiplier is not a weighted metric. |
| D. Form structure | What is the deliverable? | FORM_SPEC_SOURCE, FORM_SECTIONS, FIELD_LIMITS, BEHAVIOUR_FRAMEWORK_NAME, BEHAVIOUR_FRAMEWORK_ITEMS, BEHAVIOUR_SCALE_VALUES, SELF_ASSESSMENT_PROMPTS, PROCESS_CALENDAR | Through the end of the current year | The section list in order; the objective structure; the behaviour items with their observed-frequency scale; the free-text prompts quoted verbatim from the form; the field limits, marked as defaults rather than facts; and the dated stages of the review cycle with their owners. |
| E. Rating criteria | What is the quality bar? | RATING_SCALE, RATING_AXES | Through the end of the current year | The rating bands with their distribution guidance, the outcome and behaviour axes, and, critically, **the operative test that separates the top band from the one below it.** That one sentence is what a write-up is actually aimed at, and a block that omits it is not usable. |
| F. Goal methodology | How is a well-formed objective written? | GOAL_FRAMEWORK_NAME, GOAL_TERM, MEASURE_TERM, GOAL_PATTERN, GOAL_FAILURE_PATTERNS, ORG_AI_USE_POLICY_REFERENCE | Through the end of the current year | The definitions of the goal level and the measure level; the distinction between an input measure and an output measure; the evaluation cadence; the enforced pattern of verb plus metric plus population plus deadline; one worked example in the organization's own language; and the named policy under which machine assistance is disclosed. |

## 12.3 Rules that govern every block

- **NO BLOCK CONTENT EVER APPEARS INSIDE A FIELD BLOCK.** A cached reference is
  configuration and a form section is a submission. The lineage line, the metric
  weight and the initiative name are reported to the person OUTSIDE the field, per
  1.5 and LINEAGE_LINE_PLACEMENT, which places them below the submission boundary in
  the artifact. See 2.20 and 8.3 D2 and D5. **A reference block is never a copy
  block**, and nothing in this part changes what the copy region may contain.
- **A stale block MAY NOT be used until refreshed.** See 2.21 and gate G17.
- **A stale block that could not be refreshed IS used, and is disclosed.** A halted
  run is a dead end.
- **A refreshed block is reported back in the closing summary** so that one
  configuration stays authoritative for everybody rather than every user re-crawling
  the same documents forever.
- **Discover the path every run; never hard-code it.** Reference values are a
  starting point for discovery only. See SD-SRC-14.
- **A rubric that has changed recently is the quiet way a write-up gets built
  against last year's standard.** Where a block carries a volatility note, the note
  travels with every citation of that block.
- **A missing block is never a stop.** CENTRAL_BRIEF_REQUIRED must be false. Walk
  the fallback ladder: the target period's block, then the current period's, then
  the most recently published one, dated honestly. **A block one period old is worth
  far more than no plan, and stopping the run over a folder-name mismatch is the
  worse failure.** See SD-SRC-13, SD-SRC-18 and SD-SRC-21. Neither an absent block
  nor a stale one is a member of HARD_GATES, and nothing in this part adds to the
  stop list.
- **Reading the block is mandatory, never assumed.** SD-SRC-21. The content comes
  from the document, never from memory or inference. Where it comes from a cached
  copy, the copy names its release and its date and the run says which release it
  used. **A location may be bound; a standard may not.** Standing rule S8: this
  skill binds where an authoritative document lives, what it is called and when a
  cached copy expires, and never binds the content of a requirement set as the
  authority for a run.

---

# PART 13: FIXED AND FLOW

A write-up is written about a population, and populations come in two shapes. This
part carries SD-POP-21 through SD-POP-24 into the review cycle. It is not an
appendix to the pipeline: Stage 4, Stage 6, Stage 6.4 and Part 7 all read it, and a
run that has not resolved its population and its shape has not started.

The resolution below is the one the period-planning skill uses. It is deliberately
identical, because two skills scoring the same business on the same morning must
not diverge on what the population is.

## 13.0 What shape IS, and where the run gets it

**Shape is a property of the POPULATION BEING SCORED, not of the company.**
SD-POP-23. FIXED and FLOW are not a fact about an organization. Many real
businesses are genuinely BOTH: a stable roster of units with work items flowing
across them, or a roster of containers with a stream moving through them. **Forcing
one answer for the whole company is itself the error.**

POPULATION_SHAPE is therefore a KEYED SET of declared populations, each carrying
its own key, its own mode of FIXED or FLOW, its own unit noun and its own fields. A
business may declare one; it may declare three. Where only one is declared it is
the default for every run and nothing else changes.

**A run never asks whether this company is FIXED or FLOW. It asks WHICH POPULATION
IT IS SCORING and WHAT SHAPE THAT POPULATION HAS.** The population is resolved from
the request and from the source in hand, at Stage 0, and the run READS that
population's shape. **The run NAMES the population it scored in its own front
panel, with the mode and with which test decided.**

Two consequences, both stated in the artifact:

- Two skills in this bundle running the same morning on the same business may
  legitimately be in DIFFERENT shapes, and each names the population it scored.
- Two skills scoring DIFFERENT populations of the same business will report
  DIFFERENT COUNTS, and neither is broken. A write-up written about the open set
  and a scorecard scored over stage arrivals in the same window are answering
  different questions. **The two counts are not expected to agree, and this skill
  says so on its front panel wherever it emits a FLOW count.**

**Where the shape comes from, and it is two branches, not one:**

| Run | Where the shape comes from |
|---|---|
| BOUND run | READ from the declared population the run resolved. Never inferred, never guessed. |
| PROVISIONAL run, POPULATION_SHAPE unbound | INFERRED from the columns present at MEDIUM confidence, per 3.3, with the inference and its evidence printed in the front panel and in the method section, the tie-break disclosed as a tie-break where the third test could not be answered, and every sub-key that could not be inferred treated as UNBOUND. |

## 13.1 Detect the shape by three tests, and the third one decides

SD-POP-24.

**SD-POP-24 IS THE SINGLE SHAPE DETECTION PROCEDURE IN THIS BUNDLE AND IT GOVERNS.**
The table below reproduces its three tests for reading convenience. Where it and
SD-POP-24 ever differ, SD-POP-24 is right and this table is stale, including on the
order of the tests, on which one decides, and on when the tie-break may be
consulted.

| Test | Question | Evidence for |
|---|---|---|
| 1. THE ROSTER TEST | Can a complete list of all of them be produced as of a given date, without reference to what stage each is in? | a roster |
| 2. THE ENTRY AND EXIT TEST | Does each one have a date it entered and a date it stops being the organization's problem? | a pipeline |
| 3. THE REPLACEMENT TEST, WHICH DECIDES | When one of them leaves, does it leave a HOLE somebody notices and moves to fill, or does the next one simply take its place in a QUEUE? | A HOLE means the population is a FIXED roster whose members happen to be dated, and the dates are UNIT ATTRIBUTES rather than a pipeline. A QUEUE means FLOW. |

**Tests one and two both passing is the COMMON case, not the ambiguous one.** A
roster of dated standing positions passes both. So does a pipeline held inside a
stable set of containers. **The third test separates them and is not optional.**

**THE TIE-BREAK IS CONSULTED ONLY WHERE TESTS ONE AND TWO DID NOT DISCRIMINATE
AND TEST THREE CANNOT BE ANSWERED.** Not discriminating means both passed or both
failed. Test one passing while test two FAILS is FIXED, decided, and the
tie-break is not run and FLOW is not preferred. Test two passing while test one
FAILS is FLOW, decided. Only where the first two leave the question open, and the
third cannot be answered from what is in hand, is the tie-break reached.

Where the tie-break IS reached, prefer FLOW and RECORD that the shape was taken
on the TIE-BREAK rather than answered, so the binding owner can see it and
correct it. **A tie-break that leaves no trace is a guess, and a shape recorded
as tie-broken when it was in fact decided is a guess in the other direction.**
SD-POP-24 is the single shape detection procedure in this bundle; no shorter
formulation anywhere is a second one.

Where the roster test passes over CONTAINERS and the entry-exit test passes over
the things moving across them, that is NOT a conflict. **It is two populations.**
Declare both, per SD-POP-23, and let each run name which it scored. Worked example,
neutral: a service centre has a fixed roster of handlers and a flowing population
of cases. That is two declared populations, not one contested one; the case
population's container is a scope level, and the handler population is a roster in
its own right.

**Shape changes the DENOMINATOR, never the DELIVERABLE.** SD-POP-21. Both shapes
draft the same form sections in the same order, under the same field limits, with
the same gates. What changes is what "the population" MEANS.

A FIXED model applied to a pipeline silently mixes CLOSED and OPEN units into one
denominator, and the reader cannot recover it from the output. A FLOW model applied
to a roster of standing positions cohorts those positions by the year they opened
and produces a comparison nobody asked for, and their end dates are not null. Both
directions are real, which is why the third test decides rather than a tie-break.

## 13.2 The two shapes, side by side, through this skill's pipeline

| Where | FIXED | FLOW |
|---|---|---|
| What the population IS, Stage 4 | Every unit on the roster from POPULATION_SHAPE.enumeration_source as of census_basis, after scope, qualifiers and exclusions. | Every OPEN unit under FLOW_OPEN_DEFINITION as of the run moment, after scope, qualifiers and exclusions, with the run moment PRINTED. |
| Census disclosure | Print the census date and POPULATION_CENSUS_INTERVAL. | Print the open rule AS APPLIED, the run moment, and POPULATION_CENSUS_INTERVAL. |
| Not-actionable exclusion | Settled by the UNIT_ACTIONABLE_NOW_VALUES row, on whether a COLUMN RESOLVED and never on whether a binding exists, and read under this skill's REVIEW mode per SD-POP-30 and Stage 4. | The SAME rule and the SAME review-mode reading, and it is SEPARATE from the open-set rule. A unit can be open and still not actionable. Both counts are reported separately so they never double count. |
| Stage exclusion | not applicable | Units removed because they are closed, withdrawn or outside the open set are reported WITH THEIR COUNTS exactly as any other exclusion. SD-POP-22. Never silently absent. |
| Aging | Days since the recency concept, where one is bound. | Days from POPULATION_SHAPE.aging_basis, computed rather than maintained. |
| Cohorts | not applicable | FLOW_COHORT_BASIS groups units into comparable cohorts: entry, exit or event. |
| Like-for-like across two periods, Stage 4 item 2 | A ROSTER OVERLAP test against FIXED_ROSTER_CHURN_TOLERANCE, with JOIN_OVERLAP_FLOOR applying, PLUS a separate EXIT TEST whose count is printed and whose zero case is decided before anything is computed. See divergence 1, SD-CMP-09 and gate G23. | A COHORT DEFINITION test. JOIN_OVERLAP_FLOOR is NEVER applied and is never a gate, and G23 is NOT APPLICABLE because the cohort basis already carries the exit side. See divergence 1. |
| Join key, Stage 4 item 2 | The unit identifier. | The EPISODE KEY, which is the unit identifier plus the entry date, wherever reopen_allowed is true. See divergence 2. |
| Duplicate identifiers, Stage 4 | Merge the signals, per SD-PRS-29. | Merge WITHIN an episode; never merge ACROSS episodes where reopen_allowed is true. See divergence 2. |
| Peer set, Stage 4 item 7 | Sibling units at the resolved peer level, anchored by PEER_SET_ANCHOR_PERIOD. | Sibling CONTAINERS at the resolved peer level, with the cohort basis stated alongside. The subordinate test in SD-SPN-14 applies unchanged to containers. |
| The cut lattice, Stage 6.4 | Cuts over persistent units and their groupings. | The same cuts computed over the open set on one stated cohort basis, plus stage-based cuts where a stage column resolves. A cut whose input is a persistent attribute of a unit is recorded as unavailable, never scored at zero. |
| Recency as a signal | Maintained contact field: exception reporting only. | Computed age from a system-recorded date: may enter the ranking once, never twice. See divergence 3. |
| Carryover of unfinished work | Attaches to the UNIT, which persists. | Attaches to the WORK ITEM, because the unit may have left the population. See divergence 4. |
| Zero-measure units | Included at zero and ranked last by the sort key. | Identical. A newly arrived unit with no measure yet ranks last and is VISIBLE there. SD-POP-12. |
| Cold start detection, 2.2.3 | Tests 1 and 3 fire. | All three fire, and test 2 is the sharpest because entry dates are always present. |

## 13.3 The four places the two paths cannot be reconciled and must diverge

Everywhere else, one rule serves both shapes. **Each of the divergences below is
stated as a pair of rules, one per shape, on purpose**, because collapsing a pair
into one rule would make one of the two shapes wrong and the wrongness would be
invisible in the output. All of them survive the keyed-set model in
SD-POP-23, because each is a divergence between two SHAPES and not between two
companies.

### Divergence 1: the like-for-like test across two periods

There is no single test.

- **FIXED.** Like-for-like is a ROSTER OVERLAP test AND A SEPARATE EXIT TEST, and
  neither substitutes for the other. Compute the fraction of the roster that changed
  between the two periods and compare it against FIXED_ROSTER_CHURN_TOLERANCE.
  Beyond it, the comparison is LABELLED not like for like and is still published; it
  is never suppressed. **JOIN_OVERLAP_FLOOR applies here and only here.** It is
  CONDITIONAL on the population's mode being FIXED, and it is set low even then,
  because a real roster churns.

  **THE OVERLAP TEST MEASURES THE ENTRY SIDE ONLY AND CANNOT SEE WHAT LEFT.**
  SD-CMP-09. Units absent from the current file are absent from both sides of an
  overlap test, so a prior file holding only the survivors passes it at one hundred
  percent and is certified ideally comparable while being unusable for retention and
  biased upward for growth. **Count the units present in the prior file and absent
  from the current one, print that count, and where it is zero decide between a
  survivor-only extract and a population that genuinely lost nothing, with the
  evidence, before computing anything on the pair.** The caps that follow are in
  Stage 4 item 2 and are enforced by gate G23. This is the one place in this part
  where a passing test is evidence of nothing.
- **FLOW.** Like-for-like is a COHORT DEFINITION test. Compute both periods on the
  same FLOW_COHORT_BASIS and **state the basis beside every comparison.** Grouping
  by EXIT date makes a slow period look good, because only the easy ones closed;
  grouping by ENTRY date compares intake to intake. The basis is a binding, not a
  judgment, and the run never switches basis mid-comparison. **JOIN_OVERLAP_FLOOR
  is NEVER APPLIED under FLOW and it is never a gate here.**

**Why the gate cannot survive under FLOW.** A healthy pipeline shares perhaps a
fifth of its rows with itself one period later, because most of what was open has
closed and most of what is open is new. Any reasonable overlap floor therefore
declares every real comparison invalid, and the stop that results is
**correct-looking**: it reports both rosters and reads as a data problem at the
company rather than as a method that does not handle pipelines. That is the worst
property a stop can have. Applying the roster test to a pipeline reports one
hundred percent churn on a healthy pipeline; applying the cohort test to a roster
invents cohorts that do not exist. Both fail silently, so both tests are named
separately, both are printed in the audit under their own names, and **the run
states WHICH test it applied.**

### Divergence 2: duplicate identifiers, when a unit can re-enter

SD-PRS-29 says MERGE the signals on a duplicate identifier, and under FIXED that is
unconditional.

Under FLOW with POPULATION_SHAPE.reopen_allowed true it is WRONG. Two rows carrying
the same unit identifier with non-overlapping entry and exit windows are two
DISTINCT EPISODES of the same unit, not one unit recorded twice. Merging them
fabricates a single long-lived unit, sums two cycles of measure into one, inflates
the workload attached to it, and makes its aging meaningless. In a write-up that
becomes a claim about a result that never happened as described.

**The FLOW rule: the merge key is the EPISODE KEY, which is the unit identifier
plus the entry date.** Merge duplicates WITHIN an episode exactly as SD-PRS-29
requires. Across episodes, keep them separate, treat them separately in every cut,
and report how many units carry more than one episode, in a sentence that agrees at
one unit and at many and that has its own wording at zero, per SD-LNG-13. **Zero is
the sentence worth writing here**, because it is the evidence that the episode test
ran at all.

Where entry dates are absent and reopen_allowed is true, the run cannot form an
episode key. It says so, keeps the rows separate, marks them UNRESOLVED DUPLICATES,
names them with their count, and excludes them from any uniqueness assumption
rather than merging them on a guess.

**On a PROVISIONAL run, reopen_allowed is ALWAYS unbound**, because it cannot be
inferred from the columns present. The run therefore takes the
unresolved-duplicates path rather than merging on a guess. It is not permitted to
infer reopen_allowed from the presence of duplicate identifiers, because a
duplicate identifier is equally evidence of a merge candidate.

Where reopen_allowed is false, FLOW uses the FIXED rule unchanged.

### Divergence 3: whether the recency signal may enter the ranking

SD-EXC-12 keeps a lagging recency field out of the ranking, because weighting it
would steer people back to units they just left. That reasoning holds for a
MAINTAINED last-contact field and does NOT hold for an age COMPUTED from a
system-recorded entry or stage date, which does not lag anything.

**The general rule: a recency signal may enter the ranking only when it does not
lag the thing it measures, and then only once.**

- A MAINTAINED contact field, on either shape: exception reporting only, weight
  zero everywhere else, RECENCY_LAG_DISCLAIMER printed.
- A COMPUTED age from a system-recorded date, which is the normal case under FLOW:
  it may enter as a named gap term. If it does, it must NOT also carry weight in an
  exception flag, because that applies the same factor twice, which SD-WGT-19
  forbids. **The run states which of the two placements it used.**
- Where it is unclear which kind the field is, take the MAINTAINED reading, because
  that is the reading whose error a reader can detect: an under-weighted signal
  shows up as something ranking lower than expected, while a double-counted one
  shows up as nothing at all. SD-STR-10.

### Divergence 4: what carryover attaches to

Expired prior-period work stays VISIBLE at the floor weight, labelled with
CARRYOVER_LABEL, contributing zero to workload. SD-SCO-06.

- **FIXED.** The unit persists between periods, so the label sits on the unit's row
  and the reader sees it beside everything else about that unit.
- **FLOW.** The unit may have LEFT the population entirely, and a closed unit
  cannot appear on a list of open units without re-admitting an excluded row, which
  SD-EFF-07 makes a regression failure. So under FLOW **the carryover object is the
  WORK ITEM, not the unit**: expired work on a unit that is still open behaves
  exactly as under FIXED, and expired work on a unit that has left the open set is
  reported as unfinished carried work, with the unit named, its exit date and the
  item. It scores nothing, it never enters the ranked population, and its count is
  reported.
- **The run states which of the two it did for each carried item**, so a reader can
  see that the work was not lost and was not smuggled back into the ranking.

## 13.4 What does NOT diverge, and must not be made to

Stated so that no implementer invents a third path:

- The form sections, their order, the field limits, the compression order and the
  never-cut list.
- The claim doctrine in Part 2, entire. The credit rule, the counterfactual ladder,
  the two comparative quantities, the classifier, the marriage model, the lineage
  ladder, the altitude ceiling and the span-of-control tiers are identical under
  both shapes.
- The confidence gating and the proposal state machine.
- The retrieval gate, the expiry gate and the submission boundary.
- The question bank, its budget arithmetic and its skip semantics.
- The verification gates, their routing, and the shared core of HARD_GATES.
- The character set rules and the audit specification.

## 13.5 The cut lattice under FLOW, stated so it is not left to inference

Stage 6.4 runs under both shapes. Under FLOW the dimensions are read against the
open set on one stated cohort basis, and three of them change their noun:

| Direct-tier cut | Under FLOW |
|---|---|
| The self-determined subset | The subset whose outcome was determined locally rather than above the writer, resolved as the complement of a populated grouping field, and subject to the proper-subset test: where the grouping field is blank on every row or populated on every row, the distinction does not exist in this population, the subset is recorded as NOT PRESENT, and every cut and gate that depends on it is skipped and named. |
| Each managed grouping as a bloc | Each grouping of flowing units, compared against the same grouping outside the writer's scope, on the same cohort basis. |
| Individual units | Individual episodes, keyed by the episode key. |
| Breadth and depth of what was delivered | Stage progression achieved: how far units were advanced, not only whether they closed. |
| Upgrades to terms, tiers or programme participation | Unchanged. |
| Process discipline against the eligible population | Coverage of the open set, staleness against the stage's own dwell, and completion against the population flagged. |
| Discretionary engagement | Unchanged. |

| Aggregate-tier cut | Under FLOW |
|---|---|
| Whole-scope performance against the next level up | Computed over the open set on the stated cohort basis, with the basis named. |
| Each top-tier grouping rolled | Unchanged. |
| Each creditable entity rolled | Unchanged. |
| Team and system outcomes | Adds throughput and cycle outcomes: how the shape of the pipeline changed, not only its total. |
| The distribution of performance inside the scope | Unchanged, and it still belongs only to leaders. A leader who lifted the bottom of the distribution has a real win that no single-unit number shows. |

---

# APPENDIX A: THE NAMED DOCTRINE INDEX

Every doctrine the source skill named, where it is executed in this file, and the
shared rule that governs it. Nothing in this table is optional and nothing in it was
dropped.

| Named doctrine | Section here | Shared rule |
|---|---|---|
| The Permanent Record Principle | The governing premise, before Part 1 | SD-CLM-01 |
| The orphaned-fact problem | The mission, before Part 1 | SD-CLM-02 |
| The Credit Rule | 2.1 | SD-CLM-03 |
| The Counterfactual Denominator | 2.2, 2.2.1, 2.2.2 | SD-CLM-04, SD-CLM-16 |
| Every business must name its ground | 2.3, gate G19 | SD-CLM-05 |
| The Two Comparative Quantities, never interchange them | 2.4, gate G13 | SD-CLM-06 |
| WIN / MISS / FLAT | 2.5 | SD-CLM-07 |
| The Marriage Model | 2.6 | SD-CLM-08 |
| The Lineage Ladder | 2.7, gate G3 | SD-CLM-09, SD-CLM-10 |
| Span of Control | 2.8, gate G16 | SD-SPN-09 through SD-SPN-13 |
| The Source Hierarchy | 2.9 | SD-PRI-32, SD-PRI-31, SD-PRI-33 |
| Confidence Gating, the anti-slop rule | 2.10 | SD-CNF-01, SD-CNF-02, SD-CNF-03, SD-CNF-05 |
| The Proposal State Machine | 2.11, gate G15 | SD-CNF-04 |
| Never Infer A Target | 2.12, gate G5 | SD-CLM-21 |
| Never invent an action; never fabricate | 2.12, gate G2 | SD-CNF-06, SD-CNF-07, SD-CNF-08, SD-CLM-24 |
| Tie handling is mandatory | 2.13, gate G12 | SD-CLM-11 |
| No named third parties | 2.13, gate G8 | SD-CLM-12 |
| Show the benchmark, never claim it | 2.14, 8.4, gates G1 and G7 | SD-CLM-14, SD-CLM-15, SD-CLM-26 |
| Activity is not claimable | 2.15, Stage 11 | SD-CLM-22, SD-CLM-23 |
| Learning is synthesized from losses | 2.16, Stage 7 | SD-CLM-25 |
| Team credit for a direct report's work | 2.17 | SD-CLM-13 |
| Reconstruct rather than halt | 2.18, Stage 6.5 | SD-CLM-19 |
| Never backdate; never call a reconstruction contemporaneous | 2.18 | SD-CLM-20 |
| Under-finding wins; the cut lattice | 2.19, Stage 6.4 | SD-CLM-17 |
| A working list the person edits; drop means drop | 2.19, Stage 8 | SD-CLM-18 |
| The Submission Boundary | 2.20, 8.3 | SD-CTR-22, SD-CTR-23 |
| The Expiry Gate | 2.21, Stage 2b, gate G17 | SD-SRC-17, SD-SRC-18, SD-SRC-19 |
| Cache-first and always-live classification | 1.7, Stage 2c | SD-SRC-16 |
| The Retrieval Gate | 1.6, gate G18 | SD-SRC-02 |
| The attachment retrieval ladder | 1.6 | SD-SRC-01, SD-SRC-03 through SD-SRC-12, SD-SRC-20 |
| No time limit; the closed stop list | 1.1, 7.4 | SD-EFF-01, SD-EFF-02 |
| Durability: write continuously | 1.2 | SD-EFF-30, SD-EFF-22, SD-EFF-23, SD-EFF-25, SD-EFF-31, SD-EFF-33 |
| The Retry Ladder and UNCONFIRMED | 1.3 | SD-EFF-09, SD-EFF-10, SD-EFF-11 |
| Ask questions to buy time | 1.4 | SD-EFF-38 |
| Field character limits | 1.5, gate G6 | SD-LNG-08, SD-LNG-09, SD-LNG-10, SD-LNG-11 |
| Two independent readers | 3.4 | SD-RUN-01, SD-RUN-03, SD-RUN-04 |
| NOT REFUTED Is Not Confirmation | 3.4 | SD-RUN-06, SD-RUN-07, SD-RUN-08 |
| Reconciliation and the UNRESOLVED rule | 3.4 | SD-RUN-05, SD-RUN-09 |
| Route Before You Match | Stage 4 item 5 | SD-QUA-01, SD-QUA-02, SD-QUA-03, SD-QUA-07 |
| Resolve Absences By Rule | Stage 4 item 5, 2.8 | SD-QUA-04 |
| Never silently widen | Stage 4 item 5 | SD-QUA-10, SD-QUA-11, SD-QUA-12 |
| Rate, Unit and Lookback separation | Stage 4 item 4, gate G14 | SD-PRS-39, SD-PRS-40 |
| Unit drift: orient before you test | Stage 4 item 3, gate G4 | SD-PRS-34 through SD-PRS-38 |
| The Overlap Floor | Stage 4 item 2 | SD-PRS-31, SD-PRS-32, SD-PRS-33 |
| The peer set is defined by the period-end file | 2.13, Stage 4 item 7 | SD-CMP-06 |
| Never present incomplete as finished | 1.2, Stage 12.1 | SD-EFF-04, SD-EFF-05, SD-EFF-32 |
| The Preview Doctrine | Stage 11.5, Stage 12 | SD-CNF-09 |
| Character set enforcement | Part 10.1, gate G11 | SD-FMT-14 through SD-FMT-20 |
| The guardrails | Part 9 | as cited per line |
| Shape is a property of the population | Part 13, 4.4 | SD-POP-23, SD-POP-24 |
| Shape changes the denominator, never the deliverable | Part 13, Stage 4 | SD-POP-21, SD-POP-22 |
| The cold start, governing | 2.2.3, gate G20 | SD-CLM-27 |
| A cold start is detected, never declared | 2.2.3 | SD-CLM-28 |
| Rung availability is re-evaluated, never inherited | 2.2.3 | SD-CLM-29 |
| A denominator the writer is building is not a counterfactual | 2.2.3, gate G20 | SD-CLM-30 |
| No prior period means no WIN and no MISS; NO BASELINE | 2.2.3, gate G20 | SD-CLM-31 |
| What is honestly claimable during a cold start | 2.2.3, gate G20 | SD-CLM-32 |
| The rung table, promoted into shared doctrine | 2.2.1, deferred to | SD-CLM-33 |
| A comparison against a cold population is answered, not stopped | Stage 4, 2.2.3 | SD-CMP-08 |
| An unbound value never overrides a bound one | 2.2.1 | SD-CTR-24, standing rule S9 |
| A peer set is siblings, never subordinates | Stage 4 item 7, gate G22 | SD-SPN-14 |
| The top of the chain has no internal peer set | Stage 4 item 7, gate G22 | SD-SPN-15 |
| Below the minimum rankable population, a ranked list is not a deliverable | 4.5, gate G21 | SD-POP-25 |
| The unit of business must sit at or below the reader's scope | 4.5, 2.8, gate G21 | SD-POP-26 |
| A uniform measure contributed nothing, and the output says so | 2.2.3, gate G21 | SD-POP-27 |
| Reading the published standard is mandatory, never assumed, never a stop | 8.1, 12.3, 7.4.3 | SD-SRC-21 |
| No stem belongs to two concepts | Stage 4 item 5 | SD-PRS-47 |
| Two tests, engagement and influence | 2.16 | SD-EXC-14 |
| HARD_GATES is one variable and four keyed groups | 7.4 | SD-EFF-02, SD-EFF-37 |
| Test the exit side separately; a survivor-only prior file scores perfectly | Stage 4 item 2, Stage 4 comparing two periods, Part 13 divergence 1, gate G23 | SD-CMP-09 |
| A closed set must name the ordinary case | 8.2 | SD-CTR-29 |
| The not-workable exclusion asks a different question in a retrospective | Stage 4, gate G21, Part 13.2 | SD-POP-30 |
| A blocking question supplies a CONSTRAINT or CONTENT, never both | 6.1, 6.3, Stage 12.1 | SD-IDN-21, SD-EFF-04 |
| A shared default may not carry one skill's content | 8.1, 7.4 | SD-CTR-30 |
| A templated sentence agrees at zero, at one and at many | 10.2, 2.16, 4.5, 8.5, Part 13 divergence 2 | SD-LNG-13 |
| A stated peer count outranks the level derivation | Stage 4 item 7, gate G22 | SD-CTR-24, SD-SPN-14 |
| The noise band is per rung, in each rung's own unit | 2.5, 2.2.3 | SD-CLM-07, SD-CLM-33, SD-CLM-34 |
| A peer set below the anonymity floor is a THIRD state with its own rung | 2.2.2, 2.13, Stage 4 item 7 Test 3, gate G22 | SD-SPN-16 |
| The shape of a target decides the attainment arithmetic; a zero target has none | 2.2.4, gates G5 and G10 | SD-CLM-33, SD-POP-18, SD-CLM-21 |
| A level comparison is a third quantity with its own unit and a derived band | 2.4.1, 2.5, gate G13 | SD-CLM-06, SD-CLM-34 |
| A period whose end postdates the run date is impossible, not unusual | Stage 4 period validation, gate G10 | SD-EXC-07, SD-SRC-15 |
| A third party is a natural person, and an organization is not one | 2.13, gate G8 | SD-CLM-12 |
| A form SECTION and a submission FIELD are different things | 8.1.1, 7.6 V1 | SD-CTR-22, SD-CTR-23 |
| The bracketed placeholder lives below the boundary, and the claim ships without the number | 2.12, 8.3 D5, gate G2 | SD-CLM-24, SD-CNF-07 |
| The count caption is the block's last line, below the field text | 8.3 D2 and D3, 1.5 | SD-LNG-09, SD-CTR-23 |
| The front panel is one line per disclosure, and the full form sits below the boundary | 8.3, 2.20 | SD-CTR-14, SD-LNG-03 |
| The permitted character set is a range PLUS an exception list carrying the line feed | 1.5, 10.1, gate G11 | SD-FMT-14, SD-FMT-18 |
| The classification test governs where a bound class contradicts it | 6.1, 6.3, Stage 12.1 | SD-IDN-21, SD-EFF-04 |
| A second file carrying the evidence is JOINED on a shared identifier, not left unread | Stage 4 item 6, 7.5 invariant 9 | SD-PRS-48, SD-CTR-13, SD-SPN-06 |
| The entity breadth and the item count are two numbers, and the strict concept refuses | Stage 4 item 5, Stage 6.4 cut 4 | SD-PRS-47, SD-PRS-16 |
| The submission FIELD set is a variable, derived once, and printed | 8.1.1, 7.6 V1 | SD-CTR-22, SD-CTR-30 |
| The outward peer walk stops at the first level meeting BOTH floors | Stage 4 item 7 Test 3, 2.2.2, 2.13, 2.4.1, 2.5, gate G22 | SD-SPN-16 |
| A delta against a withheld comparator is itself withheld, and the withholding is stated | 2.5, 2.4.1, Stage 4 item 7 | SD-POP-19 |
| A verification never scans its own record, and the record declares the span it excluded | 7.6 | SD-FMT-27 |
| Formatting degrades safely: a band and its ink are asserted against both degraded renderings, and every colour is written with an explicit opaque alpha | 8.3 D6, 7.6 | SD-FMT-29 |
| An empty drafted section is a finished section with nothing in it | 8.2, 7.6, gate G21 | SD-FMT-07, SD-CTR-07 |
| An ignition value no document can answer is DERIVED before it is floored | 2.2.1, 3.2, 3.3, 7.5 invariant 10 | SD-CTR-24, SD-CLM-33 |
| The ground is named in full above the copy region and by its short form inside every claim | 2.3, 1.5, 8.3 D5, gate G19 | SD-CLM-05 |
| The copy region is written in the person's register and the method's tokens sit below the boundary | 10.2.1, 8.3 D5, gates G13 and G5 | SD-LNG-01, SD-LNG-08, SD-CTR-23 |
| A closed set is never made to fit by choosing the nearest member | 8.2 | SD-CTR-29 |
| A person's own claim that a resolved cell contradicts is UNRESOLVED, never unsourced and never deleted | 2.12.1, 3.4, Stage 6, gate G24, `review.contradicted_items` | SD-CNF-10, SD-CTR-23, SD-CNF-07, SD-CNF-09 |
| A join that lands and cannot be scored has not answered the failure it exists to prevent | Stage 4 item 6, 7.5 invariant 9 | SD-PRS-48 |
| The sibling set excludes the requester, and both floors are tested against that count | Stage 4 item 7 Test 3 | SD-SPN-16, SD-SPN-14 |
| The gap between survivor growth and total movement is a figure only where both rest on one measure | Stage 4 item 2, Stage 4 comparing two periods, gates G23 and G14 | SD-CMP-09, SD-PRS-39 |
| The targeted fill is verified as a warning, because the margin belongs to the person | 1.5, 7.6 V3b | SD-LNG-08, SD-LNG-09 |
| The three claim strengths have stated wordings, and the rung-to-strength mapping is the variable's | 2.2.1, 10.2.1, gate G19 | SD-CLM-33, SD-CLM-16 |
| The copy region's opening span is tested as break structure, and the section heading is a member of it | 8.3, 8.1.1, 7.6 V7 | SD-CTR-14, SD-CTR-22 |

## The doctrines named as non-negotiable, confirmed present

| Doctrine | Present at | ID |
|---|---|---|
| The Credit Rule | 2.1 | SD-CLM-03 |
| The Two Comparative Quantities and the never-interchange rule | 2.4 | SD-CLM-06 |
| WIN / MISS / FLAT | 2.5 | SD-CLM-07 |
| The Marriage Model | 2.6 | SD-CLM-08 |
| The Lineage Ladder | 2.7 | SD-CLM-09, SD-CLM-10 |
| Span of Control | 2.8 | SD-SPN-09, SD-SPN-10, SD-SPN-11, SD-SPN-12, SD-SPN-13 |
| Source Hierarchy | 2.9 | SD-PRI-32 |
| Confidence Gating and the anti-slop rule | 2.10 | SD-CNF-01 |
| The Permanent Record Principle | The governing premise, before Part 1 | SD-CLM-01 |
| The Retrieval Gate | 1.6 | SD-SRC-02 |
| NOT REFUTED Is Not Confirmation | 3.4 | SD-RUN-06 |
| Route Before You Match | Stage 4 item 5 | SD-QUA-01 |
| Resolve Absences By Rule | Stage 4 item 5 | SD-QUA-04 |
| Rate / Unit / Lookback separation | Stage 4 item 4 | SD-PRS-39 |
| The Overlap Floor | Stage 4 item 2 | SD-PRS-32 |
| The Proposal State Machine | 2.11 | SD-CNF-04 |
| Never Infer A Target | 2.12 | SD-CLM-21 |
| The Expiry Gate | 2.21 | SD-SRC-17 |
| The Submission Boundary | 2.20 | SD-CTR-23 |

---

# APPENDIX B: WHERE A SPECIFIC CASE SURVIVES AS A WORKED EXAMPLE

Where a source rule was an instance of a general rule, the general rule is stated in
the body and the specific case survives here as an illustration or as seed data the
skill extends at runtime. **Nothing was deleted.** The illustrations below are
neutral inventions; none names a real organization, system, product or place.

| General rule | Where | The specific case it came from, kept as an example |
|---|---|---|
| Credit attaches only to units you are accountable for | 2.1 | An allowlist of the entities a person may claim, plus a denylist of totals, wider-population aggregates and outside parties. Worked form: a service line the person runs is claimable; the whole-market total that contains it is not. |
| An alias that is a common short word or carries punctuation needs a sentinel | 2.1 | A brand name containing punctuation whose bare remainder was a common two-letter word, which falsely attributed more than two hundred rows of unrelated flags to that brand. The same class of error as a short place code that happens to sit inside a longer place name. |
| A population defined by absence is resolved as the complement of a populated field | 2.8, Stage 4 item 5 | A retail outlet with no parent chain, represented by an empty chain-name column rather than by the word. The generalized bindings are the self-determined subset, the managed subset, and the unbenchmarked entity. |
| The self-determined subset is the highest-evidence cut | 2.8 | Outlets with no headquarters dictating layout, assortment or pricing, where everything that happened happened because the person made it happen. Neutral parallels: an inbound lead against a self-sourced one; an unmandated renewal against a corporate contract; a discretionary purchase against a required one. |
| Influence inside a managed grouping is still a legitimate claim | 2.8 | A national account's sites inside one person's district, where the contract is set above them and the local outcome is not. |
| The illustration rule at the aggregate tier | 2.8 | A named site appearing inside an aggregate claim, with the credit staying with the team that executed it. |
| Action evidence yields counts, coverage, staleness and depth | Stage 4 item 6 | Sales-call records. The same four questions apply to a code review, a customer check-in, a safety inspection, a chart audit or a maintenance visit. |
| The cut lattice | Stage 6.4 | A named set of sales cuts, generalized into the direct-tier and aggregate-tier dimensions listed in Stage 6.4, with the distribution cut preserved verbatim because it belongs only to leaders. The dimensions are counted in that section and nowhere else. |
| A small unit-drift factor might be a real result | Stage 4 item 3 | A genuine cartons-to-packs conversion at factor ten with an interquartile range of 18 to 24 percent of the median, which a tight dispersion test would have missed; and a genuine doubling at factor two, which silent correction would have erased. |
| A lookback may differ where the rate denominator matches | Stage 4 item 4 | Two real files where all four pairings differed in lookback and none differed in rate denominator; a lookback-blocking rule would have produced no output at all. |
| A rejection test is necessary, never sufficient | 3.4 | A containment test that failed to refute 18 of 20 deliberately wrong pairings. |
| The overlap floor prevents two-method validation of nothing | Stage 4 item 2 | A near-empty intersection that both readers derive identically, agree on perfectly, and promote to CONFIRMED. |
| Discover the path every run | Stage 2d | Two consecutive periods' folders in one library that differed only by a space after a numeral. |
| A heading with no counterpart on the live form never enters the body | 2.9, 2.20 | A heading that appeared in employees' own prior self-written documents and was not on the live form. BANNED_HEADINGS is seed data and grows whenever a prior document introduces another. |
| An embedded reference cache with per-block validity | Part 12 | Six employer reference blocks covering initiatives, multi-year goals, metric weights, form structure, rating criteria and goal methodology. The structure survives; the content is bound. |
| The roster test cannot be applied to a pipeline | Part 13 divergence 1 | A healthy pipeline sharing roughly a fifth of its rows with itself one period later, which any reasonable overlap floor declares invalid, producing a stop that reads as a data problem at the company. |
| The episode key | Part 13 divergence 2 | A unit that leaves the pipeline and re-enters, whose two passes are two distinct atoms. Merging them sums two cycles into one and makes the aging meaningless. |
| Two populations, not one contested one | Part 13.1 | A service centre with a fixed roster of handlers and a flowing population of cases: the case population's container is a scope level, and the handler population is a roster in its own right. |
| A denominator the writer is building | 2.2.3 | A launch computing share of a population that is the sum of the authorizations its own team has just won, arriving near one hundred percent by construction. |
| A peer set drawn from subordinates | Stage 4 item 7 | A system-level executive whose peer level resolves to the only level the default names, one step BELOW her, so the run ranks her among the units she manages. |
| A stated peer count that the level default contradicts | Stage 4 item 7 | An interview that collected a peer count and never a peer level, where the one-step-coarser default resolved to a set of two, below every floor, and would have dropped a peer comparison the organization had already described. |
| A prior file with no exits in it | Stage 4 item 2 | A prior-period extract that was the current roster valued a year earlier, on which retention is one hundred percent by construction and the weakest performer by total movement is the joint best by survivor growth. |
| The not-workable exclusion read forward in a retrospective | Stage 4 | A unit that went onto hold in the ninth month of a reviewed year, workable for eight of twelve months, removed from the person's own review by a forward-looking exclusion and invisible in the output because the row is simply not there. |
| One unanswered formatting question emptying a document | 6.3, Stage 12.1 | A run with every content question answered and the field limit question unanswered, which under a literal blocking rule placed the placeholder in every capped field and emitted a review with nothing in it. |
| A published external comparison group | Stage 4 item 7 | A regulated business whose real second number is a comparison group somebody else maintains and refreshes annually, which cannot be forced into a containment chain of units the organization owns. |
| A reader who owns part of a unit | 4.5 | A containment chain of five levels with the unit of business declared at level three, so a reader at level five owns a part of one unit and every count reconciles at one. |
| A stem in two concepts | Stage 4 item 5 | A generic status stem carried by both the not-actionable exclusion concept and the pipeline stage concept, where the exclusion silently removes a stage and every invariant passes. |
| Authority to set against ability to move | 2.16 | A measure set by an external body that the reader's own actions plainly affect, which a single-test reading would move out of scope and leave a near-empty findings list reading as "you are fine". |

---

# APPENDIX C: WHAT COULD NOT BE GENERALIZED WITHOUT SOME LOSS

Three places, recorded openly rather than papered over, because a reader is entitled
to know where the port is thinner than the original. All three were re-checked
against the cold-start doctrine and the FIXED and FLOW model; C1 and C3 are
unchanged, and C2 gains a second branch rather than being repaired.

**C1. The proportion delta loses its meaning above rung 3.** A share is only real
where the entity sits inside a bounded population whose value the method can read.
At rung 4 and below there is no such population, so the proportion delta is
UNDEFINED and is not emitted. The source skill always had a category and therefore
always had both quantities. **What is lost:** at the weaker rungs a person has one
comparative quantity rather than two, so a claim about capturing more of a
population cannot be made at all. **What replaces it:** the rung is named beside the
figure and the artifact says which quantity was unavailable and why. Nothing is
approximated.

**C2. The WIN and MISS classifier does not fire at rung 6, and it does not fire at
all on a cold population.** These are two different silences from two different
causes and they are stated separately.

Branch one, the floor rung. With a bare denominator there is no second growth rate
to subtract, so the label is UNPAIRED by construction and the environment-credit
warning cannot be delivered numerically. **What is lost:** the classifier's
diagnostic power at the floor rung. **What replaces it:** gate G19 and the
MOVING_GROUND_NAME binding, which force the ground to be named in words beside every
claim even when it cannot be measured, and which drop every claim to bounded
strength so that no achievement wording can be built on an unmeasured ground. The
warning survives; only its arithmetic does not.

Branch two, the cold population, added by SD-CLM-31. Where the population has no
prior period, the classifier does not fire at any rung, because a label asserts
movement and there is nothing to have moved from. **This is not the same silence and
must not be reported as one.** The state emitted is NO BASELINE, which is
distinguishable from UNPAIRED and from FLAT, and a plan attainment figure is exempt
and keeps its own three states. **What is lost:** nothing that was ever true. What
would have been lost, had this branch not been written, is a first-period number
labelled a win against nothing. **What replaces it:** the three claimable kinds in
2.2.3, so that the absence of a comparison is not the absence of a finding.

**C3. Two mail-stack specifics could not be preserved as instructions.** The source
carried a named list of retrieval calls that fail, one of them silently, tested
against one live stack. Those literals cannot appear here. **What is lost:** the
concrete list. **What replaces it:** FORBIDDEN_RETRIEVAL_PATHS, which holds the same
list as bound configuration with each entry naming its failure mode, plus the
standing instruction in 1.6 that the dangerous member of any such list is the one
that does not error, and the instruction to add a fifth path to the list the first
time one is found. The mechanism and the warning survive; the specific call names are
configuration.

---

# APPENDIX D: THE VARIABLES THIS SKILL READS

Read the definition, validation, documented default and degradation notice for each
in reference/schema/. This list exists so that a binding owner can see, in one place,
what this skill will eventually ask for.

**Ignition, organization tier:** ORG_NAME, BINDING_OWNER_NAME, SCOPE_LEVELS,
ROLE_LADDER, POPULATION_SHAPE, COUNTERFACTUAL_AVAILABLE_RUNGS,
COUNTERFACTUAL_DEFAULT_RUNG, MOVING_GROUND_NAME, PLANNING_PERIOD_NAME,
PLANNING_PERIOD_LENGTH_DAYS. **BINDING_OWNER_CONTACT is DEFERRED and is not a
member of this set**, per 3.2.

**Ignition, person tier:** PERSON_ROLE_TITLE, PERSON_SCOPE_CODE,
PERSON_SUPERVISOR_NAME, PERSON_HAS_DIRECT_REPORTS.

**Population, shape and scope:** POPULATION_SHAPE and its per-population sub-keys
mode, unit_singular, unit_plural, enumeration_source, entry_field, exit_field,
stage_field, stages, aging_basis, census_basis and reopen_allowed;
FLOW_OPEN_DEFINITION; FLOW_COHORT_BASIS; FIXED_ROSTER_CHURN_TOLERANCE;
UNIT_LEVEL_KEY; MIN_POPULATION_FOR_RANKING; JOIN_UNIQUENESS_FLOOR;
JOIN_OVERLAP_FLOOR; UNRESOLVED_STOP_COUNT; DELIVERABLE_CONTAINER_REQUIRED.

**Cold start:** COLD_START_MIN_PRIOR_SHARE, ADDRESSABLE_SELF_SHARE_CEILING,
COUNTERFACTUAL_RUNG_SCOPES.

**Peer sets:** PEER_SET_LEVEL_DEFAULT, PEER_SET_ANCHOR_PERIOD, PEER_SET_IS_EXTERNAL,
EXTERNAL_PEER_SET_SOURCE.

**Claims and comparison:** COUNTERFACTUAL_BY_METRIC, CLAIM_STRENGTH_BY_RUNG,
RUNG_DISCLOSURE_REQUIRED, DEADBAND, MOVING_GROUND_SOURCE,
ADDRESSABLE_POPULATION_DEFINITION, ADDRESSABLE_POPULATION_CONCEPT,
CONTROL_GROUP_DEFINITION,
PLAN_SOURCE_NAME, PLAN_SET_BY_ROLE, PRIOR_PERIOD_BASIS, BARE_DENOMINATOR_CONCEPT,
LINEAGE_LADDER, CONTRIBUTION_VERBS, OWNERSHIP_VERBS, CLAIM_PART_ORDER,
PROOF_ACCEPTED_FORMS, SUPERLATIVE_REQUIRES_TIE_COUNT, ANONYMITY_FLOOR,
NAMED_THIRD_PARTIES_ALLOWED, ATTRIBUTION_TEAM_PHRASES, ILLUSTRATION_RULE_ENABLED.

**Entities and benchmarks:** CREDITABLE_ENTITY_CLASS_NAME, CREDITABLE_ENTITIES,
ENTITY_WEIGHT_FLOOR, NON_CLAIMABLE_ENTITIES, ENTITY_BENCHMARK_MAP,
BENCHMARK_POPULATIONS, SENTINEL_TOKENS, ENTITY_ALIAS_UNRECOGNIZED_ACTION,
SPECIFIC_INITIATIVE_NAMES, FAMILY_NAMES, MATCH_STOPWORDS.

**Measures and parsing:** MEASURE_TIERS, MEASURE_UNIT_TOKENS, MEASURE_RATE_TOKENS,
MEASURE_LOOKBACK_TOKENS, ZERO_MEASURE_TREATMENT, PERCENTILE_DEFINITION,
MIN_POPULATION_FOR_NORM, UNIT_DRIFT_CANDIDATE_FACTORS, UNIT_DRIFT_AUTONORM_FACTORS,
UNIT_DRIFT_MIN_PAIRS, UNIT_DRIFT_TOLERANCE, UNIT_DRIFT_CONCENTRATION,
UNIT_DRIFT_BAND, RATE_DENOMINATOR_MUST_MATCH, LOOKBACK_MAY_DIFFER,
COLUMN_CONCEPT_DICTIONARY, MIN_STEM_LENGTH, HEADER_SCAN_DEPTH, NULL_LIKE_VALUES,
CONCEPT_LEARNING_ENABLED, CONCEPT_LEARNING_LOG_PATH, UNIT_ID_CONCEPT,
UNIT_ID_IS_TEXT, UNIT_OF_BUSINESS_SINGULAR, UNIT_OF_BUSINESS_PLURAL.

**Priorities and periods:** SOURCE_AUTHORITY_MAP, PRIORITY_SOURCES,
PRIORITY_SOURCE_COUNT, SUPERVISOR_SWEEP_WINDOW_CURRENT,
SUPERVISOR_SWEEP_WINDOW_PRIOR, CHAIN_WALK_DEPTH, CHAIN_DISTANCE_WEIGHTS,
DIRECTIVE_RELEASE_PHRASES, ACTOR_TEST_ENABLED, CENTRAL_BRIEF_NAME,
CENTRAL_BRIEF_REQUIRED, OPERATING_WINDOW_SOURCE, OPERATING_WINDOW_DERIVATION_RULE,
PLAN_AHEAD_RULE, REPORTING_CALENDAR_IS_NOT_AUTHORITY, PERIOD_TOKEN_MAP,
CYCLE_POSITIONS, CYCLE_POSITION_NAMES, GOAL_REVIEW_CADENCE, PROCESS_CALENDAR,
REFERENCE_VALIDITY_PERIODS.

**The form and the fields:** DESTINATION_SYSTEM_NAME, FORM_SPEC_SOURCE,
FORM_SECTIONS, FORM_SECTIONS_BY_CYCLE_POSITION, FORM_FIELDS, FIELD_LIMITS,
OBJECTIVE_FIELD_IS_SINGLE, FIELD_BUDGET_SPLIT, TARGET_FILL_RATIO, COMPRESSION_ORDER,
NEVER_CUT_LIST, OVER_LIMIT_REMEDY, LINEAGE_LINE_PLACEMENT, BEHAVIOUR_FRAMEWORK_NAME,
BEHAVIOUR_FRAMEWORK_ITEMS, BEHAVIOUR_SCALE_VALUES, RATING_SCALE, RATING_AXES,
SELF_ASSESSMENT_PROMPTS, STATUS_VALUES, ACTIVITY_STATUS_VALUES,
COMPLETION_ABOVE_100_ALLOWED, INCOMPLETE_PLACEHOLDER_TEXT, INCOMPLETE_BANNER_TEXT,
GOAL_FRAMEWORK_NAME, GOAL_TERM, MEASURE_TERM, GOAL_PATTERN, GOAL_FAILURE_PATTERNS,
INCENTIVE_PLAN_NAME, METRIC_SET, METRIC_MULTIPLIERS, BANNED_HEADINGS,
SUBMISSION_BOUNDARY_BANNER, PEOPLE_LEADER_OBJECTIVE_REQUIRED,
PEOPLE_LEADER_OBJECTIVE_SOURCE.

**Questions and run control:** QUESTION_BANK, QUESTION_BATCH_MAX,
NON_BLOCKING_BUDGET_FORMULA, COMPOSITE_QUESTION_IDS, FORM_REQUIRED_EXEMPT_QUESTIONS,
ANOMALY_QUESTION_CAP, HEADLINE_CANDIDATE_THRESHOLD, MISS_SUGGESTION_COUNT,
EVIDENCE_SUFFICIENCY_FLOOR, SYNTHESIS_MIN_EVIDENCE, SYNTHESIS_MAX_OBJECTIVES,
RUN_ESTIMATE_BANDS, ASK_LANGUAGE_RULE, HARD_GATES, RETRY_BACKOFF_SCHEDULE,
SCOPED_RETRY_LIMIT, REPAIR_CYCLE_LIMIT, GLOBAL_REMEDIATION_BUDGET,
PER_GATE_FAILURE_LIMIT, CHECKPOINT_PATH_PATTERN, CHECKPOINT_DELETE_ON_PUBLISH,
REGRESSION_INVARIANTS, SPOT_CHECK_SAMPLE_SIZE, REGRESSION_CASES,
REFERENCE_CLASSIFICATION_FIXTURE.

**Sources and systems:** SOURCE_WORKBOOK_NAME, SOURCE_WORKBOOK_LOCATIONS,
DOC_STORE_NAME, DOC_STORE_PATH_DISCOVERY_REQUIRED, MAIL_SYSTEM_NAME,
MAIL_SWEEP_FOLDERS, DIRECTORY_SELF_LOOKUP, DIRECTORY_MANAGER_LOOKUP,
CHAT_PLATFORM_NAME, EVIDENCE_SOURCES, DOWNLOAD_DIR, FORBIDDEN_RETRIEVAL_PATHS,
INLINE_FETCH_CEILING, MIME_ENCODING_FACTOR, SYSTEM_OF_RECORD_EXCLUSIONS,
SIBLING_SKILLS, OUTPUT_DIR, UPLOAD_DIR, SCRATCH_DIR.

**The artifact and its styling:** TAB_CONTRACT, DELIVERABLE_NAME,
OUTPUT_FILENAME_PATTERN, COLOR_TITLE_BAND, COLOR_SECTION_HEADER, COLOR_LABEL_FILL,
COLOR_HEADER_TEXT, BODY_FONT, BODY_FONT_SIZE, TITLE_FONT_SIZE. **THE FOUR COLOUR
VARIABLES ARE READ AS THE SCHEMA BINDS THEM AND THE DIRECTION IS PART OF THE
BINDING**: the three bands are LIGHT, COLOR_HEADER_TEXT is the DARK ink carried on
them, and each is written with an explicit opaque alpha in the `FFRRGGBB` form, per D6,
SD-FMT-29 and reference/output-contract.md PART 2.8 and 2.9. No value of any of them is written
in this file.

**Language and formatting:** BINDING_OWNER_CONTACT, ALLOWED_CHARACTER_RANGE,
TITLE_CASE_HEADINGS,
IMPACT_LANGUAGE_RULE, BANNED_PHRASES, CONTROLLED_VOCABULARY, CHAT_REPLY_MAX_LINES,
MSG_DEGRADED_RUN, MSG_UNBOUND_VALUE, MSG_AUTHOR_LINE, METHOD_OWNER_STATEMENT,
TUNING_INVITATION, BUNDLE_VERSION, BUNDLE_VERSION_DATE, BINDING_LOCKED,
ORG_AI_USE_POLICY_REFERENCE.

**Person tier, beyond ignition:** PERSON_SCOPE_LEVEL, PERSON_SUPERVISOR_CONTACT,
PERSON_UPLINE_CHAIN, PERSON_SECONDARY_SCOPES, PERSON_DISPLAY_NAME, PERSON_CONTACT,
PERSON_ROLE_START_DATE, PERSON_CONFIRMED_FIELD_LIMITS, PERSON_BINDING_VERSION.

---

# THE LAST RULE

If a rule in this file and a convenience conflict, the rule wins. If a rule in this
file and a rule in reference/doctrine/ appear to conflict, reference/doctrine/ wins and this file is
the defect. If a number in this file and a bound value conflict, the bound value
wins and the number here was an illustration.

And if a claim in a draft cannot name what it was compared against, it does not
ship.

## Live-run remediation, fifth pass

- **The tier-size statement is rewritten as shorter RELATIVE TO SPAN**, with the
  senior pair named as the larger pair in absolute rows, matching SD-RNK-09 and
  the schema default.
- **The shape tie-break is scoped**: consulted only where tests one and two did
  not discriminate AND test three cannot be answered, with SD-POP-24 named as the
  single shape detection procedure in the bundle.

## Live-run remediation, sixth pass

From the first end-to-end drive of this skill at two altitudes against a hostile
file. Nothing was deleted to make any of these simpler.

- **The exit test is carried into every two-period comparison**, per SD-CMP-09, with
  gate G23, regression case 16 and the front panel statement. The run that found
  this was handed a survivor-only prior file, and the like-for-like test certified
  it as ideally comparable while it made the weakest performer look joint best.
- **DEADBAND is a mapping per rung with every band's unit named**, and a bare scalar
  is rejected at validation.
- **Plan attainment carries its own fixed band in percent of target**, so a reader
  with no peer set still receives labelled figures, including at the top of the
  house where rung 3 is dropped.
- **The peer LEVEL is bound or derived alongside the peer COUNT**, and a stated
  count outranks the one-step-coarser derivation.
- **Gate G15 is scoped to the copy region**, and an unconfirmed proposal removed for
  want of an answer may be offered below the submission boundary under the five
  conditions in 2.20. A rejected proposal still appears nowhere.
- **The third-party rule states its identity-field exemption explicitly**, so the
  schema's "in a claim" and the gate's "anywhere" no longer diverge on whether the
  form's own supervisor field may be filled.
- **A period length read off a period name is DERIVED, never ANSWERED**, which
  closes a hole in the ignition completeness trace.
- **Every blocking question is classified CONSTRAINT or CONTENT**, the class is a
  column of the bank, and Stage 12.1 resolves a non-answer by the class. A
  constraint question can no longer empty a field that has content, which is what a
  literal reading of the old blocking rule did to a document with an unanswered
  field limit.
- **The not-workable exclusion takes its REVIEW reading**, per SD-POP-30: workable
  at any point in the period, not workable now. A unit that became unworkable
  mid-period is included and marked rather than deleted from the person's own year.
- **Specific unbound-ignition consequences are read from the ignition rows** rather
  than restated here, in 2.3 and 3.3.
- **Four restated counts were removed** and their sets left to derive themselves:
  the doctrine rule counts, the regression case count, the guardrail count and the
  question bank counts. **A count restated outside the block that derives it is a
  second declaration**, and this file had four of them, two already wrong.

## Live-run remediation, seventh pass

From one end-to-end drive of this skill against a real book of business, in which a
document was built and read back from the built container rather than from the build
intention. Nothing was deleted to make any of these simpler.

- **Q-WINS is classed CONSTRAINT**, and the classification test in 6.3 governs
  wherever a bound bank's class contradicts it. A run with no channel to ask
  anything used to put a placeholder in every block and emit an empty review, which
  is regression case 18's failure arriving through the CONTENT door where none of the
  guards was watching. The default shape is stated so it cannot be misread as
  permission to write: the discovered list ships unedited, nothing is added, promoted
  or dropped, and the departure is named.
- **The empty-document check runs before any incomplete emit.** Where every drafted
  field would carry a placeholder and the evidence ledger is not empty, the
  classification is re-worked before anything is emitted, and a review with a
  placeholder in every block is reported as a failed run rather than delivered
  quietly.
- **A peer set that is non-empty and below the anonymity floor has a rule**, SD-SPN-16,
  executed as Test 3 at Stage 4 item 7: walk outward, stop at the first level that
  meets the floor, publish nothing at all from any level below it, print the level
  used and its count beside every figure, name the derived level as superseded, and
  say which of three states the reader is in. The fallback produced a peer set of ONE
  routinely and nothing covered it. **Superseded in part by the eighth pass below**:
  the walk stops at the first level meeting BOTH peer floors, and the artifact
  distinguishes FOUR states rather than three.
- **Rung 4 attainment is defined over every target shape this skill can receive**, in
  2.2.4: level over level, change over change, target over actual for a ceiling, and
  UNDEFINED for a zero target, which drops to rung 6 with its denominator population
  rather than dividing by zero.
- **A LEVEL DELTA is a third comparative quantity**, in 2.4.1, named by SD-CLM-34 and
  banded by DEADBAND, which is now keyed PER RUNG AND PER QUANTITY FORM: rungs 3 and 5
  each carry a movement band and a required level delta band, both guarded by
  MIN_POPULATION_FOR_NORM, and neither is ever read as the other. One rate against
  another rate is the commonest comparison in a service business and the classifier
  used to be silent on it.
- **The count caption is the block's LAST line**, per reference/output-contract.md PART 3.3, and
  the document says on its face where a selection starts and stops. Every other
  placement breaks a requirement, and the one previously written here was picked up by
  every drag that began at a heading.
- **A form SECTION and a submission FIELD are different things**, per that contract's
  PART 3.1 and 8.1.1 here. **The field set is FORM_FIELDS**, derived once by its own
  SECTION A1 row rather than in prose in every place that needs it, PRINTED in the
  field index, and read by V1 and by `review.field_block_set_mismatch`; run against
  the section list the assertion failed a correct document wherever one section held
  two fields.
- **Rung 4's arithmetic follows the target's shape**, per SD-CLM-33, with the zero
  target guarded by SD-POP-18's degenerate table. 2.2.4 now carries the four shapes
  and cites the principle rather than establishing it.
- **A second file carrying the evidence is JOINED on the shared identifier**, per
  SD-PRS-48, at Stage 4 item 6: four preconditions before any join, both non-matching
  sides reported, a blocking row-count assertion carried as regression invariant 9,
  and the enrichment disclosed wherever an enriched term is used. Leaving the file
  unread computed seven terms as zero on every row with nothing in the output to
  notice.
- **The entity breadth and the item count are separated by the seed dictionary**,
  through the strict concept `concept_distinct_entity_count` and its reciprocal
  forbidden neighbour `concept_item_count`, so the next run refuses by rule where this
  one refused by care.
- **The bracketed placeholder has one home**, below the boundary, per that contract's
  PART 3.4: the claim ships without the number, the number goes below with its source
  and the question that would settle it, and the two are linked by the field's heading.
- **FORM_SECTIONS has one documented default and it is the schema's**, with the
  `drafted` flag that reconciles six sections and five drafted blocks. The second
  table that used to sit in 8.1 is gone.
- **The ignition set is TEN organization values.** BINDING_OWNER_CONTACT is DEFERRED,
  with its own standing disclosure, because it is the one value a documents-only
  binding can never supply.
- **The permitted character set is a range PLUS an exception list carrying the line
  feed**, which reconciles a field-limit rule that counted line breaks with a gate
  that forbade them.
- **A period whose end postdates the run date is IMPOSSIBLE**, is disclosed with both
  dates, and makes every figure from that source provisional. Coverage alone passed it.
- **A third party is a natural person**, an organization is named where the
  organization's own published sources name it, and the contract's own contact line is
  not a violation of the gate that requires it.
- **The front panel is one line per disclosure**, with every full form below the
  boundary, so the copy region starts on the first page. Nothing was dropped from it.
- **Q-STATUS, Q-BEHAVIOUR and Q-INCLUSION carry the trigger clause Q-LEARN already
  had**, so a blocking question whose answer has no home does not fire and does not
  route a complete document to the incomplete path.

## Live-run remediation, eighth pass

From one end-to-end drive of this skill against a real agency book of business, in
which a document was built and read back from the document XML. Nothing was deleted to
make any of these simpler.

- **COUNTERFACTUAL_DEFAULT_RUNG is DERIVED before it is floored**, in 2.2.1, 3.2 and
  3.3, with regression invariant 10 and regression case 26. It is a question about
  this method's configuration that no organization document answers, exactly as
  BINDING_OWNER_CONTACT was, and leaving it unbound used to word every claim in a
  document at the floor rung on a year where three bound rungs supported far more.
  **An unbound ignition value can no longer delete the effect of a bound one.**
- **The outward peer walk stops at the first level meeting BOTH the anonymity floor
  and the norm floor**, per the amended SD-SPN-16, executed as Test 3 at Stage 4
  item 7, with a fourth artifact state for a set large enough to name and too small to
  band. Stopping on the anonymity floor alone landed every walk on a set that could be
  ranked and could not be compared, so the LEVEL DELTA band computed and could never
  fire, on any data.
- **A delta against a comparator below the norm floor is not computed at all**, per
  SD-POP-19, which 2.5 now defers to instead of instructing otherwise. Two sections
  giving two answers produced two artifacts off one configuration and one data set.
- **The moving ground is named in FULL in two places outside the field blocks and by a
  short form inside every claim carrying a number**, per 2.3, and no claim can travel
  to the destination system without it. Naming it in full six times cost a quarter of
  every objective box; dropping a third party's name from the short form cuts nothing
  NEVER_CUT_LIST protects, because that list protects entities the writer claims credit
  FOR.
- **The copy region is written in the person's register**, per 10.2.1, with the plain
  form of every mandatory in-block disclosure and the method's own tokens moved below
  the boundary. The boxes used to read like a method's audit output in a document whose
  whole purpose is to be pasted as somebody's own words.
- **The copy region begins on its own page**, which is a test that can be met on the
  run 3.3 calls the most likely one. The old test, that the first block begins on the
  first page of the document, could not be met with twelve live panel disclosures and
  an eight-capability degradation block, and its only remedy was to report its own
  failure.
- **The degradation block is a leading count line and one line per capability, each
  carrying all three parts**, per reference/capability-probe.md 4.1, which governs where any
  panel ordering here disagrees. A count plus the single worst effect dropped the "what
  to do" statement for every degradation but one.
- **A section that yields exactly one field has its section heading suppressed**, in
  8.1.1, because two adjacent headings carrying identical words, one a copy block and
  one not, is the careful reading of a heading that D5 forbids.
- **INCOMPLETE_BANNER_TEXT has two documented defaults and the check that chooses
  between them already runs**, in Stage 12.1. One literal served both, so a run whose
  only fault was an unrunnable preview opened with DO NOT SUBMIT above a paragraph
  telling the reader to submit it.
- **A field component with no source is allocated zero and its budget is released in
  proportion**, in 1.5, with the release recorded. A description budget reserved for a
  component the source does not have is either filled by fabrication or left unspent,
  and nothing said which.
- **STATUS_VALUES carries a member for an objective with nothing to judge it against**,
  and no closed set is ever made to fit by choosing the nearest member.
- **The elements of reference/output-contract.md that cannot reach a document are named one by
  one in 7.6**, each recorded not applicable with its reason, so nobody scores this
  skill against a grid it does not emit; and PART 7.1's own-record exclusion is adopted
  for every string-searching assertion, while the character sweep still reads
  everything.

## Live-run remediation, ninth pass

From a second end-to-end drive of this skill against a real agency book of business, in
which a document was built and read back from the document XML, and from the shared
layer's own repairs in the same round. Twenty-four of the twenty-five prior defects
were verified fixed on that run, one partially, none still present. Nothing was deleted
to make any of these simpler.

- **A CLAIM IN THE PERSON'S OWN NOTE THAT A RESOLVED CELL CONTRADICTS IS A NAMED STATE
  WITH ITS OWN RULE**, per SD-CNF-10, executed in 2.12.1, swept at Stage 6, gated by
  G24, counted by `review.contradicted_items` and cased at 31. **Neither source wins
  automatically**: nothing contradicted enters the permanent record, nothing
  contradicted is deleted, both readings ship below the boundary with the question that
  would settle them, and CONTRADICTED, UNSOURCED and UNVERIFIED are three labels with
  three remedies. A unit the person names that is absent from the source entirely is a
  contradiction of the identity. Before this, the run reached for SD-RUN-09 by analogy
  and decided a question of fact that no rule authorized it to decide, twice in one run.
- **The copy region's opening span is tested as BREAK STRUCTURE and its permitted set
  is CLOSED rather than counted**, in 8.3, read back as V7 and cased at 32. The old
  enumeration named four things and meant five, because 8.1.1 requires the section
  heading of a one-to-many section immediately above the first block, and the test
  therefore FAILED A CORRECT DOCUMENT. It also called itself mechanical while naming an
  attribute a document engine computes at render time and cannot read back.
- **The derive-before-floor fix is now reconciled across both files.** 3.3 cites
  reference/binding-interview.md PART 6 step 4, which now derives before it floors in the same
  terms 2.2.1 and 3.3 use, and both files defer to the two ignition rows rather than
  restating them. The fix had landed here and not there, and PART 6 is the section a
  first-run implementer opens.
- **The rung-5 level-delta band is uncomputable on every annual run by construction**,
  because a year-end review has one prior period and the band needs
  MIN_POPULATION_FOR_NORM of them. 2.5 now names that as a STRUCTURAL silence, says
  which routes are shut and why, and forbids borrowing the movement band or lowering
  either floor to fill it. Cased at 33. The band itself is DEADBAND's and the repair is
  not this file's to make.
- **The sibling set EXCLUDES the requester and both floors are tested against that
  count**, stated at Stage 4 item 7 Test 3 where the walk is executed rather than only
  inside a worked example. On a five-unit organization at the documented floors the two
  readings produce two materially different permanent records off one file.
- **The gap between survivor growth and total movement is a FIGURE only where both rest
  on the same measure and basis**, and words with both bases named where they do not,
  at Stage 4 item 2, in the two-period section and in G23. G14 governs the pair and is
  never overridden to satisfy a disclosure. Cased at 34.
- **A priority source is admitted where its period OVERLAPS the window, for the part it
  covers**, at Stage 2c. Read as a coverage test it rejected a dated, attributable
  directive issued for one month of the year being reviewed, and it bites the other way
  on a planning run over one month of a bound year.
- **The TARGETED FILL is verified, as V3b in 7.6, and it warns rather than blocks.**
  Every gate in the file read the limit and nothing read the target, so a run could ship
  every field one character under its cap and hand the person a document in which any
  word they add truncates their own record silently. The margin belongs to them.
- **The three claim strengths have stated wordings**, in 2.2.1, with the rung-to-strength
  mapping left to CLAIM_STRENGTH_BY_RUNG. The middle of a three-value scale was
  undefined, so two implementers would word the same rung differently.
- **The title band is first and the incomplete banner is second, immediately below it**,
  settled once in Stage 12.1 and agreed to in 8.3. Two rules wanted the same line and
  the silence made one of them wrong on every incomplete run.
- **Which FIELD_LIMITS key caps a drafted section is a stated total rule and the
  resolved kind is printed**, in 8.1.1, with a bound kind outranking all of it. At the
  documented defaults two candidate keys carry the same number and the hole is
  invisible; at an organization that binds them apart, two implementers cap one box
  differently and one of them truncates a record.
- **Regression invariant 4 is now review-shaped and can fail.** It tested that no
  measure floor was applied and that the whole population was ranked, which this skill
  never does, so it passed by construction at every gate. It now tests that no in-scope
  unit left a published count without appearing in the exclusion list with its reason.
- **The impossible-period disclosure travels into the COPY REGION**, at Stage 4 period
  validation item 6 and gate G10, and is protected from COMPRESSION_ORDER in 1.5. The
  front panel does not get pasted, so a permanent record built on an unfinished period
  carried no trace of it into the destination system.
- **The rewritten contract parts and the new grid variables are recorded NOT APPLICABLE
  and NOT READ with their reasons**, in 7.6: PART 2.5 as rewritten, PART 2.6 as
  rewritten, the new PART 2.7, and `GRID_MAX_TOTAL_WIDTH`, `CLASSIFICATION_VOCABULARY`
  and `CLASSIFICATION_FILLS`. **SD-FMT-28, SD-FMT-03 and SD-CTR-08 are named as NOT
  ADOPTED on their own APPLIES lines rather than silently ignored**, because a new rule
  nobody records reads as a rule somebody missed; SD-FMT-27 is adopted in the half that
  reaches a document, and SD-PRS-48's amendment, that a join which lands and cannot be
  scored has not answered the failure, is executed at Stage 4 item 6.
