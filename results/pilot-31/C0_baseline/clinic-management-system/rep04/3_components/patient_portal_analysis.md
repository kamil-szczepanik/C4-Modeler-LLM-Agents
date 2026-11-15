## Overview
The Patient Portal is a secure, mobile-responsive interface enabling patients to self-manage appointments, view EMR data, and communicate with care teams. It acts as a thin, HIPAA-compliant gateway that enforces strict data isolation and authorization across a hybrid cloud infrastructure.

## Key Elements
*   **Authentication Component:** OIDC/OAuth2 integration with IdP.
*   **Appointment Manager:** gRPC client for scheduling services.
*   **Records Viewer:** FHIR-compliant data fetcher.
*   **Relationship Manager:** Handles delegation and proxy access logic.
*   **Messaging Gateway:** WebSocket-based service for secure communication.
*   **Audit Logging Interceptor:** Asynchronous sidecar for forensic tracking.

## Relationships
*   **Patients to Patient Portal:** HTTPS access with mTLS.
*   **Patient Portal to Spring Cloud Gateway:** REST/gRPC routing.
*   **Messaging Gateway to HashiCorp Vault:** Key retrieval for application-level encryption.
*   **Backend Services to IdP:** Claims-Based Access Control (CBAC) validation.

## Technology Stack
*   **Next.js (React):** Server-side rendering to minimize client-side PHI exposure.
*   **gRPC/WSS:** Protobuf-based service communication and real-time messaging.
*   **HashiCorp Vault:** Centralized secret management for message-level encryption.
*   **OpenTelemetry:** Distributed tracing for cross-environment observability.
*   **K8s (Hybrid):** On-prem and AWS deployment with Pod Disruption Budgets for 99.99% availability.

## Rationale
This architecture uses a thin, SSR-based portal to minimize client-side PII exposure while enforcing strict server-side authorization and audit logging. The hybrid deployment with asynchronous sidecars ensures the system meets 99.99% availability and HIPAA requirements without compromising EMR retrieval performance.