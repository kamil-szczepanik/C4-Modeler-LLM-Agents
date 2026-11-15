## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals to handle patient admissions, EMRs, scheduling, and billing securely. It guarantees HIPAA/GDPR compliance, a 99.99% uptime SLA, and long-term data retention.

## Key Elements
- **Envoy API Gateway / Edge Proxy:** Edge layer routing traffic and enforcing security.
- **Listener & TLS Termination Component (C++):** Handles TLS 1.3 and WAF filtering.
- **Auth & Authorization Filter (Lua/External):** Validates OAuth2/OIDC JWTs, scopes, and persona-based rate limits.
- **Routing & Load Balancing Engine:** Manages circuit breaking and mTLS to backend services.
- **Telemetry & Audit Emitter:** Streams PII-sanitized OpenTelemetry logs.
- **Backend Services:** EMR & Scheduling, Billing & Claims, and FHIR Interoperability Services.
- **External Systems:** Centralized SIEM, HashiCorp Vault, and Global Traffic Manager.

## Relationships
- **Global Traffic Manager -> Envoy API Gateway:** Routes external traffic via [DNS / HTTPS].
- **React Clients -> Envoy API Gateway:** Sends API requests with OAuth2/OIDC tokens via [HTTPS / TLS 1.3].
- **Envoy API Gateway -> EMR / Billing / FHIR Services:** Routes internal requests via [Internal mTLS via Istio/Linkerd].
- **Envoy API Gateway -> Centralized SIEM:** Streams sanitized telemetry via [gRPC / TLS 1.3].
- **Envoy API Gateway -> HashiCorp Vault:** Fetches JWKS keys and secrets via [HTTPS / Vault API].

## Technology Stack
- **Envoy Proxy:** Core edge proxy and load balancer for high performance and hybrid deployment support.
- **OpenTelemetry / gRPC:** For real-time, non-blocking telemetry streaming to the SIEM.
- **HashiCorp Vault:** For dynamic secrets management, JWKS caching, and TLS certificate storage.
- **Prometheus:** For native metrics scraping and operational alerting.

## Rationale
This architecture uses Envoy at the edge to offload critical security, rate-limiting, and TLS termination, protecting backend microservices. Local-memory token-buckets and robust circuit breaking guarantee high availability (99.99%) without introducing centralized points of failure.