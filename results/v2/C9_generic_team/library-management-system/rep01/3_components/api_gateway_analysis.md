## Overview
The Library Management System provides cataloging, circulation management, and self-service portals for academic and public libraries. The API Gateway serves as the single secure entry point enforcing routing, security, and performance constraints.

## Key Elements
- Self-Service Portals and Kiosks
- API Gateway
- API Composition / BFF Container
- Core Domain Services
- Caching Layer (Redis)
- Observability & Logging Container
- Configuration & Feature Management Container

## Relationships
- Self-Service Portals and Kiosks -> API Gateway: HTTPS/REST
- API Gateway -> API Composition / BFF Container: HTTP/REST
- API Gateway -> Caching Layer (Redis): In-memory / TCP
- API Gateway -> Observability & Logging Container: Centralized metrics and tracing

## Technology Stack
- API Gateway: HTTP/REST, TLS termination, W3C Trace Context
- Authentication: OAuth2/JWT token introspection at the edge
- Error Handling: RFC 7807 (Problem Details for HTTP APIs)
- Observability: Prometheus-compatible `/metrics` endpoint
- Caching & Idempotency: Redis for mutating request protection
- Configuration: Dynamic declarative routing via Configuration Container

## Rationale
This architecture ensures strict EU data residency compliance, resilient edge traffic management, and low-latency responses meeting the < 800 ms search SLA. Centralizing cross-cutting concerns at the API Gateway decouples downstream business logic and protects internal domain services.