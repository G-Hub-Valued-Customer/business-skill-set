# GROUP 22: RUN CONTROL AND RELIABILITY

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| HARD_GATES | The closed, enumerated conditions that stop a run, in four keyed groups. | ORG | DEFERRED | taxonomy | FOUR keyed groups and no others: shared, planning, review, scorecard. A gate in the shared group is inherited by all three skills and is declared once. EVERY gate record carries exactly six fields: `key`, a stable id; `group`, one of the four; `fires_at`, the stage or step it fires at; `behaviour`, exactly one of `stop_outright` or `ask_one_question_then_stop` and no third value; `reads`, the name of a schema variable this gate tests against or the literal `none`; `doctrine`, the doctrine id that authorizes it. Every name in a `reads` field must exist in this schema. The count per group is stated in this taxonomy and NOWHERE else in the bundle. Fatigue, run length, retry count and output size are never members. A condition that changes the OUTPUT rather than ending the run is not a gate. THIS SCHEMA STATES NO MEMBERSHIP AND NO COUNT: it states the record shape, the four group names and the two behaviour values, and nothing else. Membership is declared by the skills. | one record: key source_unreadable, group shared, fires_at probe step 1 and again at acquire, behaviour ask_one_question_then_stop, reads SOURCE_WORKBOOK_LOCATIONS, doctrine SD-PRS-25 |
| RETRY_BACKOFF_SCHEDULE | Waits between transient retries. | ORG | DEFERRED | list | Increasing, then a repeating final value. Transient failures have no attempt limit. | 30s; 60s; 120s; then 120s |
| SCOPED_RETRY_LIMIT | Failures on one scoped unit before the unit is split. | ORG | DEFERRED | scalar | Integer at least 2. | 3 |
| REPAIR_CYCLE_LIMIT | Repair cycles per logical invariant before escalation. | ORG | DEFERRED | scalar | Integer at least 2. | 3 |
| GLOBAL_REMEDIATION_BUDGET | Total gate-fix cycles across all gates in one run. | ORG | DEFERRED | scalar | Integer 4 to 20. Without a global cap, two gates can alternate longer than any user will wait. | 8 |
| PER_GATE_FAILURE_LIMIT | Failed returns on one gate before the run emits a bannered partial. | ORG | DEFERRED | scalar | Integer 2 to 5. | 3 |
| WRITE_CHUNK_SIZE | Rows per write call. | ORG | DEFERRED | scalar | Integer 10 to 200. | 50 |
| WRITE_VERIFY_TAIL_ROWS | How many rows at the END of a chunk are read back to confirm it landed. | ORG | DEFERRED | scalar | Integer at least 2. Reading the head proves nothing, because a partial write fills the head. | 3 |
| WRITE_CONFIRM_WAIT_SECONDS | How long to wait before treating an empty read as anything but unconfirmed. | ORG | DEFERRED | scalar | At least 20. | 30 |
| PARTITION_SIZE | Records per partition when a stage fans out. | ORG | DEFERRED | scalar | Positive integer. | 25000 |
| MAX_CONCURRENT_WORKERS | Concurrency cap inside a stage. | ORG | DEFERRED | scalar | Integer 1 to 16. | 8 |
| SCALE_TIER_BOUNDARIES | Record counts separating the read and write mechanics tiers. | ORG | DEFERRED | list | Increasing. The method, the sections, the caps and every gate are identical in all tiers. | 5000; 50000; 250000 |
| CHECKPOINT_PATH_PATTERN | Path pattern for stage checkpoints. | ORG | DEFERRED | scalar | Under SCRATCH_DIR. Never under OUTPUT_DIR. | SCRATCH_DIR/ckpt_{stage}.json |
| PARTITION_CHECKPOINT_PATH_PATTERN | Path pattern for per-partition checkpoints. | ORG | DEFERRED | scalar | Under SCRATCH_DIR. | SCRATCH_DIR/ckpt_{stage}_p{index}.json |
| CHECKPOINT_DELETE_ON_PUBLISH | Whether the checkpoint is deleted when the real artifact publishes. | ORG | DEFERRED | scalar | Boolean. Not deleted on a partial emit. | true |
| REGRESSION_INVARIANTS | The invariants re-checked at every gate from the parse stage onward, against the CURRENT artifact. | ORG | DEFERRED | list | At least 6. Includes record count reconciliation, scope purity, exclusion persistence, ordering of the mandatory set before any class filter, absence of a measure floor, qualifier membership, and percentile stability. | eight named invariants |
| SPOT_CHECK_SAMPLE_SIZE | How many units are re-read from source and compared to the artifact before publication. | ORG | DEFERRED | scalar | Integer at least 3. | 3 |
| REGRESSION_CASES | Named end-to-end cases run before any change ships, each with inputs, expected and failure. | ORG | DEFERRED | taxonomy | At least 5 cases. Includes the environment-credit trap, the no-data user, the altitude ceiling, the unconfirmed action, the span-of-control error, the low-confidence inference, and the tied superlative. | seven cases |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 22: Run control and reliability

| Variable | Documented default | Degradation notice |
|---|---|---|
| HARD_GATES | The standing closed set is the four keyed groups DECLARED BY THE SKILLS, each record carrying key, group, fires_at, behaviour, reads and doctrine. This schema states the shape only; membership and counts live with the skills. Of the shared group, and only because a binding owner asking what would stop a run deserves a concrete answer, the shared core keys, reproduced from the PLANNING skill's own stop-list section, which is authoritative for them, are: source_unreadable, record_count_zero, scope_unresolvable, formatting_unverifiable, character_gate_unrunnable. Every other gate is a skill extension and is read from that skill, never from here. Reading the published standard is not a member, per SD-SRC-21, and a population below MIN_POPULATION_FOR_RANKING is not a member, per SD-POP-25: it changes what the output is and never ends the run. | The stop conditions have not been set for your organization, so each skill applied the standing set it declares, being the shared core gates plus that skill's own extension. Fatigue, run length, retry count and output size are not on any of them, and neither is an unreadable standard or a population too small to rank. |
| RETRY_BACKOFF_SCHEDULE | 30 seconds, 60, 120, then 120 thereafter. | The standing backoff was used for transient failures, which have no attempt limit. |
| SCOPED_RETRY_LIMIT | 3. | The standing limit was used before narrowing a failing unit. |
| REPAIR_CYCLE_LIMIT | 3. | The standing limit was used per logical invariant. |
| GLOBAL_REMEDIATION_BUDGET | 8. | The standing global budget was used, so two gates could not alternate indefinitely. |
| PER_GATE_FAILURE_LIMIT | 3. | The standing per-gate limit was used before emitting a bannered partial. |
| WRITE_CHUNK_SIZE | 50 rows. | The standing chunk size was used. |
| WRITE_VERIFY_TAIL_ROWS | 3. | The standing tail check was used; the end of each chunk was read back, never the head. |
| WRITE_CONFIRM_WAIT_SECONDS | 30. | The standing wait was used before treating an empty read as anything other than unconfirmed. |
| PARTITION_SIZE | 25000 records. | The standing partition size was used. |
| MAX_CONCURRENT_WORKERS | 8. | The standing concurrency cap was used. |
| SCALE_TIER_BOUNDARIES | 5000, 50000, 250000 records. | The standing tiers were used. The method, the sections, the caps and every gate are identical in all of them. |
| CHECKPOINT_PATH_PATTERN | A stage-named file under the scratch directory. | The standing checkpoint path was used, and no working file was written near your outputs. |
| PARTITION_CHECKPOINT_PATH_PATTERN | A stage-and-partition-named file under the scratch directory. | The standing partition checkpoint path was used. |
| CHECKPOINT_DELETE_ON_PUBLISH | true. | The checkpoint is deleted when the real artifact publishes and retained on a partial emit, which is the standing setting. |
| REGRESSION_INVARIANTS | The standing eight: record count reconciles, scope purity holds, the not-actionable exclusion holds, the class exclusion and its ordering hold, no measure floor was applied, qualifier membership holds, the directed set was resolved before any class filter, and sampled percentiles are stable. | The standing invariants were re-checked at every gate against the artifact itself, not against an earlier claim about it. |
| SPOT_CHECK_SAMPLE_SIZE | 3. | The standing sample was re-read from the source and compared to the artifact before publication. |
| REGRESSION_CASES | The standing seven named cases. | No organization-specific regression cases have been recorded, so the standing seven were used when validating changes to this configuration. |
