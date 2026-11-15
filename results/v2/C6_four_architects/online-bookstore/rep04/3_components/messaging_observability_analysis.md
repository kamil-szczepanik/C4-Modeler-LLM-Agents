## Overview
The Online Bookstore is a scaled-down e-commerce platform providing catalog browsing, secure checkout, recommendations, and reviews. Its core purpose is delivering a reliable, compliant multi-currency retail experience for 1M Monthly Active Users (MAU).

## Key Elements
- Customers and Store Administrators
- Single-Page Application (React/TypeScript)
- Amazon API Gateway
- Catalog Service (Node.js/ECS Fargate)
- Order & Checkout Service (Java/Spring Boot/ECS Fargate)
- Recommendation Service (Python/FastAPI/ECS Fargate)
- Auth Service, Privacy Service, Background Worker (ECS Fargate)
- Messaging & Observability (Amazon SNS, SQS, CloudWatch, AWS X-Ray, EventBridge Schema Registry)
- Databases & Storage: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon OpenSearch, Amazon S3, Amazon CloudFront
- External Systems: Payment Gateway, Shipping Provider APIs, Identity Provider, Tax Calculation Service, Notification Service

## Relationships
- Single-Page Application -> Amazon API Gateway: HTTPS/JSON
- Amazon API Gateway -> Microservices (Catalog, Order, Recommendation, Auth, Privacy): Internal REST/gRPC
- Microservices -> Amazon Aurora PostgreSQL & Amazon DynamoDB: SQL/NoSQL queries
- Microservices -> Amazon SNS/SQS: Publish/Subscribe events [HTTPS/Internal AWS API]
- Services -> Amazon CloudWatch & AWS X-Ray: Emits logs, metrics, and traces [UDP/HTTPS]
- Order & Shipping Services -> External Shipping Provider APIs: REST [HTTPS]

## Technology Stack
- Frontend: React & TypeScript hosted on Amazon S3 and CloudFront for high-performance content delivery
- Compute: AWS ECS on AWS Fargate for scalable, serverless container orchestration
- Databases: Amazon Aurora PostgreSQL for relational transactional data, Amazon DynamoDB for fast key-value access, Amazon OpenSearch for keyword search
- Messaging & Observability: Amazon SNS/SQS for asynchronous events, CloudWatch and AWS X-Ray for telemetry, EventBridge Schema Registry for contract validation

## Rationale
This architecture uses serverless containers and managed AWS services to effortlessly scale to 1M MAU while maintaining 99.95% availability. Decoupled event-driven messaging ensures high performance, strict regional compliance, and resilience against failures.