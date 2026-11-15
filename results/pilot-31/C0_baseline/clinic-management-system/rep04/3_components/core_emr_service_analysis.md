## Overview
The Core EMR Service is a high-availability, hybrid-cloud component designed to manage electronic medical records, clinical encounters, and interoperability. It ensures HIPAA/GDPR compliance while providing sub-second P95 latency for critical clinical workflows.

## Key Elements
*   **Core EMR Service (Spring Boot):** Primary transactional service.
*   **Components:** Patient Record Controller, Clinical Encounter Manager, Audit Trail Interceptor, FHIR Integration Gateway, Emergency Access Manager, Clinical Normalization Engine.
*   **Infrastructure:** PostgreSQL (CloudNativePG), HashiCorp Vault, Redis, OPA (Open Policy Agent) sidecar.
*   **External Systems:** Lab/Imaging Systems, Compliance/Audit Log Aggregator.

## Relationships
*   **Spring Cloud Gateway -> Core EMR:** mTLS-secured request forwarding.
*   **Core EMR -> PostgreSQL:** SQL transactions with Field-Level Encryption (FLE).
*   **Core EMR -> HashiCorp Vault:** API-based retrieval of per-record Data Encryption Keys (DEKs).
*   **FHIR Integration Gateway -> Lab/Imaging Systems:** HL7 FHIR protocol with circuit breaking (Resilience4j).
*   **Emergency Access Manager -> Audit Log:** Synchronous, high-priority immutable event logging.

## Technology Stack
*   **Spring Boot:** Foundation for microservices and event-driven architecture.
*   **HAPI FHIR:** Normalization of external lab data into a canonical internal model.
*   **OPA (Open Policy Agent):** Centralized Attribute-Based Access Control (ABAC) for clinical data.
*   **Redis:** Caching layer for FHIR resources to optimize latency.
*   **OpenTelemetry:** Distributed tracing across hybrid on-prem/AWS boundaries.
*   **Resilience4j:** Circuit breaking for external system dependencies.

## Rationale
The architecture utilizes asynchronous audit processing and Redis caching to meet sub-second P95 performance requirements for clinical staff. Field-level encryption and OPA-based authorization ensure strict regulatory compliance while supporting "break-glass" emergency access via an isolated, high-integrity component.