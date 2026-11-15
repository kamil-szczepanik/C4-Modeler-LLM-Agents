## Overview
The Library Management System provides public and academic libraries with catalogue management, circulation control, and self-service portals. It enforces strict EU-only data residency and high-performance search requirements.

## Key Elements
- Library Patrons [person]
- Circulation Staff and Library Administrators [person]
- Web Portal (React/TypeScript on Nginx) [container]
- API Gateway (Envoy/Kong) [container]
- Core Services API (Java/Spring Boot) [container]
- Search & Catalogue Service (OpenSearch/Java) [container]
  - Search API Handler (Java/Spring Boot) [component]
  - Query Builder & Faceting Engine (Java) [component]
  - Indexing Worker (Java/Spring Boot) [component]
  - Search Engine Index (OpenSearch) [component]
- Database (PostgreSQL with EU hosting) [container]
- Identity Provider / SSO [externalSystem]
- Notification Gateway [externalSystem]
- Observability & Logging Platform (Prometheus/Grafana) [externalSystem]

## Relationships
- Library Patrons -> Web Portal [HTTPS/TLS 1.3]
- Web Portal -> API Gateway [HTTPS / JSON over TLS 1.3]
- API Gateway -> Search & Catalogue Service [gRPC over mTLS]
- Search & Catalogue Service -> Database [PostgreSQL Replication Protocol over TLS 1.3 via Debezium CDC]
- Search API Handler -> Query Builder & Faceting Engine [In-process method call]
- Query Builder & Faceting Engine -> Search Engine Index [REST over mTLS]
- Core Services API -> Database [PostgreSQL Wire Protocol over TLS 1.3]

## Technology Stack
- OpenSearch: Executes inverted-index queries for high-performance search (<800ms SLA).
- PostgreSQL with Debezium CDC: Streams real-time updates via replication protocol for strong consistency.
- Java & Spring Boot: Powers stateless API handlers, workers, and query engines.
- Kubernetes: Enables independent auto-scaling of services and data nodes.
- TLS 1.3 and mTLS: Secures all internal and external communication channels.

## Rationale
Decoupling the search layer using CDC and independent Java microservices prevents database bottlenecks and guarantees the sub-800ms search SLA. Restricting all components and data storage to EU infrastructure strictly satisfies regional compliance constraints.