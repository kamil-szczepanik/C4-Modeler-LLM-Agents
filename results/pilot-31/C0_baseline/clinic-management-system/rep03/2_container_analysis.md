## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage patient EMRs, scheduling, and billing for clinical environments. It ensures high availability and regulatory compliance while providing low-latency access to medical data.

## Key Elements
*   **Users:** Clinical Staff, Patients, Hospital Administrators.
*   **Core Services:** Patient Service (Java/Spring Boot), EMR Service (Node.js/Fastify), Billing Service (Go), Patient Portal Service (Next.js).
*   **Integration/Security:** API Gateway (Kong), FHIR Integration Gateway (HAPI FHIR), Istio Service Mesh, NATS JetStream (Event Bus).
*   **Infrastructure:** Hybrid Kubernetes (On-prem & AWS eu-central-1), PostgreSQL, Redis, ArgoCD.

## Relationships
*   **API Gateway (Kong):** Manages OAuth2/OIDC and mTLS for all internal/external traffic.
*   **NATS JetStream:** Handles asynchronous audit logging and FHIR-based diagnostic data ingestion.
*   **FHIR Gateway:** Maps internal models to HL7 FHIR R4; uses mTLS for external diagnostic system handshakes.
*   **Service Mesh (Istio):** Enforces mTLS, circuit breaking, and traffic management across hybrid clusters.

## Technology Stack
*   **Kubernetes:** Orchestration for hybrid-cloud deployment with GitOps (ArgoCD).
*   **PostgreSQL/Redis:** Relational storage for billing and caching for EMR session states.
*   **Istio & Kong:** Service mesh and API gateway for secure, high-availability traffic routing.
*   **KMS/HSM:** Envelope encryption for AES-256 data at rest.
*   **Falco:** Runtime security scanning for anomalous process detection.

## Rationale
The architecture utilizes microservices and Kubernetes to meet 99.99% availability and high-performance requirements through active-active deployments. Security is enforced via mTLS, network isolation, and WORM-compliant audit logging to satisfy strict HIPAA and GDPR compliance mandates.