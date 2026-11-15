## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and manage reviews. It ensures sub-50ms decision latency, 7-year tamper-evident auditability, and PCI-DSS Level 1 compliance on AWS.

## Key Elements
- Fraud Analysts, Risk & Compliance Officers, Fraud Engineers
- AWS API Gateway / Application Load Balancer
- Scoring Engine (Rust, AWS ECS Fargate)
- Case Management App (Node.js/Python + React SPA, AWS ECS Fargate)
- Model & Rule Management Service (Python/FastAPI, AWS ECS Fargate)
- Amazon Aurora PostgreSQL, Amazon S3, Amazon SNS, Amazon SQS
- External Systems: IdP, Payment Gateway, Audit Ledger

## Relationships
- Scoring Engine receives payment authorizations via HTTPS/TLS 1.3 from Payment Gateway.
- Model & Rule Management Service publishes cryptographically signed rule bundles via Amazon SNS to Scoring Engine for in-memory hot-reloading.
- Case Management App routes suspicious payments and interacts with Fraud Analysts via HTTPS.
- Model & Rule Management Service writes audit events to Audit Ledger and state to Amazon Aurora PostgreSQL.

## Technology Stack
- AWS ECS Fargate: Container orchestration for cost-effective microservices within the 25,000 EUR budget.
- Rust: High-performance language for the Scoring Engine to meet sub-50ms P99 latency.
- Python/FastAPI: Rapid development framework for the Model & Rule Management Service.
- Amazon Aurora PostgreSQL: Relational persistence for case data, rules, and transaction integrity.
- Amazon SNS: Pub/sub messaging for zero-downtime model and rule distribution.
- AWS KMS: Encryption at rest for card and model data satisfying PCI-DSS requirements.

## Rationale
This architecture decouples the low-latency scoring data plane from the administrative management plane, ensuring high performance under load. Strict security controls, immutable audit logging, and automated workflows satisfy all compliance mandates and budget constraints.