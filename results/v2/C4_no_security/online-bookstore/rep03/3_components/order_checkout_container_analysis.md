## Overview
The Order & Checkout Container manages shopping sessions, secure multi-currency payments, and transactional workflows for the Online Bookstore. It ensures transactional integrity, high availability, and asynchronous fulfillment to prevent cart abandonment.

## Key Elements
- Cart Management Component (Node.js / Express)
- Checkout Orchestrator Component (Java / Spring Boot)
- Payment & Fulfillment Gateway Client (Java)
- Event Publisher Component (Java / Spring Cloud Stream)
- Audit & Support Query Component (Node.js)
- Amazon DynamoDB and Amazon Aurora PostgreSQL
- Amazon SQS / SNS with Dead Letter Queues (DLQs)

## Relationships
- Edge & Ingress -> Cart Management & Checkout Orchestrator: Forwards client requests [gRPC over TLS]
- Edge & Ingress -> Audit & Support Query Component: Queries order audit trails [gRPC over TLS]
- Checkout Orchestrator -> Payment & Fulfillment Gateway Client: Invokes payment and tax integrations [Internal REST/gRPC]
- Checkout Orchestrator -> Event Publisher: Dispatches domain events [Spring Application Events]
- Event Publisher -> Amazon SQS/SNS: Publishes order events [AWS SDK / HTTPS]

## Technology Stack
- Node.js & Express: Powers low-latency shopping cart sessions and administrative query APIs
- Java & Spring Boot: Coordinates complex, multi-step transactional checkout workflows
- Spring State Machine: Manages transaction states and guarantees idempotency
- Amazon DynamoDB: Persists ephemeral shopping cart sessions with low latency
- Amazon Aurora PostgreSQL: Stores transactional records and audit logs with automated failover
- Resilience4j: Implements circuit breakers and retries for external API calls
- Amazon SQS / SNS: Decouples fulfillment and transactional email tasks asynchronously

## Rationale
Decomposing the container isolates stateful cart management from transactional checkout orchestration, protecting core revenue streams. Asynchronous event publishing via SQS/SNS prevents third-party shipping and email latencies from impacting user-facing checkout performance.