---
name: analyzing-threat-landscape-with-misp
description: Analyze the threat landscape using MISP (Malware Information Sharing
  Platform) by querying event statistics, attribute distributions, threat actor galaxy
  clusters, and tag trends over time. Uses PyMISP to pull event data, compute IOC
  type breakdowns, identify top threat actors and malware families, and generate threat
  landscape reports with temporal trends.
domain: cybersecurity
subdomain: threat-intelligence
tags:
- threat-intelligence
- misp
- threat-landscape
- ioc-analysis
- cti
- threat-sharing
version: '1.0'
author: mahipal
license: Apache-2.0
d3fend_techniques:
- File Metadata Consistency Validation
- Application Protocol Command Analysis
- Identifier Analysis
- Content Format Conversion
- Message Analysis
nist_csf:
- ID.RA-01
- ID.RA-05
- DE.CM-01
- DE.AE-02
mitre_attack:
- T1566
- T1071.001
- T1568
- T1583.001
- T1102
atlas_techniques:
- AML.T0023
- AML.T0040
nist_ai_rmf:
- GOVERN-4.1
- MANAGE-2.2
- MEASURE-2.6
- MEASURE-2.7
---


# Analyzing Threat Landscape with MISP


## When to Use

- When a new threat actor or campaign is reported and you need rapid intelligence profiling
- When mapping your detection coverage against a specific APT group's TTPs in ATT&CK Navigator
- When a CISO requests a briefing on emerging threats targeting your sector
- When IOCs from an active incident need to be correlated with known threat actor infrastructure
- When building a threat model for a new system or business unit acquisition
- When updating your ATT&CK layer after a detection gap is identified during a purple team exercise

## Prerequisites

- Familiarity with threat intelligence concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Instructions

1. Install dependencies: `pip install pymisp`
2. Configure MISP URL and API key.
3. Run the agent to generate threat landscape analysis:
   - Pull event statistics by threat level and date range
   - Analyze attribute type distributions (IP, domain, hash, URL)
   - Identify top MITRE ATT&CK techniques from event tags
   - Track threat actor activity via galaxy clusters
   - Generate temporal trend analysis of IOC submissions

```bash
python scripts/agent.py --misp-url https://misp.local --api-key YOUR_KEY --days 90 --output landscape_report.json
```

## Examples

### Threat Landscape Summary
```
Period: Last 90 days
Events analyzed: 1,247
Top threat level: High (43%)
Top attribute type: ip-dst (31%), domain (22%), sha256 (18%)
Top MITRE technique: T1566 Phishing (89 events)
Top threat actor: APT28 (34 events)
```
