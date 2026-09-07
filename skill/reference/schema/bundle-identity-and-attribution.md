# GROUP 1: BUNDLE IDENTITY AND ATTRIBUTION

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| BUNDLE_VERSION | Version stamp of the bound bundle. | ORG | DEFERRED | scalar | Matches a major.minor pattern. | 3.1 |
| BUNDLE_VERSION_DATE | Date the binding was last changed. | ORG | DEFERRED | scalar | A valid ISO date, not in the future. | 2026-09-04 |
| BINDING_OWNER_NAME | The person who bound the ORG tier and receives tuning requests. | ORG | IGNITION | scalar | Non-empty. | Director of Field Operations |
| BINDING_OWNER_CONTACT | The address printed in every generated artifact, so a reader can reach whoever can fix what the report could not do. | ORG | DEFERRED | scalar | Contains one at-sign and one dot after it. **NOT IGNITION, and the reason is stated in the ignition table above: it is the one ignition candidate that a documents-only binding can never satisfy, because no policy document carries a mailbox.** | fieldops at example-hvac.test |
| BINDING_LOCKED | Whether the ORG tier is closed to further edits from a run. | ORG | DEFERRED | scalar | Boolean. True after the ORG interview completes. | true |
| METHOD_OWNER_STATEMENT | Two sentences printed in every artifact: what the method computed from the user's own data, and what was supplied as a binding. | ORG | DEFERRED | scalar | 2 sentences, plain business language, no jargon. | Thresholds in this report were computed from your own service area. Local pricing and permit rules are inputs this method does not assume. |
| TUNING_INVITATION | The standing invitation to raise a calibration request, printed with the contact line. | ORG | DEFERRED | scalar | Names at least one category of adjustable value. | Peer norms, cadence floors and program benchmarks can be re-tuned on request. |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 1: Bundle identity and attribution

| Variable | Documented default | Degradation notice |
|---|---|---|
| BUNDLE_VERSION | The literal string "unversioned". | This configuration carries no version stamp, so two reports built weeks apart cannot be compared for method changes. |
| BUNDLE_VERSION_DATE | The date the config file was last written. | The binding date is inferred from the file timestamp, not recorded, so it may not reflect when the answers were actually given. |
| BINDING_OWNER_CONTACT | EMPTY. No address is invented, and no address is inferred from a name, a domain or another document, per SD-CNF-07. MSG_AUTHOR_LINE prints the owner's NAME and ROLE with no address, and the standing disclosure below is printed at the same prominence on every run until an address is bound. Binding authority is UNAFFECTED: it is computed from BINDING_OWNER_NAME and the standing senior-role grant, so every deferred question still fires and still finds an authorized answerer. | No address is recorded for whoever owns this configuration, so the invitation in this report names a person or a role and no way to reach them. Everything this run could not determine is still listed, still routed to an authorized answerer, and still asked once when somebody with authority next runs the tool; what is missing is the ability to post a notice to them between runs. One line fixes it, and it is the highest-value line in this configuration. |
| BINDING_LOCKED | false, meaning the org tier is still open and any deferred question may fire. | The organization tier is not locked, so this run may ask for organization settings it needs; answers are recorded and not asked again. |
| METHOD_OWNER_STATEMENT | A generic statement: thresholds in this report were computed from your own data, and local commercial rules were not assumed. | No organization-specific statement of what was computed and what was supplied has been set, so a generic one is printed. |
| TUNING_INVITATION | A generic invitation naming peer norms, cadence floors and program benchmarks as adjustable. | No organization-specific tuning invitation has been set, so a generic one is printed. |
