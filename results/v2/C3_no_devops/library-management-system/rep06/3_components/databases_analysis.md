## Overview
The Library Management System is an EU-compliant platform providing cataloging, circulation, and self-service portals for public and academic libraries. Its database container ensures secure, high-performance data persistence while strictly adhering to GDPR requirements.

## Key Elements
- PostgreSQL Primary Node
- PostgreSQL Read Replica
- Audit & Compliance Logger
- Backup & PITR Agent
- Data Anonymization Views

## Relationships
- Circulation & Member Service -> PostgreSQL Primary Node: Transactional reads/writes [TCP/IP via mTLS 1.3]
- Analytics & Reporting Container -> Data Anonymization Views: De-identified reporting queries [TCP/IP via TLS 1.3]
- PostgreSQL Primary Node -> PostgreSQL Read Replica: Asynchronous WAL streaming [Internal streaming replication protocol via mTLS]
- Backup & PITR Agent -> PostgreSQL Primary Node: Continuous WAL archiving [Filesystem / Storage API]

## Technology Stack
- PostgreSQL 16: Core transactional database for performance and ACID compliance
- pgAudit: Structured tamper-evident logging for GDPR compliance
- Barman / pgBackRest: Continuous backup and Point-in-Time Recovery (PITR)
- PostgreSQL Row-Level Security (RLS) & Secure Views: Data isolation and anonymization

## Rationale
This architecture guarantees EU-only data residency and stringent GDPR compliance via pgAudit, mTLS 1.3, and data anonymization views. Furthermore, read replicas and PITR ensure high availability and sub-800ms search/query performance.