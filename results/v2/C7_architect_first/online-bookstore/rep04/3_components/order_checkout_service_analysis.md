## Overview
- **System**: Order & Checkout Service container for the Online Bookstore e-commerce platform.
- **Core Purpose**: Manages secure, multi-step order placement, payment processing, and checkout workflows while ensuring strict compliance, high availability, and idempotency.

## Key Elements
- **Order Controller**: Exposes RESTful endpoints for cart finalization and checkout workflows [Spring MVC].
- **Checkout Orchestrator**: Manages multi-step saga patterns for payment processing and inventory reservation.
- **Payment Integration Client**: Communicates securely with external Payment Gateways using PCI-DSS compliant tokenization.
- **Shipping Facade**: Interfaces with external Third-Party Shipping APIs for rate calculations.
- **Promotion & Discount Engine**: Validates and applies coupon codes and promotional discounts in real-time.
- **Idempotency Manager**: Prevents double-charging and duplicate order creation.
- **Order Data Access Component**: Persists transactional order state and audit logs.
- **Event Publisher**: Emits asynchronous order fulfillment events.
- **Order Notification Trigger**: Dispatches confirmation messages and digital receipts.

## Relationships
- **Order Controller** -> **Checkout Orchestrator**: Triggers saga execution [Java Method Calls].
- **Checkout Orchestrator** -> **Payment Integration Client**: Executes secure payment processing [HTTPS/REST].
- **Checkout Orchestrator** -> **Shipping Facade**: Fetches shipping rates [gRPC].
- **Checkout Orchestrator** -> **Promotion & Discount Engine**: Validates coupons [In-memory / Java].
- **Checkout Orchestrator** -> **Idempotency Manager**: Checks request uniqueness [Lettuce].
- **Idempotency Manager** -> **Amazon ElastiCache**: Stores idempotency keys [Redis protocol].
- **Order Data Access Component** -> **Amazon Aurora PostgreSQL**: Persists transactional data [Spring Data JPA / TCP].
- **Event Publisher** -> **Amazon SQS/SNS**: Publishes fulfillment events [AWS SDK for Java].
- **Order Notification Trigger** -> **Notification Service**: Dispatches customer communications [gRPC / HTTPS].

## Technology Stack
- **Java / Spring Boot**: Core container framework for robust enterprise transaction management.
- **Amazon ECS on AWS Fargate**: Scalable serverless container hosting supporting 99.95% uptime requirements.
- **Amazon Aurora PostgreSQL**: Multi-region relational database ensuring ACID compliance for financial transactions.
- **Amazon ElastiCache (Redis)**: In-memory store for sub-millisecond idempotency checks and deduplication.
- **Amazon SQS/SNS**: Asynchronous messaging backbone for decoupled event-driven workflows.
- **Resilience4j**: Circuit breaker implementation for fault-tolerant external API calls.

## Rationale
- This architecture uses a modular, domain-isolated microservice design on AWS to easily scale past 1 million MAU while enforcing strict PCI-DSS and GDPR security controls.
- Distributed sagas, Redis-backed idempotency, and multi-region database replication guarantee zero double-charging and high fault tolerance.