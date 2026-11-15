## Overview
The Checkout & Order Service is a core e-commerce component responsible for processing secure payments, managing order workflows, and fulfilling regulatory compliance. It ensures reliable, multi-currency transactions while isolating sensitive financial data.

## Key Elements
- **Checkout Orchestrator**: Express router handling multi-step workflows, currency conversion, idempotency, and Zod input validation.
- **Payment Gateway Client**: Encapsulates external payment processing via TLS-HTTPS with circuit breakers.
- **Shipping Integrator**: Manages third-party shipping API calls using resilience patterns.
- **Order Repository**: Handles transactional persistence via Prisma/PgBouncer with Amazon Aurora PostgreSQL.
- **Order/Compliance Event Publisher**: Emits asynchronous domain and PII-masking events to Amazon SQS.

## Relationships
- **API Gateway -> Checkout Orchestrator**: Routes authenticated checkout requests via mTLS and AWS IAM using OAuth2/JWT.
- **Checkout Orchestrator -> Amazon Aurora PostgreSQL**: Stores orders, idempotency keys, and column-level encrypted PII.
- **Order Event Publisher -> Amazon SQS**: Sends asynchronous order-placed and compliance events with Dead Letter Queue backups.
- **Payment Gateway Client -> Third-Party Payment Gateway**: Processes tokenized card transactions over TLS-secured HTTPS.
- **Shipping Integrator -> Shipping Provider**: Manages fulfillment operations via TLS-secured HTTPS.

## Technology Stack
- **Runtime**: Node.js with Express framework on AWS ECS Fargate for scalable execution.
- **Persistence**: Amazon Aurora PostgreSQL with Prisma ORM and PgBouncer connection pooling.
- **Messaging**: Amazon SQS with Dead Letter Queues for asynchronous event decoupling.
- **Security & Resilience**: AWS Secrets Manager for credentials, Opossum/circuit breakers for external calls, and Zod for schema validation.

## Rationale
This architecture guarantees 99.95% availability and high scalability for 1M MAU by decoupling downstream workflows with Amazon SQS and enforcing strict circuit breakers. Furthermore, it achieves PCI-DSS scope reduction and GDPR/CCPA compliance via tokenized client-side payment flows and asynchronous PII anonymization.