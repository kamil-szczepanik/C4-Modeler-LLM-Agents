## Overview
- Global online bookstore system handling 1 million monthly active users with multi-currency support and secure e-commerce operations.
- Provides catalogue browsing, secure checkout, reviews, and personalized book recommendations.

## Key Elements
- Customers / Shoppers
- Registered Users / Reviewers
- Store Administrators
- Payment Gateway
- Third-Party Shipping APIs
- Identity Provider
- Analytics & Monitoring Platform
- Single-Page Application (SPA)
- API Gateway / Backend-for-Frontend (BFF)
- Catalog & Search Service
- Order & Checkout Service
- Recommendation & Review Service

## Relationships
- Customers / Shoppers -> Single-Page Application (SPA) via HTTPS (TLS 1.3) through global CDN/WAF and Route 53
- Single-Page Application (SPA) -> API Gateway / Backend-for-Frontend (BFF) via HTTPS/REST and GraphQL
- API Gateway / Backend-for-Frontend (BFF) -> Catalog & Search Service via internal gRPC over AWS Cloud Map / ECS Service Connect with mTLS
- API Gateway / Backend-for-Frontend (BFF) -> Order & Checkout Service via internal gRPC over AWS Cloud Map / ECS Service Connect with mTLS
- API Gateway / Backend-for-Frontend (BFF) -> Recommendation & Review Service via internal gRPC over AWS Cloud Map / ECS Service Connect with mTLS
- Online Bookstore System -> Payment Gateway via HTTPS/REST using tokenized iframe SDKs
- Online Bookstore System -> Third-Party Shipping APIs via HTTPS/REST with circuit breakers and fallback caching
- Online Bookstore System -> Identity Provider via OAuth2/OIDC with short-lived JWTs

## Technology Stack
- React, TypeScript, Vite for global SPA delivery on AWS CloudFront/S3
- AWS API Gateway / NestJS on AWS ECS Fargate for BFF request routing and rate limiting
- Node.js / Java with AWS OpenSearch for isolated, scalable catalogue search
- Spring Boot / Go for ACID-compliant Order & Checkout transactions
- Python / FastAPI with AWS DynamoDB / ElastiCache for recommendations and reviews
- Amazon MSK (Kafka) for asynchronous change-data-capture ingestion

## Rationale
- Microservices architecture on AWS ECS Fargate isolates search, checkout, and recommendation domains to independently scale for 1M MAU.
- Multi-region deployment across us-east-1, eu-west-1, and ap-southeast-1 guarantees 99.95% uptime and sub-2s page loads.