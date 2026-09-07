# GROUP 4: THE ROLE LADDER

TAXONOMY SHAPE, ROLE_LADDER. An ordered list, most junior first. Each role
carries:
- `key`: stable id.
- `display_name`: the canonical title.
- `titles`: every title string and abbreviation that resolves to this role.
- `scope_level`: the SCOPE_LEVELS key this role owns.
- `claim_tier`: DIRECT (the person personally changed the unit) or AGGREGATE
  (someone on their team did).
- `report_line`: which deliverable size this role receives.
- `altitude_ceiling`: the highest LINEAGE_LADDER rung this role may claim as
  ownership.
- `peer_level`: the level whose siblings form this role's peer set.
- `is_specialist`: true where the role covers a subset of another role's units
  under direction, which makes it both a reader and the subject of a
  de-duplication discount.
- `has_reports_default`: whether this role normally carries direct reports.
- `binding_authority`: the list of schema GROUP numbers this role may answer
  deferred ORG questions for, or the literal `NONE`, or the literal `ALL`.

  **AUTHORITY IS ADDITIVE. THE DEFAULT IS A UNION OF TWO STANDING GRANTS, AND
  NAMING A BINDING OWNER MUST NEVER REMOVE AN ANSWERER.** Both grants stand at
  all times, and neither is conditional on the other:

  1. The named BINDING_OWNER_NAME holds `ALL`, whenever a name is recorded.
  2. The MOST SENIOR ROLE in ROLE_LADDER holds `ALL`, WHETHER OR NOT an owner is
     named. This grant is not a fallback and it is not withdrawn when an owner
     appears.

  Every other role holds `NONE` by default. An organization may narrow the
  default afterwards by binding the field explicitly, per role, and that
  narrowing is the ONLY thing that may take authority away from the most senior
  role. A run may never narrow it, and no other binding may narrow it as a side
  effect.

  **WHY IT IS A UNION AND NOT A FALLBACK, STATED SO IT CANNOT REGRESS AGAIN.** An
  earlier revision made the senior-role grant conditional on the owner being
  unbound. That made the default a REPLACEMENT rather than an addition, and it
  ran backwards: at any organization whose configuration owner sits in
  operations, in IT, in enablement or in any other function that is not an entry
  on the operating role ladder, which is most of them, naming an owner STRICTLY
  REDUCED the set of people who could answer a deferred question. The senior role
  went from `ALL` to `NONE` the moment somebody did the right thing at ignition,
  and progressive binding became less likely to fire than if the owner had never
  been named. See SD-CTR-25, which states the invariant as a rule.

  The two grants are not mutually exclusive in practice either: where the named
  owner DOES hold a ladder role, and where that role is the most senior one, the
  two grants land on the same person and the union is simply that person. Nothing
  special happens and nothing is double counted.

  Every run that relies on a grant discloses WHICH grant authorized the question
  it asked: the named owner, or the standing senior-role grant. Without any grant
  at all there is no authorized answerer, so no deferred question can ever fire,
  all of them default, and every request queues to a person who does not exist:
  the progressive binding mechanism switches itself off silently at exactly the
  organizations most likely to have skipped the name.

  This is the field that makes the right-answerer constraint computable: without
  it the constraint cannot be evaluated, and a gate that cannot be evaluated has
  failed, per SD-EFF-03. With it, the test is a lookup.

The line boundary between report shapes is a single cut in this ordered list.
There is exactly one cut, and it is named once.

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| ROLE_LADDER | The ordered role taxonomy, junior first. | ORG | IGNITION | taxonomy | At least 2 roles. Every scope_level is a key in SCOPE_LEVELS. Every altitude_ceiling is a rung in LINEAGE_LADDER. | Adjuster; Senior Adjuster; Claims Supervisor; Branch Manager; Regional Claims Director |
| ROLE_TITLE_ABBREVIATIONS | Normalization dictionary from abbreviation to expansion, applied before title matching. | ORG | DEFERRED | mapping | Keys lowercased, no punctuation. SEED, extended at runtime. | sr to senior; mgr to manager; dir to director; asst to assistant |
| SENIOR_TIER_PREDICATE | The single predicate that decides which report line a role receives, stated once. | ORG | DEFERRED | scalar | Must reference role keys or claim_tier, never a restated list of titles. | claim_tier equals AGGREGATE, or is_specialist is true |
| REPORT_LINE_JUNIOR_KEY | Key of the deliverable shape for the direct-action tier. | ORG | DEFERRED | scalar | Must exist in DELIVERABLE_LINES. | line_a |
| REPORT_LINE_SENIOR_KEY | Key of the deliverable shape for the aggregate tier. | ORG | DEFERRED | scalar | Must exist in DELIVERABLE_LINES. | line_b |
| ROLE_FALLBACK_KEY | The role assumed when the directory cannot be read and the user does not answer. | ORG | DEFERRED | scalar | Must be a key in ROLE_LADDER. Should be the narrowest role, so an unknown never inflates a claim. | adjuster |
| PEOPLE_LEADER_OBJECTIVE_REQUIRED | Whether a role with direct reports must carry a people-leadership objective. | ORG | DEFERRED | scalar | Boolean. | true |
| PEOPLE_LEADER_OBJECTIVE_SOURCE | The named document defining that objective. | ORG | CONDITIONAL | scalar | Required when PEOPLE_LEADER_OBJECTIVE_REQUIRED is true. | Leader Goal Standard |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 4: The role ladder

| Variable | Documented default | Degradation notice |
|---|---|---|
| ROLE_TITLE_ABBREVIATIONS | The generic set: sr to senior, jr to junior, mgr to manager, dir to director, asst to assistant, sup to supervisor, vp to vice president. | No organization-specific title abbreviations have been bound. A title written in local shorthand may not resolve, in which case you are asked once to pick your role from a list. |
| SENIOR_TIER_PREDICATE | Derived: claim tier equals AGGREGATE, or the role is marked as a specialist. | Derived from the role ladder rather than stated separately. |
| ROLE_LADDER.binding_authority | ADDITIVE, a union of two standing grants: ALL for the named BINDING_OWNER_NAME whenever a name is recorded, AND ALL for the MOST SENIOR ROLE in ROLE_LADDER whether or not an owner is named. NONE for every other role. Naming an owner never removes an answerer, per SD-CTR-25. Only an explicit per-role binding may narrow this, and no run may narrow it. Anyone without authority is never asked; the documented default is applied, the notice is printed, and the request is queued. | Authority for configuration questions has not been set per role, so the standing grants were used: whoever is recorded as owning this configuration, and the most senior role on the role list, may answer them. This report says which of those authorized any question it asked. Where a setting was missing and nobody present could answer it, the standing default was used and the report names it. |
| ROLE_LADDER.scope_level | DERIVED by position, and **THE ANCHOR IS THE FINEST LEVEL STRICTLY COARSER THAN UNIT_LEVEL_KEY, NOT THE FINEST LEVEL OUTRIGHT.** Nobody owns one unit of business as their scope: the unit is the ROW, not a span. So the most junior role maps to the finest OWNABLE level, which is the first level above the unit, and the ladder walks upward from there. **The chain is then anchored at BOTH ENDS: the most SENIOR role maps to the COARSEST level, the top of the house.** Where the ladder is shorter than the remaining chain, the surplus levels are absorbed by the SENIOR roles, each of which then owns its level and everything between it and the next role below; the top level is never left unowned. Where the ladder is LONGER than the chain, consecutive junior roles share a level and the tie goes to the FINER level, because reading a junior role too narrowly is the safe direction. Where UNIT_LEVEL_KEY is unbound, anchor at SCOPE_FINEST_KEY, which is the level immediately coarser than the finest level in the chain, and disclose that the anchor was not confirmed. **NEVER anchor at the finest level of the chain outright: that level is one unit of business, and a role anchored there is reported as a binding error by SD-POP-26.** | The level each role owns was not stated for every role, so it was read off the order of the two lists you gave: the most junior role owns the smallest thing anybody owns, which is one level above a single {unit noun} rather than the {unit noun} itself, the most senior role owns the whole organization, and the roles between them fill in upward. Every role and the level it was given are printed here for you to correct in one line. |
| ROLE_LADDER.claim_tier | DERIVED from UNIT_LEVEL_KEY and the corrected scope_level anchor: **EXACTLY ONE LEVEL IS DIRECT, and it is the finest OWNABLE level, meaning the level immediately COARSER than UNIT_LEVEL_KEY.** A role at that level works units with its own hands. **EVERY role coarser than that level is AGGREGATE, without exception**, because a person who owns a group of the things that own units does not touch the units. A role whose scope_level is AT or FINER than UNIT_LEVEL_KEY is a binding error, not a claim tier, and is reported under SD-POP-26. Where UNIT_LEVEL_KEY is unbound, the most junior role is DIRECT and every other role is AGGREGATE. **The two paths must give the same answer on a well formed ladder, and where they differ the derivation is wrong and the fallback is right.** | Whether each role does the work themselves or leads a team that does was not stated, so it was worked out from where each role sits relative to one {unit noun}: exactly one level does the work with its own hands, the finest level anybody actually owns, and every level above it leads people who do. Claim wording follows that split, so if it is wrong for a role, that role's claims are worded at the wrong strength and this is the line to fix. |
| ROLE_LADDER.altitude_ceiling | DERIVED: the LINEAGE_LADDER rung corresponding to the role's scope_level, or where no correspondence exists, the rung one below the top so no role claims the whole organization by default. | The highest thing each role may claim as their own was not stated, so it was set from the level they own. No role defaults to claiming an organization-wide outcome. |
| ROLE_LADDER.report_line | DERIVED by applying SENIOR_TIER_PREDICATE to the role's claim_tier and is_specialist. | Which report size each role receives was not stated, so it follows the single senior-tier predicate rather than a separate list. |
| ROLE_LADDER.peer_level | DERIVED: the level immediately COARSER than the role's own scope_level, so a role is never compared with its own subordinates. Where the role owns the top level, the peer set is EMPTY and no peer comparison is attempted, per SD-SPN-15. | The peer group for each role was not stated, so each role is compared with others owning the same kind of thing one level up. Nobody is compared against their own subordinates. Where a role owns the whole organization, no peer comparison was attempted at all. |
| ROLE_LADDER.titles | DERIVED: the display name alone, normalized. | No alternative titles or abbreviations were recorded for a role, so only its own name resolves. A person whose title is written differently is asked once to pick their role from a list. |
| ROLE_LADDER.is_specialist | false for every role. | It is not recorded whether any role covers a subset of another role's units under direction, so no de-duplication discount was applied and no role was treated as both a reader and a subject. |
| ROLE_LADDER.has_reports_default | DERIVED: true for every role whose claim_tier is AGGREGATE, false otherwise. | Whether each role normally has direct reports was not stated, so it follows the direct-or-aggregate split. It is confirmed per person by the person-tier question rather than relied on. |
| REPORT_LINE_JUNIOR_KEY | The first line in DELIVERABLE_LINES. | Derived from the deliverable lines rather than stated. |
| REPORT_LINE_SENIOR_KEY | The second line in DELIVERABLE_LINES. | Derived from the deliverable lines rather than stated. |
| ROLE_FALLBACK_KEY | The narrowest role in ROLE_LADDER. | No fallback role has been set, so an unresolved title is treated as the narrowest role. This produces a shorter list and a narrower set of claims than a senior person is entitled to, which is the safe direction. |
| PEOPLE_LEADER_OBJECTIVE_REQUIRED | false. | It is not recorded whether people leaders must carry a leadership goal, so none was required or drafted for this user. |

---

## CONDITIONAL DEFAULTS AND NOTICES ONCE TRIGGERED, FOR THIS GROUP

Moved here from APPENDIX A2 for the same reason. The text is unchanged.

### Group 4: The role ladder

| Variable | Trigger | Documented default | Degradation notice |
|---|---|---|---|
| PEOPLE_LEADER_OBJECTIVE_SOURCE | PEOPLE_LEADER_OBJECTIVE_REQUIRED is true | None. The requirement is stated and no source document is cited. | A leadership goal is required here but the document defining it has not been named, so none was drafted from it. The requirement is named and left for you to fill. |
