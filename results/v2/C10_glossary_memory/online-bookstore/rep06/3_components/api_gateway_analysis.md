## Overview
The Online Bookstore is a cloud-native, multi-region e-commerce platform designed to provide catalog browsing, secure multi-currency checkout, recommendations, and reviews for physical and electronic books. It handles 1 million MAU with 99.95% availability while ensuring GDPR and CCPA compliance.

## Key Elements
- Book Buyer (Customer), Registered Reviewer, Store Administrator
- Storefront SPA (React hosted on AWS S3 & CloudFront)
- API Gateway (AWS API Gateway) containing Edge Router & SSL Termination, Auth Validation Middleware, Throttling & Rate Limiting, and API Analytics & Monetization components
- Catalog & Search Service (Go/Gin, Elasticsearch)
- Order & Checkout Service (Node.js/Express)
- Recommendation & Review Service (Python/FastAPI)
- Async Notification Service (Node.js, AWS SQS)
- Database (Amazon Aurora PostgreSQL with multi-AZ and read replicas)
- Caching Layer (Amazon ElastiCache (Redis))
- External Systems: Payment Gateway (Stripe/PayPal), Third-Party Shipping APIs (FedEx/UPS), Identity Provider (Auth0/AWS Cognito), Notification Provider (SendGrid/Twilio), Tax Calculation Service (Avalara), AWS CloudFront

## Relationships
- Book Buyer (Customer), Registered Reviewer, Store Administrator -> Storefront SPA [HTTPS]
- Storefront SPA -> AWS CloudFront [CDN]
- Storefront SPA -> API Gateway [HTTPS]
- API Gateway -> Catalog & Search Service, Order & Checkout Service, Recommendation & Review Service [HTTPS/REST with mTLS]
- Auth Validation Middleware Component -> Identity Provider [HTTPS]
- Order & Checkout Service -> Async Notification Service [AWS SQS]
- Microservices -> Database [PostgreSQL Protocol over TLS]
- Catalog & Search Service -> Caching Layer [Redis Protocol]

## Technology Stack
- AWS API Gateway & AWS CloudFront: Global edge routing, TLS 1.3 termination, and canary deployments
- React on AWS S3 & CloudFront: High-performance frontend SPA delivery
- Go/Gin & Elasticsearch: High-throughput catalog browsing and search
- Node.js/Express: Secure order and checkout processing
- Python/FastAPI: Fast AI/ML recommendations and review management
- Amazon Aurora PostgreSQL: Scalable relational database with multi-AZ replication
- Amazon ElastiCache (Redis): Low-latency caching layer
- AWS Lambda & WAF: Edge token validation and OWASP Top-10 security mitigations

## Rationale
The serverless edge routing and containerized microservices architecture ensure independent scalability and high availability (99.95% uptime) across three AWS regions. Strict mTLS, JWT edge validation, and managed database replicas deliver enterprise-grade security and sub-2-second page loads globally.