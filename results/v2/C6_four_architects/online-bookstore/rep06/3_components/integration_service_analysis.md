## Overview
The Online Bookstore is a scaled-down, Amazon-style e-commerce platform designed for browsing, purchasing, and reviewing physical and electronic books. The Integration Service securely orchestrates all external communications with third-party partners while ensuring high availability and compliance.

## Key Elements
- Payment Orchestrator Component
- Shipping Adaptor Component
- Currency Sync Worker Component
- Integration Message Consumer Component
- Notification Dispatcher Component
- Integration State Store Client Component
- Payment Gateway (External)
- Third-Party Shipping API (External)
- Currency Exchange Rate API (External)
- Notification Service Container
- Amazon Aurora PostgreSQL
- Amazon ElastiCache (Redis)
- Amazon SQS

## Relationships
- Integration Message Consumer -> Integration State Store Client: Persists outbox state [SQL/TCP]
- Integration Message Consumer -> Payment Orchestrator / Shipping Adaptor / Notification Dispatcher: Internal dispatch [In-Memory Function Call]
- Payment Orchestrator -> Payment Gateway: Processes secure payments [HTTPS/REST]
- Shipping Adaptor -> Third-Party Shipping API: Coordinates fulfillment [HTTPS/REST]
- Notification Dispatcher -> Notification Service: Sends alerts [HTTPS/REST]
- Currency Sync Worker -> Currency Exchange Rate API: Fetches rates [HTTPS/REST]
- Currency Sync Worker -> Amazon ElastiCache (Redis): Updates exchange rates [Redis Protocol]

## Technology Stack
- Node.js with TypeScript: Lightweight runtime ideal for I/O-bound operations on Amazon ECS Fargate.
- `axios`: HTTP client for communicating with external REST APIs.
- `opossum`: Circuit breaker library to prevent cascading failures.
- `pg`: Database client for PostgreSQL outbox tracking.
- `ioredis`: Redis client for caching currency exchange rates.
- Amazon Aurora PostgreSQL: Relational database for transactional outbox pattern and auditability.
- Amazon SQS: Message queue for asynchronous task distribution.

## Rationale
This architecture isolates brittle third-party integrations using the Transactional Outbox pattern, circuit breakers, and rate limiting to guarantee fault tolerance. These decisions collectively protect system reliability to meet the 99.95% uptime requirement.