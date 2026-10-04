# Manifest

Every file in this bundle, so an agent that unpacked it knows what it received. The count
below is the number of rows in the table, so the two cannot disagree.

**`field-deployment-reference/` ships in the repository and is NOT listed below.** It is a
company-neutral specification of the eight-skill production bundle this method came out of:
nothing in it runs, nothing in the skill tree cites it, and no workflow reads it. It has its
own README listing its own files. **The omission is stated here rather than left silent**,
because a reader who counts the repository's files and compares against this table should
find out why the numbers differ from the table itself and not from guessing.

98 files.

| File | Size | What it is |
|---|---|---|
| `GITHUB-ABOUT.txt` | 2 KB | Repository metadata, not part of the skill: the text of the GitHub About field and topics, with a note on why the public README was reordered. |
| `LICENSE` | 1 KB | MIT licence, with a patent reservation. |
| `MANIFEST.md` | 12 KB | Every file in this bundle, so an agent that unpacked it knows what it received. The count above is the number of rows in this table. |
| `README.md` | 16 KB | Start here. What this is, how to try it, the ideas underneath it, and how it was verified. |
| `conformance-check.py` | 16 KB | Checks the whole tree for the defects a workflow's integration can introduce: hardcoded skill or group counts, unknown Applies tokens, unrouted workflows, index and group-table disagreement, an unreachable reference file, a relied-on doctrine rule that does not name the relying skill, and incomplete gate records. Exits non-zero on any failure. |
| `sample-data/README.md` | 2 KB | What sample data ships, which workflows each dataset was driven against, and the standard a dataset has to meet to be here. |
| `sample-data/facilities-services/DATASET.md` | 9 KB | The second worked dataset: a facilities services contractor, the files, the traps planted in them, and the second altitude. |
| `sample-data/facilities-services/contract_status_2026-10.csv` | 1 KB | Sample data file for the facilities dataset: contract tier and renewal, with no row for some scheduled sites. All content invented. |
| `sample-data/facilities-services/open_work_orders_AS_OF_2026-09-28.csv` | 4 KB | Sample data file for the facilities dataset: a work order export older than the briefing, carrying its own as-of date. All content invented. |
| `sample-data/facilities-services/operator_notes.md` | 1 KB | Sample data file for the facilities dataset: what the person who assembled the files said about them. All content invented. |
| `sample-data/facilities-services/parts_on_order_2026-10.csv` | 1 KB | Sample data file for the facilities dataset: a hand-made export whose own author disclaimed the rows below a note. All content invented. |
| `sample-data/facilities-services/period_plan_2026-10.csv` | 2 KB | Sample data file for the facilities dataset: the month's plan, which does not cover every scheduled stop. All content invented. |
| `sample-data/facilities-services/schedule_feed_2026-10-06.csv` | 2 KB | Sample data file for the facilities dataset: one day's regional schedule across three technicians. All content invented. |
| `sample-data/facilities-services/sites.csv` | 3 KB | Sample data file for the facilities dataset: the site register. All content invented. |
| `sample-data/insurance-agency/DATASET.md` | 5 KB | The first worked dataset: the organization, the files, and the five traps planted in it. |
| `sample-data/insurance-agency/agency_book_2025Q4_prior.csv` | 11 KB | Sample data file for the worked dataset. All content invented. |
| `sample-data/insurance-agency/agency_book_2026Q4.csv` | 28 KB | Sample data file for the worked dataset. All content invented. |
| `sample-data/insurance-agency/agency_objectives_2026.md` | 1 KB | Sample data file for the worked dataset. All content invented. |
| `sample-data/insurance-agency/october_agency_priorities.md` | 1 KB | Sample data file for the worked dataset. All content invented. |
| `sample-data/insurance-agency/october_directives.csv` | 2 KB | Sample data file for the worked dataset. All content invented. |
| `sample-data/insurance-agency/production_by_producer_2026.csv` | 1 KB | Sample data file for the worked dataset. All content invented. |
| `sample-data/insurance-agency/service_standard_2026.md` | 1 KB | Sample data file for the worked dataset. All content invented. |
| `sample-data/insurance-agency/servicing_evidence_2026Q4.csv` | 22 KB | Sample data file for the worked dataset. All content invented. |
| `sample-data/insurance-agency/whitlock_evidence_2026.md` | 1 KB | Sample data file for the worked dataset. All content invented. |
| `sample-data/insurance-agency/whitlock_objectives_2026.csv` | 1 KB | Sample data file for the worked dataset. All content invented. |
| `sample-output/Agency FAIRHAVEN 2026-09 Requirement Scorecard.xlsx` | 69 KB | Artifact produced by a workflow from the sample dataset. Not hand-edited. |
| `sample-output/Agency FAIRHAVEN 2026-10 Work Plan.xlsx` | 82 KB | Artifact produced by a workflow from the sample dataset. Not hand-edited. |
| `sample-output/Briefing J-Ferreira 2026-10-06.html` | 21 KB | Artifact produced by a workflow from the facilities dataset, at the regional manager altitude. Not hand-edited. |
| `sample-output/Briefing T-Boone 2026-10-06.html` | 10 KB | Artifact produced by a workflow from the facilities dataset, at the technician altitude. Not hand-edited. |
| `sample-output/Producer D-Whitlock 2026 Performance Review.docx` | 50 KB | Artifact produced by a workflow from the sample dataset. Not hand-edited. |
| `sample-output/Producer D-Whitlock 2026-10 Work Plan.xlsx` | 56 KB | Artifact produced by a workflow from the sample dataset. Not hand-edited. |
| `sample-output/README.md` | 7 KB | What the six sample artifacts are, what to look at first, and how the two briefings are rebuilt and verified. |
| `sample-output/build-briefing.py` | 37 KB | Builds both briefing artifacts from the facilities dataset, at whichever altitude is named. Reproducible byte for byte, and prints its own measured bounds on every run. |
| `sample-output/verify-briefing.py` | 24 KB | Checks the rendered briefings against the contract in three states, and exits non-zero on a failure or an unexplained not-applicable. |
| `skill/SKILL.md` | 9 KB | THE ROUTER. The only file always read. Picks the workflow and states how citations resolve. |
| `skill/reference/binding-interview.md` | 132 KB | The first-run interview, and how deferred values are asked later. |
| `skill/reference/capability-probe.md` | 44 KB | What tooling is available, and the degradation ladder for what is absent. |
| `skill/reference/doctrine/BRD.md` | 5 KB | Doctrine group BRD. Every rule identified SD-BRD-nn is defined here. |
| `skill/reference/doctrine/CLM.md` | 37 KB | Doctrine group CLM. Every rule identified SD-CLM-nn is defined here. |
| `skill/reference/doctrine/CMP.md` | 9 KB | Doctrine group CMP. Every rule identified SD-CMP-nn is defined here. |
| `skill/reference/doctrine/CNF.md` | 9 KB | Doctrine group CNF. Every rule identified SD-CNF-nn is defined here. |
| `skill/reference/doctrine/CTR.md` | 31 KB | Doctrine group CTR. Every rule identified SD-CTR-nn is defined here. |
| `skill/reference/doctrine/DUP.md` | 4 KB | Doctrine group DUP. Every rule identified SD-DUP-nn is defined here. |
| `skill/reference/doctrine/EFF.md` | 18 KB | Doctrine group EFF. Every rule identified SD-EFF-nn is defined here. |
| `skill/reference/doctrine/EXC.md` | 20 KB | Doctrine group EXC. Every rule identified SD-EXC-nn is defined here. |
| `skill/reference/doctrine/FMT.md` | 60 KB | Doctrine group FMT. Every rule identified SD-FMT-nn is defined here. |
| `skill/reference/doctrine/IDN.md` | 11 KB | Doctrine group IDN. Every rule identified SD-IDN-nn is defined here. |
| `skill/reference/doctrine/LNG.md` | 8 KB | Doctrine group LNG. Every rule identified SD-LNG-nn is defined here. |
| `skill/reference/doctrine/MND.md` | 2 KB | Doctrine group MND. Every rule identified SD-MND-nn is defined here. |
| `skill/reference/doctrine/POP.md` | 36 KB | Doctrine group POP. Every rule identified SD-POP-nn is defined here. |
| `skill/reference/doctrine/PRI.md` | 15 KB | Doctrine group PRI. Every rule identified SD-PRI-nn is defined here. |
| `skill/reference/doctrine/PRS.md` | 28 KB | Doctrine group PRS. Every rule identified SD-PRS-nn is defined here. |
| `skill/reference/doctrine/QUA.md` | 7 KB | Doctrine group QUA. Every rule identified SD-QUA-nn is defined here. |
| `skill/reference/doctrine/README.md` | 5 KB | The doctrine groups, and the rule that an identifier names its own file. |
| `skill/reference/doctrine/RNK.md` | 8 KB | Doctrine group RNK. Every rule identified SD-RNK-nn is defined here. |
| `skill/reference/doctrine/RUN.md` | 7 KB | Doctrine group RUN. Every rule identified SD-RUN-nn is defined here. |
| `skill/reference/doctrine/SCL.md` | 40 KB | Doctrine group SCL. Every rule identified SD-SCL-nn is defined here. |
| `skill/reference/doctrine/SCO.md` | 12 KB | Doctrine group SCO. Every rule identified SD-SCO-nn is defined here. |
| `skill/reference/doctrine/SPN.md` | 19 KB | Doctrine group SPN. Every rule identified SD-SPN-nn is defined here. |
| `skill/reference/doctrine/SRC.md` | 12 KB | Doctrine group SRC. Every rule identified SD-SRC-nn is defined here. |
| `skill/reference/doctrine/STR.md` | 5 KB | Doctrine group STR. Every rule identified SD-STR-nn is defined here. |
| `skill/reference/doctrine/WGT.md` | 9 KB | Doctrine group WGT. Every rule identified SD-WGT-nn is defined here. |
| `skill/reference/field-resolution.md` | 113 KB | How a column is found by what it MEANS rather than by its header. |
| `skill/reference/output-contract.md` | 130 KB | The formatting elements, ranking rules, caps, and the verifications that block publication. |
| `skill/reference/schema/README.md` | 67 KB | Every configuration variable and the one file it lives in. |
| `skill/reference/schema/breadth-section.md` | 5 KB | Schema: breadth section. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/bundle-identity-and-attribution.md` | 4 KB | Schema: bundle identity and attribution. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/column-concept-dictionary.md` | 9 KB | Schema: column concept dictionary. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/compliance-and-jurisdiction.md` | 6 KB | Schema: compliance and jurisdiction. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/counterfactual-denominator.md` | 28 KB | Schema: counterfactual denominator. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/creditable-entities.md` | 14 KB | Schema: creditable entities. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/defaults-and-notices.md` | 1 KB | Schema: defaults and notices. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/deliverable-contract.md` | 21 KB | Schema: deliverable contract. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/exception-flags-and-thresholds.md` | 22 KB | Schema: exception flags and thresholds. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/formatting.md` | 63 KB | Schema: formatting. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/intentional-non-variables.md` | 6 KB | Schema: intentional non variables. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/language-labels-and-messages.md` | 53 KB | Schema: language labels and messages. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/lineage-and-claims.md` | 6 KB | Schema: lineage and claims. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/measures-and-units.md` | 10 KB | Schema: measures and units. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/organization-identity.md` | 3 KB | Schema: organization identity. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/periods-and-the-operating-calendar.md` | 11 KB | Schema: periods and the operating calendar. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/person-tier.md` | 9 KB | Schema: person tier. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/population-shape.md` | 28 KB | Schema: population shape. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/priority-sources-and-authority.md` | 9 KB | Schema: priority sources and authority. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/questions-and-interaction.md` | 5 KB | Schema: questions and interaction. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/recurring-delivery.md` | 30 KB | Schema: recurring delivery. Variables with their definitions, defaults and degradation notices. The one group specific to a single workflow, which it says in its own opening line. |
| `skill/reference/schema/review-form-and-field-limits.md` | 22 KB | Schema: review form and field limits. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/role-ladder.md` | 13 KB | Schema: role ladder. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/run-control-and-reliability.md` | 9 KB | Schema: run control and reliability. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/scope-hierarchy.md` | 13 KB | Schema: scope hierarchy. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/scoring-constants.md` | 8 KB | Schema: scoring constants. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/systems-of-record-and-capability-bindings.md` | 6 KB | Schema: systems of record and capability bindings. Variables with their definitions, defaults and degradation notices. |
| `skill/reference/schema/unbound-variable-limits.md` | 60 KB | NOT a group file and defines no variable: Appendix B, what an unbound variable may never do, plus the change log of this schema's acceptance-test remediation. Kept for provenance, read by nobody during a run, and named in the schema index so it is accounted for. Every governing rule in it is also stated in a file a run can reach. |
| `skill/reference/schema/work-items-and-work-types.md` | 5 KB | Schema: work items and work types. Variables with their definitions, defaults and degradation notices. |
| `skill/workflows/objectives-and-review.md` | 508 KB | WORKFLOW: sets objectives, tracks them, writes the completed review. |
| `skill/workflows/period-planning.md` | 730 KB | WORKFLOW: builds the prioritized work list for the coming period. |
| `skill/workflows/recurring-briefing.md` | 132 KB | WORKFLOW: assembles and sends one recurring briefing, unasked, to one person. |
| `skill/workflows/standard-gap-scorecard.md` | 372 KB | WORKFLOW: scores a population against a published standard. |

## How the skill tree is meant to be read

Only `skill/SKILL.md` is always read. It is short. It picks one workflow, and that
workflow is the second and last file read up front. Everything under
`skill/reference/` is opened only when something names it: a rule identifier of the
form `SD-XXX-nn` resolves to `skill/reference/doctrine/XXX.md`, and a configuration
variable resolves through `skill/reference/schema/README.md` to one group file.

**Nothing is subsetted.** Every rule and every variable is present in the tree. A
rule is never missing, only unread, and it is unread only when nothing cited it.

