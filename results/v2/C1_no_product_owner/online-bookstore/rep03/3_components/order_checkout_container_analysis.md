## Overview
The Order & Checkout Container is a Node.js/Express service responsible for managing shopping carts, transaction orchestration, order persistence, and fulfillment integration. It ensures secure, resilient, and multi-currency compliant checkout workflows for the online bookstore.

## Key Elements
- Cart Management Component (Node.js, Express, Amazon DynamoDB)
- Checkout Orchestrator Component (Node.js, Express) with Idempotency Service (Amazon DynamoDB)
- Order Processing Component (Node.js, Express, Amazon Aurora PostgreSQL)
- Shipping Integrator Component (Node.js, Express)
- External Systems: Payment Gateway, Tax & Compliance Service, Shipping Provider APIs
- Infrastructure: AWS Secrets Manager, Amazon EventBridge, AWS KMS, AWS X-Ray, Amazon CloudWatch

## Relationships
- Cart Management & Checkout Orchestrator -> Client: Validates JWT tokens and enforces Object-Level Authorization [HTTPS/REST]
- Checkout Orchestrator -> Payment Gateway & Tax & Compliance Service: Coordinates transactions via client-side tokenization and REST/JSON [HTTPS, Circuit Breakers]
- Checkout Orchestrator -> Order Processing: Initiates order creation [Internal Function Call / TypeScript Interface]
- Order Processing -> Amazon EventBridge: Publishes `OrderPlaced` events [AWS SDK]
- Shipping Integrator -> Shipping Provider APIs: Fetches rates and generates labels [REST/JSON]

## Technology Stack
- Node.js & Express: Lightweight runtime for scalable microservice components.
- Amazon DynamoDB: Single-table design for low-latency session carts and idempotency keys.
- Amazon Aurora PostgreSQL: ACID-compliant transactional persistence for financial order records with cross-region replication.
- AWS Secrets Manager: Secure runtime injection and automatic rotation for external API keys.
- Zod/Joi: Strict schema validation to prevent injection attacks.
- AWS X-Ray & CloudWatch: Distributed tracing and immutable audit logging for 99.95% uptime SLA (R-07).

## Rationale
This component architecture isolates high-risk financial logic while leveraging client-side tokenization to reduce PCI-DSS scope. DynamoDB-backed idempotency and circuit breakers guarantee financial safety and resilience against third-party outages.