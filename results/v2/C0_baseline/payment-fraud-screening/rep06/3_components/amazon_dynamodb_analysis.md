## Overview
[The system is a Real-Time Payment Fraud Screening engine deployed on AWS eu-west-1, designed to score payment authorizations and manage fraud review cases. Its core purpose is to prevent fraudulent card-not-present transactions while maintaining a sub-50ms P99 decision latency at 3,000 TPS.]

## Key Elements
*   **Feature Store Table**: DynamoDB table managing operational feature data with automated TTL.
*   **Case Management Table**: DynamoDB table storing analyst review cases with DynamoDB Streams enabled.
*   **Idempotency Store Table**: DynamoDB table ensuring fail-open resilience under R-07.
*   **AWS KMS**: Provides Customer Managed Keys (CMKs) with annual key rotation for encryption at rest.
*   **AWS IAM**: Enforces least privilege using `dynamodb:LeadingKeys` condition keys and account-level SCPs.
*   **VPC Gateway Endpoints**: Secures private connectivity between ECS Fargate tasks and DynamoDB.
*   **Amazon Kinesis Data Streams**: Receives CDC events from DynamoDB Streams for downstream audit extraction.

## Relationships
*   **Scoring Engine -> Feature Store Table**: `Query/GetItem via AWS SDK (HTTPS)` over VPC Gateway Endpoints
*   **Case Management API -> Case Management Table**: `PutItem/UpdateItem via AWS SDK (HTTPS)` over VPC Gateway Endpoints
*   **Feature Store Table & Case Management Table -> DynamoDB Streams**: `Change Data Capture (CDC)` to Amazon Kinesis Data Streams
*   **Scoring Engine & Case Management API -> AWS KMS**: `Decrypt/Encrypt via AWS SDK (HTTPS)` for tokenized and encrypted data

## Technology Stack
*   **Amazon DynamoDB**: Selected with On-Demand capacity to eliminate capacity planning toil for a 3-engineer team while supporting low-latency throughput.
*   **Terraform**: Utilized for Infrastructure as Code provisioning of all tables, TTLs, and KMS policies with drift detection.
*   **AWS CloudWatch & AWS Config**: Deployed for anomaly detection, Contributor Insights, and automated security rule compliance.

## Rationale
[This architecture fits requirements by leveraging serverless On-Demand DynamoDB components to meet stringent <50ms P99 latency constraints without exceeding the 25,000 EUR monthly budget or overwhelming a 3-engineer team. Strict encryption, VPC endpoints, and IAM guardrails ensure PCI-DSS Level 1 compliance and 7-year auditability.]