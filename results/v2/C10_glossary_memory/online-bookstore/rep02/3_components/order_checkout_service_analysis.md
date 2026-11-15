## Overview
The Online Bookstore is a cloud-native e-commerce platform providing catalogue browsing, secure checkout, customer reviews, and personalized recommendations. The architecture utilizes distributed microservices deployed on AWS to handle high transaction volumes securely.

## Key Elements
- Book Buyer / Customer and Site Visitor
- Public Catalog & Search SPA & Authenticated Customer Portal SPA (Amazon S3, Amazon CloudFront, AWS WAF)
- AWS API Gateway (AWS API Gateway, AWS App Mesh)
- Order & Checkout Service (Java/Spring Boot, AWS ECS on Fargate)
- Checkout Orchestrator Component, Cart Management Component, Payment & Tax Integration Component, Order Fulfillment Component
- Payment Gateway, Third-Party Shipping Providers, Tax & Compliance Service
- Amazon RDS, Redis on Amazon ElastiCache, Amazon SQS, AWS Secrets Manager, Centralized Logging & SIEM

## Relationships
- Book Buyer / Customer and Site Visitor -> Public Catalog & Search SPA & Authenticated Customer Portal SPA: HTTPS (TLS 1.3)
- Public Catalog & Search SPA & Authenticated Customer Portal SPA -> AWS API Gateway: HTTPS
- AWS API Gateway -> Order & Checkout Service: gRPC over TLS (with mutual TLS via AWS App Mesh)
- Order & Checkout Service -> Payment Gateway: REST over HTTPS with circuit breakers
- Order & Checkout Service -> Third-Party Shipping Providers: REST over HTTPS with circuit breakers
- Order & Checkout Service -> Tax & Compliance Service: REST over HTTPS with circuit breakers
- Cart Management Component -> Redis on Amazon ElastiCache: RESP (AWS SDK)
- Order Fulfillment Component -> Amazon SQS: AWS SDK
- Order & Checkout Service -> Amazon RDS: AWS SDK

## Technology Stack
- Java/Spring Boot: Core framework for business logic and component implementation
- AWS ECS on Fargate: Container orchestration for scalable microservice deployment
- Redis on Amazon ElastiCache: In-memory store for session management and persistent cart state
- Amazon SQS: Asynchronous message queuing for decoupling order fulfillment events
- AWS API Gateway & App Mesh: Secure routing and service mesh management with mTLS

## Rationale
This architecture ensures 99.95% uptime and scalability for 1 million MAU through containerized microservices on AWS ECS Fargate. Strict PCI-DSS scoping and circuit-breaker patterns protect revenue processing against third-party latency and failures.