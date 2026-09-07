# Business Skill Set

One skill, three workflows, for running a business operating rhythm and producing the
real deliverable at the end of it.

| Workflow | What it does | What it produces |
|---|---|---|
| **Period planning** | Builds the prioritized work list for the coming period. Reads every direction published by headquarters and by the supervisor chain, scores the whole population, and returns a ranked plan with a plain-language reason on every row. | Spreadsheet |
| **Objectives and review** | Sets objectives at period start, tracks mid-period, and writes the completed performance review. Wraps the character-limited fields of a submission form so each is separately copyable, with its limit and its live character count. | Document |
| **Standard gap scorecard** | Scores any population against any published standard, with a reason code on every miss and a rate that separates what a person can fix from what they cannot. | Spreadsheet |

Plain text. No install, no dependency, no vendor. Any agent that can read files, run code
and write a spreadsheet or a document can run it.

Author: Daniel J. Coon.

---

## Try it

**If you only want to judge the output, run nothing.** Open `sample-output/`. Those four
files were produced by these workflows against the data in `sample-data/`, unedited.

**To run a demo**, paste this to your agent:

> Read `skill/SKILL.md`, then run the demo described in `README.md`.

It should offer you a choice and then run end to end with no further setup:

```
Which would you like to run against?

  1  Insurance agency - a fully worked dataset with measured answers
  2  Bring your own data

Which workflow?

  a  Period planning        - what to work on next period, as a spreadsheet
  b  Objectives and review  - a performance review, as a document
  c  Standard gap scorecard - conformance to a published standard, as a spreadsheet
```

Choosing 1 runs against `sample-data/insurance-agency/`. Read that folder's `DATASET.md`
first if you want to know what the run should find: five things are planted in the data
and a correct run catches all five. Two altitudes are worth trying both ways. Run as the
Principal, who owns the whole agency, or as producer D. Whitlock, who owns one book of 48
accounts. Same files, same workflow, structurally different and correct outputs.

Choosing 2 starts the first-run interview: ten questions about the organization, in eight
conversational turns. Have your own files to hand.

### Whether this will work where you are, stated plainly

**A zip does not unpack itself.** If your agent can run code or has a filesystem, upload
the zip, ask it to unpack, and point it at this file. That works. **In a plain chat window
with no code execution the zip will do nothing** - that is a chat window behaving
normally, not the project failing. Two options there: clone or download the repository and
upload the folder contents, or upload just what one workflow needs, which is
`skill/SKILL.md` plus `skill/workflows/<the one you want>.md` plus
`skill/reference/output-contract.md` and `skill/reference/capability-probe.md`. The agent
will ask for a reference file when it needs one.

---

## How it is put together

One short router, three workflows, and a reference tree that is read on demand.

```
skill/
  SKILL.md                    the router. short, and the only file always read
  workflows/
    period-planning.md
    objectives-and-review.md
    standard-gap-scorecard.md
  reference/
    capability-probe.md       what tooling exists, and the ladder down when it does not
    output-contract.md        the formatting elements and the gates that block publication
    field-resolution.md       how a column is found by meaning rather than by header
    binding-interview.md      the first-run interview
    doctrine/                 one file per rule group, named by its three-letter code
    schema/                   one file per variable group
```

**Citations resolve on demand, deterministically.** A rule identifier of the form
`SD-CTR-01` resolves to `reference/doctrine/CTR.md`. The three letters ARE the file name:
no search, no index lookup, no ambiguity. A configuration variable resolves through
`reference/schema/README.md`, which lists every variable and the one file it lives in.

A run therefore reads the router, then one workflow, then only the reference files that
something actually names. It does not load the tree.

**And nothing is subsetted.** Every rule and every variable is present. A rule is never
missing, only unread, and it is unread only when nothing cited it. A workflow that cites
a rule it cannot reach stops and says so rather than proceeding without it. That
distinction is the whole difference between loading on demand and shipping a subset, and
it is never traded for speed.

**Each variable's default lives with its definition.** In the schema tree a variable's
definition, its documented default and its exact degradation notice are in the same file.
They were deliberately moved together, because a run holding a definition without the
default would have nothing to print at the moment a value turns out to be unbound, and
that is the guarantee the whole method rests on.

---

## How to run one

1. Give the agent `skill/SKILL.md`. It picks the workflow from what you asked for.
2. Point it at your data and tell it who is asking. That is the whole invocation.
3. On the first run at an organization it asks ten questions, in eight conversational
   turns, in under ten minutes. Someone who knows the business answers them once. After
   that each person answers four questions about themselves on their own first run, and
   nobody is ever asked an organization-level question again.
4. Anything still unbound is requested at the moment a decision actually needs it, or
   defaulted with the default named in the output.

A frontline employee and a chief executive run the same workflow and get structurally
different, correct answers. Neither configures anything.

---

## What makes it portable

**Nothing organization-specific is written into the text.** Every such value is a named
variable with a documented default, a tier, and an exact degradation notice. That is what
makes it portable, and it is also why it carries nothing confidential: there are no
literals to leak.

Field resolution is by CONCEPT, never by literal column header. It looks for the column
that means "the date this closes", not for a column called `close_date`. The seed
dictionary is extended at run time and never written back on a run's own authority.

**No tooling is assumed.** It probes what is available at run start and takes a
documented, named path down when something is missing. A missing capability produces a
stated degradation, never a silent wrong answer.

---

## The ideas underneath

**Everything is ranked by real business volume and real impact, not by activity.** This is
the first idea and the others serve it. A list of things to do that is not weighted by
what each one is actually worth is a to-do list, and a to-do list is what people already
have. Every unit carries the measure that matters, the size of the gap against a
comparable population, how soon a commitment falls due, how much work it would take to
close, how much of that work is already done, and how much direction from above is
pointed at it. Those combine into one published score, and the row states in plain
language which terms moved it. Lowest effort, highest return is not a slogan here; it is
the sort order, and the reader can check it row by row.

**Every metric carries a counterfactual denominator** - a second number the writer did not
choose. Six ranked sources, best to worst: share of a bounded addressable population, a
matched control group, a peer distribution, plan attainment, own prior period run rate,
and the bare denominator population. An organization with no competitive market still has
a moving baseline, and the binding forces it to name what its ground is. This is what
stops a review from crediting somebody for a rising tide.

**Span of control decides everything about the output** - its size, its altitude, and
which claims the reader may make. It is detected, not configured.

**Cold starts cannot manufacture a result.** A population where no unit has a prior period
is not the same as a new unit inside an established one. Cold starts are detected rather
than declared, and no WIN or MISS can attach where no prior period exists. What stays
claimable is stated explicitly and surfaced without being asked.

**Blank is not fail.** Missing evidence and a documented failure are different facts and
no published rate mixes them. Conflating them turns "we do not know" into "you failed".

**Attributable and total are reported separately.** A gap somebody can close and a gap set
by a regulator, a carrier or head office are never averaged together. Suppressing the
second kind would take real work off an honest person's list; merging them would blame a
person for something outside their control.

**Formatting is a correctness property.** Header row in row 1. A filter on every column. A
rank and a reason for that rank on every row. Column widths computed from the header plus
an allowance for the filter dropdown, so no header is ever hidden, and never narrower than
the longest word they must display, so no word is ever broken by a cell line. Row heights
computed from wrapped content, so nothing clips. Every capped sheet states `showing n of N`
and reconciles against its own method section. All of it is verified programmatically
against the BUILT file before publication, and a failure blocks publication.

**Formatting degrades safely.** The header band is light and the ink is dark, so the header
stays readable if the fill fails to render and also if the font colour fails to render. A
dark band carrying white text fails catastrophically in one of those directions, and it
failed exactly that way in an earlier build. Every colour is written with an explicit
opaque alpha, because a transparent alpha renders correctly in the tool the file was built
in and invisibly in the tool the reader opens.

---

## Verification

Mechanically checked on every build: every rule identifier resolves to the one file its
own name specifies; every variable resolves to one file that actually defines it; every
deferred variable has its default in the same file as its definition; no duplicate
headings; no malformed table rows; ASCII only; no organization names, system names,
document numbers, identifiers, endpoints or URLs anywhere. The split from the earlier
single-file form is proved lossless by comparing every source word against the tree.

Acceptance tested across seventeen adversarial rounds. First against five invented
organizations at two and three altitudes each, on paper: a regional hospital system with
no competitive category, a B2B software company with a flowing pipeline, a consumer goods
company launching a new category with no history, a restaurant chain, and an insurance
agency. Then, in the last four rounds, all three workflows were driven END TO END against
real files by agents that had never seen them, that were told to be hostile, and that were
required to verify by reading the built artifact back through the engine rather than
trusting their own build code.

| Round | Defects found | Verdict on every prior defect, judged by execution |
|---|---|---|
| Fourteen | 53 | first end to end round |
| Fifteen | 39 | 45 of 53 fixed, 6 partial, 2 still present |
| Sixteen | 34 | 85 of 92 fixed, 6 partial, 1 still present |
| Seventeen | remediation and one production run | all 34 fixed |

Deliberate traps were planted in the test data. All were caught. They are documented in
`sample-data/insurance-agency/DATASET.md`, so anyone can check the claim by running it.

- A producer whose headline premium growth read +2.72 percent, in a year when carrier rate
  filings lifted premium about 7 percent for everyone with no producer action. Graded a
  MISS against the counterfactual, and led with rather than buried.
- A prior-period file containing only survivors and zero exits. Growth computed on it
  would have moved the weakest performer from last of five to second. The exit test caught
  the file and that ranking appears nowhere.
- Evidence carrying three states where a blank meant missing rather than failed. Kept
  separate throughout.
- A requirement genuinely outside a reader's control for some units and obtainable for
  others. Routed at the granularity the finding actually holds at, with both counts
  published.

One more was not planted and caught itself: an objective written in lines of business
against a data column holding a policy count. A three-policy account can be one line. The
run refused to grade the objective rather than report a false number.

---

## If something looks wrong

**It says a capability is absent and degrades.** That is designed. It probes at run start
and takes a documented path down. The output names what was unavailable and what it cost.

**It refuses to compute something.** Read the reason. In testing most refusals were
correct: a column that did not mean what the objective meant, a prior-period file that
contained only survivors, evidence that was missing rather than failed.

**It asks a question you cannot answer.** Say so. Every deferred value has a documented
default and the default is named in the output.

**The output is large or small.** The size is set by the reader's span of control, not by
the data. A frontline reader gets a short list; a senior reader gets a wider one that is a
far smaller share of what they own.

---

## Honest limits

- The end-to-end testing covered one industry's shape of data. The paper testing covered
  five. Run yours once with somebody watching before anyone acts on the output.
- It is long. That is deliberate: nothing that worked was removed to make it shorter. The
  length is judgment written out, not padding, and the tree means a run reads a fraction
  of it.
- It does not integrate with anything. It reads files and published documents and writes a
  file. If your priorities live only in a system with an API, somebody has to export them
  first.
- One dataset ships, not five. The other four industries were paper tests and no files
  were ever built for them. `sample-data/README.md` says so plainly rather than shipping
  datasets for runs that never happened.

---

## License

Licensed under the MIT License. See `LICENSE`. The MIT License grants copyright
permissions only. No patent license is granted. The author has patent applications pending
covering related subject matter, and those rights are expressly reserved.
