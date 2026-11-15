## Overview
The Online Bookstore is a cloud-native e-commerce platform providing catalog browsing, secure multi-currency checkout, recommendations, and reviews for physical and electronic books. It features a scalable, decoupled microservices architecture designed to support 1 million monthly active users with high availability.

## Key Elements
- Book Buyer (Customer), Registered Reviewer, Store Administrator
- Storefront SPA (React on AWS S3 & CloudFront)
- API Gateway (AWS API Gateway)
- Catalog & Search Service (Go/Gin, Elasticsearch)
- Order & Checkout Service (Node.js/Express)
- Recommendation & Review Service (Python/FastAPI)
- Async Notification Service (Node.js, AWS SQS)
- Database (Amazon Aurora PostgreSQL)
- Caching Layer (Amazon ElastiCache (Redis))

## Relationships
- Book Buyer -> Storefront SPA [HTTPS]
- Storefront SPA -> API Gateway [HTTPS]
- API Gateway -> Recommendation & Review Service [HTTPS/REST]
- Recommendation & Review Service -> Database [PostgreSQL Protocol over TLS]
- Recommendation & Review Service -> Caching Layer [Redis Protocol over TLS]
- Online Bookstore -> Payment Gateway [Outbound HTTPS/REST with mTLS/HMAC]

## Technology Stack
- AWS CloudFront & S3: Global content delivery and static frontend hosting for sub-second page loads.
- Python/FastAPI: High-performance asynchronous backend for recommendation and review processing.
- Amazon Aurora PostgreSQL: Scalable multi-AZ relational database with read replicas.
- Amazon ElastiCache (Redis): In-memory caching for low-latency recommendation delivery.
- AWS Fargate: Containerized serverless compute for isolating ML batch recommendation workloads.

## Rationale
This architecture uses decoupled microservices and managed AWS cloud services to ensure independent scalability under high traffic spikes. Caching layers and container isolation satisfy stringent performance and 99.95% availability targets while maintaining enterprise-grade security.