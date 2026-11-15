## Overview
The Amazon Aurora PostgreSQL database system serves as the core transactional data store for the Online Bookstore. It ensures secure, highly available, and compliant multi-region storage for e-commerce transactions, customer data, and catalogs.

## Key Elements
* **Writer Instance**: Primary Aurora PostgreSQL engine handling regional write traffic.
* **Reader Instances**: Aurora PostgreSQL read replicas scaled horizontally across availability zones.
* **Cluster Endpoint (Writer)**: DNS routing component directing write traffic.
* **Reader Endpoint**: Load-balanced DNS endpoint for read queries.
* **Amazon RDS Proxy**: Connection pooler securing and managing database connections.
* **Aurora Distributed Storage**: Asynchronously replicated global storage layer across AWS regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`).

## Relationships
* Core E-Commerce Container -> **Cluster Endpoint (Writer)**: Transmits transactional writes [PostgreSQL wire protocol / TLS 1.3].
* Core E-Commerce Container -> **Reader Endpoint**: Transmits read queries [PostgreSQL wire protocol / TLS 1.3].
* **Reader Endpoint** -> **Amazon RDS Proxy**: Pools and forwards read traffic [PostgreSQL wire protocol].
* **Amazon RDS Proxy** -> **Reader Instances**: Manages query distribution [PostgreSQL wire protocol].

## Technology Stack
* **Amazon Aurora PostgreSQL**: Provides relational storage, multi-AZ failover, and global replication.
* **Amazon RDS Proxy**: Prevents connection exhaustion and handles IAM token management.
* **AWS KMS**: Enforces encryption-at-rest using customer-managed keys (CMK).
* **PostgreSQL `pgaudit`**: Enables detailed audit logging for GDPR/CCPA compliance.
* **AWS CloudWatch & CloudTrail**: Monitors replica lag, connections, and system audit logs.

## Rationale
This architecture guarantees 99.95% uptime and high scalability for 1M MAU through connection pooling and automated read scaling. Regional active-local writes and encrypted global storage ensure strict GDPR and CCPA compliance.