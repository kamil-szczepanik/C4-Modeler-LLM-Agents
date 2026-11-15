## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within strict EU data residency constraints. It delivers reliable transaction processing and rapid search performance to support patrons and circulation staff.

## Key Elements
- **Database Container**: PostgreSQL 15+ database system enforcing EU data residency.
- **Transactional Data Store**: Internal component utilizing row-level security and cryptographic erasure for GDPR compliance.
- **Audit Schema**: Isolated schema for compliance interfacing with the Audit Logging Service.
- **Primary Database Instance**: Dedicated PostgreSQL node handling write-heavy operations.
- **Read Replica Cluster**: Scaled-out read-only nodes servicing non-critical analytical queries.
- **Core Business Service**: Spring Boot (Java) application interacting with the database.

## Relationships
- Core Business Service -> Primary Database Instance: Writes data via JDBC over TLS 1.3 with mTLS and SCRAM-SHA-256.
- Core Business Service -> Read Replica Cluster: Reads data via JDBC over TLS 1.3 with strict `SELECT`-only least-privilege accounts.
- Primary Database Instance -> Read Replica Cluster: Replicates data streams using TLS 1.3 with certificate validation.
- Audit Schema -> Audit Logging Service: Interfaces directly for immutable WORM storage.

## Technology Stack
- **PostgreSQL 15+**: Relational database providing transactional integrity and `pg_stat_statements` for query optimization.
- **AES-256 / External KMS**: Encryption-at-rest with key management restricted strictly within the EU boundary.
- **JDBC over TLS 1.3 & mTLS**: Encrypted transit protocol utilizing mutual TLS and SCRAM-SHA-256 authentication.

## Rationale
This architecture ensures strict EU regulatory and GDPR compliance through cryptographic erasure, isolated audit schemas, and external KMS key management. The read/write split topology and optimized PostgreSQL configuration guarantee high write concurrency and sub-second transaction processing during peak hours.