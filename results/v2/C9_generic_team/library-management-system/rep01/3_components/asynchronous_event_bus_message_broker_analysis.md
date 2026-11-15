## Overview
The Library Management System is a public and academic platform for cataloging items and managing circulation, enforcing EU-only data residency and sub-800ms search responses.

## Key Elements
- Core Domain Services
- Dedicated Search Tier
- Asynchronous Event Bus (Message Broker)
- Observability & Logging Container

## Relationships
- Core Domain Services -> Asynchronous Event Bus (Message Broker): publishes updates [AMQP/Kafka]
- Asynchronous Event Bus (Message Broker) -> Dedicated Search Tier: consumes events [Message Broker Protocol]
- Core Domain Services -> Asynchronous Event Bus (Message Broker): utilizes transactional outbox pattern [HTTP/gRPC]

## Technology Stack
- AMQP / Kafka: Ensures decoupled, EU-compliant event-driven synchronization and high throughput.
- Avro / JSON Schema: Standardized schema registry for message payload compatibility.
- W3C Trace Context headers: Enables distributed tracing across asynchronous message boundaries.
- TLS mutual authentication (mTLS): Enforces topic-level authorization and secure transport.
- Pact: Automated consumer-driven contract testing in CI/CD.

## Rationale
An event-driven architecture using AMQP/Kafka decouples services to achieve <800ms search performance while enforcing strict EU data residency via regional routing. Robust reliability patterns, including DLQs, idempotency, and the outbox pattern, ensure fault-tolerant catalog and circulation management.