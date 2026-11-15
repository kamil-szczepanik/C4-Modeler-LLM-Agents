## Overview
The Online Bookstore is a cloud-native e-commerce platform providing catalog browsing, secure multi-currency checkout, recommendations, and reviews. It ensures high scalability, OWASP top-10 security, and GDPR/CCPA compliance across global regions.

## Key Elements
- Book Buyer (Customer), Registered Reviewer, Store Administrator
- Storefront SPA (React on AWS S3 & CloudFront)
- API Gateway (AWS API Gateway)
- Catalog & Search Service (Go/Gin, Elasticsearch)
- Order & Checkout Service (Node.js/Express)
- Recommendation & Review Service (Python/FastAPI)
- Async Notification Service (Node.js, AWS SQS)
- Database (Amazon Aurora PostgreSQL with multi-AZ and read replicas)
- Caching Layer (Amazon ElastiCache (Redis))
- External Systems: Payment Gateway, Third-Party Shipping APIs, Identity Provider, Notification Provider, Tax Calculation Service, AWS CloudFront

## Relationships
- Storefront SPA -> API Gateway (HTTPS)
- API Gateway -> Catalog & Search Service, Order & Checkout Service, Recommendation & Review Service (HTTPS/REST)
- Order & Checkout Service -> Async Notification Service (AWS SQS)
- Catalog & Search Service, Order & Checkout Service, Recommendation & Review Service, Async Notification Service -> Database (PostgreSQL Protocol over TLS)
- Catalog & Search Service -> Caching Layer (Redis Protocol)
- Storefront SPA -> Payment Gateway, Third-Party Shipping APIs, Notification Provider, Tax Calculation Service (Outbound HTTPS/REST with mTLS and HMAC)
- Storefront SPA -> Identity Provider (OAuth2/OIDC with JWT scopes)

## Technology Stack
- AWS Cloud & Multi-Region Support: Chosen for 99.95% availability (R-07) across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.
- Go/Gin & Elasticsearch: High-performance catalog searching and low latency.
- Node.js/Express & Python/FastAPI: Rapid development for business services and recommendation processing.
- Amazon Aurora PostgreSQL: Scalable relational database with multi-AZ and read replicas.
- Amazon ElastiCache (Redis): In-memory caching layer to maintain page load times under 2s on 3G.
- AWS SQS & Node.js: Asynchronous messaging for reliable, decoupled transactional notifications.

## Rationale
This architecture uses decoupled microservices and managed cloud services to handle 1M MAU without performance degradation. It integrates robust security controls, caching, and multi-region deployment to meet strict compliance and availability targets.