## Overview
[A secure, high-performance API Gateway built on Kong for the Library Management System, providing edge routing, security enforcement, and observability for public and academic library portals.]

## Key Elements
- **Routing Engine (Kong Proxy)**: Handles API versioning, priority routing for Library Staff, and downstream traffic direction.
- **Authentication Filter (Kong OIDC Plugin)**: Performs local JWT/OIDC token validation at the edge.
- **Rate Limiting & Circuit Breaker**: Protects downstream services and enforces throttling on search/auth endpoints.
- **Security & Telemetry Enforcers**: Injects security headers, sanitizes inputs, and emits OpenTelemetry/Prometheus metrics.

## Relationships
- **Web Application -> Routing Engine**: Forwards versioned client requests [HTTPS/REST using TLS 1.3]
- **Routing Engine -> Core Domain Service & Search Service**: Proxies validated traffic [gRPC with mTLS]
- **Routing Engine -> Telemetry Exporter**: Emits distributed traces and Prometheus metrics [Internal]

## Technology Stack
- **Kong API Gateway**: Selected for its robust plugin ecosystem and low-latency edge processing.
- **DB-less Kubernetes Mode**: Eliminates stateful database dependencies at the edge to support EU data residency and GitOps.
- **gRPC with mTLS**: Ensures secure, high-performance service-to-service communication.
- **OpenTelemetry & Prometheus**: Enables distributed tracing to meet the <800ms search SLA.

## Rationale
[The DB-less Kong architecture eliminates external edge latency while enforcing strict EU data residency compliance. Furthermore, priority routing, local JWT validation, and gRPC/mTLS guarantee rapid, secure self-service portal performance.]