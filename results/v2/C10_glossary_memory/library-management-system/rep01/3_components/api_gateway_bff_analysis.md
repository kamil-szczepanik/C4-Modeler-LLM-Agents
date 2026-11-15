## Overview
[System handles catalogue management, circulation, and self-service portals for public and academic libraries while enforcing strict EU-only data residency. It uses an Envoy-based API Gateway / BFF architecture to route and secure traffic across tailored user portals and backend microservices.]

## Key Elements
- API Gateway / BFF (Envoy)
- Edge Router & TLS Termination Component
- Authentication & JWT Validation Filter
- Rate Limiting & Threat Protection Component
- BFF Aggregator & Protocol Translator
- Patron Portal, Staff Circulation App, Admin Console
- Search & Catalog Service (Java/Spring Boot + Elasticsearch)
- Circulation & Core Engine (Go/Node.js)
- Primary Database (PostgreSQL, EU-hosted)
- EU Identity Provider (IdP)

## Relationships
- Anycast CDN / DDoS Protection Service (EU-PoPs) -> Edge Router & TLS Termination Component [TLS 1.3, HTTPS]
- Patron Portal -> API Gateway / BFF [HTTPS/REST, WSS]
- Staff Circulation App -> API Gateway / BFF [HTTPS/REST]
- Admin Console -> API Gateway / BFF [HTTPS/REST]
- API Gateway / BFF -> EU Identity Provider (IdP) [OIDC/OAuth2]
- BFF Aggregator & Protocol Translator -> Search & Catalog Service [gRPC over mTLS]
- BFF Aggregator & Protocol Translator -> Circulation & Core Engine [gRPC over mTLS]

## Technology Stack
- Envoy: Chosen for the API Gateway / BFF to handle edge routing, TLS 1.3 termination, and low-latency proxying.
- gRPC over mTLS: Used for internal service-to-service communication to ensure zero-trust security and high performance.
- Redis: Backs the rate-limiting component with multi-AZ replication to protect catalog search from scraping.
- PostgreSQL (EU-hosted): Provides primary ACID-compliant persistence with AES-256 encryption at rest.

## Rationale
[The Envoy-based API Gateway pattern provides persona-specific BFF routing, strict EU data residency compliance, and optimized payloads. This ensures sub-800ms search performance while securing sensitive library workflows.]