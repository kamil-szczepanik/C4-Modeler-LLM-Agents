## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for fraud and manages analyst reviews. It operates within AWS (`eu-west-1`) under strict PCI-DSS Level 1 compliance and a fixed monthly budget.

## Key Elements
- Fraud Analyst & Risk Manager, Compliance Auditor
- Payment Gateway, Tokenization / Vault Service
- AWS Application Load Balancer (ALB)
- Scoring Engine Container (Go/Rust on AWS ECS Fargate)
- Case Management & Reporting Container (Node.js on AWS ECS Fargate)
- Amazon ElastiCache Redis
- Amazon SQS / Kinesis Data Firehose
- Amazon S3 Object Lock (Compliance Archive with `GOVERNANCE` mode and Cross-Region Replication to `eu-central-1`)
- Amazon Athena / Glue Data Catalog
- AWS CloudWatch, S3 Storage Lens, & PagerDuty

## Relationships
- Payment Gateway -> AWS ALB: Forwards card-not-present authorization requests [HTTPS]
- AWS ALB -> Scoring Engine Container: Routes authorization traffic [HTTP/gRPC]
- Scoring Engine Container -> Amazon ElastiCache Redis: Retrieves scoring rules and caches state [Redis Protocol]
- Scoring Engine Container -> Amazon SQS / Kinesis Data Firehose: Emits scoring decision payloads [AWS API]
- Firehose Container -> Amazon S3 Object Lock: Writes tamper-evident audit payloads [HTTPS / S3 PutObject API]
- S3 Bucket (Compliance Archive) -> Replica Bucket (`eu-central-1`): Replicates immutable audit objects [AWS Replication API]
- Amazon Athena -> Athena Data Catalog / S3 Bucket: Queries historical audit partitions [SQL / HTTPS]
- S3 Storage Lens & CloudWatch Alarms -> PagerDuty: Alerts engineering team on replication lag or storage anomalies [HTTPS / AWS API]

## Technology Stack
- AWS ECS Fargate: Runs serverless containers with minimal operational overhead for a 3-person team.
- Amazon S3 Object Lock (`GOVERNANCE` mode): Ensures 7-year tamper-evident audit retention (R-06) while preventing runaway storage costs.
- Amazon Athena & Parquet: Enables cost-effective, serverless SQL queries for compliance auditors.
- Amazon S3 Replication Time Control (RTC): Guarantees cross-region compliance synchronization to `eu-central-1` within a 15-minute SLA.

## Rationale
This serverless AWS architecture minimizes operational burden for a three-engineer team while meeting strict sub-50ms performance (R-04) and 7-year auditability (R-06). Cost controls like `GOVERNANCE` mode and Athena partition pruning ensure compliance within the 25,000 EUR/month budget.