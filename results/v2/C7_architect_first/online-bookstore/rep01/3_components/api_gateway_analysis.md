## Overview
The Online Bookstore system is a scalable e-commerce platform built to support book browsing, secure checkout, reviews, and personalized recommendations for 1M MAU. It features a microservices architecture hosted on AWS across multiple global regions.

## Key Elements
- **Users**: Customer, Admin / Support Staff, Authors / Publishers
- **Containers**: Single Page Application (SPA), API Gateway, Catalog Service, Order Management & Payment Integration Containers, Recommendation Service
- **API Gateway Components**: Authentication & Authorization Filter, Scope & RBAC Enforcement Component, Request Transformation & Localization Component, Routing & Rate Limiting Component, Edge Observability & Telemetry Component
- **External Systems**: Payment Gateway, Shipping Provider API, Email / Notification Service

## Relationships
- **Single Page Application (SPA) -> Authentication & Authorization Filter**: Sends API requests [HTTPS / REST / JSON]
- **Authentication & Authorization Filter -> Scope & RBAC Enforcement Component**: Passes validated identity claims [Internal]
- **Scope & RBAC Enforcement Component -> Request Transformation & Localization Component**: Forwards authorized requests [Internal]
- **Request Transformation & Localization Component -> Routing & Rate Limiting Component**: Injects locale/currency and forwards requests [Internal]
- **Routing & Rate Limiting Component -> Edge Observability & Telemetry Component**: Offloads request metrics and logs [Internal]
- **Routing & Rate Limiting Component -> Catalog, Order, Recommendation Services**: Routes traffic [HTTPS / mTLS via AWS App Mesh]

## Technology Stack
- **Client**: React and TypeScript hosted on AWS S3 & CloudFront for high-performance content delivery
- **API Gateway**: AWS API Gateway combined with AWS WAF for perimeter security and OWASP Top-10 mitigations
- **Services**: Node.js (Express), Spring Boot (Java), Python (FastAPI) for backend microservices
- **Databases**: Amazon RDS (PostgreSQL) and Amazon DynamoDB for persistent storage
- **Infrastructure & Monitoring**: AWS SQS, AWS App Mesh, AWS Route 53, AWS X-Ray, and AWS CloudWatch Synthetics for multi-region operations

## Rationale
This architecture ensures 99.95% uptime, sub-2-second page loads, and 1M MAU scalability by offloading cross-cutting edge concerns to an API Gateway. It maintains strict GDPR/CCPA compliance and multi-currency support through dedicated perimeter components.