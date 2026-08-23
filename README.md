<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=180&section=header&text=Bartosz%20Osiej&fontSize=42&fontColor=fff&animation=fadeIn&desc=Systems%20Developer%20%C2%B7%20Rust%20%C2%B7%20eBPF%20%C2%B7%20Compilers&descSize=18&descAlignY=68" width="100%" />

<div align="center">

[![Typing SVG](https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&weight=600&size=22&duration=2800&pause=1000&color=58A6FF&center=true&vCenter=true&multiline=false&repeat=true&width=700&height=50&lines=Kernel-level+tooling+in+Rust+%F0%9F%A6%80;eBPF+probes+%C2%B7+perf+buffers+%C2%B7+TUI;Compilers+from+scratch+%E2%9A%A1;Voxel+engines+%C2%B7+wgpu+%C2%B7+multiplayer;14+packages+across+4+registries+%F0%9F%93%A6)](https://github.com/BartoszOsiej)

[![Portfolio](https://img.shields.io/badge/Portfolio-bartoszosiej.github.io-1a1a2e?style=for-the-badge&logo=firefox&logoColor=white)](https://bartoszosiej.github.io/Portfolio/)
[![Email](https://img.shields.io/badge/mmc29213@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mmc29213@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Bartosz_Osiej-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/bartosz-osiej)

</div>

> [!IMPORTANT]
> **19 y/o · Poland · open to first paid role** — remote/hybrid, junior systems/backend.
> Everything below is *deployed infrastructure*, not tutorials: 15 repositories, every one with CI/CD, releases with binaries, Docker images and published packages.

---

## ⚙️ Stack

<div align="center">

[![Rust](https://img.shields.io/badge/Rust-systems-000000?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![eBPF](https://img.shields.io/badge/eBPF-Aya_0.13-F00613?style=flat-square&logo=linux&logoColor=white)](https://aya-rs.dev/)
[![Python](https://img.shields.io/badge/Python-compilers-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-engines-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-backend-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![wgpu](https://img.shields.io/badge/wgpu-GPU_rendering-red?style=flat-square&logo=webgl&logoColor=white)](https://wgpu.rs/)
[![Docker](https://img.shields.io/badge/Docker-multi--stage-2496ED?style=flat-square&logo=docker&logoColor=white)](https://github.com/features/packages)
[![Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/features/actions)

</div>

---

## 🚀 Flagship Projects

<table>
<tr><td valign="top" width="50%">

### 🔬 [halcyon-process-monitor](https://github.com/BartoszOsiej/halcyon-process-monitor)

eBPF ransomware behavior tracker — kernel-level `execve`/`openat` tracing through Aya, per-CPU perf buffers, sliding-window alerting, full ratatui TUI.

`Rust` `Aya` `ratatui` `eBPF`

[![crates.io](https://img.shields.io/crates/v/process-monitor?style=flat-square&logo=rust)](https://crates.io/crates/process-monitor) [![GHCR](https://img.shields.io/badge/GHCR-image-2496ED?style=flat-square&logo=docker)](https://github.com/BartoszOsiej/halcyon-process-monitor/pkgs/container/halcyon-process-monitor) [![binary](https://img.shields.io/badge/release-binary-8A2BE2?style=flat-square)](https://github.com/BartoszOsiej/halcyon-process-monitor/releases)

</td><td valign="top" width="50%">

### 🎮 [NV2_ENGINE](https://github.com/BartoszOsiej/NV2_ENGINE)

Voxel game engine with MLP neural renderer, multiplayer over TCP, Epic Games Store integration. Published as a crate.

`Rust` `wgpu` `MLP` `TCP`

[![crates.io](https://img.shields.io/crates/v/nv2_engine?style=flat-square&logo=rust)](https://crates.io/crates/nv2_engine) [![GHCR](https://img.shields.io/badge/GHCR-image-2496ED?style=flat-square&logo=docker)](https://github.com/BartoszOsiej/NV2_ENGINE/pkgs/container/nv2_engine) [![binary](https://img.shields.io/badge/release-binary-8A2BE2?style=flat-square)](https://github.com/BartoszOsiej/NV2_ENGINE/releases)

</td></tr>
<tr><td valign="top" width="50%">

### ⚡ [externum](https://github.com/BartoszOsiej/externum)

Programming language built from scratch — compiles to Python, Bash and native binary. Ownership, traits, macros. 192-test suite, on PyPI since v2.

**▶ [Run it in your browser — and extend the language live](https://bartoszosiej.github.io/externum/)**

`Python` `Compiler design` `PyPI`

[![PyPI](https://img.shields.io/pypi/v/externum?style=flat-square&logo=pypi)](https://pypi.org/project/externum/) [![GHCR](https://img.shields.io/badge/GHCR-image-2496ED?style=flat-square&logo=docker)](https://github.com/BartoszOsiej/externum/pkgs/container/externum) [![Playground](https://img.shields.io/badge/▶_LIVE_PLAYGROUND-extend_it_in_browser-a371f7?style=flat-square)](https://bartoszosiej.github.io/externum/)

</td><td valign="top" width="50%">

### 🔒 [cybersec-tools](https://github.com/BartoszOsiej/cybersec-tools)

Four security tools as one workspace — port scanner, web scanner, hash cracker, packet analyzer. Each shipped separately on crates.io.

`Rust` `Tokio` `libpcap`

[![crates.io](https://img.shields.io/crates/v/netrecon?style=flat-square&label=netrecon&logo=rust)](https://crates.io/crates/netrecon) [![crates.io](https://img.shields.io/crates/v/shadowscan?style=flat-square&label=shadowscan&logo=rust)](https://crates.io/crates/shadowscan) [![crates.io](https://img.shields.io/crates/v/hashsleuth?style=flat-square&label=hashsleuth&logo=rust)](https://crates.io/crates/hashsleuth) [![crates.io](https://img.shields.io/crates/v/packeteye?style=flat-square&label=packeteye&logo=rust)](https://crates.io/crates/packeteye)

</td></tr>
<tr><td valign="top" width="50%">

### 🛡️ [pqguard](https://github.com/BartoszOsiej/pqguard)

Post-quantum file encryption CLI — ML-KEM-768 key exchange + AES-256-GCM + HKDF. NIST FIPS 203 compliant, fuzz-tested.

**▶ [Landing page](https://bartoszosiej.github.io/pqguard/)**

`Rust` `Cryptography` `NIST`

[![crates.io](https://img.shields.io/crates/v/pqguard?style=flat-square&logo=rust)](https://crates.io/crates/pqguard) [![CI](https://img.shields.io/github/actions/workflow/status/BartoszOsiej/pqguard/ci.yml?branch=main&style=flat-square&logo=githubactions&label=ci)](https://github.com/BartoszOsiej/pqguard/actions) [![GHCR](https://img.shields.io/badge/GHCR-image-2496ED?style=flat-square&logo=docker)](https://github.com/BartoszOsiej/pqguard/pkgs/container/pqguard)

</td><td valign="top" width="50%">

### 🧬 [Docs](https://bartoszosiej.github.io/Docs/)

Technical documentation site — architecture guides, API reference, deployment playbooks.

`TypeScript` `Deploy` `GitHub Pages`

[![npm](https://img.shields.io/npm/v/bartosz-osiej-docs?style=flat-square&logo=nodedotjs)](https://www.npmjs.com/package/bartosz-osiej-docs) [![Deploy](https://img.shields.io/badge/Deploy-live-green?style=flat-square)](https://bartoszosiej.github.io/Docs/)

</td></tr>
</table>

<details>
<summary><b>📦 More projects (click to expand)</b></summary>

| | Project | What it is | Try it |
|---|---------|-----------|--------|
| ◈ | [**AURORA-OS**](https://github.com/BartoszOsiej/AURORA-OS) | Complete OS in the browser — kernel, window manager, filesystem, 8 apps, procedural audio | [npm](https://www.npmjs.com/package/aurora-os) |
| 🌐 | [**n2-mesh**](https://github.com/BartoszOsiej/n2-mesh) | Serverless P2P chat — WebRTC + MQTT signaling, zero dependencies | [npm](https://www.npmjs.com/package/n2-mesh) |
| 🔗 | [**FastAPI-url**](https://github.com/BartoszOsiej/FastAPI-url) | URL shortener — JWT auth, click tracking, React dashboard | [PyPI](https://pypi.org/project/fastapi-url/) |
| 🎯 | [**prompt-inbox**](https://github.com/BartoszOsiej/prompt-inbox) | Remote prompt inbox for AI agents — mobile-first, zero backend | [npm](https://www.npmjs.com/package/prompt-inbox) |
| 🎮 | [**novactorio**](https://github.com/BartoszOsiej/Factorio-web-game) | Factorio-style factory builder fully playable in browser | [npm](https://www.npmjs.com/package/novactorio) |
| 📚 | [**teleinformatyka-wikipedia**](https://github.com/BartoszOsiej/teleinformatyka-wikipedia) | PL/EN telecom encyclopedia — networking, 5G, fiber, security | [docs](https://bartoszosiej.github.io/Docs/) |

</details>

---

## 📦 Distribution — everything ships, nothing rots

```mermaid
flowchart LR
    T["🐳 git tag"] --> CI["GitHub Actions"]
    CI --> D["Docker multi-stage"]
    D --> G["GHCR: 11 images"]
    CI --> B["cargo release build"]
    B --> R["Release + binaries"]
    CI --> P["Registry publish"]
    P --> C["crates.io: 6 crates"]
    P --> Y["PyPI: 2 packages"]
    P --> N["npm: 6 packages"]
```

<div align="center">

| 🐳 GHCR images | 🦀 crates.io | 🐍 PyPI | 🟢 npm | 📋 Repos with CI/CD |
|:--------------:|:------------:|:-------:|:------:|:----------------------:|
| **13** | **8** | **2** | **6** | **15 / 15** |

</div>

### 🕹️ Interactive — a recruiter can actually run this

| | |
|---|---|
| **▶ [Externum Playground](https://bartoszosiej.github.io/externum/)** | The programming language running 100% in your browser (Pyodide). Write programs, hot-load your own modules into the live runtime, compile to Python/Bash/binary. Sessions shareable by URL. |
| **🧬 `/define`** | Comment on an issue → the bot validates your module against Externum's type checker → opens a PR into the stdlib → once merged, `import` works for everyone including the web playground. [The language evolves from comments.](https://github.com/BartoszOsiej/externum/issues/7) |
| **🎮 `/run`** | [Comment on cybersec-tools](https://github.com/BartoszOsiej/cybersec-tools/issues/10) → the bot builds the workspace in CI and executes the real binaries with sandboxed guardrails, posting output back. |
| **🔏 `./verify.sh v0.4.5`** | One command verifies SLSA provenance + Sigstore signatures + SBOM of any release. No trust required. |

### ⚡ One-command install — like real CLI tools

```bash
# macOS (Apple Silicon & Intel)
brew tap bartoszosiej/tap https://github.com/BartoszOsiej/homebrew-tap
brew install bartoszosiej/tap/netrecon bartoszosiej/tap/hashsleuth

# Windows
scoop bucket add bartoszosiej https://github.com/BartoszOsiej/scoop-bucket
scoop install netrecon hashsleuth
```

*Formulas & manifests are re-synced hourly by a bot with fresh SHA-256 sums — never stale.*

### 🖥️ Build matrix — 5 platforms per release

<div align="center">

| Linux x86_64 | Linux arm64 | macOS arm64 | macOS x86_64 | Windows x64 |
|:------------:|:-----------:|:-----------:|:------------:|:-----------:|
| ✅ | ✅ | ✅ | ✅ | ✅ |

</div>

---

## 🔐 Signed supply chain

*The same pipeline discipline big tech uses — cryptographically verifiable, not "trust me".*

<div align="center">

[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/BartoszOsiej/cybersec-tools/badge)](https://scorecard.dev/viewer/?uri=github.com/BartoszOsiej/cybersec-tools)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/BartoszOsiej/halcyon-process-monitor/badge)](https://scorecard.dev/viewer/?uri=github.com/BartoszOsiej/halcyon-process-monitor)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/BartoszOsiej/NV2_ENGINE/badge)](https://scorecard.dev/viewer/?uri=github.com/BartoszOsiej/NV2_ENGINE)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/BartoszOsiej/externum/badge)](https://scorecard.dev/viewer/?uri=github.com/BartoszOsiej/externum)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/BartoszOsiej/FastAPI-url/badge)](https://scorecard.dev/viewer/?uri=github.com/BartoszOsiej/FastAPI-url)

</div>

| Layer | What it means |
|---|---|
| **cosign keyless signing** | Every GHCR image is signed via Sigstore/Fulcio OIDC — no keys to leak, identity bound to the GitHub workflow |
| **SLSA v1 provenance** | Every release binary carries a build attestation proving *which commit, which runner, which pipeline* produced it |
| **SPDX SBOM** | Every release ships a machine-readable software bill of materials |
| **OpenSSF Scorecard** | Automated supply-chain security grading on 5 production repos |

Verify it yourself — no trust required:

```bash
# verify a container image signature
cosign verify ghcr.io/bartoszosiej/cybersec-tools \
  --certificate-identity-regexp "^https://github.com/BartoszOsiej/" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com

# verify binary build provenance
gh attestation verify netrecon-x86_64-unknown-linux-gnu \
  -R BartoszOsiej/cybersec-tools
```

---

<details>
<summary><b>🗂️ Full package index</b></summary>

**npm**
[![aurora-os](https://img.shields.io/npm/v/aurora-os?style=flat-square&logo=nodedotjs&label=aurora-os)](https://www.npmjs.com/package/aurora-os)
[![n2-mesh](https://img.shields.io/npm/v/n2-mesh?style=flat-square&logo=nodedotjs&label=n2-mesh)](https://www.npmjs.com/package/n2-mesh)
[![novactorio](https://img.shields.io/npm/v/novactorio?style=flat-square&logo=nodedotjs&label=novactorio)](https://www.npmjs.com/package/novactorio)
[![prompt-inbox](https://img.shields.io/npm/v/prompt-inbox?style=flat-square&logo=nodedotjs&label=prompt-inbox)](https://www.npmjs.com/package/prompt-inbox)
[![docs](https://img.shields.io/npm/v/bartosz-osiej-docs?style=flat-square&logo=nodedotjs&label=bartosz-osiej-docs)](https://www.npmjs.com/package/bartosz-osiej-docs)
[![portfolio](https://img.shields.io/npm/v/bartosz-osiej-portfolio?style=flat-square&logo=nodedotjs&label=bartosz-osiej-portfolio)](https://www.npmjs.com/package/bartosz-osiej-portfolio)

**crates.io**
[![process-monitor](https://img.shields.io/crates/v/process-monitor?style=flat-square&logo=rust)](https://crates.io/crates/process-monitor)
[![pqguard](https://img.shields.io/crates/v/pqguard?style=flat-square&logo=rust)](https://crates.io/crates/pqguard)
[![nv2_engine](https://img.shields.io/crates/v/nv2_engine?style=flat-square&logo=rust)](https://crates.io/crates/nv2_engine)
[![netrecon](https://img.shields.io/crates/v/netrecon?style=flat-square&logo=rust)](https://crates.io/crates/netrecon)
[![shadowscan](https://img.shields.io/crates/v/shadowscan?style=flat-square&logo=rust)](https://crates.io/crates/shadowscan)
[![hashsleuth](https://img.shields.io/crates/v/hashsleuth?style=flat-square&logo=rust)](https://crates.io/crates/hashsleuth)
[![packeteye](https://img.shields.io/crates/v/packeteye?style=flat-square&logo=rust)](https://crates.io/crates/packeteye)

**PyPI**
[![externum](https://img.shields.io/pypi/v/externum?style=flat-square&logo=pypi)](https://pypi.org/project/externum/)
[![fastapi-url](https://img.shields.io/pypi/v/fastapi-url?style=flat-square&logo=pypi)](https://pypi.org/project/fastapi-url/)

</details>

---

## 🛡️ Engineering discipline

> [!NOTE]
> Every repository runs the same production-grade pipeline — this is how I work, not how I pretend to work.

| Practice | Coverage |
|----------|:--------:|
| CodeQL security scanning | ✅ 15/15 |
| Dependabot + vulnerability alerts | ✅ 15/15 |
| Branch protection + squash-merge history | ✅ 15/15 |
| Public sprint boards + milestones | ✅ 6 boards |
| Discussions, CONTRIBUTING, SECURITY, CoC | ✅ 15/15 |
| MIT licensing, topics, descriptions | ✅ 15/15 |

---

## 📊 Live Package Metrics

*Self-hosted stats engine — a scheduled workflow queries npm / PyPI / crates.io /
GitHub releases and renders these cards from scratch. No badge services, no
third-party renderers: every pixel comes from my own pipeline.*

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/metrics-dark.svg" />
  <img src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/metrics-light.svg" />
</picture>

---

## 📈 GitHub Stats

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats-eight-theta.vercel.app/api?username=BartoszOsiej&show_icons=true&hide_border=true&bg_color=0d1117&title_color=58a6ff&icon_color=1f6feb&text_color=c9d1d9&count_private=true" />
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats-eight-theta.vercel.app/api?username=BartoszOsiej&show_icons=true&hide_border=true&bg_color=f6f8fa&title_color=0969da&icon_color=0969da&text_color=24292f&count_private=true" />
  <img width="49%" src="https://github-readme-stats-eight-theta.vercel.app/api?username=BartoszOsiej&show_icons=true&hide_border=true&count_private=true" />
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=BartoszOsiej&layout=compact&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9&langs_count=8" />
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=BartoszOsiej&layout=compact&hide_border=true&bg_color=f6f8fa&title_color=0969da&text_color=24292f&langs_count=8" />
  <img width="41%" src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=BartoszOsiej&layout=compact&hide_border=true&langs_count=8" />
</picture>
<br/>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com/?user=BartoszOsiej&hide_border=true&background=0d1117&ring=58a6ff&fire=F0883E&currStreakLabel=58a6ff" />
  <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com/?user=BartoszOsiej&hide_border=true&background=f6f8fa&ring=0969da&fire=D4A017&currStreakLabel=0969da" />
  <img width="70%" src="https://streak-stats.demolab.com/?user=BartoszOsiej&hide_border=true" />
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=BartoszOsiej&theme=tokyo-night&hide_border=true&bg_color=0d1117&color=c9d1d9&line=58a6ff&point=F0883E" />
  <source media="(prefers-color-scheme: light)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=BartoszOsiej&theme=minimal&hide_border=true&bg_color=f6f8fa&color=24292f&line=0969da&point=D4A017" />
  <img width="100%" src="https://github-readme-activity-graph.vercel.app/graph?username=BartoszOsiej&hide_border=true" />
</picture>

---

## 🗺️ Timeline

```
2021 ──► first lines of code — Java, CryEngine, Minecraft mechanics
2025 ──► networking & security track (teleinformatyka)
2026 Q1 ──► Rust deep dive: voxel engine, eBPF kernel probes, compiler from scratch
2026 Q3 ──► production CI/CD: Actions → GHCR → crates.io / PyPI / npm, 14 packages live
2026 Q4 ──► shipping: teleinformatyka-wikipedia, NV2 multiplayer, first paid role 🎯
```

---

## 🌐 Also here

- **[`ghost0development`](https://github.com/ghost0development)** — archive account since 2021 (31 repos); canonical `halcyon-process-monitor` lives there

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/output/github-contribution-grid-snake.svg" />
  <img width="100%" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/output/github-contribution-grid-snake.svg" />
</picture>

---

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer" width="100%" />

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/views-dark.svg">
  <img alt="Ecosystem views" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/views-light.svg">
</picture>

*Open to work — [`mmc29213@gmail.com`](mailto:mmc29213@gmail.com)*

</div>
