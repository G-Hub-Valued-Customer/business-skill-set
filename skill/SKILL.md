---
name: business-skill-set
description: >-
  Runs a business operating rhythm end to end and produces the real deliverable.
  Three workflows: build the prioritized work list for the coming period as a
  formatted spreadsheet; set objectives, track them and write the completed
  performance review as a document whose fields are separately copyable into a
  submission form; and score any population against any published standard with
  a reason code on every miss. Binds to any organization in about ten minutes
  and serves every level from a frontline employee to a chief executive. Use
  when asked to plan a period, prioritize accounts or territories, write or
  track objectives or a performance review, or score a population against a
  standard, policy or checklist.
---

# OPERATING CADENCE

One skill, three workflows, one shared body of judgment. **The agent reads this
file, picks the workflow, then reads that workflow. It reads nothing else until
something in the workflow cites it by name.**

---

**If the request is to try, test or demo this rather than to run it on real
work, read `README.md` at the bundle root and follow its Try It section.**
It offers a dataset and a workflow and then runs end to end with no further
setup. Nothing else in this file changes; the demo path is a way in, not a
different method.

---

# 1. PICK THE WORKFLOW

| The request is about | Workflow | It produces |
|---|---|---|
| What to work on next period. A plan, a target list, a route, a call list, what to prioritize, where to spend the month. | `workflows/period-planning.md` | A formatted spreadsheet |
| Objectives, goals, a self assessment, a mid-year or year-end review, a write-up for a form. | `workflows/objectives-and-review.md` | A document |
| Conformance to a published standard, policy, checklist or requirement set. Where are we failing, who is behind, what is missing. | `workflows/standard-gap-scorecard.md` | A formatted spreadsheet |

**Where a request touches two, run them separately and say so.** They rank on
different bases and merging their outputs produces a list that answers neither
question: planning ranks by opportunity, the scorecard ranks by severity.

**Where a request matches none of the three**, say what the skill does and does
not do rather than stretching a workflow to cover it. A workflow run outside
its subject produces a confident artifact about the wrong question.

---

# 2. THE FIVE RULES THAT GOVERN EVERY OTHER RULE

Carried here in full, verbatim from the doctrine, because they govern every
workflow and every reference file and a run must hold them before it reads
anything else.

- **G1. One declared contract per deliverable, superior to every other section.**
  Any later instruction that disagrees with the contract is the defect.
- **G2. Fail closed. Unknown is not pass.**
- **G3. Never default an unknown to the value that maximizes its score.**
- **G4. Every number carries a second number the writer did not choose.**
- **G5. A rule that costs nothing when it does not fire and keeps the method
  portable is worth carrying.**

---

# 3. HOW TO RESOLVE A CITATION

The workflows cite two kinds of thing by name. Both resolve to exactly one file,
deterministically, with no searching and no judgment.

| Citation | Resolves to | Rule |
|---|---|---|
| `SD-XXX-nn`, a doctrine rule | `reference/doctrine/XXX.md` | The three letters ARE the file name. The rule is under a heading that is the identifier itself. |
| A name in capitals with underscores, which is a configuration value | one file under `reference/schema/` | Look it up in `reference/schema/README.md`, which lists every variable and the one file it lives in. |

**A citation is resolved WHEN IT IS REACHED, never before.** This is the whole
reason the skill is a tree rather than one file: a run reads the router and one
workflow, then opens a reference file only when a step names something in it.

**AND NOTHING IS SUBSETTED.** Every rule and every variable the bundle carries
is present in this tree. A rule is never missing, only unread, and it is unread
only when nothing cited it. That is the difference between loading on demand
and shipping a subset, and it is the property that must never be traded for
speed: a workflow that cites a rule and cannot reach it STOPS and says so
rather than proceeding without it.

---

# 4. THE REFERENCE TREE

| File | What it holds | When it is read |
|---|---|---|
| `reference/capability-probe.md` | What tooling is available, and the degradation ladder for everything absent. | ALWAYS, at run start, before any stage. |
| `reference/output-contract.md` | The output medium per workflow, the formatting elements, the ranking and cap rules, and the verifications that block publication. | ALWAYS, before anything is built and again at the gate. |
| `reference/schema/README.md` | Every variable and the one file it lives in. | ALWAYS, so a variable can be resolved the moment one is named. |
| `reference/schema/group-*.md` | A group of variables, each with its definition, its documented default and its exact degradation notice together. | On demand, when a variable in it is named. |
| `reference/doctrine/README.md` | The groups, and the rule that an identifier names its own file. | ALWAYS, and it is short. |
| `reference/doctrine/XXX.md` | The rules in group XXX. | On demand, when an `SD-XXX-nn` is cited. |
| `reference/field-resolution.md` | How a column is found by concept rather than by literal header. | On demand, the first time a column must be resolved. |
| `reference/binding-interview.md` | The first-run interview, and how deferred values are asked later. | On the FIRST run at an organization, and afterwards only when a deferred value is requested. |

**Read `capability-probe.md` and `output-contract.md` on every run without being
told to.** Everything else waits to be named. Those two are not exceptions to
the on-demand rule; they are named by every workflow at stage zero and at the
gate, so loading them up front only saves a round trip.

---

# 5. BINDING, AND WHAT A FIRST RUN ACTUALLY COSTS

**On the first run at an organization, 10 values are asked.** Everything else is
DEFERRED: it is requested at the moment a decision actually needs it, from a
person who would know, once; or it takes its documented default and the exact
degradation notice is printed in the artifact. Nobody sits through an interview
before their first plan.

The ignition set, and it is the whole of it:

- `BINDING_OWNER_NAME`
- `COUNTERFACTUAL_AVAILABLE_RUNGS`
- `COUNTERFACTUAL_DEFAULT_RUNG`
- `MOVING_GROUND_NAME`
- `ORG_NAME`
- `PLANNING_PERIOD_LENGTH_DAYS`
- `PLANNING_PERIOD_NAME`
- `POPULATION_SHAPE`
- `ROLE_LADDER`
- `SCOPE_LEVELS`

`reference/binding-interview.md` holds the questions, their order and their
follow-ups. A frontline employee is never asked an organization-level question.

**An unbound value never produces a wrong answer.** It produces a documented
default, named in the output, or an honest notice saying what could not be
determined and what was therefore not attempted.

---

# 6. WHAT THIS SKILL WILL NOT DO

- It will not invent an organization fact that no document supports.
- It will not publish past a gate its own output contract failed.
- It will not report a number it could not compute; it reports that it could not
  compute it, and what that cost the reader.
- It will not merge a gap somebody can close with a gap set outside their
  control, and it will not mix missing evidence with a documented failure.

