## Overview
The Order & Checkout Service is a Node.js-based microservice responsible for orchestrating secure e-commerce transactions, payments, and fulfillment. It ensures reliable distributed workflows, strict idempotency, and seamless integration with third-party financial and shipping APIs.

## Key Elements
- **Checkout Controller (Node.js/Express):** Exposes REST/gRPC endpoints for API Gateway interaction.
- **Idempotency Guard (Node.js/Redis Client):** Prevents duplicate order creation via atomic locks.
- **Cart Manager (Node.js):** Encapsulates shopping cart state and lifecycle management.
- **Order Orchestrator (Node.js/Temporal.io SDK):** Manages distributed checkout sagas and consistency.
- **Payment & Tax Client (Node.js/Axios):** Integrates with Stripe/PayPal and Avalara.
- **Fulfillment & Risk Client (Node.js/Axios):** Interfaces with UPS/FedEx and AWS Fraud Detector.
- **Event Publisher (Node.js/AWS SDK):** Dispatches asynchronous domain events.
- **Order Data Access Layer (Node.js/DynamoDB Document Client):** Manages single-table design access patterns.

## Relationships
- **Checkout Controller** -> **Idempotency Guard**: Validates request uniqueness [In-memory]
- **Idempotency Guard** -> **Amazon ElastiCache (Redis)**: Checks/stores transaction locks [TCP]
- **Checkout Controller** -> **Cart Manager**: Retrieves active cart items [In-memory]
- **Checkout Controller** -> **Order Orchestrator**: Initiates saga workflow [In-memory]
- **Order Orchestrator** -> **Payment & Tax Client & Fulfillment & Risk Client**: Executes transaction steps [HTTPS Egress]
- **Order Orchestrator** -> **Order Data Access Layer**: Persists state transitions [NoSQL API over TCP]
- **Cart Manager** -> **Order Data Access Layer**: Clears cart state [NoSQL API over TCP]
- **Order Orchestrator** -> **Event Publisher**: Emits completion events [Event-driven Messaging]

## Technology Stack
- **Node.js with TypeScript:** Selected for rapid asynchronous I/O handling and developer velocity.
- **Temporal.io:** Used for robust code-based workflow orchestration and saga compensation handling.
- **Amazon ElastiCache (Redis):** Provides sub-millisecond atomic operations (`SETNX`) for strict idempotency enforcement.
- **Amazon DynamoDB:** Utilizes single-table design for scalable, low-latency persistence of carts and orders.
- **Axios & AWS SDK:** Standardized clients for secure external API integration and event publishing.

## Rationale
This component architecture separates cross-cutting concerns—such as idempotency, state persistence, and third-party orchestration—into discrete, testable units. Using Temporal.io and Redis guarantees transactional integrity and resilience when invoking external financial and shipping APIs.