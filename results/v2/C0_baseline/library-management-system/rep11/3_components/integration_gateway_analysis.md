## Overview
[The Integration Gateway for the Library Management System routes, secures, and manages all ingress and egress traffic for public and academic library portals. It enforces strict EU data residency constraints while protecting the 99th-percentile search response SLA (< 800 ms).]

## Key Elements
- Kong / Envoy API Gateway
- API Router Component (Kong/Envoy Core)
- Authentication & Authorization Plugin Component
- Data Residency Enforcement Plugin
- Transformation & Header Injection Component
- Circuit Breaker & Resilience Component
- Patron Self-Service Portal & Librarian Workbench
- Catalog API & Search Service
- EU Identity Provider & EU Payment Gateway
- Redis (Shared Token Bucket Store)

## Relationships
- Web Application Firewall (WAF) -> Integration Gateway [HTTPS / REST over TLS 1.3]
- Patron Self-Service Portal -> Integration Gateway [HTTPS / REST over TLS 1.3]
- Integration Gateway -> Catalog API & Search Service [gRPC over mTLS with OAuth2/OIDC token validation]
- Integration Gateway -> EU Payment Gateway [HTTPS / REST over TLS 1.3]
- Integration Gateway -> EU Notification Service [HTTPS / REST over TLS 1.3]
- Integration Gateway -> EU Identity Provider [OIDC/OAuth2 over HTTPS]
- Integration Gateway -> Asynchronous Processing Worker [gRPC over mTLS]
- Integration Gateway -> Central Logging & Monitoring SIEM [OpenTelemetry with PII sanitization]

## Technology Stack
- Kong / Envoy API Gateway: Chosen for high-performance routing and rich plugin extensibility.
- Redis: Used as a shared token bucket store for distributed rate-limiting to protect backend search performance.
- OpenTelemetry & W3C Trace Context: Mandated for standardized distributed tracing across services.
- Kubernetes & ArgoCD: Used for multi-AZ deployment and GitOps-driven zero-downtime rollouts.
- mTLS & TLS 1.3: Enforced for secure east-west and north-south communication.

## Rationale
[This architecture enforces strict EU data residency and robust security controls without compromising performance. Distributed rate-limiting, caching, and circuit-breaking protect the sub-800ms search SLA under load.]