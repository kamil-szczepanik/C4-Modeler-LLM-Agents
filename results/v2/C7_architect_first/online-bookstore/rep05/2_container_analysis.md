## Overview
The Online Bookstore is a globally distributed, highly scalable e-commerce platform designed to support 1 million monthly active users with 99.95% uptime and sub-2-second page loads. It provides secure multi-currency book browsing, checkout, recommendations, reviews, and strict GDPR/CCPA compliance across three AWS regions.

## Key Elements
- **Users**: Customers and Administrators.
- **Global Edge Layer**: Amazon CloudFront, Amazon Route 53, and AWS WAF.
- **Ingress**: Amazon API Gateway (REST/GraphQL).
- **Frontend Container**: React Single Page Application hosted in Amazon S3.
- **Backend Containers**: Catalog Service, Order & Checkout Service, Recommendation Service, Customer Privacy/Compliance Service, Notification Service, Review Service, and Analytics Ingestion Pipeline.
- **Databases & Caching**: Amazon Aurora (PostgreSQL), Amazon DynamoDB, and Amazon ElastiCache (Redis).
- **Messaging & Infrastructure**: Amazon SQS/SNS, Amazon ECS Fargate, AWS App Mesh, and AWS Secrets Manager.
- **External Systems**: Stripe/PayPal, FedEx/UPS, SendGrid/Amazon SES, and Fixer/Open Exchange Rates.

## Relationships
- Customers access the React SPA via HTTPS through Amazon CloudFront and Amazon Route 53.
- The SPA communicates with Amazon API Gateway using HTTPS/WSS for authentication and routing.
- Amazon API Gateway routes requests to internal ECS Fargate containers using gRPC over HTTP/2 via AWS App Mesh.
- Order & Checkout Service integrates securely with Stripe/PayPal via HTTPS and triggers third-party shipping APIs.
- Notification Service consumes events from Amazon SQS to send messages via SendGrid/Amazon SES.

## Technology Stack
- **Compute**: Amazon ECS Fargate for serverless container orchestration with minimal operational overhead.
- **Frontend**: React and Amazon S3 for fast global static asset delivery.
- **Databases**: Amazon Aurora PostgreSQL for transactional checkout integrity, DynamoDB for fast catalogue/search, and Redis for real-time recommendations.
- **Communication**: gRPC over HTTP/2 via AWS App Mesh for low-latency internal microservice communication.
- **Security & Compliance**: AWS Secrets Manager, AWS KMS, and AWS WAF for OWASP mitigations and data protection.

## Rationale
This containerized microservices architecture uses Amazon ECS Fargate and multi-region deployments to guarantee 99.95% availability and handle 1M MAU without performance degradation. Isolating core business domains into dedicated polyglot services ensures strict GDPR/CCPA compliance, payment security, and low-latency user experiences globally.