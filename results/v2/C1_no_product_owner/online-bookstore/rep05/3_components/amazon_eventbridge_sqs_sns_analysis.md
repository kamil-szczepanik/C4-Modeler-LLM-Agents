## Overview
The Online Bookstore system is a scalable e-commerce platform for physical and electronic books, supporting browsing, secure checkout, reviews, and recommendations. It relies on a distributed event-driven architecture hosted on AWS to handle high traffic and meet strict availability and compliance goals.

## Key Elements
- React Single-Page Application (SPA) hosted on Amazon S3 and distributed via Amazon CloudFront
- Microservices running on Amazon ECS (Fargate): Catalog Service, Order & Checkout Service, Recommendation Service
- Data & Search stores: Amazon RDS (PostgreSQL), Amazon DynamoDB, Amazon ElastiCache (Redis), Amazon OpenSearch Service
- Messaging & Integration backbone: Amazon EventBridge, Amazon SNS, Amazon SQS
- External services: Stripe, FedEx/UPS, Avalara, Auth0/AWS Cognito, SendGrid/AWS SES

## Relationships
- React SPA -> Amazon API Gateway: Client requests [HTTPS / JSON]
- Services -> Amazon EventBridge, SQS, SNS: Asynchronous domain event publishing and consumption [AWS SDK with SigV4 over HTTPS]
- Services -> Amazon RDS (PostgreSQL) / DynamoDB / OpenSearch: Data persistence and search queries [TCP / TLS]
- Order & Checkout Service -> Stripe / FedEx / Avalara: Payment, shipping, and tax calculations [REST APIs over HTTPS]

## Technology Stack
- React & Node.js / Express / Python FastAPI / Spring Boot: Frontend and microservices implementation for modularity and performance
- Amazon ECS (Fargate): Serverless container orchestration for scalability without server management
- Amazon PostgreSQL, DynamoDB, Redis, OpenSearch: Purpose-built data layers for transactional, caching, and search needs
- Amazon EventBridge, SQS, SNS: Asynchronous messaging with DLQs and KMS encryption for decoupled microservices

## Rationale
This architecture uses serverless containers and managed AWS services to easily scale to 1 million MAU while maintaining sub-second performance. The event-driven messaging topology isolates failure domains to achieve 99.95% availability.