# GROUP IDN: IDENTITY, ROLE AND SCOPE

### SD-IDN-01 The manager lookup is mandatory and non-substitutable
- Rule: use the call that returns the manager relationship and nothing else. A
  profile record that carries no manager field can never answer who someone
  reports to, and "using it for that purpose returns a confident wrong answer
  rather than an error."
- Prevents: "Concluding no supervisor from a profile record is the single most
  damaging error this method can make, because it silently deletes the nearest
  priority sources and produces an artifact that ranks on the central source
  alone while telling the reader the supervisor published nothing."
- General form: never infer an absence from a source that does not carry the
  field.
- Source: P-D67
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-02 Only one person in the organization has no supervisor
- Rule: before recording "no supervisor", both must hold: the manager call was
  actually made and returned empty, AND the person's own title names the top of
  the house. An error is a failed lookup, not an absent manager. "Do not convert
  a data gap into a claim about the organization."
- **WHERE NO DIRECTORY EXISTS AT ALL, THE PERSON IS ASKED, AND THEIR ANSWER IS AN
  ANSWER.** The two-part test governs what may be inferred from a directory that
  FAILED. It does not require a person to be recorded as unresolved when they have
  told you the answer themselves. Where the directory capability is ABSENT rather
  than failing, the person-tier supervisor question is the instrument, and three
  outcomes are possible: a name, which binds; a statement that they are the top of
  the house, which is recorded as such on the person's own account with the source
  named as SELF-REPORTED rather than as a directory reading; and no answer, which
  is UNRESOLVED. Recording the head of an organization as having an unresolved
  supervisor when they have just said they have none is correct by the letter and
  reads as ridiculous, which costs the artifact more credibility than the
  precision buys.
- Rule: whichever outcome is recorded, the SOURCE is recorded with it: directory,
  self-reported, or unresolved. A self-reported top of house never suppresses the
  priority sweep for anybody below them, and it is never written back to the org
  tier by a run.
- Source: P-D68
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-03 A scope word outranks a role word, and that test runs FIRST
- Rule: if the title carries any token from WIDE_SCOPE_TOKENS anywhere in it, the
  role is the senior tier regardless of what follows. Only a title whose most
  senior token is a junior role AND which names no wider scope gets the junior
  shape. Record the token that decided it.
- Prevents: demoting a senior title to a narrower scope than the file supports.
- Source: P-D69
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-04 Expand abbreviations before matching, and take the most senior token
- Rule: match case-insensitively, ignore punctuation, expand
  ROLE_TITLE_ABBREVIATIONS, then take the most senior token present.
- Mechanism: "Real directory titles are written in shorthand rather than in full,
  and a table lookup that misses the abbreviation falls through to inference when
  the record was unambiguous all along."
- Source: P-D70
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-05 Losing the directory costs the shortcuts, not the deliverable
- Rule: if identity cannot be resolved at all, infer role and scope from the
  file, note what was assumed, and carry on. "Losing the directory costs the
  supervisor's priorities and the my shortcut; it does not cost the artifact."
- Source: P-D71
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-06 Nothing may be hard-coded from the reference data
- Rule: no row count, column count, unit list, median or item count may be
  hard-coded. Every threshold is computed from the file in hand and the actual
  figures are reported. "The source is never the same size twice, and the method
  must not assume otherwise."
- Source: P-D72
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-07 An ambiguous identifier is resolved against the DATA, never against its own pattern
- Rule: whenever a padded code is ambiguous between two levels, test the candidate
  against each level's own column and take the level that returns rows.
  Trailing-pad classification is decisive only up to SCOPE_CODE_AMBIGUITY_THRESHOLD
  minus one; at or above it the code is ambiguous and the pattern is never the
  last word.
- Mechanism: an explicit precedence row that overrides the pattern rules above it.
- Prevents: silently scoping a narrow-unit owner to an entire coarse unit.
- General form: applies wherever hierarchical identifiers share a namespace.
- Source: P-D73
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-08 One tie-break for ambiguity, used everywhere: the word, then the role
- Rule: when more than one reading returns rows, prefer the level named by the
  word the user used, then the level their own role implies. Ask only when no
  reading returns rows. "That order, word first then role, is the single
  tie-break used everywhere for an ambiguous scope code."
- Prevents: an ad hoc tie-break invented per site.
- Source: P-D74
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-09 Compare identifiers as TEXT on both sides
- Rule: before filtering, cast both the column value and the resolved code to
  text, trim whitespace, drop any decimal tail, strip separators, and pad the
  column value to the code's length. Apply the same to unit identifiers and
  postal codes.
- Prevents: "a typed comparison between a resolved code and the wrong one of
  those returns zero rows and looks exactly like an empty scope."
- Source: P-D75; R-D24
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-10 If the requested scope is at or above everything the file contains, apply no filter
- Rule: test whether every in-scope row already carries the requested code as a
  left-anchored prefix. If so, skip the filter, rank the whole file, and say so.
  This is a normal path, not a degraded one.
- Source: P-D76
- Applies: PLANNING, SCORECARD

### SD-IDN-11 The user speaks naturally; the skill does the arithmetic
- Rule: accept a short code or a plain phrase, identify the level from the digit
  count or the word used, and pad it yourself. Never ask the user to pad and
  never reject a short code.
- Prevents: friction that gets a tool abandoned.
- Source: P-D77
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-12 Search every record before asking, and asking is the last resort
- Rule: work the ladder and stop at the first hit: the request itself; the user's
  own directory record read in FULL, not only the title; their manager's record;
  memory; the file itself; the filename or the message that carried the file; and
  only then ask. "A record that is bare on one person is often complete on the
  person above them."
- Quote: "Never ask for a number the records already hold."
- Source: P-D78
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-13 When you must ask, ask in the user's language, not the file's
- Rule: offer the distinct values present, each labelled with something a person
  recognizes and a count beside each, and accept a name or a list position as the
  answer, not only the code.
- Source: P-D79
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-14 Narrow before asking
- Rule: if a coarser level resolves but a finer one does not, use the coarser
  level to narrow the question. That turns a question about eleven options into a
  question about a handful.
- Source: P-D80
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-15 Persist a settled answer and verify the save succeeded
- Rule: save the resolved value immediately, confirm the call returned success,
  retry once on failure, and tell the user plainly if it still will not stick,
  "because a failed save means the user gets asked again every run."
- Source: P-D81
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-16 Zero rows means the filter is wrong before it means the scope is empty
- Rule: re-test the comparison as text on both sides and re-test the level
  reading first. Only then stop and list the distinct values present at every
  level.
- Source: P-D82
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-17 Batch every question into a single message
- Rule: if three items are ambiguous, ask about all three at once. Never ask,
  work, then ask again, "that is the pattern that makes a tool feel like an
  interrogation."
- Source: P-D83
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-18 Ask only for REQUIRED concepts; never ask for optional ones
- Rule: required means the minimum set the method cannot run without. For an
  optional concept, skip the feature it feeds, name it in the audit section, and
  continue. "A missing breadth column costs one section; a question costs the
  user's attention and the run's momentum."
- Source: P-D84
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-19 Propose, do not prompt
- Rule: at scope lock, resolve identity, role, manager and chain from records and
  present them as confirmations, never as open prompts. "A write-up built on the
  wrong scope is worthless."
- Source: R Stage 0
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-20 Never ask what the tools can answer, and keep every question under thirty seconds
- Rule: every question must be answerable in under thirty seconds, must carry the
  findings that prompted it, and must never ask for something the tools could
  have resolved.
- Source: R 6.3
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-21 Blocking and non-blocking questions have different failure semantics
- Rule: a non-blocking question is freely skippable and an empty answer means
  skip, never cancel. A blocking question is not ignorable: if the user declines
  or does not answer, the run terminates through the bannered incomplete path.
  The skill never fabricates the missing value and never silently proceeds as if
  the question had been answered. "This distinction is the difference between a
  user choosing to leave a field blank and the skill inventing content for a
  permanent record."
- Source: R 6.2
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-22 Question batching is arithmetic, not judgment
- Rule: fire every blocking question whose trigger is met at the current stage.
  Count them as B. The non-blocking budget for the round is
  max(0, QUESTION_BATCH_MAX minus B), filled by weight. Where several share a
  weight, order by position in the bank. "Batch composition is never left to
  judgment." A wall of questions is abandonment.
- Source: R 6.1
- Applies: PLANNING, REVIEW, SCORECARD

### SD-IDN-23 A composite question is one question
- Rule: a grid covering many objectives, behaviours or items counts as one toward
  the batch, not as N.
- Source: R 6.1
- Applies: REVIEW

### SD-IDN-24 A question that is the sole input to a required section is exempt from the budget
- Rule: where a question is the only source for a section the destination form
  requires, it always fires and is never dropped by arithmetic.
- Source: R 6.1
- Applies: REVIEW

### SD-IDN-25 A question never fires before the stage that supplies its context
- Rule: the stage assignment in the question bank is authoritative.
- Source: R 6.1
- Applies: PLANNING, REVIEW, SCORECARD

---
