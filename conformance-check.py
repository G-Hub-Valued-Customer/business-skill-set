#!/usr/bin/env python3
"""
Checks that the bundle's own declarations agree with each other.

    python3 conformance-check.py

Exits non-zero on any failure, so it can gate a commit.

This exists because of a specific defect. The bundle was extended from three workflows to
four, and the extension touches the doctrine's Skills line, its `Applies` field definition,
every cited rule's own Applies line, the router's frontmatter and table, the schema index,
the HARD_GATES group set, and the prose of six other files. Adding the fourth workflow by
hand produced two inconsistencies within one sitting: one doctrine rule was cited AFTER the
Applies sweep had already run, and one shipped workflow still stated a group count that had
just changed. Neither was visible to any reader and both were mechanical to find.

The rule it enforces is the bundle's own: **no definition states how many skills or how
many groups there are.** A rule's reach is declared by its own Applies line, a gate's group
by its own record, and a count written anywhere else is a second place to update that
nothing checks.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

fails = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {name}")
    if not ok:
        fails.append(name)
        if detail:
            for line in str(detail).rstrip().split("\n"):
                print(f"        {line}")

def read(p):
    return open(p, encoding="utf-8", errors="replace").read()

# ---------------------------------------------------------------- the skill set
doc = read("skill/reference/doctrine/README.md")
m = re.search(r"^Skills: (.+?)\n\n", doc, re.M | re.S)
SKILLS = re.findall(r"\b([A-Z]{5,})\b", m.group(1)) if m else []
print(f"Skills declared in the doctrine: {', '.join(SKILLS)}\n")
check("the doctrine declares at least one skill", bool(SKILLS))

# ------------------------------------------- no DEFINITION hardcodes the skill or group set
# The rule is about definitions, not prose. "Four workflows" in a description is useful to a
# reader. What must never carry a count is a statement that DEFINES a rule's reach or a
# taxonomy's membership, because that is the statement a new skill falsifies silently. An
# earlier version of this check swept every file for a number next to the word "skills" and
# flagged thirteen lines, eleven of which were correct English: "two skills producing two
# different answers off the same configuration" is a quantity of instances, not a count of
# the set. A check that cries wolf gets switched off, so this one names its sites.
DEFINITION_SITES = [
    ("skill/reference/doctrine/README.md",
     "which of the bundle's skills the rule binds",
     [r"which of the \w+ skills the rule binds"]),
    ("skill/reference/schema/run-control-and-reliability.md",
     None,
     [r"\b(?:TWO|THREE|FOUR|FIVE|SIX) KEYED GROUPS\b", r"`group`, one of the \w+;"]),
]
bad = []
for path, required, forbidden in DEFINITION_SITES:
    if not os.path.exists(path):
        bad.append(f"{path}: file missing"); continue
    t = read(path)
    if required and required not in t:
        bad.append(f"{path}: missing the countless form {required!r}")
    for pat in forbidden:
        for mm in re.finditer(pat, t):
            bad.append(f"{path}: definition carries a count: {mm.group(0)!r}")
check("no definition hardcodes the skill or group set", not bad, "\n".join(bad))

# A scope claim of the form "all N skills" or "the N-skill bundle" is a definition wherever
# it appears in the reference tree, because a run reads the reference tree as normative.
# A SCOPE claim says what a rule or a file GOVERNS. A historical fact says what happened:
# "the two skills stated the same rule independently" is evidence of doctrine, not a count
# of the set, and an earlier version of this check flagged three such lines and nothing else.
# So the pattern requires a verb of governance next to the count.
SCOPE_CLAIM = re.compile(
    r"\b(?:govern|governs|binds|bind|applies to|apply to|shared by|read by|inherited by|"
    r"across)\s+(?:all\s+|the\s+)?(?:two|three|four|five|six)\s+skills\b"
    r"|\b(?:two|three|four|five|six)-skill bundle\b", re.I)
hits = []
for f in sorted(glob.glob("skill/reference/**/*.md", recursive=True)):
    for i, line in enumerate(read(f).split("\n"), 1):
        if SCOPE_CLAIM.search(line):
            hits.append(f"{f}:{i}: {line.strip()[:100]}")
check("no reference file states a scope claim over a counted skill set", not hits,
      "\n".join(hits))

# Every token in every Applies line is a declared skill. This is what catches a typo, and a
# skill named in a rule that the doctrine never declared.
unknown = {}
for f in sorted(glob.glob("skill/reference/doctrine/*.md")):
    if f.endswith("README.md"):
        continue
    for rule in re.finditer(r"^### (SD-[A-Z]{3}-\d+) .*?(?=^### SD-|\Z)", read(f), re.M | re.S):
        ap = re.search(r"^- Applies: (.+)$", rule.group(0), re.M)
        if not ap:
            unknown.setdefault("no Applies line", []).append(rule.group(1)); continue
        for tok in (t.strip() for t in ap.group(1).split(",")):
            if tok and tok not in SKILLS:
                unknown.setdefault(tok, []).append(rule.group(1))
check("every token in every Applies line is a declared skill", not unknown,
      "\n".join(f"{k}: {', '.join(v[:6])}{' and more' if len(v) > 6 else ''}"
                for k, v in sorted(unknown.items())))

# ------------------------------------------------- the router routes every declared skill
router = read("skill/SKILL.md")
wf_files = sorted(glob.glob("skill/workflows/*.md"))
routed = set(re.findall(r"`(workflows/[a-z-]+\.md)`", router))
missing = [os.path.relpath(w, "skill") for w in wf_files
           if os.path.relpath(w, "skill").replace(os.sep, "/") not in routed]
check("every workflow file is routed from SKILL.md", not missing, str(missing))
check("every routed workflow file exists",
      all(os.path.exists(os.path.join("skill", r)) for r in routed),
      str([r for r in routed if not os.path.exists(os.path.join("skill", r))]))

# ------------------------------- the schema index resolves every variable every file cites
sch = read("skill/reference/schema/README.md")
INDEX_ROW = re.compile(r"^\| `([A-Z][A-Z_0-9]*)` \| `(reference/schema/[a-z0-9-]+\.md)` \|")
indexed, index_files = {}, set()
for line in sch.split("\n"):
    mm = INDEX_ROW.match(line)
    if mm:
        indexed[mm.group(1)] = mm.group(2)
        index_files.add(mm.group(2))
names = list(indexed)
check("the variable index is sorted", names == sorted(names))
check("the variable index has no duplicate names", len(names) == len(set(names)))
check("every file the variable index names exists",
      all(os.path.exists(os.path.join("skill", f)) for f in index_files),
      str(sorted(f for f in index_files if not os.path.exists(os.path.join("skill", f)))))
groups = re.findall(r"^\| (\d+) \| `(reference/schema/[a-z0-9-]+\.md)` \|", sch, re.M)
check("the group table numbers run 1..N with no gap",
      [int(g) for g, _ in groups] == list(range(1, len(groups) + 1)),
      str([g for g, _ in groups]))
# BUG 4, FOUND BY LOOKING FOR A CHECK THAT COULD NOT FAIL. This check used to read
#     {f for _, f in groups} <= index_files | {f for _, f in groups}
# and the right-hand side contains the left-hand side, so it was true for every possible
# input, including a group table and a variable index that named disjoint sets of files.
# It is the exact shape of the defect the three-state verification record exists to catch:
# an assertion that cannot fire and an assertion nobody wrote look identical in a two-state
# pass/fail record. The replacement is a bijection in both directions, which is what the
# sentence above it always claimed.
gfiles = {f for _, f in groups}
check("the group table and the variable index name the same files",
      gfiles == index_files,
      f"in the group table only={sorted(gfiles - index_files)}; "
      f"in the variable index only={sorted(index_files - gfiles)}")

# ---------------------------------------- NO FILE UNDER skill/reference/ IS UNREACHABLE
# The bundle's reading model is that nothing is subsetted: a rule is never missing, only
# unread, and it is unread only when nothing cited it. **A file nothing names can never be
# read at all**, which turns "present but unread" into "present and unreachable", and the
# difference is invisible from inside the tree.
#
# MANIFEST.md IS DELIBERATELY NOT COUNTED AS NAMING A FILE. It is an inventory of what was
# shipped, written for an agent that has just unpacked the bundle, and it is not on any
# resolution path a run takes. A file whose only mention is its inventory row is exactly
# the case this check exists to find, and letting the inventory satisfy the check would
# make the check unable to fail on the one input that matters.
#
# This found two: schema/intentional-non-variables.md, which exists to stop a sweep
# reporting fixed vocabulary as variables defined nowhere and so had a live consequence,
# and schema/defaults-and-notices.md, which is provenance. The fix for the first was to
# name it in the resolution rule at the moment a run needs it; the fix for the second was
# to say in the index that it is read by nobody, because a file declared unread is
# accounted for and a file nobody mentions is not.
ref_files = sorted(glob.glob("skill/reference/**/*.md", recursive=True))
corpus = {f: read(f) for f in sorted(glob.glob("skill/**/*.md", recursive=True))}
unreachable = []
for f in ref_files:
    base = os.path.basename(f)
    rel = os.path.relpath(f, "skill")
    named = any(base in body or rel in body for other, body in corpus.items() if other != f)
    if not named and base != "README.md" and f.startswith("skill/reference/doctrine/"):
        grp = base[:-3]
        named = any(re.search(rf"SD-{grp}-\d+", body)
                    for other, body in corpus.items() if other != f)
    if not named:
        unreachable.append(rel)
check("no file under skill/reference/ is named by nothing", not unreachable,
      "\n".join(unreachable))

# -------------- THE VARIABLE INDEX IS VALIDATED FROM THE GROUP FILES, NOT THE REVERSE
# SD-CTR-29's direction, and it is the only direction that finds anything. Walking the index
# and checking each named file exists is the check above, and it passes on an index that is
# missing half the variables in the tree. Walking the GROUP FILES and checking each variable
# they define is indexed, against the file that defines it, is what catches a variable a run
# cannot resolve: an unindexed variable is unresolvable, and the run has no way to tell that
# from a variable that does not exist.
#
# This found three. Two were variables added to a group file whose index rows had not been
# written, which is a name the workflow citing them could never resolve. The third was the
# opposite and more interesting: the index carried entries for `NAME` and `PERSON`, which
# are not variables at all. `NAME` is the header cell of every group file's variable table
# and `PERSON` is a row label in a counts table, both picked up by whatever sweep built the
# index. An index row for a non-variable sends a run to a file that cannot define it, and
# reference/schema/intentional-non-variables.md exists to say that an upper-case name which
# is not a variable must never be reported as one.
#
# The row shape is what keeps this check free of the same false positives: a definition row
# carries exactly seven cells, and the header line and the counts-table row that fooled the
# original sweep carry seven and six respectively, so the header is excluded by name and
# the counts row by its width.
VAR_HEADER = "| NAME | DEFINITION | TIER | STATE | TYPE | VALIDATION | EXAMPLE |"
defined = {}
for p in sorted(glob.glob("skill/reference/schema/*.md")):
    base = os.path.basename(p)
    if base == "README.md":
        continue
    body = read(p)
    i = body.find(VAR_HEADER)
    if i < 0:
        continue
    block = body[i + len(VAR_HEADER):]
    cut = block.find("\n\n")
    for line in (block[:cut] if cut > 0 else block).split("\n"):
        if line.startswith("|---"):
            continue
        cells = line.split("|")
        if len(cells) != 9:          # leading and trailing empties plus seven cells
            continue
        nm = cells[1].strip()
        if re.fullmatch(r"[A-Z][A-Z_0-9]*", nm):
            defined[nm] = "reference/schema/" + base

unindexed = sorted(n for n in defined if n not in indexed)
misfiled = sorted(f"{n}: indexed to {indexed[n]}, defined in {defined[n]}"
                  for n in defined if n in indexed and indexed[n] != defined[n])
notdefined = sorted(n for n in indexed if n not in defined)
check("every variable a group file defines is in the variable index", not unindexed,
      str(unindexed))
check("every variable is indexed against the file that defines it", not misfiled,
      "\n".join(misfiled))
check("every entry in the variable index is defined in the file it names", not notdefined,
      str(notdefined))

# ------------------- every doctrine ID a workflow cites exists and names that workflow
def applies_of(rid):
    g = rid.split("-")[1]
    p = f"skill/reference/doctrine/{g}.md"
    if not os.path.exists(p):
        return None, "group file missing"
    rule = re.search(rf"^### {rid} .*?(?=^### SD-|\Z)", read(p), re.M | re.S)
    if not rule:
        return None, "rule missing"
    ap = re.search(r"^- Applies: (.+)$", rule.group(0), re.M)
    if not ap:
        return None, "no Applies line"
    return [t.strip() for t in ap.group(1).split(",")], None

# A CITATION OF A RULE'S RATIONALE RATHER THAN OF ITS MECHANISM. This check reads an ID in
# a file as reliance on the rule, and sometimes a file is appealing to a rule's REASONING
# while the rule's own mechanism plainly does not reach it. That distinction is real and
# this check cannot see it, so each instance is carried here with the reason written out.
# An entry with no reason is a failure, per the same rule the bundle applies to a
# not-applicable formatting element: an unexplained exemption is not an exemption.
#
# These are SETTLED, not open. A rule actually in force in a workflow names that workflow
# on its Applies line, and the fix for those is the Applies line, which is why this table
# holds one entry rather than the two it started with.
RATIONALE_ONLY = {
    ("period-planning.md", "SD-CTR-23"):
        "period-planning cites this REVIEW rule for its REASONING, that deleting somebody's "
        "own record of their work is the most expensive kind of loss, and not for its "
        "mechanism, which is about where content sits relative to a COPY BLOCK. A "
        "spreadsheet has no copy block, so the rule does not reach PLANNING and its Applies "
        "line is correct as it stands. What the planning file is doing is borrowing the "
        "argument, which is legitimate and is not reliance.",
}
UNCLASSIFIED = RATIONALE_ONLY

WF_SKILL = {  # which declared skill each workflow file is
    "period-planning.md": "PLANNING",
    "objectives-and-review.md": "REVIEW",
    "standard-gap-scorecard.md": "SCORECARD",
    "recurring-briefing.md": "BRIEFING",
}
for wf in wf_files:
    base = os.path.basename(wf)
    skill = WF_SKILL.get(base)
    if not skill:
        check(f"{base} maps to a declared skill", False,
              "add it to WF_SKILL in this script")
        continue
    # A workflow MAY name a rule its own Applies line excludes, and both shipped workflows
    # do: one keeps a doctrine coverage index listing the rules that do not apply to it,
    # the other marks each one NOT ADOPTED with the reason. That is a declaration and not a
    # defect. What IS a defect is relying on such a rule silently. An earlier version of
    # this check reported all twenty-three and twenty-one of them were declared, which is
    # the cry-wolf failure this file's own docstring warns about.
    # Whitespace between the words is flexible, because the marker is wrapped prose and a
    # line break plus an indent is three characters where a naive pattern wants one. That
    # was the second bug in this check: "named as NOT\n  ADOPTED" flattens to three spaces.
    NOT_ADOPTED = re.compile(
        r"NOT\s+ADOPTED|do\s+not\s+apply\s+to|does\s+not\s+apply\s+to|"
        r"REVIEW-only|PLANNING-only|SCORECARD-only|BRIEFING-only|"
        r"carried\s+into\s+(?:PLANNING|REVIEW|SCORECARD|BRIEFING)", re.I)
    text = read(wf)
    # Newlines become spaces so a marker split across a line break still matches. The
    # substitution is one character for one, so every offset below is still the real one.
    # Three of the nine findings on the first real run were this bug: the shipped file says
    # "are named as NOT\nADOPTED on their own APPLIES lines" and the marker did not match.
    flat = text.replace("\n", " ")
    declared_blocks = [m.start() for m in NOT_ADOPTED.finditer(flat)]
    bad, rationale = [], []
    for rid in sorted(set(re.findall(r"SD-[A-Z]{3}-\d+", text))):
        ap, err = applies_of(rid)
        if err:
            bad.append(f"{rid}: {err}"); continue
        if skill in ap:
            continue
        # every occurrence must sit near a not-adopted marker for the exclusion to count
        occ = [m.start() for m in re.finditer(re.escape(rid), flat)]
        undeclared = [o for o in occ
                      if not any(abs(o - d) < 2000 for d in declared_blocks)]
        if undeclared:
            lineno = text[:undeclared[0]].count("\n") + 1
            if (base, rid) in UNCLASSIFIED:
                rationale.append(f"{rid} at line {lineno}: {UNCLASSIFIED[(base, rid)]}")
            else:
                bad.append(f"{rid}: Applies is {', '.join(ap)}, relied on at line {lineno} "
                           f"with no NOT ADOPTED marker")
    check(f"every doctrine ID {base} relies on names {skill}", not bad, "\n".join(bad))
    for u in rationale:
        print(f"NOTE  {base}: cites a rule's rationale, not its mechanism. {u}")

# ----------------------------------------- every gate record carries all six fields
GATE = re.compile(r"^\| `([a-z_]+)` \| ([^|]+) \| `([a-z_]+)` \| ([^|]+) \| ([^|]+) \|$", re.M)
for wf in wf_files:
    base = os.path.basename(wf)
    skill = WF_SKILL.get(base)
    rows = GATE.findall(read(wf))
    if not rows:
        continue
    bad = []
    for key, fires, beh, reads, doctrine in rows:
        if beh not in ("stop_outright", "ask_one_question_then_stop"):
            bad.append(f"{key}: behaviour is {beh!r}")
        if not fires.strip():
            bad.append(f"{key}: no fires_at")
        if not reads.strip():
            bad.append(f"{key}: no reads")
        ids = re.findall(r"SD-[A-Z]{3}-\d+", doctrine)
        if not ids:
            bad.append(f"{key}: no doctrine ID")
        for rid in ids:
            ap, err = applies_of(rid)
            if err:
                bad.append(f"{key}: {rid} {err}")
            elif skill and skill not in ap:
                bad.append(f"{key}: {rid} does not name {skill}")
    check(f"every gate record in {base} carries all six fields", not bad, "\n".join(bad))

# ---------------------------------------------------------------- character set
nonascii = [f for f in sorted(glob.glob("**/*.md", recursive=True)) if not read(f).isascii()]
check("every markdown file is ascii", not nonascii, "\n".join(nonascii))

print(f"\n{len(fails)} failure(s)" if fails else "\nALL CHECKS PASS")
sys.exit(1 if fails else 0)
