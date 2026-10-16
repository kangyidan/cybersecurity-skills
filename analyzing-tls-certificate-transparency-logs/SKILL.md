---
name: analyzing-tls-certificate-transparency-logs
description: 'Queries Certificate Transparency logs via crt.sh and pycrtsh to detect
  phishing domains, unauthorized certificate issuance, and shadow IT. Monitors newly
  issued certificates for typosquatting and brand impersonation using Levenshtein
  distance. Use for proactive phishing domain detection and certificate monitoring.

  '
domain: cybersecurity
subdomain: security-operations
tags:
- certificate-transparency
- ct-logs
- crt-sh
- phishing-detection
- tls-monitoring
- security-operations
version: '1.0'
author: mahipal
license: Apache-2.0
atlas_techniques:
- AML.T0073
- AML.T0052
nist_csf:
- DE.CM-01
- RS.MA-01
- GV.OV-01
- DE.AE-02
mitre_attack:
- T1583.001
- T1566.002
- T1598.003
- T1583.006
d3fend_techniques:
- D3-PHDURA
- D3-SFAS
nist_ai_rmf:
- GOVERN-4.1
- MEASURE-2.7
---

# Analyzing TLS Certificate Transparency Logs


## When to Use

- When a SIEM alert fires and you need a structured triage procedure to avoid false positive fatigue
- When building new detection content and need reference queries for this technique
- When security operations need to reduce mean-time-to-detect (MTTD) on a specific attack pattern
- When a new log source is onboarded and needs baseline correlation rules
- When reviewing SOC metrics and identifying detection gaps by ATT&CK tactic coverage
- When a purple team exercise reveals detection blind spots that require new rule development

## Prerequisites

- Familiarity with security operations concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Instructions

Query crt.sh Certificate Transparency database to find certificates issued for
domains similar to your organization's brand, detecting phishing infrastructure.

```python
from pycrtsh import Crtsh

c = Crtsh()
# Search for certificates matching a domain
certs = c.search("example.com")
for cert in certs:
    print(cert["id"], cert["name_value"])

# Get full certificate details
details = c.get(certs[0]["id"], type="id")
```

Key analysis steps:
1. Query crt.sh for all certificates matching your domain pattern
2. Identify certificates with typosquatting variations (Levenshtein distance)
3. Flag certificates from unexpected CAs
4. Monitor for wildcard certificates on suspicious subdomains
5. Cross-reference with known phishing infrastructure

## Examples

```python
from pycrtsh import Crtsh
c = Crtsh()
certs = c.search("%.example.com")
for cert in certs:
    print(f"Issuer: {cert.get('issuer_name')}, Domain: {cert.get('name_value')}")
```
