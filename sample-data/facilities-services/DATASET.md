# Facilities services dataset

A commercial HVAC and building services region. 48 sites, three technicians, a monthly
period plan and a daily dispatch feed. Deliberately a different industry from the
insurance agency dataset and from the consumer goods bundle in
`field-deployment-reference/`, so a reader can see the method move.

Run the recurring briefing as **T. Boone**, a technician, for **Tuesday 6 October 2026**.
Eight stops are scheduled.

## What a correct run finds

**Six things are planted here. A correct run catches all six.** They are listed so the
claim is checkable rather than asserted. No answer key is supplied for anything else.

### 1. One source is CARRIED, and every line from it must say so

`open_work_orders_AS_OF_2026-09-28.csv` is eight days older than the briefing.
`operator_notes.md` says the weekly export has been failing since the 28th, so the file
is real, readable and stale. The ladder resolves it to CARRIED.

**Correct:** every work-order line in the briefing carries the carried label and the date
28 September. **Wrong:** work orders presented plainly, as though read that morning. That
is the single failure this workflow exists to prevent, and it is invisible to a reader
unless the briefing says it.

### 2. One source is ABSENT for two of today's eight stops, and absence is not zero

`contract_status_2026-10.csv` has no row for **S-1011** or **S-1032**. Both are stops
today. `operator_notes.md` explains why: the renewals file does not cover sites in
onboarding.

**Correct:** those two stops print the bound named-absence string for contract status.
**Wrong:** a blank, a dash, "None", or a tier of zero. Nothing is known about their
contract; "we have no file for this site" and "this site has no contract" are different
facts and only one of them is true.

### 3. A genuine zero that must NOT be read as absent

**S-1026** IS in the work-order file and has **zero open work orders**. That is a
measured result, not a gap.

**Correct:** S-1026 reads as none open, stated as a fact, still carrying the carried
label from trap 1 because the file it came from is stale. **Wrong:** S-1026 treated the
same as S-1011's missing contract row. Traps 2 and 3 are the same cell value and
different facts, and a run that collapses them has failed the whole freshness contract.

### 4. One source is PARTLY AUTHORITATIVE AND PARTLY SELF-DISCLAIMED, which is three wrong answers rather than two

`parts_on_order_2026-10.csv` is not a clean CSV. Two title lines sit above the header,
**three clean rows follow it**, then a row of empty fields, then a prose note saying that
the rows BELOW IT are pending confirmation and may duplicate the rows above, then three
such rows, one of which duplicates a row above and one of which names a site with no part.

**Correct: the source resolves PER BLOCK rather than per source.** The three rows above the
file's own disclaimer are CURRENT and are printed, and all three are for sites on today's
schedule. The block below the disclaimer is never used as a VALUE, and is still READ, to
establish which sites it mentions, because "the readable block names no part for this site"
and "a row for this site sits in a block its own author disclaimed" are two different facts
and only one of them is an absence. So today's eight stops get three different sentences:
a part with its quantity and its due date; a statement that an unconfirmed row exists and
no part is shown; and a statement that the readable block holds nothing for this site and
that this is not a measured absence.

**Wrong, in THREE directions.** Treating the file as ABSENT, which tells the reader nothing
is there when something is. Parsing past the note and printing the unconfirmed rows, which
shows the S-1003 compressor twice and invents a part for S-1032. **And declaring the whole
file UNRESOLVED, which throws away three authoritative rows because a different block of
the same file is disclaimed.** That third answer is the one this sample itself shipped
first, and the rule that catches it is the shipped scorecard's own: two extractors fail
differently on the same document, so try a second reading before concluding a document is
unreadable. One of the three discarded rows is the compressor for the first stop of the
day.

### 5. A stop missing from ONE source, where every other source has it

**S-1047** is on today's schedule feed and is **not in the period plan**, which covers 44
of 48 sites. It IS in `sites.csv`, it IS in `contract_status_2026-10.csv`, and it has
**three open work orders** in the work-order export, one of them a condensate overflow in
a data room, seventeen days old.

**Correct: every section resolves against its own source and against no other.** S-1047
gets its header, its scheduled time, a PLAN section that is empty with a stated reason, and
its contract section and its work-order section and its parts line **in full**, because
those were read from their own sources and the period plan governs none of them.

**Wrong, in three directions.** Dropping the stop, which sends a technician a day that is
missing a visit. Generating plausible plan content for it, which is the fabrication the
method forbids outright. **And suppressing every section because one source has no row,
which is absence in one source read as absence in all** and is the exact collapse the whole
method exists to prevent. That third answer is the one this sample shipped first, and its
cost is specific: a technician drove to an unplanned call at a data room without being told
about three open work orders, under a line reading "everything below is omitted rather than
guessed" when nothing needed guessing.

### 6. The carried tripwire fires

Of four configured sources, one is CARRIED and one is UNRESOLVED. At the documented
default tripwire, half the sources rounded down with a floor of one, that is enough.

**Correct:** a banner above the first stop naming what is stale, not per-line labels
alone. **Wrong:** labels only. A technician scrolling a phone at 07:15 does not assemble
scattered labels into the conclusion that half the briefing is old.

## Files

| File | Role | Expected state |
|---|---|---|
| `sites.csv` | The population. 48 sites, three technicians. | reference |
| `period_plan_2026-10.csv` | The required source. Covers 44 of 48. | CURRENT |
| `schedule_feed_2026-10-06.csv` | Today's eight stops. | the delivery input |
| `open_work_orders_AS_OF_2026-09-28.csv` | Weekly export, failing since the 28th. | CARRIED |
| `contract_status_2026-10.csv` | Renewals file. No rows for S-1011, S-1032. Every renewal month is forward of the briefing date, as a renewals file published for a period carries the NEXT renewal. | CURRENT, with gaps |
| `parts_on_order_2026-10.csv` | Manual export, three clean rows then a self-disclaimed block. | PARTIALLY READ |
| `operator_notes.md` | Context a person would have. | reference |

## The second altitude, which has been run

Run the same date as **the regional manager** rather than as T. Boone:

    python3 ../../sample-output/build-briefing.py "J. Ferreira"

Span of control changes the altitude, and the manager does not get all three technicians'
stops concatenated. Same files, structurally different and correct outputs, nothing
configured between the two runs. That is the property the insurance dataset demonstrates
for the other three workflows, and it was a claim here until it was a result.

**It held, and the difference is not cosmetic.** The manager's briefing covers twenty-three
stops owned by three people, in one global time order, with one attribution per stop. It
groups nothing by person, computes no count per person, and its action list is written at
the aggregate tier, naming populations and sources and never an owner or a single stop. The
technician's briefing over the same files names one person's eight stops and writes its
actions as atoms. The person-bearing checks in `verify-briefing.py` run over both rendered
artifacts rather than over the intention, and pass on both.

**What the run produced that the narrow altitude could not was a defect, which is the
reason to run a second altitude at all.** A per-item explanatory sentence costs its full
length on every item carrying it while telling the reader one thing, and a span multiplies
the items. The parts-absence sentence alone accounted for two thousand nine hundred and
forty-one characters across eighteen stops. The build prints the measured share on every
run. Nothing in the specification was wrong; the message a manager would have received was
half explanation. **A rule tested at one width is a rule tested at one width**, and the
other technicians in this feed are two more widths nobody has run yet.

One rule did NOT transfer, and it is recorded as not adopted rather than quietly dropped:
SD-SPN-16's anonymous peer set, because both of its floors default to five while a manager's
span yields a sibling set of two, and the briefing computes no performance figure for a
distribution to sit behind. The workflow's A5.2.3 states that with its arithmetic.
