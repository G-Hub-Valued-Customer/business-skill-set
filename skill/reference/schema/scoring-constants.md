# GROUP 17: SCORING CONSTANTS

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| SCORE_FORMULA_SHAPE | The composite score expression, written out. | ORG | DEFERRED | scalar | Multiplicative bracket times measure percentile raised to MEASURE_EXPONENT. Every constant referenced by name. | (1.0 + alignment + gap + capped_workload + steer) x (measure_pct ^ MEASURE_EXPONENT) |
| BASE_TERM | The constant inside the bracket that keeps a unit with no signal above zero. | ORG | DEFERRED | scalar | Positive. | 1.0 |
| GAP_TERM_WEIGHT | Weight of each flat gap term. | ORG | DEFERRED | scalar | Positive. | 0.50 |
| GAP_TERM_CAP | Cap on the summed gap terms. | ORG | DEFERRED | scalar | Must equal or exceed the reachable maximum of the flat terms plus the graduated bucket. A cap below the reachable maximum silently clips the highest-signal units. | 2.50 |
| GAP_TERM_DEFINITIONS | The flat gap terms with their named sources, PER POPULATION SHAPE. | ORG | DEFERRED | taxonomy | Keyed by shape. Each term has key, shape, source concept, test, and weight. The set is closed per shape; adding a term requires raising the cap to match. | FIXED: coverage absent; presence absent; benchmark shortfall; commitment missing. FLOW: overdue and open; stalled in stage; no next action; slipped more than once |
| GRADUATED_BUCKET | The banded opportunity marker and its weights. | ORG | OPTIONAL | taxonomy | Bands on two axes. Largest weight not greater than GAP_TERM_WEIGHT. | high opportunity low performance 0.50; high and high 0.25; low and high 0.15; low and low 0.00 |
| STEER_TILT_TARGET_WEIGHT | Weight assigned to the named entity under a lean. Must sit ABOVE the standing top, or the lean is a no-op labelled as an action. | ORG | DEFERRED | scalar | Strictly greater than the maximum standing_weight in CREDITABLE_ENTITIES. | 1.25 |
| STEER_TILT_OTHERS_FACTOR | Factor applied to every other entity's weight under a lean. | ORG | DEFERRED | scalar | Between 0 and 1. | 0.60 |
| INITIATIVE_STEER_TERM | The additive term a named initiative steer contributes. | ORG | DEFERRED | scalar | Positive. The only additive steer; an entity-level steer never enters as a term. | 0.50 |
| COVERAGE_DUPLICATION_FACTOR | Factor applied when another named party is already engaging the unit on its only open work. | ORG | DEFERRED | scalar | Between 0 and 1. | 0.50 |
| COVERAGE_DUPLICATION_APPLIES_TO | Which report line the duplication discount applies to. | ORG | DEFERRED | scalar | Must be the junior line only. It is misleading to the person who assigned the other party. | line_a |
| SECOND_ACTOR_RESOLUTION_LADDER | Ordered sources for the other party's unit set. | ORG | DEFERRED | list | Ordered. A derivable identifier only where the scheme supports one; then an explicit assignment list; then a per-unit flag naming the other actor. | derived code; assignment list; per-unit flag |
| SECOND_ACTOR_UNIT_SUFFIX | The construction that derives the other party's unit code from the parent unit code, where the scheme supports it. | ORG | OPTIONAL | scalar | Tested by equality against one derived code, never by a suffix search across the file. | parent code followed by 41 |
| TIE_BREAK_KEYS | The mandatory deterministic tie-break, in order. | ORG | DEFERRED | list | Must end with the unit identifier ascending. The measure key is whichever column supplied the run's percentile. | score desc; measure desc; unit id asc |
| ZERO_MEASURE_SORT_KEY | Whether units with no measure are forced last by a sort key rather than by a score adjustment. | ORG | DEFERRED | scalar | Must be sort_key. Never zero the score, never add a penalty term, always publish the real score. | sort_key |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 17: Scoring constants

| Variable | Documented default | Degradation notice |
|---|---|---|
| SCORE_FORMULA_SHAPE | The standing multiplicative shape: a bracket of base plus alignment plus gap plus capped workload plus steer, multiplied by the measure percentile raised to the exponent. | The standing scoring shape was used and is printed in full in the method section with a worked example. |
| BASE_TERM | 1.0. | The standing base term was used, which is what keeps a unit with no other signal above zero. |
| GAP_TERM_WEIGHT | 0.50. | The standing gap weight was used. |
| GAP_TERM_CAP | 2.50. | The standing cap was used, and it is set at the reachable maximum so no high-signal unit is clipped. |
| GAP_TERM_DEFINITIONS | SHAPE DEPENDENT, and **EVERY TERM NAMES ITS SOURCE CONCEPT AND ITS TEST, because a term that names neither is a word rather than a wiring and two implementers will score it differently.** Under FIXED, four terms: COVERAGE ABSENT, source concept_presence_ours, test the presence flag is false or blank for a category the unit is eligible for, and it is NOT sourced from the last-engagement date under any circumstances, per the note below; PRESENCE ABSENT, source concept_presence_ours, test no presence recorded at all across every category; BENCHMARK SHORTFALL, source concept_benchmark_satisfaction, test the value is below the bound benchmark; COMMITMENT MISSING, source concept_commitment, test no commitment recorded where the unit type requires one. Under FLOW, four terms: OVERDUE AND OPEN, source concept_exit_date with the stage, test the exit date has passed and the stage is not terminal; STALLED IN STAGE, source concept_stage with concept_entry_date, test the dwell exceeds the local median dwell for that stage; NO NEXT ACTION, source concept_next_action, test the field is blank; SLIPPED MORE THAN ONCE, source concept_exit_date history, test the exit date moved more than once. Any term whose source concept does not resolve is NOT SCORED and is named. **THE COVERAGE-ABSENT SOURCING RULE, AND IT IS A PROHIBITION:** coverage absent is NEVER sourced from the last-engagement or recency date. That field feeds the exception section's coverage-stale flag, and scoring a gap term from it as well would count one signal twice, which SD-WGT-19 forbids. Where concept_presence_ours does not resolve, coverage absent is NOT EVALUATED and says so; it does not fall back to recency. | The gap terms have not been defined for your organization, so the generic set for this population's shape was used, with the standing source concept and test for each, and the shape is named beside the score. Each term that could not be evaluated is named as not evaluated rather than scored at zero, with the concept that failed to resolve. Coverage absent was not scored from any recency field, because that field already feeds the staleness flag and one signal must not be counted twice. |
| STEER_TILT_TARGET_WEIGHT | 1.25, which sits above the standing top weight. | The standing lean weight was used, and the resulting weight matrix is printed so the consequence is visible. |
| STEER_TILT_OTHERS_FACTOR | 0.60. | The standing lean factor was used. |
| INITIATIVE_STEER_TERM | 0.50. | The standing initiative steer term was used. |
| COVERAGE_DUPLICATION_FACTOR | 0.50. | The standing duplication factor was used where another named party is already working a unit's only open work. |
| COVERAGE_DUPLICATION_APPLIES_TO | The junior line only. | The duplication discount applies only to the person choosing where to spend a day, never to the person who deployed the other party, which is the only permitted setting. |
| SECOND_ACTOR_RESOLUTION_LADDER | Derived code, then explicit assignment list, then a per-unit flag naming the other actor. | The standing ladder was used. Where no second actor resolved, no discount was applied and that is recorded as a normal result, not a failure. |
| TIE_BREAK_KEYS | Score descending, measure descending, unit identifier ascending. | The standing tie-break was used, which is what makes two runs on the same file return the same list. |
| ZERO_MEASURE_SORT_KEY | sort_key. | Units with no measure are forced last by a sort key rather than by a score penalty, which is the only permitted setting, and their real score is published. |
