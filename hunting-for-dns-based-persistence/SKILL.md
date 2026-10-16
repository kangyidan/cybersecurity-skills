---
name: hunting-for-dns-based-persistence
description: Hunt for DNS-based persistence mechanisms including DNS hijacking, dangling
  CNAME records, wildcard DNS abuse, and unauthorized zone modifications using passive
  DNS databases, SecurityTrails API, and DNS audit log analysis.
domain: cybersecurity
subdomain: threat-hunting
tags:
- dns
- persistence
- threat-hunting
- passive-dns
- dns-hijacking
- subdomain-takeover
- securitytrails
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
- T1547
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

# Hunting for DNS-based Persistence

## Overview

Attackers establish DNS-based persistence by hijacking DNS records, creating unauthorized subdomains, abusing wildcard DNS entries, or modifying NS delegations to redirect traffic through attacker-controlled infrastructure. These techniques survive credential rotations, endpoint reimaging, and traditional remediation because DNS changes persist independently of compromised hosts. Detection requires passive DNS historical analysis, zone file auditing, and monitoring for unauthorized record modifications. This skill covers hunting methodologies using SecurityTrails passive DNS API, DNS audit logs from Route53/Azure DNS/Cloudflare, and zone transfer analysis.


## When to Use

- When new threat intelligence describes TTPs not yet covered by existing detections
- When a hypothesis-driven hunt is initiated after a peer organization reports a breach
- When ATT&CK coverage analysis reveals a gap that needs proactive hunting before alerting is built
- When crown-jewel assets (domain controllers, backup servers) need targeted behavioral monitoring
- When MSSP or MDR service requires documented hunt procedures for client reporting
- When a red team exercise concludes and blue team needs to verify detection of TTPs used

## Prerequisites

- SecurityTrails API key (free tier provides 50 queries/month)
- Access to DNS provider audit logs (Route53, Azure DNS, Cloudflare, or on-premises DNS)
- Python 3.9+ with requests library
- DNS zone file access or AXFR capability for internal zones
- Historical DNS baseline for comparison

## Steps

### Step 1: Baseline DNS Records

Export current DNS zone records and establish baseline for all authorized A, AAAA, CNAME, MX, NS, and TXT records.

### Step 2: Query Passive DNS History

Use SecurityTrails API to retrieve historical DNS records and identify unauthorized changes, new subdomains, and CNAME records pointing to decommissioned services (dangling CNAMEs).

### Step 3: Detect Anomalies

Compare current records against baseline to identify unauthorized modifications, wildcard records that resolve all subdomains, NS delegation changes, and MX record hijacking.

### Step 4: Investigate Findings

Correlate DNS anomalies with threat intelligence feeds, check resolution targets against known malicious infrastructure, and validate record ownership.

## Expected Output

JSON report listing DNS anomalies with record type, historical changes, risk severity, and remediation recommendations for each finding.
