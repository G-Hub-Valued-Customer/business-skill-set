# GROUP RUN: RUN ARCHITECTURE AND VERIFICATION DESIGN

### SD-RUN-01 A supervised swarm, not one long script
- Rule: the supervisor owns the gates and never does the work. Workers own
  exactly one stage each and are disposable. Every worker writes a checkpoint. A
  worker failure is isolated to its own partition.
- Source: P-S23 architecture; P-D50 through P-D55
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RUN-02 Every stage has the same six-field contract
- Rule: PRECONDITION, ACTION, POSTCONDITION, ON FAIL, WAIT, STOP. Uniform failure
  semantics across every stage removes the need for per-stage judgment.
- Source: R Part 3
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RUN-03 Two verifiers are independent only when they answer DIFFERENT questions
- Rule: "If both analysts emit computed metrics, each must do the same arithmetic
  on the same cells, and their agreement proves only that they picked the same
  columns. Independence is real only when the two methods answer DIFFERENT
  questions." One answers what a column MEANS, from names and vocabulary. The
  other answers what a column's DATA LOOKS LIKE, from distribution, cardinality,
  range, null pattern and cross-file ratio behaviour. The arithmetic is then done
  once, deterministically, by the orchestrator.
- Prevents: fake corroboration from two agents doing the same thing.
- General form: applies to any two-agent verification design in any skill.
- Source: R-D17
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RUN-04 Never reconcile against a single ledger
- Rule: a single verifier produces an UNVERIFIED result, which does not meet the
  standard for a record with consequence. Never promote single-method output.
- Source: R-D17
- Applies: REVIEW, PLANNING, SCORECARD

### SD-RUN-05 Reconcile only what BOTH verifiers can independently emit
- Rule: split reconciled items into MUST MATCH EXACTLY and CORROBORATED, NOT
  MATCHED. For a corroborated item, one verifier is authoritative and the other
  runs a rejection test only. "Demanding that two differently-instructed verifiers
  produce identical semantic output is unsatisfiable and would hard-stop every
  data-bearing run."
- Mechanism: count UNRESOLVED only for items both verifiers actually emit or
  corroborate. An item only one produces by design is never counted as a
  disagreement.
- Source: R-D19
- Applies: REVIEW, PLANNING, SCORECARD

### SD-RUN-06 NOT REFUTED is not confirmation
- Rule: a rejection test is a necessary condition, never a sufficient one. In the
  case that produced this rule the test "failed to refute 18 of 20 deliberately
  WRONG pairings, since almost any part is smaller than almost any whole. It can
  only catch a gross error."
- General form: an epistemic rule about validation tests everywhere. A test that
  can only catch a gross error must never be reported as a confirmation.
- Source: R-D18
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RUN-07 A declared incompatibility outranks any corroboration verdict
- Rule: a blocking incompatibility declared by an earlier item outranks a
  not-refuted verdict from a later one. "Corroboration never overrides a declared
  rate or unit incompatibility."
- Source: R-D18
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RUN-08 A sparse population is not a mispairing
- Rule: a median of exactly zero means the entity is thinly distributed, not
  mispaired. Report the zero share and mark the verdict INCONCLUSIVE, never
  REFUTED.
- Source: R-D18
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RUN-09 Never average two disagreeing derivations, and never publish a disputed value
- Rule: on disagreement, the authoritative side re-derives once, showing its work.
  Still refuted, mark UNRESOLVED and exclude that item's metrics. Above
  UNRESOLVED_STOP_COUNT unresolved items, stop.
- Source: R-D19; R-D41 guardrail 11
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RUN-10 Named regression cases run before any change ships
- Rule: keep a small closed set of end-to-end cases, each with inputs, expected
  and failure, covering the named traps. Run all of them before a change ships.
- Mechanism: REGRESSION_CASES. The set covers, at minimum, the environment-credit
  trap, the user with no documentation, the altitude ceiling, the unconfirmed
  inference, the span-of-control error, the low-confidence inference, and the tied
  superlative.
- Source: R Part 11
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RUN-11 Freeze a ground-truth classification and gate on reproducing it exactly
- Rule: apply the classifier to every item of one real dataset, freeze the result
  as a fixture, run the classifier against it before scoring anything, and report
  the match rate. Anything under a perfect match is a failing gate. "An
  implementation that does not reproduce this table exactly has a defect in its
  classifier, not a difference of opinion."
- Companion rule: "On a dataset this table does not cover, the ladder is the
  authority and this table is the worked example."
- General form: REFERENCE_CLASSIFICATION_FIXTURE starts empty and is populated
  from the first real dataset.
- Source: P-D211
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RUN-12 The portability test is two real files of the same source, months apart
- Rule: hold two real exports of the same source from different periods, and
  declare that a change to the resolution dictionary which would break either one
  is wrong.
- Mechanism: the two files will differ on header row, sheet count, column naming,
  measure basis, code type, block presence, flag presence and column count.
- Source: P-S28
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RUN-13 Version stamp, what changed, and what was verified versus not
- Rule: carry a version block that separates what was verified by execution from
  what was not, and name the first-run checks a deployer should watch.
- Prevents: a reader trusting an unverified path as much as a verified one.
- Source: P-S2
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RUN-14 Compute every figure with a tool, never mentally
- Rule: every arithmetic result in an artifact is computed by code.
- Source: P-D235
- Applies: PLANNING, REVIEW, SCORECARD

### SD-RUN-15 A run that cannot be reproduced cannot be trusted
- Rule: a rerun on identical inputs must produce an identical result. Where it
  does not, find the non-determinism before the report is used.
- Mechanism: enforced by deterministic tie-breaks ending in the identifier, by
  the percentile definition averaging tied ranks, and by a stable ordering rule
  for any list of suggestions offered to a user.
- Source: P-D64; P-D228; P-D216
- Applies: PLANNING, REVIEW, SCORECARD

---
