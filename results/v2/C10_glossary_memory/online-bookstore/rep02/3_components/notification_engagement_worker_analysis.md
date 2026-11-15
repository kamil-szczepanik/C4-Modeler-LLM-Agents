## Overview
The Online Bookstore system is a cloud-native e-commerce platform providing catalogue browsing, secure checkout, customer reviews, and personalized recommendations. It utilizes a microservices architecture deployed on AWS to deliver high scalability and availability for book buyers and site visitors globally.

## Key Elements
- Book Buyer / Customer and Site Visitor
- Public Catalog & Search SPA & Authenticated Customer Portal SPA (Amazon S3, Amazon CloudFront, AWS WAF)
- AWS API Gateway (AWS API Gateway, AWS App Mesh)
- Catalog & Search Service (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Order & Checkout Service (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Recommendation & Review Service (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Customer Review & Moderation Service (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Notification & Engagement Worker (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Amazon RDS
- Redis on Amazon ElastiCache (Redis, Amazon ElastiCache)
- Amazon SQS
- AWS Secrets Manager (AWS Secrets Manager, AWS KMS)
- Payment Gateway, Third-Party Shipping Providers, Tax & Compliance Service, Recommendation Engine (AWS Personalize), Email/Notification Service (Amazon SES), Centralized Logging & SIEM

## Relationships
- Book Buyer / Customer and Site Visitor -> Public Catalog & Search SPA & Authenticated Customer Portal SPA [HTTPS (TLS 1.3)]
- Public Catalog & Search SPA & Authenticated Customer Portal SPA -> AWS API Gateway [HTTPS]
- AWS API Gateway -> Catalog & Search Service [gRPC over TLS with mutual TLS via AWS App Mesh]
- AWS API Gateway -> Order & Checkout Service [gRPC over TLS with mutual TLS via AWS App Mesh]
- AWS API Gateway -> Recommendation & Review Service [gRPC over TLS with mutual TLS via AWS App Mesh]
- AWS API Gateway -> Customer Review & Moderation Service [gRPC over TLS with mutual TLS via AWS App Mesh]
- Order & Checkout Service -> Payment Gateway [REST over HTTPS with circuit breakers]
- Order & Checkout Service -> Third-Party Shipping Providers [REST over HTTPS with circuit breakers]
- Order & Checkout Service -> Tax & Compliance Service [REST over HTTPS with circuit breakers]
- Recommendation & Review Service -> Recommendation Engine [REST over HTTPS]
- Notification & Engagement Worker -> Email/Notification Service [HTTPS]
- Notification & Engagement Worker -> Amazon SQS [AWS SDK]
- Notification & Engagement Worker -> Amazon RDS [AWS SDK]
- Catalog & Search Service -> Redis on Amazon ElastiCache [RESP]

## Technology Stack
- AWS ECS on Fargate: Container orchestration for microservices without server management.
- Node.js/Express, Java/Spring Boot, Python/FastAPI: Polyglot backend implementation choices.
- Amazon RDS: Relational storage for persistent transactional and preference data.
- Redis on Amazon ElastiCache: In-memory caching layer to optimize performance and protect checkout availability.
- Amazon SQS: Decoupled asynchronous messaging queue.
- Amazon SES: Email and notification delivery service.

## Rationale
This microservices architecture ensures independent scaling and high availability to comfortably meet the 1M MAU scalability requirement and 99.95% uptime target. AWS managed services reduce operational overhead while maintaining strict security, GDPR/CCPA compliance, and performance standards.