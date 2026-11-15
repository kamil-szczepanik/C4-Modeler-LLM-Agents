## Overview
The Online Bookstore is a scaled-down e-commerce system designed to provide book browsing, secure checkout, reviews, and recommendations. It is engineered to support 1 million monthly active users globally with high availability and compliance standards.

## Key Elements
- **Customer**: End-user interacting with the bookstore.
- **Single Page Application**: React and TypeScript interface hosted on AWS S3 and CloudFront.
- **API Gateway**: AWS API Gateway routing traffic via gRPC and HTTP.
- **Order & Checkout Service**: Node.js container decomposed into Cart Controller & Manager, Checkout Orchestrator with Saga/State Machine, Fulfillment Adapter, Domain Event Publisher, and Order Repository.
- **External Systems**: Payment Gateway, Shipping Provider API, Tax Calculation Service, Identity Provider, Notification Service.
- **Databases & Cache**: PostgreSQL (RDS), MongoDB, Vector DB, and Amazon ElastiCache Redis.

## Relationships
- **API Gateway -> Order & Checkout Service**: Routes checkout and order requests [gRPC / HTTP]
- **Order & Checkout Service -> Amazon ElastiCache (Redis)**: Reads and writes cached session and order data [TCP]
- **Order & Checkout Service -> AWS SQS / SNS**: Publishes asynchronous events via AWS SDK
- **Checkout Orchestrator -> Payment Gateway**: Processes secure payments [HTTPS]
- **Checkout Orchestrator -> Tax Calculation Service**: Queries regional tax rates [HTTPS]
- **Fulfillment Adapter -> Shipping Provider API**: Requests fulfillment and shipping labels [HTTPS]

## Technology Stack
- **Frontend**: React, TypeScript, AWS S3, AWS CloudFront for low-latency global delivery.
- **Backend Services**: Node.js (Order & Checkout), Go (Catalog), Python FastAPI (Recommendations), Java Spring Boot (Reviews).
- **Databases**: PostgreSQL (RDS) for transactional data, MongoDB for reviews, Vector DB for recommendations.
- **Messaging & Cache**: AWS SQS/SNS for asynchronous messaging, Redis for session caching.
- **Infrastructure**: AWS deployed across us-east-1, eu-west-1, and ap-southeast-1.

## Rationale
This multi-region AWS architecture ensures 99.95% uptime and high scalability to handle 1M MAU while meeting strict GDPR, CCPA, and OWASP security requirements. Decomposing the Order & Checkout Service with a Saga state machine guarantees ACID compliance and reliable distributed transactions across third-party APIs.