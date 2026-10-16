---
name: detecting-sql-injection-via-waf-logs
description: Analyze WAF (ModSecurity/AWS WAF/Cloudflare) logs to detect SQL injection
  attack campaigns. Parses ModSecurity audit logs and JSON WAF event logs to identify
  SQLi patterns (UNION SELECT, OR 1=1, SLEEP(), BENCHMARK()), tracks attack sources,
  correlates multi-stage injection attempts, and generates incident reports with OWASP
  classification.
domain: cybersecurity
subdomain: security-operations
tags:
- waf-log-analysis
- sql-injection-detection
- modsecurity
- aws-waf
- cloudflare-waf
- web-application-security
version: '1.0'
author: mahipal
license: Apache-2.0
nist_csf:
- DE.CM-01
- RS.MA-01
- GV.OV-01
- DE.AE-02
mitre_attack:
- T1190
- T1505.003
- T1059.007
atlas_techniques:
- AML.T0043
d3fend_techniques:
- D3-HPVA
- D3-SAOR
nist_ai_rmf:
- GOVERN-6.1
- MEASURE-2.6
---


# Detecting SQL Injection via WAF Logs


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

1. Install dependencies: `pip install requests`
2. Collect WAF logs (ModSecurity audit log, AWS WAF JSON logs, or Cloudflare firewall events).
3. Run the agent to parse and analyze:
   - Detect SQLi payloads via 15+ regex patterns
   - Classify attacks by OWASP injection type (classic, blind, time-based, UNION-based)
   - Identify persistent attackers by IP clustering
   - Correlate multi-request injection campaigns
   - Calculate attack success probability based on response codes

```bash
python scripts/agent.py --log-file /var/log/modsec_audit.log --format modsecurity --output sqli_report.json
```

## Examples

### ModSecurity SQLi Detection
```
Rule 942100 triggered: SQL Injection Attack Detected via libinjection
URI: /api/users?id=1' UNION SELECT username,password FROM users--
Source IP: 203.0.113.42 (47 requests in 5 minutes)
Classification: UNION-based SQLi campaign
```
