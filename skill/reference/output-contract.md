# THE UNIVERSAL OUTPUT CONTRACT

**This file is the ONE statement of the output contract. Every skill CITES it and
none restates it.** A restated contract is how this one drifted the first time: the
formatting elements survived into an earlier bundle only as passing mentions, so
nothing enforced them, and a scorecard shipped with no autofilter on any sheet, no
rank column on its main sheet, no consolidated reason column and no cap, while a
planning workbook put a title banner in row 1 and pushed its headers to rows 4
through 6. Every one of those is a violation of a rule the bundle already contained
in prose. Prose is not a contract. A contract is a named element, a stated standard,
and a verification that runs before publication and blocks it on failure.

Where a skill appears to state one of these rules differently, THIS FILE GOVERNS and
the skill is stale.

---

# PART 1: THE OUTPUT MEDIUM IS KEYED PER SKILL

**There is no single output container for this bundle.** OUTPUT_MEDIUM is a mapping
from skill to medium, and a run reads its own entry. An earlier assumption that all
three skills emit the same container is what let one skill's section list and one
skill's artifact name become defaults for the others.

| Skill | Medium | Why that medium and not another |
|---|---|---|
| PLANNING | xlsx | A ranked worklist is sorted, filtered and worked column by column. It is a spreadsheet whatever else it is. |
| SCORECARD | xlsx | A census grid with one row per unit and one column per requirement is a spreadsheet by construction, and the reader isolates the failures with a filter. |
| REVIEW | docx | A review is read as prose and then COPIED, field by field, into a submission form. |

**PART 2 governs every xlsx-emitting skill. PART 3 governs the docx one.** A skill
reads the part that matches its medium and ignores the other.

---

# PART 2: THE FORMATTING ELEMENTS, UNIVERSAL AND MANDATORY FOR EVERY XLSX SKILL

**Every element is verified PROGRAMMATICALLY before publication, and a failure
BLOCKS publication.** They are not cosmetic, they are never traded for speed, and an
element that does not apply to a sheet scores NOT APPLICABLE, which is a pass. An
element scored not applicable is recorded as such with its reason; it is never
silently skipped.

**WHERE AN ELEMENT'S OWN TEXT NAMES THE CONDITION UNDER WHICH IT DOES NOT APPLY,
THAT CONDITION IS THE REASON, AND IT IS ALWAYS A QUALIFYING REASON.** Element 13
names one: a sheet with no elapsed-time column. A closed list of not-applicable
reasons kept anywhere else, in any skill, that cannot express an element's own stated
exemption is an INCOMPLETE LIST, and the workbook it rejects is not the thing at
fault. A skill carrying such a list makes it able to express, at minimum, the case
where the INPUT AN ELEMENT READS IS NOT PRESENT ON THE SHEET, named.

## 2.0 The sheet classes, because an element binds a CLASS and not a workbook

**Three classes, and every sheet in an xlsx artifact is exactly one of them.** The
class is DECLARED by the skill, per sheet, and the declaration is recorded on the
method sheet, so a reader can see which elements were expected to run where rather
than inferring it from what the verification happened to check.

| Class | What it is | What binds it |
|---|---|---|
| ENTITY SHEET | Any sheet carrying ONE ROW PER UNIT OF BUSINESS: an action tier, a census, an extract of a census, a reference tier, a directed sheet. | Elements 1 to 14 and 16, and R1 through R5 as PART 7.2 scopes them row by row. |
| REFERENCE TABLE | A grid whose rows are NOT units of business: a summary by scope unit, a legend emitted as a grid, a code table. | Elements 1 to 14 and 16, exactly as an entity sheet, and R1 through R5 as PART 7.2 scopes them row by row. R1 binds it in its POSITION-column form per 4.1; R2 does not, since it has no merit tiers. |
| PANEL SHEET | The front panel, the method sheet, and a legend emitted as PROSE rather than as a grid. It has no header row and no grid of units, and cell A1 is a title. | Elements 7, 15 and 16. **ELEMENT 7 REACHES A PANEL, AND THAT IS A CHANGE FROM AN EARLIER SCOPE:** its rule is a border on all four sides of every populated cell OF THE SHEET, a panel's cells are populated cells of a sheet, and there was never a reason a label cell should be bounded on an entity sheet and unbounded on a panel. Elements 1 to 6 and 8 to 14 are NOT APPLICABLE on it, with the sheet class as the stated reason. R3 and R5 still reach it: R3 wherever a panel's own row count is bounded, R5 because it scans the whole workbook apart from the one range 7.1 excludes from it. |

**THIS TABLE IS A SUMMARY AND 7.2 IS THE STATEMENT.** Where this table gives a scope
more loosely than the matrix row does, **THE MATRIX ROW GOVERNS**, because it is
written per row and this column is written per class. Two of the R rows are not scoped
by sheet class at all: R3 binds EVERY BOUNDED SHEET whatever its class, and R5 binds
THE WHOLE WORKBOOK less the excluded range of 7.1. Neither becomes inapplicable because
a sheet is a reference table or a panel.

**Wherever an element below says ENTITY SHEET, it binds a REFERENCE TABLE too**,
because a reference table is a grid in every respect these elements care about. Of the
R rows, only R1 and R2 turn on that distinction, and 7.2 says how.

**A LEGEND IS NOT AUTOMATICALLY A PANEL.** A skill that emits its legend as a grid
with one row per code DECLARES IT A REFERENCE TABLE and it takes every grid element.
A skill that emits it as label-and-prose DECLARES IT A PANEL SHEET and it takes
element 15. Either is correct. Declaring neither is not, and it is how one sheet came
to be scored against two families of element in one bundle.

## 2.1 The element table

| # | Element | Standard |
|---|---|---|
| 1 | **HEADER ROW POSITION** | **On an entity sheet and on a reference table, the header row is ROW 1. There is no banner row, no title row and no note row ABOVE it, ever.** The report title, the scope, the period and every caveat live on the front panel, which is where a reader looks for them and where they can be read without scrolling a grid sideways. A title banner in row 1 pushes the headers down, breaks the freeze pane, breaks the table range, breaks the autofilter and makes a header-name lookup return a caption. This element is first because every other element depends on it. **It governs what sits ABOVE the header row and nothing else.** The NOTE BAND of 5.3 sits BELOW the populated block, is not a row above the header row, and does not engage this element. On a PANEL SHEET this element is NOT APPLICABLE, with the sheet class as the reason, because a panel has no header row and its cell A1 is a title by element 15. |
| 2 | **FREEZE PANES** | Row 2, at `IDENTITY_BLOCK_ANCHOR_COLUMN`, which is the first column AFTER THE LAST FROZEN IDENTITY COLUMN, computed by reading the header row and locating that column BY NAME. Never a fixed cell reference: the span-of-control block changes the column position by role, so a hard-coded freeze silently breaks for half the readers. **THE REASON-FOR-RANK COLUMN IS THE FIRST COLUMN AFTER THE IDENTITY COLUMNS AND IS NEVER INSIDE THE FROZEN SPAN.** Where the whole identity block fits inside the frozen-span bound, the anchor is the last identity column and the freeze lands ON the reason column. Where the bound of 4.1.2 truncates the span, the anchor is EARLIER and the freeze lands on the first identity column that did not fit; the reason column is still outside the span, because truncation only ever shortens it. **One position for the reason column, stated in 4.1.1; one bound on the span, stated in 4.1.2.** This element reads both and restates neither. |
| 3 | **REAL TABLE OBJECT** | A real table over exactly the populated block, with no blank row inside its range and **NO POPULATED DATA ROW OUTSIDE ITS RANGE**. A visually formatted range is not a table and does not survive a sort. The prohibition is about DATA: a unit row left outside the table is a row that does not sort, does not filter and is not seen. The NOTE BAND of 5.3, which carries no unit and no data row, is explicitly outside the table range and is explicitly permitted there. **WHERE THE ENGINE CANNOT CARRY BOTH THIS TABLE OBJECT AND THE VISIBLE FILTER OF ELEMENT 6 OVER ONE RANGE, THIS ELEMENT IS THE ONE THAT GIVES AND ELEMENT 6 IS NEVER TRADED AWAY.** It is then recorded NOT APPLICABLE with the conflict named, which is a qualifying reason under the opening of this PART. Nothing this element exists for is lost when that happens: the purpose stated above is a sort that keeps a row's cells together, and the filter of element 6 sorts the same range on the same terms, while a filter the reader cannot see serves nothing at all. **ELEMENT 6 FIXES THE MECHANISM, THIS ELEMENT FIXES THE RANGE, AND A RUN MAKES NEITHER DECISION ON ITS OWN JUDGMENT.** |
| 4 | **TABLE STYLE, WHICH MUST NOT FIGHT THE DIRECT FORMATTING** | One named style with row stripes on, identical on every entity sheet in the workbook, from TABLE_STYLE_NAME. **THE STYLE'S OWN HEADER BAND MUST AGREE IN DIRECTION WITH ELEMENT 5's BAND: a LIGHT band carrying DARK text, never a dark band carrying light text.** Element 5 applies the header band as direct formatting and direct formatting outranks a style, so on a renderer honouring both, the style's own header band is never seen. **That is exactly why it is not free to oppose element 5.** A renderer honouring the STYLE and dropping the direct formatting, and a renderer honouring the DIRECT FORMATTING, must BOTH produce a readable header, and they cannot while the two pull in opposite directions. Measured on three delivered workbooks: every table carried a style whose own header band is a solid dark fill under light text, beneath a direct dark fill under light text, so the two agreed on darkness and nothing in the file stayed readable once the direct fill failed to render. **ROW STRIPES STAY ON**, because they are what lets a reader hold their place across twenty columns, and nothing in this element turns them off. |
| 5 | **HEADER STYLING, APPLIED EXPLICITLY, AND CHOSEN TO DEGRADE SAFELY** | Solid fill in COLOR_TITLE_BAND, **which is a LIGHT band**, body font bold, font colour COLOR_HEADER_TEXT, **which is a DARK ink**, on every header cell of every entity sheet. **Applied as DIRECT CELL FORMATTING, never left to the table style**, because element 7's gridlines are direct formatting and outrank a style. The same colour as the panel title bands, so the sheets and the panels read as one document. **THE DIRECTION IS A RULE AND NOT A PREFERENCE, AND THE RULE IS THIS: A HEADER IS THE ONE ROW THAT MUST NEVER BE AMBIGUOUS, SO ITS FORMATTING IS CHOSEN TO DEGRADE SAFELY IN BOTH DIRECTIONS RATHER THAN TO LOOK BEST WHEN EVERYTHING WORKS.** Dark ink on a light band stays readable when the BAND fails to render, because dark ink still sits on the default sheet ground; and it stays readable when the INK COLOUR fails to render, because the container's default dark ink still sits on the light band. The reverse pairing, light ink on a dark band, is readable only while BOTH halves render and is invisible the moment either one does not, which is a design with no tolerance for a single rendering failure. **THE CONTRAST FLOOR, THE ARITHMETIC AND ALL THREE ASSERTIONS ARE 2.8's**, and the verification runs the two DEGRADED renderings as well as the intended pair. |
| 6 | **AUTOFILTER, IN THE FORM THE READER'S OWN ENGINE LOOKS FOR** | Live on EVERY column of EVERY entity sheet, without exception. This is what lets a reader isolate the rows that matter in one click, and it is the single most-used feature of a delivered workbook. A sheet shipping without it has failed. **THE FILTER IS THE SHEET'S OWN FILTER, DECLARED ON THE SHEET, AND ITS RANGE IS THE POPULATED BLOCK ELEMENT 3 FIXES. EXACTLY ONE FILTER OBJECT STANDS OVER THAT RANGE, NEVER TWO.** A filter carried INSIDE a table object and a filter declared ON the sheet are two different objects in the container, and only the second is the one every renderer this bundle's workbooks are actually opened in goes looking for. **THE MECHANISM IS CHOSEN FOR THE READER'S ENGINE AND NOT FOR THE ONE THE FILE WAS BUILT IN, WHICH IS SD-FMT-29, DEGRADE SAFELY**, and it is the same choice already made for the header band's direction: the reading that survives the widest set of renderers wins over the reading that is most correct in the authoring tool. **WHERE THE ENGINE CANNOT EXPRESS BOTH A TABLE OBJECT AND A VISIBLE FILTER OVER ONE RANGE WITHOUT SETTING TWO OBJECTS, THE VISIBLE FILTER WINS AND ELEMENT 3 GIVES**, per element 3's own text, because element 3's stated purpose is served by this filter's sort and this element's purpose is served by nothing else. **THE MEASURED FAILURE THIS WORDING ANSWERS, STATED PLAINLY AS ELEMENT 7 STATES ITS OWN:** the previous wording required the filter to be the TABLE OBJECT'S OWN and forbade a sheet-level one, and the workbooks built to it shipped with NO VISIBLE FILTER CONTROL ON ANY SHEET OF ANY WORKBOOK, on the one feature this element calls the most-used in a delivered file. The check certified them, because it read the filter back out of the table container rather than off the sheet, so the artifact and the record agreed with each other and disagreed with the reader. **A FILTER THAT EXISTS ONLY INSIDE A CONTAINER THE READER'S ENGINE DOES NOT OPEN IS ABSENT, NOT PRESENT**, and it is scored absent by the verification. |
| 7 | **FULL GRIDLINES, ON EVERY POPULATED CELL OF THE SHEET** | Thin borders in COLOR_GRIDLINE on ALL FOUR SIDES of **EVERY POPULATED CELL OF THE SHEET**, whatever block it belongs to: the header row, every data row, **the NOTE BAND of 5.3, the explanatory row of 5.4, and every populated cell of a PANEL SHEET**. A complete grid: not outline-only, not horizontal-only. **A MERGED REGION IS ONE CELL FOR THIS ELEMENT AND CARRIES ITS BORDER ON THE OUTSIDE OF THE REGION**, on all four outer edges of the region rather than on its top-left cell alone. **THE SCOPE IS THE SHEET, NEVER THE TABLE**, and the difference is the whole of a measured failure: a note band is populated, is merged across the sheet width, and sits outside the table by construction, so a rule scoped to the table block excused the one band of populated cells that most needed bounding. An earlier wording sent it to element 15 for its border instead, which is how three delivered workbooks shipped a fully bordered table above a completely unbordered note band. COLOR_GRIDLINE is bound so the grid is VISIBLE against the sheet ground and against the header band, per 2.8; a gridline nobody can see is the same defect as no gridline. **A BAND STYLED ACROSS A SPAN BUT NOT MERGED ACROSS IT IS THE DEFECT THIS ELEMENT MEETS FROM THE OTHER SIDE, AND THE TWO ARE EASY TO CONFUSE BECAUSE THEY LOOK IDENTICAL UNTIL A BORDER IS DRAWN.** A styled span is several cells wearing one fill, so the text sits in the first of them, spills over the ones beside it, and this element's border on the second cell is then drawn straight through whatever word happened to be crossing it. A MERGED region is one cell for this element, so no interior line exists to cut anything. **Merging is what makes the region safe and styling alone is what makes it look safe**, per 2.10, which states the placement rule for every string wider than its own cell. |
| 8 | **BODY FONT AND ALIGNMENT** | BODY_FONT at BODY_FONT_SIZE, TOP-aligned, WRAP ON, on every populated cell. **WRAP BREAKS ON SPACES AND NEVER INSIDE A WORD, ON A BODY CELL EXACTLY AS ON A HEADER CELL**, which is primitive 1 of 2.2 and is a property of the wrap rather than of the row it runs on. The width floor of 2.2 step 3b is what makes that safe to rely on: it holds every column at or above the longest unbreakable token it must display, so no line the wrap produces ever has to overflow its own cell. See 2.10. |
| 9 | **HORIZONTAL ALIGNMENT** | **Within the table block, which is the header row plus the data rows,** right-align exactly the columns RIGHT_ALIGN_COLUMNS names, CENTRE exactly the columns that qualify as a STATUS GRID COLUMN under 2.5, and LEFT align every other column. All three lists are CLOSED at run time and their MEMBERSHIP is decided by the shape-token rule of 2.5, so a numeric column added later joins the right-aligned list by construction and a column carrying prose can never join the centred one. No column is inferred into any of them during a run. The NOTE BAND of 5.3 is outside the table block and is left aligned whatever column it begins in, so a sentence in the note band is never a violation of this element. |
| 10 | **COLUMN WIDTHS, SET FROM THE HEADER'S CHARACTER REQUIREMENT** | Every column width is set EXPLICITLY, never left at default and **never computed from the data alone**. The width is the one 2.2 computes: the larger of the header's character requirement and the capped data requirement, converted into width units ONCE, at 2.2 step 5, in the widening direction only. **The width a column is given therefore holds, on its header row, at least the characters its own wrapped header needs, so the autofilter dropdown caret can never cover a word of a header and elements 10 and 14 are two readings of ONE number that cannot disagree.** **AND IT HOLDS THE LONGEST UNBREAKABLE TOKEN THE COLUMN MUST DISPLAY, TAKEN OVER THE HEADER AND OVER THE DATA**, per 2.2 step 3b, so the wrap never has to break a word to fit and no word is ever cut by the cell's own edge. See 2.2 and 2.10. **The SUMMED built width of a grid's columns is bounded by `GRID_MAX_TOTAL_WIDTH` as well as each column's own width being floored, per 2.7, and where that bound is exceeded the relief ladder of 2.7 is run before publication and its result is recorded.** |
| 11 | **TRAILING NARRATIVE COLUMN** | The narrative column, the one saying what to do or why, is LAST and WIDEST, between `NARRATIVE_WIDTH_MIN_UNITS` and `NARRATIVE_WIDTH_MAX_UNITS`. **Both are BUILT WIDTH UNITS, the same unit 2.2 sets every other width in, and both are applied to the width DIRECTLY per 2.2 step 6 with no conversion of any kind** -- they are not character counts and are never divided by CHAR_WIDTH_FACTOR. The column is never set below its own header floor. |
| 12 | **ROW HEIGHTS, COMPUTED FROM WRAPPED CONTENT** | Every row height is COMPUTED from the wrapped content of its own cells against those cells' own BUILT widths, never set to a fixed number and never left to autofit. The line count is the GREEDY WRAP of 2.2 primitive 1 and is never a division of text length by the usable count. See 2.3. Nothing clips at any width. |
| 13 | **ALERT SHADING** | On a sheet carrying an elapsed-time column: COLOR_ALERT_WARN at the approaching band, COLOR_ALERT_OVERDUE at the past band, dark text in both, per ALERT_BAND_THRESHOLDS. NOT APPLICABLE, and therefore a pass, on a sheet with no such column. A unit exempted from the cycle the alert measures is never shaded, because a long interval is expected there. **EXACTLY TWO KINDS OF CONDITIONAL FILL MAY APPEAR ON AN ENTITY SHEET: these alert band fills, and the fills of `CLASSIFICATION_FILLS` on a declared CLASSIFICATION COLUMN per 2.6, keyed on the states of `CLASSIFICATION_VOCABULARY`. Every other conditional shading is forbidden.** Shading prose by keyword and banding a number by its value are both outside those two and are forbidden. **A classification column is NOT required to be centred and is NOT bounded by `CENTRE_ALIGN_MAX_CHARS`: that bound is 2.5's and it governs alignment only.** The two palettes are DISJOINT and the disjointness is verified: no value in `CLASSIFICATION_FILLS` is ever COLOR_ALERT_WARN or COLOR_ALERT_OVERDUE, so one colour never carries two meanings in one workbook. |
| 14 | **HEADER ROW HEIGHT, COMPUTED FROM THE LONGEST WRAPPED HEADER** | The header row's height is COMPUTED so that the header needing the most wrapped lines shows ALL of them, each header measured against the USABLE HEADER CHARACTERS of its own column's BUILT width. A two-line header shows two lines. Never a fixed height. See 2.4. |
| 15 | **PANEL STYLING** | Panel sheets carry: a title band in COLOR_TITLE_BAND, section headers in COLOR_SECTION_HEADER, label cells in COLOR_LABEL_FILL, thin borders in COLOR_GRIDLINE on all four sides of every populated cell per element 7, body font throughout. Same palette as the entity sheets, so the workbook reads as one document. **EVERY TITLE BAND, SECTION HEADER BAND AND BANNER IS MERGED ACROSS EXACTLY THE SPAN IT NEEDS, NEVER MERELY STYLED ACROSS IT**, per 2.10, so no cell edge inside the band can fall in the middle of a word. **EVERY BAND ON A PANEL IS A LIGHT BAND CARRYING DARK TEXT, AND EVERY ONE OF THEM IS HELD TO BOTH DEGRADED RENDERINGS OF 2.8** exactly as element 5's header band is, because a panel title is opened in the same renderers an entity header is and fails in them the same way. This element no longer supplies a border to anything: element 7 borders every populated cell of every sheet of every class, and a second statement of the same requirement is how the two drifted apart. |
| 16 | **CHARACTER SET** | Every cell value, every sheet name and the filename contain only characters in the permitted range. Verified by scanning the BUILT artifact, not the source data. |

**Elements 10, 12 and 14 are new, and each answers a failure no earlier element
covered:** a header word hidden behind a filter caret, a cell clipped because its row
height was guessed, and a two-line header showing one line.

## 2.2 The caret allowance, and how column width is computed

**The problem it solves:** an autofilter places a dropdown caret in the RIGHT of every
header cell. A width computed to fit the header text exactly leaves the caret sitting
on top of the last word, so the reader sees a truncated header on the one row that
must never be ambiguous. Computing width from the DATA makes it worse, because a
column of short values gives a narrow column under a long header.

### 2.2.1 The three primitives, defined ONCE, used unchanged by 2.3, 2.4 and their verifications

**Everything in PART 2 that measures text is built out of these three and nothing
else. They are defined here, before any width exists, so that no step in PART 2 has
to read a number a later step produces.**

**PRIMITIVE 1: THE WRAP.** `wrap( text , c )` breaks `text` into lines GREEDILY at
SPACES ONLY: fill the current line while the next word still fits within `c`
characters, then start a new line. **A word longer than `c` is NEVER SPLIT; it takes a
line of its own and that line overflows.** `lines( text , c )` is how many lines
`wrap( text , c )` yields. `c` is always a WHOLE NUMBER of characters: where a usable
count comes out fractional, the whole number BELOW it is used. For any `c` at or above
the length of the text's longest single word, widening `c` never increases
`lines( text , c )`.

**PRIMITIVE 2: THE ONE CONVERSION, AND ITS SINGLE DIRECTION.** `CHAR_WIDTH_FACTOR`
converts a COLUMN WIDTH INTO THE NUMBER OF CHARACTERS OF THE BODY FONT THAT FIT ON ONE
LINE OF THAT COLUMN. It MULTIPLIES a width and YIELDS characters. It is less than one,
so it always yields FEWER usable characters than the width number, which is the safe
direction: every assertion built on it is a FLOOR, and erring high on a requirement
makes a column slightly wider or a row slightly taller and never clips anything. Its
single home, where it is defined and where its documented default lives, is the
BINDING SCHEMA; this file NAMES it and does not restate its value.

- `usable_body( W ) = round( W * CHAR_WIDTH_FACTOR , 2 )`
- `usable_header( W ) = round( W * CHAR_WIDTH_FACTOR , 2 ) - CARET_ALLOWANCE_CHARS`

**The caret allowance is `CARET_ALLOWANCE_CHARS`, default 3.0 characters:** the
dropdown caret plus the padding either side of it, in characters of the body font. It
is subtracted on the HEADER ROW and on no other row, because the caret sits on the
header row and nowhere else. It is a BINDING rather than a constant because a
different body font at a different size needs a different allowance, and a bound value
is checkable where a constant is not.

**Every comparison in PART 2 is made after rounding to TWO DECIMAL PLACES**, so that
no artifact is ever failed by floating-point dust in the last bit of a width.

**PRIMITIVE 3: THE HEADER'S CHARACTER REQUIREMENT, `H`.** For a header string, `H` is
**the SMALLEST whole number `c`, AT OR ABOVE THE LENGTH OF THE HEADER'S LONGEST SINGLE
WORD, for which `lines( header , c ) <= HEADER_MAX_LINES`.** `HEADER_MAX_LINES`
defaults to 2. `H` is a property of the header text and the line budget ALONE. It
never reads a width, a data value or a built artifact.

**WHY `H` IS DEFINED THAT WAY AND NOT AS "WRAP IT AND TAKE THE LONGEST LINE".** The
earlier wording said to wrap the header to the line budget and measure the longest
resulting line, and it never said WHAT LINE WIDTH TO WRAP AT. There is no such thing
as wrapping text to a number of lines; text wraps to a WIDTH, and the number of lines
is what comes out. The only width available at that step was the one the step was
about to produce, so the rule could only be read as a circle. `H` closes it: it is the
narrowest line the header can live on inside its budget, found by asking the wrap
rather than by assuming an answer. The floor at the longest single word is load
bearing: without it, a one-word header would "fit in one line" at every width down to
one character, because an over-long word takes its own line, and the requirement would
collapse to nothing.

**PRIMITIVE 4: THE LONGEST UNBREAKABLE TOKEN, `T`.** A TOKEN is a run of characters
between spaces. It is UNBREAKABLE because primitive 1 breaks on spaces and never
inside a token, so a token is the smallest thing a line can be made to hold. For a
column, `T` is **the length in characters of the LONGEST TOKEN THE COLUMN MUST
DISPLAY, taken over its HEADER STRING AND OVER EVERY VALUE THE COLUMN WILL CARRY.**
Like `H`, it is a property of TEXT ALONE: it never reads a width, a built artifact or
any quantity a later step produces. A hyphen, a slash and a full stop are ordinary
characters inside a token and are not break points, because primitive 1 does not break
on them; a token is measured exactly as it will be written.

### 2.2.2 The computation, in order, and every column gets it

1. **COMPUTE `H`** from the column's header text, per primitive 3.
2. **THE HEADER'S CHARACTER REQUIREMENT IS `H + CARET_ALLOWANCE_CHARS`**, because the
   header row must hold `H` characters of text AND the caret beside them.
3. **THE DATA CHARACTER REQUIREMENT IS** the character count of the longest value in
   the column, capped at `COLUMN_WIDTH_MAX_CHARS` so one outlier cannot make a column
   unreadable.
3b. **COMPUTE `T`** for the column, per primitive 4. **`T` IS A SECOND FLOOR AND IT IS
   NOT CAPPED**, for the same reason the header floor is not: a cap that cuts a floor
   puts back the defect the floor exists to prevent.
4. **THE COLUMN'S CHARACTER REQUIREMENT IS THE LARGEST OF THE THREE.** **The header
   requirement is a FLOOR that the data can raise and can never lower**, and **`T` IS A
   FLOOR THAT NOTHING LOWERS AT ALL.** That is the whole point of the element: a column
   is never narrower than its own header needs, whatever the data does, and never
   narrower than the longest single word it has to show, so **THE WRAP NEVER HAS TO
   BREAK A WORD TO MAKE IT FIT AND NO WORD IS EVER CUT BY THE CELL'S OWN EDGE.**
5. **CONVERT ONCE, HERE, AND NOWHERE ELSE IN THIS SECTION:**
   `W = character requirement / CHAR_WIDTH_FACTOR`, rounded UP to two decimal places.
   That is the width, in the spreadsheet's own column-width unit.
6. **THE NARRATIVE COLUMN IS EXEMPT FROM STEP 3 AND TAKES ELEMENT 11's RANGE**, since
   its data is prose and its longest value is not a width argument. Element 11's range
   is already in BUILT WIDTH UNITS and is applied to the width DIRECTLY, with no
   conversion of any kind: **step 5 does not run on this column**, because there is no
   character requirement here to convert. The narrative width is
   `NARRATIVE_WIDTH_MIN_UNITS` at least and `NARRATIVE_WIDTH_MAX_UNITS` at most, EXCEPT
   that it is never set below its own step 5 header floor, which IS a converted
   quantity and is compared against these two as a width. **A floor that no ceiling may cut is the one thing every part of
   this element agrees on**, so where the header floor exceeds the range's ceiling the
   floor wins and the over-long header is reported as below.
7. **SET THAT NUMBER AS THE WIDTH, UNCHANGED.** Nothing scales it afterwards.

**Stated as one line:**
`width = ceiling_2dp( max( H + CARET_ALLOWANCE_CHARS , min( longest_value_length ,
COLUMN_WIDTH_MAX_CHARS ) , T ) / CHAR_WIDTH_FACTOR )`, and that value is the width.

**Where `H + CARET_ALLOWANCE_CHARS` exceeds `COLUMN_WIDTH_MAX_CHARS`, the column still
gets its floor and the header is REPORTED on the method sheet as over-long**, naming
the header and the width it forced. That is a finding to act on by shortening the
header, not a failure: a header widening its own column past the cap every data column
respects is exactly the thing a reader should be told about, and clipping it instead
is the defect this element exists to prevent.

**WHERE `T` ALONE EXCEEDS `COLUMN_WIDTH_MAX_CHARS`, THE SAME THING HAPPENS AND THE
TOKEN IS NEVER BROKEN TO AVOID IT.** The column takes the width `T` requires, and the
method sheet REPORTS the column, the token, its length and the width it forced, exactly
as an over-long header is reported. **BREAKING THE TOKEN IS FORBIDDEN, AND SO IS EVERY
DISGUISED FORM OF BREAKING IT:** no inserted line break, no inserted hyphen, no
ellipsis, no truncation and no shrunken font. A single token past the cap is almost
always a value that should not have been written as one word, which is a finding for
the reader to act on at the source; the one thing that must not happen is the reader
meeting half a word with a cell line through it. **Where the column's width is then a
problem for the SHEET, that is 2.7's bound and 2.7's relief ladder**, whose three
untouchables already forbid shortening a value that carries meaning, so the two
sections agree and neither buys width with a word.

### 2.2.3 Why the division at step 5 is permitted and the multiplication is still forbidden

**Both directions have now been tried and both failures are on the record, so the rule
is stated as a DIRECTION rather than as a ban on arithmetic.**

**The first failure, multiplying.** An earlier statement of this section multiplied the
width by `CHAR_WIDTH_FACTOR` at the point of setting it. Since the factor is less than
one, every built width came out BELOW the header floor computed two steps earlier, so
the verification failed on every column whose data requirement did not exceed its
header requirement, and a correct workbook could not publish. Worse than the failed
check: the columns were genuinely narrowed below their own headers, which is the exact
defect this element exists to prevent.

**The second failure, converting nowhere at all.** The correction banned every
conversion at this point and set the width to the character requirement itself. That
made the width and the usable-character count two different quantities wearing one
number. 2.4 consumes a built width as `usable_header( W ) = W * CHAR_WIDTH_FACTOR -
CARET_ALLOWANCE_CHARS`; feeding it `W = H + CARET_ALLOWANCE_CHARS` yields
`( H + CARET ) * CHAR_WIDTH_FACTOR - CARET`, which is strictly LESS THAN `H` for every
factor below one, whatever the values. Every header therefore needed more lines than
its own budget allowed, and element 14 failed on a workbook built exactly to this
section. It was measured on a real run: 14 of 29 columns came out needing three lines
against a budget of two, on a build that satisfied the width rule literally.

**The two operations are not the same operation, and only one of them is forbidden.**

| Direction | What it does to a width | Status |
|---|---|---|
| MULTIPLY a width being set by `CHAR_WIDTH_FACTOR` | NARROWS it, below the header floor | FORBIDDEN, always, everywhere |
| DIVIDE a CHARACTER REQUIREMENT by `CHAR_WIDTH_FACTOR` to obtain the width that holds it | WIDENS it | PERMITTED at step 5 ONLY, once per column |
| Apply any factor to a width AFTER step 5 | either | FORBIDDEN |

The division is the arithmetic INVERSE of primitive 2, applied exactly once, to turn a
requirement expressed in characters into the width that supplies those characters. It
can only ever widen, so it cannot produce the defect the ban was written to stop. **It
is what makes the width a column is GIVEN and the characters 2.3 and 2.4 READ OUT of
that width the same quantity**, which no version of this section that skipped it could
manage.

### 2.2.4 The composition, stated so that it can be checked

**Every quantity below is computed from quantities to its LEFT, and nothing reads a
value produced to its right. That is the whole guarantee, and it is why a build
following 2.2, 2.3 and 2.4 passes elements 10, 12 and 14 by construction rather than
by luck:**

`header text` and `the column's own values` -> `H` and `T` -> `character requirement`
-> `W` -> `usable_header( W )` and `usable_body( W )` -> `line counts` -> `row heights`
and `header height`.

**`T` JOINS THE CHAIN AT THE SAME PLACE `H` DOES AND IN THE SAME DIRECTION.** Both are
computed from TEXT ALONE before any width exists, both feed the character requirement,
and neither reads anything produced to its right, so the chain stays one-directional
and nothing here is circular. `T` is measured over the header string and the column's
values, which are the same two texts step 2 and step 3 already read, so it introduces
no new input either.

Two consequences fall straight out of it, and both are the assertions the elements
make:

1. `usable_header( W ) >= H`, because `W` is at least
   `( H + CARET_ALLOWANCE_CHARS ) / CHAR_WIDTH_FACTOR`. So the header wraps within
   `HEADER_MAX_LINES` lines at the width it was given, which is element 14.
2. Every row height and the header height are computed from the SAME built widths the
   verification re-reads, using the SAME wrap, so recomputing them at verification
   time reproduces the numbers the build set, which is elements 12 and 14.
3. `floor( usable_body( W ) ) >= T`, because `W` is at least `T / CHAR_WIDTH_FACTOR`.
   So NO LINE primitive 1 produces in any populated cell of the column overflows that
   cell, which is the overflow case primitive 1 names and this floor removes. On the
   header row the same holds through `H`, which is itself floored at the header's
   longest single word, so `floor( usable_header( W ) ) >= H >= ` the header's longest
   token. That is 2.10's second half, asserted here where the arithmetic lives.

**The verification of element 10:** for every column on every entity sheet and every
reference table, re-read the BUILT width `W`, recompute `H` from the header string, and
assert `floor( usable_header( W ) ) >= H`. Equivalently, and it is the same assertion,
assert `W >= ( H + CARET_ALLOWANCE_CHARS ) / CHAR_WIDTH_FACTOR` at two decimal places.
A column that cannot show its own header inside its own line budget fails the element
and blocks publication. **AND RECOMPUTE `T` FROM THE HEADER STRING AND THE COLUMN'S
BUILT VALUES AND ASSERT `floor( usable_body( W ) ) >= T`.** A column narrower than the
longest word it displays fails the element and blocks publication, because that column
is where a word gets cut, and where the assertion fails because `T` exceeds
`COLUMN_WIDTH_MAX_CHARS` the remedy is the width and the report, never the token.

## 2.3 How row height is computed

**Never a fixed number and never left to autofit**, because autofit does not account
for wrap on merged or styled cells and silently clips on some engines.

For each row, for each cell in it:

1. Take the cell's TEXT and the FINAL BUILT width of its own column. For a MERGED cell,
   which on an entity sheet means a note-band row per 5.3, take the SUMMED built widths
   of the columns the merge spans.
2. **USABLE = `usable_body( W )` on a body row and on a note-band row.** The header row
   is 2.4's, and it uses `usable_header( W )` instead, because the caret occupies that
   space on the header row and on no other row. Both are primitive 2 of 2.2 and neither
   is restated here.
3. **LINES = `lines( text , floor( usable ) )`, WHICH IS THE GREEDY WRAP OF PRIMITIVE
   1.**
4. Take the MAXIMUM line count across every cell in the row.
5. **HEIGHT = ( max lines times LINE_HEIGHT_PT ) plus LINE_HEIGHT_PADDING_PT**, where
   LINE_HEIGHT_PT is the body font's own line height and LINE_HEIGHT_PADDING_PT is
   the standing padding, default 15.

**THE LINE COUNT IS THE WRAP AND IS NEVER A DIVISION OF TEXT LENGTH BY USABLE
CHARACTERS.** An earlier statement of step 3 gave both algorithms in one sentence, as
`ceiling( text length / usable characters )` qualified by "wrapping on spaces", and the
two do not agree. Worked example, and it was run: `aaaaa bbbbb ccccc` is 17 characters,
and at 9 usable characters the division gives `ceiling( 17 / 9 ) = 2` lines while the
greedy wrap gives 3, because no two of those words share a line. Two faithful
implementations then disagreed about whether one correct workbook passed element 12.
**The wrap governs, because it is what the renderer does.** The division is an
approximation that under-counts exactly where the words are long, which is exactly
where a cell clips.

**The verification:** for every populated row, recompute the required lines from the
BUILT widths using primitive 1 and assert the built height is at least the requirement.
A row shorter than its content needs fails and blocks publication.

## 2.4 How the header row height is computed

The same computation as 2.3, run over the HEADER ROW ONLY, with two differences that
both matter:

1. **The usable character count is `usable_header( W )`,** which subtracts the caret
   allowance, because the caret occupies that space on the header row and on no other
   row.
2. **The line count is taken from the header that needs the MOST lines**, not from
   any single header. One two-line header makes the whole header row two lines tall,
   which is correct: a header row where one header shows one of its two lines is the
   defect this element exists to prevent.

Per column, `header_lines = lines( header , floor( usable_header( W ) ) )` against that
column's own BUILT width. **The header height is ( the maximum of those line counts
times LINE_HEIGHT_PT ) plus LINE_HEIGHT_PADDING_PT.**

**The verification asserts three things, and on a workbook built to 2.2 all three hold
by construction:**

1. `floor( usable_header( W ) ) >= H` for every column, which is element 10's assertion
   read from the other end.
2. No header's recomputed line count exceeds `HEADER_MAX_LINES`. This follows from the
   first, so a failure here is a report that some width was NOT set by 2.2, and the
   remedy is the width and never the line budget. **RAISING `HEADER_MAX_LINES` TO CLEAR
   THIS ASSERTION IS FORBIDDEN**, because it clears the check by lowering the standard
   the check exists to hold.
3. The built header height is at least the computed header height.

Each blocks publication on failure.

## 2.5 Which columns are right aligned, which are centred, and which are left

**Element 9's three lists are CLOSED AT RUN TIME and their MEMBERSHIP IS DECIDED BY A
RULE, so that no run adds a column on its own judgment and no list goes stale when a
column is added to the contract.**

**THE MEMBERSHIP RULE, WHICH IS TOTAL OVER THE SHAPE TOKENS:** right align a column
whose shape token is COUNT_OR_MEASURE, RATE_OR_PROPORTION or DATE. Left align one whose
token is IDENTIFIER_OR_CODE, BOOLEAN_LIKE or FREE_TEXT. A column whose token is
STATUS_OR_CATEGORY is LEFT ALIGNED UNLESS it qualifies as a STATUS GRID COLUMN, in
which case it is CENTRED. The tokens are exhaustive, so every column this contract can
emit lands on exactly one side by construction.

**A STATUS GRID COLUMN, DEFINED SO THE CONDITION IS MECHANICALLY CHECKABLE.** A column
is one when ALL THREE of these hold, and the skill DECLARES it as one on the method
sheet:

1. Its shape token is STATUS_OR_CATEGORY.
2. Every populated value in it comes from a CLOSED, DECLARED vocabulary, published in
   the legend or the method sheet, so a reader can see the whole set of answers the
   column can give.
3. The LONGEST member of that vocabulary is at most `CENTRE_ALIGN_MAX_CHARS`
   characters, default 12.

**A column failing any one of the three is LEFT ALIGNED, and the failure is not a
defect; it is the ordinary case.**

**WHY CENTRING IS ADMITTED AT ALL, AND WHY ONLY THERE.** A block of adjacent columns
each holding one short code out of the same small set is read ACROSS THE ROW and DOWN
THE COLUMN as a pattern, not as text: the reader is looking for the shape of the
failures, and left-aligned codes of unequal length make a ragged edge that hides it.
That is a real readability gain and it is worth a stated exception. **It disappears the
moment a cell holds a sentence.** A centred sentence has a ragged edge on BOTH sides,
it cannot be scanned down the column, and it collides with nothing else in the
workbook being centred. Condition 3 is what keeps the exception where the gain is: a
cell carrying a code plus a finding plus the standard's own wording is not a code, and
such a column is left aligned like any other column of prose. Where a skill wants its
status grid centred, the remedy is to put the code in the grid and the sentence in the
narrative column of element 11, which is last, widest and never truncated.

**CONDITION 3 GOVERNS CENTRING AND NOTHING ELSE. IT IS NOT A CONDITION ON SHADING, AND
2.6 DOES NOT READ IT.** `CENTRE_ALIGN_MAX_CHARS` decides centring here and is read
nowhere else in this contract. A column whose longest value runs past it is left
aligned and may still carry a classification fill, on its own conditions, stated in
2.6. Where a skill wants its status grid SHADED rather than centred, no remedy is
needed and no value is shortened: it declares a CLASSIFICATION COLUMN under 2.6,
binds `CLASSIFICATION_VOCABULARY` and `CLASSIFICATION_FILLS`, and leaves the column
left aligned. 2.6's opening paragraph says why the two were separated
and must stay separated.

**The bound lists are the MATERIALISED result of this rule.** VALIDATE them whenever a
column is added to the contract: no column with a numeric or date token is missing from
`RIGHT_ALIGN_COLUMNS`; no column with a text, identifier, category or boolean token is
in it; and no column is centred that is not a declared status grid column. A list that
fails that check is wrong even if every entry in it is individually defensible.


## 2.6 The classification fills, and why they are not the alert shading and not the centring test

**A CLASSIFICATION COLUMN may carry a FILL PER STATE OF `CLASSIFICATION_VOCABULARY`,
through the map `CLASSIFICATION_FILLS`.** That is the second and last kind of
conditional shading element 13 permits on an entity sheet. Both variables are bound
in reference/schema/, which owns their defaults, their validation and the palette
separation arithmetic; this section states what a build DOES with them and restates
none of that.

**2.5 AND 2.6 ANSWER DIFFERENT QUESTIONS, AND THEY ARE NEVER COUPLED AGAIN.** This
section once hung its first condition on 2.5's centring test, which bounds a
vocabulary's longest member at `CENTRE_ALIGN_MAX_CHARS`. **CENTRING asks whether a
SHORT TOKEN reads better centred than left**, and a character bound is exactly the
right test for that, because the gain is the straight edge and the gain is gone the
moment the cell holds a phrase. **SHADING asks whether a reader can find the failures
WITHOUT READING**, and a long cell value does not harm that at all; if anything a long
cell is where the fill helps most, because it is the cell the eye cannot triage on its
own. Coupling them made the fill unreachable in practice. Measured: a scorecard whose
shortest possible gap cell is 15 characters, whose shortest qualified pass is 17, and
whose shortest unassessable cell is 29, against a centring bound of 12. No column could
ever qualify, so no fill was lawful, and 1520 status cells shipped with no colour at
all -- correctly under the old text, and contrary to everything this contract says the
workbook looks like. **A cell can be too long to centre and still be exactly the kind of
cell that needs a fill.** Whoever is tempted to reunite them is reading one question and
answering the other.

**THE CONDITIONS, ALL FOUR OF WHICH ARE VERIFIED, AND NONE OF WHICH IS A LENGTH
BOUND:**

1. **The column is a DECLARED CLASSIFICATION COLUMN, declared as one on the method
   sheet.** A column is one when all of these hold:
   - Its shape token is STATUS_OR_CATEGORY or BOOLEAN_LIKE. **Never FREE_TEXT, and
     never a numeric or a date token**: shading prose by keyword is not a
     classification fill, and banding a number by its value is not one either. Both
     stay forbidden by element 13.
   - Its states are the members of `CLASSIFICATION_VOCABULARY`, a CLOSED, DECLARED
     set published in the legend with the meaning of each, so a reader can see the
     whole set of answers the column can give. A run never invents a state.
   - **Every populated cell resolves to EXACTLY ONE state by the ONE resolution rule
     `CLASSIFICATION_VOCABULARY` carries, and that rule is TOTAL AND MECHANICAL**:
     either the cell value IS a member, or it carries its member as its own declared
     leading token. No cell resolves to two states, and no cell resolves to none. A
     rule that leaves one populated cell unresolved is not total, the column is not a
     classification column, and it carries no fill at all.
   - **`CLASSIFICATION_VOCABULARY` IS NOT THE SET OF DISTINCT CELL VALUES, and that
     distinction is what makes the fill possible on a real grid.** Where a cell value
     is a state crossed with a reason code, a qualifier or a finding, the values run
     to hundreds and the state set stays small, and it is the small set that is bound.
   - **A declared STATUS GRID COLUMN under 2.5 is automatically a classification
     column**, because it satisfies every line above by construction. The converse does
     not hold, and that asymmetry is the whole of this section.
2. **`CLASSIFICATION_FILLS` IS INJECTIVE: one fill per state, and NO TWO STATES EVER
   SHARE ONE.** Every member of `CLASSIFICATION_VOCABULARY` has an entry and no
   non-member does. **Four answers that read as three colours ARE three answers**, and
   a reader cannot recover the fourth. This is the condition a build is most tempted to
   break, because two states that feel similar look like one colour to whoever is
   writing the map and like one ANSWER to whoever is reading the grid: two states that
   are counted differently, excluded differently, or cleared by different people are
   never given one fill however alike they read. Where the vocabulary has more states
   than the palette has separable colours, a state carries NO FILL and the legend names
   which; it is never resolved by giving two answers one colour. A map that is not
   injective FAILS verification row 13 and blocks publication.
3. **The fills come from `CLASSIFICATION_FILLS`, bound for the purpose**, published in
   the legend with the state each colour carries. Where a state's fill is one of the
   contract's own status colours, the map CITES that variable rather than restating its
   value, so no colour has two setting sites.
4. **THE PALETTE IS DISJOINT FROM THE ALERT PALETTE.** `COLOR_ALERT_WARN` and
   `COLOR_ALERT_OVERDUE` are element 13's and are never a value in
   `CLASSIFICATION_FILLS`, on any sheet, whether or not that sheet carries an
   elapsed-time column. The separation between every pair in the union of those
   palettes is arithmetic, not taste, and reference/schema/ states it.

**WHY THE DISJOINTNESS IS A RULE AND NOT A PREFERENCE.** A workbook that shaded its
unassessable cells the alert-warn colour and its gap cells the alert-overdue colour
happened to collide with nothing, because no sheet in it carried an elapsed-time
column and element 13 scored NOT APPLICABLE everywhere. The same skill run at an
organization that DOES track an elapsed-time column paints the same two colours with
two meanings on one grid: an approaching deadline in one column and an unassessable
cell in the next. A reader has no way to tell which meaning a colour carries, and the
defect is invisible on the run where it was authored. **A colour is a variable with one
binding, exactly as a header string is.**

**WHY THE FILL IS WORTH THIS MUCH TEXT.** The fill is the second channel. The first is
the words in the cell, which a reader must read one at a time; the second is the colour,
which a reader takes in across the whole grid at once and which is how they find the
failures before they have read anything. A greyscale separation between the fills is the
operative half of that, because these workbooks are printed and photocopied and read by
people who do not see the hues apart. **A status grid with no fill is a grid that must
be read cell by cell, which on a sheet of any size is a grid that is not read.**

**A cell may carry at most one fill.** Where a classification column would also fall
inside an alert band, the alert fill governs and the classification fill is not
applied, because the alert is the time-critical signal; the legend states that
precedence once.

**ALIGNMENT AND FILL ARE SET INDEPENDENTLY AND NEITHER IMPLIES THE OTHER.** A
classification column is aligned by 2.5's membership rule like every other column:
centred where it also clears 2.5's three conditions, left aligned where it does not.
A left-aligned column carrying a classification fill is the ORDINARY case and is not a
defect. Verification row 9 tests the alignment, verification row 13 tests the fill, and
neither reads the other's condition.


## 2.7 The TOTAL WIDTH of a grid is bounded too, and what gives when the columns will not fit

**WHY THIS IS A SECOND BOUND AND NOT THE ONE IN 4.1.2.** 4.1.2 bounds the FROZEN
SPAN, which stops a freeze pinning the whole sheet. It says nothing whatever about
how wide the sheet IS. With that bound in force and correctly honoured, a measured
census sheet came out 21 columns and 749.12 width units across, and an extract of it
735.48, against the 659 this contract's own text already calls a measured failure.
The span bound worked: three columns stayed pinned. Everything else sat behind about
ten screens of horizontal scrolling, so the reader read the sheet THROUGH THE FILTER,
one column at a time, rather than by moving across it. **That is a real loss and not a
cosmetic one: a grid nobody can traverse is a grid whose relationships between columns
are invisible, which is most of the reason it is a grid.** One bound says what stays on
screen; this one says how much there is. Neither substitutes for the other.

**`GRID_MAX_TOTAL_WIDTH` is the maximum SUMMED BUILT WIDTH of every column of one
entity sheet or reference table**, in the SAME width unit 2.2 sets column widths in
and `FROZEN_SPAN_MAX_WIDTH` bounds the frozen span in. It binds a SHEET, not a column
and not a workbook. Its default, its two-sided validation and the arithmetic behind
both are in reference/schema/ and are not restated here.

**IT IS READ BEFORE THE COLUMNS ARE BUILT AND IS NEVER CHOSEN AFTER THE FACT.** The
build reads `GRID_MAX_TOTAL_WIDTH` first, records the value it is building to on the
method sheet, and then builds. **A run never raises it to clear a grid that failed
it**, exactly as HEADER_MAX_LINES is never raised to clear a failing element 14, and a
bound discovered after the measurement is not a bound.

**THE THREE THINGS THAT NEVER GIVE, STATED FIRST SO THE LADDER IS READ AGAINST THEM:**

- **NO COLUMN IS DROPPED.** Not a mandatory one, which SD-FMT-21 already forbids, and
  not a declared one either. A dropped column is a fact the reader cannot recover and
  cannot know to look for.
- **NO COLUMN GOES BELOW ITS OWN HEADER FLOOR.** 2.2's floor holds unchanged. A column
  narrowed under the characters its own wrapped header needs hides a header, which is
  the failure elements 10 and 14 exist for, and trading a readable header for a
  narrower sheet is trading the thing that must never be ambiguous.
- **NO VALUE THAT CARRIES MEANING IS SHORTENED.** A name, a date, an identifier, a
  finding and a per-row reason are never truncated, abbreviated, re-capped or reworded
  to save width. This is a READABILITY bound and it never buys width with correctness.

**WHAT DOES GIVE IS A STANDING QUALIFIER, AND IT IS DEFINED SO THE STEP IS
MECHANICAL.** A STANDING QUALIFIER is a phrase inside a cell that does all three of
these: it QUALIFIES the cell's own answer rather than stating it; it is drawn from a
CLOSED, DECLARED set; and it is written in the SAME WORDS every time that member
appears. It therefore costs its full length on every row that carries it while
conveying exactly one thing, WHICH MEMBER IT IS. **A phrase unique to its own row is
not a standing qualifier and this ladder never touches it.** The measured case: a
mandatory pass qualifier 50 characters long, identical wherever it appeared, set eight
requirement columns to 56.82 width units each and six more to 46.59, which is over half
the sheet.

**THE RELIEF LADDER, RUN IN ORDER, BEFORE PUBLICATION:**

1. **MOVE EVERY STANDING QUALIFIER OUT OF THE CELL AND INTO THE LEGEND.** The cell
   keeps its own answer and a SHORT DECLARED CODE for the qualifier; the legend
   publishes that code against the qualifier's FULL WORDING, once, in the words it had
   in the cell. Nothing is lost and nothing is shortened: the reader reads the sentence
   once instead of on every row, and the column's data requirement, and so its built
   width under 2.2, falls to what the answer and the code need. **THE LEGEND ENTRY IS
   MANDATORY AND IS VERIFIED.** A code with no legend row is an abbreviation the reader
   has to decode, which costs more than the width it saved, and it is the one way this
   step can be done wrongly.
2. **MOVE EVERY REMAINING PER-ROW PROSE FRAGMENT THAT IS NOT THE CELL'S OWN ANSWER
   INTO THE TRAILING NARRATIVE COLUMN of element 11**, which is last, widest and never
   truncated. A sentence belongs in one wide column read once, not spread across eight
   columns and read eight times. The narrative column's own bound in element 11 is
   unchanged and is never raised to absorb this.
3. **RECOMPUTE EVERY WIDTH FROM 2.2, FROM THE TOP.** Steps 1 and 2 change the DATA
   requirement of the columns they touch, and 2.2 is the only thing that sets a width.
   Never adjust a width by hand to bank the saving, and never apply a conversion 2.2
   does not name.
4. **WHERE THE GRID IS STILL OVER THE BOUND, IT SHIPS OVER THE BOUND AND SAYS SO.**
   The method sheet records `GRID_MAX_TOTAL_WIDTH`, the measured total, the overage, and the columns
   that account for it in DESCENDING order of built width; the front panel carries one
   line telling the reader that this sheet is wider than the bound and that the freeze
   and the filter are how it is meant to be read. **An honest overage is the correct
   last outcome**, because every other way out is one of the three things that never
   give. This record has the same shape as 4.1.2's truncation record and exists for the
   same reason: a silently over-wide sheet is indistinguishable from a broken one.

**WHERE A QUALIFIER BELONGS, DECIDED ONCE HERE SO NO RUN DECIDES IT ALONE.** It
belongs in the LEGEND where it is drawn from a closed set and the cell can carry its
code. It belongs in the TRAILING NARRATIVE COLUMN where it is per-row prose that is not
the cell's own answer. It belongs in the CELL only where it IS the cell's own answer.
Those three are exhaustive over what a cell can hold, so the step is a lookup rather
than a judgment.

**VERIFIED BY ROW 10**, because the total is a property of the widths element 10 sets,
and a sheet's total width is not a separate element to be scored not applicable
somewhere.

## 2.8 The contrast arithmetic, the two floors, and the TWO DEGRADED RENDERINGS every band is tested against

**THE MEASURE IS THE ONE THE BUNDLE ALREADY HAS, AND THIS SECTION ADDS NO SECOND WAY OF
TALKING ABOUT COLOUR.** The PALETTE SEPARATION RULE of the binding schema's formatting
group already computes a colour's GREYSCALE VALUE and already separates two colours by
the difference between their greyscale values. Contrast here is that same arithmetic,
read between a text colour and the surface under it rather than between two fills, so a
run writes ONE function, reports ONE kind of number, and a reader who has understood the
separation rule has already understood this one:

- `grey( C ) = 0.299 * R + 0.587 * G + 0.114 * B`, on the 0 to 255 scale, `C` being a
  colour's red, green and blue components.
- `sep( A , B ) = abs( grey( A ) - grey( B ) )`.

**THE TWO FLOORS, WHICH ARE DIFFERENT NUMBERS FOR A STATED REASON.**

| Floor | Value | What it governs |
|---|---|---|
| TEXT_SEPARATION_MIN | 90 | Any TEXT colour against the surface it sits on. |
| LINE_SEPARATION_MIN | 110 | Any BORDER colour against every surface it is drawn on. |

**A LINE'S FLOOR IS HIGHER THAN A LETTER'S, AND THAT IS NOT AN INCONSISTENCY.** A
hairline border lays down a fraction of the ink a glyph stroke does, over a fraction of
the area, so the separation that reads as perfectly legible text reads as an absent rule.
The gridline default measured on the delivered workbooks had a greyscale value of about
165 against a white ground, a separation of 90: enough for text, and the reason the grid
reads as faint.

**THE THREE ASSERTIONS ON EVERY TEXT-AND-BAND PAIR, AND ALL THREE RUN.** Let `T` be the
text colour, `B` the band fill, `G` the container's DEFAULT SHEET GROUND, which is white,
`FFFFFF`, and `K` the container's DEFAULT TEXT INK, which is black, `000000`. Where a
container states different defaults, those are used and the run RECORDS what it read.

1. **THE INTENDED PAIR RENDERS.** `sep( T , B ) >= TEXT_SEPARATION_MIN`.
2. **THE FILL FAILS TO RENDER.** `sep( T , G ) >= TEXT_SEPARATION_MIN`. The band is gone
   and the text is sitting on the bare sheet.
3. **THE FONT COLOUR FAILS TO RENDER.** `sep( K , B ) >= TEXT_SEPARATION_MIN`. The band
   is there and the text has fallen back to the container's default ink.

**ASSERTING ONLY 1 IS THE BLIND SPOT, AND IT IS THE BLIND SPOT THAT SHIPPED.** A dark
band under light text passes 1 handsomely, passes 3, and fails 2 completely: the light
text lands on the light sheet and is gone. A LIGHT BAND UNDER DARK TEXT is the only
pairing that can clear all three, which is why element 5 states a DIRECTION rather than a
preference, and why elements 4 and 15 are reconciled to that direction rather than left
to choose their own.

**THE GRIDLINE IS HELD TO `LINE_SEPARATION_MIN` AGAINST BOTH SURFACES IT MEETS:** the
default sheet ground, where almost all of it is drawn, and COLOR_TITLE_BAND, which is the
darkest band it is drawn over. A gridline separated from the sheet but not from the band
disappears on the one row that carries the column names.

**THE FLOORS ARE DECLARED BEFORE THE COLOURS ARE BOUND AND ARE NEVER LOWERED TO CLEAR A
COLOUR THAT FAILED**, exactly as HEADER_MAX_LINES is never raised to clear a failing
header and `GRID_MAX_TOTAL_WIDTH` is never raised to clear a failing grid. A floor
discovered after the measurement is not a floor.

## 2.9 Every colour this bundle writes carries an EXPLICIT OPAQUE ALPHA

**A COLOUR WRITTEN WITH A TRANSPARENT ALPHA, OR WITH NO ALPHA WHERE THE CONTAINER EXPECTS
ONE, IS A PUBLICATION-BLOCKING FAILURE.** It is not cosmetic and it is not the renderer's
fault. It renders correctly in the tool the author built it in and invisibly in the tool
the reader opens it in, so the run that created it verified a readable artifact and
delivered an unreadable one, with a recorded pass beside it.

**THE MEASURED EVIDENCE, WHICH IS WHY THIS SECTION EXISTS.** On three delivered
workbooks, every header cell of every entity sheet was written with the fill `001F3864`
and the font colour `00FFFFFF`. The LEADING byte of each is the ALPHA byte and its value
is `00`. The common spreadsheet engine is lenient and treats `00RRGGBB` as fully OPAQUE,
so the workbook was correct to the run that built it and to anyone opening it in that one
engine. Many other renderers -- web previewers, spreadsheet viewers, document conversion
pipelines -- honour an alpha of `00` as FULLY TRANSPARENT. In those, the dark fill dropped
out entirely and bold white header text landed on a white or lightly banded ground, where
no reader could see it. Every header cell of every entity sheet of all three workbooks
was affected, and the defect was invisible to the run that authored it.

**THE FORM, STATED ONCE AND FOR EVERY COLOUR.**

| Where the container's colour field takes | The value is written as | What is forbidden |
|---|---|---|
| EIGHT hex digits, alpha first | `FFRRGGBB`, the alpha byte literally `FF` | any alpha byte other than `FF`, and `00` above all |
| SIX hex digits, no alpha | `RRGGBB`, exactly six digits | six digits padded to eight with a `00` alpha |

**IT BINDS EVERY COLOUR A RUN WRITES ANYWHERE**, and not only the header band: every
fill, every font colour, every border colour, every panel band, both alert bands and every
classification fill. The colour VARIABLES carry the format requirement in their own
validation in the binding schema, and the verification reads the BUILT artifact rather
than the build intention, so a value that was correct in the variable and wrong in the
cell is still caught. **AN ALPHA IS NEVER LEFT TO A DEFAULT AND NEVER INHERITED**: the run
writes it, so the artifact carries it, so the verification can read it.

## 2.10 NO WORD IS EVER BROKEN BY A CELL LINE, AND THE TWO CAUSES EACH HAVE A RULE

**A READER MEETING A WORD WITH A BORDER THROUGH THE MIDDLE OF IT STOPS READING THE
SHEET AND STARTS DOUBTING THE FILE**, exactly as an unreadable header does, and it was
reported on a delivered workbook: a title band reading across the top of a sheet, whose
own text was longer than the cell it was written into, with the neighbouring cell's left
border drawn straight through the middle of a word. **THERE ARE EXACTLY TWO WAYS A CELL
LINE CAN CUT A WORD, AND EACH GETS ITS OWN RULE, BECAUSE FIXING EITHER ONE ALONE LEAVES
THE OTHER SHIPPING.**

**CAUSE ONE, OVERFLOW ACROSS A CELL BOUNDARY. THE RULE: ANY STRING THAT NEEDS MORE WIDTH
THAN ITS OWN CELL IS PLACED IN A MERGED REGION SPANNING EXACTLY THE WIDTH IT NEEDS, AND
TEXT IS NEVER PERMITTED TO OVERFLOW A CELL BOUNDARY.** That binds every band this
contract can emit: a PANEL TITLE ROW, a SECTION HEADER BAND, the NOTE BAND of 5.3, the
EXPLANATORY ROW of 5.4 and ANY BANNER. Once the region is merged, element 7 carries its
border on the OUTSIDE of the region, so there is no interior line left inside the band
for a word to be cut by, and the band is bounded exactly once.

**A BAND STYLED ACROSS A SPAN AND A BAND MERGED ACROSS A SPAN ARE DIFFERENT THINGS, AND
CONFUSING THEM IS THE DEFECT.** Styling a run of cells gives every one of them the fill,
the font and the border, and gives the text NO extra room: the string still lives in the
first cell, still overflows it, and the second cell's own left border is now guaranteed
to be drawn, wherever in the string it happens to land. Merging makes the run ONE CELL,
which is the only thing that gives the string the width it needs. **THE TWO ARE
INDISTINGUISHABLE ON SCREEN UNTIL A BORDER IS DRAWN**, which is precisely why the defect
survived a visual pass and shipped: the fill looked continuous, and only element 7's
grid revealed that the band had been three cells all along. **A BAND THAT IS STYLED
ACROSS A SPAN AND NOT MERGED ACROSS IT FAILS THIS SECTION**, whatever it looks like.

**AND THE SPAN IS EXACTLY WHAT THE STRING NEEDS**, computed from the string and the
built widths under it by the same wrap and the same usable count 2.3 uses, never a
guessed span and never the whole sheet width where less will do. A band on an entity
sheet or a reference table spans the table's full column span, per 5.3, because that is
what the band is about; a band on a panel spans what its own string requires.

**CAUSE TWO, A WRAP THAT SPLITS A WORD. THE RULE: THE COLUMN IS AT LEAST AS WIDE AS THE
LONGEST UNBREAKABLE TOKEN IT MUST DISPLAY**, taken over its header and over the data it
will carry. That is `T`, primitive 4 of 2.2, and it enters the width at step 3b as a
floor nothing lowers. **THE WRAP BREAKS ON SPACES ONLY AND NEVER INSIDE A WORD**, which
primitive 1 already says and which element 8 now says of a body cell as well as a header
cell. Primitive 1 names the case where a token is longer than the line it is given: the
token takes a line of its own AND THAT LINE OVERFLOWS. **THE FLOOR IS WHAT MAKES THAT
CASE UNREACHABLE**, because every column is built at or above `T` before a single value
is written, so the wrap is never asked to fit a word into less room than the word takes.

**WHERE A SINGLE TOKEN GENUINELY EXCEEDS `COLUMN_WIDTH_MAX_CHARS`, THE COLUMN TAKES THE
WIDTH THE TOKEN NEEDS AND THE METHOD SHEET REPORTS IT**, naming the column, the token,
its length and the width it forced, exactly as an over-long header is reported by 2.2.
**IT IS NEVER SOLVED BY BREAKING THE TOKEN**, and every disguised break is forbidden
with it: an inserted line break, an inserted hyphen, an ellipsis, a truncation and a
smaller font are all the same act. A cap that cuts a floor puts back the defect the
floor exists to prevent, and a word cut in half is not a narrower column, it is a
wrong value.

**THE VERIFICATION, AND IT IS TWO ASSERTIONS.** First, on every sheet of every class,
every populated cell whose string requires more usable characters than its OWN cell
supplies is a MERGED REGION spanning at least the columns that supply them; a cell that
is not merged and whose string exceeds its own usable count FAILS, and a band whose
cells carry a fill in common without being merged FAILS with it. Second, for every
column of every grid, `floor( usable_body( W ) ) >= T` recomputed from the header string
and the built values, per 2.2.4. Both read the BUILT artifact under 7.1 and both block
publication.

---

# PART 3: THE DOCX CONTRACT, FOR THE REVIEW SKILL

**The docx WRAPS the character-limited form-field blocks. It does not replace them.**
The review exists to be copy-pasted into a submission form, field by field, and the
field limits are real: a field that overruns is truncated by the destination system,
silently, at the moment it matters. The document makes those fields READABLE while
keeping every one of them individually COPYABLE.

## 3.1 A form SECTION and a submission FIELD are different things

**A SECTION is a part of the destination form. A FIELD is ONE CHARACTER-CAPPED BOX
inside it. One section can hold one field or many, and the two are counted
separately.** FORM_SECTIONS is a list of SECTIONS and is never read as a list of
fields.

**THE FIELD SET IS DERIVED FROM THE SECTION SET AND IS DECLARED IN THE DOCUMENT.**
Each section yields one field, EXCEPT where a section's own binding says otherwise:
where OBJECTIVE_FIELD_IS_SINGLE is true, the objectives section yields ONE FIELD PER
OBJECTIVE, each holding that objective's title, description and every measure in one
capped box. A person with four objectives therefore has one objectives SECTION and
FOUR objective FIELDS.

**THE BLOCK, THE CHARACTER COUNT AND THE CHARACTER LIMIT ATTACH TO THE FIELD.** The
section supplies the ORDER of the blocks and the name under which they are grouped,
and nothing else. A verification that counts blocks against the SECTION list will
fail a correct document the moment one section holds two fields, which is the
ordinary case rather than an exotic one.

**The derived field set is PRINTED in the document**, in the field index, so a reader
can see how many boxes they are about to fill and in what order, and so the block
count has something to reconcile against that is not the section count.

## 3.2 The requirements

**All verified before publication:**

| # | Requirement | Standard |
|---|---|---|
| D1 | **ONE BLOCK PER FIELD** | Every submission FIELD, per 3.1, is its own block, in the submission form's own order, under a heading naming the field exactly as the destination system names it. Where a section yields several fields of the same kind, the heading is the destination system's own name for the field followed by the index the form itself uses to tell the boxes apart, as in `Objective 2`. That is not a friendlier name and not an improved one; it is the destination's name plus the only thing that says WHICH BOX. |
| D2 | **THE BLOCK IS COPYABLE AS A UNIT** | A field's text is one contiguous run with nothing interleaved: no commentary inside it, no rationale, no lineage line, no coaching note, no bracketed aside, no bullet the form will not accept, no character outside the permitted set. **The block has exactly three parts in exactly this order: the HEADING, the FIELD TEXT, and the COUNT CAPTION.** What a reader selects from the END OF THE HEADING to the START OF THE COUNT CAPTION is EXACTLY what gets pasted. Nothing sits between the heading and the field text, nothing sits between the field text and that field's own count caption, and nothing sits between the count caption and the next heading. See 3.3. |
| D3 | **THE LIMIT AND THE COUNT ARE SHOWN** | Every block states its character limit and its CURRENT COUNT in its COUNT CAPTION, which is the block's LAST line, in the form `n of N characters`. A block over its limit is marked OVER by that many characters and is a publication-blocking failure, not a warning. |
| D4 | **THE LIMITS COME FROM FIELD_LIMITS** | Never from a guess and never from the destination system read at run time. Where a field's limit is not bound, the block says the limit is unknown and shows the count alone. |
| D5 | **NOTHING BELOW THE SUBMISSION BOUNDARY IS INSIDE A FIELD BLOCK** | Working notes, evidence, the counterfactual, every bracketed placeholder and anything unconfirmed sit BELOW the boundary, clearly labelled, and are never inside a copyable block. The boundary is stated once, in the document, in plain words. See 3.4 for the placeholder, which is the case that has no other home. |
| D6 | **THE PANEL STYLING MATCHES THE XLSX PALETTE** | Same title band, section header, label fill and body font, so a reader who has both documents sees one system. |

## 3.3 Where the character count goes, and why it goes there and nowhere else

**THE COUNT CAPTION IS THE LAST LINE OF THE BLOCK: below the field text, above the
next heading, in the caption style, never in the heading line and never above the
field text.** It is one line, it reads `n of N characters`, and it may name the field
it belongs to.

**The placements that were tried and are now forbidden, with what each one breaks:**

| Placement | What it breaks |
|---|---|
| In the heading line | D1. The heading is then no longer the destination system's own name for the field, and the heading is what a reader matches against the form to find the box. |
| In a caption ABOVE the field text | D2. A drag begun at the heading, which is how every reader starts, picks the caption up on the way down. This was built and measured: it caught the caption on every block. |
| ABOVE the heading | D2. Something then sits between one field's text and the next field's heading, and it belongs to the wrong block by position. |
| Nowhere at all | D3, and every verification of the count and the limit then has nothing to read. |

**Why below the text works where the others do not.** The reader drags DOWNWARD from
under the heading. A caption below the text is a VISIBLE STOP LINE, in a different
style, that the reader stops AT rather than passes THROUGH; a caption above the text
is an invisible one they have already crossed before they notice it. The count and
the limit stay on the page, readable without opening anything, and the heading keeps
the destination system's own name intact.

**The count is not moved into the field index instead.** The index carries every
count as well, and the two reconcile, but a reader pasting field six is looking at
field six and not at an index four pages up, and a limit that is only in an index is
a limit nobody reads at the moment it matters.

## 3.4 The bracketed placeholder has a defined home, and it is below the boundary

**A number that traces to no cell and no tool result becomes a bracketed placeholder
naming its source. D2 forbids a bracketed aside inside a field block. Those two are
reconciled HERE, once, so neither has to bend:**

1. **The claim ships in the copy region WITHOUT the number.** The person's own words
   survive; the unsourced quantity does not travel into a permanent record dressed as
   a fact.
2. **The number goes BELOW THE SUBMISSION BOUNDARY**, as a bracketed placeholder,
   carrying the figure as stated, WHO or WHAT stated it, and THE QUESTION THAT WOULD
   SOURCE IT.
3. **The block and the placeholder are linked by the field's own heading**, so a
   reader who sources the number knows which box to put it back into.

**Why the number is not simply dropped:** on a run with no mail, no chat and no
action-evidence column, a person's own note is the only evidence of what they did,
and a seam that strips every figure out of it silently deletes their year. Below the
boundary it is preserved, visible, and clearly marked as not yet sourced.

**The docx carries no formatting elements from PART 2.** Freeze panes, autofilters and
column widths are spreadsheet concepts, and a review has no grid to apply them to.
This is stated so nobody scores the review against the xlsx elements, which cannot
apply to it, and reports a wall of failures.

---

# PART 4: RANK AND THE REASON FOR RANK, ON EVERY ENTITY SHEET

## 4.1 Both columns, always, in every skill

**Every entity sheet and every reference table carries a POSITION column and a
REASON-FOR-RANK column. No such sheet ships without both.** This holds in planning,
in scorecard, and on any entity sheet a review emits.

- **THE POSITION COLUMN** is a FIXED IDENTITY COLUMN, in the identity block, in first
  position.
  - **Where the sheet's order IS a merit order**, the position column is the RANK
    column and its header is `HDR_RANK`.
  - **Where the sheet's order is NOT a merit order**, the column is still first, is
    still a position column, and is HEADED FOR WHAT IT IS: its header is
    `HDR_POSITION`, whose documented default is `Position`. A sheet ordered by
    something other than merit and headed `Rank` is a contract violation.
- **`HDR_PRIORITY_BAND` IS NOT A POSITION HEADER AND IS NEVER USED AS ONE.** It is
  the header of the exception BAND column, and its values are band labels of the
  High, Medium, Low kind. A column of 1, 2, 3 under a band label tells a reader they
  are looking at bands, and it is as much a contract violation as a non-merit order
  headed `Rank`. The two variables name two different things and neither substitutes
  for the other.
- **NEITHER HEADER IS EVER WRITTEN AS A LITERAL.** Read the variable. A header string
  written into a skill is a second source of truth that nothing updates.
- **REASON FOR RANK** says, in plain language, WHY THAT UNIT SITS WHERE IT DOES. It
  names the terms that actually decided the position, in the order they contributed.
  It is required on a non-merit order too, where it says why the unit sits at that
  POSITION.

**The reason column is not the narrative column and does not replace it.** The
narrative says what to DO about the unit. The reason says why the unit is HERE. A
sheet may carry both, and where it does they are different columns with different
headers.

**Why it is mandatory rather than a nicety:** a ranked list whose ordering cannot be
explained row by row is a list the reader re-sorts by hand, and a list that gets
re-sorted by hand has already lost. A scorecard shipped without a rank column at all,
which left a reader with a census and no answer to "what do I do first".

### 4.1.1 Where the reason column sits, decided once, here, in one position

**THE REASON-FOR-RANK COLUMN IS THE FIRST COLUMN AFTER THE IDENTITY COLUMNS.** It
closes the identity block, and every measure, count, status, date and narrative column
on the sheet comes after it. **THERE IS NO OTHER PERMITTED POSITION FOR IT**, and in
particular it is never placed at the far right of the sheet beside the narrative
column: a skill whose own column order puts it there is stale and this file governs.

**IT IS NEVER INSIDE THE FROZEN SPAN.** The freeze of element 2 lands ON it where the
whole identity block fits inside the bound of 4.1.2, and lands EARLIER where the bound
truncates the span. Either way the reason column is outside the frozen span, because
truncation only ever shortens the span and never extends it past the identity columns.

**Why it sits there and not further right.** The reason for a unit's position is read
WITH the unit's identity, in one glance, before the reader scrolls into the measures.
Put beside the narrative column, twenty columns to the right, it answers a question the
reader stopped asking fifteen columns ago.

**Why it is outside the frozen span rather than inside it.** The reason column is FREE
TEXT: a sentence, sometimes a short paragraph, wrapped at the width element 8 gives it.
Frozen, it is pinned to the left edge on every horizontal scroll, so a reader who
scrolls right to reach a measure drags a paragraph across the sheet with them and loses
most of the window to it. **The frozen span exists to keep the unit's IDENTITY on
screen, and a paragraph is not an identity.**

**This settles a three-way contradiction, and all three statements now hold at once:**
element 2 freezes at the first column after the last FROZEN identity column; this
section puts the reason column immediately after the identity columns; and no free-text
column ever sits inside the frozen span. They were irreconcilable only while "the
identity block's last column" and "the identity block's last FROZEN column" were read
as the same column. They are not the same column: the reason column separates them when
the block fits, and 4.1.2's bound separates them when it does not.

### 4.1.2 The frozen span is BOUNDED, and what happens when the identity block exceeds the bound

**`FROZEN_SPAN_MAX_WIDTH`, default 55, is the maximum TOTAL BUILT WIDTH of the frozen
span, in the SAME width unit 2.2 sets column widths in.** It is a bound on the span, not
on a column and not on the sheet.

**WHY A BOUND EXISTS AT ALL, WHICH IS A MEASURED FAILURE AND NOT A PREFERENCE.** A
census workbook built entirely to this contract came out 21 columns and 659
character-widths across, about ten screens. Freezing the whole identity block on it
pinned 17 of the 21 columns and 659 of the 659 widths, so scrolling right reached
nothing at all and the sheet could not be read. **A frozen span wide enough to fill the
window does not keep the identity on screen; it keeps EVERYTHING on screen, which is
the same as freezing nothing while also costing the reader the scroll.** A freeze that
costs the reader more than it saves is worse than no freeze.

**THE WALK RUNS ONCE FOR THE WHOLE ARTIFACT, FROM THE WIDEST CASE, AND NEVER ONCE PER
SHEET.** A built width depends on the longest DATA value in that column on that sheet,
per 2.2, so a per-sheet walk stops in a different place on every sheet of one workbook.
Measured: one workbook whose identity block was the same six columns everywhere froze
THREE identity columns on its three merit sheets and FIVE on its three empty ones,
because an empty sheet's name column holds no value, falls back to its own header
floor, and leaves room for two more. Every one of those sheets was individually
conformant. The WORKBOOK was not: a reader scrolling right on one tab kept three
columns pinned and on the next tab kept five, for a reason invisible on the face of the
artifact, and the method sheet recorded six different truncation statements for one
identity block. **SD-CTR-08 makes the identity block structurally identical on every
item section, and a freeze that lands in a different place per sheet breaks that
promise as surely as a different column set would.**

**HOW THE SPAN IS BUILT, AND IT IS DETERMINISTIC:**

1. For EACH identity column, take the **MAXIMUM of its BUILT width across every entity
   sheet and reference table in the artifact that carries the full identity block**.
   That is the WIDEST CASE, and it is what the walk sums. This step runs after every
   width is built and before any freeze is set.
2. Walk the identity columns LEFT TO RIGHT, summing those WIDEST-CASE widths.
3. The span ends at the LAST column whose inclusion keeps the running sum at or below
   `FROZEN_SPAN_MAX_WIDTH`. That column is `IDENTITY_BLOCK_ANCHOR_COLUMN`, **and it is
   the anchor for EVERY sheet of the artifact, computed once**.
4. **THE FIRST COLUMN IS ALWAYS FROZEN**, even where it alone exceeds the bound. A
   sheet with an empty frozen span loses the unit's position number on the first
   scroll, which is the failure the freeze exists to prevent.
5. The freeze is then set at row 2 and at the first column after the anchor, on every
   sheet, per element 2. **The anchor is located BY HEADER NAME on each sheet**, so a
   sheet whose columns sit at different positions still freezes the same columns.

**WHAT HAPPENS WHEN ONE SHEET'S IDENTITY BLOCK IS GENUINELY NARROWER. NOTHING.** The
anchor is a COLUMN, not a width. A sheet whose name column holds no value falls back to
its own header floor, so its frozen span is NARROWER IN WIDTH UNITS than the widest
case and freezes THE SAME COLUMNS. That is the intended outcome and it costs the reader
nothing: the pin is in the same place on every tab, and the sheet that needed less
simply used less. **What a narrower sheet must never do is freeze MORE columns than the
widest case allows**, which is exactly the defect this rule closes.

**A SHEET THAT DOES NOT CARRY THE WHOLE IDENTITY BLOCK is outside the walk and never
shortens it for the sheets that do.** It freezes at the last identity column it does
carry, subject to the same bound, and the method sheet names that sheet and says which
identity columns it lacks. SD-CTR-08 makes this the rare case rather than the ordinary
one, and a run that finds it common should suspect its own identity-block declaration
rather than this rule.

**WHAT HAPPENS TO THE IDENTITY COLUMNS THAT DID NOT FIT.** Nothing is moved, nothing is
dropped and nothing is narrowed. They keep their positions and their order, unfrozen,
and the reason column still follows all of them. **Never resolve an over-wide identity
block by narrowing a column below its 2.2 floor**, which trades a readable freeze for
an unreadable header.

**THE IDENTITY BLOCK IS ORDERED MOST-IDENTIFYING FIRST**, so that a truncated span keeps
the columns that answer "which unit is this row": the position column, then the unit's
own identifier, then the unit's name, then every other identity column. A skill declares
its identity block in that order.

**THE TRUNCATION IS RECORDED ONCE FOR THE ARTIFACT, because a silently shortened freeze
is indistinguishable from a broken one, and six records of one identity block are worse
than none.** Where the bound truncates the span, the method sheet states, in ONE line:
the bound; the summed WIDEST-CASE built width of the frozen span; which sheet supplied
the widest case for each identity column it walked; and the identity columns left
outside the span, by header name. Where it does not truncate, that one line states the
summed widest-case width and that the whole identity block is frozen on every sheet.
**It is one line for the workbook and never one line per sheet**, and it is verified by
row 2.

## 4.2 The three kinds of ranked sheet, and the rank arithmetic of each

**A rank means "position in the ranked population" on every sheet that carries one,
but the RANGE of ranks a sheet holds depends on what kind of sheet it is, and there
are three kinds. A skill declares which kind each of its sheets is, and the
declaration is recorded on the method sheet.**

| Kind | What it is | The ranks it holds |
|---|---|---|
| MERIT TIER | One of an ordered SET of sheets that between them partition the ranked population: a first action tier, a second action tier, a reference tier. | A contiguous slice of one unbroken sequence, per 4.2.1. |
| CENSUS | ONE sheet holding every unit in scope, ranked worst-first, with no partition and no tiers. | 1 through `min( REFERENCE_CAP , eligible_count )`, per 4.2.2. |
| EXTRACT | A sheet carrying the TOP of a census, so the reader has a short worklist as well as the full grid. | The census's OWN rank numbers for the rows it carries, never re-ranked from 1, per 4.2.3. |

**A DIRECTED SHEET IS NONE OF THE THREE.** Its units are ranked 1 to N among
themselves, are excluded from the merit tiers and from `eligible_count`, and never
consume a merit rank. It is stated here so it is not mistaken for an extract.

### 4.2.1 The merit tier set

**Ranks form ONE UNBROKEN SEQUENCE across the merit tiers. No gaps, no duplicates, no
restart at 1.**

- The FIRST action tier starts at rank 1 and holds ranks 1 through `tier_1_size`.
- The SECOND action tier RESUMES at the next rank and holds `tier_1_size + 1` through
  `last_visit_rank`, where `last_visit_rank = tier_1_size + tier_2_size`.
- The REFERENCE tier RESUMES after that, holding `last_visit_rank + 1` through
  `min( last_visit_rank + REFERENCE_CAP , eligible_count )`.

**Tier sizes are bindable, and the standing defaults are DELIVERABLE_LINES:**

| Line | First tier | Second tier | last_visit_rank |
|---|---|---|---|
| DIRECT tier reader | 10 | 25 | 35 |
| AGGREGATE tier reader | 20 | 50 | 70 |

**THE DERIVED LAST MERIT RANK IS `last_visit_rank + REFERENCE_CAP`, AND IT IS A
DERIVED RANK, NEVER A ROW CAP.** At the standing sizes that is 535 and 570. **Those
numbers are DERIVED and are never carried as literals.** A resize recomputes them: a
first tier of 20 and a second of 40 makes `last_visit_rank` 60 and the last merit rank
560. Any check asserting the standing figures against a resized run is testing the
wrong number and will fail a correct workbook.

**Never read a derived last rank as a row cap.** A scope with far more eligible units
than the cap would then ship `REFERENCE_CAP + tier sizes` rows on the reference sheet
instead of `REFERENCE_CAP`, overrunning the cap that every showing-note reconciliation
checks against, and failing a correct-looking workbook at the final gate.

**The last merit rank on a full run is therefore the DERIVED figure, not
`last_visit_rank`.** A check asserting `last_visit_rank` as the last merit rank is
testing the wrong number.

**These three quantities exist ONLY on a merit tier set.** `tier_1_size`,
`last_visit_rank` and the derived last merit rank mean nothing on a census or on an
extract of one, and a check that applies them there is testing a number the workbook
never produced.

### 4.2.2 The census

**A CENSUS HOLDS RANKS 1 THROUGH `min( REFERENCE_CAP , eligible_count )`, AND IT
HOLDS THAT MANY ROWS.** It is one sheet, it starts at 1, and it does not resume after
anything, because there is no tier before it to resume from.

**A census is not a reference tier and 4.2.1 does not describe it.** A reference tier
is the TAIL of a partition and starts after the action tiers; a census is the WHOLE
population and starts at 1. A skill emitting a census that started its ranks at
`last_visit_rank + 1` would omit its own worst units from its own census, which is
not a census.

**The cap still applies**, per PART 5.1, and the showing note of 5.2 still ships.
Where `eligible_count` exceeds `REFERENCE_CAP`, the census holds the first
`REFERENCE_CAP` ranks and says so in its note.

### 4.2.3 The extract of a census

**AN EXTRACT REPEATS THE CENSUS'S OWN RANK NUMBERS FOR THE ROWS IT CARRIES AND NEVER
RE-RANKS FROM 1.** A row at census rank 34 is at rank 34 on the extract. A reader who
finds a unit on both sheets sees one number, which is the whole point of a rank.

**AN EXTRACT DUPLICATES EVERY IDENTIFIER IT CARRIES, BY CONSTRUCTION, AND THAT IS NOT
A DEFECT.** It is a view of the top of the census, not a separate population. R2's
no-duplicate-identifier assertion is scoped to MERIT TIERS and does not run between a
census and an extract of it, per 7.2.

**An extract declares, on its own sheet and in the method section, which sheet it is
an extract OF and how many rows it takes.** Without that a reader cannot tell an
extract from a tier, and neither can a verification.

**AN EXTRACT IS A BOUNDED SHEET AND SHIPS THE SHOWING NOTE OF 5.2**, with `n` its own
counted rows and `N` the counted row count of the census it extracts from, per 5.1.1. It is
the sheet a reader opens first and the sheet whose row count is least self-explanatory,
so it is the last sheet that should be silent about what it is not showing.

**The size of an extract is the skill's own declaration**, bounded by PART 5.1's cap
like any other sheet. It is never derived from `tier_1_size` or `last_visit_rank`,
which are merit-tier quantities and mean nothing on a census workbook.

## 4.3 The reference tier's size, and the form that governs

**This section is about a MERIT TIER SET. On a census workbook the authoritative row
count is 4.2.2's, and a check reading this section against a census is testing the
wrong number.**

**The reference tier holds `min( REFERENCE_CAP , eligible_count - last_visit_rank )`
rows, and this ROW-COUNT FORM IS AUTHORITATIVE wherever any other statement gives the
size differently.**

Where `eligible_count` is at or below `last_visit_rank`, the tier holds **ZERO ROWS**
and ships with its header and one explanatory row, placed and counted per 5.4, saying
every eligible unit appears on the action tiers and there are none left to list.
**Never emit a negative count and never treat this as a failure.** A tier holding
fewer rows than the cap is a complete and correct tier, and no instruction anywhere may assert that it holds exactly
REFERENCE_CAP rows.

`eligible_count` is every unit in the ranked population EXCLUDING directed units,
after scope, qualifiers and exclusions, with no measure floor of any kind and with
zero-valued and null-valued units included and ranked last.

---

# PART 5: THE CAP, AND THE SHOWING NOTE

## 5.1 The cap is per sheet, independently

**Every capped sheet is capped at REFERENCE_CAP rows INDEPENDENTLY, default 500.**
Not a shared budget across sheets, not a workbook total. The reason is that later
sheets hold wildly different populations: a reference list, an opportunity list and an
exception list drawn from one scope routinely differ by an order of magnitude, and one
shared budget would silently starve whichever sheet was built last.

Every sheet that CAN exceed the cap is capped: the reference sheet, the directed
sheet, and every auxiliary entity sheet.

**CAPPED MEANS SUBJECT TO THE CAP, NOT CUT BY IT.** A sheet holding 13 rows under a cap
of 500 is a capped sheet that lost nothing, and it carries every obligation a capped
sheet carries, the showing note included. Reading "capped" as "cut" is what left two
uncapped-in-practice reference tables with no note at all and left R3 with nothing to
reconcile on either of them.

## 5.1.1 The THREE bounds a sheet's row count can have, and what N is under each

**EVERY SHEET WHOSE ROW COUNT IS BOUNDED BY ANYTHING SHIPS THE SHOWING NOTE OF 5.2, AND
THERE ARE EXACTLY THREE BOUNDS.** A sheet under none of them is unbounded and ships no
showing note. This table is what `N` means, and it is the only place `N` is defined:

**WHAT `n` AND `N` COUNT, DEFINED ONCE HERE FOR BOTH GRID CLASSES.** They count the
sheet's own **COUNTED ROWS**, and a counted row is **the sheet's own DATA row**: on an
ENTITY SHEET that is a UNIT ROW, one row per unit of business; on a REFERENCE TABLE,
whose rows are not units by 2.0's definition, it is **the sheet's own row**, whatever
that sheet's rows are of. **This was undefined and it mattered**: 5.1.1 requires the
showing note on every reference table under `REFERENCE_CAP`, and the note's counting
basis was written as unit rows, which a reference table has none of by construction, so
the contract required a note on a sheet whose basis it never defined. **The bound, the
note and the reconciliation all count the same thing, and it is whatever that sheet's
data rows are.** The explanatory row of 5.4 is not a counted row on either class.

| Bound on the sheet | Which sheets | `n` is | `N` is |
|---|---|---|---|
| `REFERENCE_CAP` | The reference sheet, the directed sheet, every auxiliary entity sheet, every reference table | Counted rows written to the sheet | Rows that qualified for the sheet before the cap was applied |
| The TIER SIZE of a merit tier | The first and second action tiers | Counted rows written to the tier | Units still eligible for that tier when it was filled: `eligible_count` less the ranks consumed by the tiers above it |
| The DECLARED SIZE of an extract | An extract of a census, per 4.2.3 | Counted rows written to the extract | The counted row count of the census it extracts FROM |

**THE TIER SIZES ARE A BOUND AND THE NOTE IS NOT VACUOUS.** An earlier statement said
the action tiers "carry no separate cap", which was true of `REFERENCE_CAP` and was read
as meaning they were not bounded at all, which left `N` undefined for a tier and left
two readers printing `showing 20 of 20` and `showing 20 of 181` off one run. A tier size
IS a bound: it cuts a real population down to a stated number of rows, which is exactly
what the showing note exists to disclose. `N` is the population it cut, not the number
it cut to. **What the tiers carry no separate cap FROM is `REFERENCE_CAP`**, which is
not applied to them a second time on top of their sizes.

**THE EXTRACT'S NOTE IS THE ONE A READER MOST NEEDS.** An extract is the top of a census
and is routinely the first grid a reader opens. Without the note it shows 70 rows and
says nowhere on the sheet that 120 more exist, and a reader who takes it for the whole
population acts on a fifth of their book. Its `N` is the census's own row count, so
`showing 70 of 190` reads exactly as it does on every other sheet.

## 5.2 The showing note, and its exact wording

**Every BOUNDED sheet, per 5.1.1, states the showing note ON THE SHEET and again in
the METHOD section. The two must agree, and the reconciliation is verified.** ON THE
SHEET means in the NOTE BAND, which 5.3 defines exactly and which is the only place a
per-sheet note goes.

**The exact wording, and it is one string with two substitutions:**

> **showing n of N**

where `n` and `N` are what 5.1.1 defines for that sheet's own bound. The note is
written in that form, in lower case, with no other words inside the note itself. It may
be preceded by a label naming the sheet, and it may be followed by a full stop, and
nothing may be interpolated between `showing`, `n`, `of` and `N`.

**`n` AND `N` COUNT COUNTED ROWS AND NOTHING ELSE**, as 5.1.1 defines a counted row:
unit rows on an entity sheet, the sheet's own rows on a reference table. A written row
that is not one of those is counted by neither, and the only such row this contract
permits inside a table is the explanatory row of an empty sheet, per 5.4.

**Where nothing was cut, `n` equals `N` and the note still ships.** A showing note is
the evidence the bound was evaluated, exactly as a zero count is the evidence a check
ran. **It is never omitted because there was no shortfall, and never omitted because a
capped sheet came in far under its cap.**

**THE SHOWING NOTE AND A SHORTFALL NOTE ARE TWO DIFFERENT NOTES.** The showing note
ships on every bounded sheet, always. A SHORTFALL note, which says a sheet holds fewer
rows than its own declared size allows, ships only where that is true. A rule written
for one of them is never read as governing the other.

**Agreement with SD-LNG-13:** the note carries no plural noun, so it reads correctly
at zero, at one and at many. That is why the form is `showing n of N` and not
`showing n of N rows`.

**The verification:** for each bounded sheet, count the built COUNTED rows on that
sheet's own basis per 5.1.1, parse the sheet's own note, parse the method section's note
for that sheet, and assert all three agree. A disagreement blocks publication.

**A STATEMENT THIS CONTRACT REQUIRES IN TWO PLACES IS RECONCILED, NEVER MERELY
REPEATED.** The showing note is required on the sheet and in the method section, and the
verification above reads both and asserts they agree; the duplication is the point,
because a reader at the grid and a reader at the method section each need the number
where they are standing. **Where a SKILL requires the same sentence in two places and
nothing reconciles them, that is a defect in the skill.** It names ONE PRIMARY LOCATION,
which is the place the statement is computed and published; the second location either
carries the reconciliation, as the method section does for the showing note, or carries
a cross-reference naming the primary. Two unreconciled copies of one figure make a
reader ask which of the two is current, and one of them will eventually be right.

## 5.3 THE NOTE BAND: the one place a per-sheet note lives

**Every per-sheet note goes in the NOTE BAND, and there is exactly one note band per
sheet.** The showing note is one. So is a shortfall note, an ordering note that says
what the sheet is sorted by, an extract's declaration of which sheet it extracts from,
and any other note a skill must state beside a grid rather than on the front panel.

**THE NOTE BAND, DEFINED EXACTLY:**

1. **It begins ONE BLANK SPACER ROW below the table's last row.** Table last row `r`;
   row `r + 1` is blank; the note band starts at row `r + 2`.
2. **Each note is ONE ROW, MERGED ACROSS THE FULL COLUMN SPAN OF THE TABLE**, starting
   in the table's first column. Where a sheet carries several notes they are
   consecutive rows in the same band, in a stated order, each merged the same way.
   **MERGED, NEVER MERELY STYLED ACROSS THAT SPAN**, per 2.10: a band styled across the
   span leaves the note in the first cell, overflowing into the rest, with element 7's
   border on the second cell drawn through whatever word is crossing it.
3. **It is LEFT ALIGNED, wrapped, in the body font, at the panel LABEL fill of element
   15, and it carries ELEMENT 7's BORDER ON ALL FOUR OUTER EDGES OF ITS MERGED REGION**,
   so it reads as a note rather than as a row of data and is bounded like every other
   populated cell on the sheet. **SITTING OUTSIDE THE TABLE RANGE EXEMPTS IT FROM NOTHING
   IN ELEMENT 7**, whose scope is the sheet and not the table. An earlier wording sent the
   note band to element 15 for its border, and the result was measured: three delivered
   workbooks shipped a populated, merged note band with no border on any side, directly
   beneath a table bordered on all four sides of every cell.
4. **Its row height is COMPUTED by 2.3**, against the SUMMED width of the merged span
   rather than against one column's width. A merged note that clips is the same defect
   as a clipped cell.

**WHY THERE AND NOWHERE ELSE, WHICH IS THE PART THAT WAS MISSING.** Four other
placements were tried. Three of them break a stated element. The fourth breaks
nothing at all and is invisible, which is its own way of failing:

| Placement | What it breaks |
|---|---|
| Above the header row | Element 1. It pushes the header off row 1, which breaks the freeze pane, the table range, the autofilter and every lookup by header name. |
| Inside the table range | Element 3, and worse: it is a row that is not a unit, so it sorts with the data, filters with the data, and is counted by anything that counts rows. |
| In one column below the table, in the FIRST column | Element 9 as it was written, since the first column is the right-aligned position column, and a sentence left-aligned there was a real measured violation. And it is nearly invisible. |
| In one column below the table, in the TRAILING NARRATIVE column | Nothing structurally, but the reader never sees it: on a wide sheet the trailing column is twenty columns to the right of where a reader is looking, and a note nobody reads is not a note. |

**The note band survives everything that matters.** A sort of the table does not reach
it, because it is outside the table range. It does not extend the table range, because
the blank spacer row terminates the populated block the table is built over. It does
not touch row 1. And it is where a reader's eye lands when they reach the end of the
grid, which is exactly when the count of rows they just read becomes a question.

**ELEMENTS 1, 3 AND 9 ARE RECONCILED TO IT IN THEIR OWN TEXT**, so no reader of an
element has to come here to discover that the note band is permitted: element 1
governs what is above the header row, element 3 forbids a populated DATA row outside
the table range, and element 9 governs alignment inside the table block.

**The note band is NOT a substitute for the front panel or the method sheet.** The
report title, the scope, the period and every caveat still live on the front panel per
element 1, and the showing note is still repeated in the method section and still
reconciled against the sheet, per the verification above. The note band carries the
notes that must sit BESIDE THE GRID THEY ARE ABOUT.


## 5.4 The explanatory row of an EMPTY sheet, and why it is not counted

**A SHEET THAT QUALIFIED ZERO UNITS SHIPS ITS HEADER ROW AND EXACTLY ONE EXPLANATORY
ROW.** It is a finished sheet with nothing in it, never a blank sheet and never a
missing one.

**WHERE THE ROW SITS, DECIDED HERE:** it is the FIRST AND ONLY DATA ROW OF THE TABLE,
INSIDE the table range, carrying in plain words why the sheet qualified nothing. It is styled exactly as a populated row is: element 7's
full grid across the whole width of the block and not merely the one cell holding the
text, element 8's font, wrap and top alignment, element 12's computed height. **AND THE
SENTENCE IS CARRIED IN A MERGED REGION RUNNING FROM THE TABLE'S SECOND COLUMN TO ITS
LAST**, per 2.10, because the sentence is longer than the second column and a sentence
allowed to overflow meets the third column's left border in the middle of a word. The
POSITION COLUMN stays a cell of its own and stays empty, so the counter's test below
reads exactly what it read before, and the merged region's own first cell is still the
table's SECOND column, which is what C2 asserts. Element 7 then bounds the region on its
four outer edges and no line falls inside the sentence at all.

**WHERE THE SENTENCE BEGINS, AND THE CONTRADICTION THIS RESOLVES.** The sentence begins in
the table's SECOND column, which is the first column after the POSITION COLUMN R1 puts in
first position, and the position column is LEFT EMPTY on this row because the counter's
test below reads exactly that emptiness. **AN EARLIER WORDING SAID THE ROW BEGINS IN THE
TABLE'S FIRST COLUMN AND, FOUR PARAGRAPHS LATER, THAT IT CARRIES NO VALUE IN THE FIRST
IDENTITY COLUMN, WHICH IS THE SAME COLUMN. BOTH COULD NOT HOLD**, so every correct run had
to break one of them on its own judgment, and what a run chose was measured: on three empty
sections of a delivered workbook the sentence was put in the SEVENTH column of a 23-column
sheet, the reason-for-rank column, six columns right of where the row begins. The result is
a bordered row 117 points tall, and on one sheet 180.75 points tall, whose first six columns
are a tall empty box sitting exactly where the reader looks first. **THE SECOND COLUMN IS
THE RESOLUTION** because it satisfies the counter's test, sits inside the frozen span, and
is the leftmost place a sentence can legally begin.

**THE ROW CARRIES ITS SENTENCE, AND A ROW THAT DOES NOT IS A FAILURE RATHER THAN AN EMPTY
SECTION.** The cell in the table's SECOND column holds a NON-EMPTY STRING stating, in plain
words, WHY the sheet qualified nothing. **A ROW THAT EXISTS, IS BORDERED, IS SIZED TO A COMPUTED HEIGHT
AND HOLDS NO STRING AT ALL FAILS THIS SECTION**, and it fails it more loudly than a
missing row would: a missing row is visibly missing, and a blank one looks finished.
Measured on a delivered workbook: three empty sections shipped their row 2 bordered on all
four sides across the width of the block, at 117, 117 and 180.75 points tall, with every
cell from the first column through the sixth EMPTY and the sentence sitting alone in the
seventh. What the reader meets at the left edge of the sheet, which is where the eye lands,
is a tall bordered empty box; the explanation is real and is off to the side of it. A row
holding NO string anywhere is the same defect taken one step further, and both fail.
**AN EMPTY SECTION IS A FINISHED SECTION WITH A SENTENCE IN IT, NEVER A BLANK BOX.** The
height, the borders and the styling are what make it LOOK finished; the sentence is what
makes it finished. The string is subject to element 16 and to R5 like any other written
value, and it is never a placeholder, a dash or a single space standing in for a sentence.

**IT IS NOT A COUNTED ROW AND IS NEVER COUNTED AS ONE.** `n` and `N` count counted
rows, per 5.1.1 and 5.2. On an empty sheet both are 0, the note reads `showing 0 of 0`,
and the sheet holds one written row. **R3 counts counted rows, so it reconciles 0
against 0 and passes.** This holds on a reference table exactly as on an entity sheet: a
reference table that qualified zero rows ships the same one explanatory row and the same
`showing 0 of 0`. A run that resolves the mismatch by writing `showing 1 of 1` has told
the reader a unit exists that does not, which is the one outcome this section exists to
forbid.

**HOW A COUNTER TELLS THE TWO APART, MECHANICALLY AND WITHOUT JUDGMENT:** the
explanatory row carries NO value in the sheet's **FIRST IDENTITY COLUMN**, which is the
position column R1 puts in first position on every grid of every class, and it is the
ONLY data row on the sheet. Both conditions hold together on an empty sheet and on
nothing else. **The test reads the first identity column rather than an identifier
column, because a REFERENCE TABLE carries no unit identifier and the earlier wording
gave it no test at all**; every grid this contract can emit has a first identity column
by R1, so the test is total over both classes. A sheet carrying one or more counted rows
never carries an explanatory row, so a row with a blank first identity column on a
populated sheet is a defect and not an explanation.

**WHY IT SITS INSIDE THE TABLE RANGE RATHER THAN IN THE NOTE BAND.** The note band was
the obvious alternative and it is worse in two ways. A table object over a header row
with no data rows is degenerate: some engines repair it, some drop the table, and the
sheet then loses the style, the stripes and the filter that every other sheet carries,
so the empty section stops looking like a finished section. And the objection that
normally forbids a non-unit row inside a table, that such a row sorts, filters and
counts as though it were a unit, cannot arise here: it is the only row on the sheet,
there is nothing to sort it against, and 5.2 has just said what counts it. **The
exemption is therefore narrow and stated as such: exactly one non-unit row is permitted
inside a table range, only on a sheet that qualified zero units, and only as this
section describes it.**

**The note band still ships on an empty sheet**, carrying the showing note and any
ordering note, exactly as it does on a populated one. The explanation of WHY the sheet
is empty lives in the row; the count lives in the note band; neither substitutes for
the other.

---

# PART 6: THE UNIT NOUN

**UNIT_NOUN_PLURAL and UNIT_NOUN_SINGULAR are BOUND VARIABLES, and where nothing is
bound the plural default is "Accounts" and the singular is "Account".** A retailer
binds Stores and Store; a hospital binds Facilities and Facility; a service business
binds Clients and Client. The default is generic and is used verbatim in sheet names,
headers and prose until an organization binds its own word.

**Bind it once and it is everywhere.** No skill hard-codes a unit noun in a sheet
name, a header, a message or a heading. Every occurrence reads the variable, and the
verification scans the built artifact for any hard-coded unit noun that does not match
the bound value.

**Where the population shape declares its own noun**, per POPULATION_SHAPE
`unit_singular` and `unit_plural`, THAT noun governs for that population and these
scalars are the fallback used where only one population is declared.

---

# PART 7: THE VERIFICATION, WHICH RUNS BEFORE PUBLICATION

**Every element and every requirement in this file has a programmatic verification,
and the whole set runs BEFORE the artifact is published. A failure BLOCKS
publication.** This is the half that was missing: the rules existed and nothing ran
them.

## 7.1 How the verification runs

**READ BACK THROUGH THE ENGINE, NEVER FROM THE BUILD INTENTION.** Open the BUILT
artifact and read structural attributes directly: the actual freeze pane, the actual
table range, the actual fill of a header cell, the actual column width, the actual row
height. A value-only read verifies nothing about formatting, and asserting what the
code intended to do is not verification.

**If the environment cannot expose those attributes, the element gate CANNOT RUN, and
an element gate that cannot run has FAILED.** The artifact is not published and the
reason is stated. This is a hard failure rather than a skipped check, because a
formatting defect is invisible in the data and a reader has no way to notice it.

**A VERIFICATION NEVER SCANS ITS OWN RECORD, AND THE RECORD IS DECLARED SO THE SCAN CAN
SKIP IT.** Every verification row records its result in the matrix of 7.2, that matrix
lives inside the artifact, and a row whose record must be auditable has to say WHAT IT
SEARCHED FOR. A row that then searches the whole artifact for those same strings finds
its own record and fails itself. It was measured: writing the searched terms into the
method sheet took the raw occurrence count from 22 to 44 and turned a passing gate into
a failing one, so a run that recorded its evidence failed and a run that hid its
evidence passed. **That inversion is the exact thing an audit trail exists to prevent,
and the artifact is not the thing at fault.**

**The mechanism, and it is one range:** the verification matrix on the method sheet
occupies a DECLARED CELL RANGE, and the method sheet states that range. **Every
STRING-SEARCHING verification excludes that range from its own scan and says in its own
record that it did so.** Excluding it costs nothing, because the range is written by the
verification pass and is read by no consumer of the data; and the record then holds what
it must hold, which is the terms searched, the count found and the result.

**THE EXCLUSION IS FOR STRING SEARCHES AND FOR NOTHING ELSE.** Element 16, the character
gate, still scans every cell of every sheet including that range, because a character
outside the permitted set is a defect wherever it sits and a character scan cannot be
tripped by a record of itself. A verification that reads a structural attribute rather
than a string is unaffected. **No verification may exclude a range in order to pass;
the only permitted exclusion is a row's own record of its own search.**

## 7.2 The verification matrix

Verified per sheet, on every run, and recorded as a matrix so a reader can see which
sheet failed which element rather than being told the workbook failed:

**EVERY ROW NAMES THE SHEET CLASS IT APPLIES TO**, per 2.0, because a row that says
"every sheet" is a row that fails a correct workbook on the first panel it meets. A
row is run on the sheets its class column names and is NOT APPLICABLE elsewhere, with
the sheet class as the stated reason.

| # | Sheet class it applies to | What is asserted |
|---|---|---|
| 1 | ENTITY SHEET, REFERENCE TABLE | The header row is row 1 and cell A1 holds a header string rather than a title. NOT APPLICABLE on a PANEL SHEET, whose A1 is a title by element 15. |
| 2 | ENTITY SHEET, REFERENCE TABLE | The freeze pane is at row 2 and at the column whose header NAME follows the last FROZEN identity column; the reason-for-rank column is the first column after the identity columns and is NOT inside the frozen span; and the summed WIDEST-CASE built width of the frozen span is at or below `FROZEN_SPAN_MAX_WIDTH`, or the span is one column. **The anchor's header NAME is IDENTICAL on every sheet of the artifact that carries the full identity block**, per 4.1.2's one walk; a workbook whose sheets freeze different numbers of identity columns FAILS this row even where each sheet is individually within the bound. Where 4.1.2's bound truncated the span, the method sheet carries the ONE truncation record for the artifact and the freeze column is the first identity column that did not fit. |
| 3 | ENTITY SHEET, REFERENCE TABLE | A table object exists over exactly the populated block, with no blank row inside its range and no populated DATA row outside it. The note band of 5.3 is outside the range and does not fail this row. **WHERE THE ENGINE COULD NOT CARRY BOTH THIS TABLE OBJECT AND ROW 6's VISIBLE FILTER OVER ONE RANGE, THIS ROW IS RECORDED NOT APPLICABLE with the conflict named**, which is a pass under element 3's own text, and ROW 6 STILL RUNS AND STILL BLOCKS PUBLICATION ON FAILURE. A run that clears this row by dropping the visible filter has inverted the two and fails row 6. |
| 4 | ENTITY SHEET, REFERENCE TABLE | The table style name matches on every one of them in the workbook, row stripes are on, **and the style named is one whose own header band is a LIGHT band under DARK text, agreeing in direction with element 5's band rather than opposing it**. A style whose header band opposes element 5's fails this row even where every sheet carries the identical string, because identity across sheets was never the only thing this row was for. |
| 5 | ENTITY SHEET, REFERENCE TABLE | Every header cell carries the direct fill, bold and font colour, read back from the cell. **AND ALL THREE OF 2.8's ASSERTIONS RUN ON THE PAIR THAT WAS READ BACK, NOT ONLY THE FIRST.** The INTENDED pair clears `TEXT_SEPARATION_MIN`. The header text still clears `TEXT_SEPARATION_MIN` against the DEFAULT SHEET GROUND, which is what a renderer shows when THE FILL FAILS TO RENDER. And the container's DEFAULT TEXT INK still clears `TEXT_SEPARATION_MIN` against the band, which is what a renderer shows when THE FONT COLOUR FAILS TO RENDER. **A pair that passes the first and fails either of the other two FAILS THIS ROW and blocks publication**, however good it looks in the engine that built it: the old wording verified the intended pair alone, which is the blind spot 2.8 names. All three measured separations are recorded, with the floor beside them. |
| 6 | ENTITY SHEET, REFERENCE TABLE | **The SHEET'S OWN FILTER is read back FROM THE SHEET of the BUILT artifact, in the form the reader's engine looks for it**, and it spans every column of the populated block element 3 fixes. **A FILTER THAT EXISTS ONLY INSIDE A TABLE OBJECT, AND NOT ON THE SHEET, IS SCORED ABSENT AND FAILS THIS ROW**, however completely the container describes it, because absent to the reader is what absent means. **EXACTLY ONE filter object stands over that range**: two over one range fails this row and blocks publication, and so does none. **THIS ROW READ THE FILTER BACK OUT OF THE TABLE CONTAINER, AND IT CERTIFIED WORKBOOKS THAT SHIPPED WITH NO VISIBLE FILTER ON ANY SHEET**, which is the same shape as the failure recorded at row 7: a check that reads a property somewhere other than where the reader meets it certifies the defect, and a recorded pass standing behind a defect is worse than no check. The mechanism, the range and the count of filter objects are all recorded. |
| 7 | ENTITY SHEET, REFERENCE TABLE, PANEL SHEET | **Every populated cell of the SHEET'S USED RANGE carries a border on all four sides**, and the walk covers THE USED RANGE rather than the table range: the header row, every data row, the explanatory row of 5.4, **EVERY NOTE-BAND ROW of 5.3, and EVERY PANEL ROW**. A MERGED REGION is walked as ONE cell and its border is asserted on the OUTSIDE of the region, on all four outer edges. **The border COLOUR is asserted too**: it is COLOR_GRIDLINE, and COLOR_GRIDLINE clears `LINE_SEPARATION_MIN` against the default sheet ground and against COLOR_TITLE_BAND, per 2.8. **THIS ROW WALKED THE TABLE RANGE, AND IT PASSED THREE WORKBOOKS THAT VISIBLY FAILED ELEMENT 7**, whose note bands were populated, merged across the sheet width and unbordered on every side, directly beneath fully bordered tables. **A CHECK SCOPED MORE NARROWLY THAN THE RULE IT ENFORCES IS WORSE THAN NO CHECK, BECAUSE IT CERTIFIES THE DEFECT:** with no check the defect is merely unnoticed, and with a too-narrow one it ships with a recorded pass standing behind it, which is the thing a reader of the matrix relies on. Any row of this matrix whose walk is narrower than its element's stated scope is stale for the same reason and is widened rather than explained. **AND EVERY BAND IS ASSERTED MERGED RATHER THAN MERELY STYLED**, per 2.10: a run of cells sharing one fill, one of which holds a string longer than its own cell, FAILS THIS ROW, because the border this row asserts on the next cell of that run is a line drawn through a word. |
| 8 | ENTITY SHEET, REFERENCE TABLE | Every populated cell, the note band included, carries the body font, top alignment and wrap. |
| 9 | ENTITY SHEET, REFERENCE TABLE | Within the table block, every column named in RIGHT_ALIGN_COLUMNS is right aligned and no other column is; every column declared a STATUS GRID COLUMN is centred, meets all three of 2.5's conditions and no other column is centred; every remaining column is left aligned. The note band is outside the table block and is not tested by this row. |
| 10 | ENTITY SHEET, REFERENCE TABLE | For every column, `H` recomputed from the header string and `usable_header` recomputed from the BUILT width satisfy `floor( usable_header ) >= H`, per 2.2.4. No width was multiplied by CHAR_WIDTH_FACTOR, and the only conversion applied is 2.2 step 5's. **And the SUMMED built width of every column on the sheet is at or under `GRID_MAX_TOTAL_WIDTH`, or 2.7's relief ladder was run to exhaustion and the method sheet carries the overage record: the bound, the measured total, the overage and the columns that account for it in descending width order.** `GRID_MAX_TOTAL_WIDTH` is read before the build and is never raised to clear this row. **AND `T` recomputed from the header string and the column's built values satisfies `floor( usable_body( W ) ) >= T`, per 2.2.4 and 2.10**, so no column is narrower than the longest word it displays. A column failing it fails this row and blocks publication, and where `T` exceeded `COLUMN_WIDTH_MAX_CHARS` the method sheet carries the over-long-token record: the column, the token, its length and the width it forced. |
| 11 | ENTITY SHEET | The narrative column is last and its built width sits between `NARRATIVE_WIDTH_MIN_UNITS` and `NARRATIVE_WIDTH_MAX_UNITS`, read as built width units and never converted, or above the ceiling where its own header floor required it, which is recorded. NOT APPLICABLE on a sheet that carries no narrative column, named. |
| 12 | ENTITY SHEET, REFERENCE TABLE | Every row's built height, the note band's merged rows included, is at least the height 2.3 requires of its wrapped content against the BUILT widths, with lines counted by the greedy wrap of 2.2 primitive 1. |
| 13 | ENTITY SHEET, REFERENCE TABLE | Alert shading matches the bands exactly, or the element is recorded NOT APPLICABLE with element 13's own reason, which is that the sheet carries no elapsed-time column. In either case every other conditional fill on the sheet is a value of `CLASSIFICATION_FILLS` on a declared CLASSIFICATION COLUMN meeting all four conditions of 2.6; `CLASSIFICATION_VOCABULARY`'s resolution rule is TOTAL over the populated cells of that column; **`CLASSIFICATION_FILLS` is INJECTIVE, with one entry per state, no state without one and no two states sharing a fill**; and no value in it is COLOR_ALERT_WARN or COLOR_ALERT_OVERDUE. This row never reads 2.5's centring condition; a left-aligned classification column passes it. |
| 14 | ENTITY SHEET, REFERENCE TABLE | The header row's built height is at least what 2.4 computes from the built widths, and no header's recomputed line count exceeds HEADER_MAX_LINES. HEADER_MAX_LINES is never raised to clear this row. |
| 15 | PANEL SHEET | The panel palette is carried in full, **and every band on the panel goes through all three of 2.8's assertions against its own text colour**, exactly as row 5 does for the header band. A panel band that reads only while both halves of its formatting render fails this row. Borders on a panel are asserted by row 7, which walks every populated cell of every sheet of every class, and are not re-asserted here. |
| 16 | EVERY SHEET OF EVERY CLASS | No character outside the permitted range appears in any cell value, sheet name or the filename. |
| C1 | EVERY SHEET OF EVERY CLASS | **Every colour written anywhere in the artifact is OPAQUE, per 2.9**, read back from the built artifact: every fill, every font colour and every border colour on every populated cell of every sheet. Where the container's colour field carries an alpha byte, that byte is `FF` and nothing else. **An alpha of `00` is named in the failure text as the TRANSPARENT case**, because it is the one that renders correctly in the engine that wrote it and invisibly elsewhere, so it is the one a run will otherwise ship. This row is scoped to the WHOLE artifact and never to one block of one sheet, per the scope lesson recorded at row 7. |
| R1 | ENTITY SHEET, REFERENCE TABLE | A position column stands in first position, headed HDR_RANK on a merit order and HDR_POSITION otherwise, and a reason-for-rank column is present. |
| R2 | MERIT TIER SETS ONLY | Ranks are continuous across the merit tiers, with no gap, no duplicate and no restart, and no unit identifier appears on two MERIT TIERS. A unit appearing on two merit tiers is a defect and blocks publication. The assertion does NOT run between a census and an extract of that census, which share identifiers by construction per 4.2.3, and it does not run against a directed sheet. |
| C2 | ENTITY SHEET, REFERENCE TABLE, on a sheet that qualified ZERO units | The explanatory row of 5.4 exists, is the only data row, is bordered and sized like a populated row, **AND THE CELL IN THE TABLE'S SECOND COLUMN HOLDS A NON-EMPTY STRING saying why the sheet qualified nothing**, with the POSITION COLUMN empty so the counter's test of 5.4 still reads it. A bordered, sized row holding no string at all FAILS this row and blocks publication: it is the shape a reader reads as a finished section and it explains nothing. **A row whose string sits further right than the second column ALSO FAILS IT**, and that is the case actually measured: the sentence was in the seventh column of a 23-column sheet, behind six empty cells of a bordered row 117 points tall. NOT APPLICABLE, and a pass with its reason recorded, on a sheet carrying one or more counted rows. |
| C3 | EVERY SHEET OF EVERY CLASS | **No word in the artifact is broken by a cell line, asserted two ways per 2.10.** Every populated cell whose string needs more usable characters than its OWN cell supplies is a MERGED REGION spanning at least the columns that supply them, read back from the built artifact; an unmerged cell overflowing its own boundary FAILS, and so does a band whose cells share a fill without being merged, which is the case actually reported: a title band styled across three cells, its text overflowing, with the second cell's left border through the middle of a word. And for every column of every grid, `floor( usable_body( W ) ) >= T`, which is row 10's second assertion read from this side. This row is scoped to the WHOLE artifact and never to one block of one sheet, per the scope lesson recorded at row 7. |
| R3 | EVERY BOUNDED SHEET, whatever its class: capped by REFERENCE_CAP, bounded by a tier size, or bounded by an extract's declared size, per 5.1.1 | The built COUNTED row count reconciles against the sheet's own note band and the method section's note for that sheet, with `N` read from 5.1.1's table for that sheet's own bound. **A counted row is the sheet's own DATA row per 5.1.1: a unit row on an entity sheet, the sheet's own row on a reference table**, so this row runs identically on both classes and needs no local reading. The explanatory row of an empty sheet is not a counted row and is not counted, per 5.4. |
| R4 | The RANKED SHEET SET of the workbook | On a merit tier set, the reference tier's row count equals 4.3's authoritative row-count form, including the zero-row case. On a census workbook, the census row count equals 4.2.2's form, min( REFERENCE_CAP , eligible_count ), and an extract holds its declared size. The row runs on every workbook; only the form it reads changes. |
| R5 | THE WHOLE WORKBOOK, LESS ITS OWN RECORD | No hard-coded unit noun appears anywhere that disagrees with the bound value. **The declared verification-matrix range of the method sheet is EXCLUDED from this scan, per 7.1, because that range is where this row's own record of the nouns it searched for lives.** The record states the terms searched, the count found, the result, and that the exclusion was applied. Any other string-searching row added later is scoped the same way and for the same reason. |
| D1 to D6 | THE DOCX ARTIFACT | Each requirement of PART 3, in place of every element above. |

## 7.3 What the contract guarantees, per run

1. Every declared section ships, in order, with an empty one carrying its header and one explanatory row inside its table range, per 5.4, **that row carrying a non-empty sentence saying why the section is empty**, and that row is counted as a counted row by nothing.
2. Every entity sheet satisfies every element that APPLIES to it, and every not-applicable is recorded with its reason.
3. The identity block is structurally identical across every entity sheet, AND the frozen span holds the SAME SET OF COLUMNS on every one of them, because the span is walked once for the artifact per 4.1.2 and never once per sheet.
4. Ranks are continuous across the merit tiers, with no duplicate identifier BETWEEN TWO MERIT TIERS. A census and an extract of that census carry the same identifiers by design and are outside this guarantee, per 4.2.3.
5. Every entity row has a populated identity block, a populated reason for rank, and a populated narrative column.
6. Identifier and postal-style columns read as TEXT so leading zeros survive.
7. No character outside the permitted range appears anywhere in the artifact.
8. Every heading, every SHEET NAME and every COLUMN HEADER is in Title Case, in the one convention `TITLE_CASE_HEADINGS` states and validates. The only exemption is a string the ORGANIZATION BOUND, which ships in the case it was bound in because those are the organization's own words. The exemption for table column headers is WITHDRAWN.
9. Every BOUNDED sheet, per 5.1.1, reconciles against its own showing note on its own counting basis, which sits in that sheet's note band per 5.3 and is repeated in the method section.
10. A sample of units re-read from the source matches the artifact exactly.
11. Every grid's summed built width is at or under `GRID_MAX_TOTAL_WIDTH`, or the relief ladder was run and the residual overage is recorded with the columns that account for it. No column was dropped, narrowed below its own header floor, or had a meaning-carrying value shortened to get there.
12. Every header band and every panel band is READABLE UNDER ALL THREE RENDERINGS of 2.8: the intended pair, the fill failing to render, and the font colour failing to render. No band in the artifact depends on both halves of its own formatting arriving.
13. Every colour written anywhere in the artifact is explicitly OPAQUE, per 2.9, and every populated cell of every sheet of every class carries a border on all four sides in a gridline colour that clears `LINE_SEPARATION_MIN` against the sheet ground and against the header band.
14. NO WORD ANYWHERE IN THE ARTIFACT IS BROKEN BY A CELL LINE, per 2.10: no string overflows its own cell boundary, every band wider than one cell is MERGED across exactly the span it needs rather than styled across it, and every column is at least as wide as the longest unbreakable token it displays, so the wrap never breaks a word and no token was ever shortened to make one fit.
15. Every entity sheet and every reference table carries a VISIBLE filter, read back from the SHEET of the built artifact in the form the reader's engine looks for, spanning every column, with exactly one filter object over that range.

---

# PART 8: WHAT A SKILL MAY AND MAY NOT DO WITH THIS FILE

**MAY:** cite an element by number; state which elements are not applicable to one of
its sheets and why; bind any variable this file names; add a sheet, which then
inherits every element automatically; DECLARE each sheet's CLASS per 2.0 and, for a
ranked sheet, its KIND per 4.2, both of which this file requires it to declare.

**MAY NOT:** restate an element's standard in its own words; state a different value
for any figure this file gives; state a count of the elements; carry a literal derived
last rank; assert a row cap that is not REFERENCE_CAP; emit an entity sheet without a
position column and a reason-for-rank column; put the reason-for-rank column anywhere
but immediately after the identity columns; head a position column with a band label;
write a header string as a literal where this file names a variable for it; keep a
closed list of not-applicable reasons that cannot express an element's own stated
exemption; MULTIPLY a column width being set by CHAR_WIDTH_FACTOR, or apply any
conversion to a width at a step 2.2 does not name; centre a column that is not a
declared STATUS GRID COLUMN under 2.5; carry a classification fill on a column that is
not a declared CLASSIFICATION COLUMN under 2.6, or make a classification fill conditional
on the centring test of 2.5; give two states of `CLASSIFICATION_VOCABULARY` one fill in
`CLASSIFICATION_FILLS`; bind a value of `CLASSIFICATION_FILLS` to either alert
colour; raise HEADER_MAX_LINES to clear a failing element 14; walk the frozen span once
per sheet rather than once for the artifact; drop a column, narrow a column below its own
header floor, or shorten a value that carries meaning in order to meet the grid width
bound `GRID_MAX_TOTAL_WIDTH` sets, or raise `GRID_MAX_TOTAL_WIDTH` to clear a failing grid; bind COLOR_TITLE_BAND to a DARK band or COLOR_HEADER_TEXT to a LIGHT ink, or name a
TABLE_STYLE_NAME whose own header band opposes element 5's direction; lower
`TEXT_SEPARATION_MIN` or `LINE_SEPARATION_MIN` to clear a colour that failed 2.8; verify
the INTENDED text-and-band pair without also verifying both degraded renderings; write any
colour with an alpha byte other than `FF`, or pad a six-digit colour to eight digits with a
`00` alpha; scope element 7's border walk to the table range, or to anything narrower than
the sheet's used range; ship an explanatory row under 5.4 that carries no string, or that begins anywhere but the table's second column; carry the filter of element 6 only inside a table object, set a second filter object over a range that already has one, or trade away the visible filter in order to keep a table object; style a band across a span without MERGING it across that span, or let any string overflow its own cell boundary; narrow a column below `T`, the longest unbreakable token it displays, or break, hyphenate, truncate, ellipsize or shrink a token so that it fits a narrower column; Title-Case a string the ORGANIZATION BOUND, or ship a heading, a sheet name or a column header this bundle wrote in any case but Title Case; or exclude any range from
a verification other than a row's own record under 7.1.

**A skill that appears to disagree with this file is stale, and this file governs.**
That sentence is the whole reason this file exists as one contract rather than as
three copies of a contract.
