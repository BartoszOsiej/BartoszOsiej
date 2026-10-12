#!/usr/bin/env python3
"""Generate 1280x640 social-preview cards for the flagship repos.

GitHub's API cannot set a repo's social preview image, so these PNGs are
generated locally (SVG -> rsvg-convert) and uploaded by hand per repo.
"""
import os
import subprocess

SANS = "Inter, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'JetBrains Mono', 'SFMono-Regular', Menlo, Consolas, monospace"
OUT = os.environ.get("SOCIAL_OUT", os.path.join(os.path.dirname(__file__), "..", "social"))

REPOS = [
    ("talus-process-monitor", "Talus", "Anti-ransomware for Linux", "Rust · eBPF · LSM", "#a371f7"),
    ("trustnode", "TrustNode", "Proof-of-History validator, from scratch", "Rust · Solana-style · MIT", "#2ea043"),
    ("NV2_ENGINE", "NV2_ENGINE", "Genuinely reproducible builds", "Rust · bit-for-bit", "#58a6ff"),
    ("externum", "externum", "A language that compiles itself away", "Python → Py · Bash · VM", "#e3b341"),
    ("CyberForge", "CyberForge", "Offensive-security toolkit", "Rust · rustls", "#f85149"),
    ("QuantumShield", "QuantumShield", "Post-quantum cryptography", "Rust · PQC", "#39c5cf"),
    ("pqbit", "pqbit", "Post-quantum bit-level primitives", "Rust · lattice", "#db61a2"),
    ("Docs", "Docs", "Where the thinking lives", "Docs · npm CI", "#8b949e"),
]


def card(repo, name, tag, tech, accent):
    W, H = 1280, 640
    defs = [
        '<radialGradient id="a" cx="0.18" cy="0.15" r="0.9">'
        f'<stop offset="0" stop-color="{accent}" stop-opacity="0.42"/>'
        '<stop offset="1" stop-color="#0d1117" stop-opacity="0"/></radialGradient>',
        '<radialGradient id="b" cx="0.95" cy="1.05" r="0.85">'
        '<stop offset="0" stop-color="#39c5cf" stop-opacity="0.30"/>'
        '<stop offset="1" stop-color="#0d1117" stop-opacity="0"/></radialGradient>',
        f'<linearGradient id="t" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0" stop-color="#e6edf3"/>'
        f'<stop offset="1" stop-color="{accent}"/></linearGradient>',
    ]
    b = [
        f'<rect width="{W}" height="{H}" fill="#0d1117"/>',
        '<rect width="1600" height="800" fill="url(#a)" transform="translate(-160,-80)"/>',
        '<rect width="1600" height="800" fill="url(#b)" transform="translate(-160,-80)"/>',
        f'<rect x="0" y="0" width="{W}" height="6" fill="{accent}"/>',
        f'<text x="80" y="150" font-family="{MONO}" font-size="20" fill="{accent}" '
        f'letter-spacing="6">HARTWELL LABS</text>',
        f'<text x="80" y="300" font-family="{MONO}" font-size="96" font-weight="700" '
        f'fill="url(#t)">{name}</text>',
        f'<text x="80" y="370" font-family="{SANS}" font-size="34" fill="#c9d1d9">{tag}</text>',
        f'<rect x="80" y="430" width="{26 + len(tech) * 16}" height="46" rx="23" '
        f'fill="none" stroke="{accent}" stroke-width="1.5"/>',
        f'<text x="{80 + 13 + len(tech) * 8}" y="461" text-anchor="middle" '
        f'font-family="{MONO}" font-size="20" fill="{accent}">{tech}</text>',
        f'<text x="80" y="558" font-family="{MONO}" font-size="22" fill="#8b949e">'
        f'github.com/BartoszOsiej/{repo}</text>',
    ]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}"><defs>{"".join(defs)}</defs>{"".join(b)}</svg>')


def main():
    os.makedirs(OUT, exist_ok=True)
    made = []
    for repo, name, tag, tech, accent in REPOS:
        s = card(repo, name, tag, tech, accent)
        sp = os.path.join(OUT, f"{repo}.svg")
        pp = os.path.join(OUT, f"{repo}.png")
        open(sp, "w").write(s)
        subprocess.run(["rsvg-convert", "-w", "1280", "-h", "640", sp, "-o", pp], check=True)
        os.remove(sp)
        made.append((repo, os.path.getsize(pp)))
    for repo, size in made:
        print(f"social/{repo}.png  {size // 1024} KB")


if __name__ == "__main__":
    main()
