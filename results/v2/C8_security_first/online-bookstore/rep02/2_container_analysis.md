## Overview
An Amazon-style online bookstore providing catalogue browsing, secure checkout, 5-star reviews, and recommendations. The system is architected as a globally distributed, highly available e-commerce platform deployed on AWS.

## Key Elements
- Shoppers / Customers and Book Publishers / Administrators
- React Single Page Application (SPA) hosted in Amazon S3 and CloudFront
- AWS API Gateway & Edge Lambda
- Catalog & Search Service (Node.js/Express)
- Order & Checkout Service (Java/Spring Boot)
- Recommendation Service (Python/FastAPI)
- Amazon Aurora PostgreSQL, Redis, and Elasticsearch
- External Payment Gateway and Third-Party Shipping APIs

## Relationships
- Shoppers to CloudFront/S3 SPA via HTTPS
- SPA to AWS API Gateway via HTTPS/JSON
- API Gateway to Backend Containers via gRPC over mTLS with JWT claims in metadata
- Order & Checkout Service to Amazon Aurora PostgreSQL and Redis via TCP/TLS
- Catalog & Search Service to Elasticsearch via TCP/TLS
- System to External Payment Gateway and Third-Party Shipping APIs via HTTPS

## Technology Stack
- **Frontend:** React hosted in Amazon S3 + CloudFront CDN for global sub-2-second page loads.
- **Backend:** Node.js/Express (Catalog), Java/Spring Boot (Checkout), and Python/FastAPI (Recommendations) for containerized microservices.
- **Data & Caching:** Amazon Aurora PostgreSQL (multi-region with PII isolation) and Redis (multi-AZ cart cache).
- **Search & Infrastructure:** Elasticsearch, AWS API Gateway, AWS ECS Fargate, Terraform, and AWS KMS (AES-256).
- **Protocols:** HTTPS/JSON externally; gRPC over mTLS internally.

## Rationale
This multi-region AWS container architecture guarantees 99.95% uptime and scales smoothly to 1M MAU using ECS Fargate, HPA, and multi-AZ database replication. Strict data isolation, encryption, and OAuth 2.0/JWT controls ensure robust GDPR and CCPA compliance.