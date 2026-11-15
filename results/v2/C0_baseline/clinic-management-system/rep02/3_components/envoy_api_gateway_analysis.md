## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and interoperability with external medical systems.

## Key Elements
- **Envoy API Gateway (Envoy):** Manages edge routing, security, and traffic prioritization.
- **Router Component:** Handles dynamic ingress routing and virtual hosts.
- **External Authorization Filter (Envoy Ext-Authz / OPA):** Validates JWT tokens and scopes.
- **Traffic Priority & Rate Limiting Filter:** Enforces tiered quotas using a Redis backend.
- **WASM Security & Sanitization Filter:** Performs real-time PII masking.
- **Telemetry & Metrics Emitter (OpenTelemetry):** Exports traces and audit logs.
- **Domain Microservices (Spring Boot / Kubernetes / Istio):** Processes clinical and administrative logic.
- **Redis Rate Limit Store:** Multi-region replicated cluster for rate limiting.

## Relationships
- **Clients -> Envoy API Gateway:** Routes ingress traffic via `HTTPS / REST / JSON` with TLS 1.3 termination.
- **Envoy API Gateway -> Domain Microservices:** Forwards authenticated traffic via `gRPC over mTLS (Istio)`.
- **Traffic Priority Filter -> Redis Rate Limit Store:** Fetches token counts via `Redis Protocol / TCP`.
- **External Authorization Filter -> Identity Provider:** Validates tokens via `gRPC`.
- **Telemetry Emitter -> Observability Stack:** Exports logs and metrics via `OTLP / gRPC`.

## Technology Stack
- **Envoy Proxy:** Chosen as the edge gateway for low-latency routing, circuit breaking, and filter extensibility.
- **Open Policy Agent (OPA):** Used with Ext-Authz for dynamic, policy-based access control.
- **Rust / WASM:** Powers lightweight, high-performance edge PII masking and sanitization.
- **Redis:** Provides fast, in-memory rate-limit state management across hybrid regions.
- **Istio & mTLS:** Secures service-to-service communication with strict SPIFFE ID validation.

## Rationale
This architecture ensures sub-second P95 performance and 99.99% availability through hybrid active-active deployments and intelligent traffic prioritization. It guarantees HIPAA/GDPR compliance via strict edge security, mTLS service mesh isolation, and immutable audit logging.