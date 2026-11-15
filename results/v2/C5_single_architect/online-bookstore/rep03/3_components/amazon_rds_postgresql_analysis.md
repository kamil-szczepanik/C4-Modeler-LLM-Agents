## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform designed to provide book browsing, secure checkout, reviews, and personalized recommendations. It operates globally across AWS regions while maintaining high availability, regulatory compliance, and performance standards.

## Key Elements
- **Customer & Administrator**: End-users and system managers.
- **Single-Page App (SPA)**: React hosted on AWS S3 and distributed via Amazon CloudFront.
- **API Gateway**: AWS API Gateway managing client entry points.
- **Backend Services**: Catalog, Order & Checkout, Recommendation, and Email services running on Amazon ECS/Fargate using Node.js and NestJS.
- **Data & Caching Tiers**: Amazon RDS (PostgreSQL) with Connection Pooler, Read Replica, Audit, and PITR components; Amazon OpenSearch; Amazon DynamoDB; Amazon ElastiCache (Redis).
- **External Systems**: Payment Gateway, Shipping Provider APIs, Email Service, Identity Provider, Tax Calculation Service, AWS Secrets Manager, AWS EventBridge, and SQS.

## Relationships
- **SPA -> API Gateway**: HTTPS / REST and GraphQL.
- **API Gateway -> ECS/Fargate Services**: gRPC and REST over HTTPS.
- **Order & Checkout Service -> Connection Pooler Component**: SQL over TLS (PostgreSQL Protocol / TCP 5432).
- **Connection Pooler Component -> Relational Schema Component**: TCP Local / Unix Domain Sockets.
- **Relational Schema Component -> Read Replica Component**: Asynchronous replication.

## Technology Stack
- **AWS Cloud (us-east-1, eu-west-1, ap-southeast-1)**: Multi-region target deployment providing 99.95% availability.
- **Amazon ECS / Fargate**: Container orchestration for microservices ensuring scalability for 1M MAU.
- **Amazon RDS (PostgreSQL)**: ACID-compliant relational data storage with `pgAudit` and AWS Automated Backups for GDPR/CCPA compliance.
- **PgBouncer / RDS Proxy**: Connection pooling to mitigate exhaustion under high concurrency.
- **AWS Secrets Manager**: Secure, automated database credential rotation supporting OWASP Top-10 mitigations.

## Rationale
This architecture uses cloud-native managed services and containerization to achieve high scalability, low-latency performance, and strict transactional integrity. Distributed storage and caching layers ensure compliance, reliability, and security across multi-currency and global traffic demands.