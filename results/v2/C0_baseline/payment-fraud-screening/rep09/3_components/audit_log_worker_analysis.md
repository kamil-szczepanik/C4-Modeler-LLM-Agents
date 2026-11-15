## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud prior to approval and provides case management for suspicious payments. It ensures PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a fixed monthly infrastructure budget.

## Key Elements
- Fraud Analyst & Risk Officer
- Payment Gateway / Core Processing Platform
- Identity Provider (IdP)
- SIEM / Compliance Archive
- API Gateway (Envoy) (Envoy, AWS ECS Fargate)
- Real-Time Scoring Engine (Go, ONNX Runtime, AWS ECS Fargate)
- Case Management Backend (Node.js / Spring Boot, AWS ECS Fargate)
- Web Application (React SPA, AWS S3, CloudFront)
- Audit Log Worker (Go, AWS ECS Fargate)
- Redis (ElastiCache) (Redis, AWS ElastiCache)
- AWS Aurora PostgreSQL (PostgreSQL, AWS Aurora)
- Amazon SQS (Amazon SQS)

## Relationships
- API Gateway (Envoy) -> Real-Time Scoring Engine: Forwards authorization requests [gRPC / TLS 1.3]
- Real-Time Scoring Engine -> Redis (ElastiCache): Fetches sliding-window velocity counters [Redis TCP Protocol / TLS]
- API Gateway (Envoy) -> Case Management Backend: Routes analyst review actions [HTTPS / REST]
- Case Management Backend -> AWS Aurora PostgreSQL: Reads/writes review cases and decisions [PostgreSQL Wire Protocol / IAM-authenticated TLS]
- Real-Time Scoring Engine -> Amazon SQS: Publishes asynchronous decision and audit events [AWS SDK / HTTPS]
- Amazon SQS -> Audit Log Worker: Delivers asynchronous audit logs [SQS Polling]
- Audit Log Worker -> AWS Aurora PostgreSQL: Persists canonicalized, hash-chained logs into append-only partitioned tables [PostgreSQL Wire Protocol / IAM-authenticated TLS]
- Audit Log Worker -> SIEM / Compliance Archive: Forwards batched audit logs with local disk spooling [HTTPS / TLS 1.3 with pinned certificates]
- Web Application -> API Gateway (Envoy): Accesses frontend assets and backend APIs [HTTPS / TLS 1.3]

## Technology Stack
- **AWS ECS Fargate**: Container orchestration chosen for zero-server management overhead, aligning with the 3-engineer team constraint.
- **Go**: Language selected for high-throughput, low-latency components (Scoring Engine, Audit Log Worker) and minimal memory footprint.
- **ONNX Runtime**: Embedded inference engine for running fraud scoring models with sub-50ms P99 latency.
- **AWS Aurora PostgreSQL**: Relational database utilizing table partitioning to manage 7-year audit data growth efficiently.
- **Amazon SQS with DLQ**: Messaging queue providing asynchronous decoupling and zero data loss guarantees for compliance workflows.
- **AWS KMS**: Hardware-backed Key Management Service providing cryptographic keys for SHA-256 tamper-evident hash chaining.
- **AWS S3 & Glacier Flexible Retrieval**: Object storage tiered via lifecycle policies to archive audit logs for 7 years within the €25,000 monthly budget.

## Rationale
This architecture meets sub-50ms P99 latency and strict PCI-DSS Level 1 compliance by decoupling real-time scoring from asynchronous compliance logging. Leveraging serverless and managed AWS services minimizes operational burden for a three-engineer team while guaranteeing 7-year tamper-evident auditability.