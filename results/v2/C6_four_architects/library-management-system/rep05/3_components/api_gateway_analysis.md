## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The system enforces strict EU-only data residency and meets high-performance search requirements.

## Key Elements
- Web Application (SPA) (React/TypeScript)
- API Gateway Container (Envoy)
- Geo-Routing & Compliance Filter (Envoy Component)
- Authentication Filter (Envoy Component)
- Rate Limiting Filter (Envoy Component)
- Transformation Filter (Envoy Component)
- Routing & Dispatcher Engine with Circuit Breaker (Envoy Component)
- Core Services Container (Spring Boot / Java)
- Search Container (Elasticsearch Cluster)
- Cache / Session Store (Managed AWS Redis)
- LDAP/SAML IdP

## Relationships
- Web Application (SPA) -> API Gateway (Geo-Routing & Compliance Filter): Ingress point for all client requests [HTTPS/REST]
- API Gateway (Geo-Routing & Compliance Filter) -> API Gateway (Authentication Filter): Forwards validated, geo-compliant requests [In-memory]
- API Gateway (Authentication Filter) -> LDAP/SAML IdP: Validates user tokens [HTTPS/OIDC]
- API Gateway (Rate Limiting Filter) -> Cache / Session Store: Checks rate limit counters [RESP over TLS]
- API Gateway (Transformation Filter) -> API Gateway (Routing & Dispatcher Engine): Translates JSON to gRPC [In-memory]
- API Gateway (Routing & Dispatcher Engine) -> Core Services Container: Forwards requests with circuit breaking [gRPC]
- API Gateway (Routing & Dispatcher Engine) -> Search Container: Routes search queries [gRPC]

## Technology Stack
- Envoy: Selected for API Gateway due to native gRPC support, dynamic service discovery, and filter chain architecture.
- WebAssembly (WASM) / Lua: Utilized for custom geo-compliance filtering at the gateway perimeter.
- Spring Boot / Java: Powers backend business logic in the Core Services Container.
- Elasticsearch Cluster: Provides low-latency search capabilities.
- Managed AWS Redis: Handles caching, session storage, and rate-limiting counters.

## Rationale
The Envoy-based API Gateway utilizes a modular filter chain to enforce EU data residency and security at the perimeter while optimizing internal communication via gRPC. This architecture ensures low latency to meet the sub-800ms search performance requirement.