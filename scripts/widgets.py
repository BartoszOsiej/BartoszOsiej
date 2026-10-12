#!/usr/bin/env python3
"""Custom animated profile widgets.

Everything here is rendered by tooling that "does not exist" as a GitHub
feature. GitHub strips scripts from READMEs, but an SVG served from *your own*
repo and embedded via <img> still animates (SMIL + CSS keyframes). No badge
service, no renderer, no JS - the whole widget set below is self-hosted and
refreshed by the stats pipeline on a schedule.

Outputs (dark + light):
    terminal-*.svg     animated terminal replaying the real products
    dashboard-*.svg    live ecosystem board (downloads, views, stars, CI)
    achievements-*.svg custom trophy case (GitHub has none that is embeddable)
    pipeline-*.svg     animated supply-chain flow (tag -> registries)
"""

import html
import json
import os
import urllib.request
from datetime import datetime, timezone

OUT = os.environ.get("STATS_OUT", os.path.join(os.getcwd(), "out"))
TOK = os.environ.get("GH_TOKEN", "")
USER = "BartoszOsiej"

MONO = "'JetBrains Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"

P = {
    "dark": dict(bg="#0d1117", panel="#161b22", border="#30363d", fg="#e6edf3",
                 sub="#8b949e", purple="#a371f7", cyan="#39c5cf", pink="#f778ba",
                 green="#3fb950", amber="#d29922", blue="#58a6ff", red="#f85149"),
    "light": dict(bg="#ffffff", panel="#f6f8fa", border="#d0d7de", fg="#1f2328",
                  sub="#656d76", purple="#8250df", cyan="#0969da", pink="#bf3989",
                  green="#1a7f37", amber="#9a6700", blue="#0969da", red="#cf222e"),
}

CI_REPOS = ["talus-process-monitor", "externum", "NV2_ENGINE", "pqbit",
            "pqguard", "CyberForge", "Docs"]


def esc(s):
    return html.escape(str(s), quote=True)


def fetch(url, auth=True):
    h = {"User-Agent": "widgets/1.0", "Accept": "application/vnd.github+json"}
    if auth and TOK:
        h["Authorization"] = f"Bearer {TOK}"
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fmt(n):
    n = float(n or 0)
    if n >= 1e6:
        return f"{n/1e6:.2f}M"
    if n >= 1e3:
        return f"{n/1e3:.1f}k"
    return str(int(n))


def live_data():
    meta = {}
    try:
        with open(os.path.join(OUT, "meta.json")) as f:
            meta = json.load(f)
    except Exception:
        pass
    d = {
        "stamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "totals": meta.get("totals", {"npm": 0, "pypi": 0, "crates": 0, "gh": 0}),
        "views": meta.get("profile_views", {"total": 0, "uniques": 0}),
        "stars": 0, "followers": 0, "repos": 0, "ci": [],
    }
    try:
        u = fetch(f"https://api.github.com/users/{USER}")
        d["followers"] = u.get("followers", 0)
        d["repos"] = u.get("public_repos", 0)
    except Exception:
        pass
    try:
        repos = fetch(f"https://api.github.com/users/{USER}/repos?per_page=100")
        d["stars"] = sum(r.get("stargazers_count", 0) for r in repos)
    except Exception:
        pass
    # persist a daily star history - self-tracked, same pattern as views
    hp = os.path.join(OUT, "stars.json")
    series = []
    if os.path.exists(hp):
        try:
            with open(hp) as f:
                series = json.load(f).get("series", [])
        except Exception:
            series = []
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    series = [x for x in series if x.get("d") != today][-89:]
    if d["stars"] or not series:
        series.append({"d": today, "v": d["stars"]})
    series.sort(key=lambda x: x["d"])
    with open(hp, "w") as f:
        json.dump({"series": series}, f, indent=1)
    d["star_hist"] = [x["v"] for x in series]
    try:
        issues = fetch(f"https://api.github.com/repos/{GB_REPO}/issues"
                       f"?labels=guestbook&state=all&per_page=50")
        gb = []
        for i in issues:
            if "pull_request" in i:
                continue
            gb.append({"user": i["user"]["login"], "title": i.get("title", ""),
                       "body": (i.get("body") or "").strip().replace("\r", ""),
                       "created": i["created_at"][:10],
                       "reactions": (i.get("reactions") or {}).get("total_count", 0)})
        d["guestbook"] = gb
    except Exception:
        d["guestbook"] = []
    for repo in CI_REPOS:
        try:
            runs = fetch(f"https://api.github.com/repos/{USER}/{repo}/actions/runs?per_page=1")
            rs = runs.get("workflow_runs", [])
            concl = rs[0].get("conclusion") if rs else None
            d["ci"].append((repo, concl or "none"))
        except Exception:
            d["ci"].append((repo, "none"))
    return d


# --------------------------------------------------------------------------- #
#  terminal
# --------------------------------------------------------------------------- #

T_LINES = [
    ("cmd", "pip install externum && externum build hello.ext"),
    ("out", "lex > parse > typecheck > codegen  |  3 targets: python / bash / binary"),
    ("ok",  "hello, world  compiled in 41 ms      307/307 test suite green"),
    ("cmd", "talus --web :8080"),
    ("out", "eBPF probes: execve / openat / connect      ~280k events/s"),
    ("warn", "cryptor matched ransomware heuristic -> SIGKILL + fs snapshot"),
    ("cmd", "pqguard seal ./docs --recipient me"),
    ("ok",  "ML-KEM-768 + AES-256-GCM sealed 42 files     FIPS 203 verified"),
    ("cmd", "./verify.sh v0.4.5"),
    ("ok",  "SLSA-L3 provenance OK   cosign signature OK   SPDX SBOM OK"),
]


def terminal(dark):
    c = P["dark" if dark else "light"]
    W, H = 764, 392
    top, lh, slot = 60, 26, 1.0
    n = len(T_LINES)
    cycle = n * slot + 2.4
    hide = n * slot + 0.6
    defs, body = [], []
    body.append(f'<rect width="{W}" height="{H}" rx="14" fill="{c["panel"]}" '
                f'stroke="{c["border"]}" stroke-width="1"/>')
    # title bar
    defs.append(
        '<linearGradient id="tbar" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{c["purple"]}" stop-opacity="0.30"/>'
        f'<stop offset="0.5" stop-color="{c["cyan"]}" stop-opacity="0.18"/>'
        f'<stop offset="1" stop-color="{c["pink"]}" stop-opacity="0.30"/></linearGradient>')
    body.append(f'<path d="M14,0 H{W-14} A14,14 0 0 1 {W},14 V40 H0 V14 A14,14 0 0 1 14,0 Z" '
                f'fill="url(#tbar)"/>')
    for i, col in enumerate([c["red"], c["amber"], c["green"]]):
        body.append(f'<circle cx="{28+i*22}" cy="20" r="6" fill="{col}"/>')
    body.append(f'<text x="{W/2}" y="25" text-anchor="middle" font-family="{SANS}" '
                f'font-size="12" fill="{c["sub"]}">bartosz@hartwell-labs: ~/lab - zsh</text>')

    colon = {"cmd": c["green"], "out": c["sub"], "ok": c["green"], "warn": c["amber"]}
    for i, (kind, txt) in enumerate(T_LINES):
        y = top + 30 + i * lh
        cid = f"cl{i}"
        t0 = 0.15 + i * slot
        kt = [0.0, t0/cycle, (t0+0.34)/cycle, (n*slot)/cycle, hide/cycle, 1.0]
        defs.append(f'<clipPath id="{cid}"><rect x="28" y="{y-16}" width="0" height="20">'
                    f'<animate attributeName="width" '
                    f'values="0;0;{W-56};{W-56};0;0" '
                    f'keyTimes="{";".join(f"{k:.4f}" for k in kt)}" '
                    f'dur="{cycle}s" repeatCount="indefinite"/></rect></clipPath>')
        if kind == "cmd":
            body.append(f'<text x="28" y="{y}" clip-path="url(#{cid})" font-family="{MONO}" '
                        f'font-size="14" fill="{c["green"]}">$ <tspan fill="{c["fg"]}">{esc(txt)}</tspan></text>')
        else:
            pre = {"out": "  ", "ok": "  ", "warn": "  "}[kind]
            body.append(f'<text x="28" y="{y}" clip-path="url(#{cid})" font-family="{MONO}" '
                        f'font-size="14" fill="{colon[kind]}">{pre}{esc(txt)}</text>')
    # blinking cursor at the end
    body.append(f'<rect x="28" y="{top+30+n*lh-14}" width="9" height="17" fill="{c["fg"]}">'
                f'<animate attributeName="opacity" values="1;1;0;0;1" dur="1.1s" '
                f'repeatCount="indefinite"/></rect>')
    return svg(W, H, defs, body)


# --------------------------------------------------------------------------- #
#  dashboard
# --------------------------------------------------------------------------- #

def dashboard(dark, d):
    c = P["dark" if dark else "light"]
    W, H = 880, 340
    defs, b = [], []
    defs.append(
        '<linearGradient id="sweep" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{c["purple"]}"/>'
        f'<stop offset="0.5" stop-color="{c["cyan"]}"/>'
        f'<stop offset="1" stop-color="{c["pink"]}"/></linearGradient>')
    defs.append('<clipPath id="clip"><rect width="%d" height="%d" rx="14"/></clipPath>' % (W, H))
    b.append(f'<rect width="{W}" height="{H}" rx="14" fill="{c["bg"]}" stroke="{c["border"]}"/>')
    b.append(f'<rect width="{W}" height="{H}" rx="14" fill="url(#sweep)" opacity="0.05"/>')
    b.append(f'<rect x="0" y="0" width="120" height="3" fill="url(#sweep)">'
             f'<animate attributeName="x" values="-120;{W}" dur="3.4s" repeatCount="indefinite"/></rect>')
    b.append(f'<text x="22" y="34" font-family="{SANS}" font-size="13" font-weight="700" '
             f'letter-spacing="2" fill="{c["fg"]}">LIVE ECOSYSTEM</text>')
    b.append(f'<circle cx="200" cy="29" r="4" fill="{c["green"]}">'
             f'<animate attributeName="opacity" values="1;0.25;1" dur="1.6s" repeatCount="indefinite"/></circle>')
    b.append(f'<text x="212" y="33" font-family="{MONO}" font-size="10" fill="{c["sub"]}">'
             f'SELF-HOSTED PIPELINE - NO BADGE SERVICES</text>')
    b.append(f'<text x="{W-22}" y="33" text-anchor="end" font-family="{MONO}" font-size="10" '
             f'fill="{c["sub"]}">{esc(d["stamp"])}</text>')

    tiles = [
        ("npm", d["totals"]["npm"], c["red"]),
        ("PyPI", d["totals"]["pypi"], c["cyan"]),
        ("crates.io", d["totals"]["crates"], c["amber"]),
        ("GH releases", d["totals"]["gh"], c["purple"]),
    ]
    tw, gap, x0, ty = 198, 14, 22, 58
    for i, (label, val, col) in enumerate(tiles):
        x = x0 + i * (tw + gap)
        defs.append(f'<linearGradient id="t{i}" x1="0" y1="0" x2="0" y2="1">'
                    f'<stop offset="0" stop-color="{col}" stop-opacity="0.28"/>'
                    f'<stop offset="1" stop-color="{col}" stop-opacity="0.04"/></linearGradient>')
        b.append(f'<rect x="{x}" y="{ty}" width="{tw}" height="76" rx="10" fill="url(#t{i})" '
                 f'stroke="{col}" stroke-opacity="0.35"/>')
        b.append(f'<text x="{x+14}" y="{ty+24}" font-family="{MONO}" font-size="11" '
                 f'fill="{c["sub"]}">{esc(label)}</text>')
        b.append(f'<text x="{x+14}" y="{ty+56}" font-family="{MONO}" font-size="26" '
                 f'font-weight="700" fill="{c["fg"]}">{fmt(val)}'
                 f'<animate attributeName="opacity" values="0;1" dur="0.8s" begin="{i*0.15}s" fill="freeze"/></text>')
        b.append(f'<text x="{x+tw-14}" y="{ty+24}" text-anchor="end" font-family="{MONO}" '
                 f'font-size="10" fill="{c["sub"]}">last 30d</text>')

    rows = [
        ("Ecosystem views", f'{d["views"].get("total",0):,}', c["blue"]),
        ("Unique visitors", f'{d["views"].get("uniques",0):,}', c["cyan"]),
        ("Stars across repos", f'{d["stars"]:,}', c["amber"]),
        ("Public repositories", f'{d["repos"]:,}', c["purple"]),
        ("Followers", f'{d["followers"]:,}', c["pink"]),
    ]
    y0 = 168
    colw = (W - 44) / 2
    for i, (label, val, col) in enumerate(rows):
        cx = 22 + (i % 2) * (colw + 0)
        cy = y0 + (i // 2) * 34
        b.append(f'<circle cx="{cx+7}" cy="{cy}" r="4" fill="{col}"/>')
        b.append(f'<text x="{cx+22}" y="{cy+5}" font-family="{SANS}" font-size="13" '
                 f'fill="{c["sub"]}">{esc(label)}</text>')
        b.append(f'<text x="{cx+colw-24}" y="{cy+5}" text-anchor="end" font-family="{MONO}" '
                 f'font-size="15" font-weight="700" fill="{c["fg"]}">{esc(val)}</text>')

    # CI strip
    b.append(f'<line x1="22" y1="{y0+92}" x2="{W-22}" y2="{y0+92}" stroke="{c["border"]}"/>')
    b.append(f'<text x="22" y="{y0+114}" font-family="{MONO}" font-size="10" '
             f'fill="{c["sub"]}">CI STATUS</text>')
    cx = 130
    for i, (repo, concl) in enumerate(d["ci"]):
        ok = concl == "success"
        col = c["green"] if ok else (c["red"] if concl in ("failure", "cancelled") else c["sub"])
        b.append(f'<circle cx="{cx}" cy="{y0+110}" r="4" fill="{col}">'
                 f'<animate attributeName="opacity" values="1;0.3;1" dur="2s" '
                 f'begin="{i*0.2}s" repeatCount="indefinite"/></circle>')
        b.append(f'<text x="{cx+9}" y="{y0+114}" font-family="{MONO}" font-size="11" '
                 f'fill="{c["fg"]}">{esc(repo)}</text>')
        cx += 18 + len(repo) * 7
        if cx > W - 90:
            break
    return svg(W, H, defs, b)


# --------------------------------------------------------------------------- #
#  achievements (a trophy case GitHub does not offer)
# --------------------------------------------------------------------------- #

MEDALS = [
    ("Compiler author", "language from scratch", "FL", "#a371f7", "#f778ba"),
    ("Kernel whisperer", "eBPF probes in prod", "BP", "#39c5cf", "#58a6ff"),
    ("Post-quantum", "ML-KEM / ML-DSA / SLH", "PQ", "#3fb950", "#39c5cf"),
    ("Polyglot deployer", "npm + PyPI + crates", "PX", "#d29922", "#f778ba"),
    ("Supply chain", "cosign + SLSA + SBOM", "SC", "#58a6ff", "#a371f7"),
    ("Open source", "MIT, every active repo", "OS", "#f778ba", "#d29922"),
]


def achievements(dark):
    c = P["dark" if dark else "light"]
    W, H = 880, 168
    defs, b = [], []
    b.append(f'<rect width="{W}" height="{H}" rx="14" fill="{c["bg"]}" stroke="{c["border"]}"/>')
    b.append(f'<text x="22" y="32" font-family="{SANS}" font-size="13" font-weight="700" '
             f'letter-spacing="2" fill="{c["fg"]}">TROPHY CASE</text>')
    b.append(f'<text x="{W-22}" y="32" text-anchor="end" font-family="{MONO}" font-size="10" '
             f'fill="{c["sub"]}">hand-forged, not server-issued</text>')
    n = len(MEDALS)
    gap = 12
    mw = (W - 44 - gap * (n - 1)) / n
    for i, (title, sub, glyph, a, bcol) in enumerate(MEDALS):
        x = 22 + i * (mw + gap)
        defs.append(f'<linearGradient id="m{i}" x1="0" y1="0" x2="1" y2="1">'
                    f'<stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{bcol}"/></linearGradient>')
        b.append(f'<rect x="{x}" y="50" width="{mw}" height="100" rx="10" fill="{c["panel"]}" '
                 f'stroke="{c["border"]}"/>')
        b.append(f'<circle cx="{x+mw/2}" cy="82" r="18" fill="url(#m{i})">'
                 f'<animate attributeName="r" values="18;19.5;18" dur="2.6s" begin="{i*0.2}s" '
                 f'repeatCount="indefinite"/></circle>')
        b.append(f'<text x="{x+mw/2}" y="87" text-anchor="middle" font-family="{MONO}" '
                 f'font-size="13" font-weight="700" fill="#0d1117">{esc(glyph)}</text>')
        b.append(f'<text x="{x+mw/2}" y="118" text-anchor="middle" font-family="{SANS}" '
                 f'font-size="10.5" font-weight="700" fill="{c["fg"]}">{esc(title)}</text>')
        b.append(f'<text x="{x+mw/2}" y="134" text-anchor="middle" font-family="{MONO}" '
                 f'font-size="8.5" fill="{c["sub"]}">{esc(sub)}</text>')
    return svg(W, H, defs, b)


# --------------------------------------------------------------------------- #
#  pipeline
# --------------------------------------------------------------------------- #

def pipeline(dark, d):
    c = P["dark" if dark else "light"]
    W, H = 880, 150
    defs, b = [], []
    defs.append('<linearGradient id="flow" x1="0" y1="0" x2="1" y2="0">'
                f'<stop offset="0" stop-color="{c["purple"]}"/>'
                f'<stop offset="0.5" stop-color="{c["cyan"]}"/>'
                f'<stop offset="1" stop-color="{c["pink"]}"/></linearGradient>')
    defs.append(f'<radialGradient id="dot"><stop offset="0" stop-color="#fff"/>'
                f'<stop offset="0.4" stop-color="{c["cyan"]}"/>'
                f'<stop offset="1" stop-color="{c["cyan"]}" stop-opacity="0"/></radialGradient>')
    b.append(f'<rect width="{W}" height="{H}" rx="14" fill="{c["bg"]}" stroke="{c["border"]}"/>')
    b.append(f'<text x="22" y="32" font-family="{SANS}" font-size="13" font-weight="700" '
             f'letter-spacing="2" fill="{c["fg"]}">EVERY RELEASE, VERIFIED</text>')
    b.append(f'<text x="{W-22}" y="32" text-anchor="end" font-family="{MONO}" font-size="10" '
             f'fill="{c["sub"]}">git tag -&gt; CI -&gt; signed images -&gt; registries</text>')
    y = 96
    x0, x1 = 70, W - 70
    defs.append(f'<path id="flowpath" d="M{x0},{y} H{x1}"/>')
    b.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{c["border"]}" '
             f'stroke-width="2" stroke-dasharray="4 6"/>')
    b.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="url(#flow)" '
             f'stroke-width="2" stroke-dasharray="40 1000">'
             f'<animate attributeName="stroke-dashoffset" values="0;-1040" dur="3.2s" '
             f'repeatCount="indefinite"/></line>')
    nodes = ["git tag", "Actions", "cosign", "GHCR", "crates.io", "PyPI", "npm"]
    span = (x1 - x0) / (len(nodes) - 1)
    for i, label in enumerate(nodes):
        cx = x0 + i * span
        b.append(f'<circle cx="{cx}" cy="{y}" r="9" fill="{c["bg"]}" stroke="url(#flow)" stroke-width="2">'
                 f'<animate attributeName="r" values="9;10.5;9" dur="3.2s" '
                 f'begin="{i*0.32}s" repeatCount="indefinite"/></circle>')
        b.append(f'<text x="{cx}" y="{y+30}" text-anchor="middle" font-family="{MONO}" '
                 f'font-size="10" fill="{c["sub"]}">{esc(label)}</text>')
    b.append(f'<circle r="6" fill="url(#dot)">'
             f'<animateMotion dur="3.2s" repeatCount="indefinite"><mpath href="#flowpath"/>'
             f'</animateMotion></circle>')
    return svg(W, H, defs, b)


# --------------------------------------------------------------------------- #
#  guestbook wall (rendered from issues - GitHub strips <script>, so no giscus)
# --------------------------------------------------------------------------- #

GB_REPO = "BartoszOsiej/BartoszOsiej"


def _wrap(text, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines


def guestbook(dark, d):
    c = P["dark" if dark else "light"]
    entries = d.get("guestbook", [])[:6]
    W = 880
    top, rowh = 62, 92
    H = top + max(len(entries), 1) * rowh + 14
    defs, b = [], []
    b.append(f'<rect width="{W}" height="{H}" rx="14" fill="{c["bg"]}" stroke="{c["border"]}"/>')
    b.append(f'<text x="22" y="36" font-family="{SANS}" font-size="13" font-weight="700" '
             f'letter-spacing="2" fill="{c["fg"]}">GUESTBOOK</text>')
    b.append(f'<text x="{W-22}" y="36" text-anchor="end" font-family="{MONO}" font-size="10" '
             f'fill="{c["sub"]}">{len(d.get("guestbook", []))} signature(s) · rendered from issues</text>')
    if not entries:
        b.append(f'<text x="{W/2}" y="{top+40}" text-anchor="middle" font-family="{MONO}" '
                 f'font-size="13" fill="{c["sub"]}">be the first to sign ✍</text>')
        return svg(W, H, defs, b)
    palette = [c["purple"], c["cyan"], c["pink"], c["amber"], c["green"], c["blue"]]
    for i, e in enumerate(entries):
        y = top + i * rowh
        col = palette[i % len(palette)]
        b.append(f'<rect x="22" y="{y}" width="{W-44}" height="{rowh-12}" rx="10" '
                 f'fill="{c["panel"]}" stroke="{c["border"]}"/>')
        b.append(f'<rect x="22" y="{y}" width="4" height="{rowh-12}" rx="2" fill="{col}"/>')
        b.append(f'<circle cx="52" cy="{y+28}" r="15" fill="{col}" opacity="0.20"/>')
        b.append(f'<text x="52" y="{y+33}" text-anchor="middle" font-family="{MONO}" '
                 f'font-size="14" font-weight="700" fill="{col}">{esc(e["user"][0].upper())}</text>')
        b.append(f'<text x="78" y="{y+24}" font-family="{SANS}" font-size="13" font-weight="700" '
                 f'fill="{c["fg"]}">@{esc(e["user"])}</text>')
        b.append(f'<text x="{W-34}" y="{y+24}" text-anchor="end" font-family="{MONO}" '
                 f'font-size="10" fill="{c["sub"]}">{esc(e["created"])}'
                 + (f'  ♥ {e["reactions"]}' if e.get("reactions") else "") + '</text>')
        body = e.get("body") or e.get("title") or ""
        for k, line in enumerate(_wrap(body, 92)[:2]):
            b.append(f'<text x="78" y="{y+44+k*17}" font-family="{MONO}" font-size="11.5" '
                     f'fill="{c["sub"]}">{esc(line)}</text>')
    return svg(W, H, defs, b)


# --------------------------------------------------------------------------- #
#  section rule + self-hosted star history
# --------------------------------------------------------------------------- #

def rule(dark):
    c = P["dark" if dark else "light"]
    W, H = 1280, 8
    defs = ['<linearGradient id="rr" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0" stop-color="{c["purple"]}"/>'
            f'<stop offset="0.5" stop-color="{c["cyan"]}"/>'
            f'<stop offset="1" stop-color="{c["pink"]}"/></linearGradient>']
    b = [f'<line x1="0" y1="4" x2="{W}" y2="4" stroke="{c["border"]}" stroke-width="1"/>',
         f'<line x1="0" y1="4" x2="{W}" y2="4" stroke="url(#rr)" stroke-width="2" '
         f'stroke-dasharray="90 1190">'
         f'<animate attributeName="stroke-dashoffset" values="0;-1280" dur="4.5s" '
         f'repeatCount="indefinite"/></line>']
    return svg(W, H, defs, b)


def star_history(d, dark):
    c = P["dark" if dark else "light"]
    W, H = 880, 190
    hist = d.get("star_hist") or [d["stars"]]
    defs = ['<linearGradient id="sa" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{c["amber"]}" stop-opacity="0.45"/>'
            f'<stop offset="1" stop-color="{c["amber"]}" stop-opacity="0"/>'
            '</linearGradient>']
    b = [f'<rect width="{W}" height="{H}" rx="14" fill="{c["bg"]}" stroke="{c["border"]}"/>',
         f'<text x="22" y="34" font-family="{SANS}" font-size="13" font-weight="700" '
         f'letter-spacing="2" fill="{c["fg"]}">STAR HISTORY</text>',
         f'<text x="{W-22}" y="34" text-anchor="end" font-family="{MONO}" font-size="10" '
         f'fill="{c["sub"]}">self-tracked · {len(hist)} day(s)</text>']
    x0, x1, y0, y1 = 40, W - 40, H - 40, 58
    vals = hist[-60:]
    mx = max(vals) or 1
    n = len(vals)
    pts = []
    for i, v in enumerate(vals):
        x = x0 + (i / (n - 1) * (x1 - x0) if n > 1 else (x1 - x0) / 2)
        y = y1 - (v / mx) * (y1 - y0)
        pts.append((x, y))
    poly = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    if n > 1:
        area = f"{pts[0][0]:.1f},{y1} {poly} {pts[-1][0]:.1f},{y1}"
        b.append(f'<polygon points="{area}" fill="url(#sa)"/>')
        b.append(f'<polyline points="{poly}" fill="none" stroke="{c["amber"]}" '
                 f'stroke-width="2.5" stroke-linejoin="round"/>')
    lx, ly = pts[-1]
    b.append(f'<circle cx="{lx:.1f}" cy="{ly:.1f}" r="5" fill="{c["amber"]}">'
             f'<animate attributeName="r" values="5;7;5" dur="2s" repeatCount="indefinite"/></circle>')
    b.append(f'<text x="{lx-10:.1f}" y="{ly-12:.1f}" text-anchor="end" font-family="{MONO}" '
             f'font-size="16" font-weight="700" fill="{c["fg"]}">{d["stars"]} ★</text>')
    return svg(W, H, defs, b)


# --------------------------------------------------------------------------- #
#  banner + divider (self-hosted animated hero)
# --------------------------------------------------------------------------- #

def banner(dark):
    c = P["dark" if dark else "light"]
    W, H = 1280, 320
    lo = 0.18 if dark else 0.10
    defs, b = [], []
    defs.append(f'<filter id="soft" x="-40%" y="-40%" width="180%" height="180%">'
                f'<feGaussianBlur stdDeviation="90"/></filter>')
    defs.append(f'<filter id="glow" x="-30%" y="-30%" width="160%" height="160%">'
                f'<feGaussianBlur stdDeviation="10"/></filter>')
    defs.append('<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">'
                f'<path d="M40 0H0V40" fill="none" stroke="{c["fg"]}" stroke-width="1"/></pattern>')
    defs.append('<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">'
                f'<stop offset="0" stop-color="{c["purple"]}"/>'
                f'<stop offset="0.5" stop-color="{c["cyan"]}"/>'
                f'<stop offset="1" stop-color="{c["pink"]}"/></linearGradient>')
    defs.append('<linearGradient id="scan" x1="0" y1="0" x2="1" y2="0">'
                f'<stop offset="0" stop-color="{c["cyan"]}" stop-opacity="0"/>'
                f'<stop offset="0.5" stop-color="{c["cyan"]}" stop-opacity="0.5"/>'
                f'<stop offset="1" stop-color="{c["cyan"]}" stop-opacity="0"/></linearGradient>')
    defs.append(f'<clipPath id="tclip"><text x="{W/2}" y="164" text-anchor="middle" '
                f'font-family="{SANS}" font-size="64" font-weight="800" '
                f'letter-spacing="8">BARTOSZ OSIEJ</text></clipPath>')

    b.append(f'<rect width="{W}" height="{H}" rx="18" fill="{c["bg"]}"/>')
    b.append(f'<rect width="{W}" height="{H}" rx="18" fill="url(#grid)" opacity="0.05"/>')

    blobs = [(c["purple"], 300, 90, 300, 200, "0,0;110,40;-70,-30;0,0", 19),
             (c["cyan"], 950, 240, 340, 200, "0,0;-120,-50;80,30;0,0", 23),
             (c["pink"], 640, 40, 260, 170, "0,0;60,70;-90,-20;0,0", 27)]
    for col, cx, cy, rx, ry, vals, dur in blobs:
        b.append(f'<g filter="url(#soft)" opacity="{lo}"><ellipse cx="{cx}" cy="{cy}" '
                 f'rx="{rx}" ry="{ry}" fill="{col}">'
                 f'<animateTransform attributeName="transform" type="translate" '
                 f'values="{vals}" dur="{dur}s" repeatCount="indefinite"/></ellipse></g>')

    for i in range(30):
        x = 30 + (i * 47) % (W - 60)
        y = 40 + (i * 83) % (H - 70)
        r = 1 + (i % 3) * 0.7
        col = [c["cyan"], c["purple"], c["pink"]][i % 3]
        b.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}">'
                 f'<animateTransform attributeName="transform" type="translate" '
                 f'values="0,0;0,{-(18 + i % 26)};0,0" dur="{5 + i % 5}s" '
                 f'begin="{i * 0.2:.1f}s" repeatCount="indefinite"/>'
                 f'<animate attributeName="opacity" values="0.12;0.7;0.12" '
                 f'dur="{3 + i % 4}s" begin="{i * 0.13:.2f}s" repeatCount="indefinite"/></circle>')

    b.append(f'<rect x="-200" y="0" width="200" height="{H}" fill="url(#scan)" opacity="0.16">'
             f'<animateTransform attributeName="transform" type="translate" '
             f'values="0,0;{W+200},0" dur="7s" repeatCount="indefinite"/></rect>')

    b.append(f'<text x="{W/2}" y="164" text-anchor="middle" font-family="{SANS}" '
             f'font-size="64" font-weight="800" letter-spacing="8" fill="url(#tg)" '
             f'filter="url(#glow)" opacity="0.55">BARTOSZ OSIEJ</text>')
    b.append(f'<text x="{W/2}" y="164" text-anchor="middle" font-family="{SANS}" '
             f'font-size="64" font-weight="800" letter-spacing="8" fill="url(#tg)">BARTOSZ OSIEJ</text>')
    b.append(f'<g clip-path="url(#tclip)"><rect x="-160" y="90" width="120" height="120" '
             f'fill="#ffffff" opacity="0.35" transform="skewX(-18)">'
             f'<animateTransform attributeName="transform" type="translate" '
             f'values="0,0;{W+320},0" dur="5.5s" repeatCount="indefinite"/></rect></g>')

    b.append(f'<text x="{W/2}" y="205" text-anchor="middle" font-family="{MONO}" '
             f'font-size="25" fill="{c["sub"]}">systems developer · rust · ebpf · compilers</text>')
    b.append(f'<text x="{W/2}" y="237" text-anchor="middle" font-family="{MONO}" '
             f'font-size="20" fill="{c["fg"]}" opacity="0.85">founder @ hartwell labs · open source, MIT</text>')
    b.append(f'<circle cx="{W/2 - 210}" cy="262" r="5" fill="{c["green"]}">'
             f'<animate attributeName="opacity" values="1;0.2;1" dur="1.8s" repeatCount="indefinite"/></circle>')
    b.append(f'<text x="{W/2 - 195}" y="267" font-family="{MONO}" font-size="18" '
             f'fill="{c["sub"]}">shipping tested software</text>')
    b.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="none" '
             f'stroke="url(#tg)" stroke-opacity="0.4"/>')
    return svg(W, H, defs, b)


def divider(dark):
    c = P["dark" if dark else "light"]
    W, H = 1280, 26
    defs = ['<linearGradient id="dg" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0" stop-color="{c["purple"]}" stop-opacity="0"/>'
            f'<stop offset="0.5" stop-color="{c["cyan"]}" stop-opacity="0.9"/>'
            f'<stop offset="1" stop-color="{c["pink"]}" stop-opacity="0"/></linearGradient>']
    b = [f'<line x1="0" y1="13" x2="{W}" y2="13" stroke="{c["border"]}" stroke-width="1"/>',
         f'<line x1="0" y1="13" x2="{W}" y2="13" stroke="url(#dg)" stroke-width="2" '
         f'stroke-dasharray="160 1120">'
         f'<animate attributeName="stroke-dashoffset" values="0;-1280" dur="5s" '
         f'repeatCount="indefinite"/></line>']
    return svg(W, H, defs, b)


def svg(W, H, defs, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}">\n<defs>\n' + "\n".join(defs) +
            '\n</defs>\n' + "\n".join(body) + '\n</svg>\n')


def main():
    os.makedirs(OUT, exist_ok=True)
    d = live_data()
    for dark, suffix in ((True, "dark"), (False, "light")):
        outs = {
            f"banner-{suffix}.svg": banner(dark),
            f"divider-{suffix}.svg": divider(dark),
            f"rule-{suffix}.svg": rule(dark),
            f"stars-{suffix}.svg": star_history(d, dark),
            f"guestbook-{suffix}.svg": guestbook(dark, d),
            f"terminal-{suffix}.svg": terminal(dark),
            f"dashboard-{suffix}.svg": dashboard(dark, d),
            f"achievements-{suffix}.svg": achievements(dark),
            f"pipeline-{suffix}.svg": pipeline(dark, d),
        }
        for name, content in outs.items():
            with open(os.path.join(OUT, name), "w") as f:
                f.write(content)
    print(json.dumps({"widgets": "ok", "stamp": d["stamp"],
                      "stars": d["stars"], "followers": d["followers"]}, indent=1))


if __name__ == "__main__":
    main()
