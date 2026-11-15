## Overview
The Library Management System provides a catalogue, circulation management, and self-service portals for public and academic libraries. It enforces strict EU-only data residency and high-performance search SLAs.

## Key Elements
- Library Patrons, Librarians/Circulation Staff, Library Administrators
- EU-hosted Identity Provider (IdP)
- CDN/WAF Edge Services
- API Gateway (Istio Service Mesh / Kubernetes Gateway)
- Patron Portal (Web Frontend / Backend Service)
- Circulation & Cataloguing Container (Java / Microservice)
- Elasticsearch Container (Elasticsearch)
- Kafka/Redpanda Event Streaming Container (Apache Kafka / Redpanda)
- PostgreSQL Database (PostgreSQL)

## Relationships
- CDN/WAF Edge Services -> API Gateway: Routes traffic [HTTPS/TLS 1.3 and OAuth2/OIDC (JWT)]
- API Gateway -> Patron Portal: Routes traffic [mTLS]
- API Gateway -> Circulation & Cataloguing Container: Routes traffic [mTLS]

## Technology Stack
- Kubernetes Gateway / Istio Service Mesh: Centralized routing, mTLS, traffic-splitting, and API versioning.
- OAuth2/OIDC with JWT: Centralized authentication, token exchange, and claims enrichment.
- Redis: Backend for distributed global rate-limiting.
- Prometheus: Telemetry and latency scraping for SLA monitoring.
- Elasticsearch: High-performance indexing for rapid search responses.

## Rationale
This architecture centralizes perimeter security, traffic shaping, and data residency enforcement at the API Gateway to protect downstream microservices. Distributed tracing, caching, and optimized data storage guarantee high-performance search SLAs and robust operational observability.