## Overview
[Component-level C4 architecture for the Order & Checkout Service container within the Online Bookstore platform. Core purpose is handling secure, distributed transaction checkouts and order processing.]

## Key Elements
- **API Controller Component** (NestJS)
- **Idempotency Manager Component** (Node.js / TypeScript)
- **Cart Manager Component** (TypeScript)
- **Checkout Orchestrator Component** (TypeScript with Saga pattern)
- **Order Repository Component** (TypeORM / Prisma)
- **Event Publisher Component** (AWS SDK)
- **External Systems:** Payment Gateway, Tax Calculation Service, Shipping Provider APIs

## Relationships
- **AWS API Gateway** -> **API Controller Component**: Routes internal traffic [gRPC over TLS / HTTPS]
- **API Controller Component** -> **Idempotency Manager Component**: Validates request tokens synchronously [In-memory TypeScript]
- **Idempotency Manager Component** -> **Redis ElastiCache**: Checks/stores cryptographic request hashes [Redis Protocol over VPC]
- **Cart Manager Component** -> **Redis ElastiCache**: Manages session and cart state [Redis Protocol over VPC]
- **Cart Manager Component** -> **Order Repository Component**: Snapshots cart data upon checkout [TypeORM / Prisma]
- **Checkout Orchestrator Component** -> **Payment Gateway**: Authorizes and captures payments [HTTPS / REST with Opossum Circuit Breaker]
- **Checkout Orchestrator Component** -> **Tax Calculation Service**: Calculates dynamic taxes [HTTPS / REST with Opossum Circuit Breaker]
- **Checkout Orchestrator Component** -> **Shipping Provider APIs**: Generates shipping labels [HTTPS / REST with Opossum Circuit Breaker]
- **Order Repository Component** -> **Amazon Aurora PostgreSQL**: Persists order data [Native Database Protocol over VPC]
- **Event Publisher Component** -> **Amazon EventBridge & SQS**: Dispatches domain events [AWS SDK / API]

## Technology Stack
- **NestJS:** Enforces strict DTO validation, modular architecture, and OWASP Top-10 security postures.
- **TypeScript:** Powers strongly-typed internal domain logic and workflow orchestration.
- **Redis ElastiCache:** Delivers low-latency session caching and atomic idempotency checks (`SETNX`).
- **TypeORM / Prisma:** Encapsulates ACID-compliant data access patterns to PostgreSQL.
- **Opossum:** Implements circuit breaker patterns and exponential backoff for third-party API resilience.

## Rationale
[This component architecture guarantees financial accuracy and ACID compliance through robust idempotency checks and transactional cart snapshotting. It ensures 99.95% availability by isolating third-party failures via circuit breakers and resilient Saga orchestration.]