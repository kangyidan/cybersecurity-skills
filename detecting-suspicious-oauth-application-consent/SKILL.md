---
name: detecting-suspicious-oauth-application-consent
description: Detect risky OAuth application consent grants in Azure AD / Microsoft
  Entra ID using Microsoft Graph API, audit logs, and permission analysis to identify
  illicit consent grant attacks.
domain: cybersecurity
subdomain: cloud-security
tags:
- OAuth
- Azure-AD
- Entra-ID
- Microsoft-Graph
- illicit-consent
- cloud-security
- application-permissions
version: '1.0'
author: mahipal
license: Apache-2.0
nist_csf:
- PR.IR-01
- ID.AM-08
- GV.SC-06
- DE.CM-01
mitre_attack:
- T1528
- T1550.001
- T1098.001
- T1566.002
atlas_techniques:
- AML.T0012
d3fend_techniques:
- D3-ALAM
- D3-UAP
nist_ai_rmf:
- GOVERN-6.2
- MEASURE-2.6
---

# Detecting Suspicious OAuth Application Consent

## Overview

Illicit consent grant attacks trick users into granting excessive permissions to malicious OAuth applications in Azure AD / Microsoft Entra ID. This skill uses the Microsoft Graph API to enumerate OAuth2 permission grants, analyze application permissions for overly broad scopes, review directory audit logs for consent events, and flag high-risk applications based on publisher verification status and permission scope.


## When to Use

- When a CLOUD security alert triggers and you need structured investigation steps
- When performing a cloud infrastructure review before a compliance audit (SOC 2, ISO 27001)
- When investigating unusual API calls, privilege escalation attempts, or resource modifications
- When a new workload is deployed and needs a security posture baseline before going to production
- When building detection rules for cloud-native SIEM (Sentinel, Security Hub, Chronicle)
- When a penetration tester identifies a misconfiguration and you need to scope the blast radius

## Prerequisites

- Azure AD / Entra ID tenant with Global Reader or Security Reader role
- Microsoft Graph API access with `Application.Read.All`, `AuditLog.Read.All`, `Directory.Read.All`
- Python 3.9+ with `msal`, `requests`
- App registration with client secret or certificate for authentication

## Steps

1. Authenticate to Microsoft Graph using MSAL client credentials flow
2. Enumerate all OAuth2 permission grants via `/oauth2PermissionGrants`
3. List service principals and their assigned application permissions
4. Query directory audit logs for `Consent to application` events
5. Flag applications with high-risk scopes (Mail.Read, Files.ReadWrite.All, etc.)
6. Check publisher verification status for each application
7. Generate risk report with remediation recommendations

## Expected Output

- JSON report listing all OAuth apps with granted permissions, risk scores, unverified publishers, and suspicious consent patterns
- Audit trail of consent grant events with user and IP details
