# GROUP 19: THE BREADTH SECTION

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| BREADTH_COUNT_CONCEPT | The concept key holding how many distinct things a unit has adopted. | ORG | OPTIONAL | scalar | A COUNT, never a percentage. | concept_items_carried |
| BREADTH_SATISFACTION_CONCEPT | The concept key holding the percentage of the available range satisfied. | ORG | OPTIONAL | scalar | Scale read from the column's own maximum. | concept_range_satisfaction |
| BREADTH_ADMISSION_IS_THE_PAIR | Whether the section is built only where BOTH a count and a percentage resolve. | ORG | DEFERRED | scalar | Boolean. Must be true. The pair is the admission test, not the entity name. | true |
| BREADTH_FLOOR_FRACTION | The size floor for this section, expressed as a fraction of the ranked population kept. | ORG | CONDITIONAL | scalar | Between 0 and 1. Computed with floor, never round or ceiling, so two implementations never differ by one unit. Required when the section is enabled. | 0.3333 |
| BREADTH_FLOOR_DEPARTURE_STATEMENT | The sentence stating that this section deliberately carries a size floor the ranked lists do not. | ORG | CONDITIONAL | scalar | Required when the floor is bound. | This section is deliberately stricter than the ranked lists, because a breadth recommendation only pays at genuine scale. |
| MIN_BREADTH_GAP | The smallest gap below the peer norm worth reporting. | ORG | CONDITIONAL | scalar | Positive integer. | 2 |
| INTENSITY_PER_ITEM_CONCEPT | The concept key or derivation for usage divided by breadth. | ORG | OPTIONAL | scalar | Numerator and denominator period tokens must match, or the result is directional and both tokens are stated. | measure divided by breadth count |
| PLAY_RULES | The ordered classification rules, first match wins, with the override order stated. | ORG | CONDITIONAL | taxonomy | Each rule has key, test, label, and upside_formula. Evaluated in order. | below half the range means Add; above the range with low intensity means Drive usage |
| PLAY_LABELS | Display labels for the plays. | ORG | CONDITIONAL | list | One per rule. | Add items; Drive usage |
| BREADTH_SORT_KEYS | Mandatory sort for the section. | ORG | CONDITIONAL | list | Must sort by estimated value descending, never by the classification label, and must end with the unit identifier. | upside desc; measure desc; unit id asc |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 19: The breadth section

| Variable | Documented default | Degradation notice |
|---|---|---|
| BREADTH_ADMISSION_IS_THE_PAIR | true. | The breadth section is built only where both a count and a percentage resolve, which is the only permitted setting. Where they did not, the section ships with one row saying so. |

---

## CONDITIONAL DEFAULTS AND NOTICES ONCE TRIGGERED, FOR THIS GROUP

Moved here from APPENDIX A2 for the same reason. The text is unchanged.

### Group 19: The breadth section

| Variable | Trigger | Documented default | Degradation notice |
|---|---|---|---|
| BREADTH_FLOOR_FRACTION | both breadth concepts resolve and the section is built | One third, computed with floor rather than round or ceiling. | No size floor was set for the breadth section, so a standing one third was used, computed with floor so two runs never differ by one unit. The departure from the no-floor rule elsewhere is stated in the method section. |
| BREADTH_FLOOR_DEPARTURE_STATEMENT | as above | The standing sentence explaining that this section is deliberately stricter than the ranked lists because a breadth recommendation only pays at genuine scale. | The explanation of why this section carries a floor when nothing else does was not written for your organization, so a standing one is printed. |
| MIN_BREADTH_GAP | as above | 2. | No minimum reportable gap was set, so a standing one was used and gaps below it are not listed. |
| PLAY_RULES | as above | Two ordered rules: below half the available range is an add, and at or above the range with intensity below the median is a use-what-is-there. First match wins. | The classification rules for this section were not set, so the standing two were used, evaluated in order, and the rule that fired is named on each row. |
| PLAY_LABELS | PLAY_RULES fires | Add items; Drive usage. | The labels for this section's recommendations were not set, so generic ones were used. |
| BREADTH_SORT_KEYS | the section is built | Estimated value descending, then the measure descending, then the identifier ascending. | The sort for this section was not set, so a standing one was used. It sorts by estimated value and never by the classification label, because sorting on a label inverts the value order. |
