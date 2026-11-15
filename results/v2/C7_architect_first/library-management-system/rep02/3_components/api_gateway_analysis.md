## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU-only data residency constraints. The API Gateway container is decomposed into distinct components to guarantee sub-800ms search performance and robust security.

## Key Elements
- **Web Application (SPA)**: React/TypeScript frontend served via CDN used by patrons, staff, and administrators.
- **Routing & Upstream Component**: Kong Proxy (Lua/Nginx core) handling reverse proxying, load balancing, circuit breaking, and fallback responses.
- **Authentication & Authorization Component**: Kong OIDC / JWT Plugin enforcing edge validation of JSON Web Tokens.
- **Rate Limiting & Security Component**: Kong plugins enforcing role-aware throttling and WAF payload inspection.
- **Telemetry Emission Component**: OpenTelemetry and Prometheus plugin capturing metrics and scrubbing PII for EU compliance.
- **Core Services API**: Node.js/NestJS downstream services receiving proxied gRPC traffic.

## Relationships
- Web Application (SPA) -> Authentication & Authorization Component: Sends requests [HTTPS / JSON]
- Authentication & Authorization Component -> Rate Limiting & Security Component: Passes enriched context [Internal Lua context]
- Rate Limiting & Security Component -> Routing & Upstream Component: Forwards sanitized requests
- Routing & Upstream Component -> Core Services API: Proxies payload [gRPC / mTLS 1.3]
- Telemetry Emission Component -> Analytics Event Collector: Streams logs and metrics [HTTP / TLS 1.3]

## Technology Stack
- **API Gateway**: Kong (Lua/Nginx core) for edge routing, security, and native plugin extensibility.
- **Protocol**: gRPC with mTLS 1.3 and certificate pinning for internal service-to-service communication.
- **Configuration**: Deck (GitOps) for declarative, auditable infrastructure and policy management.
- **Observability**: OpenTelemetry and Prometheus for custom metrics, tracing, and autoscaling.
- **Secrets Management**: HashiCorp Vault for secure injection and rotation of mTLS certificates and OIDC secrets.

## Rationale
This component-based API Gateway architecture ensures strict EU data residency compliance, zero-trust edge security, and robust fault tolerance. Role-aware throttling and circuit-breaking timeouts protect downstream services to consistently achieve the 99th-percentile search latency SLA under 800ms.