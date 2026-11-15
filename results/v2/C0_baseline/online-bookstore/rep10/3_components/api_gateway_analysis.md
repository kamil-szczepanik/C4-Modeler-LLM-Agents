## Overview
The Online Bookstore is a scaled-down e-commerce platform for purchasing physical and electronic books with recommendations and reviews. The system uses a multi-region cloud architecture to handle high concurrency, secure transactions, and global compliance.

## Key Elements
- Customers (Shoppers), Book Authors/Publishers, Store Administrators
- Edge Routing & CDN Layer (Amazon Route 53, Amazon CloudFront, AWS WAF)
- Single Page Application (SPA) (React, TypeScript, Amazon S3)
- API Gateway (AWS API Gateway)
- Backend Services (Catalog & Search, Checkout & Order, Recommendation Service on Amazon ECS Fargate, AWS Lambda)
- Data Stores (Amazon Aurora PostgreSQL, Amazon DynamoDB, AWS KMS)
- Third-Party Integrations (Payment Gateway, Shipping API, Tax & Compliance Service)

## Relationships
- Single Page Application (SPA) -> API Gateway: HTTPS/REST (JSON)
- API Gateway -> Catalog & Search Container: HTTPS/REST with mTLS
- API Gateway -> Checkout & Order Container: HTTPS/REST with mTLS
- API Gateway -> Recommendation Service: gRPC with mTLS
- API Gateway -> Third-Party APIs: HTTPS/REST via AWS SQS and Lambda

## Technology Stack
- AWS API Gateway: Single secure entry point with integrated AWS WAF, JWT validation, and request schema validation.
- Amazon ECS Fargate: Serverless container orchestration for microservices, ensuring scalability.
- Amazon Aurora PostgreSQL & DynamoDB: Relational and NoSQL persistence for multi-currency transactions and high-speed catalog lookups.
- AWS Secrets Manager & KMS: Dynamic rotation of OAuth/JWT keys and comprehensive data encryption.
- Amazon Route 53 & CloudFront: Global latency-based DNS routing and edge content delivery.

## Rationale
This architecture ensures 99.95% availability and sub-2-second performance for 1M MAU through edge caching, regional endpoints, and stateless containerization. Strict security controls, mTLS, and AWS WAF provide robust GDPR/CCPA compliance and OWASP Top-10 mitigation.