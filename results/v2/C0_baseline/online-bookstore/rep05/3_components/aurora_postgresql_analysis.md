## Overview
The Online Bookstore system is a scalable e-commerce platform providing physical and electronic book purchasing, catalog browsing, customer reviews, and personalized recommendations. It ensures high availability, multi-region support, and strict GDPR and CCPA compliance.

## Key Elements
- Core Services (NestJS on Amazon ECS Fargate)
- Aurora PostgreSQL (Amazon Aurora PostgreSQL Multi-AZ with Read Replicas)
- Database Internal Components: PostgreSQL Storage Engine, Aurora Query Processing Engine, Aurora Replication Agent, Logical Replication / CDC Publisher
- PgBouncer (Connection Pooling)
- Analytics Ingestion Container (Amazon ECS Fargate)
- AWS Secrets Manager & AWS KMS (CMK)
- Amazon CloudWatch & AWS Backup

## Relationships
- Core Services -> Aurora Query Processing Engine: Reads and writes transactional data via TCP/TLS [PostgreSQL Wire Protocol]
- Aurora PostgreSQL (CDC Publisher) -> Analytics Ingestion Container: Streams change events via TCP/TLS [PostgreSQL Logical Streaming Replication / AWS SQS]

## Technology Stack
- Amazon Aurora PostgreSQL (Multi-AZ): Selected for ACID compliance, transactional reliability, and multi-region read scalability.
- PgBouncer: Deployed alongside ECS Fargate to prevent connection exhaustion under high concurrency.
- AWS KMS & AWS Secrets Manager: Utilized for encryption-at-rest (CMK) and automated credential rotation to meet GDPR/CCPA.
- PostgreSQL Logical Decoding: Powers asynchronous Change Data Capture (CDC) without impacting primary transaction performance.

## Rationale
This architecture uses Amazon Aurora PostgreSQL with asynchronous CDC and strict security controls to handle high transaction volumes and global traffic. It guarantees ACID compliance, strict regulatory adherence, and sub-second performance while isolating analytical and operational workloads.