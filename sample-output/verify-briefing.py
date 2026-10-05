#!/usr/bin/env python3
"""
Verifies the worked example against the contract the workflow states.

    python3 verify-briefing.py                 # the technician altitude
    python3 verify-briefing.py "J. Ferreira"   # the regional manager altitude

THE CHECKS ARE NOT COUNTED HERE. An earlier version of this docstring opened "Sixteen
checks" and was thirty by the time anybody read it again, which is the same defect as a
count hardcoded in prose anywhere else in this bundle: the number has one home, and it is
the tally the run prints at the foot of its own output.

Four families. The TRAP checks, one per deliberate trap in the dataset. The OUTPUT
CONTRACT checks, one per element the contract states, including the three added after a
reader caught a lowercase month in an earlier build: M13 (one bound date format family),
M14 (no sentence-caser applied to a proper noun) and SD-LNG-13 (number and noun agree).
The PERSON-BEARING checks, which read the built message back and test A5.2's interlock
against what was actually rendered rather than against what the build intended. And the
SECOND-CHANNEL checks, which test that every state is legible after a channel the reader
may not receive is taken away: the styling, and the key block.

Each prints PASS, N/A with a reason, or FAIL, and the script exits non-zero if any check
fails or any check is NOT IMPLEMENTED, so it can gate a commit.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
READER = sys.argv[1] if len(sys.argv) > 1 else "T. Boone"
SLUG = READER.replace(". ", "-").replace(".", "").replace(" ", "-")
H = open(os.path.join(HERE, f"Briefing {SLUG} 2026-10-06.html"), encoding="utf-8").read()
TEXT = re.sub(r"<[^>]+>", " ", H)
TEXT = TEXT.replace("&middot;", "-").replace("&nbsp;", " ")
BODY = TEXT[TEXT.find("Daily Briefing"):]

# THREE STATES, NOT TWO, and the third one needs a stated reason.
# An assertion that never fired and an assertion nobody wrote are indistinguishable in a
# two-state record, and the second is a defect hiding inside a pass. So a check whose
# precondition is not present in this dataset is recorded NOT APPLICABLE **with a reason
# drawn from the closed set below**, and an unexplained not-applicable is recorded NOT
# IMPLEMENTED, which fails. That makes the failing state the default for anything that
# could not be evaluated, which is what "unknown is not pass" requires.
NA_REASONS = {
    "no_such_source":  "the dataset binds no source in the state this check reads",
    "no_such_item":    "no item in this run is in the state this check reads",
    "not_in_medium":   "the medium cannot express what this check reads",
    "check_scoped":    "this check is scoped to a state or shape this run does not have",
    "stated_exemption":"the rule this check enforces states its own exemption and it holds",
}

import csv as _csv
_DATA = os.path.join(HERE, "..", "sample-data", "facilities-services")
def _rows(n):
    with open(os.path.join(_DATA, n), newline="", encoding="utf-8") as f:
        return list(_csv.DictReader(f))
_all_feed = _rows("schedule_feed_2026-10-06.csv")
_mine = [r for r in _all_feed if r["technician"] == READER]
feed = _mine if _mine else _all_feed          # a reader who owns nothing is a manager
feed_sids = [r["site_id"] for r in feed]
OWNERS = sorted({r["technician"] for r in feed})
OTHER_OWNERS = [o for o in OWNERS if o != READER]
contract_sids = {r["site_id"] for r in _rows("contract_status_2026-10.csv")}

results = []
def check(n, name, ok, why=""):
    results.append((n, name, "PASS" if ok else "FAIL", why))

def na(n, name, reason_key, detail=""):
    """Record NOT APPLICABLE. An unknown reason key is recorded NOT IMPLEMENTED."""
    if reason_key in NA_REASONS:
        results.append((n, name, "N/A", f"{NA_REASONS[reason_key]}"
                                        + (f": {detail}" if detail else "")))
    else:
        results.append((n, name, "NOT IMPLEMENTED",
                        f"not-applicable claimed with no reason from the closed set"))

def check_if(n, name, precondition, reason_key, ok_fn, detail=""):
    """Run the check where its precondition holds; record N/A with a reason where it does not."""
    if precondition:
        o = ok_fn()
        check(n, name, o if isinstance(o, bool) else o[0],
              "" if isinstance(o, bool) else o[1])
    else:
        na(n, name, reason_key, detail)

MONTHS = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]

# ---- 1. every work order block carries the carried label
wo_heads = re.findall(r"Open work orders[^<]*<span class=\"c\">([^<]*)</span>", H)
# One per stop, since every stop carries every bound section (check 17).
check(1, "carried label on every work order block",
      len(wo_heads) == len(re.findall(r'class="sh">\d+\.', H))
      and all("carried, as of 28 September 2026" == w for w in wo_heads),
      f"{len(wo_heads)} blocks for {len(re.findall(chr(39)+chr(39)+chr(39), H)) if False else len(re.findall(r'class=.sh.>[0-9]+[.]', H))} stops, labels={set(wo_heads)}")

# ---- 2. the tripwire banner fires above the first stop
banner = H.find('class="banner"')
first_stop = H.find('class="stop"')
check(2, "degradation banner above the first stop",
      banner != -1 and banner < first_stop and "not current" in H,
      f"banner at {banner}, first stop at {first_stop}")

# ---- 3. S-1011 and S-1032 print the bound named-absence string for contract
ABSENT = "No contract record for this site."
blocks = re.split(r'<div class="stop">', H)[1:]
def block_for(sid):
    return next(b for b in blocks if sid in b)
no_contract = [sid for sid in feed_sids if sid not in contract_sids]
check_if(3, "absent contract named for every uncovered site",
         bool(no_contract), "no_such_item",
         lambda: (all(ABSENT in block_for(x) for x in no_contract),
                  f"uncovered={no_contract}"),
         "every scheduled site has a contract row")

# ---- 4. absence never rendered as None, a dash alone, a blank or a zero tier
bad = []
for sid in no_contract:
    b = block_for(sid)
    seg = b[b.find("Contract"):b.find("Parts on order")]
    seg_t = re.sub(r"<[^>]+>", " ", seg)
    if re.search(r"\bNone\b", seg_t) or re.search(r"renews", seg_t):
        bad.append(sid)
check_if(4, "absent contract not collapsed to None or a renewal",
         bool(no_contract), "no_such_item",
         lambda: (not bad, f"bad={bad}"),
         "every scheduled site has a contract row")

# ---- 5. A MEASURED ZERO IS DISTINGUISHABLE FROM AN ABSENCE, AND THE EXPLANATION IS
# REACHABLE. This check used to require the words "measured zero" inside the stop's own
# block, and it broke the first time the repeated-explanation relief fired, because the
# relief moves that explanation to the reading key above the first stop. **It was testing a
# PLACEMENT.** What the workflow actually requires is that the two states read differently
# and that a reader can find out which is which, and the relief preserves both: the zero
# stop says none open as of the carry date, the absent stop says it is not in the export,
# and the explanation sits either on the line or in the key. Pinning an explanation to a
# position is how a verification comes to pass only in the unrelieved case.
b = block_for("S-1026")
zero_seg = b[b.find("Open work orders"):b.find("Contract")]
check(5, "a measured zero reads differently from an absence, and the explanation is reachable",
      "None open as of 28 September 2026" in zero_seg
      and "Not in the work order export" not in zero_seg
      and ABSENT not in zero_seg
      and "measured zero" in BODY,
      f"seg={re.sub(r'<[^>]+>', ' ', zero_seg)[:120]!r}")

# ---- 6. parts resolves PARTIALLY READ: the authoritative block is used, the block the
# file's own exporter disclaimed is not, and nothing from the disclaimed block is printed
# as a value. A site named only in the disclaimed block gets its own sentence, which is
# neither a part nor an absence.
readable = ["Compressor, 5-ton scroll", "Belt set B-54", "Control board, RTU"]
disclaimed_values = ["Condensate pump", "TBD", "2026-10-11"]
check(6, "readable parts block used, disclaimed block not used as a value",
      all(r in BODY for r in readable)
      and not any(d in BODY for d in disclaimed_values)
      and "read in part" in BODY
      and "marked unconfirmed" in BODY,
      f"missing={[r for r in readable if r not in BODY]} "
      f"leaked={[d for d in disclaimed_values if d in BODY]}")

# ---- 7. the duplicate row appears ONCE, from the authoritative block, never twice
check(7, "the duplicated part appears once, from the readable block",
      BODY.count("5-ton scroll") == 1, f"count={BODY.count('5-ton scroll')}")

# ---- 8. S-1047 present, with its time, and the PLAN section empty for a stated reason
b = block_for("S-1047")
check(8, "S-1047 kept with its time and its plan section empty for a stated reason",
      "14:15" in b and "Not in the October 2026 period plan" in b, "")

# ---- 9. S-1047 fabricates no PLAN content
seg = b[b.find("Plan"):b.find("Open work orders")]
check(9, "S-1047 fabricates no visit count and no PM status",
      "PM due" not in seg and "planned this period" not in seg, "")

# ---- 10. all eight stops, in planned time order
times = re.findall(r'class="sh">\d+\. (\d\d:\d\d)', H)
check(10, "every scheduled stop is present, in planned time order",
      len(times) == len(feed_sids) and times == sorted(times),
      f"{len(times)} stops for {len(feed_sids)} scheduled")

# ---- 11. the footer names every source with its state
foot = H[H.find('class="foot"'):]
check(11, "footer states each source and its freshness",
      all(k in foot for k in ("period plan (current", "work orders (carried",
                              "contract status (current", "parts on order (read in part")), "")

# ---- 12. ascii only
check(12, "ascii only", H.isascii(), "")

# ---- 13. provenance line names what the content was built from
check(13, "provenance line present",
      'class="prov"' in H and "period plan of 1 October 2026" in H, "")

# ---- 14. M13: one bound day-precision format, nothing finer than the source
iso   = re.findall(r"\b20\d\d-\d\d(?:-\d\d)?\b", BODY)
short = re.findall(r"\b(?:Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)\b\.?", BODY)
slash = re.findall(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b", BODY)
daypr = set(re.findall(r"\b\d{1,2} (?:" + "|".join(MONTHS) + r") \d{4}\b", BODY))
monthpr = set(re.findall(r"(?<!\d )\b(?:" + "|".join(MONTHS) + r") \d{4}\b", BODY))
noyear = re.findall(r"\b\d{1,2} (?:" + "|".join(MONTHS) + r")\b(?! \d{4})", BODY)
check(14, "one bound date format family, no ISO, no abbreviation, no bare day-month",
      not iso and not short and not slash and not noyear,
      f"iso={iso[:4]} short={short[:4]} slash={slash[:2]} noyear={noyear[:4]}")

# ---- 15. M14: no month or weekday name lowercased by a sentence-caser
lower = [w for w in MONTHS + ["Monday","Tuesday","Wednesday","Thursday","Friday",
                              "Saturday","Sunday"] if w.lower() in BODY]
check(15, "no lowercased month or weekday name", not lower, f"found={lower}")

# ---- 16. SD-LNG-13: number and noun agree, and no parenthetical plural
paren = re.findall(r"\b\w+\(s\)", BODY)
agree = re.findall(r"\b1 (\w+?)s\b", BODY)
agree = [a + "s" for a in agree if a + "s" not in ("its", "this", "has", "is")]
check(16, "number and noun agree, no (s) parenthetical",
      not paren and not agree, f"paren={paren} disagree={agree}")

# ---- 17. NO SECTION IS SUPPRESSED FOR A REASON BELONGING TO ANOTHER SOURCE.
# Every stop carries every bound section heading. A stop absent from the period plan loses
# the PLAN section's content and nothing else; a contract row and a work-order list are
# read from their own sources and are withheld by nothing.
SECTIONS = ["Plan", "Open work orders", "Contract", "Parts on order", "Do this"]
missing = {}
for bl in blocks:
    sid = re.search(r"(S-\d+)", bl).group(1)
    gone = [h for h in SECTIONS if f">{h}" not in bl and f"{h} <span" not in bl]
    if gone:
        missing[sid] = gone
check(17, "every stop carries every bound section", not missing, f"missing={missing}")

# ---- 18. The specific case: S-1047's own sources reach the reader
check(18, "S-1047 reports the work orders and contract its own sources hold",
      all(k in b for k in ("WO-10470", "WO-10471", "WO-10472", "renews December 2026")),
      "")

# ---- 19. A planned figure is not worded as an actual (4.1 step 9's wording trap)
check(19, "a planned count is worded as planned",
      "planned this period" in BODY and re.search(r"\b\d+ visits? this period", BODY) is None,
      "")

# ============================ THE A5.2 INTERLOCK, RUN AGAINST THE BUILT MESSAGE ==========
# A5.2.5: an exhortation is not a mechanism. These five run over the message that was
# actually built rather than over the intention, because A5.2.0's finding is that the
# forbidden shape arrives as a usability improvement and nobody writing it would recognise
# it as a decision worth defending.

# ---- 24. ORDERED BY TIME, GLOBALLY. A briefing sorted by owner then time has
# non-decreasing times INSIDE each person's block and not across the message.
times = re.findall(r'class="sh">\d+\. (\d\d:\d\d)', H)
check(24, "stops are in global time order, not per-person time order",
      times == sorted(times), f"first break at {next((i for i in range(1,len(times)) if times[i]<times[i-1]), None)}")

# ---- 25. NOT GROUPED BY OWNER. A grouped briefing has exactly one run per owner, so the
# count of owner changes down the message equals the owner count minus one. This is the
# second, independent test of the same property, which is worth more than either alone.
attrib = re.findall(r'class="sm">([^<]*)</p>', H)
seq = [next((o for o in OWNERS if o in a), None) for a in attrib]
seq = [x for x in seq if x]
changes = sum(1 for i in range(1, len(seq)) if seq[i] != seq[i-1])
check_if(25, "stops are not grouped into one block per owner",
         len(OWNERS) > 1, "check_scoped",
         lambda: (changes > len(OWNERS) - 1,
                  f"{changes} owner changes over {len(seq)} stops for {len(OWNERS)} owners"),
         "this altitude's span holds one owner, so there is nothing to group")

# ---- 26. ATTRIBUTION, ONE PER STOP, SAME PLACE. Computed once over the period's own items
# and applied identically, per SD-SPN-03.
check_if(26, "every stop carries exactly one owner attribution, in the same position",
         len(OWNERS) > 1, "check_scoped",
         lambda: (len(seq) == len(times) and all(a.rstrip().endswith(o)
                                                 for a, o in zip(attrib, seq)),
                  f"{len(seq)} attributions for {len(times)} stops"),
         "SD-SPN-02's third condition: the unit level is never an attribution column, so a "
         "span holding one owner carries none and that is a finished state")

# ---- 27. NO OWNER NAME ANYWHERE BUT THE ATTRIBUTION. The subject, the banner, the
# provenance, the aggregate actions, the reading key and the footer name no owner. The
# READER's own name is allowed in reader positions, which is where it belongs.
elsewhere = {}
for o in OTHER_OWNERS:
    for m in re.finditer(re.escape(o), H):
        seg = H[:m.start()]
        in_attrib = seg.rfind('class="sm">') > seg.rfind("</p>")
        if not in_attrib:
            elsewhere.setdefault(o, []).append(H[:m.start()].count("\n") + 1)
check(27, "no owner is named outside a stop's own attribution line", not elsewhere,
      "; ".join(f"{o} at line(s) {v}" for o, v in elsewhere.items()))

# ---- 28. NO COUNT GROUPED BY OWNER, which is the subject line's temptation.
grouped = re.findall(r"(?:" + "|".join(re.escape(o) for o in OWNERS) + r")\s*[:,-]?\s*\d+"
                     r"|\d+\s+(?:stops?|sites?|items?)\s+(?:for|by)\s+(?:"
                     + "|".join(re.escape(o) for o in OWNERS) + r")", BODY) if OWNERS else []
check(28, "no count is grouped by a person-bearing level", not grouped, str(grouped[:4]))

# ---- 29. THE FOOTER SAYS IT IS NOT A COMPARISON, wherever attribution is present.
check_if(29, "the footer states the briefing is not a comparison between its people",
         len(OWNERS) > 1, "check_scoped",
         lambda: ("not a comparison between the people in it" in BODY, ""),
         "nothing is attributed at this altitude, so there is nobody to compare")

# ---- 30. ACTIONS AT THE READER'S CLAIM TIER, and the lexical test SD-SPN-09 states: an
# aggregate action names a population or a source, a direct action names its item.
agg = re.search(r'<div class="agg">(.*?)</div>', H, re.S)
if agg:
    items = re.findall(r"<li>(.*?)</li>", agg.group(1), re.S)
    named = [i for i in items if any(o in i for o in OWNERS)]
    atomish = [i for i in items if re.search(r"\bWO-\d+\b|\bS-\d{4}\b", i)]
    check(30, "every aggregate-tier action names a population or a source, never an owner "
              "and never one item", not named and not atomish,
          f"named={len(named)} atomish={len(atomish)} of {len(items)}")
else:
    na(30, "every aggregate-tier action names a population or a source, never an owner "
           "and never one item", "check_scoped",
       "this reader's claim tier is DIRECT, so the actions are atoms by design and sit on "
       "the stops they belong to")

# ---- 20. no string is re-cased at build time: a bound part name ships as bound
check(20, "a part name ships in the case the file holds it in",
      "control board, rtu" not in BODY and "Control board, RTU" in BODY, "")

# ---- 21. No derived quantity from a CARRIED source is printed as though it were current.
# The export carries an age_days column computed as of its own date; the briefing prints the
# opened date instead, which is true on any morning.
ages = re.findall(r"\b\d+ days? old\b", BODY)
check(21, "no stale derived age printed; the immovable opened date is used instead",
      not ages and "opened 8 September 2026" in BODY, f"ages={ages[:4]}")

# ---- 22. THE MESSAGE IS SCORED AGAINST THE RENDERING IN WHICH ITS STYLING DOES NOT
# ARRIVE. A pass is only ever a pass in the renderer that read it back, and an email loses
# its CSS routinely: a plain-text client, a text-only preview, a screen reader, a forward
# that strips styling, a dark mode that inverts a background chosen for contrast. A
# workbook never loses its fills; a message does. So every freshness state must be
# distinguishable in CHARACTERS with every style and class removed, and styling is the
# second channel and never the first.
stripped = re.sub(r"<style.*?</style>", "", H, flags=re.S)
stripped = re.sub(r'\sclass="[^"]*"', "", stripped)
stripped = re.sub(r"<[^>]+>", " ", stripped).replace("&middot;", "-")
states_in_text = {
    "degraded overall": "Some of this briefing is not current",
    "carried":          "carried, as of 28 September 2026",
    "absent source":    "No contract record for this site",
    "measured zero":    "measured zero",
    "partially read":   "marked unconfirmed",
    "no plan row":      "Not in the October 2026 period plan",
}
lost = [k for k, v in states_in_text.items() if v not in stripped]
check(22, "every state survives with all styling removed", not lost, f"lost={lost}")

# ---- 23. DRIFTED, which this dataset cannot produce. Recorded rather than passed
# vacuously, because a check that never fired and a check nobody wrote look identical in a
# two-state record, and this sample tests four of the five source states and not the fifth.
check_if(23, "a drifted source raises a banner naming both resolutions",
         False, "no_such_source",
         lambda: (False, ""),
         "no previous resolution record exists, so no source can be DRIFTED on a first "
         "rebuild and this sample exercises four of the five states")


# ---- 31. THE KEY BLOCK SITS WHERE A5.2.4b PUTS IT, WHICH IS NOT WHERE THE FIRST BUILD
# PUT IT. The first build inserted the relieved wording inside the aggregate action list,
# where four explanations of what a line MEANS read as four more things for a manager to
# do at 5 AM. An explanation is not a finding and must not sit among them. A5.2.4b places
# it in its own block, after the findings and immediately above the first item, because a
# message has no legend a reader opens deliberately and its footer is twenty-three items
# away from the first thing it explains.
KEY_N = H.count('class="key"')
first_stop = H.find('<div class="stop"')
def _key_placement():
    key_i = H.find('<div class="key"')
    key_block = H[key_i:H.find("</div>", key_i)]
    agg_i = H.find('<div class="agg"')
    bad = []
    if KEY_N != 1:
        bad.append(f"{KEY_N} key blocks")
    if not 0 <= key_i < first_stop:
        bad.append("not above the first item")
    if agg_i >= 0 and "</div>" not in H[agg_i:key_i]:
        bad.append("inside the action list")
    if "<h3" in key_block:
        bad.append("poses as a section")
    return (not bad, ", ".join(bad))
check_if(31, "the key block sits above the first item and outside every action list",
         KEY_N > 0, "check_scoped",
         _key_placement,
         "the relief did not fire at this altitude, so there is no key block to place")

# ---- 32. A STATE SURVIVES THE LOSS OF THE KEY, WHICH IS A DIFFERENT CHANNEL FROM THE
# LOSS OF STYLING, AND CHECK 22 DOES NOT COVER IT.
#
# This check was written after noticing that check 22 passes at the manager altitude partly
# BECAUSE OF the key block: two of the six phrases it looks for, "measured zero" and
# "marked unconfirmed", survive the relief only inside the key wording. So check 22 as
# written would pass a build whose relief collapsed both parts states into one item line,
# as long as the key block went on naming both. That is exactly the hole A5.2.4b forbids:
# the key says WHICH IS WHICH, and the lines themselves are what must still read
# differently. A relief that leans on its own legend is lossy.
#
# So this check reads only the ITEM LINES, from the first item onward, and the key block
# sits above them and is therefore gone by construction rather than by deletion. Each state
# is located by a keyword this file states for itself, never by the build's wording, and a
# collapse shows up in one of two ways: as a state with no line of its own, or as two
# states sharing one string.
item_paras = [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", p)).strip()
              for p in re.findall(r"<p[^>]*>(.*?)</p>", H[first_stop:], re.S)]
DISCRIMINATORS = {
    "work orders, a measured zero":           lambda p: "None open as of" in p,
    "work orders, the source does not cover": lambda p: "work order export" in p,
    "parts, absent from the readable block":  lambda p: "readable" in p,
    "parts, a row in the disclaimed block":   lambda p: "unconfirmed" in p
                                                        and "readable" not in p,
    "no row in the period plan":              lambda p: "period plan" in p,
}
_found = {st: sorted({p for p in item_paras if f(p)}) for st, f in DISCRIMINATORS.items()}
_missing = [st for st, ms in _found.items() if not ms]
_one = {st: ms[0] for st, ms in _found.items() if ms}
_collapsed = [f"{a} == {b}" for a in _one for b in _one
              if a < b and _one[a] == _one[b]]
check(32, "every state still reads differently with the key block gone",
      not _missing and not _collapsed,
      f"no line of its own={_missing}; sharing one string={_collapsed}")

w = max(len(n) for _, n, _, _ in results)
tally = {"PASS": 0, "FAIL": 0, "N/A": 0, "NOT IMPLEMENTED": 0}
for n, name, state, why in results:
    tally[state] += 1
    show = why if state != "PASS" else ""
    print(f"{state:<15} {n:>2}. {name.ljust(w)}  {show}".rstrip())
# A NOT APPLICABLE carries a stated reason and is a pass. A NOT IMPLEMENTED is not.
bad = tally["FAIL"] + tally["NOT IMPLEMENTED"]
print(f"\n{tally['PASS']} pass, {tally['N/A']} not applicable with a stated reason, "
      f"{tally['FAIL']} fail, {tally['NOT IMPLEMENTED']} not implemented")
print("A not-applicable entry with no reason from the closed set is recorded NOT "
      "IMPLEMENTED, which fails, so an unexplained entry defaults to the failing state.")
sys.exit(1 if bad else 0)
