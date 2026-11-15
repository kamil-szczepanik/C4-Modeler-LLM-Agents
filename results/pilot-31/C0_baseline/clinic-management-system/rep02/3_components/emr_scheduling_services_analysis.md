## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage patient admissions, EMRs, scheduling, and billing. It provides high-availability clinical services while ensuring strict HIPAA/GDPR compliance and interoperability via HL7 FHIR.

## Key Elements
*   **EMR/Scheduling Services (Java/Spring Boot):** Core business logic container.
*   **Internal Components:** Patient Record Manager, Scheduling Engine (Temporal.io), Resource Orchestrator, FHIR Facade.
*   **Data Tier:** PostgreSQL Cluster (with Patroni), Redis Cache, WORM Storage.
*   **Infrastructure:** Istio Service Mesh, NATS/Kafka Message Broker, FIPS 140-2 HSM.
*   **Sidecars:** Audit Logging Sidecar.

## Relationships
*   **Clinical/Patient Gateways -> EMR/Scheduling Services:** mTLS-secured routing via Istio.
*   **EMR/Scheduling Services -> PostgreSQL:** Optimistic locking for state consistency.
*   **EMR/Scheduling Services -> Redis:** Read-through cache for P95 latency.
*   **EMR/Scheduling Services -> Message Broker:** Asynchronous event-driven communication.
*   **Audit Logging Sidecar -> WORM Storage:** Tamper-proof log streaming.

## Technology Stack
*   **Temporal.io:** Orchestrates complex, fault-tolerant scheduling workflows.
*   **CQRS Pattern:** Decouples Command (write) and Query (read) sides for independent scaling.
*   **Istio Service Mesh:** Manages mTLS, circuit breaking, and canary deployments.
*   **PostgreSQL/Patroni:** High-availability relational storage with cross-region replication.
*   **ABAC (Attribute-Based Access Control):** Context-aware security for PHI access.
*   **FIPS 140-2 HSM:** Manages envelope encryption keys for data at rest.

## Rationale
The architecture utilizes CQRS and Temporal.io to balance high-volume scheduling writes with low-latency EMR reads, meeting the sub-second P95 requirement. A hybrid-cloud deployment with Istio and HSM integration ensures 99.99% availability and robust regulatory compliance.