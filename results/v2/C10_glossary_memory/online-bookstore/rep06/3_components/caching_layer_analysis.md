## Overview
• The Online Bookstore is a cloud-native e-commerce platform providing catalog browsing, secure multi-currency checkout, recommendations, and reviews for physical and electronic books.
• The system is designed to handle 1 million monthly active users globally while ensuring high availability, sub-second performance, and strict GDPR and CCPA compliance.

## Key Elements
• Book Buyer (Customer) [person]
• Registered Reviewer [person]
• Store Administrator [person]
• Storefront SPA [container] (React hosted on AWS S3 & CloudFront)
• API Gateway [container] (AWS API Gateway)
• Catalog & Search Service [container] (Go/Gin, Elasticsearch)
• Order & Checkout Service [container] (Node.js/Express)
• Recommendation & Review Service [container] (Python/FastAPI)
• Async Notification Service [container] (Node.js, AWS SQS)
• Database [container] (Amazon Aurora PostgreSQL with multi-AZ and read replicas)
• Caching Layer [container] (Amazon ElastiCache (Redis) with Catalog Cache, Session Store, and Recommendation Cache components)
• Payment Gateway [externalSystem] (Stripe/PayPal)
• Third-Party Shipping APIs [externalSystem] (FedEx/UPS)
• Identity Provider [externalSystem] (Auth0/AWS Cognito)
• Notification Provider [externalSystem] (SendGrid/Twilio)
• Tax Calculation Service [externalSystem] (Avalara)

## Relationships
• Book Buyer (Customer), Registered Reviewer, Store Administrator -> Storefront SPA (HTTPS)
• Storefront SPA -> AWS CloudFront (CDN)
• Storefront SPA -> API Gateway (HTTPS)
• API Gateway -> Catalog & Search Service, Order & Checkout Service, Recommendation & Review Service (HTTPS/REST)
• Order & Checkout Service -> Async Notification Service (AWS SQS)
• Catalog & Search Service, Order & Checkout Service, Recommendation & Review Service, Async Notification Service -> Database (PostgreSQL Protocol over TLS)
• Catalog & Search Service -> Caching Layer Catalog Cache Component (Redis Protocol over TLS 1.3)
• Order & Checkout Service -> Caching Layer Session Store Component (Redis Protocol over TLS 1.3)
• Recommendation & Review Service -> Caching Layer Recommendation Cache Component (Redis Protocol over TLS 1.3)
• Storefront SPA -> Payment Gateway, Third-Party Shipping APIs, Notification Provider, Tax Calculation Service (Outbound HTTPS/REST with mTLS and HMAC)
• Storefront SPA -> Identity Provider (OAuth2/OIDC with JWT scopes)

## Technology Stack
• React hosted on AWS S3 & CloudFront: Delivers high-performance global frontend content caching.
• Go/Gin and Elasticsearch: Provides high-throughput catalog browsing and keyword search.
• Node.js/Express and Python/FastAPI: Powers scalable backend microservices for orders and recommendations.
• Amazon Aurora PostgreSQL: Ensures scalable relational data storage with multi-AZ and read replicas.
• Amazon ElastiCache (Redis): Accelerates search, shopping cart sessions, and recommendations with in-memory caching.
• AWS SQS: Enables reliable asynchronous notifications.

## Rationale
• This architecture uses managed AWS services and decoupled microservices to achieve high availability and handle 1 million monthly active users without performance degradation.
• Strict adherence to encryption standards, private VPC isolation, and tokenization ensures robust security and compliance with GDPR and CCPA regulations.