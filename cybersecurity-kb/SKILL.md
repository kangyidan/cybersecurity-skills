---
name: cybersecurity-kb
description: 网络安全知识库入口 — 754 个结构化技能，覆盖 26 个安全领域，映射 MITRE ATT&CK / NIST CSF 2.0 / MITRE ATLAS / D3FEND / NIST AI RMF 五大框架。需要执行具体安全任务时，按领域调用对应子技能。
domain: meta
version: '1.0'
license: Apache-2.0
source: github.com/ctkqiang/CybersecuritySkills (fork of mukul975/Anthropic-Cybersecurity-Skills)
---

# Cybersecurity Knowledge Base (cybersecurity-kb)

本技能是 **754 个结构化网络安全技能** 的入口与索引。每个子技能都遵循 agentskills.io 标准，
包含可执行的方法论、工具指引、前置条件、步骤与验证，并映射到主流安全框架。

## 框架覆盖范围（共 754 个技能）
- MITRE ATT&CK：754/754
- NIST CSF 2.0：754/754
- MITRE ATLAS：624/754
- D3FEND：0/754
- NIST AI RMF：626/754

## 领域总览（45 个细分领域）
- **cloud-security**（63 个）：`analyzing-cloud-storage-access-patterns`、`analyzing-office365-audit-logs-for-compromise`、`auditing-aws-s3-bucket-permissions` 等
- **threat-hunting**（56 个）：`analyzing-persistence-mechanisms-in-linux`、`analyzing-powershell-empire-artifacts`、`analyzing-ransomware-network-indicators` 等
- **threat-intelligence**（50 个）：`analyzing-apt-group-with-mitre-navigator`、`analyzing-campaign-attribution-evidence`、`analyzing-certificate-transparency-for-phishing` 等
- **network-security**（43 个）：`analyzing-network-flow-data-with-netflow`、`analyzing-network-packets-with-scapy`、`analyzing-network-traffic-with-wireshark` 等
- **web-application-security**（42 个）：`bypassing-authentication-with-forced-browsing`、`exploiting-broken-link-hijacking`、`exploiting-http-request-smuggling` 等
- **malware-analysis**（39 个）：`analyzing-android-malware-with-apktool`、`analyzing-bootkit-and-rootkit-samples`、`analyzing-cobalt-strike-beacon-configuration` 等
- **digital-forensics**（37 个）：`acquiring-disk-image-with-dd-and-dcfldd`、`analyzing-browser-forensics-with-hindsight`、`analyzing-disk-image-with-autopsy` 等
- **soc-operations**（33 个）：`analyzing-dns-logs-for-exfiltration`、`analyzing-windows-event-logs-in-splunk`、`building-automated-malware-submission-pipeline` 等
- **identity-access-management**（33 个）：`building-identity-federation-with-saml-azure-ad`、`building-identity-governance-lifecycle-process`、`building-role-mining-for-rbac-optimization` 等
- **container-security**（29 个）：`analyzing-kubernetes-audit-logs`、`detecting-container-drift-at-runtime`、`detecting-container-escape-attempts` 等
- **security-operations**（28 个）：`analyzing-api-gateway-access-logs`、`analyzing-azure-activity-logs-for-threats`、`analyzing-memory-forensics-with-lime-and-volatility` 等
- **ot-ics-security**（28 个）：`detecting-anomalies-in-industrial-control-systems`、`detecting-attacks-on-historian-servers`、`detecting-attacks-on-scada-systems` 等
- **api-security**（28 个）：`detecting-api-enumeration-attacks`、`detecting-broken-object-property-level-authorization`、`detecting-shadow-api-endpoints` 等
- **incident-response**（26 个）：`analyzing-linux-audit-logs-for-intrusion`、`analyzing-network-traffic-for-incidents`、`analyzing-security-logs-with-splunk` 等
- **vulnerability-management**（25 个）：`building-patch-tuesday-response-process`、`building-vulnerability-aging-and-sla-tracking`、`building-vulnerability-dashboard-with-defectdojo` 等
- **red-teaming**（24 个）：`building-c2-infrastructure-with-sliver-framework`、`building-red-team-c2-infrastructure-with-havoc`、`conducting-domain-persistence-with-dcsync` 等
- **penetration-testing**（20 个）：`conducting-api-security-testing`、`conducting-external-reconnaissance-with-osint`、`conducting-internal-network-penetration-test` 等
- **devsecops**（17 个）：`building-devsecops-pipeline-with-gitlab-ci`、`implementing-aqua-security-for-container-scanning`、`implementing-code-signing-for-artifacts` 等
- **zero-trust-architecture**（17 个）：`configuring-aws-verified-access-for-ztna`、`configuring-identity-aware-proxy-with-google-iap`、`configuring-microsegmentation-for-zero-trust` 等
- **endpoint-security**（17 个）：`configuring-host-based-intrusion-detection`、`configuring-windows-defender-advanced-settings`、`configuring-windows-event-logging-for-detection` 等
- **phishing-defense**（15 个）：`analyzing-malicious-url-with-urlscan`、`building-phishing-reporting-button-workflow`、`detecting-business-email-compromise` 等
- **cryptography**（15 个）：`configuring-certificate-authority-with-openssl`、`configuring-hsm-for-key-storage`、`configuring-tls-1-3-for-secure-communications` 等
- **mobile-security**（13 个）：`analyzing-ios-app-security-with-objection`、`detecting-mobile-malware-behavior`、`exploiting-deeplink-vulnerabilities` 等
- **ransomware-defense**（13 个）：`analyzing-ransomware-payment-wallets`、`building-ransomware-playbook-with-cisa-framework`、`deploying-decoy-files-for-ransomware-detection` 等
- **threat-detection**（7 个）：`detecting-credential-dumping-techniques`、`detecting-golden-ticket-forgery`、`detecting-insider-threat-with-ueba` 等
- **application-security**（4 个）：`implementing-devsecops-security-scanning`、`implementing-runtime-application-self-protection`、`performing-fuzzing-with-aflplusplus` 等
- **compliance-governance**（4 个）：`implementing-gdpr-data-protection-controls`、`implementing-iso-27001-information-security-management`、`implementing-pci-dss-compliance-controls` 等
- **supply-chain-security**（3 个）：`analyzing-sbom-for-supply-chain-vulnerabilities`、`detecting-typosquatting-packages-in-npm-pypi`、`implementing-sigstore-for-software-signing` 等
- **deception-technology**（3 个）：`deploying-active-directory-honeytokens`、`implementing-deception-based-detection-with-canarytoken`、`implementing-network-deception-with-honeypots` 等
- **ai-security**（2 个）：`detecting-ai-model-prompt-injection-attacks`、`implementing-llm-guardrails-for-security` 等
- **wireless-security**（2 个）：`detecting-bluetooth-low-energy-attacks`、`performing-bluetooth-security-assessment` 等
- **offensive-security**（2 个）：`implementing-attack-surface-management`、`performing-binary-exploitation-analysis` 等
- **privacy-compliance**（2 个）：`implementing-gdpr-data-subject-access-request`、`performing-privacy-impact-assessment` 等
- **identity-and-access-management**（2 个）：`implementing-hardware-security-key-authentication`、`implementing-privileged-access-workstation` 等
- **red-team**（2 个）：`performing-active-directory-forest-trust-attack`、`performing-red-team-with-covenant` 等
- **identity-security**（1 个）：`analyzing-active-directory-acl-abuse` 等
- **blockchain-security**（1 个）：`analyzing-ethereum-smart-contract-vulnerabilities` 等
- **firmware-security**（1 个）：`analyzing-uefi-bootkit-persistence` 等
- **social-engineering-defense**（1 个）：`detecting-deepfake-audio-in-vishing-attacks` 等
- **data-protection**（1 个）：`implementing-data-loss-prevention-with-microsoft-purview` 等
- **zero-trust**（1 个）：`implementing-zero-trust-with-beyondcorp` 等
- **ot-security**（1 个）：`monitoring-scada-modbus-traffic-anomalies` 等
- **firmware-analysis**（1 个）：`performing-firmware-extraction-with-binwalk` 等
- **purple-team**（1 个）：`performing-purple-team-atomic-testing` 等
- **governance-risk-compliance**（1 个）：`performing-soc2-type2-audit-preparation` 等

## 如何使用
当用户提出具体网络安全任务时，**直接调用对应的子技能**（通过 Skill 工具，传入子技能的文件夹名）：

- 恶意代码分析 → `analyzing-android-malware-with-apktool`
- 磁盘取证 → `acquiring-disk-image-with-dd-and-dcfldd`
- 云安全 → `analyzing-azure-activity-logs-for-threats` / `analyzing-cloud-storage-access-patterns`
- 威胁狩猎 → `analyzing-indicators-of-compromise`
- 红队/渗透 → `analyzing-cobalt-strike-beacon-configuration`

不确定用哪个时，先读 `SKILLS_INDEX.md`（本目录下的完整按领域清单），或直接用关键词检索子技能名。

## 本目录附带资源
- `SKILLS_INDEX.md` — 754 个技能的完整清单（按领域分组）
- `README.md` — 原项目说明
- `index.json` — 机器可读的技能元数据索引
- `ATTACK_COVERAGE.md` — ATT&CK 框架覆盖率明细
- `mappings/` — 各框架映射数据
- `LICENSE` — Apache-2.0
