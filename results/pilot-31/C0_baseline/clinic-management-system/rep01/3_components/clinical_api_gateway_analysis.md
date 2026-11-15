## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage clinical workflows, EMR data, and billing for hospitals. It ensures 99.99% availability and HIPAA/GDPR compliance while providing low-latency access for clinical staff.

## Key Elements
*   **Personas:** Clinical Staff, Patients, Administrative Auditors, Third-Party Integrators.
*   **Containers:** Clinical API Gateway (Go), EMR Service (Java/Spring Boot), Billing Service (Python/FastAPI), FHIR Integration Service (Java), Audit Log Service (Go/S3 Glacier).
*   **Infrastructure:** On-prem Kubernetes, AWS (eu-central-1), Keycloak (OIDC Provider), NATS/Kafka (Audit stream).

## Relationships
*   **Clinical Staff/Patients -> Clinical API Gateway:** HTTPS/mTLS.
*   **Clinical API Gateway -> EMR/Billing Services:** gRPC with circuit-breaker pattern.
*   **Clinical API Gateway -> FHIR Integration Service:** REST/FHIR.
*   **Clinical API Gateway -> Audit Log Service:** Asynchronous event streaming via NATS/Kafka.

## Technology Stack
*   **Go & Envoy Proxy:** High-performance routing, mTLS termination, and QoS traffic prioritization.
*   **gRPC-web:** Minimizes serialization overhead for frontend-to-gateway communication.
*   **Keycloak (OIDC):** Centralized identity management with Token Binding (RFC 8471).
*   **Istio/Linkerd:** Service mesh for cross-environment mTLS and traffic management.
*   **OpenTelemetry:** Distributed tracing for observability and latency monitoring.
*   **OpenAPI/Swagger:** Automated documentation for third-party integrators.

## Rationale
The Go/Envoy-based gateway architecture ensures sub-second performance for clinical staff through request prioritization and gRPC optimization. The hybrid-cloud service mesh and asynchronous audit logging satisfy strict 99.99% availability and HIPAA/GDPR compliance requirements without compromising system throughput.