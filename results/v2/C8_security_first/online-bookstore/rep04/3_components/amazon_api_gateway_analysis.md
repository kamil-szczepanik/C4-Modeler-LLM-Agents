## Overview
The Online Bookstore is a scaled-down e-commerce platform providing catalog browsing, shopping carts, secure checkout, reviews, and recommendations for 1M MAU. It ensures global availability across three AWS regions while meeting strict GDPR, CCPA, and OWASP Top-10 security constraints.

## Key Elements
- **Users**: Shopper, Administrator
- **External Systems**: Third-Party Payment Gateway, Third-Party Shipping Provider, Third-Party Currency Exchange Service, Third-Party Recommendation Engine
- **Frontend App**: React SPA hosted via Amazon CloudFront and Amazon S3
- **Amazon API Gateway**: Single entry point, rate limiter, and edge router
- **Backend Services**: Catalog Service, Order & Checkout Service, Recommendation Service (Node.js, Java Spring Boot, Python FastAPI on AWS ECS Fargate)
- **Data & Search**: Amazon Aurora PostgreSQL, Amazon OpenSearch
- **Security & Infrastructure**: AWS WAF, AWS App Mesh, AWS Secrets Manager, Amazon Route 53

## Relationships
- Shopper / Administrator -> Amazon CloudFront: Browses site and submits requests [HTTPS/JSON with TLS 1.3]
- Amazon CloudFront -> Amazon S3: Fetches static frontend assets [HTTPS]
- Frontend App -> Amazon API Gateway: Sends API requests with currency headers [HTTPS/JSON]
- Amazon API Gateway -> Catalog Service / Order & Checkout Service / Recommendation Service: Forwards requests with JWT validation and context headers [gRPC/HTTPS via AWS App Mesh]
- Services -> Amazon Aurora PostgreSQL / Amazon OpenSearch: Reads and writes domain data [TCP]

## Technology Stack
- **API Management**: Amazon API Gateway with native JWT Authorizers for low-latency authentication
- **Security**: AWS WAF for OWASP Top-10 mitigation, AWS Secrets Manager for secret rotation
- **Compute & Mesh**: AWS ECS Fargate containers managed via AWS App Mesh for secure service-to-service communication
- **Infrastructure as Code**: Terraform and AWS CDK for repeatable deployments across regions
- **Global Routing**: Amazon Route 53 with latency-based routing across `us-east-1`, `eu-west-1`, and `ap-southeast-1`

## Rationale
This architecture leverages serverless edge routing and containerized microservices to scale efficiently for 1M MAU while guaranteeing sub-2-second page loads. Multi-region redundancy and native AWS security services ensure high availability (99.95%) and strict compliance with GDPR and CCPA.