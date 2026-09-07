# GROUP 25: PERSON TIER

Three or four cheap questions, answered by each user on their own first run,
then remembered. A frontline user is never asked anything from Groups 1 through
24. Every PERSON value is either directly known to the person or derivable from
their own record.

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| PERSON_ROLE_TITLE | The person's own job title, as written in the directory or as they say it. | PERSON | IGNITION | scalar | Resolves to exactly one key in ROLE_LADDER after abbreviation expansion and the wide-scope token test. If it resolves to none, ask once with the ladder's display names as options. | Claims Supervisor |
| PERSON_SCOPE_LEVEL | Which level of SCOPE_LEVELS the person owns. | PERSON | DEFERRED | scalar | Must be a key in SCOPE_LEVELS. Defaults to the scope_level of the resolved role and is confirmed, not prompted. | branch |
| PERSON_SCOPE_CODE | The identifier of the person's own unit at that level. | PERSON | IGNITION | scalar | Compared as text on both sides after padding. Must return rows against the resolved level's column. Accepted short and padded by the skill; never demanded padded. | 41207 |
| PERSON_SUPERVISOR_NAME | Who the person reports to. | PERSON | IGNITION | scalar | Resolved from the directory where a manager lookup exists; asked only when it does not. Recorded as empty only when the lookup was actually made and returned empty AND the person's own title names the top of the house. | District Claims Manager |
| PERSON_HAS_DIRECT_REPORTS | Whether the person leads people. | PERSON | IGNITION | scalar | Boolean. Decides the people-leadership objective and the attribution check. | true |
| PERSON_SUPERVISOR_CONTACT | The supervisor's mailbox, used to filter the priority sweep by sender. | PERSON | OPTIONAL | scalar | Contains one at-sign. Derived from the directory where possible. | district.manager at example-insure.test |
| PERSON_UPLINE_CHAIN | The resolved chain above the supervisor, to CHAIN_WALK_DEPTH. | PERSON | OPTIONAL | list | Derived, not asked. Each level recorded by name, including levels that published nothing. | 3 levels resolved |
| PERSON_SECONDARY_SCOPES | Additional scopes the person holds, for a mixed-scope role. | PERSON | OPTIONAL | list | Each entry names a level and a code. Store-level and aggregate claims are never blended in one sentence. | account: national logistics program |
| PERSON_DISPLAY_NAME | The name printed on the artifact. | PERSON | OPTIONAL | scalar | Non-empty if present. Derived from the directory. | A. Okonkwo |
| PERSON_CONTACT | The person's own address, printed for provenance only. | PERSON | OPTIONAL | scalar | Contains one at-sign. Never sent anywhere. | a.okonkwo at example-insure.test |
| PERSON_PREFERRED_LIST_SIZE | A standing override of the role default list size. | PERSON | OPTIONAL | scalar | Positive integer. Splits by USER_SIZE_TIER_1_FRACTION. Every cap and gate is unchanged. | 30 |
| PERSON_ROLE_START_DATE | When the person took this scope, so a prior-period comparison is not attributed to them wrongly. | PERSON | OPTIONAL | scalar | A valid date, not in the future. | 2026-03-02 |
| PERSON_CONFIRMED_FIELD_LIMITS | The character limits the person can read off the live form in five seconds. | PERSON | OPTIONAL | mapping | Overrides FIELD_LIMITS for this person's run only. Asked once, before drafting. | objective 500 |
| PERSON_BINDING_VERSION | The BUNDLE_VERSION the person's answers were captured against. | PERSON | DEFERRED | scalar | Re-ask the person tier when the ORG role ladder or scope hierarchy changes. | 3.1 |

---

# COUNTS

| Tier | IGNITION | DEFERRED | OPTIONAL | CONDITIONAL | Total |
|---|---|---|---|---|---|
| ORG | 10 | 364 | 52 | 41 | 467 |
| PERSON | 4 | 2 | 8 | 0 | 14 |
| Total | 14 | 366 | 60 | 41 | 481 |

Every DEFERRED variable carries a documented default and an exact degradation
notice in SECTION A1. Every CONDITIONAL variable carries its trigger, its
documented default once triggered, and its exact degradation notice in SECTION
A2. Coverage is exact in both directions: no DEFERRED variable lacks an A1 row,
and no CONDITIONAL variable lacks an A2 row.

**APPENDIX ROW COUNTS, which live here and nowhere else:**

| Appendix | Rows | Made up of |
|---|---|---|
| A1 | 381 | one row per DEFERRED variable, plus 15 sub-keys of three taxonomies, 9 on ROLE_LADDER, 5 on SCOPE_LEVELS and 1 on CREDITABLE_ENTITIES |
| A2 | 49 | one row per CONDITIONAL variable, plus 8 POPULATION_SHAPE sub-keys |

The row counts differ from the variable counts above only by those sub-key rows,
which is the whole of the discrepancy and the reason both figures are stated.
A figure restated outside the block that derives it is the single defect class
this schema has grown back most often, because a restatement drifts silently
while the block itself is checkable against the tables.

**MAINTAINER NOTE, AND IT HAS NOW BEEN NEEDED SIX TIMES.** Do not edit one of
these counts by hand after changing a table. Re-derive every count mechanically
from the tables and replace the whole block. Counts in this file drifted in five
consecutive revisions because each was adjusted by arithmetic in somebody's head.

**AND THIS BLOCK IS THE ONLY PLACE ANY OF THESE FIGURES APPEARS.** A count
restated anywhere else, in a change log, in a prose summary, in another file's
description of this one, or in an EXAMPLE cell, is a second source of truth that
nothing updates, and every drift found so far has been a restatement rather than
this block. Change logs record WHAT CHANGED AND WHY and state no totals. Another
file describing this one names the invariant, never the number: say that every
deferred variable carries a default and a notice, not how many there are. This is
the same rule the bundle already applies to gate counts under C5 and C8, applied
to itself.

**THE SWEEP TO RUN AFTER ANY TABLE CHANGE**, and it is three lines of script: count
the rows by tier and state from the variable tables; count the appendix rows; assert
that every DEFERRED variable has an A1 row and every CONDITIONAL variable an A2 row;
then replace this block wholesale. Then grep the bundle for any other digit string
claiming to be one of these counts and delete it rather than updating it.

By type: scalar 352; list 59; taxonomy 40; mapping 30. These four sum to 481, which equals the total above; a by-type line that does not reconcile to the total is a defect in this block, not a rounding.

Taxonomies declared in this schema, with their shapes specified above: 40.

ENTERPRISE_STRATEGY_PILLARS; ENTERPRISE_LONG_TERM_GOALS; SCOPE_LEVELS;
ROLE_LADDER; POPULATION_SHAPE; CREDITABLE_ENTITIES; BENCHMARK_POPULATIONS;
MEASURE_TIERS; COLUMN_CONCEPT_DICTIONARY; ORIGINATOR_PREFIX_MAP; WORK_TYPES;
REFERENCE_CLASSIFICATION_FIXTURE; PRIORITY_SOURCES; LINEAGE_LADDER;
PROCESS_CALENDAR; JURISDICTION_NAME_TO_CODE; COMPLIANCE_FINDINGS;
DELIVERABLE_LINES; TAB_CONTRACT; FORMATTING_ELEMENTS; GAP_TERM_DEFINITIONS;
GRADUATED_BUCKET; EXCEPTION_FLAGS; PLAY_RULES; FORM_SECTIONS; RATING_SCALE;
RATING_AXES; METRIC_SET; METRIC_MULTIPLIERS; QUESTION_BANK; HARD_GATES;
REGRESSION_CASES; EVIDENCE_SOURCES; CLASSIFICATION_LABELS; REASON_CODE_SET;
COUNTERFACTUAL_RUNG_SCOPES; CLOSE_STATE_VOCABULARY; URGENCY_VOCABULARY;
PASS_QUALIFIER_VOCABULARY; CLASSIFICATION_VOCABULARY.

COUNTERFACTUAL_LADDER is a fixed structure, not a bound variable: its six rungs
are specified in Group 6 and are not configurable. What is bound is which rungs
are available, which rung each metric uses, and how strongly each rung lets a
claim be worded.

Mappings that are flat key-to-value and are NOT taxonomies: SCOPE_LEVEL_ID_WIDTHS,
SCOPE_PLAIN_LANGUAGE_MAP, ROLE_TITLE_ABBREVIATIONS, ENTITY_BENCHMARK_MAP,
COUNTERFACTUAL_BY_METRIC, CLAIM_STRENGTH_BY_RUNG, SOURCE_AUTHORITY_MAP,
CHAIN_DISTANCE_WEIGHTS, PERIOD_TOKEN_MAP, CLOSE_WEIGHTS,
REFERENCE_VALIDITY_PERIODS, COMPLIANCE_GUIDE_SUPPLEMENTS, FIELD_LIMITS,
FIELD_BUDGET_SPLIT, FORM_SECTIONS_BY_CYCLE_POSITION, PRIORITY_BAND_THRESHOLDS,
FLAG_EXEMPTIONS, MSG_EMPTY_SECTION, SIBLING_SKILLS, CYCLE_POSITION_NAMES,
OUT_OF_MODEL_ESCAPES_ENABLED, CENTRAL_BRIEF_TABLE_COLUMNS,
PERSON_CONFIRMED_FIELD_LIMITS, CLASSIFICATION_FILLS.

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 25: Person tier

| Variable | Documented default | Degradation notice |
|---|---|---|
| PERSON_SCOPE_LEVEL | The scope level of the resolved role. | Your level was taken from your role rather than asked. If your role covers a different level than usual, say so and it will be recorded. |
| PERSON_BINDING_VERSION | The bundle version at the moment the answers were captured, recorded automatically. | Recorded automatically, never asked. |

---
