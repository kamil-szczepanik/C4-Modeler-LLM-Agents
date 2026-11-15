## Overview
[The system screens real-time card-not-present payment authorizations for fraud and manages case reviews for suspicious transactions. It ensures zero-downtime rule updates while meeting strict PCI-DSS Level 1 compliance and 7-year auditability mandates.]

## Key Elements
- Merchants / Payment Gateways
- Fraud Analysts, Data Scientists, and Risk Managers
- API Gateway / Tokenization Proxy (Envoy / AWS API Gateway)
- Real-Time Scoring Engine (Go / AWS ECS on Fargate, Redis)
- Case Management API (Node.js / Java Spring Boot)
- Rule & Model Distribution Service (Python / FastAPI + Pydantic, AWS S3, AWS SQS)
- Audit Log Sitter (Rust), AWS QLDB / S3 Object Lock

## Relationships
- Merchants send payment authorizations to API Gateway via HTTPS (REST/gRPC).
- Real-Time Scoring Engine evaluates transactions and fetches rules/models from AWS S3 via AWS SigV4.
- Rule & Model Distribution Service publishes update notifications to Scoring Engines via AWS SQS.
- Audit Log Sitter records tamper-evident logs to AWS QLDB / S3 via internal event streams.

## Technology Stack
- AWS (eu-west-1): Target cloud provider for scalability and compliance.
- Python / FastAPI + Pydantic: Management API for model ingestion and dry-run validation.
- Go: High-performance Real-Time Scoring Engine meeting sub-50ms P99 latency.
- AWS S3 & SQS: Durable artifact storage and decoupled, hash-based distribution notifications.
- AWS KMS & Cosign: Cryptographic signing and verification for R-06 auditability and zero-trust security.

## Rationale
[This architecture uses lightweight, managed AWS services and decoupled components to fit a 3-engineer team and 25,000 EUR monthly budget. It guarantees sub-50ms scoring latency, zero-downtime canary rollouts, and cryptographic immutability to satisfy PCI-DSS Level 1 and 7-year audit requirements.]