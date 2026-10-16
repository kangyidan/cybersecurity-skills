---
name: analyzing-powershell-script-block-logging
description: Parse Windows PowerShell Script Block Logs (Event ID 4104) from EVTX
  files to detect obfuscated commands, encoded payloads, and living-off-the-land techniques.
  Uses python-evtx to extract and reconstruct multi-block scripts, applies entropy
  analysis and pattern matching for Base64-encoded commands, Invoke-Expression abuse,
  download cradles, and AMSI bypass attempts.
domain: cybersecurity
subdomain: security-operations
tags:
- powershell
- script-block-logging
- event-id-4104
- obfuscation-detection
- windows-forensics
- endpoint-security
version: '1.0'
author: mahipal
license: Apache-2.0
nist_csf:
- DE.CM-01
- RS.MA-01
- GV.OV-01
- DE.AE-02
mitre_attack:
- T1059.001
- T1027.010
- T1140
- T1105
atlas_techniques:
- AML.T0017
- AML.T0031
d3fend_techniques:
- D3-DQSA
- D3-FH
- D3-HBPI
- D3-SBV
nist_ai_rmf:
- GOVERN-6.1
- MANAGE-1.3
- MEASURE-2.6
---


# Analyzing PowerShell Script Block Logging


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

1. Install dependencies: `pip install python-evtx lxml`
2. Collect PowerShell Operational logs: `Microsoft-Windows-PowerShell%4Operational.evtx`
3. Parse Event ID 4104 entries using python-evtx to extract ScriptBlockText, ScriptBlockId, and MessageNumber/MessageTotal for multi-part script reconstruction.
4. Apply detection heuristics:
   - Base64-encoded commands (`-EncodedCommand`, `FromBase64String`)
   - Download cradles (`DownloadString`, `DownloadFile`, `Invoke-WebRequest`, `Net.WebClient`)
   - AMSI bypass patterns (`AmsiUtils`, `amsiInitFailed`)
   - Obfuscation indicators (high entropy, tick-mark insertion, string concatenation)
5. Generate a report with reconstructed scripts, risk scores, and MITRE ATT&CK mappings.

```bash
python scripts/agent.py --evtx-file /path/to/PowerShell-Operational.evtx --output ps_analysis.json
```

## Examples

### Detect Encoded Command Execution
```python
import base64
if "-encodedcommand" in script_text.lower():
    encoded = script_text.split()[-1]
    decoded = base64.b64decode(encoded).decode("utf-16-le")
```

### Reconstruct Multi-Block Script
Scripts split across multiple 4104 events share a `ScriptBlockId`. Concatenate blocks ordered by `MessageNumber` to recover the full script.
