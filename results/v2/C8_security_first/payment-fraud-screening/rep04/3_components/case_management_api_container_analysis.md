## Overview
- This system screens card-not-present payment authorizations for fraud in real-time while providing a case management interface for fraud analysts.
- It ensures PCI-DSS Level 1 compliance, explainable decisions, and 7-year tamper-evident auditability under a strict cloud budget.

## Key Elements
- Fraud Analysts & Risk Operations
- Compliance & Audit Officer
- Envoy Proxy
- Scoring Engine Container (Go)
- Case Management API Container (Node.js with NestJS)
- Audit & Compliance Ledger Container
- Amazon Aurora PostgreSQL
- AWS QLDB
- Amazon SQS

## Relationships
- Fraud Analysts -> Case Management API Container: Review flagged transactions [Corporate IdP Authentication / HTTPS]
- Case Management API Container -> Amazon Aurora PostgreSQL: Reads/writes operational state and queries read replicas [TLS / Prisma ORM]
- Case Management API Container -> Amazon SQS: Publishes bulk decision jobs [AWS SDK / TLS]
- Case Workflow Service -> Audit & Compliance Ledger Container: Forwards immutable audit trails [gRPC / TLS]
- Audit Query Component -> AWS QLDB: Queries decision histories for compliance [AWS SDK / TLS]

## Technology Stack
- Node.js with NestJS: Provides a robust framework for building the Case Management API Container with strict DTO validation (`class-validator`).
- AWS ECS with Fargate: Runs containerized services scalably within a 25,000 EUR monthly budget.
- Amazon Aurora PostgreSQL: Stores transactional operational state using read replicas to isolate heavy read loads.
- AWS QLDB: Delivers native immutability and cryptographic verification for 7-year auditability.
- Amazon SQS: Decouples batch processing to prevent API timeouts and database contention.

## Rationale
- The architecture isolates high-throughput real-time scoring from analyst workflows using asynchronous messaging and dedicated containers.
- Managed AWS services and explicit component boundaries satisfy strict PCI-DSS Level 1, auditability, and budgetary constraints for a small engineering team.