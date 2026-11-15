## Overview
[The Online Bookstore system provides a scalable, secure, and compliant e-commerce platform for catalog browsing, ordering, and personalized recommendations. It guarantees high availability and sub-second performance for 1 million monthly active users globally across AWS regions.]

## Key Elements
- **Users**: Book Buyers, Registered Reviewers, Store Administrators
- **External Systems**: Payment Gateway, Shipping Providers, Tax & Compliance Service, Identity Provider, CDN / Edge WAF, Marketing & Email Service, Observability & APM
- **Frontend Container**: Frontend SPA (React, Next.js, AWS S3, CloudFront CDN)
- **Backend Containers**: API Gateway (AWS API Gateway), Catalog & Search Service (ECS Fargate, Node.js/Go), Order & Checkout Service (ECS Fargate, Java/Spring Boot), Recommendation Service (ECS Fargate, Python/FastAPI), Pricing & Localization Service (ECS Fargate, Polyglot backend)
- **Data & Infrastructure Containers**: Relational Database (AWS RDS PostgreSQL), Search Index (AWS OpenSearch), Cache & Session Store (AWS ElastiCache (Redis)), Event Bus / Messaging (AWS EventBridge, SNS, SQS)
- **Cache Components**: Session Manager Component, Catalog & Pricing Cache Component, Rate Limiter & Throttle Component

## Relationships
- Frontend SPA -> CDN / Edge WAF: HTTPS
- API Gateway -> Order & Checkout Service: Encrypted HTTP/REST
- Order & Checkout Service -> Cache & Session Store (Session Manager): Encrypted TCP via Redis Protocol
- Catalog & Search Service -> Cache & Session Store (Catalog & Pricing Cache): Read/Write product details [Encrypted TCP via Redis Protocol]
- Pricing & Localization Service -> Cache & Session Store (Catalog & Pricing Cache): Read exchange rates [Encrypted TCP]
- API Gateway -> Cache & Session Store (Rate Limiter): Check rate limits [Encrypted TCP]

## Technology Stack
- **Compute**: AWS ECS Fargate for containerized microservices across multiple regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`)
- **Cache & Session**: AWS ElastiCache (Redis) configured with Cluster Mode, Multi-AZ, `volatile-lru` eviction, and Redis ACLs for segregated isolation
- **Database**: AWS RDS PostgreSQL with AWS KMS encryption at rest
- **Search**: AWS OpenSearch for catalog keyword search and recommendations
- **Security & Networking**: TLS 1.3 for encryption in transit, AWS Secrets Manager for Redis AUTH rotation, and AWS IAM / Security Groups for strict network boundaries

## Rationale
[This architecture leverages AWS managed services and a decomposed ElastiCache Redis topology to satisfy stringent performance, scalability, and security mandates. Strict component isolation, multi-region replication, and automated encryption ensure compliance with GDPR/CCPA while maintaining 99.95% uptime and sub-second page loads.]