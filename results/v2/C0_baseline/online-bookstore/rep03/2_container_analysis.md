## Overview
- An Amazon-style online bookstore designed to handle physical and electronic book sales, customer reviews, and personalized recommendations.
- Built for global scale across three AWS regions supporting 1M MAU while ensuring strict GDPR, CCPA, and PCI-DSS compliance.

## Key Elements
- **Users**: Customers (Shoppers), Book Authors/Publishers, Store Administrators.
- **Frontend Container**: Single Page App (SPA) built with React, hosted on Amazon CloudFront and S3.
- **Routing Container**: Amazon API Gateway for rate limiting, SSL termination, and OAuth2/JWT authentication.
- **Backend Containers**: Node.js BFF, Java/Spring Boot Checkout Service, Python FastAPI Recommendations Service, and a dedicated Notification Service running on AWS ECS (Fargate).
- **Data & Storage Containers**: Amazon Aurora (PostgreSQL), Amazon ElastiCache (Redis), Amazon DynamoDB, and Aurora Global Databases.
- **External Systems**: Stripe/PayPal, FedEx/DHL, Auth0/AWS Cognito, SendGrid/Twilio, Segment/Snowflake.

## Relationships
- **SPA to API Gateway**: HTTPS / REST for client-to-backend communication.
- **API Gateway to BFF/Containers**: mTLS via AWS App Mesh and internal VPC endpoints.
- **Checkout Service to Stripe/PayPal**: Synchronous HTTPS for secure payment processing.
- **Containers to Event Broker**: Asynchronous event publishing and consumption via Amazon EventBridge and SQS.
- **Containers to Databases**: TLS-encrypted connections to Aurora, DynamoDB, and ElastiCache.

## Technology Stack
- **Frontend**: React, Amazon CloudFront, S3 for static asset delivery and low-latency global rendering.
- **Backend Compute**: AWS ECS (Fargate) for serverless container orchestration with zero-downtime deployments.
- **Languages**: Node.js (BFF), Java/Spring Boot (Checkout), Python (Recommendations).
- **Databases**: Amazon Aurora PostgreSQL (transactional data), Redis (sessions/caching), Amazon DynamoDB (recommendations).
- **Messaging & Security**: Amazon EventBridge/SQS, AWS KMS, AWS Secrets Manager, Auth0/Cognito, OpenTelemetry (OTel).

## Rationale
- Microservices running on AWS ECS Fargate isolate critical domains like Checkout and Recommendations, protecting the PCI-DSS boundary and ensuring the system easily scales to 1M MAU.
- Asynchronous event-driven patterns and multi-region Aurora Global Databases guarantee high availability (99.95%), low latency (<2s page loads), and strict GDPR/CCPA data residency compliance.