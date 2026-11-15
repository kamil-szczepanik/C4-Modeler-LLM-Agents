## Overview
- Online Bookstore e-commerce system built on AWS supporting 1M MAU.
- Provides scalable book cataloging, secure checkout, multi-currency pricing, and GDPR/CCPA compliance.

## Key Elements
- Frontend SPA: React, Next.js, AWS S3, CloudFront CDN
- API Gateway: AWS API Gateway
- Microservices: Catalog, Order, Recommendation, Pricing (ECS Fargate, Node.js/Go/Python/Java)
- Relational Database: AWS RDS PostgreSQL with Multi-AZ, Read Replicas, and PgBouncer
- Search & Cache: AWS OpenSearch, AWS ElastiCache (Redis)
- Messaging: AWS EventBridge, SNS, SQS

## Relationships
- Frontend SPA -> API Gateway: Client requests [HTTPS/WSS]
- API Gateway -> ECS Fargate Services: Routes REST/GraphQL traffic [HTTP/JSON]
- Microservices -> Relational Database: Persistent queries and transactions [TCP/TLS 1.3, mTLS]
- Microservices -> AWS ElastiCache: Caching and session management [Redis Protocol]
- Microservices -> AWS OpenSearch: Catalogue keyword search [HTTPS]

## Technology Stack
- AWS RDS PostgreSQL: ACID compliance for financial orders and multi-currency data.
- PgBouncer: Connection pooling to handle 1M MAU scaling requirements.
- AWS ECS Fargate: Serverless container execution for microservices.
- AWS ElastiCache (Redis): Low-latency caching for high performance.
- AWS KMS & Secrets Manager: Encryption and automated credential rotation for security.

## Rationale
- This architecture guarantees high availability (99.95% uptime) and performance (<2s page load) through read replicas, connection pooling, and multi-region deployment.
- It ensures strict data protection and regulatory compliance via encryption at rest, schema-level isolation, and pgaudit logging.