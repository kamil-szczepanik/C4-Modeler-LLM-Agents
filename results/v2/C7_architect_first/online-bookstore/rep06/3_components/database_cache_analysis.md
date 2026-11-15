## Overview
The Online Bookstore uses a scalable AWS-hosted e-commerce architecture designed to handle 1M MAU with high availability and GDPR/CCPA compliance. It provides secure catalogue browsing, multi-currency checkout, and personalized recommendations.

## Key Elements
- Core API Application (Node.js, Express on Amazon ECS Fargate)
- Connection Pooling Component (Amazon RDS Proxy / PgBouncer sidecar)
- Primary Relational Datastore (Amazon Aurora PostgreSQL Multi-AZ)
- Read Replica Cluster (Amazon Aurora PostgreSQL Read Replicas)
- Distributed Cache Layer (Amazon ElastiCache for Redis)
- Supporting Services (Amazon CloudWatch, AWS Secrets Manager, AWS KMS)

## Relationships
- Core API Application -> Connection Pooling Component: Acquires database connections via TLS
- Connection Pooling Component -> Primary Relational Datastore: Executes transactional queries on port 5432 using `pgJDBC` over TLS
- Core API Application -> Primary Relational Datastore: Reads/Writes transactional data (`pg` driver over TLS)
- Core API Application -> Distributed Cache Layer: Gets/Sets session and catalogue cache via RESP (`ioredis`, `rediss://`)

## Technology Stack
- Amazon Aurora PostgreSQL: Chosen for ACID compliance, multi-currency decimal precision, and automated cross-region replication.
- Amazon ElastiCache for Redis: Selected for low-latency session persistence and cache-aside catalogue performance.
- Amazon RDS Proxy / PgBouncer: Implemented to manage connection limits from auto-scaling ECS Fargate tasks.
- AWS Secrets Manager & KMS: Utilized for credential rotation and encryption at rest to satisfy GDPR/CCPA.

## Rationale
This architecture ensures sub-second response times and 99.95% availability under heavy traffic by combining read replicas, distributed caching, and connection pooling. Security controls and multi-region failovers protect customer data and guarantee compliance with regulatory standards.