## Overview
- Node.js microservice managing secure e-commerce transactions, payments, and fulfillment for the Online Bookstore.
- Designed for high availability, multi-currency support, and strict regulatory compliance across global regions.

## Key Elements
- **Cart Controller & Manager**: Node.js/Express component handling cart lifecycle and Redis persistence.
- **Checkout Orchestrator**: Manages transactions, idempotency, data masking, and orchestration.
- **Payment & Fulfillment Client**: Integrates with Stripe, PayPal, FedEx, and UPS using circuit breakers.
- **Order Event Publisher & Notification Adapter**: Emits domain events and notification triggers.
- **Data Stores & Infrastructure**: Amazon RDS PostgreSQL, Amazon ElastiCache (Redis), AWS EventBridge, PgBouncer.

## Relationships
- Checkout Orchestrator -> Cart Controller: Manages cart lifecycle [In-memory function call]
- Checkout Orchestrator -> Payment & Fulfillment Client: Executes transactions [Async/Await REST via HTTPS]
- Order & Checkout Service -> Stripe/PayPal: Processes payments [HTTPS / REST with TLS 1.3]
- Order & Checkout Service -> FedEx/UPS: Calculates shipping [HTTPS / REST with TLS 1.3]
- Order & Checkout Service -> Amazon RDS PostgreSQL: Persists transactional state [Encrypted TCP with gRPC/TLS 1.3 and PgBouncer]
- Order & Checkout Service -> Amazon ElastiCache (Redis): Caches cart data [Encrypted TCP]
- Order Event Publisher -> AWS EventBridge: Publishes domain events [JSON over AWS SDK / HTTPS]

## Technology Stack
- **Node.js**: Chosen for lightweight asynchronous request handling in the checkout pipeline.
- **Amazon RDS PostgreSQL & Redis**: Selected for ACID compliance in orders and low-latency cart persistence.
- **AWS EventBridge**: Enables asynchronous, decoupled event-driven workflows and notifications.
- **PgBouncer**: Manages database connection pooling to handle traffic surges up to 1M MAU.
- **gRPC over TLS 1.3**: Optimizes internal synchronous communication latency.

## Rationale
- This architecture isolates critical payment and third-party dependencies using circuit breakers and idempotency to meet 99.95% availability targets.
- Strict data masking, least-privilege IAM, and TLS 1.3 encryption satisfy GDPR, CCPA, and OWASP Top-10 security requirements.