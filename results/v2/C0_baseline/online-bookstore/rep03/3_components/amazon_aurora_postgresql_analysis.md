## Overview
Amazon Aurora (PostgreSQL) serves as the primary transactional and relational data store for the online bookstore. It ensures zero-loss financial transactions, secure inventory management, and multi-region data persistence.

## Key Elements
- Amazon Aurora PostgreSQL: Global database cluster acting as the primary transactional data store.
- Amazon RDS Proxy: Connection pooler managing traffic between ECS Fargate services and Aurora.
- Logical Schemas: `order_management`, `inventory_catalog`, and `user_identity` isolating domain data.
- Read Replicas: Regional replicas handling read-heavy queries and inventory checks.
- AWS Key Management Service (KMS): Manages customer-managed encryption keys.

## Relationships
- Checkout Service & Node.js BFF -> Amazon RDS Proxy: Connects via PostgreSQL wire protocol over TLS 1.3.
- Amazon RDS Proxy -> Amazon Aurora (PostgreSQL): Routes pooled read/write traffic to primary writer and read replicas.
- AWS Secrets Manager -> Amazon RDS Proxy: Provides IAM database authentication tokens and secret rotations.
- Amazon CloudWatch -> Amazon Aurora (PostgreSQL): Receives performance insights and advanced audit logs.

## Technology Stack
- Amazon Aurora PostgreSQL: Chosen for native multi-region global databases and 99.95% availability.
- Amazon RDS Proxy: Implemented to handle connection spikes and prevent backend exhaustion at 1M MAU.
- Aurora Serverless v2: Utilized for automatic capacity scaling (ACUs) during flash sales.
- AWS KMS: Enforces encryption-at-rest and protects cross-region backups.
- Flyway / Liquibase: Automated CI/CD schema migration tools connecting directly to the primary writer.

## Rationale
This architecture ensures high availability (99.95%) and low latency globally through multi-region deployment and connection pooling. It strictly fulfills GDPR, CCPA, and OWASP security requirements via encryption, IAM authentication, and network isolation.