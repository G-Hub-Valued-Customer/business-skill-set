# GROUP 12: LINEAGE AND CLAIMS

TAXONOMY SHAPE, LINEAGE_LADDER. Ordered rungs, highest altitude first. Each
rung carries `key`, `display_name`, `source_variable` naming where that rung's
content is read from, and `requires_weight_named` for rungs whose content
carries a published weight.

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| LINEAGE_LADDER | The authority ladder a claim resolves as high up as the evidence defends. | ORG | DEFERRED | taxonomy | Between 3 and 7 rungs. Depth is configurable, never fixed. Rung 1 is enterprise strategy; the last rung is the individual's own objective. | L1 enterprise goal; L2 incentive metric; L3 district objective; L4 supervisor priority; L5 own objective |
| CONTRIBUTION_VERBS | Verbs permitted when a claim cites a rung above the role's own scope. | ORG | DEFERRED | list | Non-empty. Ports verbatim across businesses. | advances; supports; contributes to |
| OWNERSHIP_VERBS | Verbs forbidden when a claim cites above the ceiling. | ORG | DEFERRED | list | Non-empty and disjoint from CONTRIBUTION_VERBS. | achieved; delivered; drove; led; owned |
| CLAIM_PART_ORDER | The four parts of a claim, in order. | ORG | DEFERRED | list | Exactly: action; result; proof; consequence. | action; result; proof; consequence |
| PROOF_ACCEPTED_FORMS | What may fill the proof slot. | ORG | DEFERRED | list | At least one entry. Must include the counterfactual denominator. | counterfactual denominator; peer rank with tie count |
| SUPERLATIVE_REQUIRES_TIE_COUNT | Whether a superlative may ship without a verified count of peers at the same value. | ORG | DEFERRED | scalar | Boolean. Must be true. | true |
| ANONYMITY_FLOOR | Below this peer count, generalize rather than rank, because a positional claim identifies a person by elimination. | ORG | DEFERRED | scalar | Integer at least 3, **AND AT LEAST MIN_POPULATION_FOR_NORM**, mirroring the relation MIN_POPULATION_FOR_RANKING already carries. **THE PAIR RULE, STATED HERE ONCE: an outward walk that stops at the first level meeting this floor and no other lands on a set that can be RANKED and cannot be COMPARED, because a set of exactly this size sits below the norm floor whenever the two are set apart. The walk therefore stops at the first level whose count is at or above BOTH floors, and the two defaults are set EQUAL so a shipped configuration cannot land in the gap.** A binding owner who lowers this one below the norm floor is rejected at validation rather than silently given a set that carries a rank and no comparison. | 5 |
| NAMED_THIRD_PARTIES_ALLOWED | Whether any third party may be named in a claim. | ORG | DEFERRED | scalar | Boolean. Must be false, including indirect identification. | false |
| ATTRIBUTION_TEAM_PHRASES | Phrasing used when the evidence shows a direct report performed the work. | ORG | DEFERRED | list | Non-empty. | the team executed; I directed; the branch delivered |
| ILLUSTRATION_RULE_ENABLED | Whether an aggregate-tier claim may name one unit as an illustration with credit staying with the team. | ORG | DEFERRED | scalar | Boolean. | true |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 12: Lineage and claims

| Variable | Documented default | Degradation notice |
|---|---|---|
| LINEAGE_LADDER | A three-rung ladder: your supervisor's stated priority, your own objective, and nothing above them. | No authority ladder has been bound above your own supervisor, so no claim in this report is connected to a company priority. Claims are worded at the level they could actually be defended. |
| CONTRIBUTION_VERBS | advances, supports, contributes to. | The standing contribution verbs were used to word any claim above your own scope. |
| OWNERSHIP_VERBS | achieved, delivered, drove, led, owned. | The standing ownership verbs were used, and none of them appears in a claim above your own scope. |
| CLAIM_PART_ORDER | action, result, proof, consequence. | The standing claim shape was used. |
| PROOF_ACCEPTED_FORMS | The counterfactual denominator, and a peer rank with its tie count. | The standing proof forms were used. |
| SUPERLATIVE_REQUIRES_TIE_COUNT | true. | Every superlative carries a verified tie count, which is the only permitted setting. |
| ANONYMITY_FLOOR | **5, WHICH IS DELIBERATELY EQUAL TO MIN_POPULATION_FOR_NORM AND NOT ONE BELOW IT.** An earlier revision shipped 4 against a norm floor of 5. An outward walk stops at the first level meeting the anonymity floor, the smallest set meeting a floor of 4 is 4, and 4 is below 5, so the shipped defaults sent every walk to a set that could be ranked and could not be compared: the level-delta band computed and then had every label it exists to emit withheld. Two defaults one apart, with a rule that stops in the gap. They are now equal, and the validation forbids setting this one below the norm floor. | The standing anonymity floor was used: below five peers, this report generalizes rather than ranks, so a positional claim cannot identify a colleague by elimination. It is set equal to the smallest population this report will draw a comparison from, so a peer set that is large enough to name a position is also large enough to compare against; if you lower one of the two, lower both or the comparisons go silent. |
| NAMED_THIRD_PARTIES_ALLOWED | false. | No third party is named anywhere, which is the only permitted setting. |
| ATTRIBUTION_TEAM_PHRASES | the team delivered, I directed, the team executed. | The standing team-credit phrasing was used for work performed by someone who reports to you. |
| ILLUSTRATION_RULE_ENABLED | true. | A named unit may appear as an illustration inside an aggregate claim, with the credit staying with the team. |
