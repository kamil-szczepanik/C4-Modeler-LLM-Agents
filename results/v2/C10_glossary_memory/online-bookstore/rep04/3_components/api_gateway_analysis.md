## Overview
The Online Bookstore System is an AWS-hosted e-commerce platform designed to support 1 million monthly active users with multi-currency capabilities and GDPR/CCPA compliance. It provides secure catalog browsing, checkout, customer reviews, and personalized recommendations.

## Key Elements
- API Gateway (Amazon API Gateway)
- Routing & Dispatcher Component
- Authentication & Authorization Authorizer
- Throttling & Rate Limiting Component
- Request Transformation & Enrichment Component
- Web App Frontend (React, Next.js, TypeScript)
- Catalog & Search Service (Java, Spring Boot, Amazon OpenSearch)
- Checkout & Order Service (Go, gRPC/REST)
- Recommendation Service (Python, FastAPI)
- Admin Management Service (Java, Spring Boot)
- Identity Provider (AWS Cognito/Auth0)
- AWS CloudFront CDN/WAF
- AWS Secrets Manager

## Relationships
- Web App Frontend -> API Gateway: Sends API requests [HTTPS / REST / gRPC]
- Routing & Dispatcher Component -> Catalog & Search Service: Forwards queries [gRPC over TLS with mTLS]
- Routing & Dispatcher Component -> Checkout & Order Service: Routes checkout payloads [gRPC/HTTP/2 over mTLS]
- Authentication & Authorization Authorizer -> Identity Provider: Validates tokens [HTTPS / OAuth 2.0 / OIDC]
- Request Transformation & Enrichment Component -> AWS Secrets Manager: Fetches routing secrets [HTTPS]

## Technology Stack
- Amazon API Gateway: Manages and routes ingress traffic with built-in scalability.
- AWS Private Certificate Authority: Enforces mutual TLS (mTLS) for secure service-to-service communication.
- AWS X-Ray & Amazon CloudWatch: Provides end-to-end tracing and real-time observability.
- AWS CloudFront WAF: Mitigates DDoS attacks and OWASP Top-10 threats at the edge.

## Rationale
This architecture ensures 99.95% uptime and sub-second performance by decoupling routing, security, and throttling logic within the API Gateway. Strict mTLS and token validation meet rigorous GDPR/CCPA and OWASP security constraints.