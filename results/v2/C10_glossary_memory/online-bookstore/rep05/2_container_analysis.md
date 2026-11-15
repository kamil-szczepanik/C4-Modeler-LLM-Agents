## Overview
[An AWS-hosted global online bookstore handling 1 million monthly active users with multi-currency support and secure e-commerce operations, providing catalogue browsing, secure checkout, reviews, and personalized book recommendations.]
[The system employs isolated microservices deployed across multiple regions to ensure high availability, scalability, and strict compliance with security standards.]

## Key Elements
- Customers / Shoppers [person, context]
- Registered Users / Reviewers [person, context]
- Store Administrators [person, context]
- Online Bookstore System [softwareSystem, context]
- Payment Gateway [externalSystem, context]
- Third-Party Shipping APIs [externalSystem, context]
- Identity Provider [externalSystem, context]
- Analytics & Monitoring Platform [externalSystem, context]
- Single-Page Application (SPA) [container, React, TypeScript, Vite]
- API Gateway / Backend-for-Frontend (BFF) [container, AWS API Gateway / NestJS on AWS ECS Fargate]
- Catalog & Search Service [container, Node.js / Java, AWS OpenSearch]
- Order & Checkout Service [container, Spring Boot / Go]
- Recommendation & Review Service [container, Python / FastAPI, AWS DynamoDB / ElastiCache]

## Relationships
- Customers / Shoppers -> Online Bookstore System via HTTPS (TLS 1.3) via global CDN/WAF and Route 53
- Registered Users / Reviewers -> Online Bookstore System via HTTPS (TLS 1.3)
- Store Administrators -> Online Bookstore System via HTTPS (TLS 1.3)
- Online Bookstore System -> Payment Gateway via HTTPS/REST using tokenized iframe SDKs
- Online Bookstore System -> Third-Party Shipping APIs via HTTPS/REST with circuit breakers and fallback caching
- Online Bookstore System -> Identity Provider via OAuth2/OIDC with short-lived JWTs
- Online Bookstore System -> Analytics & Monitoring Platform via HTTPS
- SPA -> API Gateway / BFF via HTTPS/REST and GraphQL
- API Gateway / BFF -> Backend Services via internal gRPC over AWS Cloud Map / ECS Service Connect with mTLS

## Technology Stack
- React, TypeScript, Vite: Delivers sub-2s page loads on 3G for the SPA hosted globally on AWS CloudFront/S3.
- AWS API Gateway / NestJS on ECS Fargate: Handles request routing, rate limiting, and TLS termination.
- Node.js / Java with AWS OpenSearch: Isolates keyword searches for scalable catalogue browsing.
- Spring Boot / Go with Amazon Aurora PostgreSQL: Ensures ACID-compliant transactions for carts and orders across multiple regions.
- Python / FastAPI with Amazon DynamoDB: Isolates heavy analytical recommendation and review queries from checkout.
- AWS ECS Fargate & App Mesh: Provides Blue/Green deployments, auto-scaling, and internal mTLS service-to-service communication.

## Rationale
[This microservices architecture isolates high-load recommendation queries from critical transactional paths to protect core browsing and checkout performance for 1 million monthly active users.]
[Regional AWS deployment strategies, multi-AZ databases, and aggressive circuit breaking collectively guarantee 99.95% uptime and sub-2-second page load requirements.]