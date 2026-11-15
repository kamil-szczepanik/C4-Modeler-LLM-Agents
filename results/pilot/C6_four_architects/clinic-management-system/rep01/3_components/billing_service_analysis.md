## Overview
The Clinic Management System is a clinical IT platform that manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA and GDPR compliance while maintaining 99.99% high availability across hybrid cloud infrastructures.

## Key Elements
- Invoice Engine & Pricing Cache (Node.js, Redis)
- Claim Submitter & X12 EDI Formatter (Node.js, XState, ANSI X12 837/835)
- Payment Gateway Integrator & PCI-DSS Tokenizer (Node.js, HTTPS/TLS 1.3, Resilience4J)
- Webhook Receiver & Signature Verifier (Express.js, Node.js Crypto)
- Batch Settlement Processor & Statement Generator (Node.js Worker Threads, PDFKit)
- Ledger Auditor & Analytics Emitter (gRPC, Unix Domain Sockets, ClickHouse)

## Relationships
- Billing Service -> PostgreSQL Container cluster: Executes transactional queries and connection pooling [SQL / gRPC]
- Claim Submitter -> Apache Kafka StatefulSet: Streams financial events [TLS / KafkaJS]
- X12 EDI Formatter -> RabbitMQ Container cluster: Dispatches clearinghouse payloads [AMQP 0-9-1]
- Statement Generator -> MinIO Object Storage Gateway Container: Uploads PDF statements [HTTPS / S3 API]
- Ledger Auditor -> Audit & Compliance Sidecar Container: Streams audit events [Local gRPC]

## Technology Stack
- Node.js & TypeScript: Core runtime and type safety for billing microservices
- PostgreSQL: ACID-compliant persistence with multi-tenant schemas
- Redis: In-memory pricing cache and distributed locking via Redlock
- Apache Kafka & RabbitMQ: Asynchronous event streaming and resilient message queuing
- MinIO: S3-compatible object storage for generated patient billing statements

## Rationale
This architecture uses decoupled asynchronous workers and robust state machines to handle high-volume financial transactions without event loop starvation. Strict data segregation, tokenization, and cryptographic auditing ensure full compliance with healthcare security mandates.