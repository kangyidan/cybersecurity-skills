<div align="center">

# CybersecuritySkills

### The largest open-source cybersecurity skills library for AI agents — fully tested

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-754-brightgreen?style=flat-square)](#whats-inside)
[![Frameworks](https://img.shields.io/badge/frameworks-5-orange?style=flat-square)](#framework-coverage)
[![Domains](https://img.shields.io/badge/domains-26-9cf?style=flat-square)](#whats-inside)
[![Tests](https://img.shields.io/badge/tests-12828%20passing-success?style=flat-square)](tests/)
[![Platforms](https://img.shields.io/badge/platforms-26%2B-blueviolet?style=flat-square)](#compatible-platforms)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![Hermes Agent](https://img.shields.io/badge/Hermes_Agent-compatible-blueviolet?style=flat)](https://github.com/NousResearch/hermes-agent)
[![agentskills.io](https://img.shields.io/badge/standard-agentskills.io-ff6600?style=flat-square)](https://agentskills.io)

**754 production-grade cybersecurity skills · 26 security domains · 5 framework mappings · 26+ AI platforms · 12,828 tests passing**

[Get Started](#quick-start) · [What's Inside](#whats-inside) · [Frameworks](#framework-coverage) · [Testing](#testing) · [Contributing](#contributing)

</div>

---

> **Fork notice** — This is a community fork of [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) by Mahipal Jangra (mukul975), released under the same Apache 2.0 license. Not affiliated with Anthropic PBC.
>
> **What's improved in this fork:**
> - All 90 generic "When to Use" sections replaced with specific, contextual triggers
> - ATLAS/D3FEND/AI RMF mappings extended (83%/86%/83% skill coverage, up from 11/18/11%)
> - All 753 `agent.py` scripts upgraded to use `argparse` (no more raw `sys.argv`)
> - Zero hardcoded credentials — env var references throughout
> - 12,828 automated tests covering structure, frontmatter, syntax, and security
> - Proper atomic git history with commits organized by domain

## Give any AI agent the security skills of a senior analyst

A junior analyst knows which Volatility3 plugin to run on a suspicious memory dump, which Sigma rules catch Kerberoasting, and how to scope a cloud breach across three providers. **Your AI agent doesn't — unless you give it these skills.**

This repo contains **754 structured cybersecurity skills** spanning **26 security domains**, each following the [agentskills.io](https://agentskills.io) standard. Every skill is mapped to industry frameworks and includes a working Python agent script, step-by-step procedures, and agent-optimized discovery metadata.

## Quick Start

```bash
# Option 1: npx (recommended for Claude Code / agentskills.io platforms)
npx skills add Razor25000/CybersecuritySkills

# Option 2: Git clone
git clone https://github.com/Razor25000/CybersecuritySkills.git
cd CybersecuritySkills

# Option 3: Direct install on VPS / Hermes Agent
git clone --depth=1 https://github.com/Razor25000/CybersecuritySkills.git ~/skills/cybersec
```

Works immediately with Claude Code, Hermes Agent, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI, and any [agentskills.io](https://agentskills.io)-compatible platform.

## Framework Coverage

| Framework | Version | Coverage in this repo | Skill coverage |
|---|---|---|---|
| [MITRE ATT&CK](https://attack.mitre.org) | v19.1 | 15 tactics · 286 techniques | 754/754 skills (100%) |
| [NIST CSF 2.0](https://www.nist.gov/cyberframework) | 2.0 | 6 functions · 22 categories | 754/754 skills (100%) |
| [MITRE ATLAS](https://atlas.mitre.org) | v5.4 | 16 tactics · 84 techniques | 624/754 skills (83%) |
| [MITRE D3FEND](https://d3fend.mitre.org) | v1.3 | 7 categories · 267 techniques | 649/754 skills (86%) |
| [NIST AI RMF](https://airc.nist.gov/AI_RMF) | 1.0 | 4 functions · 72 subcategories | 626/754 skills (83%) |

> **Note on ATLAS/D3FEND/AI RMF coverage:** Mappings are derived from ATT&CK technique correlations. Skills whose ATT&CK techniques don't have established ATLAS/D3FEND/AI RMF mappings in the published literature are not mapped — coverage is accurate, not inflated.

**Example — a single skill mapped across frameworks:**

| Skill | ATT&CK | NIST CSF | ATLAS | D3FEND | AI RMF |
|---|---|---|---|---|---|
| `analyzing-network-traffic-of-malware` | T1071 | DE.CM | AML.T0040 | D3-NTA | MEASURE-2.6 |

## What's Inside

**26 security domains, 754 skills:**

| Domain | Skills | Key capabilities |
|---|---|---|
| Cloud Security | 60 | AWS, Azure, GCP hardening · CSPM · cloud forensics |
| Threat Hunting | 55 | Hypothesis-driven hunts · LOTL detection · behavioral analytics |
| Threat Intelligence | 50 | STIX/TAXII · MISP · feed integration · actor profiling |
| Web Application Security | 42 | OWASP Top 10 · SQLi · XSS · SSRF · deserialization |
| Network Security | 40 | IDS/IPS · firewall rules · VLAN segmentation · traffic analysis |
| Malware Analysis | 39 | Static/dynamic analysis · reverse engineering · sandboxing |
| Digital Forensics | 37 | Disk imaging · memory forensics · timeline reconstruction |
| Security Operations | 36 | SIEM correlation · log analysis · alert triage |
| Identity & Access Management | 35 | IAM policies · PAM · zero trust identity · Okta · SailPoint |
| SOC Operations | 33 | Playbooks · escalation workflows · metrics · tabletop exercises |
| Container Security | 30 | K8s RBAC · image scanning · Falco · container forensics |
| OT/ICS Security | 28 | Modbus · DNP3 · IEC 62443 · historian defense · SCADA |
| API Security | 28 | GraphQL · REST · OWASP API Top 10 · WAF bypass |
| Vulnerability Management | 25 | Nessus · scanning workflows · patch prioritization · CVSS |
| Incident Response | 25 | Breach containment · ransomware response · IR playbooks |
| Red Teaming | 24 | Full-scope engagements · AD attacks · phishing simulation |
| Penetration Testing | 23 | Network · web · cloud · mobile · wireless pentesting |
| Endpoint Security | 17 | EDR · LOTL detection · fileless malware · persistence hunting |
| DevSecOps | 17 | CI/CD security · code signing · Terraform auditing |
| Phishing Defense | 16 | Email authentication · BEC detection · phishing IR |
| Cryptography | 14 | TLS · Ed25519 · certificate transparency · key management |
| Zero Trust Architecture | 13 | BeyondCorp · CISA maturity model · microsegmentation |
| Mobile Security | 12 | Android/iOS analysis · mobile pentesting · MDM forensics |
| Ransomware Defense | 7 | Precursor detection · response · recovery · encryption analysis |
| Compliance & Governance | 5 | CIS benchmarks · SOC 2 · regulatory frameworks |
| Deception Technology | 2 | Honeytokens · breach detection canaries |

## Skill Anatomy

Every skill follows a consistent, agent-optimized structure:

```
skills/performing-memory-forensics-with-volatility3/
├── SKILL.md              ← YAML frontmatter + structured Markdown workflow
├── references/
│   └── api-reference.md  ← Tool commands, API calls, technical reference
└── scripts/
    └── agent.py          ← Working Python agent script with argparse CLI
```

**YAML frontmatter (example):**

```yaml
---
name: performing-memory-forensics-with-volatility3
description: Analyze memory dumps to extract running processes, network connections,
  injected code, and malware artifacts using the Volatility3 framework.
domain: cybersecurity
subdomain: digital-forensics
tags: [forensics, memory-analysis, volatility3, incident-response, dfir]
atlas_techniques: [AML.T0047]
d3fend_techniques: [D3-MA, D3-PSMD]
nist_ai_rmf: [MEASURE-2.6]
nist_csf: [DE.CM-01, RS.AN-03]
version: "1.2"
author: mahipal
license: Apache-2.0
---
```

**Markdown body sections:**

```markdown
## When to Use          ← Specific contextual triggers (not generic templates)
## Prerequisites        ← Required tools, access levels, environment
## Workflow             ← Step-by-step execution with real commands
## Verification         ← How to confirm successful execution
```

Each skill costs **~30 tokens to scan** (frontmatter only) and **500–2,000 tokens to fully load**. This progressive disclosure architecture lets agents search all 754 skills in a single pass without exceeding context windows.

## Testing

This fork includes a comprehensive test suite covering all 754 skills:

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run full test suite
pytest tests/ -v

# Run structure tests only (fast)
pytest tests/test_skill_structure.py -q

# Run script validation tests
pytest tests/test_scripts_importable.py -q
```

**Test coverage:**
- Frontmatter completeness and YAML validity (all 754 skills)
- Name format, description length, license compliance
- Required Markdown sections (`## When to Use`, `## Prerequisites`)
- No generic template text in "When to Use"
- ATT&CK technique ID format validation
- `agent.py` presence, syntax validity, argparse CLI, docstring
- No hardcoded credentials in any script
- `index.json` completeness and accuracy
- Framework coverage minimum thresholds (ATLAS/D3FEND/AI RMF ≥ 70%)

## Compatible Platforms

**AI code assistants**
Claude Code (Anthropic) · GitHub Copilot (Microsoft) · Cursor · Windsurf · Cline · Aider · Continue · Roo Code · Amazon Q Developer · Tabnine · Sourcegraph Cody · JetBrains AI

**CLI agents**
OpenAI Codex CLI · Gemini CLI (Google)

**Autonomous agents**
Hermes Agent (Nous Research) · Devin · Replit Agent · SWE-agent · OpenHands

**Agent frameworks & SDKs**
LangChain · CrewAI · AutoGen · Semantic Kernel · Haystack · Vercel AI SDK · Any MCP-compatible agent

## Contributing

**Add a new skill** — Domains like Deception Technology (2 skills) and Compliance & Governance (5 skills) need the most help. Follow the template in [CONTRIBUTING.md](CONTRIBUTING.md) and submit a PR. All PRs must pass the full test suite (`pytest tests/`).

**Improve existing skills** — Add framework mappings, refine workflows, update tool references, or improve `agent.py` scripts.

**Report issues** — Found an inaccurate procedure or broken script? [Open an issue](https://github.com/Razor25000/CybersecuritySkills/issues).

## License

This project is licensed under the [Apache License 2.0](LICENSE). Fork of [Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) by Mahipal Jangra (mukul975). Not affiliated with Anthropic PBC.

---

<div align="center">

**If this project helps your security work, consider giving it a ⭐**

[⭐ Star](https://github.com/Razor25000/CybersecuritySkills/stargazers) · [🍴 Fork](https://github.com/Razor25000/CybersecuritySkills/fork) · [📝 Contribute](CONTRIBUTING.md)

</div>
