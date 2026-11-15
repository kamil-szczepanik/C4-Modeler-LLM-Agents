## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It guarantees strict EU-only data residency and sub-800ms search performance.

## Key Elements
*   PostgreSQL Primary Node
*   PostgreSQL Read-Only Replica
*   PgBouncer Connection Pooler Sidecar
*   Partitioned Storage Engine
*   Circulation & Catalogue Microservice
*   Search Microservice

## Relationships
*   Circulation & Catalogue Microservice -> PostgreSQL Primary Node: Persists transactional writes (checkouts, fines) [JDBC over TLS 1.3]
*   Search Microservice -> PostgreSQL Read Replica: Executes reads and search hydrations [JDBC over TLS 1.3]
*   Microservices -> PgBouncer Sidecar: Manages and pools database connections
*   PgBouncer -> PostgreSQL Cluster: Forwards client identity for auditing [TLS 1.3]

## Technology Stack
*   PostgreSQL (AWS RDS/Aurora EU-Central): Relational database chosen for ACID compliance and transactional reliability.
*   PgBouncer: Connection pooler selected to prevent connection exhaustion under peak patron load.
*   TLS 1.3 & AWS KMS: Protocols and key management chosen to enforce encryption in transit and at rest for EU compliance.
*   PostgreSQL `pgaudit` Extension: Security logging tool chosen for GDPR and regulatory audit tracking.
*   HashiCorp Vault: Secret management tool selected for dynamic database credential injection.

## Rationale
This architecture isolates heavy read and reporting traffic onto a read replica, protecting core transactional performance to maintain the <800ms search SLA. Furthermore, it strictly enforces EU data residency and security controls through private subnets, TLS 1.3, and KMS encryption.