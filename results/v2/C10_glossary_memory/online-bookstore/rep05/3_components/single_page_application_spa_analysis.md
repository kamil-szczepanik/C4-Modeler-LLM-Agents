## Overview
- An AWS-hosted global online bookstore handling 1 million monthly active users with multi-currency support and secure e-commerce operations.
- Features catalogue browsing, secure checkout, reviews, and personalized book recommendations.

## Key Elements
- Customers / Shoppers, Registered Users / Reviewers, Store Administrators
- Single-Page Application (SPA) (React, TypeScript, Vite)
- API Gateway / Backend-for-Frontend (BFF) (AWS API Gateway / NestJS on AWS ECS Fargate)
- Catalog & Search Service (Node.js / Java, AWS OpenSearch)
- Order & Checkout Service (Spring Boot / Go)
- Recommendation & Review Service (Python / FastAPI, AWS DynamoDB / ElastiCache)
- External Systems: Payment Gateway, Third-Party Shipping APIs, Identity Provider, Analytics & Monitoring Platform

## Relationships
- Customers / Shoppers -> Single-Page Application (SPA): HTTPS (TLS 1.3) via global CDN/WAF and Route 53
- Registered Users / Reviewers -> Single-Page Application (SPA): HTTPS (TLS 1.3)
- Store Administrators -> Single-Page Application (SPA): HTTPS (TLS 1.3)
- Single-Page Application (SPA) -> API Gateway / Backend-for-Frontend (BFF): HTTPS/REST and GraphQL
- API Gateway / Backend-for-Frontend (BFF) -> Catalog & Search Service: internal gRPC over AWS Cloud Map / ECS Service Connect with mTLS
- API Gateway / Backend-for-Frontend (BFF) -> Order & Checkout Service: internal gRPC over AWS Cloud Map / ECS Service Connect with mTLS
- API Gateway / Backend-for-Frontend (BFF) -> Recommendation & Review Service: internal gRPC over AWS Cloud Map / ECS Service Connect with mTLS
- Order & Checkout Service -> Payment Gateway: HTTPS/REST using tokenized iframe SDKs
- Order & Checkout Service -> Third-Party Shipping APIs: HTTPS/REST with circuit breakers and fallback caching

## Technology Stack
- React, TypeScript, Vite: Delivers sub-2s page loads on 3G for the SPA hosted globally on AWS CloudFront/S3.
- AWS API Gateway / NestJS on AWS ECS Fargate: Handles request routing, rate limiting, and TLS termination for the BFF.
- Node.js / Java & AWS OpenSearch: Isolates keyword searches for scalable catalogue browsing.
- Spring Boot / Go: Ensures ACID-compliant transactions for carts and orders across multiple regions.
- Python / FastAPI & AWS DynamoDB / ElastiCache: Isolates heavy analytical recommendation and review queries from checkout.

## Rationale
- Microservices architecture on AWS ensures 99.95% uptime and horizontal scalability for 1M MAU across three global regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`).
- Strict decoupling of search, checkout, and recommendation services guarantees sub-2s performance on 3G networks and meets rigorous GDPR, CCPA, and OWASP security standards.