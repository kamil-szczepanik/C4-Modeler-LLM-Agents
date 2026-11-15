## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud, providing sub-50ms decisions and case management for analysts. It ensures PCI-DSS Level 1 compliance and 7-year tamper-evident auditability within a fixed budget and small engineering team.

## Key Elements
- Fraud Analysts & Risk Operations
- Compliance & Audit Officer
- Payment Gateway / Core Processing Platform
- Card Networks / Tokenization Service
- Corporate Identity Provider (OIDC/SAML)
- AWS KMS & Secrets Manager
- Envoy Proxy
- Scoring Engine Container (Go)
- Case Management API Container (Node.js with NestJS)
- Audit & Compliance Ledger Container (Go / ECS Fargate)
- Amazon ElastiCache / SQS
- Amazon Aurora PostgreSQL
- AWS QLDB
- Amazon S3

## Relationships
- Payment Gateway / Core Processing Platform -> Envoy Proxy: Forwards payment authorization requests [HTTPS / gRPC]
- Envoy Proxy -> Scoring Engine Container: Routes requests for real-time fraud scoring [gRPC]
- Scoring Engine Container -> Amazon Aurora PostgreSQL: Reads fraud rules and scoring parameters [PostgreSQL Wire Protocol]
- Scoring Engine Container -> Amazon ElastiCache / SQS: Dispatches audit events and case triggers [Queue Protocol]
- Amazon ElastiCache / SQS -> Audit & Compliance Ledger Container: Streams decision payloads for ledger ingestion [Queue Protocol]
- Audit & Compliance Ledger Container -> AWS QLDB: Commits tamper-evident audit records [PartiQL / AWS SDK]
- Compliance & Audit Officers -> Audit & Compliance Ledger Container: Queries decision histories and exports reports [REST / OIDC]

## Technology Stack
- **Go:** Powers the Scoring Engine and Audit & Compliance Ledger for minimal memory footprint and low latency.
- **Node.js with NestJS:** Used for the Case Management API to ensure rapid feature development and maintainability.
- **AWS QLDB:** Provides cryptographically verifiable, immutable journals for mandatory 7-year auditability.
- **Amazon Aurora PostgreSQL:** Delivers high-performance, relational storage for rules, models, and case data.
- **Amazon ECS Fargate:** Runs containerized services with auto-scaling to control operational overhead.
- **Amazon SQS / ElastiCache:** Buffers asynchronous events and guarantees backpressure handling.

## Rationale
This architecture combines high-throughput, low-latency technologies like Go and gRPC with serverless AWS primitives to meet sub-50ms P99 latency at 3,000 TPS. Managed services and containerization on ECS Fargate minimize operational overhead, allowing a three-person engineering team to maintain PCI-DSS compliance within a 25,000 EUR monthly budget.