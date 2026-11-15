## Overview
- The system is an online bookstore providing catalog browsing, shopping carts, secure checkout, reviews, and personalized recommendations for 1 million monthly active users.
- The architecture utilizes a scalable, cloud-native AWS microservices ecosystem designed to ensure high performance, GDPR/CCPA compliance, and 99.95% availability.

## Key Elements
- Users: Customer, Inventory Manager, Customer Support Representative
- External Systems: AWS Cognito, Payment Gateway, Shipping APIs, Notification Service, Publisher Partner Systems
- Frontend Container: Single-Page Application (SPA) (React/TypeScript, AWS S3, Amazon CloudFront)
- Gateway Container: Amazon API Gateway (AWS)
- Backend Containers: Catalog & Search Service, Order & Checkout Service, Recommendation Service, Localization Service, Review Moderation Container (all Node.js/Express or Java/Spring Boot or Python/FastAPI, Amazon ECS on AWS Fargate)
- Database Containers: Amazon Aurora PostgreSQL (Multi-AZ/Global), Amazon DynamoDB, Amazon ElastiCache (Redis)
- Messaging Container: Amazon SQS/SNS (AWS)
- DynamoDB Components: Cart Table Component, Session Store Component, DynamoDB Streams Component

## Relationships
- `SPA` -> `Amazon API Gateway`: Routes client requests [HTTPS/TLS]
- `Amazon API Gateway` -> `ECS Containers`: Dispatches microservice requests [HTTP/REST/gRPC]
- `Order & Checkout Service` -> `Cart Table Component`: Reads/deletes cart items during checkout via AWS SDK [HTTPS/TLS with SigV4]
- `Cart Table Component` -> `DynamoDB Streams Component`: Emits real-time item mutation events [Internal AWS IPC]
- `DynamoDB Streams Component` -> `Amazon SQS/SNS`: Forwards cart abandonment events [AWS SDK / HTTPS]

## Technology Stack
- Cloud Provider: AWS (us-east-1, eu-west-1, ap-southeast-1 regions) for global multi-region scalability and high availability.
- Frontend: React & TypeScript hosted on AWS S3 and distributed via Amazon CloudFront for sub-2-second page loads.
- Compute: Amazon ECS on AWS Fargate for serverless container orchestration of microservices.
- Databases: Amazon Aurora PostgreSQL for relational data, Amazon DynamoDB for low-latency shopping carts and sessions, and Amazon ElastiCache (Redis) for caching.
- Security & Messaging: AWS KMS for encryption at rest, AWS IAM (SigV4) for service-to-service auth, and Amazon SQS/SNS for asynchronous event-driven messaging.

## Rationale
- This architecture uses managed serverless and containerized AWS services to effortlessly scale to 1 million MAU while guaranteeing 99.95% uptime and sub-2-second page loads.
- Strict adherence to AWS KMS, IAM least privilege, and DynamoDB operational controls ensures robust GDPR/CCPA compliance and data protection without sacrificing performance.