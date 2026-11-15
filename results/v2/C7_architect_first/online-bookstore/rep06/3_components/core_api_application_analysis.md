## Overview
- The Core API Application is a Node.js and Express container deployed on Amazon ECS Fargate that manages business logic, routing, and transactional workflows for the Online Bookstore.
- It processes e-commerce operations including catalog browsing, cart and checkout, order management, and customer reviews while complying with scalability and security requirements.

## Key Elements
- Catalog Component (TypeScript): Handles browsing, keyword search queries, and caching interactions.
- Cart & Checkout Component (TypeScript): Manages shopping carts, payment coordination, session persistence, and idempotency.
- Order Management Component (TypeScript): Orchestrates fulfillment, transactional outbox pattern, and event publishing.
- Review Component (TypeScript): Manages customer reviews, 5-star ratings, and moderation workflows.
- Database & Cache: Amazon Aurora PostgreSQL and Amazon ElastiCache Redis.
- Messaging & Integration: Amazon SQS, Amazon SNS, and Amazon EventBridge.

## Relationships
- API Gateway -> Core API Application: Routes external traffic [mTLS / AWS Service Connect]
- Core API Application -> Database & Cache: Queries and transactions [Prisma ORM over TLS / ioredis (RESP)]
- Core API Application -> Messaging & Integration: Publishes events for async processing [AWS SQS/SNS/EventBridge]
- Core API Application -> Payment Gateway: Processes secure financial transactions [HTTPS via AWS Network Firewall]
- Core API Application -> Shipping Provider APIs: Calculates shipping and generates labels [HTTPS via AWS Network Firewall]

## Technology Stack
- Node.js & Express: Runtime and framework for the core API container on Amazon ECS Fargate.
- TypeScript: Strongly typed language utilized across all internal application components.
- Prisma ORM: Database toolkit for type-safe interaction with Amazon Aurora PostgreSQL.
- Zod: Runtime schema validation library for input sanitization and payload security.
- OpenTelemetry: Distributed tracing framework for internal component monitoring and span metrics.
- AWS Secrets Manager: Credential management tool for runtime injection of database and API keys.

## Rationale
- The modular TypeScript component decomposition isolates blast radiuses and enables independent scaling on Amazon ECS Fargate to handle 1M MAU without performance degradation.
- CQRS, the Transactional Outbox pattern, and robust idempotency safeguards ensure high availability, zero dual-write failures, and strict transactional integrity for revenue-critical checkout workflows.