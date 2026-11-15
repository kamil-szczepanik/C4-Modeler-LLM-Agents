## Overview
The Checkout & Cart Service is a secure, highly scalable microservice that manages shopping cart operations, multi-currency pricing, and transactional checkout processing for the Online Bookstore. It ensures reliable, PCI-compliant payment orchestration while supporting the platform's global availability and high-throughput requirements.

## Key Elements
- Cart Management Component (Node.js / Express)
- Checkout Orchestrator Component (Node.js / TypeScript)
- Payment Integration Component (Node.js / TypeScript)
- Order Fulfillment Component (Node.js / TypeScript)
- Currency & Pricing Sub-module
- Amazon ECS / Fargate
- Amazon ElastiCache (Redis)
- Amazon RDS (PostgreSQL)
- Amazon SQS / SNS
- AWS Secrets Manager & AWS WAF

## Relationships
- API Gateway -> Checkout & Cart Service: Routes cart and checkout requests [HTTPS / REST over TLS 1.3]
- Cart Management Component -> Amazon ElastiCache (Redis): Retrieves and persists cart state [Redis Protocol]
- Payment Integration Component -> Payment Gateway: Processes secure payments [HTTPS / REST via Outbox Pattern]
- Order Fulfillment Component -> Shipping Provider APIs & Identity Service: Dispatches orders and events [Amazon SQS / SNS]
- Checkout & Cart Service -> Amazon RDS (PostgreSQL): Reads and writes transactional data and outbox events [PostgreSQL Protocol]

## Technology Stack
- Node.js / TypeScript: Standardized runtime for all internal components, ensuring type safety and shared domain logic.
- Amazon ECS / Fargate: Container orchestration providing elastic scalability without server management.
- Amazon ElastiCache (Redis): Low-latency in-memory data store for ephemeral cart management and session persistence.
- Amazon RDS (PostgreSQL): Relational database utilizing the Outbox Pattern for reliable transactional processing.
- AWS Secrets Manager: Secure credential storage enforcing automated 30-day rotation for API keys.
- AWS App Mesh / WAF: Enforces internal mTLS traffic boundaries and protects endpoints against card-testing attacks.

## Rationale
This architecture guarantees 99.95% availability and high scalability to handle 1 million MAU through decoupled, elastic container components deployed on AWS. The Outbox Pattern and strict single-region write model protect financial data integrity while meeting rigorous GDPR, CCPA, and PCI-DSS compliance standards.