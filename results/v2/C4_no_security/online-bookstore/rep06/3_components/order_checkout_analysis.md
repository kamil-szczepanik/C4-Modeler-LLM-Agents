## Overview
The Order & Checkout container manages transactional integrity, multi-currency cart finalization, and fulfillment workflows for the Online Bookstore. It ensures secure processing, strict idempotency, and high availability across distributed AWS regions.

## Key Elements
- **Users**: Customers, Customer Support Representatives
- **Containers**: Order & Checkout (Spring Boot), API Gateway, Localization & Tax, Payment Gateway, Third-Party Shipping Provider
- **Internal Components**: Checkout Orchestrator, Order Management, Payment Integration, Event Publisher, Order Modification, Idempotency Manager
- **Data & Infrastructure**: Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis), Amazon SQS/SNS, AWS Secrets Manager, AWS X-Ray

## Relationships
- API Gateway -> Order & Checkout: Routes internal traffic via VPC links [gRPC]
- Checkout Orchestrator -> Localization & Tax: Calculates local taxes and totals [gRPC]
- Checkout Orchestrator -> Payment Integration: Processes secure transactions [Internal REST/gRPC]
- Checkout Orchestrator -> Idempotency Manager: Tracks transaction states and request keys [Redis Protocol]
- Payment Integration -> Payment Gateway: Executes payment processing [HTTPS]
- Order & Checkout -> Third-Party Shipping Provider: Handles logistics and fulfillment [HTTPS]
- Event Publisher -> Amazon SQS/SNS: Emits domain events (`OrderPlaced`) [AWS SDK]

## Technology Stack
- **Backend Framework**: Spring Boot (Java) for enterprise microservice structure
- **Orchestration**: Spring State Machine for managing complex saga workflows
- **Persistence**: Amazon Aurora PostgreSQL via Spring Data JPA for ACID-compliant order state
- **Caching & Idempotency**: Amazon ElastiCache (Redis) with Multi-AZ and AOF persistence
- **Resilience**: Resilience4j for circuit breakers and retry logic
- **Security & Ops**: AWS Secrets Manager, AWS X-Ray for distributed tracing

## Rationale
This architecture uses a saga pattern with an ElastiCache Redis-backed idempotency store to guarantee transaction safety and prevent double-charging during network failures. Aurora PostgreSQL and multi-AZ deployments ensure 99.95% uptime and strict compliance for global retail operations.