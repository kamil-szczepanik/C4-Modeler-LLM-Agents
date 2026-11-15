## Overview
[The Library Management System is a comprehensive solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals.]
[It is architected with strict EU-only data residency and high-performance search requirements to serve patrons, librarians, and administrators.]

## Key Elements
- **Patron Web App & API**: Node.js/Next.js application serving patrons.
- **Staff Management API**: Java/Spring Boot application for staff workflows.
- **Database Container**: Managed PostgreSQL (EU-hosted, AES-256 encrypted).
- **Connection Pooler Component**: PgBouncer for connection management.
- **PostgreSQL Database Engine Component**: Relational storage with logical schemas (`patron_data`, `inventory`, `transactions`).
- **Audit Logging & Security Component**: Handles pgcrypto encryption and telemetry.
- **Search Engine**: Managed OpenSearch/Elasticsearch (EU-hosted).
- **Observability Platform & SIEM**: Captures logs, metrics, and audit events.

## Relationships
- **Patron Web App & API -> Connection Pooler**: Manages queries [mTLS / PostgreSQL Protocol]
- **Staff Management API -> Connection Pooler**: Manages queries [mTLS / PostgreSQL Protocol]
- **Connection Pooler -> PostgreSQL Database Engine**: Proxies authenticated traffic [TCP/IP]
- **PostgreSQL Database Engine -> Observability Platform & SIEM**: Forwards audit logs and metrics [Syslog/TLS]

## Technology Stack
- **Managed PostgreSQL**: Core relational store ensuring EU-only data residency and ACID compliance.
- **PgBouncer**: Connection pooler preventing thread and connection exhaustion during traffic spikes.
- **PostgreSQL pgcrypto**: Provides column-level encryption for sensitive patron PII.
- **Managed OpenSearch/Elasticsearch**: Offloads heavy text-search to meet the 99th-percentile < 800ms NFR.
- **TLS 1.3 with mTLS**: Secures all transit connections between APIs and the database.

## Rationale
[This architecture balances stringent EU data residency and GDPR compliance with enterprise-grade performance and security requirements.]
[By isolating search workloads, decoupling connections via PgBouncer, and enforcing least-privilege schemas, the system achieves sub-second response targets and robust fault tolerance.]