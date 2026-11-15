## Overview
The Core E-Commerce API is a NestJS container on AWS ECS Fargate that orchestrates business logic for the Online Bookstore. It securely handles catalog browsing, shopping carts, secure checkouts, and multi-currency transactions.

## Key Elements
- Catalog Controller & Service (NestJS)
- Cart & Checkout Engine (NestJS)
- Currency Conversion Provider (NestJS)
- Feature Flag Module (AWS AppConfig / Unleash SDK)
- Idempotency Interceptor (NestJS / Redis)
- Payment & Shipping Gateway Adapters (NestJS / Circuit Breaker)
- Order Event Publisher (NestJS / Amazon EventBridge / Amazon SQS)

## Relationships
- Amazon API Gateway -> Core E-Commerce API: Routes client requests securely via mTLS
- Core E-Commerce API -> Amazon Aurora PostgreSQL: Reads/writes transactional data via TLS over TCP
- Core E-Commerce API -> Amazon ElastiCache (Redis): Caches exchange rates, promos, and idempotency locks via TLS over TCP
- Core E-Commerce API -> Recommendation Service: Requests personalized recommendations via gRPC
- Core E-Commerce API -> Amazon SQS: Queues shipping fulfillment tasks via AWS SDK
- Amazon EventBridge -> Core E-Commerce API: Triggers event handlers via Event Bus

## Technology Stack
- Node.js with NestJS: Modular framework for organizing controllers, services, and middleware.
- AWS ECS (Fargate): Scalable serverless container hosting for 1M MAU performance.
- Amazon Aurora PostgreSQL: Multi-AZ relational database with AWS KMS PII encryption.
- Amazon ElastiCache (Redis): High-performance caching for currency rates and idempotency locks.
- class-validator: Strict DTO validation for OWASP Top-10 security mitigation.

## Rationale
This architecture modularizes core e-commerce domains while enforcing strict security, idempotency, and fault tolerance via circuit breakers. It ensures 99.95% uptime, GDPR/CCPA compliance, and multi-currency support for a global user base.