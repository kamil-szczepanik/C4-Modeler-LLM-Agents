## Overview
The Patient Portal Service is a secure, high-availability web interface enabling patient self-service, care plan management, and caregiver access. It serves as the primary engagement layer for the Clinic Management System to reduce administrative burden and improve clinical outcomes.

## Key Elements
*   **UI Orchestrator:** Next.js (SSR) for accessible, responsive patient engagement.
*   **Patient Context Provider (BFF):** Node.js service aggregating EMR and Billing data.
*   **Consent Manager:** Go-based service enforcing ABAC for "Family Access" and granular permissions.
*   **Security Proxy Layer:** Enforces OIDC/MFA and CSP policies.
*   **API Gateway:** Kong (via Istio) for traffic routing and mTLS termination.

## Relationships
*   **Client to UI Orchestrator:** HTTPS/TLS 1.3 with "SameSite=Strict" cookies.
*   **UI Orchestrator to BFF:** gRPC for low-latency internal communication.
*   **BFF to Consent Manager:** gRPC with mandatory ACL validation.
*   **Internal Services to API Gateway:** mTLS-encrypted communication for all PHI requests.

## Technology Stack
*   **Next.js:** Server-Side Rendering for performance and SEO/Accessibility.
*   **gRPC:** High-performance internal service communication with strict schema contracts.
*   **Redis:** Distributed caching for session data and UI state.
*   **Istio:** Service mesh for traffic shifting (blue-green), observability, and mTLS.
*   **ABAC (Attribute-Based Access Control):** Logic for managing complex caregiver/family permissions.
*   **Field-Level Encryption (FLE):** Application-layer encryption for PHI using HSM-backed keys.

## Rationale
This architecture utilizes a BFF pattern and gRPC to minimize latency and attack surface, meeting the <1s P95 performance requirement. The decoupling of the Consent Manager ensures robust, auditable HIPAA/GDPR compliance for complex family-access scenarios within a hybrid cloud environment.