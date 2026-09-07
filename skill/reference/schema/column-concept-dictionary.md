# GROUP 9: THE COLUMN CONCEPT DICTIONARY

TAXONOMY SHAPE, COLUMN_CONCEPT_DICTIONARY. A map from concept key to an entry
carrying:
- `stems`: normalized stems, each 4 characters or more where the language allows.
- `required`: boolean. Only three concepts are required for a source to be
  usable: the unit identifier, one ranking measure, and any one scope column.
- `value_check`: the predicate a resolved column's values must satisfy.
- `strict_exact_only`: true where a wrong resolution is a failure no downstream
  gate can catch. Such a concept never resolves by prefix or substring.
- `forbidden_neighbours`: CONCEPT KEYS in the same semantic neighbourhood that
  must never serve as a fallback. **This field holds concept keys and nothing
  else.** It is never a bare English word: an implementation reading it looks each
  entry up in the dictionary, and a word naming no concept refuses nothing. Where
  the thing to be refused is a level, a family or an idea rather than a concept,
  name the concept keys that carry it.
- `feeds`: which flags, gates, weights and benchmarks this concept supplies, so
  a resolved-but-empty column can be excluded from exactly those.
- `scale_read_from_data`: true where the column's own maximum decides whether it
  is a fraction or a points value.

Full seed contents and the runtime learning rule live in reference/field-resolution.md.

| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |
|---|---|---|---|---|---|---|
| COLUMN_CONCEPT_DICTIONARY | The concept-to-stems dictionary the parser resolves against. | ORG | DEFERRED | taxonomy | Exactly three REQUIRED CONCEPT GROUPS: the unit identifier, one of the ranking measures, and one of the scope columns. A group is satisfied when any member resolves. Two further concepts, the flow entry date and the flow stage, are required only when that population mode is FLOW. Every strict_exact_only entry names at least one forbidden_neighbour, and no stem appears in two concepts. | concept_unit_id; concept_measure_tier_1; concept_scope_branch |
| MIN_STEM_LENGTH | Below this normalized length, only an exact match counts. | ORG | DEFERRED | scalar | Integer at least 3. | 4 |
| CONTEXT_GROUPER_MAX_DISTINCT | The distinct-value count above which a categorical column is a label rather than a grouper, for the purpose of ordering the carried context block. | ORG | DEFERRED | scalar | Integer at least 2. Affects ORDER only, never membership. | 25 |
| FILE_QUESTION_BATCH_CAP | The maximum number of PERSON-tier file questions batched into the single question message a run may send. File questions do not count against the ORG deferred-request budget. | ORG | DEFERRED | scalar | Integer at least 1. Anything beyond the cap is reported as unasked rather than dropped. | 4 |
| IDENTIFIER_MIN_WIDTH | The character width at or above which an all-digit column of consistent length is read as an IDENTIFIER_OR_CODE rather than a COUNT_OR_MEASURE, where the values are not near-unique. | ORG | DEFERRED | scalar | Integer at least 3. Applies only to the all-digit rung of the value classifier; an alphanumeric pattern is an identifier at any width. | 5 |
| HEADER_SCAN_DEPTH | How many leading rows are scanned when detecting the header row. | ORG | DEFERRED | scalar | Integer between 5 and 30. | 15 |
| YEAR_PLAUSIBLE_RANGE | The inclusive year range within which a bare four-digit value is read as a DATE at year granularity rather than as an identifier, and only when testing a DATE concept. | ORG | DEFERRED | list | Two integers, low then high. The high bound is at least the current year. Applies only to date concepts; a numeric code tested for a non-date concept is never converted. | 1900; current year plus 5 |
| NULL_LIKE_VALUES | Literal strings treated as missing in addition to empty and whitespace. | ORG | DEFERRED | list | Compared case-insensitively after trimming. SEED. | null; none; n/a; #n/a; - ; tbd |
| ACTIVITY_BLOCK_TERMINATOR_CONCEPT | The concept key of the structural anchor that closes the block of work-item columns. | ORG | OPTIONAL | scalar | Matched EXACTLY, rightmost match wins. Never substring matched. | concept_row_total |
| ORIGINATOR_PREFIX_MAP | Map from a header prefix pattern to the origin of the work item. | ORG | OPTIONAL | taxonomy | Each entry has pattern, origin key, and separator_tolerant true. Optional metadata for weighting only, never an admission test. | central: to headquarters; local: to own_unit; L####: to another_unit |
| PROVISIONAL_ADOPTION_MIN_FILL | The non-null share, within scope, that a candidate column must carry before a run may adopt it PROVISIONALLY for a concept no stem matched. One of the six tests in reference/field-resolution.md 7.4a, and never sufficient on its own. | ORG | DEFERRED | scalar | Fraction between 0 and 1, and strictly above 0.5, because a column that answers fewer than half the rows in scope answers a different question from the one the concept asks. Never applied to a strict_exact_only concept, which is never adopted provisionally at all. | 0.60 |
| CONCEPT_LEARNING_ENABLED | Whether a run may add a newly learned stem to the dictionary and record it. | ORG | DEFERRED | scalar | Boolean. Should be true. | true |
| CONCEPT_LEARNING_LOG_PATH | Where learned stems are appended for the binding owner to review. | ORG | CONDITIONAL | scalar | Required when CONCEPT_LEARNING_ENABLED is true. A path variable, never a live URL. | LEARNED_STEMS_PATH |

---

---

## DEFERRED DEFAULTS AND DEGRADATION NOTICES FOR THIS GROUP

Moved here from APPENDIX A1 so that a variable, its documented default and
its exact degradation notice are never in three different places. The text
is unchanged.

### Group 9: The column concept dictionary

| Variable | Documented default | Degradation notice |
|---|---|---|
| COLUMN_CONCEPT_DICTIONARY | The seed dictionary in reference/field-resolution.md Part 6. | Column resolution used the shared starting dictionary rather than one built for your files. Every header that did not resolve is listed in the audit so it can be added once for everybody. |
| MIN_STEM_LENGTH | 4. | The standing short-string guard was used: a stem shorter than four characters matches only exactly. |
| CONTEXT_GROUPER_MAX_DISTINCT | 25 distinct values. | The point at which a categorical column stops being a grouping and starts being a label was not set, so twenty-five was used. It affects only the ORDER of the carried context columns, never which ones are carried, and the class of every candidate is printed beside its figures. |
| FILE_QUESTION_BATCH_CAP | 4 questions in one message. | The cap on file questions in a single message was not set, so four was used. File questions ask what something in your own file means and never what your organization's policy is, so they do not consume the configuration question budget. Anything beyond the cap is listed in the audit as unasked, with what it would have decided. |
| IDENTIFIER_MIN_WIDTH | 5 characters. | The width at which a column of digits is read as a code rather than a count was not set, so five was used. A column of digits narrower than that, whose values repeat, is read as a count; one that is near-unique across rows is read as a code whatever its width. Which reading each column took is named in the audit. |
| HEADER_SCAN_DEPTH | 15. | The standing header scan depth was used. The header row chosen and its runner-up are named in the audit. |
| YEAR_PLAUSIBLE_RANGE | 1900 to the current year plus 5. | The plausible year range was not set, so a generic one was used. A column of bare four-digit years is read as a date at YEAR granularity, which answers whether something falls before or after a window and answers nothing finer. Any value outside that range is treated as a code, not a year, so an ordinary numeric identifier is never turned into a date. |
| NULL_LIKE_VALUES | The seed set: null, none, n/a, hash-n-a, a bare hyphen, tbd. | No local null vocabulary is bound. If your files write missing values another way, those cells are read as real values; the distinct values of every grouping column are listed in the audit. |
| PROVISIONAL_ADOPTION_MIN_FILL | 0.60. | No fill threshold was set for provisionally adopting a column whose header this method did not recognize, so a standing one was used: at least sixty percent of the rows in scope must carry a value. It is one of six tests, all of which must pass, and every column adopted this way is named beside the figures it fed together with the share it carried. Nothing is adopted this way for a concept where a wrong answer would be invisible later, and nothing adopted this way is written into your configuration by a run. |
| CONCEPT_LEARNING_ENABLED | true. | Learning is on by default, so headers resolved by asking or by value check are proposed for the shared dictionary in the closing summary. |

---

## CONDITIONAL DEFAULTS AND NOTICES ONCE TRIGGERED, FOR THIS GROUP

Moved here from APPENDIX A2 for the same reason. The text is unchanged.

### Group 9: The column concept dictionary

| Variable | Trigger | Documented default | Degradation notice |
|---|---|---|---|
| CONCEPT_LEARNING_LOG_PATH | CONCEPT_LEARNING_ENABLED is true and a header is learned | A learned-stems file under the scratch directory, reported in the closing summary rather than persisted to a shared location. | No location was set for learned column names, so they are reported to you at the end of the run instead of being stored. Paste them into the configuration to stop the next person meeting the same unresolved header. |
