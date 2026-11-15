## Overview
The Online Bookstore system is a scaled-down Amazon-style e-commerce platform enabling shoppers to browse, search, and purchase physical and electronic books with recommendations and reviews. It ensures high scalability, multi-currency support, and strict compliance across multiple AWS regions.

## Key Elements
- Shopper and Customer Support Agent
- AWS Route 53, AWS CloudFront, Amazon S3
- React SPA, AWS API Gateway
- Catalog Service (Amazon ECS/Fargate)
- Order & Checkout Service, User & Compliance Service, Notification Service, Recommendation Worker
- Amazon RDS PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis)
- Catalog Service Components: Product API Controller, Search & Filter Engine, Catalog Management Domain Logic, Cache-Aside Proxy, Data Access Layer, Localized Pricing Service, Search Analytics Collector

## Relationships
- AWS API Gateway -> Catalog Service [gRPC over TLS in private VPC subnets]
- Product API Controller -> Search & Filter Engine [In-memory]
- Catalog Management Domain Logic -> Localized Pricing Service & Cache-Aside Proxy [In-memory]
- Catalog Management Domain Logic -> Data Access Layer [JDBC]
- Catalog Service -> Amazon RDS PostgreSQL [SQL with cross-region read replicas]
- Catalog Service -> Amazon DynamoDB [NoSQL]
- Catalog Service -> Amazon ElastiCache (Redis) [Redis Protocol with circuit breakers]
- Search & Filter Engine -> Amazon SQS [AWS SDK]

## Technology Stack
- Spring Boot / Node.js on Amazon ECS/Fargate for containerized microservices
- Amazon RDS PostgreSQL with cross-region replication for transactional and localized catalog data
- Amazon ElastiCache (Redis) for sub-10ms caching of top-selling books and promotional banners
- Amazon DynamoDB for promotional data storage
- Amazon SQS for asynchronous event publishing (search analytics)
- AWS X-Ray and CloudWatch for distributed tracing and observability

## Rationale
This architecture uses Amazon ECS/Fargate microservices paired with Redis caching and PostgreSQL read replicas to easily meet the 1M MAU scalability, sub-2-second performance, and 99.95% uptime requirements across three global regions. Isolated components for pricing, search, and resilient circuit breakers cleanly address regional compliance, multi-currency display, and fault tolerance.