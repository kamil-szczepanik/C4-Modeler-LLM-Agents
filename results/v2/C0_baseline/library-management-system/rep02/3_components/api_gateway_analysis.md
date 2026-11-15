## Overview
The Library Management System provides catalogue and circulation services for public and academic libraries. The architecture enforces strict EU data residency and high-performance search capabilities.

## Key Elements
- API Gateway (Kong/Envoy)
- Self-Service Portal & Staff Management Console (React/Nginx)
- Backend Services: Catalogue Service, Circulation Management, Search Engine (ElasticSearch)
- External Systems: EU Identity Provider, EU Payment Gateway, EU Notification Service
- Infrastructure: Redis (Local Caching/Rate Limiting), WAF, Kafka/Fluentbit (Audit Logging)

## Relationships
- Self-Service Portal -> API Gateway: Routes requests [HTTPS/JSON REST]
- Staff Management Console -> API Gateway: Routes requests [HTTPS/REST]
- API Gateway -> Catalogue Service / Search Engine: Routes traffic [gRPC/HTTP2]
- API Gateway -> EU Identity Provider: Validates OIDC tokens and fetches JWKS [HTTPS]

## Technology Stack
- Kong/Envoy: Core API Gateway technology for routing and plugin extensibility
- OpenTelemetry: Distributed tracing (W3C Trace Context) and Prometheus metrics for latency tracking
- Redis: In-memory caching for JWKS and rate-limiting counters
- Mutual TLS (mTLS): Secures internal communication channels across backend containers

## Rationale
This architecture uses an optimized API Gateway with local JWKS caching and gRPC routing to achieve the required 99th-percentile search response under 800 ms. Strict mTLS, claim sanitization, and PII log scrubbing ensure complete compliance with EU data residency constraints.