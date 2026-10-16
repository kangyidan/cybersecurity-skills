---
name: analyzing-cloud-storage-access-patterns
description: Detect abnormal access patterns in AWS S3, GCS, and Azure Blob Storage
  by analyzing CloudTrail Data Events, GCS audit logs, and Azure Storage Analytics.
  Identifies after-hours bulk downloads, access from new IP addresses, unusual API
  calls (GetObject spikes), and potential data exfiltration using statistical baselines
  and time-series anomaly detection.
domain: cybersecurity
subdomain: cloud-security
tags:
- cloud-security
- aws-s3
- gcs
- azure-blob-storage
- cloudtrail
- data-access-anomaly
- exfiltration-detection
version: '1.0'
author: mahipal
license: Apache-2.0
atlas_techniques:
- AML.T0024
- AML.T0056
nist_ai_rmf:
- MEASURE-2.7
- MAP-5.1
- MANAGE-2.4
nist_csf:
- PR.IR-01
- ID.AM-08
- GV.SC-06
- DE.CM-01
mitre_attack:
- T1530
- T1567.002
- T1619
- T1078.004
- T1048
d3fend_techniques:
- D3-MFA
- D3-UAP
---


# Analyzing Cloud Storage Access Patterns


## When to Use

- When a CLOUD security alert triggers and you need structured investigation steps
- When performing a cloud infrastructure review before a compliance audit (SOC 2, ISO 27001)
- When investigating unusual API calls, privilege escalation attempts, or resource modifications
- When a new workload is deployed and needs a security posture baseline before going to production
- When building detection rules for cloud-native SIEM (Sentinel, Security Hub, Chronicle)
- When a penetration tester identifies a misconfiguration and you need to scope the blast radius

## Prerequisites

- Familiarity with cloud security concepts and tools
- Access to a test or lab environment for safe execution
- Python 3.8+ with required dependencies installed
- Appropriate authorization for any testing activities

## Instructions

1. Install dependencies: `pip install boto3 requests`
2. Query CloudTrail for S3 Data Events using AWS CLI or boto3.
3. Build access baselines: hourly request volume, per-user object counts, source IP history.
4. Detect anomalies:
   - After-hours access (outside 8am-6pm local time)
   - Bulk downloads: >100 GetObject calls from single principal in 1 hour
   - New source IPs not seen in the prior 30 days
   - ListBucket enumeration spikes (reconnaissance indicator)
5. Generate prioritized findings report.

```bash
python scripts/agent.py --bucket my-sensitive-data --hours-back 24 --output s3_access_report.json
```

## Examples

### CloudTrail S3 Data Event
```json
{"eventName": "GetObject", "requestParameters": {"bucketName": "sensitive-data", "key": "financials/q4.xlsx"},
 "sourceIPAddress": "203.0.113.50", "userIdentity": {"arn": "arn:aws:iam::123456789012:user/analyst"}}
```
