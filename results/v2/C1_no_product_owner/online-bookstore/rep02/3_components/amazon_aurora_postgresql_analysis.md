## Overview
[This architecture defines the component-level database design for the Online Bookstore system, using Amazon Aurora PostgreSQL with RDS Proxy to handle high-throughput transactional e-commerce data securely across multi-region AWS deployments.]

## Key Elements
- Database Engine (PostgreSQL 15+)
- Aurora Storage Volume
- Aurora Read Replica
- Amazon RDS Proxy
- PL/pgSQL Procedural Extensions (`pg_trgm`, `uuid-ossp`)
- Security & Monitoring (IAM Auth, AWS KMS, RDS Advanced Auditing, Amazon CloudWatch)

## Relationships
- Order & Checkout Service -> RDS Proxy: Proxies transactional queries [TCP/TLS 1.3]
- Catalog Service -> RDS Proxy: Proxies read queries to replica [TCP/TLS 1.3]
- RDS Proxy -> Database Engine: Routes pooled connections [TCP/TLS 1.3]
- Database Engine -> Aurora Storage Volume: Replicates and persists blocks [AWS proprietary low-latency storage fabric]

## Technology Stack
- Amazon Aurora PostgreSQL 15+: Provides relational core for ACID compliance and transactional data.
- Amazon RDS Proxy: Prevents connection spikes and ensures sub-30-second failovers for ECS Fargate tasks.
- AWS KMS: Encrypts storage volumes and read replicas using customer-managed keys for GDPR/CCPA compliance.
- PL/pgSQL Extensions (`pg_trgm`, `uuid-ossp`): Enables fast fuzzy text searching and native UUID generation.

## Rationale
[The architecture ensures 99.95% uptime and high scalability for 1 million MAU by utilizing multi-AZ replication, connection pooling, and strict network isolation. Security controls, encryption, and fine-grained RBAC fully satisfy GDPR/CCPA compliance and OWASP mitigation requirements.]