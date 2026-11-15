## Overview
The Administrative Dashboard is a centralized Angular-based operational hub for clinical and administrative staff. It provides secure, high-performance access to patient EMRs, billing, and scheduling within a hybrid cloud environment.

## Key Elements
*   **Users:** Clinical Staff, Administrative Staff.
*   **Frontend Components:** Auth Guard, NgRx State Management, API Client Layer, UI Policy Engine, Context Orchestrator.
*   **Infrastructure:** Spring Cloud Gateway (with gRPC-Web proxy), On-prem K8s, AWS eu-central-1.
*   **Observability:** OpenTelemetry, Synthetic Monitoring, Core Web Vitals tracking.

## Relationships
*   **Dashboard to Gateway:** REST/gRPC-Web for service communication and real-time streaming.
*   **Dashboard to Identity Provider (IdP):** OIDC/JWT for authentication and ABAC claims.
*   **Cross-Module Communication:** RxJS-based event bus for state synchronization.
*   **Security:** mTLS termination at Gateway; CSP headers; Web Crypto API for local encryption.

## Technology Stack
*   **Framework:** Angular (with NgRx for state, lazy-loading for performance).
*   **Communication:** gRPC-Web (type-safe streaming), Axios (interceptors for audit logging).
*   **Security:** OIDC/JWT, ABAC (Attribute-Based Access Control), Web Crypto API.
*   **Observability:** OpenTelemetry (distributed tracing), synthetic monitoring.
*   **Deployment:** Blue-green with automated canary analysis; HPA for frontend assets.

## Rationale
The component-based Angular architecture with lazy-loading and a UI Policy Engine ensures sub-1s performance and strict separation of clinical/billing workflows. Hybrid deployment with circuit breaking and synthetic monitoring supports the 99.99% availability requirement while maintaining HIPAA/GDPR compliance.