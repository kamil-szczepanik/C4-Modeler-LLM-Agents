## Overview
The Online Bookstore uses a cloud-native architecture to provide catalogue browsing, secure checkout, customer reviews, and personalized recommendations. It guarantees high availability and scalability for 1 million monthly active users while complying with GDPR and CCPA regulations.

## Key Elements
- Book Buyer / Customer and Site Visitor
- Public Catalog & Search SPA & Authenticated Customer Portal SPA (Amazon S3, Amazon CloudFront, AWS WAF)
- AWS API Gateway (AWS API Gateway, AWS App Mesh)
- Catalog & Search Service, Order & Checkout Service, Recommendation & Review Service, Customer Review & Moderation Service, Notification & Engagement Worker (Node.js/Express, Java/Spring Boot, Python/FastAPI, AWS ECS on Fargate)
- Amazon RDS (Amazon Aurora PostgreSQL, Multi-AZ, Amazon RDS Proxy)
- Redis on Amazon ElastiCache (Redis, Amazon ElastiCache)
- Amazon SQS
- AWS Secrets Manager (AWS Secrets Manager, AWS KMS)
- Payment Gateway, Third-Party Shipping Providers, Tax & Compliance Service, Recommendation Engine (AWS Personalize), Email/Notification Service (Amazon SES), Centralized Logging & SIEM

## Relationships
- Book Buyer / Customer and Site Visitor -> Public Catalog & Search SPA & Authenticated Customer Portal SPA: HTTPS (TLS 1.3)
- Public Catalog & Search SPA & Authenticated Customer Portal SPA -> AWS API Gateway: HTTPS
- AWS API Gateway -> ECS Fargate Microservices: gRPC over TLS with mutual TLS via AWS App Mesh
- ECS Fargate Microservices -> Amazon RDS Proxy: PostgreSQL wire protocol over TLS 1.3
- Amazon RDS Proxy -> Amazon Aurora PostgreSQL Cluster: PostgreSQL wire protocol over TLS 1.3 via internal VPC
- Order & Checkout Service -> Payment Gateway, Third-Party Shipping Providers, Tax & Compliance Service: REST over HTTPS with circuit breakers
- Recommendation & Review Service -> Recommendation Engine (AWS Personalize): REST over HTTPS
- Notification & Engagement Worker -> Email/Notification Service (Amazon SES): HTTPS

## Technology Stack
- AWS ECS on Fargate: Runs containerized microservices without server management for scalability.
- Amazon Aurora PostgreSQL (Multi-AZ): Provides high-performance relational database storage with automated failover.
- Amazon RDS Proxy: Manages and pools database connections to prevent exhaustion during traffic spikes.
- Redis on Amazon ElastiCache: Delivers in-memory caching to protect checkout availability.
- AWS Secrets Manager & AWS KMS: Secures credentials and enforces encryption-at-rest for GDPR/CCPA compliance.

## Rationale
This architecture uses serverless containers and managed AWS services to easily scale for 1 million active users while maintaining sub-2-second page loads. Strict network isolation, encryption, and multi-AZ deployments ensure 99.95% uptime and robust regulatory compliance.