## Overview
[The system is a scalable global e-commerce online bookstore serving 1M MAU with multi-currency support, secure checkout, and personalized recommendations. The architecture leverages AWS managed services and microservices to ensure high availability, low latency, and strict GDPR/CCPA compliance.]

## Key Elements
*   **Users:** Book Buyer & Reviewer, Store Administrator
*   **Clients:** Single-Page Application (SPA) (React / TypeScript on AWS S3 & CloudFront), Admin / Back-Office App
*   **Gateway Layer:** Amazon API Gateway
*   **API Gateway Components:** WAF Integration Component, Edge Router & SSL Terminating Proxy, Authorizer Component, Throttling & Rate Limiter, API Router & Transformer, Analytics & Metrics Component
*   **Backend Services:** Core E-Commerce API (Node.js/NestJS on AWS ECS Fargate), Recommendation Service (Python/FastAPI on AWS ECS Fargate)
*   **Data & Messaging:** Amazon Aurora PostgreSQL (Multi-AZ), Amazon ElastiCache (Redis), Amazon EventBridge, Amazon SQS
*   **External Systems:** External Payment Gateway, Third-Party Shipping Provider API, External Recommendation Service

## Relationships
*   Single-Page Application -> Amazon API Gateway: Makes API requests via HTTPS (REST/GraphQL)
*   Admin App -> Amazon API Gateway: Makes administrative API requests via HTTPS (REST/GraphQL)
*   AWS WAF -> Edge Router: Inspects and forwards clean traffic via HTTPS
*   API Router & Transformer -> Core E-Commerce API: Routes validated requests via mTLS over VPC Links
*   API Router & Transformer -> Recommendation Service: Routes recommendation requests via mTLS over VPC Links

## Technology Stack
*   **API Gateway:** AWS API Gateway with Lambda Authorizers, Usage Plans, and VPC Links for secure routing and scalability.
*   **Security:** AWS WAF for edge protection against OWASP Top-10 threats; TLS 1.3 and mTLS for data-in-transit.
*   **Compute:** AWS ECS (Fargate) running Node.js (NestJS) and Python (FastAPI) for containerized microservices.
*   **Database & Cache:** Amazon Aurora PostgreSQL (Multi-AZ) for transactional data; Amazon ElastiCache (Redis) for performance caching.
*   **Messaging:** Amazon EventBridge and Amazon SQS for asynchronous event-driven communication.

## Rationale
[This architecture uses AWS managed services and a containerized microservices pattern to easily scale past 1M MAU while guaranteeing 99.95% uptime and sub-2-second page loads. Offloading edge security, rate limiting, and JWT validation to Amazon API Gateway and AWS WAF directly protects backend ECS workloads and satisfies strict GDPR/CCPA compliance.]