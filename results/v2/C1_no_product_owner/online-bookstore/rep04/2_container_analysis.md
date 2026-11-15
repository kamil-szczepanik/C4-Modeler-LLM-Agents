## Overview
- Scaled-down Amazon-style e-commerce site for books, supporting 1M MAU across three global AWS regions.
- Delivers secure catalog browsing, shopping cart/checkout, recommendations, reviews, and third-party shipping integrations while meeting GDPR/CCPA and 99.95% uptime SLAs.

## Key Elements
- Customers (Browsing via HTTPS)
- Amazon CloudFront & AWS S3 (SPA hosting CDN)
- AWS API Gateway (Entry point & WAF)
- Core E-Commerce Service (Node.js/TypeScript on AWS ECS Fargate)
- Recommendation & Search Service (Python/FastAPI on ECS with Amazon OpenSearch)
- Background Worker Service (Node.js/TypeScript on ECS for async tasks)
- Amazon Aurora PostgreSQL Global Database & Amazon ElastiCache Redis
- Amazon SQS / SNS (Asynchronous messaging & DLQs)
- Identity Provider, AWS Secrets Manager, & AWS KMS

## Relationships
- Customer to SPA: HTTPS
- SPA to API Gateway: HTTPS/REST with JWT validation
- API Gateway to Core E-Commerce & Recommendation Services: gRPC over internal VPC
- Core E-Commerce Service to Amazon SQS / SNS: TLS / IAM authenticated messaging
- Services to Aurora, Redis, & OpenSearch: mTLS with IAM least-privilege roles

## Technology Stack
- React/TypeScript SPA: Fast client-side rendering for <2s page load SLA
- Node.js & Python (FastAPI): Lightweight, high-performance containerized microservices
- Amazon ECS (Fargate): Serverless container orchestration reducing operational overhead
- Amazon Aurora PostgreSQL (Global): Multi-region transactional integrity and low-latency failover
- Amazon ElastiCache (Redis): In-memory session and cart state management
- Amazon SQS/SNS: Decoupled asynchronous processing for third-party shipping and payments

## Rationale
- Containerized microservices on AWS ECS Fargate with multi-region Aurora Global Databases ensure high availability (99.95% uptime) and scalable performance for 1M MAU.
- Asynchronous SQS messaging and strict mTLS/IAM security controls mitigate third-party dependencies while satisfying stringent GDPR/CCPA and OWASP compliance requirements.