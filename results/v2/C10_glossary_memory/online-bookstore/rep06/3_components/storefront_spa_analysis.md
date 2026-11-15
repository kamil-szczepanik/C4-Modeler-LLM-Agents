## Overview
The Online Bookstore is a cloud-native e-commerce platform providing catalog browsing, secure multi-currency checkout, recommendations, and reviews. It is built to serve 1 million monthly active users with high availability and stringent compliance on AWS.

## Key Elements
- Book Buyer (Customer), Registered Reviewer, Store Administrator
- Storefront SPA (React hosted on AWS S3 & CloudFront)
- API Gateway (AWS API Gateway)
- Catalog & Search Service (Go/Gin, Elasticsearch)
- Order & Checkout Service (Node.js/Express)
- Recommendation & Review Service (Python/FastAPI)
- Async Notification Service (Node.js, AWS SQS)
- Database (Amazon Aurora PostgreSQL with multi-AZ and read replicas)
- Caching Layer (Amazon ElastiCache (Redis))
- External Systems: Payment Gateway, Third-Party Shipping APIs, Identity Provider, Notification Provider, Tax Calculation Service, AWS CloudFront

## Relationships
- Book Buyer (Customer), Registered Reviewer, Store Administrator -> Storefront SPA (HTTPS)
- Storefront SPA -> AWS CloudFront (CDN)
- Storefront SPA -> API Gateway (HTTPS)
- API Gateway -> Catalog & Search Service, Order & Checkout Service, Recommendation & Review Service (HTTPS/REST)
- Order & Checkout Service -> Async Notification Service (AWS SQS)
- Catalog & Search Service, Order & Checkout Service, Recommendation & Review Service, Async Notification Service -> Database (PostgreSQL Protocol over TLS)
- Catalog & Search Service -> Caching Layer (Redis Protocol)
- API Gateway -> Payment Gateway, Third-Party Shipping APIs, Notification Provider, Tax Calculation Service (Outbound HTTPS/REST with mTLS and HMAC)
- API Gateway -> Identity Provider (OAuth2/OIDC with JWT scopes)

## Technology Stack
- React: Frontend SPA framework for responsive user interfaces
- AWS S3 & CloudFront: Immutable asset storage and global CDN delivery
- Go/Gin & Elasticsearch: High-performance catalog browsing and search
- Node.js/Express: Scalable order processing and secure checkout handling
- Python/FastAPI: Rapid development of recommendation and review features
- Amazon Aurora PostgreSQL: Multi-AZ relational database with read replicas
- Amazon ElastiCache (Redis): In-memory caching for low-latency performance
- AWS API Gateway: Centralized secure entry point for all backend services

## Rationale
The serverless edge delivery combined with containerized backend microservices ensures high scalability and sub-2-second performance. Routing all external transactions exclusively through the API Gateway isolates sensitive credentials and enforces strict compliance requirements.