## Overview
The Order & Checkout Service is a modular NestJS microservice responsible for orchestrating secure purchases, order state management, and external payment/shipping integrations. It ensures reliable, transactional e-commerce operations while maintaining high availability across AWS cloud regions.

## Key Elements
- **CheckoutController & CheckoutFacade**: Entry point handling API requests, workflow orchestration, and request idempotency.
- **IdempotencyGuard**: Interceptor leveraging Redis to prevent double-charging on retries.
- **OrderManager**: Manages the order state machine and transactional database persistence.
- **PaymentClient**: Integrates securely with external payment gateways using circuit breakers.
- **FulfillmentClient**: Coordinates third-party shipping provider APIs and regional tax calculations.
- **EventPublisher**: Publishes asynchronous domain events for downstream processing.

## Relationships
- **CheckoutController** -> **OrderManager**: In-process TypeScript method calls
- **OrderManager** -> **PaymentClient & FulfillmentClient**: In-process coordination
- **EventPublisher** -> **AWS EventBridge**: Publishes `OrderPlaced` events [AWS SDK / HTTPS]
- **OrderManager** -> **Amazon RDS (PostgreSQL)**: Persists transactional state [PostgreSQL Protocol]
- **PaymentClient** -> **Payment Gateway**: Processes secure charges [HTTPS / REST]
- **FulfillmentClient** -> **Shipping Provider & Tax API**: Coordinates shipping and tax [HTTPS / REST]
- **IdempotencyGuard** -> **Amazon ElastiCache (Redis)**: Caches request keys for deduplication [Redis Protocol]

## Technology Stack
- **Node.js & NestJS**: Modular framework providing dependency injection and robust TypeScript architecture.
- **Amazon ECS/Fargate**: Serverless container orchestration for scalable microservice deployment.
- **Amazon RDS (PostgreSQL)**: Relational database utilizing SERIALIZABLE isolation for ACID order consistency.
- **Amazon ElastiCache (Redis)**: In-memory data store for high-performance idempotency locking.
- **AWS EventBridge & SQS**: Event bus for reliable, asynchronous message delivery.

## Rationale
This component architecture uses strict ACID transactions and a transactional outbox pattern to guarantee financial and inventory accuracy. The decoupled NestJS modules and Redis-backed idempotency ensure low latency, fault tolerance, and compliance with high availability requirements.