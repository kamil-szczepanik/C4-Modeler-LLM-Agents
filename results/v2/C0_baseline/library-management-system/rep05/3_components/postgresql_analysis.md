## Overview
[The Library Management System is a comprehensive solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and high-performance search requirements.]

## Key Elements
* PostgreSQL v15+ (Primary relational database engine)
* PgBouncer (Connection pooler)
* Catalog Service & Circulation Service (Spring Boot Java microservices)
* Patroni (Automated primary-replica failover manager)
* Prometheus PostgreSQL Exporter & OpenTelemetry (Observability stack)
* Flyway / Liquibase (Schema migration management)

## Relationships
* Catalog Service / Circulation Service -> PgBouncer: Encrypted TCP/IP via TLS 1.3 (mTLS) using PgJDBC driver with SCRAM-SHA-256 authentication
* PgBouncer -> PostgreSQL Primary: Local UNIX domain sockets or loopback TCP with strict Role-Based Access Control (RBAC)
* PostgreSQL -> EU-certified Cloud Provider Infrastructure: Native block storage replication and EU-only object storage for WAL archiving
* PostgreSQL -> Observability Backend: Metrics scraped via Prometheus PostgreSQL Exporter over HTTP/OpenTelemetry

## Technology Stack
* PostgreSQL v15+: Chosen for robust ACID compliance, zero data loss, and transactional integrity
* PgBouncer: Implemented to prevent connection exhaustion under heavy load from Spring Boot services
* Patroni: Selected for automated high-availability clustering and failover management
* Flyway / Liquibase: Utilized for version-controlled, zero-downtime database schema migrations
* pgaudit: Enabled for comprehensive DDL, DCL, and data access logging to achieve audit readiness

## Rationale
[This architecture directly satisfies the EU-only data residency constraint by deploying managed database components exclusively on EU-certified cloud infrastructure. Furthermore, it guarantees high performance, strict ACID compliance for circulation records, and robust security controls like mTLS and RLS.]