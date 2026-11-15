## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform providing catalog browsing, secure checkout, reviews, and personalized book recommendations. It is architected as a cloud-native, multi-region system deployed across AWS us-east-1, eu-west-1, and ap-southeast-1.

## Key Elements
- Users: Customers, Store Administrators
- External Systems: Payment Gateway, Shipping Provider APIs, Identity Provider, Tax Calculation Service, Notification Service
- Containers: Single-Page Application (SPA) (React/TypeScript), API Gateway (Amazon API Gateway), Catalog Service, Order & Checkout Service, Recommendation Service, Auth Service, Privacy Service, Background Worker (Node.js/Java/Python on ECS Fargate)
- Data Stores & Services: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon OpenSearch, Amazon S3, Amazon CloudFront, Amazon SNS/SQS
- API Gateway Components: SSL Termination (AWS Certificate Manager), Rate Limiting (AWS WAF), Authentication Interceptor (JWT/Lambda Authorizer), Request/Response Transformation, Routing & Dispatcher (AWS Cloud Map / HTTP Integrations), Request Logging & Audit Component (CloudWatch)

## Relationships
- SPA -> API Gateway: Sends client requests [HTTPS / JSON]
- API Gateway -> Backend Services (Catalog, Order, Recommendation, Auth, Privacy): Routes requests via service discovery [Internal gRPC / HTTP/2, AWS Cloud Map]
- API Gateway -> Amazon CloudWatch: Exports audit and metric data [AWS API / TLS]

## Technology Stack
- Amazon API Gateway: Manages entry traffic and routes requests to backend services for managed scale and high availability.
- AWS WAF: Enforces per-client usage quotas and rate limiting to protect against traffic spikes.
- AWS Certificate Manager (ACM): Enforces TLS 1.3 at the edge for secure connections.
- AWS Cloud Map: Handles internal service discovery for gRPC over HTTP/2 backend dispatching.
- AWS ECS Fargate: Hosts backend services securely and scalably without server management.

## Rationale
This architecture uses managed AWS cloud primitives and serverless patterns to guarantee 99.95% availability, support 1 million monthly active users, and maintain fast page loads. It enforces strict GDPR, CCPA, and OWASP Top-10 compliance with minimal operational overhead.