## Overview
The Billing & Claims Container manages financial transactions, patient payments, and automated insurance claim submissions for the Clinic Management System. It ensures secure processing, strict regulatory compliance, and high availability across hybrid cloud environments.

## Key Elements
- Billing Specialists (Users)
- Billing & Claims Container (Node.js / Express)
- Billing API Controller (Express.js)
- Claim Validation & Mapping Engine (TypeScript / AJV)
- Payment & Clearinghouse Integration Service (Axios / Node SDKs)
- Idempotent Dispatcher Middleware
- Transaction & DLQ Manager
- Ledger & Audit Writer (TypeORM)
- Primary DB & Audit Store (PostgreSQL with Patroni)
- Third-Party Payment Gateway & Insurance Clearinghouse (External Systems)

## Relationships
- API Gateway -> Billing API Controller: Routes validated requests [TLS / JWT / HTTP]
- Billing API Controller -> Claim Validation & Mapping Engine: Passes billing data for validation [Internal Function Call]
- Payment & Clearinghouse Integration Service -> Third-Party Payment Gateway: Processes co-pays and balances [HTTPS / REST]
- Payment & Clearinghouse Integration Service -> Insurance Clearinghouse: Submits insurance claims [HTTPS / REST]
- Transaction & DLQ Manager -> Ledger & Audit Writer: Logs transactions and failed payloads [Internal Function Call]
- Ledger & Audit Writer -> Primary DB & Audit Store: Enforces ACID-compliant writes [PostgreSQL Protocol, AES-256]

## Technology Stack
- Node.js & Express: Lightweight container runtime for high-throughput billing APIs
- TypeScript & AJV: Ensures strict schema validation for claim rules
- TypeORM: Manages database interactions and immutable transaction ledgers
- PostgreSQL with Patroni: Provides high-availability relational data storage with AES-256 encryption
- Prometheus & OpenTelemetry: Enables distributed tracing and circuit breaker metrics

## Rationale
This architecture ensures financial compliance, zero data loss, and high availability (99.99%) through strict idempotency controls and dead-letter queues. The component decomposition directly minimizes claim rejections and revenue leakage while satisfying the 10-year data retention mandate.