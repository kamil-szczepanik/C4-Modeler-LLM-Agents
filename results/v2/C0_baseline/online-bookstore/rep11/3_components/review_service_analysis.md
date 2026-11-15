## Overview
The Online Bookstore is a globally scaled e-commerce system providing physical and electronic book purchasing, catalog browsing, and personalized recommendations. The architecture leverages AWS multi-region infrastructure to ensure high availability, performance, and GDPR compliance.

## Key Elements
- Customers (Shoppers, Registered Reviewers, Content Moderators)
- Amazon API Gateway / Application Load Balancer
- Single Page Application (React / TypeScript, Amazon S3, Amazon CloudFront)
- Review Service (AWS ECS / Fargate, Spring Boot / Java)
- Catalogue & Search, Checkout & Cart, and Recommendation Services
- Amazon RDS (PostgreSQL with read replicas) and Amazon ElastiCache (Redis)
- Amazon SQS, SNS, and Kinesis

## Relationships
- Customer -> Single Page Application [HTTPS]
- Single Page Application -> API Gateway / Load Balancer [HTTPS / REST]
- API Gateway -> Review Service API Controller [HTTPS / REST]
- Review Service -> Amazon SQS / SNS [AWS SQS/SNS protocol]
- Review Service -> Amazon RDS (PostgreSQL) [JDBC / PostgreSQL]
- Review Service -> Identity & Notification Service [HTTPS / REST]

## Technology Stack
- **Frontend:** React / TypeScript hosted on Amazon S3 and distributed via Amazon CloudFront for sub-2-second page loads.
- **Compute:** AWS ECS / Fargate containers managed via Terraform and automated CI/CD pipelines.
- **Database:** Amazon RDS (PostgreSQL) with cross-region read replicas for multi-region scalability.
- **Messaging:** Amazon SQS and SNS for decoupled, asynchronous event-driven processing and high availability.
- **Security:** AWS KMS for data encryption at rest, TLS 1.3 for transit, and JSON Web Tokens (JWT) for RBAC.

## Rationale
This architecture decouples core domains using asynchronous messaging via SQS/SNS to guarantee 99.95% availability and resilience against traffic spikes. Utilizing ECS Fargate, multi-region RDS replicas, and AWS edge services satisfies stringent performance, security, and global scaling requirements.