## Overview
The Order & Checkout Service is an internal Node.js container within the Online Bookstore handling ACID-compliant transactions, shopping carts, and order processing. It ensures secure multi-currency checkouts while integrating with external payment and shipping providers on AWS.

## Key Elements
- **Checkout Controller**: Express.js component for request routing, input validation, and rate-limiting.
- **Order Management Service**: Domain logic component for cart processing, order state transitions, and multi-currency pricing.
- **Transaction Coordinator**: Prisma ORM-backed component managing ACID database transactions.
- **Idempotency Manager**: Redis-backed component deduplicating checkout requests to prevent double-charging.
- **Integration Facade**: Opossum-protected component handling external HTTPS integrations.
- **Event Publisher**: AWS SDK v3 component for asynchronous messaging.

## Relationships
- **Checkout Controller** -> **Order Management Service**: Direct TypeScript function calls [In-Memory]
- **Order Management Service** -> **Transaction Coordinator**: Direct TypeScript function calls [In-Memory]
- **Transaction Coordinator** -> **Amazon Aurora PostgreSQL**: Persists transactions and orders [PostgreSQL Protocol over TCP]
- **Checkout Controller** -> **Idempotency Manager**: Validates request tokens [Redis Protocol over TCP]
- **Integration Facade** -> **Payment Gateway**, **Shipping Provider APIs**, **Tax Calculation Service**, **Email/Notification Service**: Processes external workflows [HTTPS REST APIs & webhooks]
- **Event Publisher** -> **Amazon SNS/SQS**: Publishes domain events [AWS SDK v3 over AWS VPC Endpoints]

## Technology Stack
- **Node.js & Express.js**: Runtime and web framework for fast asynchronous request handling.
- **TypeScript**: Typed language ensuring compile-time safety across components.
- **Prisma ORM**: Type-safe database toolkit for managing migrations and queries against **Amazon Aurora PostgreSQL**.
- **Amazon Aurora PostgreSQL**: Relational database providing strict ACID guarantees for financial data.
- **Amazon ElastiCache (Redis)**: In-memory store utilized by the Idempotency Manager for request deduplication.
- **Opossum**: Circuit breaker library ensuring fault-tolerance for external API calls.
- **AWS SDK for JavaScript v3**: Library for publishing asynchronous events to **Amazon SNS/SQS**.

## Rationale
This component architecture uses Prisma and Aurora PostgreSQL to guarantee strict ACID compliance for financial orders. Incorporating Redis-backed idempotency and circuit breakers ensures high availability and resilience against third-party failures under peak loads.