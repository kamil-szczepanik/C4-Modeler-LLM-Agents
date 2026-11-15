## Overview
The Library Management System provides a comprehensive solution for cataloguing, circulation, and self-service portals. It ensures high performance and strict EU-only data residency compliance.

## Key Elements
- RabbitMQ: Message broker container
- Notification Queue & Audit & Analytics Queue: Quorum queues for reliable storage
- Exchange (Direct/Topic) & Audit Topic Exchange: Erlang-based message routers
- Dead-Letter Exchange (DLX): Failed delivery capture component
- Core Circulation Service, Integration Service, Notification Worker, Reporting Service: Interacting microservices

## Relationships
- Core Circulation Service -> RabbitMQ: Publishes domain events [AMQP 0-9-1 over TLS 1.3]
- Integration Service -> RabbitMQ: Publishes integration events [AMQP 0-9-1 over TLS 1.3]
- Notification Worker -> RabbitMQ: Consumes background tasks [AMQP over TLS 1.3]

## Technology Stack
- RabbitMQ: Message broker handling asynchronous messaging and task processing
- Erlang: Core runtime for RabbitMQ exchanges
- Quorum Queues: Durable queue implementation for guaranteed message persistence in EU-bound volumes
- TLS 1.3 / mTLS: Protocol securing all broker communication channels
- LUKS: Volume-level encryption securing persistent storage at rest

## Rationale
This architecture guarantees zero data loss for critical notifications using durable quorum queues while maintaining strict EU data residency. Security is enforced via least-privilege vhost scoping, mTLS, and volume encryption.