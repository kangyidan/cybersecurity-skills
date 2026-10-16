---
name: analyzing-memory-forensics-with-lime-and-volatility
description: 'Performs Linux memory acquisition using LiME (Linux Memory Extractor)
  kernel module and analysis with Volatility 3 framework. Extracts process lists,
  network connections, bash history, loaded kernel modules, and injected code from
  Linux memory images. Use when performing incident response on compromised Linux
  systems.

  '
domain: cybersecurity
subdomain: security-operations
tags:
- memory-forensics
- linux-forensics
- lime
- volatility
- incident-response
- kernel-modules
version: '1.0'
author: mahipal
license: Apache-2.0
nist_csf:
- DE.CM-01
- RS.MA-01
- GV.OV-01
- DE.AE-02
mitre_attack:
- T1055
- T1003.001
- T1620
- T1564.001
atlas_techniques:
- AML.T0018
- AML.T0024
d3fend_techniques:
- D3-CRO
- D3-LSCFA
- D3-PA
- D3-PLA
nist_ai_rmf:
- GOVERN-6.2
- MANAGE-1.3
- MEASURE-2.6
---

# Analyzing Memory Forensics with LiME and Volatility


## When to Use

- When you receive a suspicious binary sample for triage and need to characterize its capabilities
- When an EDR or AV alert fires on an endpoint and you need to understand the threat's full behavior
- When threat intel reports a new malware family and you need to validate IOCs against a sample
- When performing post-incident forensic analysis to characterize the attacker's toolset
- When building YARA or Sigma detection rules from a confirmed malicious artifact
- When validating sandbox detonation results with static analysis to confirm or enrich findings

## Prerequisites

- Familiarity with security operations concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Instructions

Acquire Linux memory using LiME kernel module, then analyze with Volatility 3
to extract forensic artifacts from the memory image.

```bash
# LiME acquisition
insmod lime-$(uname -r).ko "path=/evidence/memory.lime format=lime"

# Volatility 3 analysis
vol3 -f /evidence/memory.lime linux.pslist
vol3 -f /evidence/memory.lime linux.bash
vol3 -f /evidence/memory.lime linux.sockstat
```

```python
import volatility3
from volatility3.framework import contexts, automagic
from volatility3.plugins.linux import pslist, bash, sockstat

# Programmatic Volatility 3 usage
context = contexts.Context()
automagics = automagic.available(context)
```

Key analysis steps:
1. Acquire memory with LiME (format=lime or format=raw)
2. List processes with linux.pslist, compare with linux.psscan
3. Extract bash command history with linux.bash
4. List network connections with linux.sockstat
5. Check loaded kernel modules with linux.lsmod for rootkits

## Examples

```bash
# Full forensic workflow
vol3 -f memory.lime linux.pslist | grep -v "\[kthread\]"
vol3 -f memory.lime linux.bash
vol3 -f memory.lime linux.malfind
vol3 -f memory.lime linux.lsmod
```
