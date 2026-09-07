# GROUP CTR: THE OUTPUT CONTRACT AND ITS SHAPE

### SD-CTR-01 A single declared source of truth for the output
- Rule: one section states the whole shape of the output, and every other
  instruction is subordinate to it. "Where any later instruction disagrees with
  this contract, the contract governs and the later instruction is the defect."
- Mechanism: read before step one, verified at the final gate.
- Prevents: defects that live at the seam between two individually correct
  sections, because no single place stated the whole shape of the output.
- General form: TAB_CONTRACT plus IDENTITY_BLOCK_COLUMNS plus DELIVERABLE_LINES
  is the contract. Every stage is subordinate to it.
- Source: P-D1
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-02 Exactly two deliverable shapes, differing only in three numbers
- Rule: there are two report lines and no others. Every run emits exactly one
  artifact in the shape that matches the resolved role, and the two shapes are
  identical in every respect except three counts.
- Mechanism: DELIVERABLE_LINES holds tier 1 size, tier 2 size and REFERENCE_CAP.
- Prevents: format proliferation, and an artifact whose structure varies by
  requester so two runs cannot be compared.
- General form: the deliverable's shape is a function of role tier only, and only
  in size.
- Source: P-D2
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-03 "Up to" is load bearing on a reference section
- Rule: a capped reference section holds min(REFERENCE_CAP, eligible_count minus
  last_action_rank) rows, or zero rows plus one explanatory row, and no
  instruction anywhere may assert it holds exactly REFERENCE_CAP.
- Mechanism: the row-count form is authoritative wherever any other section
  states the size differently.
- Prevents: a correct artifact failing its own reconciliation gate, and a retry
  loop that burns the build budget the formatting pass needs.
- General form: any capped section is described by its arithmetic, never by its
  cap.
- Source: P-D3
- Applies: PLANNING, SCORECARD

### SD-CTR-04 Two population figures exist and are published separately
- Rule: N is every unit in the ranked population, including mandatory ones, and
  is what every percentile and median was computed over. eligible_count is the
  merit remainder that sized the action sections. Publish both.
- Mechanism: "A funnel showing only one of them cannot be reconciled against the
  section sizes."
- Prevents: an unreconcilable population funnel and percentiles computed over the
  wrong denominator.
- General form: whenever a population is split for routing, both the whole and
  the remainder are published.
- Source: P-D4
- Applies: PLANNING, SCORECARD

### SD-CTR-05 A user-requested size overrides the role default; everything else stays fixed
- Rule: honour the number the user asked for, split it by
  USER_SIZE_TIER_1_FRACTION rounded up to the first tier and the remainder to the
  second, keep every cap and gate unchanged, and rename the sections for the
  counts they hold.
- Mechanism: the last merit rank becomes requested_size plus min(REFERENCE_CAP,
  eligible_count minus requested_size).
- Prevents: a resize silently carrying the literal derived rank ceilings.
- General form: a size request changes counts and nothing else.
- Source: P-D5
- Applies: PLANNING, SCORECARD

### SD-CTR-06 Three independent request axes compose freely and none changes the shape
- Rule: SCOPE selects whose units, QUALIFIER selects which subset of them by
  matching any other column on its values, STEER selects what to lean on. All
  three compose in any order and any combination. "They change the population and
  the weighting; they never change the sections, the formatting elements, or the
  two sizes."
- Prevents: asking the user to restate a multi-axis request, and letting a filter
  mutate the deliverable.
- General form: unchanged.
- Source: P-D6
- Applies: PLANNING, SCORECARD

### SD-CTR-07 Every section ships every run, even with nothing to report
- Rule: a section with nothing to report still ships, carrying its header plus
  exactly one row stating the reason in plain language. Never drop a section,
  never renumber around one, never reorder them.
- Mechanism: the table is placed over the header plus that single row, because a
  table over an empty block is invalid and will fail the build.
- Prevents: a silently missing section reading as an unfinished artifact.
- General form: MSG_EMPTY_SECTION carries one message per entry in TAB_CONTRACT.
- Source: P-D7
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-08 The identity block is structurally identical on every item section
- Rule: the same identity columns, in the same order, on every item section
  without exception.
- **Rule: AND THE FREEZE LANDS IN THE SAME PLACE ON ALL OF THEM.** Identical columns
  in identical order with the pin in a different place per section is not a structurally
  identical block, because what the reader experiences moving between sections is the
  pin. The span is walked ONCE for the artifact from the widest case and applied by
  name everywhere, per SD-FMT-03.
- Mechanism: verified by header NAME and relative order, never by fixed column
  number, "because the block's width changes with the requester's level: a check
  written against columns 1 to 9 passes a wrongly built junior artifact and fails
  a correct senior one."
- Prevents: one freeze point and one visual system breaking across sections; a
  gate that passes the wrong artifact.
- General form: unchanged.
- Source: P-D8
- Applies: PLANNING, SCORECARD

### SD-CTR-09 Header strings are byte-identical between runs
- Rule: copy header strings literally. Do not rename, reorder, add, omit or
  improve a header for readability. "Two runs on the same source must produce
  artifacts whose header rows are byte-identical."
- Prevents: loss of comparability between two runs, and between runs at different
  scope levels.
- General form: every HDR_ variable is a config string, never a phrasing choice.
- Source: P-D9
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-10 Publish the number you ranked on
- Rule: the score column is mandatory on every item section, written to
  SCORE_DECIMAL_PLACES, and is never omitted.
- Prevents: an unauditable list. "A ranked list that does not publish the number
  it ranked on cannot be checked by the person holding it, and a reviewer
  comparing two runs has nothing to compare."
- General form: unchanged.
- Source: P-D10
- Applies: PLANNING, SCORECARD

### SD-CTR-11 The rank-within-scope header is the same string at every level
- Rule: the header string is SCOPE_RANK_HEADER at every scope level. Never
  retitle it for the requester's own level.
- Mechanism: the scope is already stated in the section title and the front
  panel, "and a header that changes with the requester breaks comparison between
  two runs at different levels."
- Prevents: two runs at different levels becoming incomparable.
- Source: P-D11
- Applies: PLANNING, SCORECARD

### SD-CTR-12 A derived analysis needs BOTH halves of its inputs, and the pair is the admission test
- Rule: a derived section is built only where its formula's inputs both resolve.
  Test every candidate against the pair. If two qualify, take the highest ranked
  in the standing hierarchy. If none qualifies, ship the section with one
  explanatory row.
- Mechanism: "The entity is NOT a free choice: it is the one whose columns
  resolve BOTH a distinct-item COUNT and a satisfaction PERCENTAGE. That pair is
  the admission test."
- Prevents: computing a gap, a peer norm and an upside estimate against a count
  that does not exist, so every number is blank or invented.
- General form: BREADTH_ADMISSION_IS_THE_PAIR. Any derived metric whose formula
  needs two inputs is admitted on the pair, never on a name.
- Source: P-D12
- Applies: PLANNING, SCORECARD

### SD-CTR-13 An unresolved column is written blank, never dropped
- Rule: a column whose source does not resolve is still written, header present
  and cells blank, with the failure named in the audit section. "Dropping the
  column instead changes the shape of the artifact and is a contract violation."
- General form: UNRESOLVED_COLUMN_TREATMENT is write_blank_keep_header.
- Source: P-D13
- Applies: PLANNING, SCORECARD

### SD-CTR-14 The items come first; everything explanatory goes after
- Rule: the list leads. "The opener is a few lines, not a page." This governs
  order inside a section and inside the reply, and does not reorder the sections.
- Prevents: a hurried reader having to scroll past methodology to reach the work.
- Source: P-D295; R-D41 guardrail 6
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-15 The audit trail is exhaustive BY DESIGN and sits at the very end
- Rule: the audit section is complete to the point of tedium and is placed last.
  "It sits at the very end, after the lists, where it costs a hurried operator
  nothing but lets a skeptical manager reconstruct every number."
- Mechanism: an ordered specification including a worked example taken end to end
  so a reader can recompute one unit by hand.
- Prevents: the tension between brevity for the operator and auditability for the
  reviewer, resolved by placement rather than by omission.
- Source: P-D296
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-16 The reply is short and never pastes the list
- Rule: at most CHAT_REPLY_MAX_LINES, naming the scope and period, the source
  used, the mode in plain words, the priorities found or plainly that none were,
  the mandatory count, the top three with one line each, and the filename.
  Anything else belongs in the artifact.
- Source: P-D304
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-17 A one-line heads-up on a large input
- Rule: state the row count, the scope, and that the build will take a while, so
  the user knows the silence is work and not a hang.
- Source: P-D305; R-D11 (the coffee gate)
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-18 Do not send or share the artifact automatically
- Rule: produce it, name it, hand it over. Never mail it, post it or share it
  without being asked.
- Source: P-D306
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-19 Every artifact carries the owner's contact line and an invitation to tune
- Rule: two sentences in plain business language, free of jargon, stating that
  thresholds are computed from the user's own scope, that local commercial rules
  are inputs the method does not assume, and how to reach the binding owner.
- Mechanism: METHOD_OWNER_STATEMENT plus MSG_AUTHOR_LINE, in every artifact,
  "so a user who opens the file months from now still knows who to ask and what
  is adjustable."
- Source: P-D307
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-20 The method is built to be calibrated, and local reality is an INPUT rather than a guess
- Rule: everything the method can compute from the data it computes at run time;
  everything it cannot infer is left as an input. "A wrong assumption stated
  confidently is worse than a stated gap."
- General form: this is the design principle the whole binding schema exists to
  serve.
- Source: P-D308
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-21 Transparency exists so a disagreement can be traced rather than argued
- Rule: publish the formula and a worked example, "so a disagreement can be
  traced to a specific term and corrected rather than argued."
- Source: P-D309
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-22 A heading with no counterpart on the destination form never enters the body
- Rule: any heading that does not exist on the live destination form is banned
  from the submitted body, however familiar it is from prior documents.
- Mechanism: BANNED_HEADINGS, plus SUBMISSION_BOUNDARY_BANNER below which
  planning content and verification items sit.
- **Rule: A SECTION OF A FORM AND A FIELD OF A SUBMISSION ARE DIFFERENT THINGS, AND
  ONE SECTION CAN HOLD MANY FIELDS.** A section is a part of the form; a field is one
  character-capped box inside it. The block, the character count and the character
  limit attach to the FIELD. The section supplies the order of the blocks and nothing
  else. A verification that counts blocks against the SECTION list blocks a correct
  document the moment one section holds two fields, which is ordinary rather than
  exotic: an objectives section holding one capped box per objective produces four
  fields for a person with four objectives. The derived field set is PRINTED in the
  document, so the block count reconciles against something real.
- Prevents: a bad house format propagating through an organization because
  everyone inherited last year's document; and a correct artifact stopped at
  publication by a check reading a list of one kind of thing as a list of another.
- Source: R-D42; R-D7; extended by the demonstration run, review D5
- Applies: REVIEW, SCORECARD

### SD-CTR-23 Content that must not travel sits below a banner, never inside a copy block
- Rule: forward-planning content and items-to-verify sit outside and below the
  copy region under an explicit banner, so they cannot travel into a destination
  system by accident.
- **Rule: A COPY REGION NEEDS A VISIBLE STOP LINE AT BOTH ENDS.** A reader drags
  DOWNWARD from under a heading, so anything placed between the heading and the field
  text is caught before they notice it, while a line placed AFTER the field text is
  something they stop at rather than pass through. Metadata about a field, its
  character count and its limit included, therefore sits BELOW that field's text and
  above the next heading, in its own style, and never in the heading line and never
  above the text. This was built and measured: a caption above the text was picked up
  by a drag begun at the heading on every block of the document.
- **Rule: an UNSOURCED NUMBER has a defined home, and it is below the banner.** Where
  a rule turns a number that traces to no cell and no tool result into a bracketed
  placeholder, and the copy-block rule forbids a bracketed aside inside a field, the
  two are reconciled one way: the claim ships in the copy region WITHOUT the number,
  and the number goes below the banner carrying its source and the question that
  would settle it, linked to the field by that field's own heading. Deleting it
  instead is not neutral: on a run with no mail and no chat, a person's own note is
  the only evidence of what they did, and a seam that strips every figure out of it
  silently deletes their year.
- Prevents: content travelling into a permanent record by accident, and evidence
  falling down the gap between two rules that each looked complete alone.
- Source: R-D42; extended by the demonstration run, review D1 and D6
- Applies: REVIEW

### SD-CTR-24 A bound value outranks a default, and an unbound value never overrides a bound one
- Rule: precedence runs strictly downhill from evidence to convention. In order:
  a value the answerer bound at IGNITION; a value the answerer bound later; a
  value derived from the data this run; a documented default. A documented
  default applied to an unbound variable may narrow what the run attempts. It may
  never contradict, replace or silently supersede a value the organization
  actually bound.
- Mechanism: before applying any documented default, test whether the default
  would change a decision that a bound value already decided. If it would, the
  default is not applied to that decision. The bound value stands, the run does
  only the part the unbound variable was needed for, and the notice names the
  narrowing rather than the substitution.
- The named case: the entity-to-benchmark map is deferred and, at a business with
  no wider population, will never be bound, correctly. Its old default routed
  EVERY figure to the floor rung, overriding a rung the organization had bound at
  ignition as its primary control. An unbound deferred value had quietly deleted
  a bound ignition value.
- The general form of the fix: an unbound value that supplies ONE rung, ONE flag
  or ONE section removes only that rung, that flag or that section. The run then
  falls to the best remaining BOUND option, never past it to the floor. A weaker
  option is never silently substituted for a stronger one that failed, and the
  floor is reached only when no bound option resolves.
- Prevents: a deferred default silently overriding an ignition binding, which
  produces a run that is internally consistent, disclosed, and answering a
  question the organization did not ask.
- Source: report 1 D4; extends P-D174 and P-D223
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-26 A fully answered interview must produce a fully bound run
- Rule: if a competent answerer answers every question the interview asks, in the
  way a competent person naturally answers it, the run that follows is NOT
  provisional. Where it is, the defect is in this bundle and never in the
  answerer: either the interview is not asking for something the validation
  requires, or a required sub-field is missing a derivation.
- **THE INTERVIEW AND THE VALIDATION ARE ONE CONTRACT AND THEY ARE CHECKED
  AGAINST EACH OTHER.** For every variable the validation requires, exactly one of
  three must be true: a turn elicits it directly; a documented derivation computes
  it from what the turns do elicit; or it carries a documented default. A variable
  for which none of the three holds is a hole in the interview, not a gap in the
  organization's knowledge.
- The named case: an ignition set of eleven, three of them taxonomies. A
  co-operative director answered all seven turns naturally, giving the ORDER of
  the roles and the name of the thing being ranked, and walked away without
  claim_tier, without scope_level and without population mode. Validation then
  found ignition incomplete, so every artifact that organization ever produced was
  stamped PROVISIONAL, off a fully answered interview, and nothing told the
  interviewer they had left anything out. A working interview that silently
  produces a permanently degraded product is worse than an interview that fails,
  because nobody goes back to fix it.
- Mechanism, three states and all three satisfy the validation: ANSWERED, at high
  confidence; DERIVED, at medium confidence, by the derivation named in the
  variable's own documented-default row; DEFAULTED, at low confidence, carrying
  its notice. A DERIVED sub-field is NOT an unbound sub-field.
- **Rule: every DERIVED value is read back to the answerer BEFORE the interview
  closes, in one table, in their own words, with the invitation to correct any
  line.** A correction promotes that line to ANSWERED. This is the only
  circumstance in which a medium-confidence value may be written to an
  organization's configuration, and it is legitimate only because a person with
  authority looked at it and said yes. A RUN may still never do this. The
  confidence rule for inference during a run is untouched.
- Rule: the close of any binding interview states what was answered, what was
  derived, and what was left to a default, with a count of each. An interviewer
  who is told nothing was left out is entitled to believe it.
- Prevents: a permanently provisional deployment created by a successful
  interview.
- Source: confirmation run 2, blocker 3
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-27 A derived scope ladder is anchored at BOTH ends, and never on the unit itself
- Rule: where role scope levels are derived by position rather than stated, anchor
  the mapping at BOTH ends of the chain. The most junior role maps to the FINEST
  OWNABLE level, which is the level immediately COARSER than the unit level, and
  the most SENIOR role maps to the COARSEST level. Surplus levels in the middle are
  absorbed by the senior roles; surplus roles share the finest levels.
- **NOBODY OWNS ONE UNIT OF BUSINESS AS THEIR SCOPE. THE UNIT IS THE ROW, NOT A
  SPAN.** Anchoring the junior end on the finest level outright maps the most
  junior role onto the unit level, which says that person owns exactly one unit.
  Read literally that fires the level-equals-the-reader's-level path, which
  suppresses the ranked list, the percentile and every comparative statement, and
  hands the frontline reader the method was built for a report with no ranking in
  it. SD-SPN-02 condition three and SD-POP-26 both already say the unit level is
  not a span; this rule makes the derivation agree with them.
- **AND IT IS OFF BY ONE AT EVERY ROLE, NOT ONLY THE FIRST.** A single-anchored
  mapping shifts the whole ladder one rung narrow: the top of the house comes out
  owning a region, the top level comes out owned by nobody, and a role that leads
  people who work units comes out as a role that works units. That last one is the
  consequence that survives into an artifact, because it flips a claim tier and
  SD-SPN-09 calls that error fatal in both directions.
- **THE TELL THAT THE ANCHOR IS THE BUG: the derivation's own FALLBACK gives the
  right answer where the derivation gives the wrong one.** The fallback, used when
  the unit level is unbound, says the most junior role is DIRECT and every other
  role is AGGREGATE. Where a derivation that knows MORE produces a worse answer
  than the fallback that knows LESS, the extra knowledge is being applied at the
  wrong end. Treat that pattern as a diagnosis, not a coincidence.
- Mechanism: derive, then CHECK the two paths against each other. Where the
  positional derivation and the fallback disagree about any role's claim tier, the
  derivation is wrong, the fallback stands, and the disagreement is recorded for
  the binding owner. Both paths must agree on a well formed ladder.
- Rule: exactly ONE level is DIRECT, the finest ownable level, and every level
  coarser than it is AGGREGATE without exception. A person who owns a group of the
  things that own units does not touch the units.
- Prevents: a leader receiving the junior list size and claiming a subordinate's
  individual work, off a derivation nobody was asked to confirm.
- Source: acceptance run 3, defect 3
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-28 The cost order for a deferred question is computed on this run, never read from a table
- Rule: where a run may ask only one or two configuration questions, WHICH ones it
  asks is decided by what the defaults actually changed in the artifact this run is
  about to publish, not by a priority table fixed when the skill was written. A
  static order cannot know which question is decorative on a file it has never
  seen.
- The named case: a run spent its entire question budget on a request whose default
  changed nothing observable, the artifact being identical either way, while the
  request deciding whether eleven units that had already given notice of exit sat
  inside a published plan was pushed out of budget. The static table had ranked
  them in that order. Two rows of a top ten turned on the question that was never
  asked.
- Mechanism, four classes, computed before any request fires, because every default
  has already been applied by the time a run can publish anything:
  1. CHANGES MEMBERSHIP OF A RANKED LIST. Jumps the queue ahead of every class
     below, whatever any static order says.
  2. CHANGES A PUBLISHED ORDER OR FIGURE. Ordered within the class by the number of
     published rows affected, descending.
  3. CHANGES SOMETHING NOT PUBLISHED THIS RUN.
  4. PROVABLY CHANGED NOTHING. **Does not fire at all this run.** It stays queued.
- Rule: ties, and only ties, fall back to the skill's documented decision-point
  order, then to variable name, so the same file always spends its budget the same
  way and two runs over the same data are comparable.
- Rule: record the computation and not only its result. Name every outstanding
  request, its class, the count of published rows its default affected, and whether
  it fired. A binding owner can then see which questions are suppressed as class 4
  run after run, which is the list worth clearing in one sitting.
- Rule: this changes WHICH questions fire, never HOW MANY. The budget is untouched.
- Prevents: a scarce question spent on a difference nobody could observe while the
  expensive one waits for a run that never comes.
- Source: acceptance run 3, defect 4
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-29 A closed set must name the ORDINARY case, and coverage is validated against the states it serves
- Rule: a CLOSED vocabulary that a run must draw from is only usable if it carries
  at least one member for every state the contract can produce. Validate coverage
  in that direction, from the STATES to the SET, and do it whenever either changes.
  A set validated only for internal consistency can be perfectly well formed and
  still unable to name the commonest thing that happens.
- The named case, and the shape of it is what makes it worth a rule: a closed
  reason vocabulary seeded eleven codes for a rare state and eight for another rare
  state, and ZERO for the state that is the skill's entire subject. The contract
  required a code on every non-pass cell, the set could supply none, and a run
  produced hundreds of unmapped cells on ordinary data. The skill's central output
  was the one state with no vocabulary.
- **THE TEST: for every state the contract can emit, does the closed set contain at
  least one member that applies to it?** Any state with zero members is a HOLE, and
  a hole guarantees an unmapped value on every run in which that state occurs.
  Where the holed state is the common case, the set is not merely incomplete; it is
  unusable, and it will look complete to anybody who reads it without counting.
- Rule: distinguish a HOLE from a DELIBERATELY EMPTY ADDITIVE LIST. A filter list
  that starts empty, such as a list of locally banned words, is correct when empty:
  nothing is filtered yet, and nothing is required to produce a value from it. A
  VOCABULARY the contract requires a value FROM is a different kind of set, and an
  empty family in one is a defect. The test is whether some output cannot be
  produced without drawing from the set.
- Rule: a member whose implied action is genuinely NONE states that explicitly, and
  names NOBODY as able to clear it. An entry that looks actionable and is not sends
  a reader to do work that does not exist, which is worse than the unmapped value it
  replaced.
- Prevents: a closed set that certifies as complete and cannot name the ordinary
  case.
- Source: scorecard acceptance run, defect 1
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-30 A default shared by several skills may not carry one skill's content
- Rule: where a variable is read by more than one skill, its documented default
  must be either SKILL-NEUTRAL or KEYED BY SKILL. A shared variable whose default is
  one skill's content is that skill's contract wearing a shared name, and a literal
  implementer of any other skill ships the wrong document.
- The named case: the ordered section list and the artifact name were single shared
  defaults holding the planning skill's sections and the planning skill's title, so
  a literal implementer running a scorecard produced a document titled and shaped
  like a work plan. Its own body named six different sections, and the contract
  elsewhere declares the section list fixed and identical for every requester, so
  the implementer had to choose which instruction to break.
- Mechanism, and it is a two-part sweep to run whenever a default is written or
  changed:
  1. Determine which skills READ the variable. One reader means a single default is
     correct and its vocabulary may be that skill's, because there is no other
     skill to mislead.
  2. More than one reader means the default is either neutral in its wording, or it
     is a KEYED SET with one entry per skill. A single string shared across three
     documents titles two of them wrongly.
- Rule: a default that must name a THING whose noun differs by skill names the ROLE
  rather than the noun. What a compliance gate holds back is THE VALIDATED ITEMS,
  which are priorities in one skill and requirements in another; naming one of them
  reads as an instruction to hold back something the other document does not have.
- Rule: this is about DEFAULTS, not about variables. A variable only one skill reads
  is not a defect and is not renamed; the sweep is only ever over the shared ones.
- Prevents: a correct implementer producing the wrong artifact by following a
  documented default exactly.
- Source: scorecard acceptance run, defect 2
- Applies: PLANNING, REVIEW, SCORECARD

### SD-CTR-25 Binding authority is ADDITIVE, and answering a question never removes an answerer
- Rule: the set of people authorized to answer a deferred ORG question is a UNION
  of standing grants, never a replacement of one grant by another. Recording a
  fact about an organization may ADD an authorized answerer. It may NEVER remove
  one. Any default written as "where X is bound, A; where X is unbound, B" is a
  replacement, and it is forbidden for authority.
- Mechanism, the two standing grants, both live at all times:
  1. The named configuration owner holds ALL, whenever a name is recorded.
  2. The most senior role on the role ladder holds ALL, WHETHER OR NOT an owner is
     named.
  Every other role holds NONE. Only an EXPLICIT per-role binding by the
  organization may narrow either grant. No run may narrow either grant, and no
  other binding may narrow one as a side effect of being set.
- **THE MONOTONICITY TEST, RUN IT BEFORE ANY CHANGE TO AN AUTHORITY DEFAULT
  SHIPS.** Take any organization and any person. Compare the set of questions that
  person can answer with a configuration owner named against the same set with no
  owner named. The first set must be a SUPERSET of the second, or equal to it. If
  binding one more fact ever makes the set smaller, the default is a replacement
  wearing a union's clothes and it is wrong.
- The named case, which is why this rule exists: an earlier revision granted the
  most senior role ALL only where the owner name was UNBOUND. At any organization
  whose configuration owner sits in operations, in IT, in enablement or in any
  function that is not an entry on the operating role ladder, which is most of
  them, naming an owner moved the most senior role from ALL to NONE. Doing the
  right thing at ignition made progressive binding STRICTLY LESS LIKELY TO FIRE
  than skipping it, at exactly the organizations that had taken the interview
  seriously. The mechanism ran backwards and nothing in the artifact showed it,
  because a question that is never asked leaves no trace but a queued request.
- Rule: every run that fires a deferred question names WHICH grant authorized it,
  the named owner or the standing senior-role grant, so a reader can tell why they
  were asked and an auditor can tell whether the union held.
- Rule: this generalizes beyond authority. Wherever a default is written with two
  branches on whether some other variable is bound, check that the bound branch is
  not strictly poorer than the unbound one. A default that punishes binding is a
  default that trains an organization not to bind.
- Prevents: the progressive binding mechanism switching itself off in response to
  correct configuration.
- Source: confirmation run 2, new defect 1; regression against report 3
- Applies: PLANNING, REVIEW, SCORECARD

---
