## Overview
An online bookstore offering browsing, secure checkout, reviews, and recommendations. It implements a resilient multi-region cloud architecture to serve a global customer base.

## Key Elements
- Customers & Store Administrators (People)
- Single Page Application (Container: React, TypeScript, Amazon CloudFront, Amazon S3)
- API Gateway (Container: Amazon API Gateway)
- Backend Microservices (Containers: Catalog, Checkout, Recommendation, and User Privacy Services on AWS ECS Fargate)
- Data Stores & Messaging (Containers: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon SQS)
- External Systems (Payment Gateway, Shipping Provider, Identity Provider)

## Relationships
- Single Page Application -> API Gateway: Sends client API requests [HTTPS/TLS 1.3]
- API Gateway -> Backend ECS Fargate Services: Routes sanitized requests [mTLS and AWS IAM]
- API Gateway -> Identity Provider (IdP): Validates authentication tokens [HTTPS / OIDC / OAuth 2.0]
- API Gateway -> Amazon S3 & Athena: Streams anonymized access logs for analytics [HTTPS]

## Technology Stack
- Amazon API Gateway: Manages entry routing, rate limiting, and JWT token validation.
- AWS WAF: Mitigates DDoS attacks and bot scraping to protect uptime.
- AWS Lambda Authorizers: Performs custom token exchange and claims enrichment.
- AWS Route 53: Provides multi-region geoproximity routing and DNS failover.
- AWS X-Ray: Enables distributed tracing across microservices.

## Rationale
This architecture ensures 99.95% availability and high scalability for 1M MAU via distributed multi-region routing and serverless edge controls. Security and compliance (GDPR/CCPA, OWASP Top-10) are enforced directly at the gateway through PII masking, WAF protection, and strict TLS 1.3 encryption.