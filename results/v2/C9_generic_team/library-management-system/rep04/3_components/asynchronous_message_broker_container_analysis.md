## Overview
The Library Management System is a public and academic library platform designed to catalogue items, manage circulation, and provide self-service portals. It relies on an asynchronous event-driven architecture to ensure high performance and strict EU-only data residency.

## Key Elements
- Asynchronous Message Broker Container: RabbitMQ / Kafka
- Spring Boot Microservices: Catalog Management, Circulation, User Portals
- Supporting Infrastructure: Schema Registry, Log/Metrics Collector Agent, Disaster Recovery / Backup Target

## Relationships
- Catalog Management -> Asynchronous Message Broker Container: Publishes/consumes events [AMQP/TCP]
- Circulation -> Asynchronous Message Broker Container: Publishes/consumes events [AMQP/TCP]
- User Portals -> Asynchronous Message Broker Container: Publishes/consumes events [AMQP/TCP]
- Asynchronous Message Broker Container -> Log/Metrics Collector Agent: Exports Prometheus-compatible metrics [HTTP/TCP]

## Technology Stack
- RabbitMQ / Kafka: Handles asynchronous event streaming with multi-node clustering for high availability.
- Schema Registry / AsyncAPI: Enforces strict message payload governance to prevent silent integration failures.
- Prometheus: Collects broker metrics including consumer lag, queue depth, and throughput.
- Testcontainers: Validates publisher and consumer contracts locally in the CI/CD pipeline.

## Rationale
This architecture uses an event-driven broker pattern with strict schema governance, idempotency, and dead-letter queues to ensure decoupled, reliable communication. Multi-node clustering and EU-hosted persistence guarantee data residency compliance while maintaining low-latency search and circulation operations.