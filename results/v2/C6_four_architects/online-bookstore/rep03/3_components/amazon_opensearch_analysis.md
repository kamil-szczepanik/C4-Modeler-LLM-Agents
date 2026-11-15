## Overview
The Online Bookstore system uses a microservices-based e-commerce platform on AWS to support global book sales, search, and secure checkout. It ensures high performance, multi-region scalability, and strict regulatory compliance.

## Key Elements
- **Customers & Store Administrators**: End-users and back-office staff.
- **Frontend Containers**: React SPA deployed via Amazon S3 and CloudFront.
- **Backend Services**: Catalog & Search, Order & Checkout, Payment & Currency, Recommendation & Review, Data Privacy & User, Admin & Content Management, Async Worker Services (Spring Boot, Node.js, .NET Core, Python).
- **Data & Search Stores**: Amazon RDS PostgreSQL, Amazon DynamoDB, Amazon ElastiCache Redis, Amazon OpenSearch.
- **External Systems**: Stripe, PayPal, UPS, FedEx, Avalara, AWS SES/SNS, AWS Personalize, AWS Fraud Detector, AWS CloudWatch.

## Relationships
- React SPA -> Amazon API Gateway: Forwards client requests [HTTPS/REST]
- Catalog & Search Service -> Amazon OpenSearch: Queries catalogue search indices [HTTPS/REST via OpenSearch DSL]
- Async Worker Service -> Amazon OpenSearch: Syncs catalogue update events [HTTPS/REST]
- Cluster Management & Storage -> Amazon CloudWatch: Emits health metrics and logs [AWS API/HTTPS]

## Technology Stack
- **Frontend**: React, Amazon S3, Amazon CloudFront for low-latency global delivery.
- **Backend**: Spring Boot, Node.js, .NET Core, Python for specialized domain services.
- **Databases & Caching**: Amazon RDS (PostgreSQL), Amazon DynamoDB, Amazon ElastiCache (Redis) for transactional and session data.
- **Search & Messaging**: Amazon OpenSearch for catalog indexing; Amazon EventBridge and SQS for async event-driven decoupling.
- **Cloud Infrastructure**: AWS (us-east-1, eu-west-1, ap-southeast-1) for multi-region high availability.

## Rationale
This architecture decouples core domain services to easily scale and handle 1 million MAU with low latency. Leveraging managed AWS services guarantees 99.95% uptime and meets strict security, privacy, and performance requirements.