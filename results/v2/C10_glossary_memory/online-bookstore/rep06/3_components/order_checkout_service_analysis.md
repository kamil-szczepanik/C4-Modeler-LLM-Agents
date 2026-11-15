## Overview
The Online Bookstore system is a cloud-native e-commerce platform providing catalog browsing, secure multi-currency checkout, and recommendations for books. It serves customers globally across multiple regions with high availability and stringent compliance standards.

## Key Elements
- Book Buyer (Customer)
- Storefront SPA (React on AWS S3 & CloudFront)
- API Gateway (AWS API Gateway)
- Order & Checkout Service (Node.js/Express)
- Catalog & Search Service (Go/Gin, Elasticsearch)
- Recommendation & Review Service (Python/FastAPI)
- Async Notification Service (Node.js, AWS SQS)
- Database (Amazon Aurora PostgreSQL)
- Caching Layer (Amazon ElastiCache (Redis))
- External Systems: Payment Gateway, Third-Party Shipping APIs, Identity Provider, Tax Calculation Service

## Relationships
- Storefront SPA -> API Gateway [HTTPS/REST]
- API Gateway -> Order & Checkout Service [HTTPS/REST]
- Order & Checkout Service -> Database [PostgreSQL Protocol over TLS]
- Order & Checkout Service -> Async Notification Service [AWS SQS]
- Order & Checkout Service -> Payment Gateway [Outbound HTTPS/REST with mTLS and HMAC]
- Order & Checkout Service -> Third-Party Shipping APIs [Outbound HTTPS/REST with mTLS and HMAC]

## Technology Stack
- Node.js/Express & TypeScript for the Order & Checkout Service backend logic
- Amazon Aurora PostgreSQL with multi-AZ for transactional data storage
- Amazon ElastiCache (Redis) for low-latency session and cart management
- AWS ECS (Fargate) for container orchestration and scaling
- AWS SQS with Dead-Letter Queues for asynchronous messaging

## Rationale
This architecture ensures 99.95% availability and sub-2-second performance for 1 million monthly active users by decoupling services and utilizing regional AWS infrastructure. Security and compliance mandates are strictly met via client-side payment tokenization and OAuth2/OIDC authentication.