## Overview
- Amazon Aurora PostgreSQL serves as the primary relational database for the Online Bookstore, ensuring transactional integrity for shopping carts and secure checkouts.
- It provides scalable, highly available data storage across multiple global regions while enforcing strict GDPR and CCPA compliance.

## Key Elements
- Aurora PostgreSQL Cluster (Multi-AZ with Primary Writer and Read Replicas)
- Aurora Global Database (cross-region replication for us-east-1, eu-west-1, ap-southeast-1)
- Aurora Distributed Storage (auto-scaling up to 128TB across 3 AZs)
- PostgreSQL Extension Manager (`pg_stat_statements`, `pgcrypto`)
- IAM & Secrets Manager Integration
- Private Database Subnets (isolated VPC deployment)

## Relationships
- Core Microservices -> Aurora PostgreSQL Cluster: Executes queries and transactions [PostgreSQL wire protocol over TLS 1.3 via PgBouncer]
- Core Microservices -> IAM & Secrets Manager: Authenticates and manages database credentials [HTTPS/TLS 1.3]
- Aurora PostgreSQL Cluster -> Amazon CloudWatch: Streams audit logs for compliance monitoring [AWS Internal API]
- Aurora PostgreSQL Cluster -> Amazon S3: Performs continuous backups and point-in-time recovery (PITR) with immutable storage [AWS Internal API]

## Technology Stack
- Amazon Aurora PostgreSQL: Chosen for high availability, ACID compliance, and multi-region replication.
- AWS IAM & Secrets Manager: Implemented to eliminate static credentials and secure database access.
- PgBouncer: Utilized for connection pooling to sustain 1M MAU concurrency.
- AWS KMS: Applied for transparent data encryption (TDE) at rest and column-level PII encryption.

## Rationale
- The multi-AZ cluster and global database replication fulfill the 99.95% uptime and multi-region scalability requirements under heavy traffic.
- Strict network isolation, IAM authentication, and encryption mechanisms ensure comprehensive GDPR, CCPA, and OWASP Top-10 security compliance.