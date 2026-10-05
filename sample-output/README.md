# Sample output

Six artifacts, produced by an agent running these workflows against the two datasets in
`sample-data/`. Nothing here was hand-edited.

| File | Workflow | Reader |
|---|---|---|
| `Agency FAIRHAVEN 2026-10 Work Plan.xlsx` | Period planning | The Principal, whole agency |
| `Producer D-Whitlock 2026-10 Work Plan.xlsx` | Period planning | One producer, one book |
| `Agency FAIRHAVEN 2026-09 Requirement Scorecard.xlsx` | Standard gap scorecard | The Principal |
| `Producer D-Whitlock 2026 Performance Review.docx` | Objectives and review | One producer |
| `Briefing T-Boone 2026-10-06.html` | Recurring briefing | One technician, his own stops |
| `Briefing J-Ferreira 2026-10-06.html` | Recurring briefing | Her regional manager, a span of three |

**Each workflow ships two artifacts at two altitudes, and the pairs are the point.** The
two work plans have identical sections, columns and headers by contract, while their sizes,
the altitude of their language and the claims each reader is permitted to make are not. The
two briefings are the same property in a medium that cannot carry a Method tab.

## The workbooks and the review: what to look at first

Open the front panel of either workbook. It leads with the answer rather than the method:
what to do this week, what changes how to read the numbers, then how the list was built.
Then open the first action list and read the reason column. Every row says in plain
language why it sits where it does, naming the terms that actually moved it.

Then open the Method sheet at the end. Every default that was applied is named, every
capability that was missing is named with what it cost, and every figure reconciles.

## The briefings: rebuild them

Both are reproducible from `sample-data/facilities-services/`, byte for byte:

```
cd sample-output
python3 build-briefing.py "T. Boone"    && python3 verify-briefing.py "T. Boone"
python3 build-briefing.py "J. Ferreira" && python3 verify-briefing.py "J. Ferreira"
```

Open either in a browser, or on a phone, which is what they were built for.

**What the technician's briefing shows.** One weekday, his own scheduled stops, and every
trap planted in that dataset visible without reading the dataset notes: a banner above the
first stop saying part of the briefing is not current and why; work order lines carrying a
carried label and the date they were last current; a named absence for contract status
rather than a blank or a zero; a measured zero that says it is measured; parts resolved per
block, so the rows above the file's own disclaimer are printed, the block below it is never
used as a value, and a site named only in that block gets a sentence that is neither a part
nor an absence; and a stop whose plan section is empty for a stated reason while its
contract and work order sections are full, because those were read from their own sources.

**What the manager's briefing shows.** The same date and the same files over a span of
three technicians. She does not get three briefings concatenated and she does not get a
league table. Every stop in her span sits in one global time order, with one attribution per
stop in the same position, nothing grouped by person, no count computed per person, and an
action list written at the aggregate tier that names populations and sources and never an
owner or a single stop.

**That second altitude earned its place by producing a defect the first could not express.**
A per-item explanatory sentence costs its full length on every item carrying it while
telling the reader one thing, and a span multiplies the items: the parts-absence sentence
alone accounted for two thousand nine hundred and forty-one characters across eighteen
stops, and over half the manager's reader-facing text was explanation said more than once.
The relief moves the repeated wording into one block above the first stop and leaves a short
form on each stop. No stop is dropped, no per-item fact is dropped, and no state loses its
characters. The build prints the measured share on every run whether or not the relief
fires.

**The defects building this sample caught are recorded in one place**, Part I5 of
`skill/workflows/recurring-briefing.md`, with what each one cost and what rule came out of
it. They are not restated here: a record kept in two places is two records, and the one
that goes stale is the copy.

## How the briefings are verified

`verify-briefing.py` reads the RENDERED HTML rather than the code that produced it. A run
advances on evidence read from the artifact and never on the builder's report, because
"wrote eight stops" is a claim and a read showing eight populated stops is evidence. Four
families of check.

**The trap checks**, one per deliberate trap in the dataset. **The output contract checks**,
one per element the contract states. **The person-bearing checks**, which read the built
message back and test the interlock against what was rendered rather than against what the
build intended. **The second-channel checks**, which take away a channel the reader may not
receive and assert every state is still legible without it.

There are two such channels and they are independent. The styling goes first: the message
is re-read with its stylesheet and every class attribute stripped, because an email loses
its CSS routinely and on exactly the readers least able to recover it, and a workbook never
loses its fills. Then the key block goes: the item lines alone must still distinguish every
state, because **the key says which is which and is never permitted to carry the
distinction.** That second check was written after mutating a built artifact to collapse two
different parts states into one line and watching the styling check pass it.

**The record has three states, not two.** An assertion that never fired and an assertion
nobody wrote are indistinguishable in a two-state record, and the second is a defect hiding
inside a pass. A check whose precondition a run does not contain is recorded NOT APPLICABLE
with a reason drawn from a closed set, and **a not-applicable entry with no qualifying
reason is recorded NOT IMPLEMENTED, which fails.** That makes the failing state the default
for anything that could not be evaluated.

**Run both altitudes and the comparison is the point.** The same checks report several
not-applicable entries for the technician and one for the manager, because a run over one
person's stops genuinely cannot exercise a check about ordering across owners. In a
two-state record both would have read as all pass, and the narrow one would have been the
more reassuring of the two. The entry both runs record is DRIFTED: no previous resolution
record exists on a first rebuild, so this sample exercises four of the five source states
and says so rather than passing the fifth on an empty condition.

Every applicable check passes at both altitudes, and both rebuilds are byte-identical.
Each run prints its own tally, and that tally is the one place the number of checks is
stated.
