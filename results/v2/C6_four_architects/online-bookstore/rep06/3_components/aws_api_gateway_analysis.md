## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform for purchasing physical and electronic books with recommendations and reviews. The architecture leverages AWS to support 1 million monthly active users (MAU) with 99.95% uptime and GDPR/CCPA compliance.

## Key Elements
- **Users:** Customer, Store Administrator
- **External Systems:** Payment Gateway, Third-Party Shipping API, Notification Service, Currency Exchange Rate API
- **Frontend Container:** React Single-Page Application (SPA) (React, AWS CloudFront, Amazon S3)
- **API Gateway Container:** AWS API Gateway (Custom Domain & SSL/TLS Termination, AWS WAF, Amazon Cognito JWT Authorizer, API Router & Validator, API Gateway Usage Plans & Throttling, Request Transformer, Endpoint Logging & Metrics, Mock / Documentation)
- **Backend Containers:** Core E-Commerce Service, Recommendation Engine, Audit & Compliance Service, Integration Service, Search & Analytics Service (Node.js/Python on Amazon ECS Fargate)
- **Data & Messaging:** Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis), Amazon EventBridge, Amazon SQS/SNS, AWS Lambda

## Relationships
- React SPA -> AWS API Gateway: Interacts via [HTTPS/REST]
- AWS API Gateway -> Core E-Commerce Service: Routes requests via [HTTPS/gRPC]
- AWS API Gateway -> Audit & Compliance Service: Routes compliance queries via [HTTPS/gRPC]
- AWS API Gateway -> Search & Analytics Service: Routes search and review queries via [HTTPS/gRPC]
- Core E-Commerce Service -> Amazon Aurora PostgreSQL & Amazon ElastiCache (Redis): Persists data and manages cache via [TCP]

## Technology Stack
- **Frontend:** React hosted on Amazon S3 and distributed via AWS CloudFront for low-latency delivery.
- **API Gateway:** AWS API Gateway managed with AWS WAF, Amazon Cognito, and AWS Certificate Manager for edge security and routing.
- **Backend Services:** Node.js (TypeScript) and Python deployed on Amazon ECS Fargate for elastic scalability.
- **Databases & Cache:** Amazon Aurora PostgreSQL, Amazon DynamoDB, and Amazon ElastiCache (Redis) for transactional data, flexible storage, and caching.
- **Integration:** Amazon EventBridge and Amazon SQS/SNS for asynchronous event-driven messaging.

## Rationale
This architecture uses serverless and containerized AWS services to ensure high availability (99.95%) and auto-scaling to handle 1M MAU. Separation of concerns across ECS Fargate services and strict edge security via WAF and Cognito meet performance, GDPR/CCPA compliance, and OWASP Top-10 requirements.