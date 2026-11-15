## Overview
The Online Bookstore is a cloud-native e-commerce platform providing catalogue browsing, secure checkout, customer reviews, and personalized recommendations for physical and electronic books. The architecture utilizes AWS services and microservices to support global scalability, high performance, and strict regulatory compliance.

## Key Elements
- Book Buyer / Customer and Site Visitor
- Public Catalog & Search SPA & Authenticated Customer Portal SPA (Amazon S3, Amazon CloudFront, AWS WAF)
- AWS API Gateway (AWS API Gateway, AWS App Mesh)
- Catalog & Search Service (Java/Spring Boot, AWS ECS on Fargate)
- Order & Checkout Service (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Recommendation & Review Service (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Customer Review & Moderation Service (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Notification & Engagement Worker (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Amazon RDS
- Amazon OpenSearch Service
- Redis on Amazon ElastiCache (Redis, Amazon ElastiCache)
- Amazon SQS
- AWS Secrets Manager (AWS Secrets Manager, AWS KMS)
- Payment Gateway, Third-Party Shipping Providers, Tax & Compliance Service, Recommendation Engine (AWS Personalize), Email/Notification Service (Amazon SES), Centralized Logging & SIEM

## Relationships
- Book Buyer / Customer and Site Visitor -> Public Catalog & Search SPA & Authenticated Customer Portal SPA [HTTPS (TLS 1.3)]
- Public Catalog & Search SPA & Authenticated Customer Portal SPA -> AWS API Gateway [HTTPS]
- AWS API Gateway -> Catalog & Search Service [gRPC over TLS (with mutual TLS via AWS App Mesh)]
- Catalog & Search Service -> Amazon RDS [AWS SDK]
- Catalog & Search Service -> Amazon OpenSearch Service [HTTPS]
- Catalog & Search Service -> Redis on Amazon ElastiCache [RESP over TLS]
- Catalog & Search Service -> AWS Secrets Manager [AWS SDK]
- Catalog & Search Service -> Centralized Logging & SIEM [HTTPS / AWS Infrastructure]
- Order & Checkout Service -> Payment Gateway [REST over HTTPS with circuit breakers]
- Order & Checkout Service -> Third-Party Shipping Providers [REST over HTTPS with circuit breakers]
- Order & Checkout Service -> Tax & Compliance Service [REST over HTTPS with circuit breakers]

## Technology Stack
- AWS ECS on Fargate: Runs containerized microservices with serverless container management to meet 1M MAU scalability requirements.
- Java/Spring Boot: Implements high-throughput gRPC and REST handling for the Catalog & Search Service.
- Amazon OpenSearch Service: Offloads heavy keyword searches, facets, and localized multi-currency catalog filtering.
- Redis on Amazon ElastiCache: Provides in-memory caching with RESP over TLS to protect database performance and support fallback resilience.
- Amazon RDS: Stores persistent relational application data.
- AWS API Gateway & App Mesh: Manages API routing and mutual TLS service-to-service communication.
- AWS Secrets Manager & KMS: Manages encrypted secrets, AWS SigV4, and field-level data protection.

## Rationale
This architecture leverages AWS serverless containerization and managed data layers (OpenSearch, ElastiCache, RDS) to achieve sub-second search responses and handle 1M MAU under strict performance constraints. Robust security controls, IaC automation, and multi-region readiness ensure GDPR/CCPA compliance, 99.95% availability, and OWASP Top-10 mitigation.