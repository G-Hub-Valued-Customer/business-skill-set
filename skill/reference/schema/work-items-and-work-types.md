# GROUP 10: WORK ITEMS AND WORK TYPES

TAXONOMY SHAPE, WORK_TYPES. A closed graduated scale ordered by how much the
state of the world changes because the person showed up. Each entry carries:
- `key`, `display_name`, `weight`.
- `trigger_verbs`: tier-1 words that set this type outright.
- `trigger_nouns`: nouns used when a work item name carries no verb.
- `is_marker`: true for the bottom rung, which labels a unit's standing and asks
  for nothing.

There is exactly one type per work item, no seventh type, and no "other".
Scan the whole name for every verb and take the HIGHEST type present.

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| WORK_TYPES | The closed graduated work-type scale. | ORG | DEFERRED | taxonomy | Between 3 and 8 entries. Weights strictly decreasing. Exactly one is_marker true, and its weight is 0. | change_a_decision 1.25; change_a_state 1.00; change_knowledge 0.75; confirm_state 0.50; produce_record 0.25; label_only 0.00 |
| GENERIC_COMPLETION_VERBS | Semantically empty verbs that promote a low type one step and never promote a type already at or above the baseline. | ORG | DEFERRED | list | Lowercased. SEED. | execute; complete; handle; process; action |
| WORK_TYPE_BASELINE_KEY | The type a recognized but unclassifiable work item takes. | ORG | DEFERRED | scalar | Must be a key in WORK_TYPES and must not be the marker. | change_a_state |
| WORK_TYPE_CLASSIFY_BY | Whether classification reads the verb or the subject. | ORG | DEFERRED | scalar | Must be verb. Classifying by subject is the named expensive error. | verb |
| EXTERNAL_WORK_TYPE_IS_EVIDENCE_ONLY | Whether a published external type may override the local verb ladder. | ORG | DEFERRED | scalar | Boolean. Must be false: external type breaks a genuine tie and never overrides. | false |
| REFERENCE_CLASSIFICATION_FIXTURE | A frozen ground-truth classification over one real dataset, used as a gate on the classifier. | ORG | OPTIONAL | taxonomy | Each row: work item name, assigned type, dataset id. Empty at first bind; populated from the first real dataset. | 61 work item names typed and frozen |
| REFERENCE_FIXTURE_MATCH_REQUIRED | Whether reproducing the fixture exactly is a failing gate. | ORG | CONDITIONAL | scalar | Boolean. Required when the fixture is populated. Anything under a perfect match is a failing gate. | true |
| WORKLOAD_COUNT_CAP | The maximum number of closing work items that count toward the workload term. | ORG | DEFERRED | scalar | Positive integer. The COUNT is capped first, then multiplied. | 5 |
| WORKLOAD_MULTIPLIER | Multiplier applied to the capped workload count. | ORG | DEFERRED | scalar | Positive number. | 1.2 |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 10: Work items and work types

| Variable | Documented default | Degradation notice |
|---|---|---|
| WORK_TYPES | The six-rung generic ladder with its standing weights: change a decision, change a state, change knowledge, confirm a state, produce a record, label only. | No local work-type vocabulary has been bound, so work items were typed with the generic ladder. Every item whose type could not be recognized is named in the audit at the baseline weight rather than discounted. |
| GENERIC_COMPLETION_VERBS | execute, complete, handle, process, action, perform. | No local generic verbs are bound, so the standing list was used. A local completion verb not on the list will be read as a specific verb and may type an item one rung too high. |
| WORK_TYPE_BASELINE_KEY | change_a_state, the second rung. | The baseline type for an unrecognized work item was not set, so the standing baseline was used and every item that took it is named. |
| WORK_TYPE_CLASSIFY_BY | verb. | Classification is by verb, never by subject, which is the only permitted setting. |
| EXTERNAL_WORK_TYPE_IS_EVIDENCE_ONLY | false, meaning an external type never overrides the local ladder. | An externally published work type breaks ties only and never overrides, which is the standing setting. |
| WORKLOAD_COUNT_CAP | 5. | The standing cap on how many closing items count toward workload was used. |
| WORKLOAD_MULTIPLIER | 1.2. | The standing workload multiplier was used. |

---

## CONDITIONAL DEFAULTS AND NOTICES ONCE TRIGGERED, FOR THIS GROUP

Moved here from APPENDIX A2 for the same reason. The text is unchanged.

### Group 10: Work items and work types

| Variable | Trigger | Documented default | Degradation notice |
|---|---|---|---|
| REFERENCE_FIXTURE_MATCH_REQUIRED | REFERENCE_CLASSIFICATION_FIXTURE is populated | true. Anything under a perfect match is a failing gate. | Whether the frozen classification must be reproduced exactly was not set, so it was treated as a failing gate, which is the strict reading. The match rate is reported. |
