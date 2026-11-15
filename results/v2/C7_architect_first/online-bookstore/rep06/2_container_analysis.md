## Overview
The Online Bookstore is a globally distributed, scalable e-commerce platform designed to support 1 million MAU with 99.95% uptime. It enables users to browse, purchase, review, and receive book recommendations securely across multiple regions.

## Key Elements
- Single Page Application (React/TypeScript)
- API Gateway (AWS API Gateway)
- Core API Application (Node.js/Express)
- Recommendation Service (Python/FastAPI)
- Admin Dashboard Container
- Database & Cache (Amazon Aurora PostgreSQL & ElastiCache Redis)
- Messaging & Integration (Amazon SQS/SNS & EventBridge)

## Relationships
- Users access SPA via Amazon CloudFront (HTTPS)
- SPA communicates with API Gateway via HTTPS/REST/GraphQL
- API Gateway routes traffic to Core API, Recommendation Service, and Admin Dashboard via mTLS / AWS Service Connect
- Core API interacts with Aurora PostgreSQL (JDBC/TLS) and ElastiCache Redis (RESP)
- Core API publishes events to SQS/SNS/EventBridge for asynchronous shipping, notification, and analytics processing
- Services egress securely through AWS Network Firewall to third-party payment and shipping APIs

## Technology Stack
- **Frontend Hosting:** Amazon S3 & CloudFront for static asset delivery and sub-2s global page loads
- **Compute:** Amazon ECS (Fargate) for serverless container orchestration across regions
- **Database:** Amazon Aurora PostgreSQL with regional read replicas and partitioning for GDPR/CCPA data residency
- **Caching & Messaging:** Amazon ElastiCache (Redis) for cache-aside patterns; Amazon SQS/SNS/EventBridge for async decoupling and resilience
- **Security & DevOps:** AWS KMS (SSE), AWS Secrets Manager, IAM task roles, AWS Network Firewall, Terraform/CDK, and AWS X-Ray

## Rationale
This multi-region AWS architecture guarantees 99.95% uptime and sub-2s performance via edge caching, regional database partitioning, and asynchronous decoupling. It enforces strict GDPR/CCPA compliance and OWASP security standards through localized PII storage, mTLS, and rigorous egress filtering.