## Overview
The PostgreSQL component provides a secure, highly available relational data store for the Library Management System. It manages structured catalogue and circulation data while enforcing strict EU data residency constraints.

## Key Elements
- Relational Engine (PostgreSQL 16)
- Storage Subspace
- Connection Pooler (PgBouncer)
- Schema Partitioning Component
- Audit Logging Component (pgaudit)

## Relationships
- Catalogue Service -> Connection Pooler: SQL/TCP [TLS 1.3, mTLS, SCRAM-SHA-256]
- Circulation Service -> Connection Pooler: SQL/TCP [TLS 1.3, mTLS, SCRAM-SHA-256]
- Connection Pooler -> Relational Engine: Inter-process socket [TLS 1.3]
- Relational Engine -> Storage Subspace: File I/O [AES-256, TDE]
- Relational Engine -> Schema Partitioning: Logical isolation [Internal]

## Technology Stack
- PostgreSQL 16: Core relational engine for ACID transactions and data storage
- PgBouncer: Connection pooling to prevent thread exhaustion from microservices
- Kubernetes StatefulSets & CloudNativePG: High availability and automated failover
- pgaudit & pgcrypto: Compliance auditing and column-level encryption for GDPR

## Rationale
This architecture uses connection pooling and schema isolation to maintain microservice boundaries and meet performance goals. Kubernetes operators, encryption, and automated backups ensure high availability and strict EU data compliance.