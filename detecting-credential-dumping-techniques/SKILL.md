---
name: detecting-credential-dumping-techniques
description: Detect LSASS credential dumping, SAM database extraction, and NTDS.dit
  theft using Sysmon Event ID 10, Windows Security logs, and SIEM correlation rules
domain: cybersecurity
subdomain: threat-detection
tags:
- credential-dumping
- lsass
- mimikatz
- sysmon
- active-directory
- windows-security
- defense-evasion
version: '1.0'
author: mahipal
license: Apache-2.0
d3fend_techniques:
- Token Binding
- Execution Isolation
- File Metadata Consistency Validation
- Restore Access
- Application Protocol Command Analysis
nist_csf:
- DE.CM-01
- DE.AE-02
- DE.AE-06
- ID.RA-05
mitre_attack:
- T1078
- T1190
- T1059
- T1003
- T1110
atlas_techniques:
- AML.T0012
- AML.T0017
- AML.T0024
- AML.T0043
nist_ai_rmf:
- GOVERN-6.1
- GOVERN-6.2
- MEASURE-2.6
---

# Detecting Credential Dumping Techniques

## Overview

Credential dumping (MITRE ATT&CK T1003) is a post-exploitation technique where adversaries extract authentication credentials from OS memory, registry hives, or domain controller databases. This skill covers detection of LSASS memory access via Sysmon Event ID 10 (ProcessAccess), SAM registry hive export via reg.exe, NTDS.dit extraction via ntdsutil/vssadmin, and comsvcs.dll MiniDump abuse. Detection rules analyze GrantedAccess bitmasks, suspicious calling processes, and known tool signatures.


## When to Use

- When a privilege escalation alert fires and you need to trace misconfigured ACLs or group memberships
- When onboarding a new Active Directory environment and running a baseline security audit
- When a red team engagement reveals AD attack paths that require detection coverage
- When investigating a compromised account's lateral movement potential across the domain
- When preparing a BloodHound analysis and needing structured remediation steps for findings
- When validating that GPO and OU permissions follow least-privilege principles post-hardening

## Prerequisites

- Sysmon v14+ deployed with ProcessAccess logging (Event ID 10) for lsass.exe
- Windows Security audit policy enabling process creation (Event ID 4688) with command line logging
- Splunk or Elastic SIEM ingesting Sysmon and Windows Security logs
- Python 3.8+ for log analysis

## Steps

1. Configure Sysmon to log ProcessAccess events targeting lsass.exe
2. Forward Sysmon Event ID 10 and Windows Event ID 4688 to SIEM
3. Create detection rules for known GrantedAccess patterns (0x1010, 0x1FFFFF)
4. Detect comsvcs.dll MiniDump and procdump.exe targeting LSASS PID
5. Alert on reg.exe SAM/SECURITY/SYSTEM hive export commands
6. Detect ntdsutil/vssadmin shadow copy creation for NTDS.dit theft
7. Correlate detections with user/host context for risk scoring

## Expected Output

JSON report containing detected credential dumping indicators with technique classification, severity ratings, process details, MITRE ATT&CK mapping, and Splunk/Elastic detection queries.
