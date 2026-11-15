## Overview
The Library Management System provides catalogue and circulation services for public and academic libraries. The architecture uses PostgreSQL for secure, EU-resilient data persistence.

## Key Elements
* Data Access Layer / Persistence Container (PostgreSQL)
* Core Business Logic / Circulation API Container
* PgBouncer Connection Pooling
* PostgreSQL Read Replicas
* HashiCorp Vault (Encryption Key Management)

## Relationships
* Core Business Logic Container -> PostgreSQL: Relational read/write via TLS 1.3
* Core Business Logic Container -> PgBouncer: Connection routing and pooling
* PostgreSQL -> Read Replicas: Asynchronous replication for read-heavy queries
* PostgreSQL -> HashiCorp Vault: Envelope encryption key management

## Technology Stack
* PostgreSQL: Chosen for ACID compliance and EU-only data residency
* PgBouncer: Manages connection spikes to maintain < 800 ms response times
* Flyway / Liquibase: Automates version-controlled schema migrations
* pgaudit: Provides comprehensive audit logging for sensitive patron data
* TLS 1.3: Secures data in transit across system boundaries

## Rationale
This architecture guarantees strict EU data residency compliance while maintaining robust security through encryption and least-privilege access. Additionally, read-replicas, connection pooling, and indexing strategies ensure the system easily satisfies the 99th-percentile search response time under 800 ms.