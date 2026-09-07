# HOW THE DEFAULTS AND NOTICES ARE ORGANIZED

Each group file carries its own defaults and notices. These two preambles are
the framing text that stood above them, kept verbatim.

## APPENDIX A1: DEFERRED DEFAULTS AND DEGRADATION NOTICES


Every DEFERRED variable, its documented default when unbound, and the exact
degradation notice printed in the artifact. A CONDITIONAL variable whose trigger
condition is met behaves identically to a DEFERRED one and uses the same two
columns.

Reading the notices: every one names what was not determined and what was
therefore not attempted or was done differently. None of them says only that
something was missing. Where a notice would be identical for a group of
variables, it is still written per variable, because a notice that names three
things at once tells the reader nothing about which one to fix.

---

## APPENDIX A2: CONDITIONAL VARIABLES, DEFAULTS AND DEGRADATION NOTICES ONCE TRIGGERED


A CONDITIONAL variable is inert until its trigger condition is met. Once it is
met, it behaves exactly as a DEFERRED one and needs the same two columns. This
section supplies them. Until this section existed, forty-one variables could
trigger with no documented default and no notice, which is a direct failure of the
governing rule at the place it matters most.

Each row: the variable, what triggers it, the documented default once triggered,
and the exact notice.
