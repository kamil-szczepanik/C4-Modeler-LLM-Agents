## Overview
The Clinic Management System is a hybrid-cloud platform providing secure, high-availability clinical operations including EMR, scheduling, and billing. It serves as a centralized hub for clinical and administrative staff, ensuring HIPAA/GDPR compliance and sub-second performance for critical patient data.

## Key Elements
*   **Spring Cloud Gateway:** Centralized ingress for traffic routing, security, and traffic shaping.
*   **OPA (Open Policy Agent) Sidecar:** Local Policy Decision Point (PDP) for ABAC enforcement.
*   **Redis:** Caching layer for JWT validation and OIDC introspection.
*   **Istio/Linkerd:** Service mesh for cross-cluster failover and mTLS management.
*   **Core Services:** EMR Service, Billing Service, and Audit Visualization Service.

## Relationships
*   **Client to Gateway:** TLS 1.3 encrypted ingress for Patient/Admin portals.
*   **Gateway to IdP:** OIDC/OAuth2 for authentication.
*   **Gateway to Downstream Services:** mTLS-encrypted communication with `X-Correlation-ID` propagation.
*   **Gateway to OPA:** Local sidecar communication for ABAC policy enforcement.
*   **Gateway to Redis:** Low-latency token/cache lookups.

## Technology Stack
*   **Spring Cloud Gateway:** Utilizes Project Reactor for non-blocking I/O to meet P95 latency goals.
*   **Open Policy Agent (OPA):** Implements Policy-as-Code for granular, role-based access control.
*   **Redis:** Provides high-speed caching for token introspection and rate-limiting.
*   **Istio/Linkerd:** Manages hybrid-cloud traffic, mTLS, and cross-region failover.
*   **OpenTelemetry:** Injected for distributed tracing and latency correlation.

## Rationale
This architecture uses a non-blocking, modular gateway design to ensure high-performance request processing and strict security enforcement. By utilizing sidecars for policy and caching, the system maintains the required 99.99% availability and 1s P95 latency while meeting stringent HIPAA/GDPR auditability standards.