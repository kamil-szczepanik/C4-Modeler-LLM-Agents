## Overview
An AWS-based e-commerce platform providing catalog browsing, secure checkout, reviews, and personalized recommendations for 1M MAU. It features multi-region deployment, multi-currency support, and strict GDPR/CCPA compliance.

## Key Elements
- **Users:** Shoppers, Vendors, Admins
- **Edge & Gateway:** AWS CloudFront, AWS WAF, AWS Shield Advanced, Amazon API Gateway, AWS ALB, AWS App Mesh (Envoy)
- **Edge Compute:** AWS Lambda@Edge (Localization Service)
- **Core Microservices:** Catalogue, Checkout & Cart, Recommendation, Vendor Portal, Review & Rating (running on AWS ECS Fargate)
- **Data & Messaging:** PostgreSQL, Amazon OpenSearch, Amazon DynamoDB, Amazon SQS, Redis
- **External Systems:** Payment Gateway, Third-Party Shipping APIs, Notification Service

## Relationships
- Shoppers/Vendors/Admins -> AWS CloudFront / AWS WAF: Sends HTTPS requests [TLS 1.3]
- AWS API Gateway -> ECS Fargate Microservices: Routes requests with context headers [gRPC over mTLS]
- Checkout & Cart Microservice -> Payment Gateway & Shipping APIs: Processes transactions and fulfillment [HTTPS / REST]
- Microservices -> PostgreSQL / DynamoDB / OpenSearch / Redis: Reads and writes domain data [TCP / Internal Protocols]

## Technology Stack
- **Cloud Provider:** AWS across `us-east-1`, `eu-west-1`, `ap-southeast-1` for low-latency global reach.
- **API & Security:** Amazon API Gateway, AWS WAF, AWS Shield Advanced, and Envoy service mesh for robust edge routing, zero-trust mTLS, and OWASP protections.
- **Compute:** AWS ECS Fargate for scalable, serverless container orchestration of microservices.
- **Data Stores:** PostgreSQL for transactional data, DynamoDB for reviews, OpenSearch for catalog search, and Redis for fast recommendations.
- **Observability & Deployment:** AWS CloudWatch, AWS X-Ray, and AWS CloudFormation/CDK with canary deployments for 99.95% uptime.

## Rationale
The architecture combines global edge distribution with elastic container scaling to easily handle 1M MAU while maintaining sub-2-second page loads. Strict mTLS, JWT validation, and multi-region failover guarantee 99.95% availability, security, and GDPR/CCPA compliance.