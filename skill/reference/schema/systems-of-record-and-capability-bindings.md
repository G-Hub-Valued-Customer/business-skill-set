# GROUP 23: SYSTEMS OF RECORD AND CAPABILITY BINDINGS

Every entry here is a NAME. No live host, path, endpoint, drive id or document
number ever appears as a value in skill text. The binding interview records the
value; the skill text references only the variable.

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| SOURCE_WORKBOOK_NAME | What the business calls the periodic tabular file the skills parse. | ORG | DEFERRED | scalar | A name, never a path. | branch work file |
| SOURCE_WORKBOOK_LOCATIONS | Ordered variable names of the places the source file is looked for. | ORG | DEFERRED | list | Ordered. Each entry is a variable name. | UPLOAD_DIR; USER_DRIVE_PATH; MAIL_ATTACHMENT |
| DOC_STORE_NAME | The document store the skills read reference material from. | ORG | OPTIONAL | scalar | A name. | the document store |
| DOC_STORE_SITE_VARIABLE | The variable holding the site or container identifier, resolved at run time. | ORG | OPTIONAL | scalar | A variable name. Never a literal id. | DOC_SITE_ID |
| DOC_STORE_LIBRARY_VARIABLE | The variable holding the library identifier. | ORG | OPTIONAL | scalar | A variable name. | DOC_LIBRARY_ID |
| DOC_STORE_PATH_DISCOVERY_REQUIRED | Whether folder paths are discovered by reading the folder list every run rather than hard-coded. | ORG | DEFERRED | scalar | Boolean. Must be true. Reference values are a starting point for discovery only. | true |
| MAIL_SYSTEM_NAME | The mailbox the priority sweep reads. | ORG | OPTIONAL | scalar | A name. | the mailbox |
| MAIL_SWEEP_FOLDERS | Which folders the sender sweep covers. | ORG | DEFERRED | list | Must include the deleted-items equivalent. | inbox; archive; deleted items; all subfolders |
| DIRECTORY_SELF_LOOKUP | The variable naming the call that returns the running user's own record. | ORG | OPTIONAL | scalar | A variable name. | DIRECTORY_API_SELF |
| DIRECTORY_MANAGER_LOOKUP | The variable naming the call that returns the manager relationship. | ORG | OPTIONAL | scalar | A variable name. A profile card that carries no manager field can never answer this question. | DIRECTORY_API_MANAGER |
| CHAT_PLATFORM_NAME | The messaging platform crawled for evidence. | ORG | OPTIONAL | scalar | A name. | the chat platform |
| SYSTEM_OF_RECORD_EXCLUSIONS | Capabilities owned by a downstream system that this bundle must not duplicate. | ORG | DEFERRED | list | Each entry names the capability and the owning system by variable. | routing and scheduling, owned by SCHEDULING_SYSTEM |
| SIBLING_SKILLS | Requests routed away from this bundle. | ORG | DEFERRED | mapping | Each key is a request shape, each value a destination. | spreadsheet editing to the spreadsheet skill; document formatting to the document skill |
| EVIDENCE_SOURCES | The ordered tiers of the evidence crawl. | ORG | DEFERRED | taxonomy | Each tier has key, source, and the condition under which it runs. Widening happens only on a stated trigger. | tier1 sent mail; tier2 received mail naming the user; tier3 chat, calendar, authored files; tier4 widen on request |
| DOWNLOAD_DIR | Where fetched attachment bytes land. | ORG | DEFERRED | scalar | Under SCRATCH_DIR. | SCRATCH_DIR/downloads |
| FORBIDDEN_RETRIEVAL_PATHS | Retrieval approaches that look reasonable and fail, at least one of which fails silently. | ORG | DEFERRED | list | Each entry names the path and how it fails. | field-selected fetch (rejects); expand-in-list (hits the ceiling); metadata-only call (never returns bytes); raw-value read decoded as text (silently corrupts) |
| INLINE_FETCH_CEILING | Response size ceiling on the fallback inline retrieval path. | ORG | OPTIONAL | scalar | Positive integer, in characters. | 102400 |
| MIME_ENCODING_FACTOR | Ratio of an encoded attachment size to the real file size, so a size field is never used to decide a file is too big. | ORG | OPTIONAL | scalar | Greater than 1. | 1.4 |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 23: Systems of record and capability bindings

| Variable | Documented default | Degradation notice |
|---|---|---|
| SOURCE_WORKBOOK_NAME | Whatever file was supplied or found. | The name of your periodic source file is not recorded, so the run used the file it found. The file used, its record count and the container within it are named in the audit. |
| SOURCE_WORKBOOK_LOCATIONS | Upload directory, then the user's own drive, then a supplied attachment. | The places to look for your source file are not recorded, so the standing locations were searched in order and the one that answered is named. |
| DOC_STORE_PATH_DISCOVERY_REQUIRED | true. | Reference folders are discovered by reading the folder list every run rather than by a stored path, which is the only permitted setting. |
| MAIL_SWEEP_FOLDERS | Every folder the mailbox exposes, including the deleted-items equivalent. | The folders to sweep are not recorded, so every folder available was swept and the folders covered are named with the message counts. |
| SYSTEM_OF_RECORD_EXCLUSIONS | Empty. | No downstream system has been named as owning a capability this toolkit must not duplicate, so nothing was withheld on that ground. If something here duplicates a system you already run, tell the binding owner. |
| SIBLING_SKILLS | Empty. | No routing to other tools is recorded, so a request outside this toolkit's scope is declined rather than redirected. |
| EVIDENCE_SOURCES | Sent messages across the period, then messages naming the user, then calendar and authored files, then widen on request. | The evidence tiers have not been bound, so the standing crawl was used and the tiers actually reached are named with their counts. |
| DOWNLOAD_DIR | A downloads folder under the scratch directory. | The standing download location was used. |
| FORBIDDEN_RETRIEVAL_PATHS | The standing four: a field-selected fetch, an expand-in-list fetch, a metadata-only call, and a raw-value read decoded as text. | The standing forbidden list was honoured. If your stack has a fifth path that fails silently, tell the binding owner before it corrupts a retrieval. |
