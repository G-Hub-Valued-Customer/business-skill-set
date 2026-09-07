# Sample data

One dataset ships here: `insurance-agency/`.

It is the dataset the skills were actually driven against, end to end, in four separate
adversarial test rounds, and the traps described in its `DATASET.md` were verified caught
by measurement rather than by reading a change log.

## Why only one, stated plainly

The method was also acceptance tested against four other invented organizations: a
regional hospital system with no competitive category, a B2B software company with a
flowing pipeline, a consumer goods company launching a new category with no history, and
a restaurant chain. Those were PAPER tests. Each organization was specified in detail and
the method was walked through it by hand, at two and three altitudes, to find where the
rules broke. They found real defects and those defects were fixed.

But no CSV files were ever built for them. Shipping four datasets here and describing
"what a correct run should surface" for each would be describing runs that never
happened. The one dataset present is the one with measured answers behind it.

## Bringing your own

Nothing about the method is specific to insurance. It binds to any organization that
tracks a measure it cares about, has supervisors who set direction, and has a
headquarters that publishes priorities. Point a workflow at your own files and answer the
ten first-run questions.
