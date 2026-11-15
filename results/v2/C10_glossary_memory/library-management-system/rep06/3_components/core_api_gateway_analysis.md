## Overview
The Library Management System provides cataloging, circulation, and self-service portals with strict EU data residency. The Core API Gateway manages edge security, routing, and traffic prioritization.

## Key Elements
- Core API Gateway (Envoy, Spring Cloud Gateway)
- Authentication Filter Component (Envoy OAuth2/OIDC filter)
- Rate Limiting Component (Redis-backed Token Bucket)
- Request Prioritization & Shaping Component (Envoy Traffic Director)
- Circuit Breaker & Resilience Component (Spring Cloud Circuit Breaker)
- Routing & Load Balancing Component (Spring Cloud Gateway)
- Catalog & Search Service (Java, Spring Boot, Elasticsearch)
- Circulation Service (Java, Spring Boot)
- EU Identity Provider (IdP) (OIDC)

## Relationships
- Library Patrons -> Core API Gateway: Sends API requests [HTTPS, TLS 1.3]
- Core API Gateway -> EU Identity Provider (IdP): Validates tokens [OIDC over HTTPS]
- Core API Gateway -> Catalog & Search Service: Routes queries [gRPC, mTLS]
- Core API Gateway -> Circulation Service: Routes requests [gRPC, mTLS]

## Technology Stack
- Envoy & Spring Cloud Gateway: Chosen for high-throughput, low-latency edge routing.
- Redis: Powers high-performance rate limiting aligned with EU data residency.
- gRPC with mTLS: Secures fast internal microservice communication.
- OpenTelemetry: Enables distributed tracing across gateway components.

## Rationale
This architecture enforces the sub-800ms search SLA (R-05) via targeted traffic shaping and circuit breakers. It secures patron and staff data while maintaining strict EU residency compliance.