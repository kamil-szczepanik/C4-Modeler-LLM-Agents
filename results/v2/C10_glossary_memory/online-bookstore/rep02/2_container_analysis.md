## Overview
An AWS cloud-native e-commerce platform provides catalogue browsing, secure checkout, reviews, and personalized recommendations for physical and electronic books. It targets 1 million monthly active users while ensuring strict GDPR, CCPA, and OWASP Top-10 compliance.

## Key Elements
- Book Buyer / Customer and Site Visitor
- Public Catalog & Search SPA & Authenticated Customer Portal SPA
- Amazon S3 & CloudFront
- AWS API Gateway
- Catalog & Search Service, Order & Checkout Service, Recommendation & Review Service, Customer Review & Moderation Service, Notification & Engagement Worker
- Amazon RDS & Redis on Amazon ElastiCache
- Amazon SQS & AWS Secrets Manager
- External Systems: Payment Gateway, Third-Party Shipping Providers, Tax & Compliance Service, Recommendation Engine (AWS Personalize), Email/Notification Service (Amazon SES), Centralized Logging & SIEM

## Relationships
- Book Buyer / Customer and Site Visitor -> Amazon S3 & CloudFront via HTTPS (TLS 1.3)
- SPAs -> AWS API Gateway via HTTPS
- API Gateway -> Microservices via gRPC over TLS (with mutual TLS via AWS App Mesh)
- Order & Checkout Service -> Payment Gateway, Third-Party Shipping Providers, and Tax & Compliance Service via REST over HTTPS with circuit breakers
- Recommendation & Review Service -> AWS Personalize via REST over HTTPS
- Notification & Engagement Worker -> Amazon SES via HTTPS
- Microservices -> Amazon RDS, Redis, and Amazon SQS via AWS SDK and RESP

## Technology Stack
- Frontend: Amazon S3 and Amazon CloudFront with AWS WAF for edge security
- API Gateway & Orchestration: AWS API Gateway, AWS ECS on Fargate, AWS App Mesh, Terraform
- Backend Services: Node.js/Express, Java/Spring Boot, Python/FastAPI
- Databases & Caching: Amazon RDS, Redis on Amazon ElastiCache
- Messaging & Security: Amazon SQS, AWS KMS, AWS Secrets Manager, OpenTelemetry / AWS X-Ray

## Rationale
The microservices architecture deployed on AWS ECS Fargate across multi-region clusters ensures 99.95% uptime and scalable handling of 1M MAU. Decoupled asynchronous messaging with Amazon SQS and managed caching with Redis protect checkout availability and maintain sub-2-second page loads on 3G networks.