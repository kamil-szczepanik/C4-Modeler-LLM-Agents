## Overview
- Secure, scalable Order & Checkout Container managing shopping carts, multi-currency payments, and fulfillment workflows for an online bookstore.
- Decouples transactional processing from third-party services using asynchronous messaging to ensure high availability and conversion protection.

## Key Elements
- **Book Buyer**: Primary persona executing purchases, guest checkouts, and multi-currency transactions.
- **Cart & Checkout Orchestrator**: Node.js/Express component managing state transitions, BOLA authorization, and the Outbox Pattern.
- **Payment Processor Client**: Handles secure, PCI-DSS compliant ephemeral card tokenization and interacts with the Payment Gateway.
- **Fulfillment & Tax Broker**: Handles asynchronous dispatch of shipping and tax events.
- **Guest Session Manager**: Manages transient guest tokens and ephemeral session state.
- **Payment Error Normalizer**: Maps raw gateway exceptions to localized error codes.
- **Order Database**: PostgreSQL instance storing orders and encrypted PII.
- **Session Cache**: Amazon ElastiCache (Redis) managing high-availability guest sessions.
- **External Systems**: Payment Gateway, Third-Party Shipping API, Tax Calculation Service.

## Relationships
- **API Gateway -> Order & Checkout Container**: Routes transactions via gRPC over mTLS using AWS App Mesh.
- **Cart & Checkout Orchestrator -> Order Database**: Persists relational data via TCP/SQL.
- **Cart & Checkout Orchestrator -> AWS SQS**: Dispatches asynchronous fulfillment events via AWS SDK / HTTPS.
- **Payment Processor Client -> Payment Gateway**: Processes card data via HTTPS with TLS 1.3.
- **Cart & Checkout Orchestrator -> Amazon ElastiCache (Redis)**: Manages guest sessions via TCP/RESP.

## Technology Stack
- **Node.js / Express / TypeScript**: Chosen for rapid asynchronous I/O and strong typing in financial workflows.
- **PostgreSQL**: Selected for robust ACID compliance and transactional safety using the Outbox Pattern.
- **Amazon ElastiCache (Redis)**: Implemented for high-availability transient guest session management.
- **AWS ECS (Fargate) & App Mesh**: Used for container orchestration, mTLS ingress, and payment circuit breaking.
- **AWS SQS**: Enables asynchronous decoupling of shipping and tax calculations from the core checkout flow.

## Rationale
- Decoupling third-party APIs with Amazon SQS prevents external latency from violating the 99.95% uptime SLA and harming conversion.
- Strict PCI-DSS scope minimization, Redis session controls, and AWS Secrets Manager ensure compliance, data protection, and resilience against card-testing attacks.