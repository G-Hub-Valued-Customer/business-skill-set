# GROUP 2: ORGANIZATION IDENTITY

The three enterprise entries below hold CACHED COPIES of published content, each
behind a validity date in REFERENCE_VALIDITY_PERIODS. A cached copy is
subordinate to its live source: past its validity date it is refetched, or used
and marked stale in the output. It is never the authority a run scores against.
See standing rule S8.

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| ORG_NAME | The parent enterprise the method runs inside. | ORG | IGNITION | scalar | Non-empty. | Northgate Commercial Insurance |
| ORG_SHORT_NAME | The abbreviation used in headings and filenames. | ORG | OPTIONAL | scalar | No spaces. Falls back to ORG_NAME. | Northgate |
| OPERATING_UNIT_NAME | The division whose operating population this bundle serves. | ORG | DEFERRED | scalar | Non-empty. | Commercial Claims |
| OPERATING_UNIT_LONG_NAME | Full legal or formal name of the operating unit. | ORG | OPTIONAL | scalar | Non-empty if present. | Northgate Commercial Claims Services |
| ORG_PURPOSE_STATEMENT | The enterprise purpose line, cited as the top rung of the lineage ladder. | ORG | OPTIONAL | scalar | One sentence. | Keep working businesses working after a loss. |
| ORG_VISION_STATEMENT | The enterprise vision line. | ORG | OPTIONAL | scalar | One sentence. | Settle right, settle once. |
| ENTERPRISE_STRATEGY_PILLARS | The current strategic pillars a claim may ladder to. | ORG | DEFERRED | taxonomy | 2 to 8 entries. Each has a stable id and a name. | Cycle-time reduction; Leakage control; Adjuster capability; Digital intake |
| ENTERPRISE_LONG_TERM_GOALS | The multi-year goal set with its horizon year. | ORG | OPTIONAL | taxonomy | Horizon year is in the future when bound. | Severity flat to 2029; 60 percent digital first notice by 2028 |
| ENTERPRISE_FINANCIAL_TARGETS | Named corporate financial goals available as lineage targets. | ORG | OPTIONAL | list | Each entry names a metric and a target. | Combined ratio at or below 94 |
| ORG_AI_USE_POLICY_REFERENCE | The name of the sanctioned assistance policy, cited when the artifact discloses machine assistance. | ORG | OPTIONAL | scalar | Non-empty if present. | Assisted Drafting Standard |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 2: Organization identity

| Variable | Documented default | Degradation notice |
|---|---|---|
| OPERATING_UNIT_NAME | ORG_NAME. | The operating division has not been named, so reports are headed with the organization name and cannot distinguish two divisions using this toolkit. |
| ENTERPRISE_STRATEGY_PILLARS | Empty. The top rung of the lineage ladder resolves to nothing. | No enterprise strategy has been bound, so no claim in this report was laddered to a company priority. Claims cite the highest rung that could be resolved and no higher. |
