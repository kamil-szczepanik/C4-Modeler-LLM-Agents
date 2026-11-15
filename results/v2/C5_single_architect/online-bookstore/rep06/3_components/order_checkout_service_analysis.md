## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce system built to support high-throughput book sales with recommendations and reviews. The Order & Checkout Service container uses a modular Spring Boot architecture running on AWS to handle secure checkouts and fulfillment.

## Key Elements
- Customer & Admin / Support Staff
- Single Page Application (React, Amazon S3, Amazon CloudFront)
- API Gateway (Amazon API Gateway)
- Order & Checkout Service (Spring Boot containers: Checkout Controller, Order Management Service, Payment Coordinator, Fulfillment Adapter, Order Repository, Cart Domain Component)
- External Systems: Payment Gateway, Shipping Provider APIs, Tax Calculation Service, Identity Provider / SSO Service
- Data & Messaging: Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis), MongoDB, Amazon SQS, Amazon SNS

## Relationships
- API Gateway -> Order & Checkout Service: Routes order and checkout requests [gRPC / HTTPS]
- Checkout Controller -> Order Management Service: In-memory Java method calls [Synchronous]
- Payment Coordinator -> Payment Gateway: Processes payments with idempotency keys [HTTPS / REST]
- Fulfillment Adapter -> Shipping Provider APIs: Arranges shipping and fulfillment [HTTPS / REST]
- Order Management Service -> Amazon SNS / Messaging & Workers: Publishes asynchronous events [Async / JSON]
- Order Repository -> Amazon Aurora PostgreSQL: Persists order data [TCP / PostgreSQL protocol]

## Technology Stack
- Spring Boot & Spring Data JPA: Ensures ACID compliance for financial transactions and reliable domain modeling.
- Amazon Aurora PostgreSQL: Provides scalable, relational persistence for critical order data.
- Amazon SNS & SQS: Decouples downstream fulfillment and recommendation services asynchronously.
- React, Amazon S3, & CloudFront: Delivers high-performance frontend assets globally.

## Rationale
This architecture ensures 99.95% availability and sub-2-second page loads across multiple AWS regions while strictly meeting GDPR and CCPA compliance. Isolating third-party integrations via dedicated adapters guarantees fault tolerance during peak scalability of 1 million monthly active users.