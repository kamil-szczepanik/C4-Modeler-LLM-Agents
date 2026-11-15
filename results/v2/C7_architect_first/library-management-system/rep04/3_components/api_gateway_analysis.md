## Overview
The Library Management System provides cataloging, circulation, and self-service portals for academic and public libraries. The API Gateway orchestrates client traffic, enforces security, and ensures strict EU data residency compliance.

## Key Elements
- Web App (SPA): React application hosted via Nginx
- API Gateway: Spring Cloud Gateway container
- Internal Components: Routing Filter, Auth Filter, Rate Limiting & Resiliency, Distributed Tracing Filter, Token Translation Component
- External Systems: Identity Provider (IdP), Payment Gateway, Notification Service
- Core Services: Spring Boot backend containers
- Infrastructure: Redis (EU-only), Prometheus, Grafana, Kubernetes HPA

## Relationships
- Web App (SPA) -> API Gateway: Sends API requests [HTTPS with TLS 1.3]
- Routing & Load Balancing Filter -> Core Services Container: Proxies requests [gRPC over mTLS with W3C Trace Context]
- Auth Filter -> Identity Provider (IdP): Validates OAuth2/OIDC JWT tokens
- API Gateway -> Redis: Checks token bucket rate-limiting [Encrypted at rest, EU-only]

## Technology Stack
- Spring Cloud Gateway: Chosen for microservice routing and reactive filter architecture
- Resilience4j & Redis: Implements circuit breakers and rate-limiting to protect backend SLAs (<800ms search)
- W3C Trace Context & Prometheus/Grafana: Enables distributed tracing and custom metric-based HPA scaling
- OpenAPI / RFC 7807: Enforces strict input schema validation and standardized error responses

## Rationale
This architecture ensures secure, compliant data handling within EU boundaries while maintaining high-performance SLAs under peak academic loads. Token translation and edge validation protect backend systems from unauthorized access and injection risks.