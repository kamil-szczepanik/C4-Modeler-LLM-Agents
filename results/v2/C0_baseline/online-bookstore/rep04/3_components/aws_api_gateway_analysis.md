## Overview
The Online Bookstore system is a scalable e-commerce platform built on AWS to support physical and electronic book sales, personalized recommendations, and reviews for 1M MAU. It features a React SPA frontend communicating securely via an enterprise-grade AWS API Gateway with downstream microservices.

## Key Elements
- React / TypeScript SPA (React, TypeScript, AWS S3, AWS CloudFront)
- AWS API Gateway (API & Routing Container)
- Edge Request Router (AWS API Gateway HTTP/REST APIs)
- Security & Validation Filter (AWS WAF)
- Token Authorizer (AWS Lambda Authorizer with Auth0/AWS Cognito)
- API Response Cache (API Gateway Managed Cache)
- Telemetry & Metering Filter (Amazon CloudWatch)
- Backend Microservices (Order & Checkout, Catalog & Search, Recommendations, Review Services)

## Relationships
- React SPA -> Security & Validation Filter [HTTPS / TLS 1.3 / JSON]
- Security & Validation Filter -> Edge Request Router [Internal Routing]
- Edge Request Router -> Token Authorizer [gRPC / Lambda Invocation]
- Edge Request Router -> API Response Cache [Internal Cache Read/Write]
- Edge Request Router -> Telemetry & Metering Filter [Async / CloudWatch API]
- Edge Request Router -> Backend Microservices [mTLS / REST and gRPC]

## Technology Stack
- AWS API Gateway: Manages geo-routing, rate limiting, and HTTP/REST traffic.
- AWS WAF: Mitigates OWASP Top-10 vulnerabilities and provides DDoS protection.
- AWS Lambda: Executes lightweight JWT token authorization.
- Amazon CloudWatch & AWS X-Ray: Handles distributed tracing, telemetry, and metrics monitoring.
- TLS 1.3 & mTLS: Secures client-to-gateway and gateway-to-microservice communication.

## Rationale
This architecture ensures 99.95% uptime and sub-2-second page loads for 1M MAU through edge caching and robust rate limiting. Furthermore, it enforces GDPR/CCPA compliance via strict PII masking, regional geo-routing, and multi-currency context management.