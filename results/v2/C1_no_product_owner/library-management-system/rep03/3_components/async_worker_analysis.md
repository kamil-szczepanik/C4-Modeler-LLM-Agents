## Overview
The Async Worker is a Python-based background processing container designed to handle event-driven workloads, payments, and notifications for the Library Management System. It ensures reliable asynchronous execution while adhering to EU-only data residency and strict security policies.

## Key Elements
- Task Router (Celery App, Python)
- Task Validation Interceptor (Celery Pipeline)
- Payment Processor Task (Python)
- Notification Dispatcher Task (Python)
- Message Broker (RabbitMQ with DLQs)
- Connection Pooler (PgBouncer)
- Database (PostgreSQL)
- External Services (Payment Gateway, Notification Service)
- Secure Vault (HashiCorp Vault)

## Relationships
- Task Router -> Message Broker: Consumes background jobs [AMQPS with mTLS]
- Task Router -> Task Validation Interceptor: Passes raw messages [In-memory]
- Payment Processor Task -> Secure Vault: Fetches API credentials [HTTPS (REST)]
- Payment Processor Task -> Payment Gateway: Executes transactions [HTTPS (TLS 1.3)]
- Notification Dispatcher Task -> Notification Service: Dispatches alerts [gRPC with TLS 1.3]
- Payment & Notification Tasks -> PgBouncer -> Database: Persists state/idempotency keys [TCP via TLS]

## Technology Stack
- Python / Celery: Core worker framework chosen for async task management.
- RabbitMQ: Message broker with DLQs for fault-tolerant task routing and metric-based autoscaling.
- SQLAlchemy / AsyncPG: Database driver providing asynchronous SQL access.
- PgBouncer: Connection pooler to manage database connection limits.
- HashiCorp Vault: Secret management for dynamic credentials and AppRole authentication.
- OpenTelemetry: Distributed tracing propagated via message headers.

## Rationale
This architecture ensures high availability, secure decoupled processing, and robust idempotency for critical background tasks like payments. It strictly enforces EU data residency and least-privilege security controls across all internal and external touchpoints.