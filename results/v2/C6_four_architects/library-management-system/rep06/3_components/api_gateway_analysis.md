## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within EU-only data residency constraints. The API Gateway container manages edge routing, security, and traffic control for downstream services.

## Key Elements
- **Users**: Patron, Librarian, Library Administrator
- **External Systems**: External Payment Gateway, Digital Content Providers, Notification Service, Integrated Library System (ILS) / Legacy Data Source
- **Containers**: Web Application, API Gateway, Core Domain Service, Search Service, Integration Service, PostgreSQL, Elasticsearch, Redis, RabbitMQ
- **API Gateway Components**: SSL/TLS Termination & Reverse Proxy (NGINX), Routing Filter Component (Spring Cloud Gateway), Authentication & Authorization Component (Spring Security / OAuth2), Rate Limiting & Throttling Component (Redis-backed), Telemetry & Request Tracing Component (Micrometer / OpenTelemetry), Circuit Breaker & Fallback Component (Resilience4j), Request Validation Component (Spring Validation), Caching Component (Spring Cache)

## Relationships
- `Web Application` -> `SSL/TLS Termination & Reverse Proxy`: Sends encrypted client traffic [HTTPS]
- `Web Application` -> `Authentication & Authorization Component`: Authenticates users [HTTPS / OAuth2]
- `SSL/TLS Termination & Reverse Proxy` -> `Routing Filter Component`: Forwards decrypted traffic [HTTP/2]
- `Routing Filter Component` -> `Core Domain Service`: Forwards circulation requests [gRPC over mTLS]
- `Routing Filter Component` -> `Search Service`: Forwards search queries [gRPC over mTLS]
- `Circuit Breaker & Fallback Component` -> `Integration Service`: Forwards third-party and legacy requests [gRPC over mTLS]
- `Caching Component` -> `Redis`: Reads/writes cache entries [RESP / TCP]

## Technology Stack
- **NGINX**: Edge termination, reverse proxy, and initial request buffering
- **Spring Cloud Gateway**: Dynamic routing and filter-based extensibility
- **Spring Security / OAuth2**: Token validation for users
- **Redis**: Distributed rate-limiting and response caching
- **Resilience4j**: Circuit breaking and fallback protection
- **Micrometer / OpenTelemetry**: Telemetry and distributed tracing
- **gRPC over mTLS**: Secure internal communication protocol

## Rationale
This architecture uses NGINX and Spring Cloud Gateway to efficiently handle edge security and routing while meeting the <800ms search SLA. Distributed caching and circuit breakers with Redis and Resilience4j ensure high availability and low latency within EU data residency rules.