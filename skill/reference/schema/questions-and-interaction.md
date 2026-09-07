# GROUP 21: QUESTIONS AND INTERACTION

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| QUESTION_BANK | The question set with id, trigger, weight, blocking flag and stage. | ORG | DEFERRED | taxonomy | Row order is load bearing and is the tie-break when weights are equal. Every blocking question names what happens when it is unanswered. | limits; scope; data; objectives; period; targets; wins; preview |
| QUESTION_BATCH_MAX | Maximum questions presented at one time. | ORG | DEFERRED | scalar | Integer 2 to 6. A wall of questions is abandonment. | 4 |
| NON_BLOCKING_BUDGET_FORMULA | How many non-blocking questions may join a round. | ORG | DEFERRED | scalar | max(0, QUESTION_BATCH_MAX minus blocking count). | max(0, 4 - B) |
| COMPOSITE_QUESTION_IDS | Questions presented as one grid covering many items, counting as one toward the batch. | ORG | DEFERRED | list | Every entry is a question id. | status; targets; behaviours; actions |
| FORM_REQUIRED_EXEMPT_QUESTIONS | Questions exempt from the non-blocking budget because they are the sole input to a required form section. | ORG | DEFERRED | list | Every entry names the section it feeds. | challenges; development |
| ANOMALY_QUESTION_CAP | Maximum anomaly questions per run. | ORG | DEFERRED | scalar | Small integer. | 3 |
| HEADLINE_CANDIDATE_THRESHOLD | Above this many headline candidates, ask the user which one leads. | ORG | DEFERRED | scalar | Small integer. | 3 |
| MISS_SUGGESTION_COUNT | How many nearest values are offered when a qualifier matches no value. | ORG | DEFERRED | scalar | Integer 5 to 20. Ranked by ascending normalized edit distance with alphabetical tie-break, so the same miss always returns the same list. | 10 |
| EVIDENCE_SUFFICIENCY_FLOOR | Below this many evidence items, the crawl widens. | ORG | DEFERRED | scalar | Small integer. | 3 |
| SYNTHESIS_MIN_EVIDENCE | Minimum evidence items in a cluster before it becomes a candidate objective. | ORG | DEFERRED | scalar | Integer at least 2. | 2 |
| SYNTHESIS_MAX_OBJECTIVES | Cap on reconstructed objectives; weaker clusters merge into the nearest neighbour rather than adding one more. | ORG | DEFERRED | scalar | Integer 3 to 8. | 5 |
| RUN_ESTIMATE_BANDS | Duration estimates announced before a long run, by evidence state. | ORG | DEFERRED | mapping | Each band is a range in minutes. | fragment 4 to 6; reports 8 to 12; full 12 to 20 |
| ASK_LANGUAGE_RULE | Whether questions offer distinct values labelled with something a person recognizes plus a count. | ORG | DEFERRED | scalar | Boolean. Must be true. A code alone is not an acceptable option label. | true |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 21: Questions and interaction

| Variable | Documented default | Degradation notice |
|---|---|---|
| QUESTION_BANK | The standing bank in reference/binding-interview.md Stage 2, in its stated row order. | The question bank has not been tailored, so the standing bank was used and its row order decided which questions were asked first. |
| QUESTION_BATCH_MAX | 4. | The standing batch ceiling was used; you were never shown more than four questions at once. |
| NON_BLOCKING_BUDGET_FORMULA | Four minus the number of blocking questions in the round, floored at zero. | The standing budget formula was used. |
| COMPOSITE_QUESTION_IDS | The standing composite set. | The standing set was used, so a grid covering many items counted as one question. |
| FORM_REQUIRED_EXEMPT_QUESTIONS | Empty. | No question is exempt from the batch budget, so a question that is the sole input to a required section may be deferred to a later batch rather than always firing. |
| ANOMALY_QUESTION_CAP | 3. | The standing cap on anomaly questions was used. |
| HEADLINE_CANDIDATE_THRESHOLD | 3. | The standing threshold was used before asking which finding should lead. |
| MISS_SUGGESTION_COUNT | 10. | The standing count of nearest values was offered when a term matched no value, ordered so the same miss always returns the same list. |
| EVIDENCE_SUFFICIENCY_FLOOR | 3. | The standing floor was used before widening the evidence crawl. |
| SYNTHESIS_MIN_EVIDENCE | 2. | The standing minimum was used before a cluster became a candidate objective. |
| SYNTHESIS_MAX_OBJECTIVES | 5. | The standing cap was used, with weaker clusters merged into the nearest neighbour rather than adding one more. |
| RUN_ESTIMATE_BANDS | Four to six minutes with fragmentary evidence, eight to twelve with reports, twelve to twenty with full evidence. | The standing duration estimates were used, so the figure you were quoted at the start is generic rather than measured on your data. |
| ASK_LANGUAGE_RULE | true. | Questions offered you the values actually present, each labelled with something recognizable and a count, which is the standing setting. |
