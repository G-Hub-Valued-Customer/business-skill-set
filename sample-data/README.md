# Sample data

Two datasets ship here: `insurance-agency/` and `facilities-services/`.

Both are datasets the skills were actually driven against, end to end, and the traps
described in each `DATASET.md` were verified caught by measurement rather than by reading a
change log.

`insurance-agency/` is the one three workflows were driven against, in four separate
adversarial test rounds. `facilities-services/` is the one the recurring briefing was built
against, at two altitudes from the same files with nothing configured between the runs, and
its artifacts and the script that verifies them are in `sample-output/`.

## Why two, and why not six

The method was also acceptance tested against four other invented organizations: a
regional hospital system with no competitive category, a B2B software company with a
flowing pipeline, a consumer goods company launching a new category with no history, and
a restaurant chain. Those were PAPER tests. Each organization was specified in detail and
the method was walked through it by hand, at two and three altitudes, to find where the
rules broke. They found real defects and those defects were fixed.

But no CSV files were ever built for them. Shipping four more datasets here and describing
"what a correct run should surface" for each would be describing runs that never happened.
**The standard for a dataset in this folder is that it has measured answers behind it**,
and the second dataset is here because it now meets that standard rather than because the
bundle gained a fourth workflow.

The two also differ in a way that was worth having. The insurance dataset feeds workflows
whose artifact is a workbook or a document, which can ship degraded and explain itself in a
Method tab. The facilities dataset feeds a workflow whose artifact is a message that arrives
unasked at five in the morning, with no reader present to ask and no tab to open. Several
rules that read as preferences in the first medium are gates in the second, and only a
dataset in that medium shows which.

## Bringing your own

Nothing about the method is specific to insurance or to facilities. It binds to any
organization that tracks a measure it cares about, has supervisors who set direction, and
has a headquarters that publishes priorities. Point a workflow at your own files and answer
the first-run questions.
