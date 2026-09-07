# GROUP BRD: BREADTH AND DERIVED ANALYSIS

### SD-BRD-01 A derived analysis section never touches the ranking, and says so
- Rule: breadth of adoption and allocation of time are different questions. Keep
  them separate and say so on the section and in the audit.
- Source: P-D282
- Applies: PLANNING, SCORECARD

### SD-BRD-02 Know what your measure actually measures
- Rule: a measure derived from throughput is not a physical audit. A unit that
  holds the full range but moves little registers low even though the thing is
  present. "Ranking on satisfaction percentage alone produces false gaps and sends
  people to sell in something that is already there."
- Prevents: mistaking a velocity problem for a distribution problem.
- Source: P-D283
- Applies: PLANNING, REVIEW, SCORECARD

### SD-BRD-03 Where the method breaks its own rule, it says so and gives the reason
- Rule: this section carries the ONLY size floor left in the method. Keep it at
  BREADTH_FLOOR_FRACTION, computed with floor and never round or ceiling "so two
  implementations never differ by one unit", with a boundary tie-break on the
  identifier ascending. State the departure in the audit so the two are never
  mistaken for an inconsistency.
- Mechanism: "deliberately stricter than the action lists, which carry no floor at
  all, because a breadth recommendation only pays at genuine scale." Without it
  the list fills with small units that carry few items because they are small.
- Source: P-D284
- Applies: PLANNING, SCORECARD

### SD-BRD-04 A peer norm and a scope median use DIFFERENT populations by design, and both are stated
- Rule: the peer norm is the median count among units clearing this section's own
  floor, counting only units with a non-zero count. The intensity median is
  computed over in-scope units with a non-zero count, not over all in-scope units
  and not only over those above the floor.
- Mechanism: "Bigger units carry more, so comparing a big unit to the whole-scope
  median understates the gap." And: "Units with no items have no intensity value
  and cannot enter a median of one."
- Source: P-D285
- Applies: PLANNING, SCORECARD

### SD-BRD-05 Evaluate classification rules in order, stop at the first match, and say which overrides which
- Rule: "the first rule overrides the others, so a unit well below the range is an
  Add regardless of how slowly it moves."
- Source: P-D287
- Applies: PLANNING, SCORECARD

### SD-BRD-06 Show the upside arithmetic so it can be checked
- Rule: one named formula per play, using the same figure the classification
  compares against.
- Source: P-D288
- Applies: PLANNING, SCORECARD

### SD-BRD-07 Context columns are ordered by KIND before they are ordered by any count
- Rule: where columns are carried beside a ranking to help the reader decide what
  to do, order them by WHAT KIND OF THING THEY ARE first, and only then by any
  numeric key. A raw distinct-value count compares two kinds of usefulness that are
  not comparable, and it rewards the wrong one.
- The named case: a column of tenure years carried 28 distinct values and a column
  of line of business carried 8, so the year column outranked the line of business
  in the carried block. Distinct count is a proxy for DISCRIMINATION, not for
  USEFULNESS: a year tells a reader almost nothing about what to do with a row,
  while the line of business tells them what kind of conversation to have. The key
  was deterministic and defensible and it ordered by accident.
- Mechanism, the CLASS ORDER, applied before every other key:
  1. **QUANTITIES THE READER DECIDES WITH.** Shape token COUNT_OR_MEASURE or
     RATE_OR_PROPORTION. These are per-row facts about the unit and they are what a
     reader reaches for first.
  2. **GROUPERS.** Shape token STATUS_OR_CATEGORY or BOOLEAN_LIKE, with a distinct
     count of at least two and no more than CONTEXT_GROUPER_MAX_DISTINCT. These say
     what KIND of thing this row is, which is what decides the approach to it.
  3. **DATES.** Shape token DATE. Useful, and rarely the first thing a reader needs.
  4. **EVERYTHING ELSE**, including free text, identifiers, and any column that
     would be a grouper except that its distinct count exceeds the grouper maximum,
     which makes it a label rather than a group.
- Rule: WITHIN a class, apply the existing keys unchanged and in the existing
  order: fill rate descending, then distinct value count descending, then position
  in the source ascending. The third key still makes the whole order TOTAL, so two
  runs over one file carry the same columns in the same order.
- Rule: print the CLASS beside the fill rate and distinct count for every
  candidate, carried and not carried. A reader who disagrees with the order can see
  exactly which rule produced it.
- Rule: this changes ORDER only. It changes no membership test, no cap, and nothing
  about the block being carried and never scored. A column that did not qualify does
  not qualify now.
- Prevents: a bounded context block spending its last slot on the least useful
  qualifying column because that column happened to hold many distinct values.
- Source: release acceptance run, N10
- Applies: PLANNING, SCORECARD

---
