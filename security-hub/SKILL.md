---
name: security-hub
description: >-
  Unified security skill router combining the defensive/breadth library
  (cybersecurity-kb: 754 skills, ATT&CK/NIST/ATLAS/AI-RMF mapped) and the
  offensive/depth library (hack-skills: 102 skills, bug-bounty / CTF /
  authorized pentest). Route any security task — defensive, compliance, DFIR,
  OR offensive web/API/AD/Pwn testing — to the correct sub-skill. Only for
  authorized targets and legitimate research.
---

# Security Hub — 蓝 + 红 统一安全技能路由

## Overview

本入口把两套互补的安全技能库合并为一套可调度能力：

- **cybersecurity-kb（防御广度）** — 754 个技能，覆盖 45+ 细分领域，全部映射到
  MITRE ATT&CK / NIST CSF 2.0 / ATLAS / AI RMF。擅长威胁狩猎、数字取证、事件响应、
  合规审计、蓝队建设。每个技能含 `references/` 与可执行的 `scripts/agent.py`。
- **hack-skills（进攻深度）** — 102 个技能（1 主入口 `hack` + 6 分类路由 + 95 深度主题），
  来源长亭/yaklang（MIT, VillanCh）。擅长漏洞赏金、CTF、授权渗透：Web/API/Auth/AD/
  Pwn/逆向/密码学/区块链/AI 安全。设计取向是补大模型易漏的边界条件、解析差异、CVE 链。

## Trust Model（信任边界）

- 仅限 **授权目标、合法研究、防御验证、赏金规则内** 使用。
- 禁止用于任何未授权攻击。hack-skills 的进攻内容须严格约束在授权范围。
- 两套库各自的 LICENSE 均保留：cybersecurity-kb → Apache-2.0；hack-skills → MIT (yaklang/VillanCh)。

## Route by intent（按意图路由）

| 意图 | 路由到 |
|---|---|
| 威胁狩猎 / 取证 / 事件响应 / 合规 | `cybersecurity-kb` → 详见 `cybersecurity-kb/SKILLS_INDEX.md` |
| 云安全（AWS/Azure/GCP/K8s 审计） | `cybersecurity-kb` → cloud-security / container-security |
| 恶意代码 / Android / iOS 分析 | `cybersecurity-kb` → malware-analysis |
| Web / API 漏洞利用、赏金、CTF | `hack` → `api-sec` / `injection-checking` / `file-access-vuln` / `business-logic-vuln` |
| 认证与授权（OAuth/JWT/SAML/IDOR） | `hack` → `auth-sec` / `jwt-oauth-token-attacks` / `oauth-oidc-misconfiguration` |
| 提权 / Linux / Windows / AD | `hack` → `linux-privilege-escalation` / `windows-privilege-escalation` / `active-directory-kerberos-attacks` |
| 逆向 / 二进制 / Pwn | `hack` → `vm-and-bytecode-reverse` / `heap-exploitation` / `stack-overflow-and-rop` |
| 密码学 / 区块链 / AI 安全 | `hack` → `rsa-attack-techniques` / `smart-contract-vulnerabilities` / `llm-prompt-injection` |
| 侦察与方法论（先从哪下手） | `hack` → `recon-for-sec` |

## How to load

- **防御任务**：`Skill: cybersecurity-kb`，再用其 `SKILLS_INDEX.md` 按领域下钻。
- **进攻任务**：`Skill: hack`（主路由），由其路由到 6 个分类与 95 个深度主题。
- **直接调用**：856 个子技能均可用文件夹名直接调用，例如
  `analyzing-android-malware-with-apktool`（防御）、`ssrf-server-side-request-forgery`（进攻）。
- **合并索引**：见 `security-hub/SECURITY_HUB_INDEX.md`（领域分布 + 分类路由 + 主题清单 + 速查表）。

## Attribution & License

- cybersecurity-kb: Apache-2.0 — `mukul975/Anthropic-Cybersecurity-Skills`，改进 fork `ctkqiang/CybersecuritySkills`。
- hack-skills: MIT — `yaklang/hack-skills`（fork `strivepan-svg/hack-skills`），Copyright (c) 2026 VillanCh。
