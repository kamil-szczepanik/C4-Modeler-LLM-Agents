## Overview
- An Amazon-style online bookstore providing catalog browsing, secure checkout, reviews, and recommendations for global customers.
- Built on a multi-region AWS cloud architecture designed for high scalability, strict security compliance, and 99.95% uptime.

## Key Elements
- **Users**: Customer, Store Administrator
- **External Systems**: External Payment Gateway, External Shipping Provider, External Identity Provider, External Notification Service
- **Containers**: Storefront, API Gateway, Catalog & Search Service, Order & Checkout Service, Recommendation Service, Customer Privacy Service, Pricing & Currency Service
- **API Gateway Components**: Routing & Proxy Component, Authentication & Authorization Component, Rate Limiting & Throttling Component, Transformation & Error Handling Component

## Relationships
- Storefront -> API Gateway: Communicates via HTTPS/REST [HTTPS/REST]
- API Gateway -> Catalog & Search Service: Routes search requests via mTLS [mTLS]
- API Gateway -> Order & Checkout Service: Routes checkout requests via mTLS [mTLS]
- API Gateway -> Recommendation Service: Routes recommendation requests via mTLS [mTLS]
- API Gateway -> Customer Privacy Service: Routes privacy requests via mTLS [mTLS]
- API Gateway -> Pricing & Currency Service: Routes pricing requests via mTLS [mTLS]
- API Gateway -> External Identity Provider: Validates JWT tokens [HTTPS]

## Technology Stack
- **Frontend**: React SPA hosted on Amazon S3 and delivered via Amazon CloudFront CDN
- **API Gateway**: AWS API Gateway, AWS WAF, AWS Lambda, Amazon CloudWatch Synthetix
- **Microservices**: Node.js, Spring Boot, Python FastAPI, Go
- **Databases & Caching**: Amazon OpenSearch, Amazon DynamoDB, Redis cache
- **Infrastructure & Routing**: AWS Route 53, Terraform / AWS CloudFormation, AWS Secrets Manager, AWS X-Ray

## Rationale
- The multi-region serverless and containerized microservices architecture ensures sub-2-second page loads and 99.95% availability for 1 million MAUs.
- Integrated rate limiting, WAF, JWT validation, and automated secrets management fulfill stringent GDPR/CCPA compliance and OWASP Top-10 security requirements.