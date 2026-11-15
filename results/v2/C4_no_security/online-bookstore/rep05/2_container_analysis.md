## Overview
An Amazon-style online bookstore providing physical and electronic book sales, search, reviews, and recommendations. The architecture ensures high availability, low latency, and global regulatory compliance.

## Key Elements
- **Customers, Authors, Administrators**: End-users and back-office staff.
- **SPA**: React/TypeScript single page application.
- **API Gateway**: AWS API Gateway and Application Load Balancer (ALB).
- **Core Microservices**: Catalog & Search (Node.js), Checkout & Order (Go/Java), Recommendation (Python/FastAPI), Data Privacy, and Localization Services hosted on Amazon ECS with Fargate.
- **Data Stores**: Amazon Aurora (PostgreSQL), Amazon DynamoDB, and Amazon OpenSearch.
- **Messaging**: Amazon SQS and SNS with Dead Letter Queues (DLQs).
- **External Systems**: Payment Gateway, Shipping Provider APIs, Identity Provider, Notification System, and Tax Calculation Service.

## Relationships
- **SPA to API Gateway**: HTTPS/REST and WebSockets.
- **Internal Microservices**: gRPC for synchronous communication and Amazon SQS/SNS for asynchronous event-driven workflows.
- **Data Stores to Services**: Secure VPC connections with Amazon Aurora Global Databases.
- **External APIs**: Secure REST integration protected by circuit breakers.

## Technology Stack
- **Frontend Hosting**: Amazon CloudFront and S3 for fast global content delivery.
- **Compute**: Amazon ECS on AWS Fargate for scalable container orchestration.
- **Databases**: Amazon Aurora (PostgreSQL) for transactional safety, DynamoDB for cart sessions, and OpenSearch for catalogue search.
- **Infrastructure & Observability**: Terraform for IaC, AWS CloudWatch, and AWS X-Ray for distributed tracing.

## Rationale
Container separation and event-driven decoupling via SQS/SNS guarantee 99.95% availability and fault isolation during traffic spikes or third-party outages. Multi-region AWS deployment with localized data privacy services ensures GDPR/CCPA compliance and sub-second page loads globally.