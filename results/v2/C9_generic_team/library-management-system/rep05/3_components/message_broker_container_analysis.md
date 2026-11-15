## Overview
The Library Management System is a solution for public and academic libraries to catalogue items and manage circulation. It uses an asynchronous message broker architecture to decouple writes and maintain indexing consistency.

## Key Elements
- Message Broker Container (RabbitMQ / Kafka)
- Core Transactional Service Container
- Search Service Container (Elasticsearch / OpenSearch)
- Schema Registry
- Observability Sidecar
- EU-Hosted Object Storage

## Relationships
- Core Transactional Service Container -> Message Broker Container: Publishes events [AMQP/Kafka protocol]
- Message Broker Container -> Search Service Container: Consumes events for indexing [Asynchronous Message Stream]

## Technology Stack
- RabbitMQ / Kafka: Decouples write operations and ensures search indexing performance under 800 ms
- Avro or JSON Schema: Enforces strict payload contracts via a schema registry
- EU-Hosted Object Storage: Stores large digital item payloads via reference pointers to prevent broker memory bloat

## Rationale
This architecture ensures high performance and strict EU-only data residency compliance. Asynchronous messaging protects search response times while robust broker governance guarantees system reliability.