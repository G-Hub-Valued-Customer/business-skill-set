# Sample dataset: Fairhaven Risk Partners

An invented independent insurance agency. Every name, account, producer, carrier and
figure in these files is fabricated. No real organization, person, address or account
number appears anywhere.

This is the dataset all four end-to-end test rounds were driven against, so what a
correct run should surface is not a prediction. It was measured.

## The organization

Three branches, five producers, one Principal who owns the whole agency. Roughly 214
accounts of which 190 are active and rankable. A published account servicing standard
with eight requirements, two of which are set outside the agency, by a federal rule and
by a carrier.

## The files

| File | What it is |
|---|---|
| `agency_book_2026Q4.csv` | The current book. One row per account: producer, branch, region, line of business, carrier, premium, expiration, loss ratio, policies in force, client since, last service touch, status, open service items. |
| `agency_book_2025Q4_prior.csv` | The prior year book, for period-over-period comparison. |
| `production_by_producer_2026.csv` | Written premium, new business, retention and account counts by producer, this year and last. |
| `october_directives.csv` | What branch managers directed, by account, with the instruction and the date. |
| `october_agency_priorities.md` | What operations published for the month. |
| `agency_objectives_2026.md` | The agency's four objectives for the year. |
| `service_standard_2026.md` | The eight-requirement account servicing standard, with who sets each one. |
| `servicing_evidence_2026Q4.csv` | Evidence per account per requirement. |
| `whitlock_objectives_2026.csv` | One producer's objectives for the year. |
| `whitlock_evidence_2026.md` | That producer's own notes on what he did. |

## Which workflow each set exercises

| Workflow | Files it needs |
|---|---|
| Period planning | the current book, the prior book, the directives, the priorities, the objectives |
| Standard gap scorecard | the servicing standard, the evidence file, the current book |
| Objectives and review | the producer objectives and evidence, the production file, both books, the agency objectives |

Two altitudes work on all three: run as the Principal for the whole agency, or as
producer D. Whitlock for one book. The same files produce structurally different and
correct outputs at each.

## What a correct run should surface, including the traps

Five things are planted here. A run that misses any of them is producing a confident
wrong answer, which is the failure mode this method exists to prevent.

**1. Premium growth that is not growth.** Producer D. Whitlock's written premium is up
2.72 percent year over year. Carriers filed rate increases that lifted premium roughly 7
percent across the book with no producer action at all, and the agency's own objectives
document says so in plain words. A correct run grades this a MISS against the
counterfactual and leads with it. Reporting +2.72 percent as an achievement is the
defect.

**2. A prior-year file that contains only survivors.** `agency_book_2025Q4_prior.csv`
has 201 rows and zero exits. Same-account growth computed on it is survivorship-biased,
and it would move the weakest of five producers from last to second. A correct run tests
the exit side of the prior file separately, refuses the comparison, and that ranking
appears nowhere.

**3. Blank evidence that is not failed evidence.** The servicing evidence carries three
states. A blank means the evidence was never captured, not that the requirement was
failed. A correct run keeps them apart and no published rate mixes them. Conflating them
turns "we do not know" into "you failed" against a named person.

**4. A requirement nobody at the agency can satisfy.** Requirement 8, carrier appetite
confirmation, is granted or refused by a carrier's underwriting desk. Where a carrier has
closed a class agency-wide, no producer action obtains it. But for other accounts it is
obtainable. A correct run reports the attributable rate and the total rate separately and
publishes both counts, rather than blaming producers for a carrier decision or
suppressing real work that somebody could actually do.

**5. A column that does not mean what the objective means.** One agency objective is
written in lines of business per account. The book carries a policy count. A
three-policy account can be one line. A correct run refuses to grade that objective
rather than reporting a number that looks right and is not.

## What was not planted

Everything else is ordinary. Nine directives in the month, a normal spread of expiration
dates, a realistic loss-ratio distribution and a handful of accounts in states that are
not workable this period. The point of the ordinary data is that the traps have to be
found among it rather than announced.
