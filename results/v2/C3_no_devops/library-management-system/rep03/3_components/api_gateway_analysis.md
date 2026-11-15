## Overview
The Library Management System provides public and academic libraries with item cataloging, circulation management, and self-service portals. It enforces strict EU-only data residency and maintains a 99th-percentile search response time under 800 ms.

## Key Elements
* **Users:** Library Patrons (Members), Librarians / Circulation Staff, Library Administrators
* **Frontends:** Patron Portal (React.js SPA), Librarian Back-office (Next.js Web App)
* **API Gateway:** Envoy / NGINX
* **Backend Services:** Catalogue Service (Java / Spring Boot), Circulation Service (Node.js / Express)
* **Data & Messaging:** PostgreSQL Database (EU-hosted), Elasticsearch (EU-hosted), Distributed Cache (Redis, EU-hosted), Event Broker (Apache Kafka / RabbitMQ)
* **External Systems:** External Identity Provider (IdP), Third-Party Payment Gateway, Digital Content Repositories, EU-hosted SIEM

## Relationships
* Patron Portal -> API Gateway: Sends API requests [HTTPS, OAuth2/OIDC with JWTs]
* Librarian Back-office -> API Gateway: Sends API requests [HTTPS, OAuth2/OIDC with JWTs]
* API Gateway -> Catalogue Service: Routes catalogue queries [mTLS via Istio Service Mesh with SPIFFE/SPIRE]
* API Gateway -> Circulation Service: Routes circulation requests [mTLS via Istio Service Mesh with SPIFFE/SPIRE]
* API Gateway -> External Identity Provider (IdP): Authenticates users and caches JWKs [OIDC over HTTPS]

## Technology Stack
* **API Gateway:** Envoy with WAF filter (ModSecurity), Authentication Filter, Rate Limiting Filter, Route & Load Balancing Engine, Fault Translation & Transformation Filter
* **Caching & Limits:** Distributed Cache (Redis, EU-hosted) for rate limiting quotas
* **Security:** JWT cryptographic verification, Claims Propagation (User ID, Roles in HTTP headers), Zero-Trust mTLS via Istio Service Mesh

## Rationale
Centralizing security, rate limiting, and fault translation at the Envoy API Gateway protects backend services from abuse and guarantees the < 800 ms search latency requirement. Edge-enforced WAF, JWT validation, and mTLS ensure strict compliance with EU-only data residency and zero-trust security mandates.