## Overview
The Checkout & Order container manages secure e-commerce transactions, multi-currency pricing, and regulatory compliance for the Online Bookstore. It processes high-volume purchases while ensuring PCI-DSS, GDPR, and CCPA adherence across multi-region AWS infrastructure.

## Key Elements
- **Cart & Pricing Engine (Node.js/Express):** Manages real-time cart state and multi-currency conversions (USD, EUR, GBP).
- **Order Orchestrator (Node.js/Express):** Coordinates distributed transactions, saga patterns, and asynchronous fulfillment queues.
- **Payment & Compliance Manager (Node.js/Express):** Handles payment tokenization and automated GDPR/CCPA data masking routines.
- **Amazon Aurora PostgreSQL:** Persists transactional ledgers, localized tax data, and order states with column-level PII encryption.
- **AWS SQS (Fulfillment Queue):** Decouples order confirmation from Third-Party Shipping API availability.
- **Payment Gateway:** External third-party system processing secure financial transactions.
- **Tax Calculation Service:** Internal microservice providing regional tax rules via gRPC.

## Relationships
- **AWS API Gateway -> Cart & Pricing Engine:** Routes cart actions via REST/JSON over HTTPS with JWT validation.
- **Order Orchestrator -> Payment Gateway:** Authorizes payments via HTTPS/TLS 1.3 using client-side tokenization.
- **Order Orchestrator -> Tax Calculation Service:** Queries regional tax rules via gRPC over mTLS (AWS App Mesh).
- **Order Orchestrator -> Amazon Aurora PostgreSQL:** Persists transactional data via SQL over TLS.
- **Order Orchestrator -> AWS SQS:** Queues fulfillment details asynchronously using AWS SDK with IAM Auth.
- **Order Orchestrator & Payment & Compliance Manager:** Enforce cryptographically secure idempotency keys for transaction replays.

## Technology Stack
- **Node.js / Express:** Core runtime for microservice components, chosen for high concurrency and I/O performance.
- **Amazon Aurora PostgreSQL:** Relational database selected for ACID compliance, transactional ledger persistence, and AWS KMS integration.
- **AWS SQS:** Message broker used for asynchronous decoupling of third-party shipping dependencies.
- **AWS KMS:** Encryption service providing customer-managed keys (CMK) and server-side encryption for databases and SQS queues.
- **AWS App Mesh & mTLS:** Secures internal microservice communication and gRPC transport layers.

## Rationale
Decomposing the Checkout & Order container into specialized microservices isolates PCI-DSS and GDPR compliance scopes while ensuring zero-downtime scalability. Asynchronous queuing via AWS SQS guarantees high availability and robust fault tolerance against third-party shipping API outages.