## Overview
- PostgreSQL database infrastructure providing transactional consistency and data storage for the Library Management System.
- Enforces strict EU-only data residency and GDPR compliance for physical and digital catalog circulation.

## Key Elements
- PostgreSQL 16 Primary Storage Engine: Handles ACID-compliant circulation states and financial audit logs via WAL.
- Read-Only Replica (PostgreSQL 16): Offloads administrative reporting queries from library staff.
- Patroni and etcd: Manages high availability, multi-zone clustering, and automated failover.
- PgBouncer: Provides connection pooling at the container boundary.
- Barman / pgBackRest: Executes continuous WAL archiving for Point-in-Time Recovery (PITR).
- pgaudit: Extension for logging DDL, DML, and privileged actions.

## Relationships
- Core Domain Services -> Primary Storage Engine: Executes transactional writes and critical reads using PostgreSQL Protocol over mTLS.
- Core Domain Services -> Read-Only Replica: Executes non-blocking analytical reads and reporting queries using PostgreSQL Protocol over mTLS.
- Primary Storage Engine -> Read-Only Replica: Streams replication data using encrypted mTLS connections.

## Technology Stack
- PostgreSQL 16: Chosen for robust ACID compliance, advanced indexing, and native extension support.
- Patroni / etcd: Selected for automated failover and high-availability clustering.
- PgBouncer: Implemented to prevent connection exhaustion under peak patron load.
- Transparent Data Encryption (TDE) & KMS: Deployed for EU-bound PII protection.
- pgBackRest: Utilized for automated Point-in-Time Recovery (PITR).

## Rationale
- Multi-replica architecture offloads administrative queries to protect the 99th-percentile < 800 ms search and circulation response times.
- Integrated security, encryption, and partitioning mechanisms strictly fulfill the EU-only data residency and GDPR constraints.