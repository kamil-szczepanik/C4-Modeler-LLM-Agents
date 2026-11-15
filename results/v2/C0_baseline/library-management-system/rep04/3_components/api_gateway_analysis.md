## Overview
[Library Management System] provides catalogue, circulation, and self-service portals for public and academic libraries while ensuring EU-only data residency. The API Gateway manages incoming traffic, security, and routing to core services.

## Key Elements
- **Users**: Library Patrons, Librarians, Administrators
- **External Systems**: Identity Provider (IdP), Payment Gateway, Notification Service
- **Containers**: Web App/SPA (React/TypeScript, CDN), API Gateway (Envoy), Core Services Container (Java/Spring Boot), Search Container (Elasticsearch), Audit Container (Go), Message Broker (Kafka/RabbitMQ), Database (PostgreSQL)
- **API Gateway Components**: Authentication Filter (`envoy.filters.http.oauth2`), Rate Limiting Filter (Redis token-bucket), Request Transformation Filter, W3C Trace Injector, Routing & Upstream Cluster Manager (with Circuit Breaker), OpenAPI Schema Validation Filter

## Relationships
- Web App/SPA -> API Gateway: Communicates with backend APIs [HTTPS, TLS 1.3]
- API Gateway -> Core Services Container: Routes traffic, API requests, and injects trusted identity headers [gRPC/REST over mTLS]
- API Gateway -> Audit Container: Emits Prometheus metrics and structured access logs [gRPC]
- API Gateway -> External Identity Provider (IdP): Validates OAuth2/OIDC tokens [HTTPS]

## Technology Stack
- **API Gateway**: Envoy (selected for native filter extensibility and performance)
- **Rate Limiting State**: Redis (used for token-bucket tracking to protect against abuse)
- **Observability**: Prometheus (metrics), W3C Trace Context (distributed tracing)
- **Security & Secrets**: mTLS, OpenAPI schema enforcement, Kubernetes CSI / SPIFFE/SPIRE (short-lived certificates)

## Rationale
[This architecture enforces a single secure entry point that centralizes cross-cutting concerns like OAuth2 validation, rate limiting, and mTLS to protect patron privacy and meet EU data residency constraints. Component-level Envoy extensions and circuit breaking ensure high availability and sub-800ms search performance under load.]