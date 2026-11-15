## Overview
The Online Bookstore system is a scaled-down e-commerce platform for purchasing physical and electronic books with recommendations and reviews. The architecture relies on secure microservices hosted on AWS to handle global traffic, multi-currency transactions, and regulatory compliance.

## Key Elements
- Shopper and Administrator (Users)
- Frontend App (React SPA, Amazon CloudFront, Amazon S3)
- Amazon API Gateway
- Catalog Service, Recommendation Service (AWS ECS Fargate)
- Order & Checkout Service (Java, Spring Boot, AWS ECS Fargate)
- Checkout Controller / Facade, Order Management Engine, Payment & Currency Gateway Client, Fulfillment Coordinator, Order Repository, Transactional Outbox Processor (Components)
- Amazon Aurora PostgreSQL, Amazon OpenSearch
- Third-Party Payment Gateway, Third-Party Shipping Provider, Third-Party Currency Exchange Service

## Relationships
- Amazon API Gateway -> Order & Checkout Service: Forwards order/checkout requests [HTTPS via AWS App Mesh]
- Order Management Engine -> Order Repository: Manages persistence [JDBC over TLS/IAM]
- Payment & Currency Gateway Client -> Third-Party Payment Gateway: Processes payments [HTTPS/REST]
- Fulfillment Coordinator -> Third-Party Shipping Provider: Coordinates fulfillment [HTTPS/REST]
- Transactional Outbox Processor -> AWS EventBridge: Publishes domain events [HTTPS/AWS SDK]
- Catalog Service / Recommendation Service -> Order & Checkout Service: Internal microservice communication [gRPC over mTLS]

## Technology Stack
- Java with Spring Boot: Powers the Order & Checkout Service for robust enterprise processing.
- AWS ECS Fargate & CloudFront/S3: Delivers scalable serverless container hosting and global static content delivery.
- Amazon Aurora PostgreSQL: Stores transactional data securely with TLS and IAM authentication.
- Resilience4j: Implements circuit breakers to protect against third-party dependency outages.
- AWS KMS & EventBridge: Secures sensitive metadata with encryption and drives event-based cart recovery.

## Rationale
This microservices-based AWS architecture ensures 99.95% uptime across three global regions by leveraging auto-scaling containers and circuit breakers. Strict tokenization, KMS encryption, and an outbox pattern fulfill stringent GDPR, CCPA, and PCI-DSS compliance requirements while maintaining high performance.