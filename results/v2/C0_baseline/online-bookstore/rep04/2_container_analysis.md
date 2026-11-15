## Overview
- An Amazon-style e-commerce site built for browsing, purchasing, reviewing, and receiving book recommendations.
- Designed to support 1 million monthly active users globally across AWS regions with high availability and GDPR/CCPA compliance.

## Key Elements
- **Users**: Book Buyer, Registered Reviewer, Store Administrator.
- **External Systems**: Stripe/PayPal, FedEx/UPS, Auth0/Cognito, AWS SES, Currency Exchange Rate Service.
- **Frontend Container**: React / TypeScript Single Page Application hosted on AWS S3 & CloudFront.
- **API & Routing Container**: AWS API Gateway.
- **Backend Containers**: Order & Checkout Service (Node.js), Catalog & Search Service (Java Spring Boot), Recommendations Service (Python FastAPI), Review Service (Node.js).
- **Data & Integration Containers**: Amazon RDS PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis), AWS EventBridge.

## Relationships
- **SPA to API Gateway**: HTTPS / JSON.
- **API Gateway to Backend Services**: mTLS / REST and gRPC (internal VPC).
- **Order & Checkout Service to External APIs**: HTTPS / REST to Stripe/PayPal and FedEx/UPS.
- **Backend Services to Event Bus**: Asynchronous event publishing to AWS EventBridge.
- **Backend Services to Databases**: Encrypted TCP connections to PostgreSQL, DynamoDB, and Redis.

## Technology Stack
- **Frontend**: React / TypeScript for fast, responsive client-side rendering.
- **Search**: Elasticsearch integrated with Java Spring Boot for rapid keyword queries.
- **Caching & Carts**: Amazon ElastiCache (Redis) for sub-millisecond cart persistence.
- **Databases**: Amazon RDS (PostgreSQL) and Amazon DynamoDB with Global Tables for multi-region durability.
- **Infrastructure**: AWS ECS/EKS with Terraform/CDK, AWS EventBridge, and AWS Secrets Manager.

## Rationale
- Microservices decomposition with asynchronous event-driven communication (AWS EventBridge) guarantees 99.95% availability and sub-2s page load times at 1M MAU scale.
- Multi-region AWS deployment with strict PII isolation and encryption ensures robust GDPR/CCPA compliance and OWASP Top-10 security.