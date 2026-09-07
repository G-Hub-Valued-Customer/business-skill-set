# CAPABILITY PROBE AND DEGRADATION LADDER

Assume no tooling. Every run begins by finding out what it can actually do, and
then does the best honest version of the job with what it has.

Two rules govern this whole file:

- **C0. Probe, never assume.** A capability is present only when a probe returned
  evidence. A capability named in the environment description but not probed is
  UNKNOWN, and unknown is treated as absent.
- **C1. A degraded run announces its degradation in the output.** Not only in the
  chat, which scrolls away, but in the artifact itself, which is what survives.
  A run that quietly produces less is the failure this whole file exists to
  prevent.

---

# PART 1: THE PROBE

## 1.1 When it runs

Once, at the start of every run, before the first stage. It is not a stage and
it has no gate; it produces a record that every later stage reads.

The probe costs a few seconds. It is never skipped to save time, because
SD-EFF-01 says run length is not a cost the method recognizes, and because a
skill that discovers halfway through that it cannot write a workbook has already
spent the budget it needed for the fallback.

## 1.2 The probe record

The probe writes one record to the scratch directory before anything else runs:

    {
      "probe_version": "<BUNDLE_VERSION>",
      "probed_at": "<timestamp>",
      "capabilities": {
        "<name>": {
          "state": "PRESENT | ABSENT | DEGRADED | UNKNOWN",
          "evidence": "<what the probe actually saw>",
          "probe_cost_ms": <n>,
          "fallback_selected": "<name of the ladder rung taken>"
        }
      },
      "run_mode": "FULL | DEGRADED",
      "degradations": [ "<one line per degraded capability>" ]
    }

Every later stage reads this record rather than re-probing. A stage that finds a
capability behaving differently from its probed state updates the record, marks
the capability DEGRADED, and appends to `degradations`. It does not silently
adapt.

## 1.3 Probe order

Ordered so that the cheapest probes and the ones the most other things depend on
run first. Stop conditions are noted; there is only one, and it is the hard gate
that no source can be read at all.

| # | Capability | Why it is at this position |
|---|---|---|
| 1 | FILE_READ | Everything else depends on being able to read an input. |
| 2 | FILE_WRITE | Needed for the checkpoint before any stage produces a finding. |
| 3 | CODE_EXECUTION | Decides whether arithmetic can be computed rather than reasoned. |
| 4 | SPREADSHEET_WRITE | Decides the whole deliverable form. |
| 5 | SPREADSHEET_INSPECT | Decides whether the formatting gate can run at all. |
| 6 | DOCUMENT_WRITE | Decides the whole deliverable form for a skill whose OUTPUT_MEDIUM is docx, exactly as SPREADSHEET_WRITE does for a skill whose medium is xlsx. |
| 7 | DOCUMENT_INSPECT | Decides whether the docx gate can run at all. |
| 8 | DOCUMENT_EXTRACT | Decides whether a published brief or reference can be parsed. |
| 9 | SHELL | Decides the recovery paths available to the other capabilities. |
| 10 | SYSTEM_OF_RECORD | The source file, the roster, the pipeline query. |
| 11 | MAIL | The nearest priority source and the attachment ladder. |
| 12 | DIRECTORY | Identity, role and the supervisor chain. |
| 13 | DOC_STORE | Reference material and the cached blocks. |
| 14 | CHAT_AND_CALENDAR | Evidence tiers beyond mail. |
| 15 | WEB | External reference, and the last resort for a public document. |
| 16 | MEMORY | Whether a person-tier answer survives to the next run. |
| 17 | INTERACTIVE | Whether the run can ask a question at all. |

## 1.4 How each capability is probed

A probe is the smallest real operation that proves the capability, run against
something the skill already needs. A probe never mutates user data and never
creates anything outside SCRATCH_DIR.

### FILE_READ
Probe: list SCRATCH_DIR, then list UPLOAD_DIR, then read the first few bytes of
any file found there.
PRESENT when a directory listing returns and a read returns bytes.
DEGRADED when a listing returns but reads fail, or when reads are size-capped.
Record the cap.
ABSENT when no listing returns.

### FILE_WRITE
Probe: write a small file to SCRATCH_DIR named for the probe, read it back,
compare, delete it.
PRESENT when the round trip matches.
DEGRADED when the write reports success and the read-back is empty. Wait
WRITE_CONFIRM_WAIT_SECONDS and read again before concluding, per SD-EFF-10.
ABSENT when the write errors.

### CODE_EXECUTION
Probe: evaluate a small deterministic expression with a known answer, and a date
parse with a known answer.
PRESENT when both return correct results.
DEGRADED when arithmetic works but no library for the file formats in hand is
importable. Record which libraries resolved.
ABSENT otherwise.

### SPREADSHEET_WRITE
Probe: create a scratch workbook with one sheet, write a few cells, apply one
structural operation, read the cells back.
PRESENT when data and structure both land and read back.
DEGRADED when data lands but structural operations fail or cannot be verified.
ABSENT when no workbook can be created.

### SPREADSHEET_INSPECT
Probe: open the scratch workbook produced by the previous probe and read back a
structural attribute, not a value. Freeze position, table presence, fill colour,
font, column width, row height.
PRESENT when structural attributes are returned.
ABSENT when only cell values can be read.
This probe is separate from SPREADSHEET_WRITE on purpose: an environment that can
write a workbook and cannot inspect one cannot run the formatting gate, and
SD-FMT-06 makes that a publication blocker rather than a cosmetic issue.

### DOCUMENT_WRITE
Probe: create a scratch document, write a heading, a paragraph and one styled
run, save it, and read the text back.
PRESENT when text and structure both land and read back.
DEGRADED when text lands but heading styles, fills or fonts fail or cannot be
verified.
ABSENT when no document can be created.
DOCUMENT_WRITE is the docx counterpart of SPREADSHEET_WRITE and is probed
separately from it, because an environment routinely has one and not the other,
and OUTPUT_MEDIUM is keyed per skill rather than shared across the bundle.

### DOCUMENT_INSPECT
Probe: open the scratch document produced by the previous probe and read back a
structural attribute, not a text value. The style applied to a heading, a fill, a
font name, a font size.
PRESENT when structural attributes are returned.
ABSENT when only text can be read.
This probe is separate from DOCUMENT_WRITE for the same reason SPREADSHEET_INSPECT
is separate from SPREADSHEET_WRITE: an environment that can write a document and
cannot inspect one cannot run the docx gate, and SD-FMT-06 makes that a
publication blocker rather than a cosmetic issue.

### DOCUMENT_EXTRACT
Probe: attempt a layout-preserving text extraction from any document already in
hand; if none is in hand, defer the probe until the first document arrives and
record the state as UNKNOWN until then.
PRESENT when text with positional structure is returned.
DEGRADED when only a flat text stream is returned, or when only image rendering
is available.
ABSENT when neither works.

### SHELL
Probe: run a trivial command with a known output.
PRESENT when it returns.
DEGRADED when it returns but the working directory does not persist, or a
timeout is enforced below what a long read needs. Record the timeout.
ABSENT when no command runs.

### SYSTEM_OF_RECORD
Probe: attempt, in SOURCE_WORKBOOK_LOCATIONS order, to locate a source matching
SOURCE_WORKBOOK_NAME for the resolved period. Do not parse it yet; just confirm
it can be reached and its size read.
PRESENT when a candidate source is reachable.
DEGRADED when a source is reachable but is stale, partial, or covers a scope
narrower than the request.
ABSENT when nothing is reachable.

### MAIL
Probe: list mail folders, then list messages in one folder for a one-day window.
PRESENT when both return.
DEGRADED when folder listing succeeds and message listing spills to a file
rather than returning inline. That is not a failure; read the spilled file, per
SD-SRC-09.
ABSENT when folder listing fails.

### DIRECTORY
Probe: resolve the running user's own record. Then, separately, resolve the
manager relationship. These are two probes, not one, because a profile record
that carries no manager field can never answer the manager question and treating
one as evidence of the other is SD-IDN-01's named failure.
PRESENT when both return.
DEGRADED when self resolves and manager does not.
ABSENT when neither resolves.

### DOC_STORE
Probe: resolve the container identifier by discovery, then list one level of
folders. Never test a hard-coded path, per SD-SRC-14.
PRESENT when a listing returns.
DEGRADED when search returns but direct listing does not, or the reverse.
ABSENT when neither.

### CHAT_AND_CALENDAR
Probe: list one day of calendar events, and one channel or conversation.
Independent states for each.

### WEB
Probe: fetch one known-stable reference already named in the config, or a
harmless well-known endpoint.
PRESENT when content returns.
DEGRADED when fetches succeed only through a proxy with a size or type
restriction. Record the restriction.
ABSENT when no fetch returns.

### MEMORY
Probe: write a probe key, read it back, delete it.
PRESENT when the round trip matches.
DEGRADED when the write returns success and the read returns nothing. Retry
once, per SD-IDN-15.
ABSENT when the write errors.

### INTERACTIVE
Probe: not a call. Determine from the run context whether a question can reach a
person and receive an answer within this run. A scheduled or unattended run is
NON-INTERACTIVE.
PRESENT when a question can be answered in-run.
ABSENT otherwise.

## 1.5 What the probe never does

- It never writes to OUTPUT_DIR.
- It never sends a message, posts anything, or modifies a record.
- It never counts a capability as present because the environment claimed it.
- It never treats a single failure as ABSENT before the retry rules in
  SD-EFF-09 and SD-EFF-10 have been applied. A transient failure at probe time
  is still a transient failure.
- It never blocks the run except on the one hard gate below.

## 1.6 The one hard gate at probe time

If FILE_READ is ABSENT and SYSTEM_OF_RECORD is ABSENT and no source was supplied
inline, the run cannot begin. Stop and say exactly that: no source could be read,
name every location attempted, and ask for the file. This is the only probe-time
stop, and it is the same gate as SD-PRS-24's zero-record gate arriving earlier.

Everything else degrades.

---

# PART 2: THE DEGRADATION LADDER

Each capability has a ladder. The run takes the highest rung it can reach,
records which rung it took in the probe record, and announces it in the output.

The general shape of every ladder is the same:

1. Do the full thing.
2. Do the same thing by another route.
3. Produce a different artifact that carries **identical information**.
4. Produce a reduced artifact and name exactly what is missing from it.
5. Produce nothing and say why, naming every path attempted.

Rung 3 is the important one and it is where most of the work is. A different
container is not a reduced deliverable. The information contract is what must be
preserved, not the file format.

## 2.1 SPREADSHEET_WRITE

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT | Build the workbook: every section in TAB_CONTRACT, in order, with the full identity block, the formatting elements, and the caps. The full contract. |
| 2 | DEGRADED, data lands but structure does not | Build every section with correct data, correct column order, correct headers, correct ranks and correct caps. Apply what structure lands and verify it. For every formatting element that could not be applied, record it as not applied, not as failed. Announce: the numbers are complete and the presentation is reduced. |
| 3 | ABSENT | Emit structured markdown carrying identical information. See 2.1.1. |
| 4 | ABSENT and markdown cannot be written to a file | Emit the same structured markdown inline in the reply, with the caps still applied, and say plainly that it could not be written to a file. |
| 5 | Nothing can be emitted | Report the failure, name every path attempted, preserve the checkpoint. |

### 2.1.1 The markdown equivalent, and what identical information means

The markdown fallback is not a summary. It carries:

- Every section in TAB_CONTRACT, in the same order, as a level-two heading using
  the same section title string. A section with nothing to report still appears,
  carrying its MSG_EMPTY_SECTION row. SD-CTR-07 does not relax.
- Every column of IDENTITY_BLOCK_COLUMNS plus that section's own columns, in the
  same order, with byte-identical header strings. SD-CTR-09 does not relax.
- The same rank continuity across the merit sections. SD-RNK-01 does not relax.
- The same caps, and the same "showing n of N" note under the same condition.
  SD-RNK-06 does not relax.
- The published score to SCORE_DECIMAL_PLACES. SD-CTR-10 does not relax.
- The front panel and the audit section as prose sections in the same order.
- Identifiers and postal codes rendered so that leading zeros survive: wrap them
  in backticks or prefix-quote them, and say in the front panel which convention
  was used, so a reader importing the table can restore the text type.
- A wide table is emitted as a pipe table. Where a section has more columns than
  a pipe table reads comfortably, split it into two tables joined on the
  identifier, in the same column order, and say so. Never drop a column, per
  SD-CTR-13.
- A row-height rule has no meaning in markdown, so element checks that do not
  apply are recorded as not applicable rather than failed, per SD-FMT-01.

What changes: presentation only. What does not change: the sections, their
order, the columns, the headers, the ranks, the caps, the counts, the score, the
disclosures and the audit trail.

## 2.2 SPREADSHEET_INSPECT

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT | Run the full formatting gate: every element, per section, recorded as a pass matrix. |
| 2 | DEGRADED, some attributes readable | Run every element that can be read. Record each unreadable element as NOT VERIFIED, naming the element. |
| 3 | ABSENT, and SPREADSHEET_WRITE is PRESENT | The formatting gate cannot run. Per SD-FMT-06 the workbook must not be published as verified. Two permitted resolutions, in order: fall back to the markdown equivalent in 2.1.1, which has no unverifiable formatting contract; or publish the workbook explicitly labelled as formatting-unverified, in the front panel and in the reply, naming which elements could not be checked. Never publish silently. |

The choice between those two resolutions is a binding, not a judgment, and it has
a name: DELIVERABLE_CONTAINER_REQUIRED. Where it is true the labelled workbook is
delivered; where it is false or unbound the markdown equivalent is delivered. Where the binding does not
say, take the markdown, because SD-STR-10 says to prefer the error a reader can
detect.

## 2.2a DOCUMENT_WRITE

Read by a skill whose OUTPUT_MEDIUM is docx. A skill whose medium is xlsx reads
2.1 instead and never reads this one.

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT | Build the document: every section of the bound form, in order, one copyable block per field, each carrying its limit and its count, the submission boundary, and the panel styling. The full contract in reference/output-contract.md PART 3. |
| 2 | DEGRADED, text lands but styling does not | Build every block with correct text, correct headings in the destination system's own words, correct limits and correct counts. Apply what styling lands and verify it. For every requirement that could not be applied, record it as not applied, not as failed. Announce: the fields are complete and the presentation is reduced. |
| 3 | ABSENT | Emit structured markdown carrying identical information. See 2.2a.1. |
| 4 | ABSENT and markdown cannot be written to a file | Emit the same structured markdown inline in the reply, with every block still separately headed and still carrying its count, and say plainly that it could not be written to a file. |
| 5 | Nothing can be emitted | Report the failure, name every path attempted, preserve the checkpoint. |

### 2.2a.1 The markdown equivalent, and what identical information means here

The copy contract is INFORMATION and survives every rung. The styling is
PRESENTATION and does not. The markdown fallback carries:

- Every section of the bound form, in the bound order, as a heading using the
  destination system's own name for the field. A section with nothing to report
  still appears, carrying its one explanatory line. SD-CTR-07 does not relax.
- One block per field, with nothing interleaved between a heading and the next
  heading, so the block is still selectable and pastable as a unit.
- The limit and the current count beside every heading, and an over-limit block
  still blocks publication. A truncation reaching the destination system is the
  failure the counts exist to prevent, and no degradation excuses it.
- The submission boundary, stated in plain words, with nothing below it inside a
  block. SD-CTR-22 and SD-CTR-23 do not relax.
- The front panel, the degradation block, the focus section, the items to verify,
  the method and the contact line, in the same order.

What changes: presentation only. What does not change: the fields, their order,
their names, their limits, their counts, the boundary, the disclosures and the
audit trail.

## 2.2b DOCUMENT_INSPECT

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT | Run the full docx gate: every requirement of reference/output-contract.md PART 3, read back from the built document, recorded as a pass matrix. |
| 2 | DEGRADED, some attributes readable | Run every requirement that can be read. Record each unreadable one as NOT VERIFIED, naming it. |
| 3 | ABSENT, and DOCUMENT_WRITE is PRESENT | The docx gate cannot run. Per SD-FMT-06 the document must not be published as verified. Two permitted resolutions, in order: fall back to the markdown equivalent in 2.2a.1, which has no unverifiable styling contract; or publish the document explicitly labelled as formatting-unverified, in the front panel and in the reply, naming which requirements could not be checked. Never publish silently. |

**THE COUNT IS NOT STYLING AND IS NEVER EXCUSED BY THIS RUNG.** A character count
is read from the text, not from a structural attribute, so a run that cannot
inspect structure can still recount every block. An implementation that skips the
over-limit check because the docx gate could not run has confused a presentation
failure with a correctness one, and the field it let through arrives truncated in
a permanent record.

The choice between the two resolutions at rung 3 is a binding, not a judgment,
and it is the same one 2.2 names: DELIVERABLE_CONTAINER_REQUIRED. Where it is true
the labelled document is delivered; where it is false or unbound the markdown
equivalent is delivered.

## 2.3 FILE_READ

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT | Read from SOURCE_WORKBOOK_LOCATIONS in order. |
| 2 | DEGRADED, size-capped reads | Read in chunks. Where a chunked read cannot reconstruct the whole file, reconcile the recovered record count against any count the source itself declares, per SD-SRC-03, and report complete only when they agree exactly. |
| 3 | ABSENT for a location | Fall to the next location in order. Escalate up the scope hierarchy for a coarser file and filter down, per SD-PRS-26, stating which level was used. |
| 4 | ABSENT everywhere | Ask for the file, naming every location attempted. This is a hard gate. |

## 2.4 FILE_WRITE

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT | Checkpoint after every stage, per SD-EFF-30. |
| 2 | DEGRADED | Retry once, then continue without checkpointing and warn the user that an interruption will require restarting from the beginning. A checkpoint failure degrades durability, not correctness, per SD-EFF-33. |
| 3 | ABSENT | Same as rung 2, plus: run in a single pass with no fan-out, because SD-EFF-17 depends on per-partition checkpoints that cannot be written. Announce that the run is single-pass. |

## 2.5 CODE_EXECUTION

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT | Compute every figure with the tool, per SD-RUN-14. |
| 2 | DEGRADED, arithmetic available, format libraries missing | Convert the source through whatever route is available, then compute. If no route exists, treat SYSTEM_OF_RECORD as unreadable in that format and fall to the next location. |
| 3 | ABSENT | Do not compute percentiles, medians, peer norms, scores or attainment percentages. Emit the population, the identifiers, the resolved priorities and the qualitative sections, and state plainly that no ranked list could be produced because no computation was available. Never estimate a threshold, never rank by impression. SD-SCL-03 and SD-CNF-07 both forbid it. |

Rung 3 is a genuine deliverable in the REVIEW skill, where the evidence ledger,
the directed items, the reconstructed objectives and the questions are all
useful without arithmetic. It is a thin deliverable in PLANNING and SCORECARD,
and it says so.

## 2.6 SHELL

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT | Available as a recovery path for file access, format conversion and byte-level attachment recovery. |
| 2 | DEGRADED, timeouts or no persistent working directory | Break long operations into bounded steps, each writing its own checkpoint, and pass state by file rather than by shell state. |
| 3 | ABSENT | Every ladder that names shell as a rung skips that rung and continues. No capability depends on shell alone; shell is a recovery route, never a primary one. |

## 2.7 WEB

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT | Fetch external references named in the config when a cached block is stale. |
| 2 | DEGRADED, restricted fetches | Fetch what is permitted. Record the restriction. |
| 3 | ABSENT | Use the cached block and record it as past validity and unrefreshable, per SD-SRC-18. A stale reference is a disclosed limitation; a halted run is a dead end. Never invent the content of a reference that could not be fetched. |

Web is never the first route to an internal document. The document store and the
mailbox come first, because an internal document reached over the open web is
usually the wrong copy.

## 2.8 SYSTEM_OF_RECORD

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT for the requested period and scope | Normal run. |
| 2 | PRESENT at a coarser scope only | Read the coarser file and filter down. State which level was used, per SD-PRS-26. |
| 3 | PRESENT but from a prior period | Use it, date it honestly, and say in the front panel and the reply that the plan was built on a prior period's data. Never present it as current. |
| 4 | PRESENT but partial | Never analyze a partial source, per SD-PRS-24. Count records rather than trusting the reported extent. If the record count is zero, that is a hard gate. |
| 5 | ABSENT | Ask for the file. Do not improvise a population. |

For a FLOWING population, add one rung between 1 and 2: the query returns the
open set but not the closed set, so period-over-period comparison is impossible.
Run the current-state sections and state that no comparison could be computed.

## 2.9 MAIL

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT | Full sender sweep across MAIL_SWEEP_FOLDERS over both windows, then the attachment ladder for every attachment, then the retrieval gate. |
| 2 | DEGRADED, listing works and attachment bytes do not | Sweep and classify normally. For every detected attachment that could not be read, take the third permitted state of the retrieval gate in SD-SRC-02: name the file, the sender, the date and every path attempted, and say plainly in the opening summary that a named source could not be opened and the priority ledger is therefore incomplete. Never report zero directives. |
| 3 | DEGRADED, some folders unreachable | Sweep what is reachable, and name the folders that were not, with the windows covered. Per SD-PRI-04, an absence concluded from an incomplete sweep is not an absence. |
| 4 | ABSENT | Record that the nearest priority source could not be read. Run on the remaining bound sources. Label the artifact prominently as built without supervisor direction. Do not describe the result as "no priorities found". |

Rung 4 is the most dangerous degradation in the bundle, because the artifact
still looks complete. Its announcement is mandatory and appears in three places:
the front panel, the audit section, and the first line of the reply.

## 2.10 DIRECTORY

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT, self and manager | Resolve identity, role, scope and chain silently. Confirm, do not prompt. |
| 2 | DEGRADED, self only | Resolve role and scope from the record. Ask the PERSON-tier supervisor question. Never infer "no supervisor" from a record with no manager field, per SD-IDN-01. |
| 3 | ABSENT | Run the PERSON script in full. If INTERACTIVE is also ABSENT, infer role and scope from the file, record what was assumed, and carry on. Losing the directory costs the shortcuts, not the deliverable, per SD-IDN-05. |

## 2.11 DOC_STORE

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT | Discover paths every run, resolve the current reference set, apply the expiry gate. |
| 2 | DEGRADED, search only | Search by name content, ignoring leading numerals, punctuation and spacing. |
| 3 | ABSENT | Use the cached blocks. Where a block is past validity, use it and record it as stale and unrefreshable, per SD-SRC-18. Where a required reference has no cached equivalent at all, the run CONTINUES: the sections that reference would have filled ship with their explanatory row naming the reference, every claim that would have laddered through it drops to the highest rung it can defend, and the gap is announced in all three places per Part 4. This is NEVER a stop. HARD_GATES is the closed stop list and nothing here adds to it, per SD-EFF-02, SD-SRC-13 and SD-SRC-21. |

## 2.12 DOCUMENT_EXTRACT

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT, layout preserved | Parse the published table by layout, pair by proximity, confirm against a second reading, and report the confidence split, per SD-PRS-02. |
| 2 | DEGRADED, flat text only | Parse what pairs unambiguously. Report how many pairs were confirmed by two readings, how many rest on one, and how many could not be paired. |
| 3 | DEGRADED, image rendering only | Read the page as an image. This is a normal tool, not a last resort. |
| 4 | ABSENT | Fall to the descending close-weight ladder for anything whose date could not be read, per SD-PRS-03, and name every item that took a fallback weight, per SD-LNG-05. Never default an unread date upward. |

## 2.13 MEMORY

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT | Persist person-tier answers, confirm the save, retry once on failure. |
| 2 | ABSENT | Ask the PERSON questions this run, use the answers, and tell the person plainly that the answers could not be saved and will be asked again next time, per SD-IDN-15. |

## 2.14 INTERACTIVE

| Rung | State | Behaviour |
|---|---|---|
| 1 | PRESENT | Ask blocking questions and wait. Batch per SD-IDN-22. |
| 2 | ABSENT | No question can be asked, so no blocking question can be answered. Take the bannered incomplete path in SD-EFF-05 for every field whose blocking input is missing, list every question that would have been asked and what each would have resolved, and emit. Never fabricate an answer, never treat silence as confirmation. Silence defaults to REMOVED, per SD-CNF-04. |

Rung 2 is the correct behaviour for a scheduled or unattended run. It produces a
useful, honest, obviously-unfinished artifact rather than a confident invented
one.

**RUNG 2 COVERS THE BINDING INTERVIEW AS WELL AS THE RUN'S OWN QUESTIONS, AND THAT
IS WORTH SAYING OUT LOUD BECAUSE THE INTERVIEW IS THE FIRST THING A FIRST RUN
DOES.** An ignition interview, a progressive-binding question and an audit prompt
are all questions put to a person, so on this rung none of them fires: every
unbound variable takes its documented default, every question that would have been
asked is listed with the variable it would have bound and what that binding would
have changed, and nothing is written to the organization config, because no
authorized answerer looked at anything. reference/binding-interview.md rule I11 states that
consequence in the interview's own language and points back here; this rung is the
authority where the two ever appear to differ.

---

# PART 3: COMBINATION RULES

Capabilities interact. These rules resolve the combinations that would otherwise
be decided differently by different implementers.

- **P1. SPREADSHEET_WRITE present and SPREADSHEET_INSPECT absent** resolves per
  2.2. It never resolves to a silently unverified workbook.
- **P1b. DOCUMENT_WRITE present and DOCUMENT_INSPECT absent** resolves per 2.2b.
  It never resolves to a silently unverified document, and it never excuses the
  character counts, which are read from text rather than from structure.
- **P1c. A run reads the ladder that matches ITS OWN medium.** OUTPUT_MEDIUM is
  keyed per skill, so a skill emitting xlsx reads 2.1 and 2.2 and a skill emitting
  docx reads 2.2a and 2.2b. A run that reads the other pair reports the wrong
  capability as blocking and degrades a deliverable that was never at risk.
- **P2. CODE_EXECUTION absent** dominates. No ranked list is produced regardless
  of what else is present, because a rank computed by impression is a fabricated
  number, and SD-CNF-07 is not negotiable.
- **P3. NO PRIORITY SOURCE RESOLVED IS A CONCLUSION ABOUT REACHABILITY, NEVER
  ABOUT TWO CHANNEL NAMES BEING ABSENT.** An earlier version of this rule read
  "MAIL absent and DOC_STORE absent means no priority source resolved at all", and
  on a live run it was wrong in the most expensive way available: three priority
  documents were sitting in the input set, readable through FILE_READ, naming
  directives, published period priorities and annual objectives, and a literal
  reading of the rule discarded all of them and labelled the run as built with no
  stated priorities while every one of them was one read away. A run may only
  conclude that no priority source resolved after WALKING THE WHOLE LADDER BELOW
  AND FINDING EACH RUNG EMPTY.

  **THE PRIORITY SOURCE LADDER, IN ORDER. Each rung is attempted; the first rung
  that yields a source is used, and every later rung is still attempted where
  PRIORITY_SOURCES admits more than one kind.**

  | Rung | Source | Available when |
  |---|---|---|
  | 1 | The mailbox sweep, per PRIORITY_SOURCES | MAIL is PRESENT |
  | 2 | The document store, per PRIORITY_SOURCES | DOC_STORE is PRESENT |
  | 3 | **Priority documents SUPPLIED AS FILES in the input set, discovered by CONTENT** | FILE_READ is PRESENT |
  | 4 | Nothing resolved | every rung above returned nothing |

  **RUNG 3, WHICH IS THE RUNG THAT WAS MISSING, AND HOW DISCOVERY BY CONTENT
  WORKS.** Where FILE_READ is present, every readable non-source file in the input
  set is a CANDIDATE priority document. Candidacy is decided by what a file SAYS,
  never by its filename and never by its path: a filename is a hint and is never
  evidence, which is the same discovery discipline SD-SRC-14 already requires of
  every other retrieval in this bundle. A candidate is ADMITTED as a priority
  source when it does three things. A file that fails any of the three is READ AND
  RECORDED AS NOT ADMITTED, with the test it failed named, so a reader can see the
  run looked at it and why it did not count.

  **THE THREE TESTS, AND EACH IS WRITTEN AT THE WIDTH THE EVIDENCE ACTUALLY COMES
  IN AT.** All three were once written narrower than the documents they meet, and a
  test tighter than reality discards real evidence silently, which is the failure
  this whole rung exists to stop.

  1. **IT STATES DIRECTIONS, OBJECTIVES OR PRIORITIES.** What disqualifies a file is
     being a DATA EXTRACT that states none, not merely containing rows. **A document
     that states a direction AND enumerates the units it directs is ADMITTED**, and
     is the ordinary form a supervisor's directive takes: the list is the direction's
     own subject, not evidence that the file is a data extract. The test is what the
     file SAYS it is for, and a file that says nothing about what should be done is
     not a priority source however many rows it holds.
  2. **IT CARRIES OR IMPLIES A PERIOD THAT OVERLAPS THE WINDOW BEING RUN**, resolved
     by the ordinary period rules, **and the run RECORDS THE OVERLAP.** A source
     covering PART of the window is admitted FOR THAT PART, and its scope is stated
     beside anything drawn from it. **The earlier wording said COVERS, and it was
     wrong in both directions**: a set of priorities for one month inside a year being
     reviewed does not cover the year, and a set for a year does not cover one month
     being planned, so a literal run discarded a dated, attributable statement of what
     the organization asked for during the very window it was reporting on. Where a
     source's period does not overlap the window at all, it is NOT ADMITTED and the
     period it does cover is named, because a reader must be able to tell a source that
     was rejected for its date from one that was never found.
  3. **IT IS ATTRIBUTABLE**, to a named person, to a role, to a body, **or to the
     organization itself where the document is plainly a published organizational
     document**. A published set of objectives issued under the organization's own
     name with no individual signatory is attributable and is admitted, with the
     organization recorded as the issuer. What is NOT admitted is a file with no
     issuing identity of any kind, and **an author is never inferred, never assumed
     from a filename and never invented to clear this test**; where none can be read,
     the file is NOT ADMITTED and the test it failed is named.

  **WHAT IS RECORDED FOR EVERY ADMITTED FILE:** its title, its author or issuing
  role, its date, the rung it came in on, and the fact that it arrived as a
  supplied file rather than through a channel. Authority is unchanged by the rung:
  a direction is weighted by WHO issued it under PRIORITY_SOURCES, never by HOW it
  reached the run. A rung-3 document from a manager in the chain is a directive
  exactly as the same document would be in the mailbox.

  **ONLY WHERE ALL THREE RUNGS RETURN NOTHING** does the run conclude that no
  priority source resolved. The ranked list still ships, computed on the measure
  and the resolved signals alone, labelled as built with no stated priorities. It
  is never labelled "no priorities this period", because the run looked for
  priorities and did not find them, which is not the same as an organization
  having none.

- **P3b. A run that had FILE_READ PRESENT and did not attempt rung 3 has
  MISLABELLED ITSELF**, whatever it printed. The label "built with no stated
  priorities" asserts that the ladder was walked. Where rung 3 was skipped, the
  correct statement is that priorities were not looked for in the input set, and
  the run says that instead.
- **P4. INTERACTIVE absent and DIRECTORY absent** means role and scope come from
  the file alone. Use ROLE_FALLBACK_KEY, which is bound to the narrowest role so
  that an unknown never inflates a claim or a list size.
- **P5. FILE_WRITE absent and the record count is large** means no fan-out and no
  resumability. Announce the estimated duration before starting, per SD-CTR-17,
  because the user cannot resume if it fails.
- **P6. Any capability DEGRADED mid-run** updates the probe record and appends a
  degradation line. A capability that was PRESENT at probe time and fails during
  the run is worked through the graduated retry ladder in SD-EFF-09 first. It is
  marked DEGRADED only after the ladder is exhausted, because SD-EFF-10 says an
  empty read is unconfirmed rather than failed.
- **P7. Two capabilities missing never compound into silence.** Each is announced
  separately, with its own effect named. A single line saying "some things were
  unavailable" is not an announcement.

---

# PART 4: THE ANNOUNCEMENT RULE

**A degraded run must announce its degradation in the output rather than silently
producing less.**

## 4.1 Where it is announced

Three places, all of them, every time:

1. **The front panel of the artifact.** A named section, before the content,
   carrying a LEADING COUNT LINE and then ONE LINE PER DEGRADED CAPABILITY. Each
   of those per-capability lines names all three things 4.2 requires, compressed
   into one line rather than expanded into a paragraph. **THE COUNT LINE DOES NOT
   REPLACE THE PER-CAPABILITY LINES, AND THIS IS STATED HERE BECAUSE TWO FILES
   READ IT TWO WAYS.** A panel carrying only a count and the single most
   consequential effect drops the "what the reader should do" statement for every
   degradation but one, which 4.2 calls non-compliant; a panel carrying eight
   paragraphs pushes the content the reader came for onto a later page. One line
   each, all three parts on it, plus the count above them, satisfies both and is
   the form. Where a skill's own panel ordering says otherwise, THIS FILE GOVERNS
   and that ordering is stale.
2. **The audit section of the artifact.** The probe record in full: every
   capability, its state, the evidence, the rung taken, and the alternatives tried
   before the rung was taken. **THE FULL PER-CAPABILITY DETAIL LIVES HERE AND NOT
   ON THE PANEL**, which is what keeps the panel to one line each without losing
   anything: the panel is the notice, the audit is the record.
3. **The first line of the reply.** One line naming the count and the single
   most consequential effect.

The artifact is the copy that survives. A degradation announced only in chat is
not announced.

## 4.2 What the announcement says

Each line names three things, in this order: what was unavailable, what it
changed, and what the reader should do about it. Never only the first.

**THE THREE PARTS ARE WHAT THE LINE MUST SAY, NOT HOW MUCH ROOM IT TAKES.** On the
front panel each degradation is ONE line carrying all three parts; the examples
below are shown wrapped for reading and are one line each in the artifact. The
expanded form, with the probe evidence and the alternatives tried, belongs in the
audit section under 4.1 place 2.

Sufficient:

> The mailbox could not be reached, so no supervisor priorities were read. The
> ranking below uses the measure and the published signals only. Priorities set
> by your manager this period are not reflected.

> A named attachment from your manager could not be opened after four retrieval
> paths. The directed list below is therefore incomplete. The file was called
> {filename}, sent {date}.

> Formatting could not be verified in this environment, so the workbook is
> published unverified. Every number is complete; the presentation may be
> inconsistent between sections.

Not sufficient:

> Some sources were unavailable.

> Note: reduced functionality.

> Best effort.

## 4.3 The wording of MSG_DEGRADED_RUN

The bound message carries two slots, and both are filled: the missing capability
by name, and the effect on the output. A message that names one without the
other is not compliant.

## 4.4 What a degraded run may never do

- It may never present the degraded output as complete.
- It may never fill a gap with an estimate, an average, a plausible value or a
  value carried over from a previous run.
- It may never silently widen a population, a scope or a claim to compensate for
  a missing filter. SD-QUA-12 applies to a missing capability exactly as it
  applies to a missing column.
- It may never omit a section because the capability that populated it was
  absent. The section ships with its explanatory row naming the capability.
- It may never downgrade its own announcement between runs. A degradation
  announced last run and still present is announced again, at the same
  prominence.
- It may never let a degraded number ship at full claim strength. Where the
  missing capability was the counterfactual denominator's source, every affected
  claim drops to bounded phrasing, per reference/binding-interview.md Part 5, section 5.2
  step 6, and reference/schema/ SECTION B, final bullet.

## 4.5 The self-check

Before publication, the run answers one question and records the answer:

> If a reader opened this artifact six months from now with no memory of the
> conversation, could they tell from the artifact alone which parts of it were
> produced with less than the full method, and what that cost them?

If the answer is no, the announcement is not finished.


---

# CHANGE LOG: ACCEPTANCE TEST REMEDIATION

Three corrections after two hostile acceptance tests.

1. **An invented hard gate, deleted.** The document-store ladder at 2.11 rung 3
   declared a stop for the review skill where a required reference had no cached
   equivalent dated within the current period. That condition appears in no
   enumeration of the stop list, contradicts SD-SRC-18 four screens earlier in the
   same citation chain, and would stop every review run at a company that has just
   bound the bundle and therefore has no cached blocks at all. SD-EFF-02 exists
   specifically to prevent an implementer inventing a stop condition, and this
   file had invented one. The rung now continues, degrades, and announces.
   Reported as report 1 D13 and report 2 D11.
2. **A cross-reference corrected.** 4.4's final bullet pointed at
   reference/binding-interview.md Part 3, which is the Stage 3 full audit and says nothing
   about claim strength. The rule is Part 5, section 5.2 step 6. Reported as
   report 1 D15 and report 2 D13.
3. **A binding invoked by description now has a name.** 2.2 resolved the
   workbook-versus-markdown choice by appealing to "a business that has said its
   deliverable must be a workbook", which was not a bound variable anywhere. That
   is precisely what standing rule S1 exists to prevent. It is now
   DELIVERABLE_CONTAINER_REQUIRED, defined in reference/schema/ Group 15 with a
   documented default of false and a degradation notice. Reported as report 1 D18.

## Later pass, the front-panel form of the degradation block

4. **4.1 place 1 now states the FORM of the block and not only its existence.**
   This file required each degradation on its own line naming three things, and a
   skill's own front-panel ordering required the block to be a count and the single
   most consequential effect. Both are individually reasonable and they cannot both
   be obeyed: a literal implementer of one writes eight paragraphs onto the panel,
   a literal implementer of the other writes one line and loses seven of the eight
   statements of what the reader should do, which 4.2 already calls non-compliant.
   One run satisfied both by inventing a compromise and recorded that nothing
   authorized it. The form is now stated once, here: a leading count line, then ONE
   line per degraded capability carrying all three parts, with the full
   per-capability record in the audit section rather than on the panel. Where a
   skill's panel ordering disagrees, this file governs and that ordering is stale.
5. **4.2 now says that the three parts are what the line SAYS, not how much room it
   takes.** Its sufficient examples are shown wrapped and were read as licensing a
   paragraph each on the panel.

## Later pass, the three admission tests of the supplied-file rung

1. **P3 rung 3's period test now reads OVERLAPS rather than COVERS, and the overlap
   is recorded.** A set of production priorities for one month inside a year being
   reviewed does not COVER the year, so a literal run recorded a dated, attributable
   statement of what the organization asked for during the window as READ AND NOT
   ADMITTED, and lost it. The same wording bites the other way on a planning run,
   where a source covering the year fails a run over one month. A source is now
   admitted for the PART of the window it covers, with its scope stated beside
   anything drawn from it, and a source whose period does not overlap at all is still
   refused with the period it does cover named.
2. **The direction test now disqualifies a DATA EXTRACT, not a document that carries
   a list.** It read "states directions rather than holding rows of units", which
   refuses a supervisor's directive naming the accounts it directs, which is the
   commonest shape a real directive has. The list is the direction's own subject.
3. **The attribution test admits a document issued under the organization's own
   name.** A published set of objectives with no individual signatory was
   unattributable under the old wording and is attributable now, with the
   organization recorded as the issuer. An author is still never inferred, never
   read off a filename and never invented to clear the test.
4. **All three were narrower than the documents they meet, and that is recorded as
   one finding rather than three**, because the failure mode is shared: a test written
   tighter than reality discards real evidence silently, which is precisely what the
   rung above it exists to prevent.
