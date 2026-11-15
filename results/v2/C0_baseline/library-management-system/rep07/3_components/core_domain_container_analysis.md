## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. The Core Domain Container handles cataloguing, circulation logic, and transactional data storage while strictly enforcing EU data residency.

## Key Elements
- Core Domain Container (Java 21 / Spring Boot 3.2, OCI distroless image)
- Cataloguing Component (Spring Data JPA)
- Circulation Component (Domain-Driven Design / Spring Transaction)
- Outbox Pattern Component & Debezium / JDBC Poller
- Audit & Compliance Component (Spring Data Envers / append-only tables)
- Security & Context Propagation Component (Spring Security, OAuth2/OIDC JWT)
- PostgreSQL 16 (EU-hosted, native tablespace encryption)
- Async Event Broker (Apache Kafka)

## Relationships
- API Gateway -> Core Domain Container: Routes domain and circulation requests [gRPC or REST over TLS within EU-isolated VPC]
- Core Domain Container -> EU-hosted PostgreSQL: Persists transactional and audit data [Database protocol over TLS 1.3 with certificate pinning]
- Core Domain Container -> Async Event Broker: Publishes scrubbed domain events [SASL/SCRAM, mTLS]

## Technology Stack
- Java 21 / Spring Boot 3.2: Modern runtime for robust domain logic and performance.
- Spring Modulith: Enforces strict package boundaries between domain components.
- PostgreSQL 16: Relational storage with row-level security and `pg_partman` for EU data residency compliance.
- Spring Security & OAuth2: Handles JWT validation and fine-grained RBAC.
- OpenTelemetry / Micrometer: Enables comprehensive observability of JVM metrics and outbox lag.

## Rationale
This architecture ensures strict EU data residency via isolated cloud infrastructure and CMEK encryption while maintaining high performance. The Transactional Outbox pattern guarantees reliable event delivery to meet sub-800ms search requirements without sacrificing data consistency.