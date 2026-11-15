## Overview
The Clinic Management System is a hybrid-cloud platform designed for secure patient record management, scheduling, and billing. It ensures 99.99% availability and HIPAA/GDPR compliance through a hardened, resilient API gateway architecture.

## Key Elements
*   **Patient-Facing API Gateway:** Node.js/TypeScript-based edge entry point.
*   **Internal Components:** Authentication Interceptor (Passport.js), Request Orchestrator (Fastify), ReBAC Resolver, and Circuit-Breaker Fallback Handler.
*   **Infrastructure:** Istio Service Mesh, Redis (distributed cache), and WORM storage.
*   **Security Stack:** WAF (Edge), Audit Logging Sidecar, and Application-Level Encryption (ALE).

## Relationships
*   **Patients to Gateway:** HTTPS/mTLS for secure data access.
*   **Gateway to IdP:** OIDC/DPoP for identity validation and token binding.
*   **Gateway to Backend Services:** gRPC/REST via Istio service mesh with circuit breaking (Opossum).
*   **Gateway to Redis:** Localized caching for ReBAC decisions and read-only EMR snapshots.

## Technology Stack
*   **Runtime:** Node.js/TypeScript (Fastify) for high-concurrency request handling.
*   **Security:** DPoP for token replay prevention; ALE for cached PII/PHI protection.
*   **Resiliency:** Istio for cross-environment traffic shifting; Opossum for circuit breaking.
*   **Observability:** OpenTelemetry for distributed tracing and non-blocking audit logging.
*   **Deployment:** Hybrid K8s (On-prem + AWS) with blue-green traffic shifting.

## Rationale
This architecture utilizes a hardened edge gateway with ReBAC and circuit-breaker patterns to meet strict HIPAA/GDPR security mandates while maintaining 99.99% availability. The hybrid-cloud deployment and ALE-protected caching ensure system resilience and data integrity during downstream service outages.