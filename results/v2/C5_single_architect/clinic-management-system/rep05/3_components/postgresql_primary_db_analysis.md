## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for healthcare facilities. It ensures high availability, strict regulatory compliance, and robust data retention across on-premises Kubernetes and AWS eu-central-1.

## Key Elements
- **Web Application Frontend**: React / TypeScript user interface served via CDN/Nginx.
- **API Gateway**: Kong / Nginx managing external and internal routing.
- **Core Services Container**: Java Spring Boot / Node.js container handling business logic.
- **EMR & Audit Service**: Java Spring Boot container dedicated to patient records and audit trails.
- **PostgreSQL Primary DB**: Database container featuring PostgreSQL 15+ with Citus, PgBouncer, pgAudit, and Barman.
- **WORM-compliant storage**: Long-term immutable storage for compliance archives.

## Relationships
- **Web Application Frontend** -> **API Gateway**: REST/GraphQL over HTTPS.
- **Core Services Container** -> **Connection Pooler (PgBouncer)**: SQL queries over TLS.
- **Connection Pooler** -> **Relational Storage Engine (PostgreSQL)**: Pooled connections via TCP/IP.
- **EMR & Audit Service** -> **Audit & Compliance Logger (pgAudit)**: SQL over TLS.
- **Relational Storage Engine** -> **Backup & Archival Daemon (Barman)**: WAL streaming over TLS to WORM-compliant storage.

## Technology Stack
- **PostgreSQL 15+ with Citus**: Core relational storage engine with horizontal scaling capabilities.
- **PgBouncer**: Connection pooler for handling high-volume client traffic.
- **pgAudit**: Extension for comprehensive DDL/DML auditing to satisfy HIPAA/GDPR.
- **Barman**: Backup and recovery daemon for continuous WAL archiving.
- **Hybrid Kubernetes**: Deployment across `on-prem-k8s` and AWS `eu-central-1`.

## Rationale
This component architecture uses PgBouncer and PostgreSQL logical replication to meet the 99.99% active-active availability target. Additionally, integrating pgAudit and Barman with WORM-compliant storage enforces strict HIPAA/GDPR compliance and the 10-year data retention mandate.