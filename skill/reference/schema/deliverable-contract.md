# GROUP 15: THE DELIVERABLE CONTRACT

TAXONOMY SHAPE, DELIVERABLE_LINES. Exactly two entries and no others. Each
carries `key`, `display_name`, `tier_1_size`, `tier_2_size`, `reference_cap`,
and `roles`. The two lines are identical in every respect except those three
counts. The action list gets SHORTER as scope widens.

TAXONOMY SHAPE, TAB_CONTRACT. An ordered list of output sections. Each carries
`key`, `title_variable`, `family` (identity_and_rank, mandatory, merit,
reference, derived, exception, panel), `capped_at`, and `empty_message_variable`.
Every section ships every run, in this order, even with nothing to report.

**THE SHEET-NAME CONSTRAINT, STATED ONCE HERE AND CITED FROM EVERY VARIABLE THAT
CAN REACH A SHEET NAME.** A section title is not only a heading: where the output
medium is a workbook, the section's title variable BECOMES THE SHEET NAME, and a
sheet name is one of the few strings in this bundle that a container engine can
REJECT OUTRIGHT. A string that is merely long or merely punctuated is a heading a
reader shrugs at and a file that will not open.

Every value that can become a sheet name satisfies all four, tested at BINDING time
and not at build time:

1. **LENGTH: 31 characters or fewer**, counted after any prefix or suffix the run
   composes onto it.
2. **CHARACTER SET: none of the six forbidden characters**, which are the colon,
   the backslash, the forward slash, the question mark, the asterisk, and either
   square bracket. Also not empty, and not beginning or ending with an apostrophe.
3. **UNIQUENESS within the workbook**, compared case-insensitively, because the
   engines that reject a duplicate do not distinguish case.
4. **STABILITY between runs**, so two periods of the same report can be compared
   sheet by sheet.

**THE TRUNCATION RULE, WHICH IS STATED SO THAT TWO RUNS TRUNCATE IDENTICALLY.**
Where a BOUND value violates the constraint, the run does not fail and does not
choose for itself. In this order: replace every forbidden character with a single
space; collapse runs of spaces and trim; if the result still exceeds 31 characters,
cut to 28 and append three full stops; if that collides with a sheet name already
placed, cut to 29 and append a space and the smallest integer that makes it unique.
The rename is DISCLOSED in the method section with the original value beside it, and
the binding owner is asked to bind a legal one, because a truncated title is a
degraded title however deterministic the truncation.

**THE VARIABLES THIS REACHES, AND EVERY DEFAULT BELOW HAS BEEN CHECKED AGAINST IT:**
every TAB_CONTRACT `title_variable`; MANDATORY_SECTION_LABEL, which is the one whose
documented default failed the constraint and is now legal as written;
UNIT_NOUN_SINGULAR and UNIT_NOUN_PLURAL wherever a sheet name composes off them; and
any section heading a skill declares in place of a bound title. PANEL_SECTION_HEADINGS
are headings WITHIN a sheet and are not reached by this constraint; they are named
here so the next reader does not have to work that out twice.

**A SHEET NAME IS A HEADING AND IS WRITTEN IN THE TITLE CASE CONVENTION**, per
TITLE_CASE_HEADINGS and SD-FMT-13, which is a separate requirement from this
constraint and is checked alongside it. The one string this does not reach is a name
the ORGANIZATION BOUND, which ships in the case it was bound in; every default and
every name the method composes is written in Title Case where it is documented, so
the run never re-cases a sheet name and the stability comparison between periods is
unaffected in either case.


| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| DELIVERABLE_LINES | The two deliverable shapes and their three sizes. | ORG | DEFERRED | taxonomy | Exactly 2 entries. The senior line's absolute tier sizes are the LARGER pair, and the action list is never proportional to span: it grows far more slowly than the span it covers, so it gets shorter RELATIVE TO SPAN as scope widens. See SD-RNK-09. | line_a 10 and 25; line_b 20 and 50 |
| REFERENCE_CAP | Maximum rows on the reference section and on every auxiliary capped section. | ORG | DEFERRED | scalar | Positive integer. Counts rows on the section, never positions in the ranked list. | 500 |
| USER_SIZE_TIER_1_FRACTION | The share of a user-requested size that goes to the first tier, rounded up. | ORG | DEFERRED | scalar | Fraction between 0 and 1. | 0.3333 |
| USER_SIZE_OVERRIDE_ALLOWED | Whether a user-requested list size overrides the role default. | ORG | DEFERRED | scalar | Boolean. Every cap and gate stays unchanged; only the counts move. | true |
| TAB_CONTRACT | The ordered output sections, **PER SKILL**. A keyed set: one ordered section list per skill that produces a document, never one list shared across them. | ORG | DEFERRED | taxonomy | Keyed by skill. At least 4 sections per skill. Order fixed within a skill. Every section has an empty message. **A default that names one skill's sections is not a default for the others: it is that skill's contract wearing a shared name.** | keyed: planning, review and scorecard, each with its own ordered list; see the SECTION A1 default |
| IDENTITY_BLOCK_COLUMNS | The columns present, in the same order, on every item section. | ORG | DEFERRED | list | At least 3 entries. Verified by header NAME and relative order, never by fixed column number. | Rank; Unit ID; Unit Name; Address; City; Jurisdiction; Postal; Parent Group; Measure |
| IDENTITY_BLOCK_ANCHOR_COLUMN | The column after which the freeze point is computed. | ORG | DEFERRED | scalar | Must be a member of IDENTITY_BLOCK_COLUMNS. The freeze cell is computed, never hard-coded. **It is DERIVED from FROZEN_SPAN_MAX_WIDTH by the walk the output contract states, rather than chosen: the last identity column whose inclusion keeps the summed built width at or under the bound.** | Jurisdiction |
| FROZEN_SPAN_MAX_WIDTH | The maximum TOTAL BUILT WIDTH of the frozen span, in the same width unit column widths are set in. A bound on the span, never on one column and never on the sheet. | ORG | DEFERRED | scalar | Positive number, and small enough that the frozen span cannot fill an ordinary window, because a span wide enough to do that keeps everything on screen rather than the identity: it costs the reader the scroll and saves nothing. The first identity column is frozen even where it alone exceeds the bound. | 55 |
| GRID_MAX_TOTAL_WIDTH | The maximum SUMMED BUILT WIDTH of every column of one entity sheet or reference table, in the SAME width unit column widths are set in and FROZEN_SPAN_MAX_WIDTH is expressed in. It binds a SHEET, never a column and never a workbook. **IT IS THE SECOND OF TWO BOUNDS AND NEITHER SUBSTITUTES FOR THE OTHER:** FROZEN_SPAN_MAX_WIDTH says what stays on screen, this one says how much there is, and a sheet can honour the first perfectly and still be ten screens wide. | ORG | DEFERRED | scalar | Positive number, in the same width unit as FROZEN_SPAN_MAX_WIDTH. **BOUNDED ON BOTH SIDES, because a one-sided bound is not a bound.** Above: strictly less than 659, which is the narrowest total this bundle has measured a reader failing to traverse. Below: greater than the summed built width of the columns a sheet cannot avoid carrying, which is at least NARRATIVE_WIDTH_MAX_UNITS plus the built identity block, or the bound is unreachable by construction and every sheet ships over it. **DECLARED BEFORE THE COLUMNS ARE BUILT, never after the measurement**: a run never raises it to clear a grid that failed it, exactly as HEADER_MAX_LINES is never raised to clear a failing header, and a bound discovered after the measurement is not a bound. The relief ladder that runs when a sheet exceeds it, and the three things that never give while that ladder runs, are stated once in reference/output-contract.md PART 2.7 and are not restated here. | 500 |
| SPAN_BLOCK_POSITION | Where the span-of-control columns sit inside the identity block. | ORG | DEFERRED | scalar | Names two adjacent columns that BOTH appear in IDENTITY_BLOCK_COLUMNS, and the position must be consistent with that list, which is the authority on column order where the two disagree. | between Unit ID and Unit Name |
| SCOPE_RANK_HEADER | The header string for rank within the requester's scope. | ORG | DEFERRED | scalar | The same string at every scope level. Never retitled per level. | Scope rank |
| SCORE_COLUMN_REQUIRED | Whether the number the list was ranked on is published. | ORG | DEFERRED | scalar | Boolean. Must be true. | true |
| SCORE_DECIMAL_PLACES | The FLOOR on the decimal places carried by the published score. | ORG | DEFERRED | scalar | Integer 1 to 4, **AND IT IS A FLOOR THAT THE RUN COMPUTES UPWARD FROM, NOT THE PRECISION ITSELF.** Stated this way because the correct precision is DATA-DEPENDENT and a fixed number cannot be it: per S5, a threshold computable from the data in hand is computed from the data in hand and a bound value is the floor. **THE COMPUTATION:** the run raises precision above this floor until no two rows carrying DIFFERENT real scores print alike, because two rows that print one number and rank differently is a report contradicting itself on its own face, and the reader cannot tell a tie from a rounding. It never prints fewer places than the floor, and where the computed precision exceeds 4 it is still applied and the method section says so, since the alternative is a printed tie that is not a tie. Both the floor and the precision actually used are printed in the method section. | 2 |
| UNRESOLVED_COLUMN_TREATMENT | What happens to a column whose source does not resolve. | ORG | DEFERRED | scalar | Must be write_blank_keep_header. Dropping the column changes the shape and is a contract violation. | write_blank_keep_header |
| OUTPUT_FILENAME_PATTERN | The filename pattern for the emitted artifact. | ORG | DEFERRED | scalar | Must carry a scope label, its identifying code, the period, and any qualifier, so two runs never collide. | {ScopeLabel} {ScopeCode} {Period} {DeliverableName} |
| DELIVERABLE_NAME | The human name of the artifact, **PER SKILL**. A mapping from skill to name, never a single string. | ORG | DEFERRED | mapping | Keyed by skill. Non-empty per entry. A single string is REJECTED AT VALIDATION, because one artifact name across three different documents titles two of them wrongly. | keyed: one name per skill; see the SECTION A1 default |
| DELIVERABLE_CONTAINER_REQUIRED | Whether this organization requires the deliverable in a specific container, so that a run which cannot verify that container's formatting publishes it labelled rather than falling back to structured markdown. | ORG | DEFERRED | scalar | Boolean. | false |
| OUTPUT_DIR | Directory variable for published artifacts. | ORG | DEFERRED | scalar | A variable name, never a live path. | OUTPUT_DIR |
| UPLOAD_DIR | Directory variable where supplied source files are found. | ORG | DEFERRED | scalar | A variable name. | UPLOAD_DIR |
| SCRATCH_DIR | Directory variable for checkpoints and working files. | ORG | DEFERRED | scalar | Must never equal OUTPUT_DIR. | SCRATCH_DIR |
| CHAT_REPLY_MAX_LINES | Ceiling on the conversational reply that accompanies an artifact. | ORG | DEFERRED | scalar | Integer between 4 and 12. The full list is never pasted. | 8 |
| SUBMISSION_BOUNDARY_BANNER | The banner separating content for the destination system from content that must never travel into it. | ORG | DEFERRED | scalar | Non-empty. | ----- NOT FOR SUBMISSION ----- |
| BANNED_HEADINGS | Headings with no counterpart on the live destination form, which must never enter the submitted body. | ORG | DEFERRED | list | May be empty. SEED, extended when a prior document introduces one. | Organization Impact |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 15: The deliverable contract

| Variable | Documented default | Degradation notice |
|---|---|---|
| DELIVERABLE_LINES | Direct tier 10 plus 25; aggregate tier 20 plus 50. The senior pair is larger in absolute rows and far smaller as a share of the span it covers, which is the point. | List sizes have not been set for your organization, so the standing sizes were used. The action list is never proportional to span: it grows far more slowly than the span it covers, so a wider scope receives a list that is a much smaller share of what it owns. |
| REFERENCE_CAP | 500. | The standing reference depth was used. |
| USER_SIZE_TIER_1_FRACTION | One third, rounded up. | The standing split was used when you asked for a specific list size. |
| USER_SIZE_OVERRIDE_ALLOWED | true. | A requested list size overrides the default, which is the standing setting. |
| TAB_CONTRACT | **EACH SECTION NAME BELOW IS WRITTEN IN THE TITLE CASE CONVENTION OF TITLE_CASE_HEADINGS, because a section name becomes a SHEET NAME under the Group 15 constraint and a sheet name is a heading. PER SKILL, because the sections of a plan, a review and a scorecard are not the same sections. EACH LIST BELOW IS THE SECTION LIST ITS OWN SKILL DECLARES, IN THAT SKILL'S OWN ORDER, AND THAT IS THE TEST THIS ROW MUST PASS: a default that names sections the skill does not build, or names them in another order, silently builds a different artifact than the same skill builds when the variable is unbound and read from the skill instead.** PLANNING, nine sections: Front Panel; Priorities; Directed; First Action List; Second Action List; Reference List; Breadth; Exceptions; Method. REVIEW, eight sections, which are the DOCUMENT'S own sections and never the destination form's fields: Front Panel; Degradation Block; Field Index; Copy Region; Focus; Items to Verify; Method; Contact. The incomplete banner is not a section: it is a conditional banner that sits above everything when it fires. SCORECARD, six sections: Front Panel; Priority Fixes; Scorecard Census; Summary by Requirement; Reason-Code Legend; Method. **THE SCORECARD LIST HAS NO EXCEPTIONS SECTION AND THAT IS DELIBERATE, NOT AN OMISSION.** An earlier version of this default carried a seventh scorecard section for exceptions and put the census before the worklist, both of which contradicted the skill; a run that resolved this variable and a run that read the skill built different workbooks. The exception content is not lost: the material items sit on the front panel and the full enumeration sits in the method section, both of which a reader reaches sooner. Each list is fixed in order WITHIN its skill, and every section carries its empty message. | The section list has not been set for your organization, so the standing set FOR THE SKILL THAT RAN was used, in its standing order. The sections of a plan, a review and a scorecard differ because the documents differ; a run never inherits another skill's section list, and the standing list for each skill is the list that skill itself declares. |
| IDENTITY_BLOCK_COLUMNS | Rank, unit identifier, unit name, and every scope column finer than yours that carries more than one value. | The identity columns have not been set, so a minimal set was used: whatever identifies a unit in your file, plus the levels below you. |
| FROZEN_SPAN_MAX_WIDTH | 55 built width units. | No bound was set on how wide the frozen span may be, so a standing one was used. It exists because a workbook built entirely to contract came out about ten screens wide, and freezing its whole identity block pinned every column on the sheet: scrolling right reached nothing and the sheet could not be read. Where your identity block is narrower than the bound, nothing changes and the whole block is frozen. |
| GRID_MAX_TOTAL_WIDTH | **500 built width units, and the arithmetic that produced it is stated here so that nobody moves the number blind.** A 22-column census sheet measured 486.43 units once the relief ladder had run, with its trailing narrative column at 100; the same grid before the ladder measured 813.71. Two real workbooks failed a reader outright at 659 and at 749.12. So 500 clears a well-built grid with 13.57 units to spare and fails every bloated grid on record, which is exactly the discrimination the bound exists to make. **A BOUND SET SO HIGH THAT NOTHING EVER TRIPS IT IS NOT A BOUND**, and a bound set below 486.43 would fail a sheet that was built correctly, so the window this number can honestly sit in is about forty units wide and it sits deliberately near the bottom of it. | No bound was set on how wide a whole grid may be, so a standing one was used. It is not a preference: a grid nobody can traverse hides the relationships between its columns, which is most of the reason it is a grid. Where a sheet exceeded the bound, the relief ladder ran before publication and no column was dropped, no width went below its own header floor, and no value that carries meaning was shortened. Where the sheet was still over the bound afterwards it shipped over it and said so: the method section records the bound, the measured total, the overage and the columns that account for it, and the front panel tells the reader that this sheet is wider than the bound and that the freeze and the filter are how it is meant to be read. |
| IDENTITY_BLOCK_ANCHOR_COLUMN | **The last identity column BEFORE HDR_RANK_REASON.** Not the last identity column outright: HDR_RANK_REASON is itself the last column of the identity block, so an anchor defined as the last identity column IS the reason column, the freeze point computed one column after it puts the reason INSIDE the frozen span, and the verification asserting that the reason sits after the anchor then fails on every correctly built sheet. There is no assignment of the anchor that satisfies all three statements, and this is the one that does: anchor on the last identity column before the reason, so the freeze lands on the reason's own column and no free-text column is ever frozen. | The freeze point was computed from the resolved identity block rather than from a named column: it sits at the reason-for-rank column, so the identifying columns before it stay on screen and the free-text column that follows them scrolls. |
| SPAN_BLOCK_POSITION | Immediately after the unit name, which is where IDENTITY_BLOCK_COLUMNS places the scope columns. Where the two ever disagree, IDENTITY_BLOCK_COLUMNS governs, because it is the list the identity block is built from. | The standing position was used for the attribution columns. Where the only level finer than the reader's own IS the unit level, there is no attribution column to add and the span block is empty, which is stated rather than filled with a copy of the identifier. |
| SCOPE_RANK_HEADER | The literal string "Scope rank". | The standing header was used, and it is the same string at every level so two reports can be compared. |
| SCORE_COLUMN_REQUIRED | true. | The number the list was ranked on is always published, which is the only permitted setting. |
| SCORE_DECIMAL_PLACES | 2, as a FLOOR. The run computes upward from it and prints whatever precision is needed for no two different scores to print alike. | The standing precision floor was used, and the precision actually printed was computed from your own scores: it is raised above the floor wherever two rows with different scores would otherwise print the same number, which would make a rank look arbitrary. The floor and the precision used are both printed in the method section. |
| UNRESOLVED_COLUMN_TREATMENT | write_blank_keep_header. | A column whose source did not resolve is written blank with its header present, which is the only permitted setting, and each one is named in the audit. |
| OUTPUT_FILENAME_PATTERN | Scope label, scope code, period, deliverable name. | The standing filename pattern was used so two runs at different scopes do not collide. |
| DELIVERABLE_NAME | **PER SKILL:** the planning artifact is a "Work Plan"; the review artifact is a "Performance Review"; the scorecard artifact is a "Requirement Scorecard". Each is generic and none names an industry, a level or a role. | The report has not been given a name for your organization, so the generic name FOR THE SKILL THAT RAN is used in the filename and the title band. A run never inherits another skill's artifact name, which would title a scorecard as a work plan. |
| DELIVERABLE_CONTAINER_REQUIRED | false. Where formatting cannot be verified, the report is delivered as structured markdown carrying identical information rather than as an unverified workbook. | No container requirement has been set, so where the formatting of a workbook could not be verified this report was delivered as structured markdown instead. Nothing was dropped: the sections, their order, the columns, the headers, the ranks, the caps and the audit trail are all present. |
| OUTPUT_DIR | The session output directory. | The standing output location was used. |
| UPLOAD_DIR | The session upload directory. | The standing input location was searched. |
| SCRATCH_DIR | The session scratch directory. | The standing working location was used, and no working file was written near your outputs. |
| CHAT_REPLY_MAX_LINES | 8. | The standing reply length was used; the full list is in the file, never pasted into the reply. |
| SUBMISSION_BOUNDARY_BANNER | The literal line of hyphens reading NOT FOR SUBMISSION. | The standing banner was used to separate content meant for a destination system from content that must not travel into it. |
| BANNED_HEADINGS | Empty. | No banned headings have been recorded, so this report cannot warn you if a heading it produced has no counterpart on your live form. Check the section names against the form before submitting. |
