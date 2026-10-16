---
name: detecting-living-off-the-land-with-lolbas
description: Detect Living Off the Land Binaries (LOLBins/LOLBAS) abuse including
  certutil, regsvr32, mshta, and rundll32 via process telemetry, Sigma rules, and
  parent-child process analysis
domain: cybersecurity
subdomain: threat-detection
tags:
- lolbas
- lolbins
- sigma-rules
- process-monitoring
- sysmon
- endpoint-detection
- threat-hunting
version: '1.0'
author: mahipal
license: Apache-2.0
d3fend_techniques:
- Executable Denylisting
- Execution Isolation
- File Metadata Consistency Validation
- Application Protocol Command Analysis
- Content Format Conversion
nist_csf:
- DE.CM-01
- DE.AE-02
- DE.AE-06
- ID.RA-05
mitre_attack:
- T1078
- T1190
- T1059
atlas_techniques:
- AML.T0012
- AML.T0043
nist_ai_rmf:
- GOVERN-6.1
- GOVERN-6.2
- MEASURE-2.6
---

# Detecting Living Off the Land with LOLBAS

## Overview

Living Off the Land Binaries, Scripts, and Libraries (LOLBAS) are legitimate system utilities abused by attackers to execute malicious actions while evading detection. This skill covers detecting abuse of certutil.exe, regsvr32.exe, mshta.exe, rundll32.exe, msbuild.exe, and other LOLBins using process telemetry from Sysmon and Windows Event Logs, combined with Sigma rule-based detection.


## When to Use

- When a security investigation requires detecting living off the land with lolbas as a specific analytical technique
- When building or validating detection coverage for the ATT&CK techniques referenced in this skill
- When a junior analyst needs guided execution steps to perform this safely and correctly
- When a compliance audit requires documented procedures for this security control area
- When onboarding new security tooling and needing a structured validation procedure
- When a purple team exercise identifies gaps in this area and remediation needs to be scoped

## Prerequisites

- Sysmon or Windows Security Event Log (Event ID 4688) with command-line logging enabled
- Sigma rule conversion tool (sigmac or sigma-cli)
- SIEM platform (Splunk, Elastic, or similar) for log ingestion
- Python 3.8+ with pySigma library
- LOLBAS project reference database

## Steps

1. **Establish LOLBin Watchlist** — Build a prioritized list of monitored binaries (certutil, mshta, regsvr32, rundll32, msbuild, installutil, cmstp, wmic, bitsadmin)
2. **Collect Process Telemetry** — Ingest Sysmon Event ID 1 (Process Create) and Windows 4688 events with full command-line capture
3. **Build Sigma Detection Rules** — Create Sigma rules matching suspicious command-line arguments, network activity, and parent-child process anomalies for each LOLBin
4. **Analyze Parent-Child Relationships** — Flag unexpected parent processes spawning LOLBins (e.g., Excel spawning certutil, Word spawning mshta)
5. **Score and Prioritize Alerts** — Apply risk scoring based on argument anomaly, parent process, execution path, and network indicators
6. **Generate Detection Report** — Produce a structured report of all LOLBin abuse detections with MITRE ATT&CK mapping

## Expected Output

- JSON report listing detected LOLBin abuse events with severity scores
- MITRE ATT&CK technique mapping for each detection (T1218, T1105, T1140, T1127)
- Parent-child process anomaly analysis
- Sigma rule match details with raw event data
