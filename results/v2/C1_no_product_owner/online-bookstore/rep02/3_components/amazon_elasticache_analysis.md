## Overview
[The Online Bookstore is a scaled-down e-commerce platform providing physical and electronic book sales, recommendations, and reviews. Its core purpose is delivering a highly available, secure, and performant multi-region retail experience supporting 1 million monthly active users.]

## Key Elements
- **Users**: Customer, Administrator
- **External Systems**: Payment Gateway, Shipping Provider, Email/Notification Service, Identity Provider
- **Containers**: Single Page Application (React/TypeScript, AWS S3, AWS CloudFront), Amazon Route 53, AWS API Gateway, Catalog Service (Node.js, Amazon ECS Fargate), Order & Checkout Service (Spring Boot, Amazon ECS Fargate), Recommendation Service (Python/FastAPI, Amazon ECS Fargate), Amazon Aurora PostgreSQL, Amazon DocumentDB, Amazon ElastiCache (Redis), AWS EventBridge, Amazon SQS, AWS Secrets Manager, AWS KMS
- **Components (Amazon ElastiCache)**: Cache Router / Cluster Manager, In-Memory Datastore, Persistence & Replication Engine

## Relationships
- Recommendation Service -> Cache Router / Cluster Manager: Fetches recommendation cache data [TCP/TLS, Redis Protocol, `rediss://` on port 6379]
- Cache Router / Cluster Manager -> In-Memory Datastore: Manages slot allocation and routes queries [Internal Redis Protocol]
- In-Memory Datastore -> Persistence & Replication Engine: Backs up data asynchronously via RDB/AOF snapshots [Internal AWS Network]

## Technology Stack
- **Caching**: Amazon ElastiCache (Redis) Cluster-Mode Enabled with Multi-AZ deployment for sub-millisecond recommendation retrieval and high availability.
- **Security & Secrets**: AWS Secrets Manager and AWS KMS for encrypted data-at-rest, TLS in-transit encryption, and Redis AUTH token rotation.
- **Monitoring**: Amazon CloudWatch for tracking `EngineCPUUtilization`, `CacheHitRate`, `Evictions`, `ReplicationLag`, and `FreeableMemory`.

## Rationale
[This architecture utilizes multi-region Amazon ElastiCache Redis clusters deployed in private VPC subnets to meet the sub-2 second page load performance requirement and 99.95% uptime SLA. Strict encryption, command hardening, and Multi-AZ replication ensure GDPR/CCPA compliance and fault-tolerant scalability for 1 million active users.]