## Overview
An Amazon-style online bookstore providing catalog browsing, secure checkout, reviews, and recommendations for 1M MAU. Built on AWS with multi-region support, GDPR/CCPA compliance, and 99.95% uptime.

## Key Elements
- **Customers & Users:** Global shoppers, authors, support agents, admins, and shipping partners.
- **Frontend Containers:** Single-Page Application (React, Amazon S3, Amazon CloudFront).
- **API & Mesh Containers:** AWS API Gateway, Envoy Service Mesh (SPIFFE/SPIRE).
- **Backend Containers:** Catalog Service, Order & Checkout Service, Recommendation Service, Customer Service, Admin Service (Node.js, Java, Python, Go, AWS ECS on Fargate).
- **Database & Storage Containers:** Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis), Amazon S3.
- **Messaging Containers:** Amazon EventBridge, Amazon SQS.
- **Aurora Components:** Aurora Writer Node, Aurora Reader Nodes, Aurora Storage Volume, PgBouncer Connection Pooler (sidecar).

## Relationships
- Single-Page Application -> AWS API Gateway: HTTPS/REST & GraphQL
- AWS API Gateway -> Envoy Service Mesh: mTLS
- Envoy Service Mesh -> ECS Microservices: gRPC/HTTP
- Order & Checkout Service -> PgBouncer (Writer Endpoint): PostgreSQL Wire Protocol over TLS
- Catalog Service -> PgBouncer (Reader Endpoint): PostgreSQL Wire Protocol over TLS
- Microservices -> Amazon S3, Amazon EventBridge, Amazon SQS: AWS SDK over HTTPS

## Technology Stack
- **Cloud Infrastructure:** AWS (us-east-1, eu-west-1, ap-southeast-1) for multi-region scalability.
- **Compute:** AWS ECS on Fargate for containerized microservice execution.
- **Database:** Amazon Aurora PostgreSQL 15+ with Aurora Global Databases for multi-region replication and fast failover.
- **Connection Management:** PgBouncer (sidecar) for connection pooling and preventing exhaustion.
- **Security & Compliance:** AWS KMS (encryption at rest), IAM Database Authentication, Aurora Advanced Auditing, and Strict TLS (`verify-full`).
- **Caching:** Amazon ElastiCache (Redis) for high-performance caching.

## Rationale
Aurora PostgreSQL Global Databases combined with PgBouncer connection pooling and read/write splitting ensures low-latency global performance, sub-30-second failovers, and high availability. AWS ECS on Fargate, S3, and CloudFront natively support 1M MAU scaling requirements while maintaining strict GDPR/CCPA compliance and OWASP mitigations.