<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/banner-dark.svg" />
  <img alt="Bartosz Osiej — systems developer, Rust, eBPF, compilers, founder of Hartwell Labs" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/banner-light.svg" width="100%" />
</picture>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/typing-dark.svg" />
  <img alt="Self-hosted typewriter headline" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/typing-light.svg" width="86%" />
</picture>

[![Hartwell Labs](https://img.shields.io/badge/Founder_%26_CEO-Hartwell_Labs-F15A24?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Hartwell-Labs)
[![Portfolio](https://img.shields.io/badge/Portfolio-bartoszosiej.github.io-1a1a2e?style=for-the-badge&logo=firefox&logoColor=white)](https://bartoszosiej.github.io/Portfolio/)
[![Books](https://img.shields.io/badge/The_Thread_Calls-Crime_Horror-9c1e1a?style=for-the-badge&logo=amazondotcom&logoColor=white)](https://bartoszosiej.github.io/thethreadcalls/)
[![DEV](https://img.shields.io/badge/dev.to-bartoszosiej-000?style=for-the-badge&logo=devdotto&logoColor=white)](https://dev.to/bartoszosiej)
[![Writing](https://img.shields.io/badge/Writing-technical_articles-1a1a2e?style=for-the-badge&logo=writeforus&logoColor=white)](https://bartoszosiej.github.io/writing/)
[![Email](https://img.shields.io/badge/mmc29213@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mmc29213@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Bartosz_Osiej-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bartoszosiej2007/)
[![Telegram](https://img.shields.io/badge/Telegram-hartwell__info-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/hartwell_info)

</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/terminal-dark.svg" />
  <img alt="Live terminal — Externum compiler, Talus eBPF agent, pqguard, supply-chain verification" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/terminal-light.svg" width="100%" />
</picture>

> [!IMPORTANT]
> **Founder & CEO of [Hartwell Labs](https://github.com/Hartwell-Labs)** — independent engineering lab: eBPF security systems, programming languages and tools, all open source (MIT).
> **19 y/o · Poland · open to first paid role** — remote/hybrid, junior systems/backend. My article on eBPF ransomware detection is **accepted on LinuxSecurity** (publication Sep 22–26) — technical writing samples on request. Author of [*The Stitcher Trilogy*](https://bartoszosiej.github.io/thethreadcalls/) (crime horror).
> **Now (Oct 2026):** [TrustNode](https://github.com/BartoszOsiej/trustnode) — a Solana-like validator built from scratch in Rust (PoH clock, Tower BFT, Sealevel parallel execution, Turbine erasure coding, CRDS gossip); [Externum on DevHunt](https://devhunt.org/tool/externum); new: [Talus Field Guide](https://hartwell-labs.pl/talus-process-monitor/field-guide.html) — deployment & tuning playbook.
> Everything below is *deployed infrastructure*, not tutorials: **25 original repositories** here (+13 under the [Hartwell Labs org](https://github.com/Hartwell-Labs)) — every active one with CI/CD, releases with binaries, Docker images and published packages. 3 PRs open upstream in aya-rs/book.

---

## ⚙️ Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-light.svg" width="100%" />
</picture>

<div align="center">

[![Rust](https://img.shields.io/badge/Rust-systems-000000?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org/)
[![eBPF](https://img.shields.io/badge/eBPF-Aya_0.14-F00613?style=flat-square&logo=linux&logoColor=white)](https://aya-rs.dev/)
[![Python](https://img.shields.io/badge/Python-compilers-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-engines-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-backend-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![wgpu](https://img.shields.io/badge/wgpu-GPU_rendering-red?style=flat-square&logo=webgl&logoColor=white)](https://wgpu.rs/)
[![Docker](https://img.shields.io/badge/Docker-multi--stage-2496ED?style=flat-square&logo=docker&logoColor=white)](https://github.com/features/packages)
[![Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?style=flat-square&logo=githubactions&logoColor=white)](https://github.com/features/actions)

</div>

---

## 🚀 Flagship Projects

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-light.svg" width="100%" />
</picture>

<table>
<tr><td valign="top" width="50%">

### 🔬 [Talus](https://github.com/BartoszOsiej/talus-process-monitor)

eBPF endpoint security agent — kernel-level `execve`/`openat`/`connect` tracing through Aya, per-CPU perf buffers, sliding-window alerting, automated `SIGKILL` response, full FrankenTUI.

`Rust` `Aya` `FrankenTUI` `eBPF`

[![crates.io](https://img.shields.io/crates/v/process-monitor?style=flat-square&logo=rust)](https://crates.io/crates/process-monitor) [![GHCR](https://img.shields.io/badge/GHCR-image-2496ED?style=flat-square&logo=docker)](https://github.com/BartoszOsiej/talus-process-monitor/pkgs/container/talus-process-monitor) [![binary](https://img.shields.io/badge/release-binary-8A2BE2?style=flat-square)](https://github.com/BartoszOsiej/talus-process-monitor/releases)

</td><td valign="top" width="50%">

### 🧬 [TrustNode](https://github.com/BartoszOsiej/trustnode) — *a validator, from scratch*

Solana-like validator built in Rust: proof-of-history clock with **real sequential PoH verification**, Tower BFT fork choice, Sealevel-style parallel execution, Turbine erasure coding, CRDS gossip and JSON-RPC. **228-test suite**, MIT.

`Rust` `Consensus` `PoH` `Sealevel` `Turbine`

[![CI](https://img.shields.io/github/actions/workflow/status/BartoszOsiej/trustnode/ci.yml?branch=master&style=flat-square&logo=githubactions&label=ci)](https://github.com/BartoszOsiej/trustnode/actions) [![tests](https://img.shields.io/badge/tests-228-brightgreen?style=flat-square)](https://github.com/BartoszOsiej/trustnode) [![license](https://img.shields.io/badge/license-MIT-green?style=flat-square)](https://github.com/BartoszOsiej/trustnode/blob/master/LICENSE)

</td></tr>
<tr><td valign="top" width="50%">

### 🎮 [NV2_ENGINE](https://github.com/BartoszOsiej/NV2_ENGINE) — *VIVIA*

Voxel survival engine with NASA POWER real-climate worlds and an embedded MeMLP neural network. EGS submission kit ready — published as `nv2_engine` on crates.io.

**▶ [Landing page](https://bartoszosiej.github.io/NV2_ENGINE/)**

`Rust` `wgpu` `MeMLP` `NASA-climate`

[![crates.io](https://img.shields.io/crates/v/nv2_engine?style=flat-square&logo=rust)](https://crates.io/crates/nv2_engine) [![GHCR](https://img.shields.io/badge/GHCR-image-2496ED?style=flat-square&logo=docker)](https://github.com/BartoszOsiej/NV2_ENGINE/pkgs/container/nv2_engine) [![binary](https://img.shields.io/badge/release-binary-8A2BE2?style=flat-square)](https://github.com/BartoszOsiej/NV2_ENGINE/releases)

</td><td valign="top" width="50%">

### ⚡ [externum](https://github.com/BartoszOsiej/externum)

Programming language built from scratch — compiles to Python, Bash and native binary. Ownership, traits, macros. **382-test suite**, on PyPI since v2.

**▶ [Run it in your browser — and extend the language live](https://hartwell-labs.pl/externum/)**

`Python` `Compiler design` `PyPI`

[![PyPI](https://img.shields.io/pypi/v/externum?style=flat-square&logo=pypi)](https://pypi.org/project/externum/) [![GHCR](https://img.shields.io/badge/GHCR-image-2496ED?style=flat-square&logo=docker)](https://github.com/BartoszOsiej/externum/pkgs/container/externum) [![Playground](https://img.shields.io/badge/▶_LIVE_PLAYGROUND-extend_it_in_browser-a371f7?style=flat-square)](https://hartwell-labs.pl/externum/)

</td></tr>
<tr><td valign="top" width="50%">

### 🔒 [CyberForge](https://github.com/BartoszOsiej/CyberForge)

Four security tools as one workspace — port scanner, web scanner, hash cracker, packet analyzer. Each shipped separately on crates.io.

`Rust` `Tokio` `libpcap`

[![crates.io](https://img.shields.io/crates/v/netrecon?style=flat-square&label=netrecon&logo=rust)](https://crates.io/crates/netrecon) [![crates.io](https://img.shields.io/crates/v/shadowscan?style=flat-square&label=shadowscan&logo=rust)](https://crates.io/crates/shadowscan) [![crates.io](https://img.shields.io/crates/v/hashsleuth?style=flat-square&label=hashsleuth&logo=rust)](https://crates.io/crates/hashsleuth) [![crates.io](https://img.shields.io/crates/v/packeteye?style=flat-square&label=packeteye&logo=rust)](https://crates.io/crates/packeteye)

</td><td valign="top" width="50%">

### 🛡️ [QuantumShield](https://github.com/BartoszOsiej/pqguard)

Post-quantum file encryption CLI — ML-KEM-768 key exchange + AES-256-GCM + HKDF. NIST FIPS 203 compliant, fuzz-tested.

**▶ [Landing page](https://hartwell-labs.pl/quantum-shield/)**

`Rust` `Cryptography` `NIST`

[![crates.io](https://img.shields.io/crates/v/pqguard?style=flat-square&logo=rust)](https://crates.io/crates/pqguard) [![CI](https://img.shields.io/github/actions/workflow/status/BartoszOsiej/pqguard/ci.yml?branch=main&style=flat-square&logo=githubactions&label=ci)](https://github.com/BartoszOsiej/pqguard/actions) [![GHCR](https://img.shields.io/badge/GHCR-image-2496ED?style=flat-square&logo=docker)](https://github.com/BartoszOsiej/pqguard/pkgs/container/pqguard)

</td></tr>
<tr><td valign="top" width="50%">

### 🪙 [pqbit](https://github.com/BartoszOsiej/pqbit)

**Post-quantum Bitcoin from genesis** — fair-launch UTXO chain with *only* NIST PQ signatures (ML-DSA-44 / SLH-DSA, FIPS 204/205), no ECDSA ever. Gossiping p2p network, PQ-validated mempool, continuous mining. Genesis parameters in public review; grant application filed (NGI Zero / NLnet, decision Nov 2026).

**▶ [Landing](https://bartoszosiej.github.io/pqbit/)** · **▶ [GENESIS.md — open review](https://github.com/BartoszOsiej/pqbit/blob/master/GENESIS.md)**

`Rust` `Post-quantum` `Bitcoin research` `p2p`

[![CI](https://img.shields.io/github/actions/workflow/status/BartoszOsiej/pqbit/ci.yml?branch=master&style=flat-square&logo=githubactions&label=ci)](https://github.com/BartoszOsiej/pqbit/actions) [![tests](https://img.shields.io/badge/tests-23%2F23-brightgreen?style=flat-square)](https://github.com/BartoszOsiej/pqbit) [![landing](https://img.shields.io/badge/▶_LANDING-live-8A2BE2?style=flat-square)](https://bartoszosiej.github.io/pqbit/)

</td><td valign="top" width="50%">

### 📚 [Docs](https://bartoszosiej.github.io/Docs/)

Technical documentation site — architecture guides, API reference, deployment playbooks, and the product field guides.

`TypeScript` `Deploy` `GitHub Pages`

[![npm](https://img.shields.io/npm/v/bartosz-osiej-docs?style=flat-square&logo=nodedotjs)](https://www.npmjs.com/package/bartosz-osiej-docs) [![Deploy](https://img.shields.io/badge/Deploy-live-green?style=flat-square)](https://bartoszosiej.github.io/Docs/)

</td></tr>
</table>

---

## 📝 Technical Writing

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-light.svg" width="100%" />
</picture>

Publiczne artykuły o tym, jak działają rzeczy na niskim poziomie — z kodem, nie z marketingiem.

- **[Detecting ransomware with eBPF in Rust](https://bartoszosiej.github.io/content/ebpf-ransomware-everything)** *(2026-09-16)* — tutorial: tracepointy `execve`/`openat`, per-CPU perf buffers, sliding-window detection, automated SIGKILL. Kod źródłowy: talus-process-monitor.
- **[Catching ransomware with eBPF: what execve/openat tracing taught me about false positives](https://bartoszosiej.github.io/content/ebpf-ransomware-monitor-lessons)** *(2026-09-13)* — deep-dive: behavioral tracing, scoring without false positives, lessons from production-grade builds.

*Writing for: Draft.dev · Corellium · Honeybadger · Mattermost · Vultr · Semaphore · SigNoz · Edge Network.* → [wszystkie writing samples](https://bartoszosiej.github.io/writing/)

---

<details>
<summary><b>📦 More projects (click to expand)</b></summary>

| | Project | What it is | Try it |
|---|---------|-----------|--------|
| 🔐 | [**Fortis**](https://github.com/BartoszOsiej/riscv-trust) | Bare-metal RISC-V measured boot — SHA-256 + ML-KEM-768 chain of trust | QEMU |
| ◈ | [**Aurora**](https://github.com/BartoszOsiej/Aurora) | Complete OS in the browser — kernel, window manager, filesystem, 8 apps, procedural audio | [npm](https://www.npmjs.com/package/aurora-os) |
| 🌐 | [**Meshcore**](https://github.com/BartoszOsiej/Meshcore) | Serverless P2P chat — WebRTC + MQTT signaling, zero dependencies | [npm](https://www.npmjs.com/package/n2-mesh) |
| 🔗 | [**Shortlink**](https://github.com/BartoszOsiej/Shortlink) | URL shortener — JWT auth, click tracking, React dashboard | [PyPI](https://pypi.org/project/fastapi-url/) |
| 🎯 | [**Promptbox**](https://github.com/BartoszOsiej/Promptbox) | Remote prompt inbox for AI agents — mobile-first, zero backend | [npm](https://www.npmjs.com/package/prompt-inbox) |
| 🎮 | [**Forge**](https://github.com/BartoszOsiej/Factorio-web-game) | Factory builder playable in browser — own codebase inspired by Factorio, 50+ commits of original systems | [npm](https://www.npmjs.com/package/novactorio) |
| 📚 | [**TeleWiedza**](https://github.com/BartoszOsiej/TeleWiedza) | PL/EN telecom encyclopedia — networking, 5G, fiber, security | [docs](https://bartoszosiej.github.io/Docs/) |

</details>

---

## 📦 Distribution — everything ships, nothing rots

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-light.svg" width="100%" />
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/pipeline-dark.svg" />
  <img alt="Animated supply-chain flow — git tag to signed images and registries" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/pipeline-light.svg" width="100%" />
</picture>

```mermaid
flowchart LR
    T["git tag"] --> CI["GitHub Actions"]
    CI --> D["Docker multi-stage"]
    D --> G["GHCR: signed images"]
    CI --> B["cargo release build"]
    B --> R["Release + binaries"]
    CI --> P["Registry publish"]
    P --> C["crates.io: 7 crates"]
    P --> Y["PyPI: 2 packages"]
    P --> N["npm: 6 packages"]
```

<div align="center">

| 🐳 GHCR images | 🦀 crates.io | 🐍 PyPI | 🟢 npm | 📦 Public repos |
|:--------------:|:------------:|:-------:|:------:|:----------------------:|
| **signed & live** | **7** | **2** | **6** | **24 (21 own)** |

</div>

### 🕹️ Interactive — a recruiter can actually run this

| | |
|---|---|
| **▶ [Externum Playground](https://hartwell-labs.pl/externum/)** | The programming language running 100% in your browser (Pyodide). Write programs, hot-load your own modules into the live runtime, compile to Python/Bash/binary. Sessions shareable by URL. |
| **🧬 `/define`** | Comment on an issue → the bot validates your module against Externum's type checker → opens a PR into the stdlib → once merged, `import` works for everyone including the web playground. [The language evolves from comments.](https://github.com/BartoszOsiej/externum/issues/7) |
| **🎮 `/run`** | [Comment on cybersec-tools](https://github.com/BartoszOsiej/CyberForge/issues/10) → the bot builds the workspace in CI and executes the real binaries with sandboxed guardrails, posting output back. |
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

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-light.svg" width="100%" />
</picture>

*The same pipeline discipline big tech uses — cryptographically verifiable, not "trust me".*

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](https://github.com/BartoszOsiej/BartoszOsiej/blob/main/LICENSE)

</div>

| Layer | What it means |
|---|---|
| **cosign keyless signing** | Every GHCR image is signed via Sigstore/Fulcio OIDC — no keys to leak, identity bound to the GitHub workflow |
| **SLSA v1 provenance** | Every release binary carries a build attestation proving *which commit, which runner, which pipeline* produced it |
| **SPDX SBOM** | Every release ships a machine-readable software bill of materials |

Verify it yourself — no trust required:

```bash
# verify a container image signature
cosign verify ghcr.io/bartoszosiej/cybersec-tools \
  --certificate-identity-regexp "^https://github.com/BartoszOsiej/" \
  --certificate-oidc-issuer https://token.actions.githubusercontent.com

# verify binary build provenance
gh attestation verify netrecon-x86_64-unknown-linux-gnu \
  -R BartoszOsiej/CyberForge
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

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-light.svg" width="100%" />
</picture>

> [!NOTE]
> Every repository runs the same production-grade pipeline — this is how I work, not how I pretend to work.

| Practice | Coverage |
|----------|:--------:|
| CodeQL security scanning | ✅ every active repo |
| Dependabot + vulnerability alerts | ✅ every active repo |
| Branch protection + squash-merge history | ✅ every active repo |
| Public sprint boards + milestones | ✅ 6 boards |
| Discussions, CONTRIBUTING, SECURITY, CoC | ✅ every active repo |
| MIT licensing, topics, descriptions | ✅ every active repo |

---

## 📊 Live Package Metrics

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-light.svg" width="100%" />
</picture>

*Self-hosted stats engine — a scheduled workflow queries npm / PyPI / crates.io /
GitHub releases and renders these cards from scratch. No badge services, no
third-party renderers: every pixel comes from my own pipeline.*

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/dashboard-dark.svg" />
  <img alt="Live ecosystem dashboard — downloads, views, stars and CI status, refreshed every 6h" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/dashboard-light.svg" width="100%" />
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/metrics-dark.svg" />
  <img src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/metrics-light.svg" />
</picture>

### 🏆 Trophy case

*Hand-forged achievements. GitHub does not issue these and none of them are embeddable — every medal below is an animated SVG minted by my own pipeline, refreshed on a schedule.*

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/achievements-dark.svg" />
  <img alt="Custom animated trophy case" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/achievements-light.svg" width="100%" />
</picture>

---

## 📈 GitHub Stats

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-light.svg" width="100%" />
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/stats-dark.svg" />
  <img alt="Profile stats — self-hosted" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/stats-light.svg" width="49%" />
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/langs-dark.svg" />
  <img alt="Top languages — self-hosted" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/langs-light.svg" width="49%" />
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/streak-dark.svg" />
  <img alt="Streak stats — self-hosted" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/streak-light.svg" width="100%" />
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/heatmap-dark.svg" />
  <img alt="Contribution heatmap — self-hosted" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/heatmap-light.svg" width="100%" />
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/stars-dark.svg" />
  <img alt="Star history — self-tracked" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/stars-light.svg" width="100%" />
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/profile-3d/profile-night-rainbow.svg" />
  <img alt="3D contribution graph" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/profile-3d/profile-season-animate.svg" width="100%" />
</picture>

---

## 🗺️ Timeline

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-light.svg" width="100%" />
</picture>

```
2021 ──► first lines of code — Java, CryEngine, Minecraft mechanics (@ghost0development)
2025 ──► networking & security track (teleinformatyka)
2026 Q1 ──► Rust deep dive: voxel engine, eBPF kernel probes, compiler from scratch
2026 Q2 ──► production CI/CD: Actions → GHCR → crates.io / PyPI / npm, 14 packages live
2026 Q3 ──► ecosystem upgrade: aya 0.14, ureq 3, ml-kem 0.3, dashmap 6, RISC-V bare-metal (Fortis)
2026 Q4 ──► upstream PRs to aya-rs merged, first paid role 🎯
```

---

## 🤝 Upstream Contributions

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-light.svg" width="100%" />
</picture>

| Target | PR type | Status |
|--------|---------|--------|
| [aya-rs/book](https://github.com/aya-rs/book) | Fix outdated `offset_of!` tip in Parsing Packets page (issue #202) | [PR open](https://github.com/aya-rs/book/pulls?q=is%3Apr+author%3ABartoszOsiej) |
| [aya-rs/book](https://github.com/aya-rs/book) | Add typos spellcheck CI (issue #91) | [PR open](https://github.com/aya-rs/book/pulls?q=is%3Apr+author%3ABartoszOsiej) |
| [aya-rs/book](https://github.com/aya-rs/book) | Update deprecated `aya::Bpf` references + MAP API note (issue #73) | [PR open](https://github.com/aya-rs/book/pulls?q=is%3Apr+author%3ABartoszOsiej) |

> All PRs based on real-world experience upgrading talus-process-monitor to aya 0.14.

---

## ✍️ Guestbook

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-light.svg" width="100%" />
</picture>

*No giscus, no Disqus, no third-party embed — GitHub strips `<script>` from READMEs anyway. A signature is just a GitHub **issue** labelled `guestbook`, rendered into the wall below by my own pipeline. Say hi.*

[![Sign the guestbook](https://img.shields.io/badge/✍_Sign_the_guestbook-open_an_issue-a371f7?style=for-the-badge)](https://github.com/BartoszOsiej/BartoszOsiej/issues/new?labels=guestbook&title=Guestbook+entry)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/guestbook-dark.svg" />
  <img alt="Guestbook wall — rendered from GitHub issues" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/guestbook-light.svg" width="100%" />
</picture>

---

## 🕹️ Flex zone

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-light.svg" width="100%" />
</picture>

<table><tr><td width="248" valign="middle">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/clock-dark.svg" />
  <img alt="Live clock — pure SMIL" width="220" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/clock-light.svg" />
</picture>

</td><td valign="middle">

*A live clock, an idle screensaver, digital rain — all ticking in your browser with **zero JavaScript**.*

GitHub strips `<script>`, blocks `<iframe>`, and renders none of this natively. Everything you see here is hand-written **SMIL** animation inside SVG files served from my own repo. The clock's hands actually rotate; the box actually bounces; the matrix actually falls. View source — there isn't a single line of JS.

</td></tr></table>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/bounce-dark.svg" />
  <img alt="Bouncing logo screensaver" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/bounce-light.svg" width="100%" />
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/matrix-dark.svg" />
  <img alt="Digital rain" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/matrix-light.svg" width="100%" />
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/equalizer-dark.svg" />
  <img alt="Audio spectrum analyzer" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/equalizer-light.svg" width="100%" />
</picture>

<table><tr><td width="248" valign="middle">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/radar-dark.svg" />
  <img alt="Radar sweep" width="220" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/radar-light.svg" />
</picture>

</td><td valign="middle">

*Even the arcade keeps shipping: a radar sweep, a spectrum analyzer, and Conway's Game of Life. Every frame is computed in Python, frozen into SMIL, and animated by your browser — no JS, no GIF, no video.*

</td></tr></table>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/life-dark.svg" />
  <img alt="Conway's Game of Life" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/life-light.svg" width="100%" />
</picture>

---

## 🌐 Also here

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/rule-light.svg" width="100%" />
</picture>

- **[`ghost0development`](https://github.com/ghost0development)** — my original account, building since **Feb 2021**: 32 repos of early experiments, game prototypes and the original `halcyon-process-monitor` (ancestor of Talus). Everything archived there is preserved as history — active development happens on this account.

<details>
<summary><b>🗂️ Where the ideas came from (archive → production)</b></summary>

| Archive — @ghost0development (2021–2025) | Production — @BartoszOsiej (2026–) |
|---|---|
| `halcyon-process-monitor` — first eBPF probe | [Talus](https://github.com/BartoszOsiej/talus-process-monitor) — eBPF endpoint security, on crates.io |
| `NV-2.0` / `NV2_ENGINE` — voxel prototypes | [NV2_ENGINE](https://github.com/BartoszOsiej/NV2_ENGINE) — VIVIA engine, on crates.io |
| `Factorio-web-game` / `Factorio-pt` — game experiments | [Forge](https://github.com/BartoszOsiej/Factorio-web-game) — factory builder on npm |
| `FastAPI-url` — first FastAPI service | [Shortlink](https://github.com/BartoszOsiej/Shortlink) — on PyPI as `fastapi-url` |

</details>

---

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/divider-dark.svg" />
  <img alt="" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/divider-light.svg" width="100%" />
</picture>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/views-dark.svg">
  <img alt="Ecosystem views" src="https://raw.githubusercontent.com/BartoszOsiej/BartoszOsiej/stats/svg/views-light.svg">
</picture>

*Open to work — [`mmc29213@gmail.com`](mailto:mmc29213@gmail.com)*

**PRODUCTS** — [Talus Enterprise Pack · $50](https://buy.polar.sh/polar_cl_E577BTilme4dnUFsfbG0aE4qo7QILaugmEjsA0oajKK) (eBPF ransomware EDR: deployment guide + support) · [Externum Pro Pack · $29](https://buy.polar.sh/polar_cl_qR2GOfEhXRqlTlPICwyo8XVqKkXjv4mj15cq926Dh1F) (production guide for the language) · [Support Session · $150](https://polar.sh/checkout/polar_c_rGI15C7IzCs54qElT4NJ5aLj7o3p7Uxdj4P4T1OtUsU) (60-min deploy call + written config) — code always MIT & free

</div>
