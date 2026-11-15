## Overview
The Library Management System provides item cataloguing, circulation management, and self-service portals for public and academic libraries. It ensures strict EU-only data residency and high-performance search responses.

## Key Elements
- PostgreSQL Container (AWS RDS EU)
- Primary Database Instance (PostgreSQL 15, AWS RDS)
- Read Replica Instance (PostgreSQL 15, AWS RDS)
- Connection Pooler (PgBouncer)
- Core Services Container (Spring Boot, Java)
- AWS S3 EU Bucket
- AWS KMS

## Relationships
- Core Services Container -> PgBouncer: Manages connections via PostgreSQL Wire Protocol over TLS 1.3
- PgBouncer -> Primary Database Instance / Read Replica Instance: Routes queries via PostgreSQL Wire Protocol over TLS 1.3
- Primary Database Instance -> Read Replica Instance: Asynchronous replication via SSL/TLS
- Primary Database Instance / Read Replica Instance -> AWS S3 EU Bucket: Automated daily snapshots via HTTPS/TLS

## Technology Stack
- PostgreSQL 15 (AWS RDS EU): Relational datastore ensuring EU data residency and transactional integrity
- PgBouncer: Efficient connection pooling between services and database instances
- AWS KMS: Customer-managed keys (AES-256) for transparent storage and backup encryption
- AWS S3 EU: Secure destination for automated daily database backups

## Rationale
This architecture uses AWS RDS PostgreSQL with multi-AZ replication, connection pooling, and read-replica offloading to guarantee strict EU data residency compliance, high availability, and sub-800ms performance. Robust encryption and IAM authentication protect sensitive patron data.