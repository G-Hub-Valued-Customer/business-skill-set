# Field Deployment Reference

A company-neutral specification of a production bundle: eight agent skills, a routing hub,
a one-time setup flow and a test plan, built for and run by the field sales organization of
a national consumer goods manufacturer.

**This is a specification, not a runnable skill.** Nothing here executes. The runnable part
of this repository is `skill/`, which is a separate and smaller thing: four workflows that
run end to end and produce the files in `sample-output/`. Read that first if you want to
judge whether the method works. Read this if you want to see what the method looks like
deployed at scale against a real enterprise data estate.

## Why it is here

`skill/` states plainly in its own honest limits that it does not integrate with anything:
it reads files and published documents and writes a file. That is deliberate and it is what
makes it portable. This directory is the other half of the picture. It documents what the
same judgment looks like wired into a CRM, a data warehouse, a shelf-recognition model, a
photo capture platform and a managed pricing application, with a router over eight skills
and a scheduled job that runs unattended every weekday.

## What is in it

| File | What it specifies |
|---|---|
| `00-conventions-and-placeholders.txt` | How to read the set, the placeholder convention, and the full glossary. Start here. |
| `01-hub-router-and-scope.txt` | The entry point: routing a request to one skill, resolving who is asking from the login and what they own, and opening every answer with a scope line. |
| `02-contract-compliance-audit.txt` | Scores what is physically on the fixture in a store's latest shelf photo against the contract level the store is assigned, and resumes from the first unscored store after any interruption. |
| `03-top-opportunity-accounts.txt` | Builds a prioritized visit list from the cycle's planning workbook, weighted against the supervisor's stated focus and headquarters priorities. |
| `04-pos-gap-scorecard.txt` | A point-of-sale presence scorecard built from a recognition model without opening a photo, with a failure code in the row margin for every miss. |
| `05-performance-write-up-concierge.txt` | Objective setting, mid-period tracking and completed review sections written from the user's own evidence, claiming nothing that cannot be evidenced. |
| `06-label-sheets.txt` | Print-ready out-of-stock placeholder labels carrying a real scannable UPC-A of the reorder unit, registered to die-cut stock. |
| `07-pricing-audit.txt` | Retailer margin on our items against the lowest-margin competitive item per store and category, net of cost, allowances and competitor buy-downs, run from chat. |
| `08-pricing-opportunity-agent.txt` | The managed application the audit runs on: how it is built, seeded, repaired and ported, and how its engine is proved field for field by regression against a reference implementation. |
| `09-daily-brief-and-cycle-autopilot.txt` | A scheduled autopilot: every weekday a phone-friendly brief of the day's planned visits, every Saturday a rebuild of the cycle's per-store content, and a two-line failure email when a step fails. |
| `10-photo-bridge-flow.txt` | The one-time plumbing that moves photos from a capture platform into shared storage so the audit can reach them. |
| `11-test-plan.txt` | Ten numbered tests with pass lines and no answer key. |

## How it was genericized

Every step, decision rule, input, output, tie-breaker, failure path and verification step of
the original is preserved in its original order. Every company-specific detail is replaced by
a placeholder in angle brackets: 323 distinct placeholders across roughly 4,100 instances.

Mechanically verified: no company name, brand name, competitor name, person, geography,
system identifier, document number, store identifier, endpoint, URL or email address appears
anywhere in this directory, and every file is ASCII.

Numbers that describe the METHOD are kept as written, because they are the design: list
shapes, the thirteen-week business window, the Saturday refresh, 1.7 minutes per store for
photo scoring, time caps, retry counts, page sizes. Numbers that describe the BUSINESS are
placeholders: contract thresholds, facing counts, allowance amounts, price points.

Code is removed. Each helper script appears as Purpose, Inputs, Outputs, Logic in plain
numbered steps, and Checks and failure handling. Test fixtures are described as sample rows
and never reproduced.

Microsoft platform names are kept, because the workflows run on that platform and removing
them would make the specification unreadable. Generic retail and merchandising vocabulary is
kept, because any consumer goods sales organization uses it.

## Turning a part back into a skill

Write that part's steps in the imperative for the assistant, supply the parameters listed in
its header block, and test against `11-test-plan.txt`. Every part opens with the same five
lines: Purpose, Triggers, Inputs, Outputs, and Parameters to Fill In.

Be warned that the parameter burden is real. 323 placeholders is thorough rather than
convenient, and an organization whose shape differs from five product categories and five
operating units is doing surgery rather than filling in blanks.

## License

MIT, same as the rest of the repository. The MIT License grants copyright permissions only.
No patent license is granted, and the author's pending applications covering related subject
matter are expressly reserved.
