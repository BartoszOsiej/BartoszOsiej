#!/usr/bin/env python3
"""Self-hosted live stats engine.

Fetches real download metrics from npm / PyPI / crates.io / GitHub releases,
keeps a rolling history and renders SVG dashboard cards. No third-party
badge services involved - every pixel is generated here.
"""

import json
import os
import time
import urllib.request
from datetime import datetime, timezone, timedelta

OUT = os.environ.get("STATS_OUT", os.path.join(os.getcwd(), "out"))
HISTORY = os.path.join(OUT, "history.json")
VIEWS = os.path.join(OUT, "views.json")

NPM = ["aurora-os", "bartosz-osiej-docs", "novactorio", "n2-mesh",
       "bartosz-osiej-portfolio", "prompt-inbox"]
PYPI = ["externum", "fastapi-url"]
CRATES = ["process-monitor", "netrecon", "shadowscan", "hashsleuth",
          "packeteye", "nv2_engine"]
GH_REPOS = ["halcyon-process-monitor", "cybersec-tools", "NV2_ENGINE",
            "externum", "FastAPI-url", "AURORA-OS", "n2-mesh",
            "prompt-inbox", "Portfolio", "Docs"]


def fetch(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {"User-Agent": "stats-engine/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def npm_downloads(pkg):
    try:
        return fetch(f"https://api.npmjs.org/downloads/point/last-month/{pkg}")["downloads"]
    except Exception:
        return 0


def pypi_downloads(pkg):
    try:
        d = fetch(f"https://pypistats.org/api/packages/{pkg.replace('-', '_')}/recent")
        return d["data"]["last_month"] + d["data"].get("last_day", 0) * 0  # last_month only
    except Exception:
        try:
            d = fetch(f"https://pypistats.org/api/packages/{pkg}/recent")
            return d["data"]["last_month"]
        except Exception:
            return 0


def crates_downloads(name):
    try:
        d = fetch(f"https://crates.io/api/v1/crates/{name}")
        return int(d["crate"]["recent_downloads"] or 0), int(d["crate"]["downloads"] or 0)
    except Exception:
        return 0, 0


def gh_release_downloads(repo):
    total = 0
    try:
        page = 1
        while True:
            rels = fetch(f"https://api.github.com/repos/BartoszOsiej/{repo}/releases?per_page=100&page={page}",
                         {"User-Agent": "stats-engine/1.0",
                          "Authorization": f"Bearer {os.environ.get('GH_TOKEN','')}"}
                         if os.environ.get("GH_TOKEN") else None)
            if not rels:
                break
            for rel in rels:
                for a in rel.get("assets", []):
                    total += a.get("download_count", 0)
            page += 1
    except Exception:
        pass
    return total


TRAFFIC_REPOS = ["halcyon-process-monitor", "cybersec-tools", "NV2_ENGINE",
                 "externum", "FastAPI-url", "AURORA-OS", "n2-mesh",
                 "prompt-inbox", "Portfolio", "Docs", "BartoszOsiej"]


def ecosystem_views():
    """All-time view counter across the whole ecosystem, self-captured.

    GitHub's Traffic API exposes a rolling 14-day window per repo, so every
    run folds each repo's window into a persistent per-day map - a calendar
    day is recorded once and the running total never loses a day.
    """
    tok = os.environ.get("GH_TOKEN", "")
    state = {}
    if os.path.exists(VIEWS):
        with open(VIEWS) as f:
            state = json.load(f)
    days = state.setdefault("days", {})
    for repo in TRAFFIC_REPOS:
        try:
            d = fetch(f"https://api.github.com/repos/BartoszOsiej/{repo}/traffic/views",
                      {"User-Agent": "stats-engine/1.0",
                       "Authorization": f"Bearer {tok}",
                       "Accept": "application/vnd.github+json"})
        except Exception:
            continue
        for v in d.get("views", []):
            day = v["timestamp"][:10]
            # per-day per-repo slot: overwriting (not adding) keeps every run
            # idempotent even though the 14-day windows overlap between runs
            days.setdefault(day, {})[repo] = {"count": v["count"],
                                              "uniques": v["uniques"]}
    state["days"] = dict(sorted(days.items()))
    state["total"] = sum(r["count"] for d in state["days"].values()
                         for r in d.values())
    state["uniques"] = sum(r["uniques"] for d in state["days"].values()
                           for r in d.values())
    with open(VIEWS, "w") as f:
        json.dump(state, f, indent=1)
    return state["total"], state["uniques"]


def fmt(n):
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}k"
    return str(n)


def load_history():
    if os.path.exists(HISTORY):
        with open(HISTORY) as f:
            return json.load(f)
    return {}


def save_history(h):
    h = dict(sorted(h.items())[-90:])
    with open(HISTORY, "w") as f:
        json.dump(h, f, indent=1)


def sparkline(values, w, h, color):
    if len(values) < 2 or max(values) == 0:
        return ""
    mx = max(values)
    pts = []
    for i, v in enumerate(values):
        x = i / (len(values) - 1) * (w - 4) + 2
        y = h - 6 - (v / mx) * (h - 12)
        pts.append(f"{x:.1f},{y:.1f}")
    poly = " ".join(pts)
    area = f"2,{h-2} {poly} {w-2},{h-2}"
    return (f'<polyline points="{poly}" fill="none" stroke="{color}" stroke-width="2" '
            f'stroke-linejoin="round" stroke-linecap="round"/>'
            f'<polygon points="{area}" fill="{color}" opacity="0.12"/>')


def card(dark, totals, hist_values, stamp):
    fg = "#e6edf3" if dark else "#1f2328"
    sub = "#8b949e" if dark else "#656d76"
    bg = "#0d1117" if dark else "#ffffff"
    row = "#30363d" if dark else "#d0d7de"
    accent = "#a371f7" if dark else "#8250df"
    accent2 = "#39c5cf" if dark else "#0969da"
    accent3 = "#f778ba" if dark else "#bf3989"

    W, H = 480, 196
    rows_y = 64
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{accent}"/><stop offset="0.5" stop-color="{accent2}"/>'
        f'<stop offset="1" stop-color="{accent3}"/></linearGradient></defs>',
        f'<rect width="{W}" height="{H}" rx="12" fill="{bg}" stroke="{row}" stroke-width="1"/>',
        f'<rect width="{W}" height="34" rx="12" fill="url(#g)" opacity="0.18"/>',
        f'<text x="16" y="22" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="13" '
        f'font-weight="700" letter-spacing="2" fill="{fg}">LIVE PACKAGE METRICS</text>',
        f'<text x="{W-14}" y="22" text-anchor="end" font-family="monospace" font-size="10" '
        f'fill="{sub}">{stamp}</text>',
    ]
    items = [
        ("npm", totals["npm"], accent),
        ("PyPI", totals["pypi"], accent2),
        ("crates.io", totals["crates"], accent3),
        ("GitHub releases", totals["gh"], sub),
    ]
    y = rows_y
    for label, val, col in items:
        parts += [
            f'<circle cx="20" cy="{y-4}" r="3.5" fill="{col}"/>',
            f'<text x="32" y="{y}" font-family="Segoe UI,Helvetica,Arial,sans-serif" '
            f'font-size="13" fill="{sub}">{label}</text>',
            f'<text x="{W-16}" y="{y}" text-anchor="end" font-family="JetBrains Mono,monospace" '
            f'font-size="15" font-weight="700" fill="{fg}">{fmt(val)}</text>',
        ]
        y += 26
    # mini sparkline po prawej
    parts.append(f'<g transform="translate({W-150},40)">{sparkline(hist_values, 134, 44, accent)}</g>')
    parts.append("</svg>")
    return "\n".join(parts)


def views_badge(dark, total, uniques, stamp):
    fg = "#e6edf3" if dark else "#1f2328"
    sub = "#8b949e" if dark else "#656d76"
    bg = "#0d1117" if dark else "#ffffff"
    row = "#30363d" if dark else "#d0d7de"
    accent = "#a371f7" if dark else "#8250df"

    W, H = 340, 64
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        f'<defs><linearGradient id="vg" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="{accent}"/><stop offset="1" stop-color="#39c5cf"/>'
        f'</linearGradient></defs>',
        f'<rect width="{W}" height="{H}" rx="10" fill="{bg}" stroke="{row}" stroke-width="1"/>',
        f'<rect width="{W}" height="{H}" rx="10" fill="url(#vg)" opacity="0.08"/>',
        f'<circle cx="22" cy="{H/2}" r="5" fill="url(#vg)"/>',
        f'<text x="36" y="27" font-family="Segoe UI,Helvetica,Arial,sans-serif" font-size="11" '
        f'font-weight="700" letter-spacing="1.5" fill="{sub}">ECOSYSTEM VIEWS</text>',
        f'<text x="36" y="48" font-family="JetBrains Mono,monospace" font-size="17" '
        f'font-weight="700" fill="{fg}">{total:,}</text>',
        f'<text x="{W-14}" y="27" text-anchor="end" font-family="Segoe UI,Helvetica,Arial,sans-serif" '
        f'font-size="10" fill="{sub}">{uniques:,} unique</text>',
        f'<text x="{W-14}" y="48" text-anchor="end" font-family="monospace" font-size="9" '
        f'fill="{sub}">self-hosted counter</text>',
        "</svg>",
    ]
    return "\n".join(parts)


def main():
    os.makedirs(OUT, exist_ok=True)
    npm_total = sum(npm_downloads(p) for p in NPM)
    pypi_total = sum(pypi_downloads(p) for p in PYPI)
    crates_recent = sum(crates_downloads(c)[0] for c in CRATES)
    crates_all = sum(crates_downloads(c)[1] for c in CRATES)
    gh_total = sum(gh_release_downloads(r) for r in GH_REPOS)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    hist = load_history()
    hist[today] = {"npm": npm_total, "pypi": pypi_total,
                   "crates": crates_recent, "gh": gh_total}
    save_history(hist)

    values = [v["npm"] + v["pypi"] + v["crates"] + v["gh"] for v in hist.values()]
    totals = {"npm": npm_total, "pypi": pypi_total,
              "crates": crates_recent, "gh": gh_total}

    meta = {
        "updated": stamp,
        "totals": totals,
        "crates_all_time": crates_all,
        "packages": {"npm": NPM, "pypi": PYPI, "crates": CRATES},
    }

    views_total, views_uniq = ecosystem_views()
    meta["profile_views"] = {"total": views_total, "uniques": views_uniq}

    for dark, suffix in ((True, "dark"), (False, "light")):
        svg = card(dark, totals, values[-60:], stamp)
        with open(os.path.join(OUT, f"metrics-{suffix}.svg"), "w") as f:
            f.write(svg)
        with open(os.path.join(OUT, f"views-{suffix}.svg"), "w") as f:
            f.write(views_badge(dark, views_total, views_uniq, stamp))

    with open(os.path.join(OUT, "meta.json"), "w") as f:
        json.dump(meta, f, indent=1)

    print(json.dumps(meta, indent=1))


if __name__ == "__main__":
    main()
