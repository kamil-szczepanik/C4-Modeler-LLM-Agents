## Overview
The Library Management System is a solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. The architecture ensures strict EU-only data residency and sub-800ms search responses.

## Key Elements
- Library Patrons and Library Staff
- Patron Portal & Staff Dashboard (React / TypeScript SPA)
- API Gateway (Nginx / Envoy)
- Core Business Service (Java / Spring Boot)
- Search Service (Elasticsearch / OpenSearch)
- Relational DB Container: Transactional Engine (PostgreSQL core), Audit & Compliance Schema (pgAudit), Replication & High Availability Module (Patroni / Streaming Replication), Connection Pooling Proxy (PgBouncer)
- Message Broker (Kafka / RabbitMQ)
- Secrets Manager (HashiCorp Vault)
- Centralized Observability & SIEM Platform
- Backup & Disaster Recovery Storage

## Relationships
- Core Business Service -> Connection Pooling Proxy: Routes SQL transactions [TCP/TLS with mTLS]
- Connection Pooling Proxy -> Transactional Engine: Forwards pooled queries [TCP / internal encryption]
- Relational DB -> Backup & Disaster Recovery Storage: Streams write-ahead logs (WAL) for point-in-time recovery [Encrypted SSH/S3 API]
- Relational DB -> Centralized Observability & SIEM Platform: Exports metrics (`postgres_exporter`, `pgbouncer_exporter`), slow-query logs, and audit logs [HTTPS/TLS]

## Technology Stack
- PostgreSQL: Core transactional database ensuring ACID compliance and zero-tolerance for double-booked loans
- Patroni with etcd/Consul: Manages automated high availability and sub-30-second failover restricted to EU regions
- PgBouncer: Connection pooling proxy configured in transaction mode to handle peak portal traffic
- pgAudit: Database extension for logging administrative actions to satisfy GDPR tracking mandates
- HashiCorp Vault: Provides dynamic database credential injection and secret rotation
- AES-256 TDE: Enforces data protection at rest across primary, replica, and backup storage

## Rationale
This architecture guarantees compliance through EU-only data residency, strict GDPR data retention automation, and AES-256 encryption. It achieves performance and high availability via Patroni replication, connection pooling, and automated partitioning.