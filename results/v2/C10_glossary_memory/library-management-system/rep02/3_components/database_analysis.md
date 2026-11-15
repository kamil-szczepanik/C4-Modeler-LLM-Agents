## Overview
- The Library Management System provides public and academic libraries with catalogue management, circulation control, and self-service portals.
- The architecture enforces strict EU-only data residency and high-performance search requirements using a resilient containerized stack.

## Key Elements
- Library Patrons [person]
- Circulation Staff and Library Administrators [person]
- Web Portal [container] (React/TypeScript on Nginx)
- API Gateway [container] (Envoy/Kong)
- Core Services API [container] (Java/Spring Boot)
- Search & Catalogue Service [container] (Elasticsearch/OpenSearch)
- Database [container] (PostgreSQL with EU hosting)
- Identity Provider / SSO [externalSystem]
- Notification Gateway [externalSystem]
- Observability & Logging Platform [externalSystem]

## Relationships
- Library Patrons / Circulation Staff -> Web Portal: HTTPS / TLS 1.3
- Web Portal -> API Gateway: HTTPS / JSON over TLS 1.3
- API Gateway -> Core Services API: gRPC over mTLS
- API Gateway -> Search & Catalogue Service: gRPC over mTLS
- Core Services API -> Database: PostgreSQL Wire Protocol over TLS 1.3 via PgBouncer
- Search & Catalogue Service -> Database: PostgreSQL Wire Protocol over TLS 1.3 via PgBouncer
- Core Services API -> Notification Gateway: Asynchronous HTTPS/REST webhooks over TLS 1.3

## Technology Stack
- React/TypeScript on Nginx: Delivers responsive self-service and administrative UIs
- Envoy/Kong: Provides robust API routing, edge security, and circuit breaking
- Java/Spring Boot: Implements scalable core business logic and transactional workflows
- Elasticsearch/OpenSearch: Delivers sub-800ms high-performance catalogue search queries
- PostgreSQL with EU hosting: Ensures ACID compliance, row/column encryption, and EU data residency

## Rationale
- The chosen technology stack guarantees sub-800ms search performance while strictly adhering to EU data residency and GDPR mandates.
- Containerized microservices ensure high availability and scalability for both self-service patrons and administrative staff workflows.