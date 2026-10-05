# GROUP 26: RECURRING DELIVERY

The variables the RECURRING BRIEFING workflow needs. Nothing here is read by PLANNING,
REVIEW or SCORECARD, and nothing those three read is redefined here.

**That sentence reads against `reference/schema/README.md`, which opens "One config, three
skills. Nothing in this file is skill-specific." It is worth saying plainly that this group
is not what breaks that claim.** Group 19 binds one section of the planning spreadsheet and
Group 20 binds a review form's sections, scale and prompts; neither is read by anything but
its own workflow and neither says so. This group is the third of its kind and the first to
declare it. The claim also predates the split of the schema into separate files, so "this
file" no longer names what the claim is about. The accurate version is stronger than the
one it replaces and survives a fourth workflow without an edit: one config, no variable
defined in two groups, a group MAY be specific to one workflow and says so in its own
opening line, and every workflow reads the same bound value for every group it reads. See
work/router-and-doctrine-audit.md, finding H.

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| DELIVERY_PERIOD | The unit of work one briefing covers, named as the business names it. | ORG | DEFERRED | scalar | A singular noun denoting a recurring unit shorter than PLANNING_PERIOD_LENGTH_DAYS. A value equal to or longer than the planning period is REJECTED at validation: a briefing that covers the whole plan is the plan, and this workflow is not the plan. | working day |
| DELIVERY_PERIOD_DAYS | Which days of the week carry a delivery. | ORG | DEFERRED | list | A non-empty subset of the seven days. Days outside it get no send and no notice. | Monday; Tuesday; Wednesday; Thursday; Friday |
| REBUILD_PERIOD | How often per-item content is rebuilt from source. | ORG | DEFERRED | scalar | Strictly longer than DELIVERY_PERIOD. Placed on a day outside DELIVERY_PERIOD_DAYS where one exists, so a rebuild never competes with a send. | weekly, on Saturday |
| DELIVERY_TIME | The local clock time the recipient wants the briefing in hand. | PERSON | DEFERRED | scalar | A time of day in the recipient's own zone. Taken from the recipient's own sentence, never proposed. Same rule and same reason as PERSON_PREFERRED_LIST_SIZE in PART 4's optional follow-ups, which is never asked and is bound only when a user states it. Run time, poll deadline and expected delivery are DERIVED from it and all three are stated back before any schedule is created. | 5:00 AM |
| DELIVERY_FEED_WAIT_MINUTES | How long the delivery loop polls for the period's schedule feed before falling back. | ORG | DEFERRED | scalar | A positive integer strictly less than the gap between run time and expected delivery. A value that would push delivery past the recipient's stated time is REJECTED: late and complete is worse than on time and labelled. | 28 |
| BRIEFING_RECIPIENT | The one person a briefing is sent to. | PERSON | DEFERRED | scalar | Exactly one address, and it is the address of the person who set the briefing up. A list, a shared mailbox, a supervisor or an address supplied in a later request is REJECTED, not merged. See SD-CTR-18 and the carve-out in the workflow's A5.1. | the recipient's own work address |
| BRIEFING_SCOPE | The population of items a briefing may draw from. | PERSON | **DERIVED** | scalar | **Never asked.** DERIVED from the person-tier scope the person script already bound at Q-PERSON-2, narrowed to the recipient's own work. Asking it again violates I2, and PART 4 opens by promising four questions and no more. Where no person scope exists at all, the PERSON SCRIPT runs; this workflow does not substitute a question of its own. A scope including another named person's items is REJECTED. See SD-SPN-01, SD-IDN-03. | derived from the recipient's bound scope |
| SCHEDULE_FEED_SHAPE | The fields the standing schedule feed must carry for a briefing to be assemblable. | ORG | DEFERRED | taxonomy | Per field: concept name, whether required, and what the briefing loses without it. Must include an item identifier, an item name, a scheduled date and an owner. A planned start time is OPTIONAL and its absence costs the within-period ordering, which is then stated. | identifier; name; scheduled date; owner; planned start time (optional) |
| ITEM_IDENTIFIER | The concept that identifies one item of work across every source. | ORG | DEFERRED | scalar | Resolved by concept and never by column header. Near-unique in every source that carries it. An input whose identifier does not join at or above JOIN_OVERLAP_FLOOR is staged and reported, never joined. See SD-PRS-25, SD-PRS-31. | account number |
| BRIEFING_SOURCES | The sources that feed per-item content, each with where it lives and how it is recognized. | ORG | DEFERRED | taxonomy | Per source: concept name, location, the column signature that recognizes it, and whether it is required. Recognition is by signature, never by filename. See SD-SRC-14, SD-PRS-25. | the period plan (required); the gap export; the target list; the audit output |
| SOURCE_FRESHNESS_STATES | The five states a source may carry on a given rebuild. | ORG | DEFERRED | taxonomy | EXACTLY five: CURRENT, CARRIED, ABSENT, UNRESOLVED, DRIFTED. Per state: `is_current`, `permits_assertion`, `label_in_artifact`, `requires_named_source`, `announce_by`. Fewer is REJECTED: collapsing ABSENT into UNRESOLVED loses who must act; collapsing CARRIED into CURRENT is the defect this workflow exists to prevent; and dropping DRIFTED loses the only failure a healthy, parsed, on-time file can carry. DRIFTED alone sets `announce_by` to banner, and it is the one state that coexists with another on the same source. See SD-EFF-06, F0.1, F5.5. | the five standing states |
| PREVIOUS_RESOLUTION_RECORD | Per source, the concept-to-column resolution recorded at the last rebuild, which rung 0 compares against. | ORG | DEFERRED | mapping | One entry per source per concept. Written by every rebuild, read by the next. Absent on a first rebuild, which is why no source can be DRIFTED on one. | schedule feed: planned start -> "Planned Start Time" |
| DRIFT_ANNOUNCE_SCOPE | Whether a drift banner names the affected source only, or every source. | ORG | DEFERRED | scalar | One of: source, all. Defaults to source. Must never resolve to a per-line label, which is G-RB-9. | source |
| STEM_PROPOSAL_SINK | Where a stem meeting field-resolution 7.5 criterion 5 is proposed. | ORG | DEFERRED | scalar | Must name the unbound-value queue or an equivalent the binding owner reads. **Never the organization config**: a scheduled rebuild is INTERACTIVE ABSENT and 7.5 makes promotion an ORG-tier act. | the unbound-value queue |
| NAMED_ABSENCE_STRINGS | What a line says when its source is ABSENT, one string per source. | ORG | DEFERRED | mapping | One entry per member of BRIEFING_SOURCES. Every string names the source that is missing. A blank, a zero, a dash or a generic "not available" is REJECTED: zero is a legitimate value and a reader cannot tell it from a gap. See SD-CNF-07. | "Not in the gap export"; "No target list for this period" |
| CARRIED_SOURCE_TRIPWIRE | How many sources may sit in CARRIED before the whole briefing is bannered rather than labelled per line. | ORG | DEFERRED | scalar | A positive integer, or a proportion of BRIEFING_SOURCES. Computed from the count in hand where one is bound, per S5. | 2 |
| BRIEFING_ITEM_SECTIONS | The per-item content standard: which sections appear, in which order. | ORG | DEFERRED | taxonomy | Per section: name, order, source, and whether it is suppressed when empty. The identity header is never suppressed. The final section is always the short action list, and every entry in it cites a section above it. See SD-CTR-14. | header; gaps; programs; business; competition; do this |
| BRIEFING_ACTION_CAP | The most actions one item may carry. | ORG | DEFERRED | scalar | A positive integer. A briefing that lists everything lists nothing, and the cap is what forces the ranking to happen before the send rather than in the reader's head at 5 AM. | 6 |
| MESSAGE_MAX_WIDTH | The maximum rendered width of a briefing. | ORG | DEFERRED | scalar | A positive integer in the medium's own unit. Validated as legible on a phone held in one hand. | 640 |
| MESSAGE_BODY_SIZE | The body text size of a briefing. | ORG | DEFERRED | scalar | A positive integer in the medium's own unit, at or above the platform's accessible minimum. | 15 |
| BRIEFING_SUBJECT_SHAPE | What the subject line carries, so it is useful unopened. | ORG | DEFERRED | taxonomy | Must carry the period and the item count. Should carry a geographic or sequence anchor. A subject that is constant across periods is REJECTED: an unopened constant subject is indistinguishable from a stuck job. See SD-CTR-09, which binds the HEADER strings and not this. | period; item count; first and last location |
| DATE_FORMAT_DAY | The one rendering of a day-precision date anywhere a reader sees it. | ORG | DEFERRED | scalar | **This validation is the single statement of the date convention for this bundle's message medium, per the precedent SD-FMT-13 sets for its own convention: a convention written twice is two conventions, so element M13 and the workflow's Part J cite this row and do not restate it.** THE CONVENTION, IN THREE PARTS. ONE, one format per precision, and three precisions exist: this variable for a day, `DATE_FORMAT_MONTH` for a month, `DATE_FORMAT_WEEKDAY` for the subject and the title. TWO, the format for a precision reaches EVERY date of that precision in the message, including the ones inside sentences, inside freshness labels and inside the footer; a second rendering of one precision appearing anywhere in the same message is REJECTED at validation rather than warned about, because the comparison a briefing exists to support is a comparison between dates and a reader cannot make it quickly across two formats. THREE, **a date is never rendered at a finer precision than its source carries**, which makes giving a month-only value a day a G3 violation rather than a formatting choice, and is the one part of this convention that gates a send. All-numeric forms are rejected as the bound value: 06/10/2026 is two different dates depending on who reads it, and a briefing has no reader present to ask. | 6 October 2026 |
| DATE_FORMAT_MONTH | The one rendering of a date whose source carries a month and no day. | ORG | DEFERRED | scalar | One format, carrying a month and a year and no day. Governed by the convention stated at `DATE_FORMAT_DAY` and not restated here; part three of it is what forbids rendering a month-precision value with a day. | April 2027 |
| DATE_FORMAT_WEEKDAY | The rendering used in the subject and the title, where the reader is orienting by weekday. | ORG | DEFERRED | scalar | `DATE_FORMAT_DAY` with the weekday name prefixed. Governed by the convention stated at `DATE_FORMAT_DAY` and not restated here. Permitted in the subject and the title only; in body text it is a second day-precision rendering, which part two of that convention rejects. | Tuesday 6 October 2026 |
| MESSAGE_MAX_REPEATED_SHARE | The most of a briefing's reader-facing text that may be spent on standing explanation said more than once. | ORG | DEFERRED | scalar | A proportion at or between zero and one. Zero means the relief always runs and one means it never does; both are legitimate settings and neither is rejected. **THE MEASURE IS PART OF THE BINDING AND IS STATED HERE BECAUSE A DIFFERENT MEASURE MAKES A DIFFERENT BOUND.** It counts, over the reader-facing text, the length of each member of `STANDING_EXPLANATIONS` beyond its first appearance, and nothing else. **A measure that counts any paragraph identical to another is REJECTED**: on a span of twenty-three it sweeps in the per-item fact lines whose values happen to coincide, and a bound that counts a coincidence of values as waste is a bound that pressures a run to drop data, which inverts what the bound is for. SD-FMT-28 draws the same line for a grid: a phrase identical on every row that carries it may move, and a phrase unique to its own row is never touched. **The share is measured on every run and recorded whether or not the relief fires**, because a bound measured only when somebody suspects a problem is not a bound and a passing measurement is the evidence the check ran. | one third |
| STANDING_EXPLANATIONS | Per standing explanation, the long form an item carries, the short form that replaces it when the relief runs, and the line the key block says in its place. | ORG | DEFERRED | taxonomy | One entry per explanation the run can emit more than once. Per entry: a key, the state it explains, a long form, a short form and a key line. **An EMPTY short form is permitted and means the sentence is appended to a varying per-item line and is removed entirely when the relief runs, leaving that line intact.** The key line MAY equal the long form where the sentence reads correctly in both places. **COVERAGE IS VALIDATED FROM THE EXPLANATIONS THE RUN CAN EMIT TO THIS SET, NEVER THE REVERSE, per SD-CTR-29**: a set declaring four while the run emits six leaves two explanations the bound cannot see and the relief can never reach however often they repeat, and an undeclared repeated explanation understates the measure on every run in which it occurs. **No two entries may share a long form or a short form.** Two states collapsed into one wording is lossy however well the key block explains them, because the key says which is which and the lines are what must still read differently; a relief that leans on its own legend has lost a state. **An entry whose long form is already bound as a member of `NAMED_ABSENCE_STRINGS` cites that member and does not restate it**, per SD-FMT-13: a convention written twice is two conventions, and a sentence whose whole purpose is to be byte-identical to its twin fails on the first edit to either copy. | the measured zero; the disclaimed block; the readable-block absence; the absent contract, citing its absence string; the missing plan row, citing its absence string; the ownership note |
| COUNT_NOUN_FORMS | Per counted noun, the singular and plural forms and the zero wording, carried together. | ORG | DEFERRED | mapping | **This validation is the single statement of the agreement convention for this bundle's message medium, per the precedent SD-FMT-13 sets for its own convention: a convention written twice is two conventions, so element M14 and the workflow's Part J cite this row and do not restate it.** One entry per noun any template counts, each carrying a singular form, a plural form and, where a bare zero reads badly, a zero string. Selection is on the value: zero takes the zero string where one exists and the plural otherwise, one takes the singular, everything else takes the plural. A template that interpolates a count into one fixed noun is REJECTED. The parenthetical form, `visit(s)`, is REJECTED. **A noun already bound as a singular and plural pair elsewhere in the schema is never redeclared here and that pair governs**: `UNIT_NOUN_SINGULAR` with `UNIT_NOUN_PLURAL` in Group 16, and `UNIT_OF_BUSINESS_SINGULAR` with `UNIT_OF_BUSINESS_PLURAL` in Group 5. Those two name a singleton, which is why they are scalars; this mapping carries the open set a briefing's bound sections and sources generate, which is why it is a mapping. Redeclaring one of their nouns here would be two sources for one string. See SD-LNG-13. | stop / stops / "No stops scheduled"; visit / visits; day old / days old |

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

A variable, its documented default and its exact degradation notice are in this one file,
because a run holding a definition without its default has nothing to print at the moment
the value turns out to be unbound.

| Variable | Documented default | Degradation notice |
|---|---|---|
| DELIVERY_PERIOD | The working day. | The unit your briefing covers was not set, so each briefing covers one working day. If your work is organised in shifts or in weeks rather than in days, this is wrong in a way that will be obvious on the first one, and it is one answer to fix. |
| DELIVERY_PERIOD_DAYS | Monday through Friday. | Your delivery days were not set, so briefings go out Monday through Friday and nothing is sent at the weekend. A weekend with scheduled work would be missed. |
| REBUILD_PERIOD | Weekly, on the first day outside DELIVERY_PERIOD_DAYS. Where no such day exists, the lowest-volume delivery day, and the clash is stated. | The rebuild cadence was not set, so content is rebuilt once a week on a non-delivery day. Everything between rebuilds is assembled from that build, which is why each line carries its own freshness. |
| DELIVERY_TIME | **No default, and this is not a stop.** 5.2 step 8 is explicit that unbound is not a hard gate outside the three values that make a source unusable, and this is not one of them. An unbound delivery time does not stop a RUN; it stops a SCHEDULE from being created. | Your delivery time has not been set, so there is no scheduled briefing. The briefing is produced on request instead, with identical content, which is rung 3 of SCHEDULER. Tell me what time you want it and the schedule is created then. |
| DELIVERY_FEED_WAIT_MINUTES | Twenty-eight minutes, or the full gap between run time and expected delivery less two minutes, whichever is smaller. | The poll window was not set, so the briefing waits for the schedule feed until shortly before your stated time and then goes out from the last saved schedule. The first lines say which was used. |
| BRIEFING_RECIPIENT | **No default, and this is not a stop.** Never inferred and never widened. An unbound recipient does not stop a RUN; it stops a SEND, per rung 3 of SEND. | No recipient is bound, so nothing is sent. The briefing is written to the output location and named. A recipient is one answer and the send starts from the next period. |
| BRIEFING_SCOPE | DERIVED from the person-tier scope bound at Q-PERSON-2. Where none exists, the person script runs. Only where the person script itself could not run does it fall to the role resolution, at the narrowest role per ROLE_FALLBACK_KEY and P4. | Your scope was derived from the one you already gave rather than asked again. It is stated at the top of every briefing; if it is wrong, every item is wrong with it. |
| SCHEDULE_FEED_SHAPE | Identifier, name, scheduled date and owner required; planned start time optional. | The shape of your schedule feed was not bound, so the standing four fields were required and a start time was treated as optional. Without a start time the items appear in the order the feed gives them, which is stated rather than presented as the order of the day. |
| ITEM_IDENTIFIER | Detected from the sources in hand as the near-unique concept common to the schedule feed and the period plan, at medium confidence, and printed. | The identifier joining your sources was not bound, so it was detected and is named in the briefing's audit line. A source that would not join on it was staged and reported rather than joined, so nothing in the briefing came from a guessed match. |
| BRIEFING_SOURCES | The period plan alone, required. | Only the period plan was bound as a source, so each item carries what the plan holds and nothing else. Every additional source you add appears in the briefing without any change to the method, under its own heading, with its own columns. |
| SOURCE_FRESHNESS_STATES | The five standing states: CURRENT permits plain assertion; CARRIED permits assertion with a label and a date; ABSENT permits only its named-absence string; UNRESOLVED permits only a statement that the source was present and unreadable; DRIFTED permits every concept that still resolves and nothing from the one that moved, announced by banner. | The standing source states were used. Every line from a carried source carries the date that source was last current, and any source whose shape changed since the last rebuild is named at the top with both resolutions. |
| PREVIOUS_RESOLUTION_RECORD | None. Absent on a first rebuild by construction. | No resolution was recorded for the previous period, so nothing can be compared and no change in the shape of your sources can be detected this time. From the next rebuild onward it can. |
| DRIFT_ANNOUNCE_SCOPE | source. | The drift banner names the source that changed shape rather than every source. |
| STEM_PROPOSAL_SINK | The unbound-value queue. | Column names this briefing learned are proposed to the standing queue for whoever owns the configuration. Nothing is written to the configuration by a scheduled run. |
| NAMED_ABSENCE_STRINGS | For each source, the phrase "Not in the " followed by that source's bound name. | No absence wording was set for your sources, so each missing source prints a standing phrase naming it. The phrase is deliberately not blank and deliberately not zero, because a zero in a briefing reads as a measured value. |
| CARRIED_SOURCE_TRIPWIRE | Half the members of BRIEFING_SOURCES, rounded down, with a floor of one. | The carried threshold was not set, so a briefing built mostly from carried sources carries a banner at the top rather than labels alone. A reader skimming on a phone does not assemble scattered labels into the conclusion that the whole thing is stale; one banner does that for them. See SD-EFF-05. |
| BRIEFING_ITEM_SECTIONS | A header carrying the identifier and the item's position in the period, then one section per bound source in the order they are bound, then the action list. | Your per-item content standard was not bound, so each item shows its header, one section per source, and the actions. The section order follows the order your sources are bound in, which is probably not the order you would read them in. |
| BRIEFING_ACTION_CAP | Six. | The action cap was not set, so no item carries more than six. An item that generated more had the remainder dropped and says so, rather than shipping a list nobody works through. |
| MESSAGE_MAX_REPEATED_SHARE | One third. | The repeated-explanation bound was not set, so a briefing may spend up to a third of its text on wording said more than once. Past that, the repeated wording moves to a key above the first item and each item keeps a short form of it. No item and no fact is dropped either way. |
| STANDING_EXPLANATIONS | **No default, and the absence is reported rather than defaulted.** | Your standing explanations have not been declared, so the repeated-explanation bound cannot be enforced and is reported as unenforceable rather than as met. **This is the one degradation in this group that must never read as a pass.** An undeclared set measures zero on every run, and zero out of an empty set is the shape of a green light that means nothing, which is G2 exactly: unknown is not pass. Every briefing still ships, in full, with every explanation on every item. |
| MESSAGE_MAX_WIDTH | 640. | The briefing width was not set, so the standing single-column width was used. It renders on a phone. |
| MESSAGE_BODY_SIZE | 15. | The briefing body size was not set, so the standing size was used. |
| BRIEFING_SUBJECT_SHAPE | The period, then the item count, then the first and last location where one is derivable. | Your subject line shape was not bound, so the standing shape was used. It changes every period on purpose, because a subject that never changes cannot be told from a job that has stopped running. |
| DATE_FORMAT_DAY | Day, month name, four-digit year: 6 October 2026. Chosen over the all-numeric forms because 06/10/2026 is two different dates depending on who is reading it, and a briefing has no reader present to ask. | Your date format was not set, so every date in the briefing is written as 6 October 2026. It is one format throughout on purpose. The briefing's whole job is to tell you which facts are current, and two date formats in one message make the only comparison you need harder than it has to be. |
| DATE_FORMAT_MONTH | Month name and four-digit year: April 2027. | A date your source knows only to the month is written as April 2027 rather than given a day. The day is not in your file, so the briefing does not supply one. |
| DATE_FORMAT_WEEKDAY | DATE_FORMAT_DAY with the weekday prefixed: Tuesday 6 October 2026. Subject and title only. | The subject carries the weekday as well as the date. Nothing in the body does. |
| COUNT_NOUN_FORMS | Derived per noun at rebuild from the names your own sources and sections use: the plural is the form the source itself uses, the singular is derived from it, and both are printed in the rebuild audit. Where a plural cannot be derived with confidence, that noun is not written into a sentence at all and the count is shown as a labelled figure instead. | Your singular and plural wordings were not set, so they were derived from the names your own sources use and are listed in the rebuild audit. Where one could not be derived it is shown as a figure with a label rather than written into a sentence, because a line reading "1 stops" on your first quiet day costs more trust than a plain label ever would. |

---

## THE FEEDS LIST

Required by 5.2 step 3: "Skip exactly what the value feeds, and nothing else. The schema
records a feeds list against each concept and each binding. Suppress only those flags,
gates, weights, benchmarks and sections."

Without this an unbound value has no defined blast radius. Guessing wide costs a reader
sections they could have had; guessing narrow ships a section built on a value nobody set.

| Variable | Feeds | What is suppressed when it is unbound |
|---|---|---|
| DELIVERY_PERIOD | The period label in the subject and the heading; the window every item is selected against; the comparison against the previous period | Nothing is suppressed. The default is applied and the period in use is named in the heading. |
| DELIVERY_PERIOD_DAYS | Which days fire a send | Nothing is suppressed. The standing five days are used and are stated once at setup, not on every briefing. |
| REBUILD_PERIOD | The rebuild schedule; the freshness arithmetic that decides CURRENT against CARRIED | Nothing is suppressed. The default cadence is used, and because every line already carries its own freshness, a wrong cadence is visible rather than silent. |
| DELIVERY_TIME | The schedule registration only | **The schedule.** Not the briefing. Produced on demand instead, per SCHEDULER rung 3. |
| DELIVERY_FEED_WAIT_MINUTES | The poll window in 3.1 before the schedule ladder falls back | Nothing is suppressed. The derived window is used and the rung actually taken is named in the first lines regardless. |
| BRIEFING_RECIPIENT | The send, and the scope of the send grant | **The send.** Not the briefing. Written to the output location and named, per SEND rung 3. |
| BRIEFING_SCOPE | Which items are eligible at all | Nothing, because it is DERIVED and not asked. Where the derivation itself fails, the run has no eligible population and that is the one condition in this workflow that stops it, matching 5.2 step 8's scope-column case. |
| SCHEDULE_FEED_SHAPE | The setup walkthrough in 1.1; the parse in 3.1; the within-period ordering | The ordering only, where a start time is absent. Items appear in feed order and the briefing says so rather than presenting feed order as the order of the day. |
| ITEM_IDENTIFIER | Every join between the schedule feed, the plan and each additional source | Every section whose source joins on it, each printing its own named-absence string. The headers and the schedule survive, because those come from the feed itself. |
| BRIEFING_SOURCES | Which sections exist per item | Only the sections for sources that are not bound. Per 5.2 step 3 and capability-probe 4.4, a bound source's section always ships, with its explanatory line where it has no content. |
| SOURCE_FRESHNESS_STATES | Every freshness label; the banner condition; gates G-RB-6, G-RB-7 and G-RB-9 | Nothing may be suppressed. **This is the one binding in the group whose default is not a degradation but a floor**: the five standing states apply and the labels print. A briefing with no freshness states is a briefing whose CARRIED values are unlabelled, which A2.1 says is capability-probe 4.4's forbidden substitution. |
| PREVIOUS_RESOLUTION_RECORD | B1 rung 0, the drift comparison | **Drift detection only, and only on a first rebuild where it does not yet exist.** Every other state still resolves. A run that has lost this record is a run that cannot see drift, which is announced, because silently losing the ability to detect a silent failure is the compound version of the thing. |
| DRIFT_ANNOUNCE_SCOPE | The breadth of a drift banner | Nothing. Defaults to naming the affected source. |
| STEM_PROPOSAL_SINK | Where stem proposals are appended | The proposal only. Resolution still happens and the run still works; the dictionary simply stops learning from this briefing, and the run says so once rather than every period. |
| NAMED_ABSENCE_STRINGS | The text printed where a source is ABSENT for one item | Nothing. The standing phrase naming the source is used. It is never allowed to degrade to blank, because blank and zero are the failure this whole workflow exists to prevent. |
| CARRIED_SOURCE_TRIPWIRE | The banner condition only | Nothing. The computed default applies, per S5: a threshold computable from the sources in hand is computed from the sources in hand. |
| BRIEFING_ITEM_SECTIONS | The order and presence of each per-item section | Nothing. Sections appear in the order their sources are bound, and the briefing says that is why. |
| BRIEFING_ACTION_CAP | The length of each item's action list | Nothing. The standing cap applies and an item that generated more says how many were dropped. |
| MESSAGE_MAX_REPEATED_SHARE | The relief that moves repeated standing wording into the key block above the first item. Element M16 | Nothing. The standing third applies, and the measurement is printed on every run whether or not the relief fires. |
| STANDING_EXPLANATIONS | The relief itself; the coverage validation that is what lets the bound see a repetition at all. Element M16 | **The relief only, and the bound is then reported unenforceable rather than met.** Nothing a reader sees is lost: an unrelieved briefing is a longer briefing carrying every explanation on every item, which is merely wasteful where a silently unenforceable bound is misleading. |
| MESSAGE_MAX_WIDTH | Rendered width, element M1 | Nothing. Standing width. |
| MESSAGE_BODY_SIZE | Rendered body size, element M2 | Nothing. Standing size. |
| BRIEFING_SUBJECT_SHAPE | The subject line, element M4 | Nothing. The standing shape applies, and it still varies period to period, which is what M4 is actually protecting. |
| DATE_FORMAT_DAY | Every day-precision date in the message: the degraded banner, the provenance line, every carried label, every age, the footer. Element M13 | Nothing. The standing format reaches all of them, which is this binding's whole value: one value governs every date, so an unbound value degrades to one format rather than to several. |
| DATE_FORMAT_MONTH | Every month-precision date. Element M13 | Nothing. The standing format applies. A month-precision date may not fall back to the day format, so this binding has no degradation path that widens precision. |
| DATE_FORMAT_WEEKDAY | The subject and the title. Element M13 | The weekday prefix only. The subject still carries the date in DATE_FORMAT_DAY, so M4's requirement that the subject change each period survives. |
| COUNT_NOUN_FORMS | Every templated sentence carrying a count. Element M14 | **The sentence form only, and only for the noun whose forms are missing.** That noun's count is shown as a labelled figure instead. The count itself is never suppressed: the number is the fact and the grammar is the packaging. This is the one row in the group where the degradation changes the shape of a line rather than only its wording, and it is worth it, because a labelled figure is merely plain while a disagreeing sentence reads as a broken tool. |

**Read the right-hand column as a whole and one thing stands out: almost nothing is
suppressed.** Two bindings cost a delivery mechanism and neither costs the briefing. One is
a floor rather than a default. One changes the shape of a line rather than its wording. The
rest degrade to a documented standing value and say so.

That is not an accident of this group and it is worth stating, because it is the property
that makes a briefing safe to leave running: **an unbound value in this workflow changes how
the briefing reaches you or what it is allowed to assert, and almost never whether it
arrives.** A briefing that stops arriving is a briefing nobody notices has stopped.

---

## DECLINED, PER I10

I10: a declined answer is written as DECLINED with the date and the reason, behaves exactly
as unbound, and is not re-asked at every opportunity.

A recipient asked for a delivery time who says "whenever, I do not care" has declined. The
workflow records DECLINED, applies the row above, and does not ask again at the next setup
attempt. It surfaces only in a Stage 3 audit, or once more where a run reaches a decision
the default makes materially worse.

**The case worth naming: a declined `BRIEFING_RECIPIENT`.** A person who will not name a
recipient is a person who does not want this sent, and the correct reading is that they want
the artifact rather than the delivery. Write it, name where it is, and stop offering.

---

## NOTES FOR THE PERSON ASSIGNING THIS GROUP

1. **Three of these are PERSON tier, not ORG**: DELIVERY_TIME, BRIEFING_RECIPIENT and
   BRIEFING_SCOPE. They are answered by each recipient on their own first run and are never
   asked of one person on behalf of another. That is what makes a per-person briefing
   per-person rather than a broadcast with names in it.

2. **Two are deliberately not defaultable**: DELIVERY_TIME and BRIEFING_RECIPIENT. Both
   fail the wrongness test in the opposite direction from the usual: their absence does not
   make the output thinner, it makes it go to the wrong place or at the wrong hour forever,
   and both are asked while a person is present. Their default column says so rather than
   inventing a value to fill the cell.

3. **None of these belongs at IGNITION.** A recipient setting up a briefing answers them in
   the course of setting it up, and an organization that never uses this workflow should
   never be asked any of them.

4. **`BRIEFING_SCOPE` is DERIVED and must stay that way.** Q-PERSON-2 already binds the
   person's scope and I2 forbids asking what the records hold. PART 4 opens by promising
   four questions and no more; a fifth about the same subject makes that promise false.

5. **The FEEDS column above is required by 5.2 step 3 and was missing from the first
   draft.** Any variable added to this group later needs a feeds row in the same commit,
   because a binding with no declared blast radius leaves an implementer guessing which
   sections an unbound value should cost.
