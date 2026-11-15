## Overview
Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The architecture ensures strict EU data residency and high-performance item searches.

## Key Elements
- Library Patron and Librarian / Staff
- External Systems: Stripe EU, SendGrid EU, EU Identity Provider, National Library Registry, Interlibrary Loan Network
- Containers: Web Application (React/TypeScript, Nginx), API Gateway (Kong/Envoy), Core Services (Java/Spring Boot), Search Service (Elasticsearch/OpenSearch), Database Container (PostgreSQL 16 EU region), Redis Cache, Background Worker (Python/Celery), Event Broker (Apache Kafka EU-hosted), Digital Asset Storage (MinIO / S3-compatible)
- Database Components: Relational Engine, PgBouncer, Data Residency Enforcer (RLS), Audit Logging & Encryption Manager, Backup & PITR Agent, Query Optimization & Monitoring Subsystem (`pg_stat_statements`)

## Relationships
- Core Services Container -> PgBouncer: `SQL over TCP / TLS 1.3`
- PgBouncer -> Relational Engine: `Local Unix Domain Socket / TCP`
- Relational Engine -> Data Residency Enforcer: Internal database hooks and policies
- Relational Engine -> Audit Logging & Encryption Manager: `Filesystem API` via `Internal DB triggers / OS-level encryption (LUKS)`
- Relational Engine -> Backup & PITR Agent: `Storage API` via `WAL streaming / Local file system`
- Relational Engine -> Query Optimization Subsystem: `Shared Memory` via `Internal Extension Hooks`

## Technology Stack
- PostgreSQL 16: Core relational storage for ACID transactions
- PgBouncer: Connection pooling to meet <800ms performance target
- Row-Level Security (RLS): Native enforcement of EU-only data compliance
- AES-256 & LUKS: Data at rest encryption
- `pg_stat_statements`: Query optimization and performance monitoring

## Rationale
This component-level database architecture guarantees compliance with EU-only data residency constraints via native PostgreSQL mechanisms. Additionally, it optimizes query latency to consistently achieve the required 99th-percentile search response time under 800ms.