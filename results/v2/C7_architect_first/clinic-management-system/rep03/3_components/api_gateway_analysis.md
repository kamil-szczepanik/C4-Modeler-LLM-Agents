## Overview
• Manages patient admissions, EMRs, scheduling, and billing for clinics.
• Provides high-availability hybrid cloud architecture ensuring HIPAA and GDPR compliance.

## Key Elements
• TLS Termination & Ingress Controller (Kong Ingress Controller / Nginx)
• Authentication & JWT Validation Plugin (Kong OAuth2/OIDC Plugin with local JWKS)
• RBAC/ABAC Policy Enforcement Filter
• Rate Limiting & Throttling Filter (Kong Rate Limiting Plugin / Redis)
• Tenant-Aware Priority Router (Kong Upstream Service)
• Audit Logging & Redaction Filter

## Relationships
• Web Application (SPA) -> TLS Termination: Sends requests [HTTPS / TLS 1.3]
• Authentication Plugin -> Identity Provider (IdP): Fetches JWKS keys [HTTPS]
• Priority Router -> Core Services: Proxies prioritized requests [gRPC over mTLS]
• Audit Logging Filter -> Immutable Data Store: Streams redacted logs [Fluentbit over TLS]

## Technology Stack
• Kong / Nginx: API Gateway runtime and ingress routing for low latency and high throughput.
• Redis: Distributed caching and rate-limiting store.
• gRPC / mTLS: Secure, high-performance inter-service communication.
• JWT / JWKS: Decentralized, low-latency token verification.
• Kubernetes: Container orchestration for hybrid on-premise and AWS `eu-central-1` deployment.

## Rationale
• Active-active hybrid deployment guarantees 99.99% availability and low-latency access.
• Strict PHI redaction, mTLS, and RBAC ensure full HIPAA and GDPR compliance.