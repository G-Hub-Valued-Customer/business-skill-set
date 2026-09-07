# GROUP EFF: EFFORT, STOPPING, AND FAILING CLOSED

### SD-EFF-01 There is no time limit, and run length is not a cost the method recognizes
- Rule: zero time pressure. "A run that takes twenty-five minutes and is right is
  a complete success. A run that returns in four minutes with an unverified
  number, a fabricated action, or a missing section is a failure no matter how
  fast it returned."
- Mechanism: four explicit prohibitions. Never shorten a list, skip a
  verification, drop a section or summarize because the work is taking a while.
  Never stop at a partial result and describe what you would have done. A very
  large input gets the same treatment as a small one. Work the retry paths.
- Quote: "Length of run is not a cost this skill recognizes."
- Source: P-D41; R-D11
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-02 The stop list is closed and enumerated
- Rule: only the gates named in HARD_GATES stop a run. Fatigue, run length, retry
  count and output size are explicitly excluded, and never will be on the list. A
  missing central source is explicitly NOT a stop.
- Mechanism: each gate names where it fires. Some stop before an artifact exists
  and ask the user one question; the rest stop outright.
- Prevents: an implementer inventing a stop condition.
- Discipline: the count of gates is stated in exactly one place. A document that
  says five in one section and ten in another has an internal inconsistency that
  will be resolved differently by every reader.
- Source: P-D42; R-D11
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-03 Fail closed: unknown is not pass
- Rule: a gate that cannot be evaluated has failed.
- Source: P-D43
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-04 A labelled partial is still a partial
- Rule: partial output is never delivered silently, and a partial that looks
  finished is never delivered at all. If a section cannot be repaired, stop and
  publish nothing, name the section and the exact ranks affected, and preserve
  the checkpoint. "Do not ship the artifact with the gap described in the front
  panel: a labelled partial is still a partial, and a user cannot tell it from a
  complete report."
- Quote: "An artifact that is 80 percent populated and silently published is
  worse than one that failed loudly."
- Source: P-D44
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-05 A bannered partial that names what is missing is better than nothing
- Rule: where a run has already spent the user's time and a blocking answer never
  arrived, emit the cycle-appropriate blocks with an explicit placeholder in every
  field whose blocking input is missing, banner the whole output as incomplete and
  not for submission, name what is outstanding and which question resolves each,
  exempt the placeholder fields from the gates that inspect content, and do NOT
  delete the checkpoint.
- Reconciliation with SD-EFF-04: the two are not in conflict. A silent partial
  that reads as finished is forbidden. A partial that is unmistakably bannered,
  enumerates its own gaps and cannot be mistaken for a finished document is the
  correct terminal state after a long run with an unanswered blocking question.
  The distinguishing test is whether a reader could submit it by accident.
- Source: R-D39; R-D30
- Applies: REVIEW, PLANNING, SCORECARD

### SD-EFF-06 Two meanings of "empty" that must never be confused
- Rule: a section with nothing to report is a normal, complete section carrying
  its explanatory row and it ships. A section that failed to build is incomplete
  and blocks publication.
- Source: P-D45
- Applies: PLANNING, SCORECARD

### SD-EFF-07 No stage may weaken an earlier stage's guarantee, and every gate RE-CHECKS the previous one
- Rule: the REGRESSION_INVARIANTS run at every gate from the parse stage onward,
  verified against the CURRENT artifact and never against an earlier
  checkpoint's claim about it.
- Mechanism: record count reconciles; scope purity holds; the not-actionable
  exclusion holds; the class exclusion holds and its ordering held; no measure
  floor was applied; qualifier membership holds; the mandatory set was resolved
  before the class filter; sampled percentiles are stable.
- Prevents: "Silent re-admission of excluded rows is the failure this check
  exists to catch, and it becomes more likely with every additional worker, which
  is exactly why it runs at every gate rather than once at the end."
- Source: P-D46
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-08 Any unresolved item propagates
- Rule: a column that did not resolve in the parse stage appears in the final
  audit section. "Nothing quietly disappears between stages."
- Source: P-D47
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-09 Retry is graduated, not counted
- Rule: classify the failure first, then respond. TRANSIENT waits with escalating
  backoff and has no attempt limit. SCOPED narrows the unit and retries, then
  rebuilds it, then degrades that unit only. LOGICAL repairs in place and
  re-verifies up to REPAIR_CYCLE_LIMIT cycles per invariant. HARD GATE stops.
- Mechanism: RETRY_BACKOFF_SCHEDULE, then split a write chunk progressively, then
  rebuild one section rather than the artifact.
- Prevents: "The old rule, two attempts then stop, treated a replication lag
  identically to a genuine defect and abandoned runs that would have succeeded on
  the third read."
- Source: P-D48; R-D13
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-10 An empty or failed read is UNCONFIRMED, never failed, until the ladder says otherwise
- Rule: two failure modes look identical, a call that returns success and lands
  nothing, and a service that lags its own write. Treat both as unconfirmed and
  work the ladder.
- Mechanism: wait WRITE_CONFIRM_WAIT_SECONDS and read again before concluding
  anything.
- Source: P-D56; R-D13
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-11 One constraint relaxed, and a doctrine rule is never a relaxable constraint
- Rule: a retry relaxes exactly one constraint, in this order of preference:
  widen a date window, lower a match threshold, drop an optional filter, fall
  back from exact to fuzzy matching. "Never relax a doctrine rule as a retry
  step."
- Source: R-D13
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-12 "No forward progress" is the termination condition, and it is measured relatively
- Rule: define forward progress per stage type, record the measure in the
  checkpoint on every attempt, and compare against the previous attempt's
  recorded measure, never against an absolute.
- Mechanism: reading or writing rows, the count is higher; resolving references,
  at least one item resolved or one candidate eliminated; computing, more records
  scored; assembling, more sections with rows AND formatting verified;
  validating, fewer FAILING checks.
- Prevents: "A fixed row threshold neither scales nor terminates: on a very large
  file a stage can dribble a handful of rows forever and never be declared stuck,
  while on a small scope the same threshold declares a healthy stage stuck
  immediately."
- Source: P-D49
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-13 Never let a worker's optimism advance the run
- Rule: the supervisor advances on evidence read from the artifact, never on a
  worker's report. Where the two disagree, the file wins. "Wrote 250 rows is a
  claim; a read showing 250 populated rows is evidence."
- Source: P-D50
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-14 A stage that cannot write its checkpoint has failed
- Rule: absence of the checkpoint file is a failure signal, not an ambiguity,
  regardless of what the worker says.
- Source: P-D51
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-15 A worker failure is isolated to its own partition
- Rule: retry that partition alone through the graduated ladder, leaving every
  other partition's verified output untouched. A stage fails only when a
  partition has exhausted the ladder AND one rebuild. "Never discard the work of
  eight healthy workers because the ninth stalled: that is how a long run on a
  large file turns into no run at all."
- Source: P-D52
- Applies: PLANNING, SCORECARD

### SD-EFF-16 Only genuinely independent stages run in parallel, and never across a gate
- Rule: a stage that consumes an earlier stage's checkpoint is not independent of
  it, however independent it looks.
- Mechanism: the named case where three stages were claimed independent and all
  three were not, at once: priorities need the resolved supervisor, the compliance
  check needs the parsed jurisdiction column, the scope ladder reads distinct
  values out of the parsed file, and the period resolution reads the file.
- Prevents: "priorities gathered against an unresolved supervisor, an unknown
  target period and an unparsed jurisdiction column: a central-only, unvalidated
  priority set that silently dropped both the restricted exclusions and the
  directed matches."
- Quote: "Do not parallelize across a gate to save time. The gate is the only
  thing standing between a small error and a confidently wrong artifact."
- Source: P-D53
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-17 Partition deterministically, and verify the MERGE rather than the workers
- Rule: split into contiguous blocks of PARTITION_SIZE by identifier ascending,
  cap concurrency at MAX_CONCURRENT_WORKERS, one checkpoint per worker, and have
  the supervisor confirm every partition index is present with no gaps, that the
  row counts sum to the expected total, and that no identifier appears in two
  partitions.
- Prevents: "A missing partition is the failure mode that looks most like
  success: the run completes, the counts are internally consistent within each
  worker, and a whole block of units simply are not there."
- Source: P-D54
- Applies: PLANNING, SCORECARD

### SD-EFF-18 Nothing that needs the whole population may be computed inside a partition
- Rule: percentiles, medians and peer norms are global. Workers return raw
  values; the supervisor computes the distribution once over the merged set.
- Mechanism: "A percentile computed per partition is a different number wearing
  the same name, and it is the single most likely way a large run silently
  diverges from a small one."
- Source: P-D55
- Applies: PLANNING, SCORECARD

### SD-EFF-19 Read back the TAIL of a chunk, never the head
- Rule: verify the last WRITE_VERIFY_TAIL_ROWS rows of each chunk. "A partial
  write fills the head and drops the tail, so reading the top proves nothing."
- Source: P-D57
- Applies: PLANNING, SCORECARD

### SD-EFF-20 Never mix data writes with structural operations in one call
- Rule: one kind of operation per call. "A table applied in the same call as a
  failed write left a sheet permanently unwritable: every later write to it
  returned ok and landed nothing."
- Source: P-D58
- Applies: PLANNING, SCORECARD

### SD-EFF-21 Data first, structure second, PER unit, never one structural call for the whole artifact
- Rule: write and verify every row of one section, apply that section's structure
  in its own call or calls, verify those landed, and only then start the next
  section. "One structural call spanning every section is exactly the shape this
  rule warns against, and it is how a single dropped call un-styles half an
  artifact."
- Source: P-D59
- Applies: PLANNING, SCORECARD

### SD-EFF-22 Build order is by ACTUAL size, largest first
- Rule: count the rows each section will hold, build in descending order of that
  count, then the summary panels, with the front page last. Do not hard-code the
  resulting sequence; sort by the real count every run.
- Mechanism: "Building smallest first spends the run's budget on the small
  sections and reaches the largest with nothing left, which is precisely how an
  artifact ships with styled action sections and a bare reference section. The
  biggest section is built while the run is freshest."
- Source: P-D60; R-D12
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-23 Finish each unit completely before starting the next
- Rule: one section fully drafted, verified and checkpointed, then the next.
  Never draft everything shallowly and return to deepen it.
- Prevents: a document that ships with three polished parts and a bare fourth.
- Source: R-D12
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-24 Last in the order never means finished with less care
- Rule: the summary panels are built last for a stated reason, that the front
  page must name what was actually built, but they carry the same completion
  rule: each styled and verified before the next begins, each recording its own
  format pass. "Being last in the order never means being finished with less
  care."
- Prevents: the pages a manager opens first being the only ones with no gate
  behind them.
- Source: P-D61
- Applies: PLANNING, SCORECARD

### SD-EFF-25 A unit is not complete until its data AND its formatting are verified
- Rule: record per-section completion as rows written plus a format pass flag. A
  section whose format pass is false is as incomplete as one missing rows, and
  the run does not advance past it. Never defer formatting to a trailing pass.
- Source: P-D62
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-26 The only permitted deletion is strictly bounded
- Rule: recreating one damaged, unpublished section inside the in-progress
  scratch artifact. Never delete a published file, a user's source data, or a
  section holding verified rows, and never recreate a section to start clean when
  the real problem is a failed chunk.
- Mechanism: confirm the unwritable state is real first: wait
  WRITE_CONFIRM_WAIT_SECONDS and confirm two consecutive writes landed nothing.
  If a recreated section fails the same way twice, stop and do not delete a third
  time.
- Source: P-D63
- Applies: PLANNING, SCORECARD

### SD-EFF-27 Persist the computed result before building, and require reproducibility
- Rule: save the ranking or the ledger to a scratch file so a failed build
  resumes rather than recomputes. A rerun on the same inputs must produce the
  same result, and if it does not, something is non-deterministic and must be
  found before the report is trusted.
- Source: P-D64
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-28 Publish only once, at the end
- Rule: never publish a partially built artifact to show progress.
- Source: P-D65
- Applies: PLANNING, SCORECARD

### SD-EFF-29 A stale checkpoint is worse than none
- Rule: on re-entry, read the checkpoints first and resume at the first stage
  whose checkpoint is missing or whose invariants no longer hold. If the source
  file changed in name, size or row count, discard every downstream checkpoint
  and rebuild from the parse stage. Never resume past a gate that has not passed.
- Mechanism: "An artifact assembled half from last period's numbers is the worst
  thing this method can produce, because it looks complete."
- Source: P-D66
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-30 Write continuously; never hold more than one stage in memory
- Rule: after every stage that produces a finding, a number or a paragraph,
  append it to the checkpoint before starting the next stage.
- Source: R-D12
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-31 The checkpoint holds ledgers only and is never mistakable for a result
- Rule: the checkpoint holds raw findings, computed values, ranks, tie counts,
  matches and the parse log. It holds no assembled prose and no copy blocks.
  "If it contains nothing that looks finished, it cannot be mistaken for
  finished." It is never written to the user's output folder, and it is deleted
  when the real artifact publishes.
- Source: R-D39; R-D41 guardrail 10
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-32 Never present incomplete work as finished, in chat or in the file
- Rule: in conversation, never say findings are ready. Say the crawl is done,
  then ask the questions.
- Source: R-D39
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-33 A checkpoint failure degrades durability, not correctness
- Rule: retry the checkpoint write once, then continue and warn the user that an
  interruption will require restarting the crawl. A checkpoint failure never
  stops a run.
- Source: R-D12
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-34 Route every failure to a stage that can REMEDIATE it, never to one that only evaluates
- Rule: a gate failure re-runs a named chain of stages ending at the gate. A
  chain that stops at the stage which computes labels cannot fix a sentence, so
  the chain continues through the drafting stage, or the re-gate inspects
  unchanged text and fails identically.
- Source: R-D19 routing; R full capture A 7.1
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-35 Remediation never re-asks a question already answered
- Rule: a gate failure chain may fire only the specific question named in that
  chain, and only for items that question has never been asked about. "A user
  must never be asked the same question twice because a downstream gate failed."
- Source: R full capture A 7.1
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-36 Per-gate and global remediation budgets both exist
- Rule: PER_GATE_FAILURE_LIMIT failed returns on one gate routes to the bannered
  partial. GLOBAL_REMEDIATION_BUDGET cycles across all gates ends remediation
  regardless of which gate is failing. "Without a global cap, alternating
  failures between two gates can cycle far longer than any user will wait."
- Source: R full capture A 7.1
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-37 Not applicable is a passing state
- Rule: every gate resolves to PASS, FAIL or NOT APPLICABLE, and not applicable
  never blocks emit. Bind explicitly which gates are not applicable in which run
  mode.
- Prevents: "the no-data path and the goal-setting path can never emit: they skip
  the stages whose output those gates inspect, then fail gates that route back to
  the skipped stages, then exhaust the retry count and die. That path is the
  product and must never be blocked by a gate inspecting an artifact it does not
  produce."
- Source: R full capture A 7.0
- Applies: PLANNING, REVIEW, SCORECARD

### SD-EFF-38 Ask questions to buy time
- Rule: stopping to ask the user a question is free. It costs no correctness and
  converts dead waiting into useful input. Ask a stage's questions while that
  stage runs, rather than saving them for a batch afterward.
- Source: R-D14
- Applies: PLANNING, REVIEW, SCORECARD

---
