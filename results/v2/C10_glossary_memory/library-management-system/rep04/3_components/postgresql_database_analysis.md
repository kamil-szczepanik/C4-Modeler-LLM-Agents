## Overview
• The Library Management System is a cloud-native enterprise solution that enables public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals with EU-only data residency and security compliance.
• The PostgreSQL Database container provides robust transactional integrity, dedicated analytical read scaling, and automated GDPR compliance tooling to support both patron self-service workflows and administrative reporting.

## Key Elements
• Primary Database Instance (PostgreSQL 15): Handles transactional read/write operations for the Circulation & Loan Service.
• Analytics Read-Replica (PostgreSQL 15 Read-Replica): Dedicated replica serving heavy analytical queries from the Reporting & Analytics Service.
• PgBouncer Connection Pooler: Manages client connections efficiently to prevent resource exhaustion.
• Data Anonymization Engine: Scheduled PL/pgSQL routines executing automated pseudonymization of PII for closed accounts.
• Security & Governance Controls: Row-Level Security (RLS) policies, pgAudit logging, and TLS 1.3 / mTLS enforcement.

## Relationships
• Circulation & Loan Service -> PgBouncer Connection Pooler: Manages operational SQL queries [TCP / PostgreSQL protocol over TLS 1.3].
• Reporting & Analytics Service -> PgBouncer Connection Pooler: Queries analytics data from read-replicas [TCP / PostgreSQL protocol over TLS 1.3].
• PgBouncer Connection Pooler -> Primary Database Instance: Forwards write traffic [SQL / PostgreSQL protocol].
• PgBouncer Connection Pooler -> Analytics Read-Replica: Forwards read-only analytical traffic [SQL / PostgreSQL protocol].

## Technology Stack
• PostgreSQL 15: Selected as the core relational database to ensure strong ACID transactional guarantees for library circulation.
• PgBouncer: Deployed as a connection pooler to mitigate connection overhead and support peak patron self-service loads.
• Kubernetes StatefulSet: Utilized for stateful orchestration with persistent storage volumes restricted exclusively to EU cloud regions.
• pgAudit & SCRAM-SHA-256: Implemented for rigorous compliance auditing and secure password authentication.

## Rationale
• This architecture satisfies stringent EU-only data residency and GDPR right-to-be-forgotten mandates through regional storage provisioning and automated database-level anonymization routines.
• Isolating analytics workloads onto a dedicated read-replica via PgBouncer protects core transactional throughput and guarantees sub-800ms search and circulation performance.