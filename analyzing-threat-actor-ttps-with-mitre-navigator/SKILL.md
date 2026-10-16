---
name: analyzing-threat-actor-ttps-with-mitre-navigator
description: 'Map advanced persistent threat (APT) group tactics, techniques, and
  procedures (TTPs) to the MITRE ATT&CK framework using the ATT&CK Navigator and attackcti
  Python library. The analyst queries STIX/TAXII data for group-technique associations,
  generates Navigator layer files for visualization, and compares defensive coverage
  against adversary profiles. Activates for requests involving APT TTP mapping, ATT&CK
  Navigator layers, threat actor profiling, or MITRE technique coverage analysis.

  '
domain: cybersecurity
subdomain: threat-intelligence
tags:
- mitre-attack
- navigator
- threat-intelligence
- apt
- ttp-mapping
- stix
- attackcti
version: '1.0'
author: mahipal
license: Apache-2.0
nist_ai_rmf:
- MEASURE-2.7
- MAP-5.1
- MANAGE-2.4
atlas_techniques:
- AML.T0070
- AML.T0066
- AML.T0082
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
- T1566.001
- T1059.001
- T1071.001
- T1547.001
- T1053.005
---
# Analyzing Threat Actor TTPs with MITRE Navigator

## Overview

The MITRE ATT&CK Navigator is a web application for annotating and visualizing ATT&CK matrices.
Combined with the attackcti Python library (which queries ATT&CK STIX data via TAXII), analysts
can programmatically generate Navigator layer files mapping specific threat group TTPs, compare
multiple groups, and assess detection coverage gaps against known adversaries.


## When to Use

- When a new threat actor or campaign is reported and you need rapid intelligence profiling
- When mapping your detection coverage against a specific APT group's TTPs in ATT&CK Navigator
- When a CISO requests a briefing on emerging threats targeting your sector
- When IOCs from an active incident need to be correlated with known threat actor infrastructure
- When building a threat model for a new system or business unit acquisition
- When updating your ATT&CK layer after a detection gap is identified during a purple team exercise

## Prerequisites

- Python 3.8+ with attackcti and stix2 libraries installed
- MITRE ATT&CK Navigator (web UI or local instance)
- Understanding of STIX 2.1 objects and relationships

## Steps

1. Query ATT&CK STIX data for target threat group using attackcti
2. Extract techniques associated with the group via STIX relationships
3. Generate ATT&CK Navigator layer JSON with technique annotations
4. Overlay detection coverage to identify gaps
5. Export layer for team review and defensive planning

## Expected Output

```json
{
  "name": "APT29 TTPs",
  "domain": "enterprise-attack",
  "techniques": [
    {"techniqueID": "T1566.001", "score": 1, "comment": "Spearphishing Attachment"},
    {"techniqueID": "T1059.001", "score": 1, "comment": "PowerShell"}
  ]
}
```
