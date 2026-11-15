## Overview
An online bookstore providing catalog browsing, shopping carts, secure checkout, reviews, and recommendations for 1 million MAU globally. Built on AWS across `us-east-1`, `eu-west-1`, and `ap-southeast-1` to ensure high availability and sub-2-second performance.

## Key Elements
- Shopper / Reviewer & Store Administrator (Users)
- Single Page Application (React, TypeScript, Amazon CloudFront, Amazon S3)
- API Gateway & Security (AWS API Gateway, AWS WAF)
- Catalogue, Shopping Cart & Checkout, Review, and Localization & Currency Services (AWS ECS Fargate)
- Amazon Aurora PostgreSQL & Amazon DynamoDB (Databases)
- Amazon ElastiCache (Redis OSS v7.0+)
- External Payment Gateway, Shipping Provider APIs, Recommendation Engine, Notification Service

## Relationships
- Single Page Application -> API Gateway & Security: HTTPS / REST / WSS
- API Gateway & Security -> ECS Fargate Containers: Internal VPC routing / gRPC / HTTPS
- Localization & Currency Service -> Amazon ElastiCache: `GET`/`SET` commands over TCP/TLS [RESP]
- Amazon SNS -> Localization & Currency Service: Triggers local cache invalidation [AWS Internal Event Bus]

## Technology Stack
- **AWS ECS Fargate:** Serverless container execution for stateless microservices ensuring seamless horizontal scaling.
- **Amazon Aurora PostgreSQL:** Relational database for transactional data like user accounts, orders, and catalogue records.
- **Amazon DynamoDB:** NoSQL database optimized for low-latency shopping cart sessions and product reviews.
- **Amazon ElastiCache (Redis OSS v7.0+):** In-memory cache for ultra-fast multi-currency exchange rate lookups and ephemeral session tokens.
- **AWS API Gateway & WAF:** Edge security and request routing providing OWASP Top-10 mitigations.

## Rationale
The microservices architecture deployed across multiple AWS regions ensures high availability (99.95% uptime) and global performance. Integrating Amazon ElastiCache within a private VPC boundary optimizes multi-currency conversions and session handling while maintaining GDPR and CCPA compliance.