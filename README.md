<div align="center">

# Bartosz Osiej

**Independent Systems Developer — Rust / eBPF / Linux Internals**
I build low-level tooling that userspace devs are afraid of.

<a href="https://www.rust-lang.org/"><img alt="Rust" src="https://img.shields.io/badge/Rust-%23000000.svg?style=for-the-badge&logo=rust&logoColor=white"/></a>
<a href="https://ebpf.io/"><img alt="eBPF" src="https://img.shields.io/badge/eBPF-%23000000.svg?style=for-the-badge&logo=linux&logoColor=white"/></a>
<a href="https://www.kernel.org/"><img alt="Linux Kernel" src="https://img.shields.io/badge/Linux%20Kernel-%23FCC624.svg?style=for-the-badge&logo=linux&logoColor=black"/></a>
<a href="https://wgpu.rs/"><img alt="wgpu" src="https://img.shields.io/badge/wgpu-%237B6EF0.svg?style=for-the-badge&logo=nvidia&logoColor=white"/></a>
<a href="https://github.com/features/actions"><img alt="GitHub Actions" src="https://img.shields.io/badge/GitHub%20Actions-%232088FF.svg?style=for-the-badge&logo=githubactions&logoColor=white"/></a>

</div>

---

## Selected work

| Project | What it is | Stack |
|---|---|---|
| [**halcyon-process-monitor**](https://github.com/BartoszOsiej/halcyon-process-monitor) | Real-time eBPF ransomware behavior tracker — `execve`/`openat` tracepoints, per-CPU perf buffers, CO-RE/BTF, sliding-window heuristic | Rust · Aya · ratatui |
| [**NV2_ENGINE**](https://github.com/BartoszOsiej/NV2_ENGINE) | Voxel engine with an embedded MLP neural network, multiplayer, EGS build | Rust · wgpu · TCP |
| [**externum**](https://github.com/BartoszOsiej/externum) | Programming language written from scratch — compiles to Python, Bash, binary. 118-test suite | Rust · WASM |
| [**cybersec-tools**](https://github.com/BartoszOsiej/cybersec-tools) | Security suite: `netrecon`, `shadowscan`, `hashsleuth`, `packeteye` | Rust |
| [**n2-mesh**](https://github.com/BartoszOsiej/n2-mesh) | P2P mesh networking | Rust |
| [**AURORA-OS**](https://github.com/BartoszOsiej/AURORA-OS) | Operating system project | Rust |

## Timeline

```
2021    started programming — Java, Cry Engine, Minecraft mechanics
2026 Q1  deep-dive: Rust everywhere — voxel engine, eBPF kernel telemetry,
         compiler written from scratch
2026 Q3  production CI/CD on GitHub Actions — deploy, test, Windows matrix
     8 Docker images on GHCR · code scanning (CodeQL) · Dependabot · milestones
```

## Live infrastructure

Every active project ships as a **container image, a release, and a sprint board**:

| Project | GHCR image | Releases | Sprint board | CI | Security |
|---|---|---|---|---|---|
| halcyon-process-monitor | [ghcr.io/bartoszosiej/halcyon-process-monitor][gh-halcyon] | [releases][rel-halcyon] | [board #2][pb-halcyon] | [actions][ci-halcyon] | [CodeQL][cq-halcyon] |
| externum | [ghcr.io/bartoszosiej/externum][gh-externum] | [releases][rel-externum] | [board #3][pb-externum] | [actions][ci-externum] | [CodeQL][cq-externum] |
| cybersec-tools | [ghcr.io/bartoszosiej/cybersec-tools][gh-cyber] | [releases][rel-cyber] | [board #4][pb-cyber] | [actions][ci-cyber] | [CodeQL][cq-cyber] |
| FastAPI-url | [ghcr.io/bartoszosiej/fastapi-url][gh-fastapi] | [releases][rel-fastapi] | [board #5][pb-fastapi] | [actions][ci-fastapi] | [CodeQL][cq-fastapi] |
| NV2_ENGINE | [ghcr.io/bartoszosiej/nv2_engine][gh-nv2] | [releases][rel-nv2] | [board #6][pb-nv2] | [actions][ci-nv2] | [CodeQL][cq-nv2] |
| n2-mesh · AURORA-OS · Portfolio · Docs · Factorio-web-game · prompt-inbox | [ghcr.io/bartoszosiej/*][gh-repos] | [releases][rel-repos] | — | [actions][ci-repos] | [CodeQL][cq-repos] |

[gh-halcyon]: https://github.com/BartoszOsiej/halcyon-process-monitor/pkgs/container/halcyon-process-monitor
[gh-externum]: https://github.com/BartoszOsiej/externum/pkgs/container/externum
[gh-cyber]: https://github.com/BartoszOsiej/cybersec-tools/pkgs/container/cybersec-tools
[gh-fastapi]: https://github.com/BartoszOsiej/FastAPI-url/pkgs/container/fastapi-url
[gh-nv2]: https://github.com/BartoszOsiej/NV2_ENGINE/pkgs/container/nv2_engine
[gh-repos]: https://github.com/users/BartoszOsiej/packages
[rel-halcyon]: https://github.com/BartoszOsiej/halcyon-process-monitor/releases
[rel-externum]: https://github.com/BartoszOsiej/externum/releases
[rel-cyber]: https://github.com/BartoszOsiej/cybersec-tools/releases
[rel-fastapi]: https://github.com/BartoszOsiej/FastAPI-url/releases
[rel-nv2]: https://github.com/BartoszOsiej/NV2_ENGINE/releases
[rel-repos]: https://github.com/users/BartoszOsiej/repositories
[pb-halcyon]: https://github.com/users/BartoszOsiej/projects/2
[pb-externum]: https://github.com/users/BartoszOsiej/projects/3
[pb-cyber]: https://github.com/users/BartoszOsiej/projects/4
[pb-fastapi]: https://github.com/users/BartoszOsiej/projects/5
[pb-nv2]: https://github.com/users/BartoszOsiej/projects/6
[ci-halcyon]: https://github.com/BartoszOsiej/halcyon-process-monitor/actions
[ci-externum]: https://github.com/BartoszOsiej/externum/actions
[ci-cyber]: https://github.com/BartoszOsiej/cybersec-tools/actions
[ci-fastapi]: https://github.com/BartoszOsiej/FastAPI-url/actions
[ci-nv2]: https://github.com/BartoszOsiej/NV2_ENGINE/actions
[ci-repos]: https://github.com/BartoszOsiej/repositories
[cq-halcyon]: https://github.com/BartoszOsiej/halcyon-process-monitor/security/code-scanning
[cq-externum]: https://github.com/BartoszOsiej/externum/security/code-scanning
[cq-cyber]: https://github.com/BartoszOsiej/cybersec-tools/security/code-scanning
[cq-fastapi]: https://github.com/BartoszOsiej/FastAPI-url/security/code-scanning
[cq-nv2]: https://github.com/BartoszOsiej/NV2_ENGINE/security/code-scanning
[cq-repos]: https://github.com/users/BartoszOsiej/settings/security_analysis

## Pipeline

[`n2-mesh` `.github/workflows/deploy.yml`](https://github.com/BartoszOsiej/n2-mesh/blob/main/.github/workflows/deploy.yml) · [`Portfolio` auto-deploy](https://github.com/BartoszOsiej/Portfolio) · [`FastAPI-url` `ci.yml`](https://github.com/BartoszOsiej/FastAPI-url) · [`NV2_ENGINE` Windows matrix](https://github.com/BartoszOsiej/NV2_ENGINE) · [`build-release`](https://github.com/users/BartoszOsiej/repositories) · [`publish-ghcr`](https://github.com/users/BartoszOsiej/packages)

## Accounts

- **`BartoszOsiej`** *(this profile)* — curated project snapshots
- **[`ghost0development`](https://github.com/ghost0development)** — archive since 2021 (31 repos); canonical `halcyon-process-monitor` and the VIVIA engine

## Contact

[<img alt="Portfolio" src="https://img.shields.io/badge/Portfolio-%23111.svg?style=for-the-badge&logo=firefox&logoColor=white"/>](https://bartoszosiej.github.io/Portfolio)
[<img alt="Email" src="https://img.shields.io/badge/mmc29213@gmail.com-%23EA4335.svg?style=for-the-badge&logo=gmail&logoColor=white"/>](mailto:mmc29213@gmail.com)