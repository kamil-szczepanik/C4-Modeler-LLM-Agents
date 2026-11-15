## Overview
The Online Bookstore system is a scalable, Amazon-style e-commerce platform for purchasing physical and electronic books, featuring reviews and recommendations. It uses an AWS-hosted microservices architecture designed to handle 1 million monthly active users globally while ensuring GDPR and CCPA compliance.

## Key Elements
- **Users**: Customer, Book Author/Publisher, Customer Support Agent, Shipping Partner, Site Administrator
- **External Systems**: Payment Gateway, Shipping Provider APIs, Notification Service, Currency Exchange API
- **Client Container**: Single-Page Application (React, Amazon S3, Amazon CloudFront)
- **Edge / Ingress Container**: AWS API Gateway (Amazon API Gateway, AWS WAF, AWS Lambda, Amazon CloudWatch, AWS X-Ray)
- **Service Mesh Container**: Envoy Service Mesh (Envoy, SPIFFE/SPIRE, AWS Secrets Manager)
- **Backend Containers**: Catalog Service, Order & Checkout Service, Recommendation Service, Customer Service, Admin & Support Service (Node.js, Java, Python, Go, AWS ECS on Fargate)
- **Data & Messaging Containers**: Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis), Amazon S3, Amazon EventBridge, Amazon SQS

## Relationships
- Single-Page Application -> AWS API Gateway: Makes API requests [HTTPS (TLS 1.3)]
- AWS API Gateway (Route Dispatcher) -> Lambda Authorizer: Invokes token verification [AWS Lambda Invocation / HTTPS]
- Route Dispatcher -> Transformation & Policy: Applies header enrichment and error mapping [Internal Pipeline]
- Transformation & Policy -> Envoy Service Mesh: Forwards enriched traffic [gRPC over mTLS]
- Envoy Service Mesh -> Backend ECS Services: Routes internal microservice traffic [gRPC/HTTP]

## Technology Stack
- **Edge & Routing**: Amazon API Gateway REST/HTTP APIs with custom VTL/JSON Schema transformations for RFC 7807 error normalization.
- **Security & WAF**: AWS WAF with global rate-limiting and OWASP Top-10 rule sets; AWS Lambda for JWT validation and RBAC.
- **Compute & Orchestration**: AWS ECS on Fargate across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.
- **Database & Caching**: Amazon Aurora PostgreSQL with AWS KMS encryption; Amazon ElastiCache (Redis) for distributed rate-limiting and auth caching.
- **Observability**: Amazon CloudWatch and AWS X-Ray for active tracing and SLA tracking.

## Rationale
The architecture combines Amazon API Gateway and AWS WAF with a multi-region active-active deployment to enforce strict security and sub-2-second page loads globally. This ensures high availability (99.95%), fault tolerance, and seamless GDPR/CCPA compliance under high concurrency.