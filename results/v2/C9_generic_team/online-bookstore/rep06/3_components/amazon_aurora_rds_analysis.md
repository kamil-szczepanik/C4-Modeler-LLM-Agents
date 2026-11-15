## Overview
Amazon Aurora/RDS provides scalable, multi-region relational database storage utilizing a strict database-per-service isolation pattern for the online bookstore. It supports high availability, ACID compliance for checkout transactions, and fast retrieval for catalog browsing and reviews.

## Key Elements
* Amazon Aurora Writer Instance: Handles all transactional write operations (checkout, orders).
* Amazon Aurora Read Replicas: Scales read-heavy operations (catalog browsing, reviews, recommendations).
* AWS RDS Proxy: Manages and pools database connections from ECS/EKS containers.
* Compliance Workers: Executes GDPR/CCPA data anonymization and logical soft deletes.
* Amazon CloudWatch: Monitors database telemetry, connection pool saturation, and replication lag.

## Relationships
* Containers (Catalog, Checkout, Reviews, Recommendations, Compliance Workers) -> AWS RDS Proxy: Connects via [Database Protocol / PostgreSQL Driver].
* AWS RDS Proxy -> Amazon Aurora Writer/Replicas: Forwards transactions and queries via [PostgreSQL Wire Protocol].
* Compliance Workers -> Amazon Aurora: Executes data anonymization, partitioning, and cryptographic shredding via [Database Protocol].
* Amazon Aurora -> Amazon CloudWatch: Publishes audit logs, slow-query metrics, and telemetry via [AWS API].

## Technology Stack
* Amazon Aurora (PostgreSQL): Chosen for ACID compliance, multi-AZ high availability, and global database replication across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.
* AWS RDS Proxy: Implemented to prevent connection exhaustion from auto-scaling microservices.
* PostgreSQL `pgaudit` Extension: Utilized for immutable audit logging to satisfy GDPR, CCPA, and OWASP security constraints.
* Terraform / Infrastructure as Code: Used for automated database backup retention and Point-in-Time Recovery (PITR) provisioning.

## Rationale
Multi-AZ deployments and RDS Proxy ensure 99.95% uptime and performance under high traffic loads. Strict database-per-service boundaries and date-based partitioning support regulatory compliance while protecting system scalability and maintainability.