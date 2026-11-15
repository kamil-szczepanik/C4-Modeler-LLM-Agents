## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations for a mid-size payment processor. It provides automated fraud scoring, case management for analysts, and immutable compliance auditing.

## Key Elements
- Payment Gateway
- AWS API Gateway & Internal Network Load Balancer (NLB)
- Scoring Engine Container (Rust or Go)
- Case Management API Container (Node.js/Python)
- Fraud Analyst SPA (Single Page Application)
- S3 Model Registry & S3 Object Lock
- Amazon SQS (Audit Queue)
- AWS QLDB (Quantum Ledger Database)
- AWS KMS & AWS Secrets Manager

## Relationships
- Payment Gateway interacts with AWS API Gateway via HTTPS/TLS 1.3
- Scoring Engine receives gRPC payloads from internal NLB
- Case Management API communicates with Fraud Analyst SPA via REST/JSON over HTTPS
- Scoring Engine pushes audit events asynchronously to Amazon SQS
- Audit QLDB persists tamper-evident records via SQS triggers

## Technology Stack
- **Cloud Provider:** AWS (eu-west-1 region)
- **Compute:** AWS ECS Fargate for container orchestration
- **Scoring Runtime:** Rust or Go for <50ms P99 latency
- **Database / Audit:** AWS QLDB and S3 Object Lock for 7-year tamper-evident retention
- **Security:** AWS KMS, AWS Secrets Manager, and ACM Private CA for PCI-DSS Level 1 compliance
- **Infrastructure as Code:** AWS CDK managed by a 3-engineer team within a 25,000 EUR monthly budget

## Rationale
The architecture cleanly separates high-throughput scoring from analyst workflows to meet strict sub-50ms P99 latency SLAs under high transaction volumes. Asynchronous SQS queues and managed AWS services minimize operational overhead, fitting the constraints of a three-engineer team and a fixed monthly budget.