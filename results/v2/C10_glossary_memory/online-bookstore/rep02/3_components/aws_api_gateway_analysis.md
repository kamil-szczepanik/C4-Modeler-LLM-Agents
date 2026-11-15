## Overview
The Online Bookstore is a cloud-native e-commerce platform providing catalogue browsing, secure checkout, customer reviews, and personalized recommendations for physical and electronic books. It utilizes AWS managed services and microservices running on ECS to serve up to 1 million monthly active users while ensuring GDPR, CCPA, and OWASP compliance.

## Key Elements
- Book Buyer / Customer and Site Visitor
- Public Catalog & Search SPA & Authenticated Customer Portal SPA (Amazon S3, Amazon CloudFront, AWS WAF)
- AWS API Gateway (Amazon API Gateway HTTP API, AWS App Mesh, API Router / HTTP Proxy, JWT Authorizer / Auth Validator, Rate Limiter & Throttler, Service Mesh Proxy Sidecar, Request Validation & Transformation)
- Catalog & Search Service (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Order & Checkout Service (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Recommendation & Review Service (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Customer Review & Moderation Service (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Notification & Engagement Worker (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Amazon RDS
- Redis on Amazon ElastiCache
- Amazon SQS
- AWS Secrets Manager (AWS Secrets Manager, AWS KMS)
- Payment Gateway (Stripe/PayPal)
- Third-Party Shipping Providers (FedEx, UPS APIs)
- Tax & Compliance Service (Avalara)
- Recommendation Engine (AWS Personalize)
- Email/Notification Service (Amazon SES)
- Centralized Logging & SIEM

## Relationships
- Book Buyer / Customer and Site Visitor -> Public Catalog & Search SPA & Authenticated Customer Portal SPA [HTTPS (TLS 1.3)]
- Public Catalog & Search SPA & Authenticated Customer Portal SPA -> AWS API Gateway [HTTPS]
- AWS API Gateway -> Catalog & Search Service [gRPC over TLS (with mutual TLS via AWS App Mesh)]
- AWS API Gateway -> Order & Checkout Service [gRPC over TLS (with mutual TLS via AWS App Mesh)]
- AWS API Gateway -> Recommendation & Review Service [gRPC over TLS (with mutual TLS via AWS App Mesh)]
- AWS API Gateway -> Customer Review & Moderation Service [gRPC over TLS (with mutual TLS via AWS App Mesh)]
- Order & Checkout Service -> Payment Gateway [REST over HTTPS with circuit breakers]
- Order & Checkout Service -> Third-Party Shipping Providers [REST over HTTPS with circuit breakers]
- Order & Checkout Service -> Tax & Compliance Service [REST over HTTPS with circuit breakers]
- Recommendation & Review Service -> Recommendation Engine (AWS Personalize via REST over HTTPS)
- Notification & Engagement Worker -> Email/Notification Service (Amazon SES)
- Microservices -> Amazon RDS [AWS SDK]
- Catalog & Search Service -> Redis on Amazon ElastiCache [RESP]
- Order & Checkout Service -> Amazon SQS [AWS SDK]
- Microservices -> AWS Secrets Manager [AWS SDK]
- Microservices -> Centralized Logging & SIEM [HTTPS / AWS Infrastructure]

## Technology Stack
- Cloud Platform: AWS (us-east-1, eu-west-1, ap-southeast-1) for multi-region resilience.
- Frontend: Amazon S3, Amazon CloudFront, AWS WAF for secure static asset delivery.
- API Gateway & Routing: Amazon API Gateway HTTP API, AWS App Mesh, Envoy for low-latency routing and mTLS.
- Compute: AWS ECS on Fargate supporting Node.js/Express, Java/Spring Boot, and Python/FastAPI microservices.
- Storage & Caching: Amazon RDS for relational persistence and Redis on Amazon ElastiCache for high-performance caching.
- Messaging & Security: Amazon SQS, AWS Secrets Manager, AWS KMS, and AWS Lambda authorizers.

## Rationale
This architecture uses serverless containers and managed AWS services to easily scale and handle 1 million monthly active users without performance degradation. Mutual TLS, API gateway validation, and token caching ensure stringent security, GDPR compliance, and fast page loads under 2 seconds.