## Overview
- Library Management System for public and academic libraries to catalogue items and manage circulation.
- Provides asynchronous message processing via a secure, EU-resident message broker to ensure scalable, non-blocking user journeys.

## Key Elements
- **Message Broker Container**: RabbitMQ 3-node quorum queue cluster deployed on Kubernetes StatefulSets.
- **Exchange Router**: Routes incoming messages using AMQP.
- **Queue Manager**: Manages durable queues, Dead Letter Queues (DLQ), and persistent storage.
- **Telemetry Exporter**: Strips PII and pushes metrics/logs via OpenTelemetry.
- **Management API / Exporter**: Exposes queue metadata to the Librarian Workbench.
- **External/Connected Entities**: Catalog API & Search Service, Asynchronous Processing Worker, Librarian Workbench, Central Logging & Monitoring SIEM, EU Cloud Region Provider.

## Relationships
- Catalog API & Search Service -> Exchange Router: Publishes asynchronous events [AMQP/TLS with mTLS and SCRAM-SHA-512].
- Exchange Router -> Queue Manager: Routes messages to durable queues [AMQP over TLS].
- Queue Manager -> Asynchronous Processing Worker: Dispatches tasks [AMQP/TLS].
- Librarian Workbench -> Management API / Exporter: Inspects queue status and triggers DLQ replays [HTTPS/mTLS with OAuth2/JWT RBAC].
- Telemetry Exporter -> Central Logging & Monitoring SIEM: Pushes metrics and structured logs [OpenTelemetry over HTTPS with PII sanitization].

## Technology Stack
- **RabbitMQ**: Selected for AMQP 0-9-1 support, robust routing, durable queues, and Dead Letter Exchanges.
- **Kubernetes StatefulSets**: Ensures reliable stateful deployment of the message broker.
- **AES-256 Storage Classes**: Secures persistent volumes on EU-region-pinned storage for data residency compliance.
- **SCRAM-SHA-512 & mTLS**: Enforces strong authentication and encrypted transport across all broker connections.
- **OpenTelemetry**: Standardizes metrics and log export with PII masking.

## Rationale
- RabbitMQ clustering and memory-based backpressure safeguard the 99th-percentile search response SLA (<800ms) by preventing cascading worker failures.
- Strict EU-region data pinning, JWE message-level encryption, and mTLS guarantee compliance with EU-only data residency and GDPR privacy mandates.