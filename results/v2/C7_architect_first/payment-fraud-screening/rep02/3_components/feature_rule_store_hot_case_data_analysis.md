## Overview
Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud at 3,000 TPS, routing suspicious transactions for analyst review while maintaining PCI-DSS Level 1 compliance.

## Key Elements
- Fraud Analysts and Compliance Auditors
- AWS API Gateway (REST) and AWS Network Load Balancer (NLB)
- Fraud Scoring Engine (Go, Amazon ECS on EC2)
- Case Management Backend (Node.js/TypeScript, Amazon ECS Fargate)
- Fraud Analyst UI (React SPA, Amazon S3, Amazon CloudFront)
- Feature/Rule Store & Hot Case Data (Amazon DynamoDB, DAX, AWS AppConfig)
- Audit Log Store (Amazon Aurora PostgreSQL with ledger tables)
- Identity & Security Service (AWS Cognito, AWS Secrets Manager, AWS KMS)

## Relationships
- Fraud Scoring Engine -> Feature/Rule Store & Hot Case Data: Queries features and rules via [AWS SDK using IAM Roles / TLS 1.3]
- Case Management Backend -> Feature/Rule Store & Hot Case Data: Reads/writes hot case data via [AWS SDK / HTTPS/TLS 1.3]
- DynamoDB Streams -> Audit Log Store: Streams database mutations for tamper-evident tracking via [AWS Lambda / Internal AWS API]
- Fraud Scoring Engine -> AWS AppConfig: Polls and caches scoring rules locally via [AppConfig Agent]

## Technology Stack
- Amazon DynamoDB & DAX: Chosen for low-latency feature lookups and hot case persistence to meet the <50ms P99 latency SLA.
- AWS AppConfig: Utilized for zero-downtime rule distribution with built-in schema validation to eliminate custom sidecar complexity.
- AWS KMS: Implemented with Customer Managed Keys (CMK) and automatic annual rotation for data-at-rest encryption.
- DynamoDB Streams & Amazon Aurora PostgreSQL: Deployed for capturing immutable change logs to satisfy 7-year auditability.

## Rationale
This architecture uses fully managed AWS services to meet strict P99 latency (<50ms) and PCI-DSS Level 1 security requirements within a fixed €25,000 monthly budget. It enables a three-engineer team to operate the platform reliably while ensuring 7-year auditability and zero-downtime rule updates.