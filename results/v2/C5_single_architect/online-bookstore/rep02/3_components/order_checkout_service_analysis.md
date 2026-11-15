## Overview
The Order & Checkout Service manages shopping carts, multi-step transaction orchestration, and fulfillment coordination for the Online Bookstore. It ensures ACID compliance for financial records while decoupling asynchronous event publishing.

## Key Elements
- **Cart Component**: Manages temporary shopping cart state.
- **Checkout Orchestrator**: Manages state machines for multi-step checkout processes.
- **Payment Adapter**: Encapsulates external payment gateway communication.
- **Shipping Adapter**: Encapsulates third-party shipping API integration.
- **Order Repository**: Persists finalized orders and transactional ledger data.
- **Event Publisher Component**: Triggers domain events upon successful database commits.

## Relationships
- **Checkout Orchestrator** -> **Payment Adapter**: Processes secure payments [HTTPS / REST]
- **Checkout Orchestrator** -> **Shipping Adapter**: Coordinates shipment and tracking [HTTPS / REST]
- **Cart Component** -> **Amazon ElastiCache**: Reads and writes cart state [Redis Protocol]
- **Checkout Orchestrator** -> **Order Repository**: Persists finalized transactions [Prisma ORM / SQL via TLS]
- **Order Repository** -> **Event Publisher Component**: Triggers domain events post-commit [Internal Function Call]
- **Event Publisher Component** -> **Message Broker**: Publishes `OrderPlaced` events [AWS SDK / HTTPS]

## Technology Stack
- **Node.js / TypeScript**: Core runtime and language for all internal components, ensuring type safety and consistency.
- **Amazon ElastiCache (Redis)**: Low-latency in-memory store for high-performance shopping cart persistence.
- **Amazon Aurora (PostgreSQL)**: Relational database providing ACID guarantees for financial ledger data.
- **Prisma ORM**: Type-safe database toolkit for secure SQL queries.
- **Amazon SQS / SNS**: Managed message broker for reliable asynchronous domain event distribution.

## Rationale
This component architecture guarantees financial data integrity via ACID-compliant PostgreSQL transactions while utilizing Redis for high-performance cart operations. Decoupling event publishing ensures reliable messaging without risking transaction failures.