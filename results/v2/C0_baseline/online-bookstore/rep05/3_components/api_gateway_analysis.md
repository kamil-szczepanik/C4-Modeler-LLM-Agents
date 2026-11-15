## Overview
The Online Bookstore system is a scaled-down Amazon-style e-commerce platform providing catalog browsing, secure checkout, reviews, and recommendations. It delivers a high-performance, GDPR/CCPA-compliant shopping experience across global multi-currency markets.

## Key Elements
- **Customers (Shoppers) & Store Administrators**: Primary end-users accessing the system.
- **Single-Page Application (SPA) & Admin Back-Office**: React-based frontend clients hosted on Amazon S3 and CloudFront.
- **API Gateway (Amazon API Gateway)**: Single entry point handling routing, auth, caching, and WAF protection.
- **Core Services & Recommendation Engine**: Business logic containers running on Amazon ECS (Fargate).
- **Databases & Messaging**: Amazon Aurora PostgreSQL (Multi-AZ), Amazon DynamoDB, Amazon S3, Amazon EventBridge, and Amazon SQS.
- **External Systems**: Payment Gateways, Shipping Providers, Tax Services, and Notification Services.

## Relationships
- Single-Page Application -> API Gateway: Sends API requests [HTTPS/JSON via Amazon CloudFront]
- Admin Back-Office App -> API Gateway: Sends administrative API requests [HTTPS/gRPC with mTLS]
- API Gateway -> Core Services: Routes backend requests [HTTPS/gRPC with mTLS via AWS Service Connect]
- API Gateway -> Recommendation Engine: Requests recommendations [HTTPS/gRPC with mTLS via AWS Service Connect]

## Technology Stack
- **API Gateway & Routing**: Amazon API Gateway Regional APIs with native response caching and API schema validation.
- **Compute & Orchestration**: Amazon ECS (Fargate) running Node.js/NestJS and Python/FastAPI services.
- **Database & Storage**: Amazon Aurora PostgreSQL (Multi-AZ) and Amazon DynamoDB for persistent data.
- **Security & Compliance**: AWS WAF with OWASP Top-10 rules, Amazon Cognito for JWT validation, and AWS Certificate Manager for mTLS.
- **Infrastructure & CDN**: AWS (us-east-1, eu-west-1, ap-southeast-1), Amazon Route 53, and Amazon S3.

## Rationale
This architecture uses serverless edge routing and containerized microservices on AWS to ensure sub-2-second page loads and 99.95% availability under high load. Regional redundancy, strict data governance controls, and caching natively fulfill the scalability, multi-currency, and regulatory requirements.