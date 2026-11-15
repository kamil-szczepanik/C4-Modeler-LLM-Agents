## Overview
The Library Management System provides public and academic libraries with catalogue management, circulation control, and self-service portals. It enforces strict EU-only data residency and sub-800ms search performance requirements.

## Key Elements
- Library Patrons [person]
- Circulation Staff and Library Administrators [person]
- Web Portal [container, React/TypeScript on Nginx]
- API Gateway [container, Envoy/Kong]
- Core Services API [container, Java/Spring Boot]
- Search & Catalogue Service [container, Elasticsearch/OpenSearch]
- Database [container, PostgreSQL with EU hosting]
- Identity Provider / SSO [externalSystem]
- Digital Content Providers [externalSystem]
- Notification Gateway [externalSystem]
- Observability & Logging Platform [externalSystem]

## Relationships
- Web Portal -> API Gateway [HTTPS / JSON over TLS 1.3]
- API Gateway -> Core Services API [gRPC over mTLS with W3C Trace Context]
- API Gateway -> Search & Catalogue Service [gRPC over mTLS with W3C Trace Context]
- API Gateway -> Identity Provider / SSO [OIDC/SAML over HTTPS]
- Core Services API -> Database [PostgreSQL Wire Protocol over TLS 1.3]
- Search & Catalogue Service -> Database [PostgreSQL Wire Protocol over TLS 1.3]
- Core Services API -> Notification Gateway [Asynchronous HTTPS/REST webhooks over TLS 1.3]
- Core Services API -> Digital Content Providers [HTTPS/REST with mutual TLS]

## Technology Stack
- React/TypeScript on Nginx: Powers responsive web interfaces for patrons and staff.
- Envoy/Kong: Provides high-performance edge routing, rate limiting, and security termination.
- Java/Spring Boot: Executes core business logic and transactional processing reliably.
- Elasticsearch/OpenSearch: Delivers sub-800ms catalogue search performance.
- PostgreSQL: Ensures reliable relational data storage with strict EU-only residency compliance.
- Redis: Backs distributed rate-limiting to prevent automated scraping.

## Rationale
This microservices-based architecture uses Envoy/Kong for edge protection and decoupled Java/Spring Boot and Elasticsearch services to guarantee sub-800ms performance. Strict TLS 1.3, mTLS, and EU-hosted PostgreSQL ensure regulatory compliance and data security.