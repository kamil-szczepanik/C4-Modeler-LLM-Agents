## Overview
The Order & Checkout Service provides ACID-compliant transaction processing for carts, secure checkout, and fulfillment within the global AWS-hosted Online Bookstore. It handles multi-currency transactions, ensures strict regional data isolation, and maintains compliance with GDPR and CCPA regulations.

## Key Elements
- Cart Management Component: Manages ephemeral and persistent user cart states.
- Checkout Orchestrator Component: Enforces ACID transactions and coordinates payment/shipping.
- Order Fulfillment Component: Handles asynchronous downstream event dispatch.
- AWS Aurora PostgreSQL Multi-Region: Provides durable relational storage for orders.
- AWS ElastiCache for Redis: Caches transient cart sessions and multi-currency rates.
- AWS SQS/SNS: Delivers asynchronous event messaging and dead-letter queues.

## Relationships
- API Gateway / Backend-for-Frontend (BFF) -> Checkout Orchestrator Component: Routes gRPC requests with mTLS over AWS Cloud Map
- Checkout Orchestrator Component -> Payment Gateway: Transacts securely via HTTPS/REST using tokenized iframe SDKs
- Checkout Orchestrator Component -> AWS Aurora PostgreSQL Multi-Region: Executes transactional reads and writes over JDBC/SQL
- Cart Management Component -> AWS ElastiCache for Redis: Accesses cached cart state via RESP protocol
- Checkout Orchestrator Component -> Order Fulfillment Component: Publishes domain events asynchronously via AWS SQS/SNS

## Technology Stack
- Spring Boot / Go: Selected for high-performance, strongly typed microservice implementation.
- AWS Aurora PostgreSQL Multi-Region: Ensures robust ACID compliance and active-active regional data replication.
- AWS ElastiCache for Redis: Delivers low-latency in-memory session and cart caching.
- AWS SQS/SNS: Provides reliable asynchronous decoupling and fault-tolerant message delivery.

## Rationale
This architecture uses active-active regional deployment and strict ACID boundaries to guarantee 99.95% uptime and reliable 1M MAU scaling. Tokenized payment integration and granular IAM policies eliminate cardholder data exposure while ensuring multi-currency, secure e-commerce operations.