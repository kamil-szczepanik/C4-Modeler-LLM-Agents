## Overview
An Amazon-style e-commerce online bookstore providing catalogue browsing, secure checkout, customer reviews, and personalized recommendations. Built for global scalability, it supports multi-currency transactions and strict privacy compliance.

## Key Elements
- **Users**: Customers, Store Administrators, Content/Marketing Managers
- **Frontend**: Single Page Application (React / TypeScript)
- **Edge**: Amazon CloudFront, AWS API Gateway / ALB, Route 53
- **Services (AWS ECS Fargate)**: Catalog & Search, Checkout & Payment, Recommendation Service
- **Data & Messaging**: Amazon Aurora PostgreSQL Global Database, Amazon SQS/SNS, Redis, Elasticsearch
- **External Systems**: Stripe, PayPal, FedEx, UPS, AWS Cognito / Auth0, AWS SES / SendGrid

## Relationships
- **SPA to API Gateway**: HTTPS (REST / GraphQL)
- **API Gateway to ECS Fargate**: HTTPS, gRPC (internal service mesh)
- **Services to Database**: SQL over TLS (Aurora PostgreSQL Global Database)
- **Services to Messaging**: AMQP / AWS SQS/SNS for asynchronous shipping events
- **Checkout Service to Gateways**: HTTPS (Stripe / PayPal APIs)

## Technology Stack
- **Frontend Hosting**: Amazon S3 + CloudFront CDN for global low-latency content delivery (<2s page load).
- **Compute**: AWS ECS Fargate running Go, Node.js, and Python/FastAPI microservices for serverless container scalability.
- **Database**: Amazon Aurora PostgreSQL Global Database for multi-region active-active replication and data residency.
- **Caching & Search**: Redis for cart state locking; Elasticsearch for keyword catalogue search.
- **Security**: AWS Cognito / Auth0 for OAuth2/OIDC; AWS Secrets Manager for secure credential rotation.

## Rationale
The multi-region active-active deployment across `us-east-1`, `eu-west-1`, and `ap-southeast-1` guarantees 99.95% uptime and handles 1M MAU while maintaining sub-2-second page loads. Asynchronous messaging via SQS/SNS isolates third-party shipping API bottlenecks, ensuring high availability and secure, GDPR-compliant retail operations.