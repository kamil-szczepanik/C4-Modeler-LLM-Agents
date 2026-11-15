## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage patient admissions, EMRs, scheduling, and billing. It provides a secure, high-availability interface for patients and caregivers to access health records and clinical services.

## Key Elements
*   **Patient Portal (Node.js/React):** Frontend and orchestration layer.
*   **Identity Provider Interface (Auth0/OIDC):** Handles MFA and authentication.
*   **Patient Dashboard Controller (Express.js/GraphQL Federation):** Aggregates backend data.
*   **Relationship Management Component:** Manages delegated access for caregivers.
*   **Real-time Messaging Gateway (Socket.io):** Enables secure clinical communication.
*   **Service Mesh (Istio):** Manages cross-cluster traffic and mTLS.
*   **Backend Services:** EMR (Java/Spring Boot), Billing (Python/FastAPI).

## Relationships
*   **Patients/Caregivers -> Patient Portal:** HTTPS/TLS 1.3 with MFA.
*   **Patient Portal -> Backend Services:** mTLS via Istio service mesh.
*   **Portal -> Identity Provider:** OIDC for token introspection.
*   **Portal -> Backend:** GraphQL queries with field-level authorization.

## Technology Stack
*   **GraphQL Federation:** Efficient data aggregation for mobile performance.
*   **Istio:** Enables service discovery, mTLS, and observability across hybrid clusters.
*   **Redis:** Distributed edge caching to meet P95 latency requirements.
*   **Auth0/OIDC:** Standardized MFA and identity management.
*   **Resilience4j:** Circuit breakers for backend service fault tolerance.
*   **WORM Storage:** Immutable audit logging for HIPAA/GDPR compliance.

## Rationale
This architecture utilizes GraphQL Federation and service mesh orchestration to ensure sub-second P95 performance while maintaining strict security boundaries. The hybrid-cloud deployment with automated failover and ABAC ensures 99.99% availability and regulatory compliance for sensitive PHI.