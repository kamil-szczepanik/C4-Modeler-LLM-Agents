## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for clinics and hospitals. The architecture ensures 99.99% availability, HIPAA/GDPR compliance, and low-latency clinical workflows.

## Key Elements
- Edge Router & Reverse Proxy (Envoy)
- Authentication & Authorization Filter (OAuth2/OIDC + OPA)
- Rate Limiter & Circuit Breaker (Redis-backed with local token-bucket caching)
- API Versioning & Transformation Filter
- Request Deduplication & Idempotency Module
- Core Business Services (Go / Spring Boot)
- Compliance & Reporting Service

## Relationships
- Medical Staff, Administrators, Patients, Billing Specialists -> Edge Router: External access [HTTPS, TLS 1.3]
- Edge Router -> Authentication Filter: Request interception [In-memory / gRPC]
- Authentication Filter -> Redis: Token validation cache lookup [RESP / TLS]
- Authentication Filter -> API Versioning Filter: Passes validated claims [In-memory]
- API Versioning Filter -> Core Business Services: Forwards payloads [gRPC / mTLS via Istio]
- Edge Router -> Compliance & Reporting Service: Audit log routing [HTTPS]

## Technology Stack
- Envoy / Nginx: Edge routing, TLS termination, and WAF security controls for perimeter defense
- OAuth2/OIDC & Open Policy Agent (OPA): Perimeter authentication and RBAC/ABAC enforcement
- Redis: Localized token-bucket caching and idempotency tracking with active-active replication
- Istio Service Mesh: Manages mTLS encryption-in-transit and blue/green traffic splitting
- Go / Spring Boot: High-performance backend core services

## Rationale
This hybrid cloud architecture guarantees high availability (99.99%) through active-active replication, Istio traffic splitting, and resilient localized caching. Strict perimeter security, TLS 1.3, mTLS, token binding, and data sanitization ensure full HIPAA and GDPR compliance without compromising sub-second EMR performance.