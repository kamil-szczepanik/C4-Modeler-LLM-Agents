## Overview
The Online Bookstore is a secure, multi-region e-commerce platform designed to handle 1 million monthly active users while adhering to GDPR and CCPA compliance. It utilizes an AWS-hosted database architecture to support global catalog browsing, secure checkouts, and real-time recommendations.

## Key Elements
- Primary Database Instance (Writer): Amazon Aurora PostgreSQL-Compatible Edition in `us-east-1`
- Cross-Region Read Replica Instances: Deployed in `eu-west-1` and `ap-southeast-1`
- Global Database Proxy: AWS RDS Proxy deployed in all active regions
- Security & Secrets Management: AWS KMS and AWS Secrets Manager
- Monitoring & Auditing: Amazon CloudWatch and `pgaudit`

## Relationships
- Checkout & Payment Service -> AWS RDS Proxy: Routes transactional writes and post-purchase reads [PostgreSQL wire protocol over TLS 1.3]
- Catalog & Search / Recommendation Services -> AWS RDS Proxy: Routes local read-only traffic [PostgreSQL wire protocol over TLS 1.3]
- AWS RDS Proxy -> Aurora PostgreSQL Instances: Manages connection pooling and backend routing [Pooled PostgreSQL connections]
- Primary Writer -> Regional Read Replicas: Replicates storage data [AWS proprietary high-speed backbone using default encryption]

## Technology Stack
- Amazon Aurora PostgreSQL: Chosen for scalable relational data storage, ACID compliance, and sub-second replication lag
- AWS RDS Proxy: Selected to handle connection pooling and mitigate connection exhaustion for microservices
- AWS KMS: Mandated for data-at-rest encryption across regions using customer-managed keys
- PostgreSQL `pgaudit`: Implemented for rigorous audit logging to meet GDPR/CCPA compliance mandates

## Rationale
This architecture ensures low-latency catalog browsing and localized reads for international users via regional replicas while centralizing writes to maintain data consistency. Integrating AWS RDS Proxy and robust security controls guarantees high availability (99.95%), seamless failover, and strict regulatory compliance.