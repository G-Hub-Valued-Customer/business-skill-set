# GROUP 14: COMPLIANCE AND JURISDICTION

Everything in this group binds a LOCATION, a NAME or a per-run EFFECT. Nothing in
it binds a rule. The jurisdiction references are named so a run can find them and
read them again every run; their content is never copied into the config, because
a cached rule is a rule nobody notices going stale. See standing rule S8.

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| COMPLIANCE_CHECK_ENABLED | Whether priorities are validated against a jurisdiction reference before weighting. | ORG | DEFERRED | scalar | Boolean. | true |
| JURISDICTION_CONCEPT | The concept key holding the jurisdiction of a unit. | ORG | CONDITIONAL | scalar | Required when the compliance check is enabled. | concept_jurisdiction |
| JURISDICTION_NAME_TO_CODE | Map from the long name a person types to the short code the data stores. | ORG | CONDITIONAL | taxonomy | Each entry has long_name, code, and aliases. Conversion is by table, never by substring containment. Required when the check is enabled. | New Hampshire to NH; Rhode Island to RI |
| SUBREGION_SUFFIXES | Administrative suffixes stripped before matching, which also route the phrase to exactly one column. | ORG | OPTIONAL | list | Lowercased. | county; parish; borough; district |
| COMPLIANCE_GUIDE_SET | The jurisdiction-by-jurisdiction reference that says whether a priority may lawfully be executed. | ORG | CONDITIONAL | scalar | A name, never a path. Required when the check is enabled. | state practice bulletin set |
| COMPLIANCE_GUIDE_MASTER | The fallback reference when no jurisdiction-specific document exists. | ORG | CONDITIONAL | scalar | Required when the check is enabled. | national practice bulletin |
| COMPLIANCE_GUIDE_SUPPLEMENTS | Topic-specific restriction references consulted when a priority names that topic. | ORG | OPTIONAL | mapping | Topic to reference name. | independent adjuster licensing to licensing bulletin |
| COMPLIANCE_FINDINGS | The finding-to-effect table. | ORG | CONDITIONAL | taxonomy | Exactly five findings: permitted; restricted; permitted with condition; source unreachable; no document for the jurisdiction. Each names the effect on weight and on membership. Required when the check is enabled. | restricted means weight 0 and removal, with the rule named |
| COMPLIANCE_FAILS_CLOSED_ON | What a compliance gate fails closed on when the source is unreachable: THE VALIDATED ITEMS, whatever the running skill calls them, never the run. | ORG | DEFERRED | scalar | Must name the ITEMS the check would have validated, never the run or the deliverable. The item noun differs by skill, which is why this is stated as a role rather than as one skill's word: the items a planning run validates are its priorities, and the items a scorecard run validates are its requirements. An unreachable reference never withholds the deliverable in any skill. | validated_items |
| SHOWN_NEVER_SCORED_CONCEPTS | Concept keys whose values are printed with their benchmark and never scored, because their commercial meaning varies by jurisdiction. | ORG | OPTIONAL | list | Every entry is a concept key. | concept_price_alignment |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 14: Compliance and jurisdiction

| Variable | Documented default | Degradation notice |
|---|---|---|
| COMPLIANCE_CHECK_ENABLED | false. | No jurisdiction rules have been bound, so no priority in this report was checked against local restrictions. If something here cannot lawfully or contractually be done in a given place, this report does not know it. |
| COMPLIANCE_FAILS_CLOSED_ON | THE VALIDATED ITEMS, named by the running skill: the priorities in a planning run, the requirements in a scorecard run, the claims in a review run. Never the run itself. | An unreachable compliance reference holds back the individual items it could not validate, each of them named, and never withholds the report. That is the only permitted setting. An earlier default named one skill's item noun, which read as an instruction to hold back priorities in a document that has none. |

---

## CONDITIONAL DEFAULTS AND NOTICES ONCE TRIGGERED, FOR THIS GROUP

Moved here from APPENDIX A2 for the same reason. The text is unchanged.

### Group 14: Compliance and jurisdiction

| Variable | Trigger | Documented default | Degradation notice |
|---|---|---|---|
| JURISDICTION_CONCEPT | COMPLIANCE_CHECK_ENABLED is true | The jurisdiction concept in the seed dictionary. | The column holding jurisdiction was resolved from the shared dictionary rather than declared. Where none resolved, no compliance check ran and this report says so. |
| JURISDICTION_NAME_TO_CODE | a place name in a request must be matched against stored codes | Empty. Place names resolve only where they match the stored value exactly. | No mapping from the names your people say to the codes your data stores has been set, so a place name that does not match exactly returns the nearest values present rather than widening the report. |
| COMPLIANCE_GUIDE_SET | COMPLIANCE_CHECK_ENABLED is true | None. Every priority that would have been validated is HELD BACK and named. | The jurisdiction reference has not been named, so no priority could be validated against local rules. Every priority that needed validation was held back and is listed rather than silently permitted or silently dropped. |
| COMPLIANCE_GUIDE_MASTER | a jurisdiction-specific document does not exist | None. The finding for that jurisdiction is source unreachable, and its priorities are held back. | No fallback reference was named for a jurisdiction with no document of its own, so priorities in that jurisdiction were held back and named. |
| COMPLIANCE_FINDINGS | COMPLIANCE_CHECK_ENABLED is true and a finding must be acted on | The five standing findings: permitted; restricted, meaning weight zero and removal with the rule named; permitted with a condition, meaning the condition is printed; source unreachable, meaning held back; no document for the jurisdiction, meaning held back. | The effect of each compliance finding was not set for your organization, so the standing five were used. Every priority removed or held back is named with the finding that caused it. |
