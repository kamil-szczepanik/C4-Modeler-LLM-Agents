## Overview
[The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud at scale while supporting analyst case reviews. It ensures strict PCI-DSS compliance, <50 ms latency, and a 7-year tamper-evident audit trail within a fixed budget.]

## Key Elements
* Amazon DynamoDB (Database Container)
* Feature Store Table (DynamoDB Table)
* Case State Table (DynamoDB Table)
* Audit Stream Processor (DynamoDB Stream / AWS Lambda)
* Scoring Engine & Case Management Backend (ECS Fargate Consumers)

## Relationships
* Scoring Engine -> Feature Store Table: Performs low-latency risk profile lookups via AWS SDK over AWS PrivateLink [TLS 1.3]
* Case Management Backend -> Case State Table: Manages investigation workflow states via AWS SDK over AWS PrivateLink [TLS 1.3]
* Case State Table -> Audit Stream Processor: Publishes state changes via DynamoDB Streams
* Audit Stream Processor -> Amazon S3: Writes tamper-evident decision snapshots via AWS SDK [HTTPS]

## Technology Stack
* Amazon DynamoDB: Managed NoSQL database selected for low-latency feature lookups and case state management under high TPS.
* DynamoDB Streams & AWS Lambda: Used to asynchronously capture state changes for auditability without impacting transaction latency.
* AWS KMS: Provides customer-managed keys (CMK) and envelope encryption for data tokenization and column-level masking (R-05).
* Amazon S3 Object Lock: Enforces compliance-mode immutability for the 7-year audit trail (R-06).
* Provisioned Capacity Mode with Auto-Scaling: Configured at 70% target utilization to cap infrastructure costs under the 25,000 EUR/month budget.

## Rationale
[This architecture leverages fully managed AWS services to meet stringent <50 ms P99 latency and PCI-DSS Level 1 security requirements with minimal operational overhead for a three-engineer team. Furthermore, it implements automated cost-capping mechanisms and immutable audit logging to satisfy strict budget and 7-year compliance mandates.]