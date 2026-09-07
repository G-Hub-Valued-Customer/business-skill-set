# GROUP 8: MEASURES AND UNITS

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| MEASURE_TIERS | The ordered ladder of ranking measures, best first, each with its concept stems. | ORG | DEFERRED | taxonomy | At least 1 tier. Each tier has key, display_name, stems, and a value_check. The first tier that resolves AND is populated wins. | tier1 incurred_loss; tier2 paid_loss; tier3 claim_count |
| MEASURE_UNIT_TOKENS | What is being counted, as it appears in headers. | ORG | DEFERRED | list | Lowercased stems. SEED. | dollars; claims; hours; units; files |
| MEASURE_RATE_TOKENS | Time-base suffixes that mean the value is expressed per period. | ORG | DEFERRED | list | Each entry names a period. Interchangeable within the list; the found suffix is always recorded. | per week; per day; pw; pd |
| MEASURE_LOOKBACK_TOKENS | Lookback-length markers stripped before comparing and recorded after. | ORG | DEFERRED | list | SEED. | ytd; mtd; qtd; l13w; l26w; l52w; rolling12 |
| MEASURE_EXPONENT | The exponent applied to the measure percentile in the composite score. | ORG | DEFERRED | scalar | Positive number. 1.0 makes the measure linear; above 1 makes it a tie-shaper. | 1.5 |
| ZERO_MEASURE_TREATMENT | How a blank, null, non-numeric, zero or negative measure is handled. | ORG | DEFERRED | scalar | Must be include_as_zero. Excluding is forbidden. | include_as_zero |
| PERCENTILE_DEFINITION | How the measure percentile is computed. | ORG | DEFERRED | scalar | Must be average_rank_over_n. Never over a subset, never over a sample. | average_rank_over_n |
| MIN_POPULATION_FOR_NORM | Below this count, a median is printed with its count beside it and no comparison is drawn. | ORG | DEFERRED | scalar | Integer at least 3. **PAIRED WITH ANONYMITY_FLOOR: an outward walk for a peer set stops at the first level meeting BOTH floors, so raising this one raises where every walk stops. Whoever changes one checks the other, and the pair is stated in full at ANONYMITY_FLOOR.** | 5 |
| MIN_POPULATION_FOR_RANKING | The population below which ranking, percentile, median, distribution and peer language are meaningless and are not emitted at all. | ORG | DEFERRED | scalar | Integer at least 3, and at least MIN_POPULATION_FOR_NORM. Tested against the population the reader's own scope contains, not against the file. See SD-POP-25. | 5 |
| JOIN_UNIQUENESS_FLOOR | Minimum share of rows whose join key is unique, in each file, before a column may serve as a join key. | ORG | DEFERRED | scalar | Fraction between 0.9 and 1. | 0.98 |
| JOIN_OVERLAP_FLOOR | Minimum share of the smaller file's rows that must match before two files are treated as covering the same population. | ORG | CONDITIONAL | scalar | Fraction between 0 and 1. Applied ONLY where the population's mode is FIXED. Under FLOW it is never applied: like-for-like is a cohort-definition test, not a roster-overlap test, and a healthy pipeline fails any reasonable overlap floor. Set it low even under FIXED, because a real roster churns. | 0.50 |
| UNRESOLVED_STOP_COUNT | Reconciliation items still unresolved after re-derivation, at which a run stops rather than publishing. | ORG | DEFERRED | scalar | Integer at least 2. | 3 |
| UNIT_DRIFT_CANDIDATE_FACTORS | Conversion factors the drift test may declare. | ORG | DEFERRED | list | Positive numbers greater than 1. | 2; 5; 10; 20; 100; 1000 |
| UNIT_DRIFT_AUTONORM_FACTORS | Which of those may be applied silently. | ORG | DEFERRED | list | A subset of the candidates. Small factors must be excluded, because a genuine doubling looks like a factor of 2. | 10; 20; 100; 1000 |
| UNIT_DRIFT_MIN_PAIRS | Minimum matched pairs before a drift factor may be declared. | ORG | DEFERRED | scalar | Integer at least 20. | 30 |
| UNIT_DRIFT_TOLERANCE | How close the median oriented ratio must sit to a candidate factor. | ORG | DEFERRED | scalar | Fraction between 0 and 0.10. | 0.03 |
| UNIT_DRIFT_CONCENTRATION | Share of oriented ratios that must fall within the concentration band. | ORG | DEFERRED | scalar | Fraction between 0.5 and 1. | 0.60 |
| UNIT_DRIFT_BAND | Half-width of the concentration band around the candidate factor. | ORG | DEFERRED | scalar | Fraction. Must be loose enough for naturally dispersed unit-level metrics. | 0.25 |
| RATE_DENOMINATOR_MUST_MATCH | Whether a comparison across differing rate denominators is blocked with no override. | ORG | DEFERRED | scalar | Boolean. Must be true. | true |
| LOOKBACK_MAY_DIFFER | Whether a differing lookback is permitted as a recorded run-rate comparison. | ORG | DEFERRED | scalar | Boolean. Should be true; blocking on lookback rejects almost every real pair of files. | true |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 8: Measures and units

| Variable | Documented default | Degradation notice |
|---|---|---|
| MEASURE_TIERS | The seed measure stems in the shared dictionary, tried in order, first tier that resolves and is populated. | No ranking measure has been declared, so one was resolved from the file. The column used, its unit and its time basis are named in the audit; confirm it is the measure you rank on. |
| MEASURE_UNIT_TOKENS | The seed unit tokens. | No local unit vocabulary is bound, so unit comparison rests on the generic tokens. A comparison across two differing units may be blocked when it should not be, and is reported when it is. |
| MEASURE_RATE_TOKENS | The seed rate tokens. | No local rate vocabulary is bound. A per-period value whose marker is not recognized is treated as a period total, and any comparison against it is blocked and reported rather than computed. |
| MEASURE_LOOKBACK_TOKENS | The seed lookback tokens. | No local lookback vocabulary is bound, so a differing history length may not be detected. Where it was detected, the comparison is labelled as a run-rate comparison. |
| MEASURE_EXPONENT | 1.5. | The measure exponent has not been set, so the standing value was used. The measure acts as a tie-shaper rather than the dominant term; the formula is printed in the method section. |
| ZERO_MEASURE_TREATMENT | include_as_zero. | Units with no measure are included at zero and rank last, which is the only permitted treatment. |
| PERCENTILE_DEFINITION | average_rank_over_n. The largest unit therefore sits at exactly 1.0 and the smallest at 1 over N. Neither is rounded, capped or suppressed; at the exact endpoints the reader-facing sentence says the plain thing instead, per SD-LNG-12: the largest in this list, or the smallest in this list, naming any tie, with the figure printed beside it. | The standing percentile definition was used, with tied values receiving an identical percentile. Where a unit sits at the very top or bottom of the list, the narrative says so in those words and prints the figure alongside, because a top row described as the hundredth percentile is arithmetically right and reads as an error. |
| MIN_POPULATION_FOR_NORM | 5, equal to ANONYMITY_FLOOR by construction, so an outward walk that stops at the first level meeting the anonymity floor has also met this one. | No minimum population for a benchmark has been set, so a median over fewer than five units is printed with its count beside it and no comparison is drawn from it. The same figure is the anonymity floor, so a peer set this report will name a position in is a peer set it will also compare against. |
| MIN_POPULATION_FOR_RANKING | 5, and never below MIN_POPULATION_FOR_NORM. | No minimum rankable population has been set, so a standing one was used. Where your scope held fewer than that, this report says so before the content, delivers the rows, names every comparison it did not attempt, and names the level that would produce a rankable population for you. |
| JOIN_UNIQUENESS_FLOOR | 0.98. | No join-key uniqueness floor has been set, so a standing one was used. The column chosen as the join key, and its uniqueness in each file, are named in the audit. |
| UNRESOLVED_STOP_COUNT | 3. | No stop count for unresolved reconciliation items has been set, so a standing one was used. Any item left unresolved is excluded from every claim and named. |
| UNIT_DRIFT_CANDIDATE_FACTORS | 2, 5, 10, 20, 100, 1000. | The standing conversion factors were used when checking whether two files are in the same units. |
| UNIT_DRIFT_AUTONORM_FACTORS | 10, 20, 100, 1000. | Only large factors are corrected silently. A detected factor of two or five is never corrected automatically, because a genuine doubling looks the same, and you are asked instead. |
| UNIT_DRIFT_MIN_PAIRS | 30. | The standing minimum sample for a unit-drift finding was used. |
| UNIT_DRIFT_TOLERANCE | 0.03. | The standing tolerance was used. |
| UNIT_DRIFT_CONCENTRATION | 0.60. | The standing concentration requirement was used. |
| UNIT_DRIFT_BAND | 0.25. | The standing concentration band was used, which is deliberately loose because unit-level metrics are naturally dispersed. |
| RATE_DENOMINATOR_MUST_MATCH | true. | A comparison across differing time bases is blocked with no override, which is the only permitted setting. |
| LOOKBACK_MAY_DIFFER | true. | A differing history length is permitted and recorded as a run-rate comparison, which is the standing setting. |

---

## CONDITIONAL DEFAULTS AND NOTICES ONCE TRIGGERED, FOR THIS GROUP

Moved here from APPENDIX A2 for the same reason. The text is unchanged.

### Group 8: Measures and units

| Variable | Trigger | Documented default | Degradation notice |
|---|---|---|---|
| JOIN_OVERLAP_FLOOR | two files are compared AND the population's mode is FIXED | 0.50 of the smaller file. Never applied under FLOW. | No overlap floor has been set, so a standing one was used, and it was applied only because this population is a fixed roster. Under a flowing population no overlap floor is applied at all, because a healthy pipeline replaces most of its rows every period and an overlap test would declare every real comparison invalid. |
