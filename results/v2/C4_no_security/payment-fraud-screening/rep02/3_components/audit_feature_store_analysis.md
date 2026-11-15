## Overview
The system screens card-not-present payment authorizations for fraud in real-time while providing case management for analysts and 7-year immutable audit logs. It is operated by a three-engineer team on AWS under a strict €25,000 monthly budget.

## Key Elements
- Audit Log Store (Amazon S3 with Object Lock, S3 Lifecycle to Glacier)
- Feature Store (Amazon DynamoDB with native TTL)
- Audit Query Engine (Amazon Athena with AWS Glue Data Catalog)
- Asynchronous Ingestion (Amazon Kinesis Firehose)
- Infrastructure & Deployment (Terraform, ArgoCD)

## Relationships
- Real-Time Scoring Engine Container -> Feature Store: Low-latency point lookups [AWS SDK / HTTPS over TCP]
- Real-Time Scoring Engine Container -> Amazon Kinesis Firehose: Asynchronous batch delivery of audit payloads [HTTPS]
- Amazon Kinesis Firehose -> Audit Log Store: Batched persistence of tamper-evident logs [S3 API / HTTPS]
- Compliance Export Container / Risk Managers -> Audit Query Engine: Serverless SQL audits [Amazon Athena]

## Technology Stack
- Amazon S3 with Object Lock: Ensures WORM-compliant, tamper-evident 7-year audit retention (R-06).
- Amazon DynamoDB: Provides single-digit millisecond feature reads (R-04) and automated TTL pruning for cost control.
- Amazon Kinesis Firehose: Decouples audit writing from the critical path to protect P99 latency.
- Amazon Athena: Enables serverless SQL querying over S3 logs with zero operational overhead.
- Terraform & ArgoCD: Automates infrastructure provisioning and GitOps deployments for a three-engineer team.

## Rationale
This architecture decouples low-latency scoring operations from heavy compliance storage to satisfy sub-50ms performance requirements. Utilizing serverless and managed AWS services keeps operational overhead minimal for a three-engineer team while strictly enforcing PCI-DSS Level 1 and 7-year audit constraints within budget.