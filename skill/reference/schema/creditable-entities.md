# GROUP 7: CREDITABLE ENTITIES

TAXONOMY SHAPE, CREDITABLE_ENTITIES. An ordered list. Each entry carries:
- `key`, `display_name`.
- `rank`: standing position in the hierarchy, 1 best.
- `standing_weight`: the multiplier applied to the alignment term. **WHERE THE
  ORGANIZATION PUBLISHES AN ORDER OVER ENTITIES AND NO WEIGHTS, WHICH IS THE
  ORDINARY CASE, THE WEIGHT IS DERIVED FROM THE ORDER BY THE RAMP IN THIS
  SUB-FIELD'S SECTION A1 ROW, AND THAT ROW IS THE ONLY STATEMENT OF THE RAMP.**
  Without it a published ordering moves nothing: every entity sits at the same
  weight, the organization's clearest statement of what it wants grown is recorded
  and marked unused, and each skill is left to invent its own conversion.
- `aliases`: every spelling seen in source data, including known misspellings.
- `sentinel_aliases`: aliases containing punctuation or a common short word that
  must be protected by a sentinel token before normalization.
- `parent_key`: for a sub-entity that inherits its parent's benchmark.
- `own_measure_stems`: stems for the entity's OWN measure.
- `benchmark_measure_stems`: stems for the wider population measure that
  includes parties the writer is not accountable for.
- `signal_concept_keys`: commitment, election, breadth and presence concepts
  belonging to this entity.
- `claimable`: whether performance of this entity may be claimed as achievement.

There is NO default row. An entity that resolves to nothing in this taxonomy is
reported as unmapped and takes no standing weight. Where a default IS correct it
is tied to the hierarchy floor, never to a literal.

**WHICH COLUMN CARRIES THE ENTITY, AND WHAT THE WEIGHT IS WHEN NO COLUMN DOES.**
The taxonomy says what the entities are and what each one is worth. It does not
say which column of a source file tells a run WHICH entity a row belongs to, and
until this paragraph existed nothing did: `entity_weight` is a multiplicative
factor of the alignment term on every row of every ranked list, and the run had no
stated way to find the column it multiplies by. One run invented a procedure,
correctly, and said so; the next one would have invented a different one.

The column is resolved as the concept `concept_creditable_entity`, whose seed
stems, value check and forbidden neighbours live in reference/field-resolution.md, and whose
COVERAGE FALLBACK is stated there too: where the name passes resolve nothing, the
run measures each candidate column's distinct values against the keys and aliases
of CREDITABLE_ENTITIES and takes the column whose coverage is highest, provided it
clears ENTITY_COLUMN_MIN_COVERAGE and beats the runner-up by the stated margin.
The chosen column, its coverage and the runner-up are PRINTED, so a reader can see
what the ranking multiplied by.

**THE STATED NEUTRAL, WHICH IS NOT A GUESS AND IS NOT A ZERO.** Where no column
resolves and the fallback does not clear, `entity_weight` IS 1.0 ON EVERY ROW. It
is the identity multiplier: the alignment term reduces to its other factors, every
unit is treated alike on this axis, and NOTHING is ranked up or down by an entity
nobody could identify. A zero would delete the term and its neighbours with it; a
floor would rank every unit as if it carried the organization's least valued
entity, which is a judgment the run has no evidence for. The artifact says the
entity column did not resolve, names the candidates it measured with their
coverages, and states that no unit was weighted by entity this run.


| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| CREDITABLE_ENTITY_CLASS_NAME | The word this business uses for the class of thing credit attaches to. | ORG | DEFERRED | scalar | Non-empty. | line of business |
| CREDITABLE_ENTITIES | The ranked entity taxonomy. | ORG | DEFERRED | taxonomy | At least 1 entry. Ranks unique and contiguous from 1. Every standing_weight in the range 0 to 1. No default row. | Property; General Liability; Auto Physical Damage; Inland Marine |
| ENTITY_WEIGHT_FLOOR | The lowest standing weight in the taxonomy, referenced by name wherever a floor default is applied and used as the bottom of the rank-to-weight ramp. | ORG | DEFERRED | scalar | Must equal the minimum standing_weight present. **Where the taxonomy holds MORE THAN ONE entity it must be STRICTLY LESS THAN the highest standing_weight: a floor equal to the ceiling makes the ramp flat and turns the whole derivation into a silent no-op that looks like it ran.** Never written as a literal elsewhere. | 0.30 |
| NON_CLAIMABLE_ENTITIES | Entities and aggregates that contribute to a benchmark total but may never be claimed. | ORG | DEFERRED | list | Disjoint from CREDITABLE_ENTITIES keys. | total industry severity; carrier-wide aggregate; competitor filings |
| ENTITY_BENCHMARK_MAP | Map from creditable entity key to exactly one benchmark population key. | ORG | DEFERRED | mapping | Every key is a creditable entity. An entity absent from this map is UNBENCHMARKED and routes to execution claiming. | property to all_property_claims |
| BENCHMARK_POPULATIONS | The benchmark populations with their header aliases. | ORG | DEFERRED | taxonomy | Each entry has key, display_name, header_aliases including known misspellings. | all_property_claims; all_liability_claims |
| SENTINEL_TOKENS | Aliases that must be replaced by a sentinel before punctuation stripping, because the bare remainder is a common word. | ORG | DEFERRED | list | Every entry appears in some entity's aliases. May be empty only if no such alias exists. | e and s (never register bare "e" as an alias) |
| ENTITY_ALIAS_UNRECOGNIZED_ACTION | What to do with an alias that resolves to no entity. | ORG | DEFERRED | scalar | One of: flag_and_ask, flag_and_floor. Never guess_parent. | flag_and_ask |
| SPECIFIC_INITIATIVE_NAMES | Names distinctive enough to match a priority on a single token. | ORG | DEFERRED | list | Every entry at least 4 normalized characters and not an entity family name. SEED, grows each period from the priority document itself. | rapid resolution; photo estimate; salvage recovery push |
| FAMILY_NAMES | Names that never match a priority on their own and always need a second distinctive token. | ORG | DEFERRED | list | Generated from CREDITABLE_ENTITIES aliases rather than maintained separately. | property; liability; auto |
| ENTITY_COLUMN_MIN_COVERAGE | The share of CREDITABLE_ENTITIES keys that a candidate column's distinct values must cover before that column may be taken as the entity-bearing column by the coverage fallback. | ORG | DEFERRED | scalar | Fraction between 0 and 1, and strictly above 0.5, because a column matching half the entities is as likely to be a neighbouring category as the entity itself. A candidate that clears it wins only if it also beats the runner-up's coverage by at least a tenth; where two clear it and neither beats the other by that margin, NEITHER is taken, both are named, and the stated neutral applies. | 0.80 |
| MATCH_STOPWORDS | Tokens dropped before distinctive-token matching. | ORG | DEFERRED | list | Includes domain verbs, not only English stopwords. SEED. | the; and; for; with; review; complete; claim; claims |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 7: Creditable entities

| Variable | Documented default | Degradation notice |
|---|---|---|
| CREDITABLE_ENTITY_CLASS_NAME | The phrase "line of business". | The name for what credit attaches to has not been bound, so a generic phrase is used in headings. |
| CREDITABLE_ENTITIES | A single implicit entity covering everything, with weight 1.0. | No entity hierarchy has been bound, so nothing was weighted up or down by line of business. Ranking rests on the measure, the alignment to stated priorities, and open workload alone. |
| CREDITABLE_ENTITIES.standing_weight | **DERIVED FROM A PUBLISHED ORDER BY A LINEAR RAMP, AND THIS IS THE ONLY STATEMENT OF IT.** Where the organization publishes an ORDER over entities and no weights, and the order comes from a source that PRIORITY_SOURCES admits for the period being run, the weight of the entity at rank r of n is `1.0 - (r - 1) x (1.0 - ENTITY_WEIGHT_FLOOR) / (n - 1)`, so the first-ranked entity takes 1.0, the last takes ENTITY_WEIGHT_FLOOR, and the steps between are equal. Where n is 1 the single entity takes 1.0 and no ramp is computed. **THE FOUR CONDITIONS ON THE DERIVATION, ALL MANDATORY.** It is applied at MEDIUM confidence and never written to the ORG config by a run, per I7. The whole resulting weight matrix is PRINTED IN FULL beside the order it came from, the source that published it and that source's date, so a reader can see every number the ranking used. It is READ BACK for correction as an open request against this group, so an organization can replace a ramp with its own weights in one line. And where the published order covers only SOME of the entities in play, the ramp is computed over the ones it names and every entity it does not name is UNMAPPED and takes no standing weight, per the no-default-row rule: an unnamed entity is never quietly given the floor, because that would rank it against entities the organization actually ordered. **WHY A RAMP AND NOT A GUESS AT THE NUMBERS.** An order is real information the organization published on purpose. Discarding it flattens the alignment term to nothing; inventing eight specific weights fabricates a precision nobody stated. A ramp asserts exactly what the order asserts, which is the sequence and nothing else, and it is reproducible from the order by anybody who reads it. | Your entities were published in an order and not as weights, so a weight was derived from the order rather than invented: the first entity in your list carries the full weight, the last carries the floor, and the steps between are equal. The order, its source, its date and every derived weight are printed together. If the spacing is wrong, or if two of these should sit level, binding the weights once replaces the whole ramp and nothing else changes. |
| ENTITY_WEIGHT_FLOOR | SHAPE DEPENDENT ON THE ENTITY COUNT. Where the taxonomy is the single implicit entity, 1.0, which is that entity's own weight and is also the minimum present, so the validation holds exactly. **Where TWO OR MORE entities are in play, 0.60, which is STRICTLY BELOW the ceiling of 1.0 so the rank-to-weight ramp above actually ramps.** An earlier revision defaulted this to 1.0 in both cases; the floor then equalled the ceiling, every derived weight came out at 1.0, and a published ordering of eight entities moved nothing on the artifact while the method reported that it had been applied. | The lowest entity weight was not set for your organization, so the standing floor was used as the bottom of the derived weight range. It is deliberately below the top rather than equal to it, because a floor equal to the ceiling would give every one of your entities the same weight and quietly discard the order you published. |
| NON_CLAIMABLE_ENTITIES | Empty. | Nothing has been marked as never claimable, so this report cannot warn you when a figure describes a population whose composition you did not choose. Check any figure whose subject is a total rather than your own work. |
| ENTITY_BENCHMARK_MAP | Empty. Every entity is treated as unbenchmarked FOR RUNGS 1 AND 2 ONLY. Figures fall to the highest rung that COUNTERFACTUAL_AVAILABLE_RUNGS still supplies and whose own definition is bound, never past it to the floor. | No benchmark population has been mapped to any line of business, so no share-of-addressable and no matched-control comparison was computed. Every affected figure is printed against the rung named beside it, and the claim strength drops with the rung. A figure reaches the bare denominator ONLY where no other bound rung resolves. See S9 and SD-CTR-24. |
| BENCHMARK_POPULATIONS | Empty. | No benchmark populations have been bound, so no comparison against a wider population was computed. |
| SENTINEL_TOKENS | Empty. | No protected aliases have been bound. If one of your names is a common short word or carries punctuation, it may over-match; every matched value set and its row count is listed in the audit so an over-match is visible. |
| ENTITY_COLUMN_MIN_COVERAGE | 0.80, with a required margin of 0.10 over the runner-up. Where the fallback does not clear, `entity_weight` is 1.0 on every row, which is the identity multiplier and not a floor. | No coverage threshold was set for finding the column that says which line of business a row belongs to, so a standing one was used: a column qualifies when its own values cover at least eighty percent of your entities and cover them at least ten points better than the next candidate. The chosen column and its coverage are printed. Where nothing qualified, no unit was weighted up or down by entity at all and this report says so, rather than guessing which column carried it. |
| ENTITY_ALIAS_UNRECOGNIZED_ACTION | flag_and_ask. | Unrecognized names are flagged and asked about rather than guessed, which is the safe default. |
| SPECIFIC_INITIATIVE_NAMES | Empty. Every name requires two distinctive tokens to match a priority. | No initiative names have been bound, so a priority matches a work item only when they share two distinctive words. A one-word initiative name in a manager's message will not match, and is reported as an unmatched priority. |
| FAMILY_NAMES | Generated from CREDITABLE_ENTITIES aliases. | Derived rather than maintained separately. |
| MATCH_STOPWORDS | The generic set of English stopwords plus the generic completion verbs. | No organization-specific stopwords have been bound, so a domain word that is common in your headers may count as distinctive and produce a loose priority match. Every match shows its shared tokens in the audit. |
