## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and provides case management workflows for analysts. It is deployed on AWS in region `eu-west-1` to meet strict compliance, low-latency, and budgetary constraints.

## Key Elements
- Fraud Analysts, Regulatory / Compliance Auditors
- Payment Gateway / Acquirer Systems, Identity Provider (IdP), External Tokenization/Vault Service
- AWS API Gateway (REST)
- Scoring Engine (Go, AWS ECS Fargate)
- Case Management Backend (Node.js/Go, AWS ECS Fargate)
- Amazon DynamoDB (`FraudRulesTable`, `CaseManagementTable`)
- Amazon Aurora PostgreSQL
- Amazon Kinesis Data Firehose
- Amazon S3 with Object Lock

## Relationships
- Scoring Engine -> `FraudRulesTable`: Reads and writes rule/model state via AWS SDK / HTTPS (TCP 443) using Consistent Read
- Case Management Backend -> `CaseManagementTable`: Reads and writes analyst workflow state via AWS SDK / HTTPS (TCP 443)
- Payment Gateway -> AWS API Gateway: Submits authorization requests via HTTPS (REST)

## Technology Stack
- AWS API Gateway: Manages and secures incoming HTTP REST traffic
- Go & Node.js on AWS ECS Fargate: Provides high-throughput, low-latency containerized compute within budget
- Amazon DynamoDB: Single-table design with composite primary keys (`RuleType`, `RuleID`) for sub-50ms rule retrieval
- Amazon Aurora PostgreSQL: Relational storage for transactional case management data
- Amazon S3 with Object Lock: Tamper-evident 7-year audit log storage

## Rationale
This architecture uses serverless and managed AWS services on ECS Fargate and DynamoDB to process 3,000 TPS under 50ms P99 latency while strictly enforcing the €25,000 monthly budget. Strict data isolation, tokenization, and S3 Object Lock ensure full PCI-DSS Level 1 compliance and 7-year auditability.