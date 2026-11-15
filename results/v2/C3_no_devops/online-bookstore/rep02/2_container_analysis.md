## Overview
[An Amazon-style e-commerce site for physical and electronic books with recommendations and reviews, designed for global scale, strict compliance, and high availability.]

## Key Elements
- Users: Book Buyer & Reviewer, Store Administrator, Marketing/Merchandising Specialist
- External Systems: External Payment Gateway, Third-Party Shipping Provider API, External Recommendation Service
- Containers: Single-Page Application (SPA), Admin / Back-Office App, Amazon API Gateway, Core E-Commerce API (Node.js/NestJS), Recommendation Service (Python/FastAPI), Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis)
- Infrastructure: AWS S3, CloudFront, ECS Fargate, Amazon EventBridge, Amazon SQS, AWS Secrets Manager, AWS KMS

## Relationships
- SPA & Admin App -> HTTPS -> Amazon API Gateway (REST/GraphQL)
- API Gateway -> mTLS -> Core E-Commerce API & Recommendation Service
- Core E-Commerce API -> TLS over TCP -> Amazon Aurora PostgreSQL & ElastiCache
- Core E-Commerce API -> gRPC -> Recommendation Service
- Core E-Commerce API -> Amazon SQS -> Third-Party Shipping Provider API
- Admin App -> Amazon EventBridge -> Core API & Recommendation Service

## Technology Stack
- Frontend: React / TypeScript on AWS S3 & CloudFront for <2s page load performance
- Core Backend: Node.js (NestJS) on AWS ECS (Fargate) for scalable e-commerce logic
- Recommendation Engine: Python (FastAPI) on AWS ECS (Fargate)
- Database & Caching: Amazon Aurora PostgreSQL (Multi-AZ) and Amazon ElastiCache (Redis)
- Messaging & Integration: Amazon EventBridge and Amazon SQS
- Security: AWS KMS, AWS Secrets Manager, OAuth2/OIDC, JWT, mTLS

## Rationale
- Decouples revenue-generating storefront operations from administrative and analytical workloads to protect checkout availability and performance.
- Utilizes asynchronous event-driven patterns via SQS and EventBridge to ensure resilience against third-party shipping API degradation.