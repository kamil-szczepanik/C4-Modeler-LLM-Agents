## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. The billing container specifically accelerates revenue cycle management, claim validation, and payment reconciliation while maintaining strict HIPAA and GDPR compliance.

## Key Elements
- Billing Specialist: User persona initiating claim submissions and managing financial records.
- Billing API Controller: Node.js/Go component handling incoming REST/gRPC requests via mTLS.
- Claim Validation Engine: Node.js/Go component executing real-time business rule validation against cached schemas.
- Payment & Claims Service: Node.js/Go component managing secure outbound integrations.
- Remittance Ingestion Worker: Node.js/Go background worker processing asynchronous ERA/835 payloads.
- Billing Data Access Layer: Node.js/Go component interacting with PostgreSQL and Redis.
- Apache Kafka: Event broker utilized for the Outbox Pattern and Dead Letter Queue (DLQ).
- External Payment Gateway / Insurance Clearinghouse: External system handling financial transactions and claims.

## Relationships
- API Gateway -> Billing API Controller: Routes billing requests [HTTPS / gRPC with mTLS]
- Billing API Controller -> Claim Validation Engine: Internal function call
- Claim Validation Engine -> Payment & Claims Service: Validated claim payload [Internal via Apache Kafka]
- Payment & Claims Service -> External Payment Gateway / Insurance Clearinghouse: Submits claims and processes payments [TLS 1.3 with mTLS]
- External Payment Gateway / Insurance Clearinghouse -> Remittance Ingestion Worker: Delivers ERA/835 payloads [HTTPS / SFTP over TLS 1.3]
- Remittance Ingestion Worker -> Billing Data Access Layer: Reconciles and updates patient ledger [SQL over TLS]

## Technology Stack
- Node.js / Go: Chosen for high-performance, low-latency API and background worker execution.
- PostgreSQL with Redis Caching: Provides ACID compliance for financial ledgers and rapid schema lookups.
- Apache Kafka: Enables asynchronous messaging, Outbox Pattern, and Dead Letter Queue (DLQ) implementation.
- TLS 1.3 and mTLS: Mandated for secure external communication and cryptographic identity verification.
- OpenTelemetry: Enforces distributed tracing across all internal component calls.

## Rationale
This architecture ensures 99.99% high availability and fault tolerance through stateless horizontal pod scaling and asynchronous queueing mechanisms. It guarantees strict HIPAA and GDPR compliance via end-to-end encryption, role-based access control, and least-privilege data segregation.