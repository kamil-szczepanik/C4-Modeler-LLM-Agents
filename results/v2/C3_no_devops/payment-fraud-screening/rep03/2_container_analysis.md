## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides a case management interface for analysts to review suspicious transactions. It ensures strict PCI-DSS compliance, 7-year auditability, and sub-50ms P99 latency within a fixed €25,000 monthly budget.

## Key Elements
- Fraud Analysts and Risk & Compliance Officers (Users)
- Payment Gateway / Processor Systems, Identity Provider (IdP), Notification Service, Audit Ledger (External Systems)
- API Gateway / Application Load Balancer (Ingress)
- Scoring Engine Container (Rust, AWS ECS Fargate)
- Case Management App Container (Node.js/Python backend + React SPA, AWS ECS Fargate)
- Model & Rule Management Service Container (AWS ECS Fargate)
- Data & Audit Tier (Amazon Aurora PostgreSQL, Amazon SQS, AWS Lambda, S3 WORM / Amazon QLDB)

## Relationships
- Payment Gateway to API Gateway (Synchronous REST/gRPC, TLS 1.3)
- API Gateway to Scoring Engine (Synchronous REST/gRPC, mTLS)
- Scoring Engine to Amazon Aurora PostgreSQL (Synchronous SQL, TLS 1.3)
- Scoring Engine to SQS audit pipeline (Asynchronous event streaming)
- SQS to Lambda to S3 WORM / Amazon QLDB (Asynchronous audit logging with cryptographic signing)
- Case Management App to Identity Provider (OAuth2/OIDC with short-lived JWTs)

## Technology Stack
- **Compute:** AWS ECS Fargate (chosen to eliminate Kubernetes operational overhead for a 3-engineer team).
- **Scoring Engine:** Rust (chosen for predictable performance, no GC pauses, and meeting sub-50ms P99 latency at 3,000 TPS).
- **Database & Storage:** Amazon Aurora PostgreSQL and Amazon S3 WORM / Amazon QLDB with AWS KMS (satisfies PCI-DSS and 7-year auditability).
- **Messaging:** Amazon SQS and AWS Lambda (decouples the latency-critical scoring path from audit logging).
- **Security:** AWS Secrets Manager, AWS KMS, AWS App Mesh / TLS 1.3, and AWS Signer.

## Rationale
This architecture uses managed AWS services and ECS Fargate to minimize operational overhead for a three-engineer team while easily adhering to the €25,000 monthly budget. By combining a high-performance Rust scoring engine with asynchronous, cryptographically signed audit logging, it guarantees sub-50ms latency, tamper-evident 7-year auditability, and PCI-DSS Level 1 compliance.