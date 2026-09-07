# GROUP SRC: ACQUIRING SOURCES

### SD-SRC-01 Retrieving an attached list is mandatory work, not best effort
- Rule: run the full retrieval ladder for EVERY attachment on EVERY message from
  EVERY manager, retrying each path at least twice before moving to the next.
  "Failing to open an attachment is not a reason to report no direction; it is a
  reason to try the next retrieval path."
- Quote: "A list from the user's own manager outranks every other input this
  method reads."
- Source: P-D112; R-D16
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-02 THE RETRIEVAL GATE: a zero count is only valid when nothing was sent
- Rule: before writing the mandatory section or drafting anything, confirm for
  every detected attachment on a supervisor or upline message that one of three
  is true: it was read and folded into the ledger; it was read and contains
  nothing in scope, which is stated in the verification list; or it could not be
  read after the full ladder, in which case the run does NOT report zero. It
  names the file, the sender and the date, states every path attempted, and says
  plainly in the opening summary that a named source could not be opened and the
  ledger is therefore incomplete.
- Mechanism: "a count of zero directives is only ever a valid result when no
  manager sent a list."
- Prevents: "a clean-looking report that silently omits their boss's
  instructions." Named as the single most damaging retrieval failure, "because
  every objective downstream is then aligned to something other than what the
  manager actually asked for."
- General form: a zero must be provably a real zero, not an unattempted one.
- Source: P-D113; R-D16
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-03 A partial recovery is treated as partial, but a partial FETCH is not the same as partial DATA
- Rule: report a partial recovery by name and treat only what was read as
  directed. But first reconcile the recovered row count against any per-group
  count the message body prints; when they agree exactly, the list is complete
  for scope and should be reported as complete, with a note about how the
  recovery was confirmed.
- Mechanism: a real file declared thousands of rows and carried a hundred and
  twenty-three real ones, so a truncated fetch recovered 100 percent of the
  actual data.
- Prevents: both overclaiming and needlessly underclaiming.
- Source: P-D114
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-04 Enumerate the plausible-but-wrong approaches and say which one fails silently
- Rule: keep FORBIDDEN_RETRIEVAL_PATHS as a list of approaches that look
  reasonable, were tested, and fail, and name the failure mode of each. The
  dangerous one does not error at all and silently corrupts a large share of the
  bytes: "the file appears retrieved, opens as garbage or fails to open, and
  nothing in the response says why."
- General form: this documentation pattern is doctrine, independent of the
  specific paths.
- Source: P-D115; R-D16
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-05 Do not select a field you were told to read; request the resource and read it out
- Rule: send no field-selection parameters on a byte fetch. The payload is in a
  named field of what comes back. "Reading the field name above and then asking
  for it by name is the single most common way this step fails, and it has failed
  a real run." The resulting error text then points at a call that returns
  metadata only, "so a reader who follows it loops and concludes the attachment
  is unreachable."
- Source: P-D116
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-06 The same address is correct streamed and corrupt decoded as text
- Rule: a raw-bytes endpoint handed to a streaming file reader is the primary
  method. The same address read through a text-decoding response is corrupt. "The
  difference is whether the bytes are streamed to a file or decoded as text."
- Source: R-D16
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-07 Never decide from a subject line whether a message carries a file
- Rule: enumerate attachments on every candidate message. "The attachment
  filename is often the real content even when the subject says nothing."
- Source: R-D16
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-08 An encoded size is not a file size
- Rule: a reported attachment size is the encoded size, roughly
  MIME_ENCODING_FACTOR times the real file. Never use it to decide a file is too
  big to fetch.
- Source: R-D16
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-09 A spilled response is not an empty response
- Rule: where a tool writes a large result to a file rather than returning it,
  read the file. "A run that treats a spilled response as empty will report no
  mail from a manager who wrote twenty messages."
- Source: R-D16
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-10 A recent file will not be in search yet
- Rule: when a message references a file rather than attaching it, resolve it by
  filename in the document store, but "a file sent hours ago will NOT be in
  search yet; do not conclude from a search miss that it does not exist."
- Source: R-D16
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-11 Asking the user to fetch it is the last step, and it names everything attempted
- Rule: only after the full ladder, ask the user to supply the file, naming the
  filename, the sender, the date and every path attempted.
- Source: R-D16; P-D118
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-12 Never ask the user to fetch something the skill can read
- Rule: if it is reachable, read it. If it is not, say so and continue. "Asking a
  manager to go fetch a document is the kind of friction that gets a tool
  abandoned."
- Source: P-D118
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-13 The central source is never optional, and it is never a reason to stop
- Rule: read it every run. A search that comes back empty means the exact folder
  was not matched, not that nothing was published. Walk a fallback ladder: the
  target period's, then the current period's, then the most recently published
  one, dated honestly. Only an unreachable library falls back to supervisor
  priorities alone, with the artifact prominently labelled.
- Mechanism: "A brief one period old is worth far more than no plan. Stopping the
  run over a folder-name mismatch is the worse failure."
- Source: P-D117
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-14 Discover the path every run; never hard-code it
- Rule: read the actual folder list and select by name content, ignoring leading
  numerals, punctuation and spacing. Reference values are a starting point for
  discovery, not a hard-coded path, and fall back to search whenever any fail to
  resolve.
- Mechanism: the documented case: two consecutive periods' folders in the same
  library differed only by a space after a numeral. "A literal path breaks the
  first period somebody types it differently, and it breaks silently."
- Source: P-D119
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-15 Resolve the source for the period being PLANNED, not "the latest"
- Rule: match on the period, because the next period's source sits alongside this
  one's rather than replacing it. Work a decision ladder and never ask.
  Critically: "A relative phrase is not a named period." Phrases like this
  period, this cycle and now fall through to the calendar rules rather than being
  read as the period the run happens to start in.
- Prevents: "A run that quietly plans the wrong period is indistinguishable from
  a correct one until the person is standing in front of the work."
- Mechanism: planning happens ahead of the period. PLAN_AHEAD_RULE decides.
- Source: P-D120
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-16 Cache what does not vary, fetch live what does
- Rule: the classification test is: does this source vary per person or per
  period. If yes it is live and can never be cached. If no it is cacheable behind
  a validity date. "Re-crawling all of them on every run for every user is the
  single largest waste and the main reason a run overruns."
- Note: the supervisor's own direction is the highest-value live source and can
  never be cached, because it is different for every user and changes weekly.
- Source: R-D37
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-17 The expiry gate is blocking, per cached block
- Rule: for every cached reference block, compare today against its validity
  date. Within validity, use the block; do not crawl and do not verify. Past
  validity, the block is STALE and MAY NOT be used until refreshed. Re-fetch from
  the source named in that block's own header and use the fresh content for this
  run.
- Prevents: "Running on expired doctrine is how a write-up gets built against
  last year's strategy or the prior period's weights. The gate is not advisory."
- Source: R-D36
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-18 A stale reference is a disclosed limitation; a halted run is a dead end
- Rule: if a re-fetch fails after the retry ladder, use the stale block, record
  that it is past its validity date and could not be refreshed, and CONTINUE.
- Source: R-D36
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-19 A refreshed block is reported back so one file stays authoritative
- Rule: when a block is refreshed, report the new content to the user in the
  closing summary so the shared configuration can be updated, "rather than every
  user re-crawling the same documents forever."
- Source: R-D36
- Applies: PLANNING, REVIEW, SCORECARD

### SD-SRC-20 Attachments on a live source message are part of the source, not an extra
- Rule: "A manager who writes here are the team goals for the half, make them
  your own, and attaches a document has put the entire goal ledger in that
  attachment."
- Source: R-D37
- Applies: REVIEW, PLANNING

### SD-SRC-21 Reading the published standard is mandatory, never assumed, and never a stop
- Rule: where a skill scores against a published standard, requirement set or
  brief, that document is READ every run. It is never assumed, never remembered
  from a previous run as authoritative, and never replaced by the method's own
  idea of what the requirements are. This is mandatory work.
- Rule, and this is the half that is repeatedly got wrong: it is NOT a stop. A
  standard that cannot be reached after the full retrieval ladder degrades. The
  run continues on the fallback ladder, banners itself as standard unconfirmed,
  names the exact release it scored against with its date, and never presents the
  result as authoritative.
- The contradiction this resolves: a skill that calls this step a hard gate with
  no skip, and elsewhere says a missing central source is never a stop and that
  the run degrades under a banner, has stated three incompatible things. The
  binding statement is this rule. Mandatory means never skipped for convenience.
  It does not mean the run stops. HARD_GATES is the closed stop list and reading
  the standard is not a member of it.
- Mechanism: the correct heading for such a step is MANDATORY, NEVER ASSUMED, not
  MANDATORY, NEVER SKIPPED. The first states the real requirement, which is that
  the content must come from the document rather than from memory or inference.
  The second reads as a stop and will be implemented as one.
- Worked case, neutral: a chain publishes next period's brief on the twenty-fifth
  for a period beginning on the first. Somebody running the scorecard on the
  twenty-second cannot reach it because it does not exist yet. The correct
  behaviour is to score against the current release, name it and its date, banner
  the run, and continue. The incorrect behaviour is to return nothing.
- Prevents: a routine calendar gap between publication and use being converted
  into a dead end, and an implementer inventing a stop condition that is in no
  enumeration of the stop list.
- Source: report 2 D8; report 1 D17; extends P-D117 and SD-EFF-02
- Applies: SCORECARD, PLANNING, REVIEW

---
