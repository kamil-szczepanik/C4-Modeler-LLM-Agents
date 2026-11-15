## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The Async Event Broker container ensures reliable asynchronous event processing and decoupling while enforcing strict EU-only data residency.

## Key Elements
- **Event Router / Exchange**: Apache Kafka Topics with replication factor 3 for routing events.
- **Message Queue / Log Storage**: Apache Kafka clustered brokers for persistent event streams.
- **Dead Letter Queue (DLQ) Handler**: Dedicated Kafka DLQ topic with retention policies.
- **Schema Registry**: Confluent Schema Registry for backward/forward compatibility contracts.
- **Core Domain Service**: Java / Spring Boot service producing events.
- **Search Service**: Elasticsearch consumer for search indices (R-05 performance).
- **Background Worker**: Python/Celery or Node.js background task consumer.

## Relationships
- Core Domain Service -> Schema Registry: Validates event payload structure [HTTP/2 + mTLS]
- Core Domain Service -> Event Router: Publishes domain events [Kafka Producer API / TCP + TLS 1.3]
- Event Router -> Schema Registry: Verifies message schema compliance on ingestion [Internal Protocol]
- Event Router -> Message Queue: Appends messages to distributed commit logs [Internal Broker Protocol]
- Message Queue -> Search Service: Consumes events to update search indices [Kafka Consumer API over mTLS]
- Message Queue -> Background Worker: Consumes asynchronous background tasks [Kafka Consumer API over mTLS]

## Technology Stack
- **Apache Kafka**: Clustered brokers and topic partitions for high-throughput, durable messaging.
- **Confluent Schema Registry**: Enforces strict event schema compatibility and prevents breaking changes.
- **TLS 1.3 / mTLS**: Encrypts all data in transit and enforces strict client authentication.
- **AES-256**: Encrypts data-at-rest on all persistent volume claims (PVCs) for EU compliance.
- **Prometheus & OpenTelemetry**: Provides metrics exportation and distributed tracing.

## Rationale
This architecture guarantees strict EU data residency using region-pinned PVCs and complies with performance targets through asynchronous decoupling. Security and data integrity are maintained via mTLS, RBAC ACLs, payload encryption, and automated schema validation.