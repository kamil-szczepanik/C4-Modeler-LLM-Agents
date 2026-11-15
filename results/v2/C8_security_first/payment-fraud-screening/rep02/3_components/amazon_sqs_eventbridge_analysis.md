## Overview
Real-Time Payment Fraud Screening screens card-not-present payment authorizations for fraud before approval and provides case management for suspicious payments. It ensures sub-50ms latency, PCI-DSS Level 1 compliance, and 7-year tamper-evident auditability within a 25,000 EUR monthly budget operated by three engineers.

## Key Elements
- Fraud Analyst & Risk Manager
- Payment Gateway / Acquirer
- Payment Network / Card Brands (Visa/Mastercard)
- Core Ledger / Compliance Archive
- AWS API Gateway (Ingress/TLS Termination)
- Go Scoring Engine (Go, AWS ECS on Fargate)
- Node.js Case Management (Node.js, AWS ECS on Fargate)
- Amazon EventBridge Bus (`fraud-events-bus`)
- Amazon SQS Queue (`audit-queue`) with Dead-Letter Queue (DLQ)
- Audit Buffer Worker (AWS Lambda)
- Amazon Aurora PostgreSQL Serverless v2
- AWS QLDB
- AWS Cognito & AWS Secrets Manager

## Relationships
- Fraud Analyst & Risk Manager -> AWS API Gateway: HTTPS over TLS 1.3 [HTTPS/TLS 1.3]
- Payment Gateway -> AWS API Gateway: Payment authorization requests [HTTPS/TLS 1.3]
- AWS API Gateway -> Go Scoring Engine: Routes authorization requests [HTTP/REST over AWS VPC PrivateLink]
- AWS API Gateway -> Node.js Case Management: Case review operations [HTTP/REST over AWS VPC PrivateLink]
- Go Scoring Engine -> Amazon EventBridge / SQS: Publishes scoring decisions and audit streams using batching [AWS SDK over AWS PrivateLink]
- Amazon SQS Queue -> Audit Buffer Worker: Long polling integration [AWS SDK]
- Audit Buffer Worker -> AWS QLDB: Writes tamper-evident audit logs [AWS QLDB Ledger API via AWS PrivateLink]
- Node.js Case Management -> Amazon Aurora PostgreSQL Serverless v2: Persists case data [PostgreSQL Wire Protocol over AWS VPC PrivateLink]

## Technology Stack
- AWS ECS on Fargate: Runs containerized Go and Node.js workloads without server management for a 3-engineer team.
- Amazon EventBridge & SQS: Decouples real-time scoring from async auditing to maintain sub-50ms latency (R-04) and handle 3,000 TPS spikes.
- AWS Lambda: Buffer worker for cost-effective, auto-scaling QLDB ingestion within budget.
- AWS QLDB: Provides immutable, tamper-evident audit trails for 7-year compliance (R-06).
- Amazon Aurora PostgreSQL Serverless v2: Scalable relational storage for case management data.
- AWS KMS & PrivateLink: Enforces encryption-at-rest with segregated keys and isolates traffic from the public internet for PCI-DSS compliance.

## Rationale
This architecture uses fully managed AWS services to minimize operational overhead for a three-engineer team while staying under the 25,000 EUR budget. Asynchronous decoupling via SQS, EventBridge, and Lambda ensures the system meets the strict sub-50ms latency requirement (R-04) while guaranteeing 7-year auditability (R-06) and PCI-DSS compliance.