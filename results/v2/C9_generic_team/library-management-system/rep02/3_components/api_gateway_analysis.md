## Overview
The Library Management System provides catalogue management, circulation, and self-service portals for public and academic libraries. The architecture enforces EU-only data residency and maintains a 99th-percentile search response time under 800 ms.

## Key Elements
* Web Application (SPA): Frontend client served via CDN
* API Gateway: Edge component handling routing, security, caching, and resiliency
* Core Business Services: Decoupled microservices architecture
* Search Engine Container: Elasticsearch/OpenSearch
* Database Container: PostgreSQL
* Shared Caching Container: Redis
* Identity and Access Management (IAM) Provider: OAuth2/OIDC service
* Centralized Audit and Logging System: System for metrics and telemetry

## Relationships
* Web Application (SPA) -> API Gateway: Sends user requests [HTTPS/TLS]
* API Gateway -> Core Business Services: Routes validated requests [gRPC/REST]
* API Gateway -> Identity and Access Management (IAM) Provider: Validates IAM tokens [OAuth2/OIDC]
* API Gateway -> Shared Caching Container: Caches frequent search queries and serves fallback responses [Redis Protocol]
* API Gateway -> Centralized Audit and Logging System: Emits request telemetry and access logs [HTTPS]

## Technology Stack
* API Gateway: Custom edge router with integrated TLS termination, rate limiting, and circuit breaker patterns
* Shared Caching Container: Redis for edge response caching and fallback data
* Search Engine Container: Elasticsearch/OpenSearch for catalogue searches meeting R-05 (<800 ms)
* Database Container: PostgreSQL for persistent transactional storage respecting EU-only data residency

## Rationale
The edge-focused API Gateway architecture offloads cross-cutting concerns like TLS termination, token validation, caching, and compression, protecting downstream microservices. This design ensures strict compliance with EU data residency while leveraging Redis caching and circuit breaking to consistently meet the 800 ms search latency requirement.