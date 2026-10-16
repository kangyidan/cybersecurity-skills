---
name: hunting-for-t1098-account-manipulation
description: Hunt for MITRE ATT&CK T1098 account manipulation including shadow admin
  creation, SID history injection, group membership changes, and credential modifications
  using Windows Security Event Logs.
domain: cybersecurity
subdomain: threat-hunting
tags:
- threat-hunting
- mitre-attack
- t1098
- account-manipulation
- active-directory
- persistence
version: '1.0'
author: mahipal
license: Apache-2.0
d3fend_techniques:
- Token Binding
- Restore Access
- Application Protocol Command Analysis
- Password Authentication
- Biometric Authentication
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
- T1003
atlas_techniques:
- AML.T0007
nist_ai_rmf:
- MAP-5.1
- MEASURE-2.5
---
# Hunting for T1098 Account Manipulation

## Overview

MITRE ATT&CK T1098 (Account Manipulation) covers adversary actions to maintain or expand access to compromised accounts, including adding credentials, modifying group memberships, SID history injection, and creating shadow admin accounts. This skill covers detecting these techniques through Windows Security Event Log analysis (Event IDs 4738, 4728, 4732, 4756, 4670, 5136), correlating group membership changes with privilege escalation indicators, and identifying anomalous account modification patterns.


## When to Use

- When a privilege escalation alert fires and you need to trace misconfigured ACLs or group memberships
- When onboarding a new Active Directory environment and running a baseline security audit
- When a red team engagement reveals AD attack paths that require detection coverage
- When investigating a compromised account's lateral movement potential across the domain
- When preparing a BloodHound analysis and needing structured remediation steps for findings
- When validating that GPO and OU permissions follow least-privilege principles post-hardening

## Prerequisites

- Windows Security Event Logs (EVTX format) or SIEM access
- Python 3.9+ with `python-evtx`, `lxml` libraries
- Understanding of Active Directory group structure and SID architecture
- Familiarity with MITRE ATT&CK T1098 sub-techniques

## Steps

### Step 1: Parse Account Modification Events
Extract Event IDs 4738 (user account changed), 4728/4732/4756 (member added to security groups), and 5136 (directory service object modified).

### Step 2: Detect Privileged Group Changes
Flag additions to Domain Admins, Enterprise Admins, Schema Admins, Administrators, and Backup Operators groups.

### Step 3: Identify Shadow Admin Indicators
Detect accounts receiving AdminSDHolder protection, direct privilege assignment, or SID history injection.

### Step 4: Correlate with Attack Timeline
Cross-reference account changes with authentication events to identify initial compromise and persistence establishment.

## Expected Output

JSON report with detected account manipulation events, privileged group changes, shadow admin indicators, and timeline correlation.
