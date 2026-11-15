## Overview
An Amazon Aurora PostgreSQL database serves as the transactional backbone for the online bookstore, ensuring secure order processing, inventory tracking, and multi-currency support. It provides high availability, ACID compliance, and strict GDPR/CCPA data privacy controls across three AWS regions.

## Key Elements
* Amazon Aurora PostgreSQL Primary Write Instance (PostgreSQL 15 engine)
* Amazon Aurora PostgreSQL Read Replicas (Distributed across Availability Zones)
* PgBouncer Connection Pooling Sidecar
* AWS Secrets Manager
* AWS Key Management Service (AWS KMS)
* Amazon CloudWatch and RDS Data Protection

## Relationships
* ECS Fargate Go Microservices -> PgBouncer Sidecar: Manages database connections [TCP]
* PgBouncer Sidecar -> Amazon Aurora PostgreSQL: Executes queries and transactions [TCP, TLS 1.3, mTLS]
* Amazon Aurora PostgreSQL -> Amazon S3: Stores continuous point-in-time backups [HTTPS]
* Amazon Aurora PostgreSQL -> Amazon CloudWatch: Streams performance metrics and audit logs [HTTPS]

## Technology Stack
* Amazon Aurora PostgreSQL: ACID-compliant transactional persistence with distributed storage volume
* PostgreSQL 15 Engine: Advanced query execution, `pg_stat_statements`, and Row-Level Security (RLS)
* PgBouncer: Connection pooling to handle high-volume microservice requests
* AWS KMS & Secrets Manager: Transparent data encryption (TDE) via Customer Managed Keys and automated 30-day credential rotation

## Rationale
This architecture ensures 99.95% uptime and sub-second transaction performance required for 1M MAU through multi-AZ replication and connection pooling. It fulfills strict GDPR, CCPA, and OWASP security constraints using robust encryption, IAM authentication, and least-privilege access controls.