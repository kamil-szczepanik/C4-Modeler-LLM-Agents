## Overview
The Online Bookstore is a cloud-native e-commerce platform providing catalogue browsing, secure checkout, customer reviews, and personalized recommendations for physical and electronic books. It ensures high availability, scalability for 1M MAU, and regulatory compliance while maintaining low-latency performance.

## Key Elements
- Book Buyer / Customer and Site Visitor
- Public Catalog & Search SPA & Authenticated Customer Portal SPA
- AWS API Gateway
- Catalog & Search Service
- Order & Checkout Service
- Recommendation & Review Service
- Customer Review & Moderation Service
- Notification & Engagement Worker
- Amazon RDS
- Redis on Amazon ElastiCache
- Amazon SQS (Order Queue, Notification DLQ)
- AWS Secrets Manager / AWS KMS
- External Systems: Payment Gateway, Third-Party Shipping Providers, Tax & Compliance Service, Recommendation Engine (AWS Personalize), Email/Notification Service (Amazon SES), Centralized Logging & SIEM

## Relationships
- Book Buyer / Customer and Site Visitor -> Public Catalog & Search SPA & Authenticated Customer Portal SPA via HTTPS (TLS 1.3)
- Public Catalog & Search SPA & Authenticated Customer Portal SPA -> AWS API Gateway via HTTPS
- AWS API Gateway -> Internal Services (Catalog & Search, Order & Checkout, Recommendation & Review, Customer Review & Moderation) via gRPC over TLS with mutual TLS via AWS App Mesh
- Order & Checkout Service -> Amazon SQS (Order Queue) via AWS SDK over HTTPS (TLS 1.3)
- Amazon SQS (Order Queue) -> Notification & Engagement Worker via AWS SDK Long Polling
- Notification & Engagement Worker -> Amazon SQS (Notification DLQ) via AWS SDK
- Internal Services -> Amazon RDS via AWS SDK
- Catalog & Search Service -> Redis on Amazon ElastiCache via RESP
- Internal Services -> AWS Secrets Manager via AWS SDK
- Internal Services -> Centralized Logging & SIEM via HTTPS / AWS Infrastructure

## Technology Stack
- **Frontend:** Amazon S3, Amazon CloudFront, AWS WAF for secure, low-latency static content delivery and protection.
- **API Management:** AWS API Gateway with AWS App Mesh for mutual TLS and secure routing.
- **Compute:** AWS ECS on Fargate supporting Node.js/Express, Java/Spring Boot, and Python/FastAPI microservices.
- **Database:** Amazon RDS for relational persistence and Redis on Amazon ElastiCache for in-memory caching.
- **Messaging:** Amazon SQS for decoupled asynchronous processing and fault tolerance.
- **Security & Observability:** AWS Secrets Manager, AWS KMS, Amazon CloudWatch, and AWS CloudTrail.

## Rationale
This microservices-based architecture leverages AWS managed services to easily scale and handle peak traffic loads without performance degradation. Decoupling core workflows with Amazon SQS and implementing stringent security controls ensures high availability, data protection compliance, and system resilience.