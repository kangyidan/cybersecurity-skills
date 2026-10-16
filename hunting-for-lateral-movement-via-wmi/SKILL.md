---
name: hunting-for-lateral-movement-via-wmi
description: Detect WMI-based lateral movement by analyzing Windows Event ID 4688
  process creation and Sysmon Event ID 1 for WmiPrvSE.exe child process patterns,
  remote process execution, and WMI event subscription persistence.
domain: cybersecurity
subdomain: threat-hunting
tags:
- threat-hunting
- lateral-movement
- wmi
- sysmon
- mitre-attack
- process-creation
version: '1.0'
author: mahipal
license: Apache-2.0
nist_csf:
- DE.CM-01
- DE.AE-02
- DE.AE-07
- ID.RA-05
mitre_attack:
- T1046
- T1057
- T1082
- T1083
- T1021
atlas_techniques:
- AML.T0007
d3fend_techniques:
- D3-DNSAL
- D3-FAAA
- D3-FH
- D3-NTA
nist_ai_rmf:
- MAP-5.1
- MEASURE-2.5
---
# Hunting for Lateral Movement via WMI

## Overview

Windows Management Instrumentation (WMI) is commonly abused for lateral movement via `wmic process call create` or Win32_Process.Create() to execute commands on remote hosts. Detection focuses on identifying WmiPrvSE.exe spawning child processes (cmd.exe, powershell.exe) in Windows Security Event ID 4688 and Sysmon Event ID 1 logs, along with WMI-Activity/Operational events (5857, 5860, 5861) for event subscription persistence.


## When to Use

- When a new threat actor or campaign is reported and you need rapid intelligence profiling
- When mapping your detection coverage against a specific APT group's TTPs in ATT&CK Navigator
- When a CISO requests a briefing on emerging threats targeting your sector
- When IOCs from an active incident need to be correlated with known threat actor infrastructure
- When building a threat model for a new system or business unit acquisition
- When updating your ATT&CK layer after a detection gap is identified during a purple team exercise

## Prerequisites

- Windows Security Event Logs with Process Creation auditing enabled (Event 4688 with command line)
- Sysmon installed with Event ID 1 (Process Creation) configured
- Python 3.9+ with `python-evtx`, `lxml` libraries
- Understanding of WMI architecture and WmiPrvSE.exe behavior

## Steps

### Step 1: Parse Process Creation Events
Extract Event ID 4688 and Sysmon Event 1 entries from EVTX files.

### Step 2: Detect WmiPrvSE Child Processes
Flag processes where ParentImage/ParentProcessName is WmiPrvSE.exe, indicating remote WMI execution.

### Step 3: Analyze Command Line Patterns
Identify suspicious command lines matching WMI lateral movement patterns (cmd.exe /q /c, output redirection to admin$ share).

### Step 4: Check WMI Event Subscriptions
Parse WMI-Activity/Operational log for event consumer creation indicating persistence.

## Expected Output

JSON report with WMI-spawned processes, suspicious command lines, WMI event subscription alerts, and timeline of lateral movement activity.
