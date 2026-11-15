## Overview
The Online Bookstore is a globally distributed e-commerce platform built to handle 1M MAU with 99.95% uptime and sub-2-second page loads. It enables users to browse catalogues, securely purchase physical and electronic books in multiple currencies, manage shopping carts, and submit reviews.

## Key Elements
- **Users:** Shopper/Reviewer, Store Administrator, Third-Party Fulfillment Partner
- **External Systems:** Payment Gateway, Shipping Provider APIs, Recommendation Engine, Notification Service
- **Frontend Container:** Single Page Application (React / TypeScript) hosted on Amazon CloudFront and S3
- **API & Security:** AWS API Gateway, AWS WAF
- **Backend Containers (AWS ECS Fargate):** Catalogue Service, Shopping Cart & Checkout Service, Review Service, Localization & Currency Service
- **Databases & Caching:** Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis)

## Relationships
- **Shopper / Reviewer -> CloudFront / S3:** Accesses static assets via HTTPS
- **SPA -> API Gateway:** Communicates via HTTPS/REST
- **API Gateway -> ECS Fargate Services:** Routes internal traffic via gRPC with mTLS
- **Checkout Service -> Payment Gateway / Shipping Provider APIs:** Connects via HTTPS/REST through an AWS NAT Gateway
- **Services -> Databases / Cache:** Queries Amazon Aurora PostgreSQL, DynamoDB, and ElastiCache via internal VPC connections

## Technology Stack
- **Frontend:** React and TypeScript for a responsive client-side user experience
- **Compute:** AWS ECS Fargate for scalable, serverless container execution
- **Databases:** Amazon Aurora PostgreSQL for transactional checkout data and DynamoDB for low-latency catalogue/cart reads
- **Caching:** Amazon ElastiCache (Redis) for ultra-fast multi-currency exchange rate lookups
- **Network & Security:** Amazon CloudFront, AWS API Gateway, AWS WAF, and TLS 1.3/mTLS for secure routing

## Rationale
This multi-region active-active AWS architecture decouples high-traffic browsing from secure checkout to guarantee independent scalability and high availability. Regional data partitioning and strict VPC boundaries ensure robust GDPR/CCPA compliance and OWASP security mitigations without compromising global performance.