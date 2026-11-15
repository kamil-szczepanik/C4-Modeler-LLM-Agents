## Overview
The API Gateway serves as a unified reverse proxy and security perimeter for the Library Management System, routing traffic for patrons and staff while enforcing EU data residency. It ensures high performance, supporting a <800ms search latency SLA (R-05) and secure catalogue management (R-01).

## Key Elements
- **API Gateway**: Nginx / Spring Cloud Gateway deployed as an auto-scaling cluster across EU availability zones.
- **Routing Filter / Route Locator**: Directs traffic and prioritizes low-latency search paths.
- **JWT Validation Filter**: Validates tokens locally using cached public keys with Redis-backed revocation blacklisting.
- **Rate Limiting Filter**: Enforces quotas using a distributed Redis cache co-located in the EU.
- **RBAC Enforcement Filter**: Evaluates route-level permissions to block unauthorized access.
- **Tracing Interceptor**: Injects W3C `traceparent` headers for distributed tracing.
- **Context Propagation Interceptor**: Propagates `X-User-Id` and `X-User-Roles` headers.

## Relationships
- **Patron Web Application -> API Gateway**: Sends API requests [HTTPS/REST]
- **Staff Administration Portal -> API Gateway**: Sends API requests [HTTPS]
- **API Gateway -> Core Domain Services**: Routes requests and propagates trace headers [mTLS]
- **API Gateway -> Identity Provider / SSO**: Fetches JWT validation keys [HTTPS/REST]
- **API Gateway -> Redis (EU region)**: Checks rate limits and token revocation [RESP/TCP]
- **API Gateway -> Logging & APM**: Exports metrics and traces [OTLP/gRPC]

## Technology Stack
- **Spring Cloud Gateway**: Core framework providing flexible reactive routing and filter pipelines.
- **Redis**: Distributed cache in the EU region for high-speed rate-limiting and token blacklisting.
- **Resilience4j**: Circuit breaking for upstream routes to handle downstream degradation.
- **TLS 1.3**: Secures edge communication with strict cipher suites and certificate pinning for mTLS.
- **OTLP/gRPC**: Protocol for exporting Prometheus metrics and distributed traces.

## Rationale
This architecture uses local JWT validation, co-located caching, and dedicated routing filters to guarantee the <800ms search response time (R-05). It strictly enforces EU-only data residency and role-based access control to protect patron and staff data.