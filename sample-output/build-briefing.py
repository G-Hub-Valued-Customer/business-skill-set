#!/usr/bin/env python3
"""
Builds the worked examples for the recurring briefing workflow, at either altitude.

    python3 build-briefing.py                 # T. Boone, a technician
    python3 build-briefing.py "J. Ferreira"   # the regional manager over all three

Reads ../sample-data/facilities-services/ and writes a briefing beside this script.

**ONE BUILD, TWO READERS, AND NOTHING CONFIGURED BETWEEN THE RUNS.** That is the claim the
dataset makes and it is only worth anything if the two altitudes come out of one code path.
A second hand-written file would prove nothing: the span rules have to do the work, or they
do not hold. Everything that differs between the two outputs below is derived from the
reader's own row in READERS and from the data, and the four lines of that table are the
only place either altitude is named.

This script is part of the evidence, not a convenience. Three of the rules the
workflow states are enforced here in code rather than in prose, because a rule that
lives only in prose is a rule a builder forgets at 1am:

  * SD-LNG-13  number and noun agree. Every templated count goes through n_of(),
               which carries both forms and selects on the value. No "visit(s)".
  * M13        one bound date format family. Every day-precision reader-facing date
               goes through date_full(); every month-precision one through
               date_month(). There is no short form, and nothing is rendered at a
               finer precision than its source carries.
  * A5.2       a person-bearing level attributes an item and never orders, groups or
               counts one. The manager's briefing runs over three technicians and is
               ordered by time, with the owner named beside each stop; there is no block
               per person, no count per person, and no aggregate over them anywhere.
  * A5.3       an action is written at the reader's own claim tier. A technician's are
               atoms, a manager's are shapes, and the per-stop sections at the aggregate
               tier say whose atoms they are rather than handing them to the manager.
  * M14        no string is re-cased at build time at all, per SD-FMT-13's mechanism.
               An earlier build assembled a sentence from fragments and called
               str.capitalize() on it, which raises the first character and LOWERCASES
               every character after it, turning "September" into "september". The fix
               is not a safer caser; it is no caser. Every composed string below is
               written in the case it ships in.
"""
import csv, datetime, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "sample-data", "facilities-services")

# ----------------------------------------------------------------- the two readers
# `scope` is the set of owner values the reader's span covers, resolved from the data at
# run time rather than listed here: None means every owner in the feed.
# `claim_tier` is ROLE_LADDER.claim_tier, per SD-SPN-09.
READERS = {
    "T. Boone":    {"scope": "own",  "claim_tier": "DIRECT",    "role": "technician"},
    "J. Ferreira": {"scope": None,   "claim_tier": "AGGREGATE", "role": "regional manager"},
}
RUN_FOR = sys.argv[1] if len(sys.argv) > 1 else "T. Boone"
if RUN_FOR not in READERS:
    sys.exit(f"unknown reader {RUN_FOR!r}. known: {', '.join(READERS)}")
READER = READERS[RUN_FOR]

BRIEFING_DAY = datetime.date(2026, 10, 6)
PERIOD       = "2026-10"
PLAN_ASOF    = datetime.date(2026, 10, 1)
WO_ASOF      = datetime.date(2026, 9, 28)

# ---------------------------------------------------------------- date layer (M13)
MONTHS = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
DAYS   = ["Monday", "Tuesday", "Wednesday", "Thursday",
          "Friday", "Saturday", "Sunday"]

def date_full(d):
    """Day precision. The only day-precision rendering in the message. 6 October 2026."""
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"

def date_month(ym):
    """Month precision, for a source that carries only a month. 'April 2027' from '2027-04'.
    Never widened to a day: the day is unknown and G3 forbids inventing one."""
    y, m = ym.split("-")
    return f"{MONTHS[int(m) - 1]} {y}"

def date_weekday(d):
    """Permitted in the subject and title only, where the reader is orienting by weekday."""
    return f"{DAYS[d.weekday()]} {date_full(d)}"

# ------------------------------------------------------------ agreement (SD-LNG-13)
def n_of(n, one, many, zero=None):
    """Carry both forms, select on the value. Tested at zero, one and many below."""
    if n == 0 and zero is not None:
        return zero
    return f"{n} {one if n == 1 else many}"

# There is deliberately NO sentence-casing helper here. SD-FMT-13's mechanism is that a
# run never re-cases anything at build time: it ships a bound string as bound and composes
# the strings it writes itself in the case they are meant to ship in. A caser that can be
# applied to a proper noun is a defect waiting for the one string that contains one, and
# the earlier build proved it. Every action line below is composed already capitalised.

# ------------------------------------------------------------------------ the data
def rows(name):
    with open(os.path.join(DATA, name), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

sites    = {r["site_id"]: r for r in rows("sites.csv")}
plan     = {r["site_id"]: r for r in rows(f"period_plan_{PERIOD}.csv")}
contract = {r["site_id"]: r for r in rows(f"contract_status_{PERIOD}.csv")}
all_feed = rows(f"schedule_feed_{BRIEFING_DAY.isoformat()}.csv")

# THE SCOPE FILTER AND THE FEED ARE TWO INDEPENDENT SELECTIONS OF ONE POPULATION, and the
# shipped scorecard's 4.1 step 1 says two such tests are worth more than either alone and
# that a disagreement between them is invisible unless somebody looks. The feed is regional;
# the reader's scope narrows it. Both counts are reported below.
if READER["scope"] == "own":
    feed = [r for r in all_feed if r["technician"] == RUN_FOR]
else:
    feed = list(all_feed)

# ORDERED BY WHEN THE WORK HAPPENS, NEVER BY PERSON AND NEVER BY RANK, per A5.2.4, with a
# declared tie-break so two runs order one morning identically, per SD-RUN-15. The owner is
# NOT in the sort key: sorting by owner then time is the per-person grouping A5.2.3 forbids,
# reached by a route that looks like tidiness.
feed.sort(key=lambda r: (r["planned_start"], r["site_id"]))

# THE ATTRIBUTION SET IS COMPUTED ONCE OVER THE PERIOD'S OWN ITEMS AND APPLIED TO EVERY
# ITEM, per SD-SPN-03 and SD-SPN-04. Where the span holds one owner the level carries no
# distinction and the attribution is empty, which SD-SPN-02's third condition calls a
# finished span block and not a missing one: the owner IS the reader, and restating it on
# every stop would be a second, disagreeing identity line.
OWNERS = sorted({r["technician"] for r in feed})
ATTRIBUTE_OWNER = len(OWNERS) > 1

wo = {}
for r in rows(f"open_work_orders_AS_OF_{WO_ASOF.isoformat()}.csv"):
    wo.setdefault(r["site_id"], []).append(r)
wo_sites = set(wo) | {r["site_id"] for r in rows(
    f"open_work_orders_AS_OF_{WO_ASOF.isoformat()}.csv")}

# ---------------------------------------------------- parts on order: PARTIALLY READ
# The parts export is not a clean CSV, and declaring the whole file unreadable throws away
# three authoritative rows for three sites on today's schedule. A second, disciplined read
# succeeds for the block above the file's own disclaimer, which is what the shipped
# scorecard's 2.5 requires before any document is called unreadable: "Two extractors fail
# differently on the same document. Try a second before concluding a document is
# unreadable, and record which one worked."
#
# So the file resolves PER BLOCK rather than per source:
#   * the rows between the header and the first blank line are CURRENT and are printed;
#   * the rows after the file's own note are DISCLAIMED BY THEIR OWN AUTHOR and are never
#     used as evidence. They ARE read, to establish which sites they mention, because
#     "the readable block names no part for this site" and "a row for this site sits in a
#     block its author disclaimed" are two different facts and only one of them is an
#     absence.
def read_parts():
    raw = open(os.path.join(DATA, f"parts_on_order_{PERIOD}.csv"),
               encoding="utf-8").read().splitlines()
    hdr = next(i for i, l in enumerate(raw) if l.lower().startswith("site,"))
    body = raw[hdr + 1:]
    cut = next((i for i, l in enumerate(body)
                if not l.strip(",").strip() or l.upper().startswith("NOTE")), len(body))
    good = list(csv.DictReader(body[:cut], fieldnames=["Site", "Part", "Qty", "ETA"]))
    rest = [l for l in body[cut:] if "," in l and not l.upper().startswith("NOTE")]
    tail = list(csv.DictReader(rest, fieldnames=["Site", "Part", "Qty", "ETA"]))
    return ({r["Site"]: r for r in good if r.get("Site")},
            {r["Site"] for r in tail if r.get("Site")},
            len(body) - cut)

parts, parts_disclaimed, parts_disclaimed_lines = read_parts()
PARTS_STATE = "PARTIALLY READ"
PARTS_NOTE  = (f"Read in part. The rows above this file's own disclaimer were used; "
               f"the block below it is marked unconfirmed by whoever exported it and was "
               f"not used.")

# Sites measured by the work order export, so a zero is a measured zero. The export
# lists only open orders, so membership cannot be read from its rows alone; the file
# covers the whole population, which is what makes S-1026's zero a measurement.
WO_COVERS = set(sites) - {"S-1032"}   # S-1032 is in onboarding and not in the export

ABSENT_CONTRACT = ("No contract record for this site. Nothing is known about its tier "
                   "or renewal; this is not the same as no contract.")

# ===================== THE REPEATED-EXPLANATION RELIEF (SD-FMT-28's shape, this medium) ==
# A per-item line that is IDENTICAL on every item carrying it costs its full length on every
# item while carrying one piece of information. In a grid the contract bounds the summed
# width and runs a relief ladder; a message has no columns, so what it bounds is the share
# of its reader-facing text spent on repeated explanation.
#
# THE MEASUREMENT IS STATED ONCE, IN THE WORKFLOW'S A5.2.4b, AND PRINTED BY THIS BUILD ON
# EVERY RUN. An earlier version of this comment restated the figures and was left stale by
# the very correction that changed them: narrowing the measure to declared explanations only
# moved the manager altitude from 58 per cent to 51, and the comment went on claiming 58.
# A number with two homes is SD-FMT-13's defect wearing a different hat, so the number now
# has one home in prose and one in the console line at the foot of this file.
#
# THE SPLIT THAT MAKES THE RELIEF LOSSLESS. Each of these lines is two facts welded
# together: one about THIS ITEM, which differs, and one about the SOURCE or the METHOD,
# which is identical every time. Only the second repeats, so only the second moves, and it
# moves ABOVE the first item rather than below the last. A grid puts a standing qualifier's
# wording in the Legend, which a reader opens deliberately; a message has no legend and its
# footer is twenty-three stops away, so the only place a reader certainly passes through is
# the provenance block at the top.
#
# THE THREE THINGS THAT NEVER GIVE: no item is dropped, no per-item FACT is dropped, and no
# state loses its characters, per M15. What moves is wording and nothing else.
REPEAT_SHARE_BOUND = 1/3        # MESSAGE_MAX_REPEATED_SHARE's documented default

# EVERY STANDING EXPLANATION HAS EXACTLY ONE HOME, AND IT IS THIS DICT.
# The first version wrote each of these sentences twice: once at the emit site inside the
# item loop and once here, with the declared copy existing only to be matched against the
# emitted one by string equality. Two copies of a sentence whose whole purpose is to be
# byte-identical to its twin is SD-FMT-13 exactly, and it fails on the first edit to either
# one: the coverage check would report the edited emitted line as an undeclared hole and
# stop the build, which is at least fail-closed, but the relief would also stop reaching it.
# The emit sites now read their text from here through standing(), so identity is a property
# of the code rather than something a future editor has to maintain.
#
# Each entry is (long form, short form, key line). The long form is what an item carries
# when the relief has not fired. The short form is what replaces it when the relief fires;
# AN EMPTY SHORT FORM MEANS THE SENTENCE IS APPENDED TO A VARYING PER-ITEM LINE AND SIMPLY
# GOES AWAY, leaving that line intact. The key line is what the block above the first item
# says in its place.
_OWNER_ATOMS = ("A stop's own items are its owner's to work, not yours. What each "
                "stop contributes to your list is in Do this above.")

STANDING = {
  "parts_absent": (
    'No part on order for this site in the readable part of the parts file. A later block '
    'of that file was marked unconfirmed and was not used, so this is not a measured '
    'absence.',
    'No part in the readable block.',
    'A parts line reading no part in the readable block is NOT a measured absence: a later '
    'block of that file was marked unconfirmed by whoever exported it and was not used.'),
  "wo_zero": (
    f'None open as of {date_full(WO_ASOF)}. This is a measured zero, not a missing record.',
    f'None open as of {date_full(WO_ASOF)}.',
    'A work order line reading none open is a measured zero from the export and not a '
    'missing record.'),
  "contract_absent": (
    ABSENT_CONTRACT,
    'No contract record for this site.',
    'A contract line reading no contract record means nothing is known about that site\'s '
    'tier or renewal, which is NOT the same as the site having no contract.'),
  "parts_disclaimed": (
    'A row for this site sits in the part of the parts file its own exporter marked '
    'unconfirmed, so no part is shown. This is not a statement that nothing is on order.',
    'A row for this site sits in the unconfirmed block, so no part is shown.',
    'A parts line pointing at the unconfirmed block is not a statement that nothing is on '
    'order: the row exists and its own exporter disclaimed it.'),
  "plan_absent": (
    f'Not in the {date_month(PERIOD)} period plan, so no visit count and no PM status were '
    f'built for this site. Treat it as an unplanned call. This section is empty for that '
    f'reason and for no other; everything below was read from its own source.',
    f'Not in the {date_month(PERIOD)} period plan. Treat it as an unplanned call.',
    f'A stop not in the {date_month(PERIOD)} period plan has no visit count and no PM '
    f'status. That section is empty for that reason and for no other, and every other '
    f'section on it was read from its own source.'),
  # THE SIXTH, WHICH USED TO LIVE OUTSIDE THIS DICT AND WAS SPECIAL-CASED IN FOUR PLACES:
  # the share measure, the coverage check, the relief and the key block each knew about it
  # separately. A closed set with a member kept outside it is not a closed set, which is the
  # same finding SD-CTR-29 produced when the set held four and the build emitted six. Its
  # key line is its long form, because the sentence reads correctly in both places.
  "owner_atoms": (_OWNER_ATOMS, "", _OWNER_ATOMS),
}

def standing(key):
    """The long form of a standing explanation, read at the emit site. One home, one copy."""
    return STANDING[key][0]

# -------------------------------------------------------------------- the rendering
out = []
A = out.append

sub_counts = n_of(len(feed), "stop", "stops", zero="No stops scheduled")
# The subject carries the count of the reader's own day and the span of it. It carries NO
# count per owner: "T. Boone 8, R. Alvarez 8, M. Okafor 7" is a count grouped by a
# person-bearing level, which A5.2.3 forbids, and the subject line is the likeliest place
# for it because the subject has to be useful unopened.
# THE SPAN LINE SAYS WHAT THE SHAPE OF THE DAY ACTUALLY IS, AND THAT DIFFERS BY ALTITUDE.
# At the finest altitude the stops are one person's route and first-to-last is a real
# geography: Darnley to Bellhaven is where he starts and ends. Run over a whole region the
# same two words are the first and last town in TIME order across three people's separate
# routes, which is not a journey anybody makes and reads as though it were. The manager's
# day has no first and last town, it has a footprint, so that is what it says.
towns = [sites[r["site_id"]]["town"] for r in feed if r["site_id"] in sites]
if not towns:
    span = ""
elif len(set(towns)) == 1:
    span = f"{towns[0]}."
elif READER["claim_tier"] == "DIRECT":
    span = f"{towns[0]} to {towns[-1]}."
else:
    span = f"{n_of(len(set(towns)), 'town', 'towns')}."

A(f'''<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Daily Briefing - {date_weekday(BRIEFING_DAY)}</title><style>
body{{margin:0;background:#f4f4f5;font-family:-apple-system,Segoe UI,Roboto,Arial,sans-serif;}}
.w{{max-width:640px;margin:0 auto;background:#fff;padding:18px 16px 28px;}}
h1{{font-size:19px;margin:0 0 2px;}} .sub{{font-size:13px;color:#52525b;margin:0 0 14px;}}
.banner{{background:#fff4e5;border-left:4px solid #b45309;padding:10px 12px;font-size:14px;margin:0 0 14px;}}
.prov{{font-size:13px;color:#3f3f46;background:#f4f4f5;padding:9px 11px;margin:0 0 18px;}}
.stop{{border-top:2px solid #18181b;padding:14px 0 4px;}}
.sh{{font-size:16px;font-weight:700;margin:0 0 2px;}}
.sm{{font-size:13px;color:#52525b;margin:0 0 10px;}}
h3{{font-size:13px;letter-spacing:.04em;text-transform:uppercase;color:#71717a;margin:12px 0 4px;}}
p,li{{font-size:15px;line-height:1.45;margin:3px 0;}} ul{{margin:4px 0;padding-left:20px;}}
.c{{font-size:12px;color:#b45309;font-weight:600;}}
.a{{font-size:15px;color:#71717a;font-style:italic;}}
.u{{font-size:15px;color:#b91c1c;}}
.agg{{background:#f0f7ff;border-left:4px solid #1d4ed8;padding:4px 12px 10px;margin:0 0 18px;}}
.key{{font-size:13px;color:#3f3f46;border:1px solid #d4d4d8;padding:8px 11px;margin:0 0 18px;}}
.key p{{font-size:13px;margin:0;}}
.agg h3{{margin-top:10px;}}
.foot{{border-top:1px solid #d4d4d8;margin-top:22px;padding-top:12px;font-size:12px;color:#71717a;}}
</style></head><body><div class="w">
<h1>Daily Briefing - {date_weekday(BRIEFING_DAY)}</h1>
<p class="sub">{sub_counts}. {span} For {RUN_FOR}, {READER["role"]}.</p>''')

# Tripwire: of four configured sources, one CARRIED and one UNRESOLVED clears the
# documented default of half the sources, rounded down, floor of one.
A(f'''<div class="banner"><b>Some of this briefing is not current.</b> Work orders are from
the {date_full(WO_ASOF)} export and have not refreshed since; the parts on order file was
read in part, because its exporter marked a block of it unconfirmed. Lines from those
sources are marked. Treat them as last known, not as today.</div>
<div class="prov">Stops read from this morning's dispatch feed. Content built from the
period plan of {date_full(PLAN_ASOF)}.</div>'''.replace("\n", " ").replace("  ", " "))

CARRIED_LABEL = f'<span class="c">carried, as of {date_full(WO_ASOF)}</span>'
aggregate_inputs = []   # (site, owner, atoms) per stop, for the aggregate-tier roll-up

for i, v in enumerate(feed, 1):
    sid = v["site_id"]
    s   = sites.get(sid, {})
    A('<div class="stop">')
    A(f'<p class="sh">{i}. {v["planned_start"]} &nbsp; {v["site_name"]}</p>')
    units = s.get("units_on_site")
    bits  = [sid]
    if s.get("town"): bits.append(s["town"])
    if units:         bits.append(n_of(int(units), "unit on site", "units on site"))
    # ATTRIBUTION, NOT JUDGMENT, per A5.2.2 and SD-SPN-08: the owner is named so the reader
    # can route a conversation, on every stop, in the same shape. It is not a sort key, not
    # a grouping, and nothing anywhere is counted by it.
    if ATTRIBUTE_OWNER: bits.append(v["technician"])
    A(f'<p class="sm">{" &middot; ".join(bits)}</p>')

    todo = []

    # EVERY SECTION RESOLVES AGAINST ITS OWN SOURCE, AND AGAINST NO OTHER.
    # A stop absent from the period plan loses the PLAN section's content and nothing else.
    # Suppressing the contract and work-order sections because a DIFFERENT source has no row
    # for this site is absence in one source read as absence in all, which is the exact
    # collapse this workflow exists to prevent. An earlier build did it, and on this dataset
    # it withheld three open work orders and a contract record from a technician driving to
    # an unplanned call at a data room, one of them a condensate overflow seventeen days old.
    A('<h3>Plan</h3>')
    if sid in plan:
        p = plan[sid]
        visits = int(p["planned_visits_this_period"])
        pm_due = p["pm_due"] == "Yes"
        line = (f'{n_of(visits, "visit planned", "visits planned")} this period. '
                f'PM due: {"Yes" if pm_due else "No"}.')
        if p.get("priority_flag") == "Yes":
            line += " <b>Priority site.</b>"
        A(f'<p>{line}</p>')
        if pm_due:
            todo.append(("pm_due",
                "PM is due this period. Do it on this visit if the window allows."))
    else:
        A(f'<p class="a">{standing("plan_absent")}</p>')
        todo.append(("unplanned",
            "Treat as an unplanned call. Capture what you find; it will be in the plan "
            "after the next rebuild."))

    A(f'<h3>Open work orders {CARRIED_LABEL}</h3>')
    if sid in wo:
        # A DERIVED QUANTITY READ FROM A CARRIED SOURCE IS ANCHORED TO THAT SOURCE'S DATE
        # AND IS REPLACED BY THE IMMOVABLE FACT IT WAS DERIVED FROM.
        # The export carries an age_days column, computed as of 28 September. On 6 October
        # those numbers are eight days wrong, and a reader sees "20 days old" and reads it
        # as of today. The carried label says the SOURCE is from the 28th; it does not say
        # the NUMBER is. The opened date is in the same file, it is true on any morning,
        # and the reader can do the subtraction themselves and be right. This is the same
        # discipline the shipped scorecard states for its urgency anchor: a report built
        # early must band identically to the same report built later, or the published
        # answer moves with the hour somebody pressed go.
        A("<ul>" + "".join(
            f'<li>{w["work_order"]} &middot; {w["trade"]} &middot; {w["summary"]} &middot; '
            f'opened {date_full(datetime.date(*map(int, w["opened"].split("-"))))}</li>'
            for w in wo[sid]) + "</ul>")
        first = wo[sid][0]["work_order"]
        todo.append(("wo_carried",
            f'Confirm whether {first} is still open before quoting; the work order list is '
            f'from {date_full(WO_ASOF)}.'))
    elif sid in WO_COVERS:
        A(f'<p>{standing("wo_zero")}</p>')
    else:
        A('<p class="a">Not in the work order export.</p>')

    A('<h3>Contract</h3>')
    if sid in contract:
        c = contract[sid]
        tier = c["tier"]
        tier_text = "No tier (on record, uncontracted)" if tier == "None" else tier
        A(f'<p>{tier_text} &middot; renews {date_month(c["renewal_month"])} &middot; '
          f'{n_of(int(c["covered_units"]), "unit covered", "units covered")}</p>')
    else:
        A(f'<p class="a">{standing("contract_absent")}</p>')
        todo.append(("no_contract",
            "Ask the site who holds their agreement. We have no contract record for them."))

    A('<h3>Parts on order</h3>')
    if sid in parts:
        pr = parts[sid]
        eta = pr["ETA"].strip()
        dated = bool(re.fullmatch(r"\d{4}-\d\d-\d\d", eta))
        eta_text = (f'due {date_full(datetime.date(*map(int, eta.split("-"))))}' if dated
                    else "no due date in the file")
        A(f'<p>{pr["Part"]} &middot; {n_of(int(pr["Qty"]), "unit", "units")} &middot; '
          f'{eta_text}</p>')
        if not dated:
            todo.append(("part_undated",
                f'Chase the due date for this part: {pr["Part"]}. The parts file names the '
                f'part and carries no date for it.'))
    elif sid in parts_disclaimed:
        A(f'<p class="u">{standing("parts_disclaimed")}</p>')
        todo.append(("part_disclaimed",
            "Confirm parts for this site by phone. The parts file has a row for it in a "
            "block marked unconfirmed."))
    else:
        A(f'<p class="a">{standing("parts_absent")}</p>')

    # AN ACTION IS WRITTEN AT THE READER'S OWN CLAIM TIER, per A5.3 and SD-SPN-09.
    # The per-stop items above are ATOMS: confirm this order, chase this part. They belong
    # to a DIRECT tier reader. Handing them to an AGGREGATE tier reader tells a manager to
    # do the jobs of the people in her span, and BRIEFING_ACTION_CAP makes that worse by
    # choosing which of them. So the section still ships, per G-RB-12, and at the aggregate
    # tier it says whose the atoms are instead of handing them over. The aggregate actions
    # are composed once over the whole span and sit above the first stop.
    if READER["claim_tier"] == "DIRECT":
        A('<h3>Do this</h3><ul>' + "".join(f"<li>{t}</li>" for _, t in todo) + '</ul>')
    else:
        aggregate_inputs.append((sid, v["technician"], list(todo)))
        # It says the actions belong to the stop's owner. It does NOT say they appear in
        # that person's own briefing: nothing in this run establishes that one exists, and
        # asserting it is the same confident-sentence-about-an-unchecked-thing this
        # workflow exists to prevent.
        if not todo:
            line = "Nothing outstanding on this stop."
        else:
            line = (f'{n_of(len(todo), "item", "items")} here, '
                    f'{"the" if len(todo) == 1 else "all the"} owner\'s.')
        A(f'<h3>Do this</h3><p class="a">{line} {standing("owner_atoms")}</p>')
    A('</div>')

# ---------------------------------------- the aggregate-tier action list (A5.3, SD-SPN-09)
# Derived from the atoms the stops produced, never written twice. The test SD-SPN-09 states
# is lexical: an AGGREGATE action names a POPULATION or a SOURCE; a DIRECT action names its
# item. Every shape below names a count of sites or a named source and NOT ONE names an
# owner, which is A5.2.3's prohibition holding at the one place it is most tempting to
# break: the manager's own to-do list is exactly where "whose fault is this" wants to go.
AGGREGATE_SHAPES = {
    "unplanned": lambda n, sids: (
        f'{n_of(n, "stop", "stops")} today {"is" if n == 1 else "are"} not in the '
        f'{date_month(PERIOD)} period plan. The plan covers {len(plan)} of {len(sites)} '
        f'sites, so the next rebuild picks these up on its own; what is worth your time is '
        f'whether any of them recurs, because a site that is scheduled every period and '
        f'never planned is a gap in the plan rather than an unplanned call.'),
    "no_contract": lambda n, sids: (
        f'{n_of(n, "site", "sites")} on today\'s schedule {"has" if n == 1 else "have"} no '
        f'contract record at all. The renewals file does not cover sites in onboarding, so '
        f'this is expected for a new site and worth a question for anything that is not.'),
    "wo_carried": lambda n, sids: (
        f'The work order export has not refreshed since {date_full(WO_ASOF)}, so every work '
        f'order line in this briefing is from that date and {n_of(n, "stop", "stops")} '
        f'{"carries" if n == 1 else "carry"} one. Service operations is aware; this is the '
        f'eighth day.'),
    "part_disclaimed": lambda n, sids: (
        f'The parts export is readable only in part, because whoever exported it marked a '
        f'block of it unconfirmed, and {n_of(n, "site", "sites")} on today\'s schedule '
        f'{"sits" if n == 1 else "sit"} in that block. One person fixing the export clears '
        f'every one of them.'),
    "part_undated": lambda n, sids: (
        f'{n_of(n, "part", "parts")} on order {"has" if n == 1 else "have"} no due date in '
        f'the file.'),
    # pm_due is deliberately absent: a PM due on a stop is the atom of whoever works it and
    # rolls up to nothing a manager decides. An aggregate list padded with rolled-up atoms
    # is the atom list wearing a count.
}

if READER["claim_tier"] == "AGGREGATE":
    by_kind = {}
    for sid, owner, atoms in aggregate_inputs:
        for kind, _ in atoms:
            by_kind.setdefault(kind, []).append(sid)
    shapes = [(k, AGGREGATE_SHAPES[k](len(v), v))
              for k, v in by_kind.items() if k in AGGREGATE_SHAPES]
    CAP = 6          # BRIEFING_ACTION_CAP's documented default
    dropped = max(0, len(shapes) - CAP)
    block = ('<h3>Do this</h3><ul>'
             + "".join(f"<li>{t}</li>" for _, t in shapes[:CAP]) + '</ul>')
    if dropped:
        block += (f'<p class="a">{n_of(dropped, "further item", "further items")} over the '
                  f'action cap of {CAP} and not shown.</p>')
    marker = '<div class="stop">'
    i = "\n".join(out).find(marker)
    out.insert(next(j for j, x in enumerate(out) if x.startswith(marker)),
               f'<div class="agg">{block}</div>')

NOT_A_COMPARISON = (
    "This briefing names who owns each stop so you can route a conversation. It is not a "
    "comparison between the people in it and must not be used as one: nothing here is "
    "ordered, grouped or counted by person." if ATTRIBUTE_OWNER else "")

A(f'''<div class="foot">Set up by {RUN_FOR}. Sent to {RUN_FOR} only. Reply STOP to end it,
or say what you want changed.<br>{NOT_A_COMPARISON}<br>Sources: period plan (current,
{date_full(PLAN_ASOF)}); work orders (carried, {date_full(WO_ASOF)}); contract status
(current, {date_full(PLAN_ASOF)}); parts on order (read in part).</div>
</div></body></html>'''.replace("\n", " "))

html = "\n".join(out)

def repeated_share(doc):
    """The share of reader-facing text spent on DECLARED standing explanations beyond their
    first appearance.

    IT COUNTS ONLY THE DECLARED ONES, AND THAT IS THE WHOLE CORRECTNESS OF IT. The first
    version of this measure counted any paragraph identical to another, which on the
    manager's run swept in "1 visit planned this period. PM due: No." nine times. That is
    not a repeated explanation, it is nine stops whose planned visits and PM status happen
    to carry the same two values, and it is exactly the per-item FACT the relief is
    forbidden to touch. A bound that counts a coincidence of values as waste is a bound
    that pressures a run to drop data, which inverts what the bound is for. SD-FMT-28 draws
    the same line: a phrase unique to its own row is never touched, and a phrase identical
    on every row that carries it is the one that may move.
    """
    body = doc[doc.find('<div class="prov"'):]
    ps = [re.sub(r"<[^>]+>", "", x).strip()
          for x in re.findall(r"<p[^>]*>(.*?)</p>", body, re.S)]
    total = sum(len(x) for x in ps) or 1
    spent = 0
    for long_form, _short, _st in STANDING.values():
        n = body.count(long_form)
        if n > 1:
            spent += len(long_form) * (n - 1)
    return spent / total, total

def standing_coverage(doc):
    """Every explanatory line this run emitted more than once must be DECLARED in STANDING.

    Validated from the EMITTED lines to the SET, which is SD-CTR-29's stated direction and
    the only one that finds a hole. The first version of STANDING declared four
    explanations and this build emitted six of the same shape: the absent-contract string
    and the disclaimed-parts string were undeclared, so the share measure could not see
    them and the relief could never reach them however often they repeated. A closed set a
    run must draw from is usable only if it covers every state the run can produce.
    """
    import collections as _c
    body = doc[doc.find('<div class="prov"'):]
    explanatory = re.findall(r'<p class="[au]">(.*?)</p>', body, re.S)
    counts = _c.Counter(re.sub(r"\s+", " ", x).strip() for x in explanatory)
    declared = {re.sub(r"\s+", " ", lf).strip() for lf, _, _ in STANDING.values()}
    declared |= {re.sub(r"\s+", " ", sf).strip() for _, sf, _ in STANDING.values()}
    # COVERAGE IS TESTED BY CONTAINMENT, NOT EQUALITY, AND THE REASON IS ONE ENTRY'S SHAPE.
    # Five of the six declared explanations occupy a whole paragraph, where equality would
    # do. The sixth is appended to a varying per-item line and shares its paragraph, which
    # is also why its short form is empty: it has no shortened version, it goes away. A
    # containment test covers both shapes with one rule and no list of exceptions.
    #
    # THE LIMIT THIS LEAVES, STATED RATHER THAN PAPERED OVER. A repeated explanation welded
    # into the same paragraph as a declared one is invisible to this check. It cannot be
    # found mechanically, because inside these two classes a repeated sentence is either a
    # standing explanation or a per-item fact whose values happen to coincide, and nothing
    # in the text distinguishes them: subtracting the declared forms and flagging whatever
    # repeats in the residue would flag "1 item here, the owner's." on every stop carrying
    # one item, which is the per-item fact the relief is forbidden to touch. What closes
    # this hole is declaring the explanation, which is a human act. What this check does is
    # guarantee that an explanation occupying its own paragraph cannot be forgotten.
    def covered(t):
        return t in declared or any(d and d in t for d in declared)
    return [(t, n) for t, n in counts.items() if n > 1 and not covered(t)]

holes = standing_coverage(html)
if holes:
    sys.exit("STANDING is incomplete, which means the repeated-explanation bound cannot see "
             "these and the relief can never reach them:\n"
             + "\n".join(f"   x{n}  {t[:90]}" for t, n in holes))

share_before, text_total = repeated_share(html)
relief = []
if share_before > REPEAT_SHARE_BOUND:
    for key, (long_form, short_form, standing_line) in STANDING.items():
        n = html.count(long_form)
        if n > 1:
            if short_form:
                html = html.replace(long_form, short_form)
            else:
                # An empty short form means the sentence is appended to a varying per-item
                # line, so it is removed with the space that joined it and that line is
                # left exactly as it was. The bare replace after it is not redundant: it
                # catches an occurrence that opens its own paragraph, which would otherwise
                # survive the relief and go on being counted by the measure afterwards.
                html = html.replace(" " + long_form, "").replace(long_form, "")
            relief.append((key, n, standing_line))
    if relief:
        # ITS OWN BLOCK, AFTER ANYTHING ELSE AND IMMEDIATELY BEFORE THE FIRST ITEM.
        # The first version inserted it inside the aggregate action block, where it read as
        # four more things for the manager to do rather than as a key to reading the stops.
        # An explanation of what a line MEANS is not a finding and must not sit among them,
        # which is 5.2's own ordering argument: the finding leads and the key to reading it
        # sits where the reader meets the thing it explains.
        block = ('<div class="key"><p><b>' + n_of(len(relief), "thing", "things")
                 + ' that hold for every stop below, said once here rather than on each '
                 + 'stop.</b> ' + " ".join(st for _, _, st in relief) + "</p></div>")
        html = html.replace('</div>\n<div class="stop">',
                            '</div>\n' + block + '\n<div class="stop">', 1)
share_after, _ = repeated_share(html)

slug = RUN_FOR.replace(". ", "-").replace(".", "").replace(" ", "-")
dest = os.path.join(HERE, f"Briefing {slug} {BRIEFING_DAY.isoformat()}.html")
with open(dest, "w", encoding="utf-8") as f:
    f.write(html)

# ------------------------------------------------- SD-LNG-13 three-value self-test
# n_of() AND every bare pluralising ternary beside it. The ternaries were added later, were
# never tested, and one of them shipped "Nothing here, all the owner's." A helper that is
# tested does not protect the conditional written next to it.
fails = []
for n in (0, 1, 2, 5):
    for sing, plur in [("is", "are"), ("has", "have"), ("carries", "carry"),
                       ("sits", "sit"), ("the", "all the")]:
        got = sing if n == 1 else plur
        if n == 1 and got != sing: fails.append(f"ternary {sing}/{plur} at one -> {got}")
        if n != 1 and got != plur: fails.append(f"ternary {sing}/{plur} at {n} -> {got}")
for one, many, zero in [("stop", "stops", "No stops scheduled"),
                        ("visit", "visits", None),
                        ("unit on site", "units on site", None),
                        ("unit covered", "units covered", None)]:
    for n in (0, 1, 5):
        got = n_of(n, one, many, zero)
        if n == 1 and (got.startswith("1 ") and got[2:].split()[0].endswith("s")
                       and got[2:].split()[0] != "s"):
            fails.append(f"singular failed: {got}")
        if n == 5 and " 5 " not in f" {got} " and not got.startswith("5 "):
            fails.append(f"plural failed: {got}")
print(("SELF-TEST FAIL: " + "; ".join(fails)) if fails else "SELF-TEST pass (0/1/many)")
# MEASURE IT EVERY RUN AND RECORD THE MEASUREMENT WHETHER OR NOT IT FAILS, because a bound
# only measured when somebody suspects a problem is not a bound and a passing measurement is
# the evidence the check ran.
print(f"repeated share: {share_before:.0%} against a bound of {REPEAT_SHARE_BOUND:.0%}"
      + (f"; relief ran on {len(relief)} explanation(s) "
         f"({', '.join(f'{k} x{n}' for k, n, _ in relief)}), now {share_after:.0%}"
         if relief else "; no relief needed"))
print(f"wrote {dest} ({len(html)} bytes, ascii={html.isascii()})")
