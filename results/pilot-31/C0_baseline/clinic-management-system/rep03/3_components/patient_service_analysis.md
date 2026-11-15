## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage patient admissions, EMRs, and billing for medium-sized hospitals. It serves as a secure, high-availability source of truth for patient demographics and clinical records.

## Key Elements
*   **Users:** Clinical Staff, Patients, Hospital Administrators.
*   **Containers:** Patient Service (Java/Spring Boot), EMR Service (Node.js), Billing Service (Go), Patient Portal (Next.js), API Gateway (Kong), FHIR Integration Gateway (HAPI FHIR).
*   **Internal Components:** Registration Controller, Demographics Manager, Identity Validator, Audit Logger, Patient Profile Projection.
*   **Infrastructure:** NATS JetStream, PostgreSQL, Redis, OPA (Open Policy Agent), Istio Service Mesh, Debezium (CDC).

## Relationships
*   **API Gateway -> Patient Service:** Routes requests via Istio (mTLS).
*   **Patient Service -> EMR Service:** Retrieves medical records via gRPC/REST.
*   **Patient Service -> NATS JetStream:** Publishes immutable audit logs.
*   **Patient Service -> PostgreSQL:** Persists demographic data with TDE and field-level encryption.
*   **PostgreSQL -> Projection Schema:** Synchronized via Debezium CDC for read-optimized clinical views.
*   **OPA Sidecar -> Patient Service:** Enforces ABAC-based authorization for all requests.

## Technology Stack
*   **Java/Spring Boot:** Core logic with Spring WebFlux for high-concurrency intake.
*   **PostgreSQL:** Primary storage with TDE and HSM-backed CMK for HIPAA/GDPR compliance.
*   **NATS JetStream:** Durable, asynchronous messaging for audit trails.
*   **Open Policy Agent (OPA):** Sidecar-based ABAC policy enforcement.
*   **Istio:** Service mesh for mTLS and circuit breaking.
*   **Debezium:** CDC for maintaining read-optimized CQRS projections.

## Rationale
This architecture uses CQRS and CDC to decouple high-throughput registration from read-heavy clinical access, ensuring sub-second latency for staff. The hybrid-cloud deployment combined with OPA and mTLS provides the necessary security and 99.99% availability required for compliant, clinical-grade operations.