## Overview
[Library Management System provides catalogue and circulation services for public and academic libraries. The PostgreSQL Database container manages transactional data storage with EU-only residency enforcement.]

## Key Elements
- Relational Data Store (PostgreSQL 16 with pgcrypto, pgaudit, and PgBouncer)
- CDC Publisher (Debezium PostgreSQL Connector via Kafka Connect)
- Backup & Compliance Agent (pgBackRest)
- Core Domain Service
- Managed Event Bus (Kafka / EventBridge)

## Relationships
- Core Domain Service -> Relational Data Store: Executes SQL queries via JDBC with TLS 1.3 / mTLS
- CDC Publisher -> Relational Data Store: Reads WAL stream using Logical Replication Protocol over TCP with mTLS
- CDC Publisher -> Managed Event Bus: Streams raw database change events via Kafka Protocol

## Technology Stack
- PostgreSQL 16: Relational RDBMS for strict transactional integrity and data storage
- PgBouncer: Connection pooling to prevent thread exhaustion under high concurrency
- Debezium: Change Data Capture for decoupled search synchronization
- pgBackRest: Automated backups supporting EU-only data residency requirements
- pgaudit & pgcrypto: Compliance logging and AES-256 data-at-rest encryption

## Rationale
[Strict least-privilege role separation, mTLS, and PgBouncer connection pooling secure the data tier and prevent resource exhaustion. Automated CDC and managed multi-AZ deployments maintain performance SLAs below 800ms while strictly enforcing EU data residency.]