#!/usr/bin/env python3
"""AWS Detective threat hunting agent.

Uses the AWS Detective API to perform behavior graph analysis,
finding groups investigation, and entity-based threat hunting
across VPC Flow Logs, CloudTrail, and GuardDuty findings.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone


try:
    import boto3
    from botocore.exceptions import ClientError, NoCredentialsError
    HAS_BOTO3 = True
except ImportError:
    HAS_BOTO3 = False


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="AWS Detective threat hunting — behavior graph analysis and entity investigation"
    )
    parser.add_argument(
        "graph_arn",
        nargs="?",
        default=None,
        help="AWS Detective behavior graph ARN (arn:aws:detective:region:account:graph:id)"
    )
    parser.add_argument("--region", "-r", default="us-east-1", help="AWS region (default: us-east-1)")
    parser.add_argument("--days", "-d", type=int, default=7, help="Look-back window in days (default: 7)")
    parser.add_argument("--entity", "-e", default=None, help="Specific entity ARN or IP to investigate")
    parser.add_argument("--output", "-o", default=None, help="Output JSON file path")
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")
    return parser.parse_args()


def get_detective_client(region):
    """Initialize AWS Detective boto3 client."""
    if not HAS_BOTO3:
        print("[!] boto3 not installed. Run: pip install boto3", file=sys.stderr)
        sys.exit(1)
    return boto3.client("detective", region_name=region)


def list_graphs(client):
    """List all behavior graphs in the account."""
    try:
        resp = client.list_graphs()
        return resp.get("GraphList", [])
    except (ClientError, NoCredentialsError) as e:
        print(f"[!] Failed to list graphs: {e}", file=sys.stderr)
        return []


def get_members(client, graph_arn):
    """List member accounts in a behavior graph."""
    try:
        resp = client.list_members(GraphArn=graph_arn)
        return resp.get("MemberDetails", [])
    except ClientError as e:
        print(f"[!] Failed to list members: {e}", file=sys.stderr)
        return []


def search_graph(client, graph_arn, entity_type, entity_value, start_time, end_time):
    """Search behavior graph for an entity (IP, account, IAM role)."""
    try:
        resp = client.search_graph(
            GraphArn=graph_arn,
            QueryExpression=f"SCOPE_ACCOUNT_FILTER entity.{entity_type} = '{entity_value}'",
            EntityTypes=[entity_type.upper()],
        )
        return resp.get("Entities", [])
    except ClientError as e:
        print(f"[!] Search failed: {e}", file=sys.stderr)
        return []


def get_finding_groups(client, graph_arn, start_time, end_time):
    """Retrieve Detective finding groups for the time window."""
    try:
        resp = client.list_investigations(
            GraphArn=graph_arn,
            FilterCriteria={
                "CreatedTime": {
                    "StartInclusive": start_time.isoformat(),
                    "EndInclusive": end_time.isoformat(),
                }
            }
        )
        return resp.get("InvestigationDetails", [])
    except ClientError as e:
        print(f"[!] Could not list investigations: {e}", file=sys.stderr)
        return []


def generate_report(graph_arn, region, days, entity, verbose):
    """Run full threat hunting sweep against AWS Detective."""
    client = get_detective_client(region)
    end_time = datetime.now(timezone.utc)
    start_time = end_time - timedelta(days=days)

    report = {
        "graph_arn": graph_arn,
        "region": region,
        "hunt_window": {
            "start": start_time.isoformat(),
            "end": end_time.isoformat(),
            "days": days,
        },
        "members": [],
        "investigations": [],
        "entity_findings": [],
        "summary": {},
    }

    # List behavior graphs if no ARN provided
    if not graph_arn:
        graphs = list_graphs(client)
        if not graphs:
            print("[!] No Detective behavior graphs found in this account/region.", file=sys.stderr)
            return report
        graph_arn = graphs[0]["Arn"]
        report["graph_arn"] = graph_arn
        if verbose:
            print(f"[*] Using behavior graph: {graph_arn}")

    # Get members
    members = get_members(client, graph_arn)
    report["members"] = [{"account_id": m.get("AccountId"), "status": m.get("Status")} for m in members]
    if verbose:
        print(f"[*] Member accounts: {len(members)}")

    # Get investigations
    investigations = get_finding_groups(client, graph_arn, start_time, end_time)
    report["investigations"] = investigations
    if verbose:
        print(f"[*] Active investigations: {len(investigations)}")

    # Entity-specific hunt
    if entity:
        entity_type = "IP_ADDRESS" if entity.replace(".", "").isdigit() else "AWS_ACCOUNT"
        findings = search_graph(client, graph_arn, entity_type, entity, start_time, end_time)
        report["entity_findings"] = findings
        if verbose:
            print(f"[*] Entity findings for '{entity}': {len(findings)}")

    # Summary
    report["summary"] = {
        "member_count": len(members),
        "active_investigations": len(investigations),
        "entity_findings": len(report.get("entity_findings", [])),
        "high_severity_investigations": sum(
            1 for i in investigations if i.get("Severity") == "HIGH"
        ),
    }

    return report


if __name__ == "__main__":
    args = parse_args()
    result = generate_report(
        graph_arn=args.graph_arn,
        region=args.region,
        days=args.days,
        entity=args.entity,
        verbose=args.verbose,
    )
    output = json.dumps(result, indent=2, default=str)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output)
        print(f"[*] Report written to {args.output}")
    else:
        print(output)
