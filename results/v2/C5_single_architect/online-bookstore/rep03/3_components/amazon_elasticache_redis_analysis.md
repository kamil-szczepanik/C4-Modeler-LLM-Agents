## Overview
The Online Bookstore is a scaled-down e-commerce system built for purchasing physical and electronic books with recommendations and reviews. It utilizes a microservices architecture deployed on AWS to support global users with high availability and low latency.

## Key Elements
- Customers and Administrators (Users)
- React SPA, AWS CloudFront, Amazon S3
- AWS API Gateway
- Catalog, Order & Checkout, Recommendation, and Email Services (Node.js, NestJS, Amazon ECS/Fargate)
- Amazon RDS (PostgreSQL), Amazon OpenSearch, Amazon DynamoDB
- Amazon ElastiCache (Redis) with SessionStore, RecommendationCache, and CatalogCache components
- External Systems: Payment Gateway, Shipping Provider APIs, Email Service, Identity Provider, Tax Calculation Service

## Relationships
- React SPA -> AWS API Gateway [HTTPS/JSON]
- API Gateway -> Catalog Service, Order & Checkout Service, Recommendation Service [gRPC / HTTPS]
- Order & Checkout Service -> Amazon RDS (PostgreSQL) [SQL/TCP] and `SessionStore` [Redis Protocol / TCP]
- Catalog Service -> Amazon OpenSearch [HTTPS] and `CatalogCache` [Redis Protocol / TCP]
- Recommendation Service -> `RecommendationCache` [Redis Protocol / TCP]
- Services -> AWS EventBridge & SQS [AMQP/HTTPS]

## Technology Stack
- Frontend: React hosted on Amazon S3 and distributed via AWS CloudFront for global reach.
- Compute: Amazon ECS with AWS Fargate for serverless container orchestration.
- Databases: Amazon RDS PostgreSQL for transactional data, Amazon OpenSearch for search, Amazon DynamoDB for reviews/ratings, and Amazon ElastiCache (Redis) for caching and sessions.
- Messaging: AWS EventBridge and Amazon SQS for asynchronous event-driven communication.

## Rationale
This architecture ensures 99.95% uptime and scalability for 1M MAU through containerized microservices and managed AWS infrastructure. Redis caching and global CDNs guarantee sub-2-second page loads on 3G connections.