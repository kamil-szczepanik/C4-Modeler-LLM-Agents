## Overview
- Cloud-native online bookstore platform designed to provide catalog browsing, secure multi-currency checkout, recommendations, and reviews.
- Built to handle 1M MAU globally with high availability and GDPR/CCPA compliance.

## Key Elements
- Book Buyer (Customer) [person, context]
- Registered Reviewer [person, context]
- Store Administrator [person, context]
- Storefront SPA [container, SPA]
- API Gateway [container, API Gateway]
- Catalog & Search Service [container, Microservice]
- Order & Checkout Service [container, Microservice]
- Recommendation & Review Service [container, Microservice]
- Async Notification Service [container, Microservice]
- Database [container, Database]
- Caching Layer [container, Cache]
- External Systems: Payment Gateway, Third-Party Shipping APIs, Identity Provider, Notification Provider, Tax Calculation Service, AWS CloudFront

## Relationships
- Book Buyer, Registered Reviewer, Store Administrator -> Online Bookstore (HTTPS)
- Online Bookstore -> AWS CloudFront (CDN)
- API Gateway -> Catalog & Search Service (HTTPS/REST)
- API Gateway -> Order & Checkout Service (HTTPS/REST)
- API Gateway -> Recommendation & Review Service (HTTPS/REST)
- Order & Checkout Service -> Async Notification Service (AWS SQS)
- All Microservices -> Database (PostgreSQL Protocol over TLS)
- Catalog & Search Service -> Caching Layer (Redis Protocol)
- Online Bookstore -> Payment Gateway, Third-Party Shipping APIs, Notification Provider, Tax Calculation Service (Outbound HTTPS/REST with mTLS and HMAC)
- Online Bookstore -> Identity Provider (OAuth2/OIDC with JWT scopes)

## Technology Stack
- Frontend: React hosted on AWS S3 & CloudFront
- Compute & Orchestration: Amazon ECS with AWS Fargate across `us-east-1`, `eu-west-1`, `ap-southeast-1`
- Microservices: Node.js/Express, Go/Gin, Python/FastAPI
- Search & Database: Elasticsearch, Amazon Aurora PostgreSQL with multi-AZ and read replicas
- Caching & Queuing: Amazon ElastiCache (Redis), AWS SQS
- Security & Infrastructure: AWS API Gateway, AWS KMS, AWS Secrets Manager, mTLS via ECS service mesh

## Rationale
- Microservices isolation decouples synchronous checkout from external I/O delays and recommendations, ensuring sub-2-second page loads and high availability.
- Multi-region AWS Fargate deployment with regional Aurora read replicas guarantees GDPR/CCPA data locality and low-latency scaling for 1M MAU.