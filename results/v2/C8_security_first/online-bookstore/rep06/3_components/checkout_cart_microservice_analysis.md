## Overview
The Checkout & Cart Microservice processes secure transactions, shopping carts, and order fulfillment for the Online Bookstore. It ensures multi-currency support, cart persistence, and asynchronous payment processing while meeting strict security and compliance standards.

## Key Elements
- Cart Management Component (Node.js/Express, PostgreSQL)
- Checkout Orchestrator Component (Node.js/Express, PostgreSQL, Transaction Ledger)
- Fulfillment & Payment Publisher Component (Node.js/Express, AWS SDK)
- Amazon SQS & Dead Letter Queues (DLQ)
- External Payment Gateway & Third-Party Shipping APIs

## Relationships
- API Gateway -> Cart Management & Checkout Orchestrator Components [gRPC and HTTPS with mTLS]
- Checkout Orchestrator Component -> PostgreSQL [TLS and SQL with connection pooling via PgBouncer]
- Fulfillment & Payment Publisher Component -> Amazon SQS [AWS SDK and HTTPS with AWS KMS CMK encryption]
- Fulfillment & Payment Publisher Component -> Payment Gateway & Third-Party Shipping APIs [REST/HTTPS via SQS async queues]

## Technology Stack
- Node.js/Express: Lightweight runtime for low-latency cart and checkout request handling.
- AWS ECS Fargate: Serverless container execution with SQS-based autoscaling for 1M MAU scalability.
- Amazon SQS & DLQ: Asynchronous message decoupling and resilience against downstream outages.
- PostgreSQL: Relational database with Multi-AZ deployment and ACID guarantees for order ledgers.
- AWS KMS: Customer-managed keys for secure queue message encryption.

## Rationale
This architecture ensures 99.95% uptime and low latency by decoupling synchronous requests from asynchronous downstream dependencies using Amazon SQS. Strict transactional integrity, idempotency tokens, and PCI-DSS scope reduction protect revenue and customer trust.