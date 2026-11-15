## Overview
The Clinic Management System is a hybrid-cloud platform designed for managing patient records, scheduling, and billing in compliance with HIPAA/GDPR. It ensures 99.99% availability and high-performance clinical workflows through a modular, event-driven architecture.

## Key Elements
*   **EMR Service Components:** Record Processor, Audit Manager, FHIR Facade, Compliance Reporter.
*   **Data Layer:** Primary PostgreSQL (Transactional), Analytical PostgreSQL (Read-Replica), Redis (Session Cache).
*   **Infrastructure:** NATS JetStream (Event Bus), Kong (API Gateway), HAPI FHIR (Integration).
*   **Security:** HSM/KMS (Key Management), SIEM Integration, Egress Gateway.

## Relationships
*   **Record Processor ↔ NATS JetStream:** Asynchronous event streaming for audit and analytical updates [NATS Protocol].
*   **FHIR Facade ↔ Patient Portal:** Secure, protocol-translated access via HL7 FHIR [REST/HTTPS].
*   **EMR Service ↔ PostgreSQL:** Cross-region replication with automated failover [PostgreSQL Protocol].
*   **Inter-service:** mTLS-encrypted communication for all internal traffic [gRPC/REST].

## Technology Stack
*   **Node.js/Fastify:** High-performance runtime for EMR service components.
*   **PostgreSQL (CQRS):** Separates transactional and analytical workloads to meet P95 latency requirements.
*   **NATS JetStream:** Ensures message persistence and decoupling across hybrid cloud boundaries.
*   **OpenTelemetry:** Distributed tracing to monitor latency and system health.
*   **AES-256/mTLS:** Standardized encryption for data at rest and in transit.

## Rationale
The CQRS pattern isolates high-load clinical operations from analytical and research queries, ensuring P95 latency targets are met. Decoupling audit logging via an immutable ledger and event-driven architecture guarantees strict compliance without compromising clinician workflow performance.