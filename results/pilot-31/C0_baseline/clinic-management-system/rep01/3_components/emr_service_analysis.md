## Overview
The Clinic Management System is a hybrid-cloud platform designed for clinical operations, providing high-availability patient record management, scheduling, and billing. It ensures HIPAA/GDPR compliance while delivering sub-second performance for critical clinical decision-making.

## Key Elements
*   **EMR Service:** Core component for clinical data management.
*   **Clinical Record Manager:** Handles ACID-compliant write operations.
*   **Clinical Read Model:** Optimized projection for low-latency data retrieval.
*   **Access Control Provider:** OPA-based authorization engine.
*   **Emergency Access Controller:** Manages clinical "break-glass" overrides.
*   **Audit Log Service:** Immutable, cryptographically signed event store.
*   **FHIR Integration Service:** External interoperability gateway.

## Relationships
*   **Clinical API Gateway -> EMR Service:** gRPC for internal routing.
*   **EMR Service -> FHIR Integration Service:** FHIR RESTful APIs for external data exchange.
*   **EMR Service -> Audit Log Service:** Asynchronous event streaming via sidecar pattern.
*   **Command/Query flow:** CQRS pattern using event sourcing to sync Record Manager with Read Model.
*   **Service Communication:** mTLS for all inter-service traffic.

## Technology Stack
*   **Database:** PostgreSQL with Citus (horizontal scaling/cross-site replication).
*   **Caching:** Redis (indexed cache for read-heavy clinical history).
*   **Authorization:** Open Policy Agent (OPA) sidecars with "fail-closed" policy enforcement.
*   **Architecture Pattern:** CQRS (Command Query Responsibility Segregation) for performance isolation.
*   **Infrastructure:** Hybrid Kubernetes (on-prem + AWS eu-central-1).
*   **Security:** AES-256 at rest, field-level encryption for PHI, and mTLS.

## Rationale
The CQRS pattern decouples write-heavy administrative tasks from read-heavy clinical queries, ensuring P95 latency requirements are met. The combination of OPA sidecars and a dedicated Emergency Access Controller balances strict HIPAA compliance with the clinical necessity of high availability and emergency overrides.