## Overview
The Billing Service is a containerized Node.js/Express subsystem within the Clinic Management System that automates insurance claims, payment processing, and patient billing. It ensures secure, high-availability financial operations compliant with HIPAA, GDPR, and PCI-DSS mandates across a hybrid cloud infrastructure.

## Key Elements
- Claim Management Component (Node.js module)
- Payment Processing Component (Node.js module)
- Ledger & Invoicing Component (Node.js module)
- Billing Event Handler Component (Node.js / Kafka Consumer)
- Patient Billing Portal API Component (Express router)
- Infrastructure & Storage: Redis, PostgreSQL with Citus, Kafka/RabbitMQ, Istio, ArgoCD

## Relationships
- Core Services -> Billing Service: Asynchronous event streaming via Kafka with payload-level encryption
- Billing Service -> Payment Gateway: Processes patient credit card and digital wallet transactions via HTTPS and TLS 1.3
- Billing Service -> Insurance Clearinghouses: Transmits and validates insurance claims via HTTPS and TLS 1.3
- Billing Service -> Centralized Vault: Fetches dynamic runtime secrets via AppRole tokens
- Billing Service -> SIEM / Observability System: Sends tracing telemetry using W3C Trace Context and OpenTelemetry

## Technology Stack
- Node.js / Express: Chosen for lightweight API routing and asynchronous I/O with worker threads for serialization
- Redis: Implements distributed locks for transaction idempotency and duplicate prevention
- PostgreSQL with Citus: Persists financial ledgers with parameterized queries and application-layer encryption
- Apache Kafka: Handles event-driven messaging and Dead Letter Queues (DLQ)
- Istio Service Mesh: Enforces STRICT mTLS, circuit breakers, and traffic splitting

## Rationale
This architecture uses asynchronous messaging, distributed Redis locks, and Istio circuit breakers to guarantee 99.99% availability and prevent duplicate transactions during network partitions. Strict mTLS, TLS 1.3 pinning, tokenization, and BOLA prevention ensure full compliance with HIPAA, GDPR, and PCI-DSS standards.