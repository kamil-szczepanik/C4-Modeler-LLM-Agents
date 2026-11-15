## Overview
The architecture implements a globally distributed, high-availability PostgreSQL database system to power the Online Bookstore e-commerce platform. It ensures secure, low-latency data access, strict compliance with data privacy regulations, and robust scalability across multiple AWS regions.

## Key Elements
- Primary Write Instance (Writer Node)
- Read Replica Instances (Multi-AZ / Global)
- Database Encryption & Audit Engine
- Connection Pooler (PgBouncer / Aurora Proxy)
- Global Replication Manager

## Relationships
- Core E-Commerce API -> Connection Pooler: Manages connections [PostgreSQL Wire Protocol over TLS 1.3 with mTLS]
- Connection Pooler -> Primary Write Instance: Routes transactions [PostgreSQL Wire Protocol over TLS 1.3]
- Connection Pooler -> Read Replica Instances: Routes read queries [PostgreSQL Wire Protocol over TLS 1.3]
- Global Replication Manager -> Global Read Replicas: Synchronizes cross-region data [AWS Dedicated Backbone Network with TLS]
- Database Encryption & Audit Engine -> Amazon CloudWatch / AWS CloudTrail: Streams audit logs [AWS Internal API]

## Technology Stack
- Amazon Aurora PostgreSQL (Multi-AZ / Global Database): Chosen for ACID compliance, automated failover, and global read-scaling across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.
- PgBouncer / Aurora Proxy: Used for efficient connection pooling and preventing thread exhaustion under high traffic.
- AWS KMS: Implemented for encryption-at-rest with customer-managed keys (CMKs) and automated rotation.
- PostgreSQL `pgaudit` extension: Utilized for high-privilege query tracking and tamper-proof compliance auditing.
- IAM Database Authentication: Replaces native master passwords with short-lived, token-rotated credentials.

## Rationale
This architecture fits requirements by enforcing strict GDPR/CCPA data privacy compliance through encryption, PII masking, and audit logging while guaranteeing 99.95% uptime and sub-2-second page loads globally via read/write splitting and multi-region replication.