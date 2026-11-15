## Overview
[The system is an online bookstore designed to handle 1M MAU with 99.95% uptime across AWS regions. It securely manages catalogs, orders, and PII under GDPR and CCPA constraints.]

## Key Elements
* Connection Pooler (PgBouncer)
* Relational Storage Engine (PostgreSQL 15)
* Backup & Replication Manager
* ECS Fargate Microservices (Order & Checkout Service, Catalog Service)
* AWS Secrets Manager & AWS KMS
* Amazon CloudWatch & Amazon GuardDuty RDS Protection

## Relationships
* Order & Checkout Service -> Connection Pooler: `TCP/TLS, SQL queries via IAM auth`
* Catalog Service -> Connection Pooler: `TCP/TLS, SQL queries via IAM auth`
* Connection Pooler -> Relational Storage Engine: `Internal TCP socket`
* Backup & Replication Manager -> Amazon S3 (AWS Backup Vaults): `Encrypted snapshot exports [AWS KMS, TLS 1.3]`

## Technology Stack
* PostgreSQL 15 on Amazon RDS: Chosen for ACID-compliant transactional data storage.
* PgBouncer: Manages database connections to prevent connection exhaustion.
* Terraform/AWS CDK: Utilized for Infrastructure as Code and blue/green deployments.
* AWS KMS & AWS Secrets Manager: Enforces encryption-at-rest with CMKs and IAM database authentication.

## Rationale
[This architecture satisfies high availability and scalability requirements through Multi-AZ replication and connection pooling. Security controls like TLS 1.3, RLS, and regional CMKs ensure strict GDPR/CCPA compliance.]