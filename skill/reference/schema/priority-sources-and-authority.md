# GROUP 11: PRIORITY SOURCES AND AUTHORITY

TAXONOMY SHAPE, SOURCE_AUTHORITY_MAP. A map from QUESTION to the one artifact
that settles it. The mapping is by question, never by document rank.

Questions that must be answered: who defines the deliverable form; who defines
the goal methodology; who defines the quality bar; who defines strategy; who
defines priority ranking; who defines local targets; what counts as evidence.

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| SOURCE_AUTHORITY_MAP | Question to authoritative artifact. | ORG | DEFERRED | mapping | All seven questions present. No artifact answers more than one question unless stated. | priority ranking to incentive plan weights; local targets to supervisor chain messages |
| PRIORITY_SOURCE_COUNT | How many priority sources are read every run. | ORG | DEFERRED | scalar | Integer at least 2. Always all of them, every run. | 3 |
| PRIORITY_SOURCES | The named priority sources with their order of authority. | ORG | DEFERRED | taxonomy | Each entry has key, display_name, cadence (live or cached), and distance_weighted (boolean). The nearest source is read first and outranks the rest. | supervisor_current live; supervisor_prior live; central_brief cached |
| SUPERVISOR_SWEEP_WINDOW_CURRENT | Days back the current-period sender sweep covers. | ORG | DEFERRED | scalar | Integer at least 14. | 30 |
| SUPERVISOR_SWEEP_WINDOW_PRIOR | Days back the carry-forward sweep covers. | ORG | DEFERRED | scalar | Integer greater than the current window. | 60 |
| CHAIN_WALK_DEPTH | How many levels up the supervisor chain are searched. | ORG | DEFERRED | scalar | Integer at least 1. | 4 |
| CHAIN_DISTANCE_WEIGHTS | Weight applied to a priority by how far up the chain it came from. | ORG | DEFERRED | mapping | Keys are distances 1 upward. Values strictly decreasing, all in the range 0 to 1, first equal to 1.00. | 1 to 1.00; 2 to 0.70; 3 to 0.50; 4 to 0.30 |
| SOURCE_BOOST_NONE | The boost applied when NO source named the item, which is every item whenever mail and document access are both absent. | ORG | DEFERRED | scalar | Exactly 1.0, neutral. It is the floor of the source-boost scale, so naming a source can only raise a result and never lower one, per SD-WGT-02. It is never 0, which would delete the alignment term. | 1.0 |
| SOURCE_BOOST_ONE | Boost when one source named the item. | ORG | DEFERRED | scalar | At least SOURCE_BOOST_NONE. | 1.5 |
| SOURCE_BOOST_BOTH | Boost when two independent sources named it. | ORG | DEFERRED | scalar | Greater than SOURCE_BOOST_ONE. | 2.0 |
| MANDATORY_MULTIPLIER | Multiplier applied ONCE to the finished score of a unit named on a directive list. | ORG | DEFERRED | scalar | Greater than 1. Applied once, on the finished score, never also inside a term. | 2.00 |
| DIRECTIVE_RELEASE_PHRASES | Phrases that release a unit from a directive list. | ORG | DEFERRED | list | Non-empty. Nothing else releases an item. | do not work these; disregard; handled elsewhere |
| ACTOR_TEST_ENABLED | Whether a list naming another party as the actor is read as an assignment rather than a directive. | ORG | DEFERRED | scalar | Boolean. Must be true. The actor test is the only test. | true |
| CENTRAL_BRIEF_NAME | The periodic document that publishes the period's priorities, due dates, work types and eligibility. | ORG | OPTIONAL | scalar | A name, never a path. | monthly operations brief |
| CENTRAL_BRIEF_TABLE_COLUMNS | The published columns to parse from that document. | ORG | CONDITIONAL | mapping | Required when a central brief is bound. Keys: description, due, resources, eligibility. | description; due; supporting resources; eligible |
| CENTRAL_BRIEF_REQUIRED | Whether the run stops if the brief is unreachable. | ORG | DEFERRED | scalar | Boolean. Must be false. A missing central source is never a stop. | false |
| HQ_FLAG_BREADTH_LIMIT | A per-unit targeting flag counts as centrally named only when it is carried by less than this share of the scope. | ORG | DEFERRED | scalar | Fraction between 0 and 0.5. | 0.15 |
| NARROWNESS_THRESHOLD | A work item flagged on less than this share of the ranked population is a sharper priority and takes the narrowness multiplier. | ORG | DEFERRED | scalar | Fraction between 0 and 0.5. | 0.10 |
| NARROWNESS_MULTIPLIER | The multiplier a narrow instruction takes. | ORG | DEFERRED | scalar | Greater than 1. | 1.25 |
| OWN_ACTION_MARKER_CONCEPT | The concept key of the PUBLISHED marker that says an item requires this role's action. | ORG | OPTIONAL | scalar | Must be a published marker. Never inferred from verbs in the item name. | concept_requires_adjuster_action |
| OWN_ACTION_MULTIPLIER | The multiplier that marker confers. | ORG | CONDITIONAL | scalar | Greater than 1. Required when the marker concept is bound. | 1.25 |
| LOCAL_BOOST | The multiplier a work item tagged to the user's own unit receives. | ORG | DEFERRED | scalar | Greater than 1. | 1.25 |
| LOCAL_OVERRIDE_DEPTH | How many levels of the user's own scope count as a DIRECT local tag that overrides a work-type weight, as opposed to a broader tag that gives the boost only. | ORG | DEFERRED | scalar | Integer 1 or 2. | 2 |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 11: Priority sources and authority

| Variable | Documented default | Degradation notice |
|---|---|---|
| SOURCE_AUTHORITY_MAP | Empty. Each question falls to the nearest source that answers it. | It is not recorded which document settles which question, so where two sources disagreed this report followed the nearer one and named the disagreement. |
| PRIORITY_SOURCE_COUNT | Derived from PRIORITY_SOURCES. | Derived rather than stated. |
| PRIORITY_SOURCES | The supervisor chain only, read live. | Only your supervisor chain was read for priorities. No central or published priority source has been bound, so nothing in this report reflects an organization-wide priority. |
| SUPERVISOR_SWEEP_WINDOW_CURRENT | 30 days. | The standing current-period window was used for the message sweep. The window covered is stated with the count of messages read. |
| SUPERVISOR_SWEEP_WINDOW_PRIOR | 60 days. | The standing carry-forward window was used. |
| CHAIN_WALK_DEPTH | 4. | The standing chain depth was used. Every level resolved is named, including levels that published nothing. |
| CHAIN_DISTANCE_WEIGHTS | 1.00, 0.70, 0.50, 0.30 by distance. | The standing distance weights were used, so a priority from further up the chain counts for less than one from your own manager. |
| SOURCE_BOOST_NONE | 1.0, neutral, which is the floor of the scale. | No boost value was set for an item that no source named, so the neutral floor was used. Where no priority source could be read at all, which this report says plainly if it happened, every item took it and the alignment term rests on work type and close weight alone. |
| SOURCE_BOOST_ONE | 1.5. | The standing single-source boost was used. |
| SOURCE_BOOST_BOTH | 2.0. | The standing two-source boost was used. |
| MANDATORY_MULTIPLIER | 2.00. | The standing multiplier for a directed unit was used, applied once on the finished score. |
| DIRECTIVE_RELEASE_PHRASES | The generic set: do not work these, disregard, handled elsewhere, no action needed. | No local release phrases are bound. A manager's instruction to stand down using different wording will not be recognized, and those units stay on the directed list. |
| ACTOR_TEST_ENABLED | true. | The actor test is on, which is the only permitted setting: a list naming someone else as the actor is an assignment, not a directive. |
| CENTRAL_BRIEF_REQUIRED | false. | A missing central brief is never a stop, which is the only permitted setting. |
| HQ_FLAG_BREADTH_LIMIT | 0.15. | The standing breadth limit was used: a targeting flag counts as centrally named only when it is carried by fewer than fifteen percent of your scope. |
| NARROWNESS_THRESHOLD | 0.10. | The standing narrowness threshold was used. |
| NARROWNESS_MULTIPLIER | 1.25. | The standing narrowness multiplier was used. |
| LOCAL_BOOST | 1.25. | The standing local boost was used for work tagged to your own unit. |
| LOCAL_OVERRIDE_DEPTH | 2. | The standing override depth was used: a tag at your own finest two levels overrides a work-type weight, a broader tag does not. |

---

## CONDITIONAL DEFAULTS AND NOTICES ONCE TRIGGERED, FOR THIS GROUP

Moved here from APPENDIX A2 for the same reason. The text is unchanged.

### Group 11: Priority sources and authority

| Variable | Trigger | Documented default | Degradation notice |
|---|---|---|---|
| CENTRAL_BRIEF_TABLE_COLUMNS | CENTRAL_BRIEF_NAME is bound and the brief is parsed | The four generic columns resolved from the document by the shared dictionary: description, due, resources, eligibility. | The columns of your published brief were resolved from the shared dictionary rather than declared. Every item whose date could not be read is named and takes a banded fallback weight rather than being assumed to close this period. |
| OWN_ACTION_MULTIPLIER | OWN_ACTION_MARKER_CONCEPT is bound | 1.25. | No multiplier was set for work marked as requiring your action specifically, so a standing one was used. |
